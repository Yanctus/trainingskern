import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-8 (U12-U14, Woche 16 Phase 5): Focus on That Technique (Warm Up). 20 x 20 Yards = Feld x 30-70, y 10-50 (18 x 18 m).
# Zwei Bahnen mit je vier Koordinationsringen (Kreise in lines), je zwei Hütchen links und rechts. Ausrichtung wie im PDF.
# Ein Team (im PDF blau) -> Team Neon, Nummern wie im PDF (2-9). Statt zwei Trainern: links der Trainer, rechts ein Springer
# (F), der die Doppelpässe spielt (nur ein Trainer erlaubt). Die Wartenden stehen unter dem Feld (3D-Abstand), im PDF stehen sie
# auf der Grundlinie. Beide Spieler laufen gleichzeitig und wechseln am Ende die Seite (wie im Video).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Ringe gezeichnet (22.11.2026): je vier ring() in einer Reihe (Abstand 5.5) statt Kreislinien; Start der Paare dafür bei y 48.5,
# Laufwege enden oberhalb der Ringe, Zickzack der Steigerung führt durch die Ringe.
T = P("T", "c", 28.8, 16, "T")
F = P("f1", "t", 72, 16, "F")
POS = {"n9": (42.2, 48.5), "n8": (57.4, 48.5), "n7": (33.5, 53), "n5": (25, 53), "n3": (16.5, 53),
       "n6": (66, 53), "n4": (74.5, 53), "n2": (83, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T, F]
BAELLE = [B("b1", 29.4, 16.6), B("b2", 72.6, 16.6), B("s1", 24.8, 13), B("s2", 24.8, 9.4)]
RY = (43, 37.5, 32, 26.5)
RINGE = [ring(x, y) for x in (42.2, 57.4) for y in RY]
LINES = [rect(30, 10, 40, 40)]
CONES = [C(39.2, 22.5), C(60.9, 22.5), C(39.2, 12.9), C(60.9, 12.9)] + RINGE

u = {"title": "Schnelle Füße zum Aufwärmen", "code": "UE-178", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Koordination", "Passspiel"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Ein Aufwärmen mit schnellen Füßen. Zwei Spieler laufen gleichzeitig durch die Ringe, gehen seitwärts zum Hütchen und sprinten über Kreuz auf die andere Seite. Dort spielen sie einen Doppelpass und laufen zurück. Es zählt die saubere Technik, nicht das Tempo.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Zwei Bahnen mit je vier Ringen, darüber links und rechts je zwei Hütchen.",
  "Verteilen: Die Spieler stehen in zwei Reihen unter den Ringen. Links oben steht der Trainer mit Bällen, rechts oben ein Springer mit Ball.",
  "Ablauf: Schnelle Füße durch die Ringe, seitwärts zum Hütchen, über Kreuz zum oberen Hütchen sprinten, Doppelpass, zurück zur anderen Reihe.",
  "Wechsel: Die zwei Spieler starten gleichzeitig. Sind sie oben angekommen, starten die nächsten zwei."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle, kleine Schritte durch die Ringe", "Nach dem Sprint genau passen", "Ruhig zurücklaufen und durchatmen", "Sauber sprinten: Arme mitnehmen, kräftige Schritte"],
 "materials": ["8 Koordinationsringe", "4 Hütchen", "Einige Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Schnelle Füße zum Aufwärmen. Zwei Spieler laufen gleichzeitig durch die Ringe, sprinten über Kreuz und spielen einen Doppelpass.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Durch die Ringe", "Spieler neun und Spieler acht starten gleichzeitig. Mit schnellen, kleinen Schritten laufen beide durch die Ringe.",
     mv("n9", [42.2, 25]), mv("n8", [57.4, 25])),
   S("Seitwärts zum Hütchen", "Dann gehen beide seitwärts zum Hütchen: Spieler neun nach links, Spieler acht nach rechts.",
     mv("n9", [36.5, 27]), mv("n8", [63.6, 27])),
   S("Über Kreuz sprinten", "Jetzt sprinten beide über Kreuz zum oberen Hütchen auf der anderen Seite.",
     mv("n9", [63.5, 16]), mv("n8", [36.6, 16])),
   S("Doppelpass", "Der Trainer spielt Spieler acht den Ball zu, und Spieler acht passt direkt zurück. Gleichzeitig spielt Spieler neun einen Doppelpass mit dem Springer.",
     ps("b1", [37.2, 16.6]), ps("b1", [29.4, 16.6], after=True), ps("b2", [64.1, 16.6]), ps("b2", [72.6, 16.6], after=True)),
   S("Zurück und wechseln", "Beide laufen außen zurück und stellen sich hinten an die andere Reihe. Geschafft! Jetzt sind Spieler sieben und Spieler sechs dran.",
     mv("n8", [8, 53]), mv("n9", [92, 53]))],
  "dims": dims(30, 70, 10, 50, "18 m", "18 m")},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Seitwärts durch die Ringe, dann vor und zurück.", "Seitwärts und vor und zurück",
    "Die Spieler hüpfen seitwärts im Zickzack durch die Ringe. Am Hütchen sprinten sie nach vorn und laufen rückwärts zurück. Dann sprinten sie zum Hütchen auf der anderen Seite. Das schult Gleichgewicht, Antritt und Abbremsen.",
    sp(), BAELLE,
    [S("Zickzack durch die Ringe", "Spieler neun und Spieler acht laufen gleichzeitig seitwärts im Zickzack durch die Ringe.",
       *[mv("n9", [42.2 + (1.5 if k % 2 == 0 else -1.5), y], after=k > 0 or None) for k, y in enumerate(RY)],
       *[mv("n8", [57.4 + (-1.5 if k % 2 == 0 else 1.5), y], after=k > 0 or None) for k, y in enumerate(RY)]),
     S("Vor und zurück", "Beide gehen seitwärts zum Hütchen, sprinten nach vorn zum oberen Hütchen und laufen rückwärts wieder zurück.",
       mv("n9", [36.5, 25.5]), mv("n9", [36.5, 15.5], after=True), mv("n9", [36.5, 25.5], after=True),
       mv("n8", [63.6, 25.5]), mv("n8", [63.6, 15.5], after=True), mv("n8", [63.6, 25.5], after=True)),
     S("Zum Hütchen gegenüber", "Jetzt sprinten beide über Kreuz zum mittleren Hütchen auf der anderen Seite.",
       mv("n9", [63, 25]), mv("n8", [37, 25])),
     S("Doppelpass und zurück", "Spieler neun spielt einen Doppelpass mit dem Springer, Spieler acht mit dem Trainer. Dann laufen beide außen zurück, und Spieler sieben und Spieler sechs sind dran.",
       ps("b2", [63.6, 25.6]), ps("b2", [72.6, 16.6], after=True), ps("b1", [37.6, 25.6]), ps("b1", [29.4, 16.6], after=True),
       mv("n9", [92, 53], after=True), mv("n8", [8, 53], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Mit dem Ball am Fuß zurücklaufen.", "Mit Ball zurücklaufen",
    "Nach den Ringen und dem Hütchen sprinten die Spieler nach vorn. Dort bekommen sie einen Pass, nehmen den Ball mit und dribbeln zur eigenen Reihe zurück. Der letzte Spieler der Reihe passt den Ball zurück nach oben.",
    sp(), BAELLE,
    [S("Ringe und Hütchen", "Spieler neun und Spieler acht laufen gleichzeitig durch die Ringe und gehen seitwärts zum Hütchen.",
       mv("n9", [42.2, 25]), mv("n9", [36.5, 27], after=True), mv("n8", [57.4, 25]), mv("n8", [63.6, 27], after=True)),
     S("Pass nach dem Sprint", "Beide sprinten nach vorn. Der Trainer passt zu Spieler neun, der Springer zu Spieler acht.",
       mv("n9", [36.5, 16]), mv("n8", [63.6, 16]), ps("b1", [37.1, 16.6], delay=0.6), ps("b2", [64.2, 16.6], delay=0.6)),
     S("Mit Ball zurück", "Beide nehmen den Ball mit und dribbeln außen zurück zur eigenen Reihe. Dort passen sie zum letzten Spieler, zu Spieler drei und Spieler zwei.",
       dr("n9", "b1", [12, 45]), ps("b1", [17.1, 53.6], after=True), dr("n8", "b2", [88, 45]), ps("b2", [83.6, 53.6], after=True)),
     S("Pass nach oben", "Spieler drei passt zurück zum Trainer, Spieler zwei zum Springer. Jetzt sind Spieler sieben und Spieler sechs dran.",
       ps("b1", [29.4, 16.6]), ps("b2", [72.6, 16.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
