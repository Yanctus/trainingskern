import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P6 (U12-U14, Woche 30 Phase 6): Developing the Back 4 Unit. 45 x 30 Yards = Feld x 25-75, y 9-43 (41 x 27 m), längs in vier
# Bahnen (drei gestrichelte Linien wie im Video). Gespiegelt (oben/unten): im PDF liegen die drei Minitore unten, hier oben, und
# Team Rot greift nach oben an; die zwei Minitore für den Konter stehen unten an den Ecken, der Trainer unten mit Bällen.
# Pink (Viererkette) -> Team Neon (2, 3, 4, 5), blau (Angreifer) -> Team Rot (7, 9, 10, 11), Nummern wie im PDF, links/rechts wie
# im PDF. Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video (CB presses / provide cover / strong recovery).
# Wertung wie im Original: Treffer von Team Rot ein Punkt, Treffer von Team Neon zwei Punkte.
# Sichtkegel: Text "Awareness to cover primary pressing defender", Ton "Players must be aware of where and when the primary
# pressing defender steps out" -> in der Grundform bl() von Spieler fünf zu Spieler drei und dem Ballführer, bevor er absichert
# (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 50, 50, "T")
POS = {"n3": (31, 20), "n5": (42, 22), "n4": (58, 22), "n2": (69, 20),
       "r7": (29, 37), "r9": (40, 38), "r10": (60, 38), "r11": (71, 37)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 53.5), B("s2", 50, 53.5)]
LINES = [rect(25, 9, 50, 34), line(37.5, 9, 37.5, 43), line(50, 9, 50, 43), line(62.5, 9, 62.5, 43)]
TORE = [{"x": x, "y": 9, "side": "top"} for x in (29.5, 50, 70.5)] + [{"x": x, "y": 43, "side": "bottom"} for x in (28.5, 71.5)]

u = {"title": "Viererkette vor drei Minitoren", "code": "UE-212", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "41 x 27 m",
 "description": "Vier Verteidiger schützen als Viererkette drei Minitore, vier Angreifer wollen durch die Kette und treffen. Die Kette schiebt mit dem Ball: Einer presst, die anderen sichern ab und bleiben eng zusammen. Erobern die Verteidiger den Ball, kontern sie auf zwei Minitore in den Ecken. Ihr Treffer zählt doppelt.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 27 Metern, längs in vier Bahnen geteilt. Oben drei Minitore, unten in den beiden Ecken je ein Minitor.",
  "Verteilen: Team Neon verteidigt mit vier Spielern die oberen Minitore. Team Rot greift mit vier Spielern an. Der Trainer steht unten mit Bällen.",
  "Ablauf: Der Trainer spielt einen Ball zu Team Rot, und vier gegen vier geht es los. Team Neon presst, schiebt und sichert ab. Erobert Team Neon den Ball, kontert es auf die Minitore unten.",
  "Wertung: Ein Treffer von Team Rot gibt einen Punkt, ein Treffer von Team Neon gibt zwei Punkte. Danach spielt der Trainer den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, die anderen sichern hinter ihm ab", "Eng zusammenbleiben, damit keine Lücke entsteht", "Viel reden, damit die Kette zusammen schiebt", "Bei schlechtem Pass oder Ballkontakt sofort pressen"],
 "materials": ["5 Minitore", "Hütchen für Feld und Bahnen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Viererkette vor drei Minitoren. Vier gegen vier, und Team Neon verteidigt die Minitore eng zusammen als Kette.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 50.6)] + ERSATZ,
  "steps": [
   S("Ball zu Team Rot", "Der Trainer spielt den Ball zu Spieler neun. Spieler neun passt weiter nach links zu Spieler sieben.",
     ps("b1", [40.6, 38.6]), ps("b1", [29.6, 37.6], after=True)),
   S("Einer presst", "Spieler sieben dribbelt an. Spieler drei läuft raus und presst. Spieler fünf schaut zu ihm und sichert hinter ihm ab. Gleichzeitig schieben Spieler vier und Spieler zwei mit nach links.",
     dr("r7", "b1", [29.5, 32]), mv("n3", [30.5, 27], delay=0.2), bl("n5", [30.5, 31], after=True),
     mv("n5", [37, 24], after=True), mv("n4", [49, 23], delay=1.2), mv("n2", [61, 22], delay=1.2), mv("r9", [41, 30], delay=1.2)),
   S("Abgefangen", "Spieler sieben will zu Spieler neun passen. Spieler fünf hat gut abgesichert, geht dazwischen und fängt den Ball ab.",
     ps("b1", [38.1, 31.1]), mv("n5", [37.5, 30.5], delay=0.1)),
   S("Konter: Punkt", "Spieler fünf dribbelt schnell nach unten und schießt ins linke Minitor in der Ecke. Der Treffer zählt doppelt, und das gibt zwei Punkte für Team Neon. Dann spielt der Trainer den nächsten Ball zu Team Rot.",
     dr("n5", "b1", [34, 39]), ps("b1", [28.5, 42.7], after=True))],
  "dims": dims(25, 75, 9, 43, "41 m", "27 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Innenverteidiger rückt raus, die anderen schieben nach.", "Rausrücken und nachschieben",
    "Geht ein Innenverteidiger raus und presst, schieben die anderen drei gleichzeitig zu ihm. So bleibt die Kette eng, und es entsteht keine gefährliche Lücke. Der Angreifer muss nach außen spielen.",
    sp(), [B("b1", 60.6, 38.6)] + ERSATZ,
    [S("Spieler vier presst", "Spieler zehn dribbelt in die Mitte. Spieler vier rückt raus und presst. Gleichzeitig schieben Spieler fünf, Spieler drei und Spieler zwei zusammen und sichern ab.",
       dr("r10", "b1", [57, 32]), mv("n4", [57, 27], delay=0.2), mv("n5", [49, 21], delay=0.2), mv("n3", [39, 19], delay=0.2), mv("n2", [65, 21], delay=0.2)),
     S("Außen abgefangen", "Spieler zehn findet keine Lücke und passt nach außen zu Spieler elf. Spieler zwei hat mitgeschoben und fängt den Ball ab.",
       ps("b1", [66.6, 35.5]), mv("n2", [66, 34.9], delay=0.1))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell zurücklaufen.", "Schnell zurücklaufen",
    "Kommt der Gegner doch durch die Kette, gibt kein Verteidiger auf. Alle sprinten sofort zurück zum eigenen Minitor. Wer zuerst da ist, stellt sich in den Weg und blockt den Schuss.",
    sp(), [B("b1", 40.6, 38.6)] + ERSATZ,
    [S("Durch die Lücke", "Spieler neun spielt in die Lücke zwischen Spieler drei und Spieler fünf. Spieler sieben läuft hinter die Kette und nimmt den Ball mit.",
       ps("b1", [35.6, 17.6]), mv("r7", [36, 27]), mv("r7", [35, 17], after=True)),
     S("Zurück und blocken", "Spieler drei dreht sofort um und sprintet zurück vor das linke Minitor. Spieler sieben schießt, aber Spieler drei blockt den Schuss. Team Rot bekommt keinen Punkt, und Team Neon hat den Ball.",
       mv("n3", [31.5, 13]), dr("r7", "b1", [34, 15], delay=0.2), ps("b1", [32.1, 13.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
