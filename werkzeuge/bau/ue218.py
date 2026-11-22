import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P9 (U12-U14, Woche 32 Phase 4): 2 v 2 Pressing Game. 25 x 25 Yards = Feld x 20-80, y 4-56 (23 m), in vier Zonen geteilt
# (gestrichelt bei x 50 und y 30), Minitore in allen vier Ecken. Mittelzone (10 x 10 Yards) etwas größer gezeichnet (x 35-65, y 17-43),
# damit die acht Verteidiger mit 3D-Abstand hineinpassen (zwei Reihen zu vier). Blau (Ballbesitz) -> Team Neon (2 bis 9),
# Pink (Verteidiger) -> Team Rot, neu nummeriert 10 bis 17 (im Video doppelte Nummern). Ein Trainer statt zwei, links neben dem Feld.
# Kein Tor oben möglich (vier Ecktore). Seitenwechsel in der Grundform nach unten (oben links -> unten links), im PDF nach rechts.
# Sichtkegel aus dem Video ("Know when to press at right time - anticipation", Kegel eingezeichnet) und Text ("Awareness of next
# pass"): Der Verteidiger der nächsten Zone schaut schon zum Ball, bevor der Pass in seine Zone kommt.
T = P("T", "c", 9, 30, "T")
POS = {"n2": (24, 14), "n3": (36, 5), "n4": (64, 5), "n5": (76, 14), "n6": (76, 46), "n7": (64, 55), "n8": (36, 55), "n9": (24, 46),
       "r10": (37.4, 21), "r11": (45.8, 21), "r12": (54.2, 21), "r13": (62.6, 21),
       "r14": (62.6, 39), "r15": (54.2, 39), "r16": (45.8, 39), "r17": (37.4, 39)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 10.6, 26.5), B("s2", 7, 26.5)]
LINES = [rect(20, 4, 60, 52), line(50, 4, 50, 56), line(20, 30, 80, 30), rect(35, 17, 30, 26, dashed=True)]
TORE = [{"x": 20, "y": 9, "side": "left"}, {"x": 80, "y": 9, "side": "right"}, {"x": 20, "y": 51, "side": "left"}, {"x": 80, "y": 51, "side": "right"}]

