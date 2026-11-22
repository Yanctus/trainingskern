import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-12 (U12-U14, Woche 40 Phase 5): Fun and Engaging Heading Competition Warm Up. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m),
# oben ein Jugendtor (mit Torwart). Ausrichtung wie im PDF (Tor oben, Team Neon links, Team Rot rechts). Pink -> Team Neon (7-11),
# Gold -> Team Rot (2-6), Nummern wie im PDF; der Torwart (im PDF Gold 2, der letzte Kopfballspieler) heißt hier Spieler eins (r1,
# TW), weil der Torwart eines Teams r1 ist. Gezeigt werden je Team Werfer, Läufer und ein Wartender (Neon 10, 11, 9; Rot 5, 6, 4),
# die übrigen (Neon 7, 8, Rot 3) nur im Text (3D-Abstand). Die Puppen sind Stangen. Ein Trainer statt zwei (im PDF zwei Ecken mit
# Bällen), er steht unten mittig. Der Wurf in die Luft ist als Pass dargestellt.
# Sichtkegel: Video "Find space in goal and GK weakness to finish" -> vor dem Kopfball schaut der Läufer zum Torwart (Grundform und
# Steigerung zwei; im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 50, 50, "T")
POS = {"r1": (50, 7), "n10": (36, 10), "n11": (27, 18), "n9": (17, 12),
       "r5": (64, 10), "r6": (73, 18), "r4": (83, 12)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 53.5), B("s2", 50, 53.5)]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
MITTE = (52, 25.5)
def cones(extra=False):
    k = [C(40, 38, shape="stange", id="st1"), C(60, 38, shape="stange", id="st2"),
         C(30.5, 15, id="h1"), C(69.5, 15, id="h2"), C(*MITTE, id="k2")]
    if extra: k += [C(52.5, 18.5, id="k1"), C(52, 32, id="k3")]
    return k
# Weg um die linke Puppe herum bis vor ein Hütchen in der Mitte
def lauf(who, ziel, start_after=False):
    return [mv(who, [35, 38], after=start_after or None), mv(who, [40, 43.5], after=True), mv(who, [45, 39], after=True), mv(who, ziel, after=True)]

