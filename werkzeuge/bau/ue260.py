import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P10 (U12-U14, Torwarttraining): Goalkeeper Quick Feet Handling (Quick Feet Circuit and Handling). 10 x 8 Yards = Feld
# x 28-72, y 8-46 (9 x 7 m). Trainer unten wie im PDF, Torwart in der Mitte, kein Tor. Sechs Hütchen in drei Paaren wie im Video:
# oben und vorne orange (im Original rot), in der Mitte neongelb (im Original gelb). Reihenfolge wie im PDF: erst rechtes
# Hütchen (aus Sicht des Torwarts, der zum Trainer schaut, das linke wie im Text), dann linkes, dann die zwei vorderen.
# Der nächste Torwart (im Video oben an der Linie) wartet hier links neben dem Feld (3D-Abstand), er erholt sich dort.
# Keine Punkte (reine Technikübung), Ziel: jeden Volley festhalten und genau zurückwerfen.
# Sichtkegel aus dem PDF ("Quick set to get ready for catch") und Ton ("concentration ... to assess delivery"): nach den schnellen
# Füßen steht der Torwart kurz fest und schaut zum Trainer, bevor der Volley kommt. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Steigerung aus dem Video (Progression): Start oben, schnelle Füße als Acht um die beiden oberen Hütchen, dann der Volley.
T = P("T", "c", 50, 42, "T")
POS = {"k1": (50, 24), "k2": (18, 20)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 51.6, 45.5), B("s2", 48, 45.5)]
def baelle(b1=(50.6, 42.6)): return [B("b1", *b1)] + ERSATZ
LINES = [rect(28, 8, 44, 38)]
CONES = [C(43, 14), C(57, 14), C(42, 24, "neon"), C(58, 24, "neon"), C(42, 34), C(58, 34)]
MITTE, BALL_TW, BALL_T = [50, 24], [50.6, 24.6], [50.6, 42.6]
def weg(who, punkte, erst_after=False):
    return [mv(who, punkte[0], after=erst_after or None)] + [mv(who, p, after=True) for p in punkte[1:]]
# schnelle Füße um ein Hütchen (Abstand ca. 4) und zurück in die Mitte
UM_R = [[54, 20.5], [58, 20], [62, 24], [58, 28], [54, 27.5], MITTE]
UM_L = [[46, 20.5], [42, 20], [38, 24], [42, 28], [46, 27.5], MITTE]
UM_VR = [[54, 30], [58, 30], [62, 34], [58, 38], [54, 37], [52, 30], MITTE]
UM_VL = [[46, 30], [42, 30], [38, 34], [42, 38], [46, 37], [48, 30], MITTE]
def fangen(erst_after=True):
    return [ps("b1", BALL_TW, after=erst_after or None), ps("b1", BALL_T, after=True)]

