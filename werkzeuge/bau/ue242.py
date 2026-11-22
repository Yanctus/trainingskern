import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P7 (U12-U14, Woche 40 Phase 5): Defend as a Compact Back 4. 15 x 20 Yards (15 in Spielrichtung) = Feld x 25-75, y 10.5-49.5
# (18 x 14 m), an beiden Enden ein Springer. Um 90 Grad gedreht: im PDF wird von links nach rechts gespielt, hier von unten nach
# oben (Springer unten und oben statt links und rechts). Dunkel (Viererkette) -> Team Neon (2, 5, 4, 3 von links, Nummern wie im
# PDF), Pink (Angreifer) -> Team Rot, neu nummeriert (im PDF doppelt mit Dunkel): 3 -> 8, 5 -> 10, 4 -> 9, 2 -> 7. Springer (gelb, F)
# neutral. Ein Trainer unten rechts mit Bällen wie im PDF. Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video.
# Steigerung 2 (Springer im Feld): Wie Team Rot dann punktet, sagen PDF und Ton nicht; hier: über die obere Linie dribbeln
# (Annahme). Der zweite Springer steht dafür am oberen Rand im Feld.
# Sichtkegel: Text "Anticipate passes - Read the play", Ton "Players must recognize pressing triggers such as a bad touch or
# misplaced pass" -> Grundform: Spieler fünf schaut zum Ballführer, bevor er presst; Steigerung 1: Spieler vier sieht die
# schlechte Ballannahme (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 82, 52, "T")
POS = {"n2": (34, 26), "n5": (44, 25), "n4": (56, 25), "n3": (66, 26),
       "r8": (30, 43), "r10": (40, 42), "r9": (60, 42), "r7": (70, 43),
       "f1": (50, 52.5), "f2": (50, 7.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 85.6, 55.5), B("s2", 82, 55.5)]
LINES = [rect(25, 10.5, 50, 39)]
MINI = [{"x": 30, "y": 10.5, "side": "top"}, {"x": 70, "y": 10.5, "side": "top"},
        {"x": 30, "y": 49.5, "side": "bottom"}, {"x": 70, "y": 49.5, "side": "bottom"}]

