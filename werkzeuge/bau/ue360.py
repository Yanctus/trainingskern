import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 35-P2 (U15-U17, Woche 22 Phase 5): Compact Defending to Win Possession (How to Defend as a Compact Unit).
# 30 x 30 Yards = 27 x 27 m (gerundet 25 x 25 m) = Feld x 25-75, y 5-55, an jeder Ecke ein Minitor. Ausrichtung wie im PDF:
# Team Rot greift die beiden Minitore oben an, Team Neon verteidigt sie und kontert nach Ballgewinn auf die beiden unten
# (Video: Pink trifft oben, "That's too easy"). Navy (Verteidiger, 6, 8, 9, 10 wie im PDF) -> Team Neon, Pink -> Team Rot,
# neu nummeriert (6 und 8 doppelt): Pink 6 -> 7, Pink 8 -> 11, 4 und 5 bleiben. Gelbe Springer -> neutrale Springer F.
# Ein Trainer statt zwei (unten links neben dem Feld). Positionen leicht verschoben (3D-Abstand).
# Der Halbkreis vor der unteren Linie (nur Markierung im PDF/Video) ist weggelassen.
# Fassungen: PDF Progression 1 (Drittel, kein Zutritt ins letzte Drittel für 10-15 Sekunden = Punkt für Neon) und
# Progression 2 (Springer drehen nach innen, der Passgeber geht raus).
# Sichtkegel aus Text und Ton ("Recognise opportunities to press", "watch for rotations - awareness", "defenders must
# recognise this early"); im Video nicht eingezeichnet, Richtung aus dem Sinn: Spieler sechs liest den Pass des Springers und
# schaut nach dem Abfangen zu Spieler zehn (Kegel mit von, Drehpfeil); in Steigerung 2 schaut Spieler acht über die Schulter
# zum Spieler, der außen rotiert ist.
T = P("T", "c", 12, 52, "T")
ERSATZ = [B("s1", 15.5, 54.5), B("s2", 9, 55.5)]
POS = {"n6": (41, 13), "n8": (67, 30), "n10": (34, 33), "n9": (54, 46),
       "r11": (58, 21), "r4": (46, 30), "r5": (37, 50), "r7": (64, 53), "fl": (19, 35), "fr": (81, 25)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 29, "y": 5, "side": "top"}, {"x": 71, "y": 5, "side": "top"},
        {"x": 29, "y": 55, "side": "bottom"}, {"x": 71, "y": 55, "side": "bottom"}]
DIMS = dims(25, 75, 5, 55, "25 m", "25 m", rx=90)
BALL = [B("b1", 64.6, 53.6)] + ERSATZ
LINES1 = LINES + [{"type": "zone", "x": 25, "y": 5, "w": 50, "h": 16.7}, line(25, 21.7, 75, 21.7), line(25, 38.3, 75, 38.3)]

