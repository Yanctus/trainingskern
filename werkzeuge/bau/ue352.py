import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 36-P11 (U15-U17, Woche 19 Phase 1): Developing the 433: Midfield Rotations, Medium Sided Game. Halbes Spielfeld in voller Breite.
# Kein Großfeld quer: halbes Feld (AUFTRAG „Halbes Feld und kleiner bleibt wie bisher“, wie UE-314 und UE-340). Das Feld ist
# breiter als lang und liegt deshalb quer über die ganze Tafel (x 9-89, y 4-51), Figuren normal groß. Ausrichtung wie im PDF und
# im Video: großes Tor oben, zwei Minitore unten an der Mittellinie, Team Neon greift nach oben an. Keine Maßlinien (wie UE-314).
# Mittelzone aus vier Quadraten gestrichelt, Torraum durchgezogen. Großfeldtor (nur C- und B-Jugend).
# Pink (Aufbau im 4-3-3) -> Team Neon, Nummern wie im PDF (2-11). Blau (mit Torwart) -> Team Rot, neu nummeriert, weil alle
# Nummern doppelt sind: jeweils plus zehn (4 -> 14, 5 -> 15, 6 -> 16, 7 -> 17, 8 -> 18, 9 -> 19, 10 -> 20, 11 -> 21), Torwart r1 „TW“.
# Positionen grob wie im PDF, für den 3D-Abstand (19 Spieler) in Spalten im Abstand 8,5 geordnet; Spieler vier und Rot 20 haben
# dafür die Seiten getauscht (Spieler vier steht rechts neben Rot 20). Ein Trainer statt zwei, unten links an der Ecke.
# Grundform nach der PDF-Skizze: 6 auf 5, 5 in die Zone auf 4, 4 dreht auf und spielt auf den einrückenden Stürmer 9 (zusätzlicher
# Spieler, vier gegen drei), 9 legt auf 8 ab (zentraler Pass), 8 raus auf 7, Flanke, 9 schließt ab. Im PDF spielt 9 direkt auf 7;
# der Umweg über 8 hält den Passweg frei (3D-Abstand) und zeigt den zentralen Pass. Abschluss ergänzt („crossing and finishing“).
# Fassung 1 = PDF Progression 1 (Innenverteidiger dribbelt an, 9 kommt, 10 rotiert hinter die Mittelfeldlinie),
# Fassung 2 = Progression 2 (Flügelspieler 11 rückt ein, 10 geht nach außen, 4 zieht weg, Pass von 5 auf 11).
# Sichtkegel: In Text, Ton und Video kein Scannen. Beim Annehmen und Aufdrehen nach ZUSATZ_U15 (Vorbild ue300) schaut der Spieler
# zum Passgeber und nach der Annahme schwenkt der Kegel zum Passziel (bl mit von), dazu der Drehpfeil (drehen).
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def richt(a, b, d=20):
    # Blickkegel nicht zu lang: Punkt in Richtung b, etwa 20 Einheiten von a entfernt
    l = math.dist(a, b)
    d = min(d, l)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]
