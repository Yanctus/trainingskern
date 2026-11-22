import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-30 (U12-U14, Woche 4 Pre-Season): Speed Work & 1-2 Combinations. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m).
# Station 1 oben (Passgeber), Station 2 unten, Station 3 rechts (Leiter + Hürden als Minihürden), Station 4 links (Stangen + Ringe).
# Ablauf als Kreislauf gedeutet: oben passt nach unten und läuft über Leiter und Hürden nach unten, unten passt steil nach oben
# und läuft über Stangen und Ringe nach oben. Wartende auseinandergezogen (3D-Abstand). Ein Trainer.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 80, 52, "T")
POS = {"n4": (51, 11.5), "n2": (60, 4), "n3": (69, 1.5), "n8": (68.4, 17.5),
       "n9": (51, 47), "n11": (60, 51), "n10": (69, 53), "n7": (30.8, 39.6)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b1", 51.6, 12.1), B("s1", 81.6, 55), B("s2", 84, 52)]
RINGE = [{"type": "circle", "x": x, "y": y, "r": 2} for x, y in ((30.7, 14.5), (33.7, 10.8), (38.4, 8.7))]
LINES = [rect(25, 5, 50, 50)] + RINGE
KEGEL = [C(48, 12.4), C(48, 48.4), C(39.6, 24.8)] \
      + [C(31, y, "neon", shape="stange") for y in (22, 28.5, 35)] + [C(45.3, 30.1, "neon", shape="stange"), C(56.9, 30.1, "neon", shape="stange")] \
      + [C(68.4, y, shape="huerde_ou") for y in (20, 23, 26)] + [C(68.4, y, shape="huerde_ou") for y in (30.7, 34.6, 38.4, 42.4)]
STANGEN = [[34.5, 35], [27.5, 28.5], [34.5, 22], [30.7, 14.5], [33.7, 10.8], [38.4, 8.7], [44, 6]]  # Slalom, dann durch die Ringe
LEITER = [[68.4, 19], [68.4, 45], [66, 48.5]]  # Leiter und Hürden nach unten
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Passkreis mit Leiter", "code": "UE-137", "kind": "Übungsform",
 "focuses": ["Passspiel", "Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "18 x 18 m",
 "description": "Ein Kreislauf mit vier Stationen. Oben und unten in der Mitte stehen die Passstationen, zwischen ihnen zwei Dummys. Rechts liegen Leiter und Hürden, links stehen Stangen und Ringe. Der obere Spieler passt zwischen den Dummys hindurch nach unten und läuft über Leiter und Hürden zur unteren Station. Der untere Spieler nimmt an, spielt steil zum nächsten oben und läuft durch Stangen und Ringe zur oberen Station. So bleibt alles in Bewegung, bis der Trainer eine Pause ansagt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben und unten in der Mitte je ein Hütchen als Passstation, dazwischen zwei Dummys. Rechts eine Leiter und vier Minihürden, links drei Stangen für den Slalom und drei Ringe.",
  "Verteilen: Auf jeder Station stehen Spieler, oben und unten zwei bis drei. Der erste Spieler oben hat den Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Oben passt zwischen den Dummys nach unten und läuft über Leiter und Hürden zur unteren Station. Unten nimmt an, spielt steil zum Nächsten oben und läuft durch Stangen und Ringe zur oberen Station.",
  "Pausen: Gespielt wird mit hohem Tempo, bis der Trainer eine Erholungspause ansagt. Danach geht es mit dem Fuß weiter, der vorher nicht gespielt hat."],
 "organisation_show": ORG,
 "coaching_points": ["Genau passen, damit der Mitspieler den Ball gut annehmen kann", "Im richtigen Moment zum Ball starten", "Mit beiden Füßen abwechselnd passen", "Mit hohem Tempo und sauberen Schritten durch Leiter, Hürden, Stangen und Ringe"],
 "materials": ["3 Hütchen", "2 Dummys", "3 Stangen", "3 Ringe", "1 Koordinationsleiter", "4 Minihürden", "Mehrere Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Passkreis mit Leiter. Pässe durch die Mitte, dann über Leiter, Hürden, Stangen und Ringe, und alles bleibt in Bewegung.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Pass nach unten", "Neon vier spielt zwischen den Dummys hindurch zu Neon neun, der dem Ball entgegenkommt. Gleichzeitig läuft Neon acht über Leiter und Hürden nach unten und Neon sieben durch Stangen und Ringe nach oben.",
     ps("b1", [52.6, 40.6]), mv("n9", [52, 40]), *weg("n8", LEITER), *weg("n7", STANGEN, delay=0.2)),
   S("Steil nach oben", "Neon neun spielt steil nach oben zu Neon zwei, der zum Hütchen kommt. Neon vier läuft jetzt über Leiter und Hürden nach unten, Neon neun startet zu den Stangen.",
     mv("n2", [52, 14.5]), ps("b1", [52.6, 15.1], delay=0.2), *weg("n4", [[60, 13], [66, 17]] + LEITER, delay=0.1), *weg("n9", [[40, 43], [30.8, 40.5]], delay=0.4)),
   S("Immer weiter im Kreis", "Jetzt spielt Neon zwei nach unten zu Neon elf, und alles beginnt von vorn. So bleibt der Ball in Bewegung, bis der Trainer eine Pause ansagt.",
     mv("n11", [52.5, 40.5]), ps("b1", [53.1, 41.1], delay=0.2), mv("n2", [60, 13], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau und mit Tempo passen.", "Der Pass durch die Mitte",
    "Der Pass zwischen den Dummys hindurch muss genau und fest sein. Zu lasch, und der Mitspieler muss warten, zu ungenau, und der Ball prallt an einem Dummy ab. Dabei abwechselnd mit rechts und links passen.",
    sp(), BAELLE,
    [S("Fest und genau", "Neon vier spielt den Ball fest und genau zwischen den Dummys hindurch, Neon neun kommt entgegen und nimmt ihn sauber an.",
       ps("b1", [52.6, 40.6]), mv("n9", [52, 40])),
     S("Mit dem anderen Fuß zurück", "Neon neun spielt mit dem anderen Fuß genauso fest steil nach oben zu Neon zwei. Dann laufen beide zu ihrer Station.",
       mv("n2", [52, 14.5]), ps("b1", [52.6, 15.1], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Tempo und saubere Schritte.", "Schnelle Füße",
    "Durch Leiter, Hürden, Stangen und Ringe geht es mit voller Geschwindigkeit, aber sauber: kurze, schnelle Schritte, Arme mitnehmen, auf den Fußballen bleiben. Wer schlampig läuft, verliert Zeit und kommt zu spät zur nächsten Station.",
    sp(), BAELLE,
    [S("Leiter und Hürden", "Neon acht läuft mit kurzen, schnellen Schritten durch die Leiter und über die Hürden nach unten.",
       *weg("n8", LEITER)),
     S("Stangen und Ringe", "Gleichzeitig läuft Neon sieben im Slalom um die Stangen und durch die Ringe nach oben. Beide kommen mit Tempo an ihrer neuen Station an.",
       *weg("n7", STANGEN))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
