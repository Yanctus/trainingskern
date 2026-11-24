import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P12 (U15-U17, Woche 7 Phase 1): Technical Combinations & Driving with the Ball. 30 x 30 Yards = 27 x 27 m (gerundet 25 x 25 m),
# Feld x 25-75, y 5-55. Nicht gedreht (Start unten, Ball läuft nach oben und an der Seitenlinie zurück). Ein Team (Neon),
# Nummern wie im PDF (2-12 und 14). Ein Trainer oben wie im PDF.
# Zwei Abläufe laufen gleichzeitig und spiegelverkehrt: rechts startet Spieler acht (mit 11, 9, 2 in der Ecke oben links und 12 an
# der Puppe links), links startet Spieler sechs (mit 7, 10, 3 in der Ecke oben rechts und 14 an der Puppe rechts). Die Läufer neun
# und zehn kreuzen sich. Puppen (Mannequins) als Stangen.
# 3D-Abstand: Hütchen-Stationen in einem Raster (Spalten 42/58, Reihen 19/35/51), die Wartenden mit Ball (4, 5) und die Spieler
# an der Puppe (12, 14) unten an der Grundlinie etwas weiter nach außen gerückt als im PDF; Puppen höher.
# Doppelpass in der Ecke nach Ton gedeutet: Pass in die Ecke, Ball zurück, dann um die Ecke die Linie hinunter in den Lauf des
# Eckspielers; er dribbelt die Linie hinunter und spielt den letzten Doppelpass um die Puppe mit Spieler zwölf.
# Wechsel aus dem Video: Jeder rückt eine Station weiter (Start -> mittleres Hütchen -> oberes Hütchen -> Ecke -> Puppe ->
# mit Ball warten -> Start). Keine Punkte, Ziel statt Wertung.
# Sichtkegel: PDF Key Coaching Point 1 („keep your head up while dribbling … stay aware of teammates’ positions“): Spieler
# neun schaut beim Kreuzen erst zu Spieler zehn, dann in die Ecke zu Spieler zwei (bl mit von). Im Video kein Kegel eingezeichnet.
T = P("T", "c", 50, 2.5, "T")
ERSATZ = [B("s1", 53.5, 3), B("s2", 56, 3)]
POS = {"n2": (26, 6), "n3": (74, 6), "n10": (42, 19), "n9": (58, 19), "n7": (42, 35), "n11": (58, 35),
       "n6": (45.8, 51), "n8": (54.2, 51), "n12": (29, 55), "n4": (37.5, 55), "n5": (62.5, 55), "n14": (71, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
BAELLE = [B("b8", *fuss("n8")), B("b6", *fuss("n6")), B("b4", *fuss("n4")), B("b5", *fuss("n5"))] + ERSATZ
PUPPEN = [C(33, 42, shape="stange"), C(67, 42, shape="stange")]
CONES = ecken(25, 5, 50, 50) + [C(42, 22.5), C(58, 22.5), C(42, 38.5), C(58, 38.5)] + PUPPEN
LINES = [rect(25, 5, 50, 50)]
# Stand nach dem ersten Doppelpass (Start beider Fassungen): 11 und 7 haben sich vom Hütchen gelöst
AB = {"n11": (66.5, 31), "n7": (33.5, 31)}

def start_dp():
    return [mv("n11", [66.5, 31]), ps("b8", [67.1, 31.6], after=True), ps("b8", fuss("n8"), after=True),
            mv("n7", [33.5, 31]), ps("b6", [34.1, 31.6], after=True), ps("b6", fuss("n6"), after=True)]
def in_den_lauf():
    return [mv("n9", [53, 12]), ps("b8", [53.6, 12.6], delay=0.3), mv("n10", [47, 15], delay=0.6), ps("b6", [47.6, 15.6], delay=0.9)]
def kreuzen(blick=False):
    m = []
    if blick:
        m += [bl("n9", [31.5, 7.2], von=[47, 15], dauer=1.3)]
    return m + [dr("n9", "b8", [36, 9], after=blick or None), dr("n10", "b6", [64, 9], delay=0.4)]
def ecke():
    return [ps("b8", [26.6, 6.6]), ps("b8", [36.6, 9.6], after=True), mv("n2", [23, 14], after=True), ps("b8", [23.6, 14.6], after=True),
            ps("b6", [74.6, 6.6], delay=0.3), ps("b6", [64.6, 9.6], after=True), mv("n3", [77, 14], after=True), ps("b6", [77.6, 14.6], after=True)]
def linie():
    return [dr("n2", "b8", [23, 26]), dr("n2", "b8", [30, 32], after=True), dr("n3", "b6", [77, 26], delay=0.2), dr("n3", "b6", [70, 32], after=True)]
def puppe():
    return [ps("b8", fuss("n12")), mv("n2", [37, 40], delay=0.2), mv("n2", [37, 47], after=True), ps("b8", [37.6, 47.6], after=True),
            ps("b6", fuss("n14"), delay=0.3), mv("n3", [63, 40], delay=0.5), mv("n3", [63, 47], after=True), ps("b6", [63.6, 47.6], after=True)]

u = {"title": "Doppelpässe, kreuzen, dribbeln", "code": "UE-338", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Dribbling"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 16,
 "field_size": "25 x 25 m",
 "description": "Ein Passmuster für zwei Bälle, die gleichzeitig laufen. Nach einem Doppelpass am Start geht der Ball in den Lauf des nächsten Spielers, die beiden Läufer kreuzen sich in der Mitte. In der Ecke folgt der nächste Doppelpass, dann geht es mit Ball die Linie hinunter und um die Puppe. Kurze Pässe, Pässe in den Lauf und Tempo mit Ball wechseln sich ab.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern. In der Mitte stehen vier Hütchen als Stationen, zwei oben und zwei darunter. Unten links und unten rechts steht je eine Puppe.",
  "Verteilen: Je ein Spieler an den vier Hütchen und in den beiden oberen Ecken. Unten starten zwei Spieler mit Ball, dahinter warten die Nächsten mit Ball. Neben jeder Puppe steht ein Spieler für den letzten Doppelpass. Der Trainer steht mit Ersatzbällen oben am Rand.",
  "Ablauf: Beide Starter spielen gleichzeitig einen Doppelpass mit dem Spieler, der sich vom Hütchen löst. Dann geht der Ball in den Lauf des oberen Spielers, die beiden kreuzen sich und dribbeln Richtung Ecke. Doppelpass mit dem Eckspieler, der Ball geht um die Ecke in seinen Lauf, er dribbelt die Linie hinunter und spielt den letzten Doppelpass um die Puppe.",
  "Wechsel: Jeder rückt nach seiner Aktion eine Station weiter, vom Start ans mittlere Hütchen, dann nach oben, in die Ecke und an die Puppe. Wer an der Puppe war, wartet mit Ball am Start. Ziel: zwei Bälle ohne Fehlpass durch die ganze Runde bringen."],
 "organisation_show": ORG,
 "coaching_points": ["Pass in den Lauf, nicht in die Füße", "Kopf hoch beim Kreuzen", "Mal links, mal rechts passen", "Erst lösen, wenn der Ball kommt"],
 "materials": ["8 Hütchen", "2 Puppen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Doppelpässe, kreuzen, dribbeln. Zwei Bälle laufen gleichzeitig durchs Feld, mit Doppelpässen, Pässen in den Lauf und Tempo die Linie hinunter.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Doppelpass am Start", "Beide Starter spielen gleichzeitig. Wir schauen auf Spieler acht. Spieler elf löst sich nach außen vom Hütchen, bekommt den Ball und spielt direkt zurück. Auf der anderen Seite machen Spieler sechs und Spieler sieben dasselbe.",
     *start_dp()),
   S("Der Ball geht in den Lauf", "Jetzt startet Spieler neun schräg nach innen. Spieler acht spielt den Ball ein Stück vor ihn, so nimmt er ihn im Laufen mit. Spieler zehn bekommt den Ball von Spieler sechs genauso.",
     *in_den_lauf()),
   S("Die beiden kreuzen sich", "Mit Ball am Fuß kreuzen sich Spieler neun und Spieler zehn. Jeder dribbelt Richtung Ecke auf der anderen Seite.",
     *kreuzen()),
   S("Doppelpass in der Ecke", "Spieler neun spielt in die Ecke zu Spieler zwei und bekommt den Ball zurück. Spieler zwei startet die Linie hinunter, und Spieler neun legt ihm den Ball um die Ecke in den Lauf.",
     *ecke()),
   S("Mit Tempo die Linie hinunter", "Spieler zwei nimmt den Ball mit und geht mit Tempo die Linie hinunter. Drüben macht Spieler drei das Gleiche.",
     *linie()),
   S("Doppelpass um die Puppe", "Vor der Puppe passt Spieler zwei zu Spieler zwölf und läuft an der Puppe vorbei. Der Ball kommt in seinen Lauf zurück, und beide Bälle sind durch. Jetzt rückt jeder eine Station weiter, und Spieler vier und Spieler fünf starten die nächste Runde.",
     *puppe())],
  "dims": dims(25, 75, 5, 55, "25 m", "25 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kopf hoch beim Kreuzen.", "Kopf hoch beim Kreuzen",
    "Spieler neun und Spieler zehn laufen mit Ball direkt aufeinander zu. Wer nur auf den Ball schaut, rennt den anderen um. Darum geht der Kopf beim Dribbeln hoch, erst zum Mitspieler, dann in die Ecke.",
    sp(**AB), BAELLE,
    [S("Beide im Lauf angespielt", "Spieler neun und Spieler zehn starten schräg nach innen und bekommen den Ball in den Lauf.",
       *in_den_lauf()),
     S("Kopf hoch, dann vorbei", "Spieler neun hebt den Kopf. Er sieht Spieler zehn kommen, dann schaut er in die Ecke zu Spieler zwei. Beide ziehen eng aneinander vorbei.",
       *kreuzen(blick=True)),
     S("Ab in die Ecke", "Ohne Tempo zu verlieren, spielt Spieler neun in die Ecke zu Spieler zwei. Spieler zehn spielt drüben zu Spieler drei.",
       ps("b8", [26.6, 6.6]), ps("b6", [74.6, 6.6], delay=0.3))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Ball in den Lauf spielen.", "Pass in den Lauf",
    "Der Pass geht nicht in die Füße, sondern ein paar Schritte vor den Mitspieler. Er nimmt den Ball im vollen Lauf mit und muss nicht abbremsen. Dafür muss der Pass genau sein und das richtige Tempo haben.",
    sp(**AB), BAELLE,
    [S("Vor den Mann spielen", "Spieler neun läuft los. Spieler acht spielt nicht dorthin, wo er steht, sondern dorthin, wo er gleich ist.",
       mv("n9", [53, 12]), ps("b8", [53.6, 12.6], delay=0.3)),
     S("Im Lauf mitnehmen", "Spieler neun muss nicht stoppen. Er nimmt den Ball im Laufen mit und dribbelt weiter Richtung Ecke.",
       dr("n9", "b8", [36, 9])),
     S("Um die Ecke in den Lauf", "Doppelpass mit Spieler zwei. Dann geht der Ball die Linie hinunter, genau in den Lauf von Spieler zwei, und der nimmt ihn mit Tempo mit.",
       ps("b8", [26.6, 6.6]), ps("b8", [36.6, 9.6], after=True), mv("n2", [23, 14], after=True), ps("b8", [23.6, 14.6], after=True),
       dr("n2", "b8", [23, 26], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
