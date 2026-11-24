import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-95 (U15-U17, Woche 4 Pre-Season): Endurance Runs and Small Sided Games. 40 x 30 Yards = 37 x 27 m (gerundet 35 x 25 m).
# Keine Dublette von UE-129 (PS-59, U12-U14): dort ein Kreis, Vierergruppen und ein Läufer, der seine Mitspieler Runde für Runde
# abholt, 4 gegen 4 auf Minitore. Hier ein Rechteck, Dreiergruppen laufen zusammen außen (85 %) und quer über die Diagonale (50 %),
# danach 3 gegen 3 auf zwei Tore mit Torwart.
# Feld quer wie im PDF (Verhältnis 1,33): x 10-88, y 5-51, Tore links und rechts (Großfeldtor, nur C- und B-Jugend), zwei neutrale
# Torhüter (Grün 1 und 13 -> k1, k2). Blau (8, 10, 11) -> Team Neon, Pink (7, 3, 2) -> Team Rot, Nummern wie im PDF (eindeutig).
# Gezeigt wird nur je eine laufende Dreiergruppe; die wartenden Gruppen und das laufende Spiel aus dem PDF nur im Text (3D-Abstand).
# Die Gruppen stehen in einer Reihe an der langen Seite außen (im PDF an der Ecke). Team Neon greift rechts an, Team Rot links (Video).
# Ein Trainer statt zwei, rechts neben dem Feld unter dem Tor (im PDF unten rechts); er spielt dem schnelleren Team den Ball zu.
# Nur die Längen-Maßlinie unten (rechts steht ein Tor), die Breite steht in field_size.
# Fassungen: Video-Einblendung "Leader sets pace from the front, increase to 85 % speed" (Coaching-Punkt) und PDF Key Coaching
# Point 2 "fake front post - attack back post" (Coaching-Punkt).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
FX0, FX1, FY0, FY1 = 10, 88, 5, 51
T = P("T", "c", 94, 44, "T")
BALLE = [B("b0", 94.6, 44.6), B("s1", 96.5, 48.5), B("s2", 96.5, 51.5)]
TW = {"k1": (13.5, 28), "k2": (84.5, 28)}
START = {"n8": (27, 55), "n10": (18.6, 55), "n11": (10.2, 55), "r7": (71.2, 1.5), "r3": (79.6, 1.5), "r2": (88, 1.5)}
def sp(d):
    d = dict(d); d.update(TW)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
TORE = [{"x": FX0, "y": 28, "side": "left", "size": "gross"}, {"x": FX1, "y": 28, "side": "right", "size": "gross"}]
CONES = ecken(FX0, FY0, FX1 - FX0, FY1 - FY0)
DIMS = dims(FX0, FX1, FY0, FY1, "35 m", "25 m")[:1]
# Stationen des Laufs
AUSSEN1 = {"n8": (86, 55), "n10": (77.6, 55), "n11": (69.2, 55), "r7": (12, 1.5), "r3": (20.4, 1.5), "r2": (28.8, 1.5)}
QUER = {"n8": (12, 2), "n10": (20.5, 6.5), "n11": (29, 11), "r7": (85.5, 54), "r3": (77, 49.5), "r2": (68.5, 45)}
AUSSEN2 = {"n8": (86.5, 1.5), "n10": (78.1, 1.5), "n11": (69.7, 1.5), "r7": (12, 55), "r3": (20.4, 55), "r2": (28.8, 55)}
def lauf(ziel, wer, bend=0, **k): return [mv(i, list(ziel[i]), bend=bend, **k) for i in wer]
NEON, ROT = ["n8", "n10", "n11"], ["r7", "r3", "r2"]
# 3 gegen 3 (Coaching-Punkt 2): Team Rot greift links an
SPIEL = {"r7": (65, 16), "n10": (55.5, 24.4), "r3": (44, 28), "n11": (35, 24), "n8": (53, 40), "r2": (42, 46)}