u = {"title": "Zu viert kompakt, vier Ecktore", "code": "UE-360", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "25 x 25 m",
 "description": "Vier gegen vier in einem Quadrat mit einem Minitor an jeder Ecke, dazu zwei Springer an den Seiten. Team Rot spielt mit den Springern und will in eins der beiden oberen Minitore treffen. Team Neon verteidigt als kompakter Block, hält das Spiel vor sich und lauert auf den Ballgewinn. Dann geht es schnell auf die beiden unteren Minitore.",
 "organisation": ["Aufbauen: Ein Quadrat von 25 mal 25 Metern. An jeder Ecke steht ein Minitor.",
  "Verteilen: Team Neon und Team Rot spielen zu viert in der Mitte. Je ein Springer steht außen an jeder Seite und spielt mit dem Team am Ball. Der Trainer steht mit Bällen neben dem Feld.",
  "Ablauf: Team Rot startet mit dem Ball und spielt mit den Springern auf die oberen Minitore. Die Springer dürfen sich nicht direkt zuspielen. Team Neon schiebt als Block, lenkt das Spiel auf eine Seite und erobert den Ball. Danach kontert Team Neon auf die unteren Minitore oder hält den Ball und spielt mit einem Springer.",
  "Wertung und Wechsel: Ein Treffer von Team Rot gibt einen Punkt für Team Rot. Trifft Team Neon nach dem Ballgewinn, gibt das einen Punkt für Team Neon. Danach bringt der Trainer einen neuen Ball zu Team Rot. Nach ein paar Minuten tauschen die Springer mit anderen Spielern."],
 "organisation_show": ORG,
 "coaching_points": ["Eng zusammen, die Mitte bleibt zu", "Laut sein, wir schicken sie auf eine Seite", "Ball gewonnen? Schnell aufs Minitor", "Den Springer im Blick, auch hinter dir"],
 "materials": ["4 Minitore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zu viert kompakt, vier Ecktore. Vier gegen vier mit zwei Springern. Team Neon steht eng als Block, erobert den Ball und kontert sofort auf die Minitore.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BALL, "dims": DIMS,
  "steps": [
   S("Rot baut auf, der Block schiebt", "Team Rot hat den Ball hinten. Spieler sieben spielt quer zu Spieler fünf. Sofort schiebt der ganze Block mit zum Ball, und Spieler neun läuft an.",
     ps("b1", [37.6, 50.6]), mv("n9", [45, 45], delay=0.3), mv("n10", [30, 32], delay=0.3), mv("n6", [37, 15], delay=0.3), mv("n8", [58, 28], delay=0.3)),
   S("Raus zum Springer", "Durch die Mitte geht nichts. Also spielt Spieler fünf raus zum Springer. Spieler zehn rückt raus und stellt ihn. Spieler vier will in die Tiefe.",
     ps("b1", [19.6, 35.6]), mv("n10", [26, 38], delay=0.3), mv("r4", [37, 24], delay=0.4)),
   S("Pass gelesen und abgefangen", "Der Springer will Spieler vier in den Lauf spielen. Spieler sechs schaut genau hin und liest den Pass. Er geht dazwischen und hat den Ball.",
     bl("n6", [19, 35]), mv("n6", [33, 21], after=True), ps("b1", [33.6, 21.6], delay=1.0)),
   S("Schnell aufs Minitor: Punkt", "Jetzt schnell. Spieler sechs dreht auf und spielt steil auf Spieler zehn, der schon losläuft. Der trifft innerhalb von fünf Sekunden ins Minitor, und das gibt einen Punkt für Team Neon. Danach bringt der Trainer einen neuen Ball zu Team Rot.",
     bl("n6", [31, 46], von=[19, 35], dauer=1.3), drehen("n6", [31, 46], gegen=True, delay=0.4), mv("n10", [31, 46], delay=0.5),
     ps("b1", [31.6, 46.6], after=True), ps("b1", [29.5, 54.6], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Das letzte Drittel ist gesperrt.", "Kein Weg ins letzte Drittel",
    "Das Feld ist in drei Drittel geteilt. Schafft es Team Rot zehn bis fünfzehn Sekunden lang nicht ins letzte Drittel vor den oberen Minitoren, gibt das einen Punkt für Team Neon. Der Block bleibt eng und schiebt gemeinsam. Keiner rennt allein raus.",
    sp(r11=(58, 26)), BALL,
    [S("Die Zeit läuft", "Der Trainer zählt laut mit. Spieler sieben spielt in die Mitte zu Spieler vier. Spieler zehn und Spieler neun schieben sofort eng zusammen.",
       ps("b1", [46.6, 30.6]), mv("n10", [37, 33], delay=0.3), mv("n9", [50, 41], delay=0.3)),
     S("Außen ist auch zu", "Spieler vier spielt raus zu Spieler elf. Da steht Spieler acht schon. Spieler sechs bleibt dahinter und sichert.",
       ps("b1", [58.6, 26.6]), mv("n8", [64, 26], delay=0.3), mv("n6", [52, 14], delay=0.3)),
     S("Fünfzehn Sekunden: Punkt", "Spieler elf muss zurück. Fünfzehn Sekunden sind um, und keiner war im letzten Drittel. Das gibt einen Punkt für Team Neon. Dann startet Team Rot mit einem neuen Ball.",
       dr("r11", "b1", [60, 34]), ps("b1", [64.6, 53.6], after=True))],
    lines=LINES1, dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Springer tauschen mit.", "Springer tauschen den Platz",
    "Bekommt ein Springer den Ball, dribbelt er ins Feld. Wer ihm den Ball gespielt hat, geht raus und ist jetzt der Springer. Die Verteidiger müssen mitbekommen, wer von außen kommt. Wer nur auf seinen Gegenspieler schaut, lässt hinten Platz.",
    sp(), BALL,
    [S("Pass raus, Platz tauschen", "Spieler sieben spielt raus zum Springer. Der nimmt den Ball mit ins Feld, und Spieler sieben läuft raus an die Seite.",
       ps("b1", [81.6, 25.6]), dr("fr", "b1", [70, 40], after=True), mv("r7", [81, 42], delay=0.6)),
     S("Schulterblick, wer ist frei?", "Spieler acht schaut über die Schulter. Spieler sieben steht jetzt außen frei. Spieler acht ruft laut, und Spieler neun übernimmt den Springer.",
       bl("n8", [81, 42]), mv("n9", [62, 44], delay=0.3), mv("n8", [73, 34], after=True)),
     S("Pass nach außen abgefangen", "Der Springer will raus zu Spieler sieben. Spieler acht steht im Passweg und fängt den Ball ab. Jetzt kontert Team Neon.",
       ps("b1", [73.6, 37.6]), mv("n8", [73, 37], delay=0.2))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
