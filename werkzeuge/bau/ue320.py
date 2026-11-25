import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 78-P4 (U15-U17, Woche 16): The Compact Back 4 Unit. 24 x 30 Yards = 22 x 27 m, gerundet 20 x 25 m.
# FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Die lange Seite (25 m) liegt waagrecht, Feld x 14-84, y 4-51 (Maßstab
# 2,8 zu 2,35 Einheiten je Meter: fast gleich, so groß wie möglich). Drei Zonen nebeneinander, die Kette in der Mittelzone,
# je zwei Angreifer links und rechts davon; die Minitore der Steigerungen an den kurzen Seiten links und rechts.
# Geplant im Hochformat wie im PDF (x 27-73, y 5-55, Zonenlinien bei y 22 und 38); R() legt jede Koordinate quer:
# unten -> links, oben -> rechts, links -> oben, rechts -> unten. Bälle am Fuß bleiben mit Rb() genau bei Spieler + 0.6.
# Pink (Kette 3, 4, 5, 2) -> Team Neon. Blau (3, 4 oben, 5, 2 unten) -> Team Rot, neu nummeriert 7, 8 und 9, 10
# (Nummern waren doppelt). Ein Trainer statt zwei, quer unten an der Seitenlinie.
# Quer steht die Kette in der Tiefe hintereinander: Spieler drei und Spieler fünf etwas weiter rechts, Spieler vier und
# Spieler zwei etwas weiter links (leicht gestaffelt, 3D-Abstand). Texte ohne oben/unten/links/rechts, wo es geht.
# Maßlinien: Grundform ohne Tore mit Länge und Breite, in den Fassungen (Minitore rechts) nur die Länge unten.
# Fassungen wie im PDF: Progression 1 (Minitore, Konter vier gegen zwei, laut Ton zwei Punkte) und Progression 2
# (Außenverteidiger darf bei der Verlagerung aus der Zone pressen).
# Sichtkegel: im Video keiner eingezeichnet. Aus Video-Einblendung "Recognise the switch to press, FB awareness to press"
# und Ton "improving their ability to read the game": in der zweiten Steigerung schaut Spieler neun vor dem Querpass zu Spieler zehn
# (Regel des Inhabers, 25.11.2026: Kegel nur beim Passgeber; früher bei Spieler zwei, der die Verlagerung liest).
# Kein Dubletten-Fall: UE-166, UE-177, UE-250 (Tor mit Torwart), UE-212 (drei Minitore, vier gegen vier), UE-242 (vier gegen
# vier zwischen zwei Springern), UE-203 und UE-208 geprüft, überall andere Organisation.
FX0, FX1, FY0, FY1 = 14, 84, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 27) / 46 * (FY1 - FY0), 1)]
def Rb(x, y):  # Ball: Punkt am Fuß (Spieler + 0.6) bleibt quer am Fuß
    p = R(x - 0.6, y - 0.6); return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *Rb(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, Rb(*to), **k)
def schuss(ball, to, **k): return h.ps(ball, R(*to), **k)  # Schuss ins Tor: ohne Fuß-Versatz
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 60, 55.3, "T")  # unten an der Seitenlinie (quer gesetzt)
ERSATZ = [h.B("s1", 63.5, 55.8), h.B("s2", 66, 55.8)]
KA, KB = 27, 33   # Staffelung der Kette in der Länge: Spieler drei und fünf auf KA, Spieler vier und zwei auf KB
POS = {"n3": (35, KA), "n4": (45, KB), "n5": (55, KA), "n2": (65, KB),
       "r7": (37, 13), "r8": (63, 13), "r9": (40, 47), "r10": (60, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def kette(x3, x4, x5, x2, ya=KA, yb=KB, **k):
    return [mv("n3", [x3, ya], **k), mv("n4", [x4, yb], **k), mv("n5", [x5, ya], **k), mv("n2", [x2, yb], **k)]
Z1, Z2 = R(27, 38)[0], R(27, 22)[0]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), h.line(Z1, FY0, Z1, FY1), h.line(Z2, FY0, Z2, FY1)]
TORE = [{"x": FX1, "y": R(35, 5)[1], "side": "right"}, {"x": FX1, "y": R(65, 5)[1], "side": "right"},
        {"x": FX0, "y": R(35, 55)[1], "side": "left"}, {"x": FX0, "y": R(65, 55)[1], "side": "left"}]
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "20 m", rx=FX1 + 8)
DIMS_V = DIMS[:1]   # mit Minitoren rechts nur die Länge unten

