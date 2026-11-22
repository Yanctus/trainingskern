import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 98-P1: 15 x 20 Yards, gedreht: Feld x 21-79, y 8.25-51.75. Knallbonbon: Dreiecke an beiden Enden, Mittelfeld x 34.5-65.6, y 22-38.9 mit Hütchenreihen,
# Minitore an den inneren Enden (links Öffnung nach rechts, rechts Öffnung nach links). Rot läuft gespiegelt (x -> 100 - x, y -> 60 - y).
T = P("T", "c", 50, 3, "T")
def mi(p): return [round(100 - p[0], 1), round(60 - p[1], 1)]
xs = [42.9, 47.7, 52.5, 57.1]
cones = [C(22.9, 21.8), C(22.9, 38.4), C(28.5, 30.5), C(34.5, 22.2), C(34.5, 38.9), C(65.6, 21.8), C(65.6, 38.6), C(71.2, 30.7), C(77, 22.2), C(77, 38.7)] \
      + [C(x, 22) for x in xs] + [C(x, 38.9) for x in xs]
L = lambda a, b, c, d: line(a, b, c, d, dashed=False)
lines = [rect(21, 8.25, 58, 43.5), rect(34.5, 22, 31.1, 16.8), L(22.9, 21.8, 22.9, 38.4), L(22.9, 21.8, 34.5, 38.9), L(22.9, 38.4, 34.5, 22.2),
         L(77, 22.2, 77, 38.7), L(77, 22.2, 65.6, 38.6), L(77, 38.7, 65.6, 21.8)]
