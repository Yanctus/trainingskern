import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-109 (U15-U17, Woche 6 Pre-Season): Pass, Sprint and Tag. 35 x 30 Yards = 32 x 27 m (gerundet 30 x 25 m), Feld x 20-76, y 5-51.
# Ausrichtung wie im PDF (Start unten, Ball läuft über links, rechts nach oben, dann mit Ball zurück nach unten).
# PDF pink -> Team Neon (4, 5, 7, 8), gold -> Team Rot (9, 10, 11), Nummern wie im PDF (keine doppelten). Gejagt wird immer ein
# Spieler des anderen Teams (Farben wechseln sich im Ablauf ab), darum als Teamwertung: jedes Fangen gibt einen Punkt.
# Puppen (Mannequins) als Stangen. Ein Trainer statt zwei, er steht unten rechts am Rand. Wartende (11, 8 unten, 7 oben) neben dem Feld.
# Grundform: Im Original kommt Spieler zehn durch; hier fängt Spieler vier ihn kurz vor dem Start (zeigt die Wertung, Video
# "TOO SLOW" zeigt ein Fangen an der oberen Puppe).
# Fassung 1 = PDF Key Coaching Point (auf dem hinteren Fuß annehmen, erster Kontakt weg vom Druck, Abstand gewinnen).
# Fassung 2 = PDF Progression (Laufparcours links neben dem Feld: Leiter und Stangenslalom; oben wird jetzt zurückgepasst).
# Sichtkegel: Text "Stay open, scan early", Ton "identifying and exploiting space ahead"; im Video ist nur der Raum für den ersten
# Kontakt eingezeichnet. Richtung aus dem Sinn: Spieler neun schaut vor der Annahme über die Schulter zum Verfolger (Spieler fünf),
# nach der Annahme schwenkt derselbe Kegel zum Passziel (Spieler vier), dazu Drehpfeil (bl mit von, drehen).
T = P("T", "c", 82, 55.3, "T")
ERSATZ = [B("s1", 85.5, 55.8), B("s2", 88, 55.8)]
POS = {"n5": (47.5, 51), "r9": (23.5, 34), "n4": (74.5, 23), "r10": (49, 6.5), "n7": (59.5, 2.8), "r11": (56, 55.3), "n8": (64.5, 55.3)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(20, 5, 56, 46)]
PUPPEN = [C(49, 11, shape="stange"), C(65, 18, shape="stange"), C(33, 33, shape="stange"), C(47, 45.5, shape="stange")]
# Steigerung: Laufparcours links neben dem Feld
PARCOURS = [leiter(13, 13, senkrecht=True), C(14, 27, shape="stange"), C(14, 33, shape="stange"), C(14, 39, shape="stange"), C(14, 45, shape="stange")]
DIMS = dims(20, 76, 5, 51, "30 m", "25 m", rx=86)
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Passen, nachsetzen, fangen", "code": "UE-334", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Schnelligkeit"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 7, "players_max": 10,
 "field_size": "30 x 25 m",
 "description": "Ein Passweg um vier Puppen mit Jagd. Wer den Ball gespielt hat, sprintet sofort hinterher und will den Mitspieler fangen, bevor der weiterspielt. Oben angekommen, dribbelt der Letzte mit Ball zurück zum Start, und sein Verfolger setzt nach. Jedes Fangen gibt einen Punkt für das Team des Verfolgers.",
 "organisation": ["Aufbauen: Ein Feld von 30 mal 25 Metern. Darin stehen vier Puppen: unten, links, rechts und oben.",
  "Verteilen: Zwei Teams. An jeder Puppe steht ein Spieler, abwechselnd von Team Neon und Team Rot. Die anderen warten am Start unten, einer wartet oben. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Pass vom Start nach links, von dort nach rechts und dann nach oben. Nach jedem Pass sprintet der Passgeber hinterher und versucht, den Angespielten zu fangen. Oben nimmt der Spieler den Ball mit und dribbelt mit Tempo zurück zum Start, sein Verfolger setzt nach.",
  "Wertung und Wechsel: Jedes Fangen gibt einen Punkt für das Team des Verfolgers. Wer gejagt hat, übernimmt die Station. Der Verfolger von oben stellt sich oben an, der Dribbler unten. Dann startet der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und scharf in den Fuß passen", "Auf dem hinteren Fuß annehmen, erster Kontakt weg vom Verfolger", "Nach dem Pass sofort lossprinten", "Oben mit großen Kontakten Tempo machen"],
 "materials": ["4 Puppen oder Stangen", "1 Koordinationsleiter", "4 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passen, nachsetzen, fangen. Der Ball läuft einmal um die Puppen, und wer gespielt hat, jagt den Nächsten. Jedes Fangen gibt einen Punkt für sein Team.",
 "board": {"lines": LINES, "goals": [], "cones": PUPPEN, "players": sp(), "balls": [B("b1", *fuss(47.5, 51))] + ERSATZ,
  "steps": [
   S("Pass nach links, sofort hinterher", "Spieler fünf spielt flach zu Spieler neun. Sofort sprintet er hinterher. Er will ihn fangen, bevor der Ball weg ist.",
     ps("b1", fuss(23.5, 34)), mv("n5", [27.5, 38.5], delay=0.4)),
   S("Mitnehmen und nach rechts", "Spieler neun nimmt den Ball nach vorn mit und spielt quer zu Spieler vier. Spieler fünf kommt zu spät. Jetzt jagt Spieler neun hinterher.",
     dr("r9", "b1", [26, 29.5]), mv("n5", [25.5, 33], delay=0.3), ps("b1", fuss(74.5, 23), after=True), mv("r9", [70, 25.5], after=True)),
   S("Nach oben zu Spieler zehn", "Spieler vier legt sich den Ball nach oben vor und spielt zu Spieler zehn. Gleich hinterher, dieses Mal läuft Spieler vier los.",
     dr("n4", "b1", [75, 15]), mv("r9", [73.5, 20.5], delay=0.3), ps("b1", fuss(49, 6.5), after=True), mv("n4", [56, 8.5], after=True)),
   S("Mit Ball zurück zum Start", "Spieler zehn nimmt den Ball an der Puppe vorbei mit. Mit großen Kontakten dribbelt er nach unten. Spieler vier bleibt ihm dicht auf den Fersen.",
     dr("r10", "b1", [43, 12]), dr("r10", "b1", [45, 28], after=True), dr("r10", "b1", [52, 42], after=True),
     mv("n4", [51, 25], delay=0.8), mv("n4", [55, 39], after=True)),
   S("Gefangen: Punkt", "Kurz vor dem Start holt Spieler vier ihn ein und fängt ihn. Das gibt einen Punkt für Team Neon. Alle sind eine Station weiter, und Spieler elf startet mit dem nächsten Ball.",
     dr("r10", "b1", [53, 48.5]), mv("n4", [55.5, 46], delay=0.2))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erster Kontakt weg vom Verfolger.", "Erster Kontakt weg vom Druck",
    "Wer angespielt wird, schaut vorher über die Schulter, wo der Verfolger kommt. Er nimmt den Ball auf dem hinteren Fuß an, offen zum Feld. Der erste Kontakt geht nach vorn, weg vom Verfolger. So wächst der Abstand, und der nächste Pass kommt ohne Druck.",
    sp(), [B("b1", *fuss(47.5, 51))] + ERSATZ,
    [S("Erst über die Schulter schauen", "Bevor der Ball kommt, schaut Spieler neun über die Schulter. Wo ist Spieler fünf? Dann kommt der Pass, und Spieler fünf sprintet los.",
       bl("r9", [47.5, 51]), ps("b1", fuss(23.5, 34), after=True), mv("n5", [29, 40], delay=1.2)),
     S("Annehmen, aufdrehen, weg vom Druck", "Spieler neun nimmt den Ball auf dem hinteren Fuß an und dreht auf. Der erste Kontakt geht nach vorn, weg von Spieler fünf. Jetzt hat er Luft und spielt sauber zu Spieler vier.",
       bl("r9", [74.5, 23], von=[47.5, 51], dauer=1.3), drehen("r9", [74.5, 23], gegen=True, delay=0.4),
       dr("r9", "b1", [27.5, 28.5], after=True), mv("n5", [25, 33.5], delay=0.8), ps("b1", fuss(74.5, 23), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem letzten Pass geht es durch den Laufparcours.", "Mit Laufparcours",
    "Links neben dem Feld liegen eine Leiter und vier Stangen. Oben dribbelt keiner mehr nach unten. Spieler zehn spielt den Ball zurück zum Start und läuft dann durch die Leiter und im Slalom um die Stangen zurück. Gleichzeitig geht es im Feld schon mit dem nächsten Ball weiter.",
    sp(n5=(23.5, 34), r9=(74.5, 23), n4=(56, 12), n7=(66, 2.8), r10=(42, 12), r11=(55, 51), n8=(64, 55.3)),
    [B("b1", *fuss(42, 12))] + ERSATZ,
    [S("Oben zurück zum Start", "Spieler zehn hat oben angenommen. Jetzt spielt er den Ball weit und flach zurück zu Spieler elf am Start.",
       ps("b1", fuss(55, 51))),
     S("Leiter, Slalom, zurück", "Sofort läuft Spieler zehn zur Leiter, durch jedes Feld ein Fuß, dann im Slalom um die Stangen und zurück zum Start. Gleichzeitig spielt Spieler elf schon zu Spieler fünf und jagt hinterher.",
       *weg("r10", [[24, 4], [13, 3.5], [13, 22.5], [17.5, 27], [10.5, 33], [17.5, 39], [10.5, 45], [16, 50], [24, 55.5], [40, 55.5]]),
       dr("r11", "b1", [51, 52.5], delay=0.4), ps("b1", fuss(23.5, 34), after=True), mv("r11", [28, 39], after=True))],
    cones=[dict(c, id="k%d" % i) for i, c in enumerate(PUPPEN + PARCOURS, 1)], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
