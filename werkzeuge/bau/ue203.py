import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 35-P1 (U12-U14, Woche 26 Phase 4): Compactness and Transfer Game. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), Mittellinie
# gestrichelt. Pink (vier Verteidiger) -> Team Neon (4, 7, 8, 11, Nummern wie im PDF), dunkel (Ballbesitz) -> Team Rot, Springer
# (gelb, F) neutral. Rot neu nummeriert (im PDF doppelt mit Pink): Rot 11 -> 12, Rot 7 -> 10, sonst wie im PDF (2, 3, 5, 6, 9).
# Ausrichtung wie im PDF: unten fünf gegen vier, der Wechsel geht nach oben. Positionen auf Abstand gesetzt (3D), Passfolge der
# Grundform vereinfacht (Springer kommt nach unten, vier Pässe, langer Ball nach oben), Spielidee wie im PDF und Video.
# Steigerung wie im Video: Minitore oben und unten in der Mitte, Neon kontert nach dem Abfangen auf das untere Minitor.
# Sichtkegel: Ton "Defenders must recognise poor touches or misplaced passes as triggers to apply a high press" -> im
# Coaching-Punkt bl() von Spieler acht zu Spieler sechs, bevor die Annahme verspringt (im Video kein Kegel eingezeichnet, Richtung aus
# dem Sinn; im Video presst Pink 4 gegen Blau 6).
T = P("T", "c", 82, 30, "T")
POS = {"n11": (30, 34), "n4": (41.5, 36), "n8": (58.5, 36), "n7": (70, 34),
       "r12": (30, 12), "r9": (50, 10), "r10": (70, 12), "r3": (27, 50.5), "r5": (40, 52.5), "r6": (60, 52.5), "r2": (73, 50.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("f", "t", 50, 29, "F"), T]
ERSATZ = [B("s1", 85.6, 33.5), B("s2", 82, 33.5)]
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
MINI = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}]

