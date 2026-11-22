import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P4 (U12-U14, Woche 18 Phase 6): Defensive Recovery Runs. 20 x 25 Yards, um 90 Grad gedreht (Minitore oben, im Original
# rechts mit Öffnung nach links): Feld x 22.5-77.5, y 8-52 (23 x 18 m). Puppe als Stange links oben, Trainer links daneben
# (im Original oben rechts). Blau/Pink -> Neon: Passgeber 3, Verteidiger 5, 4, 6, 2 (Nummern wie im Video). Der zweite Trainer
# unten links (zweiter Schuss) ist hier Neon sieben, weil es nur einen Trainer gibt. Wartende oben außerhalb des Feldes
# (3D-Abstand). Der Kopfball zum Trainer ist als Pass zurück dargestellt. Punkte pro Block gibt es im Original nicht
# (dort keine Wertung), hier ergänzt, damit die Runde ein Ergebnis hat.
# Sichtkegel: PDF Coaching-Punkt 1 "avoiding ball-watching after the first clearance" mit eingezeichnetem Kegel vom
# Verteidiger zum zweiten Schuss -> nach dem ersten Block schaut Neon fünf zum zweiten Minitor (Grundform und Steigerung).
# Fassungen: Coaching-Punkt 2 aus dem PDF (genau köpfen, auch Brust und Volley wie im Ton), Steigerung aus dem Ton
# ("sprint out to a cone before defending the next one"). Nicht gebaut: drittes Minitor, große Tore.
T = P("T", "c", 15, 17, "T")
POS = {"n5": (40, 11), "n4": (50, 4), "n6": (58.5, 4), "n2": (67, 4), "n3": (48.7, 46.3), "n7": (68.5, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 16.6, 20.6), B("s2", 13, 20.6)]
BAELLE = [B("b1", 15.6, 17.6), B("b3", 49.3, 46.9), B("b7", 69.1, 46.6)] + ERSATZ
LINES = [rect(22.5, 8, 55, 44)]
KEGEL = [C(32.2, 16.6, shape="stange"), C(40, 14.5), C(48.7, 49.8), C(68.5, 49.8)]
TORE = [{"x": 48.2, "y": 18.8, "side": "top"}, {"x": 69.1, "y": 18.8, "side": "top"}]

u = {"title": "Köpfen, sprinten, blocken", "code": "UE-185", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 6, "field_size": "23 x 18 m",
 "description": "Ein Verteidiger sprintet zu einer Puppe und köpft den Ball zurück zum Trainer. Dann läuft er um die Puppe und sprintet vor das erste Minitor, um einen Schuss zu blocken. Sofort geht es weiter zum zweiten Minitor und zum nächsten Block. So üben die Kinder schnelles Zurücklaufen, Köpfen und Blocken.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern. Oben zwei Minitore nebeneinander, links daneben eine Puppe oder Stange. Unten zwei Hütchen für die Passgeber, oben ein Hütchen als Start.",
  "Verteilen: Die Verteidiger warten oben am Start. Zwei Passgeber stehen unten mit Bällen, jeder vor einem Minitor. Der Trainer steht links neben der Puppe mit Bällen.",
  "Ablauf: Der Verteidiger sprintet zur Puppe und köpft den Ball zurück zum Trainer. Dann läuft er um die Puppe, blockt den Schuss aufs erste Minitor und sprintet weiter zum zweiten.",
  "Wertung und Wechsel: Jeder geblockte Ball gibt einen Punkt für den Verteidiger. Nach dem zweiten Block startet der Nächste. Wer zweimal dran war, tauscht mit einem Passgeber. Nach jeder Runde zwei Minuten Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Mit vollem Tempo zum Ball und vor das Minitor sprinten", "Genau zurück zum Trainer köpfen, auch im Laufen", "Nach dem ersten Block nicht dem Ball nachschauen, sofort zum zweiten Minitor", "Die Passgeber spielen erst, wenn der Verteidiger eine faire Chance hat"],
 "materials": ["2 Minitore", "1 Puppe oder Stange", "3 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Köpfen, sprinten, blocken. Ein Verteidiger köpft zurück, sprintet vor zwei Minitore und blockt beide Schüsse.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Sprint zur Puppe", "Neon fünf sprintet los zur Puppe. Der Trainer wirft ihm den Ball zu.",
     mv("n5", [29, 12]), ps("b1", [29.6, 12.6], delay=0.6)),
   S("Köpft zurück", "Neon fünf köpft den Ball genau zurück zum Trainer.",
     ps("b1", [15.6, 17.6])),
   S("Erster Block", "Neon fünf läuft um die Puppe herum und sprintet vor das erste Minitor. Neon drei spielt aufs Minitor, und Neon fünf blockt den Ball.",
     mv("n5", [27, 17]), mv("n5", [31, 22], after=True), mv("n5", [46.5, 23], after=True), ps("b3", [47.1, 23.6], delay=1.2)),
   S("Nicht nachschauen", "Neon fünf schaut nicht dem Ball nach. Er schaut sofort zum zweiten Minitor und sprintet hin.",
     bl("n5", [66, 26]), mv("n5", [67.5, 23], after=True)),
   S("Zweiter Block: Punkt", "Neon sieben spielt aufs zweite Minitor, und Neon fünf blockt auch diesen Ball. Jeder Block gibt einen Punkt für Neon fünf. Jetzt startet Neon vier, und Neon fünf stellt sich hinten an.",
     ps("b7", [68.1, 23.6]), mv("n4", [40, 11], delay=0.6))],
  "dims": dims(22.5, 77.5, 8, 52, "23 m", "18 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau zurückköpfen.", "Genau zurückköpfen",
    "Der Kopfball geht genau zum Trainer zurück, auch im vollen Lauf. Mit der Stirn köpfen und die Augen offen lassen. Der Trainer wechselt ab: mal hoch, mal flach, mal mit der Brust annehmen und volley zurückspielen.",
    sp(), BAELLE,
    [S("Hoch geworfen", "Neon fünf sprintet zur Puppe, und der Trainer wirft den Ball hoch.",
       mv("n5", [29, 12]), ps("b1", [29.6, 12.6], delay=0.6)),
     S("Mit der Stirn", "Neon fünf köpft mit der Stirn genau zurück zum Trainer. Die Augen bleiben offen.",
       ps("b1", [15.6, 17.6])),
     S("Brust und Volley", "Jetzt wirft der Trainer den Ball auf die Brust. Neon fünf nimmt ihn mit der Brust an und spielt ihn volley zurück. Dann geht es weiter zu den Minitoren.",
       ps("b1", [29.6, 12.6]), ps("b1", [15.6, 17.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Erst raus zum Hütchen.", "Raus zum Hütchen",
    "Zwischen den beiden Blocks liegt ein Hütchen weiter unten im Feld. Nach dem ersten Block sprintet der Verteidiger erst zum Hütchen und dann zurück vor das zweite Minitor. So muss er noch schneller wieder aufstehen und zurücklaufen.",
    sp(n5=(46.5, 23)), [B("b1", 15.6, 17.6), B("b3", 47.1, 23.6), B("b7", 69.1, 46.6)] + ERSATZ,
    [S("Zum Hütchen", "Neon fünf hat den ersten Ball geblockt. Er schaut sofort zum Hütchen und sprintet hin.",
       bl("n5", [57, 40]), mv("n5", [57, 37.5], after=True)),
     S("Zurück vors Minitor", "Am Hütchen dreht er und sprintet zurück vor das zweite Minitor.",
       mv("n5", [67.5, 23])),
     S("Zweiter Block: Punkt", "Neon sieben spielt aufs Minitor, und Neon fünf blockt den Ball. Das gibt einen Punkt für Neon fünf.",
       ps("b7", [68.1, 23.6]))],
    cones=[dict(c, id=f"k{i}") for i, c in enumerate(KEGEL + [C(57, 40)], 1)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
