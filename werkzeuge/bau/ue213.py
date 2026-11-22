import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 85-P1 (U12-U14, Woche 30 Phase 6): How to Evade Your Marker to Receive. 20 x 15 Yards = Feld x 18-82, y 5-48 (18 x 14 m), darin
# zwei Quadrate aus Hütchen. In jedem Quadrat drei Anspieler außen mit Ball, in der Mitte ein Spieler und ein Abwehrspieler; beide
# Quadrate spielen gleichzeitig (rechts gespiegelt). Rot (im Video Angreifer) -> Team Neon, gelb (Abwehrspieler) -> Team Rot.
# Nummern neu (im Video doppelt): links Neon 2, 3, 4 außen, 5 Mitte, Rot 10; rechts Neon 6, 7, 8 außen, 9 Mitte, Rot 11.
# Der Trainer steht unten vor dem Feld (im PDF oben im Feld). Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; "awareness" im Coaching-Punkt eins meint Beteiligung, keinen Blick).
T = P("T", "c", 50, 52, "T")
POS = {"n2": (22, 26), "n3": (45, 9.5), "n4": (33, 44), "n5": (31, 25), "r10": (39.5, 27),
       "n6": (78, 26), "n7": (55, 9.5), "n8": (67, 44), "n9": (69, 25), "r11": (60.5, 27)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 55.5), B("s2", 50, 55.5)]
def balls(**k):
    d = {"b2": "n2", "b3": "n3", "b4": "n4", "b6": "n6", "b7": "n7", "b8": "n8"}
    out = []
    for b, p in d.items():
        x, y = k.get(b, (POS[p][0] + 0.6, POS[p][1] + 0.6))
        out.append(B(b, x, y))
    return out + ERSATZ
# Spiegelung linkes -> rechtes Quadrat (Bälle liegen immer bei x+0.6)
MAP = {"n2": "n6", "n3": "n7", "n4": "n8", "n5": "n9", "r10": "r11", "b2": "b6", "b3": "b7", "b4": "b8"}
def mi(m):
    m = dict(m); x, y = m["to"]
    m["to"] = [round(101.2 - x, 1) if m["type"] == "pass" else round(100 - x, 1), y]
    m["who"] = MAP[m["who"]]
    if "ball" in m: m["ball"] = MAP[m["ball"]]
    return m
def beide(*ms): return list(ms) + [mi(m) for m in ms]
def Sb(label, say, *ms): return {"label": label, "say": say, "moves": beide(*ms)}
LINES = [rect(18, 5, 64, 43)]
CONES = [C(x, y) for x in (26, 44, 56, 74) for y in (15.5, 38.5)]

