import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 10-P7 (U12-U14, Woche 28 Phase 5): Back 4s Positioning Based on Ball Position. 30 x 30 Yards = Feld x 25-75, y 5-55 (27 m).
# Gedreht: im PDF stehen die Verteidiger links und die Hütchen rechts, hier steht die Kette oben (eigenes Tor oben) und die
# Hütchen mit Ball unten. Pink -> Team Neon (2, 5, 6, 3 von links nach rechts, Nummern wie im PDF). Die Puppen (im PDF oben
# und unten am Rand auf Höhe der Kette) sind zwei Stangen links und rechts am Rand; "linke Stange" gilt aus Sicht der
# Verteidiger (auf der Tafel rechts). Vier Hütchen in vier Farben (Rot, Gelb, Blau, Weiß): auf der Tafel gibt es nur orange und
# neon, daher Rot und Blau orange, Gelb und Weiß neon; welche Farbe gemeint ist, steht im Text. Ein Trainer statt zwei, er
# steht links an der Seite (nimmt in der Steigerung den Ball an). Die Steigerung "Possession won" (Ball wieder in der Kette)
# steht nur im Text. Sichtkegel: Text "Check shoulders throughout to check for runners", Ton "check their shoulders ... be
# aware of ... attacking players looking to make runs" -> in der Grundform schaut Spieler zwei über die Schulter nach hinten
# (zum Raum hinter der Kette), Richtung aus dem Sinn (im Video kein Kegel eingezeichnet).
T = P("T", "c", 13, 32, "T")
POS = {"n2": (31, 20), "n5": (43, 15), "n6": (57, 15), "n3": (69, 20)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 14.6, 36), B("s2", 11, 36)]
HB = [B("bw", 27.5, 47), B("bb", 42, 47), B("bg", 57, 47), B("br", 71, 47)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(27.5, 49, "neon"), C(42, 49), C(57, 49, "neon"), C(71, 49), C(25, 11, "neon", shape="stange"), C(75, 11, "neon", shape="stange")]
ZURUECK = [mv(i, list(p)) for i, p in POS.items()]

