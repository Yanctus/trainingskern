import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 90-P9 (U15-U17, Woche 27 Phase 2): CAM Receiving to Attack in the Final Third. 50 x 45 Yards = 46 x 41 m, gerundet 45 x 40 m.
# Feld x 22-78, y 5-55 (fast gleicher Maßstab in beiden Richtungen), Tor oben wie im PDF, nicht gedreht. Kein Großfeld (halbes Feld).
# Die zwei grauen Querstreifen im PDF sind die Zonen der Verteidiger: hier orange Zonen (Team Rot). Dazwischen der Raum der Zehner.
# Navy -> Team Neon (Nummern wie im PDF: hinten 6, 4, 8; Zehner 10 und 11; Spitze 9). Pink/orange -> Team Rot, neu nummeriert,
# weil doppelt: vorn 3 bleibt, 4 -> 5; Mittelfeldzone 6 -> 2, 8 -> 7. Grüner Torwart 1 -> Torwart von Team Rot (r1, TW).
# Großfeldtor (nur C- und B-Jugend). Ein Trainer statt zwei, links an der Seite bei den drei Aufbauspielern.
# Grundform nach PDF und Video 0:08-0:40: 6 -> 4 -> 10 zwischen die Linien, 10 dreht auf und dribbelt auf die Lücke, ein Verteidiger
# (hier Spieler fünf) muss raus, 9 startet in die Tiefe und schließt ab. Wertung nach dem PDF-Text (abgefangen und zurück zu den
# drei hinten = Punkt für Team Rot).
# Fassungen wie die PDF-Progressionen: 1 die zwei aus der Mittelfeldzone dürfen zurückarbeiten, 2 ein Verteidiger darf auf den
# Pass zum Zehner springen; dann zieht der Zehner weg, der Ball geht direkt auf die Spitze, die ablegt (Ton und Video 1:37-1:54).
# Sichtkegel aus PDF und Ton („Scanning before receiving“, „scanning consistently for oncoming pressure“): Annehmen und Aufdrehen
# mit bl(von=...) und drehen() in Grundform und erster Steigerung. In der zweiten Steigerung bekommt nach der Sichtkegel-Regel
# (Inhaber, 25.11.2026) der Passgeber hinten den Kegel (er sieht den freien Weg auf die Spitze), nicht der wegziehende Zehner.
# Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Kein Dubletten-Fall: UE-290 (1-P24) ist Einzeltraining eins gegen eins ohne Zonen und Aufbauspieler.
T = P("T", "c", 14, 44, "T")
ERSATZ = [B("s1", 10.6, 47.5), B("s2", 13.4, 48.6)]
NEON = {"n6": (30, 48), "n4": (50, 52), "n8": (70, 48), "n11": (29, 30), "n10": (51, 31), "n9": (69, 21)}
ROT = {"r1": (50, 9), "r3": (38, 21), "r5": (60, 21), "r2": (40, 39), "r7": (61, 39)}
def sp(**k):
    d = {**NEON, **ROT}; d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
def f(i): x, y = {**NEON, **ROT}[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(22, 5, 56, 50), {"type": "zone", "x": 22, "y": 17.2, "w": 56, "h": 8, "color": "orange"},
         {"type": "zone", "x": 22, "y": 35.2, "w": 56, "h": 8.1, "color": "orange"}]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}]
DIMS = dims(22, 78, 5, 55, "45 m", "40 m", rx=86)
VIER = [50, 52]

