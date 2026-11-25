import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 78-P8 (U15-U17, Woche 25 Phase 1): Build from the Back & Defending the Counter (Wave Game). „Full half of a field“: Spielfeld bis
# zur Mittellinie (in der Skizze etwa 53 Yards = 49 m tief, gerundet 50 m) und etwa 61 Yards (56 m, gerundet 55 m) breit.
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): Hälfte wie im Fernsehbild, echte Linien
# (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Abbildung mit bau/halbfeld.py, Positionen in
# Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie).
# Lage: großes Tor LINKS (Halbfeld(tor="links")). Die Übung erzählt aus Sicht der Viererkette (Team Neon), die vom eigenen Tor
# weg auf die Minitore aufbaut: so spielt Team Neon nach rechts, Team Rot kontert nach links. Gegenüber der PDF-Skizze (Tor
# unten) im Uhrzeigersinn gedreht, nicht gespiegelt (PDF links = oben).
# Die gestrichelte Linie liegt wie im PDF 40 Yards (37 m, im Text gerundet 35 m) vor dem Tor, darauf außen zwei Minitore und
# dazwischen vier Dummys (Stangen). Dahinter bis zur Mittellinie warten die Angreifer: Jetzt ist Platz, darum stehen beide
# Gruppen auf der Tafel. Ein Trainer statt zwei, unten an der Seitenlinie auf Höhe der Dummys (spielt zum Torwart und den
# Angreifern den neuen Ball). Großfeldtor (nur C- und B-Jugend).
# Pink (Viererkette) + grüner Torwart -> Team Neon (n1 TW, 2, 4, 5, 3; Spieler 3 oben, Spieler 2 unten wie nach der Drehung
# des PDF), Blau (erste Angreifergruppe 7, 9, 10, 11) -> Team Rot, Nummern wie im PDF. Gelb (zweite Gruppe 2, 8, 6, 3) -> Team
# Rot, wegen doppelter Nummern plus zehn: 2 -> 12, 8 -> 18, 6 -> 16, 3 -> 13.
# Grundform nach PDF und Video (0:13-0:28): Trainer spielt zum Torwart, Kette macht das Feld breit, Torwart -> 4 -> 5 -> 3, Spieler 3
# trifft ins Minitor; dann spielt der Trainer den Angreifern einen neuen Ball zu (im PDF nicht gezeigt, wer den Angreifern den Ball
# gibt: Annahme), vier gegen vier aufs große Tor.
# Fassungen wie die PDF-Coaching-Punkte: 1 Innenverteidiger presst, die anderen sichern ab und lenken nach außen; 2 Torwart hält und
# leitet sofort den Konter auf ein Minitor ein (Außenverteidiger startet hoch und breit, Ton 0:35).
# Sichtkegel: Text "Quick scans to check the oppositions positioning" meint die Verteidiger, die danach nicht selbst passen: nach der
# Sichtkegel-Regel (Inhaber, 25.11.2026) dafür kein Kegel (Grundform und erster Coaching-Punkt). Im zweiten Coaching-Punkt schaut
# der Torwart nach dem Fangen zum startenden Außenverteidiger und spielt ihn an (aus dem Sinn, im Video kein Kegel eingezeichnet).
# Keine Dublette: UE-166 (03-P3, vier gegen vier mit Konter auf zwei Minitore, ohne Aufbauphase), UE-177 (78-P3), UE-212 (78-P6),
# UE-242 (78-P7), UE-250 (78-P12, Springer spielen ein, drei Minitore) und UE-320 (78-P4) haben keine Aufbauphase ohne Gegner
# und keine Wellen.
F = hf.Halbfeld(tief=50, breit=55, tor="links")   # Tor links (x 10), Mittellinie rechts (x 90), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
def schau(who, p, ziel, weit=20, **k): return h.bl(who, hf.richt(X(p), X(ziel), weit), **k)
LINIE = 37                             # gestrichelte Linie mit Minitoren und Dummys (40 Yards vor dem Tor)
T = h.P("T", "c", 60, 55.3, "T")       # unten an der Seitenlinie, kurz vor der Linie mit den Dummys
ERSATZ = [h.B("s1", 63.5, 55.8), h.B("s2", 66, 55.8)]
POS = {"n1": (3, 26), "n3": (18, 8), "n5": (13, 22), "n4": (12, 40), "n2": (18, 50),
       "r7": (40, 6), "r9": (40, 19), "r10": (40, 33), "r11": (40, 47),
       "r12": (47, 6), "r18": (47, 19), "r16": (47, 33), "r13": (47, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "n1" else i[1:]) for i, p in d.items()] + [T]
