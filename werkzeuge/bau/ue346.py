import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-48 (U15-U17, Woche 17 Phase 3): Pass and Sprint Activation, Warm Up. 25 x 30 Yards = 23 x 27 m (nach der Meter-Regel 25 x 25 m).
# Hochkant wie im PDF (Verhältnis 1,2), Start unten, es geht Station für Station nach oben. Feld x 29-71, y 4-54.
# Zwei Reihen mit je fünf Stangen (x 41 und 60), in der Mitte vier Hütchen (im PDF rot, hier orange).
# Nur die erste Dreiergruppe (Pink 8, 6, 4) auf der Tafel, als Team Neon mit den Nummern aus dem PDF. Die anderen Gruppen
# (Gelb 10, 6, 9 und Navy 4, 5, 3, Nummern doppelt) stehen nur im Text (3D-Abstand an der Grundlinie). Ein Trainer statt zwei.
# Ablauf nach PDF und Video 0:12-0:21: Station eins wie im PDF (8 passt zu 6, 6 legt ab, 8 kommt um die Stange, 4 sprintet um
# das Hütchen und außen um die Stange, 8 spielt ihn an, 8 sprintet zum nächsten Hütchen). Station zwei gespiegelt mit neuen
# Rollen (4 passt rüber zu 6, Ablage auf 4, 8 kommt um Hütchen und Stange). Danach nur im Text: weiter bis oben, zurück sprinten.
# Fassungen: PDF Key Coaching Point 1 (Sprint um das Hütchen) und 2 (Pass, um die Stange, Ablage mit einem Kontakt).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 78, 47, "T")
ERSATZ = [B("s1", 81.5, 50), B("s2", 81.5, 44)]
POS = {"n8": (41, 55.5), "n6": (60, 55.5), "n4": (53.5, 39)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(29, 4, 42, 50)]
REIHEN = [11, 21.5, 32, 42.5, 53]
CONES = [C(x, y, shape="stange") for y in REIHEN for x in (41, 60)] + [C(50, y) for y in (4.3, 14, 23.2, 36.3)]
DIMS = dims(29, 71, 4, 54, "25 m", "25 m", rx=87)
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
# Laufwege
UM_STANGE_1 = [[37, 52], [38.5, 48.5], [43.5, 48], [49, 50.5]]           # 8 um die linke Stange unten
UM_HUET_1 = [[49.5, 40.5], [45.5, 37], [47.5, 32.5], [53, 33], [63.5, 40], [64, 46]]  # 4 um das Hütchen und außen um die rechte Stange
UM_STANGE_2 = [[63.5, 41], [60, 38.5], [55, 39], [51, 41.5]]             # 4 um die rechte Stange zur Mitte
UM_HUET_2 = [[53.5, 26], [52.5, 20], [47, 20], [37.5, 27.5], [36.5, 33.5]]  # 8 um das Hütchen und außen um die linke Stange

