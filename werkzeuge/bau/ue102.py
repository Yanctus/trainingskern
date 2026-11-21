import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 41-P5: 25 x 25 Yards, gedreht: Tor rechts. Feld x 24-76, y 4-56, Strafraum x 66.6-76, y 16.8-43.2, Mittellinie x 50.
# Neon greift an (Stürmer 9, Flügel 7 und 11), Rot spielt die Pässe und verteidigt (4 in der Mitte, 2 oben, 3 unten).
T = P("T", "c", 16, 4, "T")
goals = [{"x": 76, "y": 30, "side": "right"}]
lines = [rect(24, 4, 52, 52), rect(66.6, 16.8, 9.4, 26.4), line(50, 4, 50, 56)]
cones = ecken(24, 4, 52, 52) + [C(45, 24, "neon", shape="stange")]
def sp(**k):
    d = dict(n9=(41.5, 37), n7=(34, 14), n11=(33, 49), r4=(28.4, 32.5), r2=(57.2, 9), r3=(56, 50)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k1", "t", 73, 30, "TW"), T]
balls = [B("b1", 30, 33.1), B("b2", 58.8, 9.6), B("b3", 57.6, 50.6)]
u = {"title": "Überzahl vor dem Tor", "code": "UE-102", "kind": "Übungsform",
 "focuses": ["Torschuss", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 7, "players_max": 13, "field_size": "23 x 23 m",
 "description": "Drei Angriffe hintereinander, jedes Mal mit einem Spieler mehr. Zuerst bekommt der Stürmer einen Steilpass und schließt eins gegen eins ab. Dann spielt ein Verteidiger einen Flügelspieler an und läuft zurück zum Verteidigen, es steht zwei gegen eins. Zum Schluss dasselbe von der anderen Seite, jetzt drei gegen zwei.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern mit Tor, Torwart und Strafraum. In der Mitte ein Dummy.",
  "Verteilen: Zwei Mannschaften mit je drei Spielern an sechs Stationen: Angreifer in der Mitte und auf beiden Flügeln, Passgeber und Verteidiger gegenüber.",
  "Ablauf: Erster Angriff: Steilpass auf den Stürmer, eins gegen eins gegen den Torwart. Zweiter Angriff: Ein Verteidiger spielt einen Flügelspieler an und läuft zurück, zwei gegen eins. Dritter Angriff: dasselbe von der anderen Seite, drei gegen zwei. Jedes Tor gibt einen Punkt.",
  "Wechsel: Nach jeder Runde tauschen die Mannschaften die Stationen."],
 "organisation_show": ORG,
 "coaching_points": ["In der Überzahl entschlossen und schnell angreifen", "Vor dem Tor ruhig bleiben und genau abschließen", "Als Verteidiger gut stehen und miteinander sprechen", "Sich ohne Ball frei laufen und genau passen"],
 "materials": ["1 Tor", "1 Dummy", "Hütchen für Feld und Stationen", "Bälle an den Stationen"],
 "access": "frei", "hidden": True,
 "say_intro": "Überzahl vor dem Tor. Erst eins gegen eins, dann zwei gegen eins, dann drei gegen zwei.",
 "board": {"lines": lines, "cones": cones, "goals": goals, "players": sp(), "balls": balls,
  "steps": [
   S("Steilpass auf den Stürmer", "Rot vier spielt den Ball steil in den Lauf von Neon neun.", mv("n9", [54, 31]), ps("b1", [55.6, 31.6], delay=0.3)),
   S("Eins gegen eins: Punkt", "Neon neun nimmt den Ball mit und schießt am Torwart vorbei, und das gibt einen Punkt für Neon.", ps("b1", [76, 26])),
   S("Flügel angespielt", "Jetzt spielt Rot zwei schräg zu Neon sieben und läuft sofort zurück, um zu verteidigen.",
     ps("b2", [41.6, 16.6]), mv("r2", [60, 22], delay=0.3)),
   S("Zwei gegen eins: Punkt", "Neon sieben dribbelt an und legt quer zu Neon neun, der frei ist. Neon neun schießt, und das gibt einen Punkt für Neon.",
     dr("n7", "b2", [52, 18]), ps("b2", [55.6, 31.6], after=True), ps("b2", [76, 35], after=True))],
  "dims": [{"x1": 24, "y1": 58.6, "x2": 76, "y2": 58.6, "text": "23 m"}, {"x1": 84, "y1": 4, "x2": 84, "y2": 56, "text": "23 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der dritte Angriff kommt von der anderen Seite, drei gegen zwei.", "Drei gegen zwei",
    "Nach dem zweiten Angriff spielt Rot drei von der anderen Seite Neon elf an und läuft ebenfalls zurück. Jetzt greifen drei Angreifer gegen zwei Verteidiger an. Schnell spielen und den freien Mann finden, bevor sich die Abwehr sortiert.",
    sp(n9=(55, 34), n7=(50, 14), r2=(64, 21)), [B("b3", 57.6, 50.6)],
    [S("Anspiel auf den anderen Flügel", "Rot drei spielt Neon elf an und läuft gleich zurück zum Verteidigen.", ps("b3", [34.6, 49.6]), mv("r3", [62, 40], delay=0.3)),
     S("Drei gegen zwei", "Neon elf dribbelt an, die beiden Roten gehen auf Neon neun und Neon elf. Neon sieben ist frei.",
       dr("n11", "b3", [50, 44]), mv("r3", [58, 40]), mv("r2", [60, 28])),
     S("Freier Mann: Punkt", "Neon elf spielt schräg zu Neon sieben, und der schießt ins Tor. Das gibt einen Punkt für Neon.",
       ps("b3", [51.6, 14.6]), ps("b3", [76, 26], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Erobern die Verteidiger den Ball, schießen sie auf zwei Minitore.", "Minitore für Verteidiger",
    "An beiden Seiten stehen Minitore für die Verteidiger. Erobern sie den Ball, dürfen sie sofort darauf schießen. Das belohnt gutes Verteidigen und verlangt, dass sie nach dem Ballgewinn ruhig bleiben.",
    sp(n9=(55, 34), n7=(46, 16), r2=(56, 16)), [B("b2", 47.6, 16.6)],
    [S("Ball erobert", "Neon sieben dribbelt auf Rot zwei zu, und Rot zwei spitzelt ihm den Ball weg.", dr("n7", "b2", [51, 17]), mv("r2", [53, 17.5], delay=0.2), ps("b2", [57, 13], after=True)),
     S("Aufs Minitor: Punkt", "Rot zwei schießt sofort aufs Minitor oben, und das gibt einen Punkt für Rot.", mv("r2", [57, 12]), ps("b2", [70, 3.5], after=True))],
    goals=goals + [{"x": 70, "y": 4, "side": "top"}, {"x": 70, "y": 56, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
