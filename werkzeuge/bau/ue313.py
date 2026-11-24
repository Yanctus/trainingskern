import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 62-P5 (U15-U17, Woche 14): Defensive Transition Rondos. 25 x 40 Yards = 23 x 37 m, gerundet 35 x 25 m.
# QUER GELEGT (im PDF liegen die drei Rondos übereinander, hier nebeneinander: Feld x 12-86, y 5-55), sonst stehen die
# Spieler in 3D voreinander. Drei Rondos je 10 Yards (9 m), dazwischen 5 Yards. Links und Mitte 4 gegen 2, rechts frei.
# Im PDF drei Farben für die Passgeber und Gelb für die Jäger; hier alle Passgeber Team Neon (2-13), die vier Jäger
# Team Rot (14-17). Nach jedem Ballgewinn mischen sich die Farben, das ist im Original genauso.
# Ein Trainer statt zwei. Sichtkegel: im Video keiner eingezeichnet; aus Text und Ton ("find the free rondo",
# "react quickly to find the free Rondo"): Der Ballverlierer schaut zum freien Rondo, bevor er lossprintet.
# Kein Dubletten-Fall: UE-150 (88-P5) ist ein Rondo durch drei Zonen mit Zielspieler, UE-154 ein einzelnes Rondo.
T = P("T", "c", 5, 30, "T")
ERSATZ = [B("s1", 6.6, 33.5), B("s2", 3, 33.5)]
POS = {"n2": (14.5, 9), "n3": (28, 9), "n4": (14.5, 51), "n5": (28, 51),
       "n6": (42.25, 9), "n7": (55.75, 9), "n8": (42.25, 51), "n9": (55.75, 51),
       "n10": (70, 9), "n11": (83.5, 9), "n12": (70, 51), "n13": (83.5, 51)}
JAEGER = {"r14": (16, 25), "r15": (24.5, 35), "r16": (43.75, 25), "r17": (52.25, 35)}
def sp(**k):
    d = dict(POS); j = dict(JAEGER)
    for i, v in k.items(): (d if i in d else j)[i] = v
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [P(i, "b", x, y, i[1:]) for i, (x, y) in j.items()] + [T]
def fuss(i): x, y = POS[i]; return [round(x + 0.6, 2), round(y + 0.6, 2)]
LINES = [rect(12, 5, 74, 50, dashed=True), rect(12, 5, 18.5, 50), rect(39.75, 5, 18.5, 50), rect(67.5, 5, 18.5, 50)]

