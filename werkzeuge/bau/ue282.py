import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P8 (U12-U14, Einzeltraining): Receive, Turn to Drive & Shift to Finish (Ordner "Individual Finishing Circuit 1 to 1-P8").
# 25 x 25 Yards = Feld x 25-75, y 5-55 (23 m). Ausrichtung wie im Original (nicht gedreht): zwei gespiegelte Rundläufe,
# Minitor oben rechts und unten links (ohne Torwart), Dummys (rot -> orange Stangen) links und rechts in der Mitte,
# Startstangen (gelb -> neon Stangen) unten in der Mitte und oben links. Markierungen des Trainers (rot) -> orange Hütchen.
# Spieler P -> Spieler sieben (Team Neon). Im Original wechselt der Trainer für die zweite Seite zur oberen Markierung.
# Keine Wertung im Original: Ziel statt Punkte (in die Ecke treffen). Pause nach zwei Durchgängen (vier Abschlüsse).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (in die Ecken schießen, im Video auf der zweiten Seite gezeigt;
# gerichteter erster Kontakt zum Aufdrehen).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 46, 33, "T")
POS = {"n7": (54.5, 47)}
def sp(t=(46, 33), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [P("T", "c", t[0], t[1], "T")]
ERSATZ = [B("s1", 44, 27), B("s2", 47.5, 26)]
BAELLE = [B("b1", 46.6, 33.6)] + ERSATZ
LINES = [rect(25, 5, 50, 50)]
CONES = [C(66, 30.5, shape="stange"), C(34, 30.5, shape="stange"), C(56.5, 37, "neon", shape="stange"),
         C(39, 12, "neon", shape="stange"), C(50.5, 33), C(50, 19.5)]
TORE = [{"x": 65, "y": 10, "side": "top"}, {"x": 35, "y": 50, "side": "bottom"}]
AUFDREHEN = [dr("n7", "b1", [58.5, 49.5], after=True), dr("n7", "b1", [64, 40], after=True)]

u = {"title": "Aufdrehen, vorbei, in die Ecke", "code": "UE-282", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Dribbling", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "23 x 23 m",
 "description": "Ein Spieler läuft mit dem Trainer einen Rundlauf mit zwei Seiten. Er nimmt den Pass an, dreht mit dem ersten Kontakt auf und dribbelt schnell auf einen Dummy zu. Am Dummy legt er sich den Ball blitzschnell vorbei und schießt in die Ecke des Minitors. Danach sprintet er zur Stange auf der anderen Seite und macht dasselbe noch einmal.",
 "organisation": ["Aufbauen: Ein Feld von dreiundzwanzig mal dreiundzwanzig Metern mit zwei gleichen Rundläufen. Oben rechts und unten links steht ein Minitor, links und rechts in der Mitte je ein Dummy. Zwei Startstangen stehen unten in der Mitte und oben links.",
  "Verteilen: Der Spieler startet unten an der Stange. Der Trainer steht in der Mitte mit vielen Bällen.",
  "Ablauf: Der Trainer passt, der Spieler dreht mit dem ersten Kontakt auf und dribbelt zum rechten Dummy. Er legt sich den Ball vorbei und schießt ins obere Minitor. Dann sprintet er zur Stange oben links und läuft den Rundlauf von dort zum linken Dummy und unteren Minitor.",
  "Wechsel: Nach zwei Durchgängen, also vier Abschlüssen, ruft der Trainer eine Pause aus. Danach geht es wieder von unten los."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem ersten Kontakt den Ball vom Fuß weg mitnehmen und schnell aufdrehen", "Mit Tempo auf den Dummy zudribbeln", "Den Ball blitzschnell am Dummy vorbeilegen", "Flach und hart in die Ecken schießen, nicht in die Mitte"],
 "materials": ["2 Minitore", "2 Dummys", "2 Stangen", "2 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufdrehen, vorbei, in die Ecke. Ein Spieler dreht mit dem ersten Kontakt auf, geht am Dummy vorbei und schießt in die Ecke.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Pass und aufdrehen", "Der Trainer passt zu Spieler sieben an der unteren Stange. Spieler sieben nimmt den Ball mit dem ersten Kontakt nach rechts mit und dreht sich schnell auf.",
     ps("b1", [55.1, 47.6]), *AUFDREHEN),
   S("Zum Dummy dribbeln", "Mit Tempo dribbelt er auf den rechten Dummy zu.",
     dr("n7", "b1", [66, 37])),
   S("Schnell vorbei", "Kurz vor dem Dummy legt er sich den Ball blitzschnell außen vorbei.",
     dr("n7", "b1", [70.5, 31]), dr("n7", "b1", [69, 24], after=True)),
   S("Abschluss in die Ecke", "Mit dem nächsten Kontakt schießt Spieler sieben flach in die linke Ecke des oberen Minitors.",
     ps("b1", [62, 10.5])),
   S("Sprint zur anderen Seite", "Dann sprintet er sofort zur Stange oben links, und der Trainer geht zum oberen Hütchen. Ziel ist, jeden Ball in eine Ecke zu schießen. Jetzt ist Spieler sieben von der anderen Seite dran, nach vier Abschlüssen gibt es eine Pause.",
     mv("n7", [56, 15]), mv("n7", [43.5, 12], after=True), mv("T", [54.5, 21]))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: In die Ecken schießen.", "In die Ecken schießen",
    "Im Tor steht kein Torwart. Ein lockerer Schuss in die Mitte wäre im Spiel leicht zu halten. Deshalb schießt der Spieler flach und hart in eine Ecke und achtet auf Genauigkeit.",
    sp(t=(54.5, 21), n7=(31, 37)), [B("b1", 31.6, 37.6)] + ERSATZ,
    [S("Ball vorlegen", "Spieler sieben ist auf der zweiten Seite schon am linken Dummy vorbei. Er legt sich den Ball zum Schuss vor.",
       dr("n7", "b1", [33, 41])),
     S("Flach in die Ecke", "Er schießt flach und hart in die linke Ecke, nicht in die Mitte. Dann geht es zurück zur unteren Stange.",
       ps("b1", [32, 49.5]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit dem ersten Kontakt aufdrehen.", "Mit dem ersten Kontakt drehen",
    "Der Spieler öffnet schon vor dem Pass den Körper. Mit dem ersten Kontakt nimmt er den Ball vom Fuß weg in die neue Richtung mit und dreht schnell um die Stange. So spart er Zeit und kann sofort nach vorn spielen.",
    sp(), BAELLE,
    [S("Körper öffnen", "Spieler sieben steht offen zum Trainer. Der Trainer passt ihm den Ball zu.",
       ps("b1", [55.1, 47.6])),
     S("Erster Kontakt mit Richtung", "Mit dem ersten Kontakt nimmt er den Ball nach rechts weg und dreht sich in einer Bewegung auf. Schon ist er unterwegs zum Dummy.",
       dr("n7", "b1", [58.5, 49.5]), dr("n7", "b1", [64, 40], after=True), dr("n7", "b1", [66, 37], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