u = {"title": "Tempoläufe ins 3 gegen 3", "code": "UE-329", "kind": "Spielform",
 "focuses": ["Kondition", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 14, "players_max": 20,
 "field_size": "35 x 25 m",
 "description": "Zwei Teams laufen in Gruppen zu dritt um das Feld, an den langen Seiten mit fünfundachtzig Prozent und quer über die Diagonale mit halbem Tempo. Die Gruppe, die zuerst an der Ecke gegenüber ankommt, bekommt vom Trainer den Ball. Dann wird sofort drei gegen drei auf zwei Tore mit Torwart gespielt. Nach einem Treffer oder wenn der Ball ins Aus geht, erholen sich die sechs, und die nächsten Gruppen laufen los.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 25 Metern mit Hütchen an den vier Ecken. An jeder schmalen Seite steht ein Tor mit Torwart.",
  "Verteilen: Zwei Teams, jedes in Gruppen zu dritt aufgeteilt. Eine Gruppe von Team Neon startet an einer Ecke, eine Gruppe von Team Rot an der Ecke gegenüber. Die anderen Gruppen warten neben dem Feld, der Trainer steht mit Bällen neben einem Tor.",
  "Ablauf: Auf Pfiff laufen beide Gruppen an der langen Seite mit fünfundachtzig Prozent, quer über die Diagonale mit halbem Tempo und an der anderen langen Seite wieder mit fünfundachtzig Prozent. Wer zuerst an der Ecke ankommt, bekommt den Ball, dann wird drei gegen drei gespielt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach einem Treffer oder wenn der Ball ins Aus geht, gehen die sechs raus und erholen sich. Das ist der Startschuss für die nächsten zwei Gruppen."],
 "organisation_show": ORG,
 "coaching_points": ["Der Vorderste macht das Tempo, die anderen bleiben dran", "Außen Tempo halten, quer locker laufen", "Sofort vom Laufen ins Spiel umschalten", "Schneller Doppelpass, dann hinter die Abwehr"],
 "materials": ["2 Tore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Tempoläufe ins drei gegen drei. Erst laufen zwei Dreiergruppen einmal quer über das Feld, dann geht es sofort ins Spiel auf zwei Tore.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(START), "balls": BALLE,
  "steps": [
   S("Außen mit fünfundachtzig Prozent", "Pfiff, und beide Gruppen laufen gleichzeitig los. Team Neon an der einen langen Seite, Team Rot an der anderen. Fünfundachtzig Prozent, Spieler acht und Spieler sieben laufen vorn.",
     *lauf(AUSSEN1, NEON), *lauf(AUSSEN1, ROT)),
   S("Quer mit halbem Tempo", "An der Ecke geht es quer über die Diagonale. Hier nur halbes Tempo, die Beine erholen sich kurz. Die beiden Gruppen laufen aneinander vorbei.",
     *lauf(QUER, NEON, bend=4), *lauf(QUER, ROT, bend=4)),
   S("Wieder Tempo bis zur Ecke", "An der anderen langen Seite wieder fünfundachtzig Prozent bis zur Ecke. Team Neon ist zuerst da.",
     *lauf(AUSSEN2, NEON), *lauf(AUSSEN2, ROT, delay=0.5)),
   S("Ball zum schnelleren Team", "Der Trainer spielt Spieler acht den Ball zu, und Team Neon greift sofort das Tor gegenüber an. Team Rot kommt von der anderen Ecke und verteidigt.",
     mv("n8", [66, 16]), mv("n10", [70, 38]), mv("n11", [54, 10]), ps("b0", [66.6, 16.6], after=True),
     mv("r7", [73, 17], delay=0.2), mv("r3", [50, 40], delay=0.2), mv("r2", [44, 26], delay=0.2)),
   S("Doppelpass und Abschluss: Punkt", "Spieler acht spielt zu Spieler zehn und startet sofort an Spieler sieben vorbei. Der Ball kommt direkt zurück, Spieler acht trifft ins kurze Eck, und das gibt einen Punkt für Team Neon. Jetzt gehen die sechs raus und erholen sich, und die nächsten zwei Gruppen laufen los.",
     ps("b0", [70.6, 38.6]), mv("n8", [74, 25], delay=0.2), mv("n8", [80, 24], after=True),
     ps("b0", [80.6, 24.6], after=True), ps("b0", [87.7, 20.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Erste macht das Tempo.", "Der Erste macht das Tempo",
    "Nach dem Querlauf zieht der Vorderste das Tempo wieder auf fünfundachtzig Prozent an. Die anderen beiden bleiben dicht hinter ihm. So kommt die Gruppe zusammen an und kann sofort spielen.",
    sp(QUER), BALLE,
    [S("Spieler acht zieht an", "Spieler acht ist als Erster aus der Diagonale raus und zieht sofort an. Spieler zehn und Spieler elf bleiben dicht hinter ihm. Bei Team Rot macht Spieler sieben das Tempo.",
       *lauf(AUSSEN2, NEON), *lauf(AUSSEN2, ROT, delay=0.5)),
     S("Zusammen rein ins Spiel", "Alle drei sind gleichzeitig an der Ecke. Ohne Pause geht es ins Feld, und der Trainer spielt Spieler acht den Ball.",
       mv("n8", [66, 16]), mv("n10", [70, 38]), mv("n11", [54, 10]), ps("b0", [66.6, 16.6], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Kurz antäuschen, dann lang gehen.", "Kurz antäuschen, lang gehen",
    "Team Rot greift an, Spieler zwei hat den Ball außen. Spieler drei täuscht einen Lauf an den kurzen Pfosten an und zieht dann scharf an den langen. So hängt er seinen Gegenspieler ab.",
    sp(SPIEL), [B("b0", 42.6, 46.6), B("s1", 96.5, 48.5), B("s2", 96.5, 51.5)],
    [S("Antäuschen zum kurzen Pfosten", "Spieler zwei dribbelt außen Richtung Tor. Spieler drei läuft zum kurzen Pfosten, und Spieler elf geht mit.",
       dr("r2", "b0", [32, 47]), mv("r3", [34, 37], delay=0.2), mv("n11", [37, 32], delay=0.4)),
     S("Scharf an den langen Pfosten: Punkt", "Jetzt zieht Spieler drei scharf an den langen Pfosten. Spieler elf ist zu spät. Spieler zwei spielt den Ball genau dorthin, Spieler drei trifft, und das gibt einen Punkt für Team Rot.",
       mv("r3", [25, 22]), ps("b0", [25.6, 22.6], delay=0.3), ps("b0", [10.3, 25], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
