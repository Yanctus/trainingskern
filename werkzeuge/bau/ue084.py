import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 21-P3: 30 x 30 Yards, gedreht: Feld x 27-73, y 8-52, drei Zonen (Linien x 38.5 und 61.5), Tore links/rechts mit neutralen Torhütern,
# vier Außenspieler (neutral, F) an den Zonenlinien. Neon greift nach rechts an, Rot verteidigt.
T = P("T", "c", 14, 12, "T")
F = [P("f1", "t", 38.5, 3.5, "F"), P("f2", "t", 61.5, 3.5, "F"), P("f3", "t", 38.5, 55.5, "F"), P("f4", "t", 61.5, 55.5, "F")]
TW = [P("k1", "t", 30, 30, "TW"), P("k2", "t", 71, 30, "TW")]
def sp(n2=(53, 33), r3=(44, 26), extra=()): return [P("n2", "a", *n2, "2"), P("r3", "b", *r3, "3")] + F + TW + [T] + list(extra)
fb = [B("b1", 63.1, 4.1), B("b3", 36.9, 4.1), B("b4", 40.1, 55), B("b5", 63.1, 55)]
lines = [rect(27, 8, 46, 44), line(38.5, 8, 38.5, 52), line(61.5, 8, 61.5, 52)]
cones = ecken(27, 8, 46, 44)
goals = [{"x": 27, "y": 30, "side": "left"}, {"x": 73, "y": 30, "side": "right"}]
u = {"title": "Abschütteln und abschließen", "code": "UE-084", "kind": "Übungsform",
 "focuses": ["Torschuss", "1 gegen 1", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 10, "field_size": "27 x 27 m",
 "description": "Ein Feld mit drei Zonen und einem Tor mit Torwart an jedem Ende. In der mittleren Zone spielt ein Angreifer gegen einen Verteidiger. Einer der vier Außenspieler passt den Ball hinein. Der Angreifer schüttelt den Verteidiger mit einer doppelten Bewegung ab, nimmt den Ball an und schließt ab. Erobert der Verteidiger den Ball, greift er sofort das andere Tor an.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, in drei Zonen geteilt. An beiden Enden ein Tor mit Torwart.",
  "Verteilen: In der mittleren Zone ein Angreifer und ein Verteidiger. Vier Außenspieler mit Bällen stehen an den Enden der Zonenlinien.",
  "Ablauf: Ein Außenspieler passt in die Mitte. Der Angreifer löst sich mit einer doppelten Bewegung, nimmt an und schießt aus der mittleren Zone. Die Angriffe gehen abwechselnd auf beide Tore.",
  "Ballverlust: Erobert der Verteidiger den Ball, wird er zum Angreifer und greift sofort das andere Tor an, bis er den Ball verliert."],
 "organisation_show": ORG,
 "coaching_points": ["Mit einer doppelten Bewegung den Verteidiger abschütteln", "Nach der Annahme mit Tempo dribbeln und den Gegner hinter sich lassen", "Beim Abschluss überlegen: wohin, wie und warum", "Nach Ballverlust sofort umschalten"],
 "materials": ["2 Tore", "4 orange Hütchen", "Markierungen für die Zonen", "Leibchen", "Bälle bei den Außenspielern"],
 "access": "frei", "hidden": True,
 "say_intro": "Abschütteln und abschließen. Mit einer doppelten Bewegung den Verteidiger loswerden und dann aufs Tor schießen.",
 "board": {"lines": lines, "cones": cones, "goals": goals, "players": sp(), "balls": fb,
  "steps": [
   S("Doppelte Bewegung", "Spieler zwei geht erst ein paar Schritte in die eine Richtung, dann blitzschnell in die andere. Spieler drei geht auf die Finte ein.",
     mv("n2", [55, 39]), mv("n2", [55, 26], after=True), mv("r3", [47, 34], delay=0.2)),
   S("Pass von außen", "Der Außenspieler oben rechts passt in den freien Raum zu Spieler zwei.", ps("b1", [56.6, 26.6])),
   S("Abschluss: Punkt", "Spieler zwei nimmt den Ball mit und schießt flach ins Eck, und das gibt einen Punkt für Neon.", ps("b1", [73, 25.5]))],
  "dims": [{"x1": 27, "y1": 58.6, "x2": 73, "y2": 58.6, "text": "27 m"}, {"x1": 82, "y1": 8, "x2": 82, "y2": 52, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Wer den Ball erobert, dreht sofort um und greift das andere Tor an.", "Ball erobert, umdrehen",
    "Erobert der Verteidiger den Ball, wird er sofort zum Angreifer. Schnell umdrehen und den Platz nutzen, den der Angreifer hinter sich gelassen hat. Wer zögert, verschenkt die Chance.",
    sp((55, 30), (46, 25)), [B("b1", 56.6, 30.6)] + fb[1:],
    [S("Zweikampf", "Spieler zwei dribbelt los, Spieler drei geht dazwischen.", dr("n2", "b1", [58, 32]), mv("r3", [54, 30])),
     S("Ball erobert", "Spieler drei spitzelt den Ball weg und hat ihn jetzt selbst.", ps("b1", [51, 33]), mv("r3", [50, 32.5], delay=0.2)),
     S("Zum anderen Tor", "Spieler drei dreht sofort um, dribbelt auf das andere Tor zu und schießt. Das gibt einen Punkt für Rot.",
       dr("r3", "b1", [42, 34]), ps("b1", [27, 35], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Angreifer darf in die Torzone, dann presst ein Außenspieler mit.", "Außenspieler presst mit",
    "Jetzt darf der Angreifer in die Torzone dribbeln. Sobald er sie betritt, darf ein Außenspieler hereinkommen und ihn unter Druck setzen. Erobert dieser den Ball, passt er zum ursprünglichen Verteidiger, und der greift sofort das andere Tor an.",
    sp((56, 27), (47, 33)), [B("b1", 57.6, 27.6)] + fb[1:],
    [S("Hinein in die Torzone", "Spieler zwei dribbelt in die Torzone. Gleichzeitig startet der Außenspieler oben rechts und presst.",
       dr("n2", "b1", [64, 27]), mv("f2", [65, 18], delay=0.2)),
     S("Ball erobert", "Der Außenspieler erobert den Ball und passt sofort zu Spieler drei.", mv("f2", [64, 24]), ps("b1", [48.6, 33.6], after=True)),
     S("Gegenangriff", "Spieler drei dribbelt aufs andere Tor zu und schießt. Das gibt einen Punkt für Rot.", dr("r3", "b1", [42, 34]), ps("b1", [27, 35], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
