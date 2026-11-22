import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 85-P4 (U12-U14, Woche 31 Phase 1): 433 Passing Combinations. 15 x 20 Yards. Gedreht: im PDF startet die Folge links und der
# letzte Pass geht nach links zurück zum Start, hier liegt der Start oben und der letzte Pass geht nach oben (Minitor der zweiten
# Steigerung oben). Feld x 22-78, y 8-52 (18 x 14 m). Stationen wie im PDF: Start (oben, 9 mit Ball, 8 wartet), links oben (11),
# links unten (4), Ende unten (10, 7 wartet); die zwei Hütchen rechts sind die Stationen für die andere Seite (Steigerung 1).
# Alle Spieler pink -> Neon, Nummern aus Text und Video (9, 8, 11, 4, 10, 7). Ein Trainer statt einem mit Bällen oben rechts.
# Hütchen neben die Spieler gerückt (Linienprüfung). In der Grundform spielt Spieler zehn zu Spieler acht, der am Start wartet.
# Steigerung 2 (Minitor): Spieler zehn spielt Doppelpass mit dem Start und schießt ins Minitor oben links, der Trainer spielt den
# nächsten Ball zum Start. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 88, 12, "T")
ERSATZ = [B("s1", 91.6, 15.5), B("s2", 88, 15.5)]
POS = {"n9": (48, 10.5), "n8": (57, 8), "n11": (29, 20), "n4": (26, 40), "n10": (50, 47), "n7": (59, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(22, 8, 56, 44)]
KEGEL = [C(43, 11), C(24, 17), C(21, 40), C(45, 50.5), C(76, 17), C(79, 40)]

u = {"title": "Passfolge mit zwei Doppelpässen", "code": "UE-215", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 8, "field_size": "18 x 14 m",
 "description": "Eine feste Passfolge über vier Stationen mit sechs Spielern. Nach einem kurzen Pass kommen zwei Doppelpässe, dann dribbelt der letzte Spieler an und spielt zurück zum Start. Jeder läuft seinem Pass hinterher zur nächsten Station. Nach einer Weile läuft die Folge über die andere Seite.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern mit sechs Hütchen: Start oben, links zwei Stationen, Ende unten und rechts zwei Stationen für die andere Seite.",
  "Verteilen: Zwei Spieler am Start, einer mit Ball, je einer an den zwei Stationen links und zwei am Ende. Der Trainer steht oben rechts mit Bällen.",
  "Ablauf: Pass vom Start nach links oben, Doppelpass mit links unten, Pass zum Ende, Doppelpass mit links unten. Dann dribbelt der Spieler vom Ende an und spielt zurück zum Start.",
  "Wechsel: Jeder läuft seinem Pass hinterher zur nächsten Station. Nach ein paar Minuten läuft die Folge über die rechte Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Den Körper öffnen und mit dem hinteren Fuß annehmen", "Flach, genau und mit der richtigen Härte passen", "Wenn möglich mit einem Kontakt spielen", "Sich vom Hütchen lösen und laut den Ball fordern"],
 "materials": ["6 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Passfolge mit zwei Doppelpässen. Der Ball läuft über die linke Seite nach unten und mit einem Doppelpass zurück nach oben zum Start.",
 "board": {"lines": LINES, "goals": [], "cones": KEGEL, "players": sp(), "balls": [B("b1", 48.6, 11.1)] + ERSATZ,
  "steps": [
   S("Pass", "Spieler neun spielt flach zu Spieler elf. Spieler elf löst sich vom Hütchen und nimmt den Ball mit offenem Körper an.",
     ps("b1", [29.6, 20.6])),
   S("Doppelpass mit Spieler vier", "Spieler elf spielt zu Spieler vier und startet nach innen. Spieler vier legt den Ball direkt in seinen Lauf zurück.",
     ps("b1", [26.6, 40.6]), mv("n11", [37, 33], delay=0.3), ps("b1", [37.6, 33.6], after=True)),
   S("Pass zum Ende", "Spieler elf spielt weiter zu Spieler zehn am Ende. Spieler vier rückt gleichzeitig ein Stück nach unten.",
     ps("b1", [50.6, 47.6]), mv("n4", [34, 45], delay=0.3)),
   S("Ablage in den Lauf", "Spieler zehn spielt zu Spieler vier und läuft los. Spieler vier legt den Ball vor ihn, sodass er im Lauf annehmen kann.",
     ps("b1", [34.6, 45.6]), mv("n10", [51, 35], delay=0.3), ps("b1", [51.6, 35.6], after=True)),
   S("Zurück zum Start", "Spieler zehn dribbelt nach oben und spielt genau zu Spieler acht am Start. Die Runde ist geschafft. Alle laufen ihrem Pass hinterher zur nächsten Station, und Spieler acht startet die nächste Runde.",
     dr("n10", "b1", [51, 25]), ps("b1", [57.6, 8.6], after=True), mv("n9", [46, 16], after=True), mv("n9", [29, 20], after=True), mv("n11", [26, 40], after=True),
     mv("n4", [50, 47], after=True), mv("n10", [66, 10], after=True))],
  "dims": dims(22, 78, 8, 52, "18 m", "14 m", rx=96)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Folge läuft über die andere Seite.", "Andere Seite",
    "Jetzt läuft dieselbe Folge über die rechte Seite. So kommen die Pässe aus einem anderen Winkel, und jeder muss auch mit dem schwächeren Fuß annehmen und passen.",
    sp(n11=(71, 20), n4=(74, 40)), [B("b1", 48.6, 11.1)] + ERSATZ,
    [S("Nach rechts", "Spieler neun spielt jetzt nach rechts zu Spieler elf. Er nimmt mit einem Fuß an und passt mit dem anderen.",
       ps("b1", [71.6, 20.6])),
     S("Zwei Doppelpässe", "Doppelpass mit Spieler vier, dann der Pass zu Spieler zehn. Spieler vier rückt nach unten und legt für Spieler zehn in den Lauf.",
       ps("b1", [74.6, 40.6]), mv("n11", [63, 33], delay=0.3), ps("b1", [63.6, 33.6], after=True), ps("b1", [50.6, 47.6], after=True),
       mv("n4", [66, 42], after=True), ps("b1", [66.6, 42.6], after=True), mv("n10", [49, 35], after=True), ps("b1", [49.6, 35.6], after=True)),
     S("Zurück zum Start", "Spieler zehn dribbelt nach oben und spielt zu Spieler acht am Start. Dann läuft jeder seinem Pass hinterher.",
       dr("n10", "b1", [49, 25]), ps("b1", [57.6, 8.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Minitor zum Abschluss.", "Mit Minitor",
    "Oben links steht jetzt ein Minitor. Spieler zehn spielt am Ende einen Doppelpass mit dem Start und schließt direkt ab. Danach spielt der Trainer den nächsten Ball zum Start.",
    sp(n9=(29, 20), n11=(26, 40), n4=(35, 47), n10=(51, 32), n8=(48, 10.5), n7=(59, 49)), [B("b1", 51.6, 32.6)] + ERSATZ,
    [S("Doppelpass mit dem Start", "Spieler zehn hat den Ball nach der Ablage. Er dribbelt nach oben, spielt zu Spieler acht und läuft weiter. Spieler acht legt den Ball direkt vor ihn.",
       dr("n10", "b1", [51, 25]), ps("b1", [48.6, 11.1], after=True), mv("n10", [41, 19], after=True), ps("b1", [41.6, 19.6], after=True)),
     S("Abschluss: Punkt", "Spieler zehn schießt flach und genau ins Minitor, und das gibt einen Punkt für Spieler zehn. Der Trainer spielt Spieler acht einen neuen Ball zu, und die Folge beginnt von vorn.",
       ps("b1", [35, 8.6]), ps("s2", [48.6, 11.1], after=True))],
    goals=[{"x": 35, "y": 8, "side": "top"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
