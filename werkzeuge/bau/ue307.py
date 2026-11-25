import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 69-P5 (U15-U17, Woche 12): Compact Midfield to Stop Forward Passes. 16 x 32 Yards = 15 x 29 m (gerundet 15 x 30 m).
# FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Das lange Feld liegt quer und füllt die Tafel, x 9-89 (30 m), y 5-50 (15 m).
# Im PDF hochkant; R() legt die Hochkant-Planung (Feld x 20-80 = Breite, y 5-55 = Länge) quer: unten -> links, oben -> rechts,
# links -> oben, rechts -> unten (eine Drehung, darum bleiben bend und drehen(gegen=...) wie sie sind). Die Mittelzone
# (5 Yards) liegt jetzt senkrecht in der Mitte (x 42,7-55,3), mit vier Minitoren, je zwei pro Hälfte, Rücken an Rücken.
# PDF blau -> Team Neon: außen in der linken Hälfte 5, 2, 3, Dreierkette in der rechten Hälfte 6, 10, 8. PDF pink -> Team Rot,
# neu nummeriert, weil 5, 6, 3, 10 und 8 doppelt wären: außen rechts 7 (PDF 5), 4, 9 (PDF 6), Dreierkette links 11 (PDF 10),
# 12 (PDF 3), 13 (PDF 8). Ein Trainer statt zwei, unten an der Seitenlinie in Höhe der Mittelzone.
# Die Tafel zeigt den Ablauf in der linken Hälfte, in der rechten läuft gleichzeitig dasselbe mit.
# 3D-Abstand quer: Die Dreierkette stand hochkant nebeneinander und steht jetzt in der Tiefe hintereinander. Darum steht der
# mittlere Spieler der Kette etwas weiter vorn (Richtung Ball), die beiden äußeren vor ihren Minitoren; der Springer steht
# zwischen Spieler drei und der Kette. Die rechte Hälfte ist das Spiegelbild der linken.
# Steigerung eins nach PDF Progression 1 (Ballverlust = sofort den Weg zum Minitor zustellen), Steigerung zwei nach Progression 2
# (ein Springer in der Mittelzone verlagert auf die andere Seite). Im Original werden die Minitore dort entfernt; eine Fassung
# kann Tore nicht ausblenden (leere goals-Liste zeigt die der Grundform), darum bleiben sie stehen und der Text sagt, dass sie nicht zählen.
# Sichtkegel: In Steigerung zwei schaut der Springer in der Mittelzone zum Springer mit dem Ball, nimmt an und dreht auf
# (Kegel mit von + Drehpfeil). Der frühere Kegel von Spieler fünf nach dem Ballverlust (Progression 1 „defensive awareness“)
# ist gestrichen: Er spielt danach nicht selbst (Regel des Inhabers, 25.11.2026).
FX0, FX1, FY0, FY1 = 9, 89, 5, 50
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 20) / 60 * (FY1 - FY0), 1)]
def Q(x, y): return [round(20 + (y - FY0) / (FY1 - FY0) * 60, 2), round(55 - (x - FX0) / (FX1 - FX0) * 50, 2)]  # quer -> hochkant
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def C(x, y, *a, **k): return h.C(*R(x, y), *a, **k)
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 49, 55.3, "T")  # unten an der Seitenlinie, in Höhe der Mittelzone
ERSATZ = [h.B("s1", 52.5, 55.8), h.B("s2", 55, 55.8)]
# Positionen quer geplant (Tafel-Koordinaten) und mit Q() in die Hochkant-Planung zurückgerechnet, die R() wieder quer legt
QPOS = {"n5": (23.5, 5), "n2": (23.5, 50), "n3": (9.8, 27.5), "r11": (36, 15), "r12": (27.5, 27.5), "r13": (36, 40),
        "r7": (74.5, 5), "r4": (74.5, 50), "r9": (88.2, 27.5), "n6": (62, 15), "n10": (70.5, 27.5), "n8": (62, 40)}
