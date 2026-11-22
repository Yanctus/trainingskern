import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P5: 20 x 30 Yards, gedreht (Start links, Endspieler rechts): Feld x 17-83, y 8-52. Zwei Dummys (neon Stangen) in der Mitte.
T = P("T", "c", 70, 3.5, "T")
def sp(n2=(32, 31), extra=()): return [P("n1", "a", 17, 30, "1"), P("n2", "a", n2[0], n2[1], "2"), P("n3", "a", 83, 30, "3"), T] + list(extra)
def ba(b1=(18.6, 30.6)): return [B("b1", *b1), B("c1", 72.5, 4.2), B("c2", 67.4, 3.6)]
lines = [rect(17, 8, 66, 44)]
cones = ecken(17, 8, 66, 44) + [C(41, 30, "neon", shape="stange"), C(60, 30, "neon", shape="stange")]
geh = mv("n2", [38, 24]); zeig = mv("n2", [36, 43], after=True)
u = {"title": "Antäuschen und anbieten", "code": "UE-076", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Bewegung", "Dribbling"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 3, "players_max": 4, "field_size": "27 x 18 m",
 "description": "Ein Spieler in der Mitte löst sich mit einer Finte von seinem Gegenspieler: Er macht zuerst ein paar schnelle Schritte nach vorn, als wolle er in die Tiefe, und kommt dann seitlich zurück, um sich anzubieten. So bekommt er an der Seite Platz, nimmt den Ball offen an, dribbelt an den Dummys vorbei und passt zum Spieler am anderen Ende. Danach geht es von der anderen Seite zurück.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern, in der Mitte zwei Dummys hintereinander.",
  "Verteilen: Ein Spieler mit Ball am Start, ein Spieler am anderen Ende, ein Spieler in der Mitte vor dem ersten Dummy.",
  "Ablauf: Der Mittelspieler täuscht einen Lauf nach vorn an, kommt seitlich zurück und bietet sich an. Er nimmt den Ball offen an, dribbelt an den Dummys vorbei und passt zum Endspieler. Dann von der anderen Seite das Gleiche.",
  "Wechsel: Nach zwei bis drei Durchgängen tauschen die Spieler die Rollen, damit sich der Mittelspieler erholen kann."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und scharf antäuschen, um den Gegenspieler abzuschütteln", "Offen annehmen, damit man nach vorne spielen kann", "Den Ball beim Dribbeln eng führen", "Genau zum Endspieler passen und vorher mit Ruf oder Handzeichen anzeigen"],
 "materials": ["2 Dummys", "4 orange Hütchen", "Mehrere Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Antäuschen und anbieten. Mit einer Finte löst sich der Spieler in der Mitte und bekommt an der Seite den Ball.",
 "board": {"lines": lines, "cones": cones, "players": sp(), "balls": ba(),
  "steps": [
   S("Antäuschen", "Spieler zwei macht ein paar schnelle Schritte nach vorn, als wolle er in die Tiefe. So lockt er seinen Gegenspieler mit.", geh),
   S("Anbieten und Pass", "Dann kommt er blitzschnell seitlich zurück und bietet sich an. Spieler eins spielt ihm den Ball in den freien Raum.",
     mv("n2", [36, 43]), ps("b1", [37.6, 43.6], delay=0.3)),
   S("Offen annehmen und dribbeln", "Spieler zwei nimmt den Ball offen nach vorn mit und dribbelt eng an den Dummys vorbei.",
     dr("n2", "b1", [52, 46]), dr("n2", "b1", [62, 45], after=True)),
   S("Pass zum Ende, dann zurück", "Er passt genau zu Spieler drei. Danach geht Spieler zwei vor den zweiten Dummy, und es geht von der anderen Seite zurück.",
     ps("b1", [81.4, 30.6]), mv("n2", [68, 29], after=True))],
  "dims": [{"x1": 17, "y1": 58.6, "x2": 83, "y2": 58.6, "text": "27 m"}, {"x1": 92, "y1": 8, "x2": 92, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball offen annehmen, um sofort nach vorne zu spielen.", "Offen annehmen",
    "Beim Anbieten steht der Spieler seitlich und offen, nicht mit dem Rücken zum Spielfeld. So sieht er schon vor der Annahme, was vor ihm passiert. Den Ball mit dem hinteren Fuß annehmen und gleich nach vorn mitnehmen, dann geht es ohne Pause weiter.",
    sp((38, 24)), ba(),
    [S("Seitlich anbieten", "Spieler zwei kommt seitlich zurück und dreht dabei den Körper zum Spielfeld. Spieler eins spielt den Ball.", mv("n2", [36, 43]), ps("b1", [37.6, 43.6], delay=0.3)),
     S("Mit dem ersten Kontakt nach vorn", "Mit dem hinteren Fuß nimmt er den Ball gleich nach vorn mit und sieht schon Spieler drei am Ende.", dr("n2", "b1", [50, 46]))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger darf angreifen, sobald der Pass gespielt ist.", "Mit Verteidiger",
    "Ein Verteidiger wartet an der Seite. Sobald der Pass zum Mittelspieler unterwegs ist, darf er angreifen und versucht, ihn zu berühren, bevor er in die Endzone kommt. Erst in der Endzone darf der Mittelspieler zum Endspieler passen. Den Ball eng führen und ruhig bleiben, auch unter Druck.",
    sp(extra=[P("r4", "b", 40, 12, "4")]), ba(),
    [S("Antäuschen und anbieten", "Spieler zwei täuscht nach vorn an und kommt seitlich zurück. Der Verteidiger Spieler vier wartet noch.", geh, zeig),
     S("Pass, jetzt darf er los", "Spieler eins passt, und genau jetzt darf Spieler vier angreifen.", ps("b1", [37.6, 43.6]), mv("r4", [47, 34], delay=0.3)),
     S("Vorbei in die Endzone", "Spieler zwei dribbelt eng und schnell an Spieler vier vorbei in die Endzone, ohne berührt zu werden.",
       dr("n2", "b1", [54, 47]), dr("n2", "b1", [72, 44], after=True), mv("r4", [58, 38], delay=0.2)),
     S("Pass zum Ende", "In der Endzone passt Spieler zwei zu Spieler drei. Geschafft.", ps("b1", [81.4, 30.6]))],
    lines=lines + [line(68, 8, 68, 52)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
