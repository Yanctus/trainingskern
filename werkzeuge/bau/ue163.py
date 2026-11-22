import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 04-P2 (U12-U14, Woche 27 Phase 2): Interchanging Positions Transitional Rondo. 30 x 30 Yards = Feld x 25-75, y 5-55 (27 x 27 m),
# Mittelzone 15 x 15 Yards = x 37.5-62.5, y 17.5-42.5 (gestrichelt). Pink (vier Ballhalter) -> Neon 4, 6, 8, 10;
# Blau (zwei Verteidiger und vier Außenspieler) -> Rot. Nummern neu (im PDF doppelt): blau 4 -> Rot 3, blau 8 -> Rot 2,
# blau 10 -> Rot 5, Außen 7, 9, 11 bleiben. Positionen auf ein Raster gesetzt (3D-Abstand), Spielidee wie im Video.
# Wertung ergänzt (im Original nur "zehn Pässe"): zehn Pässe in Folge = ein Punkt. Ein Trainer rechts unten.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 80, 50, "T")
POS = {"n8": (40, 22), "n6": (60, 22), "n4": (40, 38), "n10": (60, 38),
       "r3": (50, 22.5), "r2": (50, 38), "r5": (50, 7), "r11": (29, 30), "r7": (71, 30), "r9": (50, 53.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 53.5), B("s2", 76.4, 53.5)]
LINES = [rect(25, 5, 50, 50), line(37.5, 17.5, 62.5, 17.5), line(62.5, 17.5, 62.5, 42.5), line(62.5, 42.5, 37.5, 42.5),
         line(37.5, 42.5, 37.5, 17.5)]
KEGEL = ecken(25, 5, 50, 50) + ecken(37.5, 17.5, 25, 25)
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}, {"x": 25, "y": 30, "side": "left"},
        {"x": 75, "y": 30, "side": "right"}]

