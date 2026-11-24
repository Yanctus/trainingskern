import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 34-P4 (U15-U17, Woche 32 Phase 4): Develop Triangle Passing Combinations. 20 x 20 Yards = 18 x 18 m, Feld x 25-75, y 5-55,
# in vier gleiche Quadrate geteilt (gestrichelt). Ausrichtung wie im PDF (Start oben links, der Ball läuft links herunter und
# unten nach rechts, über rechts zurück nach oben). Nummern wie im PDF (2-9, nur Team Neon). Ein Trainer statt zwei, oben links
# außerhalb (im PDF oben rechts bzw. in der Progression oben links und am Minitor).
# Ablauf nach PDF und Video: Spieler sieben spielt den Prallpass mit Spieler neun, der danach nach außen geht; steil ins untere
# Feld zu Spieler drei, der dem Ball entgegenkommt und nach außen auf Spieler neun ablegt; Spieler neun steckt durch zu Spieler
# fünf unten rechts. Neustart wie im Video über Spieler vier und Spieler zwei zurück zum Start. Jeder folgt seinem Pass zur
# nächsten Station (PDF: anti-clockwise, Ton: clockwise; im Video laufen sie wie hier). Keine Punkte in der Grundform (Technik).
# Fassungen: Steigerung 1 = zweiter Ball (Ton und Video, Spieler fünf startet ihn unten rechts), Steigerung 2 = Minitor am Ende
# (PDF-Progression: Spieler fünf legt für Spieler drei ab, der abschließt). Minitor rechts neben dem unteren rechten Feld.
# Sichtkegel aus Text ("Head up to locate players on the move"): Spieler drei schaut erst zum Passgeber, nach der Annahme schwenkt
# der Kegel zu Spieler neun außen (bl mit von). Kein Aufdrehen (direkt abgelegt), darum kein Drehpfeil.
# Keine Dublette: UE-217 (34-P5, sechs gegen drei mit Dreieck), UE-226 (34-P6, Endzonen-Spiel), UE-239 (45-P12, V-Form).
T = P("T", "c", 13, 4, "T")
ERSATZ = [B("s1", 13.6, 8.5), B("s2", 10, 7.5)]
A, Aq, Bp, C_, D, Dq, E, F = (39, 9), (30, 9), (37, 30), (37, 51), (61, 51), (69.5, 52), (62, 30), (62, 9)
W, R3 = [28, 27], [46, 48.5]
BLA, BLW = [42.6, 28.8], [33.1, 33.1]  # Blickziele von Spieler drei (Richtung Start bzw. Spieler neun, ca. 20 Einheiten lang)
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
POS = {"n7": A, "n8": Aq, "n9": Bp, "n3": C_, "n5": D, "n6": Dq, "n4": E, "n2": F}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(25, 5, 50, 50), line(50, 5, 50, 55), line(25, 30, 75, 30)]
CONES = ecken(25, 5, 50, 50)
TOR = {"x": 75, "y": 42, "side": "right"}
DIMS = dims(25, 75, 5, 55, "18 m", "18 m", rx=83)
def zurueck_oben(who):  # Spieler zwei läuft oben außen herum zum Start (nicht durch den Start)
    return [mv(who, [55, 3.5], after=True), mv(who, [33, 3.5], after=True), mv(who, list(Aq), after=True)]

