import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P5 (U12-U14, Woche 34 Phase 5): How to Defend as a Pair - 5 v 2 Skill Rondo. 15 x 25 Yards = Feld x 30-70, y 4-56
# (14 x 23 m, etwas breiter gezeichnet wegen 3D-Abstand), Mittellinie gestrichelt bei y 30. Vier Minitore wie im PDF: oben, unten,
# links an der oberen Hälfte, rechts an der unteren Hälfte. Ausrichtung wie im PDF (nicht gedreht).
# Navy (5 Ballbesitz unten) -> Neon 4, 5, 6, 8, 10; Pink -> Rot (7 und 10 pressen unten, 2, 9, 6 warten oben).
# Rot neu nummeriert (im PDF doppelt): pink 10 -> Rot 11, pink 6 -> Rot 3. Ein Trainer statt zwei (unten links mit Bällen).
# Kein Duplikat von UE-080 (06-P2, ohne Minitore und ohne Abschluss nach acht Pässen), UE-044 (zwei Fünfergruppen,
# Ballgewinn = Abschluss) und UE-154 (Quadrat mit Kanal).
# Sichtkegel: PDF "Identify triggers to press, such as a bad touch" und "Awareness of opportunities to finish" -> im ersten
# Coaching-Punkt schaut Spieler elf auf den schlecht angenommenen Ball von Spieler sechs, bevor er presst (im Video kein Kegel
# eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 23, 50, "T")
POS = {"n4": (33, 34), "n8": (33, 51), "r9": (41.5, 20), "r7": (41.5, 42), "r2": (50, 8), "r11": (50, 38), "n5": (50, 54),
       "r3": (58.5, 20), "n6": (58.5, 36), "n10": (58.5, 52)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 53.5), B("s2", 20, 53.5)]
LINES = [rect(30, 4, 40, 52), line(30, 30, 70, 30)]
CONES = ecken(30, 4, 40, 52) + [C(30, 30), C(70, 30)]
TORE = [{"x": 50, "y": 4, "side": "top"}, {"x": 50, "y": 56, "side": "bottom"},
        {"x": 30, "y": 17, "side": "left"}, {"x": 70, "y": 43, "side": "right"}]

