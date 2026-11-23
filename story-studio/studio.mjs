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
import { execFile, spawn } from "node:child_process";
import { promisify } from "node:util";
import { existsSync, mkdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const run = promisify(execFile);
const HIER = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(HIER, "out"), CACHE = path.join(OUT, "cache");
const APP = "6afec076c6c4a55a7cb4995e";                       // Trainingskern bei Base44
const KATALOG = `https://app.base44.com/api/apps/${APP}/entities/Einheit?limit=1000`; // öffentliche Leseschnittstelle
const SEITE = "https://trainingskern.base44.app";             // die veröffentlichte App (für Aufnahmen im Handy)
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
const sichtbar = (e) => !e.hidden;

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
        res.writeHead(200, { "content-type": TYP[".json"] });
        return res.end(JSON.stringify({ anzahl: alle.filter(sichtbar).length, einheiten }));
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
    const info = { anzahl, fps, seite, von, bis, halt, dauer };
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

  const bilder = wert("bild");
  if (bilder) {
    const { browser, page, info } = await oeffne();
    console.log(`Dauer ${info.dauer.toFixed(2)} s · Szenen: ${info.szenen.map((s) => `${s.typ} ${s.t0.toFixed(2)}–${s.t1.toFixed(2)}`).join(" | ")}`);
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

  // H.264 mit stiller Tonspur: so nimmt Instagram die Datei ohne Umwege, Musik kommt in der Instagram-App dazu
  const mp4 = path.join(OUT, kennung + ".mp4");
  await new Promise((ok, nein) => {
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(ordner, "%05d.jpg"), "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
      "-vf", "scale=in_color_matrix=bt601:in_range=full:out_color_matrix=bt709:out_range=tv,format=yuv420p", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high",
      "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-r", String(fps), "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", mp4], { stdio: "inherit" });
    ff.on("exit", (c) => (c === 0 ? ok() : nein(new Error("ffmpeg ist mit Fehler " + c + " ausgestiegen"))));
  });
  // Titelbild für die Übersicht: ein Bild aus der ersten Szene
  const titel = path.join(OUT, kennung + ".jpg");
  const n = Math.min(anzahl - 1, Math.round((seiten[0].info.szenen[0].t0 + 2.6) * fps));
  writeFileSync(titel, readFileSync(path.join(ordner, String(n).padStart(5, "0") + ".jpg")));
  if (!flag("bilder-behalten")) rmSync(ordner, { recursive: true, force: true });
  console.log(`Fertig: ${mp4} (${(statSync(mp4).size / 1e6).toFixed(1)} MB) · Titelbild: ${titel}`);
}

const { chromium } = createRequire(import.meta.url)("playwright");
const { server, url } = await starteServer(befehl === "vorschau" ? Number(wert("port", 4173)) : 0);
await nimmAppAuf(chromium);
if (befehl === "vorschau") console.log(`Vorschau: ${url}/  (Strg+C beendet)`);
else { await render(chromium, url); server.close(); }
