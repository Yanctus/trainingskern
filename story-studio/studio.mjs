#!/usr/bin/env node
// Story-Studio: macht aus einer Story-Datei ein fertiges Video für Instagram (1080 x 1920, 30 Bilder pro Sekunde, MP4).
//
//   node studio.mjs render stories/ue-001.json            -> out/ue-001.mp4
//   node studio.mjs render stories/ue-001.json --bild 2.5,7  -> nur Standbilder bei 2,5 s und 7 s (zum Prüfen)
//   node studio.mjs vorschau stories/ue-001.json          -> im Browser ansehen und spulen
//   --neu: Übungsdaten und App-Aufnahmen neu holen · --jobs 4: so viele Browser fotografieren gleichzeitig
//
// Braucht: Node 20+, Playwright mit Chromium (npm i playwright), ffmpeg und curl.
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { execFile, execFileSync, spawn } from "node:child_process";
import { promisify } from "node:util";
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const run = promisify(execFile);
const HIER = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(HIER, "out"), CACHE = path.join(OUT, "cache");
const APP = "6afec076c6c4a55a7cb4995e";                       // Trainingskern bei Base44
const KATALOG = `https://app.base44.com/api/apps/${APP}/entities/Einheit?limit=1000`; // öffentliche Leseschnittstelle
const SEITE = "https://trainingskern.de";                      // die veröffentlichte App (für Aufnahmen im Handy)
const HANDY = { width: 390, height: 772 };                     // passt zum Bildschirm des Handys in der Szene "app"

const [befehl, datei, ...rest] = process.argv.slice(2);
const flag = (name) => rest.includes("--" + name);
const wert = (name, sonst) => { const i = rest.indexOf("--" + name); return i >= 0 ? rest[i + 1] : sonst; };
if (!["render", "vorschau"].includes(befehl) || !datei) {
  console.log("Aufruf: node studio.mjs render|vorschau stories/<name>.json [--bild 2.5,7] [--neu] [--jobs 4] [--port 4173]");
  process.exit(1);
}
const storyPfad = path.relative(HIER, path.resolve(datei)).split(path.sep).join("/");
const kennung = path.basename(storyPfad, ".json");
const story = JSON.parse(readFileSync(path.join(HIER, storyPfad), "utf8"));
const fps = story.fps || 30;
mkdirSync(CACHE, { recursive: true });

/* ---------- Übungen aus dem Katalog der App ---------- */
let katalog = null;
async function ladeKatalog() {
  if (katalog) return katalog;
  const ziel = path.join(CACHE, "einheiten.json");
  const frisch = existsSync(ziel) && Date.now() - statSync(ziel).mtimeMs < 6 * 3600e3 && !flag("neu");
  if (!frisch) {
    await run("curl", ["-sS", "--fail", "-m", "90", "-o", ziel + ".neu", KATALOG]);
    JSON.parse(readFileSync(ziel + ".neu", "utf8")); // nur gültige Antworten übernehmen
    writeFileSync(ziel, readFileSync(ziel + ".neu"));
    rmSync(ziel + ".neu");
  }
  katalog = JSON.parse(readFileSync(ziel, "utf8"));
  return katalog;
}

