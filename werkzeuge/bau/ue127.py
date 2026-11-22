import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-51 (U12-U14, Woche 1 Pre-Season): Team Relay: Sprint, Dribble and Finish. 30 x 30 Yards = Feld x 27-73, y 4-50.
# Wartende: Starter und Anspieler unten, die anderen zwei seitlich neben dem Feld (3D-Abstand). Rot neu nummeriert (2, 3, 8, 9).
# Vier Bahnen: Neon links (A: Hütchen-Zickzack 27-42.7, B: Dribbelbahn 42.7-50.2 mit Minitor unten),
# Rot rechts (C: Zickzack 50.2-64.5, D: Dribbelbahn 64.5-73 mit Minitor unten). Ein Trainer oben mit Ersatzbällen.
T = P("T", "c", 57.5, 2.4, "T")
def sp(**k):
    d = {"n6": (30, 52.6), "n7": (40.4, 53), "n4": (19.5, 40), "n5": (19.5, 23),
         "r2": (52.4, 52.6), "r3": (62.4, 53), "r8": (81, 40), "r9": (81, 23)}
    d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.2, 2.4)]
BAELLE = [B("b1", 46.5, 6.2), B("b2", 69, 6.2)] + ERSATZ
LINES = [rect(27, 4, 46, 46), line(42.7, 4, 42.7, 50), line(50.2, 4, 50.2, 50), line(64.5, 4, 64.5, 50)]
KEGEL = [C(30, 48), C(40.5, 38), C(29.5, 28), C(40.5, 18), C(29.5, 8),
         C(52.4, 48), C(63, 38), C(52, 28), C(63, 18), C(52, 8)]
TORE = [{"x": 46.4, "y": 50, "side": "bottom"}, {"x": 68.3, "y": 50, "side": "bottom"}]
# Zickzack: an jedem Hütchen vorbei bis nach oben
ZN = [[39.4, 38], [30.6, 28], [39.4, 18], [30.6, 8.6]]
ZR = [[61.9, 38], [53.1, 28], [61.9, 18], [53.1, 8.6]]
def zickzack(who, wege, delay=None):
    return [mv(who, wege[0], delay=delay)] + [mv(who, w, after=True) for w in wege[1:]]

