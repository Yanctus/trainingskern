import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 68-P2: 20 x 15 Yards, gedreht: Feld x 10-90, y 8-52, Mittellinie x 50. Rechts ein Minitor (2 Punkte), links zwei Minitore (je 1 Punkt).
T = P("T", "c", 40, 3, "T")
CB = [B("c1", 42.5, 3.6)]
POS = {"n2": (22, 55), "n3": (68, 4), "n4": (34, 22), "r7": (93, 16), "r8": (24, 38)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(10, 8, 80, 44), line(50, 8, 50, 52)]
TORE = [{"x": 90, "y": 30, "side": "right"}, {"x": 10, "y": 21, "side": "left"}, {"x": 10, "y": 38, "side": "left"}]
CONES = [C(24, 52), C(70, 8), C(90, 12)]
u = {"title": "Selbst gehen oder abspielen", "code": "UE-124", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Verteidigen", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "18 x 14 m",
 "description": "Ein Angreifer von Team Neon bekommt den Ball und muss sich entscheiden: Er geht selbst ins eins gegen eins und schießt aufs rechte Minitor, das gibt zwei Punkte. Oder er spielt quer zum Mitspieler in der anderen Hälfte, der auf zwei Minitore spielt, das gibt einen Punkt. Der Verteidiger von Team Rot versucht, so schnell und eng zu verteidigen, dass der Angreifer nicht selbst gehen will.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern, in zwei Hälften geteilt. Rechts ein Minitor, links zwei Minitore.",
  "Verteilen: Team Neon und Team Rot starten an verschiedenen Hütchen rund um das Feld, wie im Bild. Der Trainer hat die Bälle.",
  "Ablauf: Der Pass von unten links zum Angreifer ist das Startsignal für den Verteidiger. Der Angreifer geht selbst aufs rechte Minitor oder spielt quer zum Mitspieler, der links eins gegen eins auf zwei Minitore spielt.",
  "Wechsel: Wenn jeder einmal dran war, gewinnt das Team mit den meisten Punkten."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball verlagern, um den Verteidiger aus dem Gleichgewicht zu bringen", "Den Mitspieler sehen und mit ihm zusammenspielen", "Schnell Risiko und Lohn abwägen", "Als Verteidiger schnell und eng Druck machen, damit der Angreifer abspielen muss oder einen Fehler macht"],
 "materials": ["3 Minitore", "Hütchen für Feld und Startplätze", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Selbst gehen oder abspielen. Wer selbst trifft, holt zwei Punkte, über den Mitspieler gibt es einen.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": [B("b1", 23.6, 55.6)] + CB,
  "steps": [
   S("Anspiel", "Neon zwei spielt diagonal zu Neon drei, der in die rechte Hälfte läuft. Der Pass ist das Signal für Rot sieben.",
     mv("n3", [66, 12]), ps("b1", [67.6, 12.6], delay=0.3), mv("r7", [78, 20], delay=0.6)),
   S("Selbst gehen", "Neon drei entscheidet sich für das eins gegen eins und dribbelt auf Rot sieben zu. Rot sieben kommt heraus.",
     dr("n3", "b1", [70, 20]), mv("r7", [76, 23], delay=0.2)),
   S("Vorbei und Abschluss", "Neon drei zieht nach unten an Rot sieben vorbei und schießt ins rechte Minitor. Das gibt zwei Punkte für Team Neon.",
     dr("n3", "b1", [72, 34]), dr("n3", "b1", [78, 38], after=True), ps("b1", [89.5, 31], after=True))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "18 m"}, {"x1": 97, "y1": 8, "x2": 97, "y2": 52, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Verteidiger macht schnell und eng Druck.", "Eng verteidigen",
    "Kommt der Verteidiger schnell und eng an den Angreifer heran, traut sich dieser das eins gegen eins nicht zu und spielt lieber quer. Dann gibt es höchstens noch einen Punkt. Für den Verteidiger ist das schon ein kleiner Sieg.",
    sp(n3=(66, 12), r7=(76, 20)), [B("g", 67.6, 12.6), B("b1", 23.6, 55.6)] + CB,
    [S("Eng heran", "Rot sieben läuft schnell und eng an Neon drei heran.",
       mv("r7", [70, 16])),
     S("Quer zum Mitspieler", "Neon drei traut sich nicht und spielt quer zu Neon vier in die andere Hälfte. Gleichzeitig kommt Rot acht heraus.",
       ps("g", [35.6, 22.6]), mv("r8", [28, 30], delay=0.3)),
     S("Eins gegen eins links", "Neon vier dribbelt an Rot acht vorbei und trifft ins obere Minitor. Das gibt nur einen Punkt für Team Neon.",
       dr("n4", "g", [26, 16]), ps("g", [10.5, 21], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Übertreibt der Verteidiger, wird schnell gedreht.", "Schnell drehen",
    "Läuft der Verteidiger zu stürmisch heran, lockt der Angreifer ihn noch näher und dreht dann blitzschnell ab. So entkommt er dem Druck und schließt ins Minitor ab. Das gibt zwei Punkte.",
    sp(n3=(60, 26), r7=(69, 30)), [B("g", 61.6, 26.6), B("b1", 23.6, 55.6)] + CB,
    [S("Verteidiger übertreibt", "Rot sieben stürmt auf Neon drei zu und kommt zu nah heran.",
       mv("r7", [63, 28])),
     S("Drehen und Abschluss", "Neon drei dreht scharf weg, lässt Rot sieben stehen und schießt ins Minitor. Das gibt zwei Punkte für Team Neon.",
       dr("n3", "g", [58, 34]), dr("n3", "g", [70, 42], after=True), ps("g", [89.5, 33], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