T = P("T", "c", 9, 55.3, "T")  # unten links an der Ecke
ERSATZ = [B("s1", 12.5, 55.8), B("s2", 15, 55.8)]
POS = {"r1": (46.5, 6), "r14": (38, 9), "r15": (63.5, 9), "n9": (55, 10),
       "n11": (21, 16), "n7": (77, 16), "r17": (12.5, 30), "r21": (85.5, 29),
       "n10": (29.5, 24), "r18": (38, 25), "r16": (55, 26), "n8": (63.5, 30),
       "r20": (46.5, 40), "n4": (55, 41.5), "n3": (21, 42), "n2": (77, 42),
       "r19": (38, 45), "n6": (29.5, 49), "n5": (63.5, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(9, 4, 80, 47), rect(34.4, 4, 26.6, 5.4), rect(27.2, 18.9, 41.2, 23, dashed=True),
         line(47.8, 18.9, 47.8, 41.9), line(27.2, 30.4, 68.4, 30.4)]
TORE = [{"x": 47.7, "y": 4, "side": "top", "size": "gross"}, {"x": 20, "y": 51, "side": "bottom"}, {"x": 77.8, "y": 51, "side": "bottom"}]
DROP9 = (48, 30)        # dort nimmt Spieler neun in der Mittelzone an
BOX9 = (50, 13)         # Spieler neun im Strafraum
SCHUSS = [52, 4.3]

u = {"title": "Rotieren im Mittelfeld", "code": "UE-352", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 16, "players_max": 20,
 "field_size": "Halbes Spielfeld",
 "description": "Zehn gegen neun auf einer Hälfte. Team Neon baut im 4-3-3 von hinten auf und muss den Ball durch eine Mittelzone aus vier Quadraten spielen. Dort stehen von jedem Team drei Spieler, ein vierter Angreifer darf dazukommen. Mit Rotationen und Freilaufen schaffen sich die Mittelfeldspieler Platz für den Weg zum Tor.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite. Oben steht das große Tor, unten an der Mittellinie zwei Minitore. In der Mitte ist eine Zone aus vier Quadraten abgesteckt.",
  "Verteilen: Team Neon mit zehn Feldspielern im 4-3-3, Team Rot mit Torwart und acht Feldspielern. In der Mittelzone stehen von jedem Team drei Spieler. Der Trainer steht mit Bällen an der Ecke.",
  "Ablauf: Team Neon baut über die Innenverteidiger auf. Der Ball muss in die Mittelzone und dort einmal zentral gespielt werden, bevor er sie verlässt. Ein zusätzlicher Angreifer darf in die Zone, dann heißt es vier gegen drei. Erobert Team Rot den Ball, spielt es durch die Mitte auf ein Minitor.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Neon, ein Treffer in ein Minitor gibt einen Punkt für Team Rot. Nach jedem Angriff bringt der Trainer einen neuen Ball zu den Innenverteidigern von Team Neon."],
 "organisation_show": ORG,
 "coaching_points": ["Rein in die Zone, raus aus der Zone: rotieren", "Freilaufen, damit es in der Mitte frei wird", "Beim Tauschen laut ansagen", "Über außen durch und scharf flanken"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Mittelzone", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rotieren im Mittelfeld. Zehn gegen neun auf einer Hälfte. Team Neon baut im Vier-Drei-Drei auf und muss durch die Mittelzone, wo die Mittelfeldspieler ständig die Plätze tauschen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *fu(POS["n6"]))] + ERSATZ,
  "steps": [
   S("Aufbau über die Innenverteidiger", "Spieler sechs hat den Ball. Er spielt quer zu Spieler fünf, und Team Rot schiebt mit.",
     ps("b1", fu(POS["n5"])), mv("r20", [48.5, 41], delay=0.4)),
   S("Rein in die Mittelzone", "Spieler vier kommt in der Zone entgegen und schaut zum Ball. Spieler fünf spielt ihn flach an.",
     bl("n4", richt(POS["n4"], POS["n5"])), ps("b1", fu(POS["n4"]), after=True)),
   S("Aufdrehen, Spieler neun kommt", "Von oben lässt sich Spieler neun in die Zone fallen. Jetzt sind es vier gegen drei. Spieler vier dreht auf und spielt ihn an.",
     mv("n9", list(DROP9)), bl("n4", richt(POS["n4"], DROP9), von=richt(POS["n4"], POS["n5"]), dauer=1.3, delay=0.3),
     drehen("n4", list(DROP9), delay=0.7), ps("b1", fu(DROP9), after=True)),
   S("Zentral ablegen, raus auf den Flügel", "Spieler neun legt direkt ab auf Spieler acht. Das ist der Pass durch die Mitte. Spieler acht spielt sofort raus auf Spieler sieben, und Spieler neun startet in den Strafraum.",
     ps("b1", fu(POS["n8"])), ps("b1", fu(POS["n7"]), after=True), mv("n9", list(BOX9), delay=0.6)),
   S("Flanke und Abschluss: Punkt", "Spieler sieben flankt scharf vors Tor. Spieler neun ist da und trifft, und das gibt einen Punkt für Team Neon. Danach bringt der Trainer den nächsten Ball zu den Innenverteidigern.",
     ps("b1", fu(BOX9)), ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Innenverteidiger dribbelt an, und vorn wird rotiert.", "Andribbeln und rotieren",
    "Der Innenverteidiger dribbelt mit Ball in die Mittelzone und zieht einen Gegenspieler auf sich. Im selben Moment kommt der Stürmer entgegen, und der Zehner rotiert hinter die Mittelfeldlinie von Team Rot. Genau dort bekommt er den Ball und kann direkt auf die Abwehrkette gehen.",
    sp(), [B("b1", *fu(POS["n5"]))] + ERSATZ,
    [S("Spieler fünf dribbelt an", "Spieler fünf dribbelt in die Zone, Spieler sechzehn muss raus zu ihm. Spieler vier macht ihm Platz und zieht weg.",
       dr("n5", "b1", [62, 37.5]), mv("r16", [63, 31.5], delay=0.4), mv("n4", [52, 46], delay=0.2)),
     S("Neun kommt, Zehn geht", "Jetzt die Rotation. Spieler neun lässt sich fallen, und Spieler zehn läuft hinter die Mittelfeldlinie. Er schaut zum Ball.",
       mv("n9", [52, 21]), mv("n10", [36, 15], delay=0.2), bl("n10", richt((36, 15), (62, 37.5)), after=True)),
     S("Pass hinter die Linie", "Spieler fünf spielt flach durch auf Spieler zehn. Die ganze Mittelfeldlinie von Team Rot ist überspielt.",
       ps("b1", fu([36, 15]))),
     S("Aufdrehen, durchstecken: Punkt", "Spieler zehn dreht auf und steckt durch auf Spieler elf, der innen startet. Spieler elf trifft, und das gibt einen Punkt für Team Neon.",
       bl("n10", richt((36, 15), (30, 8), 12), von=richt((36, 15), (62, 37.5)), dauer=1.3), drehen("n10", [30, 8], delay=0.4),
       mv("n11", [30, 8], delay=0.4), ps("b1", fu([30, 8]), after=True), ps("b1", [42.5, 4.3], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Flügelspieler rückt ein, der Zehner geht nach außen.", "Flügel rein, Zehner raus",
    "Der Flügelspieler kommt nach innen und tauscht mit dem Zehner, der nach außen geht. Der Sechser zieht auf die Ballseite weg und nimmt seinen Gegenspieler mit. So wird der Weg in die Mitte frei, und außen steht der Zehner ohne Gegenspieler.",
    sp(), [B("b1", *fu(POS["n5"]))] + ERSATZ,
    [S("Tauschen auf der Seite", "Spieler elf rückt nach innen, Spieler zehn geht dafür nach außen. Spieler vier zieht zur Ballseite weg, und Spieler zwanzig geht mit.",
       mv("n11", [31, 25]), mv("n10", [24, 12], delay=0.1), mv("n4", [60, 36], delay=0.2), mv("r20", [54, 37], delay=0.4)),
     S("Diagonal auf Spieler elf", "Der Weg ist frei. Spieler elf schaut zum Ball, und Spieler fünf spielt diagonal in die Mitte.",
       bl("n11", richt((31, 25), POS["n5"])), ps("b1", fu([31, 25]), after=True)),
     S("Aufdrehen, raus auf Spieler zehn", "Spieler elf dreht auf und spielt raus auf Spieler zehn. Der ist außen frei und kann flanken.",
       bl("n11", richt((31, 25), (24, 12), 14), von=richt((31, 25), POS["n5"]), dauer=1.3), drehen("n11", [24, 12], delay=0.4),
       ps("b1", fu([24, 12]), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