POS = {i: tuple(Q(*p)) for i, p in QPOS.items()}
F1, F2 = tuple(Q(18.4, 22)), tuple(Q(79.6, 22))
def sp(f1=F1, f2=F2, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("f1", "t", *f1, "F"), P("f2", "t", *f2, "F"), T]
def b(i, d=POS): x, y = R(*d[i]); return Q(x + 0.6, y + 0.6)  # Ball am Fuß: quer Spieler + 0,6
def q(x, y): return Q(x, y)  # Ziel quer angeben
LINES = [h.rect(FX0, FY0, FX1 - FX0, FY1 - FY0), h.line(42.7, FY0, 42.7, FY1), h.line(55.3, FY0, 55.3, FY1)]
TORE = [{"x": 42.7, "y": 13.5, "side": "right"}, {"x": 42.7, "y": 41.5, "side": "right"},
        {"x": 55.3, "y": 13.5, "side": "left"}, {"x": 55.3, "y": 41.5, "side": "left"}]
CONES = [h.C(49, FY0), h.C(49, FY1)]
DIMS = dims(FX0, FX1, FY0, FY1, "30 m", "15 m", rx=95)
# Stand nach dem Schieben zur Seite von Spieler fünf (Ball bei Spieler fünf), quer
QLINKS = {"r11": (36, 10.5), "r12": (27.5, 21), "r13": (36, 33)}
LINKS = {i: tuple(Q(*p)) for i, p in QLINKS.items()}

