import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 94-P6: 20 x 25 Yards, gedreht: Feld x 22.5-77.5, y 8-52. Vier Minitore (je zwei an beiden Enden), 4 gegen 4 plus 4 Springer (2 an den Enden, 2 innen).
T = P("T", "c", 8, 52, "T")
goals = [{"x": 22.5, "y": 17.5, "side": "left"}, {"x": 22.5, "y": 42.5, "side": "left"}, {"x": 77.5, "y": 17.5, "side": "right"}, {"x": 77.5, "y": 42.5, "side": "right"}]
lines = [rect(22.5, 8, 55, 44), line(50, 8, 50, 52), line(22.5, 30, 77.5, 30)]
def sp(**k):
    d = dict(n9=(36, 14), n11=(34, 42), n8=(55, 50), n10=(72, 12), r2=(45, 26), r3=(44.5, 42), r6=(63, 24), r7=(73, 46.5)); d.update(k)
    F = [P("fL", "t", 19.5, 30, "F"), P("fR", "t", 80.5, 30, "F"), P("f5", "t", 54, 32, "F"), P("f9", "t", 64, 40, "F")]
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + F + [T]
cb = [B("c1", 10.6, 52.6), B("c2", 6, 55)]
fuenf_a = [ps("b1", [55.6, 32.6]), ps("b1", [35.6, 42.6], after=True)]
fuenf_b = [ps("b1", [56.6, 50.6]), ps("b1", [65.6, 40.6], after=True), ps("b1", [73.6, 12.6], after=True)]
u = {"title": "Alle Tore zusperren", "code": "UE-092", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 18 m",
 "description": "Vier gegen vier mit vier Springern auf vier Minitore. Erst nach fünf Pässen darf eine Mannschaft auf ein Minitor schießen. Trifft sie, ist dieses Tor für sie gesperrt, und sie muss eines der anderen treffen. Wer zuerst alle vier Tore gesperrt hat, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern mit je zwei Minitoren an beiden Enden.",
  "Verteilen: Zwei Mannschaften mit je vier Spielern und vier Springer: je einer an den beiden Enden und zwei im Feld. Die Springer spielen immer mit der Mannschaft am Ball.",
  "Ablauf: Nach fünf Pässen darf die Mannschaft am Ball auf ein beliebiges Minitor schießen. Ein Treffer gibt einen Punkt und sperrt dieses Tor für die Mannschaft. Erobert der Gegner den Ball, braucht er selbst erst fünf Pässe.",
  "Sieger und Wechsel: Wer zuerst alle vier Tore gesperrt hat, gewinnt. Die Verlierer tauschen mit den Springern."],
 "organisation_show": ORG,
 "coaching_points": ["Umschauen und sich ohne Ball frei laufen", "Wissen, welche Tore schon gesperrt sind und welche noch offen", "Als Verteidiger kompakt stehen und den Gegner zu den gesperrten Toren drängen", "Nach Ballgewinn schnell umschalten und ruhig fünf Pässe spielen"],
 "materials": ["4 Minitore", "4 Hütchen", "Leibchen in drei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Alle Tore zusperren. Fünf Pässe, dann ein Treffer, und jedes getroffene Tor ist danach gesperrt.",
 "board": {"lines": lines, "cones": ecken(22.5, 8, 55, 44), "goals": goals, "players": sp(), "balls": [B("b1", 37.6, 14.6)] + cb,
  "steps": [
   S("Pässe sammeln", "Neon spielt mit den Springern: Spieler neun passt zum Springer in der Mitte, der zu Spieler elf. Das sind schon zwei Pässe.", *fuenf_a),
   S("Fünf Pässe geschafft", "Weiter geht es über Spieler acht und den zweiten Springer zu Spieler zehn. Jetzt sind es fünf Pässe, und Neon darf schießen.", *fuenf_b),
   S("Tor und gesperrt", "Spieler zehn trifft ins Minitor oben rechts, und das gibt einen Punkt für Neon. Ab jetzt ist dieses Tor für Neon gesperrt.", ps("b1", [78.5, 17.5]))],
  "dims": [{"x1": 22.5, "y1": 58.6, "x2": 77.5, "y2": 58.6, "text": "23 m"}, {"x1": 90, "y1": 8, "x2": 90, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Vor dem Abschluss muss der Ball über einen Endspieler laufen.", "Ablage vom Endspieler",
    "Jetzt darf nur geschossen werden, wenn vorher ein Springer an einem Ende den Ball abgelegt hat. Das verlangt Timing und gute Laufwege. Die Verteidiger lernen dabei, den Pass nach vorn zu blocken und kompakt zu stehen.",
    sp(), [B("b1", 73.6, 12.6)] + cb,
    [S("Pass zum Endspieler", "Spieler zehn passt zum Springer am rechten Ende und startet sofort.", ps("b1", [78.9, 30.6]), mv("n10", [71, 22], delay=0.2)),
     S("Ablage", "Der Springer legt direkt ab in den Lauf von Spieler zehn.", ps("b1", [72.6, 22.6])),
     S("Abschluss: Punkt", "Spieler zehn schießt ins Minitor oben rechts, und das gibt einen Punkt für Neon.", ps("b1", [78.5, 17.5]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Tor ist erst gesperrt, wenn danach noch fünf Pässe gelingen.", "Erst fünf Pässe sperren",
    "Nach einem Treffer bleibt die Mannschaft am Ball, der Trainer spielt sofort einen neuen Ball ein. Erst wenn danach fünf Pässe gelingen, ist das Tor wirklich gesperrt. Die Gegner pressen deshalb besonders früh, um das zu verhindern.",
    sp(), [B("b1", 73.6, 12.6)] + cb,
    [S("Treffer", "Spieler zehn trifft ins Minitor oben rechts, und das gibt einen Punkt für Neon.", ps("b1", [78.5, 17.5])),
     S("Neuer Ball, Rot presst", "Sofort spielt der Trainer einen neuen Ball zu Spieler elf. Gleichzeitig pressen die Roten früh.",
       ps("c1", [35.6, 42.6]), mv("r3", [40, 40], delay=0.2), mv("r2", [38, 30], delay=0.2)),
     S("Fünf Pässe: gesperrt", "Neon spielt sich trotzdem fünfmal den Ball zu, und erst jetzt ist das Tor für Neon gesperrt.",
       ps("c1", [56.6, 50.6]), ps("c1", [65.6, 40.6], after=True), ps("c1", [55.6, 32.6], after=True), ps("c1", [37.6, 14.6], after=True), ps("c1", [73.6, 12.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
