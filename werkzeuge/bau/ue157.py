import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 100-P4 (U12-U14, Woche 11 Phase 3): One Touch Passing Combinations. 10 x 15 Yards hochkant = Feld x 33.3-66.7, y 5-55 (9 x 14 m),
# sechs Hütchen als passive Gegenspieler wie im PDF. Alle Spieler pink -> Neon: 6 (Start mit Ball), 10 (oben), 7 und 11 (warten
# unten links/rechts). Trainer oben rechts etwas neben das Feld gerückt (3D-Abstand). Grundform über die rechte Seite, die
# nächste Runde über links nur im Text. Coaching-Punkt nach PDF-Skizze (Pass in den Lauf, dort nach links).
# Sichtkegel: im Ton "concentration and awareness" bei der Steigerung (Richtungswechsel); im Video kein Kegel eingezeichnet.
# Darum in der Steigerung ein Schulterblick von Spieler sechs nach unten zu Spieler elf, bevor der Ball zurückkommt.
T = P("T", "c", 72, 5, "T")
POS = {"n10": (50, 5), "n6": (50, 52.5), "n7": (40, 53), "n11": (60, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 75.6, 8.5), B("s2", 72, 8.5)]
LINES = [rect(33.3, 5, 33.4, 50)]
KEGEL = [C(45.4, 15.2), C(55, 15.2), C(38.3, 29.3), C(61.8, 29.3), C(45.4, 43.1), C(55, 43.1)]

u = {"title": "Kombinieren mit Direktpässen", "code": "UE-157", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 4, "players_max": 8, "field_size": "9 x 14 m",
 "description": "Eine feste Passfolge mit lauter Direktpässen. Ein Spieler dribbelt in die Mitte und spielt nach oben, dann läuft der Ball mit einem Kontakt über die Seite bis zum anderen Ende. Sechs Hütchen im Feld stehen für Gegenspieler. Nach jeder Runde wechseln die Spieler die Station, und die Passfolge geht über die andere Seite.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern. Sechs Hütchen im Feld stehen für Gegenspieler, die nur im Weg stehen.",
  "Verteilen: Ein Spieler von Team Neon oben in der Mitte, einer unten mit Ball, zwei warten unten links und rechts. Der Trainer steht oben rechts mit Bällen.",
  "Ablauf: Der Spieler mit Ball dribbelt in die Mitte und passt nach oben. Danach wird nur noch direkt gespielt: zurück, nach außen, zurück, in die Tiefe und zum Schluss nach unten.",
  "Wechsel: Der Spieler aus der Mitte geht nach oben, der Spieler von oben stellt sich unten an. Jede Runde wechselt die Seite, einmal rechts, einmal links."],
 "organisation_show": ORG,
 "coaching_points": ["Vor den Mitspieler passen, damit er direkt spielen kann", "Sich schnell anbieten und in Bewegung bleiben", "Den Körper schon vor dem Ball richtig stellen", "Nach dem Pass sofort weiter, damit das Tempo hoch bleibt"],
 "materials": ["6 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Kombinieren mit Direktpässen. Der Ball läuft mit einem Kontakt über die Seite von einem Ende zum anderen.",
 "board": {"lines": LINES, "goals": [], "cones": KEGEL, "players": sp(), "balls": [B("b1", 50.6, 53.1)] + ERSATZ,
  "steps": [
   S("In die Mitte dribbeln", "Spieler sechs dribbelt mit dem Ball zwischen den Hütchen hindurch in die Mitte.",
     dr("n6", "b1", [50, 34.5])),
   S("Steil und zurück", "Spieler sechs passt nach oben zu Spieler zehn. Der spielt direkt zurück, vor Spieler sechs in den Lauf, und startet sofort nach rechts.",
     ps("b1", [50.6, 5.6]), mv("n6", [52, 33], delay=0.4), ps("b1", [52.6, 33.6], after=True), mv("n10", [62.5, 17], after=True)),
   S("Nach außen und zurück", "Spieler sechs spielt direkt nach außen zu Spieler zehn, und der legt mit einem Kontakt zurück. Dann läuft Spieler zehn außen an der Seite nach unten.",
     ps("b1", [63.1, 17.6]), ps("b1", [52.6, 33.6], after=True), mv("n10", [65, 29], after=True), mv("n10", [63.5, 41], after=True)),
   S("In die Tiefe, dann nach unten", "Spieler sechs spielt in die Tiefe, und Spieler zehn passt direkt nach unten zu Spieler elf. Die Passfolge ist geschafft. Spieler sechs geht nach oben, Spieler zehn stellt sich unten an, und Spieler elf startet die nächste Runde über links.",
     ps("b1", [64.1, 41.6]), ps("b1", [60.6, 53.6], after=True), mv("n6", [50, 6], after=True), mv("n10", [50, 52.5], after=True))],
  "dims": dims(33.3, 66.7, 5, 55, "9 m", "14 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor den Mitspieler passen.", "In den Lauf passen",
    "Der Pass geht nicht in die Füße, sondern ein Stück vor den Mitspieler, dorthin, wo er hinläuft. So kann er den Ball mit einem Kontakt weiterspielen. Auch das Tempo des Passes muss passen.",
    sp(n10=(44.6, 9.5), n6=(50.2, 26.6)), [B("b1", 50.8, 27.2)] + ERSATZ,
    [S("Pass in den Lauf", "Spieler zehn läuft schräg nach links. Spieler sechs spielt nicht in seine Füße, sondern vor ihn in den Lauf.",
       mv("n10", [38.5, 20]), ps("b1", [39.1, 20.6], delay=0.3)),
     S("Direkt weiter", "Spieler sechs läuft weiter nach vorn. Spieler zehn spielt den Ball mit einem Kontakt zurück, genau in seinen Lauf.",
       mv("n6", [50, 20]), ps("b1", [50.6, 20.6], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Richtungswechsel nach dem Pass in die Mitte.", "Aufdrehen und wenden",
    "Jetzt kommt der Ball von oben zurück, und der Spieler in der Mitte dreht auf und spielt nach unten. Vorher schaut er über die Schulter. Er nimmt den Ball offen an und spielt mit dem Spieler unten weiter, bis der Ball oben ankommt.",
    sp(), [B("b1", 50.6, 53.1)] + ERSATZ,
    [S("Dribbeln und steil", "Spieler sechs dribbelt in die Mitte und passt nach oben zu Spieler zehn. Spieler elf kommt unten ins Feld.",
       dr("n6", "b1", [50, 34.5]), ps("b1", [50.6, 5.6], after=True), mv("n11", [53, 50], delay=0.5)),
     S("Schulterblick und aufdrehen", "Spieler sechs schaut über die Schulter zu Spieler elf. Spieler zehn spielt direkt zurück, Spieler sechs dreht auf und passt nach unten zu Spieler elf.",
       bl("n6", [54, 51]), ps("b1", [50.6, 35.1], after=True), ps("b1", [53.6, 50.6], after=True)),
     S("Zurück und in den Lauf", "Spieler elf legt direkt zurück und läuft außen nach oben. Spieler sechs spielt ihm den Ball in den Lauf.",
       ps("b1", [50.6, 35.1]), mv("n11", [65, 37], after=True), mv("n11", [65, 19], after=True), ps("b1", [65.6, 19.6], after=True)),
     S("Nach oben", "Spieler elf passt direkt nach oben zu Spieler zehn. Die Passfolge ist geschafft, und die Spieler wechseln die Stationen.",
       ps("b1", [50.6, 5.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
