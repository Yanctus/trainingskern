import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-53 (U12-U14, Woche 3 Pre-Season): 2 v 2s and Sprinting. 30 x 40 Yards hochkant = Feld x 34-66, y 9-51 (27 x 36 m).
# Zone 1 links (x 34-50): 2 gegen 2 auf zwei Minitore (oben, unten). Zone 2 rechts: Sprintbahnen zu zwei Stangen oben.
# Pink -> Neon (2-7), Dunkel -> Rot (2 -> 8, 3 -> 9, 4 -> 10, 5 -> 11, 6 -> 12, 7 -> 13). Wartende seitlich (3D-Abstand).
# Ein Trainer links mit Bällen statt zwei. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 16, 30, "T")
POS = {"n2": (36.5, 55), "n5": (47.5, 55), "n4": (26, 54), "n3": (26, 38), "n6": (56, 55), "n7": (64.5, 55),
       "r8": (36.5, 5), "r11": (47.5, 5), "r9": (26, 5), "r10": (26, 22), "r12": (73, 55), "r13": (81.5, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b1", 17.6, 30.6), B("s1", 14, 34), B("s2", 14, 26)]
LINES = [rect(34, 9, 32, 42), line(50, 9, 50, 51)]
KEGEL = [C(56, 3, "neon", shape="stange"), C(64.5, 3, "neon", shape="stange")]
TORE = [{"x": 42, "y": 9, "side": "top"}, {"x": 42, "y": 51, "side": "bottom"}]
OBEN = [42, 8.7]

u = {"title": "2 gegen 2 und Sprints", "code": "UE-134", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Schnelligkeit", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "27 x 36 m",
 "description": "Das Feld ist in zwei Zonen geteilt, die gleichzeitig laufen. Links wird zwei gegen zwei auf zwei Minitore gespielt: Der Trainer spielt einem Paar den Ball zu, das kombiniert, an den Verteidigern vorbei und schließt ab. Dann sind die nächsten vier dran. Rechts sprinten zwei Spieler zu den Stangen, tippen sie an, sprinten zurück und klatschen die nächsten zwei ab. Nach sechzig Sekunden wechseln vier Spieler die Zone.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 36 Metern, längs in zwei Zonen geteilt. In Zone eins links steht oben und unten ein Minitor, in Zone zwei rechts stehen oben außerhalb des Feldes zwei Stangen.",
  "Verteilen: Zwölf Spieler in zwei Teams. In Zone eins warten vier Neon unten und vier Rot oben, in Zone zwei vier Sprinter unten. Der Trainer steht links mit den Bällen.",
  "Ablauf Zone eins: Der Trainer spielt einem Paar den Ball, das greift das Tor des anderen Paars an. Ist der Angriff vorbei, gehen die vier raus, und die nächsten vier spielen. Ablauf Zone zwei: Zwei sprinten zu den Stangen und zurück und klatschen die nächsten zwei ab.",
  "Wechsel: Nach sechzig Sekunden, je nach Alter auch etwas mehr, wechseln vier Spieler die Zone. Jedes Tor ist ein Punkt für das Team."],
 "organisation_show": ORG,
 "coaching_points": ["Im zwei gegen zwei mit Tempo angreifen, wie im Spiel", "Mit schnellen Kombinationen hinter die Abwehr kommen", "Genau abschließen", "Beim Sprint schnell starten, nach dem Abklatschen bewusst erholen"],
 "materials": ["2 Minitore", "2 Stangen", "Hütchen für das Feld", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zwei gegen zwei und Sprints. Links wird zwei gegen zwei gespielt, rechts wird gesprintet, und beide Zonen laufen gleichzeitig.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Ball ins Spiel, Sprinter los", "Der Trainer spielt Spieler fünf den Ball zu, und alle vier laufen ins Feld: Neon greift oben an, Rot verteidigt. Gleichzeitig sprinten rechts Spieler sechs und Spieler sieben zu den Stangen.",
     ps("b1", [44.6, 36.1]), mv("n5", [44, 35.5]), mv("n2", [36, 40], delay=0.1), mv("r8", [37, 22]), mv("r11", [46.5, 21], delay=0.1),
     mv("n6", [56, 6]), mv("n7", [64.5, 6], delay=0.1)),
   S("Kombinieren, durchstecken", "Spieler fünf spielt zu Spieler zwei und läuft sofort los, hinter die Abwehr. Spieler zwei steckt den Ball durch. Rechts sprinten die beiden zurück und klatschen Spieler zwölf und Spieler dreizehn ab.",
     ps("b1", [36.6, 40.6]), mv("n5", [41.5, 30], after=True), mv("n5", [40.5, 16.5], after=True), ps("b1", [41.1, 17.1], after=True),
     mv("n6", [54.5, 52]), mv("n7", [63, 52], delay=0.1), mv("r12", [57.5, 50], after=True), mv("r13", [65.5, 50], after=True)),
   S("Abschluss: Punkt", "Spieler fünf schließt direkt ab und trifft ins obere Minitor, und das gibt einen Punkt für Team Neon. Rechts laufen jetzt Spieler zwölf und Spieler dreizehn.",
     ps("b1", OBEN), mv("r12", [57.5, 8], delay=0.2), mv("r13", [65.5, 8], delay=0.3)),
   S("Die nächsten vier", "Der Angriff ist vorbei, die vier gehen raus, und Spieler drei, Spieler vier, Spieler neun und Spieler zehn sind dran. Nach sechzig Sekunden wechseln vier Spieler die Zone.",
     mv("n4", [36, 49]), mv("n3", [30, 45], delay=0.1), mv("r9", [36, 11], delay=0.1), mv("r10", [30, 15], delay=0.2))],
  "dims": [{"x1": 34, "y1": 58.6, "x2": 66, "y2": 58.6, "text": "27 m"}, {"x1": 92, "y1": 9, "x2": 92, "y2": 51, "text": "36 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnell hinter die Abwehr.", "Doppelpass in die Tiefe",
    "Im zwei gegen zwei ist ein schneller Doppelpass der kürzeste Weg zum Tor. Abspielen und sofort starten, hinter den Verteidiger. Der Rückpass kommt mit dem richtigen Tempo in den Lauf, so ist der Angreifer frei vor dem Tor.",
    sp(n5=(44, 38), n2=(34.5, 42), r8=(34.5, 26), r11=(47, 22)), [B("b1", 44.6, 38.6), B("s1", 14, 34), B("s2", 14, 26)],
    [S("Abspielen und starten", "Spieler fünf spielt zu Spieler zwei und startet im selben Moment an Spieler elf vorbei in die Tiefe.",
       ps("b1", [35.1, 42.6]), mv("n5", [41, 30], delay=0.1), mv("n5", [40, 16], after=True)),
     S("Rückpass in den Lauf: Punkt", "Spieler zwei spielt den Ball genau in den Lauf, Spieler fünf ist frei und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Dann sind die nächsten vier dran.",
       ps("b1", [40.6, 16.6]), ps("b1", OBEN, after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell starten, gleichmäßig sprinten.", "Die Sprintzone",
    "In der Sprintzone zählt jeder Start: sofort losspurten, die Stange antippen, mit gleichem Tempo zurück. Nach dem Abklatschen bewusst durchatmen und erholen, denn der nächste Sprint kommt schnell.",
    sp(), BAELLE,
    [S("Hin zur Stange", "Spieler sechs und Spieler sieben spurten gleichzeitig los und tippen oben die Stangen an.",
       mv("n6", [56, 6]), mv("n7", [64.5, 6], delay=0.1)),
     S("Zurück und abklatschen", "Mit dem gleichen Tempo geht es zurück. Sie klatschen Spieler zwölf und Spieler dreizehn ab, die sofort losspurten, und erholen sich dann kurz.",
       mv("n6", [54.5, 52]), mv("n7", [63, 52], delay=0.1), mv("r12", [57.5, 50], after=True), mv("r12", [57.5, 8], after=True),
       mv("r13", [65.5, 50], after=True), mv("r13", [65.5, 8], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
