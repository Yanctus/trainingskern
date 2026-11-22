import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-3 (U12-U14, Woche 25 Phase 1): Quick Movement and Dribbling Skills Warm Up. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m).
# Ausrichtung wie im PDF: vier Stationen (unten 11/2, rechts 3/4, oben 7/8, links 5/9), vier Mannequins in der Mitte als Stangen,
# in jeder Ecke eine schräge Reihe aus vier Hütchen. Ein Team (im PDF pink) -> Team Neon, Nummern wie im PDF.
# Stationen sind um die Mitte gedreht gleich gebaut; an den Stationen links und rechts steht der Passpartner außerhalb des Feldes
# (3D-Abstand), im PDF auf der Linie. Weg wie im PDF-Bild: unten -> Hütchen rechts unten -> Station rechts (das Bild zeigt damit
# gegen den Uhrzeigersinn, der Text sagt "clockwise"; im Text hier nur "nächste Station"). Ein Trainer statt zwei.
# Steigerung aus Ton/Video (0:37-0:50): zwei Doppelpässe (Station, nächste Station), Ball durch die Hütchen. Sichtkegel: im Video
# "Impact: ... head up" (kein Kegel eingezeichnet). Richtung aus dem Sinn: Neon zwei schaut vor dem Rückpass zu Neon elf, Neon elf
# schaut nach den Hütchen zu Neon vier an der nächsten Station.
T = P("T", "c", 84, 8, "T")
CX, CY = 50, 30
def rot(p, k):
    x, y = p
    for _ in range(k):
        x, y = y, -x
    return [round(CX + x, 1), round(CY + y, 1)]
DRIB = ["n11", "n3", "n7", "n5"]                 # unten, rechts, oben, links
BALL = ["b1", "b2", "b3", "b4"]
EMPF = {"n2": (54.5, 52), "n4": (81, 34.5), "n8": (45.5, 8), "n9": (19, 25.5)}
EMPF_ID = ["n2", "n4", "n8", "n9"]
POS = {d: tuple(rot((-4.5, 22), k)) for k, d in enumerate(DRIB)}
POS.update(EMPF)
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 85.6, 4.5), B("s2", 82, 4.5)]
BAELLE = [B(BALL[k], POS[d][0] + 0.6, POS[d][1] + 0.6) for k, d in enumerate(DRIB)] + ERSATZ
REIHE = [(10, 10.5), (13, 13), (16, 15.5), (19, 18)]
CONES = [C(*rot(p, k)) for k in range(4) for p in REIHE] + [C(*rot((0, 7), k), shape="stange") for k in range(4)]
LINES = [rect(25, 5, 50, 50)]
UM = [(-4, 10), (0, 3.5), (4, 10)]                # um die eigene Stange
SLALOM = [(8, 7.5), (11.6, 8.6), (11.4, 14.9), (17.6, 13.6), (17.4, 19.9), (21.5, 20.5)]
WEITER = (22, 4.5)                                # Platz an der nächsten Station

def um_alle():
    m = []
    for k, d in enumerate(DRIB):
        m += [dr(d, BALL[k], rot(UM[0], k)), dr(d, BALL[k], rot(UM[1], k), after=True), dr(d, BALL[k], rot(UM[2], k), after=True)]
    return m
def zurueck_alle():
    return [ps(BALL[k], [EMPF[e][0] + 0.6, EMPF[e][1] + 0.6]) for k, e in enumerate(EMPF_ID)]
def slalom(d, k):
    return [mv(d, rot(SLALOM[0], k))] + [mv(d, rot(p, k), after=True) for p in SLALOM[1:]]

