import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 45-P12 (U12-U14, Woche 39 Phase 2): Midfield Triangle Combinations. 20 x 25 Yards = Feld x 30-70, y 5-55 (18 x 23 m).
# Gespiegelt: im PDF liegt der Start oben und das V öffnet sich nach unten, hier liegt der Start unten und es wird nach oben
# gespielt (echtes V). Alle Spieler pink -> Team Neon, Nummern wie im Video: Start 5 (mit Ball), 4 und 6 warten mit Bällen,
# Mitte links 10, Mitte rechts 8, oben links 11, oben rechts 9. Je ein Hütchen neben jeder Station (außen, damit kein Weg
# hindurchgeht). Grundform über rechts wie im Video (5-8 Prallpass, quer zu 11, Doppelpass 11-8, 11 dribbelt zurück),
# jeder folgt seinem Pass (5 auf die Station von 8, 8 auf die Station von 11). Der nächste Ball über links startet schon.
# Coaching-Punkte = die zwei Key Coaching Points aus dem PDF; der zweite zeigt die Runde über links. Ein Trainer.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 21, 30, "T")
POS = {"n5": (50, 49), "n4": (41.5, 50), "n6": (58.5, 50), "n10": (37, 34), "n8": (63, 34), "n11": (36, 12), "n9": (64, 12)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 24.6, 33.5), B("s2", 21, 33.5)]
LINES = [rect(30, 5, 40, 50)]
CONES = [C(50, 53.5), C(33.5, 34), C(66.5, 34), C(32.5, 12), C(67.5, 12)]
# Zweite Runde (über links): 4 startet, 11 wartet am Start, 5 steht jetzt rechts in der Mitte, 8 oben links.
POS2 = {"n4": (50, 49), "n11": (41.5, 50), "n6": (58.5, 50), "n10": (37, 34), "n5": (63, 34), "n8": (36, 12), "n9": (64, 12)}

