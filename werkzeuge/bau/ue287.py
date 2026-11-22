import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P20 (U12-U14, Einzeltraining): Playing Out From the Back - CB (PDF: "How to Pass Out From the Back - CB").
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), Spiel nach oben. Zwei Dummys (Stürmer, Flügelspieler) als Stangen bei
# (43/68, 36,5). Drei Minitore oben: Mitte = Zehner, links = gegenüberliegender Mittelfeldspieler, rechts = Außenverteidiger.
# Die zwei Ecktore stehen im Original schräg in den oberen Ecken; hier auf der oberen Linie bei x 31 und 69.
# Innenverteidiger = Spieler vier. Trainer links unten mit den Bällen. Grundform nach PDF/Video: Prallpass, Anlaufen zur
# Stange und Bogen zurück, Pass vor der äußeren Stange annehmen, erster Kontakt nach innen, zwischen den Stangen andribbeln,
# Pass ins mittlere Minitor. Acht Durchgänge, dann Pause.
# Sichtkegel: Video 0:36-0:48 "1st touch inside - step in, scan & play out quickly" (Grundform: Blick zum mittleren Tor);
# Video 1:15-1:30 "Face hips centrally to disguise pass" mit eingezeichnetem Kegel nach vorn/links (Steigerung 1, dann
# verdeckt ins rechte Tor); Steigerung 2: Körper öffnen und zum linken Tor schauen (Ton "opens their body to find a pass").
# Fassungen = Progression 1 und 2 aus dem PDF.
T = P("T", "c", 33, 48.5, "T")
POS = {"n4": (52, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 29.5, 51.5), B("s2", 27.5, 51.5)]
TR = [33.6, 49.1]
GOALS = [{"x": 50, "y": 5, "side": "top"}, {"x": 31, "y": 5, "side": "top"}, {"x": 69, "y": 5, "side": "top"}]
CONES = [C(43, 36.5, shape="stange"), C(68, 36.5, shape="stange")]

