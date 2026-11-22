import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 60-P3 (U12-U14, Woche 24 Phase 6): Defend the Gates. 20 x 40 Yards = Feld x 25-75, y 5-55 (18 x 37 m, in der Länge gestaucht),
# drei Zonen (gestrichelt bei y 23.8 und 36.2: 15, 10 und 15 Yards), oben ein Jugendtor mit Torwart. Am Ende der Mittelzone drei
# Hütchentore (im PDF rote und gelbe Hütchen, hier orange und neon für das mittlere Tor). Ausrichtung wie im PDF (Tor oben).
# Pink (Verteidiger) + grüner Torwart -> Team Neon (n1 TW, 3 in der Mittelzone, 4, 5, 6 in der ersten Zone), blau (Ballbesitz) ->
# Team Rot (7, 8, 9, 10), Springer F (team t) spielt für Rot. Nummern frei vergeben. Positionen in zwei Reihen (3D-Abstand).
# Ein Trainer statt zwei. Fassungen: Progression 1 (zweiter Verteidiger sprintet zurück, 2 gegen 2) und Progression 2 (Verteidiger
# darf in die letzte Zone zurück). Progression 3 aus dem Video (Minitore für Verteidiger) nicht übernommen.
# Sichtkegel: Text "Awareness to recover to defend the zones", Ton "identifying which player and gate their defensive teammate
# already has protected" (im Video kein Kegel eingezeichnet): bl() vom zurücksprintenden Neon vier zu Neon drei (Steigerung 1).
T = P("T", "c", 86, 47, "T")
F = P("f1", "t", 58, 54.5, "F")
POS = {"n1": (50, 8), "n3": (50, 26), "n5": (28, 39), "r7": (37, 39), "r8": (61, 39), "n4": (70, 39),
       "r9": (30, 54.5), "n6": (45, 54.5), "r10": (71, 54.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [F, T]
ERSATZ = [B("s1", 89.6, 50.5), B("s2", 86, 50.5)]
LINES = [rect(25, 5, 50, 50), line(25, 23.8, 75, 23.8), line(25, 36.2, 75, 36.2)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(27, 23.8), C(36, 23.8), C(46, 23.8, "neon"), C(54, 23.8, "neon"), C(64, 23.8), C(73, 23.8)]

u = {"title": "Die Hütchentore verteidigen", "code": "UE-198", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 12, "field_size": "18 x 37 m",
 "description": "Team Rot spielt mit einem Springer in der ersten Zone fünf gegen drei und braucht fünf Pässe. Dann dribbelt ein Spieler mit einem Mitspieler in die Mittelzone. Dort verteidigt ein einzelner Spieler von Team Neon gegen zwei und verhindert, dass sie durch eines der drei Hütchentore kommen. Erobert er den Ball, spielt er ihn zurück in die erste Zone.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 37 Metern in drei Zonen: unten die erste Zone, in der Mitte eine Mittelzone von 9 Metern, oben die letzte Zone mit einem Jugendtor. Am Ende der Mittelzone bilden Hütchen drei kleine Tore.",
  "Verteilen: In der ersten Zone vier von Team Rot, ein Springer und drei von Team Neon. Ein Verteidiger von Team Neon wartet in der Mittelzone, der Torwart von Team Neon steht im Tor. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Team Rot spielt mit dem Springer fünf gegen drei. Nach fünf Pässen dribbelt ein Spieler in die Mittelzone, ein Mitspieler läuft mit. Wer durch ein Hütchentor kommt, schießt allein auf den Torwart.",
  "Wertung und Wechsel: Ein Treffer gibt einen Punkt für Team Rot. Erobert Neon den Ball und spielt ihn zurück in die erste Zone, gibt das einen Punkt für Team Neon. Nach einigen Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell anlaufen und den Abstand verkürzen", "Seitlich stehen und den Angreifer weg von den Toren lenken", "Den Pass zum Mitspieler mit dem Körper zustellen", "Zurücksprinten und schauen, wen der Mitspieler schon deckt"],
 "materials": ["1 Jugendtor", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben", "1 Leibchen für den Springer"],
 "access": "abo", "hidden": True,
 "say_intro": "Die Hütchentore verteidigen. Ein Verteidiger allein gegen zwei Angreifer, die durch eines von drei Hütchentoren wollen.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 71.6, 55.1)] + ERSATZ,
  "steps": [
   S("Fünf Pässe", "Team Rot spielt mit dem Springer fünf gegen drei und zählt die Pässe. Rot zehn passt zum Springer, und der Springer spielt zu Rot acht. Neon vier läuft an.",
     ps("b1", [58.6, 55.1]), mv("n4", [66, 46], delay=0.3), ps("b1", [61.6, 39.6], after=True)),
   S("Ab in die Mittelzone", "Rot acht passt zu Rot sieben. Das ist der fünfte Pass. Rot sieben dribbelt in die Mittelzone, und Rot acht läuft mit.",
     ps("b1", [37.6, 39.6]), dr("r7", "b1", [38, 31], after=True), mv("r8", [60, 31], after=True)),
   S("Zwei gegen eins", "Neon drei läuft Rot sieben schnell an. Er stellt sich so, dass der Pass zu Rot acht zu ist, und lenkt Rot sieben nach außen.",
     mv("n3", [42, 26]), dr("r7", "b1", [33, 29], delay=0.3)),
   S("Ballgewinn: Punkt", "Neon drei geht dazwischen, erobert den Ball und passt zu Neon fünf in die erste Zone. Das gibt einen Punkt für Team Neon. Kommt Rot durch ein Hütchentor und trifft, gibt das einen Punkt für Team Rot. Danach beginnt Team Rot wieder in der ersten Zone.",
     mv("n3", [34.5, 26.5]), ps("b1", [28.6, 39.6], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "37 m", rx=79)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Verteidiger sprintet zurück.", "Zu zweit zurück",
    "Sobald Team Rot in die Mittelzone dribbelt, sprintet ein zweiter Verteidiger hinterher. Jetzt heißt es zwei gegen zwei. Der zweite Verteidiger schaut, wen sein Mitspieler schon deckt, und übernimmt den anderen Angreifer.",
    sp(), [B("b1", 37.6, 39.6)] + ERSATZ,
    [S("Hinterher sprinten", "Team Rot hat fünf Pässe geschafft. Rot sieben dribbelt in die Mittelzone, und Rot acht läuft mit. Gleichzeitig sprintet Neon vier hinterher.",
       dr("r7", "b1", [38, 31]), mv("r8", [61, 30]), mv("n4", [67, 33], delay=0.2)),
     S("Wer ist frei?", "Neon drei läuft Rot sieben an. Neon vier schaut, wen Neon drei schon deckt, und stellt sich zwischen Rot sieben und Rot acht.",
       mv("n3", [41, 25.5]), bl("n4", [44, 27]), mv("n4", [63, 25.5], after=True), mv("n4", [55, 28.5], after=True)),
     S("Abgefangen: Punkt", "Rot sieben passt zu Rot acht, aber Neon vier fängt den Ball ab. Er spielt zurück zu Neon sechs in die erste Zone, und das gibt einen Punkt für Team Neon.",
       ps("b1", [55.6, 29.1]), ps("b1", [45.6, 55.1], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Verteidiger darf in die letzte Zone zurück.", "Zurück vor das Tor",
    "Jetzt darf der Verteidiger aus der Mittelzone auch in die letzte Zone zurücklaufen. Kommt ein Angreifer durch ein Hütchentor, sprintet er zurück. Er drängt den Angreifer vom Tor weg und blockt den Schuss.",
    sp(), [B("b1", 37.6, 39.6)] + ERSATZ,
    [S("Durchs Hütchentor", "Rot sieben dribbelt in die Mittelzone und passt quer zu Rot acht. Rot acht dribbelt durch das rechte Hütchentor.",
       dr("r7", "b1", [38, 31]), mv("r8", [64, 31]), ps("b1", [64.6, 31.6], after=True), dr("r8", "b1", [68.5, 17], after=True)),
     S("Zurück vor das Tor", "Neon drei sprintet durch das mittlere Hütchentor zurück in die letzte Zone. Er drängt Rot acht vom Tor weg nach außen.",
       mv("n3", [51, 18]), mv("n3", [61, 13], after=True), dr("r8", "b1", [70, 12], delay=0.5)),
     S("Schuss geblockt: Punkt", "Rot acht schießt aus spitzem Winkel. Neon drei blockt den Schuss, erobert den Ball und spielt zu Neon sechs in die erste Zone. Das gibt einen Punkt für Team Neon.",
       ps("b1", [61.6, 13.6]), ps("b1", [45.6, 55.1], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
