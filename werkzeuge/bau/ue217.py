import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 34-P5 (U12-U14, Woche 31 Phase 1): Playing the Penetrating Pass (im PDF "Penetrating That Midfield"). 15 x 20 Yards hochkant =
# Feld x 30.5-69.5, y 5-55 (14 x 18 m), in der Mitte ein Dreieck aus drei Hütchen (nur Hütchen,
# keine Linien, weil die Steigerung ein kleineres Dreieck hat und Fassungen die Linien der Grundform behalten müssen), an jeder Seite ein Minitor.
# Ausrichtung wie im PDF. Pink (6 Angreifer) -> Team Neon, Blau (3 Verteidiger) -> Team Rot, Nummern neu vergeben (im Video
# doppelt): Neon oben 7, 9, 11, unten 4, 6, 5; Rot 2 und 3 im Dreieck, 8 presst. Wie im PDF steht der pressende Verteidiger schon
# unten außerhalb des Dreiecks (3D-Abstand, drei Figuren passen nicht ins Dreieck). Ein Trainer statt zwei, rechts oben.
# Wertung für Team Neon ergänzt (Pass durch das Dreieck = Punkt), im Original nur das Ziel. Inhaltlich verwandt mit UE-152
# (80-P5, Pass durch das Dreieck), aber andere Organisation: Verteidiger im Dreieck, einer darf pressen, vier Minitore für den Konter.
# Sichtkegel aus dem Ton ("Players must be aware and ready for these spaces"): Spieler fünf bzw. Spieler elf schaut vor dem
# Steilpass in die Lücke. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 80, 12, "T")
ERSATZ = [B("s1", 83.6, 15.5), B("s2", 80, 15.5)]
POS = {"n9": (50, 9), "n7": (37, 17), "n11": (63, 17), "n4": (37, 43), "n6": (46, 53), "n5": (64, 48),
       "r2": (45.5, 30), "r3": (54.5, 30), "r8": (55, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
D1, D2, D3 = (50, 15), (38, 39), (62, 39)
K1, K2, K3 = (50, 19), (42, 35), (58, 35)
LINES = [rect(30.5, 5, 39, 50)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}, {"x": 30.5, "y": 30, "side": "left"},
        {"x": 69.5, "y": 30, "side": "right"}]

u = {"title": "Steilpass durch die Mitte", "code": "UE-217", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "14 x 18 m",
 "description": "Sechs gegen drei mit einem Dreieck aus Hütchen in der Mitte. Team Neon steht zu dritt oben und zu dritt unten und will den Ball scharf durch das Dreieck auf die andere Seite spielen. Von Team Rot darf immer nur einer aus dem Dreieck heraus pressen. Erobert Team Rot den Ball, kontert es auf eines der vier Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern, in der Mitte ein Dreieck aus drei Hütchen. An jeder Seite steht ein Minitor.",
  "Verteilen: Sechs von Team Neon, drei oben und drei unten am Rand. Drei von Team Rot im Dreieck. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon lässt den Ball laufen, bis die Verteidiger verschieben und eine Lücke aufgeht. Dann kommt der Pass durch das Dreieck. Immer nur ein Verteidiger darf heraus und pressen, die anderen zwei bleiben im Dreieck.",
  "Wertung: Jeder Pass durch das Dreieck auf die andere Seite gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, darf es auf jedes Minitor kontern, und ein Treffer gibt einen Punkt für Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell passen, damit die Verteidiger verschieben müssen", "Geduldig bleiben, wenn die Passwege zu sind", "Den Pass durch das Dreieck scharf spielen", "Nach Ballgewinn sofort auf ein Minitor kontern"],
 "materials": ["7 Hütchen", "4 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Steilpass durch die Mitte. Team Neon lässt den Ball laufen und spielt im richtigen Moment scharf durch das Dreieck.",
 "board": {"lines": LINES, "goals": TORE, "cones": [C(*D1), C(*D2), C(*D3)], "players": sp(), "balls": [B("b1", 37.6, 43.6)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Team Neon lässt den Ball unten laufen. Spieler vier spielt zu Spieler sechs, der weiter zu Spieler fünf.",
     ps("b1", [46.6, 53.6]), ps("b1", [64.6, 48.6], after=True)),
   S("Einer presst", "Spieler acht presst Spieler fünf. Spieler drei schiebt nach rechts, Spieler zwei nach links. Spieler fünf schaut hoch und sieht: In der Mitte ist eine Lücke.",
     mv("r8", [59, 50]), mv("r3", [57, 31], delay=0.2), mv("r2", [44, 33.5], delay=0.2), bl("n5", [51, 34], after=True)),
   S("Durch das Dreieck: Punkt", "Spieler fünf spielt scharf durch die Lücke zu Spieler sieben, und das gibt einen Punkt für Team Neon. Team Neon behält den Ball. Spieler acht geht zurück ins Dreieck, und jetzt darf ein anderer Verteidiger pressen.",
     ps("b1", [37.6, 17.6]), mv("r8", [52, 41], delay=0.3))],
  "dims": dims(30.5, 69.5, 5, 55, "14 m", "18 m", rx=75)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Pass schnell spielen.", "Schnell durch",
    "Zögert der Spieler am Ball oder spielt zu langsam, sehen die Verteidiger den Pass kommen. Dann fangen sie ihn ab und kontern sofort auf ein Minitor. Darum muss der Pass durch das Dreieck scharf und ohne Zögern kommen.",
    sp(), [B("b1", 63.6, 17.6)] + ERSATZ,
    [S("Zu langsam", "Spieler elf zögert und spielt den Pass zu Spieler vier zu langsam. Spieler drei sieht ihn kommen und fängt den Ball ab.",
       mv("r3", [53, 28]), ps("b1", [53.6, 28.6], delay=0.2)),
     S("Konter: Punkt", "Spieler drei dribbelt sofort los und schießt ins Minitor rechts. Das gibt einen Punkt für Team Rot.",
       dr("r3", "b1", [61, 31]), ps("b1", [69, 30], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Das Dreieck wird kleiner.", "Kleines Dreieck",
    "Jetzt ist das Dreieck kleiner, und der Weg hindurch ist schwerer zu finden. Team Neon lockt den pressenden Verteidiger heraus, spielt um ihn herum und sucht dann schnell die Lücke.",
    sp(r2=(45.8, 31), r3=(54.2, 31)), [B("b1", 64.6, 48.6)] + ERSATZ,
    [S("Herauslocken", "Spieler acht presst Spieler fünf. Spieler fünf spielt an ihm vorbei nach oben zu Spieler elf.",
       mv("r8", [59, 50]), ps("b1", [63.6, 17.6], delay=0.3)),
     S("Lücke sehen", "Spieler drei rückt nach oben, Spieler zwei nach links. Spieler elf schaut in die Mitte und sieht die Lücke.",
       mv("r3", [52, 24]), mv("r2", [44.5, 30]), bl("n11", [50, 31], after=True)),
     S("Schnell durch: Punkt", "Spieler elf spielt schnell durch das kleine Dreieck zu Spieler vier. Das gibt einen Punkt für Team Neon.",
       ps("b1", [37.6, 43.6]))],
    cones=[C(*K1, id="k1"), C(*K2, id="k2"), C(*K3, id="k3")])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