u = {"title": "Zu dritt den Steilpass zustellen", "code": "UE-307", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "15 x 30 m",
 "description": "Ein Rondo vier gegen drei in zwei Hälften gleichzeitig. Außen lassen drei Spieler mit einem Springer den Ball laufen und suchen den Pass in eins der zwei Minitore hinter der Dreierkette. Die drei in der Mitte bleiben eng zusammen, schieben mit dem Ball und stellen die Passwege zu. Fangen sie den Ball ab, dribbeln sie aus dem Feld, und das gibt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 15 mal 30 Metern mit einer Mittelzone von fünf Metern. In der Mittelzone stehen vier Minitore, zwei zeigen in die eine Hälfte und zwei in die andere. Zwei Hütchen markieren die Zone.",
  "Verteilen: Zwei Teams zu sechst und zwei Springer. In jeder Hälfte stehen drei Spieler eines Teams außen, drei vom anderen Team verteidigen innen vor den Minitoren. Je ein Springer hilft den Außenspielern. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Die Außenspieler passen sich mit dem Springer den Ball zu und suchen die Lücke zum Minitor. Die Dreierkette schiebt mit, einer greift an, die anderen sichern. Bei Ballgewinn dribbelt die Kette sofort über eine Außenlinie aus dem Feld. Beide Hälften spielen gleichzeitig.",
  "Wertung und Wechsel: Ein Pass ins Minitor gibt einen Punkt für die Außenspieler. Dribbelt die Dreierkette nach Ballgewinn aus dem Feld, gibt das einen Punkt für ihr Team. Nach jeder Runde werden die Punkte gezählt, dann tauschen innen und außen."],
 "organisation_show": ORG,
 "coaching_points": ["Einer greift an, zwei sichern dahinter", "Eng bleiben und laut reden", "Schlechter erster Kontakt? Sofort drauf!", "Ball gewonnen, dann mit Tempo raus aus dem Feld"],
 "materials": ["4 Minitore", "2 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zu dritt den Steilpass zustellen. Ein Rondo vier gegen drei, in beiden Hälften gleichzeitig. Drei Mittelfeldspieler bleiben eng zusammen und lassen keinen Pass nach vorn durch.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(),
  "balls": [B("b1", *b("n3")), B("b2", *b("r9"))] + ERSATZ,
  "steps": [
   S("Ball nach außen, die Kette schiebt", "In der einen Hälfte spielt Spieler drei zur Seite zu Spieler fünf. Die drei von Team Rot schieben sofort mit rüber. In der anderen Hälfte läuft das Gleiche, dort verteidigt Team Neon.",
     ps("b1", b("n5")), *[mv(i, list(p), delay=0.2) for i, p in LINKS.items()],
     ps("b2", b("r7")), mv("n6", q(62, 10.5), delay=0.2), mv("n10", q(70.5, 21), delay=0.2), mv("n8", q(62, 33), delay=0.2)),
   S("Der Springer kommt entgegen", "Spieler fünf findet außen keinen Weg nach vorn und spielt zum Springer. Spieler zwölf rückt raus auf den Ball. Spieler elf lässt sich fallen und steht jetzt genau vor dem nahen Minitor.",
     mv("f1", q(21, 16)), ps("b1", q(21.6, 16.6)), mv("r12", q(25, 20.5), delay=0.2), mv("r11", q(38, 13.5), delay=0.2), mv("r13", q(34, 28), delay=0.2),
     ps("b2", b("r9"), delay=0.3), mv("n6", q(62, 15.5), delay=0.5), mv("n10", q(68, 27.5), delay=0.5), mv("n8", q(62, 39), delay=0.5)),
   S("Der Weg nach vorn ist zu", "Der Springer versucht es trotzdem flach aufs nahe Minitor. Spieler elf steht im Passweg und fängt den Ball ab.",
     ps("b1", q(38.6, 14.1)), ps("b2", Q(*[c + 0.6 for c in R(*F2)]), delay=0.2)),
   S("Raus aus dem Feld: Punkt", "Jetzt geht es schnell. Spieler elf dribbelt über die Außenlinie aus dem Feld, und das gibt einen Punkt für Team Rot. Der Trainer spielt den nächsten Ball zu Spieler drei, und Team Neon greift wieder an.",
     dr("r11", "b1", q(37, 2.5)), mv("n5", q(29, 8), delay=0.3), mv("f1", q(26, 12), delay=0.3),
     ps("b2", b("r4"), delay=0.2), mv("n8", q(63, 45), delay=0.4), mv("n10", q(68, 36), delay=0.4), mv("n6", q(62, 24), delay=0.4))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball verliert, setzt sofort nach.", "Nach Ballverlust nachsetzen",
    "Die Dreierkette darf nach dem Ballgewinn jetzt auch in ein Minitor ihrer Hälfte treffen. Die Außenspieler laufen sofort nach innen und stellen den Weg zum Minitor zu. Holen sie den Ball zurück, greifen sie weiter an. Trifft die Kette, gibt das einen Punkt, und innen und außen tauschen.",
    sp(**LINKS), [B("b1", *b("n5")), B("b2", *b("r9"))] + ERSATZ,
    [S("Ball weg, sofort umschalten", "Spieler fünf will zum Springer spielen, aber Spieler zwölf geht dazwischen und hat den Ball. Jetzt will Spieler zwölf ins nahe Minitor.",
       mv("r12", q(22, 14)), ps("b1", q(22.6, 14.6))),
     S("Weg zum Minitor zustellen", "Spieler fünf sprintet nach innen und stellt sich vor das Minitor. Von hinten kommt Spieler drei dazu und nimmt Spieler zwölf den Ball wieder ab. Team Neon bleibt außen und greift weiter an.",
       mv("n5", q(30, 9.5)), mv("n5", q(35, 16.5), after=True), dr("r12", "b1", q(28, 15.5), delay=0.3), mv("n3", q(19, 28.5), delay=0.4), mv("n3", q(26.5, 18.5), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Minitore zählen nicht mehr, dafür wird verlagert.", "Verlagern über die Mitte",
    "Die Minitore zählen nicht mehr, am besten räumt man sie weg. Ein Springer steht jetzt in der Mittelzone. Bekommt er den Ball, dreht er auf und spielt in die andere Hälfte, dort geht es weiter. Die Dreierkette will genau diesen Pass durch die Mitte verhindern.",
    sp(f2=tuple(Q(49, 27.5)), n6=tuple(Q(61.5, 8.5))), [B("b1", *b("n3"))] + ERSATZ,
    [S("Erst zur Seite locken", "Team Neon spielt wieder zur Seite zu Spieler fünf, und die Kette von Team Rot schiebt mit. Der Springer in dieser Hälfte bietet sich an und bekommt den Ball.",
       ps("b1", b("n5")), *[mv(i, list(p), delay=0.2) for i, p in LINKS.items()], mv("f1", q(19, 30), delay=0.6), ps("b1", q(19.6, 30.6), after=True)),
     S("Durch die Lücke in die Mitte", "Zwischen Spieler zwölf und Spieler dreizehn ist die Lücke zu groß. Der Springer in der Mittelzone schaut zum Ball, und der Pass kommt flach durch.",
       bl("f2", q(19, 30)), ps("b1", q(49.6, 28.1), after=True)),
     S("Aufdrehen und verlagern", "Der Springer dreht auf und spielt in die andere Hälfte zu Spieler sieben. Dort läuft das Spiel jetzt weiter, und Team Neon muss verschieben.",
       bl("f2", q(64, 14.3), von=q(19, 30), dauer=1.3), drehen("f2", q(74.5, 5), delay=0.4), ps("b1", b("r7"), after=True),
       mv("n6", q(66, 8), delay=1.6), mv("n10", q(71, 18), delay=1.6), mv("n8", q(63, 32), delay=1.6))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
