import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P6 (U12-U14, Einzeltraining): Receive Turn and Finish (PDF: Directional First Touch and Finishing). 15 x 25 Yards
# = Feld x 35-65, y 5-55 (ca. 14 x 23 m), Ausrichtung wie im PDF (Minitore oben, Trainer unten). Pinker Spieler P -> Spieler
# sieben (Team Neon). Drei Minitore (oben Mitte, links und rechts etwas tiefer) mit je einer Puppe davor (als Stange gezeichnet),
# zwei gelbe Stangen links und rechts vom Starthütchen, ein Hütchen vor dem Trainer (etwas nach links gerückt, damit der Pass frei
# bleibt). Laufweg nach PDF und Video (0:16-0:38): kurz entgegenkommen, erster Kontakt in die Drehung, unten herum um die linke
# Stange, Abschluss ins Eck an der Puppe vorbei, Sprint zurück zum Start. Wettbewerb nur gegen sich selbst (Treffer in einer
# Minute als neues Ziel): deshalb Ziel statt Punkte.
# Sichtkegel aus dem Ton ("checking shoulders and creating an angle to turn", 0:16): Spieler sieben schaut beim Entgegenkommen
# über die Schulter zur Stange und zu den Minitoren. Im Video ist kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Fassungen: Coaching-Punkt 1 erster Kontakt in die Drehung (PDF Seite 2 KCP 1, Video ab 0:33, hier um die rechte Stange),
# Coaching-Punkt 2 Technik beim Abschluss (PDF Seite 2 KCP 2, Video ab 0:46 "beat the mannequin & find the corner").
T = P("T", "c", 52, 52, "T")
POS = {"n7": (52, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 56, 53), B("s2", 58.5, 53)]
LINES = [rect(35, 5, 30, 50)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 40, "y": 13, "side": "top"}, {"x": 60, "y": 13, "side": "top"}]
CONES = [C(50, 31), C(47, 47)] + [C(x, y, shape="stange") for x, y in ((45, 31), (55, 31), (50, 11.5), (40, 18), (60, 18))]

u = {"title": "Aufdrehen, Stange, drei Minitore", "code": "UE-289", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Torschuss", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "14 x 23 m",
 "description": "Der Spieler kommt dem Trainer kurz entgegen, nimmt den Pass mit dem ersten Kontakt in die Drehung mit und dribbelt um eine Stange. Dann schießt er an einer Puppe vorbei in eines von drei Minitoren. Danach sprintet er zurück zum Start, und der nächste Ball kommt. Nach einer Minute zählen die Treffer, und die Zahl ist das neue Ziel.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 23 Metern. Oben drei Minitore mit je einer Puppe davor. In der Mitte ein Starthütchen mit einer Stange links und rechts.",
  "Verteilen: Spieler sieben steht am Starthütchen. Der Trainer steht unten mit vielen Bällen.",
  "Ablauf: Spieler sieben kommt kurz entgegen, dreht mit dem ersten Kontakt auf, dribbelt um eine Stange und schießt an der Puppe vorbei ins Minitor. Dann sprintet er zurück zum Start.",
  "Wertung und Wechsel: Nach einer Minute zählt der Trainer die Treffer. Diese Zahl ist das Ziel für die nächste Minute. Dazwischen gibt es eine Pause, bei zwei Spielern ist der andere dran."],
 "organisation_show": ORG,
 "coaching_points": ["Vor dem Pass über die Schulter schauen", "Erster Kontakt in die Richtung der Drehung", "Genau statt fest schießen, ins Eck an der Puppe vorbei", "Schnell zurück zum Start und jedes Mal ein anderes Minitor"],
 "materials": ["2 Hütchen", "2 Stangen", "3 Puppen", "3 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufdrehen, Stange, drei Minitore. Spieler sieben dreht mit dem ersten Kontakt auf und trifft an der Puppe vorbei.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 52.6, 52.6)] + ERSATZ,
  "steps": [
   S("Kurz entgegenkommen", "Spieler sieben kommt dem Trainer kurz entgegen. Dabei schaut er über die Schulter: Wo ist die Stange, wo sind die Minitore?",
     mv("n7", [49, 36]), bl("n7", [40, 21], after=True)),
   S("Erster Kontakt in die Drehung", "Der Trainer spielt ihm den Ball. Spieler sieben nimmt ihn mit dem ersten Kontakt gleich zur Seite mit, in Richtung der linken Stange.",
     ps("b1", [49.6, 36.6]), dr("n7", "b1", [46.5, 38.5], after=True)),
   S("Um die Stange und schießen", "Er dribbelt unten herum um die Stange. Dann schießt er ins linke Eck des mittleren Minitors, genau an der Puppe vorbei.",
     dr("n7", "b1", [44, 39]), dr("n7", "b1", [41.5, 37.5], after=True), dr("n7", "b1", [41, 35], after=True), ps("b1", [47.8, 5.6], after=True)),
   S("Zurück zum Start: Ziel", "Sofort sprintet Spieler sieben zurück zum Start, und der Trainer spielt den nächsten Ball. Nach einer Minute zählen die Treffer. Diese Zahl ist das Ziel für die nächste Minute, und nach einer Pause ist Spieler sieben wieder dran.",
     mv("n7", [47, 36.5]), mv("n7", [52, 30], after=True))],
  "dims": dims(35, 65, 5, 55, "14 m", "23 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt geht in die Richtung der Drehung.", "Erster Kontakt in die Drehung",
    "Schon vor dem Pass steht der Spieler leicht schräg. So nimmt er den Ball mit dem ersten Kontakt direkt in die Drehung mit. Er bleibt in Bewegung und kann sofort beschleunigen.",
    sp(), [B("b1", 52.6, 52.6)] + ERSATZ,
    [S("Schräg entgegen", "Spieler sieben kommt entgegen und dreht den Körper schon leicht nach rechts, zur rechten Stange.",
       mv("n7", [51, 36]), bl("n7", [60, 21], after=True)),
     S("Mitnehmen und beschleunigen", "Der Pass kommt. Mit dem ersten Kontakt legt er den Ball nach rechts vor, dribbelt unten herum um die Stange und beschleunigt.",
       ps("b1", [51.6, 36.6]), dr("n7", "b1", [55.5, 38.5], after=True), dr("n7", "b1", [59, 35], after=True)),
     S("Anderes Minitor", "Diesmal schießt er ins rechte Eck des mittleren Minitors. Jedes Mal ein anderes Ziel, dann zurück zum Start.",
       ps("b1", [52.2, 5.6]), mv("n7", [54, 36.5], after=True), mv("n7", [52, 30], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Genau ins Eck schießen, an der Puppe vorbei.", "Genau ins Eck",
    "Ein Schuss gerade auf das Tor bleibt an der Puppe hängen, ein schwacher Schuss kommt nicht an. Der Spieler schaut kurz auf und schießt sauber und flach ins freie Eck. Genauigkeit geht vor Härte.",
    sp(n7=(41, 35)), [B("b1", 41.6, 35.6)] + ERSATZ,
    [S("Kurz aufschauen", "Spieler sieben hat die Stange hinter sich und legt sich den Ball nach vorn. Er schaut kurz auf: Wo ist das freie Eck neben der Puppe?",
       dr("n7", "b1", [42, 27]), bl("n7", [42.5, 13], after=True)),
     S("Flach ins Eck: Ziel", "Er schießt flach und genau ins rechte Eck des linken Minitors, an der Puppe vorbei. So trifft er öfter, und das ist das Ziel.",
       ps("b1", [42.6, 13.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