u = {"title": "Hütchen umlaufen, Volley fangen", "code": "UE-260", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 1, "players_max": 2, "field_size": "9 x 7 m",
 "description": "Ein Torwart steht in der Mitte von sechs Hütchen. Auf Zuruf läuft er mit schnellen, kleinen Schritten um ein Hütchen und zurück in die Mitte. Dort fängt er einen Volley vom Trainer und wirft den Ball genau zurück. So geht es um vier Hütchen, dann ist der nächste Torwart dran.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 7 Metern. Sechs Hütchen in drei Paaren: zwei oben, zwei links und rechts der Mitte, zwei vorne.",
  "Verteilen: Ein Torwart steht in der Mitte, der zweite wartet neben dem Feld. Der Trainer steht unten mit Bällen.",
  "Ablauf: Auf Zuruf läuft der Torwart mit schnellen Füßen um das rechte Hütchen und zurück in die Mitte. Er fängt den Volley vom Trainer und wirft ihn zurück. Dann das linke Hütchen und danach die zwei vorderen.",
  "Wechsel: Nach vier Hütchen ist der zweite Torwart dran, und der erste erholt sich neben dem Feld. Ziel: jeden Ball festhalten und genau zurückwerfen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle, kleine Schritte um die Hütchen", "Vor dem Fangen kurz fest stehen und zum Trainer schauen", "Den Ball sicher fangen und festhalten", "Genau zum Trainer zurückwerfen und sich in der Pause gut erholen"],
 "materials": ["6 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Hütchen umlaufen, Volley fangen. Der Torwart läuft mit schnellen Füßen um ein Hütchen, fängt einen Volley und wirft den Ball zurück.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Um das rechte Hütchen", "Der Trainer ruft. Der Torwart läuft mit schnellen, kleinen Schritten um das rechte Hütchen und zurück in die Mitte.",
     *weg("k1", UM_R)),
   S("Bereit stehen", "In der Mitte steht er kurz fest, die Hände vor dem Körper, und schaut zum Trainer.",
     bl("k1", [50, 41])),
   S("Fangen und zurückwerfen", "Der Trainer spielt einen Volley. Der Torwart fängt den Ball, hält ihn fest und wirft ihn genau zum Trainer zurück.",
     *fangen(erst_after=False)),
   S("Links herum", "Jetzt das Gleiche auf der anderen Seite: um das linke Hütchen, zurück in die Mitte, Volley fangen und zurückwerfen.",
     *weg("k1", UM_L), *fangen()),
   S("Die vorderen Hütchen", "Danach kommen die zwei vorderen Hütchen dran, wieder jedes Mal mit Volley und Wurf zurück.",
     *weg("k1", UM_VR), *fangen(), *weg("k1", UM_VL, erst_after=True), *fangen()),
   S("Vier Hütchen: Wechsel", "Nach vier Hütchen ist die Runde geschafft. Hat er jeden Ball festgehalten, ist das Ziel erreicht. Jetzt ist der zweite Torwart dran, und der erste erholt sich neben dem Feld.",
     mv("k2", [36, 19]), mv("k2", [46, 19], after=True), mv("k2", MITTE, after=True),
     mv("k1", [50, 29], delay=0.3), mv("k1", [30, 29], after=True), mv("k1", [18, 34], after=True))],
  "dims": dims(28, 72, 8, 46, "9 m", "7 m", rx=80)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor dem Fangen schnell bereit stehen.", "Schnell bereit stehen",
    "Nach den schnellen Füßen nicht in den Ball hineinlaufen. Der Torwart kommt in der Mitte an, stellt die Füße kurz fest und schaut zum Trainer. Die Hände sind vorn, und er fängt den Ball sicher vor dem Körper.",
    sp(k1=(62, 24)), baelle(),
    [S("Zurück in die Mitte", "Der Torwart kommt vom rechten Hütchen mit kleinen Schritten zurück in die Mitte.",
       mv("k1", [58, 28]), mv("k1", [54, 27.5], after=True), mv("k1", MITTE, after=True)),
     S("Fest stehen und schauen", "Er stellt die Füße fest, die Hände sind vorn, und er schaut zum Trainer.",
       bl("k1", [50, 41])),
     S("Sicher fangen", "Jetzt kommt der Volley. Er fängt den Ball vor dem Körper, hält ihn fest und wirft ihn genau zurück.",
       *fangen(erst_after=False))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Laufwege ändern sich.", "Acht um zwei Hütchen",
    "Jetzt startet der Torwart oben an der Linie. Er läuft eine Acht um die zwei oberen Hütchen und kommt dann in die Mitte zum Fangen. Danach geht es um die nächsten zwei Hütchen. Der Trainer kann auch Seit- oder Rückwärtsschritte ansagen.",
    sp(k1=(50, 9)), baelle(),
    [S("Acht oben", "Der Torwart startet oben an der Linie. Er läuft mit schnellen Füßen eine Acht um die beiden oberen Hütchen.",
       *weg("k1", [[43, 9.5], [38.5, 14], [43, 18.5], [50, 14], [57, 9.5], [61.5, 14], [57, 18.5], [50, 19]])),
     S("In die Mitte und fangen", "Dann kommt er in die Mitte, steht kurz fest und fängt den Volley. Der Ball geht zurück zum Trainer.",
       mv("k1", MITTE), bl("k1", [50, 41], after=True), *fangen()),
     S("Die nächsten zwei", "Danach läuft er um die zwei mittleren Hütchen, wieder mit Volley und Wurf zurück. Dann ist der zweite Torwart dran.",
       *weg("k1", UM_R), *fangen(), *weg("k1", UM_L, erst_after=True), *fangen())])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
