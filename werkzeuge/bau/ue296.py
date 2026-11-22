import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P13 (U12-U14, Einzeltraining): Wide Players Driving Down the Line (Ordner "WingerFullback Driving Down The Line 1 to 1-P13").
# 15 x 20 Yards = Feld x 31-69, y 5-55 (14 x 18 m). Ausrichtung wie im PDF (Minitore oben, Trainer unten, nicht gedreht).
# Spieler P -> Spieler sieben (Team Neon, Flügelspieler oder Außenverteidiger). Hütchen, Stangen und Minitore leicht
# symmetrisch gesetzt. Der Ballvorrat liegt im Original neben dem Spieler außerhalb des Feldes; hier hat der Spieler einen Ball
# am Fuß, die zwei Ersatzbälle liegen beim Trainer. Ablauf nach PDF und Video (0:06-0:22): Pass zum Trainer, nach innen
# antäuschen, an der Linie anbieten, Annahme mit dem hinteren Fuß, Dribbling die Linie hinunter bis zum Hütchen, Pass ins Minitor.
# Reine Technikübung ohne Wertung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; "open body shape to receive" ist Körperstellung, kein Blick).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (genau ins Minitor passen; Annahme mit dem hinteren Fuß, gezeigt von der
# rechten Seite, Video 0:30-0:40 "work from the other side").
T = P("T", "c", 52, 48, "T")
POS = {"n7": (33.5, 41.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 48.5, 50.5), B("s2", 46.5, 51.5)]
BALL_T = [52.6, 48.6]
LINES = [rect(31, 5, 38, 50)]
TORE = [{"x": 40, "y": 5, "side": "top"}, {"x": 60, "y": 5, "side": "top"}]
CONES = [C(37, 24), C(63, 24), C(31, 36.5), C(69, 36.5), C(55, 51.5),
         C(42, 34, shape="stange"), C(58, 34, shape="stange")]
ZIEL_L, ZIEL_R = [40, 5.5], [60, 5.5]

u = {"title": "Annehmen und die Linie runter", "code": "UE-296", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Dribbling", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "14 x 18 m",
 "description": "Ein Flügelspieler oder Außenverteidiger übt, an der Seitenlinie anzunehmen und mit Tempo nach vorn zu gehen. Er passt zum Trainer, täuscht nach innen an und bietet sich an der Linie an. Den Rückpass nimmt er mit dem hinteren Fuß an und dribbelt die Linie hinunter. Am Hütchen spielt er den Ball genau ins Minitor.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. Oben zwei Minitore, davor auf jeder Seite ein Hütchen. In der Mitte zwei Stangen, an den Seitenlinien je ein Hütchen als Start.",
  "Verteilen: Spieler sieben startet links an der Seitenlinie mit Ball. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Pass zum Trainer, nach innen antäuschen und an der Linie anbieten. Mit dem hinteren Fuß annehmen, bis zum Hütchen dribbeln und ins Minitor passen.",
  "Wechsel: Nach jedem Pass ins Minitor geht es zurück an den Start. Sind alle Bälle gespielt, werden sie eingesammelt, und es geht auf der rechten Seite mit dem anderen Fuß weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem hinteren Fuß annehmen, um schnell nach vorn zu kommen", "Erst nach innen antäuschen, dann an der Linie anbieten", "Genau ins Minitor passen, auch wenn die Beine müde werden", "Auf der anderen Seite den anderen Fuß benutzen und das Tempo hoch halten"],
 "materials": ["2 Minitore", "5 Hütchen", "2 Stangen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Annehmen und die Linie runter. Spieler sieben nimmt an der Seitenlinie an, dribbelt mit Tempo nach vorn und passt ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 34.1, 42.1)] + ERSATZ,
  "steps": [
   S("Pass zum Trainer", "Spieler sieben steht an der Seitenlinie und passt in die Mitte zum Trainer.",
     ps("b1", BALL_T)),
   S("Antäuschen, anbieten", "Dann täuscht er kurz nach innen an und bietet sich an der Linie an. Sein Körper ist offen zum Trainer.",
     mv("n7", [35.5, 35.5]), mv("n7", [33, 30], after=True)),
   S("Annahme mit dem hinteren Fuß", "Der Trainer passt zurück. Spieler sieben nimmt den Ball mit dem hinteren Fuß an und dribbelt mit Tempo die Linie hinunter.",
     ps("b1", [33.6, 30.6]), dr("n7", "b1", [33.5, 21], after=True)),
   S("Ins Minitor: Ziel", "Am Hütchen passt er den Ball flach ins linke Minitor. Das ist das Ziel. Dann läuft er zurück an den Start und holt den nächsten Ball. Sind alle Bälle gespielt, kommt die rechte Seite dran.",
     ps("b1", ZIEL_L), mv("n7", [33.5, 41.5], after=True))],
  "dims": dims(31, 69, 5, 55, "14 m", "18 m", rx=76)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau ins Minitor passen.", "Genau ins Minitor",
    "Der Pass ins Minitor soll bei jeder Wiederholung genau sein. Flach und mit der Innenseite spielen. Auch wenn die Beine müde werden, bleibt die Technik sauber.",
    sp(n7=(33, 30)), [B("b1", 33.6, 30.6)] + ERSATZ,
    [S("Bis zum Hütchen", "Spieler sieben hat den Ball angenommen und dribbelt mit Tempo bis zum Hütchen.",
       dr("n7", "b1", [33.5, 21])),
     S("Flach und genau: Ziel", "Er spielt den Ball flach mit der Innenseite genau ins linke Minitor. Das ist das Ziel. Auch beim zehnten Ball bleibt der Pass genau.",
       ps("b1", ZIEL_L))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Annahme mit dem hinteren Fuß, jetzt auf der rechten Seite.", "Mit dem hinteren Fuß",
    "Jetzt startet der Spieler rechts. Er nimmt den Ball mit dem hinteren Fuß an, hier mit dem rechten. So zeigt der erste Kontakt schon nach vorn, und er kommt schnell ins Dribbling. Den Pass ins Minitor spielt er mit dem anderen Fuß als auf der linken Seite.",
    sp(n7=(66.5, 41.5)), [B("b1", 67.1, 42.1)] + ERSATZ,
    [S("Pass und anbieten", "Spieler sieben passt zum Trainer, täuscht nach innen an und bietet sich rechts an der Linie an.",
       ps("b1", BALL_T), mv("n7", [64.5, 35.5], after=True), mv("n7", [67, 30], after=True)),
     S("Hinterer Fuß, nach vorn", "Der Trainer passt zurück. Spieler sieben nimmt den Ball mit dem hinteren Fuß an und nimmt ihn gleich nach vorn mit.",
       ps("b1", [67.6, 30.6]), dr("n7", "b1", [66.5, 21], after=True)),
     S("Ins Minitor: Ziel", "Am Hütchen passt er ins rechte Minitor. Das ist das Ziel. Danach geht es zurück an den Start.",
       ps("b1", ZIEL_R), mv("n7", [66.5, 41.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
