import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 08-P1: 30 x 32 Yards, drei Bahnen (im Original vier) zu je 16 Einheiten Höhe. Feld x 18-82, y 6-54. Endspieler links und rechts außen.
T = P("T", "c", 66, 1.5, "T")
CB = [B("c1", 68.5, 2.1)]
LY = (14, 30, 46)
POS = {"n2": (13, 14), "n3": (40, 14), "n4": (87, 14), "r5": (13, 30), "r6": (60, 30), "r7": (87, 30), "n8": (13, 46), "n9": (45, 46), "n10": (87, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BALLS = [B("b3", 41.6, 14.6), B("b6", 58.4, 30.6), B("b9", 46.6, 46.6)] + CB
LINES = [rect(18, 6, 64, 48), line(18, 22, 82, 22), line(18, 38, 82, 38)]
BAHN = [("n3", "b3", 87, 14, 1), ("r6", "b6", 13, 30, -1), ("n9", "b9", 87, 46, 1)]
def hin(): return [dr(c, b, [50 + d * 26, y]) for c, b, e, y, d in BAHN]
def herum():
    out = []
    for c, b, e, y, d in BAHN:
        out += [ps(b, [e - d * 1.6, y + 0.6])]
        out += [mv(c, list(p), after=n > 0 or None, delay=0.2 if n == 0 else None) for n, p in enumerate([(50 + d * 30, y - 6), (e + d * 4, y - 5), (e + d * 4, y + 5), (e - d * 4, y + 6)])]
        out += [ps(b, [e - d * 4 - d * 1.6, y + 6.6], after=True)]
    return out
def zurueck(): return [dr(c, b, [50, y + 3]) for c, b, e, y, d in BAHN]
u = {"title": "Mit Tempo dribbeln und ablegen", "code": "UE-122", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Erwärmung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 9, "players_max": 15, "field_size": "27 x 29 m",
 "description": "Das Feld ist in Bahnen geteilt. In jeder Bahn stehen zwei Endspieler, ein Spieler in der Mitte hat den Ball. Er läuft mit Tempo zum Endspieler, legt ab, läuft um ihn herum, bekommt den Ball auf der anderen Seite zurück und dribbelt zurück. Dabei wechselt er zwischen schnellem Laufen mit Ball und engem Dribbling.",
 "organisation": ["Aufbauen: Ein Feld von etwa 27 mal 29 Metern, in drei bis vier Bahnen geteilt.",
  "Verteilen: In jeder Bahn drei Spieler: je ein Endspieler links und rechts und ein Spieler mit Ball in der Mitte. Die Bahnen arbeiten in wechselnder Richtung.",
  "Ablauf: Der Spieler in der Mitte läuft mit Ball zum Endspieler, legt ab, läuft um ihn herum, bekommt den Ball zurück und dribbelt zum anderen Ende. Das geht 30 bis 60 Sekunden lang.",
  "Wechsel: Nach ein bis zwei Minuten wechseln die Rollen. Auf Zuruf des Trainers wird zwischen Laufen mit Ball und engem Dribbling gewechselt."],
 "organisation_show": ORG,
 "coaching_points": ["Nach wenigen Kontakten eng dribbeln, dann explodieren und mit Tempo laufen", "Bei jedem Kontakt den Kopf heben", "Schon beim Anlaufen auf den Endspieler überlegen, wie es weitergeht", "Die Endspieler helfen, damit der Lauf um sie herum frei bleibt"],
 "materials": ["Hütchen für Feld und Bahnen", "1 Ball pro Bahn", "Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Mit Tempo dribbeln und ablegen. In jeder Bahn läuft ein Spieler mit Ball hin und her und spielt mit den Endspielern.",
 "board": {"lines": LINES, "players": sp(), "balls": BALLS,
  "steps": [
   S("Mit Tempo zum Endspieler", "Gleichzeitig laufen die drei Spieler in der Mitte mit Ball los. Die mittlere Bahn läuft in die andere Richtung.", *hin()),
   S("Ablegen und herumlaufen", "Jeder legt den Ball zum Endspieler ab, läuft um ihn herum und bekommt den Ball auf der anderen Seite zurück.", *herum()),
   S("Zurück mit Kopf hoch", "Mit dem Ball geht es zurück zum anderen Ende, mit dem Kopf oben, um den Raum vor sich zu sehen.", *zurueck())],
  "dims": [{"x1": 18, "y1": 58.6, "x2": 82, "y2": 58.6, "text": "27 m"}, {"x1": 95, "y1": 6, "x2": 95, "y2": 54, "text": "29 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Alle drei Spieler einer Bahn arbeiten, mit Übergabe am Endspieler.", "Übergabe am Ende",
    "Jetzt dribbelt der Spieler aus der Mitte direkt auf den Endspieler zu. Der kommt ihm entgegen, übernimmt den Ball und dribbelt selbst los. Der bisherige Dribbler wird zum Endspieler. So arbeiten alle drei, und sie müssen sich gut absprechen.",
    sp(), BALLS,
    [S("Dribbeln zum Endspieler", "Neon drei dribbelt nach links auf Neon zwei zu, und Neon zwei kommt ihm entgegen.",
       dr("n3", "b3", [26, 14]), mv("n2", [20, 18], delay=0.3)),
     S("Übernahme", "Neon zwei übernimmt den Ball und dribbelt los. Neon drei läuft weiter und wird zum neuen Endspieler.",
       dr("n2", "b3", [40, 18]), mv("n3", [13, 14], delay=0.1))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Auch die Endspieler wechseln die Bahn.", "Endspieler wechseln",
    "Wann immer es passt, tauschen die Endspieler außen mit dem Endspieler der Nachbarbahn. Damit niemand durcheinanderkommt, sagen sie laut an, wer wohin geht.",
    sp(), BALLS,
    [S("Dribbeln", "Die Spieler in der Mitte dribbeln zu ihren Endspielern.", *hin()),
     S("Endspieler tauschen", "Gleichzeitig tauschen links Neon zwei und Rot fünf die Plätze und rechts Rot sieben und Neon zehn. Alle rufen dabei laut.",
       mv("n2", [8, 22]), mv("n2", [13, 30], after=True), mv("r5", [18, 22]), mv("r5", [13, 14], after=True),
       mv("r7", [92, 38]), mv("r7", [87, 46], after=True), mv("n10", [82, 38]), mv("n10", [87, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
