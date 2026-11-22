import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 48-P1: 25 x 20 Yards, gedreht: oben Tic-Tac-Toe (10 Yards), unten Spielfeld (15 Yards) mit Toren links/rechts und 3-Yard-Zonen davor.
T = P("T", "c", 6, 50, "T")
CB = [B("c1", 8.5, 50.6), B("c2", 5, 53.5)]
GX = (44, 50, 56); GY = (10.7, 16, 21.3)
GRID = [rect(41, 8, 18, 16), line(47, 8, 47, 24, dashed=False), line(53, 8, 53, 24, dashed=False), line(41, 13.3, 59, 13.3, dashed=False), line(41, 18.7, 59, 18.7, dashed=False)]
Z = [{"type": "zone", "x": 14, "y": 26, "w": 10, "h": 28}, {"type": "zone", "x": 76, "y": 26, "w": 10, "h": 28}]
LINES = [rect(14, 6, 72, 48), line(14, 26, 86, 26)] + GRID + Z
TORE = [{"x": 14, "y": 40, "side": "left"}, {"x": 86, "y": 40, "side": "right"}]
def kegel(k5=(34, 17), k6=(68, 17)):
    return [C(GX[0], GY[0], "neon", id="k1"), C(GX[1], GY[1], "neon", id="k2"), C(GX[2], GY[0], id="k3"), C(GX[2], GY[1], id="k4"),
            C(*k5, "neon", id="k5"), C(*k6, id="k6")]
