import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# BM-09: 20 x 25 Yards, gedreht (Start links): Feld x 18-82, y 5-55. Fünf Hütchendreiecke (gelb -> neon, rot -> orange, blau -> neon).
T = P("T", "c", 5, 30, "T")
D = {"g1": ([(77.6, 47.8), (71, 38.9), (66.8, 48.9)], "neon"), "r1": ([(63, 17.6), (57.1, 8.7), (53.1, 17.6)], "orange"),
     "b1": ([(57.8, 26.8), (60.4, 36.2), (51.2, 33.9)], "neon"), "r2": ([(45.8, 43.3), (38.2, 49.2), (35, 39.2)], "orange"),
     "g2": ([(39.2, 22.7), (32.6, 13.7), (28.4, 23.8)], "neon")}
def cones(ids=False):
    out = []
    for k, (pts, col) in D.items():
        for i, (x, y) in enumerate(pts):
            out.append(C(x, y, col, **({"id": f"{k}{i}"} if ids else {})))
    return out + [C(18, 5, **({"id": "e1"} if ids else {})), C(82, 5, **({"id": "e2"} if ids else {})), C(18, 55, **({"id": "e3"} if ids else {})), C(82, 55, **({"id": "e4"} if ids else {}))]
def sp(**k):
    d = dict(n1=(16, 44), n2=(7, 50), r5=(16, 16), r6=(7, 10)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
cb = [B("c1", 7.6, 30.6), B("c2", 6, 33.5)]
zum_r1 = [dr("r5", "c1", [52, 24]), dr("r5", "c1", [58, 19], after=True)]
u = {"title": "Ab ins Dreieck", "code": "UE-086", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 12, "players_min": 6, "players_max": 12, "field_size": "23 x 18 m",
 "description": "Ein Wettlauf zum Ball mit anschließendem Dribbling. Der Trainer spielt einen Ball ins Feld, aus jeder Mannschaft rennt ein Spieler los. Wer den Ball bekommt, dribbelt ihn in eines der Hütchendreiecke und stoppt ihn dort. Das gibt einen Punkt. Die nächsten Spieler müssen ein Dreieck in einer anderen Farbe wählen.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern. Darin fünf Dreiecke aus je drei Hütchen in zwei Farben verteilen.",
  "Verteilen: Zwei Mannschaften stellen sich an einer Seite auf. Der Trainer steht mit den Bällen dazwischen.",
  "Ablauf: Der Trainer spielt einen Ball in den freien Raum. Je ein Spieler aus jeder Mannschaft rennt los. Wer den Ball erobert, dribbelt ihn in ein Dreieck und stoppt ihn dort. Das nächste Paar muss ein Dreieck in einer anderen Farbe ansteuern.",
  "Punkte: Jeder gestoppte Ball gibt einen Punkt. Bringt eine Mannschaft zwei Bälle in dasselbe Dreieck, gibt es einen zweiten Punkt, und der Trainer nimmt das Dreieck weg."],
 "organisation_show": ORG,
 "coaching_points": ["Unter Druck dribbeln und den Ball im Dreieck sauber stoppen", "Schnell zum Ball sprinten und rechtzeitig abbremsen", "Die Wartenden helfen mit Zurufen, welches Dreieck frei ist", "Den Ball mit dem Körper gegen den Gegner schützen"],
 "materials": ["9 gelbe Hütchen", "6 orange Hütchen", "4 Hütchen für das Feld", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Ab ins Dreieck. Wer zuerst am Ball ist, dribbelt ihn in ein Hütchendreieck und stoppt ihn dort.",
 "board": {"lines": [rect(18, 5, 64, 50)], "cones": cones(), "players": sp(), "balls": cb,
  "steps": [
   S("Wettlauf zum Ball", "Der Trainer spielt einen Ball ins Feld. Gleichzeitig rennen Neon eins und Rot fünf los.",
     ps("c1", [36.2, 33.5]), mv("r5", [34.6, 32], delay=0.2), mv("n1", [38, 34], delay=0.3)),
   S("Zum Dreieck", "Rot fünf ist zuerst am Ball und dribbelt zum orangen Dreieck oben, Neon eins jagt hinterher.",
     *zum_r1, mv("n1", [48, 30], delay=0.3)),
   S("Gestoppt: Punkt", "Rot fünf stoppt den Ball mitten im Dreieck, und das gibt einen Punkt für Rot.", dr("r5", "c1", [58, 14.6]), mv("n1", [54, 23]))],
  "dims": [{"x1": 18, "y1": 58.6, "x2": 82, "y2": 58.6, "text": "23 m"}, {"x1": 91, "y1": 5, "x2": 91, "y2": 55, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zwei Bälle im selben Dreieck bringen einen Extrapunkt.", "Zweimal ins gleiche Dreieck",
    "Liegt schon ein Ball der eigenen Mannschaft in einem Dreieck, lohnt sich ein zweiter Ball genau dort. Das gibt einen Extrapunkt, und der Trainer nimmt das Dreieck weg. Deshalb vorher den Kopf heben und schauen, wo schon ein Ball liegt.",
    sp(n1=(40, 30), r5=(26, 36)), [B("c1", 41.6, 30.6), B("alt", 57.4, 13.6), B("c2", 6, 33.5)],
    [S("Ins gleiche Dreieck", "Neon eins sieht, dass im orangen Dreieck oben schon ein Ball von Neon liegt, und dribbelt genau dorthin.",
       dr("n1", "c1", [52, 24]), dr("n1", "c1", [58, 19], after=True), mv("r5", [48, 30], delay=0.3)),
     S("Zwei Punkte, Dreieck weg", "Neon eins stoppt den Ball im selben Dreieck, und das gibt zwei Punkte für Neon. Der Trainer nimmt die Hütchen des Dreiecks weg.",
       dr("n1", "c1", [59, 15]), ps("r10", [63, 2.5], after=True), ps("r11", [60, 2.5], after=True), ps("r12", [57, 2.5], after=True))],
    cones=cones(True)),
  V("Steigerung", "Und jetzt die Steigerung: Von beiden Enden wird gleichzeitig gespielt.", "Von beiden Seiten",
    "Jetzt starten an beiden Enden Spieler, und von beiden Seiten kommt gleichzeitig ein Ball ins Feld. Gewonnen hat die Mannschaft, die zuerst in jedem Dreieck drei Bälle hat. Weil von beiden Seiten gedribbelt wird, immer den Kopf oben haben. Nur für ältere Spieler.",
    sp(n3=(84, 44), r7=(84, 16)), cb + [B("c3", 88, 31)],
    [S("Zwei Bälle, vier Läufer", "Von beiden Enden kommt gleichzeitig ein Ball ins Feld. Alle vier rennen los.",
       ps("c1", [36.2, 33.5]), ps("c3", [64.6, 27]), mv("r5", [34.6, 32], delay=0.2), mv("n1", [38, 34], delay=0.3), mv("r7", [65.5, 25], delay=0.2), mv("n3", [70, 34], delay=0.3)),
     S("Beide dribbeln los", "Gleichzeitig dribbelt Rot fünf zum Dreieck oben und Rot sieben zum gelben Dreieck unten rechts. Kopf hoch, damit niemand zusammenstößt.",
       *zum_r1, dr("r7", "c3", [64, 40]), dr("r7", "c3", [70, 45], after=True)),
     S("Zwei Punkte für Rot", "Beide stoppen ihren Ball im Dreieck, und das gibt zwei Punkte für Rot.", dr("r5", "c1", [58, 14.6]), dr("r7", "c3", [71.5, 45.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