u = {"title": "Viererkette in der Mittelzone", "code": "UE-320", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 8,
 "field_size": "20 x 25 m",
 "description": "Eine Viererkette steht in der Mittelzone und macht die Wege zu. Auf beiden Seiten stehen je zwei Angreifer, die den Ball durch die Kette auf die andere Seite spielen wollen. Jeder Pass durch die Kette gibt einen Punkt für die Angreifer, jeder abgefangene Ball einen Punkt für die Kette. Die vier schieben gemeinsam zum Ball und halten die Abstände eng.",
 "organisation": ["Aufbauen: Ein Feld von 20 mal 25 Metern, in drei Zonen geteilt. Die Mittelzone ist etwas schmaler als die beiden Außenzonen.",
  "Verteilen: Team Neon steht als Viererkette in der Mittelzone. Von Team Rot stehen je zwei Spieler in den beiden äußeren Zonen. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Team Rot lässt den Ball in seiner Zone laufen und sucht die Lücke. Der Pass soll durch die Kette zu den Mitspielern auf der anderen Seite. Team Neon bleibt in der Mittelzone, schiebt zum Ball und fängt die Pässe ab.",
  "Wertung und Wechsel: Ein Pass durch die Kette gibt einen Punkt für Team Rot. Ein abgefangener Ball gibt einen Punkt für Team Neon. Nach jeder Runde von zwei bis drei Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Eng bleiben, keine Lücke in der Kette", "Alle vier schieben zusammen zum Ball", "Seitlich stehen, dann bist du schneller am Pass", "Redet miteinander: schieben, halten, raus"],
 "materials": ["Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben", "4 Minitore für die Steigerung"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette in der Mittelzone. Vier Verteidiger stehen in der Mitte und lassen keinen Ball durch. Die Angreifer auf beiden Seiten suchen die Lücke.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": [B("b1", 63.6, 13.6)] + ERSATZ,
  "steps": [
   S("Ball läuft quer, Kette schiebt", "Team Rot hat den Ball. Spieler acht spielt quer zu Spieler sieben. Die Kette von Team Neon schiebt sofort mit zum Ball, alle vier zusammen.",
     ps("b1", [37.6, 13.6]), *kette(30, 39.5, 49, 58.5, delay=0.2)),
   S("Kein Weg durch, der Ball geht zurück", "Spieler sieben findet keine Lücke. Also geht der Ball zurück zu Spieler acht. Jetzt muss die Kette schnell rüber. Spieler zwei schiebt weit raus, aber Spieler fünf kommt zu spät nach.",
     ps("b1", [63.6, 13.6]), mv("n2", [70.5, KB], delay=0.2), mv("n5", [53.5, KA], delay=0.5), mv("n4", [44.5, KB], delay=0.5), mv("n3", [35.5, KA], delay=0.5)),
   S("Durch die Lücke: Punkt", "Zwischen Spieler fünf und Spieler zwei ist die Lücke offen. Spieler acht spielt flach durch zu Spieler zehn, und das gibt einen Punkt für Team Rot.",
     ps("b1", [60.6, 47.6])),
   S("Andere Seite, Kette dreht sich um", "Es geht direkt weiter. Die Kette dreht sich zum Ball. Auf der anderen Seite spielt Spieler zehn quer zu Spieler neun, und diesmal schieben alle vier eng zusammen rüber.",
     ps("b1", [40.6, 47.6]), *kette(31, 40.5, 50, 59.5, delay=0.2)),
   S("Abgefangen: Punkt", "Spieler neun versucht es trotzdem durch die Mitte. Spieler vier steht seitlich, macht einen Schritt in den Passweg und fängt den Ball ab, und das gibt einen Punkt für Team Neon. Der Trainer spielt den nächsten Ball zu Team Rot. Nach der Runde tauschen die Teams.",
     ps("b1", [39.3, 33.4]), mv("n4", [38.7, 32.8], delay=0.2))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Vier Minitore, und die Kette darf kontern.", "Konter auf die Minitore",
    "An jeder Grundlinie stehen jetzt zwei Minitore. Fängt die Kette den Ball ab, greift sie zu viert gegen die zwei Angreifer an, von denen der Pass kam. Ein Treffer ins Minitor gibt zwei Punkte. Verliert die Kette den Ball, geht sie zurück in die Mittelzone.",
    sp(n3=(30, KA), n4=(39.5, KB), n5=(49, KA), n2=(58.5, KB)), [B("b1", 37.6, 13.6)] + ERSATZ,
    [S("Pass abgefangen", "Spieler sieben hat den Ball und will steil durch die Kette spielen. Spieler vier ahnt den Pass und geht dazwischen.",
       ps("b1", [39.4, 30.1]), mv("n4", [38.8, 29.5], delay=0.2)),
     S("Sofort zu viert nach vorn", "Jetzt schaltet Team Neon um. Spieler vier dribbelt nach vorn in die Zone von Spieler sieben, und der muss ihn stellen. Außen läuft Spieler drei mit, auf der anderen Seite kommen Spieler fünf und Spieler zwei nach.",
       dr("n4", "b1", [43, 21]), mv("r7", [40.5, 15.5], delay=0.3), mv("n3", [30, 15], delay=0.2), mv("n5", [53, 22], delay=0.3), mv("n2", [64, 20], delay=0.3), mv("r8", [58, 12], delay=0.4)),
     S("Querpass, Minitor: zwei Punkte", "Spieler vier legt quer auf Spieler drei. Der schiebt den Ball ins Minitor vor ihm, und das gibt zwei Punkte für Team Neon.",
       ps("b1", [30.6, 15.6]), schuss("b1", [34, 4.7], after=True))],
    goals=TORE, dims=DIMS_V),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Außenverteidiger darf raus.", "Außenverteidiger rückt raus",
    "Verlagern die Angreifer den Ball auf die andere Seite, darf der Außenverteidiger dort die Mittelzone verlassen und pressen. Er muss erkennen, wann er rechtzeitig ankommt. Kommt er zu spät, ist hinter ihm die Lücke offen. Die drei anderen schieben deshalb sofort nach.",
    sp(n3=(31, KA), n4=(40.5, KB), n5=(50, KA), n2=(59.5, KB)), [B("b1", 40.6, 47.6)] + ERSATZ,
    [S("Verlagerung erkennen, raus", "Jetzt hat Spieler neun den Ball, die Kette steht auf seiner Seite. Er schaut zu Spieler zehn und spielt quer. Spieler zwei erkennt die Verlagerung. Der Ball ist noch unterwegs, da läuft er schon los.",
       bl("r9", [60, 47]), ps("b1", [60.6, 47.6], after=True), mv("n2", [62, 41], delay=1.2),
       mv("n5", [56, KA], delay=1.4), mv("n4", [47, KB], delay=1.4), mv("n3", [38, KA], delay=1.4)),
     S("Pass geblockt, Ball erobert", "Spieler zehn will sofort durch die Kette spielen. Spieler zwei steht schon vor ihm und blockt den Pass. Der Ball gehört Team Neon.",
       ps("b1", [62.6, 41.6])),
     S("Aufs nächste Minitor: zwei Punkte", "Spieler zwei geht mit dem Ball außen an Spieler zehn vorbei und trifft ins nähere Minitor, und das gibt zwei Punkte für Team Neon.",
       dr("n2", "b1", [68, 49]), schuss("b1", [65.5, 55.3], after=True), mv("n5", [55, 41], delay=0.3))],
    goals=TORE, dims=DIMS_V)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
