import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 14-P3: 25 x 25 Yards (Feld 26/6, 48 x 48). Drei Spieler je Seite, Dummys in einer Reihe in der Mitte.
T = P("T", "c", 90, 40, "T")
DU = [P("d1", "t", 50, 12, "D"), P("d2", "t", 50, 30, "D"), P("d3", "t", 50, 48, "D")]
POS = {"n2": (26, 14), "n3": (26, 30), "n4": (26, 46), "n5": (74, 14), "n6": (74, 30), "n7": (74, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + DU + [T]
CB = [B("c1", 92.5, 40.6), B("c2", 89, 43.5)]
feld = rect(26, 6, 48, 48)
u = {"title": "Aufdrehen am Dummy", "code": "UE-106", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "23 x 23 m",
 "description": "An beiden Enden eines Feldes stehen je drei Spieler, in der Mitte steht eine Reihe Dummys. Ein Spieler von der einen Seite bietet sich vor einem Dummy an, nimmt den Ball mit dem ersten Kontakt quer am Dummy vorbei und spielt zur anderen Seite durch. So lernen Mittelfeldspieler, sich frei zu laufen, offen anzunehmen und nach vorn zu spielen.",
 "organisation": ["Aufbauen: Ein Feld von etwa 23 mal 23 Metern. In der Mitte stehen drei Dummys in einer Reihe.",
  "Verteilen: Mindestens sechs Spieler, je drei an den beiden Enden. Ein Spieler links hat den Ball.",
  "Ablauf: Ein Spieler der rechten Seite läuft vor einen Dummy und wird angespielt. Er nimmt den Ball quer am Dummy vorbei mit und spielt zur rechten Seite durch, dann läuft er zurück. Danach geht es in die andere Richtung.",
  "Wechsel: Wer anbietet, wechselt ständig, damit jeder oft annimmt. Mit ein oder zwei Kontakten spielen."],
 "organisation_show": ORG,
 "coaching_points": ["Guter erster Kontakt: sicher und nach vorn mitnehmen", "Offen zum Ball stehen, um beide Seiten zu sehen", "Pass genau, mit dem richtigen Tempo und der passenden Art", "Den Lauf zum Dummy richtig timen"],
 "materials": ["3 Dummys", "4 orange Hütchen", "Mehrere Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Aufdrehen am Dummy. Freilaufen, offen annehmen und zur anderen Seite durchspielen.",
 "board": {"lines": [feld], "cones": ecken(26, 6, 48, 48), "players": sp(), "balls": [B("b1", 27.6, 14.6)] + CB,
  "steps": [
   S("Vor dem Dummy anbieten", "Spieler fünf läuft von rechts vor den ersten Dummy und bietet sich an. Spieler zwei spielt ihn flach an.",
     mv("n5", [41, 16]), ps("b1", [42.6, 16.6], delay=0.4)),
   S("Quer mitnehmen und durchspielen", "Spieler fünf nimmt den Ball mit dem ersten Kontakt quer am Dummy vorbei und spielt zu Spieler sechs durch. Danach läuft er zurück auf seinen Platz.",
     dr("n5", "b1", [59, 22]), ps("b1", [72.4, 30.6], after=True), mv("n5", [74, 14], after=True)),
   S("Jetzt in die andere Richtung", "Jetzt läuft Spieler drei von links vor den mittleren Dummy, und Spieler sechs spielt ihn an.",
     mv("n3", [44, 39]), mv("n3", [59, 34], after=True), ps("b1", [57.4, 34.6], delay=0.6)),
   S("Quer mitnehmen und durchspielen", "Spieler drei nimmt den Ball quer am Dummy vorbei mit, spielt zu Spieler vier durch und läuft zurück.",
     dr("n3", "b1", [41, 40]), ps("b1", [27.6, 46.6], after=True), mv("n3", [26, 30], after=True))],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "23 m"}, {"x1": 82, "y1": 6, "x2": 82, "y2": 54, "text": "23 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Ball wird hinter dem Dummy angenommen.", "Annahme hinter dem Dummy",
    "Jetzt läuft der Spieler hinter den Dummy, also auf die Seite, die vom Passgeber weg zeigt. Er nimmt den Ball kontrolliert um den Dummy herum mit und spielt durch die Lücke zwischen zwei Dummys zur Seite des Passgebers zurück. So übt er Übersicht, Ballkontrolle und schnelles Aufdrehen unter Druck.",
    sp(), [B("b1", 27.6, 30.6)] + CB,
    [S("Hinter dem Dummy anbieten", "Spieler sechs läuft von rechts hinter den mittleren Dummy, gleichzeitig spielt Spieler drei an ihm vorbei.",
       mv("n6", [59, 22]), ps("b1", [57.4, 22.6], delay=0.3)),
     S("Herum und durch die Lücke", "Spieler sechs nimmt den Ball in einem Bogen um den Dummy herum mit und spielt durch die Lücke zu Spieler vier.",
       dr("n6", "b1", [61, 30]), dr("n6", "b1", [59, 37], after=True), ps("b1", [27.6, 46.6], after=True)),
     S("Zurück auf den Platz", "Spieler sechs läuft zurück auf seinen Platz, und der Nächste bietet sich an.",
       mv("n6", [74, 30]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Trainer ruft, zu welcher Seite der Ball geht.", "Trainer ruft die Seite",
    "Der Trainer ruft, zu welcher Seite der Ball nach der Annahme gespielt wird: durch zur anderen Seite oder zurück zur gleichen Seite. Die Spieler müssen zuhören und schnell reagieren. Ruft der Trainer nichts, entscheidet der Spieler selbst und sagt laut an, wohin er spielt.",
    sp(), [B("b1", 72.4, 30.6)] + CB,
    [S("Anbieten auf Zuruf", "Spieler drei läuft von links vor den mittleren Dummy, und Spieler sechs spielt ihn an. Der Trainer ruft: Rechts!",
       mv("n3", [44, 39]), mv("n3", [59, 34], after=True), ps("b1", [57.4, 34.6], delay=0.6)),
     S("Zurück zur gleichen Seite", "Spieler drei dreht und spielt nicht durch, sondern zurück zu Spieler sieben auf der rechten Seite. Dann läuft er zurück auf seinen Platz.",
       ps("b1", [72.4, 46.6]), mv("n3", [44, 39], after=True), mv("n3", [26, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
