import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 46-P2: 45 x 35 Yards, gespiegelt (Angriff nach rechts): Feld x 10-90, y 7-53. Zone eins links (x 10-50), Zone zwei rechts (x 50-90).
# Linie x 23: Abseitszone für den Konter. Neutrale Torhüter TW. Neon greift an (8, 9, 10, Wartende 7, 11), Rot verteidigt (4 in Zone eins, 5+6 in Zone zwei, 3 an der Seite).
T = P("T", "c", 20, 2.5, "T")
TW = [P("k1", "t", 13, 30, "TW"), P("k2", "t", 87, 30, "TW")]
def sp(**k):
    d = dict(n8=(29.5, 20), n9=(38, 33), n10=(29.5, 46), n7=(4, 40), n11=(4, 18), r3=(69.4, 3), r4=(47, 30), r5=(70, 20.8), r6=(72.2, 40.7)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + TW + [T]
lines = [rect(10, 7, 80, 46), line(50, 7, 50, 53), line(23, 7, 23, 53)]
goals = [{"x": 10, "y": 30, "side": "left"}, {"x": 90, "y": 30, "side": "right"}]
cb = [B("c1", 22.6, 3.1)]
u = {"title": "Überzahl im letzten Drittel", "code": "UE-089", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Torschuss", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 14, "field_size": "41 x 32 m",
 "description": "Drei Angreifer starten beim eigenen Torwart und spielen in der ersten Zone drei gegen einen. Sobald sie in die zweite Zone kommen, spielen sie drei gegen zwei und haben nur wenige Sekunden zum Abschluss. Erobern die Verteidiger den Ball, kommt ein vierter Verteidiger von der Seite dazu, und es gibt einen Konter vier gegen drei aufs andere Tor.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 32 Metern mit einem Tor und Torwart an jedem Ende. In der Mitte geteilt in zwei Zonen.",
  "Verteilen: Drei Angreifer starten beim Torwart. In der ersten Zone ein Verteidiger, in der zweiten Zone zwei Verteidiger. Ein vierter Verteidiger wartet an der Seitenlinie.",
  "Ablauf: Drei gegen eins in der ersten Zone, dann drei gegen zwei in der zweiten Zone. Ab dem Eintritt in die zweite Zone haben die Angreifer etwa fünf Sekunden für den Abschluss. Jedes Tor gibt einen Punkt.",
  "Konter und Wechsel: Gewinnen die Verteidiger den Ball, kommt der vierte Verteidiger dazu, und sie kontern vier gegen drei, jetzt mit Abseits. Nach jedem Angriff wechselt ein Verteidiger, die drei Angreifer nach zwei oder drei Angriffen."],
 "organisation_show": ORG,
 "coaching_points": ["Schauen, wo die Verteidiger stehen, und den Raum nutzen, den sie nicht abdecken", "Steilpässe mit gutem Tempo und im richtigen Moment spielen", "Das Tempo des Angriffs an die Abwehr anpassen und mit Positionswechseln Unruhe stiften", "Nach Ballgewinn sofort und schnell kontern"],
 "materials": ["2 Tore", "6 Hütchen", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Überzahl im letzten Drittel. Erst drei gegen eins, dann drei gegen zwei, und bei Ballverlust kommt der Konter.",
 "board": {"lines": lines, "cones": ecken(10, 7, 80, 46), "goals": goals, "players": sp(), "balls": [B("b1", 14.6, 30.6)] + cb,
  "steps": [
   S("Start beim Torwart", "Der Torwart spielt Spieler zehn an. Spieler vier kommt sofort heraus.", ps("b1", [31.1, 46.6]), mv("r4", [42, 36], delay=0.3)),
   S("Drei gegen eins", "Spieler zehn spielt zu Spieler neun. Gleichzeitig startet Spieler acht in die zweite Zone, und Spieler neun spielt ihn steil an.",
     ps("b1", [39.6, 33.6]), mv("n8", [56, 22], delay=0.3), ps("b1", [57.6, 22.6], after=True)),
   S("Drei gegen zwei", "In der zweiten Zone kommt Spieler fünf auf Spieler acht zu. Spieler neun läuft mit und bekommt den Querpass.",
     mv("r5", [64, 22]), mv("n9", [60, 34]), ps("b1", [61.6, 34.6], delay=0.4)),
   S("Abschluss: Punkt", "Spieler neun schießt schnell, bevor Spieler sechs herankommt, und das gibt einen Punkt für Neon.", ps("b1", [90, 35]), mv("r6", [68, 37]))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "41 m"}, {"x1": 96, "y1": 7, "x2": 96, "y2": 53, "text": "32 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Überzahl lässt viel Platz, den schnell nutzen.", "Den freien Raum nutzen",
    "Ein einzelner Verteidiger kann nicht alle drei Angreifer decken. Irgendwo ist immer viel Platz. Wer das früh erkennt, dribbelt schnell hinein in die zweite Zone, bevor der Verteidiger reagieren kann.",
    sp(n8=(36, 30), n9=(38, 14), n10=(34, 46), r4=(47, 25)), [B("b1", 35.6, 46.6)] + cb,
    [S("Lücke erkennen", "Spieler vier steht zwischen Spieler acht und Spieler neun. Unten ist viel Platz, und Spieler zehn dribbelt sofort los.", dr("n10", "b1", [52, 46])),
     S("Schnell hinein", "Spieler zehn dribbelt in die zweite Zone, und Spieler acht läuft mit. Spieler zehn passt zu ihm.",
       dr("n10", "b1", [64, 45]), mv("n8", [58, 28], delay=0.2), ps("b1", [59.6, 28.6], after=True)),
     S("Abschluss: Punkt", "Spieler acht schießt sofort, und das gibt einen Punkt für Neon.", ps("b1", [90, 24]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Erobern die Verteidiger den Ball, kommt der vierte dazu, und es geht vier gegen drei.", "Konter vier gegen drei",
    "Gewinnen die Verteidiger den Ball, schalten sie sofort um. Der vierte Verteidiger kommt von der Seitenlinie dazu, und sie kontern zu viert gegen drei aufs andere Tor. Jetzt gilt Abseits. Schnell spielen, bevor die Angreifer zurück sind.",
    sp(n8=(66, 26), n9=(57, 42), n10=(50, 9), r4=(45, 32), r5=(75, 22), r6=(72, 44)), [B("b1", 67.6, 26.6)] + cb,
    [S("Ball erobert", "Spieler fünf geht dazwischen und erobert den Ball von Spieler acht.", mv("r5", [71, 29]), ps("b1", [72.6, 29.6], delay=0.2)),
     S("Der Vierte kommt dazu", "Gleichzeitig spielt Spieler fünf sofort zu Spieler vier, und Spieler drei startet von der Seitenlinie in den Konter.",
       ps("b1", [46.6, 32.6]), mv("r3", [56, 14]), mv("r3", [36, 18], after=True)),
     S("Konter: Punkt", "Spieler vier spielt in den Lauf von Spieler drei, und der schießt ins Tor. Das gibt einen Punkt für Rot.",
       ps("b1", [37.6, 18.6]), ps("b1", [10, 26], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
