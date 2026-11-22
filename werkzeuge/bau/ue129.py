import json, sys, math; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-59 (U12-U14, Woche 1 Pre-Season): Endurance Runs and Small Sided Games. Kreis mit 35 Yards Durchmesser -> Mitte 50/30, r 24
# (ca. 32 m), Laufweg außen r 28.5 im Uhrzeigersinn. Minitore links und rechts im Kreis. Dunkelblau -> Neon (Start oben: 8, 11, 9, 7),
# Pink -> Rot (Start unten: 3, 4, 2, 5; Pink 7 neu nummeriert: 5). Ein Trainer rechts mit Bällen (statt zwei; dort kreuzt kein Pass ein Minitor).
# Kein Schulterblick im Original (Text, Ton und Video geprüft).
def rund(grad, r=28.5): w = math.radians(grad); return [round(50 + r * math.sin(w), 1), round(30 - r * math.cos(w), 1)]
T = P("T", "c", 88, 40, "T")
BALL = [B("b1", 89.6, 40.8), B("s1", 91, 44.5)]
START = {"n8": (50, 1.5), "n11": (39, 11), "n9": (61, 11), "n7": (50, 20),
         "r3": (50, 58.5), "r4": (61, 49), "r2": (39, 49), "r5": (50, 40)}
# Nach dem Reinlaufen: Neon oben, Rot unten, in Spalten versetzt (3D-Abstand)
DRIN = {"n11": (30, 22), "n8": (40, 12), "n7": (50, 22), "n9": (62, 14),
        "r2": (30, 40), "r3": (40, 46), "r5": (50, 38), "r4": (62, 44)}
def sp(d):
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
KREIS = {"type": "circle", "x": 50, "y": 30, "r": 24}
KEGEL = [C(50, 6), C(50, 54), C(26, 30), C(74, 30)]
TORE = [{"x": 28.5, "y": 30, "side": "left"}, {"x": 71.5, "y": 30, "side": "right"}]
LINKS, RECHTS = [28.2, 30.2], [71.8, 29.8]
def runde(who, von, first=None):
    """Eine Runde außen um den Kreis im Uhrzeigersinn, von Winkel von bis von + 360."""
    pts = [rund(von + 45 * k) for k in range(1, 9)]
    return [mv(who, pts[0], **(first or {}))] + [mv(who, p, after=True) for p in pts[1:]]
def rein(d, delay=None):
    return [mv(i, list(p), delay=delay) for i, p in d.items()]

