import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P3 (U12-U14, Woche 37 Phase 1): 2 V 2 + 2 Rondo. 10 x 15 Yards (PDF; Ton: 6 x 8 Yards) = Feld x 33.5-66.5, y 5-55
# (9 x 14 m), Ausrichtung wie im PDF/Video. Hellblau (5, 2, an den Seiten) -> Neon, Rot/Dunkelblau (8, 9, innen) -> Rot,
# Pink/Gelb (Springer oben und unten) -> neutrale Springer F. Gelb 9 wird dadurch zum Springer, keine doppelte Nummer.
# Positionen leicht verschoben (3D-Abstand). Ein Trainer. Kein Duplikat von UE-017 (zwei Quadrate, 2 gegen 1) oder UE-099
# (Pressen und Absichern an Dummys): hier ein Feld, Springer oben und unten, zehn Pässe = Punkt, Ballgewinn = hinausdribbeln.
# Grundform nach Video 0:10-0:31 (Springer unten -> Neon 5 -> Springer oben; Rot fängt ab und dribbelt hinaus). Wechsel der Paare
# nach zwei Minuten ergänzt (Original: "rotating roles", ohne Zeit). Fassungen: "Defenders split apart - penetrating pass through"
# (Video 0:45-1:01, mit Klatschpass) und Progression (Ballverlust = sofort verteidigen, Video 1:01-1:25).
# Sichtkegel: Im Video ist nur ein Deckungsschatten hinter Rot 8 eingezeichnet, kein Blickkegel. Aus Ton/Text ("anticipate passes",
# "defensive awareness") in der Steigerung: Spieler neun schaut vor dem Abfangen zum Springer am Ball.
T = P("T", "c", 24, 9, "T")
POS = {"f1": (50, 5), "f2": (50, 55), "n5": (33.5, 36), "n2": (66.5, 22), "r8": (44, 32), "r9": (54, 38)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 25.6, 5.5), B("s2", 22, 5.5)]
LINES = [rect(33.5, 5, 33, 50)]
CONES = ecken(33.5, 5, 33, 50)

