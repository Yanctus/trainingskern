import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 36-P9 (U15-U17, Woche 15): 3 V 3 + 4 Breakout Possession Game. 15 x 30 Yards = 14 x 27 m (ab 20 m gerundet: 14 x 25 m).
# Hochkant wie im PDF, Start in der unteren Hälfte, Ausbruch nach oben. Feld x 25-75, y 5-55: in der Breite gestreckt
# (14 m auf 50 Einheiten), damit neun Spieler in einer Hälfte den 3D-Abstand halten (wie UE-299).
# PDF blau -> Team Neon (6, 8, 10), pink -> Team Rot (3, 4, 5), gelb -> vier Springer (F). Ein Trainer statt zwei.
# Passfolge an die Tafel angepasst: Im PDF sind vier Pässe eingezeichnet, hier werden die fünf Pässe ausgespielt
# (Start bei Spieler zehn), danach wie im PDF der lange Pass von rechts außen zum Springer oben und die Ablage.
# Kein Dublette zu UE-189 (dort drei Zonen, vier gegen vier, zwei Tore, kein Passzählen).
# Sichtkegel: Text/Ton KCP 2 „stay aware of the pass to the end player“, im Video ein Kegel eingezeichnet:
# Spieler zehn schaut vor dem fünften Pass hoch zum Springer oben.
T = P("T", "c", 12, 12, "T")
ERSATZ = [B("s1", 15.6, 15.5), B("s2", 12, 15.5)]
POS = {"n6": (35.5, 48.5), "n8": (61, 30), "n10": (69.5, 42), "r3": (44, 40), "r4": (52.5, 38), "r5": (61, 45.5),
       "f1": (50, 6.5), "f2": (52.5, 54), "f3": (35.5, 32), "f4": (27, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
TORE = [{"x": 37.5, "y": 5, "side": "top"}, {"x": 62.5, "y": 5, "side": "top"}, {"x": 37.5, "y": 55, "side": "bottom"}, {"x": 62.5, "y": 55, "side": "bottom"}]
CONES = ecken(25, 5, 50, 50) + [C(25, 30), C(75, 30)]
DIMS = dims(25, 75, 5, 55, "14 m", "25 m", rx=88)
HOCH = [58, 20]   # Blickziel von Spieler zehn: Richtung Springer oben
def nachruecken(delay=0.3):
    return [mv("n8", [61, 17], delay=delay), mv("n6", [30.5, 38], delay=delay), mv("n6", [36, 19], after=True), mv("r4", [51, 24], delay=delay + 0.4),
            mv("r3", [43, 28], delay=delay + 0.4), mv("r5", [66, 31], delay=delay + 0.5)]

u = {"title": "Fünf Pässe, dann Ausbruch", "code": "UE-316", "kind": "Spielform",
 "focuses": ["Passspiel", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "14 x 25 m",
 "description": "Drei gegen drei in einer Hälfte, dazu helfen drei Springer dem Team am Ball. Nach fünf Pässen in Folge darf der Ball zum vierten Springer am anderen Ende. Die Angreifer laufen sofort nach, bekommen die Ablage und schießen auf die Minitore. Fängt das andere Team einen Pass ab, schießt es gleich auf die Minitore in dieser Hälfte.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 25 Metern, in der Mitte quer geteilt. Auf jeder Grundlinie stehen zwei Minitore.",
  "Verteilen: Team Neon und Team Rot spielen zu dritt in der unteren Hälfte. Zwei Springer spielen dort mit, je ein Springer steht zwischen den Minitoren oben und unten. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Team Neon hält den Ball mit den drei Springern in der Hälfte. Nach fünf Pässen in Folge geht der Ball zum Springer am anderen Ende. Team Neon läuft nach, bekommt die Ablage und schießt dort auf die Minitore. Team Rot läuft mit zurück und verteidigt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Fängt Team Rot den Ball ab, schießt es sofort auf die Minitore in dieser Hälfte. Weiter geht es in der Hälfte, in der die Aktion endet. Die Rollen wechseln nach festen Zeiten oder nach jedem abgefangenen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Schräg anbieten, nie hinter dem Gegner stehen", "Mitzählen und beim fünften Pass schon hochschauen", "Mit dem langen Pass sofort loslaufen", "Als Verteidiger gleich zurück und die Tore zustellen"],
 "materials": ["4 Minitore", "6 Hütchen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Fünf Pässe, dann Ausbruch. Drei gegen drei in einer Hälfte, die Springer helfen dem Team am Ball. Nach fünf Pässen geht es raus aus der Enge und ab auf die Minitore am anderen Ende.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 70.1, 42.6)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Pass eins und zwei", "Team Neon hat den Ball in der unteren Hälfte. Spieler zehn spielt zu Spieler acht, und der direkt weiter zum Springer links. Zwei Pässe.",
     ps("b1", [61.6, 30.6]), mv("r4", [54, 35.5], delay=0.2), ps("b1", [36.1, 32.6], after=True), mv("r3", [43, 37], delay=0.9)),
   S("Pass drei und vier", "Team Rot schiebt rüber. Der Springer spielt runter zu Spieler sechs. Der passt gleich weiter zum Springer an der Grundlinie, das ist Pass Nummer vier.",
     ps("b1", [36.1, 49.1]), mv("r3", [42, 43], delay=0.2), ps("b1", [53.1, 54.6], after=True)),
   S("Der fünfte Pass, Kopf hoch", "Rechts außen ist Spieler zehn frei. Bevor der Ball kommt, schaut er hoch zum Springer am anderen Ende. Dann kommt der fünfte Pass.",
     bl("n10", HOCH), ps("b1", [70.1, 42.6], after=True)),
   S("Ausbruch zum Springer oben", "Fünf Pässe sind voll. Spieler zehn spielt lang zum Springer oben. Spieler acht und Spieler sechs laufen sofort los, Team Rot muss hinterher.",
     ps("b1", [50.6, 7.1]), *nachruecken()),
   S("Ablage und Abschluss: Punkt", "Der Springer legt ab, Spieler acht schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Der Trainer spielt den nächsten Ball oben ein. Dort zählt Team Neon wieder bis fünf.",
     ps("b1", [61.6, 17.6]), ps("b1", [62.5, 4.7], after=True), mv("n10", [70, 26], delay=0.2))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ball abgefangen, sofort abschließen.", "Abfangen und abschließen",
    "Fängt Team Rot einen Pass ab, wartet es nicht. Zwei schnelle Pässe, dann der Schuss auf ein Minitor in dieser Hälfte. Team Neon schaltet um und stellt die Tore zu.",
    sp(), [B("b1", 70.1, 42.6)] + ERSATZ,
    [S("Spieler drei fängt den Pass ab", "Spieler acht will quer zum Springer spielen. Spieler drei ahnt das, geht dazwischen und hat den Ball.",
       ps("b1", [61.6, 30.6]), mv("r3", [45, 33], delay=0.5), ps("b1", [45.6, 33.6], after=True)),
     S("Zwei Pässe, Schuss: Punkt", "Jetzt geht es schnell. Spieler drei spielt zu Spieler vier, der steckt durch auf Spieler fünf. Schuss ins linke Minitor, und das gibt einen Punkt für Team Rot.",
       ps("b1", [53.1, 38.6]), mv("r5", [46, 47], delay=0.2), ps("b1", [46.6, 47.6], after=True), ps("b1", [38, 55.3], after=True),
       mv("n8", [56, 40], delay=0.6))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Springer oben im Blick haben und früh loslaufen.", "Früh schauen, früh starten",
    "Wer den fünften Pass bekommt, weiß schon vorher, wo der Springer am anderen Ende steht. Die anderen beiden starten mit dem langen Pass und laufen in zwei verschiedene Bahnen. So hat der Springer zwei Möglichkeiten für die Ablage.",
    sp(), [B("b1", 53.1, 54.6)] + ERSATZ,
    [S("Erst schauen, dann der Ball", "Vier Pässe sind gespielt, der Ball ist beim Springer unten. Spieler zehn schaut hoch und sieht den Springer oben. Jetzt erst kommt der Pass zu ihm.",
       bl("n10", HOCH), ps("b1", [70.1, 42.6], after=True)),
     S("Mit dem Pass loslaufen", "Der lange Ball ist unterwegs. Spieler acht startet rechts, Spieler sechs links. Beide sind vor Team Rot in der oberen Hälfte.",
       ps("b1", [50.6, 7.1]), *nachruecken(delay=0.1)),
     S("Ablage nach links: Punkt", "Diesmal legt der Springer nach links ab. Spieler sechs kommt mit Tempo und schießt ins linke Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [36.6, 19.6]), ps("b1", [37.5, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
