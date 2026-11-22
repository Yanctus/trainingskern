import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-8 (U12-U14, Torwarttraining): Goalkeeper Reactions Quick Feet Shot Stopping (im PDF "Quick Reactions and Shot Stopping
# GK-P8"). Strafraum 18 x 45 Yards, gedreht: im PDF liegt das Tor links, hier oben (wie im Video). Feld x 14-86, y 5-37
# (41 x 16 m), Torraum x 34-66, y 5-15.7. Quadrat aus vier Hütchen im Torraum, Stange zwischen Quadrat und Tor etwas rechts
# von der Mitte (wie im Video). Jugendtor mit Torwart k1.
# Statt zwei Trainern und dem zweiten Torwart als Zuspieler: ein Trainer wirft Tennisbälle und Fußbälle (Mitte), Spieler sieben
# (Team Neon) schießt von rechts an den nahen Pfosten (im Original der zweite Trainer), Spieler acht (Team Neon) schießt von
# links den zweiten Ball (im Original der zweite Torwart, Nr. 13). Der zweite Torwart k2 wartet neben dem Tor und wechselt nach
# jeder zweiten Runde (Regel: Schützen sind Trainer oder Spieler von Team Neon). Schützen etwas höher gesetzt als im Video
# (Schusswege frei von den Hütchen).
# Keine Wertung im Original: reine Technikübung, Ziel statt Punkte. Fassungen = die zwei Key Coaching Points aus PDF Seite 2.
# Sichtkegel aus dem Text ("before setting for the next ball" = Grundstellung): nach dem Ablegen stellt sich der Torwart
# wieder bereit und schaut zum Trainer. Im Video kein Kegel eingezeichnet; Richtung aus dem Sinn.
T = P("T", "c", 50, 30, "T")
POS = {"k1": (50, 13), "n7": (75, 11), "n8": (25, 11), "k2": (36, 2.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else "a", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 33.5), B("s2", 46.4, 33.5)]
def baelle(**k):
    d = {"t1": (50.6, 30.6), "b1": (48.4, 31.6), "b7": (75.6, 11.6), "b8": (25.6, 11.6)}
    d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(14, 5, 72, 32), rect(34, 5, 32, 10.7)]
