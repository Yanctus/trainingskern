import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-98 (U12-U14, Woche 2 Pre-Season): Technical Combinations & Agility Circuit. 40 x 30 Yards = Feld x 16-84, y 5-56 (36 x 27 m).
# Elf Spieler (ein Team, Neon) auf zwei gespiegelten Kreisläufen. Gezeigt wird der rechte Kreislauf bis zum letzten Pass nach links.
# Leitern senkrecht (leiter_ou), Hürden quer (huerde). Leitern als Leiter gezeichnet (22.11.2026). Einige Positionen leicht verschoben (3D-Abstand), ein Trainer statt zwei.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft: "Pull away to receive back foot" = offen annehmen).
T = P("T", "c", 91, 45, "T")
POS = {"n9": (35.9, 8.5), "n2": (80.7, 9.5), "n7": (56.3, 12.5), "n6": (41.8, 25.6), "n3": (54.7, 28.6), "n4": (73.9, 29.6),
       "n8": (31, 32.8), "n5": (41.1, 41.5), "n11": (27.6, 49), "n10": (56.3, 52.8), "n12": (66.2, 54.1)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 92.6, 48.5), B("s2", 94, 42)]
BAELLE = [B("b1", 66.8, 54.7)] + ERSATZ
LINES = [rect(16, 5, 68, 51)]
KEGEL = [C(19.1, 22.1), C(19.6, 39.3), C(20.9, 52.5), C(28.5, 36.5), C(37.9, 39.3), C(44.8, 26.1), C(52.4, 28.3), C(59.8, 15.5),
         C(69.9, 28.3), C(78.8, 18.8), C(80.4, 38), C(82, 12.5)] \
      + [C(x, 10.2, shape="huerde") for x in (65.1, 69.6, 74.5)] + [C(x, 52.4, shape="huerde") for x in (26.1, 31, 35)] \
      + [leiter(63.8, 44.5, senkrecht=True), leiter(35.8, 18, senkrecht=True)]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Kombinieren im Parcours", "code": "UE-132", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 11, "players_max": 14, "field_size": "36 x 27 m",
 "description": "Ein Kreislauf aus Pässen, Leitern und Hürden auf zwei gespiegelten Seiten. Der Erste passt zum Hütchen an der Seite und läuft durch die Leiter. Ein Mitspieler kommt dem Pass entgegen, dreht auf und spielt nach vorn, ein anderer kommt zum Hütchen und spielt quer. Von dort geht der Ball steil auf einen Spieler, der gerade über die Hürden springt, und der letzte Pass geht zur Leiter auf der anderen Seite. Dort beginnt der Ablauf in die andere Richtung.",
 "organisation": ["Aufbauen: Ein Feld von 36 mal 27 Metern mit zwei gleichen Kreisläufen, die gegeneinander gedreht sind. Jeder hat eine Leiter, drei Minihürden und mehrere Hütchen, an denen die Spieler annehmen.",
  "Verteilen: Etwa elf Spieler stehen an den Hütchen und Geräten, ein Spieler unten rechts hat den Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass zum Hütchen an der Seite, der Passgeber läuft durch die Leiter. Der Mitspieler kommt zum Hütchen, dreht mit dem ersten Kontakt auf und spielt nach vorn. Der Nächste nimmt am Hütchen an und spielt quer, der Ball geht steil auf den Spieler, der über die Hürden springt, und der spielt zur Leiter auf der anderen Seite.",
  "Regel: Höchstens zwei Kontakte. Der Spieler an der Leiter beginnt den Ablauf sofort wieder von vorn, in die andere Richtung. Nach jedem Pass rücken die Spieler eine Station weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen, damit der Ablauf flüssig bleibt", "Sauber und schnell durch Leiter und Hürden", "Im richtigen Moment zum Hütchen starten", "Mit dem ersten Kontakt aufdrehen und laut ansagen"],
 "materials": ["12 Hütchen", "2 Koordinationsleitern", "6 Minihürden", "Viele Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Kombinieren im Parcours. Ein Kreislauf aus schnellen Pässen, Leiter und Hürden, bei dem der Ball nie stehen bleibt.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Pass zum Hütchen, ab in die Leiter", "Spieler zwölf passt zum Hütchen an der Seite, und Spieler vier kommt im selben Moment entgegen. Spieler zwölf läuft durch die Leiter nach oben.",
     ps("b1", [78.6, 36.1]), mv("n4", [78, 35.5]), *weg("n12", [[63.8, 54], [63.8, 35], [66, 33]], after=True)),
   S("Aufdrehen, Pass nach vorn", "Spieler vier dreht mit dem ersten Kontakt auf und spielt nach vorn. Spieler sieben kommt zum Hütchen oben und nimmt an.",
     mv("n7", [76.2, 17.2]), ps("b1", [76.8, 17.8], delay=0.3)),
   S("Quer und steil über die Hürden", "Spieler sieben spielt quer zu Spieler drei. Der spielt sofort steil, und Spieler zwei springt über die Hürden und nimmt den Ball im Lauf an.",
     ps("b1", [55.3, 29.2]), mv("n2", [76, 10.2], after=True), mv("n2", [60, 10.2], after=True), ps("b1", [56.6, 11.9], after=True), mv("n2", [56, 11.3], after=True)),
   S("Pass zur Leiter, andere Seite", "Spieler zwei spielt den letzten Pass zu Spieler neun an der Leiter links oben. Der beginnt den Ablauf sofort in die andere Richtung: Pass zum Hütchen, Spieler acht kommt entgegen, und Spieler neun läuft durch die Leiter.",
     ps("b1", [36.5, 9.1]), ps("b1", [22.6, 25.1], after=True), mv("n8", [22, 25.5], after=True), *weg("n9", [[35.8, 9], [35.8, 27.5], [33.5, 29.5]], after=True))],
  "dims": dims(16, 84, 5, 56, "36 m", "27 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im richtigen Moment starten.", "Das Timing",
    "Wer zu früh zum Hütchen läuft, steht und wartet. Wer zu spät kommt, lässt den Ball durchlaufen. Der Mitspieler startet genau dann, wenn der Passgeber den Ball spielt, und kommt mit Tempo am Hütchen an. Ein kurzer Ruf hilft: Jetzt!",
    sp(), BAELLE,
    [S("Pass und Start zugleich", "Spieler zwölf spielt, und genau in diesem Moment startet Spieler vier zum Hütchen. Beide kommen gleichzeitig dort an.",
       ps("b1", [78.6, 36.1]), mv("n4", [78, 35.5])),
     S("Mit Tempo weiter", "So kann Spieler vier ohne Pause aufdrehen und weiterspielen, und Spieler zwölf läuft schon durch die Leiter. Dann ist Spieler sieben dran.",
       ps("b1", [76.8, 17.8]), mv("n7", [76.2, 17.2], delay=0.1), *weg("n12", [[63.8, 54], [63.8, 35], [66, 33]]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit dem ersten Kontakt aufdrehen.", "Offen annehmen",
    "Am Hütchen nimmt der Spieler den Ball offen mit dem hinteren Fuß an. So dreht er sich mit dem ersten Kontakt schon in die neue Richtung und kann sofort weiterspielen. Wer den Ball erst stoppt und sich dann dreht, bremst den ganzen Kreislauf.",
    sp(n4=(78, 35.5)), [B("b1", 78.6, 36.1)] + ERSATZ,
    [S("Erster Kontakt nach vorn", "Spieler vier nimmt den Ball mit dem hinteren Fuß an und dreht sich mit dem ersten Kontakt nach vorn.",
       dr("n4", "b1", [77.5, 31])),
     S("Sofort weiter", "Mit dem zweiten Kontakt spielt er schon zu Spieler sieben, der zum Hütchen oben kommt. Danach geht es quer zu Spieler drei.",
       mv("n7", [76.2, 17.2]), ps("b1", [76.8, 17.8], delay=0.2), ps("b1", [55.3, 29.2], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball.", "Zwei Bälle",
    "Jetzt startet auf der anderen Seite gleichzeitig ein zweiter Ball. Beide Kreisläufe laufen zur selben Zeit, die Spieler müssen sich mehr konzentrieren und dürfen sich nicht in die Quere kommen.",
    sp(), BAELLE + [B("b2", 36.5, 9.1)],
    [S("Beide Seiten zugleich", "Spieler zwölf unten rechts und Spieler neun oben links passen gleichzeitig zu ihren Hütchen. Spieler vier und Spieler acht kommen entgegen.",
       ps("b1", [78.6, 36.1]), mv("n4", [78, 35.5]), ps("b2", [22.6, 25.1], delay=0.1), mv("n8", [22, 25.5], delay=0.1)),
     S("Zwei Abläufe laufen", "Beide drehen auf und spielen nach vorn zu Spieler sieben und Spieler fünf, die Passgeber laufen durch ihre Leitern. Jetzt laufen zwei Bälle zugleich durch den Parcours, und es geht immer weiter.",
       ps("b1", [76.8, 17.8]), mv("n7", [76.2, 17.2]), *weg("n12", [[63.8, 54], [63.8, 35], [66, 33]], delay=0.2),
       mv("n5", [23.2, 42], delay=0.1), ps("b2", [23.8, 42.6], delay=0.15), *weg("n9", [[35.8, 9], [35.8, 27.5], [33.5, 29.5]], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