u = {"title": "Linie überspielen, aufdrehen", "code": "UE-377", "kind": "Spielform",
 "focuses": ["Ballannahme", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 11,
 "field_size": "45 x 40 m",
 "description": "Hinten bauen drei Spieler von Team Neon geduldig auf und suchen den Pass zwischen die Linien zu den beiden Zehnern. Team Rot verteidigt in zwei Zonen und darf sie zuerst nicht verlassen. Bekommt ein Zehner den Ball, dreht er auf und dribbelt auf die Abwehr zu. Mit Spieler neun und dem zweiten Zehner geht es dann drei gegen zwei aufs Tor.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 40 Metern mit einem Tor und Torwart. Zwei Querstreifen sind die Zonen von Team Rot, dazwischen liegt der Raum für die Zehner. Der Trainer steht mit Bällen an der Seite.",
  "Verteilen: Team Neon mit drei Spielern hinten, zwei Zehnern zwischen den Zonen und Spieler neun vorn. Team Rot mit zwei Spielern in der Mittelfeldzone, zwei Verteidigern in der Abwehrzone und dem Torwart.",
  "Ablauf: Die drei hinten passen geduldig, bis eine Lücke für den Pass zum Zehner aufgeht. Der Zehner dreht auf und dribbelt auf die Abwehr zu. Zieht er einen Verteidiger auf sich, spielt er den freien Mitspieler an, und es geht drei gegen zwei aufs Tor.",
  "Wertung: Jeder Treffer gibt einen Punkt für Team Neon. Fängt Team Rot einen Pass ab und spielt den Ball zurück zu den drei hinten, gibt das einen Punkt für Team Rot. Danach startet hinten der nächste Angriff."],
 "organisation_show": ORG,
 "coaching_points": ["Im richtigen Moment in die Lücke, nicht zu früh", "Offen stehen, damit der Blick nach vorn geht", "Vor der Annahme über die Schulter schauen", "Erster Kontakt nach vorn, weg vom Gegner"],
 "materials": ["1 Großfeldtor", "Hütchen für die Zonen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Linie überspielen, aufdrehen. Hinten wird geduldig aufgebaut, bis der Pass zwischen die Linien geht. Dann dreht der Zehner auf und greift die Abwehr an.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *f("n6"))] + ERSATZ,
  "steps": [
   S("Hinten geduldig aufbauen", "Hinten haben die drei den Ball. Spieler sechs spielt flach zu Spieler vier. Team Rot bleibt in seinen Zonen und macht die Wege zu.",
     ps("b1", f("n4")), mv("r2", [43, 39], delay=0.4), mv("r7", [58, 39], delay=0.4)),
   S("Pass zwischen die Linien", "Spieler zehn bietet sich in der Lücke an und schaut zum Ball. Spieler vier spielt flach zwischen Spieler zwei und Spieler sieben hindurch.",
     bl("n10", VIER), ps("b1", f("n10"), after=True)),
   S("Aufdrehen und andribbeln", "Spieler zehn nimmt an, dreht auf und geht mit Tempo auf die Abwehr. Spieler fünf muss raus und ihn stellen. Genau jetzt starten Spieler neun und Spieler elf in die Tiefe.",
     bl("n10", [66, 14], von=VIER, dauer=1.3), drehen("n10", [66, 14], delay=0.4), dr("n10", "b1", [55, 25], after=True),
     mv("r5", [55, 19.5], delay=1.4), mv("n9", [68, 12], delay=1.6), mv("n11", [33, 15], delay=1.4)),
   S("Steil in den Lauf: Punkt", "Spieler zehn spielt steil in den Lauf von Spieler neun. Der schießt am Torwart vorbei, und das gibt einen Punkt für Team Neon. Fängt Team Rot einen Pass ab und spielt ihn zurück zu den drei hinten, gibt das einen Punkt für Team Rot. Dann startet hinten der nächste Angriff.",
     ps("b1", [68.6, 12.6]), ps("b1", [54, 5.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei Verteidiger dürfen zurückarbeiten.", "Zwei dürfen zurückarbeiten",
    "Sobald der Pass zwischen die Linien gespielt ist, dürfen die zwei Spieler aus der Mittelfeldzone zurücklaufen und den Zehner jagen. Er hat jetzt weniger Zeit. Wer offen steht und mit dem ersten Kontakt nach vorn geht, ist trotzdem weg.",
    sp(), [B("b1", *f("n4"))] + ERSATZ,
    [S("Pass ins Loch, zwei jagen nach", "Spieler zehn schaut zum Ball, und Spieler vier spielt ihn an. Sofort drehen Spieler zwei und Spieler sieben um und laufen ihm hinterher.",
       bl("n10", VIER), ps("b1", f("n10"), after=True), mv("r2", [44, 33], after=True), mv("r7", [58, 34], delay=1.5)),
     S("Erster Kontakt nach vorn", "Spieler zehn hat sich offen hingestellt. Er dreht mit dem ersten Kontakt auf und ist an beiden vorbei. Links startet Spieler elf hinter die Abwehr.",
       bl("n10", [38, 12], von=VIER, dauer=1.3), drehen("n10", [38, 12], gegen=True, delay=0.4), dr("n10", "b1", [49, 24], after=True),
       mv("r2", [47, 29], delay=1.5), mv("r7", [53, 29], delay=1.5), mv("n11", [31, 20], delay=1.0), mv("n11", [38, 12], after=True)),
     S("Steil auf Spieler elf: Punkt", "Der Ball geht steil auf Spieler elf. Der schließt sofort ab, und das gibt einen Punkt für Team Neon.",
       ps("b1", [38.6, 12.6]), ps("b1", [46, 5.3], after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Verteidiger darf rausspringen.", "Verteidiger springt raus",
    "Jetzt darf einer der beiden Verteidiger auf den Pass zum Zehner springen. Springt er, zieht der Zehner weg. Hinten sieht der Passgeber den freien Weg und spielt direkt auf Spieler neun. Der legt ab, und der Zehner kommt mit Blick nach vorn an den Ball.",
    sp(), [B("b1", *f("n4"))] + ERSATZ,
    [S("Er springt, der Zehner zieht weg", "Spieler fünf springt raus auf den Zehner. Also zieht Spieler zehn weg in den freien Raum, und Spieler neun kommt dem Ball entgegen.",
       mv("r5", [52, 27]), mv("n10", [60, 31], delay=0.2), mv("n9", [57, 22])),
     S("Direkt auf die Spitze, ablegen", "Spieler vier schaut nach vorn. Der Weg zu Spieler neun ist jetzt frei, also spielt er ihn direkt an. Spieler neun legt ab auf Spieler zehn, und der hat das Spiel jetzt vor sich.",
       bl("n4", [54.5, 32.5]), ps("b1", [57.6, 22.6], after=True), ps("b1", [60.6, 31.6], after=True)),
     S("Nur noch einer hinten: Punkt", "Spieler fünf ist raus, hinten steht nur noch Spieler drei. Spieler zehn dribbelt an, und Spieler neun dreht ab in die Tiefe. Er bekommt den Ball und trifft, und das gibt einen Punkt für Team Neon.",
       mv("n9", [66, 14]), mv("n11", [33, 15], delay=0.2), dr("n10", "b1", [61, 25], delay=0.3), ps("b1", [66.6, 14.6], after=True), ps("b1", [54, 5.3], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
