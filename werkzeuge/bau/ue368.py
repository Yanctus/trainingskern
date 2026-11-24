import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P5 (U15-U17, Woche 24 Phase 6): The Back 4 Unit Defending The Cross (Skill). 45 x 45 Yards = 41 x 41 m (gerundet 40 x 40 m).
# Feld x 25-75, y 5-55, Ausrichtung wie im PDF: großes Tor mit neutralem Torwart oben, zwei Minitore unten an den Ecken
# (im PDF schräg, hier gerade). Drei Reihen Hütchen: Start (orange, je links neben dem Spieler, damit der Rücklauf frei ist),
# Sichern (orange, drei Paare in den Lücken), Kopfball (neon, im PDF gelb mit den Nummern eins bis vier).
# Blau (aktive Kette) -> Team Neon mit den Nummern aus dem Video (2, 6, 5, 3 von links nach rechts = Position eins bis vier).
# Die zweite Kette (im Video rot) wartet nur im Text. Ein Trainer statt zwei: Der Trainer unten wirft die Bälle zum Kopfball;
# die Flanke schlägt ein neutraler Flankengeber links oben (im PDF der zweite Trainer), team t, Label „F“.
# Kopfball zum Trainer als Pass zurück dargestellt. Wertung ergänzt (im Original keine): Kopfball nach der Flanke Richtung
# Minitor, landet er drin, gibt das einen Punkt für Team Neon.
# Fassungen: PDF Key Coaching Point 1 (kompakt, die anderen drei sichern) und 2 (mit Ziel klären, Richtung Minitor).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 50, 52.5, "T")  # unten im Feld, wirft die Bälle zum Kopfball
ERSATZ = [B("s1", 53.5, 53.4), B("s2", 56, 53.4)]
F = P("f", "t", 17, 13, "F")  # Flankengeber links oben neben dem Feld
X = {"n2": 31, "n6": 43.5, "n5": 56.5, "n3": 69}  # Positionen eins bis vier
SY, KY = 23, 47  # Startreihe, Kopfballhütchen
def sp(**k):
    d = {i: (x, SY) for i, x in X.items()}; d.update(k)
    return [P("k", "t", 50, 7, "TW")] + [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [F, T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 30, "y": 55, "side": "bottom"}, {"x": 70, "y": 55, "side": "bottom"}]
SICHERN = [35.5, 39, 48.3, 51.7, 61, 64.5]
CONES = [C(x - 3.5, SY) for x in X.values()] + [C(x, 36) for x in SICHERN] + [C(x, KY, "neon") for x in X.values()]
DIMS = dims(25, 75, 5, 55, "40 m", "40 m")
BT = fu((50, 52.5))
BALLE = [B("b1", *BT), B("b2", 17.6, 13.6)] + ERSATZ
def ruf(wer, sichern, delay=0.3):
    """Ein Spieler sprintet zum Kopfballhütchen, die anderen drei rücken gleichzeitig zu den Hütchen in der Mitte auf."""
    return [mv(wer, [X[wer], KY - 3])] + [mv(i, [x, 33.5], delay=delay) for i, x in sichern.items()]
def kopfball(wer, delay=0.2):
    return [ps("b1", fu((X[wer], KY - 3)), delay=delay, after=True), ps("b1", BT, after=True)]
def zurueck(**k):
    return [mv(i, [x, SY], **k) for i, x in X.items()]
VOR_TOR = {"n2": [38, 14], "n6": [45.5, 12.5], "n5": [54.5, 12.5], "n3": [62, 14]}
def rueck():
    """Rücklauf nach der Eins: Spieler sechs und fünf laufen erst schräg vor, damit sie nicht über die Starthütchen laufen."""
    return [mv("n2", VOR_TOR["n2"]), mv("n3", VOR_TOR["n3"]), mv("n5", [57, 26]), mv("n5", VOR_TOR["n5"], after=True),
            mv("n6", [43, 26]), mv("n6", VOR_TOR["n6"], after=True)]

