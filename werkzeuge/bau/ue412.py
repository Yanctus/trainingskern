import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 89-P12 (U15-U17, Woche 40 Phase 5): Protect the Back Line - CDM (Break Out Game). 30 x 50 Yards = 27 x 46 m (gerundet
# 25 x 45 m), Rondo-Feld 15 x 15 Yards = 14 x 14 m. Kein Großfeld (12 Feldspieler, kein ganzer Platz), aber ein langes Feld
# (Verhältnis 1,7): LANGES FELD QUER wie bau/ue317.py, direkt in Tafel-Koordinaten gebaut. Feld x 9-89, y 4-51, in beiden
# Richtungen derselbe Maßstab (1,74 Einheiten je Meter). Die eigene Hälfte mit dem Rondo liegt links (im PDF unten), die Spitzen
# greifen nach rechts aufs Tor an (im PDF oben).
# Pink (Sechser 6, Rondo 7 und 8, hinten 4 und 5) -> Team Neon, Nummern wie im PDF. Blau -> Team Rot, neu nummeriert, weil die
# Nummern doppelt sind: Rondo 6 -> 16, 8 -> 18, 4 -> 14, Spitzen 11, 9 und 7 -> 17. Der grüne Torwart im Rondo (1) spielt für
# Team Rot (r1, TW), der grüne Torwart vorn (13) ist neutral (k1, TW). Ein Trainer an der Mittellinie (unten, im PDF rechts).
# Rondo-Feld als Zone von Team Rot (orange), die schrägen Linien von den vorderen Ecken zur Seitenlinie gestrichelt, sechs
# Hütchen wie im PDF. Strafräume vereinfacht, Mittelkreis, Halbkreise und Torräume weggelassen.
# Positionen im Rondo auf ein Raster gesetzt (3D-Abstand); der Torwart steht hinter der Rondo-Linie, Spieler sechs knapp auf
# der Mittellinie.
# Grundform nach PDF, Ton und Video (0:14-0:40): Rondo vier gegen drei, Pass auf eine Spitze, drei gegen zwei aufs Tor (Punkt
# für Team Rot, im Original „progress the ball into the final third“, als Treffer gewertet); neuer Ball vom Trainer, Team Neon
# erobert im Rondo und dribbelt hinaus (Punkt).
# Fassungen: Coaching-Punkt aus Video/Ton („Effective positioning - blocking multiple lines of forward passes“) und Steigerung =
# PDF Progression 1 (Sechser läuft mit zurück, drei gegen drei; Ballgewinn hinten zurück zum Trainer, Ton 1:09). Progression 2
# (Konter auf das nahe Tor) nicht gebaut.
# Sichtkegel: Text „Constant Scanning - continuously check surroundings“, im Video nicht eingezeichnet. Der Sechser passt danach nicht
# gleich selbst: nach der Sichtkegel-Regel (Inhaber, 25.11.2026) bekommt im Coaching-Punkt der Passgeber den Kegel (Spieler sechzehn
# schaut vor seinem Pass nach vorn zu Spieler neun). Der frühere erste Schritt (nur der Schulterblick) ist im zweiten aufgegangen.
# Keine Dublette: UE-167 (89-P5, Hütchentor), UE-173 (89-P1, zwei Rondos vier gegen eins), UE-193 (89-P2, Dummys),
# UE-293 (Sechser blockt Pässe zum Minitor) haben andere Organisation und Abläufe.
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
MX, MY = 49, 27.5
RX0, RY0, RX1, RY1 = 25, 15.75, 49, 39.25  # Rondo-Feld (15 x 15 Yards) an der Mittellinie
T = P("T", "c", 46, 55.3, "T")  # unten an der Seitenlinie, an der Mittellinie
ERSATZ = [B("s1", 42.5, 55.8), B("s2", 49.5, 55.8)]
POS = {"k1": (83, 27.5), "r9": (73, 27.5), "n4": (64.5, 19), "n5": (64.5, 36), "r11": (56, 8), "r17": (56, 46.5),
       "n6": (50, 27.5), "r16": (41.7, 19), "n7": (41.7, 35.5), "r18": (33.4, 16.5), "n8": (33.4, 32.5),
       "r1": (24.5, 22), "r14": (25, 38.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i in ("k1", "r1") else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False),
         rect(FX0, 11, 14, 33), rect(FX1 - 14, 11, 14, 33),
         {"type": "zone", "x": RX0, "y": RY0, "w": RX1 - RX0, "h": RY1 - RY0, "color": "orange"},
         line(RX1, RY0, 60.2, FY0), line(RX1, RY1, 60.2, FY1)]
CONES = [C(RX0, RY0), C(RX0, RY1), C(RX1, RY0), C(RX1, RY1), C(60.2, FY0), C(60.2, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
# Nur die Länge als Maßlinie (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "45 m", "25 m")[:1]

u = {"title": "Sechser schützt die Abwehr", "code": "UE-412", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "25 x 45 m",
 "description": "Ein Rondo vier gegen drei mit Ausbruch nach vorn. Team Rot hält im Rondo den Ball, der Torwart spielt mit, und sucht den Pass auf eine der drei Spitzen in der anderen Hälfte. Der Sechser von Team Neon steht auf der Mittellinie und macht die Passwege nach vorn zu. Erobert Team Neon den Ball im Rondo, dribbelt es hinaus und bekommt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 45 Metern mit Mittellinie und einem großen Tor auf jeder Seite. In der eigenen Hälfte liegt an der Mittellinie ein Rondo-Feld von 14 mal 14 Metern. Von seinen vorderen Ecken laufen zwei Linien schräg zur Seitenlinie.",
  "Verteilen: Im Rondo spielen drei Spieler von Team Rot mit ihrem Torwart gegen zwei von Team Neon. Der Sechser von Team Neon steht auf der Mittellinie. In der anderen Hälfte stehen drei Spitzen von Team Rot gegen zwei Verteidiger und einen Torwart. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Team Rot lässt den Ball im Rondo laufen und sucht den Pass auf eine Spitze. Kommt er durch, greifen die Spitzen drei gegen zwei aufs Tor an. Der Sechser bleibt auf der Mittellinie und fängt die Pässe nach vorn ab.",
  "Wertung: Ein Treffer gibt einen Punkt für Team Rot. Erobert Team Neon den Ball im Rondo und dribbelt hinaus, gibt das einen Punkt für Team Neon. Gewinnen die Verteidiger hinten den Ball, spielen sie ihn ins Rondo, und dort wird hinausgedribbelt. Danach spielt der Trainer einen neuen Ball ins Rondo."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo stehen die Spitzen?", "Zwischen zwei Passwegen stehen", "Den Pass lesen und früh dazwischen", "Ball gewonnen? Sofort raus aus dem Rondo"],
 "materials": ["2 große Tore", "6 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechser schützt die Abwehr. Ein Rondo vier gegen drei, und vorn warten drei Spitzen. Unser Sechser steht auf der Mittellinie und macht die Passwege nach vorn zu.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *fuss("r1"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Im Rondo läuft der Ball", "Im Rondo hat Team Rot den Ball, vier gegen drei, der Torwart spielt mit. Er spielt zu Spieler achtzehn, und Spieler acht läuft sofort an. Spieler sechs bleibt auf der Mittellinie und schiebt mit zur Ballseite.",
     ps("b1", fuss("r18")), mv("n8", [30.5, 24.5], delay=0.3), mv("n6", [50, 22], delay=0.3)),
   S("Aufdrehen und steil nach vorn", "Spieler achtzehn legt kurz zu Spieler sechzehn. Der dreht auf und spielt sofort steil auf Spieler siebzehn. Spieler sechs stand zu weit auf der Ballseite, der Weg war frei.",
     ps("b1", fuss("r16")), drehen("r16", [56, 46.5], after=True), ps("b1", fuss("r17"), after=True)),
   S("Drei gegen zwei: Punkt", "Jetzt geht es drei gegen zwei aufs Tor. Spieler siebzehn zieht los und legt quer auf Spieler neun. Der schießt, und das gibt einen Punkt für Team Rot.",
     dr("r17", "b1", [68, 47]), mv("n5", [66, 42.5], delay=0.2), mv("n4", [70, 24], delay=0.3), ps("b1", fuss("r9"), after=True),
     mv("k1", [84, 31], delay=1.2), ps("b1", [88.5, 23.5], after=True)),
   S("Ball erobert, rausgedribbelt: Punkt", "Der Trainer spielt den nächsten Ball zu Spieler vierzehn. Der will steil spielen, aber Spieler acht liest den Pass und geht dazwischen. Er dribbelt aus dem Rondo, und das gibt einen Punkt für Team Neon. Danach kommt der nächste Ball vom Trainer, wieder zu Team Rot.",
     ps("s1", fuss("r14")), mv("n8", [33.3, 28.8], delay=0.4), ps("s1", [33.9, 29.4], after=True), dr("n8", "s1", [31, 44], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zwei Passwege auf einmal zustellen.", "Zwei Passwege zustellen",
    "Spieler sechs schaut immer wieder über die Schulter, wo die Spitzen stehen. Dann stellt er sich auf der Mittellinie so hin, dass er zwei Passwege auf einmal zumacht. Wer trotzdem spielt, spielt ihm den Ball in die Füße. Den Ball gibt er sofort ins Rondo, und dort wird hinausgedribbelt.",
    sp(), [B("b1", *fuss("r16"))] + ERSATZ,
    [S("Zwischen zwei Passwegen stehen", "Spieler sechzehn hat den Ball vorn im Rondo und zwei Möglichkeiten nach vorn, Spieler elf und Spieler neun. Spieler sechs weiß, wo die beiden stehen. Er schiebt auf der Mittellinie rüber und stellt sich genau dazwischen. Jetzt sind beide Wege zu.",
       opt("r16", [56, 8]), opt("r16", [73, 27.5]), mv("n6", [51, 17.5], delay=0.8)),
     S("Abgefangen, ab ins Rondo", "Spieler sechzehn schaut nach vorn und spielt trotzdem auf Spieler neun. Spieler sechs macht einen Schritt und hat den Ball. Er spielt sofort ins Rondo zu Spieler sieben. Der dribbelt hinaus, und das gibt einen Punkt für Team Neon.",
       bl("r16", [61, 24.2]), mv("n6", [51, 20.8], delay=0.3), ps("b1", [51.6, 21.4], after=True), ps("b1", fuss("n7"), after=True), dr("n7", "b1", [40, 44], after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Der Sechser läuft mit zurück.", "Sechser läuft mit zurück",
    "Kommt der Pass auf eine Spitze durch, darf Spieler sechs die Mittellinie verlassen und hinterher sprinten. Vorn heißt es dann drei gegen drei. Erobert Team Neon dort den Ball, geht er zurück zum Trainer, und das Rondo beginnt neu.",
    sp(), [B("b1", *fuss("r14"))] + ERSATZ,
    [S("Der Pass kommt durch", "Diesmal kommt der Pass durch. Spieler vierzehn spielt an der Seite lang auf Spieler siebzehn.",
       ps("b1", fuss("r17"))),
     S("Spieler sechs sprintet mit zurück", "Jetzt darf Spieler sechs mit. Er sprintet sofort hinter den Ball zurück, und vorn heißt es drei gegen drei. Spieler fünf stellt Spieler siebzehn.",
       dr("r17", "b1", [65, 46.5]), mv("n6", [61, 37], delay=0.2), mv("n5", [69.5, 47.5], delay=0.3)),
     S("Abgefangen, zurück zum Trainer", "Spieler siebzehn will nach innen auf Spieler neun spielen. Spieler sechs ist schon da und fängt den Ball ab. Er spielt ihn zurück zum Trainer, und das Rondo beginnt von vorn.",
       mv("n6", [70, 35.5]), ps("b1", [70.6, 36.1], delay=0.3), ps("b1", [46.6, 55.9], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
