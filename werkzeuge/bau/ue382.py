import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P3 (U15-U17, Woche 29 Phase 3): Combine & Run in Behind to Finish (Technical). 15 x 15 Yards = 14 x 14 m.
# Ausrichtung wie im PDF: Minitor links oben an der Seitenlinie (Öffnung zum Feld), Start unten. Feld x 28-72, y 5-49.
# Ein Team (Pink -> Team Neon), Nummern wie in der Skizze (Start 11, am mittleren Dummy 8, außen 10, Wartende 6, 7, 9).
# Im PDF-Text heißen die Rollen anders (8, 10, 9); maßgeblich ist die Skizze. Die drei Mannequins sind Dummys (Stange).
# „Medium sized goal“ ohne Torwart, in der Steigerung „mini-goal“ -> Minitor. Ein Trainer, unten links neben dem Feld.
# Wartende 6, 7, 9 hinter der Startlinie auseinandergezogen (3D-Abstand). Gestrichelte Linie unten = Startzone wie im PDF.
# Ablauf nach Skizze: 11 -> 8, Ablage auf 11, 8 dreht sich um den Dummy und bekommt den Ball noch einmal, nimmt an, dreht auf
# und spielt quer auf 10, 10 legt auf 11 ab (der schräg nachgerückt ist), 11 spielt zwischen den Dummys durch, 10 läuft
# hinter die Dummys, nimmt an und schließt ab. Wechsel: jeder eine Position weiter (PDF), Schütze stellt sich hinten an.
# Fassung 1 = Key Coaching Point (erster Kontakt aus dem Fuß, Abschluss mit dem zweiten), Fassung 2 = Progression
# (Verteidiger Team Rot Nummer 5, 1 gegen 1, erst in der zweiten Zone abschließen; Zonengrenze gestrichelt wie im Video;
# erobert der Verteidiger den Ball, dribbelt er über die Linie gegenüber dem Tor und bekommt den Punkt, laut Ton).
# Sichtkegel: Text, Ton und Video ohne Scan-Hinweis. Kegel nur beim Annehmen und Aufdrehen von Spieler acht
# („receives on the back foot around the mannequin and passes across“) nach dem Muster bl(von=...) + drehen().
T = P("T", "c", 20, 45, "T")  # unten links neben dem Feld
ERSATZ = [B("s1", 17.5, 49.5), B("s2", 20.5, 50.5)]
POS = {"n11": (49.5, 50.3), "n8": (43.4, 29.4), "n10": (69.5, 25), "n6": (37.5, 54), "n7": (59.5, 54), "n9": (68, 54)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + list(extra) + [T]
WARTE = [B("b6", 38.1, 54.6), B("b7", 60.1, 54.6), B("b9", 68.6, 54.6)]
LINES = [rect(28, 5, 44, 44), line(28, 43, 72, 43)]
TORE = [{"x": 28, "y": 10.8, "side": "left"}]
MITTE, PUPPE_A, PUPPE_B = (49.1, 29.5), (55.7, 21.5), (66, 21.5)
CONES = [C(*MITTE, shape="stange"), C(*PUPPE_A, shape="stange"), C(*PUPPE_B, shape="stange"), C(44, 49), C(56.9, 49, "neon")]
DIMS = dims(28, 72, 5, 49, "14 m", "14 m", rx=80)
AN8 = [44.5, 25]      # hier bekommt Spieler acht den zweiten Pass, hinter dem Dummy
NACH11 = [57.7, 38.3]  # hier steht Spieler elf nach dem schrägen Lauf
LAUF10 = [[70.5, 17.5], [62, 14]]  # Lauf von Spieler zehn hinter die Dummys
R5 = P("r5", "b", 52, 9, "5")
NACH = {"n11": tuple(NACH11), "n8": tuple(AN8)}
def lauf10(**k): return [mv("n10", LAUF10[0], **k), mv("n10", LAUF10[1], after=True)]

u = {"title": "Kombinieren, dann in die Tiefe", "code": "UE-382", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 4, "players_max": 8,
 "field_size": "14 x 14 m",
 "description": "Ein festes Passmuster zu dritt um drei Dummys. Der Ball läuft vom Start zum Spieler am mittleren Dummy, zurück und wieder hin, dann quer nach außen und noch einmal zurück. Zum Schluss geht ein Steilpass zwischen zwei Dummys durch, der Läufer nimmt an und schließt ins Minitor ab. Danach rückt jeder eine Position weiter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern. Oben in der Ecke steht ein Minitor an der Seitenlinie, im Feld stehen drei Dummys. Unten markieren zwei Hütchen den Start.",
  "Verteilen: Drei Spieler sind pro Durchgang dabei, einer am Start, einer am mittleren Dummy und einer außen neben den beiden anderen Dummys. Die übrigen warten mit Ball hinter dem Start. Der Trainer steht mit Ersatzbällen an der Ecke.",
  "Ablauf: Pass zum Spieler am Dummy und Ablage. Er dreht sich um den Dummy, bekommt den Ball noch einmal und spielt quer nach außen. Von dort kommt die Ablage auf den Starter, der zwischen den Dummys durchspielt. Der Läufer nimmt an und schließt ab.",
  "Wechsel: Nach jedem Durchgang rückt jeder eine Position weiter, der Schütze holt seinen Ball und stellt sich am Start an. Jeder Treffer gibt einen Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Zweimal bewegen, erst weg, dann zum Ball", "Erster Kontakt vom Fuß weg, der zweite ist der Schuss", "Scharf und genau passen", "Kein Torwart, also in die Ecken zielen"],
 "materials": ["1 Minitor", "3 Dummys", "2 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Kombinieren, dann in die Tiefe. Drei Spieler spielen sich um drei Dummys herum, bis einer hinter die Dummys startet und abschließt.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.1, 50.9)] + WARTE + ERSATZ,
  "steps": [
   S("Pass und Ablage", "Spieler elf startet und spielt flach zu Spieler acht am Dummy. Dann geht er ein paar Schritte nach. Spieler acht legt mit einem Kontakt zurück.",
     ps("b1", [44.0, 30.0]), mv("n11", [50.1, 41.4], delay=0.3), ps("b1", [50.7, 42.0], after=True)),
   S("Um den Dummy, der zweite Pass", "Spieler acht geht erst einen Schritt weg und dreht sich dann um den Dummy. Er schaut zum Ball. Spieler elf spielt ihn noch einmal an.",
     mv("n8", [41.5, 32.5]), mv("n8", AN8, after=True), bl("n8", [50.1, 41.4], after=True), ps("b1", [45.1, 25.6], after=True)),
   S("Aufdrehen und quer nach außen", "Er nimmt mit dem hinteren Fuß an und dreht auf. Sofort geht der Ball quer zu Spieler zehn. Spieler elf läuft schräg nach.",
     bl("n8", [69.5, 25], von=[50.1, 41.4], dauer=1.3), drehen("n8", [69.5, 25], gegen=True, delay=0.4), ps("b1", [70.1, 25.6], after=True),
     mv("n11", NACH11, delay=0.3)),
   S("Ablage, dann durch die Dummys", "Spieler zehn legt zurück auf Spieler elf und startet hinter die Dummys. Spieler elf spielt den Ball flach zwischen den beiden Dummys durch, genau in den Lauf.",
     ps("b1", [58.3, 38.9]), *lauf10(after=True), ps("b1", [62.6, 14.6], after=True)),
   S("Annehmen und abschließen: Punkt", "Spieler zehn nimmt den Ball Richtung Tor mit und schießt ins Eck, und das gibt einen Punkt für Spieler zehn. Dann rückt jeder weiter. Spieler elf geht an den Dummy, Spieler acht nach außen, und Spieler zehn stellt sich hinten an. Jetzt startet Spieler sechs.",
     dr("n10", "b1", [55, 12]), ps("b1", [28.4, 12.5], after=True), dr("n6", "b6", [49.5, 50.3], delay=1.2))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt geht vom Fuß weg.", "Erster Kontakt vom Fuß weg",
    "Kommt der Steilpass, nimmt der Läufer den Ball nicht unter den Körper. Der erste Kontakt legt ihn einen Schritt vor, schräg Richtung Tor. Mit dem zweiten Kontakt kommt schon der Schuss. Ohne Torwart zielt jeder in die Ecken, mit links und mit rechts.",
    sp(**NACH), [B("b1", 58.3, 38.9)] + WARTE + ERSATZ,
    [S("Starten, dann der Steilpass", "Spieler elf hat den Ball wieder. Spieler zehn startet hinter die Dummys, und der Pass kommt flach zwischen den beiden durch.",
       *lauf10(), ps("b1", [62.6, 14.6], after=True)),
     S("Erster Kontakt raus, zweiter ins Eck", "Der erste Kontakt geht einen Schritt vor Richtung Tor. Mit dem zweiten schießt Spieler zehn flach ins Eck, und das gibt einen Punkt für Spieler zehn.",
       dr("n10", "b1", [55, 12]), ps("b1", [28.4, 8.8], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger wartet vor dem Tor auf den Läufer.", "Eins gegen eins vor dem Tor",
    "Ein Spieler von Team Rot wird zum Verteidiger. Der Läufer muss ihn nach dem Steilpass im eins gegen eins schlagen. Geschossen wird erst, wenn er über die gestrichelte Linie in die zweite Zone vor dem Tor gedribbelt ist. Erobert der Verteidiger den Ball, dribbelt er über die Linie gegenüber vom Tor und bekommt den Punkt.",
    sp(extra=[R5], **NACH), [B("b1", 58.3, 38.9)] + WARTE + ERSATZ,
    [S("Steilpass, der Verteidiger kommt", "Spieler zehn startet, und Spieler elf spielt durch die Dummys. Spieler fünf kommt sofort raus und stellt sich ihm in den Weg.",
       *lauf10(), ps("b1", [62.6, 14.6], after=True), mv("r5", [56.5, 11.5], delay=0.8)),
     S("Täuschen und vorbei", "Spieler zehn täuscht nach außen an und zieht dann innen vorbei. Mit Tempo dribbelt er über die Linie in die zweite Zone.",
       dr("n10", "b1", [58.5, 17.5]), dr("n10", "b1", [44, 13], after=True), mv("r5", [51, 9.5], delay=0.6)),
     S("In der zweiten Zone: Punkt", "Jetzt darf er schießen. Flach ins lange Eck, und das gibt einen Punkt für Spieler zehn. Holt sich Spieler fünf den Ball, dribbelt er über die Linie gegenüber, und das gibt einen Punkt für Spieler fünf.",
       ps("b1", [28.4, 8.8]))],
    lines=LINES + [line(46, 5, 46, 43)], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