u = {"title": "Viererkette köpft und klärt", "code": "UE-368", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 7, "players_max": 10,
 "field_size": "40 x 40 m",
 "description": "Eine Viererkette steht vor dem großen Tor und hört auf die Rufe des Trainers. Ruft er eine Nummer, sprintet dieser Verteidiger zum Hütchen und köpft den Ball zurück, die anderen drei rücken auf und sichern ab. Ruft er „Flanke!“, sprinten alle zurück vor das Tor und klären die Flanke Richtung Minitor. Danach ist die nächste Viererkette dran.",
 "organisation": ["Aufbauen: Ein Feld von 40 mal 40 Metern mit großem Tor und Torwart oben und zwei Minitoren unten. Davor drei Reihen Hütchen: vier Starthütchen, drei Paare zum Absichern in der Mitte und vier Kopfballhütchen, nummeriert von eins bis vier.",
  "Verteilen: Vier Verteidiger stehen an den Starthütchen, die nächste Viererkette wartet neben dem Feld. Der Trainer steht unten mit Bällen, links oben steht ein Flankengeber mit Bällen.",
  "Ablauf: Der Trainer ruft eine Nummer von eins bis vier. Dieser Verteidiger sprintet zu seinem Kopfballhütchen und köpft den zugeworfenen Ball zurück, die anderen drei rücken zu den Hütchen in der Mitte auf. Danach ruft der Trainer die nächste Nummer oder „Zurück“. Ruft er „Flanke!“, sprinten alle vor das Tor und wehren die Flanke ab.",
  "Wertung und Wechsel: Wer die Flanke Richtung Minitor klärt und trifft, holt einen Punkt für Team Neon. Danach rückt die nächste Viererkette nach vorn."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, die anderen drei sichern schräg dahinter", "Mit der Stirn köpfen und sofort zurück in die Kette", "Bei „Flanke!“ Vollgas zurück vor das Tor", "Nicht einfach weghauen, Richtung Minitor klären"],
 "materials": ["1 großes Tor", "2 Minitore", "16 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette köpft und klärt. Die Kette hört auf den Trainer. Einer köpft vorn, die anderen sichern ab. Und beim Ruf „Flanke!“ sprinten alle zurück und klären.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BALLE,
  "steps": [
   S("Trainer ruft die Drei", "Der Trainer ruft drei. Das ist Spieler fünf, und der sprintet sofort vor zum dritten Kopfballhütchen. Gleichzeitig rücken die anderen drei zu den Hütchen in der Mitte auf, schräg hinter ihn.",
     *ruf("n5", {"n2": 39, "n6": 48.3, "n3": 61})),
   S("Kopfball zurück zum Trainer", "Der Trainer wirft den Ball. Spieler fünf köpft ihn mit der Stirn genau zurück.",
     *kopfball("n5", delay=None)),
   S("Zurück zum Start", "Jetzt ruft der Trainer zurück. Alle vier laufen rückwärts in ihre Startposition, die Kette steht wieder auf einer Linie.",
     *zurueck()),
   S("Die Eins, dann Kopfball", "Nächste Nummer, die Eins. Jetzt sprintet Spieler zwei ganz außen vor. Die anderen drei schieben schräg zu ihm rüber. Kopfball zurück zum Trainer.",
     *ruf("n2", {"n6": 35.5, "n5": 48.3, "n3": 61}), *kopfball("n2", delay=0.4)),
   S("Flanke! Alle vor das Tor", "Der Trainer ruft Flanke. Alle vier drehen um und sprinten zurück vor das Tor. Von links oben kommt die Flanke.",
     *rueck(), ps("b2", fu(VOR_TOR["n6"]), delay=0.3, after=True)),
   S("Geklärt ins Minitor: Punkt", "Spieler sechs ist zuerst am Ball und köpft ihn weit raus, Richtung Minitor. Er landet drin, und das gibt einen Punkt für Team Neon. Dann rückt die nächste Viererkette vor.",
     ps("b2", [30, 54.5], bend=-8))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die anderen drei sichern ab.", "Die anderen drei sichern",
    "Presst einer vorn, bleibt keiner stehen. Der Nächste rückt schräg hinter ihn, die anderen schieben mit zur Seite. So bleiben die Abstände klein, und durch die Mitte kommt kein Ball.",
    sp(), BALLE,
    [S("Die Vier: alle schieben rüber", "Der Trainer ruft vier, Spieler drei sprintet ganz rechts vor. Spieler fünf geht schräg hinter ihn, Spieler sechs und Spieler zwei schieben mit nach rechts.",
       *ruf("n3", {"n2": 39, "n6": 51.7, "n5": 64.5})),
     S("Kopfball und sofort zurück", "Kopfball zurück zum Trainer. Danach geht keiner spazieren. Alle vier laufen sofort zurück in die Kette.",
       *kopfball("n3", delay=None), *zurueck(delay=0.4))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit Ziel klären.", "Mit Ziel klären",
    "Wer die Flanke abwehrt, haut den Ball nicht irgendwohin. Er köpft ihn hoch und weit zur Seite, Richtung Minitor. Dort würde im Spiel der eigene Flügelspieler stehen. Danach rückt die Kette sofort wieder raus.",
    sp(), BALLE,
    [S("Flanke, alle vor das Tor", "Flanke! Die Kette sprintet zurück vor das Tor. Diesmal kommt der Ball zu Spieler fünf.",
       *[mv(i, p) for i, p in VOR_TOR.items()], ps("b2", fu(VOR_TOR["n5"]), delay=1.0)),
     S("Zur Seite köpfen: Punkt", "Spieler fünf köpft den Ball hoch und weit nach außen, genau Richtung Minitor. Er landet drin, und das gibt einen Punkt für Team Neon.",
       ps("b2", [70, 54.5], bend=8)),
     S("Kette rückt raus", "Sofort schiebt die ganze Kette gemeinsam raus bis zu den Starthütchen. Dann ruft der Trainer die nächste Nummer.",
       *zurueck())], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
