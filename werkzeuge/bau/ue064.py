import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P53: 20 x 20 Yards = x 28-72, y 8-52. PDF gedreht: Tor oben -> rechts. Schlange in drei Spalten (3D-Abstand).
T = P("T", "c", 24, 4, "T"); cb = [B("b9", 27.5, 4.6), B("b10", 20.5, 4.6)]
Q = [(33, 16), (33, 32), (33, 48), (24.5, 24), (24.5, 40), (16, 32)]
def schlange(nums): return [P("n" + n, "a", x, y, n) for n, (x, y) in zip(nums, Q)]
cones = [C(50, 19), C(50.3, 41.7), C(40.7, 30)]
GK = P("tw", "b", 69.2, 30, "1")
u = {"title": "1 gegen 1 gegen den Torwart", "code": "UE-064", "kind": "Übungsform",
 "focuses": ["Torschuss", "Passspiel"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 10, "field_size": "18 x 18 m",
 "description": "Vor einem Tor mit Torwart stehen drei Hütchen: eines für den Start und je eines links und rechts für den Ableger. Der Stürmer spielt den Ball zum Ableger, bekommt ihn zurück in den Lauf und schließt allein gegen den Torwart ab, das gibt einen Punkt. Danach wird der Stürmer Ableger auf der anderen Seite, und der Ableger stellt sich wieder an. So kommt jeder abwechselnd zum Ablegen und zum Abschluss.",
 "organisation": ["Aufbauen: Ein Tor mit Torwart, davor ein Starthütchen in der Mitte und je ein Hütchen links und rechts für den Ableger.",
  "Starten: Die Kinder warten mit je einem Ball hinter dem Starthütchen, auf einem der Seitenhütchen steht ein Ableger.",
  "Ablauf: Pass zum Ableger, Ablage in den Lauf, Abschluss gegen den Torwart. Danach geht es von der anderen Seite.",
  "Wechseln und einsammeln: Der Stürmer wird Ableger, der Ableger stellt sich hinten an. Nach jeder Runde sammeln alle die Bälle ein."],
 "organisation_show": ORG,
 "coaching_points": ["Genau aufs Tor zielen, nicht so fest wie möglich", "Den Ball mit dem richtigen Tempo ablegen", "Vor dem Abschluss den Kopf heben", "Mit beiden Füßen und auf verschiedene Arten abschließen"],
 "materials": ["1 Tor", "3 Hütchen", "1 Ball pro Kind", "Leibchen für den Torwart"],
 "access": "frei", "hidden": True,
 "say_intro": "Eins gegen eins gegen den Torwart. Hier legt ein Mitspieler den Ball ab, und der Stürmer schließt allein vor dem Torwart ab.",
 "board": {"lines": [rect(28, 8, 44, 44)], "goals": [{"x": 72, "y": 30, "side": "right"}], "cones": cones,
  "players": [GK, P("n11", "a", 41.5, 33, "11"), P("n6", "a", 52.5, 44.5, "6"), *schlange(["10", "2", "8", "3", "7", "9"]), T],
  "balls": [B("b1", 43, 33.6), B("b2", 34.6, 32.6), *cb],
  "steps": [
   S("Pass zum Ableger", "Spieler elf spielt den Ball zu Spieler sechs am rechten Hütchen.", ps("b1", [51.2, 43.3])),
   S("Ablage in den Lauf", "Spieler elf startet Richtung Tor, und Spieler sechs legt ihm den Ball in den Lauf.",
     mv("n11", [54.5, 31.5]), ps("b1", [56, 31.8], delay=0.3)),
   S("Abschluss gegen den Torwart: Punkt", "Allein vor dem Torwart schiebt Spieler elf den Ball ins Eck, und das gibt einen Punkt.",
     ps("b1", [73.8, 27.5]), mv("tw", [69.5, 31.5], delay=0.15)),
   S("Rollentausch, andere Seite", "Jetzt wird Spieler elf Ableger am linken Hütchen, und Spieler sechs trabt zurück zur Schlange.",
     mv("n11", [53.5, 16.5]), mv("n6", [42, 40.5], delay=0.1)),
   S("Von der anderen Seite", "Spieler zwei spielt nun auf Spieler elf, und alles beginnt von der anderen Seite.", ps("b2", [49.8, 17.6]))],
  "dims": [{"x1": 28, "y1": 58.6, "x2": 72, "y2": 58.6, "text": "18 m"}, {"x1": 82, "y1": 8, "x2": 82, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau zielen ist wichtiger als fest schießen.", "Genau statt fest",
    "Ohne Gegenspieler zählt nur eins: das Tor treffen. Wer mit aller Kraft schießt, schießt oft daneben. Besser ist ein flacher, genauer Schuss ins Eck. So treffen die Kinder öfter und gewinnen Vertrauen in ihren Schuss.",
    [GK, P("n2", "a", 60.5, 24, "2"), P("n11", "a", 52.5, 44.5, "11"), *schlange(["10", "3", "7", "8", "9", "6"]), T],
    [B("b1", 62, 24.6), B("b5", 51.2, 43.3), *cb],
    [S("Zu fest und daneben", "Spieler zwei schießt mit voller Wucht, aber der Ball fliegt am Tor vorbei.", ps("b1", [75.5, 19.5])),
     S("Neuer Ball von der Elf", "Spieler elf legt ihm einen neuen Ball vor.", ps("b5", [60, 30]), mv("n2", [58.5, 29.5], delay=0.1)),
     S("Flach ins Eck: Punkt", "Diesmal schiebt Spieler zwei den Ball flach und genau ins Eck, und das gibt einen Punkt.", ps("b5", [73.8, 33]), mv("tw", [69.5, 27], delay=0.1))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Ablage kommt vor den Stürmer, damit er im Lauf bleibt.", "Ablage vor den Stürmer",
    "Der Ableger spielt den Ball nicht in den Fuß, sondern ein Stück vor den Stürmer, mit dem richtigen Tempo. So nimmt der Stürmer den Ball im Laufen mit und kann ohne zu stoppen kontrolliert und genau abschließen.",
    [GK, P("n9", "a", 46, 32.2, "9"), P("n8", "a", 55, 44.5, "8"), P("n7", "a", 50.5, 15, "7"), *schlange(["2", "10", "3", "6", "11"]), T],
    [B("b1", 53.6, 43.6), *cb],
    [S("Pass vor den Stürmer", "Spieler neun läuft los, und Spieler acht spielt den Ball genau vor ihn in den Lauf.",
       mv("n9", [57, 32]), ps("b1", [59.5, 32.2], delay=0.25)),
     S("Im Lauf mitnehmen", "Spieler neun nimmt den Ball im Laufen mit, ohne zu stoppen.", dr("n9", "b1", [62.5, 31.5])),
     S("Abschluss: Punkt", "Dann schließt er kontrolliert ins Eck ab, und das gibt einen Punkt.", ps("b1", [73.8, 27.5]), mv("tw", [69.5, 33.5], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