u = {"title": "Paar-Rondo mit vier Minitoren", "code": "UE-224", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "14 x 23 m",
 "description": "Ein Feld mit zwei Hälften und vier Minitoren. In einer Hälfte spielen fünf gegen zwei: Nach acht Pässen darf Team Neon in ein Minitor schießen. Die zwei Verteidiger pressen als Paar, erobern den Ball und spielen ihn sofort zu ihren drei Mitspielern in der anderen Hälfte. Dann wechseln die Rollen, und zwei von Team Neon pressen dort als neues Paar.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 23 Metern, in der Mitte geteilt. Ein Minitor oben, eins unten, eins links an der oberen und eins rechts an der unteren Hälfte.",
  "Verteilen: Team Neon mit fünf Spielern in der unteren Hälfte, dazu zwei von Team Rot als Paar. Die anderen drei von Team Rot warten oben. Der Trainer steht unten links mit Bällen.",
  "Ablauf: Team Neon spielt acht Pässe und darf dann in eines der Minitore schießen. Erobert das Paar den Ball, spielt es ihn sofort in die andere Hälfte. Dann laufen zwei von Team Neon hinüber und pressen, und das Paar wird zu Angreifern.",
  "Wertung und Wechsel: Ein Treffer nach acht Pässen gibt einen Punkt. Danach spielt der Trainer einen neuen Ball ein. Nach jedem Ballgewinn wechseln die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Als Paar pressen, wenn der Gegner schlecht annimmt oder schlecht passt", "Eng zusammenbleiben und Passwege zustellen", "Schräg anlaufen, damit der Ball nur in eine Richtung kann", "Nach Ballgewinn sofort umschalten und in die andere Hälfte spielen"],
 "materials": ["4 Minitore", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Paar-Rondo mit vier Minitoren. Fünf gegen zwei, und die zwei Verteidiger pressen gemeinsam als Paar.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": [B("b1", 33.6, 34.6)] + ERSATZ,
  "steps": [
   S("Fünf gegen zwei", "Team Neon lässt den Ball in der unteren Hälfte laufen. Spieler vier spielt zu Spieler acht, der zu Spieler fünf und weiter zu Spieler zehn. Spieler sieben und Spieler elf pressen als Paar.",
     ps("b1", [33.6, 51.6]), ps("b1", [50.6, 54.6], after=True), ps("b1", [59.1, 52.6], after=True),
     mv("r7", [40, 46], delay=0.4), mv("r11", [52, 44], delay=1.2)),
   S("Acht Pässe: Punkt", "Nach acht Pässen darf Team Neon schießen. Spieler zehn trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon. Der Trainer spielt sofort einen neuen Ball zu Spieler acht.",
     ps("b1", [69.5, 43.6]), ps("s1", [33.6, 51.6], after=True)),
   S("Ballgewinn", "Spieler acht spielt zu Spieler vier, aber Spieler vier nimmt den Ball schlecht an. Spieler sieben presst sofort und erobert den Ball.",
     ps("s1", [33.6, 34.6]), mv("r7", [37.5, 36.5], delay=0.4), mv("s1", [37.1, 37.1], after=True)),
   S("Rollen tauschen", "Spieler sieben spielt sofort zu Spieler neun in die obere Hälfte. Jetzt hat Team Rot oben fünf Spieler und muss acht Pässe schaffen, dann gibt ein Treffer einen Punkt für Team Rot. Spieler vier und Spieler sechs laufen hinüber und pressen dort als neues Paar.",
     ps("s1", [42.1, 20.6]), mv("r7", [34, 25], delay=0.3), mv("r11", [64, 30], delay=0.3), mv("r11", [66, 27], after=True),
     mv("n4", [44, 27], delay=0.5), mv("n6", [55, 27], delay=0.5))],
  "dims": dims(30, 70, 4, 56, "14 m", "23 m", rx=78)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Auslöser erkennen und sofort pressen.", "Auslöser erkennen",
    "Das Paar wartet auf ein Signal: eine schlechte Annahme oder einen ungenauen Pass. Dann pressen beide sofort und mit vollem Tempo. Nach dem Ballgewinn geht der Ball schnell in die andere Hälfte.",
    sp(), [B("b1", 50.6, 54.6)] + ERSATZ,
    [S("Schlechte Annahme", "Spieler fünf spielt zu Spieler sechs. Der Ball springt ihm vom Fuß. Spieler elf schaut genau hin und erkennt: Jetzt!",
       ps("b1", [59.1, 36.6]), mv("b1", [62, 40], after=True), bl("r11", [61.5, 40], after=True)),
     S("Sofort pressen", "Spieler elf sprintet auf den Ball und erobert ihn. Gleichzeitig stellt Spieler sieben den Pass zu Spieler fünf zu.",
       mv("r11", [61.4, 39.4]), mv("r7", [46, 48])),
     S("Rüber: Ballbesitz", "Spieler elf dribbelt kurz weg und spielt sofort zu Spieler drei in die obere Hälfte. Jetzt ist Team Rot oben mit fünf am Ball.",
       dr("r11", "b1", [65, 32]), ps("b1", [59.1, 20.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Eng zusammen und schräg anlaufen.", "Eng und schräg anlaufen",
    "Die zwei Verteidiger bleiben nah beieinander. Der erste läuft schräg an, so dass der Pass nur noch in eine Richtung kann. Der zweite steht genau dort und fängt den Ball ab.",
    sp(), [B("b1", 33.6, 51.6)] + ERSATZ,
    [S("Schräg anlaufen", "Spieler acht hat den Ball. Spieler sieben läuft schräg an und stellt den Pass zu Spieler vier zu. Spieler elf bleibt nah bei ihm.",
       mv("r7", [37.5, 45]), mv("r11", [45, 47], delay=0.2)),
     S("Abfangen: Ballbesitz", "Spieler acht muss zu Spieler fünf passen. Spieler elf geht dazwischen und fängt den Ball ab. Jetzt ist Team Rot am Ball und spielt sofort in die obere Hälfte.",
       ps("b1", [45.4, 52.6]), mv("r11", [44.8, 52], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
