import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P5 (U12-U14, Torwarttraining): Handling, Speed and Reactions ("Goalkeeper Handling Speed Reactions GK- 5"). 18 x 45 Yards
# (Strafraum), gedreht: im PDF liegt das Tor links, hier oben (wie im Video). Feld x 16-84, y 5-55 (41 x 16 m, nicht maßstäblich),
# innerer Kasten x 28-72, y 5-27 mit zwei Minitoren auf seiner unteren Linie (Öffnung zum Feld, zu den Schützen).
# Drei Torhüter neutral: k1 (grün 1, arbeitet), k2 (pink 1, schießt rechts), k3 (gelb 13, schießt links), Nummern weggelassen.
# Ein Trainer statt zwei (PDF und Video zeigen einen zweiten Trainer oben, ohne Aufgabe): Er wirft die Tennisbälle und spielt den
# Volley. Er steht leicht rechts der Mitte, damit die Würfe nicht durch die Hütchenreihe gehen. Hütchenreihe mit drei Hütchen wie
# im PDF (im Video vier). Ball zurück: im PDF "rolling", im Ton "throwing" -> werfen. Wechsel wie im Video: der Torwart im Tor geht
# nach links, der linke nach rechts, der rechte ins Tor. Keine Wertung (Technikübung, Ziel statt Punkte).
# GK-13 hat einen fast gleichen Namen, ist aber eine andere Übung (Hütchen antippen, zweites Tor quer): eigene Einheit UE-258.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 62, 43, "T")
POS = {"k1": (50, 8), "k2": (78, 47), "k3": (22, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 65.6, 46.5), B("s2", 58.4, 46.5)]
def baelle(b1=(62.6, 43.6), tb1=(60.6, 40), tb2=(63.6, 40)):
    return [B("tb1", *tb1), B("tb2", *tb2), B("b1", *b1), B("b2", 78.6, 47.6), B("b3", 22.6, 47.6)] + ERSATZ
LINES = [rect(16, 5, 68, 50), rect(28, 5, 44, 22)]
CONES = [C(44, 9), C(56, 9), C(50, 14), C(50, 20), C(50, 26), C(30, 18), C(70, 18)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 36, "y": 27, "side": "top"}, {"x": 64, "y": 27, "side": "top"}]