u = {"title": "Viererkette zwischen Springern", "code": "UE-242", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 14 m",
 "description": "Vier gegen vier in einem kleinen Feld, an beiden Enden steht ein Springer. Das Team am Ball will durch die Viererkette der anderen hindurch zum Springer auf der anderen Seite spielen. Die Kette bleibt eng zusammen: Einer presst, die anderen schieben mit und sichern ab. Wer den Ball erobert, greift sofort in die andere Richtung an.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern. Oben und unten an der Linie steht je ein Springer.",
  "Verteilen: Team Neon verteidigt mit vier Spielern als Kette in der Mitte. Team Rot greift mit vier Spielern an. Der Trainer steht unten rechts mit Bällen.",
  "Ablauf: Der Springer unten spielt den Ball zu Team Rot. Team Rot will durch die Kette zum Springer oben spielen. Team Neon presst, drängt nach außen und schiebt als Kette mit.",
  "Wertung und Wechsel: Kommt der Ball zum Springer oben, gibt das einen Punkt für Team Rot. Erobert Team Neon den Ball, gibt das einen Punkt für Team Neon. Danach greift das andere Team in die andere Richtung an."],
 "organisation_show": ORG,
 "coaching_points": ["Eng zusammenbleiben, damit keine Lücke entsteht", "Einer presst, die anderen sichern ab", "Den Gegner nach außen drängen", "Bei schlechter Ballannahme sofort pressen"],
 "materials": ["Hütchen für das Feld", "Viele Bälle", "Leibchen in drei Farben", "4 Minitore für die Steigerung"],
 "access": "abo", "hidden": True,
 "say_intro": "Viererkette zwischen Springern. Vier gegen vier, und die Kette hält eng zusammen, damit niemand durchspielt.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": [B("b1", 50.6, 53.1)] + ERSATZ,
  "steps": [
   S("Ball vom Springer", "Der Springer unten spielt den Ball zu Spieler zehn. Team Rot will durch die Kette zum Springer oben spielen.",
     ps("b1", [40.6, 42.6])),
   S("Einer presst", "Spieler fünf sieht, dass Spieler zehn den Ball hat. Er rückt raus und presst. Gleichzeitig schieben Spieler zwei, Spieler vier und Spieler drei eng zu ihm und sichern ab.",
     bl("n5", [40.5, 40]), mv("n5", [41, 34], after=True),
     mv("n2", [33, 25], delay=1.0), mv("n4", [50.5, 24], delay=1.0), mv("n3", [60, 25.5], delay=1.0)),
   S("Nach außen", "Spieler zehn findet keine Lücke und passt nach außen zu Spieler acht. Spieler zwei rückt raus und presst. Spieler fünf läuft zurück in die Kette.",
     ps("b1", [30.6, 43.6]), mv("n2", [31, 36], delay=0.3), mv("n5", [42, 26], delay=0.3)),
   S("Abgefangen: Punkt", "Spieler acht will flach durch die Kette spielen. Spieler fünf ahnt den Pass und fängt ihn ab, und das gibt einen Punkt für Team Neon. Jetzt greift Team Neon nach unten an, und Team Rot verteidigt als Kette.",
     ps("b1", [42.6, 26.6]))],
  "dims": dims(25, 75, 10.5, 49.5, "18 m", "14 m", rx=92)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: In allen vier Ecken steht ein Minitor.", "Minitore für die Kette",
    "In den vier Ecken steht je ein Minitor. Erobert die Kette den Ball, kontert sie sofort und schießt in ein Minitor auf der Seite, von der die Angreifer kommen. Ein schlechter Pass oder eine schlechte Ballannahme ist das Zeichen zum Pressen.",
    sp(), [B("b1", 50.6, 53.1)] + ERSATZ,
    [S("Schlecht angenommen", "Der Springer unten passt zu Spieler neun. Spieler neun nimmt den Ball schlecht an, er springt weg. Spieler vier sieht das und presst sofort.",
       ps("b1", [60.6, 42.6]), ps("b1", [62.6, 36.6], after=True), bl("n4", [61.5, 38], after=True), mv("n4", [62, 36], after=True),
       mv("n5", [51, 25], delay=1.6), mv("n3", [69, 27], delay=1.6)),
     S("Konter: Punkt", "Spieler vier hat den Ball. Er dribbelt sofort nach unten und schießt ins rechte Minitor unten, und das gibt einen Punkt für Team Neon.",
       dr("n4", "b1", [65.5, 44]), ps("b1", [70, 49.2], after=True))],
    goals=MINI),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Springer spielen im Feld mit.", "Springer im Feld",
    "Die beiden Springer kommen ins Feld und spielen mit Team Rot, also sechs gegen vier. Team Rot punktet, wenn ein Spieler mit dem Ball über die obere Linie dribbelt. Die Kette muss noch enger stehen, den Ball vor sich halten und verzögern.",
    sp(f1=(50, 46), f2=(50, 9.4)), [B("b1", 30.6, 43.6)] + ERSATZ,
    [S("Sechs gegen vier", "Spieler acht passt zum Springer in der Mitte. Gleichzeitig schiebt die Kette eng zusammen und bleibt vor dem Ball.",
       ps("b1", [50.6, 46.6]), mv("n2", [38, 26], delay=0.2), mv("n3", [62, 26], delay=0.2)),
     S("Verzögern", "Der Springer dribbelt an. Spieler fünf presst ihn und verzögert, Spieler vier sichert schräg dahinter ab.",
       dr("f1", "b1", [50, 38]), mv("n5", [48, 31.5], delay=0.3), mv("n4", [55, 27], delay=0.3)),
     S("Abgefangen", "Der Springer will zu Spieler neun passen. Spieler vier ahnt den Pass und fängt ihn ab. Jetzt hat Team Neon den Ball.",
       mv("n4", [57, 34.5]), ps("b1", [57.6, 35.1], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
