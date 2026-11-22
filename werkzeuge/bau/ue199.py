import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 13-P6 (U12-U14, Woche 24 Phase 6): Defending Outnumbered (Skill Game). 40 x 35 Yards = Feld x 20-80, y 5-55 (37 x 32 m) vor dem
# Strafraum, oben ein Jugendtor mit neutralem Torwart und Torraum. Gedreht (180 Grad): im PDF liegt das Tor unten.
# Zwei Seitenkanäle (gestrichelt bei x 32.3 und 67.7), am Tor je eine Seitenzone (Neon, wie die grauen Flächen im PDF).
# Strafraumlinie gestrichelt bei y 18.7 mit vier Hütchen (im PDF rot): links und rechts je ein Hütchentor. Halbkreis weggelassen.
# Blau (Verteidiger) -> Team Neon (4, 5, 6 im Feld, 2 und 3 in den Seitenzonen), pink (Angreifer) -> Team Rot (9, 10 und
# Pink 4 -> Rot 8, neu nummeriert wegen Neon 4), zwei Springer F (team t), grüner Torwart neutral (spielt für beide Teams).
# Ein Trainer statt zwei, rechts neben dem Feld. Positionen leicht verschoben (3D-Abstand), Wertung für Neon ergänzt (Ballgewinn und
# Pass zum Springer = Punkt). Coaching-Punkt 1 und 2 wie im PDF (Umschalten mit Flanke, Torwart hält = Rollenwechsel, fünf Pässe).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 91, 45, "T")
K = P("k", "t", 50, 8, "TW")
FS = [P("f1", "t", 65, 40, "F"), P("f2", "t", 36, 40, "F")]
POS = {"n2": (25, 12), "n3": (74, 12), "n5": (33.5, 24), "r9": (43, 24), "r10": (51.5, 24), "n6": (60, 24),
       "n4": (47, 40), "r8": (55.5, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [K] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + FS + [T]
ERSATZ = [B("s1", 94.6, 48.5), B("s2", 91, 48.5)]
LINES = [rect(20, 5, 60, 50), {"type": "zone", "x": 20, "y": 5, "w": 12.3, "h": 13.7}, {"type": "zone", "x": 67.7, "y": 5, "w": 12.3, "h": 13.7},
         line(32.3, 5, 32.3, 55), line(67.7, 5, 67.7, 55), line(32.3, 18.7, 67.7, 18.7), rect(40.5, 5, 17.5, 6)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(33, 18.7), C(40.5, 18.7), C(58, 18.7), C(66.5, 18.7)]

u = {"title": "Vor dem Strafraum verteidigen", "code": "UE-199", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 11, "players_max": 13, "field_size": "37 x 32 m",
 "description": "Vor dem Strafraum spielt Team Rot mit zwei Springern fünf gegen drei. Spielt es einen Pass durch ein Hütchentor, laufen zwei Angreifer in den Strafraum. Dort sprinten zwei Verteidiger aus den Seitenzonen zurück, und es heißt zwei gegen zwei. Erobert Team Neon den Ball, spielt es zum Springer und greift selbst an.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 32 Metern vor einem Jugendtor, mit zwei Seitenkanälen und je einer Seitenzone am Tor. Auf der Strafraumlinie bilden vier Hütchen links und rechts ein Hütchentor.",
  "Verteilen: Vor dem Strafraum drei von Team Rot, zwei Springer und drei von Team Neon. Zwei weitere von Team Neon warten in den Seitenzonen, ein neutraler Torwart steht im Tor. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Der Trainer passt zu einem Springer, und Team Rot spielt fünf gegen drei. Nach einem Pass durch ein Hütchentor laufen zwei Angreifer in den Strafraum. Die zwei aus den Seitenzonen sprinten zurück und verteidigen.",
  "Wertung und Wechsel: Ein Treffer gibt einen Punkt für Team Rot. Erobert Team Neon den Ball und spielt ihn zum Springer, gibt das einen Punkt für Team Neon, und Team Neon greift an. Hält der Torwart, wechseln die Rollen ebenso."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell zurücksprinten und das Tor schützen", "Eng stehen und den Angreifern wenig Platz lassen", "Pässe durch die Mitte und nach vorn zustellen", "Nach dem Ballgewinn schnell umschalten und angreifen"],
 "materials": ["1 Jugendtor", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben", "2 Leibchen für die Springer"],
 "access": "abo", "hidden": True,
 "say_intro": "Vor dem Strafraum verteidigen. Drei Verteidiger gegen fünf, und zwei weitere sprinten aus den Seitenzonen zurück.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 91.6, 45.6)] + ERSATZ,
  "steps": [
   S("Fünf gegen drei", "Der Trainer passt zum rechten Springer. Team Rot spielt mit den zwei Springern fünf gegen drei. Der Springer passt zu Rot acht, und Rot acht spielt zum linken Springer.",
     ps("b1", [65.6, 40.6]), ps("b1", [56.1, 49.6], after=True), ps("b1", [36.6, 40.6], after=True)),
   S("Durch das Hütchentor", "Der linke Springer spielt durch das linke Hütchentor. Rot neun startet in den Strafraum und nimmt den Ball an. Rot zehn läuft mit.",
     mv("r9", [38.5, 21]), mv("r9", [37, 12], after=True), ps("b1", [37.6, 12.6], delay=0.6), mv("r10", [53, 12.5], delay=0.3)),
   S("Zurücksprinten", "Gleichzeitig sprinten Neon zwei und Neon drei aus ihren Seitenzonen zurück. Jetzt heißt es zwei gegen zwei im Strafraum.",
     mv("n2", [31, 10.5]), mv("n3", [60, 10.5])),
   S("Ballgewinn: Punkt", "Neon zwei geht entschlossen auf Rot neun und erobert den Ball. Er passt zurück zum linken Springer, und das gibt einen Punkt für Team Neon. Ein Treffer gäbe einen Punkt für Team Rot. Danach spielt der Trainer den nächsten Ball.",
     mv("n2", [36, 11.5]), ps("b1", [36.6, 40.6], after=True))],
  "dims": dims(20, 80, 5, 55, "37 m", "32 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Ballgewinn schnell umschalten.", "Ball erobert, umschalten",
    "Fängt Team Neon den Ball ab, spielt es zurück zum Springer. Jetzt greift Team Neon an. Der Springer spielt den Ball schnell auf die Seite, von dort kommt die Flanke in den Strafraum.",
    sp(), [B("b1", 56.1, 49.6)] + ERSATZ,
    [S("Abgefangen", "Rot acht will in die Mitte passen, aber Neon vier fängt den Ball ab. Er spielt sofort zum rechten Springer.",
       mv("n4", [49, 37.5]), ps("b1", [49.6, 38.1], delay=0.2), ps("b1", [65.6, 40.6], after=True)),
     S("Auf die Seite", "Jetzt greift Team Neon an. Der Springer spielt den Ball weit auf die Seite zu Neon drei. Neon sechs läuft in den Strafraum.",
       ps("b1", [74.6, 12.6]), mv("n6", [61.5, 13], delay=0.3)),
     S("Flanke: Punkt", "Neon drei flankt in den Strafraum, und Neon sechs schießt ins Tor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [62.1, 13.6]), ps("b1", [55.5, 5.3], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Fünf Pässe zuerst, und hält der Torwart, wechseln die Rollen.", "Torwart hält, Wechsel",
    "Team Rot muss erst fünf Pässe schaffen, bevor es durch ein Hütchentor spielen darf. So haben die Verteidiger Zeit, sich zu ordnen. Hält der Torwart den Schuss, spielt er zu Team Neon, und die Rollen wechseln.",
    sp(), [B("b1", 65.6, 40.6)] + ERSATZ,
    [S("Fünf Pässe", "Team Rot zählt die Pässe. Der rechte Springer passt zu Rot acht, Rot acht zum linken Springer. Neon vier, fünf und sechs schieben eng zusammen.",
       ps("b1", [56.1, 49.6]), ps("b1", [36.6, 40.6], after=True), mv("n6", [56, 26], delay=0.3), mv("n4", [43, 36], delay=0.3)),
     S("Durch das Hütchentor", "Nach dem fünften Pass spielt der linke Springer durch das Hütchentor. Rot neun nimmt den Ball an und schießt sofort.",
       mv("r9", [38.5, 21]), mv("r9", [37, 12], after=True), ps("b1", [37.6, 12.6], delay=0.6)),
     S("Torwart hält: Wechsel", "Der Torwart fängt den Ball. Er wirft ihn zu Neon vier, und jetzt greift Team Neon an. Team Rot muss verteidigen.",
       mv("k", [43, 8]), ps("b1", [43.6, 8.6], delay=0.2), ps("b1", [43.6, 36.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
