import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 50-P4 (U15-U17, Woche 19 Phase 1): Movement to Receive and Switch Technical (im PDF „Develop Movement to Receive and Finish“).
# 15 x 20 Yards = 14 x 18 m. LANGES FELD QUER (Verhältnis 1,33, Vorbild ue317.py): Im PDF hochkant, hier liegt die Länge
# waagrecht, Feld x 14-84 (18 m), y 4-51 (14 m), so groß wie möglich. Umgerechnet: PDF unten -> links, oben -> rechts,
# PDF links -> oben, PDF rechts -> unten. Startstation (6, 9) also links unten, 11 und 8 rechts unten, 4 rechts oben,
# 2 und 7 links oben, die Puppe in der Mitte, Spieler 10 links neben der Puppe. Keine Tore, darum beide Maßlinien.
# Nur ein Team (Gelb im PDF) -> Team Neon, Nummern wie im PDF. Puppe (Mannequin) als Stange, rote Markierungen als Hütchen
# außen an den Stationen. Wartende 9, 8, 7 neben dem Feld. Ein Trainer, unten an der Seitenlinie (im PDF rechts daneben).
# Ablauf nach PDF, Ton und Video: 6 die Linie entlang auf 11, Mitnahme, 10 löst sich von der Puppe, Annahme mit dem hinteren
# Fuß, Ball an der anderen Seite der Puppe vorbei, Pass in die Ecke zu 4, 4 die Linie entlang zu 2. Jeder läuft seinem Pass
# nach. Danach dieselbe Folge von der anderen Seite (nur im Text). Fassung 1 = PDF Key Coaching Point (erster Kontakt mit dem
# hinteren Fuß, kein falscher Kontakt), Fassung 2 = PDF Progression (Doppelpass des Mittelspielers mit Spieler 4, Pass in den Lauf).
# Sichtkegel aus dem Ton („encourage them to check their shoulders“), im Video nicht eingezeichnet: Spieler zehn schaut zum
# Passgeber (Spieler elf), nimmt an, dann schwenkt der Kegel zu Spieler vier (bl mit von), dazu der Drehpfeil (drehen).
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def richt(a, b, d=20):
    # Blickkegel nicht zu lang: Punkt in Richtung b, etwa 20 Einheiten von a entfernt
    import math
    l = math.dist(a, b)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n6": (20, 45), "n9": (11, 45), "n11": (78, 45), "n8": (87, 45), "n4": (78, 10), "n2": (20, 10), "n7": (11, 10), "n10": (44, 27.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
PUPPE = (51, 27.5)
CONES = [C(16.5, 41), C(81.5, 41), C(81.5, 14), C(16.5, 14), C(*PUPPE, shape="stange")]
LINES = [rect(14, 4, 70, 47)]
DIMS = dims(14, 84, 4, 51, "18 m", "14 m", rx=93)
MITNAHME = (73, 39.5)   # Spieler elf nimmt den Ball aus dem Fuß mit nach innen
SCHEITEL = (37, 30.5)   # dort nimmt Spieler zehn an, nachdem er sich von der Puppe gelöst hat
VORBEI = (41, 22)       # Kontakt mit dem hinteren Fuß: an der anderen Seite der Puppe vorbei
ZUM_BALL, ZUR_ECKE = richt(SCHEITEL, MITNAHME), richt(SCHEITEL, POS["n4"])  # Blickrichtungen von Spieler zehn

