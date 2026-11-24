import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P8 (U15-U17, Woche 25 Phase 1): Build from the Back & Defending the Counter (Wave Game). Halbe Spielfeldhälfte, 40 Yards tief
# (37 m, gerundet 35 m), Breite nach der Skizze etwa 62 Yards (57 m, gerundet 55 m). Kein Großfeld: halbes Feld, 13 Spieler, daher
# normale Figuren. Das Feld ist breiter als tief und füllt die Tafel quer: x 9-89, Tor oben (y 4), Mittellinie gestrichelt bei y 47,
# dahinter (bis y 55) der Wartebereich mit Dummys und Trainer wie im PDF. Strafraum und Torraum nach der PDF-Skizze, Halbkreis weggelassen.
# Um 180 Grad gedreht (im PDF liegt das große Tor unten): Team Neon baut nach unten auf, Team Rot greift nach oben an.
# Pink (Viererkette) + grüner Torwart -> Team Neon (n1 TW, 2, 4, 5, 3; durch die Drehung steht 2 links, 3 rechts), Blau (erste
# Angreifergruppe 7, 9, 10, 11) -> Team Rot, Nummern wie im PDF. Die zweite Angreifergruppe (gelb 2, 8, 6, 3) steht nur im Text
# (an der Mittellinie ist neben Blau und Trainer kein Platz ohne Verdecken in 3D). Ein Trainer statt zwei.
# Grundform nach PDF und Video (0:13-0:28): Trainer spielt zum Torwart, Kette macht das Feld breit, Torwart -> 4 -> 5 -> 3, Spieler 3
# trifft ins Minitor; dann spielt der Trainer den Angreifern einen neuen Ball zu (im PDF nicht gezeigt, wer den Angreifern den Ball
# gibt: Annahme), vier gegen vier aufs große Tor.
# Fassungen wie die PDF-Coaching-Punkte: 1 Innenverteidiger presst, die anderen sichern ab und lenken nach außen; 2 Torwart hält und
# leitet sofort den Konter auf ein Minitor ein (Außenverteidiger startet hoch und breit, Ton 0:35).
# Sichtkegel: Text "Quick scans to check the oppositions positioning": in der Grundform schaut Spieler 4 beim Umschalten zu den
# Angreifern, im ersten Coaching-Punkt sichert Spieler 4 ab und schaut zu Spieler 10; im zweiten Coaching-Punkt schaut der Torwart
# nach dem Fangen zum startenden Außenverteidiger (aus dem Sinn, im Video kein Kegel eingezeichnet).
# Keine Dublette: UE-166 (03-P3, vier gegen vier mit Konter auf zwei Minitore, ohne Aufbauphase), UE-177 (78-P3), UE-212 (78-P6),
# UE-242 (78-P7), UE-250 (78-P12, Springer spielen ein, drei Minitore) und UE-320 (78-P4) haben keine Aufbauphase ohne Gegner
# und keine Wellen.
T = P("T", "c", 49.5, 51, "T")
ERSATZ = [B("s1", 53, 52.5), B("s2", 46, 52.5)]
POS = {"n1": (49, 9.5), "n2": (15, 27), "n4": (36, 21), "n5": (61, 21), "n3": (83, 27),
       "r11": (24, 47), "r10": (36, 47), "r9": (62, 47), "r7": (74, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, "TW") if i == "n1" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 51), rect(24, 4, 50, 15), rect(36.5, 4, 25, 6), line(9, 47, 89, 47)]
TORE = [{"x": 49, "y": 4, "side": "top", "size": "gross"}, {"x": 15.6, "y": 47, "side": "bottom"}, {"x": 82.4, "y": 47, "side": "bottom"}]
CONES = [C(x, 49.5, shape="stange") for x in (28.4, 42, 56.3, 69.4)]
DIMS = dims(9, 89, 4, 47, "55 m", "35 m", rx=95)
BREIT = {"n2": [12, 30], "n4": [34, 16], "n5": [63, 16], "n3": [86, 30]}
ANGRIFF = {"r10": [36, 37], "r9": [49, 34], "r7": [66, 38], "r11": [26, 40]}
ZURUECK = {"n2": [22, 25], "n4": [38, 22], "n5": [58, 22], "n3": [72, 25]}