/* ---------- Filme (filme/*.mp4): einmal in Einzelbilder zerlegen, damit jedes Bild genau getroffen wird ---------- */
// filme/filme.json: Angaben je Film, z. B. { "wischer-marker": { "maske": true, "zu": 3.9 } }
const filmInfo = () => { try { return JSON.parse(readFileSync(path.join(HIER, "filme", "filme.json"), "utf8")); } catch { return {}; } };
async function zerlegeFilm(name) {
  if (!/^[a-z0-9-]+$/.test(name)) throw new Error("Filmname: nur Kleinbuchstaben, Ziffern, Bindestrich");
  const quelle = path.join(HIER, "filme", name + ".mp4"), ordner = path.join(CACHE, "film-" + name), angaben = filmInfo()[name] || {};
  if (!existsSync(quelle)) throw new Error("Film fehlt: filme/" + name + ".mp4");
  const st = statSync(quelle), marke = `${st.size}-${Math.round(st.mtimeMs)}-${JSON.stringify(angaben)}`;
  const infoPfad = path.join(ordner, "info.json");
  if (existsSync(infoPfad)) { const alt = JSON.parse(readFileSync(infoPfad, "utf8")); if (alt.marke === marke) return alt; }
  rmSync(ordner, { recursive: true, force: true });
  mkdirSync(ordner, { recursive: true });
  // maske: Wischer in reinem Schwarz und Weiß (wird über das Bild multipliziert) · schwarz: Schwarz wirklich schwarz (für "screen")
  const filter = ["fps=30", "scale=720:1280:force_original_aspect_ratio=increase", "crop=720:1280",
    ...(angaben.maske ? ["format=gray", "lutyuv=y='clip((val-70)*255/110,0,255)'"] : []),
    ...(angaben.schwarz ? ["lutyuv=y='clip((val-28)*255/227,0,255)'"] : []),
    ...(angaben.lime ? ["colorchannelmixer=rr=0.84"] : []),
    ...(angaben.marke ? ["lut3d=file=" + path.join(HIER, "filme", "marke.cube")] : [])].join(","); // marke: Farben der App (Rasen fast schwarz, kein Blau, genaues Neon und Orange) // lime: Gelb etwas grüner
  await run("ffmpeg", ["-y", "-loglevel", "error", "-i", quelle, "-vf", filter, "-q:v", "3", "-start_number", "0", path.join(ordner, "%04d.jpg")]);
  const anzahl = readdirSync(ordner).filter((f) => f.endsWith(".jpg")).length;
  const { stdout } = await run("ffprobe", ["-v", "error", "-show_entries", "stream=codec_type", "-of", "csv=p=0", quelle]);
  const info = { anzahl, fps: 30, dauer: anzahl / 30, ton: stdout.includes("audio"), marke };
  // Intro-Filme enden auf dem K: Wo es im letzten Bild sitzt und ab wann es still steht, wird hier ausgemessen
  // (helle Fläche des Zeichens). So braucht ein neues Intro keine Angaben von Hand.
  if (name.startsWith("intro-")) {
    const mess = await run("ffmpeg", ["-hide_banner", "-i", quelle, "-vf", "fps=30,scale=720:1280,bbox=min_val=175", "-f", "null", "-"]).catch((e) => e);
    const boxen = [...String(mess.stderr || "").matchAll(/pts_time:([\d.]+) x1:(\d+) x2:(\d+) y1:(\d+) y2:(\d+) w:(\d+) h:(\d+)/g)].map((m) => m.slice(1).map(Number));
    const ende = boxen[boxen.length - 1];
    if (ende && ende[5] < 400 && Math.abs(ende[5] - ende[6]) < 30) { // nur wenn am Ende wirklich ein kleines, etwa quadratisches Zeichen steht
      const gleich = (b) => [1, 2, 3, 4].every((i) => Math.abs(b[i] - ende[i]) <= 4);
      let i = boxen.length - 1;
      while (i > 0 && gleich(boxen[i - 1])) i--;
      info.auto = { k: [ende[1], ende[3], ende[5]], bis: Math.min(info.dauer, boxen[i][0] + 0.35) };
    }
  }
  writeFileSync(infoPfad, JSON.stringify(info));
  return info;
}

