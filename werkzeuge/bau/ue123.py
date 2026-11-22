import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P1: 30 x 45 Yards, gespiegelt (Angriff nach rechts): Feld x 14-86, y 6-54, drei Bahnen je 16 hoch.
# Oben 1 gegen 2 auf zwei Minitore, Mitte 1 gegen 1 aufs große Tor, unten ohne Gegner um zwei Dummys aufs große Tor.
T = P("T", "c", 40, 1.5, "T")
CB = [B("c1", 42.5, 2.1)]
KEEP = [P("k1", "t", 82, 28, "TW"), P("k13", "t", 82, 44, "TW")]
POS = {"n2": (9, 14), "n3": (9, 30), "n4": (9, 46), "r5": (50, 13), "r6": (68, 16), "r7": (52, 30)}
DU = [P("d1", "t", 46, 47, "D"), P("d2", "t", 62, 44, "D")]
def sp(d=None, dummys=True):
    d = dict(d or POS)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + KEEP + (DU if dummys else []) + [T]
LINES = [rect(14, 6, 72, 48), line(14, 22, 86, 22), line(14, 38, 86, 38), line(38, 6, 38, 54), line(62, 6, 62, 54)]
TORE = [{"x": 86, "y": 10, "side": "right"}, {"x": 86, "y": 18, "side": "right"}, {"x": 86, "y": 30, "side": "right"}, {"x": 86, "y": 46, "side": "right"}, {"x": 14, "y": 22, "side": "left"}]
BALLS = [B("b2", 10.6, 14.6), B("b3", 10.6, 30.6), B("b4", 10.6, 46.6)] + CB
def kette(i, b, pts): return [dr(i, b, list(p), after=n > 0 or None) for n, p in enumerate(pts)]
u = {"title": "Dribbeln in drei Bahnen", "code": "UE-123", "kind": "Übungsform",
 "focuses": ["Dribbling", "1 gegen 1", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 14, "field_size": "27 x 41 m",
 "description": "Das Feld ist in drei Bahnen mit unterschiedlichen Aufgaben geteilt. Unten dribbelt ein Spieler ohne Gegner um zwei Dummys und schließt gegen einen Torhüter ab. In der Mitte muss er einen Verteidiger ausspielen, oben sogar zwei, bevor er auf eines von zwei Minitoren schießt. Die Spieler wechseln die Bahnen, damit jeder jede Aufgabe bekommt.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 41 Metern, in drei Bahnen geteilt. Unten und in der Mitte ein großes Tor mit Torhüter, oben zwei Minitore. Links ein Minitor für Konter.",
  "Verteilen: In jeder Bahn startet links ein Spieler von Team Neon mit Ball. In der Mitte wartet ein Verteidiger von Team Rot, oben zwei. Unten stehen zwei Dummys.",
  "Ablauf: Unten dribbelt der Spieler um beide Dummys und schließt ab. In der Mitte spielt er eins gegen eins, oben eins gegen zwei. Jedes Tor gibt einen Punkt.",
  "Wechsel: Erobert ein Verteidiger den Ball, kontert er schnell auf das Minitor links. Nach einigen Durchgängen wechseln die Spieler die Bahn."],
 "organisation_show": ORG,
 "coaching_points": ["Mutig und positiv dribbeln", "Den Verteidiger erst in eine Richtung locken und dann in die andere gehen", "Sauber dribbeln, mit beiden Füßen und allen Teilen des Fußes", "Mit dem Kopf oben breit spielen und vor dem Tor schnell abschließen"],
 "materials": ["2 große Tore", "3 Minitore", "2 Dummys", "Hütchen für Feld und Bahnen", "Mehrere Bälle", "Leibchen in drei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Dribbeln in drei Bahnen. Unten ohne Gegner, in der Mitte gegen einen und oben gegen zwei Verteidiger.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": BALLS,
  "steps": [
   S("Unten ohne Gegner", "Spieler vier dribbelt mit Tempo über den ersten Dummy und unter dem zweiten durch und schießt flach ins Eck. Das gibt einen Punkt für Spieler vier.",
     *kette("n4", "b4", [(36, 41), (46, 41), (54, 51), (68, 50)]), ps("b4", [85.5, 49.5], after=True)),
   S("Mitte eins gegen eins", "Spieler drei dribbelt auf Spieler sieben zu und lockt ihn nach unten. Dann zieht er oben vorbei und schießt ins Tor. Das gibt einen Punkt für Spieler drei.",
     *kette("n3", "b3", [(28, 28), (42, 25), (50, 22), (64, 30)]), mv("r7", [46, 30], delay=0.3), ps("b3", [85.5, 33], after=True)),
   S("Oben eins gegen zwei", "Spieler zwei spielt Spieler fünf und dann Spieler sechs aus und trifft ins obere Minitor. Das gibt einen Punkt für Spieler zwei.",
     *kette("n2", "b2", [(30, 10), (50, 20), (66, 9)]), mv("r5", [44, 13], delay=0.3), mv("r6", [62, 18], delay=0.8), ps("b2", [85.5, 10], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 93, "y1": 6, "x2": 93, "y2": 54, "text": "41 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erobert ein Verteidiger den Ball, wird sofort gekontert.", "Ballgewinn und Konter",
    "Gewinnt ein Verteidiger den Ball, schaltet er sofort um und kontert auf das Minitor links. So lernen die Verteidiger, schnell zu entscheiden, und die Angreifer müssen nach einem Ballverlust sofort nachsetzen.",
    sp(dict(POS, n3=(44, 30), r7=(53, 30))), [B("g", 45.6, 30.6), B("b2", 10.6, 14.6), B("b4", 10.6, 46.6)] + CB,
    [S("Ball erobert", "Spieler drei dribbelt auf Spieler sieben zu. Spieler sieben stellt sich gut und spitzelt ihm den Ball weg.",
       mv("r7", [49, 31]), ps("g", [47.4, 32], delay=0.3)),
     S("Konter aufs Minitor", "Spieler sieben dribbelt sofort los und schießt ins Minitor links. Das gibt einen Punkt für Team Rot.",
       dr("r7", "g", [30, 25]), ps("g", [14.5, 22], after=True), mv("n3", [36, 27], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Alle drei Bahnen werden zu einem Spiel drei gegen drei.", "Drei gegen drei",
    "Jetzt wird über das ganze Feld drei gegen drei gespielt, die Bahnen gelten nicht mehr. Team Neon darf auf alle Tore rechts abschließen, Team Rot kontert auf das Minitor links. Wer sieht, wo der Platz ist, und schnell dorthin dribbelt oder passt, hat Erfolg.",
    sp({"n2": (30, 14), "n3": (30, 30), "n4": (30, 46), "r5": (52, 12), "r6": (52, 46), "r7": (48, 30)}, dummys=False), [B("b3", 31.6, 30.6)] + CB,
    [S("Gegner anlocken", "Spieler drei dribbelt auf Spieler sieben zu. Gleichzeitig startet Spieler vier unten in die Tiefe.",
       dr("n3", "b3", [40, 30]), mv("r7", [46, 30], delay=0.2), mv("n4", [40, 52]), mv("n4", [62, 52], after=True)),
     S("Pass und Abschluss", "Spieler drei spielt Spieler vier in den Lauf, und Spieler vier schießt ins untere Tor. Das gibt einen Punkt für Team Neon.",
       ps("b3", [63.6, 52.6]), ps("b3", [85.5, 49.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
