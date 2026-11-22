import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 100-P2 (U12-U14, Woche 17 Phase 3): Finishing and Recovery Runs. 20 x 15 Yards = Feld x 31.25-68.75, y 5-55 (14 x 18 m),
# oben ein Jugendtor mit neutralem Torwart (im PDF grün), in der Mitte zwei Stangen, unten ein Starthütchen.
# Ausrichtung wie im PDF (Tor oben). Pink (Angreifer) -> Team Neon (7 zwischen den Stangen, 8 wartet unten rechts),
# Blau (Verteidiger) -> Team Rot (4 mit Ball, 5 wartet unten links). Nummern ergänzt (im PDF ohne Nummern).
# Ein Trainer rechts an der Seite mit Bällen (wie im PDF). Die Ballhaufen bei den Schlangen nur im Text.
# Steigerung: zwei Minitore links und rechts an den Seitenlinien für die Verteidiger (Lage aus dem Video).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; der dunkle Kreis im Video ist eine Markierung, kein Blickkegel).
T = P("T", "c", 79, 30, "T")
POS = {"n7": (50, 37), "n8": (55.5, 53), "r4": (45, 53), "r5": (36, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k", "t", 50, 8.5, "TW"), T]
ERSATZ = [B("s1", 82.6, 33.5), B("s2", 79, 33.5)]
LINES = [rect(31.25, 5, 37.5, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(43, 34, shape="stange"), C(57, 34, shape="stange"), C(50, 53)]

u = {"title": "Um die Stange zum Abschluss", "code": "UE-182", "kind": "Übungsform",
 "focuses": ["1 gegen 1", "Ballannahme", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 5, "players_max": 9, "field_size": "14 x 18 m",
 "description": "Eins gegen eins auf ein Tor mit Torwart. Der Verteidiger passt zum Angreifer zwischen den Stangen und sprintet sofort zurück, um zu verteidigen. Der Angreifer nimmt den Ball mit dem ersten Kontakt außen um die Stange mit und greift mit Tempo an. Er zieht den Verteidiger auf eine Seite, wechselt dann die Richtung und schließt schnell ab.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern mit einem Jugendtor oben. In der Mitte zwei Stangen nebeneinander, unten ein Starthütchen.",
  "Verteilen: Zwei Teams, ein neutraler Torwart im Tor. Ein Angreifer von Team Neon steht zwischen den Stangen. Team Rot steht unten links mit Bällen, Team Neon wartet unten rechts. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Verteidiger passt zum Angreifer und sprintet zwischen den Stangen hindurch zurück. Der Angreifer nimmt den Ball außen um eine Stange mit und greift das Tor an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach wird der Verteidiger der neue Angreifer zwischen den Stangen, und der Nächste aus dem anderen Team passt und verteidigt."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem ersten Kontakt sofort mit Tempo angreifen", "Kurze, schnelle Ballkontakte um die Stange", "Den Verteidiger auf eine Seite ziehen, dann Richtung und Tempo wechseln", "Als Verteidiger schnell zurücklaufen und die Richtung vorgeben"],
 "materials": ["1 Jugendtor", "2 Minitore (Steigerung)", "2 Stangen", "1 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Um die Stange zum Abschluss. Der Angreifer nimmt den Ball um die Stange mit und greift an, während der Verteidiger zurücksprintet.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 45.6, 53.6)] + ERSATZ,
  "steps": [
   S("Pass zum Angreifer", "Rot vier passt zu Neon sieben zwischen den Stangen.",
     ps("b1", [50.6, 37.6])),
   S("Um die Stange", "Neon sieben nimmt den Ball mit kurzen Kontakten außen um die linke Stange mit. Gleichzeitig sprintet Rot vier zwischen den Stangen hindurch zurück.",
     dr("n7", "b1", [44, 40]), dr("n7", "b1", [38, 36], after=True), dr("n7", "b1", [40, 28], after=True),
     mv("r4", [50, 30], delay=0.2)),
   S("Auf eine Seite ziehen", "Neon sieben greift mit Tempo an und zieht Rot vier nach links. Der Torwart geht mit.",
     dr("n7", "b1", [41, 20]), mv("r4", [44, 23.5], delay=0.2), mv("k", [46, 8.5], delay=0.3)),
   S("Haken und Abschluss: Punkt", "Neon sieben macht einen Haken nach rechts und schießt sofort. Der Ball geht rechts ins Tor, und das gibt einen Punkt für Team Neon. Jetzt ist Rot vier der neue Angreifer, und Neon acht passt und verteidigt.",
     dr("n7", "b1", [53, 15]), ps("b1", [55, 5.3], after=True))],
  "dims": dims(31.25, 68.75, 5, 55, "14 m", "18 m", rx=74)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnell zurücklaufen und die Richtung vorgeben.", "Schnell zurück",
    "Der Verteidiger sprintet nach dem Pass sofort zwischen den Stangen zurück. Ist er zwischen Ball und Tor, stellt er sich seitlich und lenkt den Angreifer nach außen. Von dort ist der Winkel spitz, und der Torwart hat es leichter.",
    sp(), [B("b1", 50.6, 37.6)] + ERSATZ,
    [S("Zurücksprinten", "Neon sieben nimmt den Ball um die rechte Stange mit. Rot vier sprintet sofort zurück und kommt zwischen Ball und Tor an.",
       dr("n7", "b1", [56, 40]), dr("n7", "b1", [62, 36], after=True), mv("r4", [52, 25], delay=0.2)),
     S("Nach außen lenken", "Rot vier stellt sich seitlich und lenkt Neon sieben nach außen. Neon sieben schießt aus spitzem Winkel, und der Torwart fängt den Ball. Jetzt ist Rot vier der neue Angreifer.",
       dr("n7", "b1", [64, 22]), mv("r4", [57, 21], delay=0.2), mv("k", [54, 8.5], after=True), ps("b1", [54.6, 9.1], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Minitore für die Verteidiger.", "Minitore für Verteidiger",
    "Links und rechts an den Seitenlinien steht jetzt je ein Minitor. Erobert der Verteidiger den Ball, schießt er in eines der Minitore. Der Angreifer muss nach einem Ballverlust sofort pressen.",
    sp(n7=(42, 26), r4=(53, 25)), [B("b1", 42.6, 26.6)] + ERSATZ,
    [S("Ball erobert", "Neon sieben dribbelt aufs Tor zu. Rot vier geht dazwischen und erobert den Ball.",
       dr("n7", "b1", [45, 19]), mv("r4", [47, 16], after=True), ps("b1", [47.6, 16.6], after=True)),
     S("Ins Minitor: Punkt", "Rot vier dribbelt nach rechts und schießt ins Minitor. Das gibt einen Punkt für Team Rot. Neon sieben presst sofort, kommt aber zu spät.",
       dr("r4", "b1", [60, 20]), mv("n7", [55, 23], delay=0.3), ps("b1", [68.4, 22], after=True))],
    goals=TORE + [{"x": 31.25, "y": 22, "side": "left"}, {"x": 68.75, "y": 22, "side": "right"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
