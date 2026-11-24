#!/usr/bin/env node
// Die drei Story-Bilder zum Reel des Tages (1080 × 1920): Ankündigung, Frage, "Jetzt neu".
//   node storys.mjs stories/<name>.json
// Braucht das fertig gerenderte Video in out/ und in der Story-Datei den Block "storys":
//   Marketing-Videos: { "art": "marketing", "zeit": "18:30", "bilder": [5, 5], "problem": [2 Zeilen], "problemSatz", "frage": [2 Zeilen], "antwort", "loesung": [2 Zeilen], "loesungSatz" }
//   Übungs-Videos: { "name": "Name der Übung", "zeit": "18:30", "bilder": [16, 36], "frage": ["Wie startet", "dein Training?"], "antwort": "Ein Satz zum Antworten." }
// "bilder": zwei Zeitpunkte im Video (Sekunden) für Bild 1 und Bild 3. Ergebnis: out/<name>-story-1.jpg bis -3.jpg
import { createRequire } from "node:module";
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
const { chromium } = createRequire(import.meta.url)("playwright");
const HIER = path.dirname(fileURLToPath(import.meta.url)), OUT = path.join(HIER, "out");
const datei = process.argv[2];
if (!datei) { console.error("Aufruf: node storys.mjs stories/<name>.json"); process.exit(1); }
const story = JSON.parse(readFileSync(path.join(HIER, datei), "utf8")), kennung = path.basename(datei, ".json"), st = story.storys;
if (!st) { console.error(`In ${datei} fehlt der Block "storys".`); process.exit(1); }
const video = path.join(OUT, kennung + ".mp4");
if (!existsSync(video)) { console.error("Erst das Video rendern: " + video); process.exit(1); }
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const bild = (t, n) => { const p = path.join(OUT, `${kennung}-story-bild${n}.jpg`); execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-ss", String(t), "-i", video, "-frames:v", "1", "-q:v", "2", p]); return pathToFileURL(p).href; };
const b1 = bild(st.bilder[0], 1), b3 = bild(st.bilder[1], 3);
const css = `@import url("${pathToFileURL(path.join(HIER, "studio/app/fonts.css")).href}");
*{box-sizing:border-box;margin:0}body{width:1080px;height:1920px;background:#0d0d0b;overflow:hidden;position:relative;color:#f8f4e9;font-family:"Space Grotesk",sans-serif}
.bg{position:absolute;inset:0;background-size:1080px 1920px}
.band{position:absolute;left:0;right:0;top:1440px;bottom:0;background:#0d0d0b}.band::before{content:"";position:absolute;left:0;right:0;top:-70px;height:70px;background:linear-gradient(transparent,#0d0d0b)}
.box{position:absolute;left:72px;top:1468px;background:#d4ff00;color:#0d0d0b;font-family:Archivo,sans-serif;font-weight:900;font-stretch:92%;font-size:120px;line-height:1;letter-spacing:-.015em;padding:18px 30px 14px;text-transform:uppercase;white-space:nowrap;box-shadow:14px 14px 0 #ff5500}
.zeile{position:absolute;left:76px;right:72px;top:1642px;font-weight:600;font-size:42px;line-height:1.2}
.marke{position:absolute;inset:0;background-size:1080px 1920px;clip-path:inset(250px 590px 1565px 55px);translate:0 45px}
.tag{position:absolute;left:72px;top:470px;background:#d4ff00;color:#0d0d0b;font-weight:700;font-size:40px;padding:10px 20px;text-transform:uppercase}
h1{position:absolute;left:72px;top:590px;font-family:Archivo,sans-serif;font-weight:900;font-stretch:92%;font-size:140px;line-height:.98;letter-spacing:-.015em;text-transform:uppercase;white-space:nowrap}h1 span{display:block}h1 span:last-child{color:#d4ff00}
.strich{position:absolute;left:72px;width:150px;height:12px;background:#ff5500}.sub{position:absolute;left:72px;right:72px;font-weight:500;font-size:46px;line-height:1.35}
.fuss{position:absolute;left:72px;top:1562px;font-weight:600;font-size:40px;color:#8d8a80}`;
const seite = (inhalt) => `<!doctype html><meta charset="utf-8"><style>${css}</style><body>${inhalt}</body>`;
const mitBild = (url, box, zeile) => seite(`<div class="bg" style="background-image:url('${url}')"></div><div class="band"></div><div class="box">${esc(box)}</div><p class="zeile">${esc(zeile)}</p>`);
const textSeite = (tag, zeilen, sub, unten) => seite(`<div class="marke" style="background-image:url('${b1}')"></div><div class="tag">${esc(tag)}</div><h1>${zeilen.map((z) => `<span>${esc(z)}</span>`).join("")}</h1><i class="strich"></i><p class="sub">${esc(sub)}</p>${unten}`);
const fuss = `<p class="fuss">trainingskern.de &nbsp;·&nbsp; Link in Bio</p>`;
// "art": "marketing" (Videos, die Trainingskern selbst bewerben): erst das Problem, dann die Frage, dann die Lösung für den Abend.
// Sonst (Übungs-Videos): Ankündigung mit Bild aus der Übung, Frage, "Jetzt neu".
const seiten = st.art === "marketing" ? [
  textSeite("Kennst du das?", st.problem, st.problemSatz, fuss),
  textSeite("Frage an dich", st.frage, st.antwort, fuss),
  textSeite("Die Lösung", st.loesung, st.loesungSatz, `<div class="box">Heute ${esc(st.zeit || "18:30")}</div><p class="zeile">So geht’s: neues Reel auf dem Profil.</p>`),
] : [
  mitBild(b1, `Heute ${st.zeit || "18:30"}`, `Neues Reel: ${st.name}`),
  textSeite("Frage an dich", st.frage, st.antwort, fuss),
  mitBild(b3, "Jetzt neu", "Ganzes Reel auf dem Profil."),
];
const browser = await chromium.launch(), page = await (await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 })).newPage();
for (const [i, html] of seiten.entries()) {
  const tmp = path.join(OUT, `${kennung}-story-${i + 1}.html`);
  writeFileSync(tmp, html);
  await page.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  // Einpassen: Fläche und Frage dürfen nicht über den rechten Rand, die Zeilen darunter rücken nach
  const zuBreit = await page.evaluate(() => {
    const passe = (el, max) => { if (!el) return; let px = parseFloat(getComputedStyle(el).fontSize); while (el.scrollWidth > max && px > 40) { px -= 4; el.style.fontSize = px + "px"; } };
    passe(document.querySelector(".box"), 880); passe(document.querySelector("h1"), 936);
    const h = document.querySelector("h1"), s = document.querySelector(".strich"), sub = document.querySelector(".sub");
    if (h) { s.style.top = h.offsetTop + h.offsetHeight + 40 + "px"; sub.style.top = h.offsetTop + h.offsetHeight + 96 + "px"; }
    return [...document.querySelectorAll(".box,h1,.zeile,.sub,.tag")].filter((e) => e.getBoundingClientRect().right > 1010 || e.scrollWidth > e.clientWidth + 2).map((e) => e.textContent.slice(0, 40));
  });
  if (zuBreit.length) console.warn("ACHTUNG, Text zu lang in Bild " + (i + 1) + ": " + zuBreit.join(" | "));
  const ziel = path.join(OUT, `${kennung}-story-${i + 1}.jpg`);
  await page.screenshot({ path: ziel, type: "jpeg", quality: 92 });
  execFileSync("rm", ["-f", tmp]);
  console.log(ziel);
}
await browser.close();