u = {"title": "Kompakt schieben, Seite wechseln", "code": "UE-203", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "18 x 18 m",
 "description": "Ein Feld in zwei Hälften: In einer Hälfte spielen vier Spieler von Team Rot und ein Springer gegen die vier Verteidiger von Team Neon. Nach vier Pässen in Folge darf Team Rot den Ball in die andere Hälfte spielen, und das gibt einen Punkt. Team Neon schiebt eng zusammen, macht die Passwege zu und rückt nach dem Wechsel schnell mit. Erobert Team Neon den Ball, braucht es fünf Pässe für einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, in der Mitte mit einer Linie in zwei Hälften geteilt. Der Trainer steht an der Seite mit Bällen.",
  "Verteilen: Team Neon verteidigt mit vier Spielern. Team Rot hat sieben Spieler: vier in einer Hälfte, drei in der anderen. Der Springer hilft immer dem Team am Ball.",
  "Ablauf: Team Rot und der Springer spielen fünf gegen vier. Nach vier Pässen darf der Ball in die andere Hälfte. Dann laufen ein Spieler von Team Rot, der Springer und alle vier Verteidiger mit hinüber.",
  "Wertung und Wechsel: Ein gelungener Wechsel gibt einen Punkt für Team Rot. Fünf Pässe nach einem Ballgewinn geben einen Punkt für Team Neon. Nach ein paar Minuten verteidigen vier andere Spieler."],
 "organisation_show": ORG,
 "coaching_points": ["Gemeinsam pressen und absichern, keine Lücken lassen", "So stellen, dass der Passweg zum Springer zu ist", "Nach dem Wechsel schnell in die andere Hälfte", "Nach dem Ballgewinn sofort sicher weiterspielen"],
 "materials": ["4 Hütchen", "2 Minitore für die Steigerung", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Kompakt schieben, Seite wechseln. Vier Verteidiger von Team Neon bleiben eng zusammen, und Team Rot will den Ball in die andere Hälfte spielen.",
 "board": {"lines": LINES, "goals": [], "cones": ecken(25, 5, 50, 50), "players": sp(), "balls": [B("b1", 27.6, 51.1)] + ERSATZ,
  "steps": [
   S("Vier Pässe", "Unten spielt Team Rot mit dem Springer fünf gegen vier. Der Springer kommt nach unten. Spieler drei passt zu Spieler fünf, Spieler fünf zum Springer, der Springer zu Spieler sechs. Gleichzeitig schiebt Team Neon eng mit zum Ball.",
     mv("f", [50, 44]), ps("b1", [40.6, 53.1]), ps("b1", [50.6, 44.6], after=True), ps("b1", [60.6, 53.1], after=True),
     mv("n11", [35, 33], delay=0.4), mv("n4", [45, 35], delay=0.4), mv("n8", [60, 37], delay=0.4)),
   S("Der lange Ball", "Spieler sechs passt zu Spieler zwei, das ist der vierte Pass. Spieler sieben kommt zu spät. Spieler zwei spielt den Ball weit nach oben zu Spieler zehn.",
     ps("b1", [73.6, 51.1]), mv("n7", [66, 44], delay=0.3), ps("b1", [70.6, 12.6], after=True)),
   S("Seitenwechsel: Punkt", "Der Ball ist oben angekommen, und das gibt einen Punkt für Team Rot. Jetzt laufen der Springer und Spieler sechs nach oben. Auch Team Neon rückt schnell nach oben und verteidigt dort, wieder fünf gegen vier.",
     mv("f", [50, 21]), mv("r6", [64, 22], delay=0.2), mv("n11", [36, 24]), mv("n4", [45, 25]), mv("n8", [56, 27]), mv("n7", [70, 30]))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Bei einer schlechten Ballannahme sofort pressen.", "Sofort pressen",
    "Springt dem Gegner der Ball vom Fuß, ist das das Zeichen zum Pressen. Der nächste Verteidiger läuft sofort hin, die anderen schieben nach und sichern ab. Nach dem Ballgewinn braucht Team Neon fünf Pässe, und der Springer hilft dabei.",
    sp(), [B("b1", 40.6, 53.1)] + ERSATZ,
    [S("Genau hinschauen", "Spieler fünf passt zu Spieler sechs. Spieler acht schaut genau hin: Kann Spieler sechs den Ball gut annehmen?",
       ps("b1", [60.6, 53.1]), bl("n8", [60, 52.5])),
     S("Pressen", "Der Ball springt Spieler sechs vom Fuß. Das ist das Zeichen: Spieler acht presst sofort. Gleichzeitig schieben Spieler vier und Spieler sieben nach und sichern ab.",
       ps("b1", [56.6, 46.6]), mv("n8", [56, 46], delay=0.2), mv("n4", [47, 40], delay=0.2), mv("n7", [66, 38], delay=0.2)),
     S("Ball erobert", "Spieler acht erobert den Ball und spielt sofort zum Springer. Jetzt braucht Team Neon fünf Pässe in Folge, und das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 29.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Abfangen kontert Team Neon auf ein Minitor.", "Konter auf das Minitor",
    "Oben und unten steht in der Mitte ein Minitor. Fängt Team Neon den Ball ab, greift es sofort an und schießt auf das Minitor in seiner Hälfte. Das gibt einen Punkt für Team Neon.",
    sp(), [B("b1", 40.6, 53.1)] + ERSATZ,
    [S("Abgefangen", "Spieler fünf will zum Springer passen. Spieler vier geht dazwischen und fängt den Ball ab.",
       mv("n4", [45.4, 40]), ps("b1", [46, 40.6], delay=0.3)),
     S("Minitor: Punkt", "Spieler vier dribbelt sofort los und schießt ins untere Minitor. Das gibt einen Punkt für Team Neon. Dann bringt der Trainer einen neuen Ball zu Team Rot.",
       dr("n4", "b1", [49, 47]), ps("b1", [50, 54.7], after=True))],
    goals=MINI)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
