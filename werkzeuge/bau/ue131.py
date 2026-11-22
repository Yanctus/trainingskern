import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-92 (U12-U14, Woche 2 Pre-Season): SAQ Races and Small Sided Games. 20 x 20 Yards = Feld x 22-72, y 5-55 (18 m).
# Links der Parcours (Dummys, drei Minihürden oben, Leiter unten als vier Minihürden), rechts die Spielzone mit Minitor oben und unten.
# Dunkel -> Neon (2-6, Start oben), Pink -> Rot (7-11, Start unten). Wartende über und unter dem Feld (3D-Abstand).
# Ein Trainer rechts mit Bällen. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 80, 30, "T")
POS = {"n2": (14, 12), "n3": (5, 2), "n4": (23, 2), "n5": (32, 2), "n6": (41, 2),
       "r7": (14, 48), "r8": (5, 58), "r9": (23, 58), "r10": (32, 58), "r11": (41, 58)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b1", 81.6, 30.6), B("s1", 83, 34), B("s2", 83, 26)]
LINES = [rect(22, 5, 50, 50), line(47, 5, 47, 55)]
KEGEL = [C(21.8, 12.1), C(21.8, 30), C(21.8, 48.5), C(46.6, 23.3), C(46.6, 39.6), C(48.1, 28.8), C(53.6, 32.8),
         C(45.9, 12.1, "neon", shape="stange"), C(47.8, 48.3, "neon", shape="stange")] \
      + [C(x, 23.2, shape="huerde") for x in (31.1, 34.3, 37.7)] + [C(x, 39.6, shape="huerde") for x in (30.5, 33, 35.5, 38)]
TORE = [{"x": 59.5, "y": 5, "side": "top"}, {"x": 59.5, "y": 55, "side": "bottom"}]
OBEN = [59.5, 4.7]
# Neon oben: zum Dummy, um ihn herum, um das Hütchen, durch die Hürden, Hütchen links antippen, Sprint zum Mittelhütchen, in die Zone
N1 = [[21.8, 9], [49.5, 9], [49.8, 15.5], [49, 22.5], [46.6, 26]]
N2 = [[40.5, 23.2], [28, 23.2], [23, 27], [20.5, 27.6]]
N3 = [[24, 26.5], [45.6, 27.6], [57, 24]]
R1 = [[21.8, 51], [51, 51], [51, 44.5], [49.5, 41.8], [46.6, 42.3]]
R2 = [[40.5, 39.6], [28, 39.6], [23.5, 35.5], [21, 33]]
R3 = [[24, 34.5], [51.3, 34.6], [60, 36]]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Parcours-Wettlauf ins Spiel", "code": "UE-131", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Koordination", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "18 x 18 m",
 "description": "Von jedem Team läuft einer gleichzeitig durch seinen Parcours: um einen Dummy und ein Hütchen, durch Hürden oder Leiter, ein Hütchen links antippen und dann zum Hütchen in der Mitte sprinten. Das Antippen dort schickt den Nächsten los. Wer zuerst in der Spielzone ist, bekommt vom Trainer den Ball, und es wird eins gegen eins gespielt. Kommen die Nächsten an, bevor ein Tor fällt, wird daraus zwei gegen zwei, dann drei gegen drei, bis fünf gegen fünf.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, in der Mitte geteilt. Links der Parcours mit je einem Dummy oben und unten, drei Minihürden oben, einer Leiter unten und Hütchen zum Antippen. Rechts die Spielzone mit einem Minitor oben und einem unten.",
  "Verteilen: Zwei Teams mit je fünf Spielern. Team Neon wartet oben links, Team Rot unten links. Der Trainer steht rechts neben dem Feld mit vielen Bällen.",
  "Ablauf: Auf Pfiff laufen die Ersten beider Teams gleichzeitig los: um den Dummy, um das Hütchen, durch Hürden oder Leiter, das linke Hütchen antippen und zum Mittelhütchen sprinten. Wer es antippt, schickt den Nächsten seines Teams los. Der Erste in der Spielzone bekommt den Ball vom Trainer.",
  "Spiel: Team Neon spielt aufs obere Minitor, Team Rot aufs untere. Gespielt wird, bis ein Tor fällt oder der Ball ins Aus geht. Kommen vorher die Nächsten an, spielen sie mit, bis zum fünf gegen fünf. Danach kurze Pause und neue Reihenfolge."],
 "organisation_show": ORG,
 "coaching_points": ["Durch Hürden und Leiter sauber und schnell, ohne etwas umzustoßen", "Auch müde den Ball sauber kontrollieren", "Kommt ein Mitspieler dazu, sofort zusammen spielen", "Die Mitspieler beim Laufen laut anfeuern"],
 "materials": ["7 Hütchen", "2 Dummys", "3 Minihürden", "1 Koordinationsleiter", "2 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Parcours-Wettlauf ins Spiel. Erst ein Wettrennen durch den Parcours, dann geht es sofort ins Spiel, und mit jedem, der ankommt, wird es größer.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Um Dummy und Hütchen", "Auf Pfiff laufen Spieler zwei und Spieler sieben gleichzeitig los: am Rand entlang, um den Dummy herum und um das Hütchen.",
     *weg("n2", N1), *weg("r7", R1, delay=0.15)),
   S("Hürden und Leiter", "Dann geht es zurück nach links, Spieler zwei über die Hürden, Spieler sieben durch die Leiter, und beide tippen das Hütchen links an.",
     *weg("n2", N2), *weg("r7", R2, delay=0.15)),
   S("Sprint in die Spielzone", "Jetzt sprinten beide zu den Hütchen in der Mitte und tippen sie an. Das schickt Spieler drei und Spieler acht los. Spieler zwei ist zuerst in der Spielzone.",
     *weg("n2", N3), *weg("r7", R3, delay=0.25), mv("n3", [21.8, 9], delay=0.6), mv("r8", [21.8, 51], delay=0.7)),
   S("Eins gegen eins: Punkt", "Darum spielt der Trainer Spieler zwei den Ball. Er dribbelt aufs obere Minitor und trifft, und das gibt einen Punkt für Team Neon. Inzwischen laufen schon Spieler drei und Spieler acht: Kommen sie an, bevor ein Tor fällt, wird zwei gegen zwei gespielt.",
     ps("b1", [57.6, 24.6]), dr("n2", "b1", [60, 14], after=True), ps("b1", OBEN, after=True), mv("r7", [63, 22], delay=0.4))],
  "dims": [{"x1": 76, "y1": 5, "x2": 76, "y2": 55, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Aus eins gegen eins wird zwei gegen zwei.", "Zusammen spielen",
    "Fällt im eins gegen eins kein Tor, bleiben beide drin, und die Nächsten kommen dazu. Dann wird sofort zusammen gespielt: Der Neue bietet sich an, der Ballführende sieht ihn und spielt ab. So wird das Spiel mit jedem Neuen größer und echter.",
    sp(n2=(60, 26), r7=(70, 34), n3=(48, 22), r8=(48, 40)), [B("b1", 60.6, 26.6), B("s1", 83, 34), B("s2", 83, 26)],
    [S("Die Nächsten kommen dazu", "Noch ist kein Tor gefallen. Spieler drei und Spieler acht kommen in die Spielzone, jetzt heißt es zwei gegen zwei.",
       mv("n3", [52, 16]), mv("r8", [66, 32], delay=0.15), mv("r7", [64, 24], delay=0.3)),
     S("Zu zweit zum Abschluss: Punkt", "Spieler zwei spielt zu Spieler drei, der ist frei und schießt ins obere Minitor, und das gibt einen Punkt für Team Neon. Danach kommen die Nächsten, bis fünf gegen fünf gespielt wird.",
       ps("b1", [52.6, 16.6]), ps("b1", OBEN, after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Sauber durch Hürden und Leiter.", "Erst sauber, dann schnell",
    "Wer durch Hürden und Leiter hetzt und dabei etwas umstößt, verliert mehr Zeit als er gewinnt. Kurze, schnelle Schritte, Arme mitnehmen, nicht auf die Geräte treten. Erst wenn die Technik sitzt, wird das Tempo erhöht.",
    sp(n2=(49.5, 22), r7=(49.5, 38)), BAELLE,
    [S("Kurze, saubere Schritte", "Spieler zwei läuft mit kurzen, schnellen Schritten über die Hürden, Spieler sieben genauso durch die Leiter. Keiner tritt auf ein Gerät.",
       *weg("n2", [[46.6, 26]] + N2), *weg("r7", [[46.6, 42.3]] + R2, delay=0.15)),
     S("Antippen und Sprint", "Danach tippen beide an und sprinten zum Mittelhütchen. Spieler zwei war sauberer und ist zuerst in der Spielzone, darum bekommt er den Ball.",
       *weg("n2", N3), *weg("r7", R3, delay=0.25))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
