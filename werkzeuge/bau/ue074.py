import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 28-P2: 25 x 25 Yards (Quadrat x 25-75, y 5-55). Vier Paare: zwei Spiele gleichzeitig. Gruppe eins (Neon 2+3 gegen Rot 4+5) links nach rechts,
# Gruppe zwei (Neon 6+7 gegen Rot 8+9) oben nach unten. Vier Springer an den Seiten. Figuren auf Spalten x 33.5/41.75/50/58.25/66.5 (3D-Abstand).
T = P("T", "c", 12, 50, "T")
F = [P("fL", "t", 25, 30, "F"), P("fR", "t", 75, 30, "F"), P("fT", "t", 50, 5, "F"), P("fB", "t", 50, 55, "F")]
def feld(*sp): return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, x, y in sp] + F + [T]
cb = [B("c1", 14.5, 51), B("c2", 11, 53.8)]
lines = [rect(25, 5, 50, 50)]
cones = ecken(25, 5, 50, 50)
u = {"title": "Zwei Spiele, ein Feld", "code": "UE-074", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 23 m",
 "description": "Zwei Spiele laufen gleichzeitig im selben Feld, jeweils zwei gegen zwei. Die erste Gruppe will den Ball von links nach rechts bringen, die zweite von oben nach unten. Vier Springer an den Seiten helfen immer der Mannschaft am Ball. Weil sich alle kreuzen, müssen die Spieler ständig den Kopf heben und sich umschauen.",
 "organisation": ["Aufbauen: Ein Quadrat von 23 mal 23 Metern mit vier Hütchen.",
  "Verteilen: Vier Paare und vier Springer. Je zwei Paare bilden eine Gruppe und spielen gegeneinander. An jeder Seite steht ein Springer, er darf sich bis etwa vier Meter ins Feld hinein bewegen.",
  "Ablauf: Beide Gruppen spielen gleichzeitig. Gruppe eins spielt von links nach rechts, Gruppe zwei von oben nach unten. Jedes Paar darf jeden Springer anspielen. Kommt der Ball von einem Springer zum Springer auf der anderen Seite, gibt das einen Punkt.",
  "Wechsel: Nach drei bis vier Minuten ein bis zwei Minuten Pause, dann spielen neue Paare gegeneinander. Am Ende hat jedes Paar gegen jedes gespielt, die Punkte werden zusammengezählt."],
 "organisation_show": ORG,
 "coaching_points": ["Ständig umschauen, wo sich alle bewegen", "Wissen, wo Partner und Springer stehen", "Viel miteinander sprechen", "Genau passen und sich frei laufen, um im freien Raum anzunehmen"],
 "materials": ["4 orange Hütchen", "8 Leibchen in zwei Farben", "4 Leibchen für die Springer", "Mehrere Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Zwei Spiele, ein Feld. Zwei Gruppen spielen gleichzeitig, die eine von links nach rechts, die andere von oben nach unten.",
 "board": {"lines": lines, "cones": cones,
  "players": feld(("n2", 33.5, 12), ("n3", 58.25, 12), ("r4", 33.5, 30), ("r5", 66.5, 30), ("n6", 41.75, 30), ("n7", 58.25, 48), ("r8", 66.5, 48), ("r9", 58.25, 30)),
  "balls": [B("b1", 26.6, 30.6), B("b2", 51.6, 5.6)] + cb,
  "steps": [
   S("Beide Spiele starten gleichzeitig", "Beide Spiele starten gleichzeitig bei einem Springer. Der linke Springer spielt zu Neon zwei, der obere Springer zu Neon sechs. Rot vier und Rot neun laufen sofort dagegen.",
     ps("b1", [35.1, 12.6]), ps("b2", [43.35, 30.6]), mv("r4", [36, 22], delay=0.3), mv("r9", [52, 31], delay=0.3)),
   S("Weiter zum Partner", "Gleichzeitig spielen beide weiter: Neon zwei zu Neon drei, Neon sechs zu Neon sieben. Rot fünf und Rot acht versuchen, die nächsten Wege zuzustellen.",
     ps("b1", [59.85, 12.6]), ps("b2", [59.85, 48.6]), mv("r5", [64, 27], delay=0.2), mv("r8", [63, 41], delay=0.2)),
   S("Auf die andere Seite: Punkt", "Neon drei spielt zum rechten Springer, Neon sieben zum unteren Springer. Beide Bälle sind auf der anderen Seite angekommen, und das gibt jeweils einen Punkt für Neon.",
     ps("b1", [73.4, 30.6]), ps("b2", [51.6, 54.4]))],
  "dims": [{"x1": 25, "y1": 58.6, "x2": 75, "y2": 58.6, "text": "23 m"}, {"x1": 83, "y1": 5, "x2": 83, "y2": 55, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Sind die Springer zugestellt, spielt man zum eigenen Partner.", "Springer zu, Partner frei",
    "Oft stellen die Gegner die Wege zu den Springern zu. Dann nicht stur weiterspielen, sondern umschauen und den eigenen Partner anspielen. Der Partner hilft, bietet sich an und sucht von dort den nächsten freien Weg. Schnell entscheiden und den freien Raum nutzen.",
    feld(("n2", 50, 30), ("n3", 33.5, 14), ("r4", 58.25, 14), ("r5", 58.25, 46), ("n6", 41.75, 46), ("n7", 66.5, 12), ("r8", 66.5, 46), ("r9", 33.5, 46)),
    [B("b1", 51.6, 30.6), B("b2", 51.6, 5.6)] + cb,
    [S("Springer zugestellt", "Rot vier und Rot fünf stellen die Wege zum rechten Springer zu. Gleichzeitig spielt die andere Gruppe weiter, der obere Springer passt zu Neon sieben.",
       mv("r4", [61, 22]), mv("r5", [61, 39]), ps("b2", [68.1, 12.6])),
     S("Zum freien Partner", "Neon zwei schaut sich um und spielt zum freien Partner Neon drei. Der hat Platz und sucht von dort den nächsten freien Weg.", ps("b1", [35.1, 14.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Lücken sehen und mit einem Pass durch die Gegner spielen.", "Durch die Lücke spielen",
    "Bei so vielen Spielern auf engem Raum entstehen immer wieder Lücken zwischen zwei Gegnern. Wer früh den Kopf hebt, sieht sie. Ein flacher Pass genau durch die Lücke überspielt gleich zwei Gegner. Der Mitspieler läuft zur richtigen Zeit in den Raum dahinter.",
    feld(("n2", 33.5, 14), ("n3", 66.5, 14), ("r4", 41.75, 46), ("r5", 66.5, 52), ("n6", 66.5, 30), ("n7", 33.5, 40), ("r8", 41.75, 24), ("r9", 58.25, 24)),
    [B("b1", 35.1, 14.6), B("b2", 51.6, 5.6)] + cb,
    [S("Lücke sehen", "Der obere Springer hat den Ball und sieht die Lücke zwischen Rot acht und Rot neun. Neon sechs läuft genau dahinter in den freien Raum.", mv("n6", [50, 40])),
     S("Durch die Lücke", "Der Springer spielt flach durch die Lücke, mitten zwischen die beiden roten Spieler. Zwei Gegner sind mit einem Pass überspielt.", ps("b2", [51.6, 40.6])),
     S("Nach unten: Punkt", "Neon sechs spielt weiter zum unteren Springer, und das gibt einen Punkt für Neon.", ps("b2", [51.6, 54.2]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
