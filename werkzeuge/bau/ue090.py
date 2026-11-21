import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-7: 15 x 15 Yards (x 26-74, y 6-54), vier innere und vier äußere Stationen. Alle in einer Mannschaft, die Rollen wechseln.
# Die linke Seite ist punktsymmetrisch zur rechten (x -> 100 - x, y -> 60 - y).
T = P("T", "c", 18, 3, "T")
def pm(p): return [round(100 - p[0], 1), round(60 - p[1], 1)]
pos = {"n7": (30.9, 10.7), "n8": (69.1, 10), "n9": (45.6, 22), "n5": (54.7, 22), "n4": (45.3, 38), "n3": (54.4, 38), "n11": (30.9, 49.6), "n2": (69.4, 48.9), "n10": (54.4, 55)}
def sp(**k):
    d = dict(pos); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
cones = ecken(26, 6, 48, 48) + [C(x, y) for x, y in [(33.2, 11.5), (66.6, 11.5), (42.8, 22.6), (57.2, 22.6), (42.8, 37.4), (57.2, 37.4), (33.4, 48.5), (66.8, 48.5)]]
b2 = [B("b2", 71, 49.5), B("c1", 20.6, 3.6)]
# Ablauf rechts (Spieler 2, 8, 5, 3) und gespiegelt links (Spieler 7, 11, 4, 9)
durch = lambda b, z: ps(b, z)
u = {"title": "Doppelpass-Stationen", "code": "UE-090", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Erwärmung"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 9, "players_max": 12, "field_size": "14 x 14 m",
 "description": "Ein Aufwärmen mit vier inneren und vier äußeren Stationen. Ein Außenspieler passt durch zum Außenspieler gegenüber. Ein Innenspieler setzt ihn halb unter Druck, ein anderer kommt ihm entgegen, und die beiden spielen einen Doppelpass um den Störer herum. Dann geht der Ball weiter zur nächsten Station, und alle rücken eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern mit vier Hütchen in den Ecken und vier Hütchen in der Mitte.",
  "Verteilen: An jeder Station ein Spieler, ein Außenspieler mit Ball.",
  "Ablauf: Spieler zwei passt durch zu Spieler acht. Spieler fünf setzt Spieler acht halb unter Druck, Spieler drei kommt entgegen. Spieler acht und Spieler drei spielen einen Doppelpass um Spieler fünf, dann passt Spieler acht durch zu Spieler sieben.",
  "Wechsel: Spieler fünf wird beim nächsten Doppelpass zum Mitspieler, Spieler drei bleibt an der Station von Spieler fünf. So wechseln alle ständig die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Genau passen, damit der Ablauf flüssig bleibt", "Im richtigen Moment zur nächsten Station laufen", "Als Störer echt, aber nur halb unter Druck setzen", "Abwechselnd mit beiden Füßen passen und beim Wechseln miteinander sprechen"],
 "materials": ["12 Hütchen", "2 Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Doppelpass-Stationen. Pass durch, Doppelpass um den Störer und weiter zur nächsten Station.",
 "board": {"lines": [rect(26, 6, 48, 48)], "cones": cones, "players": sp(), "balls": b2,
  "steps": [
   S("Pass durch", "Spieler zwei passt durch zu Spieler acht. Gleichzeitig kommt Spieler drei als Mitspieler entgegen.", ps("b2", [70.6, 11.2]), mv("n3", [62.5, 25], delay=0.3)),
   S("Störer kommt", "Spieler fünf läuft auf Spieler acht zu und setzt ihn halb unter Druck.", mv("n5", [62, 14])),
   S("Doppelpass um den Störer", "Spieler acht spielt zu Spieler drei und läuft hinter Spieler fünf vorbei. Spieler drei spielt direkt in seinen Lauf.",
     ps("b2", [64.1, 25.6]), mv("n8", [63, 7], delay=0.2), mv("n8", [54, 9], after=True), ps("b2", [55.6, 9.6], after=True)),
   S("Weiter und neue Plätze", "Spieler acht passt durch zu Spieler sieben. Gleichzeitig wird Spieler fünf zum nächsten Mitspieler, und Spieler drei geht an die Station von Spieler fünf.",
     ps("b2", [32.5, 11.3]), mv("n5", [45, 14], delay=0.2), mv("n3", [55, 22], delay=0.2))],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "14 m"}, {"x1": 82, "y1": 6, "x2": 82, "y2": 54, "text": "14 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball kommt dazu, beide Seiten spielen gleichzeitig.", "Mit zweitem Ball",
    "Jetzt laufen zwei Bälle gleichzeitig: rechts wie gehabt, links startet Spieler sieben genau spiegelverkehrt. Das verlangt mehr Konzentration, schnellere Reaktionen und sofortiges Nachlaufen zur nächsten Station.",
    sp(), b2[:1] + [B("b7", 29.3, 10.5), B("c1", 20.6, 3.6)],
    [S("Beide passen durch", "Gleichzeitig passt Spieler zwei durch zu Spieler acht und Spieler sieben durch zu Spieler elf. Spieler drei und Spieler neun kommen entgegen.",
       ps("b2", [70.6, 11.2]), ps("b7", pm((70.6, 11.2))), mv("n3", [62.5, 25], delay=0.3), mv("n9", pm((62.5, 25)), delay=0.3)),
     S("Zwei Störer", "Gleichzeitig setzen Spieler fünf und Spieler vier unter Druck.", mv("n5", [62, 14]), mv("n4", pm((62, 14)))),
     S("Zwei Doppelpässe", "Auf beiden Seiten läuft gleichzeitig der Doppelpass um den Störer herum.",
       ps("b2", [64.1, 25.6]), mv("n8", [63, 7], delay=0.2), mv("n8", [54, 9], after=True), ps("b2", [55.6, 9.6], after=True),
       ps("b7", pm((64.1, 25.6))), mv("n11", pm((63, 7)), delay=0.2), mv("n11", pm((54, 9)), after=True), ps("b7", pm((55.6, 9.6)), after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Störer entscheidet selbst, ob er voll presst oder sich fallen lässt.", "Störer wählt den Druck",
    "Der Störer wechselt ab: Mal presst er voll, mal lässt er sich fallen. Presst er voll, braucht der Ballspieler oft einen Kontakt mehr. Lässt er sich fallen, ist der direkte Doppelpass möglich. Der Ballspieler schaut vor dem Pass, was der Störer macht, und entscheidet dann.",
    sp(), b2,
    [S("Pass durch", "Spieler zwei passt durch zu Spieler acht, Spieler drei kommt entgegen.", ps("b2", [70.6, 11.2]), mv("n3", [62.5, 25], delay=0.3)),
     S("Voller Druck", "Spieler fünf presst diesmal voll und kommt ganz nah. Spieler acht nimmt den Ball mit einem Kontakt zur Seite.",
       mv("n5", [64, 12]), dr("n8", "b2", [70, 17], delay=0.2)),
     S("Doppelpass trotzdem", "Dann spielt Spieler acht zu Spieler drei, läuft los und bekommt den Ball zurück.",
       ps("b2", [64.1, 25.6]), mv("n8", [60, 18], delay=0.2), ps("b2", [58.6, 17.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
