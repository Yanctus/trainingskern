import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 35-P4 (U12-U14, Woche 26 Phase 4): The Compact Midfield Unit. 25 x 25 Yards = Feld x 25-75, y 5-55 (23 x 23 m), in der Mitte
# eine Zone von 5 Yards (y 25-35, gestrichelt). Pink (vier Verteidiger) -> Team Neon (11, 4, 8, 7 wie im PDF), dunkel (sieben
# Spieler am Ball) -> Team Rot, neu nummeriert (im PDF doppelt mit Pink): Rot 11 -> 12, Rot 7 -> 10, sonst wie im PDF (2, 3, 5,
# 6, 9). Ausrichtung wie im PDF: vier Rote unten, drei oben, Trainer rechts. Positionen auf Abstand gesetzt (3D), Passfolge der
# Grundform vereinfacht (drei Pässe unten, Neon sieben drückt, Chip nach oben), Spielidee wie im PDF und Video.
# Kein Punktespiel im Original (Technikübung): Der letzte Schritt sagt das Ziel und wie es weitergeht.
# Sichtkegel: PDF "Stay on the half turn to see the ball & the space behind" -> in der Grundform bl() von Neon acht nach oben
# in den Raum hinter der Kette, bevor der Wechsel kommt (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 82, 40, "T")
POS = {"n11": (30, 30), "n4": (41.5, 30), "n8": (58.5, 30), "n7": (70, 30),
       "r12": (30, 12), "r9": (50, 9), "r10": (70, 12), "r3": (27, 46), "r5": (41, 52), "r6": (58, 53), "r2": (73, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 85.6, 43.5), B("s2", 82, 43.5)]
LINES = [rect(25, 5, 50, 50), line(25, 25, 75, 25), line(25, 35, 75, 35)]

u = {"title": "Vier in der Mittelzone", "code": "UE-205", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 11, "players_max": 11, "field_size": "23 x 23 m",
 "description": "Vier Verteidiger von Team Neon stehen in einer schmalen Zone in der Mitte. Team Rot lässt den Ball unten mit vier und oben mit drei Spielern laufen. Nach drei Pässen drückt der nächste Verteidiger auf den Ball, die anderen schieben eng nach. Ruft der Trainer „Wechsel“, chippt Team Rot den Ball auf die andere Seite, und die Kette dreht sich schnell um.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern. In der Mitte eine Zone von fünf Metern, mit Hütchen und Linien markiert. Der Trainer steht an der Seite mit Bällen.",
  "Verteilen: Die vier Verteidiger von Team Neon starten in der Mittelzone. Team Rot hat sieben Spieler: vier unten, drei oben.",
  "Ablauf: Team Rot passt in seiner Zone. Nach drei Pässen drückt der nächste Verteidiger langsam auf den Ball, die anderen schieben nach. Ruft der Trainer „Wechsel“, chippt Team Rot den Ball auf die andere Seite.",
  "Wechsel: Bei „Wechsel und pressen“ läuft der nächste Verteidiger den Annehmenden sofort an. Nach ein paar Minuten verteidigen vier andere Spieler."],
 "organisation_show": ORG,
 "coaching_points": ["Einer drückt, die Kette schiebt zum Absichern mit", "Laut absprechen: Wer presst, wer bleibt und sichert ab", "Nach dem Wechsel schnell umdrehen und wieder eng stehen", "Halb offen stehen, um Ball und Raum dahinter zu sehen"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Vier in der Mittelzone. Vier Verteidiger von Team Neon bleiben eng zusammen, schieben mit dem Ball und drehen sich beim Wechsel schnell um.",
 "board": {"lines": LINES, "goals": [], "cones": ecken(25, 5, 50, 50) + [C(25, 25), C(75, 25), C(25, 35), C(75, 35)], "players": sp(),
  "balls": [B("b1", 27.6, 46.6)] + ERSATZ,
  "steps": [
   S("Drei Pässe", "Team Rot lässt den Ball unten laufen: Rot drei passt zu Rot fünf, Rot fünf zu Rot sechs, Rot sechs zu Rot zwei. Gleichzeitig schiebt die ganze Kette von Team Neon mit zum Ball.",
     ps("b1", [41.6, 52.6]), ps("b1", [58.6, 53.6], after=True), ps("b1", [73.6, 47.6], after=True),
     mv("n11", [37, 30], delay=0.5), mv("n4", [47, 30], delay=0.5), mv("n8", [57, 30], delay=0.5), mv("n7", [66, 31], delay=0.5)),
   S("Einer drückt", "Nach drei Pässen drückt Neon sieben langsam auf Rot zwei. Neon acht, vier und elf schieben nach. Neon acht steht halb offen und schaut auch in den Raum hinter sich.",
     mv("n7", [67, 41]), mv("n8", [60, 31], delay=0.2), mv("n4", [50, 30], delay=0.2), mv("n11", [40, 30], delay=0.2), bl("n8", [63, 14], after=True)),
   S("Wechsel", "Der Trainer ruft: Wechsel! Rot zwei chippt den Ball hoch zu Rot zehn. Die Kette dreht sich schnell um und steht wieder eng. Geschafft, jetzt kreist der Ball oben, und nach drei Pässen drückt wieder einer.",
     ps("b1", [70.6, 12.6]), mv("n7", [68, 28], delay=0.4), mv("n8", [59, 28], delay=0.4), mv("n4", [49, 28], delay=0.4), mv("n11", [39, 28], delay=0.4))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m", rx=91)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Wechsel und pressen.", "Wechsel und pressen",
    "Ruft der Trainer „Wechsel und pressen“, läuft der nächste Verteidiger den Annehmenden sofort an. Die anderen drei drehen sich um, laufen zurück in die Zone und sichern hinter ihm ab.",
    sp(), [B("b1", 41.6, 52.6)] + ERSATZ,
    [S("Wechsel und pressen", "Der Trainer ruft: Wechsel und pressen! Rot fünf chippt den Ball hoch zu Rot zwölf.",
       ps("b1", [30.6, 12.6])),
     S("Sofort pressen", "Neon elf ist am nächsten, dreht sich um und presst Rot zwölf sofort. Gleichzeitig drehen sich Neon vier, acht und sieben um und schieben nach links.",
       mv("n11", [31, 20]), mv("n4", [39, 28], delay=0.2), mv("n8", [49, 28], delay=0.2), mv("n7", [59, 28], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Kette schiebt hinter dem Pressing mit.", "Die Kette schiebt mit",
    "Drückt ein Verteidiger auf den Ball, schieben die anderen drei gemeinsam zur Seite. Sie bleiben eng hinter ihm, machen die Lücken zu, und der Ball kommt nicht durch die Zone.",
    sp(), [B("b1", 58.6, 53.6)] + ERSATZ,
    [S("Einer drückt", "Rot sechs hat den Ball. Neon acht drückt auf ihn. Gleichzeitig schieben Neon vier, sieben und elf eng hinter ihm zusammen.",
       mv("n8", [58, 43]), mv("n4", [49, 33], delay=0.2), mv("n7", [67, 33], delay=0.2), mv("n11", [39, 31], delay=0.2)),
     S("Kein Weg durch", "Rot sechs findet keine Lücke nach oben und spielt zurück zu Rot fünf.",
       ps("b1", [41.6, 52.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
