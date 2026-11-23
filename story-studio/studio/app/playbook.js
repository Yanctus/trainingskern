import { fluss, sprechtext } from "./sprechtext.js";
// Spielzug-Rechner: macht aus Tafel-Daten (Raster 100 x 60) eine Zeitleiste.
// Jede Position ist eine reine Funktion der Zeit, damit man vor- und zurückspulen kann.

export const K = 10; // Raster -> SVG-Einheiten (viewBox 1000 x 600)

const LEAD = 0.5, GAP = 0.45, TAIL = 0.4;
const smooth = (p) => p * p * (3 - 2 * p);
const out = (p) => 1 - (1 - p) * (1 - p);
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
// Beim Dribbeln liegt der Ball in Laufrichtung vor dem Fuß, aber immer auch ein Stück zur Kamera hin (größeres y).
// So verdeckt ihn auf dem Feld weder die Figur noch ein Hütchen, wenn er abgelegt wird.
const ahead = (from, to) => {
  const d = dist(from, to) || 1, ux = (to[0] - from[0]) / d, uy = (to[1] - from[1]) / d;
  return [to[0] + ux * 2.2, to[1] + Math.max(uy * 2.2, 0) + 1.5];
};

function control(from, to, bend = 0) {
  const dx = to[0] - from[0], dy = to[1] - from[1], len = Math.hypot(dx, dy) || 1;
  return [(from[0] + to[0]) / 2 - (dy / len) * bend, (from[1] + to[1]) / 2 + (dx / len) * bend];
}

function bezier(a, c, b, p) {
  const q = 1 - p;
  return [q * q * a[0] + 2 * q * p * c[0] + p * p * b[0], q * q * a[1] + 2 * q * p * c[1] + p * p * b[1]];
}

const pt = (p) => (p[0] * K).toFixed(1) + "," + (p[1] * K).toFixed(1);

// Pass und Lauf sind Bögen, das Dribbling eine Schlangenlinie entlang des Bogens
function pathFor(a, c, b, type) {
  if (type !== "dribbling") return `M${pt(a)} Q${pt(c)} ${pt(b)}`;
  const len = dist(a, b), n = Math.max(16, Math.round(len * 2.4)), waves = Math.max(2, Math.round(len / 4));
  let d = "";
  for (let i = 0; i <= n; i++) {
    const p = i / n, [x, y] = bezier(a, c, b, p);
    const tx = 2 * (1 - p) * (c[0] - a[0]) + 2 * p * (b[0] - c[0]), ty = 2 * (1 - p) * (c[1] - a[1]) + 2 * p * (b[1] - c[1]);
    const tl = Math.hypot(tx, ty) || 1, amp = Math.sin(p * waves * 2 * Math.PI) * 0.75 * Math.min(1, p * 6, (1 - p) * 6);
    d += (i ? " L" : "M") + pt([x - (ty / tl) * amp, y + (tx / tl) * amp]);
  }
  return d;
}

// Schulterblick: ein Kegel vom Spieler in Richtung des Ziels, so lang wie der Abstand zum Ziel
function kegel(from, to, weite = 70) {
  const L = dist(from, to) * K, h = ((weite / 2) * Math.PI) / 180, th = Math.atan2(to[1] - from[1], to[0] - from[0]);
  const o = [from[0] * K, from[1] * K];
  const p1 = [o[0] + L * Math.cos(th - h), o[1] + L * Math.sin(th - h)], p2 = [o[0] + L * Math.cos(th + h), o[1] + L * Math.sin(th + h)];
  const f = (p) => p[0].toFixed(1) + "," + p[1].toFixed(1);
  return `M${f(o)} L${f(p1)} A${L.toFixed(1)},${L.toFixed(1)} 0 0 1 ${f(p2)} Z`;
}

// Eine Fassung erbt die Tafel der Grundform: Nur gefüllte Listen der Fassung ersetzen die der Grundform.
export function mergeBoard(base, own) {
  const merged = { ...(base || {}) };
  Object.entries(own || {}).forEach(([key, value]) => {
    if (Array.isArray(value) ? value.length : value != null) merged[key] = value;
  });
  merged.sketch_steps = own?.sketch_steps || undefined; // gilt je Fassung, wird nicht vererbt
  return merged;
}

