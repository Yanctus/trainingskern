import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-44 (U15-U17, Woche 26 Phase 4): Pass and Move Activation, Warm Up. 25 x 25 Yards = 23 x 23 m (nach der Meter-Regel 25 x 25 m).
# Ausrichtung wie im PDF (Start unten, der Ball läuft im Uhrzeigersinn). Feld x 25-75, y 5-55. Keine Dublette: UE-153 (WU-43),
# UE-165 (WU-41), UE-318 (WU-49), UE-344 (WU-50), UE-346 (WU-48) haben andere Stationen und keine Hürde vor einer Mittelzone.
# Alle Pink -> Team Neon, im PDF ohne Nummern: Start 6, nächster Starter 2 (Hütchen „1st station“ rechts daneben), links 7,
# oben 9, rechts 11. Dummys als Stangen, die Hürde als Minihürde (Laufrichtung von unten nach oben), Mittelzone aus vier Hütchen
# (im PDF rot, hier orange). Spieler neun etwas nach links gerückt, damit sein Pass in die Mitte nicht am Hütchen vorbeischrammt.
# Ein Trainer statt zwei, links unten neben dem Feld (wie im Video der Steigerung mit Minitor).
# Ablauf nach PDF und Video 0:12-0:28. Das Weiterrücken im Uhrzeigersinn steht nur im Text (Laufwege kreuzen sonst Dummys und Zone).
# Fassungen: PDF Progression 1 (Doppelpass am Start, Video 0:30-0:50: Spieler sieben legt in den Lauf, direkter Pass nach oben)
# und Progression 2 (Minitor unten rechts, Doppelpass vor dem Abschluss, Video 0:55-1:10). Annahme: In Progression 2 stehen die
# Spieler so, wie sie nach dem Steilpass stehen; das Minitor steht wie im Video unten rechts an der Grundlinie.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft). Der Kegel bei Spieler sieben gehört zum Annehmen und Aufdrehen
# (KCP „Open body shape - receive on the back foot to turn out quickly“, im Video „Back foot to turn out quickly“), mit Drehpfeil.
T = P("T", "c", 17, 47, "T")
ERSATZ = [B("s1", 20.6, 50.5), B("s2", 17, 51.5)]
POS = {"n6": (47, 51.6), "n2": (56, 53), "n7": (29.3, 31.7), "n9": (44.5, 7), "n11": (72.8, 31.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
START, LINKS, OBEN = [47, 51.6], [29.3, 31.7], [44.5, 7]
CONES = [C(49.7, 8.2), C(49.6, 52.2), C(45.5, 25.5), C(54.5, 25.5), C(45.5, 34.5), C(54.5, 34.5),
         C(33.6, 29.2, shape="stange"), C(67.8, 29.2, shape="stange"), C(50, 41, shape="huerde_ou")]
LINES = [rect(25, 5, 50, 50)]
DIMS = dims(25, 75, 5, 55, "25 m", "25 m", rx=83)
def huerde(delay=0.3, von=None):
    return ([mv("n6", von, delay=delay), mv("n6", [50, 45], after=True)] if von else [mv("n6", [50, 45], delay=delay)]) \
        + [mv("n6", [50, 30], after=True)]

u = {"title": "Passrunde über die Hürde", "code": "UE-373", "kind": "Übungsform",
 "focuses": ["Passspiel", "Erwärmung", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 5, "players_max": 8,
 "field_size": "25 x 25 m",
 "description": "Ein Aufwärmen mit Pässen und Laufwegen in einem Quadrat mit zwei Dummys, einer Hürde und einer kleinen Zone in der Mitte. Der Ball läuft vom Start nach außen, nach vorn, in die Zone und mit einem Steilpass auf die andere Seite. Wer passt, läuft sofort weiter, der Starter springt über die Hürde in die Zone. Nach jeder Runde rücken alle eine Station weiter.",
 "organisation": ["Aufbauen: Ein Quadrat von 25 mal 25 Metern. Links und rechts steht je ein Dummy, in der Mitte eine kleine Zone aus vier Hütchen, davor eine Minihürde. Je ein Hütchen am Start und oben.",
  "Verteilen: Fünf Spieler: zwei am Start, je einer an den beiden Dummys und einer oben. Der Trainer steht mit Ersatzbällen links unten neben dem Feld.",
  "Ablauf: Pass nach außen, der nimmt um den Dummy mit und spielt nach vorn. Der Starter springt über die Hürde in die Zone und legt den Pass von oben nach außen ab. Dann kommt der Steilpass auf den Spieler am anderen Dummy, und der spielt zurück zum Start.",
  "Wechsel: Nach seinem Pass rückt jeder eine Station weiter, im Uhrzeigersinn. Der Nächste am Start beginnt die neue Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Pass mit dem richtigen Tempo, genau in den Fuß", "Offen stehen, mit dem hinteren Fuß annehmen und aufdrehen", "Schnell über die Hürde und rein in die Zone", "Erst weg vom Dummy, dann kurz und scharf entgegen"],
 "materials": ["6 Hütchen", "2 Dummys", "1 Minihürde", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passrunde über die Hürde. Ein Aufwärmen mit Ball. Jeder Pass, dann sofort laufen, einmal über die Hürde, und am Ende geht der Ball zurück zum Start.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 47.6, 52.2)] + ERSATZ,
  "steps": [
   S("Pass nach außen", "Spieler sechs beginnt am Start. Flacher Pass nach außen zu Spieler sieben am Dummy. Der steht offen und schaut zum Ball.",
     bl("n7", START), ps("b1", [29.9, 32.3], after=True)),
   S("Aufdrehen um den Dummy, Pass nach oben", "Spieler sieben nimmt mit dem hinteren Fuß an und dreht auf. Mit dem Ball geht er um den Dummy herum und spielt nach oben zu Spieler neun. Spieler sechs sprintet los und springt über die Hürde in die Zone.",
     bl("n7", OBEN, von=START, dauer=1.3), drehen("n7", OBEN, gegen=True, delay=0.4),
     dr("n7", "b1", [32.5, 34.5], after=True), dr("n7", "b1", [37, 33], after=True), ps("b1", [45.1, 7.6], after=True),
     *huerde(delay=0.6)),
   S("In die Zone, Ablage nach außen", "Spieler neun spielt in die Zone zu Spieler sechs und läuft gleich schräg nach außen. Spieler sechs legt mit einem Kontakt in seinen Lauf.",
     ps("b1", [50.6, 30.6]), mv("n9", [63, 27], delay=0.3), ps("b1", [63.6, 27.6], after=True)),
   S("Doppelte Bewegung, Steilpass", "Drüben geht Spieler elf erst weg vom Dummy, dann kommt er dahinter hervor. Genau da hinein spielt Spieler neun den Steilpass.",
     mv("n11", [72.8, 21]), mv("n11", [71.5, 32], after=True), mv("n11", [67, 43.5], after=True), ps("b1", [67.6, 44.1], after=True)),
   S("Zurück zum Start, alle rücken weiter", "Spieler elf spielt zurück zum Start, zu Spieler zwei. Dann rückt jeder eine Station weiter, im Uhrzeigersinn. Spieler zwei beginnt die nächste Runde.",
     ps("b1", [56.6, 53.6]))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Doppelpass gleich am Start.", "Doppelpass am Start",
    "Spieler sieben kommt vom Dummy nach innen und legt den Ball in den Lauf des Starters. Der spielt direkt nach oben und muss danach noch schneller über die Hürde in die Zone. Mehr Pässe, mehr Tempo, beide Füße benutzen.",
    sp(), [B("b1", 47.6, 52.2)] + ERSATZ,
    [S("Doppelpass mit Spieler sieben", "Spieler sechs spielt zu Spieler sieben und läuft gleich schräg nach vorn. Spieler sieben legt mit einem Kontakt in seinen Lauf.",
       bl("n7", START), ps("b1", [29.9, 32.3], after=True), mv("n6", [37, 43], delay=0.3), ps("b1", [37.6, 43.6], after=True)),
     S("Direkt nach oben, dann über die Hürde", "Spieler sechs spielt direkt nach oben zu Spieler neun. Dann Vollgas über die Hürde und rein in die Zone. Ab hier läuft die Runde weiter wie bisher.",
       ps("b1", [45.1, 7.6]), *huerde(delay=0.3, von=[47.5, 46]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Am Ende kommt der Abschluss aufs Minitor.", "Abschluss aufs Minitor",
    "Unten rechts steht ein Minitor. Nach dem Steilpass spielt der Spieler am Dummy zum Start, bekommt den Ball zurück in den Lauf und schließt direkt ab. Der Trainer bringt sofort den nächsten Ball zum Start.",
    sp(n6=(50, 30), n9=(63, 27), n11=(67, 43.5)), [B("b1", 67.6, 44.1)] + ERSATZ,
    [S("Doppelpass vor dem Tor", "Spieler elf hat den Steilpass. Er spielt zum Start zu Spieler zwei und läuft weiter Richtung Tor. Spieler zwei legt direkt in seinen Lauf.",
       ps("b1", [56.6, 53.6]), mv("n11", [69.5, 47.5], delay=0.3), ps("b1", [70.1, 48.1], after=True)),
     S("Direkt abschließen: Punkt", "Spieler elf schießt mit dem ersten Kontakt ins Minitor, und das gibt einen Punkt für Spieler elf. Der Trainer spielt sofort den nächsten Ball zum Start.",
       ps("b1", [69, 54.6]))],
    goals=[{"x": 69, "y": 55, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
