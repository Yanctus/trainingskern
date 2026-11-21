import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-13: 25 x 20 Yards, gedreht (Start unten -> links, Farbtafeln oben -> rechts): x 20-80, y 6-54. Pink -> Neon (oben), Blau -> Rot (unten, gespiegelt y -> 60 - y).
# Das Original hat drei Farben im 3x3-Feld; die Tafel kennt zwei Hütchenfarben, daher 2 Reihen x 3 Hütchen, Ziel: jede Reihe eine Farbe.
Mi = lambda p: [p[0], round(60 - p[1], 2)]
def lane(moves, m):
    out = []
    for x in moves:
        n = dict(x); n["who"] = m.get(x["who"], x["who"]); n["to"] = Mi(x["to"])
        if x.get("ball"): n["ball"] = m[x["ball"]]
        if x.get("bend"): n["bend"] = -x["bend"]
        out.append(n)
    return moves + out
ROT = {"n8": "r4", "n9": "r5", "n10": "r6", "b1": "b2", "k1": "k7", "k2": "k8", "k3": "k9", "k4": "k10", "k5": "k11", "k6": "k12"}
XS = [71, 74.5, 78]
def tafel(oben, unten, y1=11.5, y2=16.5, start=1):
    """oben/unten: Farben der zwei Reihen (o = orange, n = neon) für Team Neon; Team Rot gespiegelt mit denselben Farben."""
    out = []
    for r, (reihe, y) in enumerate(((oben, y1), (unten, y2))):
        for c, col in enumerate(reihe):
            out.append(C(XS[c], y, "neon" if col == "n" else "orange", id=f"k{start + r * 3 + c}"))
    for r, (reihe, y) in enumerate(((oben, y1), (unten, y2))):
        for c, col in enumerate(reihe):
            out.append(C(XS[c], 60 - y, "neon" if col == "n" else "orange", id=f"k{start + 6 + r * 3 + c}"))
    return out