u = {"title": "Nach Ballverlust ins freie Rondo", "code": "UE-313", "kind": "Übungsform",
 "focuses": ["Umschalten", "Verteidigen", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 16, "players_max": 18,
 "field_size": "35 x 25 m",
 "description": "Drei Rondos liegen nebeneinander. In zwei davon wird vier gegen zwei gespielt, im dritten läuft der Ball ohne Gegner. Wer den Ball an die Jäger verliert, ruft einen Mitspieler und sprintet mit ihm ins freie Rondo, um dort sofort zu pressen. Die Balleroberer bleiben und spielen als Passgeber weiter.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 25 Metern mit drei Rondos nebeneinander. Jedes Rondo ist 9 Meter breit, dazwischen bleiben knapp 5 Meter frei.",
  "Verteilen: In jedem Rondo stehen vier Passgeber mit einem Ball. Im linken und im mittleren Rondo jagen je zwei Spieler von Team Rot. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Links und in der Mitte läuft vier gegen zwei, rechts geht der Ball mit einem Kontakt im Kreis. Erobern die Jäger den Ball, sprinten der Ballverlierer und ein Mitspieler ins freie Rondo und jagen dort.",
  "Wechsel: Die Balleroberer bleiben und werden Passgeber, ihr Rondo ist jetzt das freie. Gespielt wird zwei bis drei Minuten mit vollem Tempo, dann ist Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Zu zweit eng bleiben, einer presst, einer sichert", "Ball weg? Kopf hoch und sofort rufen", "Im Sprint ins freie Rondo", "Im freien Rondo mit einem Kontakt spielen"],
 "materials": ["Hütchen für drei Rondos", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Nach Ballverlust ins freie Rondo. Drei Rondos nebeneinander, in zwei wird gejagt. Wer den Ball verliert, sprintet mit einem Mitspieler ins freie Rondo und presst dort.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(),
  "balls": [B("a", *fuss("n2")), B("b", *fuss("n6")), B("c", *fuss("n10"))] + ERSATZ,
  "steps": [
   S("Zwei Rondos, vier gegen zwei", "Links und in der Mitte läuft vier gegen zwei, beide Rondos gleichzeitig. Rechts jagt keiner. Dort geht der Ball mit einem Kontakt im Kreis.",
     ps("a", fuss("n3")), mv("r14", [22, 15], delay=0.2), mv("r15", [24.5, 30], delay=0.2),
     ps("b", fuss("n7")), ps("b", fuss("n9"), after=True), mv("r16", [47, 20], delay=0.2), mv("r17", [53, 41], delay=0.6),
     ps("c", fuss("n11")), ps("c", fuss("n13"), after=True), ps("c", fuss("n12"), after=True)),
   S("Ballgewinn in der Mitte", "Spieler siebzehn läuft Spieler neun an. Der will quer durch die Mitte spielen, aber Spieler sechzehn steht genau im Passweg und hat den Ball.",
     mv("r17", [58, 45]), ps("b", [47.7, 24.6], delay=0.5), mv("r16", [47.1, 24], delay=0.4),
     ps("a", fuss("n5")), mv("r15", [25, 42], delay=0.3), mv("r14", [20, 22], delay=0.3),
     ps("c", fuss("n10")), ps("c", fuss("n11"), after=True)),
   S("Rufen und zu zweit rüber", "Ball weg. Spieler neun schaut nach rechts, dort ist das freie Rondo. Er ruft Spieler sieben, und beide sprinten sofort hinüber.",
     bl("n9", [72, 38]), mv("n9", [74, 37], after=True), mv("n7", [79, 23], delay=0.9),
     ps("a", fuss("n4")), ps("c", fuss("n13"), delay=0.9)),
   S("Die Mitte ist jetzt frei", "Rechts läuft jetzt vier gegen zwei. Spieler sechzehn und Spieler siebzehn bleiben in der Mitte und spielen dort als Passgeber weiter. Damit ist die Mitte das freie Rondo. Wer als Nächster den Ball verliert, ruft einen Mitspieler und sprintet mit ihm dorthin.",
     dr("r16", "b", [55.75, 9]), mv("r17", [55.75, 51]), ps("b", fuss("n6"), after=True),
     ps("c", fuss("n12")), mv("n9", [75, 45], delay=0.2), mv("n7", [76, 16], delay=0.2), ps("c", fuss("n10"), after=True),
     ps("a", fuss("n2")))],
  "dims": dims(12, 86, 5, 55, "35 m", "25 m", rx=94)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Als Paar eng zusammenbleiben.", "Als Paar eng bleiben",
    "Stehen die beiden Jäger weit auseinander, geht der Pass einfach zwischen ihnen durch. Darum läuft einer den Ball an und macht eine Seite zu. Der zweite bleibt dicht dahinter und lauert auf den Pass durch die Mitte.",
    sp(), [B("a", *fuss("n2")), B("b", *fuss("n6")), B("c", *fuss("n10"))] + ERSATZ,
    [S("Zu weit auseinander", "Im mittleren Rondo laufen die beiden Jäger in verschiedene Richtungen. Zwischen ihnen ist alles offen, und Spieler sechs spielt bequem durch zu Spieler neun.",
       mv("r16", [43, 31]), mv("r17", [55, 20]), ps("b", fuss("n9"), delay=0.6)),
     S("Eng zusammen, Pass abgefangen", "Jetzt richtig. Spieler siebzehn läuft Spieler neun an und macht die Linie zu. Spieler sechzehn rückt dicht dahinter nach. Der Pass durch die Mitte bleibt bei ihm hängen.",
       mv("r17", [57, 33]), mv("r17", [57.8, 45.5], after=True), mv("r16", [50.9, 36], delay=0.3), ps("b", [51.5, 36.6], delay=1.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ball weg, Kopf hoch, rufen und sprinten.", "Rufen, schauen, sprinten",
    "Nach dem Ballverlust bleibt keine Zeit zum Ärgern. Der Ballverlierer hebt den Kopf, findet das freie Rondo und ruft einen Mitspieler. Einer sprintet direkt auf den Ball, der andere macht dahinter die Mitte zu.",
    sp(), [B("a", *fuss("n2")), B("b", 44.35, 25.6), B("c", *fuss("n13"))] + ERSATZ,
    [S("Ball weg, Kopf hoch", "Spieler sechzehn hat den Ball erobert. Spieler neun hebt sofort den Kopf. Rechts steht keiner in der Mitte, das ist das freie Rondo. Er ruft Spieler sieben.",
       bl("n9", [72, 38])),
     S("Einer auf den Ball, einer sichert", "Beide sprinten los. Spieler neun geht direkt auf den Ball, Spieler sieben macht dahinter die Mitte zu. Jetzt wird auch rechts vier gegen zwei gespielt.",
       mv("n9", [67, 42]), mv("n9", [79.5, 46.5], after=True), mv("n7", [76, 30], delay=0.2), ps("c", fuss("n11"), delay=1.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