u = {"title": "Vom Gegenspieler lösen", "code": "UE-213", "kind": "Übungsform",
 "focuses": ["Freilaufen", "Passen", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 14 m",
 "description": "In zwei Quadraten spielen je drei Anspieler außen mit Ball. In der Mitte will sich ein Spieler von seinem Gegenspieler lösen und mit jedem Anspieler einen Doppelpass spielen. Kurze, schnelle Bewegungen und Finten bringen ihn frei. Erobert der Gegenspieler den Ball, tauschen die beiden die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern. Darin zwei Quadrate aus Hütchen nebeneinander.",
  "Verteilen: An jedem Quadrat drei Anspieler von Team Neon mit Ball. In der Mitte ein Spieler von Team Neon und ein Gegenspieler von Team Rot.",
  "Ablauf: In beiden Quadraten gleichzeitig löst sich der Spieler in der Mitte und lässt den Pass direkt zum Anspieler zurückprallen. Danach bietet er sich dem nächsten Anspieler an.",
  "Wertung und Wechsel: Ein Doppelpass mit allen drei Anspielern gibt drei Punkte, dann wechselt der Spieler mit einem Anspieler. Erobert der Gegenspieler den Ball, tauschen die beiden die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Kurze, schnelle Bewegungen, um frei zu werden", "Mit Ruf oder Handzeichen den Ball fordern", "Den Ball direkt und genau zurückspielen", "Erst weglaufen, dann kurz kommen: die Doppelbewegung"],
 "materials": ["8 Hütchen", "6 Bälle und Ersatzbälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Vom Gegenspieler lösen. Der Spieler in der Mitte schüttelt seinen Gegenspieler ab und spielt Doppelpässe mit drei Anspielern.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": balls(),
  "steps": [
   Sb("Lösen", "In beiden Quadraten geht es gleichzeitig los. Wir schauen nach links: Neon fünf täuscht nach oben an und startet dann schnell zu Neon zwei. Rot zehn kommt zu spät. Rechts macht Neon neun das Gleiche.",
      mv("n5", [34.5, 21]), mv("r10", [36.5, 23.5], delay=0.3), mv("n5", [27.5, 28.5], after=True), mv("r10", [32.5, 28], after=True)),
   Sb("Doppelpass eins", "Neon zwei passt zu Neon fünf, und Neon fünf spielt direkt zurück. Gleichzeitig spielt rechts Neon sechs mit Neon neun.",
      ps("b2", [28.1, 29.1]), ps("b2", [22.6, 26.6], after=True)),
   Sb("Doppelpass zwei", "Jetzt Neon drei oben: Neon fünf täuscht nach unten an, dreht ab und sprintet nach oben. Neon drei passt, und Neon fünf spielt direkt zurück.",
      mv("n5", [26.5, 33]), mv("r10", [31, 31.5], delay=0.3), mv("n5", [27, 24], after=True), mv("n5", [37.5, 19], after=True),
      ps("b3", [38.1, 19.6], after=True), ps("b3", [45.6, 10.1], after=True)),
   Sb("Drei Pässe: Punkt", "Zum Schluss Neon vier unten: Neon fünf löst sich, bekommt den Pass und spielt direkt zurück. Mit allen drei Anspielern geklappt, und das gibt drei Punkte für Neon fünf. Danach geht Neon vier in die Mitte, und Neon fünf wird Anspieler.",
      mv("r10", [36, 25]), mv("n5", [42, 25.5], delay=0.2), mv("n5", [37, 36], after=True),
      ps("b4", [37.6, 36.6], after=True), ps("b4", [33.6, 44.6], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Doppelbewegung.", "Erst weg, dann kurz",
    "Der Spieler in der Mitte läuft zuerst vom Anspieler weg und nimmt seinen Gegenspieler mit. Dann stoppt er und kommt schnell kurz zurück. So gewinnt er den Abstand, den er für den Pass braucht.",
    sp(), balls(),
    [Sb("Erst weg", "In beiden Quadraten gleichzeitig: Neon fünf läuft zuerst von Neon zwei weg nach oben. Rot zehn geht mit.",
        mv("n5", [35, 19]), mv("r10", [40, 20], delay=0.2)),
     Sb("Dann kurz", "Jetzt stoppt Neon fünf und kommt schnell kurz zu Neon zwei. Rot zehn ist zu weit weg, und Neon fünf lässt den Pass direkt zurückprallen.",
        mv("n5", [27.5, 28.5]), mv("r10", [33, 26], delay=0.3), ps("b2", [28.1, 29.1], after=True), ps("b2", [22.6, 26.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Eng dranbleiben und abfangen.", "Eng dran und abfangen",
    "Auch der Gegenspieler lernt dabei. Er bleibt eng am Spieler in der Mitte und liest seine Bewegung. Erobert er den Ball, tauschen die beiden sofort die Rollen.",
    sp(), balls(),
    [S("Abgefangen", "Wir schauen nach links: Neon fünf läuft zu spät los. Rot zehn bleibt eng dran, geht vor ihn und fängt den Pass von Neon zwei ab. Rechts klappt der Doppelpass.",
       mv("n5", [27.5, 28.5]), mv("r10", [29, 25], delay=0.1), ps("b2", [29.6, 25.6], delay=0.3),
       mi(mv("n5", [27.5, 28.5])), mi(ps("b2", [28.1, 29.1], delay=0.3)), mi(ps("b2", [22.6, 26.6], after=True))),
     S("Rollen tauschen", "Jetzt ist Rot zehn der Spieler in der Mitte, und Neon fünf wird Gegenspieler. Rot zehn spielt den Ball zurück zu Neon zwei, und weiter geht es.",
       ps("b2", [22.6, 26.6]), mv("r10", [34, 22], after=True), mv("n5", [37, 28], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
