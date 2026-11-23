// Story-Studio: baut aus einer Story-Datei (stories/*.json) eine Instagram-Story im Aussehen der App.
// Alles hängt an einer einzigen Zeit t (Sekunden): seek(t) stellt jedes Teil genau auf diesen Moment.
// So kann der Renderer (render.mjs) Bild für Bild fotografieren, und das Video ruckelt nie.
//
// Ablauf jeder Story: Intro (immer gleich, abwählbar) -> Szenen mit Übergängen -> letzte Szene (meist "abpfiff").
import { bauePlatz, tafelVon } from "./platz.js";

const W = 1080, H = 1920;
const GRENZE = 1450;             // tiefer steht in keiner Szene Text: darunter läuft die Spielminute
const q = new URLSearchParams(location.search);
const RENDER = q.has("render");
const frame = document.getElementById("frame");

const E = { raus: "cubic-bezier(.2,.8,.2,1)", feder: "cubic-bezier(.3,1.5,.4,1)", stark: "cubic-bezier(.3,1.9,.4,1)", rein: "cubic-bezier(.76,0,.24,1)", weich: "cubic-bezier(.45,0,.55,1)", gerade: "linear" };
const clamp01 = (v) => Math.max(0, Math.min(1, v));
const smooth = (p) => p * p * (3 - 2 * p);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const el = (html) => { const t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstElementChild; };

/* ---------- Zeitleiste ---------- */
const anims = [], haken = [], ton = [];
// Ein Geräusch oder die Tonspur eines Films: datei (unter filme/ oder ton/), start = Zeit in der Story,
// von = Stelle in der Datei, dauer, laut (0..1), tempo. Der Renderer mischt daraus die Tonspur.
const klang = (datei, start, o = {}) => ton.push({ datei, start: Math.max(0, start), von: o.von || 0, dauer: o.dauer || 0, laut: o.laut ?? 1, tempo: o.tempo || 1, ein: o.ein ?? 0.04, aus: o.aus ?? 0.25 });
const bild = (src) => new Promise((ok, nein) => { const b = new Image(); b.onload = () => b.decode().then(() => ok(b), () => ok(b)); b.onerror = () => nein(new Error("Bild fehlt: " + src)); b.src = src; });
// Eine Bildfolge (Film oder App-Aufnahme) auf einer Leinwand: zeig(n) lädt Bild n nach und malt es.
// Gibt ein Versprechen zurück, auf das seek() wartet. So ist beim Fotografieren immer das richtige Bild da.
function bildfolge(cv, ordner, anzahl) {
  const cx = cv.getContext("2d");
  let soll = -1;
  return (n) => {
    n = Math.max(0, Math.min(anzahl - 1, Math.floor(n)));
    if (n === soll) return null;
    soll = n;
    return bild(`/cache/${ordner}/${String(n).padStart(4, "0")}.jpg`).then((b) => {
      if (soll !== n) return;
      if (cv.width !== b.naturalWidth) { cv.width = b.naturalWidth; cv.height = b.naturalHeight; }
      cx.drawImage(b, 0, 0);
    });
  };
}
// Eine Bewegung: kf = Keyframes, t0 = Start in Sekunden (Zeit der ganzen Story), dauer in Sekunden
function an(node, kf, t0, dauer, easing = E.raus, fill = "both") {
  const a = node.animate(kf, { delay: t0 * 1000, duration: Math.max(1, dauer * 1000), easing, fill });
  a.pause();
  anims.push(a);
  return a;
}
const steig = (node, t, d = 0.5) => an(node, [{ translate: "0 112%" }, { translate: "0 0" }], t, d);
const plopp = (node, t, d = 0.5, von = 0) => an(node, [{ scale: String(von), opacity: 0 }, { opacity: 1, offset: 0.25 }, { scale: "1", opacity: 1 }], t, d, E.feder);
const blende = (node, t, d = 0.3) => an(node, [{ opacity: 0 }, { opacity: 1 }], t, d, E.gerade);
const schieb = (node, t, d = 0.5, x = 60, y = 0) => an(node, [{ translate: `${x}px ${y}px`, opacity: 0 }, { translate: "0 0", opacity: 1 }], t, d);
const stempeln = (node, t) => an(node, [{ scale: "2.2", opacity: 0 }, { scale: "0.94", opacity: 1, offset: 0.55 }, { scale: "1.04", offset: 0.75 }, { scale: "1", opacity: 1 }], t, 0.42, E.gerade);

/* ---------- Marke ---------- */
const K = { STEM: "M250,231H455V429H333V595H455V794H250Z", UP: "M481,419L662,231H832V270L598,496H481Z", DOWN: "M481,529H598L832,754V794H655L481,612Z",
  FRAME: "M333,429H480V595H333Z", CORE: "M352,451H467V566H352Z", BOX: "M217,103H806L921,217V806L806,921H217L103,806V217Z" };
// Das K in der Box. hell = helle Box mit schwarzem K (für dunkle Flächen)
const kBox = (cls, hell = true) => `<svg class="${cls}" viewBox="102 102 820 820"><path class="k-box" d="${K.BOX}" fill="${hell ? "#f8f4e9" : "#0d0d0b"}"/>
<path class="k-stem" d="${K.STEM}" fill="${hell ? "#0d0d0b" : "#f8f4e9"}"/><path class="k-up" d="${K.UP}" fill="${hell ? "#0d0d0b" : "#f8f4e9"}"/><path class="k-down" d="${K.DOWN}" fill="${hell ? "#0d0d0b" : "#f8f4e9"}"/>
<path class="k-frame" d="${K.FRAME}" fill="#0d0d0b"/><path class="k-core" d="${K.CORE}" fill="#d4ff00"/></svg>`;
const ballSvg = (rand = "#0d0d0b") => `<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10.5" fill="#f8f4e9" stroke="${rand}" stroke-width="2"/><path d="M12,7.5 L16,10.5 L14.5,15.5 H9.5 L8,10.5 Z" fill="#0d0d0b"/></svg>`;

