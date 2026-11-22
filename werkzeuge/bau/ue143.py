import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-88 (U12-U14, Woche 6 Pre-Season): Agility and Speed Circuit. 25 x 25 Yards = Feld x 25-75, y 5-55 (23 m).
# Zwei Vierergruppen an gegenüberliegenden Ecken (im Original beide Pink): unten links -> Neon (11, 10, 8, 5), oben rechts -> Rot
# (4, 9, 7, 6), damit man die beiden Läufer unterscheidet. Leiter diagonal als vier Minihürden, Hürden diagonal. Wartende in einer
# Reihe daneben (3D-Abstand). Ein Trainer statt zwei. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 12, 22, "T")
POS = {"n11": (27, 46), "n10": (18.5, 46), "n8": (10, 46), "n5": (1.5, 46), "r4": (73, 8), "r9": (81.5, 8), "r7": (90, 8), "r6": (98.5, 8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b11", 27.6, 46.6), B("b4", 73.6, 8.6), B("s1", 13.6, 25), B("s2", 10, 25)]
LINES = [rect(25, 5, 50, 50)]
C1, C2 = (44.4, 34), (52.9, 24.4)
KEGEL = [C(28.5, 10.8), C(70.1, 10.8), C(28.5, 48.9), C(70.2, 48.9), C(*C1), C(*C2)] \
      + [C(x, y, shape="huerde_ou") for x, y in ((34.5, 14.5), (37, 17.2), (39.5, 19.9), (42, 22.6))] \
      + [C(x, y, shape="huerde") for x, y in ((55.9, 35.7), (58.7, 38), (61.6, 40.6), (64.7, 43.2))]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
LEITER_RUNTER = [[33, 13.5], [43.5, 24]]
UM_C1 = [[41.4, 34], [44.4, 37], [47.4, 34]]
HUERDEN_RUNTER = [[55, 34.8], [66.5, 45.3]]
HUERDEN_HOCH = [[66.5, 45.3], [55.5, 35.5]]
UM_C2 = [[55.9, 24.4], [52.9, 21.4], [49.9, 24.4]]
LEITER_HOCH = [[43.5, 24], [33, 13.5]]

u = {"title": "Dribbeln, Leiter, Hürden", "code": "UE-143", "kind": "Übungsform",
 "focuses": ["Dribbling", "Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "23 x 23 m",
 "description": "Ein Kreislauf mit zwei Gruppen an gegenüberliegenden Ecken. Je einer aus jeder Gruppe startet gleichzeitig: Er dribbelt an der Seite entlang zum Hütchen am Ende, lässt den Ball dort liegen und läuft dann durch Leiter und Hürden diagonal durchs Feld, um ein Hütchen in der Mitte herum. Am Ende holt er sich den Ball, den der andere liegen gelassen hat, und dribbelt ihn zur nächsten Ecke. Das startet die nächsten beiden.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 23 Metern. An allen vier Ecken ein Hütchen, in der Mitte zwei Hütchen. Diagonal durchs Feld eine Leiter oben links und Minihürden unten rechts.",
  "Verteilen: Zwei Gruppen zu viert, eine unten links, eine oben rechts, jeder mit einem Ball. Der Trainer steht am Rand mit Ersatzbällen.",
  "Ablauf: Je einer aus beiden Gruppen dribbelt gleichzeitig los zum Hütchen am Ende seiner Seite und lässt den Ball liegen. Dann durch Leiter oder Hürden, um ein Hütchen in der Mitte und durch das andere Gerät. Am Ende holt er den Ball des anderen und dribbelt ihn zur Ecke.",
  "Weiter: Das Ankommen startet die nächsten beiden. Später: nach dem Kreislauf noch ein Pass und ein Eins-gegen-eins, oder drei Sprints am Ende."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball beim schnellen Dribbeln eng am Fuß führen", "Saubere Technik in Leiter und Hürden", "Genaue Pässe, wenn später gepasst wird", "Kurz und scharf um die Hütchen in der Mitte wenden"],
 "materials": ["6 Hütchen", "1 Koordinationsleiter", "4 Minihürden", "8 Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Dribbeln, Leiter, Hürden. Zwei Spieler laufen gleichzeitig einen Kreislauf mit Ball, Leiter, Hürden und scharfen Wenden.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Dribbeln zum Hütchen", "Neon elf und Rot vier starten gleichzeitig und dribbeln an ihrer Seite entlang zum Hütchen am Ende. Dort lassen sie den Ball liegen.",
     dr("n11", "b11", [26.5, 13.5]), dr("r4", "b4", [72.5, 46.5], delay=0.1)),
   S("Leiter und Hürden", "Neon elf läuft durch die Leiter und um das untere Hütchen in der Mitte, Rot vier über die Hürden und um das obere Hütchen.",
     *weg("n11", LEITER_RUNTER + UM_C1), *weg("r4", HUERDEN_HOCH + UM_C2, delay=0.1)),
   S("Das andere Gerät", "Dann geht es weiter: Neon elf über die Hürden nach unten rechts, Rot vier durch die Leiter nach oben links.",
     *weg("n11", HUERDEN_RUNTER), *weg("r4", LEITER_HOCH, delay=0.1)),
   S("Ball holen, zurückdribbeln", "Jeder holt sich den Ball, den der andere liegen gelassen hat, und dribbelt ihn zur Ecke. Das startet die nächsten beiden: Neon zehn und Rot neun.",
     mv("n11", [72.5, 47]), dr("n11", "b4", [73, 16], after=True), mv("r4", [26.5, 14.5], delay=0.1), dr("r4", "b11", [27, 40], after=True))],
  "dims": dims(25, 75, 5, 55, "23 m", "23 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball eng führen.", "Eng am Fuß",
    "Beim schnellen Dribbeln an der Seite entlang bleibt der Ball eng am Fuß, mit vielen kleinen Kontakten. So kann man jederzeit abbremsen und den Ball genau am Hütchen ablegen.",
    sp(), BAELLE,
    [S("Kleine Kontakte", "Neon elf dribbelt mit vielen kleinen Kontakten an der Seite entlang nach oben, der Ball springt ihm nie weg.",
       dr("n11", "b11", [26.5, 30]), dr("n11", "b11", [26.5, 13.5], after=True)),
     S("Genau ablegen", "Am Hütchen bremst er ab und legt den Ball genau dort ab, dann geht es sofort zur Leiter.",
       mv("n11", [33, 13.5]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Scharf um die Hütchen wenden.", "Scharf wenden",
    "In der Mitte geht es um ein Hütchen herum. Wer einen weiten Bogen läuft, verliert Zeit. Kurz vorher abbremsen, tief gehen und eng um das Hütchen herum, dann wieder voll beschleunigen.",
    sp(n11=(43.5, 24), r4=(55.5, 35.5), n10=(18.5, 46), r9=(81.5, 8)), [B("b11", 27.1, 14.1), B("b4", 73.1, 47.1), B("s1", 13.6, 25), B("s2", 10, 25)],
    [S("Eng herum", "Neon elf läuft eng um das untere Hütchen, Rot vier gleichzeitig eng um das obere.",
       *weg("n11", UM_C1), *weg("r4", UM_C2, delay=0.1)),
     S("Wieder Tempo", "Direkt danach beschleunigen beide wieder voll und laufen zum nächsten Gerät.",
       *weg("n11", HUERDEN_RUNTER[:1]), *weg("r4", LEITER_HOCH[:1], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
