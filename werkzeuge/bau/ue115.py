import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 19-P2: 25 x 15 Yards, gedreht (Neon greift nach rechts an): Feld x 12-88, y 8-52, an beiden Enden zwei Tore aus Hütchen an den Ecken.
T = P("T", "c", 6, 52, "T")
CB = [B("c1", 8.5, 52.6), B("c2", 5, 55.5)]
POS = {"f1": (12, 30), "f2": (88, 30), "n2": (42, 17), "n3": (43, 44), "r6": (52, 13), "r7": (56, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
TORE = [C(x, y) for x in (12, 88) for y in (11, 18, 42, 49)]
u = {"title": "Zu zweit verteidigen", "code": "UE-115", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 8, "field_size": "23 x 14 m",
 "description": "Zwei Angreifer von Team Neon spielen gegen zwei Verteidiger von Team Rot, an jedem Ende steht ein Anspieler. Team Neon will über den Anspieler kombinieren und mit Ball durch eines der beiden Tore am rechten Ende laufen. Die Verteidiger arbeiten als Paar: Sie blocken Pässe nach vorn, lenken die Angreifer in die Ecke und erobern dort den Ball.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 14 Metern. An beiden Enden bilden Hütchen zwei Tore an den Ecken.",
  "Verteilen: Zwei Angreifer von Team Neon und zwei Verteidiger von Team Rot im Feld. An jedem Ende steht ein Anspieler, der immer mit dem Team am Ball spielt. Der Trainer hat die Bälle.",
  "Ablauf: Der linke Anspieler startet. Team Neon spielt über den rechten Anspieler und versucht, mit Ball durch eines der beiden rechten Tore zu kommen. Das gibt einen Punkt. Team Rot will die Angreifer nach außen und nach hinten drängen.",
  "Wechsel: Erobert Team Rot den Ball, spielt es sofort nach vorn zum linken Anspieler. Nach einigen Angriffen tauschen Angreifer und Verteidiger die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Pässe nach vorn verhindern und das Spiel nach hinten lenken", "Druck machen und den Angreifern den Platz nehmen", "Als Paar miteinander sprechen", "Auf engem Raum entschlossen den Ball erobern und danach sofort nach vorn spielen"],
 "materials": ["8 Hütchen", "Mehrere Bälle beim Trainer", "Leibchen in drei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Zu zweit verteidigen. Zwei Angreifer wollen über den Anspieler durchbrechen, zwei Verteidiger arbeiten als Paar dagegen.",
 "board": {"lines": [rect(12, 8, 76, 44)], "cones": TORE, "players": sp(), "balls": [B("b1", 13.6, 30.6)] + CB,
  "steps": [
   S("Anspiel und Prallpass", "Der linke Anspieler spielt zu Neon zwei. Neon zwei spielt sofort weiter zum rechten Anspieler.",
     ps("b1", [40.4, 17.6]), ps("b1", [86.4, 30.6], after=True)),
   S("Lauf in die Tiefe", "Gleichzeitig startet Neon drei nach vorn, und der Anspieler legt ihm den Ball in den Lauf. Rot sieben läuft hinterher.",
     mv("n3", [74, 46]), ps("b1", [75.6, 46.6], delay=0.4), mv("r7", [66, 42], delay=0.3)),
   S("Durch das Tor", "Neon drei dribbelt mit Ball durch das rechte Tor. Das gibt einen Punkt für Team Neon.",
     dr("n3", "b1", [92, 46]), mv("r7", [78, 43], delay=0.2))],
  "dims": [{"x1": 12, "y1": 58.6, "x2": 88, "y2": 58.6, "text": "23 m"}, {"x1": 96, "y1": 8, "x2": 96, "y2": 52, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Passweg nach vorn zustellen.", "Pässe nach vorn blocken",
    "Der Verteidiger stellt sich so, dass er im Passweg zwischen Angreifer und rechtem Anspieler steht. Hinter ihm liegt der Deckungsschatten, in den kein Pass durchkommt. So muss der Angreifer nach hinten spielen, und Team Neon kommt nicht nach vorn.",
    sp(), [B("b1", 13.6, 30.6)] + CB,
    [S("In den Passweg", "Der linke Anspieler spielt zu Neon zwei. Gleichzeitig schiebt Rot sechs in den Passweg zum rechten Anspieler.",
       ps("b1", [40.4, 17.6]), mv("r6", [56, 21], delay=0.2)),
     S("Nur nach hinten", "Der Weg nach vorn ist zu. Neon zwei muss zurück zum linken Anspieler spielen.",
       ps("b1", [13.6, 30.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Gemeinsam in die Ecke drängen.", "In die Ecke drängen",
    "Beide Verteidiger stellen ihren Körper so, dass die Angreifer nach außen in eine Ecke laufen müssen. Dort haben sie wenig Platz und kaum Anspielstationen. Jetzt kann ein Verteidiger den Ball abfangen und sofort nach vorn zum linken Anspieler spielen.",
    sp(), [B("b1", 43.6, 17.6)] + CB,
    [S("Nach außen lenken", "Gleichzeitig greift Rot sechs Neon zwei von innen an, und Rot sieben schiebt in die Mitte. Neon zwei dribbelt in die obere Ecke.",
       mv("r6", [46, 18]), mv("r7", [52, 30], delay=0.2), dr("n2", "b1", [32, 12], delay=0.3)),
     S("Abfangen und nach vorn", "Neon zwei versucht den Pass zu Neon drei. Rot sieben fängt ihn ab und spielt sofort zum linken Anspieler. Das gibt einen Punkt für Team Rot.",
       ps("b1", [50.4, 30.6]), ps("b1", [13.6, 30.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
