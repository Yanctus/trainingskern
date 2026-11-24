import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 61-P12 (U15-U17, Woche 27 Phase 2): 3 v 1 Transfer Rondos. Feld nach der Skizze 20 x 15 Yards = 18 x 14 m (der PDF-Text nennt
# 20 x 25 Yards, der Ton 15 x 20 Yards; die Skizze geht vor). Drei mal drei Zonen, gespielt wird in der mittleren Reihe.
# LANGES FELD QUER (Verhältnis 1,3): Feld x 9-89, y 4-51 wie im PDF (nicht gedreht). In der Länge 4,4 Einheiten je Meter, in der
# Tiefe 3,4 (die Tafel ist flacher); so stehen die neun Spieler der mittleren Reihe in einem Raster mit 9 Einheiten Abstand (3D).
# Drei Teams zu dritt: Navy (links, 7, 10, 6) und Hellblau (rechts, 8, 4, 10) sind beide Team Neon (die Passteams), Rot (Video) bzw.
# Pink (PDF) sind die Verteidiger = Team Rot. Neu nummeriert, weil doppelt: hellblau 10 -> 11, rot 7 -> 3, rot 10 -> 5 (9 bleibt).
# Die zwei goldenen Verbindungsspieler sind Springer (F), oben und unten in der mittleren Spalte. Ein Trainer statt zwei.
# Grundform nach Video 0:10-0:30: rot 7 (hier 3) presst links, 7 -> 6 -> 10, 10 -> Springer oben -> rechts zu 8, rot 10 (hier 5)
# geht ins rechte Feld; Ballgewinn rechts, Rollentausch (Team Rot spielt rechts weiter, die Ballverlierer gehen in die Mitte).
# Fassungen: PDF Key Coaching Point (ganze Zone nutzen) und Progression (Minitore oben und unten in der Mitte, drei gegen drei nach
# Ballgewinn; es verteidigen ein Spieler aus jedem Passteam und ein Springer, Regeln nach dem Ton).
# Keine Punktwertung im Original für die Grundform; Ziel: fünf Pässe, dann Übergabe ins andere Feld.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft): „receive on the back foot“ ist offene Körperstellung, kein Schulterblick.
# Kein Dubletten-Fall: UE-369 (61-P11) ist 5 gegen 4 plus 3 auf einem langen Feld, UE-110 (28-P3) 4 gegen 3 mit Übergabe,
# UE-125 (61-P4) und UE-201 (61-P6) sind andere Übungen.
T = P("T", "c", 80, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 83.5, 55.8), B("s2", 86, 55.8)]
X0, X1, Y0, Y1 = 9, 89, 4, 51
SX = [round(X0 + (X1 - X0) * i / 3, 2) for i in (1, 2)]
SY = [round(Y0 + (Y1 - Y0) * i / 3, 2) for i in (1, 2)]
NEON = {"n7": (12.5, 27), "n6": (21.5, 32.5), "n10": (31, 23), "n8": (67, 23), "n4": (76, 32), "n11": (85, 26)}
ROT = {"r3": (40, 30), "r9": (49, 24), "r5": (58, 31)}
SPR = {"f1": (49, 7.5), "f2": (49, 44)}
def sp(**k):
    d = {**NEON, **ROT, **SPR}; d.update(k)
    team = lambda i: "a" if i[0] == "n" else ("b" if i[0] == "r" else "t")
    return [P(i, team(i), x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, d=None): x, y = (d or {**NEON, **ROT, **SPR})[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(X0, Y0, X1 - X0, Y1 - Y0)] + [line(x, Y0, x, Y1) for x in SX] + [line(X0, y, X1, y) for y in SY]
DIMS = dims(X0, X1, Y0, Y1, "18 m", "14 m", rx=94)
TORE = [{"x": 49, "y": Y0, "side": "top"}, {"x": 49, "y": Y1, "side": "bottom"}]
BALL = [B("b1", *fuss("n7"))] + ERSATZ

u = {"title": "Doppel-Rondo mit Übergabe", "code": "UE-375", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 11,
 "field_size": "18 x 14 m",
 "description": "Links und rechts läuft je ein Rondo drei gegen eins, in der Mitte wartet Team Rot. Nach fünf Pässen spielt das Team mit Ball über einen Springer ins andere Feld, und dort presst sofort ein neuer Verteidiger. Erobert Team Rot den Ball, tauscht es mit den drei Spielern, die ihn verloren haben.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern, in drei mal drei Zonen geteilt. Gespielt wird in der mittleren Reihe. Oben und unten in der Mitte steht je ein Springer.",
  "Verteilen: Drei Teams zu dritt. Links und rechts stehen je drei Spieler von Team Neon, links ist der Ball. Team Rot wartet in der Mitte. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Ein Spieler von Team Rot presst im Feld mit Ball, dort heißt es drei gegen eins. Nach fünf Pässen geht der Ball über einen Springer ins andere Feld. Ist er drüben, geht dort ein neuer Verteidiger rein, und der erste läuft zurück in die Mitte.",
  "Wechsel: Erobert Team Rot den Ball, tauscht es mit den drei Spielern, die ihn verloren haben. Die Springer werden alle paar Minuten getauscht, damit jeder die Rolle einmal spielt."],
 "organisation_show": ORG,
 "coaching_points": ["Breit stehen und die ganze Zone nutzen", "Kurz und scharf passen", "Springer nimmt mit dem hinteren Fuß an und spielt gleich weiter", "Ball weg? Sofort umschalten"],
 "materials": ["Hütchen für neun Zonen", "2 Minitore für die Steigerung", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Doppel-Rondo mit Übergabe. Zwei Rondos drei gegen eins, und nach fünf Pässen wandert der Ball über einen Springer ins andere Feld.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": BALL,
  "steps": [
   S("Drei gegen eins im linken Feld", "Links haben Spieler sieben, sechs und zehn den Ball. Aus der Mitte geht Spieler drei rein und presst allein. Fünf Pässe muss das Team in seinem Feld schaffen.",
     mv("r3", [20, 26]), ps("b1", fuss("n6"), delay=0.4), ps("b1", fuss("n10"), after=True)),
   S("Fünf Pässe, dann über den Springer", "Der fünfte Pass ist da. Spieler zehn spielt hoch zum Springer. Der nimmt mit dem hinteren Fuß an und spielt gleich weiter ins rechte Feld zu Spieler acht. Jetzt geht Spieler fünf dort rein, und Spieler drei läuft zurück in die Mitte.",
     ps("b1", fuss("f1")), ps("b1", fuss("n8"), after=True), mv("r5", [71, 30], after=True), mv("r3", [40, 30], delay=0.6)),
   S("Rechts das Gleiche", "Rechts lassen Spieler acht, vier und elf den Ball laufen. Spieler fünf jagt ihn.",
     ps("b1", fuss("n11")), mv("r5", [81, 22.5], after=True), ps("b1", fuss("n4"), delay=1.2)),
   S("Ballgewinn: Rollen tauschen", "Spieler vier will zurück zu Spieler acht. Spieler fünf läuft in den Pass und hat den Ball. Jetzt wird getauscht. Spieler neun und Spieler drei kommen dazu, Team Rot spielt rechts weiter. Spieler acht, vier und elf gehen in die Mitte und sind die neuen Verteidiger.",
     mv("r5", [72.4, 28.4]), ps("b1", [73, 29], delay=0.2),
     mv("n8", [58, 22], after=True), mv("n4", [49, 33], after=True), mv("n11", [64, 34], after=True),
     mv("r9", [67, 16], after=True), mv("r9", [84, 22], after=True), mv("r3", [56, 40], after=True), mv("r3", [80, 36], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die ganze Zone nutzen.", "Die ganze Zone nutzen",
    "Stehen die drei eng zusammen, hat es der Verteidiger leicht. Darum gehen sie auseinander, bis an die Linien ihrer Zone. Dann muss er weite Wege gehen, und es gibt immer einen freien Passweg.",
    sp(), BALL,
    [S("Weit auseinander", "Spieler drei kommt ins Feld. Sofort gehen Spieler sieben, sechs und zehn auseinander, bis an die Linien ihrer Zone.",
       mv("r3", [23, 27.5]), dr("n7", "b1", [12, 21.8], delay=0.2), mv("n6", [23, 34], delay=0.2), mv("n10", [33.5, 21.8], delay=0.2)),
     S("Am Verteidiger vorbei", "Spieler drei läuft Spieler sieben an und macht den Weg zu Spieler zehn zu. Also geht der Ball runter zu Spieler sechs und von dort hoch zu Spieler zehn. Der Verteidiger läuft nur hinterher.",
       mv("r3", [17.5, 21.5]), ps("b1", [23.6, 34.6], delay=0.5), ps("b1", [34.1, 22.4], after=True), mv("r3", [27, 25], after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Minitore und drei gegen drei.", "Minitore, drei gegen drei",
    "Oben und unten in der Mitte steht je ein Minitor. Erobert Team Rot den Ball, kontert es sofort zu dritt. Ein Spieler aus jedem Passteam und ein Springer verteidigen das Minitor. Trifft Team Rot, tauscht es mit dem Team, das den Ball verloren hat. Holen die drei Verteidiger den Ball zurück, bleibt Team Rot in der Mitte.",
    sp(), BALL,
    [S("Ballgewinn im linken Feld", "Spieler drei presst links. Spieler sieben will zu Spieler zehn, aber Spieler drei geht dazwischen und hat den Ball.",
       mv("r3", [22, 25.1]), ps("b1", [22.6, 25.7], delay=0.6)),
     S("Drei gegen drei aufs Minitor", "Jetzt geht es schnell. Spieler drei dribbelt los, Spieler neun und Spieler fünf starten Richtung Minitor unten. Spieler sechs, Spieler vier und der Springer laufen zurück und verteidigen.",
       dr("r3", "b1", [30, 36]), mv("r9", [44, 38], delay=0.2), mv("r5", [58, 41], delay=0.2),
       mv("n6", [36, 44], delay=0.3), mv("n4", [65, 45], delay=0.3), mv("f2", [44, 47.5], delay=0.3)),
     S("Abschluss: Punkt", "Spieler drei spielt zu Spieler neun, und der legt quer auf Spieler fünf. Spieler fünf schiebt ins Minitor, und das gibt einen Punkt für Team Rot. Danach tauscht Team Rot mit dem Team, das den Ball verloren hat.",
       ps("b1", [44.6, 38.6]), ps("b1", [58.6, 41.6], after=True), ps("b1", [51, 50.7], after=True))],
    goals=TORE, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
