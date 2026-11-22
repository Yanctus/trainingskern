import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P14 (U12-U14, Einzeltraining): Overlaps Underlaps - Full Backs (PDF: Develop Underlaps and Overlaps - Fullbacks).
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m). Ausrichtung wie im PDF (Minitore links, Trainer rechts an der Seite,
# Spieler startet unten), nicht gedreht. Das untere Minitor steht im Original schräg; hier gerade mit Öffnung nach rechts.
# Pinker Spieler P -> Spieler zwei (Team Neon, rechter Außenverteidiger). Zwei Dummys als Stangen (Verteidiger außen,
# Verteidiger im Strafraum). Gelbes Hütchen -> neon. Ballhaufen beim Spieler nur als zwei Ersatzbälle neben dem Trainer
# (Regel: zwei Ersatzbälle beim Trainer). Trainer etwas ins Feld gerückt (Seitenlinie).
# Ablauf nach PDF und Video (0:08-0:30): Pass zum Trainer, an die Schulter des äußeren Dummys, Bogenlauf innen hinter den
# Dummy (Underlap), Pass in den Lauf, direkte Flanke ins obere Minitor oder Rückpass ins untere. Reine Technikübung: Ziel.
# Sichtkegel: Ton „The curve is key. It allows them to open their body, scan the area“, im Video (ab 0:52) „Arrive facing the
# cross“ mit eingezeichnetem Kegel nach innen Richtung Minitore -> bl() in der Steigerung vor der Flanke Richtung Minitore.
# Fassungen: Coaching-Punkt „Im Bogen laufen“ (PDF „Arc the run“, Entscheidung Rückpass), Steigerung „Außen hinterlaufen“
# (PDF Seite 2, Video 0:32-0:58: Trainer nimmt den Ball vor dem Dummy nach innen mit, Overlap außen, Rückpass in den Lauf).
T = P("T", "c", 72, 39, "T")
POS = {"n2": (61.5, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 72.5, 45.5), B("s2", 70, 47.5)]
BALL_T = [72.6, 39.6]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 28, "y": 14, "side": "left"}, {"x": 31, "y": 31, "side": "left"}]
CONES = [C(41, 23, shape="stange"), C(65, 38.5, shape="stange"), C(65.5, 53, "neon")]
OBEN = [28.5, 14]
UNTEN = [31.5, 31]
START = [61.5, 51]
SCHULTER = [61, 43]
def unterlauf(**k): return [mv("n2", [59.5, 33], **k), mv("n2", [64, 24], after=True)]

u = {"title": "Innen und außen hinterlaufen", "code": "UE-285", "kind": "Übungsform",
 "focuses": ["Passspiel", "Bewegung", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Außenverteidiger übt Läufe mit dem Trainer und die Flanke danach. Er passt zum Trainer und läuft im Bogen innen hinter den Dummy. Der Trainer spielt in den Lauf, und der Spieler flankt direkt ins obere Minitor oder spielt den Rückpass ins untere. In der Steigerung läuft er außen herum.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Links zwei Minitore und ein Dummy als Verteidiger im Strafraum, rechts ein Dummy als Gegenspieler außen und unten ein Hütchen.",
  "Verteilen: Spieler zwei startet unten am Hütchen mit Ball. Der Trainer steht rechts an der Seite mit vielen Bällen.",
  "Ablauf: Pass zum Trainer, an die Schulter des Dummys, dann im Bogen innen hinter den Dummy laufen und den Pass direkt ins Minitor flanken.",
  "Wechsel: Nach jeder Flanke zurück zum Hütchen und mit dem nächsten Ball weiter, bis alle Bälle gespielt sind oder die Anzahl erreicht ist."],
 "organisation_show": ORG,
 "coaching_points": ["Im richtigen Moment loslaufen und den Raum nutzen", "Mit Tempo in den Ball laufen und direkt flanken", "Im Bogen laufen, damit der Ball immer zu sehen ist", "Zwischen Flanke und Rückpass klug entscheiden"],
 "materials": ["2 Minitore", "2 Dummys", "1 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Innen und außen hinterlaufen. Spieler zwei spielt mit dem Trainer, läuft hinter den Dummy und flankt direkt ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 62.1, 51.6)] + ERSATZ,
  "steps": [
   S("Pass zum Trainer", "Spieler zwei passt zum Trainer. Dann läuft er an die Schulter des Dummys.",
     ps("b1", BALL_T), mv("n2", SCHULTER, after=True)),
   S("Innen hinterlaufen", "Spieler zwei startet im Bogen innen hinter den Dummy. Der Trainer spielt den Ball in den Lauf.",
     *unterlauf(), ps("b1", [64.6, 24.6], delay=1)),
   S("Direkt flanken: Ziel", "Spieler zwei flankt direkt ins obere Minitor. Das ist das Ziel. Dann geht er zurück zum Hütchen, holt den nächsten Ball, und die nächste Runde beginnt.",
     ps("b1", OBEN, bend=6), mv("n2", [57, 38], after=True), mv("n2", START, after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im Bogen laufen.", "Im Bogen laufen",
    "Der Spieler läuft nicht gerade, sondern im Bogen hinter den Dummy. So sieht er den Ball die ganze Zeit und kommt mit Tempo an. Ist oben kein Platz, spielt er den Rückpass ins untere Minitor.",
    sp(n2=tuple(SCHULTER)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Im Bogen", "Spieler zwei läuft im Bogen innen hinter den Dummy und sieht dabei immer den Ball. Der Trainer passt in den Lauf.",
       *unterlauf(), ps("b1", [64.6, 24.6], delay=1)),
     S("Rückpass: Ziel", "Spieler zwei spielt den Ball direkt zurück ins untere Minitor. Das ist das Ziel. Dann geht er zurück zum Hütchen.",
       ps("b1", UNTEN), mv("n2", [57, 38], after=True), mv("n2", START, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Spieler zwei läuft außen herum.", "Außen hinterlaufen",
    "Jetzt nimmt der Trainer den Ball vor dem Dummy nach innen mit. Der Spieler läuft im Bogen außen herum. Er öffnet den Körper, schaut nach innen und flankt den Rückpass des Trainers direkt.",
    sp(), [B("b1", 62.1, 51.6)] + ERSATZ,
    [S("Pass zum Trainer", "Spieler zwei passt zum Trainer.",
       ps("b1", BALL_T)),
     S("Außen herum", "Der Trainer nimmt den Ball vor dem Dummy nach innen mit. Gleichzeitig läuft Spieler zwei im Bogen außen herum.",
       dr("T", "b1", [64, 45]), dr("T", "b1", [56, 40], after=True),
       mv("n2", [71, 44]), mv("n2", [71.5, 32], after=True), mv("n2", [68, 20], after=True)),
     S("Schauen und Pass", "Spieler zwei öffnet den Körper und schaut nach innen zu den Minitoren. Der Trainer spielt den Ball in den Lauf.",
       bl("n2", [48, 19]), ps("b1", [68.6, 20.6], after=True)),
     S("Direkt flanken: Ziel", "Spieler zwei flankt direkt ins obere Minitor. Das ist das Ziel. Dann geht der Trainer zurück an die Seite, und Spieler zwei holt am Hütchen den nächsten Ball.",
       ps("b1", OBEN))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