u = {"title": "Kopfball-Duell der Teams", "code": "UE-244", "kind": "Spielform",
 "focuses": ["Erwärmung", "Torschuss", "Schnelligkeit"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 12, "field_size": "18 x 18 m",
 "description": "Zwei Teams treten im Köpfen gegeneinander an. Ein Spieler sprintet um eine Puppe zum Hütchen in der Mitte, ein Mitspieler wirft ihm den Ball hoch zu, und er köpft aufs Tor. Danach geht der Kopfballspieler ins Tor, und das andere Team ist dran. Welches Team nach der Spielzeit die meisten Kopfballtreffer hat, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit einem Jugendtor oben. Unten zwei Stangen als Puppen, in der Mitte ein Hütchen, oben links und rechts je ein Starthütchen.",
  "Verteilen: Team Neon steht links, Team Rot rechts. Ein Spieler von Team Rot steht im Tor. Der Trainer steht unten mit Bällen.",
  "Ablauf: Spieler elf sprintet um die linke Puppe zum Hütchen in der Mitte. Spieler zehn wirft ihm den Ball hoch zu, und Spieler elf köpft aufs Tor. Dann ist Team Rot mit der rechten Puppe dran.",
  "Wertung und Wechsel: Jeder Kopfballtreffer gibt einen Punkt für das Team. Wer geköpft hat, geht ins Tor. Welches Team nach der Spielzeit mehr Punkte hat, gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Den richtigen Moment zum Absprung finden", "Vorher schauen, wo im Tor Platz ist", "Schnell um die Puppe, am Hütchen abbremsen", "Gut hoch werfen und das Team anfeuern"],
 "materials": ["1 Jugendtor", "2 Stangen als Puppen", "5 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Kopfball-Duell der Teams. Sprinten, hochspringen und köpfen: Welches Team trifft öfter?",
 "board": {"lines": LINES, "goals": TORE, "cones": cones(), "players": sp(), "balls": [B("b1", 36.6, 10.6)] + ERSATZ,
  "steps": [
   S("Sprint um die Puppe", "Spieler elf sprintet los, nach unten und links um die Puppe herum. Dann läuft er zum Hütchen in der Mitte.",
     *lauf("n11", [48, 26])),
   S("Wurf in die Luft", "Spieler elf schaut kurz, wo der Torwart steht. Spieler zehn wirft ihm den Ball hoch zu.",
     bl("n11", [50, 9]), ps("b1", [48.6, 26.6], after=True)),
   S("Kopfball: Punkt", "Spieler elf springt hoch und köpft in die freie Ecke, und das gibt einen Punkt für Team Neon. Dann geht Spieler elf ins Tor, der Torwart geht zurück zu Team Rot, und Team Rot ist dran.",
     ps("b1", [55.5, 5.4]), mv("r1", [57, 24], after=True), mv("r1", [84, 30], after=True), mv("n11", [50, 8], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=90)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Wer trifft, bleibt dran.", "Wer trifft, bleibt dran",
    "Trifft ein Team, bleibt es dran, und der nächste Spieler köpft. Erst wenn ein Kopfball danebengeht oder der Torwart ihn hält, ist das andere Team dran. Das macht Druck und spornt das ganze Team an.",
    sp(), [B("b1", 36.6, 10.6), B("b2", 17.6, 12.6)] + ERSATZ,
    [S("Getroffen: Punkt", "Spieler elf sprintet um die Puppe, Spieler zehn wirft, und Spieler elf köpft ins Tor. Das gibt einen Punkt für Team Neon, und Team Neon bleibt dran.",
       *lauf("n11", [48, 26]), ps("b1", [48.6, 26.6], after=True), ps("b1", [55.5, 5.4], after=True), mv("n11", [27, 18], after=True)),
     S("Gehalten", "Spieler neun gibt Spieler zehn einen Ball und sprintet um die Puppe. Spieler zehn wirft, aber der Torwart fängt den Kopfball. Jetzt ist Team Rot dran.",
       ps("b2", [36.6, 10.6]), *lauf("n9", [48, 26], start_after=True), ps("b2", [48.6, 26.6], after=True), ps("b2", [50.6, 7.6], after=True))],
    cones=cones()),
  V("Steigerung", "Und jetzt die zweite Steigerung: Drei Hütchen in drei Weiten.", "Drei Hütchen, drei Weiten",
    "In der Mitte stehen jetzt drei Hütchen hintereinander, nah, mittel und weit vom Tor. Wer vom ersten Hütchen trifft, läuft noch einmal um die Puppe und köpft vom nächsten. Drei Treffer hintereinander geben drei Bonuspunkte.",
    sp(), [B("b1", 36.6, 10.6), B("b2", 17.6, 12.6)] + ERSATZ,
    [S("Erstes Hütchen: Punkt", "Spieler elf sprintet um die Puppe zum nahen Hütchen. Er schaut zum Torwart, Spieler zehn wirft, und Spieler elf köpft ins Tor. Das gibt einen Punkt für Team Neon.",
       *lauf("n11", [48, 20]), bl("n11", [50, 9], after=True), ps("b1", [48.6, 20.6], after=True), ps("b1", [55.5, 5.4], after=True)),
     S("Zweites Hütchen: Punkt", "Spieler neun gibt Spieler zehn einen Ball. Spieler elf sprintet noch einmal um die Puppe, jetzt zum mittleren Hütchen, und köpft in die andere Ecke. Das gibt wieder einen Punkt für Team Neon.",
       ps("b2", [36.6, 10.6]), mv("n11", [35, 38], after=True), *lauf("n11", [48, 26])[1:], ps("b2", [48.6, 26.6], after=True), ps("b2", [44.5, 5.4], after=True))],
    cones=cones(True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