u = {"title": "Absetzen von der Puppe", "code": "UE-353", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 7, "players_max": 10,
 "field_size": "14 x 18 m",
 "description": "Eine Passfolge über vier Ecken und einen Spieler in der Mitte. Der Mittelspieler löst sich von einer Puppe, nimmt den Ball mit dem hinteren Fuß an und spielt ihn in die gegenüberliegende Ecke. Dazu kommen Pässe die Linie entlang und eine saubere Mitnahme aus dem Fuß. Jeder läuft seinem Pass nach, danach geht es von der anderen Seite los.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. In jeder Ecke steht ein Hütchen als Station, in der Mitte eine Puppe oder Stange.",
  "Verteilen: Acht Spieler. An zwei Stationen stehen je zwei, an den anderen beiden je einer, einer steht an der Puppe. Die Bälle liegen an der Startstation, der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass die Linie entlang, Mitnahme aus dem Fuß, Pass in die Mitte. Der Mittelspieler löst sich von der Puppe, nimmt mit dem hinteren Fuß an und spielt in die andere Ecke. Von dort geht der Ball die Linie entlang zurück.",
  "Wechsel: Jeder läuft seinem Pass nach zur nächsten Station. Danach beginnt dieselbe Folge von der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Über die Schulter schauen, bevor der Ball kommt", "Mit dem hinteren Fuß annehmen, weg von der Puppe", "Den Ball aus dem Fuß mitnehmen, dann passen", "Nach jedem Pass rufen und nachlaufen"],
 "materials": ["4 Hütchen", "1 Puppe oder Stange", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Absetzen von der Puppe. Eine Passfolge über vier Ecken. In der Mitte löst sich ein Spieler von der Puppe, nimmt mit dem hinteren Fuß an und verlagert in die andere Ecke.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 20.6, 45.6)] + ERSATZ,
  "steps": [
   S("Die Linie entlang", "Spieler sechs fängt an. Flach die Linie entlang zu Spieler elf, und dann läuft er seinem Pass hinterher.",
     ps("b1", fu(POS["n11"])), mv("n6", [66, 49], delay=0.6)),
   S("Mitnahme, Spieler zehn löst sich", "Spieler elf nimmt den Ball aus dem Fuß mit nach innen. Gleichzeitig löst sich Spieler zehn von der Puppe und kommt in den freien Raum.",
     dr("n11", "b1", list(MITNAHME)), mv("n10", list(SCHEITEL), delay=0.2)),
   S("Pass in die Mitte", "Spieler zehn schaut zum Ball. Spieler elf spielt ihn flach an und läuft dann in die Mitte nach.",
     bl("n10", ZUM_BALL), ps("b1", fu(SCHEITEL), after=True), mv("n11", [57, 36], delay=0.6)),
   S("Hinterer Fuß, ab in die Ecke", "Jetzt geht der Blick rüber zu Spieler vier. Spieler zehn nimmt mit dem hinteren Fuß an, an der anderen Seite der Puppe vorbei, und spielt in die Ecke.",
     bl("n10", ZUR_ECKE, von=ZUM_BALL, dauer=1.3), drehen("n10", list(POS["n4"]), gegen=True, delay=0.4),
     dr("n10", "b1", list(VORBEI), after=True), ps("b1", fu(POS["n4"]), after=True)),
   S("Zurück die Linie entlang", "Spieler vier spielt die Linie entlang zu Spieler zwei und läuft hinterher. Spieler zehn geht zur Ecke von Spieler vier. Damit ist die Runde durch, und Spieler zwei startet dieselbe Folge von der anderen Seite.",
     ps("b1", fu(POS["n2"])), mv("n4", [30, 6], delay=0.6), mv("n10", [70, 7], delay=0.3))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt geht mit dem hinteren Fuß weg von der Puppe.", "Hinterer Fuß, weg vom Gegner",
    "Die Puppe ist der Gegenspieler. Wer mit dem vorderen Fuß annimmt, legt sich den Ball genau vor die Puppe und muss neu ansetzen. Mit dem hinteren Fuß geht der Ball an der anderen Seite vorbei, und der Pass kommt sofort. Vorher geht der Kopf über die Schulter.",
    sp(n11=MITNAHME), [B("b1", *fu(MITNAHME))] + ERSATZ,
    [S("Weg von der Puppe", "Spieler zehn steht dicht an der Puppe, wie an einem Gegenspieler. Er löst sich mit ein paar schnellen Schritten und schafft sich Platz.",
       mv("n10", list(SCHEITEL))),
     S("Blick zum Ball", "Jetzt schaut er zum Ball. Spieler elf spielt flach in den Fuß.",
       bl("n10", ZUM_BALL), ps("b1", fu(SCHEITEL), after=True)),
     S("Hinterer Fuß, Puppe umspielt", "Der erste Kontakt geht mit dem hinteren Fuß an der Puppe vorbei, nicht in sie hinein. Ein Kontakt zum Mitnehmen, einer zum Passen, und der Ball ist bei Spieler vier.",
       bl("n10", ZUR_ECKE, von=ZUM_BALL, dauer=1.3), drehen("n10", list(POS["n4"]), gegen=True, delay=0.4),
       dr("n10", "b1", list(VORBEI), after=True), ps("b1", fu(POS["n4"]), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Der Mittelspieler spielt noch einen Doppelpass.", "Doppelpass mit der Mitte",
    "Nach dem Pass in die Ecke sprintet der Mittelspieler Spieler vier entgegen. Spieler vier legt ab und startet die Linie entlang. Der Rückpass kommt vor ihn in den Lauf, dann geht es wie gewohnt zurück zur Startecke.",
    sp(n10=SCHEITEL, n11=MITNAHME), [B("b1", *fu(SCHEITEL))] + ERSATZ,
    [S("Pass in die Ecke, nachrücken", "Spieler zehn hat angenommen und spielt in die Ecke zu Spieler vier. Sofort sprintet er ihm ein Stück entgegen.",
       dr("n10", "b1", list(VORBEI)), ps("b1", fu(POS["n4"]), after=True), mv("n10", [47, 14], after=True)),
     S("Ablegen und starten", "Spieler vier legt flach auf Spieler zehn ab und startet sofort die Linie entlang.",
       ps("b1", fu([47, 14])), mv("n4", [53, 7], delay=0.4)),
     S("In den Lauf, dann zurück", "Spieler zehn spielt den Ball vor Spieler vier in den Lauf. Der spielt die Linie entlang zu Spieler zwei. Danach startet Spieler zwei von der anderen Seite.",
       ps("b1", fu([53, 7])), ps("b1", fu(POS["n2"]), after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