u = {"title": "Passdreiecke im V", "code": "UE-239", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Dribbling"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 9, "field_size": "18 x 23 m",
 "description": "Fünf Hütchen bilden ein V, an jedem steht ein Spieler, am Start unten warten drei Spieler mit Bällen. Der Startspieler spielt einen Prallpass mit dem Spieler in der Mitte und dann einen scharfen Pass quer zur oberen Station auf der anderen Seite. Dort folgt ein Doppelpass mit dem Spieler aus der Mitte, der dafür vom Hütchen wegkommt, und dann wird zurück zum Start gedribbelt. Jeder folgt seinem Pass, und der nächste Ball startet schon mit dem Querpass, abwechselnd über rechts und über links.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern. Fünf Hütchen als V: eins unten in der Mitte als Start, zwei in der Mitte links und rechts, zwei oben links und rechts.",
  "Verteilen: An jedem Hütchen ein Spieler, am Start drei Spieler mit Bällen. Der Trainer steht an der Seite mit weiteren Bällen.",
  "Ablauf: Prallpass mit dem Spieler in der Mitte, scharf quer zur oberen Station auf der anderen Seite, Doppelpass mit dem Spieler aus der Mitte, dann zurück zum Start dribbeln.",
  "Wechsel: Jeder folgt seinem Pass zur nächsten Station. Sobald der Querpass gespielt ist, startet der nächste Ball, abwechselnd über rechts und über links."],
 "organisation_show": ORG,
 "coaching_points": ["Pässe mit dem richtigen Tempo und genau in den Fuß, damit der Ablauf flüssig bleibt", "Den Querpass scharf und flach spielen, wie im Spiel", "Möglichst direkt spielen, mit beiden Füßen", "Beim Dribbling zurück den Ball eng am Fuß halten"],
 "materials": ["5 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Passdreiecke im V. Mit Prallpass, scharfem Querpass und Doppelpass kombinieren sich die Spieler durch das Mittelfeld.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 49.6), B("b2", 42.1, 50.6), B("b3", 59.1, 50.6)] + ERSATZ,
  "steps": [
   S("Prallpass rechts", "Spieler fünf startet. Er spielt zu Spieler acht in der Mitte rechts, geht einen Schritt nach vorn und bekommt den Ball direkt zurück.",
     ps("b1", [63.6, 34.6]), mv("n5", [50, 44], delay=0.3), ps("b1", [50.6, 44.6], after=True)),
   S("Scharf quer", "Jetzt spielt Spieler fünf einen scharfen, flachen Pass quer nach oben links zu Spieler elf. Spieler acht löst sich vom Hütchen in die Mitte, und Spieler fünf folgt seinem ersten Pass auf den Platz von Spieler acht.",
     ps("b1", [36.6, 12.6]), mv("n8", [52, 24], delay=0.2), mv("n5", [63, 34], delay=0.6)),
   S("Doppelpass", "Spieler elf spielt zu Spieler acht und startet sofort schräg nach innen. Spieler acht spielt den Ball direkt zurück, genau in den Lauf von Spieler elf.",
     ps("b1", [52.6, 24.6]), mv("n11", [40, 24], delay=0.2), ps("b1", [40.6, 24.6], after=True)),
   S("Zurück: geschafft", "Spieler elf dribbelt mit dem Ball eng am Fuß zurück zum Start, und Spieler acht folgt seinem Pass auf den Platz oben links. Die Passfolge ist geschafft. Spieler vier hat den nächsten Ball schon gestartet, diesmal über links mit Spieler zehn.",
     dr("n11", "b1", [46, 45]), mv("n8", [36, 12], delay=0.2), ps("b2", [37.6, 34.6], delay=0.4))],
  "dims": dims(30, 70, 5, 55, "18 m", "23 m", rx=78)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Querpass scharf spielen.", "Scharf quer spielen",
    "Der Pass quer ist der längste Pass im Ablauf. Er muss fest und flach kommen, so wie im Spiel, und trotzdem genau in den Fuß. Ein weicher Pass ist zu langsam, und der Ablauf stockt.",
    sp(n5=(50, 44)), [B("b1", 50.6, 44.6), B("b2", 42.1, 50.6), B("b3", 59.1, 50.6)] + ERSATZ,
    [S("Fest und flach", "Spieler fünf hat den Prallpass zurückbekommen. Er spielt den Ball fest und flach quer, genau in den Fuß von Spieler elf. Spieler acht löst sich schon in die Mitte.",
       ps("b1", [36.6, 12.6]), mv("n8", [52, 24], delay=0.2)),
     S("Direkt weiter", "Weil der Ball genau kommt, kann Spieler elf direkt zu Spieler acht weiterspielen. Der legt direkt zurück in den Lauf, und es bleibt flüssig.",
       ps("b1", [52.6, 24.6]), mv("n11", [40, 24], delay=0.2), ps("b1", [40.6, 24.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Direkt spielen, mit beiden Füßen.", "Direkt mit beiden Füßen",
    "Jetzt läuft die Runde über links. Die Spieler spielen möglichst mit einem Kontakt und benutzen beide Füße: den Fuß, der näher zum Ziel ist. So bleibt das Tempo hoch, und jeder Pass kommt mit dem richtigen Tempo.",
    sp(POS2), [B("b1", 50.6, 49.6), B("b2", 59.1, 50.6)] + ERSATZ,
    [S("Mit links", "Spieler vier spielt mit links zu Spieler zehn, geht einen Schritt nach vorn, und Spieler zehn spielt mit einem Kontakt zurück.",
       ps("b1", [37.6, 34.6]), mv("n4", [49, 44], delay=0.3), ps("b1", [49.6, 44.6], after=True)),
     S("Mit rechts quer", "Spieler vier spielt direkt mit rechts quer nach oben rechts zu Spieler neun. Spieler zehn löst sich in die Mitte, und Spieler vier folgt auf den Platz von Spieler zehn.",
       ps("b1", [64.6, 12.6]), mv("n10", [48, 24], delay=0.2), mv("n4", [37, 34], delay=0.6)),
     S("Doppelpass direkt", "Spieler neun spielt direkt zu Spieler zehn und startet nach innen. Spieler zehn legt direkt zurück, und Spieler neun dribbelt zurück zum Start.",
       ps("b1", [48.6, 24.6]), mv("n9", [60, 24], delay=0.2), ps("b1", [60.6, 24.6], after=True), dr("n9", "b1", [55, 44], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
