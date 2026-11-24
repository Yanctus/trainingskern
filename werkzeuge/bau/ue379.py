import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-16 (U15-U17, Woche 28 Phase 5): Pre-Season 16 Acceleration Speed Teamwork. 20 x 20 Yards = 18 x 18 m, Feld x 26-74, y 4-51.
# Ausrichtung wie im PDF (Start unten, Stange oben). Drei Teams im Original; auf der Tafel nur zwei Bahnen (Team Rot links =
# pink, Team Neon rechts = gelb), das dritte Team (blau) nur im Text. Je Bahn nur der Läufer und der nächste Spieler (3D-Abstand),
# die übrigen drei nur im Text. Neon mit den Nummern aus dem PDF (8, 6), Rot neu nummeriert, weil 4, 7 und 8 doppelt sind
# (pink 10 -> 10, 4 -> 5). Pro Bahn: Stange oben, drei Hütchen zum Aufnehmen (neon), zwei Minihürden, Starthütchen (orange).
# Das Hütchen in der Hand des Läufers ist nur im Text. Ein Trainer statt zwei, unten zwischen den Bahnen (pfeift).
# Kein Ball im Original: nur die zwei Ersatzbälle beim Trainer. Wertung: Das Siegerteam bekommt einen Punkt (Original: Sieger).
# Fassungen = PDF Key Coaching Point 1 (sofort das nächste Hütchen nehmen) und 2 (hinten anstellen, sonst zählt man nicht),
# dazu aus der Zusammenfassung „Time the start of your sprints when receiving the cone“.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Keine Dublette: keine bestehende Staffel mit Stange, Hütchen zum Umsetzen und Hürden.
T = P("T", "c", 46, 55.3, "T")
ERSATZ = [B("s1", 49.5, 55.8), B("s2", 52, 55.8)]
A, Bx = 31, 55  # linke Kante der Bahn von Team Rot bzw. Team Neon
POS = {"r10": (A + 3, 33), "r5": (A + 3, 49), "n8": (Bx + 3, 33), "n6": (Bx + 3, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def bahn(x0):
    return [C(x0 + 4, 5.5, shape="stange"), C(x0 + 7.5, 5.5, "neon"), C(x0 + 9.5, 5.5, "neon"), C(x0 + 11.5, 5.5, "neon"),
            C(x0 + 9, 13, shape="huerde_ou"), C(x0 + 7.5, 18.5, shape="huerde_ou"), C(x0 + 7, 33.5)]
LINES = [rect(26, 4, 48, 47)]
CONES = bahn(A) + bahn(Bx)
def hoch(who, x0, **k): return mv(who, [x0 + 3, 9], **k)
def holen(who, x0, **k): return mv(who, [x0 + 7.5, 8.5], **k)
def huerden(who, x0, delay=None):
    return [mv(who, [x0 + 9, 10.5], delay=delay), mv(who, [x0 + 9, 15.5], after=True), mv(who, [x0 + 7.5, 21], after=True)]

u = {"title": "Staffel mit Hütchen und Hürden", "code": "UE-379", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 9, "players_max": 18,
 "field_size": "18 x 18 m",
 "description": "Eine Staffel für die Vorbereitung mit drei Teams. Jeder sprintet mit einem Hütchen zur Stange, steckt es drauf und nimmt das nächste Hütchen mit. Über zwei Minihürden geht es zurück, und das Hütchen wandert an den Nächsten. Das Team, das zuerst wieder komplett hinten steht, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit drei Bahnen. In jeder Bahn steht oben eine Stange mit Hütchen daneben, darunter zwei Minihürden, unten ein Starthütchen.",
  "Verteilen: Drei Teams mit je fünf Spielern stehen hintereinander am Start ihrer Bahn. Der Erste jedes Teams hat ein Hütchen in der Hand. Der Trainer steht unten zwischen den Bahnen.",
  "Ablauf: Auf Pfiff sprinten die Ersten zur Stange und stecken ihr Hütchen drauf. Sie nehmen das nächste Hütchen, gehen mit schnellen Füßen über die Hürden und sprinten zurück. Dort bekommt der Nächste das Hütchen und läuft los.",
  "Wertung: Das Team, bei dem zuerst alle Spieler wieder hinten in der Reihe stehen, gewinnt, und das gibt einen Punkt. Danach beginnt die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Losrennen genau dann, wenn du das Hütchen hast", "Kurze, schnelle Schritte über die Hürden", "Schnelle Hände an der Stange", "Laut anfeuern, das ganze Team"],
 "materials": ["3 Stangen", "Viele Hütchen", "6 Minihürden"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Staffel mit Hütchen und Hürden. Drei Teams laufen um die Wette, mit Sprints, einem Hütchen in der Hand und schnellen Füßen über die Hürden.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Pfiff, Sprint zur Stange", "Pfiff, und los. Die Ersten sprinten mit einem Hütchen in der Hand hoch zur Stange. Alle Teams laufen gleichzeitig, wir schauen auf Spieler acht.",
     hoch("n8", Bx), hoch("r10", A, delay=0.15)),
   S("Hütchen drauf, neues holen", "Oben steckt Spieler acht sein Hütchen auf die Stange. Gleich daneben schnappt er sich das nächste.",
     holen("n8", Bx), holen("r10", A, delay=0.15)),
   S("Schnelle Füße über die Hürden", "Jetzt über die zwei Hürden, kleine Schritte, jeder Fuß nur kurz am Boden. Unten rückt Spieler sechs schon an die Startlinie.",
     *huerden("n8", Bx), *huerden("r10", A, delay=0.15), mv("n6", [Bx + 3, 34], delay=0.4), mv("r5", [A + 3, 34], delay=0.5)),
   S("Übergabe, der Nächste läuft: Punkt", "Spieler acht sprintet zurück und drückt Spieler sechs das Hütchen in die Hand. Der läuft sofort los, Spieler acht stellt sich hinten an. Steht ein Team zuerst wieder komplett hinten, gewinnt es, und das gibt einen Punkt für dieses Team.",
     mv("n8", [Bx + 4.5, 30]), hoch("n6", Bx, after=True), mv("n8", [Bx + 3, 48.5], after=True),
     mv("r10", [A + 4.5, 30], delay=0.15), hoch("r5", A, after=True), mv("r10", [A + 3, 48.5], after=True))],
  "dims": dims(26, 74, 4, 51, "18 m", "18 m", rx=82)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Sofort das nächste Hütchen.", "Sofort das nächste Hütchen",
    "Wer sein Hütchen auf die Stange gesteckt hat, greift sofort das nächste. Ohne Hütchen zurückzukommen kostet Zeit, dann muss er noch einmal hoch. Das kann das ganze Rennen kosten.",
    sp(n8=(Bx + 3, 9), r10=(A + 3, 9)), ERSATZ,
    [S("Hütchen drauf, nächstes greifen", "Spieler acht steckt sein Hütchen auf die Stange und greift ohne Pause das nächste. Daneben macht es Spieler zehn genauso.",
       holen("n8", Bx), holen("r10", A, delay=0.15)),
     S("Mit Hütchen zurück", "Mit dem neuen Hütchen in der Hand geht es über die Hürden und zurück zum Start. Wer es oben vergisst, muss noch einmal hoch.",
       *huerden("n8", Bx), mv("n8", [Bx + 4.5, 30], after=True), *huerden("r10", A, delay=0.15), mv("r10", [A + 4.5, 30], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Im richtigen Moment starten und hinten anstellen.", "Übergeben, hinten anstellen",
    "Der Nächste steht an der Linie, streckt die Hand aus und startet genau dann, wenn er das Hütchen hat. Wer zurückkommt, stellt sich ganz hinten in seine Reihe. Erst dann zählt er als fertig.",
    sp(n8=(Bx + 2.5, 17), r10=(A + 2.5, 17), n6=(Bx + 3, 34), r5=(A + 3, 34)), ERSATZ,
    [S("Übergabe im Lauf", "Spieler sechs steht an der Linie und streckt die Hand aus. Er startet genau in dem Moment, in dem er das Hütchen hat.",
       mv("n8", [Bx + 4.5, 30]), hoch("n6", Bx, after=True), mv("r10", [A + 4.5, 30], delay=0.15), hoch("r5", A, after=True)),
     S("Hinten anstellen", "Spieler acht läuft nicht einfach aus. Er stellt sich ganz hinten in seine Reihe, erst dann zählt er als fertig. Stehen alle wieder hinten, ist das Rennen vorbei.",
       mv("n8", [Bx + 3.5, 40]), mv("n8", [Bx + 3, 48.5], after=True), mv("r10", [A + 3.5, 40], delay=0.15), mv("r10", [A + 3, 48.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