u = {"title": "Viererkette schiebt zum Ball", "code": "UE-206", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 4, "players_max": 4, "field_size": "27 x 27 m",
 "description": "Vier Verteidiger stehen als Viererkette in der Mitte eines Feldes. Vor ihnen liegen vier farbige Hütchen mit je einem Ball. Ruft der Trainer eine Farbe, läuft der nächste Spieler zum Ball und setzt ihn unter Druck, die anderen drei schieben mit und sichern ab. Ruft er eine Stange, sprinten alle zurück und stellen sich neu auf.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern. Unten vier Hütchen in vier Farben, zum Beispiel Rot, Gelb, Blau und Weiß, auf jedem ein Ball. Auf der Tafel sind Rot und Blau orange, Gelb und Weiß neon. Oben links und rechts am Rand je eine Stange.",
  "Verteilen: Vier Spieler von Team Neon stehen als Viererkette oben in der Mitte: zwei, fünf, sechs und drei. Der Trainer steht links an der Seite mit Bällen.",
  "Ablauf: Der Trainer ruft eine Farbe. Der Spieler, der am nächsten dran ist, sprintet zum Ball und setzt ihn unter Druck. Die anderen drei schieben mit und sichern ab. Ruft der Trainer eine Stange, sprinten alle zurück zu dieser Seite. Links und rechts gelten aus Sicht der Verteidiger.",
  "Wechsel: Nach jedem Kommando gehen alle zurück in die Mitte, dann kommt das nächste. Später spielt die Kette sich einen Ball zu, und der Trainer ruft: Ballverlust und eine Farbe."],
 "organisation_show": ORG,
 "coaching_points": ["Die vier bewegen sich wie eine Einheit", "Abstände halten und den Pressenden absichern", "Viel reden und mit Zeichen zeigen", "Über die Schulter schauen und schnell reagieren"],
 "materials": ["4 Hütchen in vier Farben", "2 Stangen", "6 Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Viererkette schiebt zum Ball. Der Trainer ruft eine Farbe, und die Kette reagiert gemeinsam wie eine Einheit.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": HB + ERSATZ,
  "steps": [
   S("Rot: Druck auf den Ball", "Der Trainer ruft: Rot! Das rote Hütchen ist ganz rechts. Spieler drei ist am nächsten dran und sprintet zum Ball. Gleichzeitig schieben die anderen drei nach rechts, Spieler sechs sichert schräg dahinter ab. Spieler zwei schaut über die Schulter nach hinten.",
     mv("n3", [70, 42]), mv("n6", [62, 26]), mv("n5", [52, 21]), mv("n2", [41, 20]), bl("n2", [33, 6], after=True)),
   S("Zurück in die Mitte", "Jetzt gehen alle vier schnell zurück in die Mitte und stehen wieder als Kette.", *ZURUECK),
   S("Weiß: Druck auf den Ball", "Der Trainer ruft: Weiß! Das weiße Hütchen ist ganz links. Jetzt ist Spieler zwei am nächsten dran und sprintet los. Spieler fünf sichert ab, Spieler sechs und Spieler drei schieben nach links.",
     mv("n2", [28.5, 42]), mv("n5", [37, 28]), mv("n6", [47, 21]), mv("n3", [58, 20])),
   S("Stange links: Zurücklaufen", "Der Trainer ruft: Stange links! Ein Ball fliegt über die Kette, links aus Sicht der Verteidiger. Alle vier sprinten zurück zu dieser Stange, Spieler drei ganz außen, die anderen schräg daneben. Steht die Kette so, ist das Kommando geschafft. Dann gehen alle zurück in die Mitte, und der Trainer ruft das nächste Kommando.",
     mv("n3", [70, 8]), mv("n6", [61, 11]), mv("n5", [52, 14]), mv("n2", [42, 30]), mv("n2", [43, 17], after=True))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Als eine Einheit schieben.", "Wie eine Einheit",
    "Die vier Verteidiger bewegen sich, als wären sie mit einem Seil verbunden. Läuft einer raus, rücken die anderen nach und halten kurze Abstände. Der Nachbar sichert immer schräg dahinter ab.",
    sp(), HB + ERSATZ,
    [S("Blau: Absichern", "Der Trainer ruft: Blau! Das blaue Hütchen ist das zweite von links. Spieler fünf sprintet zum Ball, Spieler sechs sichert schräg dahinter ab. Spieler zwei und Spieler drei rücken nach innen.",
       mv("n5", [43, 42]), mv("n6", [50, 28]), mv("n2", [33, 26]), mv("n3", [61, 21])),
     S("Gelb: Weiterschieben", "Der Trainer ruft: Gelb! Spieler sechs sprintet zum gelben Hütchen. Spieler fünf geht zurück und sichert jetzt ihn ab. Die Abstände bleiben kurz, alle reden miteinander.",
       mv("n6", [57.5, 42]), mv("n5", [48, 25]), mv("n3", [66, 27]), mv("n2", [39, 20]))]),
  V("Steigerung", "Und jetzt die Steigerung: Mit Ball und Ballverlust.", "Mit Ball",
    "Jetzt hat die Kette einen Ball und spielt ihn sich zu, wie beim Aufbau von hinten. Dann geht der Ball zum Trainer, und er ruft: Ballverlust und eine Farbe. Sofort presst der Nächste den Ball, und die anderen sichern ab.",
    sp(), [B("b0", 69.6, 20.6)] + HB + ERSATZ,
    [S("Ball laufen lassen", "Spieler drei spielt zu Spieler sechs, der zu Spieler fünf und der zu Spieler zwei. Der Ball läuft schnell durch die Kette.",
       ps("b0", [57.6, 15.6]), ps("b0", [43.6, 15.6], after=True), ps("b0", [31.6, 20.6], after=True)),
     S("Ballverlust: Gelb", "Spieler zwei spielt zum Trainer. Der ruft: Ballverlust, Gelb! Spieler sechs sprintet sofort zum gelben Hütchen, Spieler fünf und Spieler drei sichern ab, Spieler zwei rückt nach innen.",
       ps("b0", [13.6, 32.6]), mv("n6", [57.5, 42], after=True), mv("n5", [49, 28], delay=1.0), mv("n3", [66, 28], delay=1.0), mv("n2", [38, 22], delay=1.0))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
