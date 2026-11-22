import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 69-P1 (U12-U14, Woche 8 Phase 4): Protect the Pockets - Technical. 20 x 30 Yards = Feld x 33-67, y 5-56 (18 x 27 m),
# zwei Bahnen (Mitte gestrichelt), Passzone quer (gestrichelt), oben zwei Minitore. Pink -> Rot (7, 9, 8), Blau -> Neon (6, 10, 4).
# Je drei Spieler pro Bahn; die Wartenden stehen außerhalb neben dem Feld (3D-Abstand), der Trainer mit Bällen unten in der Mitte.
# Sichtkegel aus dem Text ("Use visual cues to anticipate where opponents pass is going", "read the attacker's body language"):
# der Verteidiger schaut im Coaching-Punkt auf den Angreifer. In Grundform und Video kein Kegel.
T = P("T", "c", 50, 50, "T")
POS = {"r7": (41, 40), "r9": (24, 46), "r8": (15.5, 46), "n6": (59, 40), "n10": (76, 46), "n4": (84.5, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 51.6, 53.5), B("s2", 48, 53.5)]
LINES = [rect(33, 5, 34, 51), line(50, 5, 50, 56), line(33, 25.5, 67, 25.5), line(33, 36, 67, 36)]
TORE = [{"x": 41, "y": 5, "side": "top"}, {"x": 59, "y": 5, "side": "top"}]
BAELLE = [B("b7", 41.6, 40.6), B("b6", 59.6, 40.6)]

u = {"title": "Bahn wechseln, Pass blocken", "code": "UE-149", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 8, "field_size": "18 x 27 m",
 "description": "Zwei Bahnen nebeneinander, oben in jeder Bahn ein Minitor, quer durch die Mitte eine Passzone. Jeder greift zuerst in seiner eigenen Bahn an: Er dribbelt nach vorn und darf erst in der Passzone ins Minitor passen. Danach sprintet er sofort hinüber in die andere Bahn und versucht, dort den Pass des Gegners zu blocken. Wenn alle Bälle gespielt sind, werden sie eingesammelt, und es gibt eine kurze Pause.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern, längs in zwei Bahnen geteilt. Quer durch die Mitte eine Passzone von 5 Metern, oben in jeder Bahn ein Minitor.",
  "Verteilen: Team Rot links, Team Neon rechts, jeder mit einem Ball. Die Wartenden stehen neben dem Feld. Der Trainer steht unten in der Mitte mit Ersatzbällen.",
  "Ablauf: Je einer von beiden Teams startet. Er dribbelt in seiner Bahn nach vorn und passt aus der Passzone ins Minitor. Dann sprintet er sofort in die andere Bahn und blockt dort den Pass des Gegners.",
  "Wertung: Jeder Pass ins Minitor ist ein Punkt. Danach sind die Nächsten dran. Sind alle Bälle gespielt, sammeln alle die Bälle ein und erholen sich kurz."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem eigenen Pass sofort umschalten und auf dem kürzesten Weg hinüber", "Nah an den Angreifer heran, damit der Winkel für den Pass klein wird", "Auf Körper und Fuß des Angreifers achten, um den Pass vorauszuahnen", "Mit dem Körper die Mitte schützen und den Gegner zur Seite drängen"],
 "materials": ["2 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Bahn wechseln, Pass blocken. Erst greift jeder in seiner Bahn an, dann sprintet er hinüber und verteidigt die andere.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Gleichzeitig los", "Rot sieben und Neon sechs starten gleichzeitig. Jeder dribbelt in seiner Bahn nach vorn, Rot sieben ist schon in der Passzone.",
     dr("r7", "b7", [41, 31]), dr("n6", "b6", [59, 35], delay=0.3)),
   S("Pass ins Minitor: Punkt", "Erst in der Passzone darf er passen. Rot sieben spielt flach ins linke Minitor, und das gibt einen Punkt für Team Rot.",
     ps("b7", [41, 5.3]), dr("n6", "b6", [59, 32], delay=0.2)),
   S("Rüber und blocken", "Sofort sprintet Rot sieben hinüber in die rechte Bahn. Neon sechs passt, aber Rot sieben steht im Weg und blockt den Ball. Dann sind die Nächsten dran, und Neon sechs verteidigt gegen Rot neun.",
     mv("r7", [58, 20.5]), ps("b6", [59.1, 25], delay=0.6))],
  "dims": dims(33, 67, 5, 56, "18 m", "27 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nah ran und den Winkel zumachen.", "Nah ran",
    "Wer weit weg steht, blockt nichts. Der Verteidiger sprintet auf dem kürzesten Weg hinüber, geht nah an den Angreifer heran und schaut genau auf Körper und Fuß. So ahnt er, wohin der Pass geht, und macht den Winkel zu.",
    sp(r7=(44, 30), n6=(59, 33)), [B("b6", 59.6, 33.6)] + ERSATZ,
    [S("Kürzester Weg", "Rot sieben sprintet auf dem kürzesten Weg hinüber und geht nah an Neon sechs heran. Dabei schaut er genau auf Körper und Fuß von Neon sechs.",
       mv("r7", [57.5, 25.5]), bl("r7", [59, 33], after=True)),
     S("Winkel zu: geblockt", "Neon sechs will ins Minitor passen, aber Rot sieben steht so nah, dass er den Ball blockt. Kein Punkt für Team Neon.",
       ps("b6", [59.3, 29.8]))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Angreifer darf täuschen.", "Täuschen erlaubt",
    "Jetzt darf der Angreifer auch ins andere Minitor passen. Er täuscht den Pass ins eigene Tor an, und wenn der Verteidiger darauf hereinfällt, spielt er ins andere. Der Verteidiger darf sich also nicht zu früh festlegen.",
    sp(r7=(44, 30), n6=(59, 33)), [B("b6", 59.6, 33.6)] + ERSATZ,
    [S("Antäuschen", "Rot sieben sprintet hinüber, um den Pass ins rechte Tor zu blocken. Neon sechs täuscht genau diesen Pass an und legt sich den Ball nach innen.",
       mv("r7", [58, 21]), dr("n6", "b6", [56, 31], delay=0.3)),
     S("Anderes Tor: Punkt", "Rot sieben ist schon zu weit drüben. Neon sechs passt ins linke Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b6", [41.5, 5.3]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