u = {"title": "Rondo zu zweit mit Springern", "code": "UE-233", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 6, "field_size": "9 x 14 m",
 "description": "Ein Rondo zwei gegen zwei plus zwei auf engem Raum. Team Neon steht an den Seiten, zwei Springer oben und unten, und zusammen wollen sie zehn Pässe in Folge schaffen. Team Rot presst zu zweit in der Mitte, und wer den Ball erobert, dribbelt schnell aus dem Feld. Nach zwei Minuten wechseln die drei Paare die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern mit vier Hütchen an den Ecken.",
  "Verteilen: Drei Paare. Die Springer stehen oben und unten auf der Linie, Team Neon links und rechts an der Seite, Team Rot in der Mitte. Der Trainer steht an der Ecke mit Bällen.",
  "Ablauf: Team Neon und die Springer spielen sich den Ball außen herum zu. Team Rot presst zu zweit und will den Ball erobern.",
  "Wertung und Wechsel: Zehn Pässe in Folge gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und dribbelt aus dem Feld, gibt das einen Punkt für Team Rot. Nach zwei Minuten wechseln die Paare die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Zu zweit pressen, die Richtung vorgeben und den nächsten Pass ahnen", "Beim Verteidigen viel reden und die Lücken schließen", "Scharfe, genaue Pässe auf den richtigen Fuß", "Stehen die Verteidiger eng, außen herum spielen, stehen sie weit auseinander, durch die Mitte"],
 "materials": ["4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Rondo zu zweit mit Springern. Team Neon spielt mit zwei Springern gegen Team Rot und will zehn Pässe in Folge schaffen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 55.6)] + ERSATZ,
  "steps": [
   S("Über die Seite", "Der Springer unten spielt zu Spieler fünf, und Spieler fünf spielt direkt weiter zum Springer oben. Gleichzeitig verschieben Spieler acht und Spieler neun zum Ball.",
     ps("b1", [34.1, 36.6]), mv("r8", [45, 28], delay=0.3), mv("r9", [53, 34], delay=0.3), ps("b1", [50.6, 5.6], after=True)),
   S("Zehn Pässe: Punkt", "Der Springer oben spielt zu Spieler zwei, und der spielt zurück zum Springer unten. So geht es immer weiter. Schafft Team Neon zehn Pässe in Folge, gibt das einen Punkt für Team Neon.",
     ps("b1", [67.1, 22.6]), mv("r8", [44, 32], delay=0.3), mv("r9", [54, 38], delay=0.3), ps("b1", [50.6, 55.6], after=True)),
   S("Abgefangen", "Jetzt spielt der Springer unten wieder zu Spieler fünf. Aber Spieler acht ahnt den Pass, läuft in den Passweg und fängt den Ball ab.",
     mv("r8", [42, 46]), ps("b1", [42.6, 46.6], delay=0.3)),
   S("Hinaus dribbeln: Punkt", "Spieler acht dribbelt schnell aus dem Feld, bevor Spieler fünf ihn erreicht, und das gibt einen Punkt für Team Rot. Dann beginnt der Springer unten mit einem neuen Ball, und nach zwei Minuten wechseln die Paare die Rollen.",
     dr("r8", "b1", [27, 50]), mv("n5", [33, 43], delay=0.2))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Stehen die Verteidiger weit auseinander, durch die Mitte spielen.", "Durch die Lücke",
    "Stehen die beiden Verteidiger eng zusammen, spielt Team Neon außen herum. Stehen sie weit auseinander, ist in der Mitte eine Lücke. Mit einem kurzen Klatschpass lockt Team Neon einen Verteidiger an, dann geht der Ball flach durch die Mitte.",
    sp(), [B("b1", 50.6, 55.6)] + ERSATZ,
    [S("Weit auseinander", "Spieler acht und Spieler neun stehen weit auseinander. Der Springer unten spielt zu Spieler fünf.",
       mv("r8", [42, 28]), mv("r9", [58, 30]), ps("b1", [34.1, 36.6], delay=0.3)),
     S("Klatschen lassen", "Spieler fünf spielt direkt zurück zum Springer unten. Spieler acht schiebt zu Spieler fünf, und die Lücke in der Mitte wird noch größer.",
       ps("b1", [50.6, 55.6]), mv("r8", [41, 27], delay=0.2)),
     S("Durch die Mitte", "Der Springer unten spielt flach durch die Lücke zum Springer oben. Beide Verteidiger sind überspielt, und Team Neon zählt weiter bis zehn.",
       ps("b1", [50.6, 5.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball verliert, verteidigt sofort.", "Ball weg, sofort verteidigen",
    "Jetzt gibt es kein Hinausdribbeln mehr. Erobert Team Rot den Ball, geht es sofort an die Seiten und spielt mit den Springern. Team Neon kommt gleichzeitig in die Mitte und presst. Wer schneller umschaltet, gewinnt.",
    sp(), [B("b1", 50.6, 55.6)] + ERSATZ,
    [S("Pass ahnen", "Der Springer unten hat den Ball. Spieler neun schaut genau hin, wohin er spielen will, läuft in den Passweg zu Spieler zwei und fängt den Ball ab.",
       bl("r9", [50.5, 54]), mv("r9", [58.5, 40], after=True), ps("b1", [59.1, 40.6], delay=0.3)),
     S("Rollen tauschen", "Alle schalten gleichzeitig um. Spieler neun dribbelt an die rechte Seite, Spieler acht läuft an die linke. Spieler fünf und Spieler zwei kommen sofort in die Mitte.",
       dr("r9", "b1", [66.5, 42]), mv("r8", [33.5, 20]), mv("n5", [44, 36]), mv("n2", [55, 26])),
     S("Jetzt zählt Rot: Punkt", "Spieler neun spielt zum Springer unten, und Team Neon presst zu zweit. Schafft Team Rot zehn Pässe in Folge, gibt das einen Punkt für Team Rot. Erobert Team Neon den Ball zurück, wechseln die Rollen wieder.",
       ps("b1", [50.6, 55.6]), mv("n5", [40, 42], delay=0.2), mv("n2", [56, 36], delay=0.2))])]}
u["board"]["dims"] = dims(33.5, 66.5, 5, 55, "9 m", "14 m")
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
