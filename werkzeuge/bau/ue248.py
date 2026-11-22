import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P7 (U12-U14, Woche 42 Phase 6): Centre Backs Defending Crosses (Defend the Goal). 35 x 45 Yards, gedreht: im PDF liegt das
# Tor rechts, hier oben. Feld x 18-82, y 5-55 (41 x 32 m), Strafraum und Torraum nach der PDF-Skizze, Halbkreis weggelassen.
# Jugendtor mit Torwart oben, zwei Puppen als Stangen vor dem Strafraum, zwei Minitore unten (schräg im PDF, hier gerade mit
# Öffnung nach oben). Blau -> Team Neon: Torwart n1 (grün im PDF), Innenverteidiger 5 und 6, Wartende 2 und 3 oben neben dem Tor
# (im PDF an der Seitenlinie neben dem Tor). Flankengeber 8 und 4 -> Team Rot (8 links, 4 rechts), Nummern wie im PDF.
# Ein Trainer statt zwei: der Trainer unten wirft den Ball zum Kopfball (der zweite Trainer oben im PDF ist weggelassen).
# Wertung ergänzt (im Original keine): Kopfball ins Minitor gibt einen Punkt für Team Neon.
# Kein Dubletten-Fall: UE-225 (Leiter, Doppelpass, flache Flanke aufs Minitor) und UE-185 (Puppe, Köpfen, zwei Minitore blocken)
# haben eine andere Organisation und andere Abläufe.
# Sichtkegel aus dem PDF ("Quick scans to see attackers positions", Coaching-Punkt 2 "quickly assessing the situation"): im
# zweiten Coaching-Punkt schaut Spieler fünf vor der Flanke nach vorn ins Feld, ob ein Gegner kommt. Im Video ist nur eine dunkle
# Markierung um die Innenverteidiger, kein Kegel; Richtung aus dem Sinn.
T = P("T", "c", 50, 49, "T")
POS = {"n1": (50, 8), "n5": (41.5, 15), "n6": (58.5, 15), "r8": (21, 12), "r4": (79, 16), "n2": (30, 2.5), "n3": (70, 2.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 52.5), B("s2", 46.4, 52.5)]
def baelle(b8=(21.6, 12.6), b4=(79.6, 16.6)):
    return [B("b8", *b8), B("b4", *b4), B("b1", 50.6, 49.6)] + ERSATZ
LINES = [rect(18, 5, 64, 50), rect(24.8, 5, 50.4, 17.8), rect(37.3, 5, 25.4, 6.6)]
CONES = [C(41.4, 27.8, shape="stange"), C(57.5, 27.8, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 31, "y": 44, "side": "bottom"}, {"x": 67, "y": 44, "side": "bottom"}]

