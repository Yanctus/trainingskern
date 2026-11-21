import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 62-P2: 20 x 15 Yards, gedreht (PDF oben -> rechts): x 22-78, y 9-51. Gold -> Neon, Blau -> Rot. Abschlusszone links (5 Yards) vor dem linken Minitor.
T = P("T", "c", 42.5, 4.5, "T"); cb = [B("c1", 46, 5), B("c2", 39, 5)]
D = P("d", "t", 51.5, 30, "D")
zone = {"type": "zone", "x": 22, "y": 9, "w": 13.2, "h": 42, "color": "orange"}
lines = [rect(22, 9, 56, 42), zone, line(35.2, 9, 35.2, 51)]
goals = [{"x": 78, "y": 18, "side": "right"}, {"x": 22, "y": 42, "side": "left"}]
cones = ecken(22, 9, 56, 42) + [C(22, 30), C(78, 30)]
warte = [P("n6", "a", 17.5, 54.5, "6"), P("n7", "a", 9, 54.5, "7"), P("r10", "b", 89, 33, "10"), P("r11", "b", 89, 48.6, "11")]
u = {"title": "Abschluss, dann zurück", "code": "UE-070", "kind": "Spielform",
 "focuses": ["Torschuss", "Umschalten", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 12, "field_size": "18 x 14 m",
 "description": "In der Mitte eines Feldes von 18 mal 14 Metern steht ein Spieler von Team Neon an einem Dummy, an den beiden Enden steht je ein Minitor. Ein Mitspieler spielt ihn an, er löst sich vom Dummy, nimmt den Ball mit und schließt ins rechte Minitor ab, das gibt einen Punkt. Der Pass ist zugleich das Signal für einen Angreifer von Team Rot, der von der anderen Seite aufs linke Minitor losdribbelt. Der Spieler von Team Neon sprintet sofort zurück und verteidigt im 1 gegen 1, denn Team Rot darf erst in der Abschlusszone schießen.",
 "organisation": ["Aufbauen: Feld von 18 mal 14 Metern, ein Dummy in der Mitte, ein Minitor rechts und eines links. Vor dem linken Tor liegt eine Abschlusszone von viereinhalb Metern.",
  "Aufstellen: Team Neon wartet unten links mit Bällen, ein Spieler steht am Dummy. Team Rot wartet rechts mit Bällen. Ich stehe mit Ersatzbällen an der Seite.",
  "Ablauf: Pass auf den Spieler am Dummy, Abschluss ins rechte Tor, dann sofort zurücksprinten und gegen den Angreifer von Team Rot verteidigen.",
  "Regeln: Team Rot darf nur aus der Abschlusszone schießen. Jedes Tor gibt einen Punkt. Nach drei Angriffen tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Sich vom Dummy lösen und offen zum Tor annehmen", "Den Ball mit dem ersten Kontakt vorlegen und flach ins Eck schießen", "Nach dem Abschluss sofort zurücksprinten", "Auch unter Druck ruhig abschließen"],
 "materials": ["2 Minitore", "1 Dummy", "6 orange Hütchen", "Bälle bei beiden Gruppen", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Abschluss, dann zurück. Hier schließt ein Spieler ab und muss danach sofort zurück, um einen Konter zu verteidigen.",
 "board": {"lines": lines, "goals": goals, "cones": cones,
  "players": [D, P("n4", "a", 43, 30, "4"), P("n8", "a", 26, 54, "8"), P("r9", "b", 80.5, 39, "9"), *warte, T],
  "balls": [B("b1", 27.6, 53.4), B("b2", 79.6, 41), *cb],
  "steps": [
   S("Lösen und Pass auf die Vier", "Spieler vier löst sich vom Dummy, und Spieler acht spielt ihn an.", mv("n4", [43, 23.5]), ps("b1", [44.6, 23.4], delay=0.2)),
   S("Der Pass ist das Signal", "Der Pass ist das Signal für Spieler neun: Er dribbelt von rechts los, während Spieler vier den Ball nach vorn mitnimmt.",
     dr("n4", "b1", [56, 21]), dr("r9", "b2", [66, 40.5], delay=0.1)),
   S("Abschluss ins Minitor: Punkt", "Spieler vier schießt flach ins rechte Minitor, und das gibt einen Punkt für Team Neon.", ps("b1", [80, 18]), dr("r9", "b2", [56, 42])),
   S("Sofort zurücksprinten", "Sofort sprintet Spieler vier zurück, um Spieler neun vor der Zone zu stoppen.", mv("n4", [39, 37]), dr("r9", "b2", [46, 43.5], delay=0.1)),
   S("1 gegen 1 vor der Zone", "Spieler vier ist rechtzeitig zurück und stellt sich vor die Zone, jetzt heißt es eins gegen eins.",
     mv("n4", [37.5, 43]), dr("r9", "b2", [43, 44.5], delay=0.1))],
  "dims": [{"x1": 22, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "18 m"}, {"x1": 96, "y1": 9, "x2": 96, "y2": 51, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt entscheidet, wie schnell es weitergeht.", "Der erste Kontakt zählt",
    "Wer den Ball mit dem ersten Kontakt ungeschickt nach vorn an den Dummy legt, braucht lange zum Drehen. Dann kommt er spät zum Abschluss, hat weniger Zeit zum Zurücklaufen, und der Angreifer von Team Rot läuft ungestört aufs Tor.",
    [D, P("n4", "a", 43, 25, "4"), P("n8", "a", 26, 54, "8"), P("r9", "b", 73.5, 38.5, "9"), *warte, T], [B("b1", 44.4, 25.6), B("b2", 72, 39.5), *cb],
    [S("Erster Kontakt zu weit nach vorn", "Spieler vier legt sich den Ball zu weit nach vorn an den Dummy, und Spieler neun startet schon.",
       dr("n4", "b1", [46, 26]), dr("r9", "b2", [60, 39.5], delay=0.1)),
     S("Das Drehen dauert", "Spieler vier braucht lange zum Drehen, Spieler neun ist schon fast an der Zone.",
       dr("n4", "b1", [46.5, 19.5]), dr("n4", "b1", [58, 18], after=True), dr("r9", "b2", [41, 41])),
     S("Freie Bahn: Punkt für Rot", "Spieler neun dribbelt ungestört in die Zone und trifft, und das gibt einen Punkt für Team Rot.",
       dr("r9", "b2", [31, 42]), ps("b2", [20.5, 42], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Im eins gegen eins mit einer schnellen Bewegung am Verteidiger vorbei.", "Schnell vorbei im 1 gegen 1",
    "Ist der Verteidiger zurück, braucht der Angreifer seine Technik. Mit einer schnellen Täuschung und einem Antritt schafft er sich Platz, dribbelt in die Zone und schließt ruhig ab.",
    [D, P("n4", "a", 35, 37.5, "4"), P("n8", "a", 26, 54, "8"), P("r9", "b", 43.5, 46, "9"), *warte, T], [B("b1", 27.6, 53.4), B("b2", 42, 46.6), *cb],
    [S("Täuschung nach oben", "Spieler neun täuscht einen Haken nach oben an, und Spieler vier geht mit.", dr("r9", "b2", [41, 40]), mv("n4", [36, 37], delay=0.2)),
     S("Antritt nach unten", "Dann zieht er blitzschnell nach unten vorbei in die Zone.", dr("r9", "b2", [36.5, 45]), dr("r9", "b2", [31, 46], after=True)),
     S("In der Zone abschließen: Punkt", "Er schließt ruhig ins Minitor ab, und das gibt einen Punkt für Team Rot.", ps("b2", [20.5, 42.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
