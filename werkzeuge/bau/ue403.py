import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 43-P8 (U15-U17, Woche 37 Phase 1): Playing Through the Thirds (Wave of Play / Small Sided Game). 25 x 35 Yards = 23 x 32 m
# (gerundet 25 x 30 m). Sechs gegen sechs mit Torhütern (je 2-2-1) und einem Springer in der Mittelzone.
# LANGES FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51), große Tore
# links und rechts (Großfeldtore, nur C- und B-Jugend), Zonengrenzen gestrichelt. Team Neon baut links auf und greift nach rechts an
# (im Video greift Gelb ebenfalls quer an, im PDF Blau nach unten). Geplant im Hochformat (x 25-75 Breite, y 5-55 Länge, Angriff
# nach oben, Zonengrenzen bei y 21.5 und y 38.5); R() legt jede Koordinate quer: unten -> links, oben -> rechts.
# PDF blau (Video gelb) -> Team Neon mit den Nummern aus dem PDF (4, 5, 8, 10, 9). PDF pink (Video rot) -> Team Rot, neu
# nummeriert, weil die Nummern doppelt sind: 4 -> 2, 5 -> 3, 6 -> 6, 8 -> 7, 9 -> 11. Beide Torhüter neutral (k1 links für
# Team Neon, k2 rechts für Team Rot), weil zweimal TW als doppelte Nummer gilt (wie ue317, ue358). Springer F neutral.
# Ein Trainer statt zwei, unten an der Seitenlinie. Positionen gegenüber dem PDF leicht versetzt (3D-Abstand bei 14 Figuren).
# Grundform nach PDF und Video (1:20-1:50): Torwart -> 4 (beginnt den Angriff), Pass in die Mitte auf 10, 4 rückt in die Mitte
# nach (vier gegen zwei), 10 -> Springer, Springer dreht auf -> 9 in der Angriffszone, 10 läuft als Unterstützung mit (zwei gegen zwei),
# Ablage, Abschluss. Im PDF startet 4 rechts und 10 kommt von rechts; hier links (Seiten gespiegelt, damit die Wege frei bleiben).
# Fassungen: PDF Key Coaching Point 1 (Paar eng: außen herum) und Key Coaching Point 2 (Laufweg ohne Ball zieht den Gegner weg,
# im PDF/Video der Springer, der Verteidiger 5 spielt durch die Lücke auf 9).
# Sichtkegel: Text KCP 1 "attackers must recognise the space outside", "Decision making when to progress play"; im Video nicht
# eingezeichnet. Richtung aus dem Sinn: Spieler acht schaut vor dem Pass außen die Linie entlang. Der Springer und Spieler neun
# nehmen an und drehen auf (bl mit von + drehen, Vorbild ue300).
# Kein Dublette: UE-358 (36-P10, 7 gegen 7, 3-2-1, nachrückender Verteidiger, drei gegen zwei vorn) ist ähnlich, hat aber keinen
# Springer, eine andere Aufstellung (2-2-1 hier), keine Pflicht über den Springer und vorn zwei gegen zwei.
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 25) / 50 * (FY1 - FY0), 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 67.5, 55.3, "T")  # unten an der Seitenlinie (3D-Abstand)
ERSATZ = [h.B("s1", 71, 55.8), h.B("s2", 73.5, 55.8)]
POS = {"k1": (50, 53), "n5": (68, 47.5), "n4": (32, 41.5), "r11": (50, 47),
       "n10": (32, 31), "f": (50, 32), "n8": (67, 37.5), "r6": (36, 25), "r7": (61, 24.5),
       "n9": (50, 19), "r2": (33, 13), "r3": (67, 13), "k2": (50, 6.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    def lab(i): return "TW" if i[0] == "k" else ("F" if i == "f" else i[1:])
    return [P(i, {"n": "a", "r": "b", "k": "t", "f": "t"}[i[0]], x, y, lab(i)) for i, (x, y) in d.items()] + [T]
def fuss(i, d=None):
    x, y = (d or POS)[i]
    return [x + 0.6 * 50 / 47, y - 0.6 * 50 / 80]  # nach R() genau Spieler + 0,6
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
Z1, Z2 = R(0, 38.5)[0], R(0, 21.5)[0]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(Z1, FY0, Z1, FY1), line(Z2, FY0, Z2, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
CONES = [h.C(Z1, FY0), h.C(Z1, FY1), h.C(Z2, FY0), h.C(Z2, FY1)]
DIMS = dims(FX0, FX1, FY0, FY1, "30 m", "25 m")[:1]
SCHUSS, SCHUSS2 = [46, 5.2], [56, 5.2]

u = {"title": "Über den Springer nach vorn", "code": "UE-403", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "25 x 30 m",
 "description": "Sechs gegen sechs mit Torhütern und einem Springer auf einem Feld mit drei Zonen. Jedes Team steht mit zwei Verteidigern, zwei Mittelfeldspielern und einem Stürmer. Ein Verteidiger darf in die Mitte nachrücken, dann ist es dort mit dem Springer vier gegen zwei. Erst über den Springer geht es in die Angriffszone, wo ein Mittelfeldspieler mitläuft und vorn zwei gegen zwei spielt.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit einem großen Tor auf jeder Grundlinie. Zwei gestrichelte Linien teilen es in drei gleich große Zonen.",
  "Verteilen: Je Team ein Torwart, zwei Verteidiger in der eigenen Zone, zwei Mittelfeldspieler in der Mitte und ein Stürmer in der Angriffszone. Der Springer spielt in der Mittelzone immer mit dem Team am Ball. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet. Ein Verteidiger spielt nach vorn in die Mitte und darf selbst nachrücken. Bevor es in die Angriffszone geht, muss der Ball einmal über den Springer laufen. Dann darf ein Mittelfeldspieler mit nach vorn und hilft dem Stürmer.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobert das andere Team den Ball, baut es mit denselben Regeln auf. Nach einem Treffer eröffnet der Torwart auf der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Anspielbar stehen, nicht hinter dem Gegner", "Überzahl in der Mitte nutzen, dann schnell nach vorn", "Stehen sie eng, außen vorbei", "Ohne Ball weglaufen und Platz machen"],
 "materials": ["2 große Tore", "4 Hütchen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Über den Springer nach vorn. Sechs gegen sechs mit Torhütern und einem Springer. Der Ball läuft Zone für Zone nach vorn, und in der Mitte führt der Weg immer über den Springer.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *fuss("k1"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Torwart eröffnet", "Der Torwart links hat den Ball. Er spielt flach zu Spieler vier. Spieler elf läuft gleich an.",
     ps("b1", fuss("n4")), mv("r11", [42, 45], delay=0.4)),
   S("In die Mitte, Spieler vier rückt nach", "Spieler vier spielt nach vorn zu Spieler zehn und geht sofort hinterher. Jetzt ist es in der Mitte vier gegen zwei.",
     ps("b1", fuss("n10")), mv("n4", [40, 37.5], delay=0.4)),
   S("Erst über den Springer", "Ohne den Springer geht es nicht weiter. Er schaut zum Ball, und Spieler zehn spielt ihn flach an.",
     bl("f", [38, 31.5]), ps("b1", fuss("f"), after=True)),
   S("Aufdrehen, in die Spitze", "Der Springer nimmt an, dreht auf und spielt in die Angriffszone auf Spieler neun. Spieler zehn läuft sofort mit nach vorn. Vorn sind es jetzt zwei gegen zwei.",
     bl("f", [50, 21], von=[38, 31.5], dauer=1.3), drehen("f", [50, 21], delay=0.4), ps("b1", fuss("n9"), after=True),
     mv("n10", [29, 24], delay=0.3), mv("n10", [37, 16.5], after=True)),
   S("Ablage und Abschluss: Punkt", "Spieler neun legt ab auf Spieler zehn. Der schießt direkt ins Eck, und das gibt einen Punkt für Team Neon. Danach eröffnet der Torwart rechts, und Team Rot baut genauso auf.",
     ps("b1", fuss("n10", {"n10": (37, 16.5)})), mv("r2", [35, 14], delay=0.2), ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Stehen sie eng, außen vorbei.", "Stehen sie eng, außen vorbei",
    "Stehen die beiden Mittelfeldspieler von Team Rot eng in der Mitte, ist durch die Mitte kein Durchkommen. Dann ist außen Platz. Der Springer spielt schnell raus, und von dort geht der Ball die Linie entlang nach vorn.",
    sp(r6=(42, 28), r7=(58, 22.5), f=(46, 35), n8=(72, 30), n10=(28, 36), n4=(32, 44), n9=(52, 15.5), r3=(70, 12)),
    [B("b1", *fuss("f", {"f": (46, 35)}))] + ERSATZ,
    [S("Die Mitte ist zu", "Der Springer hat den Ball. Spieler sechs und Spieler sieben stehen eng zusammen, durch die Mitte geht nichts. Also spielt er raus zu Spieler acht.",
       ps("b1", fuss("n8", {"n8": (72, 30)}))),
     S("Außen die Linie entlang", "Spieler acht schaut die Linie entlang. Spieler neun startet nach außen in den freien Raum, und der Ball kommt genau in seinen Lauf.",
       bl("n8", [68, 18]), mv("n9", [68, 18], delay=0.3), ps("b1", fuss("n9", {"n9": (68, 18)}), after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ohne Ball weglaufen und Platz machen.", "Weglaufen, Platz machen",
    "Ein Laufweg ohne Ball zieht den Gegenspieler mit. Läuft der Springer weg und sein Gegner geht mit, ist die Lücke zur Spitze offen. Der Verteidiger in der Mitte sieht das und spielt sofort durch.",
    sp(n5=(48, 36), f=(40, 30), n10=(26, 36), n8=(74, 31), r6=(52, 24.5), r7=(69, 25), n9=(54, 18.5)),
    [B("b1", *fuss("n5", {"n5": (48, 36)}))] + ERSATZ,
    [S("Der Springer zieht weg", "Spieler fünf ist mit Ball in die Mitte nachgerückt. Der Springer läuft zur Seite weg, und Spieler sechs geht mit ihm mit. Jetzt ist die Lücke zur Spitze offen.",
       mv("f", [31, 25]), mv("r6", [40, 23], delay=0.3)),
     S("Durch die Lücke", "Spieler neun zeigt sich und schaut zum Ball. Spieler fünf spielt flach durch die Lücke zu ihm.",
       bl("n9", [49.8, 30.8]), ps("b1", fuss("n9", {"n9": (54, 18.5)}), after=True)),
     S("Aufdrehen und Abschluss: Punkt", "Spieler neun dreht auf und schießt sofort, und das gibt einen Punkt für Team Neon.",
       bl("n9", SCHUSS2, von=[49.8, 30.8], dauer=1.3), drehen("n9", SCHUSS2, delay=0.4), ps("b1", SCHUSS2, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
