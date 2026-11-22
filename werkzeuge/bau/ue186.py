import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-31 (U12-U14, Woche 20 Phase 4): Dribbling, Passing & Agility Activation (Warm Up). 20 x 30 Yards = Feld x 30-70, y 5-55
# (18 x 27 m). Ausrichtung wie im PDF: Stangen oben, Ringe rechts, Hütchen-Slalom unten, Passstation links.
# Ein Team (im PDF pink) -> Team Neon, Nummern wie im PDF (2-13). Wartende stehen neben dem Feld (3D-Abstand), im PDF auf der
# Linie. Ablauf nach PDF-Text: Stangen -> Ball in der Mitte ablegen, Pass vom Hütchen-Dribbler annehmen und nach unten dribbeln;
# Hütchen -> Ringe; Ringe -> Ball in der Mitte holen, Pass quer zu Spieler vier -> links anstellen; links -> zurück zum Start oben.
# Steigerungen aus PDF/Video: Zuwurf mit Volley/Kopfball (unten) und Doppelpass (links).
# Sichtkegel: Im Video "Timing: Get head to assess" (kein Kegel eingezeichnet). Richtung aus dem Sinn: Spieler sieben schaut vor
# dem Pass zu Spieler zwei, der in die Mitte läuft.
T = P("T", "c", 84, 34, "T")
POS = {"n2": (50, 3), "n3": (58.5, 3), "n10": (67, 3),
       "n8": (64, 19), "n13": (76, 17), "n5": (84.5, 17),
       "n4": (34, 30), "n6": (24, 26), "n12": (15.5, 26),
       "n7": (50, 54), "n11": (78, 51), "n9": (86.5, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 88.5, 30.5), B("s2", 88.5, 34.1)]
RINGE = [{"type": "circle", "x": x, "y": y, "r": 1.6} for x, y in ((63, 24), (66, 27), (63, 30), (66, 33), (63, 36))]
LINES = [rect(30, 5, 40, 50)] + RINGE
CONES = ([C(50, y, shape="stange") for y in (9, 14, 19, 24)] + [C(50, y) for y in (50, 46, 42, 38)]
         + [C(43, 36), C(57, 36), C(38.5, 25), C(38.5, 35)])
BAELLE = [B("b1", 50.6, 3.6), B("b2", 50.6, 54.6), B("b3", 59.1, 3.6), B("b4", 78.6, 51.6)] + ERSATZ