/* ---------- Sprecher: Sätze der Szenen ("sprecher") mit der eigenen ElevenLabs-Stimme ---------- */
// stimme.json: { "voice_id": "...", "model_id": "...", "voice_settings": {...} }. Der Schlüssel liegt nicht im Repo:
// Er ist in der Cloud-Umgebung für api.elevenlabs.io hinterlegt (oder steht in ELEVENLABS_API_KEY).
// Jede Aufnahme wird in ton/sprecher/ abgelegt und nie doppelt bezahlt.
import { createHash } from "node:crypto";
async function sprich(text) {
  const stimme = JSON.parse(readFileSync(path.join(HIER, "stimme.json"), "utf8"));
  const name = createHash("sha1").update(stimme.voice_id + "|" + (stimme.model_id || "") + "|" + text).digest("hex").slice(0, 16);
  const ordner = path.join(HIER, "ton", "sprecher"), ziel = path.join(ordner, name + ".mp3");
  mkdirSync(ordner, { recursive: true });
  if (!existsSync(ziel)) {
    const body = path.join(CACHE, "sprich.json");
    writeFileSync(body, JSON.stringify({ text, model_id: stimme.model_id || "eleven_multilingual_v2", voice_settings: stimme.voice_settings || { stability: 0.5, similarity_boost: 0.8 } }));
    await run("curl", ["-sS", "--fail-with-body", "-m", "120", "-o", ziel + ".neu", "-H", "xi-api-key: " + (process.env.ELEVENLABS_API_KEY || "platzhalter"), "-H", "content-type: application/json",
      "--data-binary", "@" + body, `https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(stimme.voice_id)}?output_format=mp3_44100_128`]).catch((e) => { throw new Error("ElevenLabs: " + (existsSync(ziel + ".neu") ? readFileSync(ziel + ".neu", "utf8").slice(0, 300) : e.message)); });
    writeFileSync(ziel, readFileSync(ziel + ".neu")); rmSync(ziel + ".neu");
  }
  const { stdout } = await run("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", ziel]);
  return { datei: "ton/sprecher/" + name + ".mp3", dauer: parseFloat(stdout) };
}
const gesprochen = new Map();
let reihe = Promise.resolve();
async function sprecherVon(storyDatei) {
  const out = {};
  if (!storyDatei || !existsSync(path.join(HIER, "stimme.json"))) return out;
  const st = JSON.parse(readFileSync(path.join(HIER, storyDatei), "utf8"));
  // Mehrere Browser fragen gleichzeitig: jeden Satz nur einmal und alle nacheinander einsprechen
  for (const [nr, sz] of st.szenen.entries()) {
    if (!sz.sprecher) continue;
    if (!gesprochen.has(sz.sprecher)) gesprochen.set(sz.sprecher, (reihe = reihe.then(() => sprich(sz.sprecher))));
    out[nr] = await gesprochen.get(sz.sprecher);
  }
  return out;
}

