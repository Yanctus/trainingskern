import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-9: 15 x 20 Yards (Feld 22/6, 56 x 48). Rot oben, Neon unten, Hürden in der Mitte, Endzonen links und rechts.
T = P("T", "c", 90, 44, "T")
POS = {"r6": (50, 8), "r7": (59, 8), "r8": (68, 8), "r9": (77, 8), "n2": (23, 52), "n3": (32, 52), "n4": (41, 52), "n5": (50, 52)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
CB = [B("c1", 92.5, 44.6), B("c2", 89, 47.5)]
HUERDEN = [C(50, y, "neon", shape="huerde_ou") for y in (12, 16.5, 21, 39, 43.5, 48)]
MARK = [C(x, y, "neon") for x, y in ((28, 24), (28, 36), (72, 24), (72, 36), (40, 30), (45, 30), (55, 30), (60, 30))]
EZ = [{"type": "zone", "x": 22, "y": 24, "w": 6, "h": 12}, {"type": "zone", "x": 72, "y": 24, "w": 6, "h": 12}]
LINES = [rect(22, 6, 56, 48)] + EZ
def hops(): return [mv("n5", [50, 44]), mv("n5", [46, 36], after=True), mv("r6", [50, 16]), mv("r6", [55, 24], after=True)]
u = {"title": "Hürden, Täuschung, Sprint", "code": "UE-107", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "1 gegen 1", "Erwärmung"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 12, "field_size": "14 x 18 m",
 "description": "Ein Aufwärmspiel für schnelle Beine. Ein Angreifer von Team Neon und ein Verteidiger von Team Rot springen gleichzeitig beidbeinig über kleine Hürden und stehen sich in der Mitte gegenüber. Der Angreifer täuscht an und sprintet in eine der beiden Endzonen, der Verteidiger versucht, ihn vorher zu fangen.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. In der Mitte eine Hütchenlinie, oben und unten je drei kleine Hürden in einer Reihe, links und rechts je eine Endzone.",
  "Verteilen: Team Neon greift an und wartet unten, Team Rot verteidigt und wartet oben. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Gleichzeitig springen ein Angreifer und ein Verteidiger über die Hürden. In der Mitte täuscht der Angreifer an und sprintet in eine Endzone. Berührt der Verteidiger ihn vorher, hat er ihn gefangen.",
  "Wechsel: Nach jedem Sprint tauschen die beiden die Rollen, damit jeder angreift und verteidigt."],
 "organisation_show": ORG,
 "coaching_points": ["Kraftvoll und sauber beidbeinig über die Hürden springen", "Mit Finten, schnellen Bewegungen und Schulter fallen lassen täuschen", "Mit Ball dieselben Bewegungen nutzen", "Als Verteidiger die Lage schnell erkennen und den Angreifer fangen"],
 "materials": ["6 kleine Hürden", "8 gelbe Hütchen", "Bälle beim Trainer", "2 Minitore für die zweite Steigerung", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Hürden, Täuschung, Sprint. Über die Hürden springen, in der Mitte täuschen und in die Endzone sprinten.",
 "board": {"lines": LINES, "cones": HUERDEN + MARK, "players": sp(), "balls": CB,
  "steps": [
   S("Über die Hürden", "Gleichzeitig springen Spieler fünf und Spieler sechs beidbeinig über die Hürden und stehen sich in der Mitte gegenüber.", *hops()),
   S("Täuschen und sprinten", "Spieler fünf täuscht nach links an und sprintet dann nach rechts in die Endzone. Spieler sechs fällt auf die Finte herein und sprintet zu spät hinterher.",
     mv("n5", [42, 33]), mv("n5", [60, 35], after=True), mv("n5", [75, 30], after=True), mv("r6", [47, 26], delay=0.2), mv("r6", [66, 27], after=True)),
   S("Zurück, Rollen tauschen", "Beide gehen zurück an ihren Start. Im nächsten Durchgang tauschen sie die Rollen.",
     mv("n5", [50, 52]), mv("r6", [50, 8]))],
  "dims": [{"x1": 22, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "14 m"}, {"x1": 86, "y1": 6, "x2": 86, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer spielt dem Angreifer einen Ball zu.", "Mit Ball täuschen",
    "Nach den Hürden spielt der Trainer dem Angreifer einen Ball zu. Mit schnellen Richtungs- und Tempowechseln, Finten und Schulter fallen lassen bringt er den Ball in eine Endzone, ohne dass der Verteidiger ihn erreicht. Gelingt das, gibt es einen Punkt.",
    sp(), CB,
    [S("Über die Hürden", "Gleichzeitig springen Spieler fünf und Spieler sechs über die Hürden.", *hops()),
     S("Pass vom Trainer", "Der Trainer spielt Spieler fünf flach an.", ps("c1", [47.6, 36.6])),
     S("Finte und in die Endzone", "Spieler fünf täuscht nach rechts an und dribbelt nach links in die Endzone. Das gibt einen Punkt für Team Neon.",
       dr("n5", "c1", [52, 38]), dr("n5", "c1", [25, 30], after=True), mv("r6", [53, 27], delay=0.2), mv("r6", [34, 27], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: In den Endzonen stehen Minitore.", "Abschluss ins Minitor",
    "Links und rechts steht hinter jeder Endzone ein Minitor. Wer mit Ball in die Endzone kommt, schließt sofort ins Minitor ab. Jeder Treffer gibt einen Punkt. Der Angreifer soll schnell entscheiden und trotz Tempo ruhig und genau schießen.",
    sp(), CB,
    [S("Hürden und Pass", "Gleichzeitig springen beide über die Hürden, dann spielt der Trainer Spieler fünf an.", *hops(), ps("c1", [47.6, 36.6], after=True)),
     S("Durchbrechen und abschließen", "Spieler fünf täuscht nach links an, dribbelt nach rechts in die Endzone und schießt ins Minitor. Das gibt einen Punkt für Team Neon.",
       dr("n5", "c1", [44, 34]), dr("n5", "c1", [73, 33], after=True), ps("c1", [77.5, 30], after=True), mv("r6", [48, 26], delay=0.2), mv("r6", [64, 27], after=True))],
    goals=[{"x": 22, "y": 30, "side": "left"}, {"x": 78, "y": 30, "side": "right"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
