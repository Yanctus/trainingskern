import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 49-P2 (U12-U14, Woche 29 Phase 3): Counter Attacking Technical Warm Up (Preparing for the Counter). 40 x 30 Yards =
# Feld x 31-69, y 6-54 (27 x 37 m), Mittellinie gestrichelt, oben zwei Minitore (eins je Hälfte). Ausrichtung wie im PDF.
# Unten je Hälfte fünf Hütchen für die schnellen Füße. Blau (navy) -> Team Neon (2 Läufer, 3 Mitte, 4 Seite, 5/6 warten),
# Pink/Schwarz -> Team Rot (7 Läufer, 8 Mitte, 9 Seite, 10/11 warten); Nummern neu vergeben (im Video gibt es die 4 doppelt).
# Ein Trainer statt zwei (oben zwischen den Toren). Ablauf wie PDF und Video: Hütchenlauf, Doppelpass mit dem Mittelspieler,
# zweiter Doppelpass mit dem Seitenspieler, Abschluss; beide Gruppen gleichzeitig (parallel gezeigt).
# Wertung im Original nicht genannt (Aufwärmen): Treffer = Punkt für den Läufer (ergänzt).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; "checking away" meint die Freilaufbewegung).
T = P("T", "c", 50, 2.5, "T")
POS = {"n2": (29.5, 51), "n5": (21, 51), "n6": (12.5, 51), "n3": (44, 30), "n4": (31, 24),
       "r7": (70.5, 51), "r10": (79, 51), "r11": (87.5, 51), "r8": (56, 30), "r9": (69, 24)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 3), B("s2", 46.4, 3)]
LINES = [rect(31, 6, 38, 48), line(50, 6, 50, 54)]
TORE = [{"x": 37, "y": 6, "side": "top"}, {"x": 63, "y": 6, "side": "top"}]
CONES = [C(x, 51) for x in (33, 36, 39, 42, 45, 55, 58, 61, 64, 67)]

