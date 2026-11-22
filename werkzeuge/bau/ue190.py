import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 50-P2 (U12-U14, Woche 21 Phase 2): Beat the Chaos to Switch (Technical Activation). 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m).
# Quadrat in der Mitte 7 x 7 m (x 40.25-59.75, y 20.25-39.75): PDF nennt 5 Yards, Ton 8 Yards; 7 m, damit drei Spieler darin den
# 3D-Abstand halten. Hütchen orange statt rot. Drei Teams zu dritt: Gelb (10, 7, 8) -> Team Neon, Pink (6, 8, 9) -> Team Rot,
# Nummer neu wegen Doppelter: Rot 8 -> 5; Blau (dritte Dreiergruppe, 4, 8, 10) -> Springer F (nur zwei Teams auf der Tafel, wie UE-160).
# Positionen leicht verschoben (3D-Abstand, keine Pässe durch Hütchen), Passwege wie im PDF: Neon links oben -> Mitte -> unten,
# Rot oben -> Mitte -> rechts oben, Springer rechts unten -> Mitte -> links. Ausrichtung wie im PDF. Ein Trainer wie im PDF.
# Steigerung wie im Video: Passgeber läuft ins Quadrat (rotate in), Spieler in der Mitte läuft hinaus (rotate out), Außenspieler
# dribbelt und passt hinein. Gezeigt für Neon und Rot parallel, die Springer nur im Text.
# Sichtkegel: Text "constant scanning", "checking shoulders before receiving", Ton "check their shoulder to see space ... where
# their teammate is" -> die drei Mittelspieler schauen vor der Annahme zum Mitspieler, an den sie weiterpassen (Grundform),
# im Coaching-Punkt schaut Neon 7 über beide Schultern.
T = P("T", "c", 16, 9, "T")
POS = {"n10": (29, 18), "n7": (42, 27), "n8": (50, 50),
       "r6": (50, 10), "r5": (58.5, 26), "r9": (71, 22),
       "f3": (71, 38), "f1": (50.2, 33), "f2": (29, 34)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 19.6, 12.5), B("s2", 16, 12.5)]
LINES = [rect(25, 5, 50, 50), {"type": "zone", "x": 40.25, "y": 20.25, "w": 19.5, "h": 19.5}]
CONES = ecken(40.25, 20.25, 19.5, 19.5)

