import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 87-P5 (U15-U17, Woche 26 Phase 4): Transitional Rondo. 20 x 20 Yards = 18 x 18 m, Feld x 25-75, y 5-55, in der Mitte eine
# Raute von 10 x 10 Yards (9 m Seitenlänge, gestrichelt; keine Hütchen an den Spitzen gezeichnet, sie lägen in den Passwegen). Ausrichtung wie im PDF.
# Keine Dublette: UE-111 (87-P1, Raute vor Minitor mit Code), UE-240 (87-P8, vier Dreiecke), UE-362 (49-P5, 5 gegen 3 im
# Längsfeld), UE-054, UE-150, UE-313 haben andere Organisation (kein 4 gegen 2 in einer Raute mit Umschalten ins 6 gegen 4).
# PDF pink (zwei Jäger und vier außen) -> Team Neon, im PDF ohne Nummern: Jäger 6 und 8, außen 7 (oben), 11 (rechts),
# 9 (unten), 2 (links). PDF blau (vier in der Raute, einer mit „10“) -> Team Rot 3 (links), 4 (oben), 5 (rechts), 10 (unten).
# Die Rot-Spieler stehen an den Spitzen der Raute (etwas in die Breite gezogen), die Jäger zwischen ihnen, die Spieler außen
# nicht mittig an den Seiten, sondern versetzt (3D-Abstand). Ein Trainer statt zwei, rechts unten neben dem Feld.
# Grundform nach PDF/Video: 4 gegen 2, Ballgewinn, Pass nach außen, 6 gegen 4, zehn Pässe gibt einen Punkt (PDF „E.g 10 passes“),
# Ballgewinn von Team Rot = Ball zurück in die Raute. Annahme: Danach jagen wieder zwei von Team Neon in der Raute.
# Fassungen: Coaching-Punkt aus PDF/Ton („Use the full field in the 6 v 4 - stretch the defenders“), Steigerung aus PDF Seite 2
# (vier Minitore, Team Rot bricht nach zehn Pässen aus; der Key Coaching Point mit acht Pässen für Team Neon steht im Text).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 82, 50, "T")
ERSATZ = [B("s1", 85.5, 50.6), B("s2", 82.6, 53.6)]
POS = {"r3": (33, 30), "r4": (50, 14), "r5": (67, 30), "r10": (50, 46), "n6": (41.5, 30), "n8": (58.5, 30),
       "n7": (62, 5), "n11": (75, 13), "n9": (38, 55), "n2": (25, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
RAUTE = [line(50, 12, 32, 30), line(32, 30, 50, 48), line(50, 48, 68, 30), line(68, 30, 50, 12)]
LINES = [rect(25, 5, 50, 50)] + RAUTE
CONES = []
DIMS = dims(25, 75, 5, 55, "18 m", "18 m", rx=91)
NACH_GEWINN = dict(n6=(35, 14), n8=(62, 46))

u = {"title": "Aus der Raute ins 6 gegen 4", "code": "UE-374", "kind": "Spielform",
 "focuses": ["Umschalten", "Passspiel", "Verteidigen"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "18 x 18 m",
 "description": "Ein Rondo vier gegen zwei in einer Raute mitten im Feld. Erobern die zwei Jäger den Ball, spielen sie sofort raus zu ihren vier Mitspielern außen, und im ganzen Feld wird sechs gegen vier gespielt. Holt sich Team Rot den Ball zurück, muss er sofort wieder in die Raute. Wer zehn Pässe schafft, bekommt einen Punkt.",
 "organisation": ["Aufbauen: Ein Quadrat von 18 mal 18 Metern. In der Mitte eine Raute mit neun Metern Seitenlänge, mit Hütchen abgesteckt.",
  "Verteilen: Team Rot steht zu viert an den Spitzen der Raute, zwei von Team Neon jagen drinnen den Ball. Die anderen vier von Team Neon verteilen sich außen an den Seiten. Der Trainer steht mit Bällen neben dem Feld.",
  "Ablauf: Team Rot hält in der Raute den Ball. Erobert Team Neon ihn, geht er sofort raus, und alle spielen im ganzen Feld sechs gegen vier. Erobert Team Rot den Ball zurück, spielt es ihn sofort in die Raute, und das Vier gegen zwei beginnt neu.",
  "Wertung: Zehn Pässe am Stück geben einen Punkt, in der Raute für Team Rot, im ganzen Feld für Team Neon. Die Jäger in der Raute werden regelmäßig getauscht."],
 "organisation_show": ORG,
 "coaching_points": ["Sauber und flach passen, dann bleibt der Ball", "Ohne Ball bewegen, immer einen Passweg anbieten", "Ball verloren? Sofort umschalten", "Im Sechs gegen vier breit machen und die Seite wechseln"],
 "materials": ["Hütchen für Feld und Raute", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aus der Raute ins Sechs gegen Vier. Ein Rondo vier gegen zwei, und sobald der Ball erobert ist, geht das Spiel aufs ganze Feld.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 33.6, 30.6)] + ERSATZ,
  "steps": [
   S("Vier gegen zwei in der Raute", "In der Raute hält Team Rot den Ball. Spieler drei spielt zu Spieler vier. Die zwei Jäger von Team Neon schieben mit.",
     ps("b1", [50.6, 14.6]), mv("n6", [41.5, 25], delay=0.3)),
   S("Abgefangen", "Spieler vier will weiter zu Spieler fünf. Spieler acht ahnt den Pass, springt dazwischen und hat den Ball.",
     mv("n8", [58.5, 22]), ps("b1", [59.1, 22.6], delay=0.2)),
   S("Sofort raus, alle gehen breit", "Jetzt schnell. Spieler acht spielt sofort raus zu Spieler elf. Beide Jäger verlassen die Raute und suchen sich Platz.",
     ps("b1", [75.6, 13.6]), mv("n6", [35, 14], delay=0.3), mv("n8", [62, 46], delay=0.3)),
   S("Sechs gegen vier im ganzen Feld", "Jetzt spielt Team Neon sechs gegen vier, im ganzen Feld. Der Ball läuft über Spieler sieben zu Spieler sechs. Team Rot muss jetzt viel laufen.",
     ps("b1", [62.6, 5.6]), mv("r4", [55, 18], delay=0.3), mv("r5", [69, 20], delay=0.3), mv("r3", [42, 22], delay=0.5),
     ps("b1", [35.6, 14.6], after=True)),
   S("Zehn Pässe: Punkt", "Weiter auf die andere Seite zu Spieler zwei und zu Spieler neun. Schafft Team Neon zehn Pässe am Stück, gibt das einen Punkt für Team Neon. Holt sich Team Rot den Ball, geht er sofort zurück in die Raute, und zwei von Team Neon jagen dort wieder.",
     ps("b1", [25.6, 47.6]), ps("b1", [38.6, 55.6], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im Sechs gegen vier breit machen.", "Breit machen, Seite wechseln",
    "Im Sechs gegen vier läuft keiner zum Ball. Die Spieler bleiben weit auseinander, bis an die Linien. Schiebt Team Rot auf eine Seite, geht der Ball schnell auf die andere.",
    sp(**NACH_GEWINN), [B("b1", 75.6, 13.6)] + ERSATZ,
    [S("Team Rot schiebt zum Ball", "Spieler elf hat den Ball. Team Rot schiebt zu viert auf diese Seite. Auf der anderen Seite wird es frei.",
       mv("r3", [44, 26]), mv("r4", [52, 10]), mv("r5", [66, 21]), mv("r10", [53, 34])),
     S("Weg vom Druck, auf die freie Seite", "Spieler elf spielt nicht in den Druck. Der Ball geht zu Spieler acht, über Spieler neun und rüber zu Spieler zwei. Der hat jetzt richtig Platz.",
       ps("b1", [62.6, 46.6]), ps("b1", [38.6, 55.6], after=True), ps("b1", [25.6, 47.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Vier Minitore rund ums Feld.", "Vier Minitore",
    "An jeder Seite steht ein Minitor. Schafft Team Rot in der Raute zehn Pässe, darf es ausbrechen und auf jedes Minitor schießen. Im Sechs gegen vier darf Team Neon nach acht Pässen auf jedes Minitor abschließen.",
    sp(), [B("b1", 50.6, 14.6)] + ERSATZ,
    [S("Zehn Pässe in der Raute", "Team Rot zählt laut mit. Spieler vier spielt den zehnten Pass zu Spieler fünf.",
       ps("b1", [67.6, 30.6])),
     S("Ausbrechen und abschließen: Punkt", "Jetzt darf Team Rot raus. Spieler fünf dribbelt aus der Raute und schießt ins Minitor, und das gibt einen Punkt für Team Rot.",
       dr("r5", "b1", [71, 30]), ps("b1", [75, 30.3], after=True))],
    goals=[{"x": 50, "y": 5, "side": "top"}, {"x": 75, "y": 30, "side": "right"}, {"x": 50, "y": 55, "side": "bottom"},
           {"x": 25, "y": 30, "side": "left"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
