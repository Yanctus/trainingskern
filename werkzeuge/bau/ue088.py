import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P4: 25 x 30 Yards, gedreht: Feld x 21.5-78.5, y 6.25-53.75, Mittelquadrat 5 x 5 Yards (Hütchen bei 45.25/54.75 und 25.25/34.75).
# An jeder Ecke eine Station: Ballspieler 1-4, Wandspieler 5-8. Gegen den Uhrzeigersinn: oben links -> unten links -> unten rechts -> oben rechts.
T = P("T", "c", 88, 30, "T")
X = {"n1": (30, 10), "n2": (70, 10), "n3": (70, 50), "n4": (30, 50)}
Y = {"n5": (21.5, 6.25), "n6": (78.5, 6.25), "n7": (78.5, 53.75), "n8": (21.5, 53.75)}
mitte = {"n1": (43.6, 23.6), "n2": (56.4, 23.6), "n3": (56.4, 36.4), "n4": (43.6, 36.4)}
ziel = {"n1": (23, 52), "n2": (23, 8), "n3": (77, 8), "n4": (77, 52)}          # Pass zur nächsten Station
lauf = {"n1": (31, 41), "n2": (34, 15), "n3": (69, 19), "n4": (66, 45)}         # Lauf für den Doppelpass
mitte2 = {"n1": (42, 21), "n2": (58, 21), "n3": (58, 39), "n4": (42, 39)}
naechste = {"n1": (43.6, 36.4), "n2": (43.6, 23.6), "n3": (56.4, 23.6), "n4": (56.4, 36.4)}
X2 = {"n1": (30, 10), "n2": (69, 17), "n3": (70, 50), "n4": (31, 43)}
def sp(xs=X): return [P(k, "a", *v, k[1:]) for k, v in xs.items()] + [P(k, "a", *v, k[1:]) for k, v in Y.items()] + [T]
def bl(xs=X): return [B("b" + k[1:], x + 1.6, y + 0.6) for k, (x, y) in xs.items()]
cones = ecken(21.5, 6.25, 57, 47.5) + [C(45.25, 25.25), C(54.75, 25.25), C(45.25, 34.75), C(54.75, 34.75)]
u = {"title": "Dribbeln, drehen, Doppelpass", "code": "UE-088", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 23 m",
 "description": "An jeder Ecke des Feldes stehen zwei Spieler, einer davon mit Ball. Alle vier Ballspieler dribbeln gleichzeitig zu einem Hütchen im Mittelquadrat, drehen sich mit einem Kontakt und passen zur nächsten Station gegen den Uhrzeigersinn. Mit dem Spieler dort spielen sie einen Doppelpass und dribbeln zum nächsten Hütchen in der Mitte. So läuft der Ball ständig im Kreis.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 23 Metern, in der Mitte ein kleines Quadrat von fünf mal fünf Metern mit vier Hütchen.",
  "Verteilen: An jeder Ecke zwei Spieler, einer mit Ball.",
  "Ablauf: Alle vier Ballspieler dribbeln gleichzeitig zu ihrem Hütchen in der Mitte, drehen mit einem Kontakt und passen zur nächsten Station gegen den Uhrzeigersinn. Dann Doppelpass mit dem Spieler dort und weiter zum nächsten Hütchen in der Mitte.",
  "Pausen: Nach einer festen Zeit eine kurze Pause. Klappt es mit vier Bällen noch nicht, erst mit zwei Bällen beginnen."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball beim Dribbeln eng unter Kontrolle halten", "Schnelle Doppelpässe mit einem Kontakt", "Kopf hoch und vor jedem Pass rufen", "Genau und mit dem richtigen Tempo passen, damit alles im Fluss bleibt"],
 "materials": ["8 Hütchen", "4 Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Dribbeln, drehen, Doppelpass. Vier Ballspieler arbeiten gleichzeitig, und der Ball läuft ständig im Kreis.",
 "board": {"lines": [rect(21.5, 6.25, 57, 47.5)], "cones": cones, "players": sp(), "balls": bl(),
  "steps": [
   S("Alle dribbeln zur Mitte", "Alle vier Ballspieler dribbeln gleichzeitig zu ihrem Hütchen im Mittelquadrat.", *[dr(k, "b" + k[1:], list(mitte[k])) for k in X]),
   S("Drehen und passen", "Am Hütchen drehen sich alle mit einem Kontakt und passen gleichzeitig zur nächsten Station gegen den Uhrzeigersinn.", *[ps("b" + k[1:], list(ziel[k])) for k in X]),
   S("Doppelpass", "Gleichzeitig laufen alle ihrem Pass hinterher, und der Spieler an der Station spielt direkt zurück.",
     *[m for k in X for m in (mv(k, list(lauf[k])), ps("b" + k[1:], [lauf[k][0] + 1.6, lauf[k][1] + 0.6], delay=0.3))]),
   S("Zum nächsten Hütchen", "Alle dribbeln zum nächsten Hütchen in der Mitte, und alles beginnt von vorn.", *[dr(k, "b" + k[1:], list(naechste[k])) for k in X])],
  "dims": [{"x1": 21.5, "y1": 58.6, "x2": 78.5, "y2": 58.6, "text": "27 m"}, {"x1": 95, "y1": 6.25, "x2": 95, "y2": 53.75, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Am Hütchen schnell drehen, ohne den Ball zu verlieren.", "Schnell drehen am Hütchen",
    "Am Hütchen dreht sich der Spieler mit einem Kontakt in die Richtung des nächsten Passes. Der Ball bleibt dabei eng am Fuß, der Kopf geht schon vorher hoch. Je sauberer die Drehung, desto flüssiger läuft die ganze Übung.",
    sp(mitte2), bl(mitte2),
    [S("Mit einem Kontakt drehen", "Alle vier drehen sich gleichzeitig mit einem Kontakt zur nächsten Station.",
       dr("n1", "b1", [40.5, 23]), dr("n2", "b2", [59.5, 19]), dr("n3", "b3", [60, 37.5]), dr("n4", "b4", [40.5, 41])),
     S("Pass in die neue Richtung", "Sofort folgt der Pass zur nächsten Station.", *[ps("b" + k[1:], list(ziel[k])) for k in X])]),
  V("Steigerung", "Und jetzt die Steigerung: Erst an der Linie entlang dribbeln, dann Doppelpass mit dem Eckspieler.", "An der Linie entlang",
    "Die Ballspieler dribbeln zuerst an der Außenlinie entlang, spielen einen Doppelpass mit dem Spieler an der nächsten Ecke und dribbeln dann zum Hütchen in der Mitte. Von dort passen sie zur nächsten Station und laufen ihrem Pass bis in die Ecke hinterher. Alle Stationen arbeiten gleichzeitig, wir schauen auf zwei davon.",
    sp(X2), bl(X2),
    [S("An der Linie entlang", "Alle dribbeln gleichzeitig an ihrer Außenlinie entlang, Spieler eins oben und Spieler drei unten.", dr("n1", "b1", [50, 9.5]), dr("n3", "b3", [50, 50.5]), dr("n2", "b2", [75, 32]), dr("n4", "b4", [25, 28])),
     S("Doppelpass mit dem Eckspieler", "Beide spielen einen Doppelpass mit dem Spieler an der nächsten Ecke.",
       ps("b1", [77, 8]), mv("n1", [60, 17], delay=0.2), ps("b1", [61.6, 17.6], after=True),
       ps("b3", [23, 52]), mv("n3", [40, 43], delay=0.2), ps("b3", [41.6, 43.6], after=True)),
     S("Zur Mitte und weiter", "Beide dribbeln zum Hütchen in der Mitte, passen zur nächsten Station und laufen dem Pass in die Ecke hinterher.",
       dr("n1", "b1", [56.4, 23.6]), ps("b1", [77, 52], after=True), mv("n1", [72, 47], after=True),
       dr("n3", "b3", [43.6, 36.4]), ps("b3", [23, 8], after=True), mv("n3", [28, 13], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
