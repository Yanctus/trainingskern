import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-56 (U15-U17, Woche 5 Pre-Season): Carousel Training Circuit. 45 x 35 Yards = 41 x 32 m (gerundet 40 x 30 m).
# Feld liegt wie im PDF quer (x 15-81, y 4-53, Maßstab fast gleich, leicht in die Breite gezogen), vier Zonen durch gestrichelte
# Linien geteilt: Zone 1 links oben (Stangen, Leiter, Ringe), Zone 2 rechts oben (Dribbling durch die Hütchen), Zone 3 rechts
# unten (Hürden, Sprint, Ablage vom Trainer, Abschluss ins Minitor), Zone 4 links unten (Pendelsprints).
# Zone 2 und Zone 3 links-rechts gespiegelt: Start rechts außen statt an der Mittellinie, damit die Wartenden neben dem Feld
# stehen können (3D-Abstand, die Zonen sind zu flach für eine Reihe hintereinander). Das Minitor in Zone 3 steht damit rechts.
# Je Zone stehen drei der vier Spieler auf der Tafel (der vierte nur im Text). Drei Ringe statt fünf (Platz), fünf Stangen,
# eine Leiter.
# Farben wie im Video: Gelb (Zonen 1 und 3) -> Team Neon, Rot (Zonen 2 und 4) -> Team Rot, neu nummeriert (im Video doppelt):
# Zone 1: 2-5, Zone 2: 6-9, Zone 3: 10-13, Zone 4: 14-17. Ein Trainer statt zwei (unten an Zone 3, er legt für den Abschluss ab).
# Pendelsprints in Zone 4 als Staffel gedeutet (wie in den anderen Zonen: wer zurück ist, übergibt an den Nächsten).
# Punkt für einen Treffer in Zone 3 ergänzt (im Original ohne Zählweise).
# Sichtkegel aus dem Ton (Zone 2: „dribble … with precision while maintaining speed and awareness“): Im ersten Coaching-Punkt
# nimmt der Dribbler den Kopf hoch und schaut auf die nächsten Hütchen. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 64.5, 55.4, "T")
ERSATZ = [B("s1", 68, 56), B("s2", 70.5, 56)]
POS = {"n2": (17, 7.5), "n3": (7.5, 6.5), "n4": (7.5, 22), "r6": (80, 10), "r7": (88.5, 7), "r8": (88.5, 23),
       "n10": (77, 35.5), "n11": (88.5, 38.5), "n12": (88.5, 54), "r14": (22.5, 51), "r15": (31, 51), "r16": (39.5, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(15, 4, 66, 49), line(48, 4, 48, 53), line(15, 28.5, 81, 28.5)]
TOR = [{"x": 77.7, "y": 49, "side": "right"}]
STANGEN = [(22, 10), (27.5, 10), (33, 10), (38.5, 10), (44, 10)]
RINGE = [(27.5, 23), (22.5, 20.5), (17.5, 23)]
OBEN = [(54, 9), (61, 9), (68, 9), (75, 9)]
UNTEN = [(54, 24), (61, 24), (68, 24), (75, 24)]
HUERDEN = [(69, 35), (65.5, 35), (62, 35), (58.5, 35)]
PENDEL = [(19, 31.5), (19, 37.5), (19, 43.5), (19, 49.5)]
CONES = [C(x, y, shape="stange") for x, y in STANGEN] + [leiter(39.5, 22)] + [ring(x, y) for x, y in RINGE] \
    + [C(x, y) for x, y in OBEN + UNTEN] + [C(x, y, shape="huerde") for x, y in HUERDEN] \
    + [C(81.5, 32, "neon"), C(51, 47.5)] + [C(x, y) for x, y in PENDEL]
DIMS = dims(15, 81, 4, 53, "40 m", "30 m", rx=96)
def weg(who, pkt, **k): return [mv(who, list(pkt[0]), **k)] + [mv(who, list(p), after=True) for p in pkt[1:]]
def dweg(who, ball, pkt, **k): return [dr(who, ball, list(pkt[0]), **k)] + [dr(who, ball, list(p), after=True) for p in pkt[1:]]
SLALOM1 = [(22, 13.5), (27.5, 6.5), (33, 13.5), (38.5, 6.5), (44, 13.5)]
RUECK1 = [(46.5, 22), (31.5, 22)] + [list(r) for r in RINGE] + [(16.5, 13)]
OBEN2 = [(75, 12.5), (68, 5.5), (61, 12.5), (54, 5.5), (50.5, 9)]
UNTEN2 = [(49.5, 22), (54, 27), (61, 20.5), (68, 27), (75, 20.5), (80, 22), (80, 13)]
HUERDEN3 = [(72, 35), (55, 35), (50.5, 44.5)]
BAELLE = [B("b6", *f(POS["r6"])), B("b7", *f(POS["r7"])), B("b8", *f(POS["r8"])), B("b3", 65.1, 56)] + ERSATZ
def pendel(who, x, hoehen, **k):
    out = []
    for i, y in enumerate(hoehen):
        out += [mv(who, [x, y], after=bool(i) or None, **({} if i else k)), mv(who, [x, 51], after=True)]
    return out

u = {"title": "Karussell mit vier Zonen", "code": "UE-332", "kind": "Übungsform",
 "focuses": ["Koordination", "Dribbling", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 12, "players_max": 16,
 "field_size": "40 x 30 m",
 "description": "Ein Stationskarussell für die Vorbereitung mit vier Zonen und vier Gruppen. In Zone eins geht es durch Stangen, Leiter und Ringe, in Zone zwei wird eng durch die Hütchen gedribbelt. Zone drei verbindet Hürden und Sprint mit einem Abschluss ins Minitor, Zone vier sind Pendelsprints. Auf Pfiff rückt jede Gruppe im Uhrzeigersinn eine Zone weiter.",
 "organisation": ["Aufbauen: Ein Feld von 40 mal 30 Metern, in vier Zonen geteilt. Zone eins: fünf Stangen, eine Leiter und Ringe. Zone zwei: zwei Reihen mit je vier Hütchen. Zone drei: vier Minihürden, ein Hütchen und ein Minitor. Zone vier: vier Hütchen als Pendelmarken.",
  "Verteilen: Vier Gruppen zu viert, jede Gruppe startet in einer Zone. In Zone zwei hat jeder einen Ball. Der Trainer steht mit Bällen an Zone drei und legt dort für den Abschluss ab.",
  "Ablauf: In jeder Zone läuft einer, die anderen warten am Start. Ist er zurück, übergibt er an den Nächsten. Alle vier Zonen laufen gleichzeitig.",
  "Wertung und Wechsel: Jeder Treffer in Zone drei gibt einen Punkt für die Gruppe. Auf Pfiff des Trainers wechseln alle Gruppen im Uhrzeigersinn in die nächste Zone."],
 "organisation_show": ORG,
 "coaching_points": ["Vollgas in jeder Zone", "Saubere Schritte an Leiter, Ringen und Hürden", "Ball eng am Fuß, beide Füße benutzen", "Nach dem Pendelsprint im Gehen durchatmen"],
 "materials": ["5 Stangen", "1 Koordinationsleiter", "3 Ringe", "4 Minihürden", "1 Minitor", "14 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Karussell mit vier Zonen. Vier Gruppen arbeiten gleichzeitig, und auf Pfiff dreht sich das Karussell eine Zone weiter.",
 "board": {"lines": LINES, "goals": TOR, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Alle vier Zonen starten", "Auf Pfiff geht es in allen vier Zonen gleichzeitig los. Spieler zwei läuft im Zickzack durch die Stangen. Spieler sechs dribbelt durch die obere Hütchenreihe. Spieler zehn springt über die Hürden, und Spieler vierzehn sprintet zur ersten Marke und zurück.",
     *weg("n2", SLALOM1), *dweg("r6", "b6", OBEN2), *weg("n10", HUERDEN3[:2]), *pendel("r14", 22.5, [43.5])),
   S("Leiter, Ringe, zurück", "Spieler zwei kommt über die Leiter und die Ringe zurück zum Start. Spieler sechs dribbelt die untere Reihe zurück. Spieler vierzehn sprintet jetzt zur zweiten Marke.",
     *weg("n2", RUECK1), *dweg("r6", "b6", UNTEN2), *pendel("r14", 22.5, [37.5])),
   S("Ablage vom Trainer, Abschluss", "Spieler zehn sprintet zum Hütchen und dreht dort ab. Der Trainer legt den Ball flach in seinen Lauf, und er schießt direkt ins Minitor. In Zone vier geht es bis zur dritten Marke.",
     mv("n10", list(HUERDEN3[2])), mv("n10", [59, 47.5], after=True), ps("b3", [59.6, 48.1], delay=1.2), ps("b3", [77.4, 49], after=True),
     *pendel("r14", 22.5, [31.5])),
   S("Übergabe: Punkt und Wechsel", "Wer zurück ist, übergibt an den Nächsten in seiner Gruppe. Jetzt starten Spieler drei, Spieler sieben, Spieler elf und Spieler fünfzehn. Der Treffer von Spieler zehn gibt einen Punkt für seine Gruppe. Auf Pfiff wechseln alle Gruppen im Uhrzeigersinn in die nächste Zone.",
     mv("n3", list(POS["n2"])), mv("n3", list(SLALOM1[0]), after=True), mv("n2", [7.5, 14], delay=0.3),
     dr("r7", "b7", list(POS["r6"])), dr("r7", "b7", list(OBEN2[0]), after=True), mv("r6", [88.5, 14.5], delay=0.3),
     mv("n10", [80, 44]), mv("n11", list(POS["n10"]), delay=0.3), mv("n11", list(HUERDEN3[0]), after=True),
     mv("r15", [31, 43.5], delay=0.3), mv("r15", [31, 51], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ball eng am Fuß, mit beiden Füßen.", "Ball eng am Fuß",
    "Wer den Ball zu weit vorlegt, verliert ihn an den Hütchen und hält die ganze Gruppe auf. Darum viele kleine Kontakte, mit rechts und mit links. Zwischendurch geht der Kopf kurz hoch zur nächsten Hütchenreihe.",
    sp(), BAELLE,
    [S("Kleine Kontakte, beide Füße", "Spieler sechs nimmt den Ball mit kleinen Kontakten um jedes Hütchen, mal mit rechts, mal mit links. Der Ball springt nie weiter als einen Schritt weg.",
       *dweg("r6", "b6", OBEN2)),
     S("Kopf hoch, dann zurück", "Am Ende der Reihe geht der Kopf kurz hoch. Spieler sechs sieht die untere Reihe und dribbelt sie genauso eng zurück zum Start.",
       bl("r6", [61, 22]), *dweg("r6", "b6", UNTEN2, after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ruhig abschließen, auch mit schweren Beinen.", "Ruhig abschließen",
    "Nach Hürden und Sprint ist der Puls oben. Trotzdem bleibt der Abschluss sauber. Kurz vor dem Ball Tempo rausnehmen, Standbein neben den Ball und flach ins Tor schieben. Ein platzierter Schuss bringt mehr als ein harter daneben.",
    sp(), BAELLE,
    [S("Hürden und Sprint", "Spieler zehn springt über die Hürden und sprintet zum Hütchen. Die Beine sind jetzt schwer.",
       *weg("n10", HUERDEN3)),
     S("Flach und platziert: Punkt", "Der Trainer legt ab. Spieler zehn nimmt kurz Tempo raus, setzt das Standbein neben den Ball und schiebt flach ins Eck, und das gibt einen Punkt für seine Gruppe.",
       mv("n10", [59, 47.5]), ps("b3", [59.6, 48.1], delay=0.6), ps("b3", [77.4, 50.2], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
