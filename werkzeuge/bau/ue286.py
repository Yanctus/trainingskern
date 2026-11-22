import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P23 (U12-U14, Einzeltraining): Passing and Receiving - CM (PDF: "Passing, Receiving and Moving - CM").
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), Trainer unten, Spiel nach oben. Vier Hütchen: zwei eng als
# "Hütchentor" oben (46,5/53,5 bei y 26), zwei breiter darunter (39/61 bei y 36). Zentraler Mittelfeldspieler = Spieler acht.
# Die zwei Minitore oben in den Ecken der PDF-Skizze fehlen im Text und im Video und werden nicht benutzt: weggelassen.
# Grundform nach PDF/Video: Prallpass Mitte, Prallpass außen am rechten Hütchen, außen neben dem Hütchentor annehmen,
# Kontakt vor das Tor und verdeckter Rückpass durch das Tor, dann andere Seite.
# Sichtkegel aus dem Video: bei 0:33-0:40 ("Disguise central pass - deception with hips & eyes") schaut der Spieler vor
# dem Rückpass nach links weg (Grundform Schritt 4), bei 1:52-2:02 ("Receive facing forward") schaut er vor der Annahme
# links außen zum Hütchentor (Coaching-Punkt). Ton: "scan the field, maintain vision" (Rückwärtsschritt) im Text.
# Fassungen: Coaching-Punkt "offen annehmen" (linke Seite) und Steigerung = Progression 1 (Drehung mit verstecktem Ball).
# Progression 2 (Drehung plus verdeckter Rückpass) nicht als eigene Fassung gebaut, nur im Text der Steigerung erwähnt.
T = P("T", "c", 50, 49, "T")
POS = {"n8": (50, 33)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 45.5, 52), B("s2", 43, 52)]
CONES = [C(46.5, 26), C(53.5, 26), C(39, 36), C(61, 36)]
TR = [50.6, 49.6]

u = {"title": "Offen annehmen, verdeckt passen", "code": "UE-286", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "18 x 18 m",
 "description": "Einzeltraining für zentrale Mittelfeldspieler mit dem Trainer. Spieler acht lässt Pässe in der Mitte und außen prallen, nimmt dann neben dem Hütchentor offen an und spielt verdeckt durch das Tor zurück. Danach kommt die andere Seite dran, immer im Wechsel. So lernt er, offen anzunehmen, mit Hüfte und Augen zu täuschen und genug Abstand zu halten.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben ein enges Hütchentor, darunter zwei Hütchen weiter auseinander.",
  "Verteilen: Spieler acht steht in der Mitte zwischen den Hütchen. Der Trainer steht unten mit mehreren Bällen.",
  "Ablauf: Prallpass in der Mitte, Prallpass außen am Hütchen, dann neben dem Hütchentor annehmen und verdeckt durch das Tor zurück zum Trainer. Danach die andere Seite.",
  "Wechsel: Spieler acht arbeitet eine feste Zeit, dann ist Pause. Sind zwei Spieler da, wechseln sie sich ab."],
 "organisation_show": ORG,
 "coaching_points": ["Beim Annehmen die Hüfte öffnen und schon nach vorn schauen", "Beim Rückpass die Hüfte schließen und mit den Augen täuschen", "Beim Drehen den Ball mit dem Körper verstecken", "Genug Abstand halten, notfalls schnell ein paar Schritte rückwärts"],
 "materials": ["4 Hütchen", "Mehrere Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Offen annehmen, verdeckt passen. Spieler acht spielt mit dem Trainer Prallpässe und spielt dann verdeckt durch das Hütchentor zurück.",
 "board": {"lines": [rect(25, 5, 50, 50)], "cones": CONES, "players": sp(), "balls": [B("b1", *TR)] + ERSATZ,
  "steps": [
   S("Prallpass in der Mitte", "Spieler acht steht in der Mitte zwischen den Hütchen. Der Trainer passt zu ihm, und Spieler acht lässt den Ball direkt zurückprallen.",
     ps("b1", [50.6, 33.6]), ps("b1", TR, after=True)),
   S("Prallpass außen", "Jetzt läuft Spieler acht nach außen neben das rechte Hütchen. Wieder kommt ein Pass vom Trainer, und wieder spielt er direkt zurück.",
     mv("n8", [64, 31]), mv("n8", [67, 38], after=True), ps("b1", [67.6, 38.6], after=True), ps("b1", TR, after=True)),
   S("Außen annehmen", "Spieler acht läuft hoch neben das Hütchentor. Er öffnet die Hüfte zur Mitte und nimmt den Pass vom Trainer offen an.",
     mv("n8", [60, 24]), ps("b1", [60.6, 24.6], after=True)),
   S("Verdeckt zurück", "Mit dem ersten Kontakt geht er vor das Hütchentor. Er schaut nach links, als wollte er dorthin spielen, und passt dann durch das Tor zurück zum Trainer.",
     dr("n8", "b1", [50, 21]), bl("n8", [33, 20], after=True), ps("b1", TR, after=True)),
   S("Andere Seite", "Der Ball ist durch das Hütchentor beim Trainer, das ist das Ziel. Spieler acht läuft zurück in die Mitte, und jetzt ist die linke Seite dran. Nach einer festen Zeit ist Pause.",
     mv("n8", [50, 33]))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Offen annehmen und nach vorn schauen.", "Offen annehmen",
    "Wer offen annimmt, sieht das Spiel vor sich. Spieler acht dreht die Hüfte schon vor dem Pass zur Mitte und schaut zum Hütchentor. Steht er zu nah, geht er schnell ein paar Schritte rückwärts und schafft sich Platz.",
    sp(n8=(40, 24)), [B("b1", *TR)] + ERSATZ,
    [S("Hüfte öffnen", "Spieler acht steht jetzt links neben dem Hütchentor. Bevor der Ball kommt, öffnet er die Hüfte und schaut schon zum Tor. Dann passt der Trainer.",
       bl("n8", [58, 21]), ps("b1", [40.6, 24.6], after=True)),
     S("Mitnehmen und zurück", "Mit dem ersten Kontakt nimmt er den Ball gleich mit vor das Hütchentor und spielt verdeckt zurück zum Trainer.",
       dr("n8", "b1", [50, 21]), ps("b1", TR, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Drehen und den Ball verstecken.", "Drehen mit Ball",
    "Nach der Annahme außen dribbelt Spieler acht über das Hütchentor und dreht sich auf der sicheren Seite. Sein Körper bleibt zwischen Ball und gedachtem Gegner. Erst dann spielt er zurück zum Trainer. Noch schwerer: nach der Drehung verdeckt zurückpassen.",
    sp(n8=(60, 24)), [B("b1", 60.6, 24.6)] + ERSATZ,
    [S("Nach innen dribbeln", "Spieler acht hat den Ball außen angenommen. Er dribbelt oberhalb vom Hütchentor nach links.",
       dr("n8", "b1", [46, 18])),
     S("Drehen", "Jetzt dreht er sich mit dem Ball weg. Sein Körper ist zwischen Ball und Gegner, so bleibt der Ball versteckt.",
       dr("n8", "b1", [46, 13]), dr("n8", "b1", [53, 14], after=True), dr("n8", "b1", [50.5, 20.5], after=True)),
     S("Zurück und wechseln", "Dann spielt er durch das Hütchentor zurück zum Trainer, läuft in die Mitte, und die andere Seite ist dran.",
       ps("b1", TR), mv("n8", [50, 33], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
