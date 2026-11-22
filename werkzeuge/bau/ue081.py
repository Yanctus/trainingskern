import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 19-P6: 30 x 20 Yards, gedreht: Feld x 12-88, y 5-55, vier Viertel (Linien x 50 und y 30), Tore links/rechts mit Torwart.
# Neon (Torwart 1) spielt nach rechts, Rot (Torwart 6) nach links. In jedem Viertel ein 1 gegen 1.
T = P("T", "c", 56, 1.5, "T")
lines = [rect(12, 5, 76, 50), line(50, 5, 50, 55), line(12, 30, 88, 30)]
cones = ecken(12, 5, 76, 50) + [C(50, 5), C(50, 55)]
goals = [{"x": 12, "y": 30, "side": "left"}, {"x": 88, "y": 30, "side": "right"}]
def sp(**k):
    d = dict(n1=(14.5, 30), n2=(26.7, 16.7), n3=(29, 44), n4=(63, 18), n5=(64, 42), r6=(85.5, 30), r7=(35, 17.5), r8=(37.5, 44), r9=(71.5, 19.5), r10=(72.5, 42)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
cb = [B("c1", 58.6, 2)]
u = {"title": "Vier Felder, vier Duelle", "code": "UE-081", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Verteidigen", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 18 m",
 "description": "Vier gegen vier mit Torwart auf zwei Tore. Das Feld ist in vier Viertel geteilt, in jedem Viertel steht ein Spieler gegen einen Gegenspieler. Jeder ist für sein eigenes Duell verantwortlich: im Angriff freilaufen und sich anbieten, in der Abwehr eng dranbleiben. Gewinnt jeder sein Duell, entstehen Torchancen für die Mannschaft.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern mit einem Tor an jedem Ende. Mit Hütchen in vier gleich große Viertel teilen.",
  "Verteilen: Zwei Mannschaften mit je vier Feldspielern und einem Torwart. In jedem Viertel steht ein Spieler jeder Mannschaft, also ein Eins gegen Eins.",
  "Ablauf: Jeder Spieler bleibt in seinem Viertel. Der Ball wird vom Torwart über die eigene Hälfte nach vorn gespielt. Die Angreifer lösen sich mit Antäuschen und Anbieten von ihrem Gegenspieler und versuchen zu treffen. Jedes Tor gibt einen Punkt.",
  "Trainer: Geht der Ball ins Aus, spielt der Trainer schnell einen neuen Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Im eigenen Viertel freilaufen: antäuschen und anbieten", "Schnell kombinieren, um den Gegenspieler abzuschütteln", "Eng verteidigen und den Weg nach vorn zustellen", "Nach Ballgewinn sofort an den Konter denken und eiskalt abschließen"],
 "materials": ["2 Tore", "6 orange Hütchen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Vier Felder, vier Duelle. In jedem Viertel ein Eins gegen Eins, und jeder ist für sein Duell verantwortlich.",
 "board": {"lines": lines, "cones": cones, "goals": goals, "players": sp(), "balls": [B("b1", 16.1, 30.6)] + cb,
  "steps": [
   S("Aufbau vom Torwart", "Torwart eins spielt Spieler zwei an. Spieler sieben bleibt eng an ihm dran.", ps("b1", [28.3, 17.3]), mv("r7", [31, 12], delay=0.3)),
   S("Anbieten und nach vorn", "Spieler fünf täuscht kurz an und kommt seinem Gegenspieler entgegen. Spieler zwei spielt ihn diagonal an.",
     mv("n5", [60, 38]), ps("b1", [61.6, 38.6], delay=0.3)),
   S("Hinter die Abwehr", "Spieler vier läuft im Bogen hinter Spieler neun in den freien Raum, und Spieler fünf spielt ihn an.",
     mv("n4", [70, 12]), mv("n4", [77.7, 18], after=True), ps("b1", [79.3, 18.6], delay=0.5)),
   S("Abschluss", "Spieler vier schießt flach ins Eck, und das gibt einen Punkt für Neon.", ps("b1", [88, 27]))],
  "dims": [{"x1": 12, "y1": 58.6, "x2": 88, "y2": 58.6, "text": "27 m"}, {"x1": 95, "y1": 5, "x2": 95, "y2": 55, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach einem Ballgewinn sofort kontern.", "Ball erobert, sofort Konter",
    "Wer den Ball abfängt, schaltet sofort um. Der schnelle Pass nach vorn erwischt die Gegner, bevor sie sich ordnen. Mit dem Pass nach vorn darf ein Spieler mitlaufen, dann steht es im Angriff zwei gegen eins. Schnell kombinieren und entschlossen abschließen.",
    sp(), [B("b1", 64.6, 18.6)] + cb,
    [S("Ball erobert", "Spieler vier will zu Spieler fünf passen, aber Spieler zehn liest den Pass und fängt ihn ab.", ps("b1", [66, 34]), mv("r10", [67, 35.5])),
     S("Sofort nach vorn", "Spieler zehn spielt sofort nach vorn zu Spieler acht und sprintet gleich hinterher. Jetzt steht es zwei gegen eins gegen Spieler drei.",
       ps("b1", [39.1, 44.6]), mv("r10", [44, 34], delay=0.3)),
     S("Zwei gegen eins: Punkt", "Spieler acht legt quer zu Spieler zehn, und der schießt ins Tor. Das gibt einen Punkt für Rot.",
       ps("b1", [42.4, 34.6]), ps("b1", [12, 34], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Mit dem Pass nach vorn darf ein Spieler mit in die Angriffshälfte.", "Einer rückt mit auf",
    "Spielt eine Mannschaft den Ball nach vorn in die Angriffshälfte, darf der Passgeber mitlaufen. So entsteht vorne ein Zwei gegen Eins. Das schult das richtige Timing für den Lauf und das Ausspielen der Überzahl.",
    sp(n2=(42, 18), r7=(33.5, 24), n4=(68, 14), r9=(76.5, 22)), [B("b1", 43.6, 18.6)] + cb,
    [S("Pass nach vorn und mit", "Spieler zwei spielt nach vorn zu Spieler vier und läuft gleich mit in die Angriffshälfte. Jetzt steht es zwei gegen eins.",
       ps("b1", [66.4, 14.6]), mv("n2", [62, 26], delay=0.3)),
     S("Überzahl ausspielen", "Spieler neun geht auf Spieler vier. Der legt sofort quer zu Spieler zwei, der frei ist.", mv("r9", [72, 17]), ps("b1", [63.6, 26.6], delay=0.3)),
     S("Abschluss", "Spieler zwei schießt sofort, und das gibt einen Punkt für Neon.", ps("b1", [88, 34.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