u = {"title": "Pressen zu zweit in vier Zonen", "code": "UE-218", "kind": "Spielform",
 "focuses": ["Verteidigen", "Passspiel", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 16, "players_max": 16, "field_size": "23 x 23 m",
 "description": "Ein Feld mit vier Zonen und einem Minitor in jeder Ecke. Team Neon hat in jeder Zone zwei Spieler und darf erst nach zwei Pässen in die nächste Zone spielen. Team Rot presst immer zu zweit, sobald der Ball in seine Zone kommt, und schießt nach einem Ballgewinn aufs Minitor. Schafft Team Neon alle vier Zonen, gibt das einen Punkt für Team Neon.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern in vier Zonen. In jeder Ecke ein Minitor, in der Mitte eine kleine Zone von etwa 9 mal 9 Metern.",
  "Verteilen: Team Neon mit acht Spielern, zwei in jeder Zone. Team Rot mit acht Spielern in der Mittelzone, je zwei gehören zu einer Zone. Der Trainer steht links mit Bällen.",
  "Ablauf: Der Trainer gibt Team Neon den Ball. Die zwei Roten dieser Zone pressen sofort. Nach zwei Pässen spielt Team Neon in die nächste Zone, dort pressen die nächsten zwei.",
  "Wertung und Wechsel: Schafft Team Neon alle vier Zonen, gibt das einen Punkt für Team Neon. Erobert Team Rot den Ball und trifft ins Minitor, gibt das einen Punkt für Team Rot. Nach einer festen Zeit tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell zu zweit pressen, sobald der Ball in die Zone kommt", "Keine Lücke zwischen den beiden Verteidigern lassen", "Den nächsten Pass ahnen und früh losstarten", "Mit Ball die Verteidiger anlocken und genau in die nächste Zone spielen"],
 "materials": ["4 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pressen zu zweit in vier Zonen. Team Neon spielt sich durch alle vier Zonen, und Team Rot presst immer zu zweit.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 24.6, 14.6)] + ERSATZ,
  "steps": [
   S("Zu zweit pressen", "Spieler zwei hat den Ball in der Zone oben links und spielt zu Spieler drei. Sofort laufen Spieler zehn und Spieler elf aus der Mitte heraus und pressen zu zweit.",
     ps("b1", [36.6, 5.6]), mv("r11", [40, 11], delay=0.2), mv("r10", [30, 18], delay=0.2)),
   S("Zweiter Pass", "Spieler drei spielt zurück zu Spieler zwei. Das sind zwei Pässe. Spieler siebzehn in der Mitte schaut schon zum Ball und weiß: Gleich kommt der Pass in seine Zone.",
     ps("b1", [24.6, 14.6]), bl("r17", [27, 20], after=True)),
   S("Ab in die nächste Zone", "Jetzt spielt Spieler zwei nach unten zu Spieler neun. Spieler siebzehn und Spieler sechzehn pressen sofort, wenn der Ball ankommt.",
     ps("b1", [24.6, 46.6]), mv("r17", [29, 43], delay=0.4), mv("r16", [31, 50], delay=0.4)),
   S("Abfangen: Punkt", "Spieler neun will zu Spieler acht passen, aber Spieler sechzehn fängt den Ball ab und schießt ins Minitor in der Ecke. Das gibt einen Punkt für Team Rot. Schafft Team Neon alle vier Zonen, gibt das einen Punkt für Team Neon. Dann bringt der Trainer einen neuen Ball, und nach einer festen Zeit tauschen die Teams die Rollen.",
     ps("b1", [31.6, 50.6]), dr("r16", "b1", [22, 51], after=True))],
  "dims": dims(20, 80, 4, 56, "23 m", "23 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zu zweit pressen und keine Lücke lassen.", "Keine Lücke lassen",
    "Die beiden Verteidiger laufen gemeinsam an. Der erste macht den Weg nach innen zu, der zweite stellt sich in den Passweg. So gibt es keine Lücke, und der Pass kann abgefangen werden.",
    sp(), [B("b1", 64.6, 5.6)] + ERSATZ,
    [S("Zusammen anlaufen", "Spieler vier hat den Ball in der Zone oben rechts. Spieler zwölf läuft ihn schräg an und macht den Weg nach innen zu. Spieler dreizehn bleibt nah dran und stellt sich zwischen Spieler vier und Spieler fünf.",
       mv("r12", [58, 11]), mv("r13", [69, 12], delay=0.2)),
     S("Abfangen: Punkt", "Spieler vier spielt trotzdem zu Spieler fünf. Spieler dreizehn fängt den Ball ab und schießt ins Minitor oben rechts. Das gibt einen Punkt für Team Rot.",
       mv("r13", [71, 10]), ps("b1", [71.6, 10.6], delay=0.2), dr("r13", "b1", [78.5, 9.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Nur noch ein Pass vor dem Wechsel.", "Nur ein Pass",
    "Team Neon darf schon nach einem Pass in die nächste Zone spielen. Die Verteidiger müssen noch schneller pressen und den nächsten Pass früh ahnen. Es wird schneller, und alle müssen schnell entscheiden.",
    sp(), [B("b1", 24.6, 14.6)] + ERSATZ,
    [S("Ein Pass", "Spieler zwei spielt zu Spieler drei. Spieler zehn und Spieler elf pressen sofort.",
       ps("b1", [36.6, 5.6]), mv("r11", [40, 11], delay=0.2), mv("r10", [30, 18], delay=0.2)),
     S("Sofort weiter", "Nach nur einem Pass spielt Spieler drei schon in die Zone oben rechts zu Spieler vier. Spieler zwölf und Spieler dreizehn pressen, sobald der Ball ankommt.",
       ps("b1", [64.6, 5.6]), mv("r12", [58, 11], delay=0.4), mv("r13", [71, 19], delay=0.4)),
     S("Durch alle Zonen: Punkt", "Spieler vier spielt zu Spieler fünf, und der spielt gleich weiter nach unten zu Spieler sechs. Geht es so durch alle vier Zonen, gibt das einen Punkt für Team Neon.",
       ps("b1", [76.6, 14.6]), ps("b1", [76.6, 46.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