u = {"title": "Tennisbälle, Slalom, Paraden", "code": "UE-257", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 3,
 "field_size": "41 x 16 m",
 "description": "Ein Zirkel für Torhüter im Strafraum. Der Torwart fängt zuerst Tennisbälle vom Trainer, läuft dann mit schnellen Füßen durch eine Hütchenreihe und fängt einen Volley. Danach sprintet er um ein Hütchen und hält einen flachen Schuss vor dem Minitor, steht schnell auf und hält auch auf der anderen Seite. Drei Torhüter wechseln sich ab, und wer nicht im Tor ist, schießt.",
 "organisation": ["Aufbauen: Im Strafraum ein Jugendtor mit je einem Hütchen links und rechts neben dem Torwart und eine Reihe aus drei Hütchen nach vorn. Weiter vorn zwei Minitore mit der Öffnung zum Feld, außen daneben je ein Hütchen.",
  "Verteilen: Der erste Torwart steht im Tor. Der zweite Torwart steht rechts, der dritte links, beide mit Bällen. Der Trainer steht vorn mit Tennisbällen und Bällen.",
  "Ablauf: Tennisbälle fangen und auf die Hütchen legen, im Slalom durch die Hütchenreihe, den Volley fangen und zurückwerfen. Dann um das rechte Hütchen sprinten und den Schuss vor dem Minitor halten, aufstehen und links dasselbe.",
  "Wechsel: Nach beiden Paraden wird neu aufgebaut. Der rechte Torwart geht ins Tor, der linke rückt nach rechts, und der erste Torwart schießt jetzt von links."],
 "organisation_show": ORG,
 "coaching_points": ["Tennisbälle mit weichen Händen fangen", "Schnelle, saubere Schritte durch die Hütchen", "Im richtigen Moment hechten und den Ball festhalten", "Ruhig und genau zum Trainer zurückwerfen, nicht hetzen"],
 "materials": ["1 Jugendtor", "2 Minitore", "7 Hütchen", "2 Tennisbälle", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Tennisbälle, Slalom, Paraden. Der Torwart fängt, läuft durch die Hütchen und hält zwei Schüsse vor den Minitoren.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Tennisbälle fangen", "Der erste Torwart steht auf der Torlinie. Der Trainer wirft ihm einen Tennisball zu. Er fängt ihn mit weichen Händen und legt ihn auf das Hütchen neben sich. Den zweiten Tennisball legt er auf das Hütchen auf der anderen Seite.",
     ps("tb1", [50.6, 8.6]), ps("tb1", [44, 9], after=True), ps("tb2", [50.6, 8.6], after=True), ps("tb2", [56, 9], after=True)),
   S("Schnelle Füße", "Jetzt läuft er mit kurzen, schnellen Schritten im Slalom durch die Hütchenreihe nach vorn.",
     mv("k1", [47, 14]), mv("k1", [53, 20], after=True), mv("k1", [47, 26], after=True), mv("k1", [50, 31], after=True)),
   S("Volley fangen", "Der Trainer spielt ihm einen Volley zu. Der Torwart fängt den Ball, hält ihn fest und wirft ihn genau zum Trainer zurück.",
     ps("b1", [50.6, 31.6]), ps("b1", [62.6, 43.6], after=True)),
   S("Erste Parade", "Dann sprintet er zu seiner linken Seite um das äußere Hütchen und stellt sich vor das Minitor. Der zweite Torwart schießt flach, und der erste Torwart hechtet und hält den Ball.",
     mv("k1", [58, 22]), mv("k1", [66, 13], after=True), mv("k1", [74, 15], after=True), mv("k1", [75, 23], after=True),
     mv("k1", [66, 30], after=True), ps("b2", [66.6, 30.6], after=True)),
   S("Zweite Parade und Wechsel", "Schnell wieder aufstehen! Er sprintet hinüber um das Hütchen auf der anderen Seite, und der dritte Torwart schießt aufs andere Minitor. Hält er auch diesen Ball, ist die Runde geschafft. Dann wird neu aufgebaut, und der zweite Torwart ist im Tor dran.",
     mv("k1", [52, 32]), mv("k1", [42, 24], after=True), mv("k1", [34, 13], after=True), mv("k1", [26, 15], after=True),
     mv("k1", [25, 23], after=True), mv("k1", [34, 30], after=True), ps("b3", [34.6, 30.6], after=True))],
  "dims": dims(16, 84, 5, 55, "41 m", "16 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Sauber hechten und den Ball festhalten.", "Sauber hechten",
    "Der Torwart kommt um das Hütchen und stellt sich vor das Minitor, die Knie leicht gebeugt. Beim Schuss stößt er sich mit dem Bein auf der Ballseite ab und fliegt seitlich zum Ball. Er fängt ihn mit beiden Händen und drückt ihn fest an sich.",
    sp(k1=(75, 23)), baelle(tb1=(44, 9), tb2=(56, 9)),
    [S("Vor das Minitor", "Der Torwart kommt um das Hütchen und stellt sich vor das Minitor. Die Knie sind leicht gebeugt, die Hände vor dem Körper.",
       mv("k1", [68, 30])),
     S("Hechten und festhalten", "Der zweite Torwart schießt flach neben ihn. Der Torwart stößt sich ab, fliegt seitlich zum Ball, fängt ihn mit beiden Händen und hält ihn fest.",
       ps("b2", [63.6, 31.6]), mv("k1", [63, 31], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Genau zurückwerfen, nicht hetzen.", "Genau zurückwerfen",
    "Wer schnell zur nächsten Parade will, wirft oft hastig und ungenau. Besser ist es, den Ball ruhig und genau zum Trainer zu werfen und erst dann loszusprinten. So bleibt die Technik sauber, und der Zirkel läuft flüssig weiter.",
    sp(k1=(50, 31)), baelle(b1=(50.6, 31.6), tb1=(44, 9), tb2=(56, 9)),
    [S("Ruhig werfen", "Der Torwart hat den Volley gefangen. Er wirft den Ball ruhig und genau in die Hände des Trainers.",
       ps("b1", [62.6, 43.6])),
     S("Dann lossprinten", "Erst danach sprintet er los zum Hütchen. Ein hastiger Wurf landet daneben, und der Trainer muss dem Ball hinterherlaufen.",
       mv("k1", [58, 22]), mv("k1", [66, 13], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
