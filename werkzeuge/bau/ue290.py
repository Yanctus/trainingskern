import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P24 (U12-U14, Einzeltraining): Receiving in the Pockets - CAM (PDF: How to Receive in the Pocket - CM). 20 x 20 Yards
# = Feld x 25-75, y 5-55 (ca. 18 x 18 m), Ausrichtung wie im PDF (Minitore oben in den Ecken, Trainer unten). Die Minitore stehen
# im Original schräg in den Ecken, hier gerade an der oberen Linie. Oranger Spieler -> Spieler sieben (Team Neon), Position Zehner.
# Vier rote Stangen bilden das Viereck in der Mitte ("Pocket", hier "Lücke zwischen den Linien"), ein Hütchen darüber, eins neben dem
# Trainer. Grundform nach PDF und Video (0:08-0:30): Prallpass, rückwärts aus der Lücke, Annahme mit dem hinteren Fuß in der
# Drehung, Steckpass ins Minitor, abwechselnd links und rechts. Reine Technikübung: Ziel statt Punkte.
# Sichtkegel aus dem PDF ("Body Position and Scanning - Open body and scan early to see space and options"): Spieler sieben schaut
# beim Rückwärtslaufen zum Minitor (Grundform) bzw. beim Entgegenkommen zum rechten Minitor (Steigerung 1). Im Video kein Kegel.
# Fassungen: Steigerung 1 dem Ball entgegen (PDF Seite 2 Progression 1, Video ab 0:40), Steigerung 2 beide Bewegungen
# hintereinander (PDF Seite 2 Progression 2, Video ab 1:16). Der Trainer rückt im Video etwas ins Feld, hier bleibt er stehen.
T = P("T", "c", 50, 50, "T")
POS = {"n7": (50, 32)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 55, 53), B("s2", 57.5, 53)]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 30, "y": 5, "side": "top"}, {"x": 70, "y": 5, "side": "top"}]
CONES = [C(50, 14), C(46, 53)] + [C(x, y, shape="stange") for x in (44, 56) for y in (26, 38)]
BALL = [B("b1", 50.6, 50.6)] + ERSATZ

