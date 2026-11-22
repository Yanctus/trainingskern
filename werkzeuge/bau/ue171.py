import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 14-P6 (U12-U14, Woche 13 Phase 1): Playing Out From The Back 6 v 4 Game. Um 180 Grad gedreht: Torwart und Jugendtor unten,
# die drei Minitore oben, Neon (im PDF blau) spielt nach oben. Feld x 30-70, y 5-55 als 22 x 27 m: im Text "30 by 15 yards",
# die Skizze ist aber fast quadratisch (Verhältnis 4:5) und 15 Yards wären für zehn Spieler zu schmal, darum nach der Skizze.
# Zwei Außenbahnen (gestrichelt, Start der Außenverteidiger) und ein schmaler Mittelstreifen zwischen den Hälften (gestrichelt).
# Pink -> Rot. Nummern neu: Rot 10 -> Rot 6 (im PDF doppelt mit Neon 10). Positionen auf ein Spaltenraster (3D-Abstand).
# Ein Trainer statt zwei. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 22, 44, "T")
POS = {"n1": (50.2, 52), "n4": (50.2, 36), "n2": (66.8, 30), "n3": (33.6, 30), "n8": (58.5, 14), "n10": (41.9, 14),
       "r9": (41.9, 34), "r7": (33.6, 14), "r6": (50.2, 14), "r11": (66.8, 14)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 22.6, 47.5), B("s2", 19, 47.5)]
LINES = [rect(30, 5, 40, 50), line(35.2, 5, 35.2, 55), line(64.8, 5, 64.8, 55), line(30, 27, 70, 27), line(30, 32, 70, 32)]
TORE = [{"x": 50, "y": 55, "side": "bottom", "size": "jugend"}] + [{"x": x, "y": 5, "side": "top"} for x in (36.4, 50, 63.6)]

u = {"title": "Herausspielen von hinten", "code": "UE-171", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "22 x 27 m",
 "description": "Sechs gegen vier: Team Neon spielt sich mit Torwart, Sechser und zwei Außenverteidigern gegen einen Stürmer von hinten heraus. In der vorderen Hälfte geht es dann vier gegen drei auf drei Minitore. Erobert Team Rot den Ball, kontert es sofort auf das große Tor. Jede Runde beginnt wieder beim Torwart.",
 "organisation": ["Aufbauen: Ein Feld von 22 mal 27 Metern, in zwei Hälften mit einem schmalen Streifen dazwischen. Links und rechts eine Außenbahn. Unten ein Jugendtor, oben drei Minitore.",
  "Verteilen: Team Neon mit Torwart, Sechser, zwei Außenverteidigern und zwei Mittelfeldspielern. Team Rot mit einem Stürmer hinten und drei Verteidigern vorn. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Torwart beginnt. Sechser, Torwart und Außenverteidiger spielen sich am Stürmer vorbei. In der vorderen Hälfte vier gegen drei: Die Außenverteidiger bleiben außen, die roten Außen dürfen nach innen.",
  "Wertung: Treffer ins Minitor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und trifft ins große Tor, gibt das einen Punkt für Team Rot. Danach beginnt wieder der Torwart."],
 "organisation_show": ORG,
 "coaching_points": ["Schräg zum Gegner stehen, damit ein Passweg frei ist", "Unter Druck ruhig bleiben und das Tempo kontrollieren", "Die Außenverteidiger nutzen die ganze Breite und helfen dem Sechser", "Nach Ballverlust sofort umschalten"],
 "materials": ["1 Jugendtor", "3 Minitore", "Hütchen für Feld und Bahnen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Herausspielen von hinten. Sechs gegen vier, und Team Neon spielt sich vom Torwart aus nach vorn bis zu den Minitoren.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(30, 5, 40, 50), "players": sp(), "balls": [B("b1", 50.8, 52.6)] + ERSATZ,
  "steps": [
   S("Abprallen", "Team Neon spielt nach oben. Der Torwart passt zu Neon vier, der direkt zurücklegt. Rot neun läuft an.",
     ps("b1", [50.8, 36.6]), mv("r9", [46, 38], delay=0.3), ps("b1", [50.8, 52.6], after=True)),
   S("Zum Außenverteidiger", "Rot neun ist weg vom Torwart. Der Torwart spielt nach rechts zu Neon zwei.",
     ps("b1", [67.4, 30.6])),
   S("Nach vorn", "Neon zwei passt weit nach vorn zu Neon zehn. Jetzt ist es vier gegen drei.",
     ps("b1", [42.5, 14.6]), mv("n3", [34.5, 20], delay=0.3)),
   S("Steil auf Acht", "Neon acht startet in die Mitte, und Neon zehn spielt ihm den Ball in den Lauf.",
     mv("n8", [52, 8.5]), ps("b1", [52.6, 9.1], delay=0.4)),
   S("Minitor: Punkt", "Neon acht trifft ins mittlere Minitor, und das gibt einen Punkt für Team Neon. Holt Team Rot den Ball, kontert es auf das große Tor. Danach beginnt wieder der Torwart.",
     ps("b1", [50, 5.3]))],
  "dims": dims(30, 70, 5, 55, "22 m", "27 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schräg stehen und aufdrehen.", "Schräg stehen, aufdrehen",
    "Der Sechser steht nicht hinter dem Stürmer, sondern schräg daneben. So ist der Passweg frei, und er kann mit dem ersten Kontakt aufdrehen. Dann spielt er sofort nach vorn oder zur anderen Seite.",
    sp(n4=(41.9, 40), r9=(50.2, 34.5), n2=(66.8, 33), n3=(33.6, 33), r7=(33.6, 17), n8=(58.5, 20), n10=(41.9, 20)), [B("b1", 67.4, 33.6)] + ERSATZ,
    [S("Schräg anbieten", "Neon zwei hat den Ball. Neon vier stellt sich schräg neben Rot neun und bekommt den Pass.",
       ps("b1", [42.5, 40.6])),
     S("Aufdrehen", "Neon vier dreht mit dem ersten Kontakt auf und spielt zur anderen Seite zu Neon drei.",
       dr("n4", "b1", [40.5, 37.5]), ps("b1", [34.2, 33.6], after=True)),
     S("Minitor: Punkt", "Neon drei spielt nach vorn zu Neon zehn. Der trifft ins linke Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [42.5, 20.6]), ps("b1", [36.4, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Mittelfeldspieler kommt zurück.", "Einer kommt zurück",
    "Jetzt darf einer der beiden Mittelfeldspieler in den Mittelstreifen zurückkommen. So hat der Spieler am Ball eine Anspielstation mehr. Der Rückkehrer dreht auf und bringt den Ball nach vorn.",
    sp(n4=(58.5, 40), r9=(50.2, 36), n3=(33.6, 38), r7=(41.9, 33), n10=(41.9, 17), n8=(58.5, 20)), [B("b1", 50.8, 52.6)] + ERSATZ,
    [S("Zum Außenverteidiger", "Der Torwart spielt nach links zu Neon drei. Rot sieben läuft ihn an.",
       ps("b1", [34.2, 38.6]), mv("r7", [39.5, 40], delay=0.3)),
     S("Zehn kommt zurück", "Neon zehn kommt in den Mittelstreifen zurück, und Neon drei passt zu ihm.",
       mv("n10", [40.5, 29]), ps("b1", [41.1, 29.6], delay=0.4)),
     S("Minitor: Punkt", "Neon zehn spielt Neon acht in den Lauf. Der trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
       mv("n8", [58, 10]), ps("b1", [58.6, 10.6], delay=0.3), ps("b1", [63.6, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