export function tokenIds(board) {
  const b = board || {};
  return {
    players: (b.players || []).map((p, i) => p.id || "p" + (i + 1)),
    balls: (b.balls || []).map((p, i) => p.id || "b" + (i + 1)),
    // Hütchen mit id können sich bewegen (geworfene Hütchen). Ohne id steht ein Hütchen fest (null).
    cones: (b.cones || []).map((c) => c.id || null),
  };
}

// Ältere Tafeln kennen nur Pfeile. Daraus wird je Pfeil ein Schritt: Der Pfeil nimmt mit, was an seinem Anfang steht.
function stepsFromArrows(b, ids, pos) {
  const cur = { ...pos };
  const nearest = (list, p, max) => {
    let best = null, bd = max;
    list.forEach((id) => { const d = dist(cur[id], p); if (d <= bd) { bd = d; best = id; } });
    return best;
  };
  return (b.arrows || []).map((a) => {
    let type = a.type === "lauf" ? "lauf" : "pass", who, ball;
    if (type === "pass") who = nearest(ids.balls, a.from, 8);
    else {
      who = nearest(ids.players, a.from, 6);
      ball = who && nearest(ids.balls, cur[who], 6);
      if (ball) type = "dribbling";
    }
    if (ball) cur[ball] = ahead(cur[who], a.to);
    if (who) cur[who] = a.to;
    return { moves: [{ who, ball, from: who ? undefined : a.from, to: a.to, type, bend: a.bend || 0 }] };
  });
}

export function buildPlay(board) {
  const b = board || {}, ids = tokenIds(b), tracks = {}, pos = {};
  (b.players || []).forEach((p, i) => { pos[ids.players[i]] = [p.x, p.y]; });
  (b.balls || []).forEach((p, i) => { pos[ids.balls[i]] = [p.x, p.y]; });
  (b.cones || []).forEach((p, i) => { if (ids.cones[i]) pos[ids.cones[i]] = [p.x, p.y]; });
  Object.keys(pos).forEach((id) => { tracks[id] = { start: pos[id], segs: [] }; });
  const source = b.steps?.length ? b.steps : stepsFromArrows(b, ids, pos);
  const arrows = [], steps = [];
  let t = LEAD;

  source.forEach((s, si) => {
    const t0 = t;
    let end = t0, prevEnd = t0;
    (s.moves || []).forEach((m, mi) => {
      // Schulterblick: bewegt niemanden, zeigt nur den Kegel. Zwei Blicke nacheinander (after) = links und rechts scannen
      if (m.type === "blick") {
        const from = pos[m.who];
        if (!from || !m.to) return;
        const a = (m.after ? prevEnd : t0) + (m.delay || 0), z = a + (m.dauer || 0.9);
        arrows.push({ t0: a, t1: z, type: "blick", step: si, d: kegel(from, m.to, m.weite || 70), join: true, head: { x: m.to[0] * K, y: m.to[1] * K, angle: 0 } });
        prevEnd = z;
        end = Math.max(end, z);
        return;
      }
      const isBall = ids.balls.includes(m.who) || ids.cones.includes(m.who);
      const from = m.from?.length === 2 ? m.from : pos[m.who];
      if (!from || !m.to) return;
      const type = m.type || (isBall ? "pass" : "lauf");
      const c = control(from, m.to, m.bend || 0), d = dist(from, m.to);
      const dur = type === "pass" ? clamp(0.3 + d * 0.014, 0.4, 1.1) : clamp(0.45 + d * 0.035, 0.7, 2.4);
      const a = (m.after ? prevEnd : t0) + (m.delay || 0), z = a + dur;
      if (tracks[m.who]) {
        tracks[m.who].segs.push({ t0: a, t1: z, from, to: m.to, c, ez: type === "pass" ? out : smooth });
        pos[m.who] = m.to;
      }
      if (m.ball && tracks[m.ball]) {
        const bf = pos[m.ball], bt = ahead(from, m.to);
        tracks[m.ball].segs.push({ t0: a, t1: z, from: bf, to: bt, c: control(bf, bt, m.bend || 0), ez: smooth });
        pos[m.ball] = bt;
      }
      arrows.push({
        t0: a, t1: z, type, step: si, d: pathFor(from, c, m.to, type),
        // Geht dieselbe Figur gleich weiter (Slalom, Laufweg mit Knick), bekommt nur das letzte Stück eine Pfeilspitze
        join: !!(s.moves[mi + 1]?.after && s.moves[mi + 1].who === m.who),
        head: { x: m.to[0] * K, y: m.to[1] * K, angle: (Math.atan2(m.to[1] - c[1], m.to[0] - c[0]) * 180) / Math.PI },
      });
      prevEnd = z;
      end = Math.max(end, z);
    });
    if (end === t0) end = t0 + 0.8;
    steps.push({ label: s.label || "", say: s.say || "", t0, t1: end });
    t = end + GAP;
  });

  return { ids, tracks, arrows, steps, total: steps.length ? t - GAP + TAIL : 0 };
}

