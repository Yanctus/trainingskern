import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 50-P8 (U12-U14, Woche 36 Phase 6): Switch Play to Attack - Wave of Play. 30 x 36 Yards = Feld x 29.5-70.5, y 5-55 (27 x 33 m),
# drei Zonen zu 12 Yards (11 m, gestrichelt). Um 180 Grad gedreht: Team Neon (im Original Pink, greift nach unten an) greift
# hier nach oben an. Navy/Gelb -> Rot. Grüne Torhüter 1 und 13 -> neutrale Torhüter TW, Jugendtore.
# Nummern neu (im PDF doppelt): Navy 8 -> Rot 11, Navy 7 -> Rot 12, Navy 4 -> Rot 14, Navy 5 -> Rot 15 (Navy 6, 9 bleiben).
# Stationen: Neon rechts (Spieler acht wartet, Spieler sieben kommt herein), Rot links (12, 9). Wartende Neon 2 und 4 auf der
# Grundlinie neben dem Tor, alle Positionen auf 3D-Abstand gesetzt. Ein Trainer statt zwei.
# Sichtkegel aus PDF und Ton ("awareness of teammates' positioning", Progression 1): Spieler drei schaut sich nach seinen
# Mitspielern um, bevor er die Bahn wechselt (Steigerung 1). Im Video kein Kegel eingezeichnet.
# Fassungen: Steigerung 1 und 2 aus dem Ton. Die Bahnen gehen hier über das ganze Feld (im Video in der Steigerung zwischen
# zwei kleinen Endzonen), die Positionen der Steigerungen sind auf 3D-Abstand gesetzt.
T = P("T", "c", 22, 40, "T")
POS = {"n5": (67, 53), "n3": (33, 50), "n2": (41.5, 55.5), "n4": (58.5, 55.5), "n7": (66, 36), "n8": (75.5, 38.5),
       "r6": (44.5, 30.5), "r11": (57.5, 32), "r15": (37, 4), "r14": (62.5, 4), "r12": (25, 21.5), "r9": (16.5, 21.5),
       "k1": (50, 51.5), "k2": (50, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else ("a" if i[0] == "n" else "b"), x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 25.6, 43.5), B("s2", 22, 43.5)]
LINES = [rect(29.5, 5, 41, 50), line(29.5, 21.67, 70.5, 21.67), line(29.5, 38.33, 70.5, 38.33)]
BAHNEN = LINES + [line(43.17, 5, 43.17, 55), line(56.83, 5, 56.83, 55)]
KEGEL = [C(70.5, 38.3), C(29.5, 21.7)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]
VPOS = dict(n3=(32, 40), n5=(49.5, 35.5), n7=(66.5, 24), r6=(41, 28), r11=(58, 28))