CONES = [C(44.5, 10.5), C(55.5, 10.5), C(44.5, 15.5), C(55.5, 15.5), C(50.8, 7.5, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Tennisbälle, dann zwei Paraden", "code": "UE-266", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 3, "players_max": 4, "field_size": "41 x 16 m",
 "description": "Torwarttraining für schnelle Reaktionen und schnelle Füße. Der Torwart steht in einem Quadrat aus Hütchen und fängt abwechselnd Tennisbälle und Fußbälle vom Trainer. Jeden Tennisball legt er auf ein Hütchen, jeden Fußball wirft er zurück. Liegen alle vier Tennisbälle, hält er einen Schuss am nahen Pfosten, läuft um die Stange und hält gleich den zweiten Schuss.",
 "organisation": ["Aufbauen: Im Strafraum vor einem Jugendtor. Im Torraum steht ein Quadrat aus vier Hütchen, zwischen Quadrat und Tor etwas rechts von der Mitte eine Stange.",
  "Verteilen: Der Torwart steht im Quadrat, der Trainer davor mit vier Tennisbällen und Fußbällen. Spieler sieben steht rechts, Spieler acht links, beide mit Bällen. Der zweite Torwart wartet neben dem Tor.",
  "Ablauf: Der Trainer wirft abwechselnd einen Tennisball und einen Fußball. Tennisbälle legt der Torwart auf ein Hütchen, Fußbälle wirft er zurück. Liegen alle vier Tennisbälle, schießt Spieler sieben an den nahen Pfosten. Der Torwart steht schnell auf, läuft um die Stange und hält den Schuss von Spieler acht.",
  "Wechsel: Nach jeder zweiten Runde tauschen die beiden Torhüter."],
 "organisation_show": ORG,
 "coaching_points": ["Voll konzentriert bleiben: Tennisball sicher fangen und aufs Hütchen legen", "Fußbälle sicher fangen und genau zum Trainer zurückwerfen", "Am nahen Pfosten sauber abtauchen und mit der richtigen Hand zum Ball", "Schnell aufstehen und mit schnellen Füßen quer durchs Tor"],
 "materials": ["1 Jugendtor", "4 Hütchen", "1 Stange", "4 Tennisbälle", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Tennisbälle, dann zwei Paraden. Der Torwart fängt Tennisbälle und legt sie auf Hütchen. Danach hält er zwei Schüsse direkt hintereinander.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": baelle(),
  "steps": [
   S("Tennisball fangen", "Der Torwart steht im Quadrat. Der Trainer wirft ihm einen Tennisball zu, und der Torwart fängt ihn sicher.",
     ps("t1", [50.6, 13.6])),
   S("Aufs Hütchen legen", "Er geht zu einem Hütchen und legt den Tennisball darauf. Dann geht er zurück in die Mitte, stellt sich bereit und schaut zum Trainer.",
     mv("k1", [47.6, 13.4], ball="t1"), ps("t1", [45.4, 11.4], after=True), mv("k1", [50, 13], after=True), bl("k1", [50, 28], after=True)),
   S("Fußball zurückwerfen", "Jeder zweite Wurf ist ein Fußball. Den fängt der Torwart und wirft ihn genau zum Trainer zurück. So geht es weiter, bis alle vier Tennisbälle auf den Hütchen liegen.",
     ps("b1", [50.6, 13.6]), ps("b1", [50.6, 29.4], after=True)),
   S("Nahen Pfosten halten", "Jetzt schießt Spieler sieben flach an den nahen Pfosten. Der Torwart taucht schnell ab und hält den Ball.",
     ps("b7", [55.1, 7.1]), mv("k1", [54.5, 6.5], delay=0.3)),
   S("Um die Stange", "Der Torwart steht sofort auf und läuft um die Stange herum, schnell quer durchs Tor zum anderen Pfosten.",
     mv("k1", [51, 11]), mv("k1", [45.5, 6.5], after=True)),
   S("Zweiter Ball gehalten", "Spieler acht schießt auf den anderen Pfosten, und der Torwart hält auch diesen Ball. Die Runde ist vorbei. Nach jeder zweiten Runde ist der zweite Torwart dran.",
     ps("b8", [46.1, 7.1]))],
  "dims": dims(14, 86, 5, 37, "41 m", "16 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit den Fingerspitzen in die Ecke.", "Fingerspitzen an den Pfosten",
    "Nach dem ersten Ball zählt jeder Schritt. Der Torwart läuft mit kleinen, schnellen Schritten um die Stange und quer durchs Tor. Kommt der zweite Schuss genau in die Ecke, streckt er sich und lenkt den Ball mit den Fingerspitzen am Pfosten vorbei.",
    sp(k1=(54.5, 6.5)), baelle(b7=(55.1, 7.1)),
    [S("Schnelle Füße", "Der Torwart hat den ersten Ball gehalten. Er steht sofort auf und läuft mit kleinen, schnellen Schritten um die Stange.",
       mv("k1", [51, 11]), mv("k1", [46.5, 7.5], after=True)),
     S("Fingerspitzen", "Spieler acht schießt genau in die linke Ecke. Der Torwart streckt sich und lenkt den Ball mit den Fingerspitzen am Pfosten vorbei.",
       ps("b8", [45, 5.8]), mv("k1", [44.5, 6.5], delay=0.2), ps("b8", [41, 2], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Flach festhalten, sofort wieder hoch.", "Festhalten und sofort hoch",
    "Den flachen Schuss am nahen Pfosten hält der Torwart mit beiden Händen fest und drückt den Ball an den Körper. So springt nichts zurück. Dann steht er ohne Pause auf, denn der zweite Schuss kommt sofort.",
    sp(), baelle(),
    [S("Flach festhalten", "Spieler sieben schießt flach an den nahen Pfosten. Der Torwart taucht ab, hält den Ball mit beiden Händen fest und drückt ihn an den Körper.",
       ps("b7", [55.1, 7.1]), mv("k1", [54.5, 6.5], delay=0.3)),
     S("Sofort hoch", "Ohne Pause steht er auf und läuft um die Stange zum anderen Pfosten. Dort hält er den Schuss von Spieler acht.",
       mv("k1", [51, 11]), mv("k1", [45.5, 6.5], after=True), ps("b8", [46.1, 7.1], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
