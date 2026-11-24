import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-10 (U15-U17, Woche 12): Developing the 433 Warm Up. 25 x 25 Yards (23 m, gerundet 25 m) = Feld x 22-72, y 5-55.
# Ausrichtung wie im PDF (Start unten links, Ball läuft gegen den Uhrzeigersinn). Nummern wie im Video (2-11, nur ein Team).
# Die drei Mittelfeldspieler (9, 4, 7) etwas auseinandergezogen und der Wartende (10) rechts neben den Start gesetzt (3D-Abstand).
# Ein Trainer statt zwei. Die Puppen sind Stangen. Jeder läuft seinem Pass nach; die beiden Doppelpass-Partner 4 und 7
# bleiben in der Mitte (im Video „work that midfield 3“ ohne eigenen Stationswechsel) und werden nach einigen Runden getauscht.
# Sichtkegel: Text „Close-control and head up before passing“; im Video nicht eingezeichnet, Richtung aus dem Sinn:
# der Außenverteidiger schaut nach dem Doppelpass hoch zum Flügelspieler, bevor er steil spielt.
# Steigerung zwei (zweiter Ball): Positionen der Grundform behalten (im PDF ist das Feld dort gedreht), zweiter Ball startet oben rechts.
T = P("T", "c", 9, 50, "T")
ERSATZ = [B("s1", 12.6, 53.5), B("s2", 9, 53.5)]
POS = {"n3": (34.5, 49.5), "n10": (43.5, 52), "n9": (47, 36), "n6": (59, 49.5), "n5": (67.8, 29.6), "n4": (56.5, 27),
       "n8": (57.3, 8.3), "n2": (37.5, 8.3), "n11": (26.4, 28.3), "n7": (37.5, 27)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def b(i): return [POS[i][0] + 0.6, POS[i][1] + 0.6]
CONES = [C(34.5, 52.5), C(56, 50.5), C(47, 39), C(53.5, 27), C(40.5, 27), C(60.3, 7), C(34.5, 7),
         C(64.5, 28.5, shape="stange"), C(29.5, 31.5, shape="stange")]
LINES = [rect(22, 5, 50, 50)]
DIMS = dims(22, 72, 5, 55, "25 m", "25 m", rx=82)
R4, R5 = [55, 35], [68, 20]          # Doppelpass rechts: Treffpunkt von Spieler vier, Laufziel von Spieler fünf
L7, L11 = [37, 23.5], [26.5, 38]       # Doppelpass links: Treffpunkt von Spieler sieben, Laufziel von Spieler elf
def dp_rechts(ball, **k):
    return [mv("n4", R4, **k), ps(ball, [55.6, 35.6], **k), mv("n5", R5, delay=(k.get("delay") or 0) + 0.3), ps(ball, [68.6, 20.6], after=True)]
def dp_links(ball, **k):
    return [mv("n7", L7, **k), ps(ball, [37.6, 24.1], **k), mv("n11", L11, delay=(k.get("delay") or 0) + 0.3), ps(ball, [27.1, 38.6], after=True)]

u = {"title": "Passfolge im Vier-Drei-Drei", "code": "UE-309", "kind": "Übungsform",
 "focuses": ["Passspiel", "Erwärmung", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 10, "players_max": 12,
 "field_size": "25 x 25 m",
 "description": "Zehn Spieler stehen so, wie sie im Vier-Drei-Drei aufbauen. Der Ball läuft vom Innenverteidiger über den Sechser auf die andere Seite, raus zum Außenverteidiger, per Doppelpass an der Stange vorbei und steil zum Flügelspieler. Oben geht es quer, und auf der linken Seite kommt derselbe Ablauf zurück zum Start. Jeder läuft seinem Pass nach.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern. Sieben Hütchen markieren die Stationen, links und rechts steht je eine Stange als Gegenspieler.",
  "Verteilen: Zehn Spieler. Zwei am Start unten links, je einer an den anderen Stationen. Ein Ball am Start, der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass auf den Sechser, klatschen lassen, raus zum Außenverteidiger. Doppelpass mit dem Mittelfeldspieler um die Stange, dann steil zum Flügelspieler. Quer nach links, und dort dasselbe zurück bis zum Start.",
  "Wechsel: Jeder läuft seinem Pass nach zur nächsten Station. Die zwei Mittelfeldspieler für den Doppelpass bleiben und werden nach ein paar Runden getauscht. Ist der Ball am Start, beginnt der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und scharf passen, der Ball bleibt nie stehen", "Kopf hoch vor dem Pass", "Erst starten, wenn der Mitspieler den Ball spielen kann", "Dem Pass im Tempo nachlaufen"],
 "materials": ["7 Hütchen", "2 Stangen", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passfolge im Vier-Drei-Drei. Ein Aufwärmen mit zehn Spielern. Der Ball läuft so, wie wir im Spiel von hinten aufbauen, und jeder läuft seinem Pass nach.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *b("n3"))] + ERSATZ,
  "steps": [
   S("Auf den Sechser und klatschen", "Spieler drei beginnt unten links und spielt in die Mitte zu Spieler neun. Der lässt mit einem Kontakt klatschen, rüber zu Spieler sechs.",
     ps("b1", b("n9")), ps("b1", b("n6"), after=True)),
   S("Raus und Doppelpass", "Spieler sechs spielt raus zu Spieler fünf. Jetzt der Doppelpass. Spieler vier kommt entgegen, bekommt den Ball und legt ihn an der Stange vorbei in den Lauf.",
     ps("b1", b("n5")), *dp_rechts("b1", after=True)),
   S("Kopf hoch, steil und quer", "Kopf hoch. Spieler fünf sieht Spieler acht oben und spielt steil. Von dort geht der Ball quer zu Spieler zwei.",
     bl("n5", list(POS["n8"])), ps("b1", b("n8"), after=True), ps("b1", b("n2"), after=True),
     mv("n4", list(POS["n4"]), delay=0.3), mv("n6", list(POS["n5"]), delay=0.2), mv("n9", list(POS["n6"]), delay=0.6), mv("n3", list(POS["n9"]), delay=1.0)),
   S("Links dasselbe zurück", "Auf der linken Seite läuft es genauso, nur nach unten. Spieler zwei spielt zu Spieler elf, der spielt den Doppelpass mit Spieler sieben. Hinter dem Ball rücken alle eine Station weiter.",
     ps("b1", b("n11")), *dp_links("b1", after=True),
     mv("n2", list(POS["n11"]), delay=1.6), mv("n8", list(POS["n2"]), delay=1.8), mv("n5", list(POS["n8"]), delay=2.0), mv("n10", list(POS["n3"]), delay=0.3)),
   S("Zurück zum Start", "Spieler elf spielt runter zum Start und stellt sich dort hinten an. Die Runde ist durch, und jeder steht eine Station weiter. Jetzt startet Spieler zehn.",
     ps("b1", b("n3")), mv("n11", list(POS["n10"]), delay=0.3), mv("n7", list(POS["n7"]), delay=0.2))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Oben kommt ein zweiter Doppelpass dazu.", "Zwei Doppelpässe",
    "Nach dem ersten Doppelpass spielt der Flügelspieler nicht einfach quer. Er spielt mit dem Stürmer noch einen Doppelpass und schickt den Ball danach diagonal auf die linke Seite. Zwei schnelle Doppelpässe hintereinander, so kommt man durch zwei Linien.",
    sp(n5=tuple(R5)), [B("b1", 68.6, 20.6)] + ERSATZ,
    [S("Steil und gleich der nächste", "Spieler fünf hat den ersten Doppelpass gespielt und spielt steil zu Spieler acht. Der spielt sofort quer zu Spieler zwei und zieht nach innen.",
       bl("n5", list(POS["n8"])), ps("b1", b("n8"), after=True), ps("b1", b("n2"), after=True), mv("n8", [47.5, 13.5], after=True)),
     S("Ablegen und diagonal raus", "Spieler zwei legt in den Lauf ab. Mit dem nächsten Kontakt spielt Spieler acht diagonal durch auf Spieler elf. Dort geht die Runde links weiter.",
       ps("b1", [48.1, 14.1]), ps("b1", b("n11"), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei Bälle laufen gleichzeitig.", "Mit zwei Bällen",
    "Ein zweiter Ball startet oben rechts, genau gegenüber vom ersten. Beide Bälle laufen gleichzeitig durch die Runde. Wer gepasst hat, läuft sofort nach, denn der nächste Ball ist schon unterwegs.",
    sp(), [B("b1", *b("n3")), B("b2", *b("n8"))] + ERSATZ,
    [S("Beide Bälle starten", "Unten spielt Spieler drei auf Spieler neun, der lässt klatschen. Gleichzeitig spielt oben Spieler acht quer und Spieler zwei weiter nach außen.",
       ps("b1", b("n9")), ps("b1", b("n6"), after=True), ps("b2", b("n2")), ps("b2", b("n11"), after=True)),
     S("Zwei Doppelpässe zur selben Zeit", "Jetzt laufen beide Doppelpässe gleichzeitig, rechts nach oben und links nach unten. Wer hier zu spät startet, hält die ganze Runde auf.",
       ps("b1", b("n5")), *dp_rechts("b1", after=True), *dp_links("b2", delay=0.3))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
