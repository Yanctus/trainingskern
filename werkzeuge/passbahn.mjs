// Aufruf: node passbahn.mjs <playbook.mjs aus der App, mit esbuild gebündelt> <alle Einheiten als JSON> <ausgabe.json>
// playbook.mjs erzeugen (in der Base44-Sandbox): NODE_PATH=/app/node_modules ./node_modules/.bin/esbuild src/lib/playbook.js --bundle --format=esm --alias:@=./src --outfile=/tmp/pb.mjs
// Treffer: Gegner beim Abspiel näher als 2,8 an der Passkurve (statisch) oder Ball fliegt näher als 2,2 an ihm vorbei (flug).
// Sucht Pässe, bei denen ein Gegenspieler in der Passbahn steht (Abspielcode der App: buildStory/buildPlay/positionAt)
import fs from "node:fs";
const pb = await import(process.argv[2]);
const roh = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const alle = Array.isArray(roh) ? roh : [roh];
const out = [];
const at = (seg, s) => { const u = 1 - s; return [u*u*seg.from[0] + 2*u*s*seg.c[0] + s*s*seg.to[0], u*u*seg.from[1] + 2*u*s*seg.c[1] + s*s*seg.to[1]]; };
const dist = (p, q) => Math.hypot(p[0]-q[0], p[1]-q[1]);
for (const e of alle) {
  if (!e.code || !e.board || e.kind === "Taktik") continue;
  let story; try { story = pb.buildStory(e); } catch { continue; }
  story.chapters.forEach((ch, ci) => {
    const play = ch.play, board = ch.board, ids = pb.tokenIds(board);
    const team = {}; (board.players || []).forEach((p, i) => { team[ids.players[i]] = p.team; });
    const spieler = Object.keys(team);
    for (const [bid, tr] of Object.entries(play.tracks)) {
      if (!ids.balls.includes(bid)) continue;
      for (const seg of tr.segs) {
        if (seg.ez?.name !== "out") continue; // nur Pässe
        const t0 = seg.t0, t1 = seg.t1;
        const posAt = (id, t) => pb.positionAt(play.tracks[id], t);
        // Passgeber = Spieler nächst am Startpunkt, Empfänger = nächst am Zielpunkt beim Ankommen
        const near = (p, t) => spieler.map((id) => [dist(posAt(id, t), p), id]).sort((a, b) => a[0] - b[0])[0];
        const [dg, geber] = near(seg.from, t0) || [];
        if (!geber || dg > 4) continue;
        const tg = team[geber]; if (tg !== "a" && tg !== "b") continue;
        const [de, empf] = near(seg.to, t1) || [];
        if (empf && team[empf] !== tg && de < 3.5) continue; // gewollter Pass zum Gegner (Abfangen)
        const L = dist(seg.from, seg.to); if (L < 6) continue;
        for (const id of spieler) {
          if (id === geber || id === empf || (team[id] !== "a" && team[id] !== "b") || team[id] === tg) continue;
          // statisch: Abstand des Gegners beim Abspiel zur Passkurve (ohne die Enden)
          const g = posAt(id, t0); let dmin = 99, smin = 0;
          for (let k = 2; k <= 38; k++) { const s = k / 40, d = dist(at(seg, s), g); if (d < dmin) { dmin = d; smin = s; } }
          // dynamisch: Ball fliegt durch den Spieler
          let dflug = 99;
          for (let k = 3; k <= 37; k++) { const s = k / 40, t = t0 + (t1 - t0) * s; dflug = Math.min(dflug, dist(at(seg, s), posAt(id, t))); }
          if (dmin < 2.8 || dflug < 2.2) out.push({ code: e.code, titel: e.title, sichtbar: !e.hidden, kap: ci, kapitel: ch.label, schritt: pb.stepAt(play, t0) + 1, geber, empf, gegner: id, statisch: +dmin.toFixed(1), flug: +dflug.toFixed(1) });
        }
      }
    }
  });
}
fs.writeFileSync(process.argv[4], JSON.stringify(out, null, 1));
const units = new Set(out.map((o) => o.code));
console.log("Treffer:", out.length, "in", units.size, "Einheiten");
