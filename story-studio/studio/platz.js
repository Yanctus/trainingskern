// Der Platz aus der App (LivePitch.jsx, Stage.jsx, Sketch.jsx) ohne React: dieselben Tafel-Daten, dasselbe Markup,
// dieselben Klassen. Das Aussehen kommt aus app/zine.css und app/einheit.css (Kopien aus der App).
// Anders als in der App läuft hier keine Uhr mit: zeichne(t) stellt den Platz auf eine Zeit, damit jedes Bild
// des Videos genau berechnet werden kann.
import { K, buildPlay, mergeBoard, positionAt, stepAt, withCoach } from "./app/playbook.js";

const TILT = 47; // Blickwinkel: etwas steiler als in der App (52), damit der Platz im Hochformat höher wird
const k = (v) => (v * K).toFixed(1);
const clamp01 = (v) => Math.max(0, Math.min(1, v));
const smooth = (p) => p * p * (3 - 2 * p);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const ARROW_HEAD = "M7,0 L-19,-12 L-19,12 Z";
const TOR_MASS = { mini: { w: 4, d: 3.2 }, jugend: { w: 7, d: 4.5 }, gross: { w: 10, d: 5.5 } };

/* ---------- Figuren und Material (Stage.jsx) ---------- */
const figur = (label) => `<svg viewBox="0 0 60 100"><g class="cut"><circle cx="30" cy="15" r="10"/>
<path d="M19,28 Q30,33 41,28 L51,40 L44,46 L42,43 V72 H39 V90 H45 V96 H15 V90 H21 V72 H18 V43 L16,46 L9,40 Z"/></g>
<path class="leg" d="M21,70 h7 v21 h-7 z M32,70 h7 v21 h-7 z"/><path class="shoe" d="M16,90 h13 v6 h-13 z M31,90 h13 v6 h-13 z"/>
<path class="short" d="M18,57 h24 v16 h-10 l-2,-7 l-2,7 h-10 z"/>
<path class="bib" d="M19,28 Q30,33 41,28 L51,40 L44,46 L42,43 V60 H18 V43 L16,46 L9,40 Z"/><circle class="head" cx="30" cy="15" r="10"/>
${label ? `<text x="30" y="53">${esc(label)}</text>` : ""}</svg>`;
const KEGEL = `<svg viewBox="0 0 34 40"><path class="cut" d="M4,34 H30 V39 H4 Z M10,34 L15,5 Q17,2 19,5 L24,34 Z"/>
<path class="cone" d="M10,34 L15,5 Q17,2 19,5 L24,34 Z"/><path class="band" d="M12.6,19 H21.4 L22.4,25 H11.6 Z"/><path class="cone" d="M4,34 H30 V39 H4 Z"/></svg>`;
const STANGE = `<svg viewBox="0 0 22 64"><path class="cut" d="M2,57 Q2,54 11,54 Q20,54 20,57 Q20,61 11,61 Q2,61 2,57 Z M7.5,4 Q11,1 14.5,4 V56 H7.5 Z"/>
<path class="cone" d="M2,57 Q2,54 11,54 Q20,54 20,57 Q20,61 11,61 Q2,61 2,57 Z"/><path class="cone" d="M7.5,4 Q11,1 14.5,4 V56 H7.5 Z"/>
<path class="band" d="M7.5,16 H14.5 V22 H7.5 Z M7.5,34 H14.5 V40 H7.5 Z"/></svg>`;
const HUERDE = `<svg viewBox="0 0 60 36"><path class="cut" d="M4,30 H20 V35 H4 Z M40,30 H56 V35 H40 Z M9,8 H15 V31 H9 Z M45,8 H51 V31 H45 Z M5,6 Q5,3 8,3 H52 Q55,3 55,6 V11 Q55,13 52,13 H8 Q5,13 5,11 Z"/>
<path class="cone" d="M9,8 H15 V31 H9 Z M45,8 H51 V31 H45 Z"/><path class="cone" d="M4,30 H20 V35 H4 Z M40,30 H56 V35 H40 Z"/>
<path class="cone" d="M5,6 Q5,3 8,3 H52 Q55,3 55,6 V11 Q55,13 52,13 H8 Q5,13 5,11 Z"/><path class="band" d="M18,4.5 H25 V11.5 H18 Z M35,4.5 H42 V11.5 H35 Z"/></svg>`;
const TOR3 = `<i class="t3 t3-rueck"></i><i class="t3 t3-seite links"></i><i class="t3 t3-seite rechts"></i><i class="t3 t3-dach"></i><i class="t3 t3-front"></i>`;
const LEITER = `<svg viewBox="0 0 160 54"><path class="cone" d="M14,8 h7 v38 h-7 Z M46,8 h7 v38 h-7 Z M77,8 h7 v38 h-7 Z M108,8 h7 v38 h-7 Z M139,8 h7 v38 h-7 Z"/>
<path class="cone" d="M2,2 H158 V10 H2 Z M2,44 H158 V52 H2 Z"/><path class="band" d="M30,3.5 H38 V8.5 H30 Z M122,3.5 H130 V8.5 H122 Z M30,45.5 H38 V50.5 H30 Z M122,45.5 H130 V50.5 H122 Z"/></svg>`;
const REIFEN = `<svg viewBox="0 0 48 48"><path class="cone" fill-rule="evenodd" d="M1,24 a23,23 0 1,0 46,0 a23,23 0 1,0 -46,0 Z M9,24 a15,15 0 1,0 30,0 a15,15 0 1,0 -30,0 Z"/></svg>`;
const BALL = `<svg viewBox="0 0 24 24"><circle class="ball" cx="12" cy="12" r="10"/><path class="dot" d="M12,7.5 L16,10.5 L14.5,15.5 H9.5 L8,10.5 Z"/></svg>`;

