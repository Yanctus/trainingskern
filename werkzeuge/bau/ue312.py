import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-32 (U15-U17, Woche 13 Phase 1): The Activation Square, Warm Up. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), in der
# Mitte ein Viereck von 5 Yards (4,5 m) aus vier Hütchen, an jeder Seite ein Starthütchen. Ausrichtung wie im PDF.
# Ein Team (im PDF Pink, im Video Gelb) -> Team Neon, Nummern wie im PDF. Auf der Tafel stehen an jeder Station nur die
# ersten zwei Spieler (3D-Abstand), der dritte (12, 9, 14, 8) steht in der Grundform nur im Text. Die Paare stehen leicht
# versetzt statt in einer Reihe. Ein Trainer wie im PDF.
# Ablauf nach PDF und Video 0:08-0:30: zum Hütchen rechts dribbeln, Ball ablegen, gegen den Uhrzeigersinn zum nächsten
# Hütchen, den Ball dort zur Station passen, weiter zur nächsten Station (im Video stellt man sich eine Station weiter an).
# Steigerung = Progression (Video ab 0:38): vier Eckspieler (12, 9, 8, 14), Doppelpass mit dem Eckspieler vor dem Pass.
# Sichtkegel aus dem Text der Progression ("awareness"): vor dem Doppelpass der Blick zum Eckspieler. Im Video kein Kegel.
T = P("T", "c", 91, 40, "T")
ERSATZ = [B("s1", 94.6, 43.5), B("s2", 91, 43.5)]
POS = {"n11": (45, 9), "n5": (55.5, 7), "n2": (35, 34), "n4": (26.5, 40), "n10": (55, 51), "n3": (44.5, 53), "n6": (65, 26), "n7": (73.5, 20)}
def sp(d): return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(25, 5, 50, 50)]
CONES = [C(44, 24), C(56, 24), C(44, 36), C(56, 36), C(50, 4.5, "neon"), C(30, 35.5, "neon"), C(50, 56, "neon"), C(69.5, 25, "neon")]
# Ablagepunkte außen an den vier Hütchen des Vierecks (oben links, unten links, unten rechts, oben rechts)
OL, UL, UR, OR_ = [42.4, 22.4], [42.2, 37], [57.6, 37.6], [57.6, 22.4]
def ball(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
BAELLE = [B("b1", 45.6, 9.6), B("b2", 35.6, 34.6), B("b3", 55.6, 51.6), B("b4", 65.6, 26.6)]
def hin(): return [dr("n11", "b1", OL), dr("n2", "b2", UL), dr("n10", "b3", UR), dr("n6", "b4", OR_)]
def rum(): return [mv("n11", UL), mv("n2", UR), mv("n10", OR_), mv("n6", OL)]
# Steigerung: Stand nach dem Umlaufen, jeder steht mit dem neuen Ball an seinem Hütchen. Alles viermal um die Mitte gedreht.
def rot(p, n):
    x, y = p
    for _ in range(n): x, y = 50 + (y - 30), 30 - (x - 50)
    return [round(x, 1), round(y, 1)]
AKT, ECK, STA, LAUF = ["n6", "n11", "n2", "n10"], ["n12", "n9", "n8", "n14"], ["n4", "n3", "n7", "n5"], [33, 22]
SPOS = {}
for k in range(4):
    SPOS[AKT[k]] = tuple(rot([41, 21.3], k)); SPOS[ECK[k]] = tuple(rot([30, 10], k)); SPOS[STA[k]] = tuple(rot([27, 30], k))
SPOS["n3"] = (50, 50); SPOS["n5"] = (50, 10)
SB = [B("b%d" % (k + 1), round(SPOS[AKT[k]][0] + 0.6, 1), round(SPOS[AKT[k]][1] + 0.6, 1)) for k in range(4)]
def doppel():
    m = []
    for k in range(4):
        e, l = SPOS[ECK[k]], rot(LAUF, k)
        m += [bl(AKT[k], list(e)), ps("b%d" % (k + 1), ball(e), after=True), mv(AKT[k], l, delay=1.0), ps("b%d" % (k + 1), ball(l), after=True)]
    return m
def weiter(): return [ps("b%d" % (k + 1), ball(SPOS[STA[k]])) for k in range(4)]

u = {"title": "Aktivierung ums Viereck", "code": "UE-312", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 8, "players_max": 12,
 "field_size": "18 x 18 m",
 "description": "Ein Aufwärmen mit vielen Ballkontakten. Vier Spieler dribbeln gleichzeitig von außen zum Viereck in der Mitte und legen ihren Ball dort an einem Hütchen ab. Ohne Ball laufen sie zum nächsten Hütchen, nehmen den Ball des Nachbarn und passen ihn zur Station nach außen. So wandern Bälle und Spieler im Kreis, und keiner steht lange.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. In der Mitte bilden vier Hütchen ein Viereck von 4,5 Metern. In der Mitte jeder Seitenlinie liegt ein Starthütchen.",
  "Verteilen: Dreiergruppen, an jedem Starthütchen eine. Der Erste jeder Gruppe hat einen Ball. Der Trainer steht am Rand.",
  "Ablauf: Alle vier Ersten dribbeln gleichzeitig zum Hütchen rechts vor ihnen und legen den Ball dort still ab. Dann laufen sie gegen den Uhrzeigersinn zum nächsten Hütchen und passen den Ball, der dort liegt, zur Station nach außen.",
  "Wechsel: Nach dem Pass läuft jeder eine Station weiter und stellt sich dort hinten an. Der Angespielte dribbelt sofort los."],
 "organisation_show": ORG,
 "coaching_points": ["Viele kleine Kontakte, der Ball bleibt am Fuß", "Ball still hinlegen, erst dann weiter", "Antreten, abbremsen, wieder antreten", "Flach und genau zur Station passen"],
 "materials": ["8 Hütchen", "4 Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aktivierung ums Viereck. Zum Aufwärmen bekommt jeder viele Ballkontakte. Den eigenen Ball lässt man in der Mitte liegen und holt sich den nächsten.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(POS), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Alle vier dribbeln zum Viereck", "Alle vier starten gleichzeitig. Wir schauen auf Spieler elf. Er dribbelt zum Hütchen rechts vor ihm und legt den Ball dort still ab.",
     *hin()),
   S("Ohne Ball zum nächsten Hütchen", "Jetzt ohne Ball weiter, gegen den Uhrzeigersinn zum nächsten Hütchen. Dort liegt schon der Ball von Spieler zwei.",
     *rum()),
   S("Pass nach außen, weiter zur Station", "Spieler elf passt diesen Ball nach außen zu Spieler vier. Er selbst läuft eine Station weiter und stellt sich dort hinten an. Die Runde ist vorbei, wenn alle vier gepasst haben. Dann dribbeln die vier Angespielten los.",
     ps("b2", [27.1, 40.6]), ps("b3", [45.1, 53.6]), ps("b4", [74.1, 20.6]), ps("b1", [56.1, 7.6]),
     mv("n11", [37, 51], delay=0.5), mv("n2", [66, 41], delay=0.5), mv("n10", [63, 10], delay=0.5), mv("n6", [34, 21], delay=0.5))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Enge Kontakte, und der Ball liegt still.", "Enge Kontakte, Ball still",
    "Auf dem kurzen Weg zum Hütchen hat der Spieler viele kleine Kontakte. Am Hütchen stoppt er den Ball, bis er wirklich still liegt. Erst dann tritt er an. Am nächsten Ball bremst er rechtzeitig ab, sonst läuft er daran vorbei.",
    sp(POS), BAELLE + ERSATZ,
    [S("Kleine Kontakte, Sohle drauf", "Spieler elf dribbelt mit vielen kleinen Kontakten. Am Hütchen geht die Sohle auf den Ball. Er liegt still.",
       *hin()),
     S("Antreten und rechtzeitig abbremsen", "Dann der Antritt zum nächsten Hütchen. Kurz davor bremst er mit kleinen Schritten ab und steht sauber hinter dem Ball.",
       *rum())]),
  V("Steigerung", "Und jetzt die Steigerung: Doppelpass mit dem Eckspieler.", "Doppelpass mit der Ecke",
    "In jeder Ecke des Feldes steht jetzt ein Spieler. Wer am Viereck den neuen Ball hat, spielt erst den Doppelpass mit dem Eckspieler und passt dann zur Station. Der Eckspieler steht offen und spielt mit einem Kontakt zurück.",
    sp(SPOS), SB + ERSATZ,
    [S("Doppelpass mit der Ecke", "Wieder alle vier gleichzeitig. Spieler sechs schaut zum Eckspieler, spielt Spieler zwölf an und läuft sofort los. Der Ball kommt mit einem Kontakt in seinen Lauf zurück.",
       *doppel()),
     S("Pass zur Station", "Aus dem Lauf passt Spieler sechs weiter zu Spieler vier an der Station. Der nimmt den Ball nach vorn mit und dribbelt zum Viereck.",
       *weiter())])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
