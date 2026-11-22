import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P10 (U12-U14, Einzeltraining): Dribbling Circuit (PDF: Master the Dribble & Ball Manipulation). Dreieck mit 15 Yards
# Seitenlänge = Feld x 29-71, y 8-50 (ca. 14 m), Seiten als durchgezogene Linien. Ausrichtung wie im PDF (Spitze oben, Start
# unten links, Trainer rechts außen; Trainer etwas weiter nach außen gerückt, damit der Weg an der rechten Seite frei bleibt).
# Pinker Spieler P -> Spieler sieben (Team Neon). Vier rote Stangen links, zwei Puppen rechts (als Stangen gezeichnet), unten zwei
# Stangen auf der Linie und eine Stange in der Mitte, Hütchen an den drei Ecken. Laufweg nach PDF und Video (0:15-0:25):
# Slalom links hoch, um das obere Hütchen, an der ersten Puppe innen, an der zweiten außen vorbei, um das Hütchen unten rechts,
# unten zwischen den Stangen hinein, im Bogen um die Mittelstange und zurück zum Start. Reine Technikübung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; im Video nur Kreise um den Spieler).
# Fassungen: Coaching-Punkt Innenseite an der Puppe (PDF Seite 2 KCP 1, Video ab 0:36), zweiter Coaching-Punkt eng führen,
# auch wenn müde (PDF Seite 2 KCP 2, Video ab 0:45 "keep the ball under control / loose touch").
T = P("T", "c", 80, 44, "T")
POS = {"n7": (31, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.5, 47.5), B("s2", 83.5, 50)]
LINES = [line(29, 50, 50, 8, False), line(50, 8, 71, 50, False), line(29, 50, 71, 50, False)]
STANGEN = [(34.9, 38.6), (37.4, 33.4), (39.7, 28.4), (41.9, 23.9), (44, 50), (55, 50), (50, 43)]
PUPPEN = [(58, 23.6), (63.2, 33.9)]
CONES = [C(29, 50), C(50, 8), C(71, 50)] + [C(x, y, shape="stange") for x, y in STANGEN + PUPPEN]
SLALOM = [[37.6, 39.9], [34.7, 32.1], [42.4, 29.7], [39.2, 22.6]]
OBEN = [[44, 14], [47, 7.5], [50, 4.5], [53.5, 8.5], [56.5, 18]]
PUPPENWEG = [[55, 25], [60, 29.5], [66, 32], [68, 38]]
ECKE = [[69, 46], [74.5, 48.5], [73.5, 53], [71, 54]]
UNTEN = [[58, 53], [53, 52], [52.5, 46], [52.5, 41.5], [50, 39.5], [47.5, 41.5], [47, 48], [45.5, 53], [33, 52], [31, 47]]
def weg(pkte):
    return [dr("n7", "b1", p, after=(i > 0) or None) for i, p in enumerate(pkte)]

