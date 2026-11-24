import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 51-P8 (U15-U17, Woche 23 Phase 3): False 9 Link Up Play to Attack (Wave). 40 x 30 Yards = 37 x 27 m (gerundet 25 x 35 m),
# drei Zonen 15 / 10 / 15 Yards = 14 / 9 / 14 m (gestrichelt, Hütchen an den Linienenden wie im PDF).
# LANGES FELD QUER (Vorbild ue317.py): Tore links und rechts (im PDF unten und oben), direkt in Querkoordinaten geplant
# (Feld x 9-89, y 4-51; 2 Einheiten je Yard in der Länge). Zwei Großfeldtore mit neutralen Torhütern (nur C- und B-Jugend).
# Vier Dreierteams im Original (Navy, Pink, Gelb, Hellblau): Auf der Tafel nur die zwei Teams der Welle. Das angreifende
# Dreierteam ist Team Neon (Nummern 7, 9, 11 wie im PDF), das Team der letzten Welle, das von hinten zurücksprintet, ist
# Team Rot, neu nummeriert 6, 8, 10 (Nummern doppelt). Die zwei wartenden Dreierteams nur im Text. Ein Trainer statt zwei:
# Er steht an der Seitenlinie auf Höhe der Mitte und spielt beide Richtungen an.
# Ablauf nach Video und PDF: Die Angreifer stehen an der Linie zum Angriffsdrittel, die Neun lässt sich in die mittlere Zone
# fallen, nimmt halb aufgedreht an (bl mit von + drehen) und schickt einen Flügelstürmer hinter die Abwehr.
# Fassungen: Progression 1 (Treffer = zweiter Ball gegen geordnete Abwehr), Progression 2 (zwei Dummys in der Mitte,
# Zuruf des Trainers links / rechts / Mitte). Die Seite im Zuruf gilt aus Sicht der Angreifer.
# Sichtkegel: Text "Scans to see recovering defenders - don't panic in possession", im Video nicht eingezeichnet. Richtung aus
# dem Sinn: Spieler neun schaut vor der Annahme über die Schulter zu den zurücksprintenden Verteidigern, dann zum Ball.
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie auf Höhe der Mitte
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
K = [P("k1", "t", 13, 27.5, "TW"), P("k2", "t", 85, 27.5, "TW")]
POS = {"n11": (62, 10.5), "n9": (64, 27.5), "n7": (62, 44.5), "r6": (24, 11), "r8": (26, 28.5), "r10": (24, 45.5)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + K + [T]
LINES = [rect(9, 4, 80, 47), line(39, 4, 39, 51), line(59, 4, 59, 51)]
TORE = [{"x": 9, "y": 27.5, "side": "left", "size": "gross"}, {"x": 89, "y": 27.5, "side": "right", "size": "gross"}]
ENDEN = [(39, 4), (39, 51), (59, 4), (59, 51)]
CONES = [C(x, y) for x, y in ENDEN]
DIMS = dims(9, 89, 4, 51, "35 m", "25 m")[:1]  # Tore links und rechts: nur die Längen-Maßlinie
BALL = [B("b1", 50.6, 55.9)] + ERSATZ
def zurueck(x=36, d=0.3):
    return [mv("r6", [x, 12], delay=d), mv("r8", [x, 33], delay=d), mv("r10", [x, 46], delay=d)]
# Steigerung 1: Team Rot steht schon geordnet vor dem Tor, Team Neon hat den zweiten Ball in der Mitte
POS2 = {"n11": (52, 11), "n9": (54, 28), "n7": (60, 43.5), "r6": (72, 14), "r8": (70, 30.5), "r10": (72, 47)}
# Steigerung 2: zwei Dummys in der mittleren Zone (alle Hütchen mit id, weil die Fassung eigene Hütchen hat)
CONES3 = [C(x, y, id=f"h{i + 1}") for i, (x, y) in enumerate(ENDEN)] + [C(47, 19, shape="stange", id="d1"), C(47, 36, shape="stange", id="d2")]

u = {"title": "Falsche Neun in der Welle", "code": "UE-364", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Umschalten", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 14,
 "field_size": "25 x 35 m",
 "description": "Angriffswellen mit drei Spielern auf zwei Tore, immer hin und her. Der Trainer spielt die falsche Neun an, die sich in die mittlere Zone fallen lässt, aufdreht und die Flügelstürmer hinter die Abwehr schickt. Das Team der letzten Welle sprintet von hinten zurück und verteidigt. Nach jedem Abschluss startet sofort die nächste Welle auf das andere Tor.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 35 Metern mit zwei großen Toren und Torhütern. Zwei gestrichelte Linien teilen es in drei Zonen, 14 Meter, in der Mitte 9 Meter, und wieder 14 Meter.",
  "Verteilen: Vier Dreierteams, jedes mit einer falschen Neun und zwei Flügelstürmern. Ein Team greift an, das Team der letzten Welle steht hinten, die beiden anderen warten an den Seiten. Der Trainer steht mit vielen Bällen an der Seitenlinie auf Höhe der Mitte.",
  "Ablauf: Der Trainer spielt die Neun an, die in die mittlere Zone kommt. Sie dreht auf und spielt die Flügelstürmer hinter der Abwehr an. Das Team der letzten Welle sprintet zurück und verteidigt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach greift das nächste Dreierteam sofort auf das andere Tor an, und die Angreifer von eben sprinten zurück und verteidigen."],
 "organisation_show": ORG,
 "coaching_points": ["Über die Schulter schauen, halb aufgedreht annehmen", "Flügelstürmer starten im richtigen Moment hinter die Kette", "Ist Platz da, früh abschließen", "Nach dem Angriff sofort zurücksprinten"],
 "materials": ["2 große Tore", "4 Hütchen", "2 Dummys", "Leibchen in vier Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Falsche Neun in der Welle. Drei gegen drei auf zwei Tore, immer hin und her. Die Spitze holt sich den Ball in der Mitte, und die Flügelstürmer laufen hinter die Abwehr.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BALL, "dims": DIMS,
  "steps": [
   S("Spieler neun kommt in die Mitte", "Team Neon greift zuerst an. Spieler neun lässt sich aus der Spitze in die mittlere Zone fallen. Er schaut kurz über die Schulter, wo Team Rot ist, dann zum Ball. Der Trainer spielt ihn an, und hinten sprintet Team Rot schon zurück.",
     mv("n9", [51, 29]), bl("n9", [50.3, 48], von=[33, 30], after=True), ps("b1", [51.6, 29.6], after=True), *zurueck()),
   S("Halb aufgedreht, steil auf Spieler sieben", "Spieler neun nimmt halb aufgedreht an und spielt sofort nach vorn. Spieler sieben ist außen hinter die Abwehr gestartet und bekommt den Ball in den Lauf. Spieler elf geht mit in die Mitte.",
     bl("n9", [72, 37.5], von=[50.3, 48], dauer=1.3), drehen("n9", [72, 37.5], gegen=True, delay=0.4), mv("n7", [77, 40], delay=0.4),
     ps("b1", [77.6, 40.6], after=True), mv("n11", [76, 20], delay=0.6), *zurueck(50, 0.2)),
   S("Früh abschließen: Punkt", "Spieler sieben wartet nicht, bis Team Rot zurück ist. Er schießt sofort, und das gibt einen Punkt für Team Neon. Jetzt geht es in die andere Richtung weiter. Der Trainer spielt das nächste Dreierteam an, das auf das andere Tor angreift, und Team Neon sprintet zurück und verteidigt.",
     ps("b1", [88.5, 31.5]), mv("n9", [40, 27], delay=1.0), mv("n11", [56, 9], delay=1.0), mv("n7", [60, 44], delay=1.0))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Wer mit dem ersten Angriff trifft, bekommt sofort einen zweiten Ball.", "Treffer gibt zweiten Ball",
    "Trifft das Dreierteam mit dem ersten Angriff, spielt der Trainer sofort einen zweiten Ball ein. Jetzt steht Team Rot schon geordnet vor dem Tor. Die Angreifer müssen sich gegen eine fertige Abwehr durchspielen und brauchen dafür mehr als einen Pass.",
    sp(POS2), BALL,
    [S("Zweiter Ball vom Trainer", "Der erste Angriff war drin. Sofort kommt der zweite Ball vom Trainer auf Spieler neun. Team Rot steht jetzt zu dritt geordnet vor dem Tor und wartet.",
       ps("b1", [54.6, 28.6])),
     S("Breit auf Spieler elf, die Neun startet", "Spieler neun spielt nach außen zu Spieler elf und läuft sofort in die Lücke zwischen Spieler sechs und Spieler acht. Spieler sechs geht raus zum Ball.",
       mv("n11", [60, 12]), ps("b1", [60.6, 12.6], after=True), mv("r6", [68, 11], delay=0.6), mv("n9", [74, 22], delay=0.8)),
     S("Pass in den Lauf: Punkt", "Spieler elf spielt flach in den Lauf von Spieler neun. Der schließt mit dem ersten Kontakt ab, und das gibt einen Punkt für Team Neon.",
       ps("b1", [74.6, 22.6]), ps("b1", [88.5, 24.5], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei Dummys stehen in der Mitte, und der Trainer ruft, wo sich Spieler neun anbietet.", "Dummys und Zuruf vom Trainer",
    "In der mittleren Zone stehen zwei Dummys. Kurz vor dem Pass ruft der Trainer links, rechts oder Mitte. Die Neun lässt sich genau in diese Lücke fallen, nimmt dort an und dreht auf. Links und rechts gelten aus Sicht der Angreifer.",
    sp(), BALL,
    [S("Der Trainer ruft: Links!", "Der Trainer ruft links. Spieler neun lässt sich in die Lücke links neben dem Dummy fallen und schaut zum Ball. Dort bekommt er ihn vom Trainer. Team Rot sprintet hinten zurück.",
       mv("n9", [52, 11.5]), bl("n9", [51.4, 31.5], after=True), ps("b1", [52.6, 12.1], after=True), *zurueck()),
     S("Aufdrehen, steil auf Spieler elf", "Spieler neun dreht auf und spielt steil. Spieler elf startet außen hinter die Abwehr und nimmt den Ball mit.",
       bl("n9", [72, 13.5], von=[51.4, 31.5], dauer=1.3), drehen("n9", [72, 13.5], gegen=True, delay=0.4), mv("n11", [77, 14], delay=0.4),
       ps("b1", [77.6, 14.6], after=True), *zurueck(50, 0.2)),
     S("Abschluss: Punkt", "Spieler elf zieht sofort ab, und das gibt einen Punkt für Team Neon. Beim nächsten Angriff ruft der Trainer eine andere Seite.",
       ps("b1", [88.5, 25]))], cones=CONES3)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
