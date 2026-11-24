import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-31 (U15-U17, Woche 4 Pre-Season): Passing Accuracy Agility. 20 x 30 Yards = 18 x 27 m (gerundet 18 x 25 m).
# Feld quer wie im PDF (Verhältnis 1,5): x 9-85, y 5-51. Zwei gleiche Rundläufe, um die Feldmitte gedreht (punktsymmetrisch):
# Team Neon (Blau im PDF: 4 Start mit Ball, 9 und 10 warten, 8 an der Puppe, 7 an der Seitenlinie) rechts, Team Rot (Gelb/Pink:
# 8 -> 2 Start, 4 -> 3 und 9 -> 5 warten, 11 an der Puppe, 7 -> 6 an der Seitenlinie; neu nummeriert wegen Doppelter) links.
# Der Rundlauf von Team Rot ist hier genau gespiegelt (im PDF stehen die Stangen links etwas anders); alle Bewegungen von Team Rot
# laufen gleichzeitig und werden mit spiegel() aus denen von Team Neon gerechnet.
# Ablauf nach den Buchstaben im Video: A scharfe Bewegung zum Ball an der Puppe, B Pass durch das Stangentor in den Lauf des Starters,
# langer Ball an die Seite, C Pass in den Fuß, D Starter dreht ab und bekommt den Ball zwischen den Stangen, E Hinterlaufen und mit
# Ball zum Start der anderen Seite dribbeln. Rotation (nicht im Original beschrieben, Annahme): Starter -> Puppe -> Seitenlinie ->
# mit Ball auf die andere Seite.
# Wartende stehen neben dem Feld (3D-Abstand), Puppen als Stangen gezeichnet, Stangen orange statt rot/gelb. Ein Trainer statt zwei,
# unten an der Seitenlinie. Gelbe Markierungen nur am Start und an der Seitenlinie (sonst liegen sie auf den Passwegen).
# Fassungen: PDF Key Coaching Point 1 (kurz, scharf, im Winkel anbieten) und 2 (Ball in den Lauf, dann direkt weiter).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
FX0, FX1, FY0, FY1 = 9, 85, 5, 51
def M(p): return [round(94 - p[0], 1), round(56 - p[1], 1)]
def MP(p): return [round(95.2 - p[0], 1), round(57.2 - p[1], 1)]  # Passziel = Spieler + 0,6, gespiegelt wieder Spieler + 0,6
ROT = {"n4": "r2", "n9": "r3", "n10": "r5", "n8": "r11", "n7": "r6", "b1": "b2"}
def spiegel(moves):
    out = []
    for m in moves:
        k = dict(m); k["who"] = ROT[m["who"]]
        if m.get("ball"): k["ball"] = ROT[m["ball"]]
        k["to"] = MP(m["to"]) if m["type"] == "pass" else M(m["to"])
        if m.get("von"): k["von"] = M(m["von"])
        out.append(k)
    return out
