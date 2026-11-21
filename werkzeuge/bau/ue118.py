import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 9v9-P7: 40 x 30 Yards, gedreht (Neon spielt nach rechts): Feld x 8-92, y 8-52, Tore links und rechts, Springer oben und unten außen.
T = P("T", "c", 4, 52, "T")
CB = [B("c1", 6.5, 52.6), B("c2", 3, 55.5)]
POS = {"n1": (11, 30), "n4": (25, 31), "n5": (36, 15), "n6": (32, 49), "n8": (60, 25), "n10": (66, 41),
       "r12": (89, 31), "r7": (76, 31), "r2": (69, 12), "r3": (75, 48), "r9": (45, 24), "r11": (42, 42), "f1": (54, 5), "f2": (54, 55)}
def sp(d=None):
    d = dict(d or POS)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
TORE = [{"x": 8, "y": 30, "side": "left"}, {"x": 92, "y": 30, "side": "right"}]
V1 = {"n1": (11, 30), "n4": (40, 50), "n5": (20, 11), "n6": (19, 49), "n8": (40, 30), "n10": (63, 38),
      "r12": (89, 31), "r7": (56, 22), "r2": (66, 12), "r3": (74, 46), "r9": (29, 21), "r11": (30, 40), "f1": (54, 5), "f2": (54, 55)}
u = {"title": "Aufbauen mit zwei Springern", "code": "UE-118", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 14, "field_size": "37 x 27 m",
 "description": "Zwei Teams mit je sechs Spielern samt Torhüter spielen auf zwei Tore, an beiden langen Seiten steht ein Springer. Das Team am Ball muss erst fünf Pässe spielen und dabei mindestens einmal einen Springer einbinden, bevor es abschließen darf. So üben die Spieler den Aufbau von hinten, gute Passwege und den Abschluss.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 27 Metern mit einem Tor links und rechts. An der oberen und unteren Seitenlinie steht je ein Springer.",
  "Verteilen: Team Neon und Team Rot mit je einem Torhüter und fünf Feldspielern. Die Springer spielen immer mit dem Team am Ball.",
  "Ablauf: Team Neon baut von hinten auf. Nach fünf Pässen, bei denen ein Springer mitgespielt hat, darf es aufs rechte Tor abschließen. Erobert Team Rot den Ball, muss es nur einmal mit einem Springer kombinieren und darf dann abschließen.",
  "Wechsel: Nach einiger Zeit werden die Springer getauscht, damit jeder einmal außen spielt. Jedes Tor gibt einen Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Mit guten Pässen den Ball in den eigenen Reihen halten", "Wenn nach vorn nichts geht, über die hinterste Reihe neu aufbauen", "Die Passwege zum Springer nicht zustellen", "Freien Raum erkennen und nutzen und kaltschnäuzig abschließen"],
 "materials": ["2 Tore", "Hütchen für das Feld", "Mehrere Bälle beim Trainer", "Leibchen in drei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Aufbauen mit zwei Springern. Fünf Pässe, einmal über den Springer, dann darf aufs Tor geschossen werden.",
 "board": {"lines": [rect(8, 8, 84, 44)], "goals": TORE, "players": sp(), "balls": [B("b1", 12.6, 30.6)] + CB,
  "steps": [
   S("Aufbau von hinten", "Der Torhüter Neon eins spielt zu Neon vier, und Neon vier spielt weiter zu Neon fünf. Das sind zwei Pässe.",
     ps("b1", [23.4, 31.6]), ps("b1", [34.4, 15.6], after=True)),
   S("Über den Springer", "Neon fünf spielt zum Springer oben, und der Springer spielt direkt zu Neon acht. Jetzt sind es vier Pässe, und ein Springer war dabei.",
     ps("b1", [52.4, 5.6]), ps("b1", [58.4, 25.6], after=True)),
   S("Pass in den Lauf", "Gleichzeitig startet Neon zehn in die Tiefe, und Neon acht spielt ihm den Ball in den Lauf. Das ist der fünfte Pass.",
     mv("n10", [80, 42]), ps("b1", [81.6, 42.6], delay=0.4)),
   S("Abschluss", "Neon zehn schließt direkt ab und trifft ins rechte Tor. Das gibt einen Punkt für Team Neon.",
     ps("b1", [91.5, 36]))],
  "dims": [{"x1": 8, "y1": 58.6, "x2": 92, "y2": 58.6, "text": "37 m"}, {"x1": 97, "y1": 8, "x2": 97, "y2": 52, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Torhüter spielt mutig durch die Lücke.", "Durch die Lücke",
    "Laufen die beiden vorderen Gegner den Torhüter an und lassen dabei eine Lücke zwischen sich, spielt der Torhüter mutig und genau durch diese Lücke zum Mittelfeldspieler. Der dreht auf, und Team Neon hat den ersten Druck schon überspielt.",
    sp(V1), [B("b1", 12.6, 30.6)] + CB,
    [S("Gegner laufen an", "Gleichzeitig laufen Rot neun und Rot elf den Torhüter an. Zwischen ihnen entsteht eine große Lücke.",
       mv("r9", [24, 23]), mv("r11", [25, 37])),
     S("Durch die Lücke", "Der Torhüter spielt flach durch die Lücke zu Neon acht. Neon acht dreht auf und spielt weiter zu Neon zehn.",
       ps("b1", [38.4, 30.6]), ps("b1", [61.4, 38.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell zum Springer spielen und nachrücken.", "Schnell über den Springer",
    "Wer unter Druck ist, spielt schnell zum Springer. Gleichzeitig sprinten die Mitspieler mit vollem Tempo nach vorn, damit der Springer sie sofort anspielen kann. So entsteht ein schneller Angriff, der mit einem guten Abschluss endet.",
    sp(), [B("b1", 33.6, 49.6)] + CB,
    [S("Schnell zum Springer", "Neon sechs spielt sofort zum Springer unten.",
       ps("b1", [52.4, 54.6])),
     S("Nachrücken mit Tempo", "Gleichzeitig sprinten Neon zehn und Neon acht nach vorn. Der Springer spielt Neon zehn in den Lauf.",
       mv("n10", [78, 40]), mv("n8", [78, 22]), ps("b1", [79.6, 40.6], delay=0.4)),
     S("Abschluss", "Neon zehn schließt ab und trifft. Das gibt einen Punkt für Team Neon.",
       ps("b1", [91.5, 34]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
