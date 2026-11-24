import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 17-P1 (U15-U17, Woche 34 Phase 5): Retain Possession To Attack Rondo Based (PDF: Retain Possession in the Rondo).
# 25 x 25 Yards = 23 x 23 m (gerundet 25 x 25 m), Feld x 26-74, y 7-51, in vier Viertel geteilt (gestrichelt).
# Um 180 Grad gedreht: Das Minitor steht oben (im PDF unten), Team Neon spielt nach oben. Dadurch stehen Spieler 2 rechts und
# Spieler 8 links, Spieler 4 rechts und Spieler 10 links von der Mitte. Der Ton nennt 25 x 20 Yards, das PDF 25 x 25: PDF genommen.
# PDF blau -> Team Neon (2, 4, 6, 8, 9, 10, Nummern wie im PDF), pink -> Team Rot, neu nummeriert, weil 8 und 9 doppelt sind:
# 9 -> 5, 8 -> 7; 3 und 11 bleiben. In jedem Viertel ein Verteidiger. Positionen auf ein Spaltenraster gesetzt (3D-Abstand),
# Spieler 6, 2 und 8 knapp außerhalb der Linien wie im PDF. Ein Trainer statt zwei (links an der Seite).
# Grundform nach PDF-Skizze (6 -> 4 -> 2 -> 9, Abschluss). Die Variante mit 15 oder 20 Spielern (zwei Felder) nur im Text.
# Fassungen: PDF Key Coaching Point 1 (nach dem Treffer spielt der Trainer sofort den nächsten Ball rein) und 2 (nach dem
# Ballgewinn zehn Pässe im vier gegen drei, dann aufs Minitor).
# Spieler 9 dreht nach der Annahme auf: Drehpfeil (drehen), kein Kegel.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Keine Dublette: UE-305 (95-P9, sieben gegen vier mit zwei Toren und Mittelzone), UE-342 (99-P9), UE-362 (49-P5) und
# UE-189 sind anders aufgebaut (keine Viertel mit je einem Verteidiger, keine Spitze vor einem Minitor).
T = P("T", "c", 8, 44, "T")
ERSATZ = [B("s1", 11.5, 47), B("s2", 5, 47)]
POS = {"n6": (49, 53.5), "n2": (77, 30), "n8": (22, 30), "n4": (58, 29), "n10": (40, 29), "n9": (49, 13),
       "r7": (31, 17), "r5": (31, 39), "r3": (67, 17), "r11": (67, 39)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(26, 7, 48, 44), line(50, 7, 50, 51), line(26, 29, 74, 29)]
TORE = [{"x": 50, "y": 7, "side": "top"}]
DIMS = dims(26, 74, 7, 51, "25 m", "25 m", rx=87)
TB = [8.6, 44.6]  # Ball am Fuß des Trainers