u = {"title": "Passen im Gedränge", "code": "UE-190", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "18 x 18 m",
 "description": "Team Neon, Team Rot und eine Gruppe Springer, je zu dritt, passen gleichzeitig durch ein kleines Quadrat in der Mitte. Von jeder Gruppe steht ein Spieler im Quadrat, bekommt den Ball von außen, dreht sich mit dem ersten Kontakt auf und passt zum anderen Mitspieler hinaus. Weil drei Spieler und drei Bälle gleichzeitig unterwegs sind, müssen alle vorher schauen und ihre Pässe gut timen. Nach zwei bis drei Minuten wechseln die Spieler in der Mitte.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, in der Mitte ein Quadrat von 7 mal 7 Metern mit vier Hütchen.",
  "Verteilen: Drei Gruppen zu dritt: Team Neon, Team Rot und die Springer. Von jeder Gruppe steht ein Spieler im Quadrat, die beiden anderen stehen außen verteilt. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Alle drei Gruppen spielen gleichzeitig. Ein Außenspieler passt in die Mitte, der Spieler im Quadrat nimmt den Ball in Richtung Mitspieler mit und passt hinaus. Dabei weichen sich die drei in der Mitte aus.",
  "Wechsel: Nach zwei bis drei Minuten geht ein anderer Spieler jeder Gruppe in die Mitte, bis jeder einmal dran war."],
 "organisation_show": ORG,
 "coaching_points": ["Vor der Annahme über die Schulter schauen", "Mit dem ersten Kontakt zum Mitspieler drehen", "Pässe gut timen, damit keine Bälle zusammenstoßen", "Nach jedem Pass weiterlaufen und reden"],
 "materials": ["4 Hütchen", "3 Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Passen im Gedränge. Drei Gruppen spielen gleichzeitig durch ein kleines Quadrat, und keiner darf mit den anderen zusammenstoßen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(),
  "balls": [B("b1", 29.6, 18.6), B("b2", 50.6, 10.6), B("b3", 71.6, 38.6)] + ERSATZ,
  "steps": [
   S("Schulterblick", "Die drei Spieler in der Mitte schauen gleichzeitig über die Schulter: Wo steht mein Mitspieler, und wo laufen die anderen?",
     bl("n7", [46, 43.5]), bl("r5", [74, 23]), bl("f1", [34, 35])),
   S("Pass hinein", "Alle drei Außenspieler passen gleichzeitig in die Mitte: Spieler zehn zu Spieler sieben, Spieler sechs zu Spieler fünf und der Springer rechts zum Springer in der Mitte.",
     ps("b1", [42.6, 27.6]), ps("b2", [59.1, 26.6]), ps("b3", [50.8, 33.6])),
   S("Aufdrehen", "Alle drei nehmen den Ball mit dem ersten Kontakt in Richtung Mitspieler mit und weichen sich dabei aus.",
     dr("n7", "b1", [41.5, 30.5]), dr("r5", "b2", [60, 25]), dr("f1", "b3", [48, 35.5])),
   S("Pass hinaus", "Jetzt passen alle drei gleichzeitig hinaus, und kein Ball stößt mit einem anderen zusammen. Geschafft! Die Außenspieler passen gleich wieder hinein, und nach zwei bis drei Minuten wechseln die Spieler in der Mitte.",
     ps("b1", [50.6, 50.6]), ps("b2", [71.6, 22.6]), ps("b3", [29.6, 34.6]),
     mv("n7", [42, 27], after=True), mv("r5", [58.5, 26], delay=0.6), mv("f1", [50.2, 33], delay=0.6))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor der Annahme über die Schulter schauen.", "Erst schauen, dann annehmen",
    "Bevor der Ball kommt, schaut der Spieler in der Mitte über beide Schultern. So weiß er, wo sein Mitspieler steht und wo die anderen laufen. Dann nimmt er den Ball gleich in die freie Richtung mit und stößt mit niemandem zusammen.",
    sp(), [B("b1", 29.6, 18.6), B("b3", 50.8, 33.6)] + ERSATZ,
    [S("Über beide Schultern", "Spieler zehn hat den Ball. Spieler sieben schaut zuerst über die eine Schulter, dann über die andere: Wo steht Spieler acht, und wo läuft der Springer?",
       bl("n7", [46, 43]), bl("n7", [30, 37], after=True)),
     S("In den freien Raum", "Spieler zehn passt zu Spieler sieben. Der Springer dribbelt gerade durch das Quadrat, darum nimmt Spieler sieben den Ball weg von ihm mit.",
       ps("b1", [42.6, 27.6]), dr("f1", "b3", [46.5, 35], delay=0.3), dr("n7", "b1", [40.5, 31], after=True)),
     S("Sicher hinaus", "Spieler sieben passt an dem Springer vorbei zu Spieler acht. Der Ball kommt sicher an, und Spieler acht passt gleich wieder hinein.",
       ps("b1", [50.6, 50.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Schnelle Wechsel und Dribbling.", "Wechseln und dribbeln",
    "Wer von außen in die Mitte passt, läuft gleich hinterher und ist der nächste Spieler im Quadrat. Der Spieler in der Mitte passt hinaus und läuft auf den frei gewordenen Platz außen. Der Außenspieler dribbelt ein Stück und spielt den Ball zurück in die Mitte. Alle drei Gruppen machen das gleichzeitig, die Springer genauso.",
    sp(), [B("b1", 29.6, 18.6), B("b2", 50.6, 10.6)] + ERSATZ,
    [S("Pass und hinein", "Wir schauen auf Team Neon und Team Rot. Spieler zehn passt zu Spieler sieben, Spieler sechs zu Spieler fünf. Beide laufen sofort hinterher in das Quadrat.",
       ps("b1", [42.6, 27.6]), mv("n10", [38, 15], after=True), mv("n10", [46, 21.5], after=True),
       ps("b2", [59.1, 26.6]), mv("r6", [52, 24], after=True)),
     S("Pass und hinaus", "Spieler sieben dreht auf und passt zu Spieler acht, Spieler fünf passt zu Spieler neun. Dann laufen beide hinaus auf den frei gewordenen Platz.",
       dr("n7", "b1", [43, 30.5]), ps("b1", [50.6, 50.6], after=True), mv("n7", [29, 18], after=True),
       dr("r5", "b2", [60, 25]), ps("b2", [71.6, 22.6], after=True), mv("r5", [52, 18], after=True), mv("r5", [50, 10], after=True)),
     S("Dribbeln und hinein", "Spieler acht und Spieler neun dribbeln ein Stück und spielen den Ball zurück in die Mitte, zu Spieler zehn und Spieler sechs. Jetzt sind die beiden in der Mitte dran, und alles beginnt von vorn.",
       dr("n8", "b1", [44, 49]), ps("b1", [46.6, 22.1], after=True),
       dr("r9", "b2", [71, 31]), ps("b2", [52.6, 24.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