const istHuerde = (c) => c?.shape === "huerde" || c?.shape === "huerde_ou";
const istLeiter = (c) => c?.shape === "leiter" || c?.shape === "leiter_ou";
const marke = (c) => (c?.shape === "tor" ? TOR3 : c?.shape === "stange" ? STANGE : istHuerde(c) ? HUERDE : istLeiter(c) ? LEITER : c?.shape === "ring" ? REIFEN : KEGEL);
const markenKlasse = (c) => (c.shape === "tor"
  ? "tok cone goal " + (c.side || "top") + (c.size === "jugend" || c.size === "gross" ? " " + c.size : "")
  : "tok cone" + (c.color === "neon" ? " neon" : "") + (c.shape === "stange" ? " pole" : "") + (istHuerde(c) ? " hurdle" : "")
    + (istLeiter(c) ? " flat ladder" + (c.shape === "leiter_ou" ? " ou" : "") : "") + (c.shape === "ring" ? " flat reifen" : ""));

/* ---------- Linien, Tore, Maße (Sketch.jsx) ---------- */
function linie(l) {
  const cls = "l" + (l.dashed ? " dash" : "");
  if (l.type === "zone") return l.w ? `<rect class="z${l.color === "orange" ? " o" : ""}" x="${k(l.x)}" y="${k(l.y)}" width="${k(l.w)}" height="${k(l.h)}"/>` : "";
  if (l.type === "rect") return l.w ? `<rect class="${cls}" x="${k(l.x)}" y="${k(l.y)}" width="${k(l.w)}" height="${k(l.h)}"/>` : "";
  if (l.type === "circle") return l.r ? `<circle class="${cls}" cx="${k(l.x)}" cy="${k(l.y)}" r="${k(l.r)}"/>` : "";
  return l.x1 == null ? "" : `<path class="${cls}" d="M${k(l.x1)},${k(l.y1)} L${k(l.x2)},${k(l.y2)}"/>`;
}
function torPfad(g) {
  const { w: tw, d: td } = TOR_MASS[g.size] || TOR_MASS.mini, x = g.x * K, y = g.y * K, w = tw * K, d = td * K;
  if (g.side === "left") return `M${x},${y - w} h${-d} v${2 * w} h${d}`;
  if (g.side === "right") return `M${x},${y - w} h${d} v${2 * w} h${-d}`;
  if (g.side === "top") return `M${x - w},${y} v${-d} h${2 * w} v${d}`;
  return `M${x - w},${y} v${d} h${2 * w} v${-d}`;
}
function tor(g) {
  const { w: tw, d: td } = TOR_MASS[g.size] || TOR_MASS.mini, x = g.x * K, y = g.y * K, w = tw * K, d = td * K;
  const quer = g.side === "left" || g.side === "right", dir = g.side === "left" || g.side === "top" ? -1 : 1;
  const rx = quer ? (dir < 0 ? x - d : x) : x - w, ry = quer ? y - w : dir < 0 ? y - d : y, rw = quer ? d : 2 * w, rh = quer ? 2 * w : d;
  const netz = [], step = 0.9 * K, p = 0.9 * K;
  for (let a = rx + step; a < rx + rw - 1; a += step) netz.push(`M${a.toFixed(1)},${ry.toFixed(1)} v${rh.toFixed(1)}`);
  for (let b = ry + step; b < ry + rh - 1; b += step) netz.push(`M${rx.toFixed(1)},${b.toFixed(1)} h${rw.toFixed(1)}`);
  const pf = quer ? [[x - p / 2, y - w - p / 2], [x - p / 2, y + w - p / 2]] : [[x - w - p / 2, y - p / 2], [x + w - p / 2, y - p / 2]];
  return `<g class="tor${g.size === "jugend" || g.size === "gross" ? " " + g.size : ""}"><rect class="tor-flaeche" x="${rx.toFixed(1)}" y="${ry.toFixed(1)}" width="${rw.toFixed(1)}" height="${rh.toFixed(1)}"/>
<path class="tor-netz" d="${netz.join(" ")}"/><path class="g" d="${torPfad(g)}"/>${pf.map(([px, py]) => `<rect class="tor-pfosten" x="${px.toFixed(1)}" y="${py.toFixed(1)}" width="${p}" height="${p}"/>`).join("")}</g>`;
}
function mass(m) {
  const x1 = m.x1 * K, y1 = m.y1 * K, x2 = m.x2 * K, y2 = m.y2 * K;
  const len = Math.hypot(x2 - x1, y2 - y1) || 1, nx = (-(y2 - y1) / len) * 13, ny = ((x2 - x1) / len) * 13;
  return `<g class="dim"><path d="M${x1.toFixed(1)},${y1.toFixed(1)} L${x2.toFixed(1)},${y2.toFixed(1)}"/>
<path class="tick" d="M${(x1 - nx).toFixed(1)},${(y1 - ny).toFixed(1)} L${(x1 + nx).toFixed(1)},${(y1 + ny).toFixed(1)} M${(x2 - nx).toFixed(1)},${(y2 - ny).toFixed(1)} L${(x2 + nx).toFixed(1)},${(y2 + ny).toFixed(1)}"/>
<text x="${((x1 + x2) / 2).toFixed(1)}" y="${((y1 + y2) / 2 + 9).toFixed(1)}">${esc(m.text)}</text></g>`;
}

