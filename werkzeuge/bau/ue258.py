import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P13 (U12-U14, Torwarttraining): Goalkeeper Handling, Speed and Reactions ("Goalkeeper Handling Speed and Reactions GK-13").
# 18 x 45 Yards (Strafraum), gedreht: im PDF liegt das Tor links, hier oben (wie im Video). Feld x 16-84, y 5-55 (41 x 16 m, nicht
# maßstäblich), Torraum x 32-68, y 5-23. Zweites Jugendtor quer links am Torraum mit Öffnung nach rechts (im PDF unten am Torraum).
# Zwei Torhüter neutral: k1 (grün 1, arbeitet), k2 (gelb 13, schießt aufs zweite Tor, steht rechts neben dem Torraum), Nummern
# weggelassen. Der Trainer schießt den ersten Ball aufs erste Tor. Keine Wertung (Technikübung, Ziel statt Punkte).
# Nicht dieselbe Übung wie GK-5 (UE-257, Tennisbälle, Slalom, Minitore), trotz fast gleichem Namen.
# Sichtkegel aus Text und Ton ("get set", "assess striker's body shape"): k1 schaut vor dem ersten Schuss zum Trainer und vor dem
# zweiten Schuss zum zweiten Torwart. Im Video ist kein Kegel eingezeichnet (nur ein Kreis um den Torwart und Pfeile fürs Abwehren
# zur Seite), Richtung aus dem Sinn.
T = P("T", "c", 53, 44, "T")
POS = {"k1": (50, 8), "k2": (72, 16)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 57.2, 45.5), B("s2", 49, 46.5)]
def baelle(b1=(53.6, 44.6)):
    return [B("b1", *b1), B("b2", 72.6, 16.6), B("s3", 76.5, 11), B("s4", 79, 14)] + ERSATZ
LINES = [rect(16, 5, 68, 50), rect(32, 5, 36, 18)]
CONES = [C(50, 22), C(30, 41)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 30, "y": 16, "side": "left", "size": "jugend"}]

u = {"title": "Antippen, zwei Tore halten", "code": "UE-258", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 2,
 "field_size": "41 x 16 m",
 "description": "Ein Torwart arbeitet, der zweite schießt. Der Torwart tippt das Hütchen vor dem Tor an, sprintet zurück auf die Torlinie und hält den Schuss des Trainers. Dann sprintet er zum zweiten Hütchen, tippt es an und hält vor dem zweiten Tor den Schuss des zweiten Torwarts. Danach tauschen die beiden Torhüter.",
 "organisation": ["Aufbauen: Im Strafraum ein Jugendtor auf der Torlinie und ein zweites Jugendtor quer dazu links am Torraum. Ein Hütchen vor dem ersten Tor, ein zweites schräg vorn links.",
  "Verteilen: Der erste Torwart steht im ersten Tor. Der zweite Torwart steht rechts neben dem Torraum mit Bällen, der Trainer vorn in der Mitte mit Bällen.",
  "Ablauf: Hütchen antippen, zurück auf die Linie und den Schuss vom Trainer halten. Dann zum zweiten Hütchen, antippen und vor dem zweiten Tor den Schuss vom zweiten Torwart halten.",
  "Wechsel: Nach beiden Paraden tauschen die Torhüter. Ist ein Ball nicht festzuhalten, wird er zur Seite oder über das Tor abgewehrt."],
 "organisation_show": ORG,
 "coaching_points": ["Den ersten Ball gleich sicher fangen", "Kurze, schnelle Schritte und früh bereit stehen", "Schnell hinüber und lang strecken, auch mit ausgestrecktem Arm", "Nicht zu haltende Bälle mit festen Händen zur Seite abwehren"],
 "materials": ["2 Jugendtore", "2 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Antippen, zwei Tore halten. Der Torwart tippt zwei Hütchen an und hält danach jedes Mal einen Schuss, erst im ersten Tor und dann im zweiten.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Hütchen antippen", "Der Torwart sprintet mit kurzen, schnellen Schritten zum Hütchen, tippt es an und läuft schnell zurück auf die Torlinie. Dort steht er bereit und schaut zum Trainer.",
     mv("k1", [50, 20]), mv("k1", [50, 9], after=True), bl("k1", [52, 27], after=True)),
   S("Erster Schuss", "Der Trainer schießt aufs Tor. Der Torwart macht einen schnellen Schritt zur Seite und fängt den Ball sicher.",
     ps("b1", [55.6, 9.6]), mv("k1", [55, 9], delay=0.2)),
   S("Zum zweiten Hütchen", "Jetzt sprintet er schräg nach vorn zum zweiten Hütchen und tippt es an.",
     mv("k1", [31, 39])),
   S("Zweite Parade und Wechsel", "Dann schnell hinüber vor das zweite Tor. Er stellt sich hin und schaut, wie der zweite Torwart zum Ball steht. Der schießt, und der Torwart hält den Ball. Damit ist die Runde vorbei, und die beiden Torhüter tauschen die Rollen.",
     mv("k1", [34, 18]), bl("k1", [52, 17], after=True), ps("b2", [34.6, 14.6], after=True), mv("k1", [34, 14], delay=0.2))],
  "dims": dims(16, 84, 5, 55, "41 m", "16 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnell hinüber und lang strecken.", "Schnell hinüber, lang strecken",
    "Nach dem zweiten Hütchen zählt jeder Schritt. Der Torwart sprintet mit schnellen Schritten vor das zweite Tor und steht rechtzeitig bereit. Geht der Schuss weit weg vom Körper, streckt er sich lang und erreicht den Ball mit ausgestrecktem Arm.",
    sp(k1=(31, 39)), baelle(b1=(55.6, 9.6)),
    [S("Schnell hinüber", "Der Torwart sprintet mit schnellen Schritten vor das zweite Tor und steht rechtzeitig bereit. Er schaut, wie der Schütze zum Ball steht.",
       mv("k1", [34, 18]), bl("k1", [52, 17], after=True)),
     S("Lang strecken", "Der Schuss geht weit weg vom Körper in die Ecke. Der Torwart stößt sich ab, streckt sich lang und erreicht den Ball mit ausgestrecktem Arm.",
       ps("b2", [34.6, 11.6]), mv("k1", [34, 11], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Zur Seite abwehren.", "Zur Seite abwehren",
    "Nicht jeder Schuss lässt sich festhalten. Dann drückt der Torwart den Ball mit festen Händen zur Seite neben das Tor oder über die Latte. So kann kein Stürmer den Abpraller verwerten.",
    sp(k1=(50, 9)), baelle(),
    [S("Bereit stehen", "Der Torwart steht bereit auf der Torlinie und schaut, wie der Trainer zum Ball steht.",
       bl("k1", [52, 27])),
     S("Zur Seite abwehren", "Der Trainer schießt hart. Der Torwart kann den Ball nicht festhalten, also drückt er ihn mit festen Händen zur Seite neben das Tor. So bekommt kein Stürmer einen Abpraller.",
       ps("b1", [56.6, 9.6]), mv("k1", [56, 9], delay=0.2), ps("b1", [65, 2.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
