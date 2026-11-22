import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-9 (U12-U14, Torwarttraining): Goalkeeper Footwork Handling (im PDF "Goalkeeper Movement and Handling GK-P9").
# Strafraum 45 x 18 Yards = Feld x 5-95, y 5-42 (41 x 16 m), Torraum x 30-70, y 5-17. Gedreht: im PDF liegt das Tor links,
# hier oben (wie im Video). Halbkreis weggelassen. Zwei Hütchenreihen zu je vier Hütchen eine Fußlänge vor der Torlinie,
# in der Mitte eine Markierung (neon) auf der Torlinie. Grüner Torwart 1 -> k1 ("der erste Torwart"), gelber 13 -> k2
# ("der zweite Torwart"). Ein Trainer statt zwei: der zweite Trainer (im Video links am Torraum, ohne Aufgabe) ist weggelassen.
# Schnelle Füße durch die Hütchen als Slalom gezeichnet (das Original sagt "type can vary each time").
# Keine Wertung im Original: Ziel statt Punkte (jeden Ball sicher fangen).
# Sichtkegel aus dem Text ("set and catch the volleyed shot", Steigerung "turn quickly to save the volley"): Der Torwart stellt
# sich und schaut zum Trainer, bevor der Volley kommt. Im Video kein Kegel eingezeichnet; Richtung aus dem Sinn.
T = P("T", "c", 50, 27, "T")
POS = {"k1": (73, 10), "k2": (83, 10)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 28), B("s2", 54, 31)]
BAELLE = [B("b1", 50.6, 27.6)] + ERSATZ
LINES = [rect(5, 5, 90, 37), rect(30, 5, 40, 12)]
CONES = [C(x, 10) for x in (32, 36, 40, 44, 56, 60, 64, 68)] + [C(50, 6, "neon"), C(44, 25)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
# Slalom durch die rechte Reihe bis zur Mitte (vor dem Trainer)
def slalom(who="k1"):
    return [mv(who, [68, 13]), mv(who, [64, 7], after=True), mv(who, [60, 13], after=True), mv(who, [56, 7], after=True),
            mv(who, [50, 10], after=True)]

u = {"title": "Hütchenreihe und Volley fangen", "code": "UE-254", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 3,
 "field_size": "41 x 16 m",
 "description": "Zwei Torhüter arbeiten im Torraum abwechselnd an schnellen Füßen und sicherem Fangen. Der Torwart läuft mit kleinen, schnellen Schritten durch eine Hütchenreihe vor der Torlinie. In der Mitte stellt er sich und fängt einen Volley vom Trainer. Er wirft den Ball zurück und geht ruhig zur anderen Hütchenreihe, während der zweite Torwart startet.",
 "organisation": ["Aufbauen: Ein Jugendtor mit Torraum. Links und rechts der Mitte liegen je vier Hütchen in einer Reihe kurz vor der Torlinie, in der Mitte eine Markierung.",
  "Verteilen: Zwei Torhüter stehen rechts neben der rechten Hütchenreihe. Der Trainer steht etwa acht Meter vor dem Tor mit vielen Bällen.",
  "Ablauf: Der erste Torwart läuft mit schnellen Füßen durch die Hütchen bis zur Mitte, stellt sich und fängt den Volley vom Trainer. Dann wirft er den Ball zurück und geht ruhig zur linken Reihe.",
  "Wechsel: Danach startet der zweite Torwart. Haben beide die rechte Reihe geschafft, laufen sie von links durch die andere Reihe zur Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Kleine, schnelle Schritte durch die Hütchen, ohne eins zu berühren", "In der Mitte kurz stellen, auf die Zehenspitzen und den Ball fest fangen", "Auf dem Weg zur nächsten Reihe ruhig gehen und gut durchatmen", "Den Ball genau und flach zum Trainer zurückwerfen"],
 "materials": ["1 Jugendtor", "10 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Hütchenreihe und Volley fangen. Zwei Torhüter laufen mit schnellen Füßen durch die Hütchen und fangen dann einen Volley vom Trainer.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Schnelle Füße", "Der erste Torwart läuft mit kleinen, schnellen Schritten durch die rechte Hütchenreihe, immer abwechselnd vor und hinter den Hütchen. So kommt er bis zur Mitte.",
     *slalom()),
   S("Stellen und fangen", "In der Mitte stellt er sich, geht auf die Zehenspitzen und schaut zum Trainer. Der Trainer schießt ihm einen Volley zu, und der Torwart fängt den Ball fest mit beiden Händen.",
     bl("k1", [50, 26]), ps("b1", [50.6, 10.6], after=True)),
   S("Zurückwerfen", "Der Torwart wirft den Ball genau zum Trainer zurück.",
     ps("b1", [50.6, 27.6])),
   S("Zur nächsten Reihe", "Dann geht der erste Torwart ruhig vor der linken Reihe entlang nach links und atmet durch. Jetzt ist der zweite Torwart dran. Ziel ist, jeden Volley sicher zu fangen. Haben beide die rechte Reihe geschafft, geht es von links.",
     mv("k1", [44, 15]), mv("k1", [28, 15], after=True), mv("k1", [27, 10], after=True), mv("k2", [73, 10]),
     mv("k2", [68, 13], after=True))],
  "dims": dims(5, 95, 5, 42, "41 m", "16 m", rx=98)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Sauber und schnell durch die Hütchen.", "Sauber und schnell",
    "Der Torwart macht kleine, schnelle Schritte und bleibt dabei leicht in den Knien. Er berührt kein Hütchen und wird zum Ende nicht langsamer. Nur wer sauber und schnell läuft, steht in der Mitte rechtzeitig bereit.",
    sp(), BAELLE,
    [S("Kleine Schritte", "Der erste Torwart läuft durch die Hütchen. Kleine, schnelle Schritte, leicht in den Knien, und kein Hütchen wird berührt.",
       *slalom()),
     S("Bereit: fangen", "In der Mitte steht er sofort bereit und schaut zum Trainer. Der Volley kommt, und er fängt ihn sicher.",
       bl("k1", [50, 26]), ps("b1", [50.6, 10.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Rückwärts durch die Hütchen und schnell drehen.", "Rückwärts und drehen",
    "Jetzt läuft der Torwart rückwärts durch die Hütchen, mit dem Rücken zur Mitte. In der Mitte dreht er sich schnell um und fängt den Volley. Wer sich schnell dreht, hat mehr Zeit für den Ball.",
    sp(), BAELLE,
    [S("Rückwärts durch", "Der erste Torwart läuft rückwärts durch die Hütchenreihe bis zur Mitte. Er macht kleine, schnelle Schritte und schaut dabei kurz über die Schulter.",
       *slalom()),
     S("Drehen und fangen", "In der Mitte dreht er sich schnell zum Trainer um und stellt sich. Sofort kommt der Volley, und er fängt ihn fest.",
       bl("k1", [50, 26]), ps("b1", [50.6, 10.6], after=True)),
     S("Zurückwerfen", "Er wirft den Ball genau zum Trainer zurück und geht ruhig zur linken Reihe. Dann ist der zweite Torwart dran.",
       ps("b1", [50.6, 27.6]), mv("k1", [44, 15], after=True), mv("k1", [28, 15], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
