import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 45-P4 (U15-U17, Woche 41 Phase 3): Diamond Passing Combinations Technical. Kein PDF, nur Video und Ton.
# 25 x 20 Yards = 23 x 18 m (gerundet 25 x 18 m) direkt vor dem Strafraum, Feld x 25-75, y 20-54; darüber (schematisch, nicht
# maßstabsgetreu) Strafraum und Torraum wie im Video, Tor oben (Großfeldtor ohne Torwart wie im Video, gebraucht nur in der
# zweiten Steigerung). Raute aus vier Hütchen (unten Start, rechts, Spitze im Strafraum, links) und ein Hütchen in der Mitte.
# Alle Spieler Team Neon, Nummern wie im Video (2-11). Wartende neben die Stationen gesetzt (3D-Abstand). Ein Trainer.
# Ablauf nach Video und Ton: Der Ball läuft gegen den Uhrzeigersinn (unten -> rechts -> Spitze -> links -> unten). Jeder spielt den
# Doppelpass mit der nächsten Station, läuft dafür in die Mitte (am Mittelhütchen), bekommt die Ablage, spielt in den Lauf des
# Stationsspielers und folgt seinem Pass auf dessen Station. Vereinfacht: Wer seinem Pass folgt, stellt sich direkt auf die Station.
# Fassungen: Steigerung 1 = zwei Bälle (Ton), Steigerung 2 = Steilpass in den Strafraum mit Abschluss, Trainer spielt sofort den
# nächsten Ball zur Spitze (Ton und Video; der Trainer steht dafür seitlich am Strafraum).
# Keine Dublette: 32-P12 (Raute 15 x 15 Yards, Ball wird quer über die Raute verlagert, kein Mittelhütchen, kein Abschluss),
# 45-P12 (UE-239, Dreiecke im V), 45-P5 (Gegnerspiel in vier Feldern) und 32-P8 (Rondo-Welle) haben andere Abläufe.
# Kein Sichtkegel im Original (Ton und Video geprüft, kein PDF-Text).
T = P("T", "c", 14, 52, "T")
POS = {"n4": (50, 50), "n5": (59, 52), "n10": (41, 52), "n7": (69, 35), "n2": (78, 35), "n3": (31, 35), "n11": (22, 35),
       "n9": (50, 14.5), "n8": (41, 12), "n6": (59, 12)}
def sp(trainer=T, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [trainer]
ERSATZ = [B("s1", 10.5, 55), B("s2", 13.5, 56.5)]
LINES = [rect(25, 4, 50, 50), line(25, 20, 75, 20, dashed=False), rect(40, 4, 20, 6)]
KEGEL = [C(50, 53.5), C(72, 35), C(50, 11.5), C(28, 35), C(50, 35)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}]
DIMS = dims(25, 75, 20, 54, "25 m", "18 m", rx=94)
MR, MO, ML = [53, 38], [53, 31], [47, 32]  # Plätze an der Mitte: von unten, von der Spitze, von links

def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]