export function positionAt(track, t) {
  let seg = null;
  for (const s of track.segs) { if (s.t0 <= t) seg = s; else break; }
  if (!seg) return track.start;
  if (t >= seg.t1) return seg.to;
  return bezier(seg.from, seg.c, seg.to, seg.ez((t - seg.t0) / (seg.t1 - seg.t0)));
}

export function stepAt(play, t) {
  let i = -1;
  play.steps.forEach((s, k) => { if (t >= s.t0) i = k; });
  return i;
}

// Der Trainer steht immer mit auf dem Platz. Fehlt er in den Daten, kommt er an den Feldrand.
export function withCoach(board) {
  const b = board || {}, players = b.players || [];
  if (players.some((p) => p.team === "c")) return b;
  return { ...b, players: [...players, { id: "T", team: "c", x: 4, y: 55.5, label: "T" }] };
}

/* ---------- Scroll-Story: Skizze, Sprung aufs Feld, dann jede Fassung nacheinander ---------- */

// Längen in Bildschirmhöhen. rate = Bildschirmhöhen pro Sekunde Spielzug.
// ende = Strecke nach der letzten Fassung, auf der die Schlusskarte "So läuft eine Runde" bildschirmfüllend aufzoomt
export const STORY = { sketch: 0.45, dive: 1, lead: 0.2, rate: 0.2, rest: 0.45, swap: 0.55, tail: 0.25, ende: 1.1 };

export function buildStory(einheit) {
  const chapters = [
    { label: "Grundform", title: "So geht’s", say: "So läuft die Grundform ab.", text: einheit.description, board: withCoach(einheit.board) },
    ...(einheit.versions || []).map((v) => ({ label: v.label, title: v.title, say: v.say || "", text: v.text, board: withCoach(mergeBoard(einheit.board, v.board)) })),
  ].map((c) => ({ ...c, play: buildPlay(c.board) }));

  // Alle Figuren und Bälle, die in irgendeiner Fassung vorkommen
  const figures = [], balls = [], cones = [], seen = new Set();
  chapters.forEach((c) => {
    (c.board.players || []).forEach((p, i) => {
      const id = c.play.ids.players[i];
      if (!seen.has(id)) { seen.add(id); figures.push({ id, team: p.team, label: p.label }); }
    });
    (c.board.balls || []).forEach((_, i) => {
      const id = c.play.ids.balls[i];
      if (!seen.has(id)) { seen.add(id); balls.push({ id }); }
    });
    // Bewegliche Hütchen (mit id), z. B. geworfene Hütchen
    (c.board.cones || []).forEach((cone, i) => {
      const id = c.play.ids.cones[i];
      if (id && !seen.has(id)) { seen.add(id); cones.push({ id, color: cone.color, shape: cone.shape }); }
    });
  });

  let u = STORY.sketch + STORY.dive;
  const segments = [{ type: "sketch", chapter: 0, u0: 0, u1: STORY.sketch }, { type: "dive", chapter: 0, u0: STORY.sketch, u1: u }];
  const marks = [{ short: "✎", label: "Skizze", u0: 0, u1: u, at: 0 }];
  chapters.forEach((c, i) => {
    const len = STORY.lead + Math.max(c.play.total, 1.5) * STORY.rate + STORY.rest;
    const last = i === chapters.length - 1, end = u + len + (last ? STORY.tail : STORY.swap);
    segments.push({ type: "play", chapter: i, u0: u, u1: u + len });
    if (!last) segments.push({ type: "swap", chapter: i, u0: u + len, u1: end });
    marks.push({ short: "ABCDEFGH"[i], label: c.label, u0: u, u1: end, at: u + 0.02, done: u + len - 0.05 });
    u = end;
  });
  // Schlusskarte: Das Feld bleibt im Endzustand der letzten Fassung stehen, davor zoomt die Karte auf (Stage.jsx)
  if (chapters.length) { segments.push({ type: "ende", chapter: chapters.length - 1, u0: u, u1: u + STORY.ende }); u += STORY.ende; }
  return { chapters, figures, balls, cones, segments, marks, length: u };
}

