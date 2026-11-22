import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 69-P6 (U12-U14, Woche 26 Phase 4): Midfield Compactness to Win Possession. 20 x 25 Yards = Feld x 30.4-69.6, y 5-55
# (18 x 23 m), oben und unten je zwei Minitore. Pink (2-4: Mittelfeldkette 7, 8, 4, 11 und Abwehr 5, 6) -> Team Neon, Nummern
# wie im PDF; dunkel (3-1-2) -> Team Rot, neu nummeriert (im PDF doppelt mit Pink): 4 -> 9, 8 -> 12, 5 -> 15, 6 -> 14,
# 3 und 10 bleiben. Ausrichtung wie im PDF: Team Rot greift nach oben an. Ein Trainer statt zwei (im PDF je einer oben links und
# unten rechts). Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video; die Grundform zeigt einen Ballgewinn der
# Kette mit Konter (zwei Punkte), die Fassungen die beiden Coaching-Punkte aus PDF und Video.
# Sichtkegel: Ton "The midfield unit must recognise poor touches or misplaced passes as triggers to apply a high press" -> im
# ersten Coaching-Punkt bl() von Spieler elf zu Spieler fünfzehn vor der verunglückten Annahme (im Video presst Pink 11 gegen Blau 5;
# kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 77, 44, "T")
POS = {"n5": (33, 8), "n6": (66, 8), "n7": (32, 32), "n8": (41, 30), "n4": (58, 30), "n11": (67, 32),
       "r10": (42, 14), "r12": (57, 14), "r9": (49.5, 38), "r3": (33, 48), "r14": (49.5, 54), "r15": (66, 48)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 80.6, 47.5), B("s2", 77, 47.5)]
LINES = [rect(30.4, 5, 39.2, 50)]
TORE = [{"x": 39, "y": 5, "side": "top"}, {"x": 61, "y": 5, "side": "top"}, {"x": 39, "y": 55, "side": "bottom"}, {"x": 61, "y": 55, "side": "bottom"}]

u = {"title": "Die Kette erobert den Ball", "code": "UE-204", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "18 x 23 m",
 "description": "Sechs gegen sechs mit zwei Minitoren an jedem Ende. Team Rot hat immer zuerst den Ball und will durch die Viererkette von Team Neon nach oben spielen. Die Kette bleibt eng zusammen, presst bei einer schlechten Ballannahme sofort und kontert nach dem Ballgewinn. Ein Treffer der Kette gibt zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern. Oben und unten stehen je zwei Minitore. Der Trainer steht an der Seite mit Bällen.",
  "Verteilen: Team Neon spielt mit einer Viererkette im Mittelfeld und zwei Abwehrspielern vor den oberen Toren. Team Rot spielt mit drei hinten, einem in der Mitte und zwei vorn.",
  "Ablauf: Team Rot startet immer mit dem Ball und greift die oberen Tore an. Team Neon verteidigt und kontert nach einem Ballgewinn auf die unteren Tore.",
  "Wertung: Ein Treffer von Team Rot gibt einen Punkt. Erobert die Kette den Ball und trifft, gibt das zwei Punkte für Team Neon, sonst einen Punkt. Danach startet Team Rot mit einem neuen Ball vom Trainer."],
 "organisation_show": ORG,
 "coaching_points": ["Eng bleiben: gemeinsam pressen und absichern", "Geduldig bleiben, die Ordnung halten und auf den Fehlpass warten", "Bei einer schlechten Ballannahme sofort pressen", "Nach dem Ballgewinn schnell kontern und mitlaufen"],
 "materials": ["4 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Die Kette erobert den Ball. Team Rot will durch das Mittelfeld, und die Viererkette von Team Neon bleibt eng zusammen und schlägt im richtigen Moment zu.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(30.4, 5, 39.2, 50), "players": sp(), "balls": [B("b1", 50.1, 54.6)] + ERSATZ,
  "steps": [
   S("Rot baut auf", "Team Rot hat immer zuerst den Ball und will nach oben. Spieler vierzehn passt zu Spieler fünfzehn. Gleichzeitig schiebt die ganze Kette von Team Neon zum Ball.",
     ps("b1", [66.6, 48.6]), mv("n11", [64, 33], delay=0.3), mv("n4", [56, 31], delay=0.3), mv("n8", [45, 31], delay=0.3), mv("n7", [36, 32], delay=0.3)),
   S("Abgefangen", "Spieler fünfzehn will zu Spieler zwölf durchspielen. Spieler elf steht nah dran, geht dazwischen und fängt den Ball ab.",
     mv("n11", [63.2, 37.3]), ps("b1", [63.8, 37.9], delay=0.2)),
   S("Konter: zwei Punkte", "Spieler elf passt sofort zu Spieler vier. Spieler vier dribbelt nach unten und trifft ins rechte Minitor. Die Kette hat den Ball erobert, und das gibt zwei Punkte für Team Neon. Dann startet Team Rot mit einem neuen Ball vom Trainer.",
     ps("b1", [56.6, 31.6]), dr("n4", "b1", [57, 46], after=True), ps("b1", [61, 54.7], after=True))],
  "dims": dims(30.4, 69.6, 5, 55, "18 m", "23 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Bei einer schlechten Ballannahme sofort pressen.", "Das Zeichen zum Pressen",
    "Springt dem Gegner der Ball vom Fuß, ist das das Zeichen. Der nächste Spieler der Kette presst sofort, die anderen schieben eng nach. So erobert Team Neon den Ball und kann schnell kontern.",
    sp(), [B("b1", 50.1, 54.6)] + ERSATZ,
    [S("Genau hinschauen", "Spieler vierzehn passt zu Spieler fünfzehn. Spieler elf schaut genau hin: Kann Spieler fünfzehn den Ball gut annehmen?",
       ps("b1", [66.6, 48.6]), bl("n11", [66, 48])),
     S("Sofort pressen", "Der Ball springt Spieler fünfzehn vom Fuß. Spieler elf presst sofort. Gleichzeitig schieben Spieler vier und Spieler acht nach.",
       ps("b1", [63.6, 42.6]), mv("n11", [63, 42], delay=0.2), mv("n4", [57, 34], delay=0.2), mv("n8", [47, 32], delay=0.2)),
     S("Erobert: zwei Punkte", "Spieler elf erobert den Ball, dribbelt los und trifft ins rechte Minitor. Das gibt zwei Punkte für Team Neon.",
       dr("n11", "b1", [61, 49]), ps("b1", [61, 54.7], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Einer presst, die anderen schieben zusammen.", "Einer presst, alle schieben",
    "Läuft ein Spieler der Kette den Ball an, schieben die anderen drei sofort eng zu ihm. So entstehen keine Lücken, und der Gegner kommt nicht durch die Mitte.",
    sp(), [B("b1", 50.1, 38.6)] + ERSATZ,
    [S("Zusammenschieben", "Spieler neun hat den Ball. Spieler vier presst ihn. Gleichzeitig schieben Spieler acht, Spieler sieben und Spieler elf eng zusammen.",
       mv("n4", [53, 33.5]), mv("n8", [44, 30.5]), mv("n7", [36, 30.5]), mv("n11", [62, 31])),
     S("Kein Weg durch", "Spieler neun findet keine Lücke und spielt zurück zu Spieler vierzehn. Team Rot muss neu aufbauen.",
       ps("b1", [50.1, 54.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
