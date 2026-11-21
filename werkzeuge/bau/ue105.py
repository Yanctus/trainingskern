import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 79-P2: 15 x 20 Yards, gedreht nicht nötig: Spielzone oben (Tore links/rechts, Spiel links nach rechts), Technikzone unten.
T = P("T", "c", 12, 28, "T")
TECH = {"n2": (31, 34), "n3": (40, 34), "r6": (55, 34), "r7": (64, 34), "n4": (31, 50), "n5": (40, 50), "r8": (55, 50), "r9": (64, 50)}
def sp(**k):
    d = dict(TECH); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def bt(*ids): return [B("b" + i[1:], round(TECH[i][0] + 1.6, 1), round(TECH[i][1] + 0.6, 1)) for i in ids]
CB = [B("c1", 14.5, 28.6), B("c2", 11, 31.5)]
feld = rect(26, 6, 48, 48); teil = line(26, 30, 74, 30)
TORE = [{"x": 26, "y": 18, "side": "left"}, {"x": 74, "y": 18, "side": "right"}]
def haken(i, dy):
    x, y = TECH[i]; return [dr(i, "b" + i[1:], [x + 5, y + dy]), dr(i, "b" + i[1:], [x, y], after=True)]
ALLE = list(TECH)
SPIEL = {"n2": (35, 10), "n3": (44, 25), "r6": (55, 14), "r7": (64, 25)}
u = {"title": "Folge dem Anführer, 2 gegen 2", "code": "UE-105", "kind": "Spielform",
 "focuses": ["Dribbling", "Umschalten", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "14 x 18 m",
 "description": "Das Feld ist geteilt: unten die Technikzone, oben die Spielzone mit zwei Minitoren. In der Technikzone dribbeln Paare nach dem Prinzip Folge dem Anführer, jeder mit eigenem Ball. Auf Zuruf des Trainers sprinten zwei Paare in die Spielzone und spielen 2 gegen 2. Nach einem Treffer geht es schnell zurück zum eigenen Ball.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern, mit einer gestrichelten Linie in zwei Zonen geteilt. In der oberen Spielzone links und rechts je ein Minitor.",
  "Verteilen: Die Spieler bilden Paare, zwei Paare in Neon und zwei in Rot. Jeder hat einen Ball und startet in der Technikzone.",
  "Ablauf: Einer im Paar führt, der Partner macht jede Bewegung gleichzeitig nach. Auf Zuruf lassen ein Neon-Paar und ein Rot-Paar die Bälle liegen und spielen oben 2 gegen 2.",
  "Wechsel: Nach einem Treffer sprinten die vier zurück zu ihren Bällen, und der Trainer ruft die nächsten zwei Paare. Die Rollen Anführer und Partner regelmäßig tauschen."],
 "organisation_show": ORG,
 "coaching_points": ["Verschiedene Teile des Fußes zum Dribbeln und Mitnehmen nutzen", "Nach dem Spiel schnell zurück zum eigenen Ball", "Im Kopf sofort umschalten: in der Spielzone geht es ums Gewinnen", "Kopf hoch, um die Bewegungen des Partners zu sehen, und neue Tricks ausprobieren"],
 "materials": ["4 orange Hütchen", "1 Ball pro Spieler", "2 Minitore", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Folge dem Anführer und zwei gegen zwei. Unten Technik in Paaren, oben auf Zuruf ein schnelles Spiel.",
 "board": {"lines": [feld, teil], "cones": ecken(26, 6, 48, 48), "goals": TORE, "players": sp(), "balls": bt(*ALLE) + CB,
  "steps": [
   S("Folge dem Anführer", "In jedem Paar führt der linke Spieler. Er dribbelt vor und dreht, und gleichzeitig macht sein Partner genau dieselbe Bewegung mit seinem Ball.",
     *[m for i, dy in zip(ALLE, [-3, -3, -3, -3, 3, 3, 3, 3]) for m in haken(i, dy)]),
   S("Zuruf: zwei Paare spielen", "Der Trainer ruft. Gleichzeitig lassen Neon zwei, Neon drei, Rot sechs und Rot sieben ihre Bälle liegen und sprinten in die Spielzone. Der Trainer spielt Spieler drei einen Ball zu.",
     *[mv(i, list(p)) for i, p in SPIEL.items()], ps("c1", [45.6, 25.6], delay=0.5)),
   S("2 gegen 2", "Spieler drei spielt zu Spieler zwei, der oben an Rot sechs vorbeidribbelt und ins rechte Minitor schießt. Das gibt einen Punkt für Team Neon. Unten dribbeln die anderen Paare weiter.",
     ps("c1", [36.6, 10.6]), dr("n2", "c1", [48, 8], after=True), dr("n2", "c1", [62, 11], after=True), ps("c1", [73.5, 17.5], after=True),
     mv("r6", [58, 18]), mv("r7", [66, 18], delay=0.3), *haken("n4", 3), *haken("r8", 3)),
   S("Schnell zurück zum Ball", "Sofort sprinten alle vier zurück zu ihrem Ball in der Technikzone. Dann ruft der Trainer die nächsten zwei Paare.",
     *[mv(i, list(TECH[i])) for i in SPIEL])],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "14 m"}, {"x1": 82, "y1": 6, "x2": 82, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Spiel geht es im Sprint zurück zum eigenen Ball.", "Schnell zurück, schnell hinein",
    "Fällt ein Tor, sprinten die vier sofort zurück zu ihrem Ball und machen ohne Pause weiter. Die nächsten vier warten auf den Zuruf und starten dann mit vollem Tempo in die Spielzone. Wer umschaltet, denkt sofort ans Gewinnen.",
    sp(n2=(65, 9), n3=(46, 26), r6=(55, 12), r7=(64, 26)), bt(*ALLE) + CB,
    [S("Zurück zum Ball", "Nach dem Tor sprinten Neon zwei, Neon drei, Rot sechs und Rot sieben gleichzeitig zurück zu ihrem Ball.",
       *[mv(i, list(TECH[i])) for i in SPIEL]),
     S("Die nächsten vier", "Der Trainer ruft, und gleichzeitig sprinten Neon vier, Neon fünf, Rot acht und Rot neun ohne Ball durch die Lücken in die Spielzone.",
       mv("n4", [47.5, 40]), mv("n4", [47.5, 28], after=True), mv("n4", [35, 10], after=True), mv("n5", [47.5, 42], delay=0.4), mv("n5", [47.5, 28], after=True), mv("n5", [44, 25], after=True), mv("r8", [70, 40]), mv("r8", [70, 26], after=True), mv("r8", [55, 14], after=True), mv("r9", [70, 42], delay=0.4), mv("r9", [70, 28], after=True), mv("r9", [64, 25], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Unten spielen die übrigen Spieler gleichzeitig eins gegen eins.", "1 gegen 1 in der Technikzone",
    "Während oben 2 gegen 2 gespielt wird, spielt unten je ein Neon-Spieler gegen einen Rot-Spieler mit einem Ball. Einer schirmt den Ball mit dem Körper ab, der andere will ihn haben. Fällt oben ein Tor, zählt unten, wer gerade den Ball hat: Jeder Ballbesitz gibt einen Punkt für sein Team. Den Ball immer auf der sicheren Seite, weg vom Gegner, halten.",
    sp(n2=(35, 10), n3=(44, 25), r6=(55, 14), r7=(64, 25), n4=(34, 44), r8=(43, 44), n5=(56, 44), r9=(65, 44)),
    [B("g", 45.6, 25.6), B("b4", 35.6, 44.6), B("b5", 57.6, 44.6)] + CB,
    [S("Oben 2 gegen 2, unten 1 gegen 1", "Gleichzeitig: Oben spielt Spieler drei zu Spieler zwei. Unten schirmt Neon vier den Ball gegen Rot acht ab, und Rot neun spitzelt Neon fünf den Ball weg.",
       ps("g", [36.6, 10.6]), dr("n2", "g", [48, 8], after=True),
       dr("n4", "b4", [32, 50]), mv("r8", [41, 48], delay=0.2),
       dr("n5", "b5", [50, 46]), ps("b5", [60.6, 48.6], after=True), mv("r9", [59, 48], after=True)),
     S("Tor oben, Ball unten zählt", "Spieler zwei schießt ins rechte Minitor. In diesem Moment hat unten Neon vier den Ball und Rot neun auch: Das gibt einen Punkt für Team Neon und einen Punkt für Team Rot.",
       dr("n2", "g", [62, 11]), ps("g", [73.5, 17.5], after=True), dr("n4", "b4", [29, 46]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