u = {"title": "Welle mit Seitenwechsel", "code": "UE-232", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Torschuss", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 14, "players_max": 14, "field_size": "27 x 33 m",
 "description": "Ein schnelles Wellenspiel drei gegen zwei. Jeder Angriff beginnt mit einem Pflicht-Seitenwechsel, dann greifen drei Spieler zwei Verteidiger in der Mittelzone an und spielen aufs Tor gegenüber. Wer den Angriff abschließt, geht zur Station an der Seite, die anderen zwei werden Verteidiger in der Mittelzone. Dann greift das andere Team an, wieder mit einem Seitenwechsel.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 33 Metern in drei gleich große Zonen geteilt. Oben und unten ein Jugendtor mit Torwart, an jeder Seite ein Hütchen als Station.",
  "Verteilen: Team Neon startet unten an der Grundlinie, Team Rot oben. Zwei Spieler von Team Rot verteidigen in der Mittelzone. An jeder Station wartet ein Team. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Angriff beginnt mit einem Seitenwechsel. Dann kommt ein Spieler von der Station dazu, und drei greifen gegen zwei aufs obere Tor an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Wer abschließt, geht zur Station, die anderen zwei verteidigen in der Mittelzone. Dann greift Team Rot nach unten an."],
 "organisation_show": ORG,
 "coaching_points": ["Den Seitenwechsel schnell und genau spielen", "Mit Ball zur Mitte ziehen, damit links und rechts Platz entsteht", "Die Überzahl schnell nutzen und gut abgestimmt laufen", "Nach dem Abschluss sofort umschalten und verteidigen"],
 "materials": ["2 Jugendtore", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Welle mit Seitenwechsel. Jeder Angriff beginnt mit einem Seitenwechsel, dann greifen drei Spieler zwei Verteidiger an, und jeder Treffer gibt einen Punkt.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 67.6, 53.6)] + ERSATZ,
  "steps": [
   S("Pflicht-Seitenwechsel", "Spieler fünf spielt den Ball quer auf die andere Seite zu Spieler drei. Gleichzeitig starten Spieler fünf und Spieler sieben nach vorn.",
     mv("n3", [40.5, 42]), ps("b1", [41.1, 42.6], delay=0.3), mv("n5", [60, 41], delay=0.5), mv("n7", [66, 26], delay=0.3)),
   S("Zur Mitte ziehen", "Spieler drei dribbelt mit Tempo Richtung Mitte. Spieler sechs muss herausrücken, und Spieler elf bleibt bei Spieler fünf.",
     dr("n3", "b1", [47, 36]), mv("r6", [44, 31], delay=0.2), mv("r11", [59, 37], delay=0.2)),
   S("Auf die andere Seite", "Jetzt ist rechts Platz. Spieler drei spielt in den Lauf von Spieler sieben.",
     mv("n7", [61.5, 15]), ps("b1", [62.1, 15.6], delay=0.3)),
   S("Abschluss: Punkt", "Spieler sieben schießt am Torwart vorbei, und das gibt einen Punkt für Team Neon. Spieler sieben geht zur Station, Spieler drei und Spieler fünf verteidigen jetzt in der Mittelzone. Dann greift Team Rot nach unten an, wieder mit einem Seitenwechsel.",
     ps("b1", [54.5, 5.3]))],
  "dims": dims(29.5, 70.5, 5, 55, "27 m", "33 m", rx=86)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Alle drei Bahnen besetzen.", "Drei Bahnen besetzen",
    "Zwei Linien teilen das Feld längs in drei Bahnen. In jeder Bahn muss ein Angreifer stehen. Wechselt einer die Bahn, füllt ein Mitspieler sofort die frei gewordene Bahn.",
    sp(**VPOS), [B("b1", 32.6, 40.6)] + ERSATZ,
    [S("Umschauen", "Nach dem Seitenwechsel hat Spieler drei den Ball in der linken Bahn. Er schaut sich um: Wo stehen Spieler fünf und Spieler sieben?",
       bl("n3", [48, 30])),
     S("Bahn tauschen", "Spieler drei dribbelt in die mittlere Bahn. Darum läuft Spieler fünf sofort in die frei gewordene linke Bahn. Spieler sechs presst.",
       dr("n3", "b1", [46, 40]), mv("n5", [46, 24], delay=0.2), mv("n5", [38, 20], after=True), mv("r6", [50, 35], delay=0.3)),
     S("Abschluss: Punkt", "Spieler drei spielt zu Spieler fünf, und der dribbelt aufs Tor und trifft. Das gibt einen Punkt für Team Neon.",
       ps("b1", [38.6, 20.6]), dr("n5", "b1", [40, 13], after=True), ps("b1", [45.5, 5.3], after=True))],
    lines=BAHNEN),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Ball muss durch alle drei Bahnen.", "Durch alle drei Bahnen",
    "In jedem Angriff muss der Ball in allen drei Bahnen gewesen sein, als Pass oder im Dribbling. So wird oft verlagert, und die ganze Breite des Feldes wird genutzt.",
    sp(**VPOS), [B("b1", 32.6, 40.6)] + ERSATZ,
    [S("In die Mitte", "Spieler drei spielt in die mittlere Bahn zu Spieler fünf. Spieler sieben kommt auf der rechten Seite entgegen.",
       ps("b1", [50.1, 36.1]), mv("n7", [66.5, 32], delay=0.2)),
     S("Nach rechts", "Spieler fünf spielt direkt weiter in die rechte Bahn zu Spieler sieben. Jetzt war der Ball in allen drei Bahnen.",
       ps("b1", [67.1, 32.6])),
     S("Abschluss: Punkt", "Spieler sieben dribbelt nach vorn und trifft ins Tor, und das gibt einen Punkt für Team Neon.",
       dr("n7", "b1", [63, 15]), mv("r11", [60, 20], delay=0.2), ps("b1", [54.5, 5.3], after=True))],
    lines=BAHNEN)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
