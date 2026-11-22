import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 92-P3: Kreis mit 30 Yards Durchmesser (Mitte 50/30, r 26), Minitore links und rechts, in jedem Tor zwei Hütchen kurz innerhalb der Pfosten.
T = P("T", "c", 84, 6, "T")
def sp(*l): return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, x, y in l] + [T]
cb = [B("c1", 81.5, 6.6), B("c2", 86.5, 7.6)]
kreis = {"type": "circle", "x": 50, "y": 30, "r": 26}
goals = [{"x": 24, "y": 30, "side": "left"}, {"x": 76, "y": 30, "side": "right"}]
hp = [(24.8, 26.8), (24.8, 33.2), (75.2, 26.8), (75.2, 33.2)]
cones = [C(x, y) for x, y in hp]
u = {"title": "Flach und genau ins Tor", "code": "UE-077", "kind": "Spielform",
 "focuses": ["Torschuss", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 6, "field_size": "Kreis, 27 m Durchmesser",
 "description": "Drei gegen drei in einem Kreis mit einem Minitor auf jeder Seite, ohne Torwart. In jedem Tor stehen zwei Hütchen kurz innerhalb der Pfosten. Ein Tor zählt nur, wenn vorher jeder Spieler des Teams am Ball war und der Ball flach, also unter Hütchenhöhe, zwischen den Hütchen ins Tor geht.",
 "organisation": ["Aufbauen: Ein Kreis mit etwa 27 Metern Durchmesser, zum Beispiel der Mittelkreis. Links und rechts je ein Minitor, darin zwei Hütchen etwa einen halben Meter innerhalb der Pfosten.",
  "Verteilen: Zwei Teams mit je drei Spielern, kein Torwart. Der Trainer steht mit vielen Bällen am Rand.",
  "Ablauf: Jedes Team greift ein Tor an. Vor dem Abschluss muss jeder Spieler des Teams den Ball berührt haben. Ein Tor zählt nur flach zwischen den Hütchen, auch wenn der Ball dabei ein Hütchen trifft. Geht der Ball aus dem Kreis oder fällt ein Tor, spielt der Trainer sofort einen neuen Ball ein.",
  "Runden: Drei bis vier Spiele von je vier Minuten, jedes mit einer anderen Regel. Zum Beispiel nur zwei Kontakte, Abschluss nur direkt, nach jedem Tor muss ein anderer Spieler treffen, oder nur mit dem schwächeren Fuß."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und fest abschließen, genau zwischen die Hütchen", "Mit schnellen Kombinationen Platz schaffen", "Sich ohne Ball klug bewegen, um anspielbar zu sein", "Gegner herauslocken und um sie herum spielen, dabei viel miteinander sprechen"],
 "materials": ["2 Minitore", "4 orange Hütchen für die Tore", "Hütchen für den Kreis, falls kein Mittelkreis da ist", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Flach und genau ins Tor. Drei gegen drei im Kreis, und ein Tor zählt nur flach zwischen den Hütchen.",
 "board": {"lines": [kreis], "cones": cones, "goals": goals,
  "players": sp(("n2", 36, 15), ("n3", 45.3, 31.4), ("n4", 36, 42.7), ("r5", 63.6, 21), ("r6", 54.5, 38), ("r7", 63.9, 39.3)),
  "balls": [B("b1", 37.6, 43.3)] + cb,
  "steps": [
   S("Kombinieren", "Spieler vier spielt zu Spieler drei, und der leitet direkt zu Spieler zwei weiter.", ps("b1", [46.9, 32]), ps("b1", [37.6, 15.6], after=True)),
   S("Starten und anspielen", "Spieler drei startet sofort in den freien Raum, und Spieler zwei spielt ihn an. Jetzt waren alle drei am Ball.",
     mv("n3", [60, 30]), ps("b1", [61.6, 30.6], delay=0.4)),
   S("Flach zwischen die Hütchen", "Spieler drei schießt flach und fest zwischen die beiden Hütchen ins Tor, und das gibt einen Punkt für Neon.", ps("b1", [76.5, 30])),
   S("Neuer Ball vom Trainer", "Sofort spielt der Trainer einen neuen Ball ein, diesmal zu Spieler fünf, und es geht weiter.", ps("c1", [62, 21.6]))],
  "dims": [{"x1": 24, "y1": 58.6, "x2": 76, "y2": 58.6, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Trifft der Ball ein Hütchen und geht trotzdem ins Tor, zählt er.", "Hütchen getroffen zählt",
    "Prallt der Schuss vom Hütchen ins Tor, ist es ein Tor. Danach stellt der Schütze das Hütchen wieder genau an seinen Platz. So bleiben alle bei der Sache und üben, den Ball flach und genau zu schießen statt einfach drauf.",
    sp(("n2", 40, 16), ("n3", 64, 26), ("n4", 40, 44), ("r5", 55, 14), ("r6", 52, 38), ("r7", 66, 44)),
    [B("b1", 65.6, 26.6)] + cb,
    [S("Vom Hütchen ins Tor", "Spieler drei schießt, der Ball prallt vom Hütchen ins Tor. Auch das zählt, und das gibt einen Punkt für Neon.",
       ps("b1", [74.4, 27]), ps("b1", [76.5, 29.5], after=True), ps("k3", [75.6, 24.4], after=True)),
     S("Hütchen zurückstellen", "Danach stellt Spieler drei das Hütchen genau an seinen Platz zurück, bevor es weitergeht.",
       mv("n3", [70, 22]), ps("k3", [75.2, 26.8], after=True))],
    cones=[C(x, y, id=f"k{i + 1}") for i, (x, y) in enumerate(hp)]),
  V("Steigerung", "Und jetzt die Steigerung: Tore zählen nur mit dem schwächeren Fuß.", "Nur mit dem schwachen Fuß",
    "In dieser Runde darf nur mit dem schwächeren Fuß aufs Tor geschossen werden. Das ist schwerer, verbessert aber Gleichgewicht, Technik und Selbstvertrauen. Wer gern mit rechts schießt, legt sich den Ball vorher auf links.",
    sp(("n2", 50, 13), ("n3", 62, 10), ("n4", 34, 44), ("r5", 40, 28), ("r6", 56, 40), ("r7", 66, 26)),
    [B("b1", 64.4, 26.6)] + cb,
    [S("Rot kombiniert", "Spieler sieben spielt zu Spieler sechs, und der direkt weiter zu Spieler fünf. Alle drei waren am Ball.", ps("b1", [54.4, 40.6]), ps("b1", [41.6, 28.6], after=True)),
     S("Abschluss mit dem schwachen Fuß", "Spieler fünf schießt mit seinem schwächeren Fuß flach zwischen die Hütchen, und das gibt einen Punkt für Rot.", ps("b1", [23.5, 30]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