u = {"title": "Passdreiecke in vier Feldern", "code": "UE-384", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 10,
 "field_size": "18 x 18 m",
 "description": "Ein Feld in vier Quadraten, an sechs Stationen stehen Spieler. Der Ball läuft mit einem Kontakt in kleinen Dreiecken: Prallpass mit dem Spieler in der Mitte, steil ins untere Feld, nach außen ablegen und quer durchstecken ins Feld daneben. Über die andere Seite kommt der Ball zurück zum Start. Wer abgespielt hat, läuft seinem Pass hinterher zur nächsten Station.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, in vier gleich große Quadrate geteilt.",
  "Verteilen: Acht Spieler an sechs Stationen. Zwei stehen mit Ball am Start im oberen Feld, einer in der Mitte am Rand der Teilungslinie, einer unten im selben Feld. Im Feld daneben stehen zwei unten, einer in der Mitte und einer oben. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Prallpass mit dem Spieler in der Mitte, der danach nach außen geht. Steilpass ins untere Feld, der Spieler dort kommt entgegen und legt nach außen ab. Von außen geht der Ball quer ins Feld daneben, dann über die Mitte und oben zurück zum Start.",
  "Wechsel: Jeder läuft seinem Pass hinterher zur nächsten Station. Ist der Ball zurück am Start, beginnt der nächste Durchgang."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und mit der richtigen Härte passen, damit es direkt weitergeht", "Erst loslaufen, wenn der Pass kommt", "Kopf hoch, bevor der Ball da ist", "Laut ansagen und mit beiden Füßen spielen"],
 "materials": ["4 Hütchen", "1 Minitor", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passdreiecke in vier Feldern. Der Ball läuft mit einem Kontakt im Dreieck, und jeder rückt nach seinem Pass eine Station weiter.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *f(A))] + ERSATZ,
  "steps": [
   S("Prallpass mit Spieler neun", "Spieler sieben startet. Er spielt zu Spieler neun und bekommt den Ball direkt zurück. Sofort geht Spieler neun ein paar Schritte nach außen.",
     ps("b1", f(Bp)), ps("b1", f(A), after=True), mv("n9", W, after=True)),
   S("Steil ins untere Feld", "Spieler drei kommt dem Ball entgegen und schaut zu Spieler sieben. Der spielt steil ins untere Feld. Gleich danach läuft Spieler sieben in die Mitte, auf den Platz von Spieler neun.",
     mv("n3", R3), bl("n3", BLA, after=True), ps("b1", f(R3), after=True), mv("n7", list(Bp), after=True)),
   S("Kopf hoch, ablegen nach außen", "Spieler drei nimmt den Kopf hoch und sieht Spieler neun außen. Mit einem Kontakt legt er ihm den Ball hin.",
     bl("n3", BLW, von=BLA, dauer=1.3), ps("b1", f(W), after=True)),
   S("Durchstecken ins Feld daneben", "Spieler neun steckt den Ball flach durch ins untere Feld daneben, genau zu Spieler fünf. Dann läuft er auf den Platz von Spieler drei.",
     ps("b1", f(D)), mv("n9", list(C_), after=True)),
   S("Hoch über Spieler vier", "Jetzt geht es zurück nach oben. Spieler fünf spielt zu Spieler vier, und der spielt direkt weiter zu Spieler zwei.",
     ps("b1", f(E)), ps("b1", f(F), after=True)),
   S("Alle rücken weiter", "Spieler acht geht an den Start, und Spieler zwei spielt ihm den Ball. Jeder läuft seinem Pass hinterher zur nächsten Station. Gezählt wird nichts, der Ball soll mit einem Kontakt laufen. Jetzt startet Spieler acht, und Spieler sieben steht in der Mitte.",
     mv("n8", list(A)), ps("b1", f(A), delay=0.4), *zurueck_oben("n2"),
     mv("n4", list(F), delay=1.2), mv("n5", list(E), delay=0.3), mv("n6", list(D), delay=0.8),
     mv("n3", [50, 56.5], delay=0.2), mv("n3", [66, 56.5], after=True), mv("n3", list(Dq), after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball kommt dazu.", "Zweiter Ball im Spiel",
    "Unten startet der zweite Ball, während der erste noch im Dreieck läuft. Jetzt muss jeder wissen, wo beide Bälle sind. Ansagen, Kopf hoch und schnell weiterrücken.",
    sp(), [B("b1", *f(A)), B("b2", *f(D))] + ERSATZ,
    [S("Zwei Bälle gleichzeitig", "Spieler sieben spielt den Prallpass mit Spieler neun. Gleichzeitig startet unten Spieler fünf mit dem zweiten Ball. Er spielt hoch zu Spieler vier, und der spielt direkt weiter zu Spieler zwei.",
       ps("b1", f(Bp)), ps("b1", f(A), after=True), mv("n9", W, after=True),
       ps("b2", f(E), delay=0.3), ps("b2", f(F), after=True)),
     S("Steil, ablegen, zum Start", "Oben links geht der erste Ball steil zu Spieler drei, der legt nach außen ab. Spieler zwei spielt den zweiten Ball schon zum Start, wo jetzt Spieler acht steht. Alle anderen rücken eine Station weiter.",
       mv("n3", R3), ps("b1", f(R3), delay=0.3), bl("n3", BLW, von=BLA, dauer=1.3, after=True), ps("b1", f(W), after=True),
       mv("n7", list(Bp), delay=1.2), mv("n8", list(A), delay=0.4),
       ps("b2", f(A), delay=1.0), *zurueck_oben("n2"),
       mv("n4", list(F), delay=2.0), mv("n5", list(E), delay=0.6), mv("n6", list(D), delay=1.0)),
     S("Beide Bälle laufen", "Spieler neun steckt durch zu Spieler sechs, der direkt hoch zu Spieler fünf spielt. Oben spielt Spieler acht schon den Prallpass mit Spieler sieben. Keiner steht, beide Bälle bleiben in Bewegung.",
       ps("b1", f(D)), ps("b1", f(E), after=True), mv("n9", list(C_), delay=0.6),
       ps("b2", f(Bp), delay=0.3), ps("b2", f(A), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Am Ende wartet ein Minitor.", "Abschluss ins Minitor",
    "Neben dem unteren Feld rechts steht ein Minitor. Spieler drei läuft nach seinem Ablegen weiter, bekommt den Ball noch einmal und schließt ab. Der Trainer spielt sofort den nächsten Ball zum Start.",
    sp(), [B("b1", *f(A))] + ERSATZ,
    [S("Prallpass, steil, ablegen", "Wie gewohnt: Prallpass mit Spieler neun, steil zu Spieler drei, und der legt nach außen ab.",
       ps("b1", f(Bp)), ps("b1", f(A), after=True), mv("n9", W, after=True), mv("n3", R3, delay=0.6),
       ps("b1", f(R3), after=True), ps("b1", f(W), after=True), mv("n7", list(Bp), delay=2.2)),
     S("Durchstecken, Spieler drei startet", "Spieler neun steckt durch zu Spieler fünf. Spieler drei läuft sofort weiter Richtung Minitor, und Spieler fünf legt ihm den Ball direkt in den Lauf.",
       ps("b1", f(D)), mv("n3", [55, 45], delay=0.4), ps("b1", [55.6, 45.6], after=True), mv("n9", list(C_), delay=0.8)),
     S("Abschluss ins Minitor: Punkt", "Spieler drei schießt direkt ins Minitor, und das gibt einen Punkt für Team Neon. Sofort spielt der Trainer den nächsten Ball zu Spieler acht, und der nächste Durchgang läuft.",
       ps("b1", [74.6, 42]), mv("n8", list(A), delay=0.3), ps("s1", f(A), delay=1.0))],
    goals=[TOR], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