u = {"title": "Pass, Ablage, Sprint", "code": "UE-346", "kind": "Übungsform",
 "focuses": ["Passspiel", "Schnelligkeit", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 6, "players_max": 12,
 "field_size": "25 x 25 m",
 "description": "Ein Aufwärmen für Pass und Antritt in Dreiergruppen. Der Erste spielt rüber, bekommt den Ball abgelegt, nachdem er um die Stange gelaufen ist, und spielt den Dritten an, der um Hütchen und Stange gesprintet ist. Dann geht es von der anderen Seite mit neuen Rollen eine Station höher weiter. Die nächste Gruppe startet, sobald die erste weitergerückt ist.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern. Zwei Reihen mit je fünf Stangen von unten nach oben, dazwischen in der Mitte vier Hütchen.",
  "Verteilen: Dreiergruppen mit je einem Ball. Die erste Gruppe steht am Start: zwei unten an der Grundlinie, einer am untersten Hütchen in der Mitte. Die nächsten Gruppen warten dahinter. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass rüber, Ablage mit einem Kontakt auf den Passgeber, der um die Stange kommt. Der Dritte sprintet um das Hütchen und außen um die Stange und wird angespielt. Der Passgeber sprintet zum nächsten Hütchen, und von der anderen Seite geht es mit neuen Rollen weiter.",
  "Wechsel: Nach der letzten Station sprinten alle drei zurück zum Start und beginnen von vorn. Die nächste Gruppe startet, sobald die erste an der zweiten Station ist."],
 "organisation_show": ORG,
 "coaching_points": ["Zwischen den Aktionen immer Vollgas", "Flach und scharf passen, damit es direkt weitergeht", "Ankommen, wenn der Ball kommt", "Auf den Fußballen bleiben, gleich kommt die nächste Rolle"],
 "materials": ["10 Stangen", "4 Hütchen", "Ein Ball pro Gruppe"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pass, Ablage, Sprint. Ein Aufwärmen in Dreiergruppen. Jeder passt, legt ab und sprintet, und an jeder Station tauschen die Rollen.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 41.6, 56.1)] + ERSATZ,
  "steps": [
   S("Pass rüber, dann um die Stange", "Spieler acht spielt flach rüber zu Spieler sechs. Sofort läuft er links herum um die Stange und kommt in die Mitte.",
     ps("b1", [60.6, 56.1]), *weg("n8", UM_STANGE_1, delay=0.3)),
   S("Ablage, Sprint ums Hütchen", "Spieler sechs legt mit einem Kontakt ab, genau in den Lauf. Gleichzeitig sprintet Spieler vier um das Hütchen und außen um die Stange.",
     ps("b1", [49.6, 51.1]), *weg("n4", UM_HUET_1)),
   S("Pass zu vier, Sprint nach vorn", "Spieler acht spielt Spieler vier an. Dann sprintet er zum nächsten Hütchen. Spieler sechs wechselt rüber auf die andere Seite.",
     ps("b1", [64.6, 46.6]), mv("n8", [46.5, 26.5], after=True), mv("n6", [37, 46.5], delay=0.6)),
   S("Andere Seite, neue Rollen", "Jetzt kommt alles von der anderen Seite. Spieler vier spielt rüber zu Spieler sechs und läuft um seine Stange in die Mitte.",
     ps("b1", [37.6, 47.1]), *weg("n4", UM_STANGE_2, delay=0.3)),
   S("Ablage und Pass zu acht", "Spieler sechs legt ab auf Spieler vier. Spieler acht sprintet um das Hütchen und außen um die Stange, und Spieler vier spielt ihn an.",
     ps("b1", [51.6, 42.1]), *weg("n8", UM_HUET_2), ps("b1", [37.1, 34.1], delay=2.4)),
   S("Station für Station nach oben", "So geht es Station für Station nach oben, jedes Mal mit neuen Rollen. Nach der letzten Station sprinten alle drei zurück zum Start. Die nächste Gruppe ist da schon unterwegs, sie startet, sobald die erste weiterrückt.",
     mv("n4", [54.5, 36]), mv("n4", [53.5, 16.5], after=True), mv("n6", [64, 35.5], delay=0.2))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vollgas um das Hütchen.", "Vollgas um das Hütchen",
    "Der Dritte sprintet mit voller Kraft um das Hütchen und außen um die Stange. Er kommt genau dann an, wenn der Ball unterwegs ist. Wer nur trabt, lässt den Passgeber warten, und das Tempo ist weg.",
    sp(n8=(45, 51)), [B("b1", 45.6, 51.6)] + ERSATZ,
    [S("Eng um das Hütchen", "Spieler acht hat die Ablage. Spieler vier geht eng um das Hütchen, mit kurzen Schritten und dem Körper nach innen gelegt.",
       *weg("n4", UM_HUET_1[:5])),
     S("Ankommen, wenn der Ball kommt", "Der Pass ist schon unterwegs, während Spieler vier noch um die Stange biegt. Er läuft in den Ball hinein und nimmt ihn im Lauf mit.",
       mv("n4", [64, 46]), ps("b1", [64.6, 46.6], delay=0.2))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Passen, um die Stange, und mit einem Kontakt weiter.", "Ablage mit einem Kontakt",
    "Nach dem Pass geht es sofort los um die Stange. Der Pass kommt flach und so scharf, dass die Ablage mit einem Kontakt klappt. Die Ablage landet genau im Laufweg. So bleibt alles im Fluss.",
    sp(), [B("b1", 41.6, 56.1)] + ERSATZ,
    [S("Passen und sofort los", "Spieler acht spielt flach und scharf auf Spieler sechs. Er wartet nicht, er läuft direkt los um die Stange.",
       ps("b1", [60.6, 56.1]), *weg("n8", UM_STANGE_1, delay=0.2)),
     S("Ablage in den Lauf", "Spieler sechs legt mit einem Kontakt ab, genau in den Lauf von Spieler acht. Der nimmt den Ball mit und spielt gleich weiter.",
       ps("b1", [49.6, 51.1]), *weg("n4", UM_HUET_1), ps("b1", [64.6, 46.6], delay=2.2))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
