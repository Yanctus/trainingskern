import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 76-P2: 30 x 40 Yards, gedreht (Tor unten -> rechts, PDF rechts -> oben): x 31-71.5, y 3-57 (1,35 je Yard).
GK = P("tw", "b", 69.5, 30.6, "1"); T = P("T", "c", 87, 10, "T"); cb = [B("c1", 89, 13), B("c2", 89.5, 7.5)]
lines = [rect(31, 3, 40.5, 54), rect(57.4, 9.4, 14.1, 41), rect(65.1, 20.4, 6.4, 19)]
stangen = [(34.4, 22.3), (39.9, 21.3), (44.2, 22.3), (49.7, 21.3), (54.8, 22.3), (32.5, 7.5), (39.6, 7.5), (44.5, 6.2), (49, 7.5), (54.2, 6.2)]
cones = [C(x, y, shape="stange") for x, y in stangen] + [C(34.2, 29.4), C(39, 38.9), C(43.1, 38.9), C(47.5, 38.9), C(52.1, 38.9)]
stationen = [P("n10", "a", 34.4, 24.3, "10"), P("n8", "a", 44.2, 24.3, "8"), P("n11", "a", 54.8, 24.3, "11"), P("n2", "a", 39.6, 5.5, "2"), P("n5", "a", 49, 5.5, "5")]
schlange = [P("n7", "a", 68.5, 3.3, "7"), P("n3", "a", 77, 3.3, "3"), P("n4", "a", 78.5, 19, "4")]
u = {"title": "Dribbel-Parcours mit Abschluss", "code": "UE-067", "kind": "Übungsform",
 "focuses": ["Dribbling", "Torschuss", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 37 m",
 "description": "Zwischen zwei Reihen Stangen stehen Spieler abwechselnd links und rechts. Jeder dribbelt quer zur gegenüberliegenden Stange und legt den Ball kurz zum nächsten Spieler ab, so wandert der Ball im Zickzack nach vorn. Der letzte Spieler dribbelt um die letzte Stange, im Slalom durch die Hütchen und schließt im Strafraum gegen den Torwart ab, das gibt einen Punkt. Danach holt er sich am Start einen neuen Ball, so bleiben alle in Bewegung.",
 "organisation": ["Aufbauen: Ein Tor mit Torwart, davor der Strafraum. Zwei Reihen mit je fünf Stangen und fünf Hütchen für den Slalom wie in der Skizze.",
  "Verteilen: Je ein Spieler steht an jeder Stange, die übrigen warten mit Bällen am Start neben dem Strafraum. Ich stehe mit weiteren Bällen daneben.",
  "Ablauf: Quer dribbeln, kurz ablegen, der Nächste macht weiter. Der letzte Spieler dribbelt um die letzte Stange, durch die Hütchen und schließt ab.",
  "Wechseln: Wer abgeschlossen hat, holt sich am Start einen Ball, alle rücken eine Station weiter. Niemand steht lange still."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball beim Dribbeln eng am Fuß führen", "Mit dem vorderen Fuß annehmen und sofort losdribbeln", "Kurze Pässe genau und mit dem richtigen Tempo spielen", "Vor dem Abschluss den Kopf heben und den Torwart sehen"],
 "materials": ["1 Tor", "10 Stangen", "5 Hütchen", "Bälle am Start", "Leibchen für den Torwart"],
 "access": "frei", "hidden": True,
 "say_intro": "Dribbel-Parcours mit Abschluss. Hier wandert der Ball im Zickzack durch die Stangen, und der Letzte schließt gegen den Torwart ab.",
 "board": {"lines": lines, "cones": cones, "goals": [{"x": 71.5, "y": 30, "side": "right"}],
  "players": [GK, P("n9", "a", 60, 3.3, "9"), *stationen, *schlange, T], "balls": [B("b1", 60, 4.9), *cb],
  "steps": [
   S("Quer dribbeln, kurz ablegen", "Spieler neun dribbelt quer zur anderen Stange und legt kurz auf Spieler elf ab. Der dribbelt zurück und legt auf Spieler fünf ab.",
     dr("n9", "b1", [59, 21.5]), ps("b1", [55.5, 23.6], after=True), dr("n11", "b1", [54.2, 8.6], after=True), ps("b1", [49.8, 6], after=True)),
   S("Weiter im Zickzack", "So geht es im Zickzack weiter: Spieler fünf legt auf Spieler acht ab, und Spieler acht auf Spieler zwei.",
     dr("n5", "b1", [49.7, 19.3]), ps("b1", [45, 23.6], after=True), dr("n8", "b1", [44.5, 8.6], after=True), ps("b1", [40.3, 6], after=True)),
   S("Ablage auf die Zehn", "Spieler zwei dribbelt quer und legt auf Spieler zehn ab, den letzten in der Reihe.",
     dr("n2", "b1", [39.9, 19.3]), ps("b1", [35.1, 23.6], after=True)),
   S("Um die letzte Stange herum", "Spieler zehn dribbelt um die letzte Stange herum und zieht dann Richtung Hütchen.",
     dr("n10", "b1", [36.5, 12]), dr("n10", "b1", [35.5, 3.8], after=True), dr("n10", "b1", [30, 4.2], after=True), dr("n10", "b1", [29.5, 12], after=True), dr("n10", "b1", [31.5, 27], after=True)),
   S("Slalom durch die Hütchen", "Mit kurzen Ballkontakten dribbelt er im Slalom durch die Hütchen.",
     dr("n10", "b1", [32, 31.5]), dr("n10", "b1", [39, 41.2], after=True), dr("n10", "b1", [43.1, 36.6], after=True), dr("n10", "b1", [47.5, 41.2], after=True), dr("n10", "b1", [52.1, 36.6], after=True), dr("n10", "b1", [55.5, 40], after=True)),
   S("Abschluss gegen den Torwart: Punkt", "Im Strafraum hebt er den Kopf und schießt am Torwart vorbei ins Eck, und das gibt einen Punkt.",
     dr("n10", "b1", [60, 35]), ps("b1", [73.5, 27.5], after=True), mv("tw", [69.5, 33], delay=0.5))],
  "dims": [{"x1": 31, "y1": 58.6, "x2": 71.5, "y2": 58.6, "text": "27 m"}, {"x1": 93, "y1": 3, "x2": 93, "y2": 57, "text": "37 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor dem Abschluss den Kopf heben und sehen, wo der Torwart steht.", "Kopf hoch, Torwart sehen",
    "Wer früh den Kopf hebt, sieht, wo der Torwart steht und welches Eck frei ist. Danach richtet der Stürmer seinen Körper aus und wählt den passenden Schuss. Genau ins Eck ist besser als fest in die Mitte.",
    [GK, P("n10", "a", 58.5, 40, "10"), P("n9", "a", 60, 3.3, "9"), P("n8", "a", 44.2, 24.3, "8"), P("n11", "a", 54.8, 24.3, "11"), P("n2", "a", 39.6, 5.5, "2"), P("n5", "a", 49, 5.5, "5"), *schlange, T],
    [B("b1", 60, 39.4), *cb],
    [S("Kopf hoch", "Spieler zehn hebt den Kopf und sieht, dass der Torwart zur Mitte hin steht.", dr("n10", "b1", [61, 36.5]), mv("tw", [68.5, 33.5], delay=0.2)),
     S("Ins freie Eck: Punkt", "Also schiebt er den Ball flach ins freie Eck, und das gibt einen Punkt.", ps("b1", [73.5, 26]))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Doppelpass an der Stange, dann legt der Trainer zum Direktabschluss auf.", "Doppelpass und Direktabschluss",
    "Statt quer zu dribbeln, spielen die Spieler an der Stange einen schnellen Doppelpass. Danach spielt der Stürmer den Ball zu mir in den Strafraum, ich lege ihm den Ball auf, und er schließt direkt ab. Das schult Timing, Genauigkeit und Ruhe vor dem Tor.",
    [GK, P("n9", "a", 60, 3.3, "9"), P("n11", "a", 57.8, 25.4, "11"), P("n10", "a", 34.4, 24.3, "10"), P("n8", "a", 44.2, 24.3, "8"), P("n2", "a", 39.6, 5.5, "2"), P("n5", "a", 49, 5.5, "5"),
     *schlange, P("T", "c", 61.2, 47.7, "T")],
    [B("b1", 60, 4.9), B("c1", 64, 49.5)],
    [S("Doppelpass an der Stange", "Spieler neun spielt auf Spieler elf und startet sofort, Spieler elf spielt direkt zurück in den Lauf.",
       ps("b1", [57.6, 23.8]), mv("n9", [56.5, 13], delay=0.2), ps("b1", [56.3, 14.5], after=True)),
     S("Pass zum Trainer", "Spieler neun dribbelt Richtung Strafraum und spielt den Ball zu mir.", dr("n9", "b1", [62.5, 30]), ps("b1", [61, 46], after=True)),
     S("Ablage und Direktabschluss: Punkt", "Ich lege ihm den Ball auf, und er schließt direkt ab, das gibt einen Punkt.",
       mv("n9", [62, 38]), ps("b1", [62.5, 37], delay=0.25), ps("b1", [73.5, 32], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
