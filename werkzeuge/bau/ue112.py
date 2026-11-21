import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P24: 20 x 15 Yards, gedreht: Feld x 14-86, y 18-52, Mittellinie x 50, je zwei Minitore links und rechts.
# Teams warten oben außerhalb (Neon links, Rot rechts), Hütchen-Sammelplätze oben links/rechts, Floater und Trainer links.
T = P("T", "c", 5, 46, "T")
F = P("f", "t", 5, 30, "F")
CB = [B("c1", 7.5, 46.6), B("c2", 4, 49.5)]
POS = {"n2": (18, 9), "n3": (27, 9), "n4": (36, 9), "n5": (45, 9), "r6": (55, 9), "r7": (64, 9), "r8": (73, 9), "r9": (82, 9)}
def sp(d=None, f=(5, 30)):
    d = dict(d or POS)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("f", "t", *f, "F"), T]
def kegel(**k):
    d = {"k1": (24, 40, "neon"), "k2": (40, 26, "neon"), "k5": (74, 42, "orange"), "k6": (60, 26, "orange")}
    d.update(k)
    return [C(x, y, c, id=i) for i, (x, y, c) in d.items()]
LINES = [rect(14, 18, 72, 34), line(50, 18, 50, 52, dashed=False)]
TORE = [{"x": 14, "y": 27, "side": "left"}, {"x": 14, "y": 43, "side": "left"}, {"x": 86, "y": 27, "side": "right"}, {"x": 86, "y": 43, "side": "right"}]
SPIEL = {"n2": (34, 26), "n3": (44, 40), "n4": (30, 48), "n5": (54, 18), "r6": (64, 26), "r7": (74, 38), "r8": (74, 18), "r9": (84, 30)}
u = {"title": "Hütchen holen, dann spielen", "code": "UE-112", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Zusammenspiel", "Torschuss"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 9, "players_max": 11, "field_size": "18 x 14 m",
 "description": "Zwei Teams machen ein Wettrennen: Auf Zuruf sprintet aus jedem Team ein Kind los, holt ein Hütchen aus seiner Hälfte, bringt es zurück und klatscht das nächste Kind ab. Das Team, das zuerst alle Hütchen geholt hat, bekommt den Ball und den Floater dazu und greift mit fünf gegen vier auf die Minitore an. Danach beginnt eine neue Runde mit einem anderen Floater.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern mit Mittellinie und zwei Minitoren an jedem Ende. In jeder Hälfte liegen vier Hütchen verteilt.",
  "Verteilen: Zwei Teams mit je vier Kindern warten am Rand, Team Neon an der linken Hälfte, Team Rot an der rechten. Ein Floater wartet beim Trainer.",
  "Ablauf: Auf Zuruf sprintet aus jedem Team ein Kind zu einem Hütchen seiner Hälfte, bringt es zurück und klatscht das nächste ab. Wer zuerst alle Hütchen hat, bekommt den Ball und den Floater und hat drei Angriffe oder zwei Minuten Zeit.",
  "Wechsel: Danach werden die Hütchen neu verteilt, der Floater wechselt und die Teams werden gemischt. Die Punkte werden über alle Runden gezählt."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell zu den Hütchen sprinten", "Schlau laufen: Wer schnell ist, holt das weiteste Hütchen", "Die Mitspieler vom Rand anfeuern", "Im Spiel die Überzahl nutzen und genau statt fest schießen"],
 "materials": ["8 Hütchen in zwei Farben", "4 Minitore", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben und eines für den Floater"],
 "access": "frei", "hidden": True,
 "say_intro": "Hütchen holen, dann spielen. Erst ein Wettrennen um die Hütchen, dann spielt das schnellere Team mit Überzahl.",
 "board": {"lines": LINES, "goals": TORE, "cones": kegel(), "players": sp(), "balls": CB,
  "steps": [
   S("Auf Zuruf los", "Der Trainer ruft. Gleichzeitig sprinten Neon fünf und Rot sechs zu einem Hütchen in ihrer Hälfte und bringen es zu ihrem Team.",
     mv("n5", [40, 23]), mv("n5", [45, 9], after=True), ps("k2", [10, 13], after=True),
     mv("r6", [60, 23]), mv("r6", [55, 9], after=True), ps("k6", [90, 13], after=True)),
   S("Abklatschen, der Nächste", "Gleichzeitig laufen Neon vier und Rot sieben zum nächsten Hütchen. Neon vier ist schneller, und Team Neon hat zuerst alle Hütchen.",
     mv("n4", [24, 37]), mv("n4", [36, 9], after=True), ps("k1", [10, 16], after=True),
     mv("r7", [74, 39], delay=0.4), mv("r7", [64, 9], after=True), ps("k5", [90, 16], after=True)),
   S("Neon spielt mit Floater", "Team Neon hat gewonnen. Alle laufen gleichzeitig ins Feld, der Floater spielt für Team Neon mit, und der Trainer spielt Neon drei den Ball zu. Jetzt greift Team Neon mit fünf gegen vier auf die rechten Minitore an.",
     *[mv(i, list(p)) for i, p in SPIEL.items()], mv("f", [62, 46]), ps("c1", [45.6, 40.6], delay=0.6))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "18 m"}, {"x1": 94, "y1": 18, "x2": 94, "y2": 52, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schlau laufen und anfeuern.", "Schlau laufen",
    "Das Team überlegt vorher, wer welches Hütchen holt: Das schnellste Kind läuft zum weitesten Hütchen. Wer zurückkommt, klatscht sofort ab, und alle am Rand feuern laut an. Das Gewinnerteam hat in allen Angriffen den Ball.",
    sp(), CB,
    [S("Das schnellste Kind läuft weit", "Neon zwei ist am schnellsten und sprintet zum weitesten Hütchen. Die anderen feuern laut an.",
       mv("n2", [24, 37]), mv("n2", [18, 9], after=True), ps("k1", [10, 16], after=True)),
     S("Weiter zum nahen Hütchen", "Sofort klatscht Neon zwei Neon drei ab, und Neon drei holt das nahe Hütchen.",
       mv("n3", [38, 23]), mv("n3", [27, 9], after=True), ps("k2", [10, 13], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Überzahl nutzen und den freien Spieler finden.", "Den Freien finden",
    "Mit fünf gegen vier ist immer ein Spieler frei. Team Neon lockt die Gegner auf eine Seite und spielt dann schnell zum freien Spieler, der in Ruhe abschließt. Genauigkeit ist wichtiger als Kraft.",
    sp(SPIEL, f=(62, 46)), [B("g", 45.6, 40.6)] + CB,
    [S("Gegner anlocken", "Neon drei spielt zu Neon fünf. Gleichzeitig verschieben Rot sechs, Rot sieben und Rot acht zu ihm.",
       ps("g", [52.4, 18.6]), mv("r6", [60, 22], delay=0.2), mv("r8", [66, 15], delay=0.2), mv("r7", [70, 30], delay=0.2)),
     S("Der Freie schließt ab", "Unten ist der Floater frei. Neon fünf spielt zu ihm, er nimmt den Ball mit und schießt genau ins Minitor. Das gibt einen Punkt für Team Neon.",
       ps("g", [60.4, 46.6]), dr("f", "g", [70, 48], after=True), ps("g", [85.5, 43], after=True))],
    cones=kegel(k1=(10, 16, "neon"), k2=(10, 13, "neon"), k5=(90, 16, "orange"), k6=(90, 13, "orange")))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
