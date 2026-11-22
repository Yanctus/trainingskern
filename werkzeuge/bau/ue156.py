import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 12-P11 (U12-U14, Woche 10 Phase 5): Defending Centrally MSG. 35 x 45 Yards = Feld x 30.6-69.4, y 5-55 (32 x 41 m), drei Bahnen
# (gestrichelt), an beiden Enden drei Minitore (Mitte 3 Punkte, außen 1 Punkt). Gedreht: Rot (im PDF dunkel, Angreifer) spielt nach
# oben, Neon (im PDF pink, verteidigt) verteidigt die oberen Tore. Nummern neu (im PDF doppelt): Neon 2-6, 8, 10; Rot 7, 9, 11-15.
# Positionen auf ein Spaltenraster gesetzt (3D-Abstand), Spielidee wie im PDF. Ein Trainer statt zwei.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 76, 30, "T")
POS = {"n5": (48.5, 9), "n8": (40, 17), "n4": (57, 17), "n6": (31.5, 26), "n3": (65.5, 22), "n2": (48.5, 25), "n10": (57, 49),
       "r15": (31.5, 9), "r9": (40, 33), "r11": (57, 33), "r12": (65.5, 40), "r14": (48.5, 41), "r7": (31.5, 46), "r13": (40, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 79.6, 33.5), B("s2", 76, 33.5)]
LINES = [rect(30.6, 5, 38.8, 50), line(43.2, 5, 43.2, 55), line(56.8, 5, 56.8, 55)]
TORE = [{"x": x, "y": 5, "side": "top"} for x in (37, 50, 63)] + [{"x": x, "y": 55, "side": "bottom"} for x in (37, 50, 63)]

u = {"title": "Das mittlere Tor schützen", "code": "UE-156", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 14, "players_max": 14, "field_size": "32 x 41 m",
 "description": "Sieben gegen sieben in drei Bahnen, an jedem Ende drei Minitore. Das Tor in der Mitte bringt drei Punkte, die beiden äußeren je einen. Das verteidigende Team steht kompakt, schützt zuerst das mittlere Tor und lenkt den Gegner nach außen. Zehn Pässe in Folge bringen dem Team am Ball einen Extrapunkt, darum muss die Abwehr auch rausrücken und pressen.",
 "organisation": ["Aufbauen: Ein Feld von 32 mal 41 Metern, längs in drei Bahnen geteilt. An jedem Ende in jeder Bahn ein Minitor.",
  "Verteilen: Zwei Teams zu siebt. Team Neon verteidigt die oberen Tore, Team Rot greift sie an. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Freies Spiel sieben gegen sieben. Die Verteidiger halten die Mitte zu und drängen nach außen. Wer den Ball erobert, greift sofort selbst an.",
  "Wertung: Mittleres Minitor drei Punkte, äußere Minitore ein Punkt. Zehn Pässe in Folge ein Extrapunkt. Nach einem Tor bringt der Trainer einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Zuerst die Bahn in der Mitte schützen", "Kompakt bleiben, kleine Abstände zwischen den Verteidigern", "Absprechen, wann gepresst und wann die Ordnung gehalten wird", "Gemeinsam rausrücken, damit der Gegner keine zehn Pässe schafft"],
 "materials": ["6 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Das mittlere Tor schützen. Sieben gegen sieben, und das verteidigende Team lenkt den Gegner weg vom wertvollen Tor in der Mitte.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 32.1, 46.6)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Team Rot greift nach oben an. Rot sieben spielt zu Rot vierzehn, der weiter zu Rot elf. Neon zehn läuft sofort an.",
     ps("b1", [49.1, 41.6]), ps("b1", [57.6, 33.6], after=True), mv("n10", [53, 44], delay=0.3)),
   S("Die Mitte ist zu", "Neon zwei und Neon vier schieben zusammen und machen die Mitte zu. Rot elf kommt nicht durch und spielt nach außen zu Rot zwölf.",
     mv("n2", [51, 29]), mv("n4", [58, 26], delay=0.1), ps("b1", [66.1, 40.6], delay=0.4), mv("n3", [60, 20], after=True)),
   S("Außen: nur ein Punkt", "Rot zwölf dribbelt außen hoch und trifft ins rechte Minitor. Das gibt einen Punkt für Team Rot, das mittlere Tor bleibt zu. Dann bringt der Trainer einen neuen Ball.",
     dr("r12", "b1", [66.5, 13]), ps("b1", [63, 5.3], after=True))],
  "dims": dims(30.6, 69.4, 5, 55, "32 m", "41 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit dem Körper nach außen lenken.", "Nach außen lenken",
    "Der Verteidiger läuft von innen an und stellt sich so, dass der Weg zur Mitte zu ist. Der Gegner kann nur nach außen. Dort wartet schon der Mitspieler und kann den Ball erobern.",
    sp(), [B("b1", 57.6, 33.6)] + ERSATZ,
    [S("Von innen anlaufen", "Rot elf hat den Ball. Neon vier läuft von innen an, und Rot elf muss nach außen dribbeln.",
       mv("n4", [55, 26.5]), dr("r11", "b1", [62, 31], delay=0.3)),
     S("Außen erobert", "Dort wartet Neon drei, erobert den Ball und dribbelt los. Jetzt greift Team Neon nach unten an.",
       mv("n3", [66, 27]), dr("n3", "b1", [68.5, 33], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Gemeinsam rausrücken.", "Gemeinsam rausrücken",
    "Wer nur hinten steht, lässt den Gegner in Ruhe passen, und zehn Pässe bringen ihm einen Extrapunkt. Darum rückt die Abwehr gemeinsam heraus und presst, sobald ein Pass kommt.",
    sp(), [B("b1", 40.6, 33.6)] + ERSATZ,
    [S("Gemeinsam raus", "Team Rot hat schon acht Pässe gespielt. Rot neun spielt zu Rot dreizehn, und Neon acht und Neon zwei rücken gemeinsam heraus.",
       ps("b1", [40.6, 49.6]), mv("n8", [45, 30], delay=0.2), mv("n2", [47, 33], delay=0.2)),
     S("Abgefangen", "Rot dreizehn will zu Rot vierzehn passen, aber Neon zwei fängt den Ball ab. Keine zehn Pässe für Team Rot, und jetzt greift Team Neon an.",
       mv("n2", [44.5, 38]), mv("n2", [45.5, 44.5], after=True), ps("b1", [46.1, 45.1], delay=0.5))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
