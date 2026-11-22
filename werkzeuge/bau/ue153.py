import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-43 (U12-U14, Woche 9 Phase 2): Activation Passing Combinations. 20 x 25 Yards = Feld x 30-70, y 5-55 (18 x 23 m),
# zwei Minitore rechts, zwei Dummys in der Mitte, Hütchentor links. Alle Pink -> Neon (Rollen wechseln): Passgeber 2, 3, 4
# rechts außen in einer Reihe, Läufer 7, 8, 9 unten links in einer Reihe (3D-Abstand). Start-Hütchen des Passgebers etwas
# nach oben gesetzt, damit sein Laufweg frei ist; Läufer läuft außen um die Dummys. Ein Trainer.
# Sichtkegel nur in der Steigerung (Ton: "more observant", "increased awareness"): Läufer schaut vor dem Diagonalschuss zum Tor.
T = P("T", "c", 22, 10, "T")
POS = {"n2": (74, 33.5), "n3": (83, 33.5), "n4": (92, 33.5), "n7": (37, 52.5), "n8": (28, 52.5), "n9": (19, 52.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 38), B("s2", 92.6, 38)]
LINES = [rect(30, 5, 40, 50)]
KEGEL = [C(70.4, 29), C(36.4, 45.7), C(36.4, 14.9), C(30.2, 25.1), C(30.2, 35),
         C(47.1, 22.4, shape="stange"), C(47.1, 38.7, shape="stange")]
TORE = [{"x": 70, "y": 15.2, "side": "right"}, {"x": 70, "y": 44.7, "side": "right"}]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Doppelpass um die Dummys", "code": "UE-153", "kind": "Übungsform",
 "focuses": ["Passspiel", "Torschuss", "Erwärmung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "18 x 23 m",
 "description": "Ein schnelles Aufwärmen mit Pässen und Abschluss. Der Passgeber spielt den Läufer an, der sich vom Hütchen löst, und bekommt den Ball zurück. Dann folgen zwei Doppelpässe um die beiden Dummys, und der Läufer schießt direkt ins Minitor. Der Passgeber sprintet danach durch das Hütchentor und stellt sich wieder an.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern. Rechts zwei Minitore, in der Mitte zwei Dummys übereinander, links ein Tor aus zwei Hütchen. Unten links ein Start-Hütchen für die Läufer, rechts eines für die Passgeber.",
  "Verteilen: Die Passgeber stehen rechts mit Bällen in einer Reihe, die Läufer unten links. Der Trainer steht oben am Rand.",
  "Ablauf: Pass auf den Läufer, der sich vom Hütchen löst. Zurück zum Passgeber, dann ein Doppelpass am unteren und einer am oberen Dummy. Der Läufer schießt direkt ins obere Minitor.",
  "Wechsel: Der Passgeber sprintet durch das Hütchentor links und stellt sich wieder an. Der Abschluss startet die nächsten beiden. Nach fünf Minuten die Seite wechseln."],
 "organisation_show": ORG,
 "coaching_points": ["Pässe mit dem richtigen Tempo und genau in den Fuß", "Scharf vom Hütchen lösen, um den ersten Pass zu bekommen", "Direkt und genau abschließen, auch mit Tempo", "Nach dem letzten Pass sofort losspurten, mit beiden Füßen passen"],
 "materials": ["5 Hütchen", "2 Dummys", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Doppelpass um die Dummys. Zwei Spieler kombinieren schnell um zwei Dummys herum, und am Ende wird direkt abgeschlossen.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b2", 74.6, 34.1)] + ERSATZ,
  "steps": [
   S("Vom Hütchen lösen", "Spieler sieben löst sich scharf vom Hütchen, und Spieler zwei spielt ihn an.",
     mv("n7", [46.5, 44.5]), ps("b2", [47.1, 45.1], delay=0.3)),
   S("Zurück, dann herum", "Spieler zwei kommt ins Feld, und Spieler sieben legt den Ball zurück. Dann läuft Spieler sieben außen um den unteren Dummy.",
     mv("n2", [60.2, 34.8]), ps("b2", [60.8, 35.4], delay=0.3), *weg("n7", [[40.5, 39], [45.5, 31]], after=True)),
   S("Doppelpass unten", "Spieler zwei spielt ihm den Ball hinter dem Dummy in den Lauf und läuft selbst weiter nach oben.",
     ps("b2", [46.1, 31.6]), mv("n2", [55, 19], delay=0.3)),
   S("Doppelpass oben", "Spieler sieben spielt zu Spieler zwei, läuft um den oberen Dummy und bekommt den Ball wieder in den Lauf.",
     ps("b2", [55.6, 19.6]), *weg("n7", [[40, 24], [41.5, 13.5]], after=True), ps("b2", [42.1, 14.1], after=True)),
   S("Abschluss: Punkt", "Spieler sieben schießt direkt ins obere Minitor, und das gibt einen Punkt. Spieler zwei sprintet durch das Hütchentor links und stellt sich wieder an. Der Abschluss startet die nächsten beiden: Spieler drei und Spieler acht.",
     ps("b2", [69.7, 15.2]), *weg("n2", [[53, 30], [24, 30]], delay=0.2))],
  "dims": dims(30, 70, 5, 55, "18 m", "23 m", rx=99)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Scharf vom Hütchen lösen.", "Scharf lösen",
    "Der Läufer wartet nicht am Hütchen auf den Ball. Er macht erst einen kurzen Schritt weg und startet dann scharf in den freien Raum. Der Passgeber spielt genau in diesen Lauf.",
    sp(), [B("b2", 74.6, 34.1)] + ERSATZ,
    [S("Erst weg", "Spieler sieben macht zuerst einen kurzen Schritt weg vom Ball.",
       mv("n7", [40.5, 53])),
     S("Dann scharf rein", "Dann startet er scharf in den freien Raum, und Spieler zwei spielt ihm den Ball genau in den Lauf. Jetzt kann der Doppelpass beginnen.",
       mv("n7", [46.5, 44.5]), ps("b2", [47.1, 45.1], delay=0.2))]),
  V("Steigerung", "Und jetzt die Steigerung: Diagonal abschließen.", "Diagonal abschließen",
    "Jetzt wird nicht ins nahe Minitor geschossen, sondern ins untere, diagonal gegenüber. Der Läufer muss vorher schauen, ob der Weg frei ist, und den Ball mit dem ersten Kontakt in die richtige Richtung schießen.",
    sp(n7=(40, 24), n2=(55, 19)), [B("b2", 55.6, 19.6)] + ERSATZ,
    [S("Ball in den Lauf", "Spieler zwei spielt Spieler sieben nach dem zweiten Doppelpass in den Lauf. Spieler sieben schaut dabei schon zum unteren Minitor.",
       mv("n7", [44, 11]), ps("b2", [44.6, 11.6], delay=0.3), bl("n7", [56, 27], after=True)),
     S("Diagonal: Punkt", "Er schießt direkt und flach diagonal ins untere Minitor, und das gibt einen Punkt.",
       ps("b2", [69.7, 44.7]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
