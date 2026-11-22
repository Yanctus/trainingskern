import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 80-P1 (U12-U14, Woche 15 Phase 2): Reverse Pass Activation. 10 x 10 Yards = Feld x 25-75, y 5-55 (9 x 9 m), drei Stangen im
# Dreieck wie im PDF. Nummern wie im PDF (alle blau -> Neon): Neon 8 arbeitet in der Mitte, Neon 4 links, Neon 10 rechts.
# Ein Trainer rechts unten mit Bällen wie im PDF. Die "drive centrally"-Phase als Dribbling über dem rechten Stangenfuß zurück in
# die Mitte. Zweite Fassung = Coaching-Punkt "Use both feet" (andere Seite), keine Steigerung im Original.
# Sichtkegel aus PDF-Seite 2 und Video ("Body shape and eyes to sell disguise", "awareness"): Neon 8 schaut vor dem Rückpass zur
# anderen Seite (Kegel nach links unten wie im PDF eingezeichnet) und spielt dann zurück nach rechts. Rückpass gebogen wie im PDF.
T = P("T", "c", 80, 48, "T")
POS = {"n8": (50.6, 27), "n4": (36.6, 37.5), "n10": (64.2, 38.8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 51.5), B("s2", 80, 51.5)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(40.3, 23, shape="stange"), C(59.8, 23, shape="stange"), C(51.3, 38, shape="stange")]
AN8, AN4, AN10 = [51.2, 27.6], [37.2, 38.1], [64.8, 39.4]
RECHTS, LINKS = [64, 20], [36.6, 20]

u = {"title": "Der versteckte Rückpass", "code": "UE-176", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 3, "players_max": 12, "field_size": "9 x 9 m",
 "description": "Drei Stangen stehen im Dreieck, ein Spieler arbeitet in der Mitte, zwei stehen außen. Nach Doppelpässen läuft der mittlere Spieler um eine Stange und bekommt den Ball. Er nimmt ihn nach innen mit, täuscht mit Körper und Blick einen Pass zur anderen Seite an und spielt dann versteckt zurück. Danach geht es auf der anderen Seite weiter.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern. Drei Stangen im Dreieck: zwei oben, eine unten in der Mitte.",
  "Verteilen: Drei Spieler pro Feld. Spieler acht arbeitet in der Mitte, Spieler vier steht links, Spieler zehn rechts. Bei mehr Kindern mehrere Felder. Der Trainer steht rechts unten mit Bällen.",
  "Ablauf: Doppelpässe mit Spieler zehn, um die rechte Stange laufen und annehmen, nach innen mitnehmen und versteckt zurückpassen. Wieder um die Stange, Ball zurück, in die Mitte dribbeln und das Gleiche links mit Spieler vier.",
  "Wechsel: Nach einer Minute oder einigen Runden geht ein anderer Spieler in die Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Den Rückpass mit Körper und Blick verstecken", "Auf Tempo und Genauigkeit der Pässe achten", "Direkt spielen: kurze, schnelle Kombinationen", "Mit beiden Füßen und mit viel Tempo üben"],
 "materials": ["3 Stangen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Der versteckte Rückpass. Drei Spieler und drei Stangen, und der Spieler in der Mitte lernt, den Gegner mit Körper und Blick zu täuschen.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", *AN8)] + ERSATZ,
  "steps": [
   S("Doppelpässe", "Spieler acht spielt Doppelpässe mit Spieler zehn: hin, zurück und wieder hin.",
     ps("b1", AN10), ps("b1", AN8, after=True), ps("b1", AN10, after=True)),
   S("Um die Stange", "Spieler acht läuft außen um die rechte Stange. Spieler zehn spielt ihm den Ball hoch in den Lauf.",
     mv("n8", [53.5, 18.5]), mv("n8", [59.8, 16.5], after=True), mv("n8", RECHTS, after=True), ps("b1", [64.6, 20.6], delay=0.8)),
   S("Versteckter Rückpass", "Spieler acht nimmt den Ball nach innen mit. Er tut so, als wolle er nach links spielen, und passt dann versteckt zurück zu Spieler zehn.",
     dr("n8", "b1", [55.5, 18]), ps("b1", AN10, after=True, bend=6)),
   S("Wieder um die Stange", "Sofort läuft Spieler acht wieder außen um die Stange, und Spieler zehn spielt ihm den Ball zurück.",
     mv("n8", [59.8, 16.5]), mv("n8", RECHTS, after=True), ps("b1", [64.6, 20.6], delay=0.5)),
   S("In die Mitte", "Spieler acht dribbelt mit Tempo zurück in die Mitte. Jetzt kommt das Gleiche links mit Spieler vier, und nach einer Minute ist ein anderer Spieler in der Mitte dran.",
     dr("n8", "b1", [61, 28]), dr("n8", "b1", [50.6, 27], after=True))],
  "dims": dims(25, 75, 5, 55, "9 m", "9 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit Körper und Blick täuschen.", "Körper und Blick",
    "Der Rückpass soll überraschen. Darum dreht Spieler acht den Körper zur anderen Seite und schaut auch dorthin, als ginge der Pass nach links. Erst im letzten Moment spielt er zurück nach rechts.",
    sp(n8=tuple(RECHTS)), [B("b1", 64.6, 20.6)] + ERSATZ,
    [S("Nach links schauen", "Spieler acht nimmt den Ball nach innen mit, dreht den Körper nach links und schaut dorthin.",
       dr("n8", "b1", [55.5, 18]), bl("n8", [44, 29], after=True)),
     S("Zurück nach rechts", "Dann spielt er den Ball überraschend zurück zu Spieler zehn. Ein Gegner wäre jetzt auf die falsche Seite gelaufen.",
       ps("b1", AN10, bend=6))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit beiden Füßen.", "Beide Füße",
    "Auf der linken Seite läuft alles spiegelverkehrt. Spieler acht spielt jetzt mit Spieler vier und benutzt den anderen Fuß. So wird jeder mit beiden Füßen sicher.",
    sp(), [B("b1", *AN8)] + ERSATZ,
    [S("Doppelpässe links", "Spieler acht spielt Doppelpässe mit Spieler vier, läuft außen um die linke Stange und bekommt den Ball.",
       ps("b1", AN4), ps("b1", AN8, after=True), ps("b1", AN4, after=True),
       mv("n8", [47, 18.5], after=True), mv("n8", [40.3, 16.5], after=True), mv("n8", LINKS, after=True), ps("b1", [37.2, 20.6], after=True)),
     S("Rückpass mit links", "Er nimmt den Ball nach innen mit und spielt mit dem anderen Fuß versteckt zurück zu Spieler vier. Nach einer Minute ist ein anderer Spieler in der Mitte dran.",
       dr("n8", "b1", [45, 18]), ps("b1", AN4, after=True, bend=-6))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