u = {"title": "Zu zweit Flanken klären", "code": "UE-248", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 9, "field_size": "41 x 32 m",
 "description": "Zwei Verteidiger stehen vor dem Tor und wehren Flanken von beiden Seiten ab. Nach der ersten Flanke sprinten sie raus zu den Puppen und gleich wieder zurück in den Strafraum, denn die zweite Flanke kommt von der anderen Seite. Danach sprinten beide zwischen den Puppen nach vorn, und der Trainer wirft einem den Ball zum Kopfball. Trifft der Kopfball ins Minitor, gibt das einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 32 Metern mit Strafraum und einem Jugendtor oben. Vor dem Strafraum stehen zwei Puppen oder Stangen, unten zwei Minitore.",
  "Verteilen: Ein Torwart und zwei Verteidiger von Team Neon stehen am Tor, zwei weitere warten oben neben dem Tor. Zwei Flankengeber von Team Rot stehen links und rechts mit Bällen. Der Trainer steht unten mit Bällen.",
  "Ablauf: Die erste Flanke kommt von links, die Verteidiger klären sie nach außen. Dann sprinten sie zu den Puppen und zurück, und die zweite Flanke kommt von rechts. Zum Schluss sprinten beide nach vorn, und der Trainer wirft den Ball zum Kopfball.",
  "Wertung und Wechsel: Trifft der Kopfball ins Minitor, gibt das einen Punkt für Team Neon. Danach sind die zwei Wartenden dran. Nach ein paar Runden tauschen Verteidiger und Flankengeber."],
 "organisation_show": ORG,
 "coaching_points": ["Die Flanke angreifen und laut rufen, wer zum Ball geht", "Den Ball weit nach außen klären, nie in die Mitte", "Schnell raus zu den Puppen und schnell zurück in den Strafraum", "Hat man Zeit, den Ball ruhig mit Kopf oder Brust zum Torwart spielen"],
 "materials": ["1 Jugendtor", "2 Minitore", "2 Puppen oder Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zu zweit Flanken klären. Zwei Verteidiger wehren Flanken von beiden Seiten ab und müssen dazwischen schnell sprinten.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": baelle(),
  "steps": [
   S("Erste Flanke", "Spieler acht flankt von links in den Strafraum. Spieler sechs greift den Ball an, ruft laut „Meiner!“ und köpft ihn weit nach außen. Spieler fünf sichert ab.",
     ps("b8", [57.6, 13.6], bend=8), mv("n6", [57, 13]), mv("n5", [44, 17]), ps("b8", [88, 32], after=True)),
   S("Raus zu den Puppen", "Jetzt sprinten beide gleichzeitig raus zu den Puppen und tippen sie an. Sofort laufen sie zurück in den Strafraum.",
     mv("n5", [41.5, 24.5]), mv("n6", [57.5, 24.5]), mv("n5", [45, 15], after=True), mv("n6", [56, 15], after=True)),
   S("Zweite Flanke", "Jetzt flankt Spieler vier von rechts. Spieler fünf greift den Ball an und köpft ihn weg vom Tor, weit nach außen.",
     ps("b4", [45.6, 15.6], bend=-8), ps("b4", [10, 28], after=True)),
   S("Nach vorn sprinten", "Beide sprinten zwischen den Puppen nach vorn, so als wollten sie die Stürmer ins Abseits stellen. Der Trainer wirft Spieler fünf den Ball zu.",
     mv("n5", [46, 35]), mv("n6", [55, 32]), ps("b1", [46.6, 35.6], after=True)),
   S("Kopfball ins Minitor: Punkt", "Spieler fünf köpft den Ball ins linke Minitor, und das gibt einen Punkt für Team Neon. Dann sind Spieler zwei und Spieler drei dran.",
     ps("b1", [31, 44.4]))],
  "dims": dims(18, 82, 5, 55, "41 m", "32 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Gut stehen und sicher klären.", "Gut stehen, sicher klären",
    "Die Verteidiger stehen offen und auf den Zehenspitzen. So sehen sie den Ball und sind schnell bei kurzen und langen Flanken. Wer zum Ball geht, ruft laut. Geklärt wird hoch und weit nach außen, nie in die Mitte vor das Tor.",
    sp(), baelle(),
    [S("Offen stehen", "Spieler acht flankt. Spieler fünf und Spieler sechs stehen offen und auf den Zehenspitzen. Spieler sechs ruft „Meiner!“ und geht dem Ball entgegen.",
       ps("b8", [57.6, 13.6], bend=8), mv("n6", [57, 13]), mv("n5", [44, 17])),
     S("Nach außen klären", "Spieler sechs köpft den Ball hoch und weit nach außen. In der Mitte vor dem Tor wäre er gefährlich.",
       ps("b8", [88, 32]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Umschauen und ruhig zum Torwart spielen.", "Ruhig zum Torwart",
    "Vor der Flanke schaut sich der Verteidiger schnell um. Kommt kein Gegner, hat er Zeit. Dann nimmt er den Ball mit der Brust oder dem Kopf und spielt ihn ruhig zurück zum Torwart. So bleibt der Ball beim eigenen Team.",
    sp(), baelle(),
    [S("Umschauen", "Spieler vier will flanken. Spieler fünf schaut sich vorher schnell um: Kommt ein Gegner? Nein, er hat Zeit.",
       bl("n5", [44, 33])),
     S("Brust zum Torwart", "Spieler vier flankt. Spieler fünf nimmt den Ball mit der Brust und spielt ihn ruhig zurück zum Torwart. Der Torwart fängt ihn.",
       ps("b4", [42.1, 15.6], bend=-8), ps("b4", [50.6, 8.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
