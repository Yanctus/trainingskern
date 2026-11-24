import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-6 (U15-U17, Woche 27 Phase 2): Activation Warm Up (im PDF „1-2 Passing and Movement Activation“). 20 x 20 Yards = 18 x 18 m,
# Feld x 25-75, y 5-55, Ausrichtung wie im PDF (nicht gedreht). Nummern wie im PDF, alle Team Neon (die Rollen wechseln).
# Vier Eckstationen (7, 8, 11, 2) und vier innere Stationen (9, 5, 4, 3), je ein Hütchen; die Hütchen liegen etwas versetzt,
# damit kein Pass und kein Laufweg hindurchgeht. Ein Trainer statt zwei.
# Ablauf nach PDF und Video: 11 spielt Doppelpass mit 4, dann quer zu 2, 11 und 4 tauschen; 2 mit 3, hoch zu 8; 8 mit 5, quer zu 7;
# 7 mit 9 und wieder runter. Der Ball läuft gegen den Uhrzeigersinn ums Viereck (im Bild: unten nach rechts, rechts nach oben).
# Fassungen wie die PDF-Progressionen: 1 zweiter Ball gleichzeitig (Start bei 11 und bei 8), 2 Sprint zum Hütchen in der Mitte,
# dann locker zur neuen Station. Im Original keine Punkte; Ziel: Der Ball läuft ohne Pause.
# Sichtkegel aus dem Text der Progressionen („sharpening awareness“, „remain alert“): In der ersten Steigerung schaut Spieler sieben
# zum Ball, nimmt an und schwenkt dann zu Spieler neun (ein Kegel mit von, kein Aufdrehen). Im Video keiner eingezeichnet.
# Kein Dubletten-Fall: UE-090 (WU-7) hat dieselbe Aufstellung mit acht Stationen, aber Pass durch die Mitte, einen Störer und den
# Doppelpass um ihn herum; hier Doppelpass mit dem Innenspieler, Pass an der Seite entlang und Platztausch. WU-8 (UE-178) und
# WU-9 (UE-107) sind andere Übungen.
T = P("T", "c", 16, 30, "T")
ERSATZ = [B("s1", 14.6, 34), B("s2", 17.4, 34.6)]
POS = {"n7": (29, 9), "n8": (71, 9), "n9": (42, 21), "n5": (58, 21), "n4": (42, 39), "n3": (58, 39), "n11": (29, 51), "n2": (71, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(i, d=None): x, y = (d or POS)[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
HUET = [(26.5, 6.5), (73.5, 6.5), (26.5, 53.5), (73.5, 53.5), (45, 24), (55, 24), (45, 36), (55, 36)]
CONES = [C(x, y) for x, y in HUET]
LINES = [rect(25, 5, 50, 50)]
DIMS = dims(25, 75, 5, 55, "18 m", "18 m")
B1 = B("b1", *f("n11"))
B2 = B("b2", *f("n8"))
# Bausteine
def doppel_unten(**k):
    return [ps("b1", f("n4"), **k), mv("n11", [35, 50], delay=(k.get("delay") or 0) + 0.3), ps("b1", [35.6, 50.6], after=True)]
def doppel_oben(**k):
    return [ps("b2", f("n5"), **k), mv("n8", [65, 10], delay=(k.get("delay") or 0) + 0.3), ps("b2", [65.6, 10.6], after=True)]

u = {"title": "Doppelpass und Platztausch", "code": "UE-376", "kind": "Übungsform",
 "focuses": ["Passspiel", "Erwärmung", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 8, "players_max": 8,
 "field_size": "18 x 18 m",
 "description": "Ein Aufwärmen mit vier Stationen in den Ecken und vier in der Mitte. Der Eckspieler spielt einen Doppelpass mit dem Innenspieler vor ihm und passt dann an der Seite entlang zur nächsten Ecke. Danach tauschen die beiden die Plätze, und die nächste Ecke macht dasselbe. So läuft der Ball ohne Pause ums Viereck.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Vier Hütchen markieren die Ecken, vier weitere ein kleines Viereck in der Mitte.",
  "Verteilen: An jedem Hütchen steht ein Spieler, also acht Spieler. Der Spieler in der Ecke unten links hat den Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass mit dem Innenspieler, dann flach an der Seite entlang zur nächsten Ecke. Ecke und Innenspieler tauschen die Plätze. Die nächste Ecke startet sofort mit ihrem Doppelpass.",
  "Wechsel: Nach jedem Doppelpass tauschen die zwei ihre Plätze. So spielt jeder mal in der Ecke und mal in der Mitte, und der Ball läuft ohne Pause weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und genau passen", "Nach dem Pass sofort los zur neuen Station", "Laut rufen, wer tauscht", "Abwechselnd mit rechts und links passen"],
 "materials": ["8 Hütchen", "2 Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Doppelpass und Platztausch. Acht Stationen, ein Ball, der ums Viereck läuft. Nach jedem Doppelpass wechseln zwei Spieler den Platz.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B1] + ERSATZ,
  "steps": [
   S("Doppelpass mit Spieler vier", "Spieler elf startet in der Ecke. Er spielt flach zu Spieler vier, geht zwei Schritte mit und bekommt den Ball direkt zurück.",
     *doppel_unten()),
   S("Quer zur Ecke, Plätze tauschen", "Jetzt geht der Ball an der Seite entlang zu Spieler zwei. Dann tauschen Spieler elf und Spieler vier die Plätze. Spieler elf geht nach innen, Spieler vier in die Ecke.",
     ps("b1", f("n2")), mv("n11", [42, 39], after=True, bend=0.3), mv("n4", [29, 51], delay=0.9, bend=0.3)),
   S("Doppelpass rechts, dann hoch", "Spieler zwei macht das Gleiche mit Spieler drei. Doppelpass, und dann geht der Ball hoch zu Spieler acht in die nächste Ecke.",
     ps("b1", f("n3")), mv("n2", [71, 44.5], delay=0.3), ps("b1", [71.6, 45.1], after=True), ps("b1", f("n8"), after=True)),
   S("Tauschen, oben geht es weiter", "Spieler zwei und drei tauschen. Oben spielt Spieler acht mit Spieler fünf und dann quer zu Spieler sieben. Danach kommt Spieler sieben mit Spieler neun. So läuft der Ball immer weiter ums Viereck, und nach jedem Doppelpass wird getauscht.",
     mv("n2", [58, 39], bend=0.3), mv("n3", [71, 51], delay=0.2, bend=0.3),
     ps("b1", f("n5"), delay=0.4), mv("n8", [65, 10], delay=0.7), ps("b1", [65.6, 10.6], after=True), ps("b1", f("n7"), after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball läuft gleichzeitig.", "Zwei Bälle gleichzeitig",
    "Jetzt laufen zwei Bälle gleichzeitig durch den Ablauf, einer startet unten bei Spieler elf, einer oben bei Spieler acht. Jeder muss früher schauen, wo der nächste Ball herkommt. Wer gerade getauscht hat, ist sofort wieder bereit.",
    sp(), [B1, B2] + ERSATZ,
    [S("Zwei Doppelpässe gleichzeitig", "Unten spielt Spieler elf mit Spieler vier, oben zur selben Zeit Spieler acht mit Spieler fünf. Beide bekommen den Ball direkt zurück.",
       *doppel_unten(), *doppel_oben()),
     S("Kopf hoch, der Ball kommt", "Jetzt gehen beide Bälle an der Seite entlang. Spieler sieben schaut zum Ball, der von Spieler acht kommt. Unten tauschen Spieler elf und Spieler vier schon die Plätze.",
       bl("n7", [49, 9.6]), ps("b2", f("n7"), after=True), ps("b1", f("n2")),
       mv("n11", [42, 39], delay=0.9, bend=0.3), mv("n4", [29, 51], delay=0.9, bend=0.3)),
     S("Annehmen und gleich weiter", "Spieler sieben nimmt an, schaut rüber zu Spieler neun und spielt den nächsten Doppelpass. Rechts startet Spieler zwei mit Spieler drei. Zwei Bälle, keine Pause.",
       bl("n7", f("n9"), von=[49, 9.6], dauer=1.3), ps("b2", f("n9"), after=True), ps("b1", f("n3"), delay=0.3))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Sprint zum Hütchen in der Mitte.", "Sprint zum Hütchen",
    "In der Mitte liegt ein Hütchen. Wer nach dem Pass nach innen wechselt, sprintet erst bis zu diesem Hütchen, bremst ab, dreht um und läuft dann locker zu seiner neuen Station. Das macht die Beine wach für die nächste Übung.",
    sp(), [B1] + ERSATZ,
    [S("Doppelpass und quer", "Spieler elf spielt den Doppelpass mit Spieler vier und dann quer zu Spieler zwei. Bis hier alles wie gehabt.",
       *doppel_unten(), ps("b1", f("n2"), after=True)),
     S("Sprint zur Mitte, dann zur Station", "Jetzt sprintet Spieler elf bis zum Hütchen in der Mitte, bremst und dreht um. Dann trabt er locker zur Station von Spieler vier. Der geht in die Ecke.",
       mv("n11", [44, 46]), mv("n11", [50, 30], after=True), mv("n11", [48, 40], after=True), mv("n11", [42, 39], after=True), mv("n4", [29, 51], delay=0.4, bend=0.3)),
     S("Rechts genauso", "Spieler zwei spielt mit Spieler drei und schickt den Ball hoch zu Spieler acht. Dann sprintet er zur Mitte, und Spieler drei geht in die Ecke.",
       ps("b1", f("n3")), mv("n2", [71, 44.5], delay=0.3), ps("b1", [71.6, 45.1], after=True), ps("b1", f("n8"), after=True),
       mv("n2", [54, 45], after=True), mv("n2", [50, 30], after=True), mv("n2", [52, 40], after=True), mv("n2", [58, 39], after=True), mv("n3", [71, 51], delay=1.5, bend=0.3))],
    cones=[C(x, y, id=f"h{i}") for i, (x, y) in enumerate(HUET)] + [C(50, 30, "neon", id="mitte")])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
