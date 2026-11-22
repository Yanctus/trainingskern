import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-118 (U12-U14, Woche 4 Pre-Season): 1 v 1 Dribble and Finish Battle. 10 x 15 Yards hochkant = Feld x 33.3-66.7, y 5-55 (9 x 14 m).
# Minitor oben in der Mitte im Feld, zwei Minitore unten. Je Seite vier Stangen (Slalom), rotes Hütchen in der Mitte unten.
# Blau -> Neon (2, 6, 7), Pink -> Rot (7 -> 8, 3, 9). Stangen etwas weiter auseinander (Slalom-Wege mit Abstand). Ein Trainer.
# Sichtkegel wie im Video: Schulterblick zum Gegner vor dem zweiten Ball ("Get body across"), Blickfinte zum linken Tor in der
# Steigerung ("Use deception to evade the defender").
T = P("T", "c", 50, 58, "T")
POS = {"n2": (39, 7), "n6": (30, 2), "n7": (21, 2), "r8": (61, 7), "r3": (70, 2), "r9": (79, 2)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 52.6, 58.6), B("s2", 47.4, 58.8)]
BAELLE = [B("b2", 39.6, 7.6), B("b8", 61.6, 7.6)] + ERSATZ
LINES = [rect(33.3, 5, 33.4, 50)]
KEGEL = [C(x, y, "neon", shape="stange") for x, y in ((38.5, 15), (44.5, 21.5), (38.5, 28), (44.5, 34.5))] \
      + [C(x, y, shape="stange") for x, y in ((61.5, 15), (55.5, 21.5), (61.5, 28), (55.5, 34.5))] + [C(50, 45)]
TORE = [{"x": 50, "y": 11, "side": "top"}, {"x": 39.5, "y": 55, "side": "bottom"}, {"x": 60.4, "y": 55, "side": "bottom"}]
OBEN, LINKS, RECHTS = [50, 10.7], [39.5, 55.3], [60.4, 55.3]
N_SLA = [[35, 13], [35, 17], [48, 19.5], [48, 23.5], [35, 26], [35, 30], [48, 32.5], [48, 36.5]]
R_SLA = [[100 - x, y] for x, y in N_SLA]
def kette(who, ball, pkt, **k): return [dr(who, ball, pkt[0], **k)] + [dr(who, ball, p, after=True) for p in pkt[1:]]