u = {"title": "Ausdauerlauf ins 4 gegen 4", "code": "UE-129", "kind": "Spielform",
 "focuses": ["Kondition", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "Kreis, 32 m Durchmesser",
 "description": "Zwei Teams zu je vier Spielern starten an gegenüberliegenden Hütchen am Kreis. Der Erste jedes Teams läuft außen um den Kreis, und jedes Mal, wenn er am Start vorbeikommt, holt er einen Mitspieler ab. Sind alle vier dabei und ist die letzte Runde gelaufen, geht es sofort in den Kreis zum 4 gegen 4 auf zwei Minitore. Das Team, das zuerst komplett im Kreis steht, bekommt den Ball.",
 "organisation": ["Aufbauen: Ein Kreis mit etwa 32 Metern Durchmesser, außen vier Hütchen oben, unten, links und rechts. Links und rechts steht je ein Minitor im Kreis.",
  "Verteilen: Zwei Teams mit je vier Spielern. Team Neon startet am oberen Hütchen, Team Rot am unteren. Der Erste steht außen am Hütchen, die anderen drei warten im Kreis dahinter. Der Trainer steht mit den Bällen am Rand.",
  "Ablauf: Auf Pfiff laufen beide Ersten gleichzeitig im Uhrzeigersinn außen um den Kreis. Am Start holen sie den Nächsten ab und laufen zu zweit weiter, dann zu dritt und zu viert. Nach der letzten Runde mit allen vier geht es sofort in den Kreis, und der Trainer spielt dem Team den Ball, das zuerst komplett drin ist. Dann wird vier gegen vier gespielt.",
  "Pause und Wechsel: Fällt ein Tor oder geht der Ball aus dem Kreis, haben alle drei Minuten Pause. Für den nächsten Lauf rückt jeder in der Reihenfolge eins nach vorn. Vier Läufe, dann eine längere Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Die ganze Runde mit hohem Tempo laufen, nicht stehen bleiben", "Am Rand die Mitspieler laut anfeuern", "Nach der letzten Runde blitzschnell ins Spiel umschalten", "Am Ball ruhig bleiben und sich ohne Ball frei laufen"],
 "materials": ["4 Hütchen", "2 Minitore", "Mehrere Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Ausdauerlauf ins vier gegen vier. Erst laufen die Teams Runden um den Kreis und sammeln ihre Mitspieler ein, dann geht es sofort ins Spiel.",
 "board": {"lines": [KREIS], "goals": TORE, "cones": KEGEL, "players": sp(START), "balls": BALL,
  "steps": [
   S("Die erste Runde", "Auf Pfiff laufen Neon acht und Rot drei gleichzeitig los, beide im Uhrzeigersinn außen um den ganzen Kreis herum bis zurück an ihr Hütchen.",
     *runde("n8", 0), *runde("r3", 180, first={"delay": 0.15})),
   S("Den Nächsten abholen", "Am Hütchen holen sie den Nächsten ab: Neon elf und Rot vier laufen mit, die zweite Runde zu zweit. So kommt nach jeder Runde einer dazu, bis alle vier zusammen laufen.",
     mv("n11", rund(-15)), *runde("n11", -15, first={"after": True}), *runde("n8", 0, first={"delay": 0.5}),
     mv("r4", rund(165), delay=0.15), *runde("r4", 165, first={"after": True}), *runde("r3", 180, first={"delay": 0.65})),
   S("Letzte Runde, rein in den Kreis", "Nach der letzten Runde mit allen vier geht es sofort in den Kreis. Team Neon ist zuerst komplett drin, Team Rot kommt einen Moment später.",
     *rein({k: v for k, v in DRIN.items() if k[0] == "n"}), *rein({k: v for k, v in DRIN.items() if k[0] == "r"}, delay=0.6)),
   S("Vier gegen vier: Punkt", "Darum spielt der Trainer Team Neon den Ball. Neon neun legt zu Neon sieben, der dribbelt an und schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann haben alle drei Minuten Pause, und im nächsten Lauf rückt jeder eins nach vorn.",
     ps("b1", [62.6, 14.6]), ps("b1", [50.6, 22.6], after=True),
     dr("n7", "b1", [58, 26], after=True), ps("b1", RECHTS, after=True))],
  "dims": [{"x1": 10, "y1": 6, "x2": 10, "y2": 54, "text": "32 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Wer zuerst drin ist, hat den Ball.", "Wer zuerst drin ist",
    "Das Team, das nach der letzten Runde zuerst komplett im Kreis steht, bekommt den Ball. Wer auf der letzten Runde nachlässt, verschenkt den Ballbesitz. Darum bis zum Schluss durchziehen und sich gegenseitig anfeuern.",
    sp({"n8": rund(60), "n11": rund(30), "n9": rund(0), "n7": rund(-30),
        "r3": rund(240), "r4": rund(210), "r2": rund(180), "r5": rund(150)}), BALL,
    [S("Rot ist zuerst drin", "Diesmal zieht Team Rot auf der letzten Runde durch und steht zuerst komplett im Kreis. Team Neon kommt zu spät.",
       *rein({"r3": (30, 40), "r2": (40, 46), "r4": (50, 38), "r5": (62, 44)}),
       *rein({"n8": (62, 14), "n11": (50, 22), "n9": (40, 12), "n7": (30, 22)}, delay=0.8)),
     S("Rot hat den Ball: Punkt", "Darum spielt der Trainer Team Rot den Ball. Rot fünf legt zu Rot vier, der dribbelt nach links und schießt ins Minitor, und das gibt einen Punkt für Team Rot. Dann drei Minuten Pause, und im nächsten Lauf rückt jeder eins nach vorn.",
       ps("b1", [62.6, 44.6]), ps("b1", [50.6, 38.6], after=True), dr("r4", "b1", [42, 32], after=True), ps("b1", LINKS, after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ohne Ball freilaufen.", "Freilaufen",
    "Im vier gegen vier ist wenig Platz, und alle sind müde. Wer den Ball nicht hat, bleibt trotzdem in Bewegung und läuft sich in den freien Raum, weg vom Gegenspieler. So entstehen Anspielstationen und Chancen zum Abschluss.",
    sp(DRIN), [B("b1", 30.6, 22.6), B("s1", 91, 44.5)],
    [S("Rot rückt raus", "Neon elf spielt zu Neon sieben. Rot fünf rückt sofort heraus und stellt ihn.",
       ps("b1", [50, 22.6]), mv("r5", [50, 30], after=True)),
     S("Freilaufen: Punkt", "Neon neun löst sich vom Gegner und läuft sich in den freien Raum frei. Neon sieben spielt ihn an, Neon neun schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann drei Minuten Pause, und der nächste Lauf beginnt.",
       mv("n9", [64.5, 23.5]), ps("b1", [64.5, 24.1], after=True), ps("b1", RECHTS, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
