import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 88-P5 (U12-U14, Woche 8 Phase 4): The Transitional Rondo - Play to Target Player. 15 x 40 Yards, quer gelegt (sonst zu schmal):
# Feld x 10-90, y 12-48 (37 x 14 m), drei Zonen 15/10/15 Yards (x 10-40, 40-60, 60-90, gestrichelt).
# Gelb -> Neon (6, 8 in Zone 1; 10, 7 in der Mitte), Pink -> Rot (4, 5; 3, 2), Navy -> neutrale Springer F (zwei in Zone 1,
# einer als Zielspieler in Zone 3). Positionen als Rondo-Viereck um die zwei Roten gesetzt (3D-Abstand). Ein Trainer statt zwei.
# Dass ein Springer in der Mitte mitspielt, steht nur im Text. Sichtkegel aus dem Text ("Spot the gaps left behind and make forward
# runs"): im zweiten Coaching-Punkt schaut Neon 10 in die Lücke hinter dem pressenden Gegner. Im Video kein Kegel.
T = P("T", "c", 5, 8, "T")
POS = {"f1": (12, 30), "f2": (38, 30), "n6": (25, 13.5), "n8": (25, 46.5), "r4": (20.5, 30), "r5": (29.5, 30),
       "n10": (47, 16), "r3": (47, 33), "r2": (56, 22), "n7": (56, 44), "f3": (80, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 6.6, 4.5), B("s2", 3, 4.5)]
LINES = [rect(10, 12, 80, 36), line(40, 12, 40, 48), line(60, 12, 60, 48)]

u = {"title": "Umschalt-Rondo durch drei Zonen", "code": "UE-150", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 11, "players_max": 11, "field_size": "37 x 14 m",
 "description": "Ein Rondo über drei Zonen mit zwei Teams zu viert und drei Springern. In der ersten Zone spielt ein Team mit zwei Springern gegen zwei Gegner und darf nach drei Pässen in die Mitte spielen. Dort wird mit einem Springer zwei gegen zwei gespielt, bis der Ball zum Zielspieler in der dritten Zone kommt. Das ist ein Punkt, dann geht es in die andere Richtung, und wer den Ball erobert, ist selbst am Ball.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 14 Metern in drei Zonen: 14 Meter, 9 Meter, 14 Meter.",
  "Verteilen: Team Neon und Team Rot je zu viert, zwei in der ersten Zone und zwei in der Mitte. Zwei Springer in der ersten Zone, einer als Zielspieler in der dritten. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: In der ersten Zone drei Pässe, dann in die Mitte. Dort kommt ein Springer dazu, die Mitte kombiniert und spielt durch zum Zielspieler.",
  "Wertung und Wechsel: Der Pass zum Zielspieler ist ein Punkt. Dann rücken alle eine Zone weiter, und es geht in die andere Richtung. Erobert das andere Team den Ball, ist es am Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Zu zweit pressen und dem Gegner die Richtung vorgeben", "Kurze, scharfe Pässe, um die Überzahl zu nutzen", "Erkennen, wann der Ball nach vorn kann, und schnell kombinieren", "Nach Ballverlust sofort pressen und laut miteinander reden"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Umschalt-Rondo durch drei Zonen. Team Neon spielt den Ball von der ersten Zone über die Mitte bis zum Zielspieler.",
 "board": {"lines": LINES, "cones": [], "players": sp(), "balls": [B("b1", 12.6, 30.6)] + ERSATZ,
  "steps": [
   S("Drei Pässe", "In der ersten Zone spielt Team Neon mit den zwei Springern gegen Rot vier und Rot fünf. Erst nach drei Pässen in Folge darf der Ball in die Mitte.",
     ps("b1", [25.6, 14.1]), ps("b1", [38.6, 30.6], after=True), ps("b1", [25.6, 47.1], after=True)),
   S("In die Mitte", "Jetzt spielt Neon acht in die Mitte zu Neon sieben. Rot zwei presst sofort, und Neon zehn läuft in die Lücke.",
     ps("b1", [56.6, 44.6]), mv("r2", [50, 40], delay=0.3), mv("n10", [55, 25], delay=0.3)),
   S("Zum Zielspieler: Punkt", "Neon sieben spielt zu Neon zehn, und der spielt durch zum Springer in der dritten Zone. Das gibt einen Punkt für Team Neon. Dann rücken alle eine Zone weiter, und es geht in die andere Richtung.",
     ps("b1", [55.6, 25.6]), ps("b1", [80.6, 30.6], after=True))],
  "dims": dims(10, 90, 12, 48, "37 m", "14 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zu zweit pressen.", "Zu zweit pressen",
    "Die beiden Verteidiger arbeiten als Paar. Der erste läuft den Ballführenden so an, dass eine Seite zu ist. Damit weiß der zweite, wohin der Pass gehen muss, und kann ihn abfangen.",
    sp(), [B("b1", 25.6, 14.1)] + ERSATZ,
    [S("Richtung vorgeben", "Neon sechs hat den Ball. Rot vier läuft ihn so an, dass der Pass nach links zu ist. Jetzt weiß Rot fünf, wohin der Ball gehen muss.",
       mv("r4", [22.5, 21])),
     S("Abfangen: Ballbesitz", "Neon sechs spielt nach rechts, aber Rot fünf steht schon im Passweg und fängt den Ball ab. Jetzt ist Team Rot am Ball und spielt mit den Springern weiter.",
       mv("r5", [33, 24]), ps("b1", [33.6, 24.6], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Lücke sehen und hineinlaufen.", "In die Lücke",
    "Presst ein Gegner nach vorn, entsteht hinter ihm eine Lücke. Wer sich umschaut, sieht sie und läuft genau im richtigen Moment hinein. So bekommt er den Ball hinter dem Pressing.",
    sp(), [B("b1", 56.6, 44.6)] + ERSATZ,
    [S("Lücke sehen", "Rot zwei presst Neon sieben. Neon zehn schaut sich um und sieht: Hinter Rot zwei ist jetzt eine Lücke.",
       mv("r2", [53, 38]), bl("n10", [60, 27], after=True)),
     S("Hinein: Punkt", "Neon zehn startet in die Lücke, Neon sieben spielt ihn an, und er spielt durch zum Springer in der dritten Zone. Das gibt einen Punkt für Team Neon.",
       mv("n10", [60, 26]), ps("b1", [60.6, 26.6], delay=0.3), ps("b1", [80.6, 30.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
