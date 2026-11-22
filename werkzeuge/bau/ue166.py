import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 03-P3 (U12-U14, Woche 12 Phase 6): Defend The Defending Third Skill (Defend as a compact four unit - 4 v 4 game). Halbe
# Platzhälfte 40 x 45 Yards = Feld x 27.8-72.2, y 5-55 (37 x 41 m), oben ein Jugendtor mit Torwart, Strafraum und Torraum nach der
# PDF-Skizze. Gestrichelte Linie bei y 47 mit zwei Minitoren (Konter der Verteidiger), die Mittellinie ist der untere Rand.
# Ausrichtung wie im PDF (Tor oben). Pink (Verteidiger + Torwart) -> Team Neon (n1 TW, 2, 3, 4, 5), dunkel (Angreifer) -> Team Rot
# (7, 9, 10, 11), Nummern wie im PDF. Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF. Trainer spielt die Bälle ein;
# im Coaching-Punkt zwei steht er als Linienrichter an der Seite (wie im PDF).
# Sichtkegel: Text "identify the right opportunities to make tackles or interceptions" -> in der Grundform bl() von Spieler vier
# zum ballführenden Spieler zehn, bevor er rausläuft und presst (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 51.5, 50.5, "T")
POS = {"n1": (50, 7.5), "n2": (33, 21), "n4": (41.5, 18), "n5": (58.5, 18), "n3": (67, 21),
       "r9": (50, 24), "r11": (30, 37), "r7": (70, 37), "r10": (42, 40)}
def sp(T=T, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 55.1, 54), B("s2", 51.5, 54)]
LINES = [rect(27.8, 5, 44.4, 50), rect(37.7, 5, 24.9, 11.9), rect(43.4, 5, 13.6, 4.4), line(27.8, 47, 72.2, 47)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 33.6, "y": 47, "side": "bottom"}, {"x": 66.4, "y": 47, "side": "bottom"}]

u = {"title": "Als Viererkette verteidigen", "code": "UE-166", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "37 x 41 m",
 "description": "Vier Angreifer spielen gegen vier Verteidiger und einen Torwart auf das große Tor. Die Verteidiger bleiben eng zusammen: Einer presst, die anderen schieben nach und sichern ab. Gemeinsam rücken sie heraus, damit die Angreifer im Abseits stehen. Erobern die Verteidiger den Ball, kontern sie schnell auf zwei Minitore.",
 "organisation": ["Aufbauen: Eine halbe Platzhälfte von 37 mal 41 Metern mit einem Jugendtor und Strafraum oben. Unten eine gestrichelte Linie mit zwei Minitoren.",
  "Verteilen: Team Neon verteidigt mit vier Spielern und einem Torwart das große Tor. Team Rot greift mit vier Spielern an. Der Trainer steht unten mit Bällen.",
  "Ablauf: Der Trainer spielt einen Ball zu Team Rot, und vier gegen vier geht es los. Team Neon presst, schiebt und hält eine Linie. Erobert Team Neon den Ball, kontert es auf die Minitore.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Rot, ein Treffer ins Minitor einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Eng zusammen als Viererkette verteidigen", "Viel reden, damit die Linie gerade bleibt", "Einer presst, die anderen schieben nach und sichern ab", "Nach dem Ballgewinn schnell auf die Minitore kontern"],
 "materials": ["1 Jugendtor", "2 Minitore", "Hütchen für Feld und Linie", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Als Viererkette verteidigen. Vier gegen vier vor dem großen Tor, und Team Neon verteidigt eng zusammen als Kette.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 52.1, 51.1)] + ERSATZ,
  "steps": [
   S("Ball zu Team Rot", "Der Trainer spielt den Ball zu Spieler zehn. Team Rot greift das große Tor an.",
     ps("b1", [42.6, 40.6])),
   S("Einer presst", "Spieler zehn dribbelt an. Spieler vier sieht das, läuft raus und presst. Gleichzeitig schieben Spieler zwei, fünf und drei nach und sichern ab. Spieler neun läuft sich frei.",
     dr("r10", "b1", [44, 32]), bl("n4", [44, 32]), mv("n4", [43.5, 26], after=True),
     mv("n2", [36, 20], delay=0.9), mv("n5", [52.5, 20], delay=0.9), mv("n3", [61, 20], delay=0.9), mv("r9", [55, 28], delay=0.9)),
   S("Abgefangen", "Spieler zehn will zu Spieler neun passen. Spieler fünf hat mitgeschoben, geht dazwischen und fängt den Ball ab.",
     ps("b1", [50.6, 30.1]), mv("n5", [50, 29.5], delay=0.1)),
   S("Konter: Punkt", "Spieler fünf dribbelt schnell nach unten und schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann spielt der Trainer den nächsten Ball zu Team Rot.",
     dr("n5", "b1", [60, 40]), ps("b1", [66.4, 46.7], after=True))],
  "dims": dims(27.8, 72.2, 5, 55, "37 m", "41 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, alle anderen schieben.", "Einer presst, alle schieben",
    "Geht ein Verteidiger raus und presst, schieben die anderen drei gleichzeitig zur Ballseite. So bleibt die Kette eng, und die Lücken für Pässe werden klein. Der Angreifer findet keinen Weg zum Tor.",
    sp(), [B("b1", 30.6, 37.6)] + ERSATZ,
    [S("Spieler zwei presst", "Spieler elf hat den Ball außen. Spieler zwei läuft raus und presst. Gleichzeitig schieben Spieler vier, fünf und drei zur Ballseite.",
       mv("n2", [31.5, 31]), mv("n4", [38, 21], delay=0.2), mv("n5", [46, 20], delay=0.2), mv("n3", [57, 21], delay=0.2)),
     S("Kein Weg nach innen", "Spieler elf findet keine Lücke und spielt zurück zu Spieler zehn. Die Kette steht weiter eng zusammen.",
       ps("b1", [42.6, 40.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Gemeinsam herausrücken.", "Gemeinsam herausrücken",
    "Der Trainer steht an der Seite wie ein Linienrichter. Die Verteidiger reden miteinander und rücken alle zusammen heraus. Wer dann hinter der Linie steht, ist im Abseits.",
    sp(T=P("T", "c", 75.5, 19, "T")), [B("b1", 42.6, 40.6), B("s1", 79.1, 22.5), B("s2", 75.5, 22.5)],
    [S("Alle raus", "Spieler zehn hat den Ball. Spieler vier ruft: Raus! Alle vier Verteidiger rücken gleichzeitig heraus, Spieler neun bleibt hinten stehen.",
       mv("n2", [33, 27]), mv("n4", [41.5, 27]), mv("n5", [58.5, 27]), mv("n3", [67, 27])),
     S("Abseits", "Spieler zehn passt zu Spieler neun. Der Trainer an der Seite hebt die Hand: Abseits! Jetzt hat Team Neon den Ball.",
       ps("b1", [50.6, 24.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