u = {"title": "Stationen mit schnellen Füßen", "code": "UE-202", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Dribbling", "Koordination"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Ein Aufwärmen mit vier Stationen, die alle gleichzeitig laufen. In der Mitte stehen vier Stangen, an jeder Station warten zwei Spieler. Der Spieler mit Ball dribbelt um seine Stange, passt zurück zur Station und läuft mit schnellen Füßen durch eine Hütchenreihe. Dann stellt er sich an der nächsten Station an.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. In der Mitte vier Stangen, in jeder Ecke eine schräge Reihe aus vier Hütchen.",
  "Verteilen: An jeder Seite eine Station mit zwei Spielern, einer davon mit Ball. Der Trainer steht an der Ecke mit Bällen.",
  "Ablauf: Alle vier Spieler mit Ball dribbeln gleichzeitig um ihre Stange, passen zurück zur Station und laufen mit schnellen Füßen durch die Hütchen.",
  "Wechsel: Danach geht jeder zur nächsten Station und ist dort Passpartner. Wer den Pass bekommen hat, dribbelt als Nächster."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und zackig von Station zu Station", "Den Ball beim Dribbeln eng am Fuß führen", "In den Hütchen die Füße schnell und abwechselnd setzen", "Konzentriert bleiben und genau passen"],
 "materials": ["4 Stangen", "16 Hütchen", "Einige Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Stationen mit schnellen Füßen. Vier Stationen laufen gleichzeitig: um die Stange dribbeln, zurückpassen und schnell durch die Hütchen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Um die Stange", "Alle vier Stationen starten gleichzeitig. Wir schauen auf Neon elf: Er dribbelt mit kleinen Kontakten um seine Stange herum.",
     *um_alle()),
   S("Zurückpassen", "Jetzt passen alle vier den Ball zurück zu ihrem Partner an der Station. Neon elf passt zu Neon zwei.",
     *zurueck_alle()),
   S("Schnelle Füße", "Ohne Ball geht es zu den Hütchen. Neon elf läuft mit schnellen, kleinen Schritten im Zickzack durch die Reihe, und die anderen drei machen es genauso.",
     *[m for k, d in enumerate(DRIB) for m in slalom(d, k)]),
   S("Zur nächsten Station", "Danach läuft jeder zur nächsten Station. Neon elf stellt sich an der Station rechts an. Geschafft! Jetzt dribbeln Neon zwei, Neon vier, Neon acht und Neon neun, und alles beginnt von vorn.",
     *[mv(d, rot(WEITER, k)) for k, d in enumerate(DRIB)])],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Eng am Ball, schnelle Füße.", "Eng am Ball",
    "Um die Stange wird der Ball mit vielen kurzen, kleinen Kontakten geführt und bleibt immer nah am Fuß. In den Hütchen setzt der Spieler die Füße schnell und abwechselnd. So werden Gewandtheit und Koordination besser.",
    sp(), BAELLE,
    [S("Kleine Kontakte", "Wieder starten alle gleichzeitig. Wir schauen auf Neon elf: Er führt den Ball mit vielen kleinen Kontakten um die Stange herum, der Ball bleibt immer nah am Fuß.",
       *um_alle()),
     S("Abwechselnd die Füße", "Neon elf passt zurück zu Neon zwei. In den Hütchen setzt er die Füße schnell und abwechselnd: links, rechts, links, rechts. Dann geht es zur nächsten Station.",
       ps("b1", [55.1, 52.6]), *[dict(m, after=True) for m in slalom("n11", 0)])]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Doppelpässe.", "Zwei Doppelpässe",
    "Nach der Stange spielt der Spieler einen Doppelpass mit seinem Partner und nimmt den Ball mit durch die Hütchen. An der nächsten Station spielt er einen zweiten Doppelpass und startet dort neu. Kopf hoch und laut rufen, damit die Pässe genau ankommen.",
    sp(), BAELLE,
    [S("Um die Stange", "Wieder starten alle gleichzeitig um die Stange. Wir schauen auf Neon elf.",
       *um_alle()),
     S("Erster Doppelpass", "Neon elf passt zu Neon zwei und läuft weiter. Neon zwei hebt den Kopf, sieht ihn und spielt den Ball direkt zurück in den Lauf.",
       ps("b1", [55.1, 52.6]), mv("n11", [58, 37.5], delay=0.3), bl("n2", [60, 36], after=True), ps("b1", [58.6, 38.1], after=True)),
     S("Mit Ball durch die Hütchen", "Jetzt nimmt Neon elf den Ball mit durch die Hütchen, mit kleinen Kontakten im Zickzack. Am Ende hebt er den Kopf und sucht Neon vier an der nächsten Station.",
       *[dr("n11", "b1", rot(p, 0), after=(i > 0)) for i, p in enumerate(SLALOM[1:])], bl("n11", [81, 34.5], after=True)),
     S("Zweiter Doppelpass", "Neon elf passt zu Neon vier und läuft hoch. Neon vier spielt direkt zurück. Neon elf nimmt den Ball mit und startet hier die nächste Runde um die Stange, und Neon vier ist jetzt sein Partner.",
       ps("b1", [81.6, 35.1]), mv("n11", [70, 37], delay=0.3), ps("b1", [70.6, 37.6], after=True), dr("n11", "b1", [64, 34], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