/* ---------- Erklärte Szenen: Übung (Aufnahmen der Seite) und Aufbau (neu eingesprochen) ---------- */
const laenge = async (pfad) => parseFloat((await run("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", pfad])).stdout);
// Eine Aufnahme der Seite holen (einmal je Adresse), als Pfad im Zwischenspeicher
async function holeTon(adresse) {
  if (!adresse) return null;
  const url = adresse.startsWith("http") ? adresse : SEITE + adresse;
  const name = createHash("sha1").update(url).digest("hex").slice(0, 16), ziel = path.join(CACHE, "ton", name + ".mp3");
  mkdirSync(path.dirname(ziel), { recursive: true });
  if (!existsSync(ziel)) { await run("curl", ["-sS", "--fail", "-L", "-m", "90", "-o", ziel + ".neu", url]); writeFileSync(ziel, readFileSync(ziel + ".neu")); rmSync(ziel + ".neu"); }
  return { datei: path.relative(HIER, ziel).split(path.sep).join("/"), dauer: await laenge(ziel) };
}
// Die Begrüßung der Seite nennt erst den Namen der Übung und beschreibt sie dann. Für Videos reicht der Name:
// abschneiden an der ersten Sprechpause.
async function nurName(ton) {
  if (!ton) return null;
  const quelle = path.join(HIER, ton.datei), ziel = quelle.replace(/\.mp3$/, "-name.mp3");
  if (!existsSync(ziel)) {
    const mess = await run("ffmpeg", ["-hide_banner", "-i", quelle, "-af", "silencedetect=noise=-32dB:d=0.22", "-f", "null", "-"]).catch((e) => e);
    // Namen mit Kommas ("Hürde, Leiter, Farbsprint") haben kurze Pausen mittendrin: Das Satzende ist die erste deutlich längere Pause
    const text = String(mess.stderr || ""), starts = [...text.matchAll(/silence_start: ([\d.]+)/g)].map((m) => Number(m[1])), laengen = [...text.matchAll(/silence_duration: ([\d.]+)/g)].map((m) => Number(m[1]));
    const pausen = starts.map((x, i) => ({ x, d: laengen[i] ?? 9 })).filter((q) => q.x > 0.9 && q.x < ton.dauer - 0.5);
    const satzende = pausen.find((q) => q.d >= 0.42) || pausen[0];
    const ende = (satzende ? satzende.x : ton.dauer) + 0.12;
    await run("ffmpeg", ["-y", "-loglevel", "error", "-i", quelle, "-t", String(ende), "-af", `afade=t=out:st=${Math.max(0, ende - 0.1)}:d=0.1`, "-b:a", "128k", ziel]);
  }
  return { datei: path.relative(HIER, ziel).split(path.sep).join("/"), dauer: await laenge(ziel) };
}
const nacheinander = (text) => { if (!gesprochen.has(text)) gesprochen.set(text, (reihe = reihe.then(() => sprich(text)))); return gesprochen.get(text); };
const erklaertCache = new Map();
async function erklaertVon(storyDatei) {
  if (!storyDatei) return {};
  if (!erklaertCache.has(storyDatei)) erklaertCache.set(storyDatei, (async () => {
    const st = JSON.parse(readFileSync(path.join(HIER, storyDatei), "utf8")), alle = await ladeKatalog(), out = {};
    const mitStimme = existsSync(path.join(HIER, "stimme.json"));
    for (const [nr, sz] of st.szenen.entries()) {
      const e = alle.find((x) => x.code === sz.code);
      if (!e || !(sz.typ === "aufbau" || (sz.typ === "uebung" && sz.stimme))) continue;
      // "fassung": 1 = Coaching-Punkt, 2 = Steigerung: Die Seite hat dafür eigene Aufnahmen (Kapitel 1 und 2), die Ansage nennt die Fassung selbst
      const fassung = sz.typ === "uebung" ? sz.fassung || 0 : 0;
      const titel = sz.ohneName || fassung ? null : await nurName(await holeTon(e.audio?.intro).catch(() => null)).catch(() => null);
      if (sz.typ === "uebung") {
        const k = e.audio?.chapters?.[fassung] || {}, zahl = sz.schritte || (k.steps || []).length;
        out[nr] = { titel, ansage: await holeTon(k.intro).catch(() => null), schritte: await Promise.all((k.steps || []).slice(0, zahl).map((u) => holeTon(u).catch(() => null))), texte: (k.steps_text || []).slice(0, zahl) };
      } else if (mitStimme) {
        // Aufbau: Die Seite hat dafür keine Aufnahmen. "sprich" in der Szene ersetzt einzelne Sätze durch kürzere Sprechfassungen.
        const { sprechtext } = await import("./studio/app/sprechtext.js");
        const texte = (e.organisation || []).slice(0, sz.schritte || 99).map((t, i) => sz.sprich?.[i] || sprechtext(t));
        out[nr] = { titel, ansage: sz.ansage === false ? null : await nacheinander(sz.ansage || "So baust du auf."), schritte: [] };
        for (const t of texte) out[nr].schritte.push(await nacheinander(t));
      }
    }
    return out;
  })());
  return erklaertCache.get(storyDatei);
}
// Geräusche und Musik in ton/: Name -> Länge in Sekunden (die Länge braucht die Zufallswahl der Musik)
const klangLaenge = new Map();
const klaenge = () => { try { return Object.fromEntries(readdirSync(path.join(HIER, "ton")).filter((f) => f.endsWith(".mp3")).map((f) => {
  if (!klangLaenge.has(f)) klangLaenge.set(f, parseFloat(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path.join(HIER, "ton", f)]).toString()) || 1);
  return [f.slice(0, -4), klangLaenge.get(f)];
})); } catch { return {}; } };

