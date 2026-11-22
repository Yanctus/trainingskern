import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 35-P3 (U12-U14, Woche 19 Phase 1): Four Corner Game Possession. Kein PDF und kein text.txt: Organisation aus Ton und
# Szenenbildern. 25 x 25 Yards = Feld x 25-75, y 5-55 (23 x 23 m), in jeder Ecke ein gestricheltes Eckfeld (ca. 5 x 5 m).
# Gelb (4, 8, 9, 11) -> Neon, Rot (2, 5, 7, 10) bleibt Rot, Blau in den Ecken (dritte Vierergruppe) -> neutrale Springer F.
# Regeln aus dem Video: 10 Pässe = Punkt, Springer mit ein oder zwei Kontakten, kein direkter Pass von Ecke zu Ecke,
# nach 10 Pässen tauscht das andere Team mit den Springern. Positionen auf ein Spaltenraster gesetzt (3D-Abstand).
# Sichtkegel: Im Video kein Kegel eingezeichnet, aber Schlussfolie "Quick scan to see defender and space to play into":
# im Coaching-Punkt bl() von Spieler elf zu Spieler zwei vor der Annahme (Richtung aus dem Sinn).
T = P("T", "c", 81, 30, "T")
POS = {"n4": (50, 12), "n11": (33.4, 30), "n9": (66.6, 30), "n8": (50, 48),
       "r2": (41.7, 28), "r5": (58.3, 28), "r7": (41.7, 44), "r10": (58.3, 44),
       "f1": (30, 10), "f2": (70, 10), "f3": (30, 50), "f4": (70, 50)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 84.6, 33.5), B("s2", 81, 33.5)]
LINES = [rect(25, 5, 50, 50), line(25, 15, 35, 15), line(35, 5, 35, 15), line(65, 15, 75, 15), line(65, 5, 65, 15),
         line(25, 45, 35, 45), line(35, 45, 35, 55), line(65, 45, 75, 45), line(65, 45, 65, 55)]

u = {"title": "Vier Ecken, zehn Pässe", "code": "UE-160", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 23 m",
 "description": "Vier gegen vier in einem Quadrat, und in jeder Ecke steht ein Springer. Das Team am Ball darf die Springer anspielen und will zehn Pässe in Folge schaffen. Die Springer spielen mit ein oder zwei Kontakten und nie direkt in eine andere Ecke. Nach zehn Pässen tauscht das andere Team mit den Springern, und das Spiel läuft sofort weiter.",
 "organisation": ["Aufbauen: Ein Quadrat von 23 mal 23 Metern. In jeder Ecke ein kleines Eckfeld von etwa 5 mal 5 Metern, gestrichelt abgeteilt.",
  "Verteilen: Drei Teams zu viert. Team Neon und Team Rot spielen in der Mitte, das dritte Team steht als Springer in den vier Ecken. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Das Team am Ball spielt mit den Springern und sammelt Pässe. Springer spielen mit ein oder zwei Kontakten und nie direkt von Ecke zu Ecke. Die Verteidiger pressen gemeinsam.",
  "Wertung und Wechsel: Zehn Pässe in Folge geben einen Punkt. Dann tauscht das andere Team mit den Springern, und das Spiel läuft sofort weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen", "Vor der Annahme kurz umschauen: Wo ist der Gegner, wo ist Platz?", "Den Gegner anlocken und dann an ihm vorbei spielen", "Gemeinsam pressen und die Räume eng machen"],
 "materials": ["Hütchen für Feld und Eckfelder", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Vier Ecken, zehn Pässe. Vier gegen vier in der Mitte, und in jeder Ecke hilft ein Springer dem Team am Ball.",
 "board": {"lines": LINES, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 48.6)] + ERSATZ,
  "steps": [
   S("Pässe sammeln", "Team Neon hat den Ball und will zehn Pässe in Folge schaffen. Spieler acht spielt zum Springer unten links. Gleichzeitig rücken Spieler sieben und Spieler zwei gemeinsam heraus.",
     ps("b1", [30.6, 50.6]), mv("r7", [38, 45.5], delay=0.2), mv("r2", [39, 35], delay=0.2)),
   S("Zurück in die Mitte", "Der Springer spielt mit einem Kontakt zu Spieler elf. Spieler elf spielt gleich weiter zum Springer oben links.",
     ps("b1", [34.0, 30.6]), ps("b1", [30.6, 10.6], after=True)),
   S("Nicht von Ecke zu Ecke", "Der Springer darf nicht direkt in eine andere Ecke spielen. Er spielt zu Spieler vier, und Spieler vier passt weiter zum Springer oben rechts. Spieler fünf läuft an.",
     ps("b1", [50.6, 12.6]), ps("b1", [70.6, 10.6], after=True), mv("r5", [62, 18], after=True)),
   S("Zehn Pässe: Punkt", "Der Springer spielt zurück zu Spieler neun, und so geht es weiter bis zum zehnten Pass. Das gibt einen Punkt für Team Neon. Dann tauscht Team Rot mit den Springern, alle laufen gleichzeitig, und das Spiel geht sofort weiter.",
     ps("b1", [67.2, 30.6]),
     mv("r2", [30, 10], after=True, bend=5), mv("f1", [41.7, 28]), mv("r7", [30, 50], bend=4), mv("f3", [41.7, 44]),
     mv("r5", [70, 10], bend=-4), mv("f2", [58.3, 28]), mv("r10", [70, 50], bend=-4), mv("f4", [58.3, 44]))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m", rx=89)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor der Annahme kurz umschauen.", "Erst umschauen",
    "Bevor der Ball kommt, schaut der Spieler kurz über die Schulter. So sieht er, wo der Gegner steht und wo Platz ist. Dann nimmt er den Ball gleich in den freien Raum mit und hat Zeit für den nächsten Pass.",
    sp(), [B("b1", 30.6, 50.6)] + ERSATZ,
    [S("Umschauen", "Der Springer unten links hat den Ball. Bevor der Pass kommt, schaut Spieler elf kurz über die Schulter und sieht Spieler zwei, der anläuft.",
       bl("n11", [50, 26]), mv("r2", [38, 24], delay=0.4)),
     S("Offen mitnehmen", "Der Springer spielt zu Spieler elf. Spieler elf nimmt den Ball weg von Spieler zwei in den freien Raum mit und spielt quer zu Spieler neun.",
       ps("b1", [34.0, 30.6]), dr("n11", "b1", [38, 37], after=True), ps("b1", [67.2, 30.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Erst drei Pässe in der Mitte, dann zu den Springern.", "Erst drei Pässe",
    "Das Team am Ball muss jetzt erst drei Pässe in der Mitte spielen, bevor es einen Springer anspielen darf. Der einfache Pass in die Ecke fällt weg. Darum müssen sich alle schneller anbieten und gute Winkel schaffen.",
    sp(r10=(58.3, 46)), [B("b1", 34.0, 30.6)] + ERSATZ,
    [S("Drei Pässe in der Mitte", "Spieler elf spielt zu Spieler vier, der weiter zu Spieler neun und der zu Spieler acht. Das sind drei Pässe in der Mitte.",
       ps("b1", [50.6, 12.6]), ps("b1", [67.2, 30.6], after=True), ps("b1", [50.6, 48.6], after=True)),
     S("Jetzt zum Springer", "Erst jetzt darf Spieler acht einen Springer anspielen. Er passt zum Springer unten rechts, und der spielt zurück zu Spieler neun.",
       ps("b1", [70.6, 50.6]), ps("b1", [67.2, 30.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
