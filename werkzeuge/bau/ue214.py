import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-16 (U12-U14, Woche 30 Phase 6): Using Speed and Brains Warm Up. 25 x 25 Yards = Feld x 25-75, y 5-55 (23 x 23 m), in der
# Mitte die Stangen. Im Original laufen drei Spieler mit drei Hütchenfarben (gelb, blau, rot) und drei Stangen; die Tafel kennt nur
# orange und neon, darum zeigt sie zwei Spieler: Neon sieben sammelt die neonfarbenen, Rot neun die orangen Hütchen. Der dritte
# Spieler mit einer dritten Farbe und einer dritten Stange steht nur im Text. Ein Trainer statt zwei (im PDF zwei Ecken), er steht
# links neben dem Feld. Hütchen-Lagen frei nach dem PDF verteilt (je vier pro Farbe), Startplatz unten wie im PDF.
# Getragene Hütchen wandern wie in UE-112 nach der Rückkehr des Spielers auf die Stange (ps mit after).
# Sichtkegel: Text "Scan the environment before starting" und "evaluate cone positions just before starting" -> in der
# Grundform und im ersten Coaching-Punkt bl() vor dem Start zu den eigenen Hütchen (links und rechts, im Video kein Kegel
# eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 18, 30, "T")
ERSATZ = [B("s1", 21.6, 33.5), B("s2", 18, 33.5)]
POS = {"n7": (43, 51), "r9": (57, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
STN, STR = [45, 30], [55, 30]
KEG = {"k1": (31, 45, "neon"), "k2": (29, 19, "neon"), "k3": (41, 10, "neon"), "k4": (62, 49, "neon"),
       "k5": (70, 37, "orange"), "k6": (69, 16, "orange"), "k7": (57, 9, "orange"), "k8": (34, 53, "orange")}
def cones():
    return [C(*STN, shape="stange", id="st1"), C(*STR, shape="stange", id="st2")] + \
           [C(x, y, c, id=i) for i, (x, y, c) in KEG.items()]
LINES = [rect(25, 5, 50, 50)]

u = {"title": "Hütchen sammeln mit Köpfchen", "code": "UE-214", "kind": "Spielform",
 "focuses": ["Erwärmung", "Schnelligkeit", "Koordination"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 2, "players_max": 3, "field_size": "23 x 23 m",
 "description": "Zwei oder drei Spieler treten gegeneinander an. Jeder hat vier Hütchen in seiner Farbe, die im Feld verteilt liegen. Wer zuerst alle vier Hütchen geholt und auf seine Stange in der Mitte gesteckt hat, gewinnt. Schnell sein reicht nicht: Wer vorher schaut und kluge, gerade Wege plant, ist vorn.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern. In der Mitte eine Stange pro Spieler, im Feld je vier Hütchen pro Spieler in seiner Farbe.",
  "Verteilen: Der Spieler von Team Neon sammelt die neonfarbenen Hütchen, der Spieler von Team Rot die orangen. Ein dritter Spieler bekommt Hütchen in einer dritten Farbe und eine dritte Stange.",
  "Ablauf: Alle starten gleichzeitig unten am Feld. Jeder holt ein Hütchen nach dem anderen und steckt es auf seine Stange.",
  "Wertung und Wechsel: Wer zuerst alle vier Hütchen auf der Stange hat, gewinnt, und das gibt einen Punkt. Dann legt der Trainer die Hütchen neu aus, und die nächsten Spieler sind dran."],
 "organisation_show": ORG,
 "coaching_points": ["Vor dem Start schauen, wo die eigenen Hütchen liegen", "Einen klugen Weg planen", "Gerade laufen, dann braucht es weniger Kurven", "Nicht zu wild sprinten: rechtzeitig bremsen und drehen"],
 "materials": ["3 Stangen", "4 Hütchen pro Spieler in einer Farbe", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Hütchen sammeln mit Köpfchen. Wer zuerst alle Hütchen seiner Farbe auf seine Stange steckt, gewinnt.",
 "board": {"lines": LINES, "cones": cones(), "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Erst schauen", "Vor dem Start schauen beide genau, wo ihre vier Hütchen liegen. Neon sieben sucht die neonfarbenen, Rot neun die orangen Hütchen.",
     bl("n7", [33, 37]), bl("n7", [59, 44], after=True), bl("r9", [67, 38]), bl("r9", [40, 49], after=True)),
   S("Los: erstes Hütchen", "Auf das Zeichen des Trainers sprinten beide gleichzeitig los. Jeder holt ein Hütchen und steckt es auf seine Stange in der Mitte.",
     mv("n7", [33.5, 43.5]), mv("n7", [42, 33], after=True), ps("k1", STN, after=True),
     mv("r9", [67.5, 38.5]), mv("r9", [58, 33], after=True), ps("k5", STR, after=True)),
   S("Zweites und drittes", "Weiter geht es mit Hütchen zwei und drei. Gerade Wege mit wenigen Kurven sparen Zeit.",
     mv("n7", [31.5, 20.5]), mv("n7", [42, 27], after=True), ps("k2", STN, after=True),
     mv("n7", [41.5, 12.5], after=True), mv("n7", [42, 27], after=True), ps("k3", STN, after=True),
     mv("r9", [67, 18.5]), mv("r9", [58, 27], after=True), ps("k6", STR, after=True),
     mv("r9", [57.5, 12], after=True), mv("r9", [58, 27], after=True), ps("k7", STR, after=True)),
   S("Viertes Hütchen: Punkt", "Neon sieben steckt als Erster das vierte Hütchen auf seine Stange und gewinnt, und das gibt einen Punkt für Team Neon. Dann legt der Trainer die Hütchen neu aus, und die nächsten Spieler sind dran.",
     mv("n7", [59.5, 47]), mv("n7", [42, 33], after=True), ps("k4", STN, after=True),
     mv("r9", [36.5, 51]), mv("r9", [48, 41], after=True))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst schauen, dann losrennen.", "Erst schauen, dann los",
    "Wer vor dem Start schaut, sieht, welches Hütchen am nächsten liegt. Neon sieben schaut und holt zuerst das nahe Hütchen. Rot neun rennt ohne Schauen los zum Hütchen, das weit weg liegt.",
    sp(), ERSATZ,
    [S("Schauen oder rennen", "Neon sieben schaut nach links und nach rechts. Rot neun rennt sofort los, ganz nach oben zum weiten Hütchen.",
       bl("n7", [33, 37]), bl("n7", [59, 44], after=True), mv("r9", [67, 18.5])),
     S("Der kurze Weg", "Neon sieben holt das nahe Hütchen und steckt es auf die Stange. Rot neun ist noch unterwegs.",
       mv("n7", [33.5, 43.5]), mv("n7", [42, 33], after=True), ps("k1", STN, after=True),
       mv("r9", [58, 27]), ps("k6", STR, after=True))],
    lines=LINES, cones=cones()),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Gerade laufen und rechtzeitig bremsen.", "Gerade laufen, früh bremsen",
    "Wer mit voller Kraft auf ein Hütchen zu sprintet, kann nicht schnell bremsen und braucht einen großen Bogen. Besser gerade laufen, kurz vor dem Hütchen langsamer werden und mit kleinen Schritten drehen.",
    sp(), ERSATZ,
    [S("Zu schnell", "Rot neun sprintet mit voller Kraft zum Hütchen. Er kann nicht bremsen, läuft vorbei und muss in einem großen Bogen zurück.",
       mv("r9", [73, 33]), mv("r9", [76.5, 36], after=True), mv("r9", [73, 40.5], after=True), mv("r9", [70.5, 39.5], after=True)),
     S("Gerade und kontrolliert", "Neon sieben läuft gerade, bremst kurz vor dem Hütchen ab und dreht mit kleinen Schritten. So ist er schneller zurück an seiner Stange.",
       mv("n7", [33.5, 43.5]), mv("n7", [42, 33], after=True), ps("k1", STN, after=True),
       mv("r9", [58, 33], delay=0.6), ps("k5", STR, after=True))],
    lines=LINES, cones=cones())]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
