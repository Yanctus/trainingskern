import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-45 (U15-U17, Woche 18 Phase 6): Fun Heading Competition Warm Up. 10 x 10 Yards = 9 x 9 m, Feld x 25-75, y 5-55.
# Ausrichtung wie im PDF: Tor aus zwei Puppen in der Mitte (Puppen als Stangen), Team Rot (PDF blau) oben, Team Neon (PDF pink)
# unten, je ein Werfer an der Seite (Rot links, Neon rechts). Nummern vergeben (im PDF ohne Nummern): Neon 7 (erster Kopfball),
# 8 (Werfer), 9, 10; Rot 2 (geht als Erster ins Tor), 3 (Werfer), 4, 5. Gezeigt je Team vier Spieler, die übrigen nur im Text
# (3D-Abstand). Der Wurf ist als Pass dargestellt. Ein Trainer statt zwei Ballstationen, er steht links oben neben dem Feld.
# Fassungen: Coaching-Punkt aus dem PDF ("Head the ball down - more difficult to make save") und die Steigerung aus dem PDF
# (wer trifft, bleibt dran). Der PDF-Coaching-Punkt "Werfer wechseln durch" steht in der Organisation.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Keine Dublette zu UE-244 (WU-12): dort ein echtes Tor mit Torwart und Lauf um eine Puppe, hier ein Puppentor in der Mitte,
# beide Teams köpfen von zwei Seiten, und wer geköpft hat, geht selbst ins Tor.
T = P("T", "c", 18, 10, "T")
ERSATZ = [B("s1", 20.6, 13.5), B("s2", 17, 14)]
POS = {"r2": (50, 15), "r4": (41, 8), "r5": (59, 8), "r3": (25.5, 27),
       "n7": (45, 45), "n9": (36, 48), "n10": (54, 48), "n8": (75, 31)}
GOAL = (50, 28.5)
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(25, 5, 50, 50)]
CONES = [C(39.5, 29.5, shape="stange"), C(60.5, 29.5, shape="stange"), C(50, 17), C(25, 31.5), C(75, 27.5)]
BAELLE = [B("b1", *f(75, 31)), B("b2", 78.5, 34.5), B("b3", *f(25.5, 27))] + ERSATZ

u = {"title": "Köpfen, dann selbst ins Tor", "code": "UE-349", "kind": "Spielform",
 "focuses": ["Erwärmung", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 8, "players_max": 14,
 "field_size": "9 x 9 m",
 "description": "Ein Kopfballwettkampf zum Aufwärmen. In der Mitte stehen zwei Puppen als Tor, die beiden Teams köpfen von beiden Seiten darauf. Ein Mitspieler wirft von der Seite, der Kopfball muss zwischen den Puppen und am Torwart vorbei. Wer geköpft hat, läuft sofort selbst ins Tor und hält gegen das andere Team.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern. In der Mitte zwei Puppen oder Stangen als Tor, links und rechts an der Seite je ein Hütchen für den Werfer, oben ein Starthütchen.",
  "Verteilen: Team Rot steht oben, Team Neon unten, je ein Werfer mit Bällen an der Seite. Ein Spieler von Team Rot steht am Hütchen und geht zuerst ins Tor. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Der Werfer wirft seinem Mitspieler den Ball hoch zu, der köpft zwischen den Puppen durch. Höher als die Puppen zählt nicht. Danach läuft der Kopfballspieler ins Tor, und das andere Team köpft.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team. Die Werfer wechseln durch, bis jeder zweimal geköpft hat. Nach zwei Runden gewinnt das Team mit mehr Punkten."],
 "organisation_show": ORG,
 "coaching_points": ["Zum Ball gehen, nicht warten", "Mit der Stirn über den Ball, nach unten köpfen", "Sauber statt fest", "Nach dem Kopfball sofort ins Tor"],
 "materials": ["2 Puppen oder Stangen", "3 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Köpfen, dann selbst ins Tor. Ein kleiner Kopfballwettkampf zum Aufwärmen, zwei Teams köpfen von beiden Seiten auf ein Tor aus zwei Puppen.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Einer geht ins Tor", "Spieler zwei von Team Rot läuft zwischen die beiden Puppen. Er ist jetzt der Torwart.",
     mv("r2", list(GOAL))),
   S("Anlauf und Wurf", "Spieler sieben läuft an. Von der Seite wirft ihm Spieler acht den Ball hoch zu.",
     mv("n7", [45, 38]), ps("b1", f(45, 38), delay=0.4)),
   S("Kopfball: Punkt", "Spieler sieben köpft am Torwart vorbei zwischen den Puppen durch, und das gibt einen Punkt für Team Neon. Sofort läuft er selbst ins Tor, und Spieler zwei geht zurück zu seinem Team. Jetzt köpft Team Rot von der anderen Seite.",
     ps("b1", [42, 17]), mv("r2", [68, 10], after=True), mv("n7", list(GOAL), delay=0.6))],
  "dims": dims(25, 75, 5, 55, "9 m", "9 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball nach unten köpfen.", "Kopfball nach unten",
    "Ein Kopfball nach unten springt vor dem Torwart auf und ist schwer zu halten. Dafür geht der Spieler mit der Stirn über den Ball und nickt ihn ab. Sauber köpfen, nicht mit aller Kraft. Zu hoch über die Puppen zählt nicht.",
    sp(r2=(68, 10), n7=GOAL), BAELLE,
    [S("Anlauf und Wurf", "Jetzt köpft Team Rot. Spieler fünf läuft an, und Spieler drei wirft von der Seite.",
       mv("r5", [54, 19]), ps("b3", f(54, 19), delay=0.4)),
     S("Über den Ball, nach unten: Punkt", "Spieler fünf geht mit der Stirn über den Ball und nickt ihn nach unten. Der Ball springt vor Spieler sieben auf und geht durch, und das gibt einen Punkt für Team Rot.",
       ps("b3", [56, 26]), ps("b3", [57.5, 40], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer trifft, köpft weiter.", "Wer trifft, köpft weiter",
    "Trifft ein Team, bleibt es dran, und der nächste Spieler köpft sofort. Erst wenn ein Kopfball danebengeht oder gehalten wird, wechseln die Rollen. Nach der Spielzeit gewinnt das Team mit den meisten Kopfballtreffern.",
    sp(r2=GOAL), BAELLE,
    [S("Getroffen: Punkt", "Spieler sieben läuft an, bekommt den Wurf und köpft am Torwart vorbei. Das gibt einen Punkt für Team Neon, und Team Neon bleibt dran.",
       mv("n7", [45, 38]), ps("b1", f(45, 38), delay=0.4), ps("b1", [42, 17], after=True), mv("n7", [30, 42], after=True)),
     S("Gehalten, Rollen wechseln", "Gleich kommt Spieler neun. Sein Kopfball geht genau auf den Torwart, und Spieler zwei fängt ihn. Jetzt wechseln die Rollen, und Team Rot köpft.",
       mv("n9", [47, 38]), ps("b2", f(47, 38), delay=0.4), ps("b2", f(*GOAL), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
