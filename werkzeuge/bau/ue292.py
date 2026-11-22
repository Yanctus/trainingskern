import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P28 (U12-U14, Einzeltraining): SAQ Exercise. 10 x 10 Yards = Feld x 30-70, y 10-50 (9 x 9 m), Orientierung wie im PDF
# (Sprint nach oben). Erste Hürde quer unten (huerde_ou, wird nach oben übersprungen), zweite Hürde links (huerde, wird seitlich
# überstiegen), zwei Hütchen oben (im Video gelb, hier orange). Ablauf nach Video: Hüpfer rechts über Hürde eins, links seitlich
# über Hürde zwei, zurück und auf dem rechten Fuß in der Mitte landen, Sprint durch die Hütchen, außen rechts zurücktraben.
# Ein Spieler (Neon 7) und der Trainer an der Seite (im Original kein Trainer zu sehen). Keine Bälle im Original, nur die zwei
# Ersatzbälle beim Trainer. Keine Progressionen im PDF: die zwei Fassungen sind Coaching-Punkte aus der Key-Coaching-Points-Liste.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 84, 48, "T")
POS = {"n7": (50, 53.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 84.6, 51.5), B("s2", 81, 51.5)]
LINES = [rect(30, 10, 40, 40)]
KEGEL = [C(50, 46, shape="huerde_ou"), C(38, 36, shape="huerde"), C(45, 15), C(55, 15)]
HUEPFER = [mv("n7", [50, 41])]
LINKS = [mv("n7", [43, 36]), mv("n7", [33.5, 36], after=True)]
ZURUECK = [mv("n7", [43, 36]), mv("n7", [50, 30], after=True)]
SPRINT = [mv("n7", [50, 8.5])]
TRAB = [mv("n7", [63, 11]), mv("n7", [63, 40], after=True), mv("n7", [54, 51], after=True), mv("n7", [50, 53.5], after=True)]

u = {"title": "Zwei Hürden, dann Sprint", "code": "UE-292", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1, "field_size": "9 x 9 m",
 "description": "Ein Spieler arbeitet allein an Schnelligkeit, Gewandtheit und schnellen Füßen. Er hüpft auf dem rechten Fuß über eine Hürde und steigt dann seitlich über eine zweite Hürde hin und zurück. Nach der Landung auf dem rechten Fuß sprintet er sofort durch zwei Hütchen. Danach trabt er locker zurück zum Start.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern. Unten in der Mitte liegt die erste Hürde quer, links davon die zweite Hürde längs. Oben stehen zwei Hütchen als Sprinttor.",
  "Verteilen: Der Spieler steht unten vor der ersten Hürde. Der Trainer steht an der Seite und schaut zu.",
  "Ablauf: Rechts über die erste Hürde hüpfen, mit dem linken Fuß seitlich über die zweite Hürde steigen, zurücksteigen und auf dem rechten Fuß landen. Dann sofort durch die Hütchen sprinten.",
  "Wechsel: Nach dem Sprint trabt der Spieler außen zurück zum Start und beginnt den nächsten Lauf. Nach ein paar Läufen gibt es eine kurze Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Groß und im Gleichgewicht bleiben, die Hürde kontrolliert nehmen", "Kurze, schnelle und leichte Bodenkontakte", "Landen und sofort in den Sprint explodieren, die Arme kräftig mitnehmen", "Locker zurücktraben und jeden Lauf sauber neu starten"],
 "materials": ["2 Minihürden", "2 Hütchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Zwei Hürden, dann Sprint. Spieler sieben hüpft über eine Hürde, steigt seitlich über eine zweite und sprintet dann durch zwei Hütchen.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Hüpfer rechts", "Spieler sieben steht vor der ersten Hürde. Er hüpft auf dem rechten Fuß darüber.", *HUEPFER),
   S("Seitlich über die Hürde", "Dann geht er zur zweiten Hürde links und steigt mit dem linken Fuß seitlich darüber.", *LINKS),
   S("Zurück und landen", "Jetzt steigt er wieder zurück über die Hürde und landet auf dem rechten Fuß, genau in der Mitte.", *ZURUECK),
   S("Sprint durch die Hütchen", "Sofort nach der Landung sprintet Spieler sieben los, mit kräftigem Armeinsatz durch die zwei Hütchen.", *SPRINT),
   S("Zurücktraben", "Danach trabt er locker außen zurück zum Start. Dann ist Spieler sieben wieder dran, und der nächste Lauf beginnt. Nach ein paar Läufen gibt es eine kurze Pause.", *TRAB)],
  "dims": dims(30, 70, 10, 50, "9 m", "9 m", rx=76)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kurz und leicht über die Hürden.", "Kurz und leicht",
    "Über den Hürden bleibt der Spieler groß und im Gleichgewicht. Die Füße berühren den Boden nur ganz kurz und leicht. So bleibt er schnell und hat die Hürde unter Kontrolle.",
    sp(), ERSATZ,
    [S("Groß und leicht", "Spieler sieben hüpft über die erste Hürde und steigt seitlich über die zweite. Er bleibt groß, die Füße tippen nur kurz auf.", *(HUEPFER + [mv("n7", [43, 36], after=True), mv("n7", [33.5, 36], after=True)])),
     S("Sicher landen", "Zurück über die Hürde landet er sicher auf dem rechten Fuß. Der Oberkörper bleibt ruhig.", *ZURUECK)]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Landen und sofort explodieren.", "Landen und explodieren",
    "Nach der Landung gibt es keine Pause. Der Spieler drückt sich sofort ab und sprintet los. Die Arme schwingen kräftig mit, das macht ihn schneller.",
    sp(n7=(50, 30)), ERSATZ,
    [S("Landen und los", "Spieler sieben landet auf dem rechten Fuß und startet ohne Pause. Die Arme schwingen kräftig mit.", *SPRINT),
     S("Ruhig zurück", "Dann trabt er bewusst ruhig zurück, atmet durch und stellt sich wieder sauber an den Start.", *TRAB)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