// Die Tafel einer Fassung: 0 = Grundform, 1.. = weitere Fassungen (Coaching-Punkt, Steigerung)
export function tafelVon(einheit, fassung = 0) {
  const v = fassung > 0 ? einheit.versions?.[fassung - 1] : null;
  return withCoach(v ? mergeBoard(einheit.board, v.board) : einheit.board);
}

// Baut den Platz in "ziel" (ein Element mit fester Größe). schritte begrenzt den Ablauf auf die ersten N Schritte.
// Gibt zurück: play (Zeitleiste), dauer (Sekunden Spielzeit), zeichne(t, auf) mit auf = 0..1 (Figuren klappen hoch)
export function bauePlatz(ziel, board, { schritte = 0, zoom = 1 } = {}) {
  const b = schritte > 0 && board.steps?.length > schritte ? { ...board, steps: board.steps.slice(0, schritte) } : board;
  const play = buildPlay(b);
  ziel.innerHTML = `<div class="scene"><div class="plane">
<svg class="plane-turf" viewBox="0 0 1000 600">
<g class="plane-rand"><rect class="r" x="-30" y="-30" width="1060" height="700"/>${[1, 3, 5].map((i) => `<rect class="s" x="${(i * 1000) / 6}" y="-30" width="${1000 / 6}" height="700"/>`).join("")}</g>
<g data-eb="lines">${(b.lines || []).map(linie).join("")}${(b.goals || []).map(tor).join("")}${(b.dims || []).map(mass).join("")}</g>
${play.arrows.map((a) => `<g data-ar data-eb="arrows" class="ar ${a.type}${a.join ? " join" : ""}" style="visibility:hidden"><path class="d" pathLength="1" d="${a.d}"/><path class="ah" transform="translate(${a.head.x.toFixed(1)} ${a.head.y.toFixed(1)}) rotate(${a.head.angle.toFixed(1)})" d="${ARROW_HEAD}"/></g>`).join("")}
</svg><div class="plane-lights"></div>
${(b.goals || []).map((g) => { const t = { x: g.x, y: g.y, shape: "tor", side: g.side, size: g.size }; return `<div data-cone data-eb="lines" class="${markenKlasse(t)}" style="transform:translate3d(${k(g.x)}px,${k(g.y)}px,0)"><div class="up">${marke(t)}</div></div>`; }).join("")}
${(b.cones || []).map((c, i) => (play.ids.cones[i]
    ? `<div data-tk="${esc(play.ids.cones[i])}" data-eb="cones" class="${markenKlasse(c)}"><div class="up">${marke(c)}</div></div>`
    : `<div data-cone data-eb="cones" class="${markenKlasse(c)}" style="transform:translate3d(${k(c.x)}px,${k(c.y)}px,0)"><div class="up">${marke(c)}</div></div>`)).join("")}
${(b.balls || []).map((_, i) => `<div data-tk="${esc(play.ids.balls[i])}" data-eb="balls" class="tok ball"><i class="disc"></i><div class="up">${BALL}</div></div>`).join("")}
${(b.players || []).map((p, i) => `<div data-tk="${esc(play.ids.players[i])}" data-eb="players:${p.team || "t"}" class="tok fig t-${p.team || "t"}"><i class="disc"></i><div class="up">${figur(p.label)}</div></div>`).join("")}
</div></div>`;
  const box = ziel.querySelector(".scene"), plane = ziel.querySelector(".plane");
  box.style.setProperty("--night", "1");
  const tokens = [...ziel.querySelectorAll("[data-tk]")].map((node) => ({ node, track: play.tracks[node.dataset.tk] }));
  const cones = [...ziel.querySelectorAll("[data-cone]")], arrows = [...ziel.querySelectorAll("[data-ar]")];
  const w = ziel.clientWidth, h = ziel.clientHeight;
  // Ausschnitt: alles, was auf der Tafel liegt oder angelaufen wird, plus Rand. Darauf wird gezoomt (der Rasen darf über den Bildrand laufen).
  const xs = [], ys = [];
  const p = (x, y) => { if (Number.isFinite(x) && Number.isFinite(y)) { xs.push(x); ys.push(y); } };
  [...(b.players || []), ...(b.balls || []), ...(b.cones || []), ...(b.goals || [])].forEach((o) => p(o.x, o.y));
  (b.lines || []).forEach((l) => { if (l.type === "circle") { p(l.x - l.r, l.y - l.r); p(l.x + l.r, l.y + l.r); } else if (l.w) { p(l.x, l.y); p(l.x + l.w, l.y + l.h); } else { p(l.x1, l.y1); p(l.x2, l.y2); } });
  (b.dims || []).forEach((m) => { p(m.x1, m.y1); p(m.x2, m.y2); });
  (b.steps || []).forEach((st) => (st.moves || []).forEach((m) => { if (m.to) p(m.to[0], m.to[1]); }));
  const x0 = Math.min(...xs, 50) - 9, x1 = Math.max(...xs, 50) + 9, y0 = Math.min(...ys, 30) - 16, y1 = Math.max(...ys, 30) + 7;
  const cos = Math.cos((TILT * Math.PI) / 180);
  // 0.93: Luft für die Perspektive (vorn am Bildrand wird der Platz breiter)
  const s0 = Math.max(0.8, Math.min((w * 0.93) / ((x1 - x0) * K), (h * 0.96) / ((y1 - y0) * K * cos + 60), 1.7));
  const dx = (50 - (x0 + x1) / 2) * K, dy = (30 - (y0 + y1) / 2) * K;

  // t: Spielzeit in Sekunden · auf: 0..1 · fahrt: 0..1, langsame Kamerafahrt über die ganze Szene
  function zeichne(t, auf = 1, fahrt = 0) {
    const now = Math.max(0, Math.min(play.total, t));
    const s = s0 * zoom * (0.94 + 0.06 * smooth(clamp01(fahrt)));
    plane.style.transform = `translate(-50%,-50%) translateY(4%) scale(${s.toFixed(4)}) rotateX(${TILT}deg) rotateZ(${(-1.2 + 2.4 * fahrt).toFixed(3)}deg) translate(${dx.toFixed(1)}px,${dy.toFixed(1)}px)`;
    const set = (node) => { node.style.setProperty("--up", auf.toFixed(3)); node.style.opacity = auf > 0.01 ? 1 : 0; };
    tokens.forEach(({ node, track }) => {
      const p = positionAt(track, now);
      node.style.transform = `translate3d(${(p[0] * K).toFixed(1)}px,${(p[1] * K).toFixed(1)}px,0)`;
      set(node);
    });
    cones.forEach(set);
    const cur = stepAt(play, now);
    arrows.forEach((node, n) => {
      const a = play.arrows[n], p = clamp01((now - a.t0) / (a.t1 - a.t0));
      node.style.visibility = p > 0 && auf > 0.5 ? "visible" : "hidden";
      node.style.opacity = a.step === cur ? 1 : a.step === cur - 1 ? 0.3 : 0;
      node.firstChild.style.strokeDashoffset = 1 - p;
      node.lastChild.style.opacity = p >= 1 ? 1 : 0;
    });
    return cur;
  }
  // Aufbau: Die Tafel steht auf Anfang, sichtbar ist nur, was "werte" freigibt (0..1 je Ebene:
  // lines, cones, balls, arrows, players:<Team>). Figuren und Material klappen hoch, Pfeile zeichnen sich ein.
  const mitEbene = [...ziel.querySelectorAll("[data-eb]")];
  function zeichneAufbau(werte, fahrt = 0) {
    zeichne(0, 1, fahrt);
    mitEbene.forEach((node) => {
      const a = clamp01(werte[node.dataset.eb] ?? 0);
      if (node.dataset.ar != null) {
        node.style.visibility = a > 0 ? "visible" : "hidden";
        node.style.opacity = 0.9;
        node.firstChild.style.strokeDashoffset = 1 - a;
        node.lastChild.style.opacity = a >= 1 ? 1 : 0;
      } else if (node.tagName.toLowerCase() === "g") node.style.opacity = a;
      else { node.style.setProperty("--up", smooth(a).toFixed(3)); node.style.opacity = a > 0.01 ? 1 : 0; }
    });
  }
  const teams = [...new Set((b.players || []).map((p) => p.team || "t"))];
  return { play, dauer: play.total, zeichne, zeichneAufbau, teams };
}