goals = [{"x": 33.5, "y": 30.5, "side": "left"}, {"x": 66.6, "y": 30.5, "side": "right"}]
def sp(**k):
    d = dict(n10=(18.5, 17.5), r4=(18.5, 42.5), n8=(81.5, 17.5), r9=(81.5, 42.5)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
weg1 = [(28, 20), (34.5, 26.5), (44.1, 25.5), (46.5, 18.5), (48.9, 18.5)]
weg2 = [(51.3, 25.5), (53.6, 25.5), (56, 18.5), (58.4, 18.5), (61, 24), (74, 26), (74, 33)]
rein = [(70, 42), (61, 42), (61, 34)]
def drw(who, ball, pts, spiegel=False):
    return [dr(who, ball, mi(p) if spiegel else list(p), after=i > 0 or None) for i, p in enumerate(pts)]
u = {"title": "Knallbonbon-Rennen", "code": "UE-085", "kind": "Spielform",
 "focuses": ["Dribbling", "1 gegen 1", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 4, "players_max": 12, "field_size": "18 x 14 m",
 "description": "Ein Wettrennen auf einer Strecke in Form eines Knallbonbons. Zwei Spieler starten an gegenüberliegenden Enden, dribbeln durch die Hütchen bis zum anderen Ende, laufen dort um ein Hütchen und rennen in das Mittelfeld. Wer zuerst drin ist, wird Angreifer, der andere verteidigt. Dann wird eins gegen eins auf die Minitore gespielt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern. Mit Hütchen eine Strecke in Form eines Knallbonbons stellen: ein Dreieck an jedem Ende, dazwischen das Mittelfeld mit je einer Hütchenreihe an beiden Seiten. An den inneren Enden des Mittelfelds je ein Minitor.",
  "Verteilen: Zwei Mannschaften. Jede Mannschaft hat an beiden Enden eine Startposition, jeder Spieler mit Ball.",
  "Ablauf: Zwei Spieler starten gleichzeitig an gegenüberliegenden Enden. Beide dribbeln durch die Strecke bis zum anderen Ende, laufen um ein Hütchen und rennen ins Mittelfeld. Der Erste dort ist Angreifer und behält seinen Ball, der Zweite wird Verteidiger.",
  "Danach: Nach dem Eins gegen Eins holen sich beide einen neuen Ball und stellen sich wieder an, das nächste Paar startet."],
 "organisation_show": ORG,
 "coaching_points": ["Beim Dribbeln durch die Hütchen den Ball eng führen", "Beide Füße benutzen, um schneller zu werden", "Scharf um die Hütchen drehen", "Im Eins gegen Eins mit eigener Technik vorbei und genau statt hart schießen"],
 "materials": ["20 Hütchen", "2 Minitore", "Bälle für alle Spieler", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Knallbonbon-Rennen. Zwei Spieler dribbeln um die Wette, und wer zuerst im Mittelfeld ist, greift an.",
 "board": {"lines": lines, "cones": cones, "goals": goals, "players": sp(), "balls": [B("b10", 20.1, 18.1), B("b9", 79.9, 41.9), B("c1", 52.5, 3.6)],
  "steps": [
   S("Beide dribbeln los", "Spieler zehn und Spieler neun starten gleichzeitig an gegenüberliegenden Enden und dribbeln durch die Hütchen.",
     *drw("n10", "b10", weg1), *drw("r9", "b9", weg1, True)),
   S("Um das Hütchen am Ende", "Beide dribbeln weiter durch die Reihe und laufen am anderen Ende um das Hütchen.",
     *drw("n10", "b10", weg2), *drw("r9", "b9", weg2, True)),
   S("Wer ist zuerst drin", "Spieler zehn ist zuerst im Mittelfeld und wird Angreifer. Spieler neun lässt seinen Ball liegen und verteidigt.",
     *drw("n10", "b10", rein), mv("r9", mi((70, 42)), delay=0.3), mv("r9", mi((61, 42)), after=True), mv("r9", [40, 28], after=True)),
   S("Eins gegen eins", "Spieler zehn dribbelt mit einem Haken an Spieler neun vorbei und schießt ins Minitor, und das gibt einen Punkt für Neon.",
     dr("n10", "b10", [50, 36]), dr("n10", "b10", [44, 31], after=True), mv("r9", [45, 34.5]), ps("b10", [32.6, 30.5], after=True))],
  "dims": [{"x1": 21, "y1": 58.6, "x2": 79, "y2": 58.6, "text": "18 m"}, {"x1": 91, "y1": 8.25, "x2": 91, "y2": 51.75, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit kurzen, schnellen Bewegungen den Verteidiger loswerden.", "Kurz antäuschen, dann weg",
    "Im Eins gegen Eins hilft eine kurze, schnelle Bewegung: kurz in eine Richtung antäuschen, dann mit dem Ball in den freien Raum ziehen. So hat der Angreifer Platz und kann in Ruhe genau ins Minitor schießen.",
    sp(n8=(52, 36), r4=(43, 28), n10=(18.5, 17.5), r9=(81.5, 42.5)), [B("b8", 50.4, 36.6), B("c1", 52.5, 3.6)],
    [S("Antäuschen", "Spieler acht täuscht mit dem Ball nach unten an. Spieler vier geht mit.", dr("n8", "b8", [48, 38]), mv("r4", [44, 33], delay=0.2)),
     S("Haken und weg", "Mit einem kurzen Haken zieht Spieler acht nach oben in den freien Raum.", dr("n8", "b8", [47, 30]), dr("n8", "b8", [41, 25], after=True)),
     S("Genau abschließen", "Spieler acht schießt genau ins Minitor, und das gibt einen Punkt für Neon.", ps("b8", [32.6, 30]))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach einem Tor kommt ein Mitspieler dazu, dann heißt es zwei gegen eins.", "Nach dem Tor zwei gegen eins",
    "Trifft eine Mannschaft im Eins gegen Eins, darf sofort ein zweiter Spieler dieser Mannschaft mit Ball ins Mittelfeld. Jetzt greifen die beiden zu zweit gegen einen Verteidiger das andere Minitor an und können einen Extrapunkt holen.",
    sp(n10=(41, 27), r9=(50, 34)), [B("b10", 39.4, 27.6), B("b8", 79.9, 18.1), B("c1", 52.5, 3.6)],
    [S("Tor im Eins gegen Eins", "Spieler zehn schießt ins Minitor, und das gibt einen Punkt für Neon.", ps("b10", [32.6, 30])),
     S("Mitspieler kommt dazu", "Sofort dribbelt Spieler acht ins Mittelfeld, und Spieler zehn läuft mit nach vorn. Jetzt steht es zwei gegen eins.",
       dr("n8", "b8", [72, 18]), dr("n8", "b8", [61, 18], after=True), dr("n8", "b8", [60, 25], after=True), mv("n10", [55, 36]), mv("r9", [57, 28], delay=0.3)),
     S("Extrapunkt", "Spieler acht passt quer zu Spieler zehn, und der schießt ins andere Minitor. Das gibt einen Extrapunkt für Neon.",
       ps("b8", [56.6, 36.6]), ps("b8", [67.6, 31], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
