import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P12 (U12-U14, Einzeltraining): Process Information Dribble Finish (PDF: "Process Information, Dribble & Shoot").
# 20 x 35 Yards (18 x 32 m) als Feld x 30-70, y 5-55: nicht maßstäblich (sonst zu schmal), wie die PDF-Skizze etwas breiter.
# Großes Tor mit neutralem Torwart oben, vier Minitore: eins in der Mitte oben (Öffnung nach unten), zwei links, drei rechts,
# vier unten. Vier Hütchen als Raute um den Spieler. Abweichungen: Im Original vier Hütchenfarben (rot, gelb, weiß, blau)
# und Ansage "Farbe + Tornummer" (z. B. "White 2"). Erlaubt sind nur orange/neon, deshalb ruft der Trainer die Lage des
# Hütchens (vorn, links, rechts, hinten) plus Tornummer. Im Original zwei Trainer (einer ruft "großes Tor" von rechts),
# hier genau einer links unten, der ruft und passt. Spieler = Spieler neun.
# Sichtkegel aus dem Text: "Quick reactions to drive towards goal & head up before finishing" -> Steigerung (großes Tor):
# vor dem Schuss Blick zum Torwart. Im Video selbst ist kein Kegel eingezeichnet.
# Fassungen: Coaching-Punkt "erster Kontakt Richtung Hütchen" (Ton 0:04-0:12, "control in the cone's direction"), Steigerung
# "großes Tor" (Text/Ton: "the coach will call for a finish in the big goals every few calls").
T = P("T", "c", 36, 50, "T")
K = P("k", "t", 50, 9, "TW")
POS = {"n9": (50, 38)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [K, T]
ERSATZ = [B("s1", 33, 52.5), B("s2", 31.5, 52.5)]
TR = [36.6, 50.6]
GOALS = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 22, "side": "top"},
         {"x": 30, "y": 44, "side": "left"}, {"x": 70, "y": 44, "side": "right"}, {"x": 50, "y": 55, "side": "bottom"}]
CONES = [C(50, 32), C(42, 38), C(58, 38), C(50, 44)]

