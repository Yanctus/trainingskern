import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 50-P3 (U15-U17, Woche 38 Phase 4): Passing Combos to Switch (Technical). 15 x 20 Yards = 14 x 18 m.
# LANGES FELD QUER (Verhältnis 1,33, Vorbild ue317.py/ue353.py): Im PDF hochkant, hier liegt die Länge waagrecht, Feld x 14-84
# (18 m), y 4-51 (14 m). Umgerechnet: PDF unten -> links, oben -> rechts, PDF links -> oben, PDF rechts -> unten.
# Nur ein Team (Gelb im Video, Pink im PDF) -> Team Neon, Nummern wie im Video (3, 6, 2, 8, 5, 7, 9, 11, 12, Mittelpaar 10 und 4).
# Zwei Puppen (Mannequins) als Stangen, rote Markierungen als Hütchen außen an den Stationen. Spieler zwölf wartet neben dem
# Feld (3D-Abstand zu Spieler drei). Spieler vier etwas zur Mitte gerückt (3D-Abstand in der Steigerung). Ein Trainer, unten an
# der Seitenlinie (im PDF rechts daneben, also quer unten).
# Ablauf nach PDF, Ton und Video: 3 Doppelpass mit 6, durch auf 2, 2 die Linie entlang zu 8, 8 in die Mitte auf 10 (der weitere
# Mittelspieler), 10 legt ab auf 4, 4 spielt quer zu 11. Jeder läuft seinem Pass nach, dann dieselbe Folge von der anderen Seite
# (11 mit 9, nur im Text). Keine Punktwertung im Original (Technikübung).
# Fassung 1 = PDF Key Coaching Point (realistisch von der Puppe lösen, Laufweg timen), Fassung 2 = PDF Progression / Ton
# (zusätzlicher Doppelpass am Anfang: 2 legt ab auf 6, 6 spielt außen; und am Ende: 4 läuft nach, 11 legt ab, 4 spielt zu 9).
# Sichtkegel aus Text und Ton („Visualise where the next pass will be played“, „player eye contact“), im Video nicht
# eingezeichnet: Spieler zehn schaut zum Passgeber, Spieler vier schaut zu Spieler zehn, nimmt an, und erst dann schwenkt sein
# Kegel zu Spieler elf (bl mit von). Kein Drehpfeil: Spieler vier muss für den Pass zu Spieler elf nicht aufdrehen.
# Keine Dublette: UE-353 (50-P4) hat einen Mittelspieler und eine Puppe ohne Doppelpass und Ablage, UE-190 (50-P2),
# UE-101 (50-P5) und UE-232 (50-P8) sind ganz andere Formen.
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def richt(a, b, d=20):
    # Blickkegel nicht zu lang: Punkt in Richtung b, etwa d Einheiten von a entfernt
    l = math.dist(a, b)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n3": (20, 7.3), "n12": (7, 9), "n6": (16, 24.2), "n2": (19, 45), "n8": (40, 49), "n5": (60, 47.7),
       "n7": (75.6, 47), "n9": (82, 27), "n11": (76, 7.3), "n10": (56.5, 28.3), "n4": (36, 26.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
PUPPE_O, PUPPE_U = (61, 27.5), (40.6, 27.5)
CONES = [C(17, 4.5), C(14, 20.5), C(16.5, 48.5), C(36.5, 51), C(63.5, 51), C(79, 50.5), C(84, 23.5), C(79.5, 4.5),
         C(*PUPPE_O, shape="stange"), C(*PUPPE_U, shape="stange")]
LINES = [rect(14, 4, 70, 47)]
DIMS = dims(14, 84, 4, 51, "18 m", "14 m", rx=93)
VOR = (27, 17)        # dorthin startet Spieler drei nach seinem Pass für den Doppelpass
ABLAGE = (43.4, 33)   # dort bekommt Spieler vier die Ablage von Spieler zehn
UM_PUPPE = (38, 32)   # Zwischenpunkt, damit Spieler vier nicht durch seine Puppe läuft
def vier_kommt(**k): return [mv("n4", list(UM_PUPPE), **k), mv("n4", list(ABLAGE), after=True)]
ZUM_ACHTER = richt(POS["n10"], POS["n8"])
ZUM_ZEHNER, ZUM_ELFER = richt(ABLAGE, POS["n10"]), richt(ABLAGE, POS["n11"])

u = {"title": "Kombinieren zum Seitenwechsel", "code": "UE-405", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 12,
 "field_size": "14 x 18 m",
 "description": "Eine feste Passfolge mit vielen kurzen Kombinationen. Sie beginnt mit einem Doppelpass in einer Ecke, dann läuft der Ball über die Außenbahn in die Mitte. Dort lösen sich zwei Spieler von ihren Puppen, legen sich den Ball ab und verlagern quer in die andere Ecke. Jeder läuft seinem Pass nach, und von dort geht es auf der anderen Seite wieder los.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. An den Rändern acht Hütchen als Stationen, in der Mitte zwei Puppen oder Stangen hintereinander.",
  "Verteilen: Elf Spieler. An der Startecke stehen zwei mit Bällen, an jeder anderen Station einer. Zwei Spieler stehen in der Mitte, jeder an seiner Puppe. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass an der Startecke, Pass durch auf die andere Seite, die Linie entlang und in die Mitte zum weiteren Mittelspieler. Der legt ab auf seinen Partner, und der spielt quer in die andere Ecke.",
  "Wechsel: Jeder läuft seinem Pass nach zur nächsten Station. Ist der Ball in der anderen Ecke, beginnt dort dieselbe Folge von der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Wenn es geht, mit einem Kontakt spielen", "Weg von der Puppe, dann anbieten", "Blickkontakt vor dem Pass, dann rufen", "In der Mitte scharf passen"],
 "materials": ["8 Hütchen", "2 Puppen oder Stangen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Kombinieren zum Seitenwechsel. Doppelpass, raus auf die Außenbahn, in die Mitte und quer in die andere Ecke. Das Mittelpaar steht dabei an zwei Puppen.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *fu(POS["n3"])), B("b2", *fu(POS["n12"]))] + ERSATZ,
  "steps": [
   S("Doppelpass an der Startecke", "Spieler drei fängt an. Kurzer Pass zu Spieler sechs, und sofort startet er nach vorn. Der Ball kommt direkt zurück in den Lauf.",
     ps("b1", fu(POS["n6"])), mv("n3", list(VOR), delay=0.3), ps("b1", fu(VOR), after=True)),
   S("Durch auf Spieler zwei", "Jetzt spielt Spieler drei den Ball quer durch auf die andere Seite zu Spieler zwei. Flach und mit Tempo.",
     ps("b1", fu(POS["n2"]))),
   S("Die Linie entlang", "Spieler zwei spielt die Linie entlang zu Spieler acht und läuft hinterher. Spieler drei rückt auf die Station von Spieler zwei nach.",
     ps("b1", fu(POS["n8"])), mv("n2", [29, 50], delay=0.5), mv("n3", list(POS["n2"]), delay=0.3)),
   S("In die Mitte zu Spieler zehn", "Spieler zehn schaut zum Ball. Spieler acht spielt ihn scharf in die Mitte, an Spieler vier vorbei zum weiteren der beiden.",
     bl("n10", ZUM_ACHTER), ps("b1", fu(POS["n10"]), after=True)),
   S("Ablage auf Spieler vier", "Spieler vier löst sich von seiner Puppe und kommt schräg nach vorn. Er schaut zu Spieler zehn, und der legt mit einem Kontakt ab.",
     *vier_kommt(), bl("n4", ZUM_ZEHNER, after=True), ps("b1", fu(ABLAGE), after=True)),
   S("Quer in die andere Ecke", "Mit der Annahme geht der Blick rüber, und Spieler vier spielt quer zu Spieler elf. Jeder läuft seinem Pass nach. Jetzt beginnt Spieler elf dieselbe Folge von der anderen Seite, mit dem Doppelpass mit Spieler neun.",
     bl("n4", ZUM_ELFER, von=ZUM_ZEHNER, dauer=1.3), ps("b1", fu(POS["n11"]), after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Von der Puppe lösen, und zwar zur richtigen Zeit.", "Von der Puppe lösen",
    "Die Puppe ist der Gegenspieler. Wer an ihr klebt, bekommt im Spiel keinen Ball. Erst ein paar Schritte weg, dann schnell zurück in den freien Raum. Losgehen, wenn der Passgeber den Ball schon hat, nicht früher.",
    sp(n2=(29, 50), n3=POS["n2"], n10=(59, 31)), [B("b1", *fu(POS["n8"])), B("b2", *fu(POS["n12"]))] + ERSATZ,
    [S("Erst weg, dann kommen", "Spieler acht hat den Ball. Spieler zehn zieht seinen Gegenspieler erst ein paar Schritte mit nach hinten. Dann kommt er schnell zurück in den freien Raum.",
       mv("n10", [65, 22]), mv("n10", [55, 31], after=True)),
     S("Jetzt kommt der Pass", "Genau in dem Moment schaut er zum Ball, und Spieler acht spielt ihn an.",
       bl("n10", richt((55, 31), POS["n8"])), ps("b1", fu((55, 31)), after=True)),
     S("Spieler vier im richtigen Moment", "Spieler vier wartet, bis der Ball unterwegs ist. Dann löst er sich von seiner Puppe, bekommt die Ablage und spielt quer zu Spieler elf.",
       *vier_kommt(), ps("b1", fu(ABLAGE), after=True), ps("b1", fu(POS["n11"]), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Doppelpässe mehr.", "Zwei Doppelpässe mehr",
    "Am Anfang legt Spieler zwei auf Spieler sechs ab, und erst der spielt außen auf Spieler acht. Am Ende läuft Spieler vier seinem Querpass nach, bekommt den Ball von Spieler elf zurück und spielt zu Spieler neun. Mehr Pässe heißt mehr Tempo, und alle bleiben wach, auch vor und nach ihrem Einsatz.",
    sp(n3=VOR), [B("b1", *fu(POS["n2"])), B("b2", *fu(POS["n12"]))] + ERSATZ,
    [S("Ablegen und außen", "Spieler zwei hat den Ball. Spieler sechs sprintet ihm entgegen und bekommt die Ablage. Direkt geht es außen weiter zu Spieler acht.",
       mv("n6", [27.6, 38]), ps("b1", [28.2, 38.6], after=True), ps("b1", fu(POS["n8"]), after=True)),
     S("Mitte und Ablage", "Wie vorher in die Mitte zu Spieler zehn. Spieler vier löst sich von seiner Puppe und bekommt die Ablage.",
       bl("n10", ZUM_ACHTER), ps("b1", fu(POS["n10"]), after=True), *vier_kommt(delay=0.4), ps("b1", fu(ABLAGE), after=True)),
     S("Quer und noch ein Doppelpass", "Spieler vier spielt quer zu Spieler elf und läuft sofort nach. Spieler elf legt ab, und Spieler vier spielt weiter zu Spieler neun. Von dort beginnt die nächste Runde.",
       ps("b1", fu(POS["n11"])), mv("n4", [60, 12.5], delay=0.4), ps("b1", [60.6, 13.1], after=True), ps("b1", fu(POS["n9"]), after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