/* ---------- kleiner Server: Studio, Story-Dateien, Daten, Aufnahmen ---------- */
const TYP = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8", ".woff2": "font/woff2", ".jpg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml" };
function starteServer(port = 0) {
  const server = createServer(async (req, res) => {
    try {
      const u = new URL(req.url, "http://x");
      if (u.pathname === "/") { res.writeHead(302, { location: `/studio/index.html?story=${storyPfad}` }); return res.end(); }
      if (u.pathname === "/api/daten") {
        const alle = await ladeKatalog(), codes = (u.searchParams.get("codes") || "").split(",").filter(Boolean);
        const einheiten = Object.fromEntries(codes.map((c) => [c, alle.find((e) => e.code === c)]).filter(([, e]) => e));
        const filme = {};
        // Fehlt ein Film, läuft die Story ohne ihn weiter (Hook ohne Hintergrund, Übergang "anstoss")
        for (const name of (u.searchParams.get("filme") || "").split(",").filter(Boolean)) {
          try { filme[name] = await zerlegeFilm(name); } catch (err) { console.warn("Hinweis:", err.message); }
        }
        res.writeHead(200, { "content-type": TYP[".json"] });
        const storyDatei = (u.searchParams.get("story") || "").replace(/[^a-zA-Z0-9_\-/.]/g, "");
        const sprecher = /^stories\/[^/]+\.json$/.test(storyDatei) ? await sprecherVon(storyDatei) : {};
        const erklaert = /^stories\/[^/]+\.json$/.test(storyDatei) ? await erklaertVon(storyDatei) : {};
        return res.end(JSON.stringify({ einheiten, filme, filmInfo: filmInfo(), klaenge: klaenge(), sprecher, erklaert }));
      }
      const frei = [["/studio/", path.join(HIER, "studio")], ["/stories/", path.join(HIER, "stories")], ["/cache/", CACHE]].find(([p]) => u.pathname.startsWith(p));
      if (!frei) { res.writeHead(404); return res.end("nicht gefunden"); }
      const pfad = path.normalize(path.join(frei[1], decodeURIComponent(u.pathname.slice(frei[0].length))));
      if (!pfad.startsWith(frei[1])) { res.writeHead(403); return res.end(); }
      const daten = await readFile(pfad);
      res.writeHead(200, { "content-type": TYP[path.extname(pfad)] || "application/octet-stream", "cache-control": "no-store" });
      res.end(daten);
    } catch (err) { res.writeHead(err.code === "ENOENT" ? 404 : 500); res.end(String(err.message || err)); }
  });
  return new Promise((ok) => server.listen(port, "127.0.0.1", () => ok({ server, url: `http://127.0.0.1:${server.address().port}` })));
}

/* ---------- Aufnahmen der echten App für die Szene "app" ---------- */
const smooth = (p) => p * p * (3 - 2 * p);
const clamp01 = (v) => Math.max(0, Math.min(1, v));
async function nimmAppAuf(chromium) {
  const szenen = story.szenen.map((s, i) => [s, i]).filter(([s]) => s.typ === "app");
  if (!szenen.length) return;
  const alle = await ladeKatalog();
  for (const [s, i] of szenen) {
    const ordner = path.join(CACHE, `${kennung}-${i}`), dauer = s.dauer || 5, anzahl = Math.round(dauer * fps);
    const seite = (s.seite || "/").replace(/\{id:([^}]+)\}/g, (_, code) => alle.find((e) => e.code === code)?.id || "");
    const [von, bis] = s.scroll || [0, 2400], halt = s.halt ?? 1.1;
    const info = { anzahl, fps, seite, von, bis, halt, dauer, verstecke: s.verstecke || "" };
    if (!flag("neu") && existsSync(path.join(ordner, "info.json")) && readFileSync(path.join(ordner, "info.json"), "utf8") === JSON.stringify(info)) continue;
    rmSync(ordner, { recursive: true, force: true });
    mkdirSync(ordner, { recursive: true });
    process.stdout.write(`App-Aufnahme ${seite} (${anzahl} Bilder) `);
    const browser = await chromium.launch();
    const page = await (await browser.newContext({ viewport: HANDY, deviceScaleFactor: 1.5, isMobile: true, hasTouch: true, reducedMotion: "no-preference" })).newPage();
    await page.goto((story.basis || SEITE) + seite, { waitUntil: "load", timeout: 90000 });
    // Warten, bis der Preloader der App weg ist und die Seite steht
    await page.waitForFunction(() => { const p = document.getElementById("tk-pre"); return !p || getComputedStyle(p).display === "none"; }, null, { timeout: 30000 }).catch(() => {});
    await page.waitForTimeout(1200);
    // verstecke: CSS-Selektoren von Blöcken, die in dieser Aufnahme nicht zu sehen sein sollen (aufgeräumter Bildschirm)
    if (s.verstecke) { await page.addStyleTag({ content: `${s.verstecke}{display:none!important}` }); await page.waitForTimeout(500); }
    for (let n = 0; n < anzahl; n++) {
      const y = von + (bis - von) * smooth(clamp01((n / fps - halt) / Math.max(0.1, dauer - halt - 0.5)));
      await page.evaluate((top) => new Promise((ok) => { window.scrollTo({ top, behavior: "instant" }); requestAnimationFrame(() => requestAnimationFrame(ok)); }), Math.round(y));
      await page.waitForTimeout(45);
      await page.screenshot({ path: path.join(ordner, String(n).padStart(4, "0") + ".jpg"), type: "jpeg", quality: 82 });
      if (n % 30 === 0) process.stdout.write(".");
    }
    await browser.close();
    writeFileSync(path.join(ordner, "info.json"), JSON.stringify(info));
    console.log(" fertig");
  }
}