u = {"title": "Erst aufbauen, dann verteidigen", "code": "UE-370", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "55 x 35 m",
 "description": "Ein Wellenspiel für die Viererkette. Sie baut mit dem Torwart ohne Gegner auf und spielt in ein Minitor an der Mittellinie. Sofort kommen vier Angreifer und kontern vier gegen vier aufs große Tor, die Kette muss schnell umschalten und eng zusammenrücken. Zwei Gruppen Angreifer wechseln sich ab, Welle um Welle.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte, etwa 55 mal 35 Meter, mit großem Tor. An der Mittellinie stehen außen zwei Minitore und dazwischen vier Dummys.",
  "Verteilen: Team Neon mit Torwart und Viererkette steht im Feld. Zwei Gruppen von Team Rot mit je vier Angreifern warten an den Dummys. Der Trainer steht mit vielen Bällen an der Mittellinie.",
  "Ablauf: Der Trainer spielt zum Torwart. Die Viererkette baut ohne Gegner breit auf und spielt in ein Minitor. Dann kommen die ersten vier Angreifer, bekommen einen neuen Ball vom Trainer und spielen vier gegen vier aufs große Tor. Erobert Team Neon den Ball, kontert es auf die Minitore.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Ist der Angriff vorbei, bekommt der Torwart den nächsten Ball, und die zweite Gruppe Angreifer ist dran."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Ball das Feld breit machen", "Nach dem Abschluss sofort umschalten und eng werden", "Einer presst, die anderen sichern ab", "Kopf hoch: Wo stehen die Angreifer?"],
 "materials": ["1 Großfeldtor", "2 Minitore", "4 Dummys", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Erst aufbauen, dann verteidigen. Die Viererkette spielt sich ohne Gegner heraus, und gleich danach kommt der Konter von vier Angreifern.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.1, 51.6)] + ERSATZ,
  "steps": [
   S("Trainer spielt zum Torwart", "Der Trainer spielt den Ball zum Torwart. Sofort macht die Viererkette das Feld breit. Die Außenverteidiger gehen ganz raus an die Linie.",
     ps("b1", fu(POS["n1"])), *[mv(i, p, delay=0.4) for i, p in BREIT.items()]),
   S("Aufbau ohne Gegner", "Noch stört keiner. Der Torwart spielt kurz zu Spieler vier, der spielt quer zu Spieler fünf, und weiter geht es raus zu Spieler drei.",
     ps("b1", fu(BREIT["n4"])), ps("b1", fu(BREIT["n5"]), after=True), ps("b1", fu(BREIT["n3"]), after=True)),
   S("Ins Minitor, jetzt kommen sie", "Spieler drei dribbelt an und schiebt ins Minitor. Das gibt einen Punkt für Team Neon. Genau das ist das Zeichen für die vier Angreifer.",
     dr("n3", "b1", [84, 39]), ps("b1", [82.4, 46.7], after=True)),
   S("Umschalten, eng zusammen", "Die Angreifer laufen los, und der Trainer spielt Spieler zehn einen neuen Ball zu. Spieler vier schaut sofort, wo die Angreifer sind. Die ganze Kette sprintet zurück und rückt eng zusammen.",
     *[mv(i, p) for i, p in ANGRIFF.items()], ps("s1", fu(ANGRIFF["r10"]), delay=0.8), bl("n4", ANGRIFF["r9"], delay=0.3),
     *[mv(i, p, delay=0.7) for i, p in ZURUECK.items()]),
   S("Durch die Mitte: Punkt für Rot", "Zwischen Spieler vier und Spieler fünf ist eine Lücke. Spieler zehn spielt durch auf Spieler neun, und der zieht sofort ab. Das gibt einen Punkt für Team Rot. Danach bekommt der Torwart den nächsten Ball, und die zweite Gruppe Angreifer ist dran.",
     ps("s1", fu(ANGRIFF["r9"])), ps("s1", [44, 4.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, die anderen sichern ab.", "Einer presst, drei sichern",
    "Geht ein Innenverteidiger raus und presst, rücken die anderen drei sofort ein. Der Nebenmann sichert hinter ihm ab, die Außenverteidiger schieben zur Mitte. So bleibt die Kette eng, der Pass durch die Mitte ist zu, und der Angreifer muss nach außen spielen.",
    sp(r9=(60, 38), r10=(47, 35), r7=(85, 36), r11=(14, 36), n5=(60, 22), n4=(38, 21), n3=(76, 23), n2=(25, 24), n1=(49, 8)),
    [B("b1", 60.6, 38.6)] + ERSATZ,
    [S("Spieler fünf presst", "Spieler neun kommt mit Ball. Spieler fünf geht raus und presst. Spieler vier rückt ein, sichert hinter ihm ab und schaut, wo Spieler zehn steht. Die Außenverteidiger schieben mit zur Mitte.",
       dr("r9", "b1", [59, 33]), mv("n5", [60, 28.5], delay=0.2), mv("n4", [47, 21], delay=0.2), mv("n3", [69, 21], delay=0.2),
       mv("n2", [32, 22], delay=0.2), bl("n4", [47, 35], after=True)),
     S("Mitte zu, nach außen gelenkt", "Der Pass auf Spieler zehn ist zu, da steht Spieler vier. Spieler neun bleibt nur der Ball nach außen zu Spieler sieben. Genau dahin will die Kette ihn haben.",
       ps("b1", [85.6, 36.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ball gewonnen, sofort kontern.", "Ball gewonnen, sofort kontern",
    "Hält der Torwart den Ball oder fängt die Kette einen Pass ab, geht es sofort nach vorn. Die Angreifer stehen dann tief im eigenen Angriff und sind weit weg. Ein Außenverteidiger startet hoch und breit, der Torwart spielt ihn direkt an, und der Konter geht auf ein Minitor.",
    sp(n1=(49, 8), n4=(38, 10), n5=(60, 10), n2=(26, 20), n3=(72, 20), r9=(44, 26), r10=(55, 26), r11=(30, 36), r7=(82, 30)),
    [B("b1", 55.6, 26.6)] + ERSATZ,
    [S("Der Torwart hält", "Spieler zehn schießt aus der Drehung, aber der Torwart hält den Ball fest. Spieler zwei startet schon nach außen.",
       ps("b1", [49.6, 8.6]), mv("n2", [20, 33], delay=0.6)),
     S("Kopf hoch, schnell raus", "Der Torwart schaut sofort nach vorn und sieht Spieler zwei frei an der Linie. Er spielt ihn direkt an.",
       bl("n1", [20, 33]), ps("b1", [20.6, 33.6], after=True)),
     S("Konter ins Minitor: Punkt", "Spieler zwei nimmt den Ball mit, ist schneller als Spieler elf und schiebt ins Minitor. Das gibt einen Punkt für Team Neon.",
       dr("n2", "b1", [17, 41]), mv("r11", [24, 40], delay=0.3), ps("b1", [15.6, 46.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
