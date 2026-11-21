import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-1: Fangen und Abschluss, 20 x 20 Yards = x 28-72, y 8-52, an jeder Seite ein Minitor, je 3 Bälle davor (auf der Linie).
T = P("T", "c", 75.5, 4, "T")
balls = [B("t1", 37, 9.5), B("t2", 50, 9.5), B("t3", 63, 9.5), B("u1", 37, 50.5), B("u2", 50, 50.5), B("u3", 63, 50.5),
         B("l1", 29.5, 17), B("l2", 29.5, 30), B("l3", 29.5, 43), B("r1", 70.5, 19.5), B("r2", 70.5, 30), B("r3", 70.5, 40.5), B("c1", 79, 5.5)]
goals = [{"x": 50, "y": 8, "side": "top"}, {"x": 50, "y": 52, "side": "bottom"}, {"x": 28, "y": 30, "side": "left"}, {"x": 72, "y": 30, "side": "right"}]
u = {"title": "Fangen und Abschluss", "code": "UE-063", "kind": "Spielform",
 "focuses": ["Erwärmung", "Bewegung", "Torschuss"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "duration_minutes": 10, "players_min": 5, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Alle Spieler laufen gleichzeitig in einem Feld von 18 mal 18 Metern, an jeder Seite steht ein Minitor mit drei Bällen davor. Jeder versucht, andere zu fangen, also mit der Hand zu berühren, ohne selbst gefangen zu werden. Wer jemanden gefangen hat, dreht sofort um und schießt einen Ball direkt ins nächste Tor, das gibt einen Punkt. Wer am Ende die meisten Fänge und Tore gesammelt hat, gewinnt.",
 "organisation": ["Feld abstecken: 18 mal 18 Meter mit vier orangen Hütchen, an jeder Seite steht mittig ein Minitor.",
  "Bälle verteilen: Vor jedem Tor liegen drei Bälle auf der Linie, ich stehe mit weiteren Bällen an der Ecke.",
  "Fangen: Alle laufen gleichzeitig im Feld und versuchen, andere zu fangen, also zu berühren, ohne selbst gefangen zu werden.",
  "Abschluss: Wer jemanden gefangen hat, holt sich den nächsten Ball und schießt ihn direkt ins Tor davor. Jeder zählt seine Fänge und Tore."],
 "organisation_show": ORG,
 "coaching_points": ["Ständig in Bewegung bleiben, damit man nicht erwischt wird", "Immer wissen, wo die anderen Spieler sind", "Den richtigen Moment zum Abschlagen wählen", "Beim Abschluss das Tor treffen"],
 "materials": ["4 Minitore", "4 orange Hütchen", "12 Bälle an den Toren", "Weitere Bälle beim Trainer"],
 "access": "frei", "hidden": False,
 "say_intro": "Fangen und Abschluss. Hier fangen sich alle Spieler gleichzeitig gegenseitig und schießen nach jedem Fang direkt aufs nächste Minitor.",
 "board": {"lines": [rect(28, 8, 44, 44)], "goals": goals, "cones": ecken(28, 8, 44, 44), "balls": balls,
  "players": [P("n2", "a", 38.3, 17.3, "2"), P("n3", "a", 59.4, 18, "3"), P("n6", "a", 49.7, 28, "6"), P("n4", "a", 33, 34, "4"), P("n7", "a", 52, 45, "7"), T],
  "steps": [
   S("Alle laufen gleichzeitig", "Alle laufen gleichzeitig durcheinander, und jeder versucht, einen anderen zu fangen. Wir schauen zuerst auf Spieler sechs.",
     mv("n6", [53, 25]), mv("n3", [61, 21], delay=0.1), mv("n2", [43, 13], delay=0.1), mv("n4", [36, 28], delay=0.2), mv("n7", [57, 46.5], delay=0.2)),
   S("Sechs fängt die Drei", "Spieler sechs berührt Spieler drei, damit hat er ihn gefangen.",
     mv("n6", [57.5, 22.5]), mv("n3", [62.5, 24], delay=0.2), mv("n7", [52, 43], delay=0.1)),
   S("Umdrehen zum Ball, die anderen jagen weiter", "Sofort dreht Spieler sechs um und sprintet zum nächsten Ball. Gleichzeitig jagt Spieler vier Spieler zwei.",
     mv("n6", [68.5, 39.5]), mv("n4", [40.5, 16.5], delay=0.1), mv("n2", [45.5, 11.5], delay=0.25)),
   S("Direkt ins Tor: Punkt", "Spieler sechs schießt direkt ins rechte Minitor, das gibt einen Punkt für ihn. Spieler vier hat inzwischen Spieler zwei gefangen und holt sich schon den nächsten Ball.",
     ps("r3", [73.8, 31]), mv("n4", [37.5, 12], delay=0.2))],
  "dims": [{"x1": 28, "y1": 58.6, "x2": 72, "y2": 58.6, "text": "18 m"}, {"x1": 82, "y1": 8, "x2": 82, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst umschauen, dann fangen, dann schnell zum Ball.", "Umschauen, fangen, abschließen",
    "Wer sich ständig umschaut, findet schnell einen Spieler, der nicht aufpasst. Hat man jemanden gefangen, dreht man sofort um, holt den nächsten Ball und schließt entschlossen ab. Umschauen, Tempo und eine schnelle Entscheidung gehören zusammen.",
    [P("n4", "a", 34, 13, "4"), P("n2", "a", 42.9, 25.5, "2"), P("n3", "a", 61.2, 16.4, "3"), P("n6", "a", 66, 32, "6"), P("n7", "a", 34.4, 42, "7"), T], balls,
    [S("Umschauen", "Spieler vier schaut sich um und sieht, dass Spieler zwei gerade nicht aufpasst.", mv("n4", [37, 17]), mv("n3", [57, 21], delay=0.2)),
     S("Schnell fangen", "Mit ein paar schnellen Schritten berührt er Spieler zwei und hat ihn gefangen.", mv("n4", [41, 22.5]), mv("n2", [46, 27], delay=0.3)),
     S("Umdrehen, Ball holen", "Sofort dreht Spieler vier um und holt sich den nächsten Ball links.", mv("n4", [32, 18.5])),
     S("Direkt ins linke Tor: Punkt", "Er schließt direkt ins linke Minitor ab, und das gibt einen Punkt.", ps("l1", [26.3, 29]))]),
  V("Steigerung", "Und jetzt die Steigerung: Mit dem Ball durch die anderen dribbeln und in ein anderes Tor treffen.", "Durch den Verkehr in ein anderes Tor",
    "Jetzt darf nicht mehr ins Tor direkt vor dem Ball geschossen werden. Wer einen Ball holt, dribbelt durch die anderen Spieler hindurch und trifft in eines der anderen Tore. Das verlangt mehr Übersicht, Ballkontrolle und schnelle Entscheidungen.",
    [P("n4", "a", 33, 47, "4"), P("n2", "a", 40, 30, "2"), P("n6", "a", 50, 18, "6"), P("n3", "a", 61, 23, "3"), P("n7", "a", 61, 40, "7"), T], balls,
    [S("Gefangen, Ball holen", "Spieler vier hat jemanden gefangen und holt sich den Ball an der linken Seite.", mv("n4", [31.2, 43.6])),
     S("Dribbling durch den Verkehr", "Mit dem Ball dribbelt er im Bogen an Spieler zwei vorbei, der ihm in den Weg läuft.",
       dr("n4", "l3", [38, 44.5]), dr("n4", "l3", [45, 43], after=True), mv("n2", [42, 38], delay=0.1)),
     S("Ins untere Tor: Punkt", "Er schließt ins untere Minitor ab, also in ein anderes Tor, und das gibt einen Punkt.", ps("l3", [48.5, 54.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