/* ---------- Bilder fotografieren und zum Video zusammensetzen ---------- */
async function render(chromium, url) {
  const ziel = `${url}/studio/index.html?render=1&story=${storyPfad}`;
  const jobs = Math.max(1, Math.min(Number(wert("jobs", Math.min(4, os.cpus().length))), 8));
  const oeffne = async () => {
    const browser = await chromium.launch();
    const page = await (await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 })).newPage();
    page.on("pageerror", (e) => console.error("Fehler in der Seite:", e.message));
    await page.goto(ziel, { waitUntil: "load" });
    const info = await page.evaluate(() => window.__story.bereit);
    return { browser, page, info };
  };
  const foto = (page, t, pfad) => page.evaluate((zeit) => window.__story.seek(zeit), t).then(() => page.screenshot({ path: pfad, type: "jpeg", quality: 96 }));

  // Tonspur: jedes Geräusch an seine Stelle, alles zusammengemischt. Ohne Geräusche bleibt die Spur still.
  async function tonspur(ton, dauer) {
    const ein = ["-f", "lavfi", "-t", String(dauer), "-i", "anullsrc=r=44100:cl=stereo"], teile = [];
    for (const k of ton) {
      const pfad = path.join(HIER, k.datei);
      if (!existsSync(pfad)) continue;
      const { stdout } = await run("ffprobe", ["-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration", "-of", "csv=p=0", pfad]);
      const ganz = parseFloat(stdout);
      if (!(ganz > 0)) continue; // Datei ohne Ton
      const stueck = Math.max(0.05, Math.min(k.dauer || ganz, ganz - k.von)), laenge = stueck / k.tempo, n = teile.length + 1;
      ein.push("-i", pfad);
      teile.push(`[${n}:a]atrim=start=${k.von}:duration=${stueck},asetpts=PTS-STARTPTS,aresample=44100,aformat=channel_layouts=stereo${k.tempo !== 1 ? `,atempo=${k.tempo}` : ""},volume=${k.laut}`
        + `,afade=t=in:d=${Math.min(k.ein, laenge / 2)},afade=t=out:st=${Math.max(0, laenge - k.aus)}:d=${Math.min(k.aus, laenge)},adelay=${Math.round(k.start * 1000)}:all=1[t${n}]`);
    }
    const mix = teile.length ? `${teile.join(";")};[0:a]${teile.map((_, i) => `[t${i + 1}]`).join("")}amix=inputs=${teile.length + 1}:normalize=0:duration=first,alimiter=limit=0.9[aus]` : "[0:a]anull[aus]";
    return { ein, mix, anzahl: teile.length };
  }

  // Prüfung vor jedem Rendern: Texte, die überstehen oder abgeschnitten werden, stehen als Warnung in der Ausgabe
  const pruefe = async (page) => {
    const funde = await page.evaluate(() => window.__story.pruefe());
    if (funde.length) console.warn("ACHTUNG, bitte ansehen:\n  " + funde.join("\n  "));
    else console.log("Textprüfung: alle Texte stehen im Bild.");
    return funde;
  };
  const bilder = wert("bild");
  if (bilder) {
    const { browser, page, info } = await oeffne();
    await pruefe(page);
    console.log(`Dauer ${info.dauer.toFixed(2)} s · ${info.ton.length} Geräusche · Szenen: ${info.szenen.map((s) => `${s.typ} ${s.t0.toFixed(2)}–${s.t1.toFixed(2)}`).join(" | ")}`);
    for (const t of bilder.split(",").map(Number)) {
      const pfad = path.join(OUT, `${kennung}-${t.toFixed(2)}.jpg`);
      await foto(page, t, pfad);
      console.log(pfad);
    }
    return browser.close();
  }

  const ordner = path.join(OUT, kennung + "-bilder");
  rmSync(ordner, { recursive: true, force: true });
  mkdirSync(ordner, { recursive: true });
  const seiten = await Promise.all(Array.from({ length: jobs }, oeffne));
  await pruefe(seiten[0].page);
  const { dauer } = seiten[0].info, anzahl = Math.round(dauer * fps);
  console.log(`${kennung}: ${dauer.toFixed(2)} s, ${anzahl} Bilder, ${jobs} Browser`);
  let naechstes = 0, fertig = 0;
  await Promise.all(seiten.map(async ({ page }) => {
    while (naechstes < anzahl) {
      const n = naechstes++;
      await foto(page, n / fps, path.join(ordner, String(n).padStart(5, "0") + ".jpg"));
      if (++fertig % 60 === 0) process.stdout.write(`  ${fertig}/${anzahl}\n`);
    }
  }));
  await Promise.all(seiten.map((s) => s.browser.close()));

  // H.264 mit Tonspur (Geräusche und Filmton; ohne beides still): so nimmt Instagram die Datei ohne Umwege
  const mp4 = path.join(OUT, kennung + ".mp4"), spur = await tonspur(seiten[0].info.ton || [], dauer);
  await new Promise((ok, nein) => {
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(ordner, "%05d.jpg"), ...spur.ein,
      "-filter_complex", `[0:v]scale=in_color_matrix=bt601:in_range=full:out_color_matrix=bt709:out_range=tv,format=yuv420p[bild];${spur.mix.replace(/\[(\d+):a\]/g, (_, n) => `[${Number(n) + 1}:a]`)}`,
      "-map", "[bild]", "-map", "[aus]", "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-profile:v", "high",
      "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-r", String(fps), "-c:a", "aac", "-b:a", "128k", "-t", dauer.toFixed(3), "-movflags", "+faststart", mp4], { stdio: "inherit" });
    ff.on("exit", (c) => (c === 0 ? ok() : nein(new Error("ffmpeg ist mit Fehler " + c + " ausgestiegen"))));
  });
  // Titelbild für die Übersicht: ein Bild aus der ersten Szene
  const titel = path.join(OUT, kennung + ".jpg");
  const erste = seiten[0].info.szenen.find((x) => x.typ !== "intro") || seiten[0].info.szenen[0];
  const n = Math.min(anzahl - 1, Math.round((erste.t0 + 2.4) * fps));
  writeFileSync(titel, readFileSync(path.join(ordner, String(n).padStart(5, "0") + ".jpg")));
  if (!flag("bilder-behalten")) rmSync(ordner, { recursive: true, force: true });
  console.log(`Fertig: ${mp4} (${(statSync(mp4).size / 1e6).toFixed(1)} MB, ${spur.anzahl} Geräusche) · Titelbild: ${titel}`);
}

const { chromium } = createRequire(import.meta.url)("playwright");
const { server, url } = await starteServer(befehl === "vorschau" ? Number(wert("port", 4173)) : 0);
await nimmAppAuf(chromium);
if (befehl === "vorschau") console.log(`Vorschau: ${url}/  (Strg+C beendet)`);
else { await render(chromium, url); server.close(); }
