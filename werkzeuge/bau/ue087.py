import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P7: 20 x 40 Yards, gedreht: Feld x 10-90, y 10-50, mittlere Zone x 43.6-56.6. Neon-Paar links, Rot-Paar rechts, Rot fünf verteidigt links.
T = P("T", "c", 50, 55, "T")
lines = [rect(10, 10, 80, 40), line(43.6, 10, 43.6, 50), line(56.6, 10, 56.6, 50)]
cones = ecken(10, 10, 80, 40)
def sp(**k):
    d = dict(n2=(18.8, 17.9), n3=(23.3, 37.6), r5=(32, 25.6), r6=(89, 20), r7=(89, 41.5)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
b0 = [B("b1", 20.4, 18.5), B("c1", 52.6, 55.4)]
weiter = [ps("b1", [87.4, 21]), mv("n3", [62, 30], delay=0.2)]
u = {"title": "Annehmen und durchstarten", "code": "UE-087", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Dribbling", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "37 x 18 m",
 "description": "Ein langes Feld mit zwei Endzonen und einer Zone in der Mitte. Ein Paar spielt sich in seiner Endzone den Ball quer zu, der Mitspieler nimmt mit dem hinteren Fuß an und dribbelt mit Tempo am Verteidiger vorbei nach vorn. In der anderen Hälfte passt er zum Paar am anderen Ende und wird sofort selbst zum Verteidiger. So geht es ständig hin und her.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 18 Metern, in drei Zonen geteilt: zwei Endzonen und eine schmale Zone in der Mitte.",
  "Verteilen: An jedem Ende ein Paar. In der ersten Endzone steht zusätzlich ein Verteidiger der anderen Mannschaft.",
  "Ablauf: Der erste Spieler spielt quer zum Partner. Der nimmt an und dribbelt am Verteidiger vorbei über die mittlere Zone. In der anderen Hälfte passt er zum Paar am anderen Ende. Dort spielt einer quer zum Partner, und der Spieler, der gerade gedribbelt hat, verteidigt jetzt gegen ihn.",
  "Wechsel: Nach der ersten Runde die Seiten tauschen, damit beide Füße trainiert werden."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem hinteren Fuß in den freien Raum annehmen und losdribbeln", "Mit Hüfte und Schultern täuschen, wohin es geht", "Den Ball auf der sicheren Seite führen und mit dem Körper abschirmen", "Mit Tempo dribbeln und trotzdem die Kontrolle behalten"],
 "materials": ["4 orange Hütchen", "Markierungen für die Zonen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Annehmen und durchstarten. Den Ball offen annehmen und mit Tempo am Verteidiger vorbei nach vorn dribbeln.",
 "board": {"lines": lines, "cones": cones, "players": sp(), "balls": b0,
  "steps": [
   S("Pass quer", "Neon zwei spielt quer zu Neon drei, und zwar vor seinen Fuß.", ps("b1", [24.9, 38.2])),
   S("Annehmen und losdribbeln", "Neon drei nimmt mit dem hinteren Fuß nach vorn an und dribbelt mit Tempo los. Gleichzeitig läuft Rot fünf heraus und setzt ihn unter Druck.",
     dr("n3", "b1", [40, 41]), dr("n3", "b1", [66, 42], after=True), mv("r5", [38, 34], delay=0.2), mv("r5", [50, 37], after=True)),
   S("Pass zum anderen Ende", "In der anderen Hälfte passt Neon drei zum roten Paar am anderen Ende.", ps("b1", [87.4, 42.1])),
   S("In die andere Richtung", "Rot sieben spielt quer zu Rot sechs. Gleichzeitig wird Neon drei zum Verteidiger und läuft Rot sechs entgegen. Jetzt geht es in die andere Richtung.", *weiter)],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "37 m"}, {"x1": 4, "y1": 10, "x2": 4, "y2": 50, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Läuft der Verteidiger zu früh heraus, mit dem ersten Kontakt an ihm vorbei.", "Mit dem ersten Kontakt vorbei",
    "Ahnt der Verteidiger den Querpass und läuft früh los, kann der Angreifer ihn schon mit der Annahme ausspielen. Hüfte und Schultern zeigen erst in die eine Richtung, dann nimmt er den Ball mit dem ersten Kontakt in die andere Richtung mit. So muss er bei jeder Annahme neu entscheiden.",
    sp(), b0,
    [S("Verteidiger läuft zu früh", "Neon zwei spielt quer. Rot fünf ahnt den Pass und läuft schon früh auf Neon drei zu.", ps("b1", [24.9, 38.2]), mv("r5", [27, 32], delay=0.1)),
     S("Mit dem ersten Kontakt vorbei", "Neon drei täuscht mit der Hüfte an und nimmt den Ball mit dem ersten Kontakt an Rot fünf vorbei nach außen mit.",
       dr("n3", "b1", [32, 44]), dr("n3", "b1", [46, 42], after=True)),
     S("Weiter und Pass", "Neon drei dribbelt durch die Mitte und passt zum Paar am anderen Ende.", dr("n3", "b1", [64, 42]), ps("b1", [87.4, 42.1], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Angreifer dribbelt quer über die Mittellinie, bevor er weiterspielt.", "Über die Mittellinie",
    "Das Feld bekommt eine Linie längs durch die Mitte. Der Angreifer muss den Verteidiger ausspielen und mit dem Ball über diese Linie dribbeln, bevor er zum anderen Paar passt. Mit dem vorderen Fuß drückt er den Ball nach vorn, bringt den Körper zwischen Ball und Gegner, bleibt tief im Schwerpunkt und nimmt die Arme zum Gleichgewicht.",
    sp(n2=(20, 18), n3=(23, 40), r5=(32, 26)), [B("b1", 21.6, 18.6), B("c1", 52.6, 55.4)],
    [S("Über die Linie", "Neon zwei dribbelt schräg auf die Mittellinie zu, Rot fünf verfolgt ihn.", dr("n2", "b1", [34, 34]), mv("r5", [30, 33], delay=0.2)),
     S("Ball abschirmen", "Neon zwei bringt den Körper zwischen Ball und Rot fünf und zieht mit Tempo davon.", dr("n2", "b1", [62, 40]), mv("r5", [50, 34], delay=0.2)),
     S("Pass zum anderen Ende", "Neon zwei passt zum roten Paar am anderen Ende und wird sofort zum Verteidiger.", ps("b1", [87.4, 42.1]), mv("n2", [70, 32], delay=0.3))],
    lines=lines + [line(10, 30, 90, 30)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