def li(a, b):
    p, q = X(a), X(b)
    return line(p[0], p[1], q[0], q[1])
LINES = F.linien() + [li((LINIE, 0), (LINIE, 55))]
TORE = [F.tor()] + F.minitore(4.5, 50.5, d=LINIE)
CONES = [C(*X((LINIE, q)), shape="stange") for q in (14, 24.5, 30, 40.5)]
BREIT = {"n3": (21, 2), "n5": (12, 19), "n4": (12, 37), "n2": (21, 53)}
ANGRIFF = {"r9": (25, 25), "r10": (30, 37), "r7": (31, 11), "r11": (30, 50)}
ZURUECK = {"n3": (17, 13), "n5": (12, 22), "n4": (12, 36), "n2": (17, 46)}
MINI_OBEN, MINI_UNTEN = [round(X((LINIE, 4.5))[0] - 0.3, 1), X((LINIE, 4.5))[1]], [round(X((LINIE, 50.5))[0] - 0.3, 1), X((LINIE, 50.5))[1]]

u = {"title": "Erst aufbauen, dann verteidigen", "code": "UE-370", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "55 x 50 m",
 "description": "Ein Wellenspiel für die Viererkette auf einer Spielfeldhälfte. Sie baut mit dem Torwart ohne Gegner auf und spielt in eines der zwei Minitore, 35 Meter vor dem eigenen Tor. Sofort kommen vier Angreifer und kontern vier gegen vier aufs große Tor, die Kette muss schnell umschalten und eng zusammenrücken. Zwei Gruppen Angreifer wechseln sich ab, Welle um Welle.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte, 55 Meter breit, mit großem Tor. 35 Meter vor dem Tor ist eine Linie abgesteckt, außen darauf zwei Minitore, dazwischen vier Dummys. Dahinter bis zur Mittellinie ist Platz zum Warten.",
  "Verteilen: Team Neon mit Torwart und Viererkette steht im Feld. Zwei Gruppen von Team Rot mit je vier Angreifern warten hinter den Dummys. Der Trainer steht mit vielen Bällen an der Seitenlinie, auf Höhe der Dummys.",
  "Ablauf: Der Trainer spielt zum Torwart. Die Viererkette baut ohne Gegner breit auf und spielt in ein Minitor. Dann kommen die ersten vier Angreifer, bekommen einen neuen Ball vom Trainer und spielen vier gegen vier aufs große Tor. Erobert Team Neon den Ball, kontert es auf die Minitore.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Ist der Angriff vorbei, bekommt der Torwart den nächsten Ball, und die zweite Gruppe Angreifer ist dran."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Ball das Feld breit machen", "Nach dem Abschluss sofort umschalten und eng werden", "Einer presst, die anderen sichern ab", "Kopf hoch: Wo stehen die Angreifer?"],
 "materials": ["1 Großfeldtor", "2 Minitore", "4 Dummys", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Erst aufbauen, dann verteidigen. Die Viererkette spielt sich ohne Gegner heraus, und gleich danach kommt der Konter von vier Angreifern.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [h.B("b1", *hf.am_fuss([T["x"], T["y"]]))] + ERSATZ,
  "steps": [
   S("Trainer spielt zum Torwart", "Der Trainer spielt den Ball zum Torwart. Sofort macht die Viererkette das Feld breit. Die Außenverteidiger gehen ganz raus an die Seitenlinie.",
     zu("b1", POS["n1"]), *[lauf(i, p, delay=0.4) for i, p in BREIT.items()]),
   S("Aufbau ohne Gegner", "Noch stört keiner. Der Torwart spielt kurz zu Spieler vier, der spielt quer zu Spieler fünf, und weiter geht es raus zu Spieler drei.",
     zu("b1", BREIT["n4"]), zu("b1", BREIT["n5"], after=True), zu("b1", BREIT["n3"], after=True)),
   S("Ins Minitor, jetzt kommen sie", "Spieler drei dribbelt an und schiebt ins Minitor. Das gibt einen Punkt für Team Neon. Genau das ist das Zeichen für die vier Angreifer.",
     h.dr("n3", "b1", X((31, 4))), h.ps("b1", MINI_OBEN, after=True)),
   S("Umschalten, eng zusammen", "Die Angreifer laufen los, und der Trainer spielt Spieler neun einen neuen Ball zu. Sofort sprintet die ganze Kette zurück und rückt eng zusammen.",
     *[lauf(i, p) for i, p in ANGRIFF.items()], zu("s1", ANGRIFF["r9"], delay=0.8, bend=2),
     *[lauf(i, p, delay=0.7) for i, p in ZURUECK.items()]),
   S("Durch die Lücke: Punkt für Rot", "Zwischen Spieler vier und Spieler fünf ist noch eine Lücke. Spieler neun nimmt den Ball mit und zieht sofort ab. Das gibt einen Punkt für Team Rot. Danach bekommt der Torwart den nächsten Ball, und die zweite Gruppe Angreifer ist dran.",
     h.ps("s1", [10.3, 30.4]))],
  "dims": F.masslinie("50 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, die anderen sichern ab.", "Einer presst, drei sichern",
    "Geht ein Innenverteidiger raus und presst, rücken die anderen drei sofort ein. Der Nebenmann sichert hinter ihm ab, die Außenverteidiger schieben zur Mitte. So bleibt die Kette eng, der Pass durch die Mitte ist zu, und der Angreifer muss nach außen spielen.",
    sp(n1=(4, 27.5), n3=(18, 7), n5=(14, 20), n4=(13, 34), n2=(18, 46), r9=(29, 20), r10=(26, 34), r7=(27, 5), r11=(27, 51)),
    [h.B("b1", *fu((29, 20)))] + ERSATZ,
    [S("Spieler fünf presst", "Spieler neun kommt mit Ball. Spieler fünf geht raus und presst. Spieler vier rückt ein und sichert hinter ihm ab. Die Außenverteidiger schieben mit zur Mitte.",
       h.dr("r9", "b1", X((25, 21))), lauf("n5", (20.5, 21), delay=0.2), lauf("n4", (12, 28.5), delay=0.2), lauf("n3", (15, 12.5), delay=0.2),
       lauf("n2", (16.5, 41.5), delay=0.2)),
     S("Mitte zu, nach außen gelenkt", "Der Pass auf Spieler zehn ist zu, da steht Spieler vier. Spieler neun bleibt nur der Ball nach außen zu Spieler sieben. Genau dahin will die Kette ihn haben.",
       zu("b1", (27, 5)))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ball gewonnen, sofort kontern.", "Ball gewonnen, sofort kontern",
    "Hält der Torwart den Ball oder fängt die Kette einen Pass ab, geht es sofort nach vorn. Die Angreifer sind dann weit aufgerückt und kommen nicht schnell genug zurück. Ein Außenverteidiger startet hoch und breit, der Torwart spielt ihn direkt an, und der Konter geht auf ein Minitor.",
    sp(n1=(3, 27.5), n5=(8, 20), n4=(8, 39), n3=(14, 10), n2=(14, 46), r9=(18, 30), r10=(23, 19), r11=(28, 42), r7=(25, 5)),
    [h.B("b1", *fu((23, 19)))] + ERSATZ,
    [S("Der Torwart hält", "Spieler zehn schießt aus der Drehung, aber der Torwart hält den Ball fest. Spieler zwei startet schon nach außen.",
       zu("b1", (3, 27.5)), lauf("n2", (22, 51), delay=0.6)),
     S("Kopf hoch, schnell raus", "Der Torwart schaut sofort nach vorn und sieht Spieler zwei frei an der Linie. Er spielt ihn direkt an.",
       schau("n1", (3, 27.5), (22, 51)), zu("b1", (22, 51), after=True)),
     S("Konter ins Minitor: Punkt", "Spieler zwei nimmt den Ball mit, ist schneller als Spieler elf und schiebt ins Minitor. Das gibt einen Punkt für Team Neon.",
       h.dr("n2", "b1", X((32, 50.5))), lauf("r11", (28, 45), delay=0.3), h.ps("b1", MINI_UNTEN, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
