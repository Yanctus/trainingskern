import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P22 (U12-U14, Einzeltraining): Developing the Switch of Play - CM. 50 x 30 Yards = Feld x 15-85, y 12-55 (46 x 27 m).
# Ausrichtung wie im PDF (Trainer unten in der Mitte, Minitore links und rechts im oberen Drittel, leicht im Feld).
# Strafraum und großes Tor des Hintergrunds weggelassen (spielen keine Rolle). Blauer Spieler -> Spieler acht (Team Neon,
# zentraler Mittelfeldspieler). Dreieck aus Hütchen etwas größer und höher gesetzt (3D-Abstand Trainer/Spieler).
# Ballhaufen beim Trainer nur als zwei Ersatzbälle. Ablauf nach PDF und Video (0:10-0:26): Prallpass im Dreieck, Lauf um das
# rechte Hütchen und zweiter Prallpass, Absetzen nach außen, Annahme, Seitenwechsel ins linke Minitor; danach andere Seite.
# Reine Technikübung: Ziel statt Punkte.
# Sichtkegel: PDF "Open hips early to scan both the ball and target", Ton "opens their hips to see both the ball and the switch
# option"; im Video (0:31-0:37) ist ein Kegel eingezeichnet, der vor der Annahme zum Minitor auf der anderen Seite zeigt.
# -> bl() vor der Annahme Richtung linkes Minitor (Grundform und beide Steigerungen).
# Fassungen: Steigerung 1 Täuschung mit Drehung zur sicheren Seite (PDF Seite 2, Video ab 0:47), Steigerung 2 Prallbretter vor
# den Minitoren, Ball hoch darüber (Video ab 1:23). Prallbretter als Minihürden gezeichnet (eigene Form gibt es nicht).
T = P("T", "c", 50, 54, "T")
POS = {"n8": (50, 36)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 45.5, 55.5), B("s2", 43, 55.5)]
LINES = [rect(15, 12, 70, 43)]
TORE = [{"x": 20, "y": 27, "side": "left"}, {"x": 80, "y": 27, "side": "right"}]
ZIEL = [20.5, 27]
def cones(bretter=False):
    k = [C(50, 31, id="k1"), C(45, 40, id="k2"), C(55, 40, id="k3")]
    if bretter: k += [C(27, 28.5, shape="huerde", id="h1"), C(73, 28.5, shape="huerde", id="h2")]
    return k
BALL_T = [50.6, 54.6]

