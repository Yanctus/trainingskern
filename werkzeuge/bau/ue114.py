import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 24-P1: 16 x 8 Yards, gedreht: Feld x 14-86, y 12-48, Mittellinie x 50 mit zwei Toren (y 13.4-20 und 40-46.6).
T = P("T", "c", 6, 50, "T")
CB = [B("c1", 8.5, 50.6), B("c2", 5, 53.5)]
POS = {"n2": (14, 30), "n3": (31, 12), "n4": (31, 48), "n5": (48, 30), "r9": (32, 30), "n6": (86, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(14, 12, 72, 36), line(50, 12, 50, 48)]
TORE = [C(50, 13.4), C(50, 20), C(50, 40), C(50, 46.6)]
u = {"title": "Rondo mit Pass durchs Tor", "code": "UE-114", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 6, "field_size": "15 x 7 m",
 "description": "Vier Spieler von Team Neon halten in einer Hälfte den Ball gegen einen Verteidiger von Team Rot. Auf der Mittellinie stehen zwei Tore aus Hütchen. Wenn die Lücke da ist, spielen sie fest durch ein Tor zum Mitspieler in der anderen Hälfte, und dort geht das Rondo weiter.",
 "organisation": ["Aufbauen: Ein Feld von 15 mal 7 Metern, in zwei Hälften geteilt. Auf der Mittellinie bilden vier Hütchen zwei Tore.",
  "Verteilen: In der linken Hälfte vier Spieler von Team Neon als Raute und ein Verteidiger von Team Rot. In der rechten Hälfte wartet ein Spieler von Team Neon.",
  "Ablauf: Team Neon hält den Ball und spielt dann durch ein Tor zum wartenden Spieler, zum Beispiel nach acht Pässen, nach einem Doppelpass oder auf Zuruf. Drei Spieler rücken nach, einer bleibt als neuer wartender Spieler zurück, und der Verteidiger setzt nach.",
  "Wechsel: Erobert der Verteidiger den Ball, darf er selbst zum wartenden Spieler durchspielen. Dann tauscht er mit dem Spieler, der den Ball verloren hat. Nach zwei bis drei Minuten wird ein neuer Verteidiger bestimmt, und die Punkte werden gezählt."],
 "organisation_show": ORG,
 "coaching_points": ["Kurz und genau mit der Innenseite passen", "Schnell Winkel anbieten, damit der Ball in den eigenen Reihen bleibt", "Erkennen, wann der feste Pass durch das Tor möglich ist", "Miteinander sprechen und als Gruppe den freien Raum nutzen"],
 "materials": ["8 Hütchen", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Rondo mit Pass durchs Tor. Vier gegen eins den Ball halten und im richtigen Moment durchs Tor in die andere Hälfte spielen.",
 "board": {"lines": LINES, "cones": TORE, "players": sp(), "balls": [B("b1", 15.6, 30.6)] + CB,
  "steps": [
   S("Ball halten", "Spieler zwei spielt zu Spieler drei. Gleichzeitig verschiebt Spieler neun und greift Spieler drei an.",
     ps("b1", [32.6, 12.6]), mv("r9", [33, 22], delay=0.2)),
   S("Fest durchs Tor", "Spieler drei sieht die Lücke und spielt fest durch das obere Tor zu Spieler sechs in die andere Hälfte.",
     ps("b1", [84.4, 30.6])),
   S("Weiter in der anderen Hälfte", "Gleichzeitig rücken Spieler drei, Spieler vier und Spieler fünf in die rechte Hälfte nach, Spieler zwei bleibt als wartender Spieler zurück. Spieler neun setzt sofort nach.",
     mv("n3", [50, 27]), mv("n3", [69, 12], after=True), mv("n4", [50, 34]), mv("n4", [69, 48], after=True), mv("n5", [54, 30], delay=0.3), mv("r9", [70, 30], delay=0.3))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "15 m"}, {"x1": 94, "y1": 12, "x2": 94, "y2": 48, "text": "7 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Im Rondo darf nur noch direkt gespielt werden.", "Nur ein Kontakt",
    "Team Neon spielt jetzt nur noch mit einem Kontakt. Das ist technisch schwerer und verlangt, dass jeder vorher schaut, offen steht und sofort weiß, wohin der Ball geht. Wird es zu leicht, kann das Feld auch kleiner werden.",
    sp(), [B("b1", 15.6, 30.6)] + CB,
    [S("Direkt weiter", "Spieler zwei spielt zu Spieler drei, und Spieler drei spielt direkt weiter zu Spieler fünf. Spieler neun läuft hinterher.",
       ps("b1", [32.6, 12.6]), ps("b1", [46.4, 30.6], after=True), mv("r9", [36, 22], delay=0.3)),
     S("Direkt durchs Tor", "Spieler fünf legt direkt zu Spieler vier, und Spieler vier spielt sofort fest durch das untere Tor zu Spieler sechs.",
       ps("b1", [32.6, 47.4]), ps("b1", [84.4, 30.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Durch das nächste Tor nur nach einem Prallpass.", "Prallpass vor dem Tor",
    "Durch das Tor, das am nächsten liegt, darf nicht direkt gespielt werden. Erst ein schneller Prallpass mit einem Mitspieler öffnet den Weg. Das macht es für Team Neon schwerer und verlangt gutes Zusammenspiel.",
    sp(), [B("b1", 32.6, 47.4)] + CB,
    [S("Prallpass", "Spieler vier spielt zu Spieler fünf und rückt etwas vor. Spieler fünf lässt den Ball direkt zu Spieler vier zurückprallen.",
       ps("b1", [46.4, 30.6]), mv("n4", [38, 47], delay=0.2), ps("b1", [39.6, 47.6], after=True)),
     S("Jetzt durchs Tor", "Nach dem Prallpass darf Spieler vier durch das untere Tor spielen und trifft Spieler sechs in der anderen Hälfte.",
       ps("b1", [84.4, 30.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
