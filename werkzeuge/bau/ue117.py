import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-17: 25 x 20 Yards, gedreht (Lauf von links nach rechts): Feld x 10-90, y 8-52. Bahn Rot oben (y 18), Bahn Neon unten (y 42).
# Pro Bahn: drei Ringe, je ein oranges und ein gelbes Reaktionshütchen links und rechts der Bahn, vier Slalomstangen.
T = P("T", "c", 24, 30, "T")
NL, RL = 44, 16
POS = {"r7": (14, RL), "r8": (5, RL), "n2": (14, NL), "n3": (5, NL)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
RINGE = [{"type": "circle", "x": x, "y": y, "r": 2.8} for y in (RL, NL) for x in (25, 31.5, 38)]
LINES = [rect(10, 8, 80, 44)] + RINGE
CONES = [C(53, RL - 6), C(53, RL + 6, "neon"), C(53, NL + 6), C(53, NL - 6, "neon")] + [C(x, y, "neon", shape="stange") for y in (RL, NL) for x in (60, 67, 74, 81)]
def ringe(i, y): return [mv(i, [45, y])]
def slalom(i, y, s):
    return [mv(i, [x, y + s * d], after=True) for x, d in ((60, 4), (67, -4), (74, 4), (81, -4))] + [mv(i, [90, y], after=True)]
def chain(i, pts): return [mv(i, list(p), after=k > 0 or None) for k, p in enumerate(pts)]
def aussen(L, s): return [(49.5, L + 10 * s), (57, L + 8.5 * s), (55, L)]
def aussen_v(L, s): return [(49.5, L + 10 * s), (57, L + 8.5 * s), (56, L + 2 * s)]
def innen(L, s): return [(57.5, L - 7 * s), (53, L - 10 * s), (49, L - 7 * s), (55, L)]
u = {"title": "Schnelle Füße, schnelle Reaktion", "code": "UE-117", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "Erwärmung"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 10, "field_size": "23 x 18 m",
 "description": "Zwei Teams laufen nebeneinander durch je eine Bahn: schnelle Füße durch die Ringe, dann ruft der Trainer eine Farbe, und die Spieler sprinten um das passende Hütchen. Danach geht es im Slalom durch die Stangen und im Sprint ins Ziel. So werden Füße, Reaktion und Tempo aufgewärmt.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern mit zwei Bahnen. In jeder Bahn drei Ringe, daneben ein oranges und ein gelbes Hütchen, dann vier Slalomstangen.",
  "Verteilen: Zwei Teams mit je vier Spielern, Team Rot an der oberen Bahn, Team Neon an der unteren. Der Trainer steht zwischen den Bahnen.",
  "Ablauf: Gleichzeitig läuft aus jedem Team ein Spieler mit schnellen Füßen durch die Ringe. Danach ruft der Trainer Orange oder Gelb, und beide sprinten um das passende Hütchen, durch den Slalom und ins Ziel.",
  "Wechsel: Wer im Ziel ist, läuft locker zurück, und der Nächste startet. Zwischen den Läufen kurz erholen."],
 "organisation_show": ORG,
 "coaching_points": ["Saubere Technik bei den schnellen Füßen", "Schnelle Richtungswechsel um die Stangen", "Sofort auf den Ruf des Trainers reagieren", "Zwischen den Läufen kurz erholen"],
 "materials": ["6 Ringe", "2 orange und 2 gelbe Hütchen", "8 Stangen"],
 "access": "frei", "hidden": True,
 "say_intro": "Schnelle Füße, schnelle Reaktion. Durch die Ringe, auf Zuruf um das richtige Hütchen und im Slalom ins Ziel.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [],
  "steps": [
   S("Schnelle Füße", "Gleichzeitig laufen Neon zwei und Rot sieben mit schnellen, kleinen Schritten durch die drei Ringe.",
     *ringe("n2", NL), *ringe("r7", RL)),
   S("Trainer ruft Orange", "Der Trainer ruft Orange. Beide sprinten sofort um das orange Hütchen herum und zurück in ihre Bahn.",
     *chain("n2", aussen(NL, 1)), *chain("r7", aussen(RL, -1))),
   S("Slalom und Sprint ins Ziel", "Gleichzeitig laufen beide im Slalom durch die Stangen und sprinten ins Ziel. Wer zuerst ankommt, holt einen Punkt für sein Team.",
     mv("n2", [57, NL]), *slalom("n2", NL, 1), mv("r7", [57, RL]), *slalom("r7", RL, -1))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "23 m"}, {"x1": 96, "y1": 8, "x2": 96, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft eine Farbe, aber zuerst geht es um das andere Hütchen.", "Erst das Gegenteil",
    "Jetzt wird umgedreht: Ruft der Trainer Orange, laufen die Spieler zuerst um das gelbe Hütchen und erst dann um das orange. Das verlangt schnelles Denken unter Zeitdruck.",
    sp(n2=(45, NL), r7=(45, RL)), [],
    [S("Erst das andere Hütchen", "Der Trainer ruft Orange. Gleichzeitig sprinten beide zuerst um das gelbe Hütchen herum.",
       *chain("n2", aussen_v(NL, -1)), *chain("r7", aussen_v(RL, 1))),
     S("Dann das gerufene", "Jetzt laufen beide um das orange Hütchen herum, bevor es in den Slalom geht.",
       *chain("n2", innen(NL, -1)), *chain("r7", innen(RL, 1)))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zum Schluss ein diagonaler Sprint.", "Diagonal und abklatschen",
    "Nach dem Lauf sprinten die Spieler diagonal über das Feld zum Endhütchen der anderen Bahn und dann zurück zum eigenen Team, wo sie den Nächsten abklatschen. Das macht das Aufwärmen noch intensiver.",
    sp(), [],
    [S("Diagonal sprinten", "Neon zwei sprintet diagonal zum Ende der oberen Bahn. Kurz danach sprintet Rot sieben diagonal zum Ende der unteren Bahn.",
       mv("n2", [92, RL]), mv("r7", [92, NL], delay=0.5)),
     S("Zurück und abklatschen", "Beide sprinten auf demselben Weg zurück zu ihrem Team und klatschen den Nächsten ab.",
       mv("n2", [16, NL]), mv("r7", [16, RL], delay=0.5))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
