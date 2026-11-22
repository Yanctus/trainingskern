import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 86-P5 (U12-U14, Woche 41 Phase 3): Develop Combination Play & 2 v 2 Attacks. 30 x 30 Yards = Feld x 25-75, y 5-55 (27 x 27 m),
# Strafraumlinie (durchgezogen) und Torraum wie im PDF, Halbkreis weggelassen. Ausrichtung wie im PDF (Tor oben).
# Navy -> Team Neon (Nummern aus dem Video: 7 rechts mit Ball, 11 links, 9 Stürmer; 3, 4, 8 warten, nur im Text, 3D-Abstand).
# Gold -> Team Rot, im Video 2, 3, 4, 5: wegen doppelter Nummern neu nummeriert (Gold 3 -> Spieler sechs, Gold 4 -> Spieler zehn,
# 2 und 5 bleiben). Gezeigt werden die zwei startenden Verteidiger (5 links, 6 rechts), 2 und 10 nur im Text. Grüner Torwart 1 ->
# Torwart von Team Rot (r1, TW), weil er laut Ton die Verteidiger coacht. Agility-Leitern als Leitern (senkrecht, außerhalb des
# Feldes), oben je ein Hütchen zum Antippen. Drei Puppen als Stangen. Ein Trainer statt zwei, er steht rechts unten.
# Sichtkegel: Text/Ton ohne Schulterblick-Wort; KCP "exploit the gap" und Progression "think ahead" -> im Coaching-Punkt schaut
# der Ballführende in die Lücke, in der Steigerung schaut der Verteidiger nach der Eroberung zum Minitor. Im Video kein Kegel
# eingezeichnet (nur Kreise um die Spieler), Richtung aus dem Sinn.
# Fassungen: Coaching-Punkt Verteidiger weglocken (PDF Seite 2, Video ab 0:36), Steigerung Minitore für die Verteidiger (Video ab 0:52).
T = P("T", "c", 88, 54, "T")
POS = {"r1": (50, 7.5), "n9": (49, 33.5), "n11": (40, 49), "n7": (60, 47.5), "r5": (20.5, 40), "r6": (79.5, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 91.6, 57.5), B("s2", 88, 57.5)]
LINES = [rect(25, 5, 50, 50), line(25, 29.5, 75, 29.5, dashed=False), rect(37.6, 5, 26.4, 7.1)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
MINI = TORE + [{"x": 31, "y": 33, "side": "bottom"}, {"x": 69, "y": 33, "side": "bottom"}]
KEGEL = [C(50.6, 28.7, shape="stange"), C(39, 42.6, shape="stange"), C(61.1, 42, shape="stange"),
         leiter(20.5, 24, senkrecht=True), leiter(79.5, 24, senkrecht=True), C(20.5, 9), C(79.5, 9)]

u = {"title": "Dritter Mann ins Zwei gegen Zwei", "code": "UE-246", "kind": "Übungsform",
 "focuses": ["Zusammenspiel", "Torschuss", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Drei Angreifer kombinieren um drei Puppen: Pass quer, Pass zum Stürmer, Ablage und Steilpass für den dritten Mann. Gleichzeitig laufen zwei Verteidiger außen durch die Leitern, tippen ein Hütchen an und verteidigen dann im Strafraum. Dort wird zwei gegen zwei aufs Tor gespielt. Danach ist die nächste Gruppe dran.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern mit Strafraum und Jugendtor oben. Drei Puppen im Dreieck, links und rechts außerhalb je eine Leiter und oben ein Hütchen.",
  "Verteilen: Team Neon greift an, drei Spieler pro Gruppe, die anderen warten unten. Team Rot verteidigt, je ein Spieler startet unter jeder Leiter. Ein Spieler von Team Rot steht im Tor. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Pass quer, Pass zum Stürmer, Ablage, Steilpass für den dritten Mann. Gleichzeitig laufen die Verteidiger durch die Leitern, tippen das Hütchen an und verteidigen. Dann zwei gegen zwei aufs Tor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon. Ist der Angriff vorbei, startet die nächste Gruppe, und zwei neue Verteidiger laufen los."],
 "organisation_show": ORG,
 "coaching_points": ["Vor der Ballannahme kurz antäuschen und dann entgegenkommen", "Genau und mit dem richtigen Tempo passen", "Schnell angreifen, bevor die Verteidiger da sind", "Mit Läufen Platz für den Mitspieler schaffen und genau abschließen"],
 "materials": ["1 Jugendtor", "3 Stangen als Puppen", "2 Koordinationsleitern", "2 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Dritter Mann ins Zwei gegen Zwei. Drei Angreifer kombinieren, während zwei Verteidiger durch die Leitern sprinten.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 60.6, 48.1)] + ERSATZ,
  "steps": [
   S("Pass quer, Leitern", "Spieler sieben passt quer zu Spieler elf. Spieler neun täuscht kurz nach vorn an und kommt entgegen. Gleichzeitig laufen Spieler fünf und Spieler sechs durch die Leitern und tippen oben das Hütchen an.",
     ps("b1", [40.6, 49.6]), mv("n9", [45, 29]), mv("n9", [46, 35.5], after=True), mv("r5", [20.5, 11]), mv("r6", [79.5, 11])),
   S("Zum Stürmer, Ablage", "Spieler elf spielt den Stürmer an. Spieler sieben kommt in die Mitte, und Spieler neun legt ihm direkt ab. Dann dreht Spieler neun ab und startet hinter die Puppe. Die Verteidiger laufen ins Feld.",
     ps("b1", [46.6, 36.1]), mv("n7", [57, 44]), mv("n7", [54, 38], after=True), ps("b1", [54.6, 38.6], after=True),
     mv("n9", [55, 31], after=True), mv("n9", [57, 21], after=True), mv("r5", [34, 17]), mv("r6", [66, 17])),
   S("Steil auf den dritten Mann", "Spieler elf startet links nach vorn. Spieler sieben spielt ihm den Ball steil in den Lauf. Spieler elf ist der dritte Mann.",
     mv("n11", [33.5, 44.5]), mv("n11", [35, 26], after=True), ps("b1", [35.6, 26.6], delay=0.8)),
   S("Zwei gegen zwei: Punkt", "Jetzt heißt es zwei gegen zwei. Spieler elf dribbelt auf Spieler fünf zu und passt zu Spieler neun. Spieler neun schießt direkt ins lange Eck, und das gibt einen Punkt für Team Neon. Dann greift die nächste Gruppe an, und zwei neue Verteidiger laufen durch die Leitern.",
     dr("n11", "b1", [38, 19]), mv("r5", [37, 14]), mv("n9", [57, 14]), mv("r6", [61, 16]), ps("b1", [57.6, 14.6], after=True),
     mv("r1", [53, 7], after=True), ps("b1", [44.5, 5.4], after=True))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=95)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Verteidiger weglocken.", "Den Verteidiger weglocken",
    "Der Angreifer ohne Ball läuft klug nach außen und nimmt seinen Verteidiger mit. In der Mitte wird eine Lücke frei. Der Mitspieler mit Ball sieht die Lücke, dribbelt hinein und schließt entschlossen ab.",
    sp(n11=(40, 30), r5=(31, 22), n9=(58, 26), r6=(67, 17), n7=(50, 45)), [B("b1", 40.6, 30.6)] + ERSATZ,
    [S("Weglocken", "Spieler neun läuft nach außen weg, und Spieler sechs geht mit. In der Mitte wird eine Lücke frei.",
       mv("n9", [75, 22]), mv("r6", [73, 16], delay=0.3)),
     S("In die Lücke: Punkt", "Spieler elf sieht die Lücke, dribbelt mit Tempo hinein und schießt ins Eck. Spieler fünf kommt zu spät, und das gibt einen Punkt für Team Neon.",
       bl("n11", [50, 14]), dr("n11", "b1", [48, 18], after=True), mv("r5", [40, 21], delay=0.5), ps("b1", [55.5, 5.4], after=True))],
    ),
  V("Steigerung", "Und jetzt die Steigerung: Minitore für die Verteidiger.", "Minitore für die Verteidiger",
    "Links und rechts stehen jetzt zwei Minitore. Erobern die Verteidiger den Ball, spielen sie schnell nach vorn hinaus und schießen auf ein Minitor. Ein Treffer dort gibt einen Punkt für Team Rot.",
    sp(n11=(60, 24), r6=(60, 8), n9=(40, 22), r5=(40, 6), n7=(51, 40)), [B("b1", 60.6, 24.6)] + ERSATZ,
    [S("Ball erobert", "Spieler elf dribbelt auf Spieler sechs zu. Spieler sechs stellt ihn und erobert den Ball.",
       dr("n11", "b1", [57, 18]), mv("r6", [59, 12.5]), ps("b1", [59.6, 13.1], after=True)),
     S("Aufs Minitor: Punkt", "Spieler sechs schaut kurz hoch und sieht das Minitor. Er dribbelt mit Tempo hinaus und schießt ins Minitor, und das gibt einen Punkt für Team Rot. Danach greift die nächste Gruppe an.",
       bl("r6", [66, 28]), dr("r6", "b1", [67, 26], after=True), ps("b1", [69, 32.4], after=True))],
    goals=MINI)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
