import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# BM-01: 20 x 15 Yards, gedreht: x 22-78, y 9-51. Mittelviereck x 35-62, y 19-41 (größer als im PDF, damit sich in 3D niemand verdeckt).
T = P("T", "c", 68, 4, "T"); cb = [B("c1", 71.5, 4.6)]
innen = [("n2", 38, 21.5), ("n3", 46.5, 21.5), ("n4", 55, 21.5), ("n5", 42.25, 38), ("n6", 50.75, 38), ("n7", 59.25, 38)]
aussen = [("r8", 20.5, 18), ("r9", 20.5, 41.4), ("r10", 79.5, 17.4), ("r11", 79.5, 41.6), ("r12", 49.7, 5.5), ("r14", 49.7, 54)]
def spieler(i=innen, a=aussen):
    return [P(k, "a", x, y, k[1:]) for k, x, y in i] + [P(k, "b", x, y, k[1:]) for k, x, y in a] + [T]
def baelle(i=innen):
    return [B("b" + k[1:], x + 1.6, y + 0.6) for k, x, y in i] + cb
lines = [rect(22, 9, 56, 42), rect(35, 19, 27, 22)]
cones = ecken(22, 9, 56, 42) + [C(35, 19, "neon"), C(62, 19, "neon"), C(35, 41, "neon"), C(62, 41, "neon")]
u = {"title": "Dribbeln, ablegen, tauschen", "code": "UE-072", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 12, "players_min": 8, "players_max": 14, "field_size": "18 x 14 m",
 "description": "Die Hälfte der Gruppe dribbelt mit Ball im Viereck in der Mitte, die andere Hälfte steht ohne Ball außen am Feldrand. Alle Spieler in der Mitte dribbeln gleichzeitig, schauen sich um und wechseln ständig die Richtung. Wer bereit ist, dribbelt nach außen und legt den Ball einem Außenspieler ab, dann tauschen beide die Rollen. Der neue Spieler dribbelt mit einem Richtungswechsel ins Viereck hinein.",
 "organisation": ["Aufbauen: Außen ein Feld von 18 mal 14 Metern, in der Mitte ein Viereck mit vier gelben Hütchen.",
  "Verteilen: Die Hälfte der Spieler hat einen Ball und dribbelt im Viereck. Die anderen stehen ohne Ball außen am Rand, zwei an jeder langen Seite und einer an jeder kurzen.",
  "Ablauf: Alle in der Mitte dribbeln gleichzeitig, mit vielen Richtungswechseln. Einer dribbelt raus, legt einem Außenspieler ab und übernimmt dessen Platz.",
  "Wechsel: Der Außenspieler nimmt den Ball mit und dribbelt mit einem Richtungswechsel ins Viereck. So bleiben alle in Bewegung."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball eng führen und die eigene Technik verbessern", "Oft und bewusst die Richtung wechseln", "Beide Füße und alle Teile des Fußes benutzen", "Genau und mit dem richtigen Tempo ablegen"],
 "materials": ["4 orange Hütchen", "4 gelbe Hütchen", "1 Ball für jeden Spieler in der Mitte"],
 "access": "frei", "hidden": True,
 "say_intro": "Dribbeln, ablegen, tauschen. Hier dribbeln alle in der Mitte gleichzeitig und tauschen nach einer Ablage die Plätze mit den Außenspielern.",
 "board": {"lines": lines, "cones": cones, "players": spieler(), "balls": baelle(),
  "steps": [
   S("Alle dribbeln gleichzeitig", "Alle Spieler in der Mitte dribbeln gleichzeitig durch das Viereck und wechseln ständig die Richtung.",
     dr("n2", "b2", [42, 28]), dr("n3", "b3", [50, 27.5]), dr("n4", "b4", [57, 29]), dr("n5", "b5", [39, 33]), dr("n6", "b6", [52, 33]), dr("n7", "b7", [57.5, 34])),
   S("Raus zum Außenspieler", "Spieler zwei dribbelt nach links raus und legt Spieler acht ab, gleichzeitig legt Spieler sieben rechts für Spieler elf ab.",
     dr("n2", "b2", [30, 22]), ps("b2", [22.1, 18.6], after=True), dr("n7", "b7", [68, 39]), ps("b7", [78, 41.2], after=True)),
   S("Tauschen und rein mit Richtungswechsel", "Jetzt tauschen sie: Spieler acht und Spieler elf dribbeln mit einem Haken ins Viereck, Spieler zwei und Spieler sieben bleiben außen.",
     dr("r8", "b2", [28, 24.5]), dr("r8", "b2", [32, 20.5], after=True), dr("r8", "b2", [40, 28], after=True), mv("n2", [21, 19.5], delay=0.4),
     dr("r11", "b7", [71, 36]), dr("r11", "b7", [66, 40], after=True), dr("r11", "b7", [58.5, 32], after=True), mv("n7", [79, 40], delay=0.4))],
  "dims": [{"x1": 22, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "18 m"}, {"x1": 91, "y1": 9, "x2": 91, "y2": 51, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnelle Richtungswechsel schaffen Platz in der engen Mitte.", "Schnell die Richtung wechseln",
    "In der Mitte ist es eng. Wer schnell die Richtung wechselt, entkommt den anderen, findet freien Raum und hat danach mehr Möglichkeiten zum Passen, Dribbeln oder Schießen.",
    spieler(), baelle(),
    [S("Auf engem Raum", "Spieler drei dribbelt auf Spieler sechs zu, und es wird eng.", dr("n3", "b3", [48.5, 30]), dr("n6", "b6", [51, 33.5], delay=0.1)),
     S("Haken und weg", "Mit einem schnellen Haken zieht Spieler drei in die andere Richtung und hat wieder Platz.",
       dr("n3", "b3", [44.5, 31]), dr("n3", "b3", [40, 25.5], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Erst ein Doppelpass mit dem Außenspieler, dann quer durch das Viereck.", "Doppelpass und quer durch",
    "Vor dem Tausch spielt der Spieler aus der Mitte einen Doppelpass mit einem Außenspieler. Danach dribbelt er quer durch das Viereck, abwechselnd mit links und rechts, bis zur anderen Seite. So entstehen mehr Ballkontakte und ein flüssigeres Spiel.",
    spieler(i=[("n2", 30, 27), ("n3", 46.5, 21.5), ("n4", 55, 21.5), ("n5", 42.25, 38), ("n6", 50.75, 38), ("n7", 59.25, 38)]),
    baelle(i=[("n2", 30, 27), ("n3", 46.5, 21.5), ("n4", 55, 21.5), ("n5", 42.25, 38), ("n6", 50.75, 38), ("n7", 59.25, 38)]),
    [S("Pass zum Außenspieler", "Spieler zwei spielt den Ball zu Spieler acht und läuft sofort weiter.", ps("b2", [22.1, 18.6]), mv("n2", [29, 21], delay=0.2)),
     S("Direkt zurück", "Spieler acht spielt den Ball direkt zurück in den Lauf.", ps("b2", [30.4, 21.6])),
     S("Quer durch das Viereck", "Spieler zwei dribbelt mit links und rechts quer durch das Viereck bis zur anderen Seite.",
       dr("n2", "b2", [44, 29.5]), dr("n2", "b2", [66, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
