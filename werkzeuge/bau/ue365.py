import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 51-P11 (U15-U17, Woche 23 Phase 3): False 9 Movements in the Final 3rd (Medium Sided Game). 50 x 36 Yards = 46 x 33 m
# (gerundet 35 x 45 m), Mittelkanal 10 Yards = 9 m (gestrichelt, Hütchen wie im PDF an den Enden und bei einem und zwei Dritteln).
# LANGES FELD QUER (Vorbild ue317.py; mit 46 m kein Großfeld): Tore links und rechts (im PDF unten und oben), direkt in
# Querkoordinaten geplant (Feld x 9-89, y 4-51; PDF links -> oben, PDF rechts -> unten). Team Neon greift nach rechts an.
# Sieben gegen sieben mit Torhütern: Pink -> Team Neon (1, 4, 7, 8, 9, 10, 11 wie im PDF), Navy -> Team Rot, neu nummeriert,
# weil die Nummern doppelt sind: 4 -> 2, 7 -> 3, 9 -> 12, 11 -> 13 (5 und 6 bleiben). Die beiden Torhüter als neutrale
# Torhüter k1 / k2 (TW) wie in ue317.py (zwei Team-Torhüter mit Label TW meldet pruefen als doppelte Nummer).
# Positionen für den 3D-Abstand leicht versetzt (z. B. Spieler zwei etwas weiter weg von Spieler neun). Ein Trainer statt zwei,
# unten an der Seitenlinie nahe dem Kanal (spielt die Neun im Kanal an).
# Fassungen: Progression 1 (Prallpass aus dem Kanal gibt einen Punkt) und Progression 2 (Zone in der Mitte des Kanals, in der
# ein Verteidiger bleiben muss; als Zone von Team Rot in Orange).
# Sichtkegel: Text/Ton "Receive on the half turn to attack forward - scan to see pressure", im Video nicht eingezeichnet.
# Richtung aus dem Sinn: Spieler neun schaut vor der Annahme über die Schulter zu seinem Gegenspieler (bl mit von), nach der
# Annahme schwenkt der Kegel zum Passziel, dazu der Drehpfeil.
T = P("T", "c", 31, 55.3, "T")  # unten an der Seitenlinie nahe dem Kanal
ERSATZ = [B("s1", 34.5, 55.8), B("s2", 37, 55.8)]
POS = {"k1": (13, 28.5), "n4": (25.5, 28.5), "n10": (38.5, 14), "n8": (44.5, 44), "n9": (59, 28), "n11": (69.5, 11), "n7": (69.5, 44),
       "k2": (86.5, 27.5), "r5": (78, 11), "r6": (78, 44), "r2": (67.5, 27.5), "r3": (47.5, 7), "r12": (35, 30), "r13": (54, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
KX0, KX1 = 40, 56  # Mittelkanal
LINES = [rect(9, 4, 80, 47), line(KX0, 4, KX0, 51), line(KX1, 4, KX1, 51)]
TORE = [{"x": 9, "y": 27.5, "side": "left", "size": "gross"}, {"x": 89, "y": 27.5, "side": "right", "size": "gross"}]
CONES = [C(x, y) for x in (KX0, KX1) for y in (4, 19, 36, 51)]
DIMS = dims(9, 89, 4, 51, "45 m", "35 m")[:1]  # Tore links und rechts: nur die Längen-Maßlinie
ZONE = {"type": "zone", "x": KX0, "y": 19, "w": KX1 - KX0, "h": 17, "color": "orange"}
GEGNER = [67.5, 27.5]  # Spieler zwei im Rücken von Spieler neun

u = {"title": "Falsche Neun im Mittelkanal", "code": "UE-365", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Ballannahme", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "35 x 45 m",
 "description": "Sieben gegen sieben mit Torhütern auf zwei große Tore. Quer durch die Mitte läuft ein schmaler Kanal. Die Spitze lässt sich in diesen Kanal fallen, nimmt halb aufgedreht an und bringt den Angriff ins letzte Drittel, zusammen mit den Flügelstürmern und nachrückenden Mitspielern. Erobert die andere Mannschaft den Ball, greift sie mit denselben Regeln an.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 45 Metern mit zwei großen Toren. In der Mitte markieren Hütchen einen Kanal von 9 Metern Breite über die ganze Feldbreite.",
  "Verteilen: Team Neon und Team Rot mit je sechs Feldspielern und einem Torwart. Jede Spitze steht vorn vor der gegnerischen Abwehr. Der Trainer steht mit vielen Bällen an der Seitenlinie neben dem Kanal.",
  "Ablauf: Freies Spiel. Die Spitze lässt sich in den Kanal fallen, nimmt an, dreht auf und spielt mit den Flügelstürmern zum Abschluss. Wer den Ball erobert, greift genauso an. Gewinnt ein Team den Ball schon in der Abwehrhälfte des Gegners, darf es sofort frei angreifen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Ist der Ball aus dem Spiel, spielt der Trainer die Spitze im Kanal an oder gibt den Ball dem Torwart zum Aufbau."],
 "organisation_show": ORG,
 "coaching_points": ["Im richtigen Moment in den Kanal kommen", "Vorher über die Schulter schauen, halb aufgedreht annehmen", "Schnell mit den Flügelstürmern kombinieren", "Hinter die Spitze nachstoßen, Platz nutzen"],
 "materials": ["2 große Tore", "8 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Falsche Neun im Mittelkanal. Sieben gegen sieben auf zwei Tore. Die Spitze holt sich den Ball im Kanal in der Mitte, dreht auf und bringt den Angriff nach vorn.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 31.6, 55.9)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Spieler neun kommt in den Kanal", "Der Trainer bringt den Ball. Spieler neun lässt sich aus der Spitze in den Kanal fallen. Vorher schaut er über die Schulter, wie dicht Spieler zwei an ihm dran ist. Dann kommt der Pass vom Trainer.",
     mv("n9", [50.5, 27]), bl("n9", [41.5, 44], von=GEGNER, after=True), ps("b1", [51.1, 27.6], after=True)),
   S("Aufdrehen und raus auf Spieler sieben", "Spieler zwei ist nicht mitgegangen. Also dreht Spieler neun mit dem ersten Kontakt auf. Spieler sieben kommt außen ein Stück entgegen und bekommt den Ball.",
     bl("n9", [67.5, 40.5], von=[41.5, 44], dauer=1.3), drehen("n9", [67.5, 40.5], gegen=True, delay=0.4), mv("n7", [67.5, 40.5], delay=0.3),
     ps("b1", [68.1, 41.1], after=True), mv("n8", [52, 40], delay=0.6)),
   S("Querpass in die Mitte: Punkt", "Spieler elf startet hinter Spieler fünf in die Mitte. Spieler sieben spielt flach quer, und Spieler elf schiebt mit dem ersten Kontakt ein. Das gibt einen Punkt für Team Neon. Danach bringt der Trainer den nächsten Ball, und erobert Team Rot den Ball, greift es nach denselben Regeln an.",
     mv("n11", [78.5, 19]), ps("b1", [79.1, 19.6], after=True), ps("b1", [88.5, 24], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Prallpass aus dem Kanal gibt schon einen Punkt.", "Prallpass gibt einen Punkt",
    "Lässt sich die Spitze in den Kanal fallen und spielt einen Prallpass mit einem Kontakt zurück zu einem Mitspieler, gibt das einen Punkt. Der Gegenspieler muss mit in den Kanal, sonst gibt es den Punkt umsonst. Geht er mit, ist hinter ihm Platz, und genau da startet die Spitze sofort hinein.",
    sp(), [B("b1", 39.1, 14.6)] + ERSATZ,
    [S("Spieler zehn spielt in den Kanal", "Spieler neun kommt in den Kanal und schaut zum Ball. Spieler zehn spielt ihn flach an. Spieler zwei geht diesmal mit.",
       mv("n9", [51.5, 22.5]), mv("r2", [58, 24], delay=0.3), bl("n9", [38.5, 14], after=True), ps("b1", [52.1, 23.1], after=True)),
     S("Prallpass: Punkt", "Mit einem Kontakt lässt Spieler neun den Ball zu Spieler acht prallen, und das gibt einen Punkt für Team Neon. Dann dreht er sich weg und läuft in den Raum, den Spieler zwei frei gemacht hat.",
       mv("n8", [47, 40]), ps("b1", [47.6, 40.6], after=True), mv("n9", [66, 18], after=True)),
     S("Steil in den Lauf: Punkt", "Spieler acht spielt sofort steil in den Lauf von Spieler neun. Der nimmt mit und trifft, und das gibt noch einen Punkt für Team Neon.",
       ps("b1", [66.6, 18.6]), ps("b1", [88.5, 22.5], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Verteidiger muss in der Zone in der Mitte des Kanals bleiben.", "Verteidiger bleibt in Zone",
    "In der Mitte des Kanals liegt jetzt eine Zone. Ein Verteidiger von Team Rot muss dort bleiben und schirmt sie ab. Für die Spitze wird es eng. Sie sucht sich den Platz neben ihm, an seiner Schulter, und braucht gutes Timing beim Fallenlassen.",
    sp(r2=(48, 27.5)), [B("b1", 39.1, 14.6)] + ERSATZ,
    [S("Platz an der Schulter suchen", "Spieler zwei steht in der Zone und darf nicht raus. Spieler neun kommt neben ihn in den Kanal, an seine Schulter. Er schaut kurz, wo Spieler zwei steht, dann zum Ball. Spieler zehn spielt ihn an.",
       mv("n9", [58.5, 17]), mv("n9", [52, 13.5], after=True), bl("n9", [38.5, 14], von=[48, 27.5], after=True), ps("b1", [52.6, 14.1], after=True)),
     S("Aufdrehen, steil auf Spieler elf", "Spieler neun dreht weg von Spieler zwei auf und spielt sofort steil. Spieler elf ist außen hinter Spieler fünf gestartet.",
       bl("n9", [72, 16], von=[38.5, 14], dauer=1.3), drehen("n9", [72, 16], delay=0.4), mv("n11", [79, 17], delay=0.4),
       ps("b1", [79.6, 17.6], after=True)),
     S("Abschluss: Punkt", "Spieler elf zieht ab und trifft, und das gibt einen Punkt für Team Neon. Danach geht es mit dem nächsten Ball vom Trainer weiter.",
       ps("b1", [88.5, 24]))], lines=LINES + [ZONE])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
