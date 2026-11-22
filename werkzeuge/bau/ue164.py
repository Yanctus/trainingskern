import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 85-P6 (U12-U14, Woche 27 Phase 2): Penetrate the End Zone to Finish. 25 x 45 Yards = Feld x 36.1-63.9, y 5-55 (23 x 41 m),
# Endzonen je 5 Yards (gestrichelt bei y 10.6 und 49.4), in jeder Endzone zwei Minitore in den Ecken.
# Blau (im PDF dunkel, Ball) -> Neon 4, 6, 8, 9, 10; Pink -> Rot, Nummern neu (im PDF doppelt): pink 5 bleibt 5,
# pink 10 -> Rot 7, pink 8 -> Rot 3, pink 4 -> Rot 2, pink 9 -> Rot 11. Positionen in Reihen gesetzt (3D-Abstand).
# Ein Trainer statt zwei. In der Steigerung werden die Minitore im Original umgedreht, das ist hier weggelassen.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 71, 14, "T")
POS = {"r5": (38.5, 7), "n9": (47, 7), "r3": (39.5, 22.5), "r7": (49, 22.5), "n6": (58.5, 22.5),
       "n8": (41, 38.5), "r2": (50.5, 38.5), "n10": (60, 38.5), "n4": (45, 54), "r11": (55, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 74.6, 17.5), B("s2", 71, 17.5)]
LINES = [rect(36.1, 5, 27.8, 50), line(36.1, 10.6, 63.9, 10.6), line(36.1, 49.4, 63.9, 49.4)]
KEGEL = ecken(36.1, 5, 27.8, 50) + [C(36.1, 10.6), C(63.9, 10.6), C(36.1, 49.4), C(63.9, 49.4)]
TORE = [{"x": 40.5, "y": 5, "side": "top"}, {"x": 59.5, "y": 5, "side": "top"},
        {"x": 40.5, "y": 55, "side": "bottom"}, {"x": 59.5, "y": 55, "side": "bottom"}]

u = {"title": "Steilpass in die Endzone", "code": "UE-164", "kind": "Spielform",
 "focuses": ["Passspiel", "Torschuss", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "23 x 41 m",
 "description": "Drei gegen drei in der Mitte, und in jeder Endzone steht ein Spieler von jedem Team. Nach vier Pässen darf das Team am Ball steil in eine Endzone zum eigenen Spieler spielen. Der löst sich mit einer kurzen, schnellen Bewegung von seinem Gegenspieler und schießt auf eines der zwei Minitore. Erobert das andere Team den Ball, tauschen die Aufgaben: Jetzt sind seine Spieler in den Endzonen die Stürmer.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 41 Metern. An jedem Ende eine Endzone von 5 Metern mit zwei Minitoren in den Ecken.",
  "Verteilen: Drei gegen drei in der Mitte. In der oberen Endzone Spieler neun und Spieler fünf, in der unteren Spieler elf und Spieler vier. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Nach vier Pässen darf das Team am Ball steil in eine Endzone spielen. Der eigene Spieler dort ist Stürmer, der Gegenspieler verteidigt.",
  "Wertung und Wechsel: Jedes Minitor gibt einen Punkt. Nach jedem Punkt tauscht der Stürmer mit einem Mitspieler aus der Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Sich anbieten und gute Passwinkel schaffen", "Geduldig bleiben und auf die Lücke für den Steilpass warten", "Stürmer: kurz und schnell vom Gegenspieler lösen", "Scharf und genau in die Endzone passen"],
 "materials": ["4 Minitore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Steilpass in die Endzone. Erst vier Pässe in der Mitte, dann steil zum Stürmer, der sich von seinem Gegenspieler löst.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 60.6, 39.1)] + ERSATZ,
  "steps": [
   S("Vier Pässe", "Team Neon hat den Ball und braucht vier Pässe. Spieler zehn spielt zu Spieler sechs, und der spielt weiter zu Spieler acht.",
     ps("b1", [59.1, 23.1]), ps("b1", [41.6, 39.1], after=True)),
   S("Pass drei und vier", "Spieler sechs läuft sich in der Mitte frei. Spieler acht spielt ihn an, und Spieler sechs legt ab zu Spieler zehn. Das sind vier Pässe.",
     mv("n6", [55, 30]), ps("b1", [55.6, 30.6], delay=0.4), ps("b1", [60.6, 39.1], after=True)),
   S("Freilaufen", "Spieler neun geht kurz auf Spieler fünf zu und dreht dann blitzschnell nach rechts weg. Spieler zehn spielt sofort steil in die Endzone.",
     mv("n9", [44, 8.5]), mv("n9", [56, 8.5], after=True), mv("r5", [49, 9], after=True, delay=0.3),
     ps("b1", [56.6, 9.1], after=True)),
   S("Minitor: Punkt", "Spieler neun schießt mit dem ersten Kontakt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann tauscht Spieler neun mit einem Mitspieler aus der Mitte, und der Trainer bringt einen neuen Ball.",
     ps("b1", [59.5, 5.3]))],
  "dims": dims(36.1, 63.9, 5, 55, "23 m", "41 m", rx=82)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kurz und schnell vom Gegenspieler lösen.", "Kurz und schnell lösen",
    "Der Stürmer wartet nicht ruhig auf den Ball. Er geht erst kurz auf seinen Gegenspieler zu und dreht dann blitzschnell weg. So hat er einen Schritt Vorsprung und kann frei schießen.",
    sp(), [B("b1", 51.1, 39.1)] + ERSATZ,
    [S("Antäuschen", "Team Rot hat den Ball erobert und vier Pässe geschafft. Jetzt ist Spieler elf der Stürmer. Er geht kurz auf Spieler vier zu und dreht dann schnell nach rechts weg.",
       mv("r11", [51, 52.5]), mv("r11", [58, 51.5], after=True), mv("n4", [50, 53.5], after=True, delay=0.3)),
     S("Frei: Punkt", "Spieler zwei spielt sofort in den Lauf, und Spieler elf trifft mit dem ersten Kontakt ins rechte Minitor. Das gibt einen Punkt für Team Rot.",
       ps("b1", [58.6, 52.1]), ps("b1", [59.5, 54.7], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Stürmer legt ab, und ein Mitspieler schießt direkt.", "Ablegen und direkt schießen",
    "Nach dem Steilpass läuft ein Mitspieler aus der Mitte sofort nach. Der Stürmer legt den Ball mit dem ersten Kontakt für ihn ab, und er schießt direkt. Kommt keiner zur Hilfe, bekommt das andere Team den Ball.",
    sp(), [B("b1", 59.1, 23.1)] + ERSATZ,
    [S("Steilpass", "Team Neon hat vier Pässe geschafft. Spieler neun löst sich nach rechts, und Spieler sechs spielt steil in die Endzone.",
       mv("n9", [56, 8.5]), mv("r5", [49, 8], delay=0.3), ps("b1", [56.6, 9.1], delay=0.4)),
     S("Nachrücken", "Spieler sechs läuft sofort nach. Spieler neun legt den Ball mit dem ersten Kontakt für ihn ab.",
       mv("n6", [51, 14]), ps("b1", [51.6, 14.6], after=True)),
     S("Direkt: Punkt", "Spieler sechs schießt direkt ins linke Minitor, und das gibt einen Punkt für Team Neon. Kommt keiner zur Hilfe, bekommt Team Rot den Ball.",
       ps("b1", [40.5, 5.3]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