u = {"title": "Dribbel-Parcours mit Pässen", "code": "UE-186", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Dribbling", "Koordination"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 12, "players_max": 12, "field_size": "18 x 27 m",
 "description": "Ein Aufwärmen mit vier Stationen, die alle gleichzeitig laufen. Oben wird durch Stangen gedribbelt, rechts auf einem Bein durch Ringe gehüpft, unten durch Hütchen gedribbelt und links mit Seitschritten gewartet. In der Mitte treffen sich die Spieler, legen Bälle ab und passen sich zu. Danach geht jeder zur nächsten Station.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern. Oben vier Stangen, rechts fünf Ringe, unten vier Hütchen im Slalom, links zwei Hütchen.",
  "Verteilen: An jeder Station steht eine kleine Reihe. Oben und unten haben die Spieler Bälle. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Der Stangen-Dribbler legt den Ball in der Mitte ab und bekommt einen Pass vom Hütchen-Dribbler. Der Spieler aus den Ringen holt den abgelegten Ball und passt quer nach links. Der Spieler links dribbelt zurück zum Start.",
  "Wechsel: Jeder geht nach seiner Aufgabe zur nächsten Station. Es geht ohne Pause weiter, bis der Trainer eine kurze Pause ruft."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball beim Dribbeln eng am Fuß führen", "Sauber auf einem Bein durch die Ringe hüpfen: Technik vor Tempo", "Kopf hoch und den Lauf zeitlich gut abstimmen", "Genau passen und laut miteinander reden"],
 "materials": ["4 Stangen", "5 Koordinationsringe", "8 Hütchen", "Einige Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Dribbel-Parcours mit Pässen. Vier Stationen laufen gleichzeitig, und in der Mitte treffen sich die Spieler zum Passen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Alle gleichzeitig", "Alle vier Stationen starten gleichzeitig. Spieler zwei dribbelt durch die Stangen, Spieler acht hüpft auf einem Bein durch die Ringe, Spieler sieben dribbelt durch die Hütchen, und Spieler vier macht schnelle Seitschritte.",
     dr("n2", "b1", [53, 9]), dr("n2", "b1", [47, 14], after=True), dr("n2", "b1", [53, 19], after=True), dr("n2", "b1", [47, 24], after=True),
     mv("n8", [63, 24]), mv("n8", [66, 27], after=True), mv("n8", [63, 30], after=True), mv("n8", [66, 33], after=True), mv("n8", [63, 36], after=True),
     dr("n7", "b2", [53, 50]), dr("n7", "b2", [47, 46], after=True), dr("n7", "b2", [53, 42], after=True), dr("n7", "b2", [47, 38], after=True),
     mv("n4", [34, 26]), mv("n4", [34, 34], after=True), mv("n4", [34, 30], after=True)),
   S("Ablegen und passen", "Spieler zwei lässt den Ball in der Mitte liegen und läuft weiter. Spieler sieben hebt den Kopf, sieht Spieler zwei und passt ihm den Ball in den Lauf.",
     dr("n2", "b1", [50, 28]), mv("n2", [54, 33], after=True), bl("n7", [61, 28], after=True), ps("b2", [54.6, 33.6], after=True)),
   S("Quer nach links", "Spieler acht kommt genau richtig aus den Ringen, holt den abgelegten Ball und passt quer zu Spieler vier. Gleichzeitig dribbelt Spieler zwei nach unten, und Spieler sieben läuft zu den Ringen.",
     mv("n8", [50, 28]), ps("b1", [34.6, 30.6], after=True), dr("n2", "b2", [60, 34]), dr("n2", "b2", [69, 55], after=True), mv("n7", [64, 19])),
   S("Zurück zum Start", "Spieler vier nimmt den Ball mit und dribbelt zurück zum Start oben. Spieler acht stellt sich links an. Geschafft! Jetzt sind Spieler drei, Spieler dreizehn, Spieler elf und Spieler sechs dran, und alles beginnt von vorn.",
     dr("n4", "b1", [41.5, 3]), mv("n8", [40, 31]), mv("n8", [24, 42], after=True))],
  "dims": dims(30, 70, 5, 55, "18 m", "27 m", rx=97)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Volleys und Kopfbälle.", "Volleys und Kopfbälle",
    "Nach den Hütchen nimmt der Spieler den Ball in die Hände. Er ruft laut, wie der Ball zurückkommen soll: links, rechts oder Kopf. Dann wirft er genau, und der Mitspieler spielt den Ball direkt zurück.",
    sp(n2=(56, 32), n7=(46, 36), n8=(66, 33)), [B("b1", 50.6, 28.6), B("b2", 46.6, 36.6), B("b3", 59.1, 3.6), B("b4", 78.6, 51.6)] + ERSATZ,
    [S("Zuwurf", "Spieler sieben nimmt den Ball nach den Hütchen in die Hände, ruft laut links und wirft ihn Spieler zwei zu.",
       ps("b2", [56.6, 32.6])),
     S("Volley zurück", "Spieler zwei spielt den Ball mit links direkt zurück. Dann ruft Spieler sieben Kopf, wirft noch einmal, und Spieler zwei köpft zurück.",
       ps("b2", [46.6, 36.6]), ps("b2", [56.6, 32.6], after=True), ps("b2", [46.6, 36.6], after=True)),
     S("Weiter wie vorher", "Jetzt passt Spieler sieben flach zu Spieler zwei, der nach unten dribbelt. Spieler acht holt den Ball in der Mitte und passt quer zu Spieler vier. Dann sind die Nächsten dran.",
       ps("b2", [56.6, 32.6]), dr("n2", "b2", [60, 34], after=True), dr("n2", "b2", [69, 55], after=True), mv("n8", [50, 28]), ps("b1", [34.6, 30.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Doppelpass auf der linken Seite.", "Doppelpass links",
    "Der Spieler links bekommt den Pass aus der Mitte und spielt ihn direkt zurück. Dann startet er nach vorn und bekommt den Ball in den Lauf. So wird aus dem Querpass ein Doppelpass.",
    sp(n8=(50, 28), n2=(62, 48), n7=(64, 19)), [B("b1", 50.6, 28.6), B("b2", 62.6, 48.6), B("b3", 59.1, 3.6), B("b4", 78.6, 51.6)] + ERSATZ,
    [S("Pass nach links", "Spieler acht hat den Ball in der Mitte und passt quer zu Spieler vier.",
       ps("b1", [34.6, 30.6])),
     S("Direkt zurück", "Spieler vier spielt den Ball direkt zurück zu Spieler acht.",
       ps("b1", [50.6, 28.6])),
     S("In den Lauf", "Spieler vier startet nach vorn, und Spieler acht spielt ihm den Ball in den Lauf.",
       mv("n4", [34, 17]), ps("b1", [34.6, 17.6], delay=0.4)),
     S("Zurück zum Start", "Spieler vier dribbelt zum Start oben, und Spieler acht stellt sich links an. Jetzt sind die Nächsten an allen Stationen dran.",
       dr("n4", "b1", [41.5, 3]), mv("n8", [40, 31]), mv("n8", [24, 42], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
