import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-11 (im PDF GK-P11, U12-U14, Torwarttraining): Goalkeeper Agility Handling (Handling and Agility Circuit Training).
# 45 x 18 Yards = Strafraum x 14-86, y 5-34 (41 x 16 m), Torraum nach der Skizze. Im PDF liegt das Tor links, hier oben wie im
# Video (dort auch oben, gleiche Seiten: zweiter Torwart links neben dem Tor, Trainer vor dem Torraum). Grüner Torwart 1 ->
# neutraler Torwart TW (k1, arbeitet), pinker Torwart 13 -> zweiter neutraler Torwart TW (k2, spielt den ersten Volley).
# Drei Hütchen wie im PDF: links vor dem Pfosten, rechts neben dem Tor (antippen), eins beim Trainer. "Nach rechts" aus Sicht
# des Torwarts ist auf der Tafel links, darum im Text "zum linken Pfosten". Kein Wettbewerb: Ziel statt Punkte.
# Fassungen = die zwei Key Coaching Points aus dem PDF (harte Volleys zur Seite abwehren; konzentriert bleiben, nachfassen).
# Sichtkegel aus Text und Ton ("move into the centre, set and catch": Grundstellung, Blick zum Ball): in der Mitte schaut der
# Torwart zum Trainer, bevor der zweite Volley kommt. Im Video kein Kegel eingezeichnet (nur Markierungen), Richtung aus dem Sinn.
T = P("T", "c", 50, 30, "T")
def sp(x=50, y=8): return [P("k1", "t", x, y, "TW"), P("k2", "t", 31, 7, "TW"), T]
ERSATZ = [B("s1", 54, 32.5), B("s2", 54, 28)]
def baelle(): return [B("b1", 50.6, 30.6), B("b2", 31.6, 7.6)] + ERSATZ
LINES = [rect(14, 5, 72, 29), rect(34, 5, 32, 9.6)]
CONES = [C(39, 13), C(62, 7.5), C(46, 31.5)]
TOR = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Volleys von zwei Seiten fangen", "code": "UE-253", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 2,
 "field_size": "41 x 16 m",
 "description": "Ein Torwart arbeitet einen kleinen Parcours im Torraum ab und fängt dabei drei Volleys. Den ersten spielt der zweite Torwart von der Seite, den zweiten und dritten der Trainer von vorn. Dazwischen läuft er schnell seitwärts und tippt ein Hütchen an. Nach zwei Runden tauschen die beiden Torhüter.",
 "organisation": ["Aufbauen: Ein Strafraum von 41 mal 16 Metern mit Torraum und einem Jugendtor. Ein Hütchen steht links vor dem Pfosten, eins rechts neben dem Tor und eins beim Trainer.",
  "Verteilen: Der Torwart steht in der Mitte des Tors. Der zweite Torwart steht links neben dem Tor mit Bällen. Der Trainer steht vor dem Torraum, auch mit Bällen.",
  "Ablauf: Der Torwart fängt einen Volley am linken Pfosten und wirft zurück. Dann fängt er in der Mitte einen Volley vom Trainer. Zum Schluss tippt er das rechte Hütchen an und fängt in der Mitte den dritten Volley.",
  "Wechsel: Nach zwei Runden tauschen die beiden Torhüter. Ziel ist, alle drei Volleys sicher festzuhalten."],
 "organisation_show": ORG,
 "coaching_points": ["Volleys sicher fangen und festhalten", "Zu harte Volleys zur Seite abwehren, weg vom Tor", "Mit schnellen Füßen seitwärts zum Hütchen", "Die ganze Runde konzentriert bleiben und in der Pause gut erholen"],
 "materials": ["1 Jugendtor", "3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Volleys von zwei Seiten fangen. Der Torwart läuft einen kleinen Parcours im Torraum und fängt drei Volleys hintereinander.",
 "board": {"lines": LINES, "goals": TOR, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Erster Volley", "Der Torwart läuft schnell zum linken Pfosten, zwischen Hütchen und Pfosten. Der zweite Torwart spielt ihm einen Volley zu, und er fängt den Ball.",
     mv("k1", [42, 8.5]), ps("b2", [42.6, 9.1], delay=0.3)),
   S("Zurück und in die Mitte", "Er wirft den Ball mit der Hand zurück und läuft in die Mitte. Dort stellt er sich bereit und schaut zum Trainer.",
     ps("b2", [31.6, 7.6]), mv("k1", [50, 9.5], after=True), bl("k1", [50, 26], after=True)),
   S("Zweiter Volley", "Der Trainer spielt einen Volley. Der Torwart fängt ihn sicher und wirft ihn zum Trainer zurück.",
     ps("b1", [50.6, 10.1]), ps("b1", [50.6, 30.6], after=True)),
   S("Hütchen antippen", "Jetzt schnell seitwärts zum rechten Hütchen, antippen und sofort zurück in die Mitte.",
     mv("k1", [60, 8.5]), mv("k1", [50, 9.5], after=True)),
   S("Dritter Volley", "Der Trainer spielt den dritten Volley aufs Tor. Der Torwart fängt ihn und wirft ihn zurück, damit ist die Runde geschafft. Nach zwei Runden tauschen die beiden Torhüter.",
     ps("b1", [50.6, 10.1]), ps("b1", [50.6, 30.6], after=True))],
  "dims": dims(14, 86, 5, 34, "41 m", "16 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Harte Volleys zur Seite abwehren.", "Harte Volleys abwehren",
    "Ist ein Volley zu hart zum Festhalten, wehrt der Torwart ihn ab. Aber nie nach vorn in die Mitte, sondern zur Seite, weg vom Tor. So macht er es auch im Spiel, damit kein Gegner nachschießen kann.",
    sp(42, 8.5), baelle(),
    [S("Harter Volley", "Der zweite Torwart spielt einen harten Volley. Der Torwart merkt: Den kann ich nicht festhalten.",
       ps("b2", [42.6, 9.1])),
     S("Zur Seite abwehren", "Er wehrt den Ball mit beiden Händen zur Seite ab, weg vom Tor. Dann ist er sofort wieder bereit für den nächsten Ball.",
       ps("b2", [36, 2.5]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Konzentriert bleiben und nachfassen.", "Konzentriert bleiben",
    "Die ganze Runde lang konzentriert bleiben. Volleys, die genau auf den Körper kommen, sicher festhalten. Rutscht der Ball doch einmal aus den Händen, sofort nachfassen und ihn sichern.",
    sp(50, 9.5), baelle(),
    [S("Ball rutscht weg", "Der Trainer spielt einen Volley genau auf den Torwart. Der Ball rutscht ihm aus den Händen und springt zur Seite.",
       ps("b1", [50.6, 10.1]), ps("b1", [58.6, 9.6], after=True)),
     S("Nachfassen", "Der Torwart reagiert sofort, fasst nach und sichert den Ball. Dann wirft er ihn zum Trainer zurück.",
       mv("k1", [58, 9]), ps("b1", [50.6, 30.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
