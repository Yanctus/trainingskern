import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 28-P5 (U12-U14, Woche 7 Phase 1): How to Break the First Line of Pressure (Goalkeeper Playing Out Skill). 40 x 40 Yards =
# Feld x 25-75, y 5-55 (37 m). Gedreht: Spiel von unten nach oben, Jugendtor mit Torwart unten, drei Minitore oben.
# Pink -> Neon (TW, 6, 4, 5), Dunkel -> Rot (9, 8, 10), Positionen leicht verschoben (3D-Abstand). Ein Trainer statt zwei.
# Mittelkreis weggelassen, Mittellinie gestrichelt. Was Rot nach Ballgewinn macht, steht nicht im Original: Neustart beim Torwart.
# Sichtkegel aus Ton und Video ("Encourage GK to be calm - look to beat the first line", "180 degree visibility when receiving",
# "Draw pressure - vision"): Torwart schaut vor dem Anspiel zu Neon 4, Neon 4 schaut über die Schulter zu Rot 8 im Rücken.
T = P("T", "c", 17, 45, "T")
POS = {"n1": (50, 51), "n6": (30, 37), "n4": (50, 31), "n5": (70, 37), "r9": (39, 27), "r8": (50, 14), "r10": (61, 28)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 18.6, 48.5), B("s2", 15, 48.5)]
LINES = [rect(25, 5, 50, 50), line(25, 39, 75, 39), rect(42, 49, 16, 6)]
TORE = [{"x": 50, "y": 55, "side": "bottom", "size": "jugend"},
        {"x": 32, "y": 5, "side": "top"}, {"x": 50, "y": 5, "side": "top"}, {"x": 68.5, "y": 5, "side": "top"}]

u = {"title": "Die erste Pressinglinie knacken", "code": "UE-147", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 10, "field_size": "37 x 37 m",
 "description": "Spielaufbau gegen Pressing, drei gegen drei plus Torwart. Der Torwart spielt zwei Verteidiger und einen Sechser an, drei Gegenspieler pressen. Das Team will die erste Pressinglinie überspielen und in eines der drei Minitore treffen. Am besten durch die Mitte und mit direkten Pässen, nicht außen herum. Der Torwart bleibt ruhig am Ball und sucht den Pass durch die Linie.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 37 Metern, gestrichelte Mittellinie. Unten ein Jugendtor mit Torwart, oben drei Minitore.",
  "Verteilen: Team Neon mit Torwart, zwei Verteidigern und einem Sechser. Team Rot mit zwei Stürmern und einem Zehner, die pressen. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Torwart eröffnet. Team Neon spielt sich unter Druck durch die erste Linie und schießt in ein Minitor. Team Rot presst und will den Ball erobern.",
  "Wertung: Jedes Tor in ein Minitor ist ein Punkt. Erobert Team Rot den Ball oder geht er ins Aus, beginnt der Torwart mit einem neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Der Torwart bleibt ruhig am Ball und sucht den Pass durch die erste Linie", "Die Spieler in der Mitte spielen sich mit direkten Pässen frei", "Lieber durch die Mitte als außen herum", "Vor der Annahme über die Schulter schauen, um alles zu sehen"],
 "materials": ["1 Jugendtor", "3 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Die erste Pressinglinie knacken. Drei gegen drei plus Torwart, und Team Neon spielt sich durch das Pressing bis zu den Minitoren.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 51.6)] + ERSATZ,
  "steps": [
   S("Ruhig eröffnen", "Der Torwart bleibt ruhig, hebt den Kopf und sieht Spieler vier frei in der Mitte. Er spielt ihn an, und Spieler acht presst sofort von hinten.",
     bl("n1", [50, 31]), ps("b1", [50.6, 31.6], after=True), mv("r8", [51, 21], after=True)),
   S("Direkt in den Lauf", "Spieler fünf startet hinter Spieler zehn nach vorn. Spieler vier spielt ihm den Ball direkt in den Lauf, ohne ihn erst anzunehmen.",
     mv("n5", [66, 18]), ps("b1", [66.6, 18.6], delay=0.3)),
   S("Abschluss: Punkt", "Spieler fünf schießt ins mittlere Minitor, und das gibt einen Punkt für Team Neon. Dann beginnt der Torwart mit einem neuen Ball.",
     ps("b1", [50, 5.3]))],
  "dims": dims(25, 75, 5, 55, "37 m", "37 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Über die Schulter schauen.", "Rundumblick",
    "Der Sechser bekommt den Ball oft mit dem Rücken zum Spiel. Bevor der Ball kommt, schaut er über die Schulter. Kommt der Gegner von hinten, spielt er direkt weiter. Ist er weit weg, kann er aufdrehen.",
    sp(), [B("b1", 50.6, 51.6)] + ERSATZ,
    [S("Schulterblick", "Bevor der Ball kommt, schaut Spieler vier über die Schulter. Er sieht: Spieler acht kommt von hinten auf ihn zu.",
       bl("n4", [50, 14]), mv("r8", [50, 24], after=True)),
     S("Direkt weiter: Punkt", "Der Torwart spielt Spieler vier an. Der spielt direkt weiter in den Lauf von Spieler sechs, und Spieler sechs trifft ins linke Minitor. Das gibt einen Punkt für Team Neon.",
       mv("n6", [33, 18]), ps("b1", [50.6, 31.6]), ps("b1", [33.6, 18.6], after=True), ps("b1", [32, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Den Druck anlocken.", "Druck anlocken",
    "Die beiden Verteidiger kommen tief zum Torwart und locken die Stürmer heraus. Laufen die Stürmer mit, wird es in der Mitte frei. Dann spielt der Torwart flach durch die Linie.",
    sp(), [B("b1", 50.6, 51.6)] + ERSATZ,
    [S("Locken", "Spieler sechs und Spieler fünf kommen tief zum Torwart. Spieler neun und Spieler zehn laufen mit und pressen.",
       mv("n6", [32, 47]), mv("n5", [68, 47]), mv("r9", [35, 40], delay=0.3), mv("r10", [65, 40], delay=0.3)),
     S("Durch die Linie: Punkt", "Jetzt ist die Mitte frei. Der Torwart sieht Spieler vier und spielt flach durch die Linie. Spieler vier dreht auf und trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
       bl("n1", [50, 31]), ps("b1", [50.6, 31.6], after=True), dr("n4", "b1", [57, 21], after=True), ps("b1", [68.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
