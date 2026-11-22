import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P18 (U12-U14, Einzeltraining): Stopping Forward Passes - CDM. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m),
# Orientierung wie im PDF (Minitore und Dummy oben, Trainer unten, Pass nach oben). Spieler startet rechts neben dem Dummy (Video: direkt davor; 3D-Sicht). Blocklinie gestrichelt kurz vor den Minitoren
# (Video), im PDF etwas tiefer. Orange (CDM) -> Neon 6 (Sechser). Acht Bälle beim Trainer: auf der Tafel zwei zum Spielen plus
# zwei Ersatzbälle. Laufweg nach Video: um den Dummy herum (hinten herum), dann auf dem kürzesten Weg an die Blocklinie, danach
# zurück um den Dummy und zur anderen Seite. Im Video wechselt der Trainer zwischendurch die Position, hier bleibt er stehen.
# Coaching-Punkt "Ran an die Linie" (Get up to the line); PDF-Progression 2 (Blocklinie näher zum Trainer, eine Erleichterung) nur im Text,
# Progression 1 (zweiter Ball sofort danach) als Steigerung.
# Sichtkegel aus dem Video ("Read hips and eyes increases reaction speed", Kegel vom Spieler zum Trainer eingezeichnet) und aus
# Text/Ton ("Scanning to read body shape", "Scanning remains crucial"): Spieler sechs schaut vor jedem Pass zum Trainer.
T = P("T", "c", 50, 44, "T")
POS = {"n6": (57, 17)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 47.5), B("s2", 46, 47.5)]
def baelle(b1=(50.6, 44.6)):
    return [B("b1", *b1), B("b2", 49, 46.2)] + ERSATZ
LINES = [rect(25, 5, 50, 50), line(25, 18, 75, 18)]
TORE = [{"x": 35, "y": 9, "side": "top"}, {"x": 65, "y": 9, "side": "top"}]
DUMMY = [C(50, 10, shape="stange")]
HERUM = [mv("n6", [57.5, 10]), mv("n6", [50, 5.5], after=True), mv("n6", [43, 9.5], after=True)]

u = {"title": "Sechser blockt Pässe zum Minitor", "code": "UE-293", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1, "field_size": "18 x 18 m",
 "description": "Der Sechser übt, Pässe nach vorn zu blocken. Er läuft um einen Dummy und sprintet dann an eine Linie vor zwei Minitoren. Der Trainer spielt von unten auf eines der Minitore, und der Spieler blockt den Pass oder fängt ihn ab. Dabei liest er Hüfte und Augen des Trainers, um den Pass vorauszuahnen.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben stehen zwei Minitore, dazwischen ein Dummy. Kurz vor den Minitoren ist eine Blocklinie markiert.",
  "Verteilen: Der Spieler steht oben am Dummy. Der Trainer steht unten mit acht Bällen.",
  "Ablauf: Der Spieler läuft um den Dummy. Der Trainer spielt flach auf eines der Minitore, und der Spieler sprintet an die Linie und blockt den Pass. Dann sofort zurück um den Dummy und den nächsten Pass verteidigen.",
  "Wechsel: Nach acht Bällen ist die Runde vorbei, und der Spieler hat Pause. Dann geht es wieder von vorn los."],
 "organisation_show": ORG,
 "coaching_points": ["Sofort reagieren, schnell zurück und den nächsten Pass blocken", "Hüfte und Augen des Trainers lesen, um den Pass vorauszuahnen", "Auf dem kürzesten Weg an die richtige Stelle sprinten", "Schnell an die Linie herausrücken, damit der Passwinkel eng wird"],
 "materials": ["2 Minitore", "1 Dummy", "8 Bälle", "Hütchen für die Blocklinie"],
 "access": "abo", "hidden": True,
 "say_intro": "Sechser blockt Pässe zum Minitor. Spieler sechs läuft um den Dummy und blockt die Pässe des Trainers, bevor sie ins Minitor gehen.",
 "board": {"lines": LINES, "goals": TORE, "cones": DUMMY, "players": sp(), "balls": baelle(),
  "steps": [
   S("Um den Dummy", "Spieler sechs startet am Dummy und läuft hinten um ihn herum.", *HERUM),
   S("Den Trainer lesen", "Dabei schaut er auf den Trainer, vor allem auf Hüfte und Augen. So ahnt er, wohin der Pass geht.",
     bl("n6", [46, 30])),
   S("Pass blocken", "Der Trainer spielt flach Richtung linkes Minitor. Spieler sechs sprintet auf dem kürzesten Weg an die Linie und blockt den Ball.",
     mv("n6", [37.5, 18]), ps("b1", [38.1, 18.6], delay=0.3)),
   S("Zurück und andersrum", "Sofort läuft Spieler sechs zurück um den Dummy, und der Trainer spielt den nächsten Ball zur anderen Seite. Spieler sechs blockt wieder. Nach acht Bällen ist die Runde vorbei, dann hat er Pause.",
     mv("n6", [43, 9.5]), mv("n6", [50, 5.5], after=True), mv("n6", [57, 9.5], after=True), mv("n6", [62.5, 18], after=True),
     ps("b2", [63.1, 18.6], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ran an die Linie.", "Ran an die Linie",
    "Der Spieler rückt schnell bis an die Linie heraus. Je näher er dem Ball kommt, desto enger wird der Winkel für den Pass. Fällt das Blocken noch schwer, kommt die Blocklinie näher zum Trainer, und klappt es gut, rückt sie wieder zurück.",
    sp(n6=(43, 9.5)), baelle(), [
     S("Früh lesen", "Spieler sechs ist um den Dummy gelaufen und liest Hüfte und Augen des Trainers.",
       bl("n6", [47, 30])),
     S("Herausrücken und blocken", "Der Trainer spielt nach rechts. Spieler sechs sprintet sofort schräg nach vorn bis an die Linie. So wird der Winkel eng, und er blockt den Pass.",
       mv("n6", [59, 18]), ps("b1", [59.6, 18.6], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Gleich ein zweiter Ball.", "Zweiter Ball sofort",
    "Kaum ist der erste Pass geblockt, spielt der Trainer sofort den zweiten Ball. Der Spieler muss blitzschnell reagieren und wissen, wo er steht. Wer den zweiten Pass zu spät erkennt, kommt nicht mehr hin.",
    sp(n6=(37.5, 18)), baelle(b1=(38.1, 18.6)), [
     S("Sofort wieder schauen", "Spieler sechs hat den ersten Ball geblockt. Er schaut sofort wieder zum Trainer.",
       bl("n6", [44, 36])),
     S("Zweiter Ball: blocken", "Der Trainer spielt gleich den zweiten Ball zum rechten Minitor. Spieler sechs sprintet an der Linie entlang und blockt auch diesen Pass. Dann hat er kurz Pause.",
       mv("n6", [62.5, 18]), ps("b2", [63.1, 18.6], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