// Was vorgelesen wird: am Anfang der Titel, je Fassung Name, Titel und Erklärung, je Schritt seine Beschriftung
export const spokenIntro = (einheit) => (einheit.say_intro || "").trim() || sprechtext(`${einheit.title}.`);
// Vor dem Ablauf wird nur die Überschrift gesprochen. Was passiert, sagt die Stimme Schritt für Schritt genau dann, wenn es im Bild passiert.
// Nur eine Fassung ohne Schritte liest ihre ganze Erklärung vor.
export const spokenChapter = (chapter) => ((chapter.say || "").trim() || sprechtext(`${chapter.label}. ${chapter.title}.`)) + (chapter.play?.steps.length ? "" : ` ${chapter.text || ""}`);

// Hat ein Schritt einen eigenen Erzähltext (say), wird genau der gesprochen: ganze Sätze, die aneinander anschließen.
// Gesprochen wird nicht der Text vom Bildschirm, sondern seine Sprechfassung: mit „Spieler“ vor jeder Nummer und ausgeschriebenen Zahlen.
// Alle Sätze der Tonspur in Sprechreihenfolge: chapter -1 = Begrüßung, step -1 = Erklärung der Fassung, sonst der Schritt
export function spokenParts(einheit) {
  return [
    { chapter: -1, step: -1, text: spokenIntro(einheit).trim() },
    ...buildStory(einheit).chapters.flatMap((c, chapter) => [
      { chapter, step: -1, text: spokenChapter(c).trim() },
      ...c.play.steps.map((s, step) => ({ chapter, step, text: (s.say || "").trim() || fluss(sprechtext(s.label), step, c.play.steps.length) })),
    ]),
  ];
}

// Die Aufnahme zu einem Satz: ihre Adresse und der Text, der dafür eingesprochen wurde
export function spokenClip(audio, { chapter, step }) {
  if (chapter < 0) return { url: audio?.intro || "", text: audio?.intro_text || "" };
  const c = audio?.chapters?.[chapter];
  return step < 0 ? { url: c?.intro || "", text: c?.intro_text || "" } : { url: c?.steps?.[step] || "", text: c?.steps_text?.[step] || "" };
}

export function storyAt(story, u) {
  let seg = story.segments[0];
  for (const s of story.segments) if (u >= s.u0) seg = s;
  const p = clamp((u - seg.u0) / (seg.u1 - seg.u0), 0, 1);
  if (seg.type !== "play") return { type: seg.type, chapter: seg.chapter, p };
  const total = story.chapters[seg.chapter].play.total;
  return { type: "play", chapter: seg.chapter, p, t: clamp((u - seg.u0 - STORY.lead) / STORY.rate, 0, total) };
}

// Wo eine Figur oder ein Ball gerade steht und ob sie auf dem Platz ist (on: 0 bis 1)
export function tokenAt(story, at, id) {
  const ch = story.chapters, track = (i) => ch[i]?.play.tracks[id];
  const home = () => ({ pos: ch.map((c) => c.play.tracks[id]).find(Boolean)?.start || [50, 30], on: 0 });
  if (at.type === "sketch" || at.type === "dive") return track(0) ? { pos: track(0).start, on: 1 } : home();
  if (at.type === "play") return track(at.chapter) ? { pos: positionAt(track(at.chapter), at.t), on: 1 } : home();
  if (at.type === "ende") return track(at.chapter) ? { pos: positionAt(track(at.chapter), ch[at.chapter].play.total), on: 1 } : home();
  const a = track(at.chapter), b = track(at.chapter + 1), q = smooth(at.p);
  const pa = a && positionAt(a, ch[at.chapter].play.total), pb = b && b.start;
  if (a && b) return { pos: [pa[0] + (pb[0] - pa[0]) * q, pa[1] + (pb[1] - pa[1]) * q], on: 1 };
  if (a) return { pos: pa, on: 1 - q };
  if (b) return { pos: pb, on: q };
  return home();
}