/* ---------- Intro ---------- */
// Ohne Angabe: der Preloader der App im Hochformat (immer gleich). Mit film: ein Clip, der auf dem K endet,
// danach steigt TRAININGSKERN auf. Das Intro ist eine Szene wie jede andere (typ "intro") und steht von selbst
// am Anfang; mit "intro": false in der Story entfällt es und kann als Szene an anderer Stelle stehen.
function introSzene(s, daten) {
  const film = s.film ? daten.filme[s.film] : null;
  const wort = [..."TRAININGSKERN"].map((c) => `<span>${c}</span>`).join("");
  const node = el(`<section class="sz intro">${film ? `<canvas class="in-film"></canvas>` : ""}
<svg class="feld" viewBox="0 0 ${W} ${H}"><line x1="0" y1="900" x2="${W}" y2="900" pathLength="1"/><circle cx="540" cy="900" r="340" pathLength="1" transform="rotate(-90 540 900)"/><circle class="punkt" cx="540" cy="900" r="9"/></svg>
<div class="mitte">${kBox("k")}<div class="wort">${wort}<i></i></div></div>
<div class="seitenlinie"><span class="hinweis">Anstoß</span><span class="min">0′</span><span class="ball">${ballSvg()}</span></div></section>`);
  frame.append(node);
  const $ = (x) => node.querySelector(x);
  // Angaben zum Film aus filme/filme.json: ab/bis = genutzter Ausschnitt, tempo, k = wo das K im letzten Bild sitzt [x, y, Breite] bei 720 px Bildbreite
  // Ohne Angaben misst der Renderer selbst aus, wo das K sitzt und ab wann es steht (film.auto). Der Filmteil dauert höchstens gut zwei Sekunden.
  const fi = film ? { ...(film.auto || {}), ...(daten.filmInfo[s.film] || {}) } : {};
  const ab = s.ab ?? fi.ab ?? 0, bis = Math.min(s.bis ?? fi.bis ?? 99, film ? film.dauer : 99);
  const tempo = s.tempo || fi.tempo || (film ? Math.max(1, (bis - ab) / 2.2) : 1);
  const filmDauer = film ? (bis - ab) / tempo : 0;
  if (fi.k) {
    // Das gezeichnete K genau auf das K des Films legen, das Wort rückt mit
    const [x, y, b] = fi.k.map((v) => v * 1.5), mitte = node.querySelector(".mitte"), k = node.querySelector(".k");
    mitte.style.translate = `${(x + b / 2 - 540).toFixed(1)}px ${(y + b / 2 - 825).toFixed(1)}px`;
    k.style.scale = (b / 310).toFixed(4);
    node.querySelector(".wort").style.translate = `0 ${Math.max(0, (b - 310) / 2 + (b > 330 ? 14 : 0)).toFixed(1)}px`; // ein größeres K schiebt das Wort nach unten
  }
  const dauer = film ? filmDauer + 0.95 : 1.85 / tempo;
  return { el: node, ton: "dunkel", dauer, intro: true, ohneMarke: true, ohneUhr: true, start(T) {
    const z = (x) => T + x / (film ? 1 : tempo), d = (x) => x / (film ? 1 : tempo); // Zeiten des Preloaders, gestaucht um tempo
    const w0 = film ? filmDauer - 0.05 : 0.48;
    if (film) {
      // Der Film läuft bis zum K, dann übernimmt das gezeichnete K nahtlos (gleiche Stelle, gleiche Größe)
      const zeig = bildfolge($(".in-film"), "film-" + s.film, film.anzahl);
      haken.push((zeit) => (zeit < T - 0.2 || zeit > T + dauer + 0.2 ? null : zeig((ab + (zeit - T) * tempo) * film.fps)));
      $(".feld").style.display = "none"; $(".seitenlinie").style.display = "none";
      blende($(".k"), T + filmDauer - 0.12, 0.12);
      an($(".in-film"), [{ opacity: 1 }, { opacity: 0 }], T + filmDauer, 0.2, E.gerade, "forwards");
      if (s.filmTon !== false) klang(`filme/${s.film}.mp4`, T, { von: ab, dauer: Math.min(film.dauer, bis + 0.9) - ab, tempo, laut: s.laut ?? 1, aus: 0.5 });
    } else {
      an($(".feld circle"), [{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], z(0.05), d(1.0), "cubic-bezier(.7,0,.2,1)");
      an($(".feld line"), [{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], z(0.15), d(0.9), "cubic-bezier(.7,0,.2,1)");
      an($(".k-box"), [{ transform: "scale(.4) rotate(-18deg)", opacity: 0 }, { transform: "none", opacity: 1 }], z(0), d(0.6), E.feder);
      an($(".k-stem"), [{ transform: "translateY(60%)", opacity: 0 }, { transform: "none", opacity: 1 }], z(0.25), d(0.5), "cubic-bezier(.3,1.4,.4,1)");
      an($(".k-up"), [{ transform: "translate(70%,-40%)", opacity: 0 }, { transform: "none", opacity: 1 }], z(0.38), d(0.5), "cubic-bezier(.3,1.4,.4,1)");
      an($(".k-down"), [{ transform: "translate(70%,40%)", opacity: 0 }, { transform: "none", opacity: 1 }], z(0.47), d(0.5), "cubic-bezier(.3,1.4,.4,1)");
      blende($(".k-frame"), z(0.52), d(0.25));
      an($(".k-core"), [{ transform: "scale(0)" }, { transform: "scale(1.45)", offset: 0.6 }, { transform: "scale(1)" }], z(0.66), d(0.55), E.gerade);
      an($(".ball"), [{ left: "0%", rotate: "0deg" }, { left: "100%", rotate: "720deg" }], z(0.1), d(1.4), E.weich);
      blende($(".seitenlinie"), T, 0.2);
      const min = $(".min");
      haken.push((t) => { min.textContent = Math.round(90 * smooth(clamp01((t - z(0.1)) / d(1.4)))) + "′"; });
      if (daten.klaenge.intro) klang("ton/intro.mp3", T, { tempo });
    }
    node.querySelectorAll(".wort span").forEach((b, i) => an(b, [{ transform: "translateY(110%)" }, { transform: "none" }], z(w0) + i * 0.026, 0.4, "cubic-bezier(.2,1.2,.3,1)"));
    an($(".wort i"), [{ transform: "scale(0)" }, { transform: "none" }], z(w0) + 0.42, 0.34, E.stark);
    // Abgang: Logo wird einen Hauch größer und verschwindet, dann zieht der Vorhang an der Mittellinie auf
    an($(".mitte"), [{ opacity: 1, scale: "1" }, { opacity: 0, scale: "1.05" }], T + dauer - 0.3, 0.22, E.gerade, "forwards");
    an($(".seitenlinie"), [{ opacity: 1 }, { opacity: 0 }], T + dauer - 0.3, 0.2, E.gerade, "forwards");
    an($(".feld"), [{ opacity: 1 }, { opacity: 0 }], T + dauer - 0.25, 0.2, E.gerade, "forwards");
  } };
}

/* ---------- Übergänge: Schnitt bei T ---------- */
// anstoss: zwei schwarze Hälften schließen an der Mittellinie, Lichtblitz, das K blitzt auf, die Hälften ziehen auf
// streifen: ein schräges Band (Orange, Neon, Schwarz) wischt über das Bild
// blitz: harter Schnitt mit kurzem Neon-Blitz
// marker: ein dicker Stift kritzelt das Bild schwarz zu und gibt das nächste wieder frei (generierter Wischer)
// staub: eine Wolke aus Neon-Kreide fegt über den Schnitt (generierter Wischer)
// nachIntro: der Vorhang ist schon zu (das Intro steht auf Schwarz), er zieht nur noch auf
function baueUebergang(art, T, nachIntro, daten) {
  const u = el(`<div class="ue"></div>`);
  frame.append(u);
  let von = T - 0.34, bis = T + 0.5;
  const film = { marker: "wischer-marker", staub: "wischer-staub" }[art], f = film && daten.filme[film];
  if (f && !nachIntro) {
    const m = daten.filmInfo[film] || {};
    u.innerHTML = `<canvas class="wisch${art === "staub" ? " gross" : ""}"></canvas>`;
    u.style.mixBlendMode = art === "marker" ? "multiply" : "screen"; // an der Hülle, sonst mischt die Leinwand nur mit sich selbst
    const zeig = bildfolge(u.firstChild, "film-" + film, f.anzahl);
    if (art === "marker") {
      // Vorwärts bis alles schwarz ist (Schnitt), dann rückwärts wieder frei
      const zu = m.zu ?? f.dauer, hin = 0.5, weg = 0.45; // zu = Stelle im Film, an der das Bild ganz schwarz ist
      von = T - hin; bis = T + weg;
      haken.push((z) => (z < von - 0.1 || z > bis + 0.1 ? null : zeig((z <= T ? zu * clamp01((z - von) / hin) ** 1.6 : zu * clamp01(1 - (z - T) / weg) ** 1.6) * f.fps)));
      klang(`filme/${film}.mp4`, von, { von: m.tonAb || 0.3, dauer: hin + weg, laut: 0.8 });
    } else {
      const a = m.ab ?? 0, e = m.bis ?? f.dauer, mitte = m.mitte ?? (a + e) / 2, hin = 0.4, weg = 0.55; // mitte = dichteste Stelle
      von = T - hin; bis = T + weg;
      haken.push((z) => (z < von - 0.1 || z > bis + 0.1 ? null : zeig((z <= T ? a + (mitte - a) * clamp01((z - von) / hin) : mitte + (e - mitte) * clamp01((z - T) / weg)) * f.fps)));
      u.insertAdjacentHTML("beforeend", `<div class="weiss"></div>`);
      an(u.lastChild, [{ opacity: 0 }, { opacity: 0.9, offset: 0.45 }, { opacity: 0 }], T - 0.1, 0.3, E.gerade);
      klang(`filme/${film}.mp4`, von, { von: m.tonAb || 0, dauer: hin + weg + 0.3, laut: 0.8 });
    }
  } else if (art === "streifen" && !nachIntro) {
    u.innerHTML = `<div class="band"><i class="o"></i><i class="n"></i><i class="t"></i><i class="n"></i><i class="o"></i></div>`;
    von = T - 0.42; bis = T + 0.42;
    // Bei T liegt das schwarze Mittelstück genau über dem Bild
    an(u.firstChild, [{ translate: "-2500px 0" }, { translate: "-410px 0", offset: 0.5, easing: "cubic-bezier(.3,0,.4,1)" }, { translate: "1680px 0" }], von, bis - von, "cubic-bezier(.6,0,.7,1)");
    if (daten.klaenge.wusch) klang("ton/wusch.mp3", T - 0.3, { laut: 0.7 });
  } else if (art === "blitz" && !nachIntro) {
    u.innerHTML = `<div class="weiss"></div>`;
    von = T - 0.06; bis = T + 0.26;
    an(u.firstChild, [{ opacity: 0 }, { opacity: 1, offset: 0.18 }, { opacity: 0 }], von, bis - von, E.gerade);
    if (daten.klaenge.klick) klang("ton/klick.mp3", T - 0.05, { laut: 0.7 });
  } else {
    u.innerHTML = `<i class="halb oben"></i><i class="halb unten"></i><i class="blitz"></i>${nachIntro ? "" : kBox("siegel")}`;
    const [o, n, b, k] = u.children;
    if (nachIntro) { von = T - 0.2; }
    else {
      an(o, [{ translate: "0 -101%" }, { translate: "0 0" }], von, 0.3, E.rein);
      an(n, [{ translate: "0 101%" }, { translate: "0 0" }], von, 0.3, E.rein);
      an(k, [{ opacity: 0, scale: ".5" }, { opacity: 1, scale: "1.08", offset: 0.35 }, { opacity: 1, scale: "1", offset: 0.7 }, { opacity: 0, scale: "1.1" }], T - 0.1, 0.3, E.gerade);
      if (daten.klaenge.rumms) klang("ton/rumms.mp3", T - 0.08, { laut: 0.8 });
    }
    an(b, [{ transform: "scaleX(0)", opacity: 1 }, { transform: "scaleX(1)", opacity: 1, offset: 0.45 }, { transform: "scaleX(1)", opacity: 0 }], T - 0.16, 0.36, E.gerade);
    an(o, [{ translate: "0 0" }, { translate: "0 -101%" }], T + 0.06, 0.44, E.rein, "forwards");
    an(n, [{ translate: "0 0" }, { translate: "0 101%" }], T + 0.06, 0.44, E.rein, "forwards");
    if (nachIntro && daten.klaenge.wusch) klang("ton/wusch.mp3", T - 0.12, { laut: 0.6 });
  }
  return { el: u, von, bis };
}

/* ---------- Szenen ---------- */
// Jede Szene: bau(s, daten) -> { el, ton, dauer, start(T) }. start(T) legt die Bewegungen an (T = Beginn der Szene in der Story).

// Titel in kurze Zeilen brechen, Bindestriche trennen mit: "Dribbel-Dreieck mit Ablage" -> DRIBBEL- / DREIECK / MIT ABLAGE
function umbrechen(text, max = 11) {
  const teile = String(text).split(/\s+/).flatMap((w) => w.split(/(?<=-)/));
  const zeilen = [];
  teile.forEach((w) => {
    const letzte = zeilen[zeilen.length - 1];
    const fuge = letzte?.endsWith("-") ? "" : " ";
    if (letzte != null && (letzte + fuge + w).length <= max) zeilen[zeilen.length - 1] = letzte + fuge + w;
    else zeilen.push(w);
  });
  return zeilen;
}
// So breit umbrechen, dass höchstens n Zeilen entstehen
function umbrechenAuf(text, n, max = 12) {
  let z = umbrechen(text, max);
  while (z.length > n && max < 60) z = umbrechen(text, ++max);
  return z;
}
// Schrift so weit verkleinern, bis das Breiteste von "teile" in maxB passt
function passeAn(node, teile, maxB, min = 60) {
  let px = parseFloat(getComputedStyle(node).fontSize);
  const breit = () => Math.max(...[...teile].map((x) => x.offsetWidth));
  while (px > min && breit() > maxB) { px -= 4; node.style.fontSize = px + "px"; }
}
function altersKurz(gruppen = []) {
  const j = gruppen.filter((g) => /-Jugend$/.test(g)).map((g) => g[0]);
  if (j.length && j.length === gruppen.length) return { gross: j.length > 1 ? j[0] + "–" + j[j.length - 1] : j[0], klein: "Jugend" };
  return gruppen.length ? { gross: gruppen[0].replace("-Jugend", ""), klein: gruppen.length > 1 ? "und älter" : "Alter" } : null;
}

// Zeilen einer Schlagzeile: "*so*" bekommt die Neon-Fläche (auf Papier alle Zeilen, wie in der App)
const titelZeilen = (zeilen, alleFlaeche) => zeilen.map((z) => {
  const stark = /^\*.*\*$/.test(z), fl = alleFlaeche || stark;
  return `<span class="z${stark ? " stark" : ""}${fl ? "" : " ohne"}">${fl ? `<i class="fl"></i>` : ""}<span class="cl"><b>${esc(z.replace(/^\*|\*$/g, ""))}</b></span></span>`;
}).join("");
// Film im Hintergrund einer Szene: läuft ab "filmAb" mit "filmTempo", bleibt am Ende stehen. Der Ton des Films läuft leise mit.
function filmHaken(node, s, daten, T, dauer) {
  const f = daten.filme[s.film];
  if (!f) return;
  const ab = s.filmAb || 0, tempo = s.filmTempo || Math.min(1, (f.dauer - ab) / dauer);
  const zeig = bildfolge(node.querySelector(".hg-film"), "film-" + s.film, f.anzahl);
  haken.push((z) => (z < T - 0.6 || z > T + dauer + 0.6 ? null : zeig((ab + Math.max(0, z - T) * tempo) * f.fps)));
  if (s.filmTon !== false && f.ton) klang(`filme/${s.film}.mp4`, T, { von: ab, dauer: Math.min(dauer, (f.dauer - ab) / tempo) * tempo, tempo, laut: s.laut ?? 0.55, ein: 0.25, aus: 0.4 });
}

const SZENEN = {
  intro: introSzene,

  // Hook: eine große Frage oder Behauptung, auf Wunsch über einem Film ("film": Name aus filme/).
  // zeilen: "*so*" = Neon-Fläche. lage: oben | mitte | unten. ton (ohne Film): dunkel | papier | neon
  hook(s, daten) {
    const mitFilm = !!(s.film && daten.filme[s.film]), tonart = mitFilm ? "dunkel" : s.ton || "dunkel";
    const node = el(`<section class="sz ${tonart} hook${mitFilm ? " mit-film" : ""}">
${mitFilm ? `<canvas class="hg-film"></canvas><i class="hg-schleier"></i><i class="hg-korn"></i>` : `<div class="raster" style="left:0;bottom:340px;width:520px;height:520px;${tonart === "dunkel" ? "--hc:#f8f4e9;opacity:.14" : ""}"></div>`}
<div class="hk-block">${s.dach ? `<div class="am-dach hk-dach"><i></i><span>${esc(s.dach)}</span></div>` : ""}
<h1 class="am-titel hk-titel">${titelZeilen(s.zeilen || ["Trainingskern"], tonart === "papier")}</h1>
${s.notiz ? `<p class="hk-notiz hand">${esc(s.notiz)}</p>` : ""}</div></section>`);
    frame.append(node);
    const titel = node.querySelector(".hk-titel"), block = node.querySelector(".hk-block");
    passeAn(titel, titel.querySelectorAll("b"), 890, 70);
    const hoehe = block.offsetHeight, lage = s.lage || "mitte";
    block.style.top = (lage === "oben" ? 400 : lage === "unten" ? GRENZE - hoehe : Math.max(380, 390 + (GRENZE - 390 - hoehe) / 2)) + "px";
    const dauer = s.dauer || 3.2;
    return { el: node, ton: tonart, dauer, start(T) {
      if (mitFilm) filmHaken(node, s, daten, T, dauer);
      const dach = node.querySelector(".hk-dach");
      if (dach) schieb(dach, T + 0.25, 0.35, -40);
      const zs = [...node.querySelectorAll(".hk-titel .z")];
      zs.forEach((z, i) => {
        const t = T + 0.3 + i * (s.takt || 0.22);
        if (z.querySelector(".fl")) an(z.querySelector(".fl"), [{ scale: "0 1" }, { scale: "1 1" }], t - 0.08, 0.3, E.rein);
        steig(z.querySelector("b"), t, 0.42);
      });
      const n = node.querySelector(".hk-notiz");
      if (n) schieb(n, T + 0.55 + zs.length * (s.takt || 0.22), 0.4, -30, 10);
    } };
  },

  // Aufmacher: große Schlagzeile auf Papier, dazu (mit code) die Eckdaten der Übung als Karten
  aufmacher(s, daten) {
    const e = s.code ? daten.einheiten[s.code] : null;
    const zeilen = s.zeilen || umbrechen(e?.title || "Trainingskern");
    const karten = [];
    if (e && s.karten !== false) {
      if (e.duration_minutes) karten.push(["", e.duration_minutes, "Minuten"]);
      if (e.players_min) karten.push(["n", e.players_max && e.players_max !== e.players_min ? `${e.players_min}–${e.players_max}` : e.players_min, "Spieler"]);
      const a = altersKurz(e.age_groups);
      if (a) karten.push(["o", a.gross, a.klein]);
      if (e.field_size) karten.push(["klein", e.field_size, "Feld"]);
    }
    const nr = e?.code ? e.code.replace(/\D/g, "") : "";
    const node = el(`<section class="sz papier">
<div class="raster" style="left:0;bottom:340px;width:520px;height:520px"></div>
${nr ? `<span class="am-nr">${esc(nr)}</span>` : ""}
<div class="am-dach"><i></i><span>${esc(s.dach || (e ? "Übung aus dem Katalog" : "Fußballtraining für Trainer"))}</span></div>
<h1 class="am-titel">${titelZeilen(zeilen, true)}</h1>
<div class="am-karten">${karten.map(([c, g, k]) => `<div class="am-karte ${c}"><b>${esc(g)}</b><span>${esc(k)}</span></div>`).join("")}</div>
${s.notiz !== false ? `<p class="am-notiz hand">${esc(s.notiz || "Erst die Skizze, dann aufs Feld ↓")}</p>` : ""}
${e?.kind || s.stempel ? `<div class="stempel am-stempel" style="right:58px;top:270px;rotate:4deg">${esc(s.stempel || e.kind)}</div>` : ""}
</section>`);
    frame.append(node);
    const titel = node.querySelector(".am-titel");
    passeAn(titel, titel.querySelectorAll("b"), 880, 90);
    const k = node.querySelector(".am-karten");
    let n = node.querySelector(".am-notiz");
    // Alles muss über der Spielminute enden (GRENZE): notfalls fällt erst die vierte Karte weg, dann die Notiz
    const setze = () => {
      k.style.top = titel.offsetTop + titel.offsetHeight + 60 + "px";
      if (n) n.style.top = k.offsetTop + k.offsetHeight + (k.children.length ? 52 : 0) + "px";
      return n ? n.offsetTop + n.offsetHeight : k.offsetTop + k.offsetHeight;
    };
    if (setze() > GRENZE && k.children.length > 3) k.lastElementChild.remove();
    if (setze() > GRENZE && n) { n.remove(); }
    return { el: node, ton: "papier", dauer: s.dauer || 3.4, start(T) {
      schieb(node.querySelector(".am-dach"), T + 0.3, 0.4, -40);
      node.querySelectorAll(".am-titel .z").forEach((z, i) => {
        an(z.querySelector(".fl"), [{ scale: "0 1" }, { scale: "1 1" }], T + 0.38 + i * 0.13, 0.4, E.rein);
        steig(z.querySelector("b"), T + 0.5 + i * 0.13, 0.5);
      });
      const t1 = T + 0.75 + zeilen.length * 0.13;
      node.querySelectorAll(".am-karte").forEach((c, i) => an(c, [{ scale: ".3", rotate: (i % 2 ? 9 : -9) + "deg", opacity: 0 }, { opacity: 1, offset: 0.3 }, { scale: "1", rotate: (i % 2 ? 1.2 : -1.4) + "deg", opacity: 1 }], t1 + i * 0.11, 0.5, E.feder));
      if (n?.isConnected) schieb(n, t1 + 0.25 + karten.length * 0.11, 0.45, -30, 12);
      const st = node.querySelector(".am-stempel");
      if (st) stempeln(st, T + 0.95);
      const zahl = node.querySelector(".am-nr");
      if (zahl) an(zahl, [{ translate: "80px 0", opacity: 0 }, { translate: "0 0", opacity: 1 }], T + 0.25, 1.2);
    } };
  },

  // Übung: der Platz aus der App, der Ablauf läuft Schritt für Schritt, darunter steht der aktuelle Schritt
  uebung(s, daten) {
    const e = daten.einheiten[s.code];
    if (!e) throw new Error("Übung " + s.code + " nicht gefunden");
    const tempo = s.tempo || 1.4, EIN = 0.95, AUS = s.nachlauf ?? 0.8;
    const fassung = s.fassung || 0, v = fassung ? e.versions?.[fassung - 1] : null;
    const titel = umbrechenAuf(s.titel || (v ? v.title : e.title), 2, 15);
    const node = el(`<section class="sz dunkel">
<div class="ub-kopf"><div class="ub-zeile"><span class="ub-code">${esc(e.code || "")}</span><span>${esc(s.dach || (v ? v.label : "So läuft’s"))}</span></div>
<h2 class="ub-titel">${titel.map((z) => `<span><b>${esc(z)}</b></span>`).join("")}</h2></div>
<div class="ub-platz"></div><div class="ub-schritte"></div><div class="ub-punkte"></div></section>`);
    frame.append(node);
    const platz = bauePlatz(node.querySelector(".ub-platz"), tafelVon(e, fassung), { schritte: s.schritte || 0, zoom: s.zoom || 1 });
    const steps = platz.play.steps, liste = node.querySelector(".ub-schritte"), punkte = node.querySelector(".ub-punkte");
    const karten = [{ nr: "▸", tx: s.vorab || "Aufstellung" }, ...steps.map((st, i) => ({ nr: i + 1, tx: st.label }))].map(({ nr, tx }) => {
      const c = el(`<div class="ub-schritt"><span class="nr">${esc(nr)}</span><span class="tx">${esc(tx)}</span></div>`);
      liste.append(c);
      return c;
    });
    punkte.innerHTML = steps.map(() => "<i></i>").join("");
    const t = node.querySelector(".ub-titel");
    passeAn(t, t.querySelectorAll("b"), 930, 56);
    const dauer = EIN + platz.dauer / tempo + AUS;
    return { el: node, ton: "dunkel", dauer, start(T) {
      schieb(node.querySelector(".ub-zeile"), T + 0.3, 0.4, -40);
      t.querySelectorAll("b").forEach((b, i) => steig(b, T + 0.4 + i * 0.1, 0.5));
      blende(node.querySelector(".ub-platz"), T + 0.2, 0.5);
      karten.forEach((c, i) => an(c, [{ translate: "0 26px", opacity: 0 }, { translate: "0 0", opacity: 1 }], i === 0 ? T + 0.55 : T + EIN + steps[i - 1].t0 / tempo, 0.28));
      let gezeigt = -9;
      haken.push((zeit) => {
        const tl = zeit - T;
        if (tl < -0.5 || tl > dauer + 0.6) return;
        const auf = smooth(clamp01((tl - 0.35) / 0.6));
        const cur = platz.zeichne((tl - EIN) * tempo, auf, clamp01(tl / dauer));
        if (cur !== gezeigt) {
          gezeigt = cur;
          karten.forEach((c, i) => { c.style.display = i === cur + 1 ? "grid" : "none"; });
          [...punkte.children].forEach((p, i) => p.classList.toggle("an", i <= cur));
        }
      });
    } };
  },

  // Punkte: zwei bis vier kurze Sätze als Karten (ohne "punkte" die Coaching-Punkte der Übung)
  punkte(s, daten) {
    const e = s.code ? daten.einheiten[s.code] : null;
    const punkte = (s.punkte || e?.coaching_points || []).slice(0, s.max || 3);
    const titel = s.titel ? [].concat(s.titel) : ["Darauf", "achtest du"];
    const tonart = s.ton || "neon";
    const node = el(`<section class="sz ${tonart}${s.streichen ? " pk-streichen" : ""}">
<div class="raster" style="right:0;top:250px;width:560px;height:560px;--hx:100%;--hy:0%;${tonart === "dunkel" ? "--hc:#f8f4e9;opacity:.14" : ""}"></div>
<h2 class="pk-titel">${titel.map((z) => `<span><b>${esc(z)}</b></span>`).join("")}</h2><i class="pk-strich"></i>
<div class="pk-liste">${punkte.map((p, i) => `<div class="pk-karte"><span class="nr">${s.streichen ? "✕" : i + 1}</span><span class="tx"><span>${esc(p)}<i class="pk-linie"></i></span></span></div>`).join("")}</div></section>`);
    frame.append(node);
    const t = node.querySelector(".pk-titel"), strich = node.querySelector(".pk-strich"), liste = node.querySelector(".pk-liste");
    passeAn(t, t.querySelectorAll("b"), 930, 70);
    strich.style.top = t.offsetTop + t.offsetHeight + 14 + "px";
    strich.style.width = Math.min(936, t.querySelector("span:last-child b").offsetWidth) + "px";
    liste.style.top = t.offsetTop + t.offsetHeight + 96 + "px";
    const takt = s.takt || (s.streichen ? 0.55 : 0.75);
    return { el: node, ton: tonart, dauer: s.dauer || 1.5 + punkte.length * (takt + 0.25) + 0.6, start(T) {
      t.querySelectorAll("b").forEach((b, i) => steig(b, T + 0.3 + i * 0.1, 0.5));
      an(strich, [{ scale: "0 1" }, { scale: "1 1" }], T + 0.6, 0.4, E.rein);
      node.querySelectorAll(".pk-karte").forEach((c, i) => {
        an(c, [{ translate: "140px 0", opacity: 0, rotate: "3deg" }, { translate: "0 0", opacity: 1, rotate: [-1.2, 0.9, -0.7, 1][i % 4] + "deg" }], T + 0.85 + i * takt, 0.5);
        an(c.querySelector(".nr"), [{ scale: "0" }, { scale: "1" }], T + 1.05 + i * takt, 0.4, E.stark);
        if (s.streichen) an(c.querySelector(".pk-linie"), [{ scale: "0 1" }, { scale: "1 1" }], T + 1.2 + i * takt, 0.28, E.rein);
      });
    } };
  },

  // App: die echte Seite der App, im Handy gescrollt. Die Bilder nimmt render.mjs vorher von der veröffentlichten App auf.
  app(s, daten, i) {
    const aufnahme = daten.aufnahmen[i];
    const node = el(`<section class="sz papier">
<div class="raster" style="left:0;bottom:340px;width:480px;height:480px"></div>
<p class="app-notiz hand">${esc(s.notiz || "So sieht’s in der App aus ↓")}</p>
<div class="app-handy"><i class="schatten"></i><div class="rahmen"><canvas></canvas></div></div>
${s.stempel !== false ? `<div class="stempel app-stempel" style="rotate:7deg">${esc(s.stempel || "Echte App")}</div>` : ""}
${s.zettel ? `<div class="app-seite">${esc(s.zettel)}</div>` : ""}</section>`);
    frame.append(node);
    const cv = node.querySelector("canvas"), handy = node.querySelector(".app-handy");
    const dauer = s.dauer || 5;
    return { el: node, ton: "papier", dauer, start(T) {
      schieb(node.querySelector(".app-notiz"), T + 0.3, 0.45, -40);
      an(handy, [{ translate: "0 900px", rotate: "7deg" }, { translate: "0 0", rotate: "-2deg" }], T + 0.15, 0.75, "cubic-bezier(.2,1.1,.3,1)");
      const st = node.querySelector(".app-stempel");
      if (st) stempeln(st, T + 1.0);
      const z = node.querySelector(".app-seite");
      if (z) schieb(z, T + 1.3, 0.4, -50);
      if (aufnahme) {
        const zeig = bildfolge(cv, aufnahme.ordner, aufnahme.anzahl);
        haken.push((zeit) => (zeit < T - 0.6 || zeit > T + dauer + 0.6 ? null : zeig((zeit - T) * aufnahme.fps + 0.001)));
      }
    } };
  },

  // Abpfiff: Logo, Schlusssatz ("*so*" = Neon), Aufruf und Adresse. zahl: eine große Zahl davor (nur auf Wunsch)
  abpfiff(s, daten) {
    const zahl = s.zahl ? String(s.zahl) : "";
    const zeilen = s.zeilen || ["Jede Übung.", "*Animiert*", "*erklärt.*"];
    const node = el(`<section class="sz dunkel">
<div class="raster" style="right:0;top:250px;width:560px;height:560px;--hx:100%;--hy:0%;--hc:#f8f4e9;opacity:.16"></div>
${kBox("ab-k")}
${zahl ? `<p class="ab-zahl">${esc(zahl)}</p>` : ""}
<p class="ab-zeilen${zahl ? "" : " gross"}">${zeilen.map((z) => `<span${/^\*.*\*$/.test(z) ? ` class="stark"` : ""}><b>${esc(z.replace(/^\*|\*$/g, ""))}</b></span>`).join("")}</p>
<div class="ab-knopf"><span>${esc(s.knopf || "Kostenlos ansehen")}</span><i>→</i></div>
<p class="ab-adresse">${esc(s.adresse || "trainingskern.de")}</p>
${s.notiz !== false ? `<p class="ab-notiz hand">${esc(s.notiz || "Link in der Bio")}</p>` : ""}</section>`);
    frame.append(node);
    const z = node.querySelector(".ab-zahl"), zl = node.querySelector(".ab-zeilen"), kn = node.querySelector(".ab-knopf"), ad = node.querySelector(".ab-adresse"), no = node.querySelector(".ab-notiz");
    passeAn(zl, zl.querySelectorAll("b"), 930, 60);
    zl.style.top = (z ? z.offsetTop + z.offsetHeight + 34 : 672) + "px";
    kn.style.top = zl.offsetTop + zl.offsetHeight + 54 + "px";
    ad.style.top = kn.offsetTop + kn.offsetHeight + 40 + "px";
    if (no) no.style.top = ad.offsetTop + ad.offsetHeight + 26 + "px";
    return { el: node, ton: "dunkel", dauer: s.dauer || 3.8, ohneMarke: true, start(T) {
      const k = node.querySelector(".ab-k");
      an(k, [{ scale: ".4", rotate: "-18deg", opacity: 0 }, { scale: "1", rotate: "0deg", opacity: 1 }], T + 0.3, 0.55, E.feder);
      an(k.querySelector(".k-core"), [{ transform: "scale(1)" }, { transform: "scale(1.5)", offset: 0.5 }, { transform: "scale(1)" }], T + 0.8, 0.45, E.gerade);
      if (z) an(z, [{ translate: "-120px 0", opacity: 0 }, { translate: "0 0", opacity: 1 }], T + 0.45, 0.55);
      zl.querySelectorAll("b").forEach((b, i) => steig(b, T + 0.7 + i * 0.12, 0.5));
      an(kn, [{ scale: ".6", opacity: 0 }, { scale: "1", opacity: 1 }], T + 1.2, 0.45, E.feder);
      an(kn, [{ scale: "1" }, { scale: "1.045" }, { scale: "1" }], T + 2.0, 0.5, E.weich, "none");
      an(kn, [{ scale: "1" }, { scale: "1.045" }, { scale: "1" }], T + 2.8, 0.5, E.weich, "none");
      blende(ad, T + 1.5, 0.35);
      if (no) schieb(no, T + 1.75, 0.45, -30, 10);
    } };
  },
};

/* ---------- Story zusammensetzen ---------- */
async function lade(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(url + " -> " + r.status);
  return r.json();
}

async function baue() {
  const datei = q.get("story") || "stories/ue-001.json";
  const story = await lade("/" + datei);
  const kennung = datei.split("/").pop().replace(/\.json$/, "");
  // Das Intro steht von selbst vorn. "intro": false lässt es weg, "intro": { "film": "..." } nimmt einen Film.
  const plan = [...(story.intro === false ? [] : [{ typ: "intro", ...(typeof story.intro === "object" ? story.intro : {}) }]), ...story.szenen.map((s, i) => ({ ...s, nr: i }))];
  const artVon = (s) => s.uebergang || story.uebergang || "anstoss";
  const codes = [...new Set(plan.map((s) => s.code).filter(Boolean))];
  const filmNamen = [...new Set([...plan.map((s) => s.film), ...plan.map((s) => ({ marker: "wischer-marker", staub: "wischer-staub" }[artVon(s)]))].filter(Boolean))];
  const daten = await lade(`/api/daten?codes=${encodeURIComponent(codes.join(","))}&filme=${encodeURIComponent(filmNamen.join(","))}`);
  daten.aufnahmen = {};
  await Promise.all(plan.map(async (s) => {
    if (s.typ !== "app") return;
    try { const info = await lade(`/cache/${kennung}-${s.nr}/info.json`); daten.aufnahmen[s.nr] = { ...info, ordner: `${kennung}-${s.nr}` }; }
    catch { daten.aufnahmen[s.nr] = null; } // ohne Aufnahme bleibt das Handy leer
  }));
  await document.fonts.ready;
  await Promise.all(["900 80px Archivo", "800 40px Archivo", "italic 900 80px Archivo", "400 40px 'Permanent Marker'", "600 40px 'Space Grotesk'", "400 40px 'Special Elite'"].map((f) => document.fonts.load(f, "Übung 123")));

  frame.classList.add("misst");
  // Erst alle Szenen bauen (sichtbar, damit Texte gemessen werden können), dann die Zeiten vergeben
  const szenen = plan.map((s) => {
    const bauer = SZENEN[s.typ];
    if (!bauer) throw new Error("Unbekannte Szene: " + s.typ);
    const sz = bauer(s, daten, s.nr); // hängt die Szene selbst an; solange #frame "misst" trägt, ist sie zum Messen sichtbar
    sz.roh = s;
    return sz;
  });
  let t = 0;
  const schnitte = [];
  szenen.forEach((sz, i) => {
    sz.t0 = t; sz.t1 = t + sz.dauer; t = sz.t1;
    if (i > 0) schnitte.push(baueUebergang(artVon(sz.roh), sz.t0, !!szenen[i - 1].intro, daten));
    sz.start(sz.t0);
  });
  const dauer = t;

  // Feste Teile: Marke oben links, Spielminute unten (der Ball rollt über alle Szenen außer dem Intro von 0′ bis 90′)
  const marke = el(`<div class="marke">${kBox("", true)}<span>Trainingskern<i></i></span></div>`);
  const uhr = el(`<div class="uhr"><i class="weg"></i><span class="min">0′</span><span class="ball">${ballSvg()}</span></div>`);
  const zonen = [el(`<div class="zone" style="top:0;height:250px"></div>`), el(`<div class="zone" style="bottom:0;height:340px"></div>`)];
  frame.append(marke, uhr, ...zonen);
  const weg = uhr.querySelector(".weg"), min = uhr.querySelector(".min"), ball = uhr.querySelector(".ball");
  const spiel = szenen.filter((x) => !x.ohneUhr), spielzeit = spiel.reduce((a, x) => a + x.dauer, 0);

  function seek(zeit) {
    const z = Math.max(0, Math.min(dauer, zeit));
    const sz = szenen.find((x) => z >= x.t0 && z < x.t1) || szenen[szenen.length - 1]; // die letzte Szene bleibt stehen
    szenen.forEach((x) => { x.el.style.display = x === sz ? "block" : "none"; });
    schnitte.forEach((u) => { u.el.style.display = z >= u.von && z <= u.bis ? "block" : "none"; });
    const dunkel = sz.ton === "dunkel";
    marke.style.display = sz.ohneMarke ? "none" : "flex";
    marke.classList.toggle("dunkel", dunkel);
    uhr.style.display = sz.ohneUhr ? "none" : "block";
    uhr.classList.toggle("dunkel", dunkel);
    const p = clamp01(spiel.reduce((a, x) => a + Math.max(0, Math.min(x.dauer, z - x.t0)), 0) / Math.max(0.1, spielzeit - 0.6));
    weg.style.width = (p * 100).toFixed(2) + "%";
    ball.style.left = (p * 100).toFixed(2) + "%";
    ball.style.rotate = (p * 1440).toFixed(1) + "deg";
    min.style.left = Math.max(4, Math.min(96, p * 100)).toFixed(2) + "%";
    min.textContent = Math.round(p * 90) + "′";
    anims.forEach((a) => { a.currentTime = z * 1000; });
    // Manche Haken laden ein Bild nach: seek() ist erst fertig, wenn alle gemalt sind
    return Promise.all(haken.map((h) => h(z)).filter(Boolean)).then(() => undefined);
  }
  frame.classList.remove("misst");
  await seek(0);
  return { dauer, fps: story.fps || 30, titel: story.titel || kennung, kennung, seek, ton, szenen: szenen.map((s) => ({ typ: s.roh.typ, t0: s.t0, t1: s.t1 })) };
}

/* ---------- Vorschau: Pult mit Regler ---------- */
function pult(st) {
  const p = document.getElementById("pult"), regler = p.querySelector("input[type=range]"), knopf = p.querySelector("button"), anzeige = p.querySelector("output");
  regler.max = st.dauer; regler.step = 1 / st.fps;
  let laeuft = false, t = Number(q.get("t") || 0), zuletzt = 0;
  const zeig = () => { st.seek(t); regler.value = t; anzeige.textContent = t.toFixed(2) + " / " + st.dauer.toFixed(2) + " s"; };
  const tick = (jetzt) => { if (!laeuft) return; t += (jetzt - zuletzt) / 1000; zuletzt = jetzt; if (t >= st.dauer) { t = 0; } zeig(); requestAnimationFrame(tick); };
  knopf.onclick = () => { laeuft = !laeuft; knopf.textContent = laeuft ? "Pause" : "Abspielen"; zuletzt = performance.now(); if (laeuft) requestAnimationFrame(tick); };
  regler.oninput = () => { t = Number(regler.value); zeig(); };
  p.querySelector("input[type=checkbox]").onchange = (e) => frame.classList.toggle("zonen", e.target.checked);
  const passe = () => { const s = Math.min(innerWidth / W, (innerHeight - 64) / H); const b = document.getElementById("buehne"); b.style.transform = `scale(${s})`; b.style.left = (innerWidth - W * s) / 2 + "px"; };
  addEventListener("resize", passe); passe(); zeig();
}

if (RENDER) document.body.classList.add("render");
window.__story = { bereit: baue().then((st) => { Object.assign(window.__story, st); if (!RENDER) pult(st); return { dauer: st.dauer, fps: st.fps, kennung: st.kennung, szenen: st.szenen, ton: st.ton }; }) };
window.__story.bereit.catch((err) => { document.body.insertAdjacentHTML("beforeend", `<pre style="position:fixed;inset:20px;color:#ff5500;font:16px monospace;z-index:999">${esc(err.stack || err)}</pre>`); });
