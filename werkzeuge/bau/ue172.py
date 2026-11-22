import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 27-P4 (U12-U14, Woche 14 Phase 4): Defensive Recovery Runs. 20 x 15 Yards = Feld x 25-75, y 10-47.5 (18 x 14 m), längs geteilt
# (gestrichelt bei x 50), oben eine Endzone von 5 Yards (gestrichelt bei y 22.5) mit je einem Minitor pro Hälfte. Zielspieler unten
# außerhalb des Feldes. Pink (Angreifer) -> Neon 3, 8, 11 (links) und 7, 6, 2 (rechts); Blau -> Rot. Nummern neu (im PDF doppelt):
# Blau 2 -> Rot 9 (Verteidiger links), Blau 4 -> Rot 4 (Ziel links), Blau 3 -> Rot 10 (Verteidiger rechts), Blau 5 -> Rot 5 (Ziel rechts).
# Positionen leicht verschoben (3D-Abstand). Ein Trainer statt zwei. Steigerung: Mittelzone (gestrichelt bei y 31.5) wie im PDF;
# im PDF verteidigt dort Blau 4 und Blau 2 ist Ziel, hier bleibt Spieler neun Verteidiger und Spieler vier Ziel.
# Sichtkegel: Im Ton "stay aware of potential threats" und "track runners in behind" (im Video kein Kegel eingezeichnet):
# bl() vom Verteidiger über die Schulter zum Läufer in die Endzone (Grundform und Steigerung).
T = P("T", "c", 84, 24, "T")
POS = {"n11": (27, 27), "r9": (36, 26), "n8": (45.4, 29), "n3": (32, 44), "r4": (42, 52),
       "n7": (71, 28), "r10": (62, 32), "n6": (53.6, 40), "n2": (71.5, 44), "r5": (62, 52)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 85.6, 27.5), B("s2", 82, 27.5)]
BAELLE = [B("b1", 32.6, 44.6), B("b2", 72.1, 44.6)]
LINES = [rect(25, 10, 50, 37.5), line(50, 10, 50, 47.5), line(25, 22.5, 75, 22.5)]
TORE = [{"x": 37.5, "y": 10, "side": "top"}, {"x": 62.5, "y": 10, "side": "top"}]