u = {"title": "Ansage hören, dribbeln, treffen", "code": "UE-288", "kind": "Übungsform",
 "focuses": ["Dribbling", "Torschuss", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 2, "players_max": 3,
 "field_size": "18 x 32 m",
 "description": "Einzeltraining für schnelles Reagieren, Dribbeln und Abschließen. Der Trainer ruft ein Hütchen und eine Tornummer, zum Beispiel: rechts, zwei. Spieler neun dribbelt um dieses Hütchen und schießt ins richtige Minitor. Ab und zu ruft der Trainer: großes Tor, dann geht es aufs große Tor gegen den Torwart.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 32 Metern. Oben ein großes Tor mit Torwart. Vier Minitore mit Nummern: eins in der Mitte, zwei links, drei rechts, vier unten. In der Mitte vier Hütchen als Raute.",
  "Verteilen: Spieler neun steht in der Mitte der Raute. Der Trainer steht links unten mit vielen Bällen.",
  "Ablauf: Der Trainer ruft ein Hütchen und eine Tornummer und passt. Spieler neun dribbelt um das Hütchen und schießt ins genannte Minitor. Ruft der Trainer großes Tor, dribbelt er nach vorn und schließt gegen den Torwart ab.",
  "Wechsel: Nach jedem Schuss schnell zurück in die Mitte. Nach einer festen Zeit Pause und Bälle einsammeln. Sind zwei Spieler da, wechseln sie sich ab."],
 "organisation_show": ORG,
 "coaching_points": ["Genau hinhören und schnell reagieren", "Kurze, schnelle Kontakte um das Hütchen", "Genau und ruhig ins Minitor schießen", "Vor dem Schuss aufs große Tor den Kopf heben"],
 "materials": ["4 Hütchen", "4 Minitore", "1 großes Tor", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Ansage hören, dribbeln, treffen. Spieler neun hört auf den Trainer, dribbelt um das richtige Hütchen und trifft ins richtige Tor.",
 "board": {"lines": [rect(30, 5, 40, 50)], "goals": GOALS, "cones": CONES, "players": sp(), "balls": [B("b1", *TR)] + ERSATZ,
  "steps": [
   S("Ansage", "Der Trainer ruft: rechts, zwei! Das heißt: um das rechte Hütchen und dann ins Tor zwei links. Dabei passt er zu Spieler neun.",
     ps("b1", [50.6, 38.6])),
   S("Um das Hütchen", "Spieler neun dribbelt mit kurzen, schnellen Kontakten um das rechte Hütchen herum.",
     dr("n9", "b1", [55, 34.5]), dr("n9", "b1", [61.5, 35], after=True), dr("n9", "b1", [61.5, 41], after=True), dr("n9", "b1", [56, 41.5], after=True)),
   S("Ins Tor zwei", "Dann dribbelt er quer durch die Raute und schießt genau ins Tor zwei auf der linken Seite.",
     dr("n9", "b1", [50, 38.5]), dr("n9", "b1", [45, 41.5], after=True), ps("b1", [30.5, 44.5], after=True)),
   S("Zurück in die Mitte", "Der Ball ist im richtigen Tor, das ist das Ziel. Spieler neun läuft schnell zurück in die Mitte, und der Trainer ruft die nächste Ansage.",
     mv("n9", [50, 38]))],
  "dims": dims(30, 70, 5, 55, "18 m", "32 m", rx=76)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt geht schon zum Hütchen.", "Erster Kontakt zum Hütchen",
    "Spieler neun hört die Ansage, bevor der Ball bei ihm ist. Mit dem ersten Kontakt nimmt er den Ball gleich in Richtung des genannten Hütchens mit. Auch wenn er müde wird, bleibt er konzentriert und wählt das richtige Tor.",
    sp(), [B("b1", *TR)] + ERSATZ,
    [S("Hinhören", "Der Trainer ruft: hinten, drei! Spieler neun weiß sofort: um das hintere Hütchen und dann ins Tor drei rechts.",
       ps("b1", [50.6, 38.6])),
     S("Erster Kontakt", "Schon der erste Kontakt geht nach hinten zum Hütchen. Dann dribbelt er eng darum herum.",
       dr("n9", "b1", [46, 43.5]), dr("n9", "b1", [47.5, 48.5], after=True), dr("n9", "b1", [53, 48], after=True)),
     S("Ins Tor drei", "Jetzt schießt er ruhig und genau ins Tor drei, das ist das Ziel. Dann zurück in die Mitte.",
       ps("b1", [69.5, 44.5]), mv("n9", [50, 38], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft großes Tor.", "Aufs große Tor",
    "Ab und zu ruft der Trainer: großes Tor! Dann nimmt Spieler neun den Ball nach vorn mit, dribbelt schnell am Minitor eins vorbei und hebt vor dem Schuss den Kopf. Er sieht, wo der Torwart steht, und schießt in die freie Ecke.",
    sp(), [B("b1", *TR)] + ERSATZ,
    [S("Großes Tor", "Der Trainer ruft: großes Tor! Und er passt zu Spieler neun.",
       ps("b1", [50.6, 38.6])),
     S("Schnell nach vorn", "Spieler neun nimmt den Ball nach vorn mit und dribbelt schnell links am Minitor eins vorbei.",
       dr("n9", "b1", [44, 31]), dr("n9", "b1", [41, 20], after=True)),
     S("Kopf hoch und schießen", "Vor dem Schuss hebt er den Kopf und schaut zum Torwart. Dann schießt er flach in die freie Ecke, das ist das Ziel. Danach läuft er zurück in die Mitte, und die nächste Ansage kommt.",
       bl("n9", [50, 9]), ps("b1", [45, 5.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
