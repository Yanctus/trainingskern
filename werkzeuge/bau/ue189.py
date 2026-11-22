import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 99-P5 (U12-U14, Woche 21 Phase 2): 4 V 4 + 2 Breakout Possession Game (Skill Rondo). 25 x 40 Yards = Feld x 34.5-65.5,
# y 5-55 (23 x 37 m), quer in drei Zonen (Endzonen je 10 Yards, gestrichelt), oben und unten ein Minitor. Ausrichtung wie im PDF.
# Blau (am Ball: 2, 5, 6, 8) -> Team Neon, Pink/Rot (4, 6, 7, 8) -> Team Rot, Nummern neu wegen Doppelten: Rot 6 -> 3, Rot 8 -> 10.
# Gold (die zwei Springer in den Endzonen) -> Springer F (f1 oben, f2 unten). Positionen auf ein Raster gesetzt (3D-Abstand),
# Ablauf wie im Video: Springer unten -> Neon 2 -> diagonal zu Neon 6 -> Springer oben -> Ablage auf Neon 8, der in die Endzone startet.
# Kein Torwart, darum Abschluss ins Eck. Steigerung 1 (Rot erobert und behält den Ball) und 2 (Springer tauscht mit Mittelspieler) wie im Video.
# Sichtkegel: Ton "positioning to see three corners of the rondo" und Video "Players ready to receive, adopt an open body shape"
# -> Neon 2 schaut vor der Ballannahme nach oben zu Neon 6 (Sinn: Ausbruchpass vorbereiten).
T = P("T", "c", 80, 14, "T")
POS = {"n6": (37.5, 22.5), "r10": (46, 22.5), "r3": (54.5, 22.5), "n8": (63, 22.5),
       "n5": (37.5, 38), "r4": (46, 38), "r7": (54.5, 38), "n2": (63, 38),
       "f1": (46, 7), "f2": (46, 53.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 17.5), B("s2", 80, 17.5)]
LINES = [rect(34.5, 5, 31, 50), line(34.5, 17.3, 65.5, 17.3), line(34.5, 42.7, 65.5, 42.7)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}]

u = {"title": "Rondo mit Ausbruchpass", "code": "UE-189", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "23 x 37 m",
 "description": "Vier gegen vier in der Mittelzone, dazu ein Springer in jeder Endzone. Das Team am Ball lässt den Ball laufen und spielt dann den Ausbruchpass zu einem Springer. Der legt für einen Mitspieler ab, der in die Endzone startet und aufs Minitor schießt. Erobert das andere Team den Ball, darf es selbst auf beide Tore spielen.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 37 Metern, quer in drei Zonen geteilt: oben und unten je eine Endzone von 9 Metern, dazwischen die Mittelzone. An beiden Enden ein Minitor.",
  "Verteilen: Team Neon und Team Rot spielen zu viert in der Mittelzone. In jeder Endzone steht ein Springer. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon hält den Ball mit Hilfe der Springer. Nach dem Ausbruchpass legt der Springer ab, ein Spieler startet in die Endzone und schießt. Erobert Team Rot den Ball, darf es auf beide Tore spielen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach bringt der Trainer einen neuen Ball. Nach einigen Minuten werden die Springer gewechselt, damit jeder einmal dran ist."],
 "organisation_show": ORG,
 "coaching_points": ["Erkennen, wann der Ausbruchpass passt", "Offen stehen, um den Ball nach vorn mitzunehmen", "Steilpässe schnell und scharf spielen", "Freilaufen und die Überzahl nutzen"],
 "materials": ["2 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Rondo mit Ausbruchpass. Vier gegen vier in der Mitte, und mit Hilfe der Springer bricht das Team am Ball aus und schießt aufs Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 46.6, 54.1)] + ERSATZ,
  "steps": [
   S("Schulterblick", "Der Springer unten hat den Ball. Spieler zwei schaut vorher nach oben: Ist Spieler sechs frei? Dann spielt der Springer zu Spieler zwei.",
     bl("n2", [46, 28]), ps("b1", [63.6, 38.6], after=True)),
   S("Pass durch die Mitte", "Spieler zwei steht offen und spielt den Ball flach und scharf schräg durch die Mitte zu Spieler sechs.",
     ps("b1", [38.1, 23.1])),
   S("Ausbruchpass", "Spieler sechs spielt den Ausbruchpass zum Springer oben. Gleichzeitig startet Spieler acht in die obere Endzone.",
     ps("b1", [46.6, 7.6]), mv("n8", [58, 12], delay=0.3)),
   S("Ablage: Punkt", "Der Springer legt direkt ab, und Spieler acht schießt flach ins Eck. Das gibt einen Punkt für Team Neon. Dann spielt der Trainer einen neuen Ball zum Springer unten, und es geht weiter.",
     ps("b1", [58.6, 12.6]), ps("b1", [52.4, 5.3], after=True))],
  "dims": dims(34.5, 65.5, 5, 55, "23 m", "37 m")},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball erobert, behält ihn.", "Ball erobern und behalten",
    "Erobert Team Rot den Ball, sichert es ihn zuerst mit ein paar Pässen. Erst dann bricht es über einen Springer aus. Team Neon verteidigt jetzt und versucht sofort, den Ball zurückzuerobern.",
    sp(), [B("b1", 63.6, 23.1)] + ERSATZ,
    [S("Ball erobert", "Spieler acht hat den Ball. Spieler drei läuft ihn an und erobert den Ball. Jetzt ist Team Rot am Ball, und Team Neon verteidigt.",
       mv("r3", [60, 24.5]), ps("b1", [60.6, 25.1], delay=0.5)),
     S("Ball sichern", "Spieler drei spielt sicher zu Spieler sieben. Spieler zwei läuft sofort an, um den Ball zurückzuerobern.",
       ps("b1", [55.1, 38.6]), mv("n2", [59.5, 35], delay=0.3)),
     S("Ausbruch: Punkt", "Spieler sieben spielt den Ausbruchpass zum Springer unten, und Spieler vier startet in die Endzone. Der Springer legt ab, und Spieler vier schießt ins Eck. Das gibt einen Punkt für Team Rot.",
       ps("b1", [46.6, 54.1]), mv("r4", [56, 47.5], delay=0.2), ps("b1", [56.6, 48.1], after=True), ps("b1", [52.4, 54.7], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Springer tauscht mit einem Spieler aus der Mitte.", "Mit dem Springer tauschen",
    "Spielt ein Spieler aus der Mitte den Springer an, läuft er sofort in die Endzone und wird selbst zum Springer. Der Springer dribbelt dafür in die Mitte und spielt dort mit. So entstehen neue Passwege, und die Gegner müssen sich neu sortieren.",
    sp(), [B("b1", 38.1, 38.6)] + ERSATZ,
    [S("Platz tauschen", "Spieler fünf spielt zum Springer unten und läuft sofort in die Endzone. Gleichzeitig dribbelt der Springer in die Mitte.",
       mv("n5", [37.5, 50], delay=0.4), ps("b1", [46.6, 54.1]), dr("f2", "b1", [41, 43], after=True)),
     S("Neuer Springer", "Jetzt ist Spieler fünf unten der Springer. Der alte Springer spielt in der Mitte zu ihm, und Spieler zwei startet in die Endzone.",
       ps("b1", [38.1, 50.6]), mv("n2", [57, 48], delay=0.3)),
     S("Ablage: Punkt", "Spieler fünf legt quer ab, und Spieler zwei schießt flach ins Eck. Das gibt einen Punkt für Team Neon.",
       ps("b1", [57.6, 48.6]), ps("b1", [52.4, 54.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
