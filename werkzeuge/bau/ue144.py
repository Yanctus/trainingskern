import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-94 (U12-U14, Woche 6 Pre-Season): Sprints, Recovery Runs and 2 v 2's. 25 Yards Quadrat = Feld x 25-75, y 5-55 (23 m),
# Jugendtor oben mit neutralem Torwart, Spielzone in der oberen Hälfte. Pink (Angreifer) -> Neon 7, 9; Dunkel (Verteidiger) -> Rot 4, 5.
# Verteidiger seitlich versetzt hinter den Angreifern (3D-Abstand), Wartepaare nur im Text. Ein Trainer statt zwei.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 17, 25, "T")
TW = P("k", "t", 50, 7.1, "TW")
POS = {"n7": (42.7, 45.5), "n9": (57.6, 45.5), "r4": (34, 54.5), "r5": (66, 54.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
ERSATZ = [B("s1", 18.6, 28), B("s2", 15, 28)]
LINES = [rect(25, 5, 50, 50), line(25, 26.4, 75, 26.4)]
KEGEL = [C(25.5, 5.4), C(74.7, 5.4)] + [C(x, y, "neon", shape="stange") for x in (40.6, 59.1) for y in (44.7, 51.9)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Sprint ins 2 gegen 2", "code": "UE-144", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 13, "field_size": "23 x 23 m",
 "description": "Zwei Angreifer stehen vorn an den Stangen, zwei Verteidiger dahinter. Auf Zuruf sprinten die Angreifer zum Ball, die Verteidiger jagen hinterher. In der Spielzone vor dem Tor wird zwei gegen zwei gespielt: Die Angreifer müssen mindestens einmal passen, bevor sie schießen dürfen. Erobern die Verteidiger den Ball, dürfen sie selbst aufs Tor schießen. Danach sprinten alle zu den Eckhütchen und laufen locker zurück.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern, oben ein Jugendtor mit Torwart. Die obere Hälfte ist die Spielzone. Unten stehen vier Stangen als Start, oben in den Ecken zwei Hütchen.",
  "Verteilen: Paare aus Angreifern und Verteidigern. Die Angreifer stehen vorn an den Stangen, die Verteidiger dahinter, die anderen Paare warten unten. Der Trainer legt einen Ball in die Spielzone.",
  "Ablauf: Auf Zuruf sprinten die Angreifer zum Ball, die Verteidiger hinterher. In der Spielzone zwei gegen zwei, mindestens ein Pass vor dem Schuss. Erobern die Verteidiger den Ball, schießen sie selbst aufs Tor.",
  "Wechsel: Nach dem Angriff sprinten alle vier zu den Eckhütchen und laufen locker zurück, das startet die nächste Gruppe. Wer angegriffen hat, verteidigt beim nächsten Mal. Jedes Tor ist ein Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Mit vollem Tempo zum Ball sprinten oder dem Angreifer hinterher", "In der Spielzone ruhig bleiben und entscheiden: schnell angreifen oder neu aufbauen", "Mit schnellen Kombinationen Platz schaffen und eiskalt abschließen", "Beim Zurücklaufen bewusst erholen"],
 "materials": ["4 Stangen", "2 Hütchen", "1 Jugendtor", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Sprint ins zwei gegen zwei. Erst ein Wettlauf zum Ball, dann ein schnelles Spiel zwei gegen zwei mit Torwart und Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 40.8, 24.3)] + ERSATZ,
  "steps": [
   S("Sprint auf Zuruf", "Auf Zuruf sprinten Neon sieben und Neon neun nach vorn zum Ball, Rot vier und Rot fünf jagen ihnen hinterher.",
     mv("n7", [41.5, 25.5]), mv("n9", [56, 28]), mv("r4", [37, 42], delay=0.3), mv("r4", [44.5, 33], after=True), mv("r5", [61, 32], delay=0.3)),
   S("Zwei gegen zwei", "In der Spielzone dribbelt Neon sieben an und passt zu Neon neun. Der Pass muss sein, bevor geschossen werden darf.",
     dr("n7", "b1", [44, 20]), mv("r4", [47, 23], after=True), mv("n9", [57, 18.6], delay=0.2), ps("b1", [57.6, 19.2], after=True), mv("r5", [61, 24], delay=0.4)),
   S("Abschluss: Punkt", "Neon neun schießt am Torwart vorbei, und das gibt einen Punkt für Team Neon.",
     ps("b1", [53.5, 4.7])),
   S("Zu den Ecken, zurück", "Dann sprinten alle vier zu den Eckhütchen und laufen außen locker zurück. Das startet die nächste Gruppe, und wer angegriffen hat, verteidigt beim nächsten Mal.",
     *weg("n7", [[28, 8.5], [21, 40]]), *weg("r4", [[28.5, 11.5], [21.5, 50]], delay=0.2),
     *weg("n9", [[72, 8.5], [79, 40]]), *weg("r5", [[71.5, 11.5], [79, 50]], delay=0.2))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Verteidiger fangen ab und kontern.", "Abfangen und kontern",
    "Die Verteidiger lauern auf den Pass. Wer ihn vorausahnt und abfängt, schaltet sofort um und schießt selbst aufs Tor. Aus Verteidigung wird in einer Sekunde Angriff.",
    sp(n7=(42, 26), n9=(59, 21), r4=(33, 32), r5=(51, 37)), [B("b1", 42.6, 26.6)] + ERSATZ,
    [S("Pass vorausahnen", "Neon sieben will zu Neon neun passen. Rot fünf ahnt das voraus und läuft in den Passweg.",
       mv("r5", [51.5, 25]), ps("b1", [51.6, 24.4], delay=0.3)),
     S("Konter: Punkt", "Rot fünf fängt den Ball ab, dribbelt los und schießt am Torwart vorbei, und das gibt einen Punkt für Team Rot. Dann sprinten alle zu den Ecken.",
       dr("r5", "b1", [52, 15]), ps("b1", [54.5, 4.7], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ruhig bleiben in der Spielzone.", "Ruhig bleiben",
    "Ist der Weg zum Tor zu, nicht blind hineindribbeln. Lieber kurz zurück oder quer spielen, neu aufbauen und dann mit Tempo in die Lücke gehen. Erst entscheiden, dann handeln.",
    sp(n7=(42, 24), r4=(33, 14), n9=(58, 30), r5=(59, 14)), [B("b1", 42.6, 24.6)] + ERSATZ,
    [S("Zu, also quer", "Neon sieben dribbelt an, aber Rot vier macht den Weg zu. Also spielt er ruhig quer zu Neon neun.",
       dr("n7", "b1", [42, 19]), mv("r4", [37.5, 18], delay=0.1), ps("b1", [58.6, 30.6], after=True)),
     S("In die Lücke: Punkt", "Neon sieben läuft sofort in die Lücke, Neon neun spielt ihn an, und Neon sieben trifft. Das gibt einen Punkt für Team Neon.",
       mv("n7", [47, 15]), mv("r5", [59, 20], delay=0.2), ps("b1", [47.6, 15.6], after=True), ps("b1", [45, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
