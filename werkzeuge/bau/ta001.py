import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# TA-001: erste Taktik-Erklärung (kind "Taktik", Inhaber 24.11.2026). Aufbau im 4-3-3 von hinten über den Torwart.
# Für Trainer U12 bis U17, etwa vier Minuten, drei Kapitel: 1 Grundordnung und Aufbau ohne Gegner, 2 gegen zwei anlaufende
# Stürmer (4-4-2, Sechser kippt ab, freier Mann, dritter Mann), 3 Verschieben und Seitenwechsel über den Torwart.
# Großfeld quer wie UE-319 (massstab "gross"): Team Neon baut links auf und spielt nach rechts. Von Team Neon aus gesehen ist
# oben die linke Seite (Linksverteidiger 3, Linksaußen 11), unten die rechte (Rechtsverteidiger 2, Rechtsaußen 7).
# Nummern wie im klassischen 4-3-3: 2 RV, 3 LV, 4 und 5 Innenverteidiger, 6 Sechser, 8 und 10 Achter, 7 RA, 9 Stürmer, 11 LA.
# Team Rot (4-4-2) neu nummeriert 12-21, beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Ein Trainer.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]
T = P("T", "c", 16, 55.3, "T")
ERSATZ = [B("s1", 19.5, 55.8), B("s2", 22, 55.8)]
f = lambda p: [p[0] + 0.6, p[1] + 0.6]  # Ball am Fuß

# Kapitel 1: kompakte Grundordnung in der eigenen Hälfte
GRUND = {"k1": (10.5, 27.5), "n5": (24, 21), "n4": (24, 34), "n3": (30, 8), "n2": (30, 47), "n6": (35, 27.5),
         "n10": (46, 17), "n8": (46, 38), "n11": (60, 7), "n7": (60, 48), "n9": (66, 27.5)}
# Aufbau-Ordnung: Feld groß gemacht (Ende von Kapitel 1, Start von Kapitel 2 und 3)
GROSS = {"k1": (10.5, 27.5), "n5": (19, 13.5), "n4": (19, 41.5), "n3": (40, 5), "n2": (40, 50), "n6": (30, 27.5),
         "n10": (44, 18), "n8": (44, 37), "n11": (68, 5), "n7": (68, 50), "n9": (72, 27.5)}
# Team Rot im 4-4-2, presst hoch (Kapitel 2)
ROT = {"k2": (88, 27.5), "r12": (80, 46), "r15": (80, 34), "r14": (80, 21), "r13": (80, 9),
       "r21": (54, 47), "r18": (54, 34), "r17": (54, 21), "r16": (54, 8), "r19": (27, 15), "r20": (27, 40)}
# Team Rot hat auf unsere rechte Seite (unten) verschoben (Kapitel 3)
ROT3 = {"k2": (88, 27.5), "r12": (80, 49), "r15": (80, 37), "r14": (80, 25.5), "r13": (83, 14),
        "r21": (49, 50.5), "r18": (54, 39), "r17": (56, 27), "r16": (60, 15), "r19": (26, 39.5), "r20": (33, 44)}
NEON3 = dict(GROSS, n2=(40, 50), n8=(44, 37), n4=(19, 41.5), n9=(72, 31))

def sp(*dicts):
    d = {}
    for x in dicts: d.update(x)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
def hin(wer, ziel, **k): return [mv(i, list(ziel[i]), **k) for i in wer]

