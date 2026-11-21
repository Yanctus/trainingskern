import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 97-P3: 16 x 20 Yards, gedreht: Feld x 22-78, y 7.6-52.4, Mittellinie x 50. Links Neon (6 Spieler) mit zwei roten Pressern, rechts die anderen vier Roten.
T = P("T", "c", 88, 3, "T")
lines = [rect(22, 7.6, 56, 44.8), line(50, 7.6, 50, 52.4)]
cones = ecken(22, 7.6, 56, 44.8) + [C(50, 7.6), C(50, 52.4)]
def sp(**k):
    d = dict(n4=(22.7, 16.8), n3=(21.3, 44.6), n5=(33.4, 4.4), n2=(34.5, 54), n6=(50, 21), n8=(50, 42.3),
             r9=(40, 21.5), r7=(36, 37.5), r10=(78.8, 20), r11=(78.8, 41.5), r12=(66.9, 4.2), r13=(65.7, 53.2)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
b0 = [B("b1", 22.9, 45.2), B("c1", 90.6, 3.6)]
u = {"title": "Zehn Pässe für einen Punkt", "code": "UE-091", "kind": "Spielform",
 "focuses": ["Passspiel", "Verteidigen", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "18 x 15 m",
 "description": "Ein Rondo in zwei Hälften. In der einen Hälfte spielen sechs gegen zwei: Schafft die Passmannschaft zehn Pässe in Folge, gibt das einen Punkt. Erobern die zwei Verteidiger den Ball, spielen sie ihn sofort in ihre eigene Hälfte zu ihren Mitspielern. Dort geht es sechs gegen zwei weiter, jetzt mit zwei Verteidigern der anderen Mannschaft.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 15 Metern, in der Mitte geteilt. Jede Mannschaft hat ihre eigene Hälfte.",
  "Verteilen: Zwei Mannschaften mit je sechs Spielern. Zwei Spieler der einen Mannschaft pressen in der Hälfte der anderen.",
  "Ablauf: Sechs gegen zwei. Zehn Pässe in Folge geben einen Punkt. Erobern die Presser den Ball, spielen sie ihn sofort in die eigene Hälfte, während die anderen versuchen, den Ball direkt zurückzuerobern.",
  "Wechsel: Klappt der Pass in die andere Hälfte, wechseln zwei Spieler der Mannschaft, die den Ball verloren hat, hinüber und pressen dort."],
 "organisation_show": ORG,
 "coaching_points": ["Sich ohne Ball so bewegen, dass Passwinkel entstehen", "Erst langsam spielen, um die Presser zu locken, dann schnell durch die Linie", "Als Paar kompakt pressen und Passwege zustellen", "Mit der Körperhaltung die Richtung vorgeben"],
 "materials": ["6 Hütchen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Zehn Pässe für einen Punkt. Sechs gegen zwei, und wer den Ball erobert, spielt ihn sofort hinüber.",
 "board": {"lines": lines, "cones": cones, "players": sp(), "balls": b0,
  "steps": [
   S("Sechs gegen zwei", "Neon spielt sich den Ball zu, Neon drei passt zu Neon vier. Gleichzeitig verschieben Rot neun und Rot sieben gemeinsam.",
     ps("b1", [24.3, 17.4]), mv("r9", [36, 18], delay=0.2), mv("r7", [38, 32], delay=0.2)),
   S("Ball abgefangen", "Neon vier spielt zu Neon fünf, der will weiter zu Neon sechs. Rot neun ahnt den Pass und fängt ihn ab.",
     ps("b1", [35, 5.4]), ps("b1", [44.4, 15.6], after=True), mv("r9", [44, 14.5], delay=0.3)),
   S("Sofort hinüber", "Rot neun spielt den Ball sofort hinüber in die eigene Hälfte zu Rot zehn. Neon versucht noch, den Ball zurückzuerobern.",
     ps("b1", [77.2, 20.6]), mv("n6", [52, 15], delay=0.1)),
   S("Neue Rollen", "Jetzt spielen die Roten sechs gegen zwei. Gleichzeitig laufen Rot neun und Rot sieben hinüber, und Neon sechs und Neon acht pressen als neues Paar.",
     mv("r9", [62, 13]), mv("r7", [62, 46]), mv("n6", [62, 24], delay=0.2), mv("n8", [64, 36], delay=0.2))],
  "dims": [{"x1": 22, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "18 m"}, {"x1": 95, "y1": 7.6, "x2": 95, "y2": 52.4, "text": "15 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Pass genau zwischen den beiden Pressern hindurch gibt einen Punkt.", "Zwischen den Pressern durch",
    "Jetzt gibt auch ein Pass einen Punkt, der genau zwischen den beiden Verteidigern hindurchgeht. Die Passmannschaft achtet darauf, wann die Lücke zwischen ihnen groß wird, und spielt dann möglichst direkt hindurch. Die Verteidiger müssen dafür eng zusammenbleiben.",
    sp(r9=(38, 22), r7=(40, 45), n2=(30, 54)), b0,
    [S("Presser gehen drauf", "Neon drei passt zu Neon vier. Rot neun läuft auf ihn zu, Rot sieben bleibt weiter hinten, und zwischen den beiden geht eine Lücke auf.",
       ps("b1", [24.3, 17.4]), mv("r9", [31, 20], delay=0.2)),
     S("Durch die Lücke: Punkt", "Neon vier spielt genau zwischen den beiden Roten hindurch zu Neon acht, und das gibt einen Punkt für Neon.", ps("b1", [48.4, 42.9]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein dritter Verteidiger kommt dazu, jetzt heißt es sechs gegen drei.", "Sechs gegen drei",
    "Ein dritter Spieler darf mitpressen. Die Passmannschaft hat weniger Platz und muss schneller entscheiden. Die Spieler stehen auf verschiedenen Linien, damit es immer mehrere Anspielstationen gibt und keine geraden, leicht abfangbaren Pässe. Die drei Verteidiger pressen, sichern ab und bleiben kompakt.",
    sp(), b0,
    [S("Der Dritte kommt", "Neon drei spielt zu Neon vier. Gleichzeitig sprintet Rot zehn aus der eigenen Hälfte herüber und presst mit.",
       ps("b1", [24.3, 17.4]), mv("r10", [42, 29], delay=0.1), mv("r9", [34, 18], delay=0.2)),
     S("Zu dritt erobert", "Neon vier findet keinen freien Mitspieler, spielt ungenau zu Neon acht, und Rot sieben erobert den Ball.",
       ps("b1", [37.6, 36.6]), mv("r7", [37, 35], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