u = {"title": "Sprintstaffel mit Doppelpass", "code": "UE-127", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Dribbling", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Zwei Teams laufen eine Staffel gegeneinander, jedes Team hat seinen eigenen Parcours. Der Erste sprintet im Zickzack an allen Hütchen vorbei nach oben, holt sich dort den Ball und dribbelt in der Nebenbahn zurück. Unten spielt er einen Doppelpass mit einem Mitspieler und schließt ins Minitor ab. Dann klatscht er den Nächsten ab. Sind alle vier durch, läuft das Team die Runde noch einmal ohne Ball, und wer zuerst wieder komplett am Start steht, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, geteilt in vier Bahnen. Jedes Team hat eine breite Bahn mit fünf Hütchen im Zickzack und daneben eine schmale Dribbelbahn mit einem Minitor unten. Oben in der Dribbelbahn liegt der Ball, beim Trainer liegen Ersatzbälle.",
  "Verteilen: Zwei Teams mit je vier Spielern, Team Neon links, Team Rot rechts. Der Erste steht am Start-Hütchen, der Nächste wartet links neben dem Minitor als Anspieler, die anderen beiden warten neben dem Feld.",
  "Ablauf: Auf Pfiff sprinten die Ersten im Zickzack nach oben, holen den Ball, dribbeln zurück, spielen einen Doppelpass mit dem Anspieler und schließen ins Minitor ab. Danach klatschen sie den Nächsten ab, und der Trainer legt oben einen neuen Ball hin.",
  "Wertung: Sind alle vier durch, läuft das Team die Runde noch einmal ohne Ball. Das Team, das zuerst wieder komplett am Start steht, gewinnt die Staffel. Dann neue Reihenfolge und nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Zwischen den Hütchen voll sprinten", "An jedem Hütchen scharf abdrehen und sofort neu antreten", "Den Ball beim Dribbeln eng führen, mit beiden Füßen", "Genau passen und mit einem Kontakt abschließen"],
 "materials": ["10 Hütchen", "2 Minitore", "Mehrere Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Sprintstaffel mit Doppelpass. Zwei Teams, Zickzack-Sprint, Dribbling, Doppelpass und Abschluss, dann das Ganze noch einmal ohne Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Im Zickzack nach oben", "Auf Pfiff sprinten Spieler sechs und Spieler zwei gleichzeitig los und laufen im Zickzack an jedem Hütchen vorbei bis nach oben.",
     *zickzack("n6", ZN), *zickzack("r2", ZR, delay=0.15)),
   S("Ball holen, zurückdribbeln", "Oben holen sie sich den Ball und dribbeln in ihrer Nebenbahn mit Tempo zurück nach unten.",
     mv("n6", [45.6, 6.8]), dr("n6", "b1", [46.2, 31.5], after=True),
     mv("r2", [68.1, 6.8], delay=0.15), dr("r2", "b2", [68.6, 31.5], after=True)),
   S("Doppelpass, dann Abschluss", "Unten spielen sie einen Doppelpass mit ihrem Anspieler und schließen mit einem Kontakt ins Minitor ab.",
     ps("b1", [40.6, 52.3]), mv("n6", [47.4, 37], after=True), ps("b1", [47.4, 37.6], after=True), ps("b1", [46.4, 50.3], after=True),
     ps("b2", [62.6, 52.3], delay=0.15), mv("r2", [69.4, 37], after=True), ps("b2", [69.4, 37.6], after=True), ps("b2", [68.3, 50.3], after=True)),
   S("Abklatschen, der Nächste läuft", "Dann klatschen sie den Anspieler ab, und Spieler sieben und Spieler drei starten. Sind alle vier durch, läuft jedes Team die Runde noch einmal ohne Ball. Das Team, das zuerst wieder komplett am Start steht, gewinnt die Staffel.",
     mv("n6", [42.6, 51.6]), mv("n7", [30.6, 50.5], after=True), mv("n7", ZN[0], after=True),
     mv("r2", [64.6, 51.6], delay=0.15), mv("r3", [53, 50.5], after=True), mv("r3", ZR[0], after=True))],
  "dims": dims(27, 73, 4, 50, "27 m", "27 m", rx=89)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: An jedem Hütchen scharf abdrehen und mit einem Kontakt abschließen.", "Scharf abdrehen",
    "Wer an den Hütchen weite Bögen läuft, verliert die Staffel. Kurz vor dem Hütchen mit kleinen Schritten abbremsen, mit dem äußeren Fuß abdrücken und sofort in die neue Richtung sprinten. Unten kommt der Rückpass in den Lauf und geht direkt ins Minitor, ohne ihn vorher zu stoppen.",
    sp(), BAELLE,
    [S("Scharf abdrehen am Hütchen", "Spieler sechs bremst kurz vor dem Hütchen mit kleinen Schritten ab und drückt sich sofort in die neue Richtung ab.",
       mv("n6", ZN[0]), mv("n6", ZN[1], after=True), mv("n6", ZN[2], after=True)),
     S("Direkt abschließen", "Oben holt er den Ball und dribbelt zurück. Unten kommt der Rückpass in den Lauf, und Spieler sechs schießt ihn mit einem Kontakt ins Minitor. Dann klatscht er Spieler sieben ab, der als Nächster läuft.",
       mv("n6", ZN[3]), mv("n6", [45.6, 6.8], after=True), dr("n6", "b1", [46.2, 31.5], after=True), ps("b1", [40.6, 52.3], after=True),
       mv("n6", [47.4, 37], after=True), ps("b1", [47.4, 37.6], after=True), ps("b1", [46.4, 50.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Die zweite Runde läuft ohne Ball.", "Die Runde ohne Ball",
    "Sind alle vier mit Ball durch, kommt sofort die zweite Runde ohne Ball. Jetzt zählt nur noch das Tempo: Zickzack nach oben, in der Dribbelbahn gerade zurück sprinten und abklatschen. Das Team, das zuerst wieder komplett am Start steht, gewinnt die Staffel.",
    sp(), ERSATZ,
    [S("Zickzack nach oben", "Spieler sechs und Spieler zwei sprinten wieder gleichzeitig im Zickzack nach oben, diesmal ohne Ball.",
       *zickzack("n6", ZN), *zickzack("r2", ZR, delay=0.15)),
     S("Gerade zurück, abklatschen", "Oben wechseln sie in die Nebenbahn, sprinten gerade zurück und klatschen den Nächsten ab, der sofort startet. Wer zuerst wieder komplett am Start steht, gewinnt die Staffel.",
       mv("n6", [46.2, 8]), mv("n6", [42.6, 51.6], after=True), mv("n7", [30.6, 50.5], after=True), mv("n7", ZN[0], after=True),
       mv("r2", [68.6, 8], delay=0.15), mv("r2", [64.6, 51.6], after=True), mv("r3", [53, 50.5], after=True), mv("r3", ZR[0], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Daneben schießen kostet Zeit.", "Daneben kostet Zeit",
    "Jetzt zählt jedes Tor einen Punkt für das Team, und Daneben schießen wird bestraft: Geht der Abschluss am Minitor vorbei, muss das ganze Team zwei Sekunden warten, bevor der Nächste starten darf. So zählt Genauigkeit genauso viel wie Tempo.",
    sp(n6=(47.4, 37), r2=(69.4, 37)), [B("b1", 47.4, 37.6), B("b2", 69.4, 37.6)] + ERSATZ,
    [S("Rot trifft, Neon schießt daneben", "Spieler zwei trifft ins Minitor, und das gibt einen Punkt für Team Rot. Spieler sechs schießt am Minitor vorbei.",
       ps("b2", [68.3, 50.3]), ps("b1", [41.4, 51.2], delay=0.15)),
     S("Rot startet, Neon wartet", "Spieler zwei klatscht Spieler drei ab, der sofort startet. Team Neon muss zwei Sekunden warten, erst dann darf Spieler sieben loslaufen.",
       mv("r2", [64.6, 51.6]), mv("r3", [53, 50.5], after=True), mv("r3", ZR[0], after=True),
       mv("n6", [42.6, 51.6], delay=0.15), mv("n7", [30.6, 50.5], delay=2.2), mv("n7", ZN[0], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