POS = {"n2": (18, 12), "n3": (27, 12), "n4": (36, 12), "r7": (64, 12), "r8": (73, 12), "r9": (82, 12)}
def sp(d=None, **k):
    d = dict(d or POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
NACH2 = dict(POS, n4=(49, 24), r7=(63, 23), n2=(40, 34), n3=(40, 50), r8=(66, 40))
u = {"title": "Tic-Tac-Toe ins Spiel", "code": "UE-108", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Zusammenspiel", "Erwärmung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 12, "field_size": "18 x 23 m",
 "description": "Zwei Teams spielen zuerst Tic-Tac-Toe: Abwechselnd rennt ein Spieler los und legt ein Hütchen in das Raster. Wer zuerst drei in einer Reihe hat, gewinnt und darf im Spielfeld mit zwei gegen eins und Ball beginnen. Nach jedem Angriff kommt in jedem Team ein Spieler dazu, bis zum Schluss fünf gegen fünf gespielt wird.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern. Oben ein Raster mit drei mal drei Feldern, unten das Spielfeld mit einem Minitor links und rechts und je einer Zone davor.",
  "Verteilen: Zwei Teams mit je fünf Spielern, Team Neon links, Team Rot rechts. Jeder Spieler hat ein Hütchen in seiner Teamfarbe. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Abwechselnd sprintet je ein Spieler beider Teams los und legt sein Hütchen ins Raster. Das Team mit drei in einer Reihe beginnt unten mit zwei gegen eins und bekommt den Ball. Ein Tor zählt nur aus der Zone, und Verteidiger dürfen nicht in die Zone zurückweichen.",
  "Steigern: Nach jedem Angriff kommt in jedem Team ein Spieler dazu, also drei gegen zwei, vier gegen drei, fünf gegen vier und zum Schluss fünf gegen fünf."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell denken: Wo muss mein Hütchen hin, damit wir gewinnen", "Kräftig beschleunigen und vor dem Raster rechtzeitig abbremsen", "Die Überzahl nutzen, um die Abwehr auszuspielen", "Immer wissen, wie viele Spieler im Feld sind, und danach angreifen oder verteidigen"],
 "materials": ["Raster aus Hütchen oder Stangen", "Je 5 Hütchen in zwei Farben", "2 Minitore", "Hütchen für die Zonen", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Tic-Tac-Toe ins Spiel. Wer zuerst drei in einer Reihe hat, startet mit Überzahl und Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": kegel(), "players": sp(), "balls": CB,
  "steps": [
   S("Wettlauf ums Raster", "Gleichzeitig sprinten Spieler vier und Spieler sieben los. Beide brauchen das Feld unten rechts. Spieler vier ist schneller, legt sein Hütchen hin und hat drei in einer Reihe.",
     mv("n4", [49, 24]), mv("r7", [63, 23], delay=0.3), ps("k5", [GX[2], GY[2]], delay=0.6)),
   S("Zwei gegen eins mit Ball", "Team Neon hat gewonnen. Gleichzeitig laufen Spieler zwei und Spieler drei ins Spielfeld, Spieler acht verteidigt allein. Der Trainer spielt Spieler zwei den Ball zu.",
     mv("n2", [40, 34]), mv("n3", [40, 50]), mv("r8", [66, 40]), ps("c1", [41.6, 34.6], delay=0.6)),
   S("Überzahl ausspielen", "Spieler zwei dribbelt an, Spieler acht kommt heraus. Spieler zwei spielt zu Spieler drei, der in die Zone dribbelt und ins Minitor schießt. Das gibt einen Punkt für Team Neon.",
     dr("n2", "c1", [50, 34]), mv("n3", [54, 48]), mv("r8", [60, 36], delay=0.2), ps("c1", [55.6, 48.6], after=True),
     dr("n3", "c1", [79, 46], after=True), ps("c1", [85.5, 41], after=True)),
   S("Ein Spieler mehr", "Jetzt kommt in jedem Team ein Spieler dazu: Gleichzeitig laufen Spieler vier und Spieler sieben ins Spielfeld. Der Trainer spielt den nächsten Ball zu Spieler vier, und es geht drei gegen zwei weiter.",
     mv("n4", [40, 44]), mv("r7", [70, 28]), ps("c2", [41.6, 44.6], delay=0.6))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "18 m"}, {"x1": 94, "y1": 6, "x2": 94, "y2": 54, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Überzahl richtig nutzen.", "Überzahl nutzen",
    "Bei zwei gegen eins dribbelt der Ballführende auf den Verteidiger zu, bis dieser herauskommt. Erst dann kommt der Pass zum freien Mitspieler. Der Mitspieler hält Abstand und Breite, damit der Verteidiger nicht beide decken kann. Weil nur aus der Zone getroffen werden darf, muss der Angriff schnell und genau sein.",
    sp(NACH2), [B("g", 41.6, 34.6)] + CB,
    [S("Verteidiger anlocken", "Spieler zwei dribbelt direkt auf Spieler acht zu. Gleichzeitig bleibt Spieler drei breit und läuft mit nach vorn.",
       dr("n2", "g", [50, 34]), mv("n3", [54, 48]), mv("r8", [60, 36], delay=0.3)),
     S("Pass in die Lücke", "Spieler acht kommt heraus, und Spieler zwei spielt sofort zu Spieler drei. Der dribbelt in die Zone und schießt ins Minitor. Das gibt einen Punkt für Team Neon.",
       ps("g", [55.6, 48.6]), dr("n3", "g", [79, 46], after=True), ps("g", [85.5, 41], after=True))],
    cones=kegel(k5=(GX[2], GY[2]))),
  V("Steigerung", "Und jetzt die Steigerung: Zum Schluss spielen beide Teams fünf gegen fünf.", "Fünf gegen fünf zum Schluss",
    "Nach jedem Angriff kam ein Spieler pro Team dazu, jetzt sind alle im Spielfeld. Gespielt wird fünf gegen fünf, und weiterhin zählt ein Tor nur aus der Zone. Jetzt geht es um Zusammenspiel im ganzen Team, gute Entscheidungen und schnelles Umschalten zwischen Angriff und Abwehr.",
    sp({"n2": (24, 32), "r8": (33, 32), "n4": (42, 32), "r10": (51, 32), "n6": (60, 32), "n3": (28, 48), "r7": (37, 48), "n5": (46, 48), "r9": (55, 48), "r11": (64, 48)}),
    [B("b1", 61.6, 32.6)] + CB,
    [S("Durchbruch auf rechts", "Spieler sechs dribbelt mit Tempo nach rechts in die Zone. Gleichzeitig läuft Spieler elf hinterher, darf aber nicht in die Zone.",
       dr("n6", "b1", [80, 34]), mv("r11", [70, 42], delay=0.2)),
     S("Abschluss aus der Zone", "Spieler sechs schießt aus der Zone ins Minitor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [85.5, 39]))],
    cones=kegel(k5=(GX[2], GY[2]), k6=(GX[0], GY[2])))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