u = {"title": "Seitenwechsel ins Minitor", "code": "UE-274", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "46 x 27 m",
 "description": "Ein zentraler Mittelfeldspieler übt den Seitenwechsel. Nach zwei Prallpässen mit dem Trainer löst er sich nach außen, öffnet die Hüfte und nimmt den Ball an. Mit dem zweiten Kontakt spielt er den langen Ball ins Minitor auf der anderen Seite. Danach kommt die andere Seite dran.",
 "organisation": ["Aufbauen: Ein Feld von 46 mal 27 Metern. Unten in der Mitte ein Dreieck aus drei Hütchen, links und rechts im oberen Drittel je ein Minitor für die Flügelspieler.",
  "Verteilen: Spieler acht steht im Dreieck. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Prallpass mit dem Trainer, Lauf um das Hütchen und zweiter Prallpass. Dann nach außen absetzen, annehmen und mit dem zweiten Kontakt ins Minitor auf der anderen Seite wechseln.",
  "Wechsel: Nach jedem Seitenwechsel kommt die andere Seite dran. Gearbeitet wird auf Zeit oder bis alle Bälle gespielt sind, dann Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Die Hüfte früh öffnen und Ball und Minitor sehen", "Abstand zum Trainer schaffen und den Ball in der Bewegung annehmen", "Mit dem hinteren Fuß annehmen und nach vorn mitnehmen", "Wenige Kontakte: annehmen und mit dem zweiten Kontakt wechseln"],
 "materials": ["2 Minitore", "3 Hütchen", "2 Prallbretter (Steigerung)", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Seitenwechsel ins Minitor. Spieler acht spielt zwei Prallpässe mit dem Trainer und wechselt dann mit einem langen Ball die Seite.",
 "board": {"lines": LINES, "goals": TORE, "cones": cones(), "players": sp(),
  "balls": [B("b1", *BALL_T)] + ERSATZ,
  "steps": [
   S("Erster Prallpass", "Der Trainer passt zu Spieler acht ins Dreieck. Spieler acht spielt den Ball direkt zurück.",
     ps("b1", [50.6, 36.6]), ps("b1", BALL_T, after=True)),
   S("Um das Hütchen", "Spieler acht läuft außen um das rechte Hütchen. Der Trainer passt wieder, und Spieler acht spielt direkt zurück.",
     mv("n8", [57.5, 35.5]), mv("n8", [59.5, 42], after=True), ps("b1", [60.1, 42.6], after=True), ps("b1", BALL_T, after=True)),
   S("Absetzen, Hüfte öffnen", "Spieler acht setzt sich nach außen ab und öffnet die Hüfte. So sieht er den Ball und das Minitor auf der anderen Seite. Der Trainer passt in den Lauf.",
     mv("n8", [65, 38]), bl("n8", [45.5, 33], after=True), ps("b1", [65.6, 38.6], after=True)),
   S("Seitenwechsel: Ziel", "Spieler acht nimmt den Ball mit dem hinteren Fuß nach vorn mit. Mit dem zweiten Kontakt spielt er den langen Ball ins linke Minitor. Das ist das Ziel. Danach geht er zurück ins Dreieck, und es geht zur anderen Seite.",
     dr("n8", "b1", [63, 35]), ps("b1", ZIEL, after=True, bend=8), mv("n8", [50, 36], after=True))],
  "dims": dims(15, 85, 12, 55, "46 m", "27 m", rx=91)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Spieler acht täuscht den Seitenwechsel nur an.", "Seitenwechsel antäuschen",
    "Ist der Seitenwechsel nicht frei, täuscht der Spieler ihn nur an. Er dreht zur sicheren Seite weg, schützt den Ball und spielt zurück zum Trainer. Dann löst er sich neu, nimmt den Ball wieder an und wechselt jetzt die Seite.",
    sp(n8=(65, 38)), [B("b1", 65.6, 38.6)] + ERSATZ,
    [S("Antäuschen, wegdrehen", "Spieler acht schaut zum Minitor und täuscht den langen Ball an. Dann dreht er zur sicheren Seite nach außen weg und spielt zurück zum Trainer.",
       bl("n8", [45.5, 33]), dr("n8", "b1", [67, 44], after=True), ps("b1", BALL_T, after=True)),
     S("Neu anbieten", "Spieler acht löst sich wieder nach außen und öffnet die Hüfte. Der Trainer passt noch einmal.",
       mv("n8", [64, 37.5]), bl("n8", [44.5, 32.5], after=True), ps("b1", [64.6, 38.1], after=True)),
     S("Jetzt der Wechsel: Ziel", "Spieler acht nimmt den Ball nach vorn mit und spielt den langen Ball ins linke Minitor. Das ist das Ziel. Danach geht es zur anderen Seite.",
       dr("n8", "b1", [62, 34.5]), ps("b1", ZIEL, after=True, bend=8))],
    cones=cones()),
  V("Steigerung", "Und jetzt die zweite Steigerung: Vor den Minitoren stehen Prallbretter.", "Hoch über das Prallbrett",
    "Vor jedem Minitor steht ein Prallbrett. Es steht für Gegenspieler, über die der Ball hinweg muss. Der Spieler lehnt sich leicht zurück und trifft den Ball unten. Ist der Ball zu flach, prallt er vom Brett ab.",
    sp(n8=(65, 38)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Annehmen, Hüfte offen", "Spieler acht steht außen und öffnet die Hüfte. Er sieht Ball und Minitor. Der Trainer passt zu ihm.",
       bl("n8", [45.5, 33]), ps("b1", [65.6, 38.6], after=True)),
     S("Über das Brett: Ziel", "Spieler acht nimmt den Ball nach vorn mit. Er bleibt locker, lehnt sich leicht zurück und chippt den Ball über das Prallbrett ins Minitor. Das ist das Ziel. Danach kommt die andere Seite dran.",
       dr("n8", "b1", [63, 35]), ps("b1", ZIEL, after=True, bend=8))],
    cones=cones(True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
