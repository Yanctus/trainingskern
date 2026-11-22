import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 32-P6 (U12-U14, Woche 9 Phase 2): How to Deal With Increasing Pressure. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 m),
# innere Zone 10 x 10 Yards (x 37.5-62.5, y 17.5-42.5, gestrichelt), an jeder Seite ein Minitor. Pink (Ballbesitz, 5) -> Neon
# 9, 8, 10, 4, 7; Blau (Verteidiger) -> Rot, neu nummeriert wegen doppelter Nummern: innen 5 (im PDF 7), Ecken 2, 11, 6, 3.
# Neon im Viereck leicht versetzt (3D-Abstand), ein Trainer statt zwei. Sichtkegel aus dem Text ("Checking shoulders for
# defenders joining in from outside zone"): Neon 8 schaut im Coaching-Punkt über die Schulter zum Verteidiger in der Ecke.
# Im Video kein Kegel.
T = P("T", "c", 15, 22, "T")
POS = {"n9": (37.5, 30), "n8": (46, 17.5), "n7": (54.5, 25), "n10": (63, 30), "n4": (46, 42.5),
       "r5": (54.5, 42), "r2": (29, 9), "r11": (71, 9), "r6": (29, 51), "r3": (71, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 16.6, 25.5), B("s2", 13, 25.5)]
LINES = [rect(25, 5, 50, 50), rect(37.5, 17.5, 25, 25, dashed=True)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}, {"x": 25, "y": 30, "side": "left"}, {"x": 75, "y": 30, "side": "right"}]

u = {"title": "Ballhalten gegen mehr Druck", "code": "UE-151", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 18 m",
 "description": "Fünf Spieler halten in einer inneren Zone den Ball gegen zuerst einen Verteidiger. Nach jeweils zwei Pässen darf ein weiterer Verteidiger aus der Ecke dazukommen, der Druck wird also immer größer. Erobern die Verteidiger den Ball, schießen sie schnell in das nächste der vier Minitore außen. Team Neon spielt mit zwei Kontakten.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit einem Minitor an jeder Seite. In der Mitte eine Zone von 9 mal 9 Metern.",
  "Verteilen: Fünf von Team Neon in der Zone, einer davon in der Mitte. Ein Verteidiger von Team Rot in der Zone, vier warten in den Ecken. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon hält den Ball mit zwei Kontakten. Nach jeweils zwei Pässen darf ein weiterer Verteidiger aus einer Ecke in die Zone.",
  "Wertung: Erobert Team Rot den Ball, schießt es schnell ins nächste Minitor. Jedes Tor ist ein Punkt. Dann beginnt Team Neon mit einem neuen Ball, und die Verteidiger gehen zurück in die Ecken."],
 "organisation_show": ORG,
 "coaching_points": ["Über die Schulter schauen, ob ein Verteidiger von außen kommt", "Schnelle, genaue Pässe mit zwei Kontakten", "Den Spieler in der Mitte nutzen, um aus dem Druck herauszuspielen", "Nach Ballgewinn schnell umschalten und gemeinsam pressen"],
 "materials": ["4 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Ballhalten gegen mehr Druck. Fünf gegen erst einen, dann immer mehr Verteidiger, und wer den Ball erobert, schießt sofort.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 38.1, 30.6)] + ERSATZ,
  "steps": [
   S("Zwei Pässe", "Team Neon hält den Ball in der Zone gegen Rot fünf. Neon neun spielt zu Neon acht, der spielt weiter zu Neon sieben.",
     ps("b1", [46.6, 18.1]), ps("b1", [55.1, 25.6], after=True)),
   S("Der nächste kommt", "Zwei Pässe geschafft, also darf Rot zwei aus der Ecke in die Zone. Gleichzeitig spielt Neon sieben weiter zu Neon zehn.",
     mv("r2", [40, 14.5]), ps("b1", [63.6, 30.6], delay=0.2)),
   S("Ballgewinn: Punkt", "Neon zehn will zu Neon vier passen, aber Rot fünf fängt den Ball ab, dribbelt aus der Zone und schießt ins untere Minitor. Das gibt einen Punkt für Team Rot. Dann beginnt Team Neon mit einem neuen Ball, und die Verteidiger gehen zurück in die Ecken.",
     mv("r5", [54.5, 37.5]), ps("b1", [55.1, 38.1], delay=0.2), dr("r5", "b1", [52, 47], after=True), ps("b1", [50, 54.7], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Über die Schulter schauen.", "Schulterblick",
    "Die Verteidiger kommen von außen, oft von hinten. Bevor der Ball kommt, schaut der Spieler über die Schulter. Sieht er einen Verteidiger kommen, spielt er direkt weiter, weg vom Druck.",
    sp(), [B("b1", 38.1, 30.6)] + ERSATZ,
    [S("Über die Schulter", "Neon neun hat den Ball. Neon acht schaut über die Schulter und sieht: Rot zwei kommt aus der Ecke auf ihn zu.",
       bl("n8", [29, 9]), mv("r2", [40, 14.5], after=True)),
     S("Direkt weiter", "Neon neun spielt Neon acht an. Weil er Rot zwei gesehen hat, spielt Neon acht direkt weiter zu Neon sieben, weg vom Druck. Der Ball bleibt bei Team Neon.",
       ps("b1", [46.6, 18.1]), ps("b1", [55.1, 25.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach zehn Pässen darf Team Neon schießen.", "Zehn Pässe",
    "Schafft Team Neon zehn Pässe in Folge, darf es selbst in ein Minitor schießen. Das belohnt Geduld und genaue Pässe, auch wenn immer mehr Verteidiger kommen.",
    sp(r2=(37, 13)), [B("b1", 55.1, 25.6)] + ERSATZ,
    [S("Der zehnte Pass", "Team Neon hat neun Pässe geschafft. Neon sieben spielt den zehnten zu Neon zehn.",
       ps("b1", [63.6, 30.6])),
     S("Raus und rein: Punkt", "Jetzt darf Neon zehn schießen. Er dribbelt aus der Zone und trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
       dr("n10", "b1", [68, 30]), ps("b1", [74.7, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
