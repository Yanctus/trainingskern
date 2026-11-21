import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 94-P3: 20 x 20 Yards, gedreht: Feld x 26-74, y 6-54. In der Mitte zwei Stangen (50/24, 50/36), dazwischen der Mittelspieler.
# Zwei Quadrate für den ersten Kontakt (unten rechts x 52-61, oben links x 39-48), Hütchentore vor den Endspielern (x 34 und x 66).
T = P("T", "c", 85, 50, "T")
def zone(x, y, w, h): return {"type": "zone", "x": x, "y": y, "w": w, "h": h}
lines = [rect(26, 6, 48, 48), zone(52, 39, 9, 9), zone(39, 12, 9, 9)]
cones = ecken(26, 6, 48, 48) + [C(50, 24, "neon", shape="stange"), C(50, 36, "neon", shape="stange"), C(34, 26), C(34, 34), C(66, 26), C(66, 34)] \
      + [C(52, 39, "neon"), C(61, 39, "neon"), C(52, 48, "neon"), C(61, 48, "neon"), C(39, 12, "neon"), C(48, 12, "neon"), C(39, 21, "neon"), C(48, 21, "neon")]
def sp(**k):
    d = dict(n1=(25, 30), n4=(16.5, 30), n3=(50, 30), n2=(75, 30), n5=(83.5, 30)); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
b0 = [B("b1", 26.6, 30.6), B("c1", 87.6, 50.6)]
u = {"title": "Erster Kontakt mit Richtung", "code": "UE-093", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Ein Spieler in der Mitte bekommt den Ball zwischen zwei Stangen und nimmt ihn mit dem ersten Kontakt halb gedreht in ein kleines Quadrat mit. Von dort dribbelt er nach vorn und passt zum Endspieler, dessen erster Kontakt durch ein Hütchentor gehen muss. Dann geht es von der anderen Seite zurück, und alle laufen ihrem Pass zur nächsten Station hinterher.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. In der Mitte zwei Stangen, daneben zwei kleine Quadrate von etwa vier mal vier Metern. Vor beiden Endspielern ein kleines Hütchentor.",
  "Verteilen: An beiden Enden Spieler, einer mit Ball. Ein Spieler in der Mitte.",
  "Ablauf: Der Endspieler passt in die Mitte. Der Mittelspieler nimmt den Ball mit dem ersten Kontakt ins Quadrat mit, dribbelt nach vorn und passt zum anderen Endspieler. Dessen erster Kontakt geht durch das Hütchentor. Dann von dort zurück.",
  "Wechsel: Jeder läuft seinem Pass zur nächsten Station hinterher. Fehler sind kein Problem, einfach weiter üben."],
 "organisation_show": ORG,
 "coaching_points": ["Der erste Kontakt zeigt schon in die neue Richtung", "Den Ball unter Kontrolle und im Quadrat halten", "Den Körper vor der Annahme öffnen und über die Schulter schauen", "Genau und mit gutem Tempo passen, mit beiden Füßen annehmen und viel sprechen"],
 "materials": ["2 Stangen", "8 gelbe Hütchen für die Quadrate", "8 orange Hütchen", "Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Erster Kontakt mit Richtung. Halb gedreht annehmen und den Ball mit dem ersten Kontakt in die neue Richtung mitnehmen.",
 "board": {"lines": lines, "cones": cones, "players": sp(), "balls": b0,
  "steps": [
   S("Pass in die Mitte", "Spieler eins passt durch das Hütchentor zum Mittelspieler drei und läuft seinem Pass hinterher.", ps("b1", [48.4, 30.6]), mv("n1", [38, 30], delay=0.3)),
   S("Erster Kontakt ins Quadrat", "Spieler drei hat sich halb gedreht und nimmt den Ball mit dem ersten Kontakt direkt ins Quadrat mit.", dr("n3", "b1", [56.5, 42])),
   S("Nach vorn und Pass", "Spieler drei dribbelt kurz nach vorn und passt zu Spieler zwei. Gleichzeitig läuft Spieler eins in die Mitte.",
     dr("n3", "b1", [58, 30]), ps("b1", [73.4, 30.6], after=True), mv("n1", [50, 30], delay=0.3)),
   S("Annahme durchs Tor", "Spieler zwei nimmt den Ball mit dem ersten Kontakt durch das Hütchentor mit. Spieler drei läuft zu seiner Station, und es geht von dieser Seite zurück.",
     dr("n2", "b1", [62, 30]), mv("n3", [70, 42], delay=0.2), mv("n3", [78, 40], after=True))],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "18 m"}, {"x1": 92, "y1": 6, "x2": 92, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Körper öffnen, damit der erste Kontakt in die neue Richtung gehen kann.", "Körper öffnen",
    "Schon bevor der Ball kommt, dreht sich der Mittelspieler halb zur Seite und schaut über die Schulter. Mit offener Haltung nimmt er den Ball direkt in die neue Richtung mit, statt ihn erst zu stoppen. So ist er sofort bereit für die nächste Aktion.",
    sp(n3=(42, 30)), b0,
    [S("Hinein zwischen die Stangen", "Spieler drei läuft zwischen die Stangen und öffnet dabei den Körper. Spieler eins passt.", mv("n3", [50, 30]), ps("b1", [48.4, 30.6], delay=0.3)),
     S("Mit dem ersten Kontakt weg", "Mit offenem Körper nimmt Spieler drei den Ball sofort ins Quadrat mit.", dr("n3", "b1", [56.5, 42]))]),
  V("Steigerung", "Und jetzt die Steigerung: Am Start wird zuerst ein Doppelpass gespielt.", "Doppelpass am Start",
    "Am Start stehen zwei Spieler. Bevor der Ball in die Mitte geht, spielen sie einen kurzen Doppelpass. Das bringt mehr Pässe, verlangt gutes Timing und genaue, kurze Zuspiele.",
    sp(n4=(34, 44)), b0,
    [S("Doppelpass am Start", "Spieler eins spielt zu Spieler vier, läuft durch das Hütchentor und bekommt den Ball direkt zurück.",
       ps("b1", [35.6, 44.6]), mv("n1", [37, 30], delay=0.2), ps("b1", [38.6, 30.6], after=True)),
     S("Pass in die Mitte", "Dann passt Spieler eins zum Mittelspieler.", ps("b1", [48.4, 30.6])),
     S("Erster Kontakt ins Quadrat", "Spieler drei nimmt den Ball mit dem ersten Kontakt ins Quadrat mit.", dr("n3", "b1", [56.5, 42]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