u = {"title": "Rondo mit Platztausch", "code": "UE-163", "kind": "Spielform",
 "focuses": ["Passspiel", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 27 m",
 "description": "Vier Spieler von Team Neon halten in der kleinen Mitte den Ball gegen zwei Verteidiger von Team Rot. Erobern die Verteidiger den Ball, spielen sie ihn raus, und die vier Außenspieler von Team Rot machen mit: Jetzt heißt es sechs gegen vier im ganzen Feld. Holt Team Neon den Ball zurück, geht es sofort wieder in die Mitte. Wer den Ball gut laufen lässt und klug die Plätze tauscht, schafft zehn Pässe in Folge.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, in der Mitte eine Zone von 14 mal 14 Metern, alle Ecken mit Hütchen.",
  "Verteilen: Vier Spieler von Team Neon und zwei Verteidiger von Team Rot in der Mitte. Vier Außenspieler von Team Rot stehen an den Seiten im großen Feld. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Team Neon spielt vier gegen zwei in der Mitte. Erobert Team Rot den Ball, spielt es sechs gegen vier im ganzen Feld. Holt Team Neon ihn zurück, geht es wieder in die Mitte.",
  "Wertung und Wechsel: Zehn Pässe in Folge geben einen Punkt, für Team Neon in der Mitte, für Team Rot im großen Feld. Nach drei Minuten gehen zwei andere Spieler von Team Rot in die Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Plätze tauschen, damit neuer freier Raum entsteht", "Flach und genau passen, damit die Verteidiger laufen müssen", "Nach dem Ballgewinn sofort umschalten und raus spielen", "Viel miteinander sprechen und sich gegenseitig helfen"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Rondo mit Platztausch. Vier gegen zwei in der Mitte, und nach dem Ballgewinn wird blitzschnell umgeschaltet.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 40.6, 38.6)] + ERSATZ,
  "steps": [
   S("Vier gegen zwei", "Team Neon spielt in der Mitte vier gegen zwei. Neon vier spielt zu Neon acht, und der spielt schräg weiter zu Neon zehn. Rot drei läuft an.",
     ps("b1", [40.6, 22.6]), mv("r3", [46, 19], delay=0.3), ps("b1", [60.6, 38.6], after=True)),
   S("Abgefangen", "Neon zehn will zu Neon sechs passen. Aber Rot zwei läuft dazwischen und fängt den Ball ab.",
     mv("r2", [59, 30.5]), ps("b1", [59.6, 31.1], delay=0.3)),
   S("Sechs gegen vier", "Jetzt spielt Team Rot sechs gegen vier im ganzen Feld. Rot zwei spielt raus zu Rot sieben, und alle Außenspieler laufen sich gleichzeitig frei. Rot sieben spielt weiter zu Rot fünf.",
     ps("b1", [71.6, 30.6]), mv("r5", [63, 8]), mv("r11", [30, 42]), mv("r9", [62, 51]),
     ps("b1", [63.6, 8.6], after=True)),
   S("Zurückerobert", "Neon sechs presst sofort und erobert den Ball. Er dribbelt zurück in die Mitte, und die Außenspieler von Team Rot gehen wieder an ihre Seiten.",
     mv("n6", [59.5, 11]), dr("n6", "b1", [53, 27], after=True), mv("r5", [50, 7], after=True), mv("r11", [29, 30], after=True),
     mv("r9", [50, 53.5], after=True)),
   S("Zehn Pässe: Punkt", "Wieder vier gegen zwei in der Mitte. Schafft Team Neon zehn Pässe in Folge, und das gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, geht es wieder raus ins große Feld.",
     ps("b1", [40.6, 38.6]), ps("b1", [40.6, 22.6], after=True))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=90)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Nach jedem fünften Pass tauschen zwei Spieler die Plätze.", "Plätze tauschen",
    "Nach jedem fünften Pass tauschen zwei Spieler von Team Neon die Plätze. Sie laufen genau dann, wenn der Ball unterwegs ist. So entsteht neuer freier Raum, und die Verteidiger müssen sich neu sortieren.",
    sp(), [B("b1", 60.6, 38.6)] + ERSATZ,
    [S("Fünfter Pass", "Neon zehn spielt zu Neon sechs. Das ist der fünfte Pass, jetzt wird getauscht.",
       ps("b1", [60.6, 22.6])),
     S("Plätze tauschen", "Neon vier und Neon zehn laufen gleichzeitig los und tauschen die Plätze. Neon vier läuft oben an Rot zwei vorbei, Neon zehn unten.",
       mv("n4", [50, 30.5]), mv("n4", [60, 38], after=True), mv("n10", [50, 45.5]), mv("n10", [40, 38], after=True)),
     S("Neuer Platz", "Neon sechs spielt zu Neon vier auf seiner neuen Position. Nach fünf weiteren Pässen wird wieder getauscht.",
       ps("b1", [60.6, 38.6]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Nach zehn Pässen raus aufs Minitor.", "Raus aufs Minitor",
    "An jeder Seite steht jetzt ein Minitor. Nach zehn Pässen darf Team Neon aus der Mitte raus und auf ein Minitor spielen. Ein Tor, in das schon getroffen wurde, ist danach gesperrt, dann zählen nur noch die anderen drei. Erobert Team Rot den Ball, spielt es auch auf die offenen Tore.",
    sp(r5=(31, 8), r11=(29, 44), r7=(71, 16), r9=(69, 52)), [B("b1", 60.6, 38.6)] + ERSATZ,
    [S("Raus nach zehn Pässen", "Team Neon hat zehn Pässe geschafft. Neon sechs läuft aus der Mitte nach rechts, und Neon zehn spielt ihn an.",
       mv("n6", [68, 30]), ps("b1", [68.6, 30.6], delay=0.4)),
     S("Minitor: Punkt", "Neon sechs dribbelt zum rechten Minitor und trifft. Das gibt einen Punkt für Team Neon, und dieses Tor ist jetzt gesperrt.",
       dr("n6", "b1", [71, 33]), ps("b1", [74.7, 30.3], after=True)),
     S("Neuer Ball", "Der Trainer spielt Neon sechs einen neuen Ball, und er dribbelt zurück in die Mitte. Nach zehn Pässen darf Team Neon jetzt nur noch auf die anderen drei Tore spielen.",
       ps("s2", [71.6, 33.6]), dr("n6", "s2", [59, 29], after=True))], goals=TORE)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
