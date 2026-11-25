import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 94-P8 (U15-U17, Woche 37 Phase 1): Playing Through the Thirds (Wave of Play, Possession). 20 x 30 Yards = 18 x 27 m
# (gerundet 18 x 25 m). Zonen laut PDF 7 / 5 / 8 / 5 / 7 Yards (ergibt 32, nicht 30 Yards; darum im Text nur die Streifen
# mit knapp fünf Metern, die Zonen anteilig auf das Feld verteilt); die beiden 5-Yard-Streifen (4,6 m) sind die Zonen der Verteidiger.
# LANGES FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51), die
# Dreiergruppen spielen von links nach rechts (im PDF von oben nach unten). Koordinaten direkt quer gesetzt (2,67 Einheiten je
# Yard in der Länge): Verteidigerzonen x 27.7-41 und x 62.3-75.7 als orange Zonen (Team Rot), keine Tore.
# Ballbesitz (PDF/Video rot) -> Team Neon in drei Dreiergruppen: Gruppe am Ball 2, 3, 4 (Video), Zielgruppe am anderen Ende
# 6, 8, 10 (Video), wartende Gruppe hinter der Startlinie 7, 9, 11 (Video). Verteidiger (Video orange 8, 6, 5, 4) -> Team Rot,
# neu nummeriert, weil die Nummern doppelt sind: 8 -> 12, 6 -> 13, 5 -> 5, 4 -> 14. Ein Trainer statt zwei, unten an der Seitenlinie.
# Grundform nach PDF und Video 0:00-0:16: Die Dreiergruppe lässt den Ball laufen, das erste Paar verschiebt, einer dribbelt durch
# die Lücke in die Mitte, die anderen kommen nach, dann der Pass durch das zweite Paar auf die Gruppe am anderen Ende (Punkt).
# Im Video wird die Gruppe am Ziel gleich zur neuen Angriffsgruppe in die andere Richtung, die Angreifer bleiben dort stehen.
# Fassungen: PDF Progression 1 (Pass in den freien Raum, Lauf mit Timing; im Video zusätzlich "allow dropping into half space")
# und Progression 2 (Zielgruppe steht verteilt auf zweiter und dritter Linie).
# Sichtkegel: Text "Awareness of spaces to drive through / play penetrating passes", "Awareness of teammates positions"; im Video
# nicht eingezeichnet. Richtung aus dem Sinn: Spieler drei schaut vor dem Pass zu Spieler vier an der Lücke und vor dem Pass
# durch das zweite Paar auf die Zielgruppe; in Fassung 2 nimmt Spieler sechs an und dreht auf (bl mit von + drehen, Vorbild ue300).
# Kein Dublette: UE-310 (Aufbauwelle drei gegen drei, eine Kette aus drei Verteidigern, Passgeber verteidigen danach) und
# UE-121 (24-P5, zwei gegen eins durch drei Zonen auf Tor) haben andere Organisation und Abläufe.
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n2": (14, 10), "n3": (23, 27.5), "n4": (14, 45),
       "n7": (3.5, 10), "n9": (3.5, 27.5), "n11": (3.5, 45),
       "r12": (34.5, 16), "r13": (34.5, 39), "r5": (69, 16), "r14": (69, 39),
       "n8": (86, 10), "n6": (86, 27.5), "n10": (86, 45)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, d=None): x, y = (d or POS)[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
ZONEN = [{"type": "zone", "x": 27.7, "y": 4, "w": 13.3, "h": 47, "color": "orange"}, {"type": "zone", "x": 62.3, "y": 4, "w": 13.4, "h": 47, "color": "orange"}]
LINES = [rect(9, 4, 80, 47)] + ZONEN
CONES = [C(9, 4), C(89, 4), C(9, 51), C(89, 51)]
DIMS = dims(9, 89, 4, 51, "25 m", "18 m", rx=96)

u = {"title": "Zu dritt durch zwei Abwehrpaare", "code": "UE-404", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Dribbling"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "18 x 25 m",
 "description": "Drei Angreifer spielen sich durch zwei Paare von Verteidigern. Jedes Paar steht in einem schmalen Streifen quer über das Feld. Mit schnellen Pässen ziehen die drei das erste Paar auseinander, dribbeln durch die Lücke in die Mitte und spielen dann durch das zweite Paar auf die Gruppe am anderen Ende. Die startet sofort in die andere Richtung.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern. Zwei Streifen von knapp fünf Metern liegen quer über das Feld. Dazwischen liegt die Mitte, an beiden Enden bleibt je eine Endzone.",
  "Verteilen: Team Neon in drei Gruppen zu dritt. Eine Gruppe hat den Ball an einem Ende, eine steht am anderen Ende, die dritte wartet hinter der Startlinie. Je zwei Verteidiger von Team Rot stehen in einem Streifen. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Die drei am Ball kombinieren schnell, bis eine Lücke im ersten Paar aufgeht. Durch die Lücke dribbelt einer in die Mitte, die anderen kommen nach. Dann geht der Ball durch das zweite Paar zur Gruppe am anderen Ende.",
  "Wertung und Wechsel: Kommt der Ball bei der Gruppe am anderen Ende an, gibt das einen Punkt für Team Neon. Die Gruppe spielt sofort in die andere Richtung, die Angreifer bleiben dort stehen. Erobert Team Rot den Ball und dribbelt über eine Endlinie, gibt das einen Punkt für Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell passen, bis das Paar verschiebt", "Lücke gesehen? Mit Ball rein", "Tempo hoch halten, auch beim zweiten Paar", "Kopf hoch, wo stehen die anderen?"],
 "materials": ["4 Hütchen", "Markierungen für zwei Streifen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zu dritt durch zwei Abwehrpaare. Drei Angreifer spielen sich mit schnellen Pässen durch zwei Paare von Verteidigern bis zur Gruppe am anderen Ende. Dann geht es sofort in die andere Richtung.",
 "board": {"lines": LINES, "cones": CONES, "goals": [], "players": sp(), "balls": [B("b1", *fuss("n3"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Ball laufen lassen", "Spieler drei hat den Ball und spielt zu Spieler zwei. Das erste Paar schiebt mit zum Ball. Sofort geht der Ball zurück zu Spieler drei.",
     ps("b1", fuss("n2")), mv("r12", [33.5, 12], delay=0.3), mv("r13", [34.5, 31], delay=0.3), ps("b1", fuss("n3"), after=True)),
   S("Lücke sehen, Pass rüber", "Jetzt ist auf der anderen Seite die Lücke. Spieler drei sieht sie und schaut zu Spieler vier, dann spielt er direkt zu ihm.",
     bl("n3", [14, 45]), ps("b1", fuss("n4"), after=True)),
   S("Rein in die Mitte", "Spieler vier dribbelt durch die Lücke in die Mitte. Spieler drei und Spieler zwei laufen sofort nach.",
     dr("n4", "b1", [31, 46.5]), dr("n4", "b1", [50, 44], after=True),
     mv("n3", [36, 23], delay=0.4), mv("n3", [52, 25.5], after=True), mv("n2", [26, 21], delay=0.6), mv("n2", [49, 10], after=True)),
   S("Das zweite Paar ziehen", "Spieler vierzehn kommt raus auf Spieler vier. Der legt quer zu Spieler drei. Spieler fünf schiebt mit, aber zu spät.",
     mv("r14", [67, 42]), ps("b1", fuss("n3", {"n3": (52, 25.5)}), delay=0.3), mv("r5", [67, 20], delay=0.6)),
   S("Durch das Paar: Punkt", "Spieler drei hebt den Kopf, sieht Spieler sechs und spielt flach zwischen den beiden durch. Das gibt einen Punkt für Team Neon. Jetzt spielen Spieler sechs, acht und zehn in die andere Richtung, und Spieler zwei, drei und vier bleiben drüben stehen.",
     bl("n3", [72, 27.5]), ps("b1", fuss("n6"), after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Ball darf in den freien Raum gespielt werden.", "Pass in den freien Raum",
    "Der Pass muss nicht mehr in den Fuß kommen. Einer startet durch die Lücke, und der Ball kommt in den Raum davor. Der Lauf beginnt erst, wenn der Passgeber den Kopf hebt. Auch die Spieler am anderen Ende dürfen sich in ihre Zone fallen lassen und anbieten.",
    sp(), [B("b1", *fuss("n3"))] + ERSATZ,
    [S("Starten, Ball in den Raum", "Spieler zwei startet durch die Lücke zwischen den beiden Verteidigern. Spieler drei spielt den Ball in den Raum vor ihm, nicht in den Fuß.",
       mv("n2", [30, 27]), mv("n2", [48, 26], after=True), ps("b1", [48.6, 26.6], delay=0.6)),
     S("Fallen lassen und anspielen", "Spieler acht lässt sich in seine Zone fallen und bietet sich an. Spieler zwei spielt ihn durch das zweite Paar an. Das gibt einen Punkt für Team Neon.",
       mv("n8", [80, 21]), bl("n2", [68, 24], delay=0.3), ps("b1", [80.6, 21.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Zielgruppe steht verteilt auf drei Linien.", "Zielgruppe auf drei Linien",
    "Die Gruppe am anderen Ende steht jetzt nicht mehr nebeneinander. Einer steht in der Mitte zwischen den Paaren, einer in der Endzone, einer an der Endlinie. So gibt es mehr Anspielstationen, und der Ball kommt schneller durch.",
    sp(n6=(52, 27.5), n8=(82, 20)), [B("b1", *fuss("n3"))] + ERSATZ,
    [S("Anspiel zwischen die Paare", "Spieler sechs steht in der Mitte und schaut zum Ball. Spieler drei spielt flach durch das erste Paar zu ihm.",
       bl("n6", [33, 27.5]), ps("b1", fuss("n6", {"n6": (52, 27.5)}), after=True)),
     S("Aufdrehen, weiter durch: Punkt", "Spieler sechs nimmt an und dreht auf. Er spielt sofort durch das zweite Paar zu Spieler acht in der Endzone. Das gibt einen Punkt für Team Neon.",
       bl("n6", [72, 23.5], von=[33, 27.5], dauer=1.3), drehen("n6", [72, 23.5], delay=0.4), ps("b1", fuss("n8", {"n8": (82, 20)}), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
