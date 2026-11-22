import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P15 (U12-U14, Einzeltraining): Movement Recovery - Full Backs (PDF: Movement and Recovery Runs - Fullbacks).
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m). Ausrichtung wie im PDF (Minitore links, Trainer unten, Spieler läuft nach
# oben und flankt nach links), nicht gedreht. Das untere Minitor steht im Original schräg; hier gerade mit Öffnung nach rechts.
# Pinker Spieler P -> Spieler zwei (Team Neon, rechter Außenverteidiger). Zwei Dummys als Stangen (Verteidiger im Strafraum,
# gegnerischer Außenverteidiger). Gelbes Hütchen -> neon. Ballhaufen beim Trainer nur als zwei Ersatzbälle.
# Ablauf nach PDF und Video (0:08-0:34): Prallpass mit dem Trainer, Rückzug zum Hütchen, Pass auf den hinteren Fuß, Dribbling
# am Dummy vorbei (außen), Flanke ins Minitor, sofort Sprint zurück vor den Dummy. Reine Technikübung: Ziel statt Punkte.
# Sichtkegel: Im Video kein Kegel eingezeichnet. PDF „Decision on Cross - choose the best cross based on space“ und Video
# (1:03-1:12) „Disguise the delivery - play to the goal with more space“: Richtung aus dem Sinn -> im Coaching-Punkt schaut
# Spieler zwei vor der Flanke zu den Minitoren.
# Fassungen: Coaching-Punkt „Flanke wählen“ (PDF, Video 1:03-1:12), Steigerung „Lauf hinter den Gegner“ (PDF Seite 2,
# Video 0:40-1:03: zweiter Prallpass am Hütchen, Bogenlauf hinter den Dummy, langer Pass, direkte Flanke).
T = P("T", "c", 54, 45, "T")
POS = {"n2": (61, 24.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 48.5, 47), B("s2", 46, 49)]
BALL_T = [54.6, 45.6]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 28, "y": 12, "side": "left"}, {"x": 30, "y": 32, "side": "left"}]
CONES = [C(41, 21.5, shape="stange"), C(67.5, 29, shape="stange"), C(67, 52, "neon")]
OBEN = [28.5, 12]
UNTEN = [30.5, 32]
START = [61, 24.5]
HUT = [62.5, 47.5]
HUT_B = [63.1, 48.1]

u = {"title": "Flanke, dann Rücklauf zum Dummy", "code": "UE-284", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Außenverteidiger übt Flanken und den schnellen Rücklauf. Nach einem Prallpass mit dem Trainer zieht er sich zum Hütchen zurück, bekommt den Ball und dribbelt am Dummy vorbei. Dann flankt er in eines der zwei Minitore. Sofort danach sprintet er zurück vor den Dummy.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Links zwei Minitore und ein Dummy als Verteidiger im Strafraum, rechts ein Dummy als Gegenspieler und unten ein Hütchen.",
  "Verteilen: Spieler zwei steht vor dem rechten Dummy. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Prallpass mit dem Trainer, zurück zum Hütchen, Ball annehmen, am Dummy vorbeidribbeln und in ein Minitor flanken.",
  "Wechsel: Nach jeder Flanke sofort zurück vor den Dummy sprinten, dann kommt der nächste Ball. Gearbeitet wird auf Zeit oder bis alle Bälle gespielt sind."],
 "organisation_show": ORG,
 "coaching_points": ["Hohes Tempo: schnelle, scharfe Bewegungen wie im Spiel", "Vor den Ball kommen und die Läufe gut timen", "Nach der Flanke sofort zurücksprinten", "Die Flanke genau und mit dem richtigen Tempo spielen"],
 "materials": ["2 Minitore", "2 Dummys", "1 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Flanke, dann Rücklauf zum Dummy. Spieler zwei dribbelt am Gegenspieler vorbei, flankt ins Minitor und sprintet sofort zurück.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *BALL_T)] + ERSATZ,
  "steps": [
   S("Prallpass", "Der Trainer passt zu Spieler zwei. Spieler zwei spielt den Ball direkt zurück.",
     ps("b1", [61.6, 25.1]), ps("b1", BALL_T, after=True)),
   S("Zurück zum Hütchen", "Spieler zwei sprintet zurück zum Hütchen und kommt vor den Ball. Der Trainer passt ihm den Ball auf den hinteren Fuß.",
     mv("n2", HUT), ps("b1", HUT_B, after=True)),
   S("Am Dummy vorbei", "Spieler zwei dribbelt schnell auf den Dummy zu. Mit einer Finte geht er außen vorbei und nach vorn.",
     dr("n2", "b1", [65, 37]), dr("n2", "b1", [72.5, 30], after=True), dr("n2", "b1", [70, 18], after=True)),
   S("Flanke ins Minitor", "Spieler zwei flankt in das obere Minitor. Das ist wie eine Flanke in den Strafraum.",
     ps("b1", OBEN, bend=6)),
   S("Rücklauf: Ziel", "Sofort sprintet Spieler zwei zurück vor den Dummy. Steht er dort, ist das Ziel geschafft. Dann kommt der nächste Ball, und die nächste Runde beginnt.",
     mv("n2", START))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die richtige Flanke wählen.", "Die richtige Flanke wählen",
    "Vor der Flanke schaut der Spieler, wo mehr Platz ist. Ist der Strafraum zu, spielt er den Rückpass ins untere Minitor. Er verrät dabei nicht zu früh, wohin der Ball geht.",
    sp(n2=(70, 18)), [B("b1", 70.6, 18.6)] + ERSATZ,
    [S("Schauen", "Spieler zwei ist am Dummy vorbei und schaut nach innen: Wo ist mehr Platz?",
       bl("n2", [49, 21])),
     S("Rückpass: Ziel", "Unten ist mehr Platz. Spieler zwei spielt den Rückpass ins untere Minitor. Das ist das Ziel. Dann sprintet er zurück vor den Dummy.",
       ps("b1", UNTEN), mv("n2", START, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Spieler zwei läuft hinter den Gegner.", "Lauf hinter den Gegner",
    "Am Hütchen gibt es einen zweiten Prallpass. Dann läuft der Spieler im Bogen außen hinter den Dummy. Der Trainer spielt den langen Ball in den Lauf, und der Spieler flankt direkt.",
    sp(n2=tuple(HUT)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Prallpass am Hütchen", "Der Trainer passt zu Spieler zwei am Hütchen. Spieler zwei spielt direkt zurück.",
       ps("b1", HUT_B), ps("b1", BALL_T, after=True)),
     S("Lauf hinter den Gegner", "Spieler zwei startet im Bogen außen hinter den Dummy. Der Trainer spielt den langen Ball in den Lauf.",
       mv("n2", [72.5, 38]), mv("n2", [73, 22], after=True), mv("n2", [70, 12], after=True), ps("b1", [70.6, 12.6], delay=1.2)),
     S("Direkt flanken: Ziel", "Spieler zwei flankt direkt ins obere Minitor. Das ist das Ziel. Danach sprintet er zurück vor den Dummy, und die nächste Runde beginnt.",
       ps("b1", OBEN), mv("n2", START, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
