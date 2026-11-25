// Abspielcode bündeln wie in passbahn.mjs beschrieben (/tmp/claude-0/pb.mjs).
// Prüft alle Sichtkegel (Schritt-Typ "blick") mit dem Abspielcode der App (playbook.mjs, siehe passbahn.mjs):
//  A "ohne Ballaktion": Wer schaut, spielt danach (im selben oder nächsten Schritt) nicht selbst den Ball (Pass, Schuss, Dribbling).
//     Regel des Inhabers (25.11.2026): Der Kegel gehört zu dem Spieler, der schaut und DANN handelt, nie zum Passempfänger,
//     der nur angespielt wird. Verteidiger-Blicke (Gegner im Blick) werden getrennt als "Verteidiger" gemeldet.
//  B "Kegel nicht am Spieler": Der Kegel beginnt nicht dort, wo der Spieler in dem Moment steht.
// Aufruf: node blickpruefung.mjs <playbook.mjs> <einheiten.json (Liste oder eine)> <ausgabe.json>
import fs from "node:fs";
const pb = await import(process.argv[2]);
const roh = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const alle = Array.isArray(roh) ? roh : [roh];
const dist = (p, q) => Math.hypot(p[0] - q[0], p[1] - q[1]);
const out = [];
for (const e of alle) {
  if (!e.code || !e.board) continue;
  let story; try { story = pb.buildStory(e); } catch { continue; }
  story.chapters.forEach((ch) => {
    const play = ch.play, board = ch.board, ids = pb.tokenIds(board);
    const team = {}; (board.players || []).forEach((p, i) => { team[ids.players[i]] = p.team; });
    const spieler = Object.keys(team);
    const posAt = (id, t) => pb.positionAt(play.tracks[id], t);
    const near = (p, t) => spieler.map((id) => [dist(posAt(id, t), p), id]).sort((a, b) => a[0] - b[0])[0] || [99, null];
    // Ballaktionen: Pässe/Schüsse (Ballsegment "out") mit Passgeber, Dribblings (Ball läuft mit Spieler)
    const aktionen = [];
    for (const [bid, tr] of Object.entries(play.tracks)) {
      if (!ids.balls.includes(bid)) continue;
      for (const seg of tr.segs) {
        const [d, wer] = near(seg.from, seg.t0);
        if (d < 4.5) aktionen.push({ wer, t: seg.t0, art: seg.ez?.name === "out" ? "pass" : "dribbling" });
      }
    }
    const steps = (board.steps || []);
    const blicke = play.arrows.filter((a) => a.type === "blick");
    let k = 0;
    steps.forEach((s, si) => {
      (s.moves || []).forEach((m) => {
        if (m.type !== "blick") return;
        const a = blicke[k++]; if (!a || !play.tracks[m.who]) return;
        const mm = /M\s*([-\d.]+)[ ,]([-\d.]+)/.exec(a.d || ""); const von = mm ? [+mm[1] / pb.K, +mm[2] / pb.K] : null;
        const wo = posAt(m.who, a.t0);
        const ende = play.steps[si + 1] ? play.steps[si + 1].t1 : play.total;
        const eigene = aktionen.filter((x) => x.wer === m.who && x.t >= a.t0 - 0.05 && x.t <= ende + 0.05);
        const gegnerTeam = team[m.who] === "a" ? "b" : team[m.who] === "b" ? "a" : null;
        const zielGegner = gegnerTeam && spieler.some((id) => team[id] === gegnerTeam && dist(posAt(id, a.t1), m.to) < 6);
        const hatBall = aktionen.some((x) => x.wer === m.who);
        const [dz, ziel] = near(m.to, a.t1);
        const pass_an_ihn = play.tracks && Object.entries(play.tracks).some(([bid, tr]) => ids.balls.includes(bid) && tr.segs.some((sg) => sg.ez?.name === "out" && sg.t0 >= play.steps[si].t0 - 0.05 && sg.t0 <= play.steps[si].t1 + 0.05 && near(sg.to, sg.t1)[1] === m.who));
        const spaeter = aktionen.some((x) => x.wer === m.who && x.t >= a.t0 - 0.05);
        const row0 = { schautAuf: dz < 4 ? ziel : "Raum", passAnIhnImSchritt: pass_an_ihn, handeltSpaeter: spaeter };
        const row = { code: e.code, titel: e.title, ton: !e.hidden, fassung: ch.label, schritt: si + 1, wer: m.who, team: team[m.who], label: s.label || "", ...row0 };
        if (von && dist(von, wo) > 2.5) out.push({ ...row, fehler: "Kegel nicht am Spieler", abstand: +dist(von, wo).toFixed(1) });
        if (pass_an_ihn && dz >= 4 && eigene.length) out.push({ ...row, fehler: "Kegel beim Passempfänger (schaut nicht zum Passgeber)" });
        else if (pass_an_ihn && dz < 4) { /* Annehmen: schaut zum Passgeber, erlaubt */ }
        if (pass_an_ihn && dz < 4) return; // bereit zur Annahme: schaut zum Ball/Passgeber, immer erlaubt
        if (!eigene.length) out.push({ ...row, fehler: hatBall ? "ohne Ballaktion danach" : (zielGegner ? "Verteidiger (schaut zum Gegner)" : "ohne Ballaktion danach") });
      });
    });
  });
}
fs.writeFileSync(process.argv[4], JSON.stringify(out, null, 1));
const z = {}; out.forEach((o) => { z[o.fehler] = (z[o.fehler] || 0) + 1; });
console.log("Funde:", out.length, JSON.stringify(z), "in", new Set(out.map((o) => o.code)).size, "Einheiten");
