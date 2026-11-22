import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P21 (U12-U14, Einzeltraining): Develop Technique to Win Aerial Duels - CB (Ordner "Winning Aerial Duels - CB 1 to 1-P21").
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m). Ausrichtung wie im PDF (Dummys oben, Trainer unten, nicht gedreht).
# Blauer Spieler -> Spieler vier (Team Neon, Innenverteidiger). Drei Dummys im Dreieck: hinterer Dummy knapp im Feld (im
# Original auf der Linie), die beiden vorderen etwas weiter auseinander, damit der Laufweg frei bleibt. Die Minitore stehen im
# Original schräg in den oberen Ecken; hier gerade an der oberen Linie (schräge Tore gibt es auf der Tafel nicht).
# Ballhaufen beim Trainer -> zwei Ersatzbälle. Reine Technikübung ohne Wertung: Ziel statt Punkte.
# Sichtkegel: Video 0:20-0:27 ("eyes on ball", Kegel vom Spieler zum Trainer) und 0:50-0:58 ("Scan, adjust body shape,
# sprint out", Kegel vom Spieler zum Trainer, bevor der Pass zum Minitor kommt), Ton "scan early", PDF "Eyes on the Ball"
# -> bl() zum Trainer in der Grundform und in beiden Steigerungen.
# Fassungen: Steigerung 1 = nach dem Kopfball einen Pass zum rechten Minitor blocken (PDF Seite 2 links, Video 0:34-1:05),
# Steigerung 2 = Ball mit der Brust annehmen, Pass zum Trainer, dann zur anderen Seite blocken (PDF Seite 2 rechts, Video ab 1:06).
# Laufweg zum Blocken unterhalb der Dummys mit Zwischenpunkt (im Original Bogen oberhalb, dort sind die Dummys im Weg).
T = P("T", "c", 50, 42, "T")
POS = {"n4": (53, 9.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 46.5, 44.5), B("s2", 44.5, 45.5)]
BALL_T = [50.6, 42.6]
KOPF = [50.6, 21.6]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 33, "y": 5, "side": "top"}, {"x": 67, "y": 5, "side": "top"}]
CONES = [C(50, 7, shape="stange"), C(44.5, 17, shape="stange"), C(55.5, 17, shape="stange")]

u = {"title": "Hohe Bälle köpfen und blocken", "code": "UE-297", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "18 x 18 m",
 "description": "Ein Innenverteidiger übt, hohe Bälle zu gewinnen. Drei Dummys stehen eng zusammen wie Gegenspieler. Der Trainer wirft den Ball hoch, der Spieler sprintet nach vorn und köpft ihn kontrolliert nach unten zurück. Danach berührt er den hinteren Dummy, dreht den Körper und ist bereit für den nächsten Ball.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben in der Mitte ein Dummy, davor zwei Dummys eng nebeneinander. Oben links und rechts je ein Minitor für die Steigerungen.",
  "Verteilen: Spieler vier steht beim hinteren Dummy. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Der Trainer wirft den Ball hoch. Spieler vier sprintet zwischen den Dummys nach vorn und köpft den Ball nach unten zurück zum Trainer. Dann läuft er zurück und berührt den hinteren Dummy.",
  "Wechsel: Nach jedem Kopfball dreht der Spieler den Körper, mal über links, mal über rechts, und der nächste Ball kommt. Sind alle Bälle gespielt, gibt es eine Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Den Sprung so timen, dass du den Ball am höchsten Punkt triffst", "Die Augen bis zum Kopfball immer am Ball lassen", "Die Arme für Gleichgewicht, Sprungkraft und Schutz nutzen", "Nach dem Kopfball schnell reagieren und wieder bereit sein"],
 "materials": ["3 Dummys", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Hohe Bälle köpfen und blocken. Spieler vier ist Innenverteidiger und gewinnt hohe Bälle mit dem Kopf.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *BALL_T)] + ERSATZ,
  "steps": [
   S("Dummy berühren, Ball im Blick", "Spieler vier berührt den hinteren Dummy und dreht sich zum Trainer. Er hat den Ball immer im Blick.",
     bl("n4", [50, 30])),
   S("Sprinten und springen", "Der Trainer wirft den Ball hoch. Spieler vier sprintet zwischen den beiden Dummys nach vorn, nimmt die Arme mit und springt zum Ball.",
     mv("n4", [50, 21]), ps("b1", KOPF, delay=0.3)),
   S("Kopfball nach unten: Ziel", "Er trifft den Ball am höchsten Punkt und köpft ihn nach unten genau zum Trainer. Das ist das Ziel. Dann läuft er zurück, berührt wieder den hinteren Dummy, dreht den Körper, und der nächste Ball kommt.",
     ps("b1", BALL_T), mv("n4", [53, 9.5], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Kopfball einen Pass blocken.", "Köpfen, dann blocken",
    "Nach dem Kopfball spielt der Trainer sofort einen Pass zu einem der Minitore, so als hätte der Gegner den Ball gewonnen. Der Spieler landet sicher, schaut zum Trainer, drückt sich kräftig mit dem Standbein ab und blockt den Pass.",
    sp(), [B("b1", *BALL_T)] + ERSATZ,
    [S("Kopfball", "Der Trainer wirft, Spieler vier sprintet nach vorn und köpft den Ball nach unten zurück zum Trainer.",
       mv("n4", [50, 21]), ps("b1", KOPF, delay=0.3), ps("b1", BALL_T, after=True)),
     S("Früh schauen", "Er landet sicher und schaut sofort zum Trainer. Wohin geht der Pass?",
       bl("n4", [50, 40])),
     S("Pass blocken: Ziel", "Der Trainer passt zum rechten Minitor. Spieler vier drückt sich ab, sprintet hin und blockt den Pass. Das ist das Ziel. Dann zurück zum hinteren Dummy, und der nächste Ball kommt.",
       mv("n4", [57, 23]), mv("n4", [65, 16], after=True), ps("b1", [65.6, 16.6], delay=0.2))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Mit der Brust annehmen, dann blocken.", "Brust, Pass und blocken",
    "Jetzt nimmt der Spieler den Ball mit der Brust an. Mit dem zweiten Kontakt spielt er einen festen, genauen Pass zum Trainer. Ruhig bleiben, nur zwei Kontakte. Dann kommt der Pass zum Minitor auf der anderen Seite, und er blockt ihn.",
    sp(), [B("b1", *BALL_T)] + ERSATZ,
    [S("Mit der Brust", "Der Trainer wirft den Ball hoch. Spieler vier sprintet nach vorn und nimmt den Ball ruhig mit der Brust an.",
       mv("n4", [50, 21]), ps("b1", KOPF, delay=0.3)),
     S("Pass zum Trainer", "Mit dem zweiten Kontakt spielt er einen festen, genauen Pass zurück zum Trainer.",
       ps("b1", BALL_T)),
     S("Früh schauen", "Sofort schaut er zum Trainer. Wohin geht der nächste Pass?",
       bl("n4", [50, 40])),
     S("Andere Seite blocken: Ziel", "Der Trainer passt zum linken Minitor. Spieler vier sprintet hin und blockt den Pass. Das ist das Ziel. Dann zurück zum hinteren Dummy, und es geht von vorn los.",
       mv("n4", [43, 23]), mv("n4", [35, 16], after=True), ps("b1", [35.6, 16.6], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