u = {"title": "Slalom, Abschluss, Zweikampf", "code": "UE-136", "kind": "Übungsform",
 "focuses": ["Dribbling", "Torschuss", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "9 x 14 m",
 "description": "Zwei Spieler starten gleichzeitig mit Ball und dribbeln im Slalom durch ihre Stangen, dann um das Hütchen unten herum und schießen ins Minitor oben in der Mitte. Sofort danach spielt der Trainer einen zweiten Ball ins Feld. Jetzt kämpfen beide darum, sich vor den Gegner zu schieben, den Ball anzunehmen und in eines der beiden Minitore unten zu treffen. Dann holen sich beide einen neuen Ball, und das nächste Paar ist dran.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern. Oben in der Mitte steht ein Minitor im Feld, unten zwei Minitore. Auf jeder Seite stehen vier Stangen für den Slalom, unten in der Mitte ein Hütchen.",
  "Verteilen: Zwei Teams, Team Neon links oben, Team Rot rechts oben, jeder mit einem Ball. Der Trainer steht unten zwischen den Minitoren mit vielen Bällen.",
  "Ablauf: Auf Pfiff dribbeln die Ersten gleichzeitig durch ihre Stangen, um das Hütchen und schießen ins Tor oben. Sofort spielt der Trainer einen zweiten Ball, und beide kämpfen darum. Wer ihn bekommt, schließt in eines der Tore unten ab.",
  "Wertung: Jedes Tor ist ein Punkt für das Team. Danach holen beide einen neuen Ball beim Trainer oder aus dem Tor und stellen sich oben wieder an."],
 "organisation_show": ORG,
 "coaching_points": ["Im Slalom mit dem Fuß führen, der näher an der Stange ist", "Den Körper zwischen Gegner und Ball schieben und abschirmen", "Auch unter Druck genau abschließen", "Die Mitspieler am Rand feuern laut an"],
 "materials": ["8 Stangen", "1 Hütchen", "3 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Slalom, Abschluss, Zweikampf. Erst ein Wettrennen im Slalom mit Abschluss, dann sofort der Kampf um den zweiten Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Slalom durch die Stangen", "Auf Pfiff dribbeln Neon zwei und Rot acht gleichzeitig im Slalom durch ihre Stangen nach unten.",
     *kette("n2", "b2", N_SLA), *kette("r8", "b8", R_SLA, delay=0.2)),
   S("Um das Hütchen, Abschluss: Punkt", "Neon zwei ist zuerst um das Hütchen und schießt ins Tor oben, und das gibt einen Punkt für Team Neon. Gleich danach schießt auch Rot acht.",
     *kette("n2", "b2", [[47, 44.5], [50, 48.4], [53, 44.5]]), ps("b2", OBEN, after=True),
     *kette("r8", "b8", [[53, 41], [56, 44.5], [54.5, 49.5], [47, 46.5]], delay=0.8), ps("b8", OBEN, after=True)),
   S("Zweiter Ball: Punkt", "Sofort spielt der Trainer einen zweiten Ball. Neon zwei schiebt sich vor Rot acht, schirmt den Ball ab und trifft ins rechte Minitor unten, und das gibt noch einen Punkt für Team Neon. Dann sind Neon sechs und Rot drei dran.",
     ps("s1", [50.6, 50.6]), mv("n2", [50, 49.5], delay=0.1), mv("r8", [47.5, 48], delay=0.3), ps("s1", RECHTS, after=True))],
  "dims": [{"x1": 86, "y1": 5, "x2": 86, "y2": 55, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Körper dazwischen schieben.", "Abschirmen",
    "Beim zweiten Ball gewinnt, wer zuerst den Körper zwischen Gegner und Ball bringt. Vorher kurz über die Schulter schauen, wo der Gegner ist, dann den Körper quer stellen, den Ball abschirmen und erst dann abschließen.",
    sp(n2=(54, 42), r8=(45.5, 42)), [B("b2", 50, 10.7), B("b8", 50.3, 10.7)] + ERSATZ,
    [S("Über die Schulter schauen", "Der Trainer spielt den zweiten Ball. Neon zwei schaut kurz über die Schulter, wo Rot acht ist, und schiebt sich vor ihn.",
       ps("s1", [50.6, 50.6]), bl("n2", [45.5, 42]), mv("n2", [52.8, 48.6], after=True), mv("r8", [47.5, 46.5], delay=0.4)),
     S("Abschirmen und abschließen: Punkt", "Mit dem Körper zwischen Gegner und Ball nimmt er an, dreht sich weg und trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann holen beide einen neuen Ball.",
       mv("n2", [51, 50]), ps("s1", RECHTS, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein dritter Ball für ein eins gegen eins.", "Dritter Ball, eins gegen eins",
    "Jetzt spielt der Trainer noch einen dritten Ball, und es gibt ein eins gegen eins auf die beiden Tore unten. Der Verteidiger presst, wenn der Angreifer mit dem Rücken zum Tor steht. Der Angreifer täuscht mit dem Blick eine Seite an und geht dann auf die andere.",
    sp(n2=(40, 38), r8=(50, 36)), [B("b2", 50, 10.7), B("b8", 50.3, 10.7)] + ERSATZ,
    [S("Ball kommt, Verteidiger presst", "Der Trainer spielt Neon zwei den dritten Ball, Rot acht läuft sofort auf ihn zu.",
       ps("s1", [40.6, 41.1]), mv("n2", [40, 40.5]), mv("r8", [46, 42], delay=0.3)),
     S("Blick links, Weg rechts", "Neon zwei schaut zum linken Tor, als wolle er dorthin. Rot acht schiebt nach links, und Neon zwei zieht nach rechts weg.",
       bl("n2", LINKS), mv("r8", [44, 46], after=True), dr("n2", "s1", [49, 44], after=True), dr("n2", "s1", [54, 48], after=True)),
     S("Abschluss rechts: Punkt", "Jetzt ist das rechte Tor frei, und Neon zwei trifft, und das gibt einen Punkt für Team Neon. Dann sind Neon sechs und Rot drei dran.",
       ps("s1", RECHTS))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
