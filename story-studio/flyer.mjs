#!/usr/bin/env node
// Flyer zu allem, was Trainingskern bietet: out/flyer-feed.jpg (1080 × 1350, Beitrag) und out/flyer-story.jpg (1080 × 1920, Story/Status).
// Braucht out/whatsapp-status-01.mp4 (daraus kommen Marke und das Bild der Tafel).
import { createRequire } from "node:module";
import { execFileSync } from "node:child_process";
import { writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
const { chromium } = createRequire(import.meta.url)("playwright");
const HIER = path.dirname(fileURLToPath(import.meta.url)), OUT = path.join(HIER, "out");
const video = path.join(OUT, "whatsapp-status-01.mp4"), tafel = path.join(OUT, "flyer-tafel.jpg");
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-ss", "19.5", "-i", video, "-frames:v", "1", "-q:v", "2", tafel]);
const T = pathToFileURL(tafel).href;
const punkte = ["Jede Übung animiert", "Auf Deutsch eingesprochen", "Bambini bis Senioren", "Torhüter & Einzeltraining",
  "Fertige Trainingspläne", "Spielsysteme erklärt", "Nach DFB: 15-30-15-30", "Anpassbar an deine Zeit", "Über 100 neue Übungen im Monat"];
const css = (h) => `@import url("${pathToFileURL(path.join(HIER, "studio/app/fonts.css")).href}");
*{box-sizing:border-box;margin:0}body{width:1080px;height:${h}px;background:#0d0d0b;color:#f8f4e9;font-family:"Space Grotesk",sans-serif;overflow:hidden;position:relative}
.raster{position:absolute;right:-60px;top:${h > 1500 ? 160 : 60}px;width:620px;height:620px;background:radial-gradient(circle,#d4ff00 2.2px,transparent 2.6px) 0 0/22px 22px;opacity:.16;mask-image:radial-gradient(circle at 70% 30%,#000,transparent 70%)}
.marke{position:absolute;left:55px;top:${h > 1500 ? 90 : 50}px;width:435px;height:105px;background:url('${T}') -55px -250px/1080px 1920px}
h1{position:absolute;left:66px;top:${h > 1500 ? 260 : 190}px;font-family:Archivo,sans-serif;font-weight:900;font-stretch:92%;font-size:${h > 1500 ? 94 : 96}px;line-height:.95;letter-spacing:-.015em;text-transform:uppercase}
h1 span{display:block}h1 .n{display:inline-block;background:#d4ff00;color:#0d0d0b;padding:.05em .14em 0;margin:.08em 0 0 -.06em;box-shadow:10px 10px 0 #ff5500}
.tafel{position:absolute;left:0;right:0;top:${h > 1500 ? 590 : 0}px;height:${h > 1500 ? 420 : 0}px;background:url('${T}') center -${h > 1500 ? 680 : 0}px/1080px 1920px;${h > 1500 ? "" : "display:none"}}
.tafel::after{content:"";position:absolute;inset:0;background:linear-gradient(#0d0d0b,transparent 18%,transparent 78%,#0d0d0b)}
.grid{position:absolute;left:66px;right:66px;top:${h > 1500 ? 1030 : 490}px;display:grid;grid-template-columns:1fr 1fr;gap:${h > 1500 ? 20 : 18}px 22px}
.p{display:flex;align-items:center;gap:16px;background:#f8f4e9;color:#0d0d0b;padding:${h > 1500 ? 20 : 18}px 20px;font-weight:600;font-size:${h > 1500 ? 31 : 31}px;line-height:1.1;box-shadow:7px 7px 0 #ff5500;rotate:var(--r)}
.p b{flex:none;display:grid;place-items:center;width:44px;height:44px;background:#d4ff00;font-size:30px}.p.breit{grid-column:1/3;background:#d4ff00}.p.breit b{background:#0d0d0b;color:#d4ff00}
.cta{position:absolute;left:66px;top:${h > 1500 ? 1690 : 1085}px;background:#d4ff00;color:#0d0d0b;font-family:Archivo,sans-serif;font-weight:900;font-stretch:92%;font-size:${h > 1500 ? 66 : 62}px;line-height:1;padding:20px 28px 14px;text-transform:uppercase;white-space:nowrap;box-shadow:12px 12px 0 #ff5500}
.adr{position:absolute;left:70px;top:${h > 1500 ? 1810 : 1205}px;font-weight:700;font-size:44px}.adr span{color:#8d8a80;font-weight:500}
.hand{position:absolute;right:66px;top:${h > 1500 ? 1600 : 1085}px;font-family:"Permanent Marker",cursive;font-size:44px;color:#ff5500;rotate:-6deg;text-align:right;line-height:1.05}`;
const seite = (h) => `<!doctype html><meta charset="utf-8"><style>${css(h)}</style><body><div class="raster"></div><div class="marke"></div>
<h1><span>Training heute?</span><span>Kein Plan?</span><span class="n">trainingskern.de</span></h1><div class="tafel"></div>
<div class="grid">${punkte.map((p, i) => `<div class="p${i === punkte.length - 1 ? " breit" : ""}" style="--r:${[-0.8, 0.7, 0.5, -0.6, -0.4, 0.8, 0.6, -0.7, -0.3][i]}deg"><b>✓</b>${p}</div>`).join("")}</div>
<div class="cta">Kostenlos registrieren</div><p class="adr">trainingskern.de <span>· Insta @trainings.kern</span></p><p class="hand">${h > 1500 ? "" : ""}</p></body>`;
const browser = await chromium.launch(), page = await browser.newPage();
for (const [name, h] of [["flyer-feed", 1350], ["flyer-story", 1920]]) {
  await page.setViewportSize({ width: 1080, height: h });
  const tmp = path.join(OUT, name + ".html"); writeFileSync(tmp, seite(h)); await page.goto(pathToFileURL(tmp).href, { waitUntil: "load" }); await page.evaluate(() => document.fonts.ready);
  const ueber = await page.evaluate(() => [...document.querySelectorAll("h1,.p,.cta,.adr")].filter((e) => { const r = e.getBoundingClientRect(); return r.right > 1080 || r.bottom > innerHeight || e.scrollWidth > e.clientWidth + 1; }).map((e) => e.textContent));
  if (ueber.length) console.log("ACHTUNG, steht über:", ueber.join(" | "));
  await page.screenshot({ path: path.join(OUT, name + ".jpg"), type: "jpeg", quality: 92 }); console.log(path.join(OUT, name + ".jpg"));
}
await browser.close();
