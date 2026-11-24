import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P13 (U15-U17, Woche 28 Phase 5): The Back 4 Unit Advanced Lead. Kein PDF und kein Text: alles aus Video und Ton.
# Halbe Spielfeldhälfte: Länge im Video 10 + 40 Yards = 46 m (gerundet 45 m), Breite nach dem Video etwa 58 Yards = 53 m
# (gerundet 55 m). Kein Großfeld (halbes Feld), kein langes Feld (1,2): normal, Feld x 22-78, y 4-51, normale Figuren.
# Um 180 Grad gedreht (im Video liegt das große Tor unten): Tor oben, Team Rot greift nach oben an. Durch die Drehung stehen
# Spieler 2 und 11 links, 3 und 7 rechts. Rot (Viererkette) + grüner Torwart -> Team Neon (n1 TW, 2, 4, 5, 3), Blau (6, 8, 10
# im Mittelfeld, 7 und 11 außen, 9 vorn) -> Team Rot; Nummern wie im Video (eindeutig). Großfeldtor (nur C- und B-Jugend).
# Mittelfeldzone (10 Yards = 9 m) an der Mittellinie gestrichelt, darin die zwei Minitore in den Ecken; die zwei roten Puppen vor
# dem Mittelfeld als Stangen; Flügelzonen als Zonen von Team Rot (orange), darunter die gestrichelte Linie wie im Video.
# Ein Trainer an der Mittellinie (wie im Video). Halbkreise weggelassen.
# Grundform nach Ton und Video (0:07-0:50): Mittelfeld passt, Kette schiebt; Pass auf den Flügel, Außenverteidiger presst; der
# Flügelspieler dreht ab und spielt zurück nach innen (ab dann frei); Kette rückt gemeinsam raus, Spieler neun im Abseits.
# Ballgewinn und Treffer ins Minitor als Ergebnis (Ton: „If defenders win possession … finish in either of the two mini goals“);
# Punkt für Team Rot bei einem Treffer ins große Tor ergänzt.
# Fassungen: Coaching-Punkt aus dem Video („Full back must press winger …, but drop to cover“, „Over press leaves space in
# behind“) und Steigerung aus Ton/Video (zwei Mittelfeldspieler greifen mit an, fünf gegen vier; Torwart steht hoch und läuft
# den Ball hinter der Kette ab).
# Sichtkegel: Video-Schlussfolie „Awareness of runners moving in behind - checks“: Spieler vier schaut vor dem Herausrücken
# zu Spieler neun (aus dem Sinn). In der Steigerung ist im Video beim Torwart ein Kegel eingezeichnet („GK plays as a sweeper
# with high line“): Der Torwart schaut nach vorn zum Ball.
# Keine Dublette: UE-166 (03-P3), UE-177 (78-P3), UE-204, UE-206 (10-P7), UE-208 (78-P5), UE-212 (78-P6), UE-242 (78-P7),
# UE-250 (78-P12), UE-302, UE-320 (78-P4), UE-368, UE-370 (78-P8) haben kein Mittelfeld-Dreieck mit Schattenphase, keine
# Flügelzonen und keinen Start „live nach dem Rückpass nach innen“.
T = P("T", "c", 56.5, 55.3, "T")
ERSATZ = [B("s1", 60, 55.8), B("s2", 62.5, 55.8)]
POS = {"n1": (50, 10.5), "n2": (31, 22.5), "n4": (41.5, 18.5), "n5": (58.5, 18.5), "n3": (69, 22.5),
       "r9": (50, 27), "r6": (48, 49.5), "r10": (35, 45.5), "r8": (65, 45.5), "r11": (25.5, 38.5), "r7": (74, 38.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(22, 4, 56, 47), rect(32.7, 4, 34.8, 12.3), rect(41.2, 4, 17.8, 5.2), line(22, 44.3, 78, 44.3), line(22, 28.7, 78, 28.7),
         {"type": "zone", "x": 22, "y": 28.7, "w": 6, "h": 12.8, "color": "orange"},
         {"type": "zone", "x": 72, "y": 28.7, "w": 6, "h": 12.8, "color": "orange"}]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}, {"x": 27, "y": 51, "side": "bottom"}, {"x": 73, "y": 51, "side": "bottom"}]
