import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 34-P6 (U12-U14, Woche 34 Phase 5): Develop Off the Ball Runs in Behind (End Zone Finishing). 20 x 30 Yards = Feld x 30-70,
# y 4-56 (18 x 27 m), Endzonen je knapp 4 Yards (y 4-10.5 neon für Team Neon, y 49.5-56 orange für Team Rot).
# Gespiegelt (oben/unten): im PDF greifen die Pinken nach unten an, hier greift Team Neon nach oben an.
# Pink (5 Angreifer) -> Team Neon 4, 8, 9, 10, 11 (Nummern wie im PDF). Navy (6 Verteidiger) -> Team Rot, neu nummeriert
# (im PDF doppelt): navy 9 -> Rot 3, navy 4 -> Rot 2, navy 11 -> Rot 12; 5, 6, 7 bleiben. Positionen in Spalten gesetzt (3D-Abstand),
# grob wie im PDF. Ein Trainer statt zwei (links unten mit Bällen).
# Steigerung wie im PDF/Ton: Ballgewinn vor dem achten Pass gibt einen Punkt für Team Rot (PDF sagt zehn Pässe, Video und Ton acht).
# Coaching-Punkt aus PDF Seite 2 und Video: auf eine Seite locken, dann schnell verlagern.
# Sichtkegel: PDF "Head up to see space", "Recognise player movement to trigger forward pass", Ton "spotting this movement to
# release at the right moment" -> in der Grundform schaut Spieler elf zum startenden Spieler neun, bevor er steil spielt (im Video
# kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 23, 50, "T")
POS = {"r5": (33, 16), "r12": (33, 34), "n9": (41.5, 24), "n4": (41.5, 47), "r2": (50, 20), "n10": (50, 36),
       "n11": (58.5, 25), "r3": (58.5, 42), "r6": (67, 14), "r7": (67, 30), "n8": (67, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 53.5), B("s2", 20, 53.5)]
LINES = [rect(30, 4, 40, 52), {"type": "zone", "x": 30, "y": 4, "w": 40, "h": 6.5},
         {"type": "zone", "x": 30, "y": 49.5, "w": 40, "h": 6.5, "color": "orange"}]
CONES = ecken(30, 4, 40, 52) + [C(30, 10.5), C(70, 10.5), C(30, 49.5), C(70, 49.5)]

u = {"title": "Tiefenlauf in die Endzone", "code": "UE-226", "kind": "Spielform",
 "focuses": ["Passspiel", "Bewegung", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 11, "players_max": 11, "field_size": "18 x 27 m",
 "description": "Fünf Angreifer von Team Neon spielen gegen sechs Verteidiger von Team Rot, an jedem Ende liegt eine Endzone. Nach fünf Pässen darf Team Neon steil in die obere Endzone spielen. Ein Mitspieler startet im richtigen Moment hinter die Abwehr und nimmt den Ball dort an, das gibt einen Punkt. Erobert Team Rot den Ball, spielt es selbst auf die untere Endzone.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern. An jedem Ende eine Endzone von gut 3 Metern.",
  "Verteilen: Team Neon mit fünf Spielern und Team Rot mit sechs Spielern im Mittelfeld. Der Trainer steht links unten mit Bällen.",
  "Ablauf: Team Neon spielt fünf Pässe und darf dann steil in die obere Endzone spielen. Ein Mitspieler läuft hinter die Abwehr und nimmt den Ball dort an. Erobert Team Rot den Ball, kombiniert es und spielt auf die untere Endzone.",
  "Wertung und Wechsel: Ein angenommener Ball in der Endzone gibt einen Punkt. Danach spielt der Trainer einen neuen Ball zu Team Neon. Nach ein paar Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch und schauen, wo Platz ist", "Den Lauf des Mitspielers sehen und genau dann steil spielen", "Antäuschen, um den Verteidiger wegzulocken, und laut rufen", "Ist keine Lücke da, geduldig weiter passen und den Gegner auf eine Seite locken"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Tiefenlauf in die Endzone. Team Neon kombiniert und sucht den Steilpass hinter die Abwehr.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 42.1, 47.6)] + ERSATZ,
  "steps": [
   S("Fünf Pässe", "Team Neon lässt den Ball laufen. Spieler vier spielt zu Spieler acht und bekommt ihn zurück. Dann spielt er zu Spieler zehn. Erst nach fünf Pässen darf der Ball in die Endzone.",
     ps("b1", [67.6, 46.6]), ps("b1", [42.1, 47.6], after=True), ps("b1", [50.6, 36.6], after=True)),
   S("Lauf sehen", "Spieler zehn spielt zu Spieler elf. Spieler neun startet hinter die Abwehr, und Spieler elf hebt den Kopf und sieht den Lauf.",
     ps("b1", [59.1, 25.6]), mv("n9", [43, 16], delay=0.6), bl("n11", [43.5, 17], after=True)),
   S("In die Endzone: Punkt", "Spieler elf spielt steil in die Endzone. Spieler neun nimmt den Ball dort an, und das gibt einen Punkt für Team Neon. Dann spielt der Trainer einen neuen Ball zu Team Neon.",
     mv("n9", [44, 7]), ps("b1", [44.6, 7.6], delay=0.2))],
  "dims": dims(30, 70, 4, 56, "18 m", "27 m", rx=78)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Auf eine Seite locken, dann verlagern.", "Locken und verlagern",
    "Team Neon spielt kurze Pässe auf einer Seite. Die Verteidiger schieben alle dorthin. Dann geht der Ball schnell auf die andere Seite, wo jetzt Platz ist.",
    sp(), [B("b1", 42.1, 47.6)] + ERSATZ,
    [S("Auf eine Seite locken", "Spieler vier und Spieler zehn spielen sich kurz den Ball zu. Team Rot schiebt nach links zum Ball.",
       ps("b1", [50.6, 36.6]), ps("b1", [42.1, 47.6], after=True),
       mv("r3", [52, 43], delay=0.3), mv("r7", [60, 33], delay=0.3), mv("r6", [56, 13], delay=0.3), mv("r2", [46, 21], delay=0.3)),
     S("Verlagern: Punkt", "Spieler vier verlagert schnell zu Spieler acht auf die freie Seite. Spieler acht dribbelt nach vorn und spielt steil zu Spieler elf in die Endzone. Das gibt einen Punkt für Team Neon.",
       ps("b1", [67.6, 46.6]), dr("n8", "b1", [67, 30], after=True), mv("n11", [64, 7], delay=1.6), ps("b1", [64.6, 7.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ballgewinn gibt einen Punkt.", "Ballgewinn gibt einen Punkt",
    "Erobert Team Rot den Ball, bevor Team Neon acht Pässe geschafft hat, gibt das einen Punkt für Team Rot. Darum pressen die Verteidiger jetzt früh. So entsteht aber auch mehr Platz hinter ihnen.",
    sp(), [B("b1", 50.6, 36.6)] + ERSATZ,
    [S("Früh pressen", "Spieler zehn hat den Ball. Spieler zwei presst ihn sofort, und Spieler drei stellt den Pass zu Spieler vier zu.",
       mv("r2", [50, 30]), mv("r3", [47, 42], delay=0.2)),
     S("Ballgewinn: Punkt", "Spieler zehn spielt trotzdem zu Spieler vier. Spieler drei fängt den Ball ab, und das gibt einen Punkt für Team Rot. Jetzt spielt Team Rot auf die untere Endzone.",
       ps("b1", [46.4, 42.6]), mv("r3", [45.8, 42], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
