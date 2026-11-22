import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P26 (U12-U14, Einzeltraining): 1st Touch and Passing. 10 x 10 Yards = Feld x 25-75, y 5-55 (9 x 9 m).
# Ausrichtung wie im PDF (Trainer oben, die zwei Spieler unten links und rechts). Drei Stangen im Dreieck wie im PDF
# (rechts neben dem Trainer, rechts über dem linken Spieler, links über dem rechten Spieler); rechte Stange etwas höher gesetzt,
# damit der Pass in der Steigerung frei ist. Pinker Arbeitsspieler links -> Spieler sieben, pinker Helfer rechts -> Spieler acht
# (beide Team Neon). Ablauf nach PDF und Video (0:05-0:17): Trainer -> sieben -> acht, dann andersherum acht -> sieben -> Trainer.
# Reine Technikübung: Ziel statt Punkte. Rollentausch nach zwei Minuten.
# Sichtkegel: Text "scan and receive", "Constant scanning", Ton "constant scanning before every receive"; im Video (0:15-0:20)
# ist bei Spieler sieben ein Kegel nach hinten (vom Trainer weg) eingezeichnet -> bl() vor jeder Annahme Richtung unten links.
# Fassungen: Steigerung 1 erster Kontakt vor die Stange (PDF Seite 2, Video ab 0:28), Steigerung 2 Doppelpass um die Stange
# (PDF Seite 2, Video ab 0:39).
T = P("T", "c", 46, 13, "T")
POS = {"n7": (33, 41), "n8": (69, 41)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 42.5, 8.5), B("s2", 39.5, 8.5)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(55, 12, shape="stange"), C(41, 35, shape="stange"), C(62, 34, shape="stange")]
BT = [46.6, 13.6]
B7 = [33.6, 41.6]
B8 = [69.6, 41.6]
BLICK = [29, 57]

u = {"title": "Im Stangendreieck annehmen", "code": "UE-268", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 2, "players_max": 2,
 "field_size": "9 x 9 m",
 "description": "Ein Spieler übt die erste Ballberührung und den Pass im Dreieck aus drei Stangen. Er schaut vor jeder Annahme über die Schulter, nimmt den Pass vom Trainer mit dem hinteren Fuß an und spielt quer zu seinem Mitspieler. Dann läuft alles andersherum zurück zum Trainer. Nach zwei Minuten tauschen die beiden Spieler die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern. Drei Stangen im Dreieck: eine oben neben dem Trainer, zwei unten links und rechts.",
  "Verteilen: Spieler sieben übt und steht unten links an der Stange, Spieler acht hilft und steht unten rechts. Der Trainer steht oben mit vielen Bällen.",
  "Ablauf: Spieler sieben schaut über die Schulter, nimmt den Pass vom Trainer mit dem hinteren Fuß an und spielt quer zu Spieler acht. Dann andersherum: Spieler acht passt zurück, und Spieler sieben spielt zum Trainer.",
  "Wechsel: Nach zwei Minuten tauschen Spieler sieben und Spieler acht die Rollen. Jeder spielt zwei Durchgänge, dann kommt die Steigerung."],
 "organisation_show": ORG,
 "coaching_points": ["Vor jeder Annahme über die Schulter schauen", "Mit dem hinteren Fuß annehmen, um schnell weiterzuspielen", "Annahme und Pass abwechselnd mit beiden Füßen", "Auch müde genau und mit dem richtigen Tempo passen"],
 "materials": ["3 Stangen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Im Stangendreieck annehmen. Spieler sieben schaut über die Schulter, nimmt den Ball an und spielt ihn quer weiter.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", *BT)] + ERSATZ,
  "steps": [
   S("Schulterblick, Pass", "Spieler sieben steht unten links an der Stange und schaut kurz über die Schulter. Dann passt der Trainer zu ihm.",
     bl("n7", BLICK), ps("b1", B7, after=True)),
   S("Annehmen, quer passen", "Spieler sieben nimmt den Ball mit dem hinteren Fuß an und öffnet sich dabei. Mit dem anderen Fuß passt er quer zu Spieler acht.",
     ps("b1", B8)),
   S("Andersherum zurück", "Jetzt geht es andersherum. Spieler sieben schaut wieder über die Schulter. Spieler acht passt zurück, und Spieler sieben nimmt mit dem hinteren Fuß an.",
     bl("n7", BLICK), ps("b1", B7, after=True)),
   S("Zum Trainer: Ziel", "Spieler sieben passt zurück zum Trainer. Das Ziel: jeder Pass kommt genau und im richtigen Tempo an. Dann geht es von vorn los. Nach zwei Minuten tauschen Spieler sieben und Spieler acht die Rollen.",
     ps("b1", BT))],
  "dims": dims(25, 75, 5, 55, "9 m", "9 m", rx=83)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der erste Kontakt geht vor die Stange.", "Erster Kontakt vor die Stange",
    "Spieler sieben nimmt den Ball nicht im Stand an. Mit dem ersten Kontakt nimmt er ihn im Bogen nach vorn vor die Stange mit. Von dort passt er quer zu Spieler acht. So übt er die gerichtete Ballmitnahme.",
    sp(), [B("b1", *BT)] + ERSATZ,
    [S("Schulterblick, Pass", "Spieler sieben schaut über die Schulter. Der Trainer passt zu ihm.",
       bl("n7", BLICK), ps("b1", B7, after=True)),
     S("Vor die Stange", "Mit dem ersten Kontakt nimmt Spieler sieben den Ball im Bogen vor die Stange mit.",
       dr("n7", "b1", [33.5, 34]), dr("n7", "b1", [37.5, 30], after=True), dr("n7", "b1", [44, 30], after=True)),
     S("Quer zu Spieler acht", "Von dort passt Spieler sieben quer zu Spieler acht und läuft zurück an seine Stange. Dann geht es in die andere Richtung.",
       ps("b1", B8), mv("n7", [45, 39], after=True), mv("n7", [33, 41], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Doppelpass um die Stange.", "Doppelpass um die Stange",
    "Spieler sieben spielt den Pass vom Trainer direkt zurück. Dann läuft er an der Stange vorbei, und der Trainer passt ihm in den Lauf. Erst dann geht der Pass quer zu Spieler acht. Mehr Pässe machen die Übung schneller.",
    sp(), [B("b1", *BT)] + ERSATZ,
    [S("Direkt zurück", "Spieler sieben schaut über die Schulter. Der Trainer passt zu ihm, und Spieler sieben spielt direkt zurück.",
       bl("n7", BLICK), ps("b1", B7, after=True), ps("b1", BT, after=True)),
     S("Um die Stange", "Spieler sieben läuft unten an der Stange vorbei nach rechts. Der Trainer passt ihm in den Lauf.",
       mv("n7", [47, 40]), ps("b1", [47.6, 40.6], delay=0.6)),
     S("Quer zu Spieler acht", "Spieler sieben nimmt an und passt quer zu Spieler acht. Dann läuft er zurück an seine Stange, und es geht in die andere Richtung.",
       ps("b1", B8, after=True), mv("n7", [33, 41], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
