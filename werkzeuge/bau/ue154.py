import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P2 (U12-U14, Woche 10 Phase 5): Defending as a Pair. 15 x 15 Yards = Feld x 25-75, y 5-55 (14 m), Kanal in der Mitte
# (4 Yards, x 44.5-56.7, gestrichelt). Pink (5 Ballbesitz) -> Neon 3, 4, 8, 7, 6; Blau (Paar) -> Rot 9, 11.
# Spieler sechs etwas tiefer (3D-Abstand). Steigerung mit je einem Minitor oben und unten am Kanal (wie im Video). Ein Trainer.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 85, 50, "T")
POS = {"n3": (23.5, 39.2), "n4": (36.9, 54.5), "n8": (35.2, 16.1), "n7": (63.4, 13.6), "n6": (61.5, 46),
       "r9": (35.4, 33.5), "r11": (56, 29.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 86.6, 53.5), B("s2", 83, 53.5)]
LINES = [rect(25, 5, 50, 50), line(44.5, 5, 44.5, 55), line(56.7, 5, 56.7, 55)]

u = {"title": "Zu zweit pressen im Rondo", "code": "UE-154", "kind": "Spielform",
 "focuses": ["Verteidigen", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 7, "field_size": "14 x 14 m",
 "description": "Fünf gegen zwei im Quadrat, in der Mitte ein schmaler Kanal. Team Neon lässt den Ball laufen und sucht den Pass quer durch den Kanal zu einem Mitspieler, das sind zwei Punkte. Zehn Pässe in Folge sind ein Punkt. Die beiden Verteidiger pressen als Paar: Einer geht auf den Ball, der andere stellt die Passwege zu, und ein Ballgewinn bringt ihnen zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern mit einem Kanal von knapp 4 Metern in der Mitte.",
  "Verteilen: Fünf von Team Neon am Rand, links und rechts vom Kanal. Zwei Verteidiger von Team Rot in der Mitte. Der Trainer steht am Rand mit Bällen.",
  "Ablauf: Team Neon lässt den Ball schnell laufen und spielt quer durch den Kanal, sobald es geht. Das Paar presst gemeinsam und will die Fünf in eine Ecke drängen.",
  "Wertung: Pass durch den Kanal zwei Punkte, zehn Pässe ein Punkt. Ballgewinn zwei Punkte für Rot, dazu ein Punkt für je zwei Pässe danach. Nach Ballverlust presst Team Neon sofort. Die Verteidiger regelmäßig wechseln."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, der andere sichert ab und stellt die Passwege zu", "Gemeinsam den Gegner in eine Ecke drängen", "Lücken für den Pass durch den Kanal erkennen und geduldig bleiben", "Nach Ballverlust sofort zurückpressen"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zu zweit pressen im Rondo. Fünf gegen zwei, und die beiden Verteidiger arbeiten als Paar gegen den Pass durch die Mitte.",
 "board": {"lines": LINES, "cones": [], "players": sp(), "balls": [B("b1", 24.1, 39.8)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Spieler drei spielt zu Spieler vier. Spieler neun und Spieler elf schieben mit.",
     ps("b1", [37.5, 55.1]), mv("r9", [36.5, 42], delay=0.3), mv("r11", [57.5, 38], delay=0.3)),
   S("Pressen, Lücke", "Spieler neun presst Spieler vier, aber Spieler elf schiebt zu spät mit. Im Kanal ist eine Lücke.",
     mv("r9", [36, 47]), mv("r11", [55, 40], delay=0.4)),
   S("Durch den Kanal: Punkte", "Spieler vier sieht die Lücke und spielt quer durch den Kanal zu Spieler sechs. Das gibt zwei Punkte für Team Neon. Team Neon behält den Ball und spielt weiter, die Verteidiger werden regelmäßig gewechselt.",
     ps("b1", [62.1, 46.6]))],
  "dims": dims(25, 75, 5, 55, "14 m", "14 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, einer sichert.", "Pressen im Paar",
    "Der Verteidiger am Ball presst und drängt den Gegner in eine Ecke. Der zweite stellt sich so, dass der Pass durch den Kanal zu ist. Muss der Gegner trotzdem passen, fängt der zweite den Ball ab.",
    sp(), [B("b1", 24.1, 39.8)] + ERSATZ,
    [S("Einer presst, einer sichert", "Spieler neun presst Spieler drei. Spieler elf stellt sich so, dass der Weg durch den Kanal zu ist.",
       mv("r9", [29, 36]), mv("r11", [50, 40], delay=0.2)),
     S("In der Ecke: Ballgewinn", "Spieler drei spielt zu Spieler vier, und Spieler neun drängt ihn sofort in die Ecke. Spieler vier will durch den Kanal passen, aber Spieler elf fängt den Ball ab. Das gibt zwei Punkte für Team Rot.",
       ps("b1", [37.5, 55.1]), mv("r9", [33, 49], after=True), mv("r11", [50, 50.2], after=True), ps("b1", [50.6, 50.8], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Minitore für die Verteidiger.", "Minitore für Rot",
    "Oben und unten am Kanal steht jetzt je ein Minitor. Erobert das Paar den Ball, schießt es sofort darauf. So haben die Verteidiger direkt nach dem Ballgewinn ein klares Ziel.",
    sp(), [B("b1", 64, 14.2)] + ERSATZ,
    [S("Pressen und zustellen", "Spieler sieben hat den Ball. Spieler elf presst ihn, und Spieler neun stellt den Passweg zu Spieler acht zu.",
       mv("r11", [60, 21]), mv("r9", [44, 17], delay=0.2)),
     S("Abfangen, Minitor: Punkt", "Spieler sieben spielt trotzdem zu Spieler acht, aber Spieler neun fängt den Ball ab und schießt sofort ins obere Minitor. Das gibt einen Punkt für Team Rot.",
       ps("b1", [44.6, 17.4]), dr("r9", "b1", [48, 10], after=True), ps("b1", [50.6, 5.3], after=True))],
    goals=[{"x": 50.6, "y": 5, "side": "top"}, {"x": 50.6, "y": 55, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