u = {"title": "Zurück sprinten und abfangen", "code": "UE-172", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 14 m",
 "description": "In jeder Hälfte spielen drei Angreifer gegen einen Verteidiger. Nach fünf Pässen dürfen die Angreifer in die Endzone spielen und dort aufs Minitor schießen. Der Verteidiger presst, sprintet zurück und fängt den Pass in die Tiefe ab. Erobert er den Ball und spielt ihn zum Zielspieler, gibt das einen Punkt für sein Team.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern, längs in zwei Hälften geteilt. Oben eine Endzone von gut 4 Metern mit einem Minitor in jeder Hälfte.",
  "Verteilen: In jeder Hälfte drei von Team Neon und ein Verteidiger von Team Rot. Unter jeder Hälfte steht ein Zielspieler von Team Rot. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon spielt drei gegen eins und braucht fünf Pässe. Dann darf es in die Endzone spielen, wo ein Mitspieler hinläuft und aufs Minitor schießt. Der Verteidiger presst und sprintet zurück.",
  "Wertung und Wechsel: Treffer ins Minitor gibt einen Punkt für Team Neon, Pass zum Zielspieler einen Punkt für Team Rot. Die Hälften spielen abwechselnd, Verteidiger und Zielspieler tauschen nach jeder Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Den Pass in die Tiefe zustellen und vorausahnen", "Im richtigen Moment abfangen, bei schlechter Annahme oder schlechtem Pass", "Den Läufer im Rücken verfolgen und nicht aufgeben", "Nach dem Ballgewinn ruhig zum Zielspieler spielen"],
 "materials": ["2 Minitore", "10 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zurück sprinten und abfangen. Drei gegen eins, und der Verteidiger sprintet zurück, um den Pass in die Tiefe abzufangen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Drei gegen eins", "Links spielt Team Neon drei gegen eins und zählt die Pässe. Spieler drei spielt zu Spieler acht, und Spieler neun läuft an.",
     ps("b1", [46, 29.6]), mv("r9", [40, 27], delay=0.3)),
   S("Läufer in die Tiefe", "Fünf Pässe sind geschafft. Spieler elf sprintet in die Endzone. Spieler neun schaut über die Schulter, sieht den Läufer und sprintet zurück.",
     mv("n11", [29, 16]), bl("r9", [29, 16], delay=0.3), mv("r9", [33, 18], after=True)),
   S("Abgefangen", "Spieler acht spielt den Ball in die Tiefe zu Spieler elf. Spieler neun ist rechtzeitig zurück und fängt den Ball ab.",
     ps("b1", [33.6, 18.6])),
   S("Zum Zielspieler: Punkt", "Spieler neun spielt sofort zu Spieler vier, und das gibt einen Punkt für Team Rot. Trifft Spieler elf ins Minitor, gibt das einen Punkt für Team Neon. Danach ist die rechte Hälfte dran, und Spieler neun tauscht mit Spieler vier.",
     ps("b1", [42.6, 52.6]))],
  "dims": dims(25, 75, 10, 47.5, "18 m", "14 m", rx=91)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im richtigen Moment abfangen.", "Den Moment erwischen",
    "Der Verteidiger rennt nicht blind auf den Ball. Er lauert und presst erst, wenn ein Angreifer den Ball schlecht annimmt oder schlecht passt. Dann geht er entschlossen drauf.",
    sp(), BAELLE + ERSATZ,
    [S("Lauern", "Jetzt ist die rechte Hälfte dran. Spieler zwei spielt zu Spieler sechs. Spieler zehn wartet und lauert auf einen Fehler.",
       ps("b2", [54.2, 40.6])),
     S("Schlechte Annahme", "Spieler sechs nimmt den Ball schlecht an, und er springt weg. Das ist der Moment: Spieler zehn presst sofort und erobert den Ball.",
       ps("b2", [57.6, 36.6]), mv("r10", [57, 36], delay=0.2)),
     S("Zum Zielspieler: Punkt", "Spieler zehn spielt sofort zu Spieler fünf, und das gibt einen Punkt für Team Rot.",
       ps("b2", [62.6, 52.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Mittelzone verteidigen.", "Die Mittelzone",
    "Eine zweite Linie teilt das Feld in drei Zonen. Der Verteidiger startet in der Mittelzone, durch die die Angreifer hindurch müssen. Er stellt Pässe zu, verfolgt Läufer in den Rücken und fängt den Ball ab.",
    sp(n11=(27, 43), n3=(45, 42), n8=(44, 26), r9=(35.5, 28), r4=(36, 53)), [B("b1", 27.6, 43.6), B("b2", 72.1, 44.6)] + ERSATZ,
    [S("Durch die Mittelzone", "Spieler elf spielt zu Spieler drei, der weiter in die Mittelzone zu Spieler acht. Spieler neun schiebt mit und presst.",
       ps("b1", [45.6, 42.6]), ps("b1", [44.6, 26.6], after=True), mv("r9", [38, 27], delay=0.4)),
     S("Läufer im Rücken", "Spieler elf sprintet in die Endzone. Spieler neun schaut über die Schulter, sieht den Läufer und verfolgt ihn.",
       mv("n11", [27.5, 31]), mv("n11", [31, 16], after=True), bl("r9", [31, 16], delay=0.4), mv("r9", [34, 18], after=True)),
     S("Abgefangen: Punkt", "Spieler acht spielt in die Tiefe, aber Spieler neun fängt den Ball ab und spielt sofort zu Spieler vier. Das gibt einen Punkt für Team Rot.",
       ps("b1", [34.6, 18.6]), ps("b1", [36.6, 53.6], after=True))],
    lines=LINES + [line(25, 31.5, 75, 31.5)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