def beide(*moves): return list(moves) + spiegel(moves)
T = P("T", "c", 27, 55.5, "T")
ERSATZ = [B("s1", 30.5, 56), B("s2", 33, 56)]
POS = {"n4": (81, 46.5), "n9": (92.5, 46.5), "n10": (92.5, 30), "n8": (79, 24), "n7": (50, 8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [P(ROT[i], "b", *M((x, y)), ROT[i][1:]) for i, (x, y) in d.items()] + [T]
def baelle(x, y): return [B("b1", x, y), B("b2", *MP((x, y)))] + ERSATZ
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
STANGEN = [(70, 38), (70, 44.2), (49, 18.5), (63.5, 15.5), (57, 24.5), (79, 30)]
CONES = [C(x, y, shape="stange") for p in STANGEN for x, y in (p, M(p))] + [C(*p) for q in [(84, 49.5), (47, 6.5)] for p in (q, M(q))]
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "18 m", rx=97.5)
# Stand nach dem Doppelpass (Start der zweiten Fassung)
NACH_B = {"n4": (63, 43), "n8": (80.5, 36)}

u = {"title": "Passgenau durch die Stangen", "code": "UE-328", "kind": "Übungsform",
 "focuses": ["Passspiel", "Bewegung", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 10, "players_max": 12,
 "field_size": "18 x 25 m",
 "description": "Zwei Gruppen zu fünft spielen gleichzeitig auf zwei gleichen Rundläufen, die am Ende ineinander übergehen. Kurze und lange Pässe wechseln sich ab, dazu kommen scharfe Bewegungen zum Ball, ein Abdrehen und ein Hinterlaufen. Am Ende dribbelt ein Spieler mit Ball zum Start auf der anderen Seite. Fünf Minuten mit hohem Tempo, dann eine Pause.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 18 Metern mit zwei gleichen Rundläufen, um die Mitte gedreht. Jeder Rundlauf hat ein Tor aus zwei Stangen, drei Stangen in der Mitte und eine Puppe außen.",
  "Verteilen: Zwei Gruppen zu fünft, Team Neon und Team Rot, jede auf ihrer Seite. Drei Spieler stehen am Start, der Erste mit Ball. Einer steht an der Puppe, einer in der Mitte der Seitenlinie. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass zur Puppe, der Spieler dort kommt scharf entgegen und spielt durch das Stangentor zurück in den Lauf. Langer Ball an die Seite, Pass in den Fuß. Der Starter dreht ab und bekommt den Ball zwischen den Stangen, dann legt er in den Lauf des Hinterlaufenden. Der dribbelt mit Ball zum Start auf der anderen Seite.",
  "Wechsel: Beide Gruppen laufen gleichzeitig. Jeder rückt eine Station weiter, wer mit dem Ball ankommt, stellt sich am anderen Start an. Fünf Minuten Belastung, dann Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Kurz und scharf zum Ball, nicht im Stehen warten", "Ball flach in den Lauf, nicht in den Rücken", "Genau passen, auch wenn die Beine müde werden", "Reden: Ball fordern, Namen rufen"],
 "materials": ["10 Stangen", "2 Puppen", "4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passgenau durch die Stangen. Zwei Gruppen spielen gleichzeitig einen Rundlauf mit kurzen und langen Pässen. Wer den letzten Ball bekommt, dribbelt rüber auf die andere Seite.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": baelle(81.6, 47.1),
  "steps": [
   S("Scharf zum Ball an der Puppe", "Beide Gruppen starten gleichzeitig, wir schauen auf Team Neon. Spieler acht geht erst hinter die Puppe und kommt dann scharf zum Ball. Spieler vier spielt ihn flach an.",
     *beide(mv("n8", [74, 30]), mv("n8", [80.5, 36], after=True), ps("b1", [81.1, 36.6], after=True))),
   S("Durch das Stangentor zurück", "Spieler vier startet sofort und läuft unter dem Stangentor durch. Spieler acht spielt ihm den Ball durch die Stangen in den Lauf.",
     *beide(mv("n4", [70, 48.5]), mv("n4", [63, 43], after=True), ps("b1", [63.6, 43.6], delay=0.6))),
   S("Langer Ball an die Seite", "Spieler acht dreht ab und sprintet an der Seitenlinie nach vorn. Spieler vier spielt den langen Ball genau dorthin.",
     *beide(mv("n8", [83.5, 26]), mv("n8", [79, 12], after=True), ps("b1", [79.6, 12.6], delay=0.5))),
   S("Pass in den Fuß, abdrehen", "Spieler sieben kommt kurz entgegen und will den Ball in den Fuß. Spieler acht spielt ihn genau so. Gleichzeitig dreht Spieler vier ab und läuft im Bogen zwischen die Stangen.",
     *beide(mv("n7", [63, 9]), ps("b1", [63.6, 9.6], after=True),
            mv("n4", [55, 38], delay=0.2), mv("n4", [51, 28], after=True), mv("n4", [56, 18], after=True))),
   S("Ablegen und hinterlaufen", "Spieler sieben legt zwischen die Stangen auf Spieler vier und läuft sofort hinter ihm vorbei. Spieler vier spielt den Ball direkt in seinen Lauf.",
     *beide(ps("b1", [56.6, 18.6]), mv("n7", [44, 9], delay=0.3), ps("b1", [44.6, 9.6], after=True))),
   S("Mit Ball auf die andere Seite", "Spieler sieben dribbelt mit Tempo zum Start auf der anderen Seite und stellt sich dort an. Jeder rückt eine Station weiter, Spieler vier an die Puppe, Spieler acht an die Seitenlinie. Jetzt startet Spieler neun mit dem Ball, der von drüben kommt.",
     *beide(dr("n7", "b1", [18, 8]), mv("n4", [79, 24], delay=0.4), mv("n8", [50, 8], delay=0.4), mv("n9", [81, 46.5], delay=0.4)))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kurz und scharf anbieten.", "Kurz und scharf anbieten",
    "Wer an der Puppe steht, wartet nicht auf den Ball. Er macht erst ein paar Schritte weg, so als stünde dort ein Gegenspieler. Dann kommt er scharf und im Winkel entgegen. So hat er Platz für die Annahme.",
    sp(), baelle(81.6, 47.1),
    [S("Erst weg vom Ball", "Spieler acht macht zwei, drei Schritte weg und geht hinter die Puppe. Spieler vier wartet mit dem Pass.",
       *beide(mv("n8", [74, 30]))),
     S("Dann scharf entgegen", "Jetzt kommt Spieler acht scharf und schräg entgegen. Genau in dem Moment spielt Spieler vier, und der Ball kommt in den Lauf.",
       *beide(mv("n8", [80.5, 36]), ps("b1", [81.1, 36.6], delay=0.3)))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Ball in den Lauf spielen.", "Den Ball in den Lauf spielen",
    "Der Ball geht nicht auf den Mann, sondern in den Raum vor ihm. Dann nimmt der Läufer ihn im vollen Lauf mit. Ist der Pass gut, kann er gleich mit einem Kontakt weiterspielen.",
    sp(**NACH_B), baelle(63.6, 43.6),
    [S("Der Ball läuft vor dem Läufer", "Spieler acht sprintet an der Seitenlinie nach vorn. Spieler vier spielt nicht zu ihm, sondern in den Raum vor ihm. Ball und Läufer kommen gleichzeitig an.",
       *beide(mv("n8", [83.5, 26]), mv("n8", [79, 12], after=True), ps("b1", [79.6, 12.6], delay=0.5))),
     S("Mit einem Kontakt weiter", "Weil der Pass passt, spielt Spieler acht direkt weiter in den Fuß von Spieler sieben. Kein Stoppen, kein Zwischenschritt.",
       *beide(mv("n7", [63, 9]), ps("b1", [63.6, 9.6], delay=0.3)))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