CONES = [C(44, 44.3, shape="stange"), C(56.5, 44.3, shape="stange")]
DIMS = dims(22, 78, 4, 51, "55 m", "45 m", rx=86)

u = {"title": "Viererkette mit hoher Linie", "code": "UE-380", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 13,
 "field_size": "55 x 45 m",
 "description": "Die Viererkette mit Torwart verteidigt das große Tor gegen sechs Angreifer. Erst lassen drei Mittelfeldspieler den Ball laufen, und die Kette schiebt mit dem Ball. Geht der Pass auf einen Flügel, presst der Außenverteidiger, und nach dem Rückpass nach innen ist das Spiel frei. Die Kette rückt gemeinsam raus, stellt die Angreifer ins Abseits und kontert nach dem Ballgewinn auf zwei Minitore.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte, etwa 55 mal 45 Meter, mit großem Tor und Strafraum. An der Mittellinie eine Zone von 9 Metern Tiefe mit zwei Minitoren in den Ecken und zwei Stangen davor, außen zwei schmale Flügelzonen.",
  "Verteilen: Team Neon mit Torwart und Viererkette vor dem eigenen Strafraum. Team Rot mit drei Spielern in der Mittelfeldzone, je einem Flügelspieler in den Flügelzonen und einer Spitze. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Der Trainer spielt ins Mittelfeld, und die drei lassen den Ball laufen. Der Pass auf einen Flügel ist das Signal für den Außenverteidiger. Der Flügelspieler dreht ab und spielt zurück nach innen, ab dann ist das Spiel frei und die Kette rückt gemeinsam raus.",
  "Wertung: Ein Treffer von Team Rot ins große Tor gibt einen Punkt für Team Rot, ein Treffer von Team Neon in ein Minitor einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball ins Mittelfeld."],
 "organisation_show": ORG,
 "coaching_points": ["Die Kette schiebt immer mit dem Ball", "Außen pressen, aber nicht zu weit raus", "Über die Schulter schauen, wo die Läufer sind", "Zusammen raus, laut rufen"],
 "materials": ["1 Großfeldtor", "2 Minitore", "2 Stangen", "Hütchen für die Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette mit hoher Linie. Die Kette verteidigt gegen sechs Angreifer, schiebt mit dem Ball, presst außen und rückt gemeinsam raus.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 57.1, 55.9)] + ERSATZ,
  "steps": [
   S("Mittelfeld lässt den Ball laufen", "Der Trainer spielt zu Spieler sechs, und der gibt weiter zu Spieler zehn. Noch greift keiner an. Unsere Kette schiebt mit dem Ball zur Seite, alle vier zusammen.",
     ps("b1", [48.6, 50.1]), ps("b1", [35.6, 46.1], after=True),
     mv("n2", [29, 23.5], delay=1.0), mv("n4", [39, 19.5], delay=1.0), mv("n5", [55, 19.5], delay=1.0), mv("n3", [65, 22], delay=1.0)),
   S("Pass auf den Flügel, Spieler zwei presst", "Spieler zehn spielt raus auf Spieler elf. Das ist das Signal. Spieler zwei läuft ihn an, die anderen drei rücken nach und schieben zur Ballseite.",
     ps("b1", [26.1, 39.1]), mv("n2", [27, 31], delay=0.4), mv("n4", [37, 24], delay=0.6), mv("n5", [53, 22.5], delay=0.6), mv("n3", [63, 25], delay=0.6)),
   S("Rückpass nach innen, die Kette rückt raus", "Spieler elf dreht ab und spielt zurück zu Spieler zehn. Ab jetzt ist das Spiel frei. Spieler vier schaut kurz, wo Spieler neun steht, und ruft. Die ganze Kette rückt zusammen raus, Spieler neun steht im Abseits.",
     drehen("r11", [35, 45.5]), ps("b1", [35.6, 46.1], after=True), bl("n4", [50, 27], delay=0.4),
     mv("n2", [29, 32], delay=1.6), mv("n4", [41, 31.5], delay=1.6), mv("n5", [55, 31], delay=1.6), mv("n3", [64, 31.5], delay=1.6)),
   S("Abgefangen, ins Minitor: Punkt", "Spieler zehn spielt trotzdem steil. Spieler fünf ist näher dran, geht dazwischen und hat den Ball. Er dribbelt außen vorbei und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Spieler sechs.",
     ps("b1", [52.1, 35.6]), mv("n5", [51.5, 35], delay=0.2), dr("n5", "b1", [68, 38], after=True), ps("b1", [73, 50.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Außen pressen, aber nicht zu weit.", "Pressen, nicht zu weit",
    "Kommt der Ball auf den Flügel, läuft der Außenverteidiger an, so nah, dass der Flügelspieler nicht aufdrehen kann. Spielt der Flügelspieler zurück, geht der Außenverteidiger sofort zurück in die Kette. Läuft er weiter hinterher, ist hinter ihm ein großes Loch.",
    sp(), [B("b1", 65.6, 46.1)] + ERSATZ,
    [S("Pass raus, Spieler drei presst", "Spieler acht spielt raus auf Spieler sieben. Spieler drei läuft ihn an, aber nicht blind. Er bleibt so nah, dass Spieler sieben nicht aufdrehen kann. Die anderen schieben rüber.",
       ps("b1", [74.6, 39.1]), mv("n3", [73, 31], delay=0.4), mv("n5", [60, 21], delay=0.6), mv("n4", [46, 20.5], delay=0.6), mv("n2", [36, 21], delay=0.6)),
     S("Sofort zurück in die Kette", "Spieler sieben dreht ab und spielt zurück. Jetzt läuft Spieler drei nicht weiter hinterher. Er geht sofort zurück in die Kette, sonst ist hinter ihm ein großes Loch.",
       drehen("r7", [65, 45.5], gegen=True), ps("b1", [65.6, 46.1], after=True), mv("n3", [68, 24.5], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei aus dem Mittelfeld greifen mit an.", "Fünf gegen vier",
    "Nach dem Pass auf die Spitze dürfen zwei Mittelfeldspieler mit angreifen, und es steht fünf gegen vier. Die Kette muss jetzt genauer entscheiden, wann sie rausrückt. Weil sie hoch steht, steht auch der Torwart hoch und läuft Bälle hinter der Kette ab.",
    sp(), [B("b1", 35.6, 46.1)] + ERSATZ,
    [S("Steil, prallen lassen, nachrücken", "Spieler zehn spielt steil auf Spieler neun. Der lässt den Ball prallen auf Spieler sechs, der nachrückt. Jetzt greifen Spieler sechs und Spieler zehn mit an. Fünf gegen vier.",
       ps("b1", [50.6, 27.6]), mv("n5", [55, 24], delay=0.4), mv("r6", [48, 38], delay=0.2), ps("b1", [48.6, 38.6], after=True), mv("r10", [38, 33], delay=0.6)),
     S("Torwart steht hoch", "Unser Torwart rückt mit der Kette auf und steht vor dem Tor, nicht auf der Linie. Er schaut, was Spieler sechs vorhat.",
       mv("n1", [50, 17]), bl("n1", [48.6, 38.6], after=True)),
     S("Ball hinter die Kette, Torwart ist da", "Spieler sechs spielt den Ball hinter die Kette, Spieler elf startet. Der Torwart ist zuerst am Ball und fängt ihn. Jetzt geht es schnell auf die Minitore.",
       mv("r11", [26, 24]), mv("r11", [30, 16], after=True), ps("b1", [34, 12], delay=0.3), mv("n1", [33.4, 11.4], delay=0.5))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