u = {"title": "Aufbau im 4-3-3 über den Torwart", "code": "TA-001", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 4-3-3 von hinten auf? Zuerst siehst du, wer wo steht, wie der Torwart mitspielt und wie die Mannschaft das Feld groß macht. Dann laufen zwei Stürmer an: So entsteht hinten eine Überzahl, und so wird das Pressing überspielt. Zum Schluss geht es um das Verschieben und den Seitenwechsel über den Torwart.",
 "organisation": ["Grundordnung: Torwart, Viererkette, ein Sechser, zwei Achter, vorn ein Stürmer und zwei Flügelspieler.",
  "Hinten: Beim Aufbau gehen die Innenverteidiger breit bis an die Ecken vom Strafraum, die Außenverteidiger schieben hoch, der Torwart spielt mit.",
  "Mittelfeld: Der Sechser bietet sich zentral an oder lässt sich zwischen die Innenverteidiger fallen, die Achter stehen in den Halbräumen.",
  "Vorn: Die Flügelspieler bleiben breit an der Linie, der Stürmer drückt die gegnerische Abwehr nach hinten."],
 "organisation_show": ORG,
 "coaching_points": ["Feld groß machen: breit und tief stehen", "Offen annehmen, Kopf hoch vor dem Pass", "Hinten immer einer mehr als der Gegner", "Eine Seite zu? Über den Torwart verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Vier-drei-drei über den Torwart. Diesmal keine Übung, sondern das System. Wer steht wo, wie spielen wir von hinten heraus, und was tun wir, wenn der Gegner presst?",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(GRUND), "balls": [B("b1", 16.6, 55.9)] + ERSATZ,
  "dims": DIMS,
  "steps": [
   S("Wer steht wo im 4-3-3", "Der Trainer spielt dem Torwart den Ball. Wir stehen im Vier-drei-drei. Hinten die Viererkette, also zwei Innenverteidiger und außen die zwei Außenverteidiger. Davor der Sechser, daneben die zwei Achter. Vorn der Stürmer mit den beiden Flügelspielern.",
     ps("b1", f(GRUND["k1"]))),
   S("Das Feld groß machen", "Hat der Torwart den Ball, machen wir das Feld groß. Die Innenverteidiger gehen breit bis an die Ecken vom Strafraum. Die Außenverteidiger schieben hoch an die Seitenlinie. Vorn bleiben die Flügel ganz breit, und der Stürmer drückt die Abwehr nach hinten.",
     *hin(["n5", "n4", "n3", "n2", "n6", "n10", "n8", "n11", "n7", "n9"], GROSS)),
   S("Torwart auf den Innenverteidiger", "Der Torwart spielt flach zum rechten Innenverteidiger. Der nimmt den Ball offen an, mit dem Körper schon zum Spielfeld, und schaut sofort nach vorn.",
     ps("b1", f(GROSS["n4"])), bl("n4", [44, 44], delay=0.9)),
   S("Raus zum Außenverteidiger", "Außen an der Linie hat der Außenverteidiger Platz. Er bekommt den Ball. Gleichzeitig bietet sich der rechte Achter innen an, schräg vor ihm.",
     ps("b1", f(GROSS["n2"])), mv("n8", [50, 40], delay=0.3)),
   S("Das Dreieck auf der Seite", "Innenverteidiger, Außenverteidiger und Achter bilden ein Dreieck. Der Achter schaut zum Ball und bekommt ihn in den Fuß.",
     bl("n8", f(GROSS["n2"])), ps("b1", [50.6, 40.6], after=True)),
   S("Aufdrehen und nach vorn", "Erst nach der Annahme dreht der Achter auf. Der Blick geht nach vorn zum Flügelspieler, der in die Tiefe startet. So sind wir mit wenigen Pässen vom Torwart bis über die Mittellinie.",
     bl("n8", [76, 49], von=f(GROSS["n2"]), dauer=1.3), drehen("n8", [76, 49], delay=0.4), mv("n7", [76, 49], delay=0.6),
     ps("b1", [76.6, 49.6], after=True), mv("n9", [80, 30], delay=0.8))]},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Gegen zwei Stürmer",
    "Jetzt presst ein Gegner im 4-4-2 mit zwei Stürmern. Der Sechser lässt sich zwischen die Innenverteidiger fallen. Hinten sind wir dann zu dritt plus Torwart gegen zwei, einer ist immer frei. Über den freien Mann und den dritten Mann kommen wir durch das Pressing.",
    sp(GROSS, ROT), [B("b1", 11.1, 28.1)] + ERSATZ,
    [S("Zwei Stürmer laufen an", "Jetzt laufen zwei Stürmer an. Der Sechser lässt sich zwischen die Innenverteidiger fallen, und die gehen noch breiter. Hinten sind wir jetzt zu dritt plus Torwart gegen zwei. Einer von uns ist immer frei.",
       mv("n6", [20, 27.5]), mv("n5", [16, 8]), mv("n4", [16, 47]), mv("n3", [46, 4]), mv("n2", [46, 51]),
       mv("r19", [24, 18], delay=0.4), mv("r20", [24, 37], delay=0.4)),
     S("Den freien Mann finden", "Der Torwart spielt den Sechser an. Ein Stürmer läuft ihn sofort an. Damit ist der linke Innenverteidiger frei, und der Sechser legt direkt zu ihm.",
       ps("b1", [20.6, 28.1]), mv("r19", [22, 25], delay=0.5), ps("b1", [16.6, 8.6], after=True)),
     S("Andribbeln", "Der Innenverteidiger hat Platz. Er dribbelt an, bis ein Gegner kommt. Erst dann spielt er ab.",
       dr("n5", "b1", [32, 8]), mv("r16", [36, 15], delay=0.5)),
     S("Der dritte Mann", "Der Stürmer kommt entgegen und bekommt den Ball. Er lässt ihn direkt prallen auf den Achter, der mit Blick nach vorn mitläuft. Das ist der dritte Mann.",
       mv("n9", [60, 17]), ps("b1", [60.6, 17.6], delay=0.4), mv("n10", [52, 13], delay=0.4), ps("b1", [52.6, 13.6], after=True)),
     S("Steil in die Tiefe", "Jetzt geht es schnell. Der Achter spielt den linken Flügelspieler in die Tiefe an. Mit wenigen Pässen ist das Pressing überspielt.",
       mv("n11", [84, 15]), ps("b1", [84.6, 15.6], delay=0.4))]),
  V("Kapitel 3", "Kapitel drei: Verschieben und Seitenwechsel.", "Verlagern über den Torwart",
    "Der Gegner schiebt mit allen auf unsere Ballseite. Dort ist es eng, auf der anderen Seite ist Platz. Wir spielen zurück über den Innenverteidiger zum Torwart und verlagern auf die freie Seite. Danach schiebt die ganze Mannschaft mit.",
    sp(NEON3, ROT3), [B("b1", 40.6, 50.6)] + ERSATZ,
    [S("Der Gegner schiebt zum Ball", "Unser rechter Außenverteidiger hat den Ball, und der Gegner schiebt mit allen auf diese Seite. Dort wird es eng. Auf der anderen Seite bleiben unser Außenverteidiger und der Flügelspieler trotzdem breit. Da ist jetzt der Platz.",
       mv("r21", [44, 50.5]), mv("r18", [50, 40], delay=0.2), mv("r20", [25, 38], delay=0.3), mv("r17", [52, 31], delay=0.3)),
     S("Zurück über den Torwart", "Also kein Pass in die enge Seite. Der Ball geht zurück zum Innenverteidiger und weiter zum Torwart. Das ist kein Rückschritt, so verlagern wir das Spiel.",
       ps("b1", f(NEON3["n4"])), ps("b1", f(NEON3["k1"]), after=True), mv("r19", [20, 30], delay=0.8)),
     S("Seitenwechsel", "Der Torwart spielt zum linken Innenverteidiger, und der sofort weiter auf den Außenverteidiger. Der Gegner muss quer über das ganze Feld schieben. Unser Außenverteidiger hat Zeit und Platz.",
       ps("b1", f(NEON3["n5"])), ps("b1", f(NEON3["n3"]), after=True), mv("r16", [52, 10], delay=1.2), mv("r17", [54, 20], delay=1.2)),
     S("Die Mannschaft schiebt mit", "Jetzt schiebt die ganze Mannschaft auf die neue Seite. Der Achter bietet sich an, der Flügelspieler startet in die Tiefe. So greifen wir dort an, wo der Gegner gerade nicht ist.",
       dr("n3", "b1", [50, 5]), mv("n10", [56, 14], delay=0.3), mv("n11", [80, 6], delay=0.3), mv("n6", [38, 22], delay=0.3),
       mv("n9", [76, 22], delay=0.4), mv("n8", [50, 30], delay=0.4))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