u = {"title": "Aufdrehen, andribbeln, Minitor", "code": "UE-287", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Dribbling"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "18 x 18 m",
 "description": "Einzeltraining für Innenverteidiger mit dem Trainer. Spieler vier nimmt vor der äußeren Stange an, dreht mit dem ersten Kontakt nach innen auf und dribbelt zwischen den beiden Stangen an. Dann spielt er den Ball in das mittlere Minitor, also zum Zehner. So lernt er, mit Ball aus der Abwehr herauszurücken und die erste Pressinglinie zu überspielen.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Zwei Stangen in der Mitte als Stürmer und Flügelspieler des Gegners, oben drei Minitore.",
  "Verteilen: Spieler vier steht unten in der Mitte. Der Trainer steht links unten mit vielen Bällen.",
  "Ablauf: Prallpass mit dem Trainer, zur Stange laufen und im Bogen zurück. Den Pass vor der äußeren Stange annehmen, nach innen aufdrehen, andribbeln und ins mittlere Minitor spielen.",
  "Wechsel: Nach acht Durchgängen ist Pause. Sind zwei Spieler da, wechseln sie sich ab."],
 "organisation_show": ORG,
 "coaching_points": ["Den Körper öffnen und in Spielrichtung schauen", "Erster Kontakt nach innen, an der Stange vorbei", "Mit Ball mutig nach vorn rücken", "Fest und genau ins Minitor spielen"],
 "materials": ["2 Stangen", "3 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufdrehen, andribbeln, Minitor. Spieler vier ist Innenverteidiger und rückt mit dem Ball an den Stangen vorbei nach vorn.",
 "board": {"lines": [rect(25, 5, 50, 50)], "goals": GOALS, "cones": CONES, "players": sp(), "balls": [B("b1", *TR)] + ERSATZ,
  "steps": [
   S("Prallpass", "Der Trainer passt zu Spieler vier, und Spieler vier lässt den Ball direkt zurückprallen.",
     ps("b1", [52.6, 51.6]), ps("b1", TR, after=True)),
   S("Anlaufen und zurück", "Jetzt läuft Spieler vier Richtung äußere Stange und dreht im Bogen wieder nach hinten außen.",
     mv("n4", [60, 42]), mv("n4", [66, 41], after=True), mv("n4", [70, 46], after=True)),
   S("Nach innen aufdrehen", "Der Trainer spielt ihm den Ball vor der äußeren Stange zu. Spieler vier nimmt mit offenem Körper an, und der erste Kontakt geht nach innen.",
     ps("b1", [70.6, 46.6]), dr("n4", "b1", [62, 41], after=True)),
   S("Andribbeln", "Er dribbelt zwischen den beiden Stangen durch und hebt den Kopf. Wo ist der Zehner?",
     dr("n4", "b1", [56, 33]), bl("n4", [50, 14], after=True)),
   S("Ins mittlere Minitor", "Spieler vier spielt fest und genau ins mittlere Minitor, das ist das Ziel. Dann geht er zurück nach unten, und der Trainer spielt den nächsten Ball. Nach acht Durchgängen ist Pause.",
     ps("b1", [50, 6.5]), mv("n4", [52, 51], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball für den verdeckten Pass nach rechts.", "Zweiter Ball nach rechts",
    "Nach dem Pass ins mittlere Tor läuft Spieler vier sofort um die innere Stange und spielt einen Doppelpass mit dem Trainer. Dann öffnet er sich nach außen und bekommt den zweiten Ball. Er nimmt nach innen an, zeigt mit Hüfte und Augen zur Mitte und spielt dann mit links ins rechte Minitor.",
    sp(n4=(56, 33)), [B("b2", *TR)] + ERSATZ,
    [S("Um die Stange", "Der erste Ball ist im mittleren Tor. Spieler vier läuft sofort um die innere Stange herum nach hinten.",
       mv("n4", [46, 30]), mv("n4", [38, 33], after=True), mv("n4", [38, 41], after=True)),
     S("Doppelpass", "Der Trainer passt zu ihm, und Spieler vier spielt direkt zurück. Dann läuft er nach außen.",
       ps("b2", [38.6, 41.6]), ps("b2", TR, after=True), mv("n4", [55, 47], after=True), mv("n4", [68, 47], after=True)),
     S("Zur Mitte zeigen", "Der zweite Ball kommt. Spieler vier nimmt nach innen an, die Hüfte zeigt zur Mitte, und er schaut nach vorn.",
       ps("b2", [68.6, 47.6]), dr("n4", "b2", [60, 40], after=True), dr("n4", "b2", [55, 34], after=True), bl("n4", [46, 16], after=True)),
     S("Verdeckt nach rechts", "Doch dann spielt er mit links ins rechte Minitor zum Außenverteidiger. Das ist das Ziel. Danach ist der nächste Durchgang dran.",
       ps("b2", [69, 6.5]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein dritter Ball zum Mittelfeldspieler links.", "Dritter Ball nach links",
    "Nach dem Pass ins rechte Tor dreht Spieler vier schnell um und spielt wieder einen Doppelpass mit dem Trainer. Dann öffnet er sofort den Körper, nimmt den dritten Ball an und spielt ihn quer über das Feld ins linke Minitor.",
    sp(n4=(55, 34)), [B("b3", *TR)] + ERSATZ,
    [S("Schnell zurück", "Spieler vier dreht nach dem Pass ins rechte Tor sofort um und läuft nach hinten.",
       mv("n4", [52, 46])),
     S("Doppelpass", "Doppelpass mit dem Trainer. Dann macht Spieler vier zwei Schritte nach rechts.",
       ps("b3", [52.6, 46.6]), ps("b3", TR, after=True), mv("n4", [58, 47], after=True)),
     S("Körper öffnen", "Der dritte Ball kommt. Spieler vier öffnet sofort die Hüfte, nimmt nach vorn an und schaut schon nach links hinüber.",
       ps("b3", [58.6, 47.6]), dr("n4", "b3", [57, 37], after=True), bl("n4", [36, 20], after=True)),
     S("Zum Gegenüber", "Dann spielt er fest ins linke Minitor zum Mittelfeldspieler auf der anderen Seite. Drei Bälle, drei Tore: der Durchgang ist geschafft.",
       ps("b3", [31, 6.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