slalom = [C(x, y, id=f"s{i}") for i, (x, y) in enumerate([(33, 17), (40, 17), (47, 17), (54, 17), (33, 43), (40, 43), (47, 43), (54, 43)])]
T = P("T", "c", 58, 3.5, "T"); H = P("h", "t", 58, 55.5, "T")
neon = lambda a, b, c: [P("n8", "a", *a, "8"), P("n9", "a", *b, "9"), P("n10", "a", *c, "10")]
rot = lambda a, b, c: [P("r4", "b", *Mi(a), "4"), P("r5", "b", *Mi(b), "5"), P("r6", "b", *Mi(c), "6")]
START = [(24, 17), (15.5, 8), (7, 17)]
lines = [rect(20, 6, 60, 48)]
u = {"title": "Staffel mit Farbrätsel", "code": "UE-068", "kind": "Spielform",
 "focuses": ["Erwärmung", "Dribbling", "Schnelligkeit"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 12, "field_size": "23 x 18 m",
 "description": "Zwei Teams spielen gleichzeitig eine Staffel mit Rätsel. Der Erste dribbelt durch die Hütchen, passt zum Trainer und läuft zu seiner Farbtafel, wo er zwei Hütchen tauscht. Dann bekommt er den Ball zurück, dribbelt zum Start und klatscht den Nächsten ab. Gewonnen hat das Team, das zuerst jede Reihe in einer Farbe hat und dessen Spieler danach als Erster zurück ist.",
 "organisation": ["Aufbauen: Zwei Bahnen nebeneinander, in jeder vier Hütchen für den Slalom und am Ende eine Farbtafel aus sechs Hütchen in zwei Reihen.",
  "Teams einteilen: Jedes Team stellt sich mit Bällen am Start seiner Bahn auf. Ich stehe neben der einen Tafel, ein Helfer neben der anderen.",
  "Ablauf: Slalom dribbeln, zum Trainer passen, an der Tafel genau zwei Hütchen tauschen, Ball zurück bekommen, zum Start dribbeln und abklatschen.",
  "Wertung: Das Team, das zuerst jede Reihe in einer Farbe hat und dessen Spieler danach als Erster am Start ist, gewinnt. Alle setzen sich dann hin."],
 "organisation_show": ORG,
 "coaching_points": ["Unter Druck gut entscheiden: Welche zwei Hütchen tausche ich?", "Den Ball im Slalom eng am Fuß führen", "Als Team planen und sich gegenseitig anfeuern", "Schnell sprinten, sobald der Tausch geschafft ist"],
 "materials": ["8 Hütchen für die Slaloms", "12 Hütchen in zwei Farben für die Tafeln", "1 Ball pro Spieler", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Staffel mit Farbrätsel. Hier dribbeln zwei Teams gleichzeitig und lösen an ihrer Tafel ein kleines Farbrätsel.",
 "board": {"lines": lines, "cones": slalom + tafel("onn", "noo"),
  "players": neon(*START) + rot(*START) + [T, H], "balls": [B("b1", 25.6, 17), B("b2", 25.6, 43)],
  "steps": [
   S("Beide starten: Slalom", "Beide Teams starten gleichzeitig. Spieler acht dribbelt im Slalom durch die Hütchen.",
     *lane([dr("n8", "b1", [33, 13.5]), dr("n8", "b1", [40, 20.5], after=True), dr("n8", "b1", [47, 13.5], after=True), dr("n8", "b1", [54, 20.5], after=True), dr("n8", "b1", [59, 17], after=True)], ROT)),
   S("Pass zum Trainer, ab zur Tafel", "Er passt zu mir und läuft sofort zu seiner Farbtafel.",
     *lane([ps("b1", [57.2, 4.9]), mv("n8", [67.5, 14], delay=0.2)], ROT)),
   S("Zwei Hütchen tauschen", "An der Tafel tauscht er genau zwei Hütchen, damit die Farben besser sortiert sind.",
     *lane([ps("k2", [74.5, 16.5]), ps("k5", [74.5, 11.5])], ROT)),
   S("Ball zurück, ab zum Start", "Ich spiele ihm den Ball zurück, und er dribbelt außen an den Hütchen vorbei zurück zum Start.",
     *lane([mv("n8", [66, 21]), ps("b1", [65.5, 22.4], delay=0.15), dr("n8", "b1", [58, 24.5], after=True), dr("n8", "b1", [29, 24.5], after=True)], ROT)),
   S("Abklatschen, der Nächste startet", "Er klatscht Spieler neun ab, und der startet mit seinem Ball in die nächste Runde.",
     *lane([mv("n9", [23.5, 12])], ROT))],
  "dims": [{"x1": 20, "y1": 58.6, "x2": 80, "y2": 58.6, "text": "23 m"}, {"x1": 88, "y1": 6, "x2": 88, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst schauen, dann den richtigen Tausch machen.", "Erst schauen, dann tauschen",
    "Wer an der Tafel ankommt, schaut zuerst, welche zwei Hütchen falsch liegen. Ein überlegter Tausch bringt das Team weiter, ein schneller Fehler kostet Zeit. Hier sind nach dem zweiten Tausch alle Reihen sortiert, und Team Neon ist zuerst fertig.",
    [P("n9", "a", 67.5, 14, "9"), P("n8", "a", 24, 17, "8"), P("n10", "a", 15.5, 8, "10"), P("r5", "b", 54, 39.5, "5"), *rot((24, 17), (15.5, 8), (7, 17))[:1], P("r6", "b", 15.5, 52, "6"), T, H],
    [B("b1", 57.2, 4.9), B("b2", 55.6, 39.5)],
    [S("An der Tafel: erst schauen", "Spieler neun kommt an die Tafel und schaut genau: In jeder Reihe liegt noch ein Hütchen falsch.", mv("n9", [68, 14.5])),
     S("Der richtige Tausch", "Er tauscht die beiden letzten Hütchen, und jetzt hat jede Reihe nur noch eine Farbe.", ps("k3", [78, 16.5]), ps("k6", [78, 11.5])),
     S("Zuerst fertig: Team Neon gewinnt", "Ich spiele ihm den Ball zurück, er sprintet zum Start, und Team Neon hat gewonnen.",
       ps("b1", [65.5, 21.5]), mv("n9", [66, 20.5]), dr("n9", "b1", [58, 24.5], after=True), dr("n9", "b1", [30, 24.5], after=True))],
    cones=slalom + tafel("oon", "nno")),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Rätsel sprinten und ins Minitor treffen.", "Sprint und Abschluss",
    "Zwei Minitore kommen dazu. Ist eine Tafel sortiert, sprintet der Spieler mit dem Ball über die Linie und schließt ins Minitor seines Teams ab. Erst danach läuft er zurück und klatscht ab. Das bringt mehr Tempo und ein klares Ziel am Ende.",
    [P("n9", "a", 67.5, 14, "9"), P("n8", "a", 24, 17, "8"), P("n10", "a", 15.5, 8, "10"), P("r5", "b", 54, 39.5, "5"), *rot((24, 17), (15.5, 8), (7, 17))[:1], P("r6", "b", 15.5, 52, "6"), T, H],
    [B("b1", 57.2, 4.9), B("b2", 55.6, 39.5)],
    [S("Tafel sortiert", "Spieler neun macht den letzten Tausch, und die Tafel ist sortiert.", ps("k3", [78, 16.5]), ps("k6", [78, 11.5])),
     S("Ball zurück, Sprint über die Linie", "Er bekommt den Ball zurück und sprintet mit ihm über die Linie.",
       ps("b1", [65.5, 21.5]), mv("n9", [66, 21]), dr("n9", "b1", [74, 22.5], after=True)),
     S("Abschluss ins Minitor: Punkt", "Er schießt ins Minitor, das gibt einen Punkt, dann läuft er zurück und klatscht ab.", ps("b1", [82, 22.5]), mv("n9", [60, 26], delay=0.3))],
    cones=slalom + tafel("oon", "nno"), lines=lines + [line(68, 6, 68, 54)], goals=[{"x": 80, "y": 22.5, "side": "right"}, {"x": 80, "y": 37.5, "side": "right"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
