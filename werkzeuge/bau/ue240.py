import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 87-P8 (U12-U14, Woche 39 Phase 2): Possession in a Diamond Setup. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), durch die
# Diagonalen (gestrichelt) in vier Dreiecke geteilt, oben und unten ein Minitor. Pink (im PDF Ballbesitz) -> Team Neon: 9 oben,
# 8 links, 10 rechts, 4 unten, je einer pro Dreieck. Blau -> Team Rot, Nummern neu (im PDF doppelt): 5 und 6 pressen, 2 und 3
# warten links und rechts draußen. Ablauf wie im Video (9-8-4, dann weiter bis zehn Pässe, Abschluss). Positionen auf ein
# Spaltenraster gesetzt (3D-Abstand). Ein Trainer statt zwei. Coaching-Punkt „Passwinkel schaffen" aus dem Video ("Create effective
# passing angles"), Steigerung = Progression 1 (4 gegen 3, sechs Pässe, mit dem Ballgewinn aus dem Video). Progression 2 (Torhüter
# in Toren spielen mit, 6 gegen 3) weggelassen: die Minitore müssten zu Jugendtoren werden, das erlaubt die Fassung nicht.
# Kein Dublette: UE-111 „Knack den Code" ist eine Passfolge mit Code, UE-054 „Ausbruch aus der Raute" ein 1 gegen 3 im Dribbling.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 17, 47, "T")
POS = {"n9": (52, 13), "n8": (33, 30), "n10": (67, 30), "n4": (50, 47), "r5": (43.5, 27), "r6": (58.5, 36), "r2": (17, 30), "r3": (83, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 20.6, 50.5), B("s2", 17, 50.5)]
LINES = [rect(25, 5, 50, 50), line(25, 5, 75, 55), line(75, 5, 25, 55)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}]

u = {"title": "Ballbesitz in vier Dreiecken", "code": "UE-240", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Ein Rondo vier gegen zwei in einem Quadrat, das durch die Diagonalen in vier Dreiecke geteilt ist. In jedem Dreieck steht ein Spieler des Teams am Ball, zwei Gegner pressen zu zweit, zwei weitere warten draußen. Nach zehn Pässen in Folge darf das Team am Ball in eines der beiden Minitore schießen. Nach einem Treffer wechseln die Verteidiger mit den Wartenden, und wer den Ball erobert, ist selbst am Ball.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, mit Hütchen oder Linien entlang der Diagonalen in vier Dreiecke geteilt. Oben und unten steht ein Minitor.",
  "Verteilen: Team Neon mit vier Spielern, einer in jedem Dreieck. Von Team Rot pressen zwei im Feld, zwei warten links und rechts draußen. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon lässt den Ball durch die Dreiecke laufen und zählt laut mit. Jeder bleibt in seinem Dreieck. Die zwei Verteidiger pressen zu zweit.",
  "Wertung und Wechsel: Nach zehn Pässen darf Team Neon in ein Minitor schießen, das gibt einen Punkt. Dann tauschen die Verteidiger mit den Wartenden. Erobern die Verteidiger den Ball, kommen ihre zwei Mitspieler dazu, und zwei von Team Neon gehen raus."],
 "organisation_show": ORG,
 "coaching_points": ["Im eigenen Dreieck so stehen, dass ein Passweg frei ist", "Laut mitzählen und ansagen, wann abgeschlossen wird", "Mit einem oder zwei Kontakten spielen und die Verteidiger zum Ball locken", "Als Verteidiger zu zweit pressen und die Passwege zumachen"],
 "materials": ["2 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Ballbesitz in vier Dreiecken. Team Neon spielt zehn Pässe durch die Dreiecke und darf dann aufs Minitor schießen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 52.6, 13.6)] + ERSATZ,
  "steps": [
   S("Pass eins", "Team Neon hat den Ball, und jeder bleibt in seinem Dreieck. Spieler neun spielt zu Spieler acht, und alle zählen laut mit: eins! Spieler fünf läuft sofort an.",
     ps("b1", [33.6, 30.6]), mv("r5", [37, 26], delay=0.3)),
   S("Am Verteidiger vorbei", "Spieler acht spielt am Verteidiger vorbei nach unten zu Spieler vier: zwei! Jetzt läuft Spieler sechs an.",
     ps("b1", [50.6, 47.6]), mv("r6", [47, 40], delay=0.3)),
   S("Weiter zählen", "Spieler vier spielt weiter zu Spieler zehn: drei! So läuft der Ball durch alle Dreiecke, bis zehn Pässe geschafft sind.",
     ps("b1", [67.6, 30.6]), mv("r6", [58.5, 36], delay=0.3)),
   S("Zehn, Abschluss: Punkt", "Zehn! Spieler zehn spielt zu Spieler neun, und der schießt ins obere Minitor. Das gibt einen Punkt für Team Neon. Dann tauschen Spieler fünf und Spieler sechs mit Spieler zwei und Spieler drei von draußen.",
     ps("b1", [52.6, 13.6]), ps("b1", [50, 5.5], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=91)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einen Passwinkel schaffen.", "Passwinkel schaffen",
    "Steht ein Verteidiger im Passweg, wartet der Mitspieler nicht, sondern bewegt sich in seinem Dreieck, bis der Weg frei ist. So hat der Spieler am Ball immer eine Anspielstation.",
    sp(r6=(58.5, 39)), [B("b1", 50.6, 47.6)] + ERSATZ,
    [S("Passweg zu", "Spieler vier hat den Ball. Aber Spieler sechs steht genau im Passweg zu Spieler zehn.",
       mv("r5", [45, 36])),
     S("Winkel frei", "Spieler zehn bewegt sich in seinem Dreieck ein Stück nach unten. Jetzt ist der Passweg frei, und Spieler vier spielt zu ihm.",
       mv("n10", [69, 41]), ps("b1", [69.6, 41.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Vier gegen drei.", "Vier gegen drei",
    "Jetzt pressen drei Verteidiger, nur einer wartet draußen. Dafür reichen schon sechs Pässe für den Abschluss. Erobert Team Rot den Ball, kommt der Wartende dazu, und ein Spieler von Team Neon geht raus. Dann presst Team Neon zu dritt.",
    sp(n10=(69, 32), r2=(60.5, 20)), [B("b1", 33.6, 30.6)] + ERSATZ,
    [S("Zu zweit anlaufen", "Jetzt pressen drei. Spieler acht spielt zu Spieler neun, und Spieler zwei und Spieler fünf laufen ihn gemeinsam an.",
       ps("b1", [52.6, 13.6]), mv("r2", [57, 16], delay=0.3), mv("r5", [46, 19], delay=0.3)),
     S("Abgefangen: Wechsel", "Spieler neun will nach rechts passen, aber Spieler zwei fängt den Ball ab. Jetzt ist Team Rot am Ball. Spieler drei kommt von draußen dazu, Spieler neun geht raus, und Team Neon presst zu dritt.",
       ps("b1", [57.6, 16.6]), mv("r3", [72, 44], delay=0.4))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
