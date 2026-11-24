import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# The 10-P2 (U15-U17, Woche 33 Phase 2): How to Play the 10 Role, Practice 2 Possession Rondo. 20 x 25 Yards = 18 x 23 m
# (gerundet 18 x 25 m). Hochkant wie im PDF (Verhältnis unter 1,3), nicht gedreht. Feld x 30-70, y 7-53, Hütchen an den Ecken
# und in der Mitte jeder Seite wie im PDF.
# PDF pink (am Ball) -> Team Neon mit den Nummern aus dem PDF: innen 10, 8, 4, außen 9 (oben), 3 (rechts), 7 (links).
# PDF blau -> Team Rot, doppelte Nummern plus zehn: innen 4 -> 14, 8 -> 18, 10 -> 20 (Zehner von Team Rot), außen 7 -> 17,
# 9 -> 19; 2 bleibt. Ein Trainer (links mit Bällen wie im PDF). Positionen leicht verschoben (3D-Abstand).
# Grundform nach PDF und Video: Schulterblick des Zehners, Doppelbewegung (erst weg, dann in die Lücke), 8 -> 10, 10 dreht auf
# (Blick mit von + Drehpfeil), 4 startet in den Raum, 10 -> 4, 4 -> 9 nach außen. Wertung aus dem PDF (zehn Pässe plus
# Verbindung über den Zehner gibt einen Punkt), Wechsel bei Ballverlust aus dem PDF.
# Fassungen: Steigerung 1 = PDF Progression 1 (drei Zonen, der Zehner bleibt in der Mitte, Prallpass, dann auf der anderen
# Seite hinter dem Druck annehmen, wie im Video: 7 -> 10 -> 8 -> 3 -> 10). Steigerung 2 = Progression 2 (zwei Hälften, der Zehner
# nimmt von außen nur in der weiter entfernten Hälfte an, diagonaler Pass, erster Kontakt nach vorn).
# Minitore und Spielerzahl-Varianten aus dem Ton nicht übernommen (nur in players_min/max).
# Sichtkegel: Text „Check shoulders to see oppositions positions“, „constant scanning“, Ton „check their shoulders“, im Video
# eingeblendet „Check shoulders! Easy interception for defender“: Spieler zehn schaut über die Schulter zu Spieler vierzehn
# hinter sich, vor der Annahme zum Passgeber, nach der Annahme schwenkt der Kegel zum Passziel (bl mit von plus drehen).
T = P("T", "c", 14, 30, "T")
ERSATZ = [B("s1", 14.6, 34), B("s2", 12, 34)]
POS = {"n10": (49, 31), "n8": (52, 47), "n4": (65, 40), "n9": (40, 3.5), "n3": (74, 18), "n7": (26, 44),
       "r14": (40, 20), "r18": (58, 23), "r20": (40, 40), "r2": (26, 16), "r17": (74, 44), "r19": (40, 55.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def kurz(a, b, L=22):
    # Blickkegel nicht zu lang: Punkt in derselben Richtung, höchstens L Einheiten vom Spieler entfernt
    import math
    d = math.dist(a, b)
    return list(b) if d <= L else [round(a[0] + (b[0] - a[0]) * L / d, 1), round(a[1] + (b[1] - a[1]) * L / d, 1)]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def F(i, pos=POS): return fuss(pos[i])
LINES = [rect(30, 7, 40, 46)]
CONES = ecken(30, 7, 40, 46) + [C(50, 7), C(50, 53), C(30, 30), C(70, 30)]
DIMS = dims(30, 70, 7, 53, "18 m", "25 m", rx=82)
# Steigerung 1: drei Zonen, Zehner in der mittleren Zone, zwei von Team Rot schirmen oben ab
P1 = dict(n10=(49, 31), r20=(40, 31), r14=(54, 13), r18=(45, 15), n4=(63, 15), n9=(36, 3.8), n8=(58, 46))
# Steigerung 2: zwei Hälften; Spieler zwanzig und neunzehn stehen aus dem Weg des diagonalen Passes
P2 = dict(r20=(38, 47), r19=(61, 55.7))

u = {"title": "Rondo über den Zehner", "code": "UE-391", "kind": "Spielform",
 "focuses": ["Ballannahme", "Passspiel", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 16,
 "field_size": "18 x 25 m",
 "description": "Drei gegen drei im Feld, dazu stehen von jedem Team drei Spieler außen. Das Team am Ball sucht immer wieder seinen Zehner in der Mitte. Der nimmt an, dreht auf und spielt raus zu einem Mitspieler. Nach zehn Pässen mit so einer Verbindung über den Zehner gibt es einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern, an den Ecken und in der Mitte jeder Seite ein Hütchen.",
  "Verteilen: Zwei Teams mit je sechs Spielern. Je drei spielen im Feld, je drei stehen außen an den Linien. Jedes Team hat im Feld einen Zehner. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Das Team am Ball hält den Ball und spielt so oft wie möglich seinen Zehner an. Der dreht auf und spielt zu einem Mitspieler außen oder im Feld. Fängt das andere Team den Ball ab, spielt es genauso über seinen Zehner.",
  "Wertung und Wechsel: Zehn Pässe in Folge mit einer Verbindung über den Zehner geben einen Punkt. Danach bringt der Trainer einen neuen Ball. Nach ein paar Minuten tauschen die Spieler außen und innen."],
 "organisation_show": ORG,
 "coaching_points": ["Schulterblick, bevor der Ball kommt", "Offen stehen, mit dem hinteren Fuß annehmen", "Erst weg, dann in die Lücke", "Zwischen den Gegnern anbieten"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rondo über den Zehner. Drei gegen drei im Feld, dazu sechs Spieler außen. Wir suchen den Zehner, er dreht auf und spielt raus.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", *F("n8"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Erst weg, dann in die Lücke", "Team Neon hat den Ball. Spieler zehn geht erst einen Schritt weg und kommt sofort in die Lücke zurück. Dabei schaut er über die Schulter, wo die Gegner stehen, und dann zum Ball.",
     mv("n10", [54, 25]), mv("n10", [47, 32], after=True), bl("n10", POS["n8"], von=POS["r14"], dauer=1.3, after=True)),
   S("Pass in den Fuß", "Jetzt ist er frei. Spieler acht spielt flach in den Fuß.",
     ps("b1", [47.6, 32.6])),
   S("Aufdrehen, Pass auf Spieler vier", "Spieler zehn dreht mit dem ersten Kontakt auf. Spieler vier ist schon in den freien Raum gestartet und bekommt den Ball.",
     bl("n10", [66, 25], von=POS["n8"], dauer=1.3), drehen("n10", [66, 25], gegen=True, delay=0.4), mv("n4", [66, 25], delay=0.2),
     ps("b1", [66.6, 25.6], after=True)),
   S("Raus nach außen: Punkt", "Spieler vier spielt direkt raus zu Spieler neun. Nach zehn Pässen mit so einer Verbindung über den Zehner gibt das einen Punkt für Team Neon. Fängt Team Rot den Ball ab, spielt Team Rot genauso über seinen Zehner, Spieler zwanzig.",
     ps("b1", F("n9")))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: drei Zonen, und der Zehner bleibt in der Mitte.", "Drei Zonen, prallen lassen",
    "Zwei Linien teilen das Feld in drei Zonen. Der Zehner spielt nur in der mittleren Zone. Er lässt den Ball prallen und löst sich sofort auf die andere Seite, weg vom Druck. Dort bekommt er den nächsten Pass, hinter seinem Gegenspieler.",
    sp(**P1), [B("b1", *F("n7"))] + ERSATZ,
    [S("Anspiel in die Mittelzone", "Spieler zehn darf nur in der mittleren Zone spielen. Er schaut zu Spieler sieben, und der spielt ihn von außen an. Spieler zwanzig drückt sofort.",
       bl("n10", kurz(P1["n10"], POS["n7"])), ps("b1", F("n10", P1), after=True), mv("r20", [44, 32], delay=0.8)),
     S("Prallen lassen, Seite wechseln", "Spieler zehn lässt direkt prallen auf Spieler acht. Dann löst er sich weg vom Druck, auf die andere Seite der Zone.",
       ps("b1", F("n8", P1)), mv("n10", [61, 26], after=True)),
     S("Hinter dem Druck annehmen", "Spieler acht spielt raus zu Spieler drei. Spieler zehn schaut schon dahin, und von dort kommt der Ball zurück, hinter dem Rücken von Spieler zwanzig.",
       ps("b1", F("n3"), bend=-3), bl("n10", POS["n3"], delay=0.3), ps("b1", [61.6, 26.6], after=True))],
    lines=LINES + [line(30, 22.3, 70, 22.3), line(30, 37.7, 70, 37.7)]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Zehner nimmt nur in der weiten Hälfte an.", "Nur in der weiten Hälfte",
    "Eine Linie teilt das Feld in zwei Hälften. Von außen darf der Zehner nur in der Hälfte angespielt werden, die weiter weg ist. So kommen diagonale Pässe, und der Zehner muss früh den freien Raum finden. Nimmt er in der falschen Hälfte an, bekommt das andere Team den Ball.",
    sp(**P2), [B("b1", *F("n7"))] + ERSATZ,
    [S("Weg vom Ball, rüber", "Jetzt teilt eine Linie das Feld in zwei Hälften. Spieler sieben hat den Ball außen. Spieler zehn darf ihn nur in der anderen Hälfte annehmen, also läuft er rüber.",
       mv("n10", [60, 34])),
     S("Diagonal in die weite Hälfte", "Spieler zehn schaut zum Ball. Spieler sieben spielt diagonal durch das Feld, an Spieler zwanzig vorbei.",
       bl("n10", kurz((60, 34), POS["n7"])), ps("b1", [60.6, 34.6], after=True)),
     S("Erster Kontakt nach vorn", "Spieler zehn nimmt mit dem hinteren Fuß an und dreht auf, der erste Kontakt geht nach vorn. Dann spielt er raus zu Spieler drei.",
       bl("n10", POS["n3"], von=kurz((60, 34), POS["n7"]), dauer=1.3), drehen("n10", POS["n3"], delay=0.4), dr("n10", "b1", [63, 30], after=True),
       ps("b1", F("n3"), after=True))],
    lines=LINES + [line(50, 7, 50, 53)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