u = {"title": "Zwei Doppelpässe zum Abschluss", "code": "UE-209", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Passspiel", "Torschuss"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 10, "players_max": 12, "field_size": "27 x 37 m",
 "description": "Ein Aufwärmen für schnelle Füße, Doppelpässe und einen schnellen Abschluss. Ein Spieler läuft durch eine Hütchenreihe, mal seitlich, mal vorwärts, mal rückwärts. Dann spielt er einen Doppelpass mit dem Spieler in der Mitte und einen zweiten mit dem Spieler an der Seite und schießt aufs Minitor. Beide Gruppen arbeiten gleichzeitig, jede in ihrer Hälfte.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 37 Metern, in der Mitte längs geteilt. Oben in jeder Hälfte ein Minitor, unten in jeder Hälfte eine Reihe aus fünf Hütchen.",
  "Verteilen: Team Neon links und Team Rot rechts, je ein Spieler in der Mitte mit Ball und einer an der Seite. Die anderen warten unten neben den Hütchen. Der Trainer steht oben zwischen den Toren mit Bällen.",
  "Ablauf: Der Läufer läuft durch die Hütchen und spielt einen Doppelpass mit dem Mittelspieler. Dann bekommt er den Ball noch einmal, spielt einen Doppelpass mit dem Seitenspieler und schießt aufs Minitor. Beide Gruppen laufen gleichzeitig.",
  "Wertung und Wechsel: Ein Treffer gibt einen Punkt für den Läufer. Dann rücken alle eine Rolle weiter: Der Läufer wird Mittelspieler, der Mittelspieler geht an die Seite, und der Seitenspieler joggt zurück zur Gruppe."],
 "organisation_show": ORG,
 "coaching_points": ["Tief in die Knie und schnelle Füße an den Hütchen", "Erst weg vom Ball, dann schnell zum Ball anbieten", "Den Pass genau in den Lauf spielen", "Direkt abschließen, ohne langsamer zu werden"],
 "materials": ["2 Minitore", "10 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zwei Doppelpässe zum Abschluss. Ein Läufer kommt mit schnellen Füßen durch die Hütchen, spielt zwei Doppelpässe und schießt aufs Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(),
  "balls": [B("b1", 44.6, 30.6), B("b2", 56.6, 30.6)] + ERSATZ,
  "steps": [
   S("Schnelle Füße", "Beide Gruppen starten gleichzeitig. Spieler zwei läuft durch die Hütchen, mal seitlich, mal vorwärts, mal rückwärts. Auf der anderen Seite macht Spieler sieben dasselbe.",
     mv("n2", [33, 48]), mv("n2", [36, 54], after=True), mv("n2", [39, 48], after=True), mv("n2", [42, 54], after=True), mv("n2", [45, 48], after=True), mv("n2", [46, 45], after=True),
     mv("r7", [67, 48]), mv("r7", [64, 54], after=True), mv("r7", [61, 48], after=True), mv("r7", [58, 54], after=True), mv("r7", [55, 48], after=True), mv("r7", [54, 45], after=True)),
   S("Erster Doppelpass", "Nach dem letzten Hütchen spielt Spieler drei aus der Mitte zu Spieler zwei, und Spieler zwei spielt direkt zurück. Spieler acht und Spieler sieben machen es genauso.",
     ps("b1", [46.6, 45.6]), ps("b1", [44.6, 30.6], after=True),
     ps("b2", [54.6, 45.6]), ps("b2", [56.6, 30.6], after=True)),
   S("Zweiter Doppelpass", "Spieler zwei macht zwei Schritte zur Seite, und Spieler drei spielt ihn noch einmal an. Spieler zwei passt weiter zu Spieler vier an der Seite. Rechts spielen Spieler acht, Spieler sieben und Spieler neun gleichzeitig.",
     mv("n2", [42, 43]), ps("b1", [42.6, 43.6], after=True), ps("b1", [31.6, 24.6], after=True),
     mv("r7", [58, 43]), ps("b2", [58.6, 43.6], after=True), ps("b2", [69.6, 24.6], after=True)),
   S("Abschluss: Punkt", "Spieler zwei läuft nach vorn, Spieler vier spielt ihm den Ball in den Lauf, und Spieler zwei schießt direkt ins Minitor. Das gibt einen Punkt für Spieler zwei, und Spieler sieben trifft genauso. Dann wird Spieler zwei Mittelspieler, Spieler drei geht an die Seite, Spieler vier joggt zurück zur Gruppe, und Spieler fünf läuft als Nächster.",
     mv("n2", [39, 27]), ps("b1", [39.6, 27.6], delay=0.4), ps("b1", [37.5, 7], after=True),
     mv("r7", [61, 27]), ps("b2", [61.6, 27.6], delay=0.4), ps("b2", [62.5, 7], after=True))],
  "dims": dims(31, 69, 6, 54, "27 m", "37 m", rx=95)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Pass genau in den Lauf spielen.", "Pass in den Lauf",
    "Der Seitenspieler spielt den Ball nicht zum Läufer, sondern vor ihn in den Lauf. So muss der Läufer nicht abbremsen. Er läuft auf den Ball und schießt direkt, ohne den Ball erst anzunehmen.",
    sp(n2=(41, 46), r7=(59, 46)), [B("b1", 31.6, 24.6), B("b2", 69.6, 24.6)] + ERSATZ,
    [S("In den Lauf", "Spieler zwei sprintet los. Spieler vier spielt den Ball nicht zu ihm, sondern ein Stück vor ihn, genau in seinen Lauf. Rechts machen es Spieler neun und Spieler sieben gleichzeitig.",
       mv("n2", [39, 27]), ps("b1", [39.6, 27.6], delay=0.3), mv("r7", [61, 27]), ps("b2", [61.6, 27.6], delay=0.3)),
     S("Direkt schießen: Punkt", "Spieler zwei muss nicht abbremsen und schießt direkt ins Minitor. Das gibt einen Punkt für Spieler zwei. Spieler sieben trifft auch.",
       ps("b1", [37.5, 7]), ps("b2", [62.5, 7]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Erst weg vom Ball, dann schnell anbieten.", "Weg und wieder hin",
    "Wer den Ball haben will, läuft zuerst ein paar Schritte weg und kommt dann schnell zurück zum Ball. So schüttelt er im Spiel seinen Gegenspieler ab. Wichtig ist der richtige Moment: Der Pass kommt genau dann, wenn er sich anbietet.",
    sp(n2=(41, 46), r7=(59, 46)), [B("b1", 41.6, 46.6), B("b2", 59.6, 46.6)] + ERSATZ,
    [S("Weg vom Ball", "Spieler vier läuft erst ein paar Schritte weg vom Ball und kommt dann schnell zurück. Spieler neun macht es auf der anderen Seite genauso.",
       mv("n4", [32, 15]), mv("n4", [35, 25], after=True), mv("r9", [68, 15]), mv("r9", [65, 25], after=True)),
     S("Anbieten: Punkt", "Genau jetzt passt Spieler zwei zu ihm. Spieler vier legt den Ball direkt in den Lauf von Spieler zwei, und Spieler zwei schießt ins Minitor. Das gibt einen Punkt für Spieler zwei. Rechts spielen Spieler sieben und Spieler neun genauso.",
       ps("b1", [35.6, 25.6]), mv("n2", [39, 24], after=True), ps("b1", [39.6, 24.6], after=True, delay=0.2), ps("b1", [37.5, 7], after=True),
       ps("b2", [65.6, 25.6]), mv("r7", [61, 24], after=True), ps("b2", [61.6, 24.6], after=True, delay=0.2), ps("b2", [62.5, 7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
