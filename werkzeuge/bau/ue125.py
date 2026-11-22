import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 61-P4: 25 x 15 Yards (Skizze 20 x 15), gedreht (Spielrichtung nach rechts): Feld x 14-86, y 8-52, Viereck in der Mitte x 40-60, y 22-38.
T = P("T", "c", 88, 56, "T")
CB = [B("c1", 90.5, 56.6)]
POS = {"n10": (24, 30), "n11": (15, 30), "n8": (46, 28), "n9": (76, 30), "n4": (85, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
CONES = ecken(40, 22, 20, 16) + [C(27, 35), C(73, 35)]
LINES = [rect(14, 8, 72, 44), rect(40, 22, 20, 16, dashed=True)]
u = {"title": "Prallen lassen und abdrehen", "code": "UE-125", "kind": "Übungsform",
 "focuses": ["Passspiel", "Bewegung", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 8, "field_size": "18 x 14 m",
 "description": "In der Mitte steht ein Viereck aus Hütchen, an beiden Enden ein Starthütchen. Der erste Spieler passt zum Spieler im Viereck, der den Ball prallen lässt und aus dem Viereck abdreht. Der Spieler von der anderen Seite kommt ins Viereck, nimmt den nächsten Pass an, legt zum abgedrehten Spieler ab, und dieser spielt durch zum Endspieler. Dann geht es von der anderen Seite weiter.",
 "organisation": ["Aufbauen: Ein Feld von etwa 18 mal 14 Metern mit einem Viereck aus vier Hütchen in der Mitte und je einem Starthütchen an beiden Enden.",
  "Verteilen: An jedem Starthütchen zwei Spieler von Team Neon, ein Spieler steht im Viereck. Der Trainer hat Bälle am Rand.",
  "Ablauf: Pass ins Viereck, Prallpass zurück, der Spieler dreht aus dem Viereck ab. Der Spieler von der anderen Seite läuft ins Viereck, bekommt den Pass und legt zum abgedrehten Spieler ab, der durch zum Endspieler spielt.",
  "Wechsel: Wer zum Endspieler gespielt hat, läuft seinem Pass hinterher und stellt sich dort hinten an. Wer zuletzt ins Viereck gekommen ist, bleibt als neuer Spieler im Viereck, und der Endspieler startet den nächsten Ablauf von der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen", "Schnell ins Viereck kommen, um anzunehmen", "Wo es geht mit einem Kontakt spielen, mit beiden Füßen", "Im Winkel von etwa 45 Grad abdrehen und vor jedem Pass sprechen"],
 "materials": ["6 orange Hütchen", "Mehrere Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Prallen lassen und abdrehen. Kurze, schnelle Kombinationen mit einem oder zwei Kontakten.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 25.6, 30.6)] + CB,
  "steps": [
   S("Prallpass und abdrehen", "Spieler zehn spielt zu Spieler acht ins Viereck. Spieler acht lässt den Ball direkt zurückprallen und dreht schräg aus dem Viereck ab.",
     ps("b1", [44.4, 28.6]), ps("b1", [25.6, 30.6], after=True), mv("n8", [44, 16], after=True)),
   S("Ins Viereck kommen", "Gleichzeitig läuft Spieler neun von der anderen Seite ins Viereck, und Spieler zehn spielt ihn an.",
     mv("n9", [55, 30]), ps("b1", [53.4, 30.6], delay=0.4)),
   S("Ablegen und durchspielen", "Spieler neun legt zu Spieler acht ab. Spieler acht nimmt den Ball mit und spielt durch zu Spieler vier.",
     ps("b1", [45.6, 16.6]), dr("n8", "b1", [49, 12], after=True), ps("b1", [83.4, 30.6], after=True)),
   S("Wechsel, dann von rechts", "Spieler acht läuft seinem Pass hinterher und stellt sich rechts hinten an. Gleichzeitig dribbelt Spieler vier ans rechte Starthütchen, und Spieler neun bleibt als neuer Spieler im Viereck. Jetzt beginnt der Ablauf von rechts.",
     dr("n4", "b1", [76, 30]), mv("n8", [85, 30], delay=0.4))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "18 m"}, {"x1": 94, "y1": 8, "x2": 94, "y2": 52, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Ablage so spielen, dass direkt durchgespielt werden kann.", "Gute Ablage",
    "Die Ablage kommt mit dem richtigen Tempo genau in den Lauf des Mitspielers. Dann kann er den Ball direkt mit dem ersten Kontakt durchspielen. Das macht die Kombination schneller und schwerer zu verteidigen.",
    sp(n9=(55, 30), n8=(44, 16)), [B("g", 53.4, 30.6), B("b1", 25.6, 30.6)] + CB,
    [S("Ablage in den Lauf", "Spieler acht läuft an, und Spieler neun legt ihm den Ball genau in den Lauf.",
       mv("n8", [49, 12]), ps("g", [50.6, 12.6], delay=0.2)),
     S("Direkt durch", "Spieler acht spielt den Ball mit dem ersten Kontakt durch zu Spieler vier.",
       ps("g", [83.4, 30.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Doppelpässe kommen dazu.", "Zwei Doppelpässe",
    "Jetzt werden zwei Doppelpässe in den Ablauf eingebaut, einer auf jeder Seite des Vierecks. So gibt es mehr Ballkontakte und mehr Pässe, und die Spieler müssen ständig in Bewegung bleiben und sich gut abstimmen.",
    sp(n9=(55, 30), n8=(46, 14)), [B("b1", 25.6, 30.6)] + CB,
    [S("Erster Doppelpass", "Spieler zehn spielt zu Spieler acht und startet. Spieler acht spielt den Ball direkt in seinen Lauf zurück.",
       ps("b1", [44.4, 14.6]), mv("n10", [32, 20], delay=0.3), ps("b1", [33.6, 20.6], after=True)),
     S("Pass ins Viereck", "Spieler zehn dribbelt kurz an und spielt zu Spieler neun ins Viereck.",
       dr("n10", "b1", [36, 30]), ps("b1", [53.4, 30.6], after=True)),
     S("Zweiter Doppelpass", "Spieler neun spielt zu Spieler vier und startet. Spieler vier spielt ihn direkt wieder an.",
       ps("b1", [83.4, 30.6]), mv("n9", [68, 24], delay=0.3), ps("b1", [69.6, 24.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
