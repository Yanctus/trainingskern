import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-1 (GK-P1, U12-U14, Torwarttraining): Goalkeeper Quick Feet and Shot Stopping. 45 x 18 Yards = Strafraum, Feld x 10-90,
# y 5-55 (41 x 16 m), gedreht: im PDF liegt das Tor links, hier oben wie im Video. Torraum x 29-71, y 5-23, Jugendtor oben.
# Im Torraum wie im Video: zwei Hütchen nah am Tor (zum Antippen), eine Reihe aus drei Hütchen, darunter zwei Hütchen senkrecht,
# unter dem Torraum eine Minihürde. Grüner Torwart 1 -> Torwart k1, wartender Torwart 13 (im Video orange, rechts mit Bällen)
# -> zweiter Torwart k2. Zwei Trainer im Original: der untere mittlere bleibt der Trainer (Prallpass und erster Schuss), der
# linke untere wird Spieler sieben von Team Neon (Pass zum Abtauchen). Den zweiten Schuss gibt wie im Video der wartende
# Torwart von rechts. Danach tauschen die Torhüter (im Video läuft Torwart 1 zu den Bällen rechts, 13 beginnt).
# Sichtkegel: PDF "Quick reactions to jump up to face 2nd shot" -> der Torwart schaut nach der ersten Parade zum zweiten Torwart,
# bevor der zweite Schuss kommt. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Fassungen: zwei Coaching-Punkte (Abtauchen richtig, schnell quer durchs Tor), im Original gibt es keine Steigerung.
T = P("T", "c", 62, 48, "T")
POS = {"k1": (60, 19), "k2": (85, 17), "n7": (22, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else "a", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 65.6, 50.5), B("s2", 58.4, 50.5)]
LINES = [rect(10, 5, 80, 50), rect(29, 5, 42, 18)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
KEGEL = [C(39, 7.5), C(43, 10.5), C(48, 14), C(53.5, 14), C(59, 14), C(48, 19.5), C(48, 26), C(48, 32, shape="huerde_ou")]

u = {"title": "Parcours und zwei Paraden", "code": "UE-263", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 3, "field_size": "41 x 16 m (Strafraum)",
 "description": "Der Torwart läuft einen kurzen Parcours im Torraum: Prallpass mit dem Trainer, schnelle Füße durch die Hütchen und ein Sprung über die Hürde. Dann taucht er auf einen flachen Ball ab und rollt ihn zurück. Er läuft rückwärts zu den Hütchen am Tor und muss quer durchs Tor zwei Schüsse halten. Danach tauschen die beiden Torhüter.",
 "organisation": ["Aufbauen: Ein Strafraum mit Jugendtor. Im Torraum stehen zwei Hütchen nah am Tor, eine Reihe aus drei Hütchen und darunter zwei Hütchen untereinander. Unter dem Torraum liegt eine Minihürde.",
  "Verteilen: Ein Torwart startet rechts neben den Hütchen, der zweite Torwart wartet rechts mit Bällen. Der Trainer steht unten in der Mitte, Spieler sieben unten links, beide mit Bällen.",
  "Ablauf: Prallpass mit dem Trainer, schnelle Füße durch die Hütchen, Sprung über die Hürde. Abtauchen auf den Pass von Spieler sieben und zurückrollen. Rückwärts zu den zwei Hütchen am Tor, quer zum Schuss des Trainers, dann sofort aufstehen zum zweiten Schuss.",
  "Wechsel: Nach jedem Durchgang tauschen die Torhüter. Der erste Torwart holt die Bälle und gibt jetzt den zweiten Schuss."],
 "organisation_show": ORG,
 "coaching_points": ["Mit schnellen, kurzen Schritten quer durchs Tor", "Nach der Parade sofort aufstehen und zum Ball drehen", "Beim Abtauchen den Ball sicher an den Körper ziehen", "Den Parcours mit vollem Tempo laufen und genau passen"],
 "materials": ["1 Jugendtor", "7 Hütchen", "1 Minihürde", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Parcours und zwei Paraden. Der Torwart läuft einen Parcours, taucht ab und hält danach zwei Schüsse.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(),
  "balls": [B("b1", 62.6, 48.6), B("b2", 22.6, 46.6), B("b3", 85.6, 17.6)] + ERSATZ,
  "steps": [
   S("Prallpass", "Der Trainer passt zum Torwart, und der Torwart spielt direkt zurück.",
     ps("b1", [60.6, 19.6]), ps("b1", [62.6, 48.6], after=True)),
   S("Schnelle Füße und Sprung", "Jetzt schnelle Füße: Der Torwart läuft im Zickzack durch die Reihe, dann links und rechts um die zwei Hütchen und springt über die Hürde.",
     mv("k1", [63.5, 15]), mv("k1", [59.5, 10.5], after=True), mv("k1", [53.5, 17], after=True), mv("k1", [48, 10.8], after=True),
     mv("k1", [44.5, 16], after=True), mv("k1", [44.5, 19.5], after=True), mv("k1", [51.5, 26], after=True), mv("k1", [48, 29.5], after=True), mv("k1", [48, 35], after=True)),
   S("Abtauchen und zurückrollen", "Spieler sieben spielt flach zur Seite. Der Torwart taucht auf den Ball ab, steht schnell auf und rollt ihn zurück zu Spieler sieben.",
     ps("b2", [38.6, 36.6]), mv("k1", [38, 36], delay=0.3), ps("b2", [22.6, 46.6], after=True)),
   S("Rückwärts und quer: Parade", "Der Torwart läuft rückwärts und tippt die zwei Hütchen am Tor an. Dann schnell quer durchs Tor, der Trainer schießt, und der Torwart hält den Ball.",
     mv("k1", [41.5, 12.5]), mv("k1", [38, 9], after=True), mv("k1", [54, 8.5], after=True), ps("b1", [54.6, 9.1], delay=1.6)),
   S("Zweiter Schuss, dann Wechsel", "Sofort steht der Torwart auf und schaut zum zweiten Torwart. Der schießt aufs Tor, und der Torwart hält auch diesen Ball. Damit ist die Runde vorbei: Jetzt tauschen die Torhüter, und der zweite Torwart läuft den Parcours.",
     mv("k1", [53, 10]), bl("k1", [70, 19], after=True), ps("b3", [53.6, 10.6], after=True))],
  "dims": dims(10, 90, 5, 55, "41 m", "16 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Richtig abtauchen.", "Richtig abtauchen",
    "Beim Abtauchen fällt der Torwart seitlich auf den Ball. Die Hände sind zuerst am Ball, dann zieht er ihn fest an den Körper. Danach steht er sofort wieder auf und rollt den Ball genau zurück.",
    sp(k1=(48, 35)), [B("b2", 22.6, 46.6), B("b1", 62.6, 48.6)] + ERSATZ,
    [S("Seitlich abtauchen", "Spieler sieben spielt flach zur Seite. Der Torwart macht einen kleinen Schritt und fällt seitlich auf den Ball, die Hände zuerst.",
       ps("b2", [38.6, 36.6]), mv("k1", [38, 36], delay=0.3)),
     S("Aufstehen und zurückrollen", "Er zieht den Ball fest an den Körper, steht sofort auf und rollt ihn genau zurück zu Spieler sieben.",
       ps("b2", [22.6, 46.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell quer durchs Tor und sofort wieder bereit.", "Quer durchs Tor",
    "Vom Hütchen am Tor geht es mit kurzen, schnellen Schritten quer durchs Tor. Nach der ersten Parade steht der Torwart sofort auf, dreht sich zum Ball und ist für den zweiten Schuss bereit.",
    sp(k1=(38, 9)), [B("b1", 62.6, 48.6), B("b3", 85.6, 17.6)] + ERSATZ,
    [S("Kurze, schnelle Schritte", "Der Torwart läuft mit kurzen, schnellen Schritten quer durchs Tor. Der Trainer schießt, und der Torwart hält den Ball.",
       mv("k1", [54, 8.5]), ps("b1", [54.6, 9.1], delay=0.8)),
     S("Sofort wieder bereit", "Sofort aufstehen und zum Ball schauen. Der zweite Torwart schießt, und der Torwart hält auch diesen Ball.",
       mv("k1", [53, 10]), bl("k1", [70, 19], after=True), ps("b3", [53.6, 10.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