u = {"title": "Zwischen den Linien annehmen", "code": "UE-290", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "18 x 18 m",
 "description": "Eine Übung für den Zehner, der zwischen den Linien den Ball bekommt. Nach einem Prallpass mit dem Trainer läuft der Spieler rückwärts aus der Lücke und nimmt den nächsten Pass in der Drehung mit dem hinteren Fuß an. Mit dem zweiten Kontakt spielt er einen Steckpass in ein Minitor, als ob ein Stürmer losläuft. Danach geht es zur anderen Seite.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit zwei Minitoren in den oberen Ecken. In der Mitte bilden vier Stangen ein Viereck, die Lücke zwischen den Linien. Darüber liegt ein Hütchen.",
  "Verteilen: Spieler sieben steht in der Lücke. Der Trainer steht unten mit vielen Bällen.",
  "Ablauf: Prallpass mit dem Trainer, dann rückwärts aus der Lücke. Der zweite Pass wird in der Drehung angenommen und als Steckpass ins Minitor gespielt.",
  "Wechsel: Abwechselnd ins linke und ins rechte Minitor, bis alle Bälle gespielt sind. Dann Pause, bei zwei Spielern ist der andere dran."],
 "organisation_show": ORG,
 "coaching_points": ["Früh umschauen und den Körper öffnen", "Mit dem hinteren Fuß annehmen, damit es schnell nach vorn geht", "Die Bewegung so timen, dass Platz und ein guter Winkel entstehen", "Der erste Kontakt geht nach vorn aus der Lücke, dann schnell und sauber passen"],
 "materials": ["2 Hütchen", "4 Stangen", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Zwischen den Linien annehmen. Spieler sieben ist der Zehner und bekommt den Ball in der Lücke zwischen den Stangen.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BALL,
  "steps": [
   S("Prallpass", "Der Trainer spielt Spieler sieben in der Lücke zwischen den Stangen an. Er lässt den Ball direkt zum Trainer zurückprallen.",
     ps("b1", [50.6, 32.6]), ps("b1", [50.6, 50.6], after=True)),
   S("Rückwärts aus der Lücke", "Jetzt läuft Spieler sieben rückwärts aus der Lücke. Dabei öffnet er den Körper und schaut schon zum linken Minitor.",
     mv("n7", [50, 22]), bl("n7", [34, 10], after=True)),
   S("Mit dem hinteren Fuß", "Der Trainer spielt den zweiten Pass. Spieler sieben nimmt ihn in der Drehung mit dem hinteren Fuß an und legt ihn nach vorn.",
     ps("b1", [50.6, 22.6]), dr("n7", "b1", [46, 19], after=True)),
   S("Steckpass ins Minitor: Ziel", "Mit dem nächsten Kontakt spielt er einen Steckpass ins linke Minitor, als ob ein Stürmer losläuft. Das Ziel: jeder Ball mit wenigen, sauberen Kontakten ins Minitor. Dann geht er zurück in die Lücke, und der nächste Ball geht nach rechts.",
     ps("b1", [30.6, 5.8]), mv("n7", [50, 32], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Spieler sieben kommt dem Ball entgegen.", "Dem Ball entgegen",
    "Jetzt startet der Spieler oben am Hütchen. Nach dem Prallpass läuft er nicht rückwärts, sondern kommt dem Ball in die Lücke entgegen. So lässt sich ein Zehner im Spiel fallen, um den Ball zu bekommen. Er nimmt im Laufen an, dreht auf und spielt ins rechte Minitor.",
    sp(n7=(53, 15)), BALL,
    [S("Prallpass von oben", "Spieler sieben steht oben am Hütchen. Der Trainer spielt ihn an, und er lässt den Ball zurückprallen.",
       ps("b1", [53.6, 15.6]), ps("b1", [50.6, 50.6], after=True)),
     S("In die Lücke entgegen", "Jetzt läuft er dem Ball entgegen in die Lücke. Dabei schaut er schon zum rechten Minitor.",
       mv("n7", [50, 29]), bl("n7", [66, 12], after=True)),
     S("Im Laufen aufdrehen", "Der Pass kommt. Spieler sieben nimmt ihn im Laufen an und dreht mit dem ersten Kontakt nach vorn aus der Lücke.",
       ps("b1", [50.6, 29.6]), dr("n7", "b1", [54, 22], after=True)),
     S("Ins rechte Minitor: Ziel", "Dann spielt er den Steckpass ins rechte Minitor. Das Ziel: annehmen, aufdrehen und passen in einem Fluss.",
       ps("b1", [70.6, 5.8]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Beide Bewegungen hintereinander.", "Erst weg, dann entgegen",
    "Erst läuft der Spieler rückwärts und lässt den Ball zum Trainer prallen. Gleich danach kommt er wieder in die Lücke, bekommt den zweiten Pass im Laufen, dreht auf und spielt ins Minitor. Er lernt, wann er vom Ball weg und wann er zum Ball hin läuft.",
    sp(n7=(50, 28)), BALL,
    [S("Rückwärts und prallen lassen", "Spieler sieben läuft rückwärts aus der Lücke. Der Trainer spielt ihn an, und er lässt den Ball zurückprallen.",
       mv("n7", [50, 19]), ps("b1", [50.6, 19.6], after=True), ps("b1", [50.6, 50.6], after=True)),
     S("Sofort wieder entgegen", "Sofort läuft er wieder nach vorn in die Lücke und bekommt den zweiten Pass im Laufen.",
       mv("n7", [50, 30]), ps("b1", [50.6, 30.6], delay=0.4)),
     S("Aufdrehen ins Minitor: Ziel", "In der Lücke dreht er auf, nimmt den Ball nach vorn mit und spielt ins linke Minitor. Das Ziel: der erste Kontakt bringt ihn aus dem Viereck heraus.",
       dr("n7", "b1", [47, 23]), ps("b1", [30.6, 5.8], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
