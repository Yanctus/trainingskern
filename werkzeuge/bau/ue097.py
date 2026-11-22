import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 37-P1: 20 x 25 Yards, gedreht: Feld x 14-86, y 6-54, Tore links (Neon verteidigt) und rechts (Rot verteidigt), neutrale Torhüter.
# Jede Mannschaft hat einen Helfer (Neon 2, Rot 11), der nur im Feld ist, wenn seine Mannschaft zuletzt getroffen hat.
T = P("T", "c", 32, 2.5, "T")
goals = [{"x": 14, "y": 30, "side": "left"}, {"x": 86, "y": 30, "side": "right"}]
def sp(**k):
    d = dict(n5=(12, 14), n7=(12, 46), n6=(3, 54), n8=(3, 6), n2=(45, 30), r3=(88, 14), r4=(88, 46), r9=(97, 6), r10=(97, 54), r11=(22, 2.5)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k1", "t", 17, 30, "TW"), P("k2", "t", 83, 30, "TW"), T]
cb = [B("c1", 34.6, 3.1), B("c2", 37, 4)]
u = {"title": "Zu zweit gegen die Überzahl", "code": "UE-097", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 14, "field_size": "23 x 18 m",
 "description": "Zwei gegen zwei plus Helfer auf zwei Tore mit Torwart. Der Trainer ruft und spielt einen Ball ins Feld, je zwei Spieler beider Mannschaften rennen los. Wer den Ball erobert, greift mit seinem Helfer drei gegen zwei an. Die zwei Verteidiger stehen kompakt, lenken das Spiel nach außen und kontern sofort, wenn sie den Ball gewinnen. Der Helfer gehört immer zur Mannschaft, die zuletzt getroffen hat.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern mit einem Tor und Torwart an jedem Ende.",
  "Verteilen: Zwei Mannschaften warten neben dem eigenen Tor. Jede Mannschaft hat einen Helfer. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Der Trainer ruft und spielt einen Ball ins Feld. Je zwei Spieler jeder Mannschaft rennen los. Wer den Ball hat, greift mit dem Helfer drei gegen zwei an. Erobern die Verteidiger den Ball, kontern sie auf das andere Tor. Jedes Tor gibt einen Punkt.",
  "Wechsel: Nach jedem Angriff kommen neue Paare. Der Helfer der Mannschaft, die getroffen hat, ist im nächsten Durchgang im Feld."],
 "organisation_show": ORG,
 "coaching_points": ["Das Spiel vom Tor weg nach außen lenken", "Nach Ballgewinn kompakt bleiben und schnell kontern", "Beim Verteidigen viel miteinander sprechen und sich absprechen", "Die Gefahr erkennen und immer zuerst das Tor schützen"],
 "materials": ["2 Tore", "4 Hütchen", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Zu zweit gegen die Überzahl. Zwei Verteidiger gegen drei Angreifer, und nach Ballgewinn geht es sofort in den Konter.",
 "board": {"lines": [rect(14, 6, 72, 48)], "cones": ecken(14, 6, 72, 48), "goals": goals, "players": sp(), "balls": cb,
  "steps": [
   S("Wettlauf zum Ball", "Der Trainer spielt einen Ball ins Feld. Gleichzeitig rennen je zwei Spieler beider Mannschaften los.",
     ps("c1", [45.6, 46.6]), mv("n5", [34, 22]), mv("n7", [44, 46]), mv("r3", [62, 22]), mv("r4", [58, 42])),
   S("Drei gegen zwei", "Spieler sieben ist zuerst am Ball und spielt zum Helfer Spieler zwei. Gleichzeitig startet Spieler fünf in den freien Raum.",
     ps("c1", [46.6, 30.6]), mv("n5", [60, 16], delay=0.2), mv("r3", [60, 28], delay=0.3), mv("r4", [54, 40], delay=0.3)),
   S("Freier Spieler: Punkt", "Spieler zwei spielt zum freien Spieler fünf, und der schießt ins Tor. Das gibt einen Punkt für Neon.",
     ps("c1", [61.6, 16.6]), ps("c1", [86, 26], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die zwei Verteidiger lenken den Ballführenden nach außen.", "Nach außen lenken",
    "Die beiden Verteidiger stellen sich so hin, dass der Weg durch die Mitte zu ist. Der Ballführende muss nach außen ausweichen. Dort ist es eng, und der zweite Verteidiger kann den nächsten Pass abfangen. Nach dem Ballgewinn geht es sofort in den Konter.",
    sp(n2=(48, 32), n5=(52, 14), n7=(52, 48), r3=(64, 24), r4=(66, 40)), [B("b1", 49.6, 32.6)] + cb,
    [S("Mitte zu", "Spieler drei schiebt in die Mitte und stellt den Weg zum Tor zu. Spieler zwei muss nach außen dribbeln.",
       mv("r3", [58, 30]), dr("n2", "b1", [55, 40], delay=0.2)),
     S("Pass abgefangen", "Spieler zwei will zu Spieler sieben passen, doch Spieler vier hat darauf gewartet und fängt den Ball ab.",
       ps("b1", [58.6, 44.6]), mv("r4", [58, 44])),
     S("Konter: Punkt", "Spieler vier kontert sofort auf das andere Tor und schießt. Das gibt einen Punkt für Rot.",
       dr("r4", "b1", [32, 40]), ps("b1", [14, 33], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: In der Überzahl den freien Spieler finden.", "Den Freien finden",
    "Drei Angreifer gegen zwei Verteidiger heißt: Einer ist immer frei. Wer am Ball ist, lockt die Verteidiger an, hebt den Kopf und spielt im richtigen Moment zum freien Mitspieler. Der schließt ruhig und genau ab.",
    sp(n2=(3, 30), n5=(38, 22), n7=(38, 38), r11=(58, 30), r3=(60, 12), r4=(62, 46)), [B("b1", 56.4, 30.6)] + cb,
    [S("Verteidiger anlocken", "Spieler elf dribbelt auf die beiden Verteidiger zu, und beide kommen auf ihn zu.",
       dr("r11", "b1", [48, 30]), mv("n5", [40, 28]), mv("n7", [42, 36])),
     S("Pass zum Freien", "Gleichzeitig startet Spieler drei in den freien Raum, und Spieler elf spielt ihn an.",
       mv("r3", [36, 12]), ps("b1", [37.6, 12.6], delay=0.3)),
     S("Abschluss: Punkt", "Spieler drei schießt ruhig ins Tor, und das gibt einen Punkt für Rot.", ps("b1", [14, 27]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
