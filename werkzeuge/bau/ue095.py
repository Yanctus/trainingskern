import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 91-P1: Eine der beiden gleichen Bahnen (15 x 30 Yards) gedreht: Start links, Minitor rechts. Feld x 10-90, y 10-50.
# Dummys (gelbe Stangen) bei x 52. Neon: Innenverteidiger 5 und 6, Mittelfeldspieler 4, wartend 10. Rot 8 verteidigt.
T = P("T", "c", 12, 4, "T")
D1 = [(52, 21.7), (52, 39)]
D2 = [(68, 14), (68, 30), (68, 46)]
def dummys(extra=False, ids=False):
    pts = D1 + (D2 if extra else [])
    return [C(x, y, "neon", shape="stange", **({"id": f"d{i}"} if ids else {})) for i, (x, y) in enumerate(pts)] + \
           [C(x, y, **({"id": f"e{i}"} if ids else {})) for i, (x, y) in enumerate([(10, 10), (90, 10), (10, 50), (90, 50)])]
def sp(**k):
    d = dict(n5=(17.6, 21), n6=(20.7, 42.5), n4=(39, 32), n10=(5, 21), r8=(70, 30)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
cb = [B("c1", 14.6, 4.6), B("c2", 9.5, 6.5)]
goals = [{"x": 90, "y": 30, "side": "right"}]
auf = [ps("c1", [19.2, 21.6]), ps("c1", [37.4, 32.6], after=True), mv("n6", [36, 46], delay=0.3)]
u = {"title": "Abwehrspieler rückt auf", "code": "UE-095", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 14 m",
 "description": "Ein Innenverteidiger lernt, mit Ball aufzurücken und sich zwischen den Linien anzubieten. Der erste Innenverteidiger spielt zum Mittelfeldspieler, der zweite rückt währenddessen nach vorn und bekommt den Ball an den Dummys vorbei. Dann spielen beide zu zweit gegen einen Verteidiger auf das Minitor. Zwei gleiche Bahnen laufen gleichzeitig nebeneinander.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, längs in zwei gleiche Bahnen geteilt. In jeder Bahn zwei Dummys in der Mitte und ein Minitor am Ende.",
  "Verteilen: Pro Bahn zwei Innenverteidiger und ein Mittelfeldspieler, dahinter wartende Spieler. Ein Verteidiger hinter den Dummys. Der Trainer steht mit Bällen am Start.",
  "Ablauf: Der Trainer spielt den ersten Innenverteidiger an, der passt zum Mittelfeldspieler. Gleichzeitig rückt der zweite Innenverteidiger auf und bekommt den Ball hinter den Dummys. Dann zwei gegen eins auf das Minitor, ein Tor gibt einen Punkt.",
  "Ballgewinn und Wechsel: Erobert der Verteidiger den Ball, dribbelt er zwischen den Dummys hindurch und holt so einen Punkt. Nach zwei bis drei Durchgängen wechselt der Verteidiger."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo durch die Linie passen", "Der Innenverteidiger startet im richtigen Moment nach vorn", "Die Überzahl im letzten Feld mit einem schnellen Doppelpass nutzen", "Offen annehmen und den ersten Kontakt nach vorn mitnehmen"],
 "materials": ["4 Dummys", "2 Minitore", "Hütchen", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Abwehrspieler rückt auf. Der Innenverteidiger startet nach vorn und bekommt den Ball zwischen den Linien.",
 "board": {"lines": [rect(10, 10, 80, 40)], "cones": dummys(), "goals": goals, "players": sp(), "balls": cb,
  "steps": [
   S("Aufbau", "Der Trainer spielt Spieler fünf an, der passt weiter zu Spieler vier. Gleichzeitig startet Spieler sechs nach vorn.", *auf),
   S("An den Dummys vorbei", "Spieler vier spielt den Ball an den Dummys vorbei in den Lauf von Spieler sechs und läuft selbst mit nach vorn.",
     mv("n6", [58, 46]), ps("c1", [59.6, 46.6], delay=0.3), mv("n4", [50, 30]), mv("n4", [64, 20], after=True)),
   S("Zwei gegen eins", "Rot acht geht auf Spieler sechs. Der spielt sofort quer zu Spieler vier, der frei ist.",
     mv("r8", [64, 40]), ps("c1", [65.6, 20.6], delay=0.3)),
   S("Abschluss: Punkt", "Spieler vier schießt ins Minitor, und das gibt einen Punkt für Neon.", ps("c1", [90, 28]))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "27 m"}, {"x1": 96, "y1": 10, "x2": 96, "y2": 50, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erobert der Verteidiger den Ball, dribbelt er zwischen den Dummys hindurch.", "Ball erobert, durch die Dummys",
    "Spielt der Mittelfeldspieler ungenau, kann der Verteidiger den Ball erobern. Dann dribbelt er sofort zwischen den Dummys hindurch, wie bei einem Konter durch das Mittelfeld. Das gibt einen Punkt für seine Mannschaft.",
    sp(n6=(30, 47), r8=(62, 34)), [B("c1", 37.4, 32.6), B("c2", 9.5, 6.5)],
    [S("Pass abgefangen", "Spieler vier spielt zu ungenau, und Rot acht fängt den Pass ab.", ps("c1", [56, 37]), mv("r8", [57.5, 36], delay=0.2)),
     S("Durch die Dummys: Punkt", "Rot acht dribbelt sofort zwischen den Dummys hindurch, und das gibt einen Punkt für Rot.", dr("r8", "c1", [44, 30]))]),
  V("Steigerung", "Und jetzt die Steigerung: Eine zweite Reihe Dummys kommt dazu.", "Zwei Reihen Dummys",
    "Eine zweite Reihe Dummys steht weiter vorn. Jetzt müssen Pass und Lauf noch besser abgestimmt sein. Die Spieler erkennen, wann sie durch eine Lücke spielen und wann um die Dummys herum.",
    sp(r8=(84, 26)), cb,
    [S("Aufbau", "Wie gehabt: Trainer zu Spieler fünf, weiter zu Spieler vier, und Spieler sechs startet.", *auf),
     S("Zwischen die Linien", "Spieler vier spielt an der ersten Reihe vorbei zu Spieler sechs, der zwischen den beiden Reihen anbietet. Spieler vier läuft mit.",
       mv("n6", [60, 46]), ps("c1", [61.6, 46.6], delay=0.3), mv("n4", [50, 30]), mv("n4", [60, 22], after=True)),
     S("Durch die zweite Reihe", "Spieler sechs spielt durch die Lücke der zweiten Reihe in den Lauf von Spieler vier, und der schießt ins Minitor. Das gibt einen Punkt für Neon.",
       mv("n4", [72, 22]), mv("n4", [78, 36], after=True), ps("c1", [79.6, 36.6], delay=0.5), ps("c1", [90, 32], after=True), mv("r8", [82, 22]))],
    cones=dummys(True, True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