u = {"title": "Doppelpässe über die Rautenmitte", "code": "UE-416", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "25 x 18 m",
 "description": "Eine Passform für kurze Kombinationen vor dem Strafraum. Vier Stationen stehen als Raute, in der Mitte liegt ein Hütchen. Der Ball läuft über Doppelpässe einmal rundherum, und jeder holt sich die Ablage in der Mitte ab, statt außen herumzulaufen. Danach folgt jeder seinem Pass zur nächsten Station.",
 "organisation": ["Aufbauen: Direkt vor dem Strafraum ein Feld von 25 mal 18 Metern. Vier Hütchen bilden eine Raute, die Spitze liegt im Strafraum. Ein Hütchen kommt in die Mitte.",
  "Verteilen: Zehn Spieler, an jeder Station zwei bis drei. Die Bälle liegen am Start unten. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Der Spieler am Start spielt zur rechten Station und läuft in die Mitte. Er bekommt die Ablage und spielt in den Lauf seines Partners. Der macht mit der Spitze genauso weiter, dann geht es über links zurück zum Start.",
  "Wechsel: Jeder folgt seinem Pass zur nächsten Station. Ist der Ball zurück am Start, beginnt der Nächste mit einem neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem Pass in die Mitte, nicht außen herum", "Flach und scharf passen, die Ablage mit einem Kontakt", "In den Lauf spielen, nicht in den Fuß", "Sofort dem Pass folgen und den Rhythmus halten"],
 "materials": ["5 Hütchen", "1 Tor", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Doppelpässe über die Rautenmitte. Eine Passform vor dem Strafraum, und der Ball läuft über vier Doppelpässe einmal um die Raute.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 50.6, 50.6)] + ERSATZ,
  "steps": [
   S("Pass raus, rein in die Mitte", "Spieler vier startet unten. Er spielt flach zu Spieler sieben auf der rechten Station und läuft sofort in die Mitte ans Hütchen.",
     ps("b1", [69.6, 35.6]), mv("n4", MR, delay=0.3)),
   S("Ablage, dann in den Lauf", "Spieler sieben legt direkt in die Mitte ab und startet Richtung Strafraum. Spieler vier spielt ihm den Ball in den Lauf und folgt seinem Pass auf die rechte Station.",
     ps("b1", f(MR)), mv("n7", [63, 24], after=True), ps("b1", [63.6, 24.6], after=True), mv("n4", [69, 35], after=True)),
   S("Doppelpass mit der Spitze", "Jetzt das Gleiche mit der Spitze. Spieler sieben spielt zu Spieler neun und holt sich die Ablage in der Mitte. Spieler neun startet nach links, bekommt den Ball in den Lauf, und Spieler sieben geht hoch auf die Spitze.",
     ps("b1", [50.6, 15.1]), mv("n7", MO, delay=0.3), ps("b1", f(MO), after=True), mv("n9", [37, 24], after=True),
     ps("b1", [37.6, 24.6], after=True), mv("n7", [50, 14.5], after=True)),
   S("Doppelpass auf der linken Seite", "Spieler neun spielt zu Spieler drei und läuft wieder in die Mitte, nicht an der Raute entlang. Die Ablage kommt direkt, Spieler drei startet nach unten.",
     ps("b1", [31.6, 35.6]), mv("n9", ML, delay=0.3), ps("b1", f(ML), after=True), mv("n3", [38, 45], after=True)),
   S("Zurück zum Start", "Spieler neun spielt in den Lauf und geht auf die linke Station. Spieler drei dribbelt zurück zum Start, und die Runde ist durch. Jetzt startet Spieler fünf mit dem nächsten Ball.",
     ps("b1", [38.6, 45.6]), mv("n9", [31, 35], after=True), dr("n3", "b1", [46, 49], delay=0.6))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei Bälle gleichzeitig.", "Zwei Bälle gleichzeitig",
    "Ist der erste Ball an der Spitze, startet unten schon der zweite. Jetzt laufen zwei Bälle in der Raute. Die Spieler müssen genau schauen, wann die Mitte frei ist, und den Rhythmus halten.",
    sp(), [B("b1", 50.6, 50.6), B("b2", 59.6, 52.6)] + ERSATZ,
    [S("Der erste Ball läuft", "Spieler vier spielt den Doppelpass mit Spieler sieben über die Mitte und spielt ihn steil Richtung Strafraum. Spieler fünf geht mit dem zweiten Ball an den Start.",
       ps("b1", [69.6, 35.6]), mv("n4", MR, delay=0.3), ps("b1", f(MR), after=True), mv("n7", [63, 24], after=True),
       ps("b1", [63.6, 24.6], after=True), mv("n4", [69, 35], after=True), dr("n5", "b2", [50, 50], delay=1.5)),
     S("An der Spitze, der Zweite startet", "Spieler sieben spielt den Doppelpass mit der Spitze, und Spieler neun startet mit dem Ball nach links. In dem Moment spielt Spieler fünf unten schon zu Spieler vier.",
       ps("b1", [50.6, 15.1]), mv("n7", MO, delay=0.3), ps("b1", f(MO), after=True), mv("n9", [37, 24], after=True),
       ps("b1", [37.6, 24.6], after=True), mv("n7", [50, 14.5], after=True), ps("b2", [69.6, 35.6], delay=2.0), mv("n5", MR, delay=2.3)),
     S("Zwei Bälle, eine Mitte", "Jetzt laufen zwei Bälle. Links holt sich Spieler neun die Ablage von Spieler drei, rechts bekommt Spieler fünf die Ablage von Spieler vier. Jeder spielt weiter in den Lauf und folgt seinem Pass.",
       ps("b1", [31.6, 35.6]), mv("n9", ML, delay=0.3), ps("b1", f(ML), after=True), ps("b2", f(MR), delay=0.6),
       mv("n4", [63, 24], delay=1.2), ps("b2", [63.6, 24.6], delay=1.6), mv("n3", [38, 45], delay=1.6), ps("b1", [38.6, 45.6], delay=2.0))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Steil in den Strafraum und abschließen.", "Steilpass und Abschluss",
    "Nach dem Doppelpass spielt der Spieler in der Mitte steil in den Strafraum. Sein Partner nimmt den Ball mit dem ersten Kontakt mit und schließt ab. Der Trainer steht seitlich am Strafraum und spielt sofort den nächsten Ball zur Spitze, damit es ohne Pause weitergeht.",
    sp(trainer=P("T", "c", 22, 9, "T"), n8=(40, 17.5), n6=(31, 17.5)), [B("b1", 50.6, 50.6), B("s1", 22.6, 9.6), B("s2", 20, 12)],
    [S("Doppelpass über die Mitte", "Spieler vier spielt zu Spieler sieben und läuft in die Mitte. Die Ablage kommt direkt zurück.",
       ps("b1", [69.6, 35.6]), mv("n4", MR, delay=0.3), ps("b1", f(MR), after=True)),
     S("Steil in den Strafraum", "Spieler sieben startet in den Strafraum, an der Spitze vorbei. Spieler vier spielt den Ball steil in seinen Lauf, nicht zu kurz und nicht zu lang.",
       mv("n7", [62, 21]), ps("b1", [62.6, 21.6], delay=0.5)),
     S("Mitnehmen, abschließen: Punkt", "Spieler sieben nimmt den Ball mit dem ersten Kontakt mit und schießt mit dem zweiten, und das gibt einen Punkt für Spieler sieben. Sofort spielt der Trainer den nächsten Ball zu Spieler neun, und es geht über links weiter.",
       dr("n7", "b1", [57, 13]), ps("b1", [53.5, 4.4], after=True), ps("s1", [50.6, 15.1], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