u = {"title": "Slalom, Puppen und Wendestange", "code": "UE-275", "kind": "Übungsform",
 "focuses": ["Dribbling", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "Dreieck, 14 m Seitenlänge",
 "description": "Ein Dribbel-Parcours im Dreieck mit drei Stationen. Links dribbelt der Spieler im Slalom durch Stangen, rechts legt er sich den Ball schnell an zwei Puppen vorbei. Unten dribbelt er im Bogen um eine Stange in der Mitte zurück zum Start. Erst kommt die Technik, dann das Tempo.",
 "organisation": ["Aufbauen: Ein Dreieck mit vierzehn Metern Seitenlänge und Hütchen an den Ecken. Links vier Stangen, rechts zwei Puppen, unten zwei Stangen auf der Linie und eine Stange in der Mitte.",
  "Verteilen: Spieler sieben startet mit Ball am Hütchen unten links. Der Trainer steht rechts außen mit Ersatzbällen.",
  "Ablauf: Slalom durch die Stangen, um das obere Hütchen, schnell an den Puppen vorbei, um das Hütchen unten rechts und im Bogen um die Mittelstange zurück zum Start.",
  "Wechsel: Nach jeder Runde eine kurze Pause, dann die nächste Runde. Sind zwei Spieler da, startet der zweite, sobald der erste zurück ist."],
 "organisation_show": ORG,
 "coaching_points": ["Mit beiden Füßen durch die Stationen dribbeln", "Den Ball an den Puppen schnell zur Seite legen", "Den Ball immer eng am Fuß führen", "Erst sauber, dann schneller, und Innenseite, Außenseite und Spann abwechseln"],
 "materials": ["3 Hütchen", "7 Stangen", "2 Puppen", "Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Slalom, Puppen und Wendestange. Spieler sieben dribbelt einen Parcours im Dreieck mit drei Stationen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(),
  "balls": [B("b1", 31.6, 47.6)] + ERSATZ,
  "steps": [
   S("Slalom durch die Stangen", "Spieler sieben startet unten links. Er dribbelt im Slalom durch die vier Stangen nach oben und nimmt dabei beide Füße.",
     *weg(SLALOM)),
   S("Um das Hütchen oben", "Oben dribbelt er eng um das Hütchen herum und nimmt die rechte Seite des Dreiecks.",
     *weg(OBEN)),
   S("Schnell an den Puppen vorbei", "Vor jeder Puppe legt er sich den Ball schnell zur Seite und dribbelt vorbei. An der ersten Puppe innen, an der zweiten außen.",
     *weg(PUPPENWEG)),
   S("Um das Hütchen unten", "Dann dribbelt er zum Hütchen unten rechts und eng darum herum.",
     *weg(ECKE)),
   S("Bogen zum Start: Ziel", "Unten dribbelt er zwischen den zwei Stangen hinein, im Bogen um die Stange in der Mitte und zurück zum Start. Das Ziel: die ganze Runde mit dem Ball eng am Fuß. Nach einer kurzen Pause startet Spieler sieben die nächste Runde.",
     *weg(UNTEN))],
  "dims": [{"x1": 29, "y1": 58.6, "x2": 71, "y2": 58.6, "text": "14 m"}, {"x1": 94, "y1": 8, "x2": 94, "y2": 50, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball schnell an der Puppe vorbeilegen.", "Mit der Innenseite verlagern",
    "Kurz vor der Puppe legt der Spieler den Ball mit der Innenseite schnell zur Seite. So bleibt der Ball unter Kontrolle, auch bei der schnellen Richtungsänderung. Danach geht es sofort wieder nach vorn.",
    sp(n7=(56.5, 18)), [B("b1", 57.1, 18.6)] + ERSATZ,
    [S("Innenseite, zur Seite", "Spieler sieben kommt auf die erste Puppe zu. Kurz davor legt er den Ball mit der Innenseite schnell zur Seite und dribbelt innen vorbei.",
       *weg(PUPPENWEG[:2])),
     S("Zweite Puppe außen", "An der zweiten Puppe legt er den Ball genauso schnell nach außen und dribbelt weiter zum Hütchen unten.",
       *weg(PUPPENWEG[2:]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Ball eng führen, auch wenn die Beine müde werden.", "Eng führen, auch wenn müde",
    "Nach ein paar Runden werden die Beine schwer. Gerade dann bleibt der Spieler konzentriert und führt den Ball mit kurzen Kontakten. Springt der Ball weg, geht der Rhythmus verloren.",
    sp(n7=(71, 54)), [B("b1", 71.6, 54.6)] + ERSATZ,
    [S("Kurze Kontakte", "Spieler sieben ist schon müde. Trotzdem dribbelt er mit kurzen Kontakten zwischen die zwei Stangen.",
       *weg(UNTEN[:3])),
     S("Konzentriert bis zum Start", "Eng um die Mittelstange und zurück zum Start. Der Ball springt nicht weg, und das ist das Ziel.",
       *weg(UNTEN[3:]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
