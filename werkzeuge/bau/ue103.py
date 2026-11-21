import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 02-P2: Kreis mit 25 Yards Durchmesser (Mitte 50/30, r 26). Jeder Spieler mit Ball.
T = P("T", "c", 20.6, 41.3, "T")
POS = {"n2": (35.3, 15.5), "n3": (67.8, 14.3), "n4": (56.8, 29.4), "n5": (33.1, 43.5), "n6": (61.8, 47)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T] + list(extra)
def bl(**k):
    d = dict(POS); d.update(k)
    return [B("b" + i[1:], round(x + 1.6, 1), round(y + 0.6, 1)) for i, (x, y) in d.items()] + [B("c1", 23.2, 41.9)]
kreis = {"type": "circle", "x": 50, "y": 30, "r": 26}
zA = {"type": "zone", "x": 58, "y": 18, "w": 8, "h": 8}; zB = {"type": "zone", "x": 36, "y": 33, "w": 8, "h": 8}
def d(k, *pts): return [dr(k, "b" + k[1:], list(p), after=i > 0 or None) for i, p in enumerate(pts)]
u = {"title": "Dribbeln auf engem Raum", "code": "UE-103", "kind": "Übungsform",
 "focuses": ["Dribbling", "Koordination", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 12, "field_size": "Kreis, 23 m Durchmesser",
 "description": "Alle Spieler dribbeln gleichzeitig mit eigenem Ball in einem Kreis. Weil viele Spieler unterwegs sind, wird es eng: Ball nah am Fuß, Kopf hoch, Haken schlagen, in den freien Raum beschleunigen. Die Spieler sollen dabei kreativ sein und möglichst viele Tricks ausprobieren.",
 "organisation": ["Aufbauen: Ein Kreis mit etwa 23 Metern Durchmesser, zum Beispiel der Mittelkreis.",
  "Verteilen: Sechs bis zwölf Spieler, jeder mit einem Ball.",
  "Ablauf: Alle dribbeln gleichzeitig durcheinander, schlagen Haken, probieren Tricks und suchen ständig freien Raum, ohne zusammenzustoßen.",
  "Steigern: Erst zwei Trickzonen, dann ein Verteidiger und ein Springer für Doppelpässe."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball auch im Gedränge eng am Fuß führen", "Mit beiden Füßen dribbeln", "Nach einem Haken mit Tempo in den freien Raum", "Kopf hoch, um zu erkennen, wann gedreht oder ein Doppelpass gespielt wird"],
 "materials": ["Hütchen für den Kreis", "1 Ball pro Spieler", "1 Leibchen für den Verteidiger"],
 "access": "frei", "hidden": True,
 "say_intro": "Dribbeln auf engem Raum. Alle dribbeln gleichzeitig im Kreis, und jeder probiert seine Tricks.",
 "board": {"lines": [kreis], "cones": [], "players": sp(), "balls": bl(),
  "steps": [
   S("Alle dribbeln gleichzeitig", "Alle Spieler dribbeln gleichzeitig mit ihrem Ball durch den Kreis und suchen freien Raum.",
     *d("n2", (40, 22), (44, 30)), *d("n3", (62, 20)), *d("n4", (52, 38)), *d("n5", (40, 44)), *d("n6", (68, 40))),
   S("Haken und weg", "Wird es eng, schlägt jeder einen Haken und beschleunigt in eine freie Lücke. Wir schauen auf Spieler zwei.",
     *d("n2", (41, 33), (33, 28)), *d("n3", (70, 26)), *d("n4", (60, 30)), *d("n5", (34, 36)), *d("n6", (56, 50))),
   S("Mit dem anderen Fuß weiter", "Gleichzeitig dribbeln alle weiter, jetzt bewusst mit dem anderen Fuß, und suchen den nächsten freien Raum.",
     *d("n2", (38, 20)), *d("n3", (64, 36)), *d("n4", (52, 20)), *d("n5", (44, 48)), *d("n6", (46, 42)))],
  "dims": [{"x1": 24, "y1": 58.6, "x2": 76, "y2": 58.6, "text": "23 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei Trickzonen, in denen ein bestimmter Trick gezeigt wird.", "Zwei Trickzonen",
    "Im Kreis liegen zwei kleine Zonen. Wer hineindribbelt, zeigt dort den Trick, den der Trainer vorgibt, zum Beispiel eine Drehung oder einen Übersteiger. Weil viele Spieler in die Zonen wollen, wird es dort eng, und der Ball muss besonders nah am Fuß bleiben.",
    sp(), bl(),
    [S("Hinein in die Zonen", "Gleichzeitig dribbeln Spieler drei und Spieler zwei in je eine Trickzone, die anderen dribbeln weiter.",
       *d("n3", (62, 22)), *d("n2", (40, 37)), *d("n4", (54, 40)), *d("n6", (68, 38))),
     S("Trick zeigen und raus", "In der Zone zeigen beide den Trick und dribbeln dann mit Tempo wieder heraus.",
       *d("n3", (60, 24), (64, 20), (70, 28)), *d("n2", (38, 35), (42, 39), (46, 46)))],
    lines=[kreis, zA, zB]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Verteidiger jagt den Ball, ein Springer hilft mit Doppelpässen.", "Verteidiger und Springer",
    "Ein Verteidiger darf jedem Spieler den Ball wegspielen. In den zwei Zonen ist man sicher und darf dort fünf Sekunden stehen bleiben. Ein Springer hilft: Wer unter Druck gerät, spielt mit ihm einen Doppelpass und dribbelt weg.",
    sp([P("r7", "b", 44, 22, "7"), P("f", "t", 54, 10, "F")]), bl(),
    [S("Verteidiger kommt", "Rot sieben läuft auf Spieler zwei zu. Gleichzeitig spielt Spieler zwei zum Springer und startet an Rot sieben vorbei.",
       mv("r7", [39, 18]), ps("b2", [55.6, 10.6], delay=0.2), mv("n2", [44, 27], delay=0.3)),
     S("Doppelpass und ab in die Zone", "Der Springer spielt direkt zurück, und Spieler zwei dribbelt in die sichere Zone.",
       ps("b2", [45.6, 27.6]), dr("n2", "b2", [40, 37], after=True))],
    lines=[kreis, zA, zB])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