u = {"title": "Positionsrondo zum Minitor", "code": "UE-395", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 20,
 "field_size": "25 x 25 m",
 "description": "Ein Positionsrondo auf einem Feld mit vier Vierteln. Team Neon hat drei Spieler außen an den Linien, zwei im Zentrum und eine Spitze vor dem Minitor, Team Rot hat in jedem Viertel einen Verteidiger. Team Neon lässt den Ball schnell laufen, spielt durch die Linien auf die Spitze und schließt ab. Erobert Team Rot den Ball, braucht es zehn Pässe, bevor es selbst aufs Minitor darf.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern, mit gestrichelten Linien in vier gleich große Viertel geteilt. In der Mitte einer Linie steht ein Minitor.",
  "Verteilen: Team Neon mit sechs Spielern. Drei stehen außen an den Linien, zwei im Zentrum auf der Mittellinie, die Spitze vor dem Minitor. Von Team Rot steht in jedem Viertel ein Verteidiger. Der Trainer steht mit Bällen an der Seite. Bei zwanzig Spielern zwei Felder nebeneinander.",
  "Ablauf: Team Neon spielt mit ein oder zwei Kontakten und sucht den Pass durch die Linien auf die Spitze. Die Spitze dreht auf und schließt ab. Nach jedem Treffer spielt der Trainer sofort den nächsten Ball ins Zentrum.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, spielt es vier gegen drei gegen die Spieler im Feld und darf nach zehn Pässen aufs Minitor, das gibt einen Punkt für Team Rot. Nach einigen Minuten werden die Verteidiger getauscht."],
 "organisation_show": ORG,
 "coaching_points": ["Ein, zwei Kontakte, dann ist der Druck weg", "Die zwei im Zentrum suchen die Außen", "Durch die Linien auf die Spitze", "Nach dem Ballgewinn breit und tief"],
 "materials": ["1 Minitor", "Hütchen für Feld und Viertel", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Positionsrondo zum Minitor. Sechs gegen vier in vier Vierteln. Team Neon spielt durch die Linien auf die Spitze, und Team Rot braucht nach dem Ballgewinn zehn Pässe.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 49.6, 54.1), B("b0", *TB)] + ERSATZ,
  "steps": [
   S("Ins Zentrum zu Spieler vier", "Spieler sechs hat den Ball hinten an der Linie. Flach ins Zentrum zu Spieler vier. Spieler elf schiebt in seinem Viertel zum Ball, raus darf er nicht.",
     ps("b1", [58.6, 29.6]), mv("r11", [63, 35], delay=0.3)),
   S("Raus zu Spieler zwei", "Spieler vier legt mit einem Kontakt nach außen auf Spieler zwei. Die Verteidiger müssen wieder rüber.",
     ps("b1", [77.6, 30.6]), mv("r11", [67, 39], delay=0.3)),
   S("Durch die Linien auf die Spitze", "Zwischen Spieler drei und Spieler elf ist eine Lücke. Spieler zwei spielt flach durch, genau auf Spieler neun vor dem Minitor.",
     ps("b1", [49.6, 13.6])),
   S("Aufdrehen, Abschluss: Punkt", "Spieler neun dreht mit dem ersten Kontakt auf und schießt ins Minitor, und das gibt einen Punkt für Team Neon. Sofort spielt der Trainer den nächsten Ball rein zu Spieler zehn.",
     drehen("n9", [50, 7], gegen=True), ps("b1", [50, 7.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Treffer kommt sofort der nächste Ball.", "Sofort der nächste Ball",
    "Ist der Ball im Minitor, spielt der Trainer sofort den nächsten Ball ins Zentrum. Keiner hat Zeit zum Durchatmen. Die Verteidiger müssen sofort wieder stehen, und Team Neon spielt gleich wieder mit ein oder zwei Kontakten.",
    sp(), [B("b0", *TB)] + ERSATZ,
    [S("Der Trainer spielt sofort rein", "Der Ball ist gerade im Minitor, da kommt schon der nächste. Der Trainer spielt zu Spieler acht. Spieler fünf schiebt sofort zum Ball.",
       ps("b0", [22.6, 30.6]), mv("r5", [27, 36], delay=0.4)),
     S("Direkt weiter", "Spieler acht legt direkt ins Zentrum auf Spieler zehn, und der spielt gleich weiter zu Spieler vier. Zwei Kontakte, und der Druck ist weg.",
       ps("b0", [40.6, 29.6]), ps("b0", [58.6, 29.6], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Nach dem Ballgewinn zehn Pässe.", "Abgefangen, zehn Pässe",
    "Fängt Team Rot den Ball ab, spielt es vier gegen drei gegen die Spieler im Feld. Erst nach zehn Pässen darf es aufs Minitor. Die Verteidiger machen das Feld breit und tief und spielen von Viertel zu Viertel.",
    sp(), [B("b1", 58.6, 29.6), B("b0", *TB)] + ERSATZ,
    [S("Spieler drei fängt ab", "Spieler vier will steil auf Spieler neun spielen. Spieler drei ahnt das, geht dazwischen und hat den Ball.",
       mv("r3", [56, 20]), ps("b1", [56.6, 20.6], delay=0.3)),
     S("Breit und tief, Pässe zählen", "Jetzt steht es vier gegen drei. Der Ball läuft von Viertel zu Viertel, über Spieler sieben und Spieler fünf bis zu Spieler elf. Spieler neun, Spieler zehn und Spieler vier jagen ihn.",
       ps("b1", [31.6, 17.6]), mv("r3", [67, 17], delay=0.5), mv("n9", [42, 19], delay=0.3),
       ps("b1", [31.6, 39.6], after=True), mv("n10", [34, 31], delay=1.0), ps("b1", [67.6, 39.6], after=True), mv("n4", [60, 33], delay=1.6)),
     S("Zehn Pässe, dann aufs Tor: Punkt", "Der zehnte Pass ist gespielt. Spieler elf spielt steil zu Spieler drei, und der trifft ins Minitor. Das gibt einen Punkt für Team Rot. Danach bringt der Trainer den nächsten Ball zu Team Neon.",
       ps("b1", [67.6, 17.6]), ps("b1", [50.5, 7.3], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
