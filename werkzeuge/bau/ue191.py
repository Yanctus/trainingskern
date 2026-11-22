import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 37-P6 (U12-U14, Woche 22 Phase 5): Defending and Countering from Deep SSG. 25 x 35 Yards = Feld x 32-68, y 5-55 (23 x 32 m),
# Mittellinie gestrichelt, an beiden Enden ein Jugendtor mit Torwart. Gedreht (180 Grad): Pink (im PDF greift es nach unten an)
# -> Team Neon greift nach oben an (4, 5, 6, 7, 11); dunkel -> Team Rot verteidigt oben (2, 3, 8, 9, 10). Die beiden Torhüter
# (im PDF grün 1 und 13) als neutrale Torhüter k1 oben, k2 unten (zwei Team-Torhüter gäben doppelte Nummer "TW"). Nummern wie im PDF. Positionen auf ein Spaltenraster gesetzt (3D-Abstand), Spielidee wie im PDF
# (Pass, Kombinieren, alle in der Angriffshälfte, Abschluss). Ein Trainer statt zwei.
# Sichtkegel: Text "vision" (Coaching-Punkt eins) und "Awareness when to step up" -> im Coaching-Punkt eins schaut Rot zwei nach
# dem Abfangen in den freien Raum hinter Team Neon, bevor er steil spielt (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 76, 30, "T")
POS = {"k1": (50, 7.5), "r3": (33.5, 13), "r2": (66.5, 13), "n11": (41.7, 20), "n7": (58.3, 20), "r8": (66.5, 29),
       "r10": (41.7, 36), "n4": (50, 36), "r9": (58.3, 36), "n6": (33.5, 45), "n5": (66.5, 45), "k2": (50, 52.5)}
HOCH = {"k1": (50, 7.5), "r3": (33.5, 10), "r2": (66.5, 10), "n11": (41.7, 17), "n7": (58.3, 17), "n6": (33.5, 26),
        "n4": (50, 27), "n5": (66.5, 26), "r10": (41.7, 33), "r9": (58.3, 33), "r8": (33.5, 42), "k2": (50, 52.5)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 79.6, 33.5), B("s2", 76, 33.5)]
LINES = [rect(32, 5, 36, 50), line(32, 30, 68, 30)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Kontern aus der Tiefe", "code": "UE-191", "kind": "Spielform",
 "focuses": ["Umschalten", "Verteidigen", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 32 m",
 "description": "Fünf gegen fünf mit zwei Torhütern, das Feld ist in zwei Hälften geteilt. Ein Team darf erst schießen, wenn alle fünf Spieler in der gegnerischen Hälfte sind. Erobern die Verteidiger den Ball, kontern sie schnell in den freien Raum, und auch dann muss das ganze Team mit nach vorn. Wer den Ball verliert, läuft sofort gemeinsam zurück.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern mit einer Mittellinie. An beiden Enden steht ein Jugendtor.",
  "Verteilen: Zwei Teams zu fünft, dazu ein Torwart in jedem Tor. Team Neon greift nach oben an, Team Rot nach unten. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Freies Spiel fünf gegen fünf. Geschossen wird erst, wenn alle fünf Spieler des Teams in der gegnerischen Hälfte sind. Nach einem Ballgewinn sofort kontern.",
  "Wertung: Jeder Treffer gibt einen Punkt. Trifft ein Team, bevor alle fünf in der gegnerischen Hälfte sind, zählt es nicht, und der Trainer spielt den Ball dem anderen Team zum Konter."],
 "organisation_show": ORG,
 "coaching_points": ["Als Team nach vorn spielen, bis alle in der gegnerischen Hälfte sind", "Nach dem Ballgewinn sofort steil in den freien Raum spielen", "Nach dem Ballverlust sofort gemeinsam zurücklaufen", "Viel reden, damit die Abstände in der Abwehr stimmen"],
 "materials": ["2 Jugendtore", "Hütchen für Feld und Mittellinie", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Kontern aus der Tiefe. Fünf gegen fünf, und geschossen wird erst, wenn das ganze Team in der gegnerischen Hälfte ist.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 67.1, 45.6)] + ERSATZ,
  "steps": [
   S("Pass", "Team Neon greift nach oben an. Neon fünf passt zu Neon vier, und der spielt steil zu Neon sieben.",
     ps("b1", [50.6, 36.6]), ps("b1", [58.9, 20.6], after=True)),
   S("Alle in die obere Hälfte", "Erst wenn alle fünf in der oberen Hälfte sind, darf Team Neon schießen. Darum laufen Neon vier, fünf und sechs gleichzeitig nach vorn.",
     mv("n4", [50, 26]), mv("n5", [62, 27]), mv("n6", [37, 27])),
   S("Kombinieren", "Neon elf startet in die Lücke, und Neon sieben spielt ihm den Ball quer in den Lauf.",
     mv("n11", [43, 13]), ps("b1", [43.6, 13.6], delay=0.3)),
   S("Abschluss: Punkt", "Neon elf schießt flach ins kurze Eck, und das gibt einen Punkt für Team Neon. Danach spielt der obere Torwart zu Team Rot, und Team Rot greift nach unten an.",
     ps("b1", [46.6, 4.8]))],
  "dims": dims(32, 68, 5, 55, "23 m", "32 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Ballgewinn sofort nach vorn.", "Schneller Konter",
    "Team Neon greift mit allen fünf Spielern oben an. Hinter ihnen ist viel Platz. Erobert Team Rot den Ball, hebt der Spieler sofort den Kopf und spielt steil in diesen freien Raum. Alle anderen laufen mit, denn auch beim Konter muss das ganze Team in der gegnerischen Hälfte sein.",
    sp(HOCH), [B("b1", 58.9, 17.6)] + ERSATZ,
    [S("Abgefangen", "Team Neon greift oben an. Neon sieben passt zu Neon fünf, aber Rot zwei geht dazwischen und fängt den Ball ab.",
       mv("r2", [62.6, 21.6]), ps("b1", [63.2, 22.2], delay=0.3)),
     S("Kopf hoch", "Rot zwei hebt sofort den Kopf und sieht den freien Raum hinter Team Neon. Rot neun läuft schon los.",
       bl("r2", [60, 40]), mv("r9", [60, 44], after=True)),
     S("Steil und alle mit", "Rot zwei spielt sofort steil zu Rot neun. Gleichzeitig laufen Rot zwei und Rot drei in die untere Hälfte, denn das ganze Team muss mit.",
       ps("b1", [60.6, 44.6]), mv("r2", [64, 34], delay=0.2), mv("r3", [38, 22], delay=0.2), mv("r3", [38, 34], after=True)),
     S("Konter: Punkt", "Rot neun schießt ins kurze Eck, und das gibt einen Punkt für Team Rot.",
       ps("b1", [53.5, 55.2]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Nach dem Ballverlust sofort zurück.", "Schnell zurück",
    "Verliert ein Team den Ball, laufen alle sofort gemeinsam zurück hinter den Ball. Dabei bleiben sie eng zusammen und reden miteinander. So findet der Gegner keine Lücke für den Konter.",
    sp(HOCH), [B("b1", 42.3, 33.6)] + ERSATZ,
    [S("Ball verloren", "Team Neon hat den Ball an Rot zehn verloren. Sofort rufen alle: Zurück! Alle fünf sprinten gleichzeitig hinter den Ball.",
       mv("n4", [50, 42]), mv("n11", [46, 30]), mv("n11", [45.5, 44], after=True), mv("n6", [38, 47]),
       mv("n7", [54, 30]), mv("n7", [55, 42], after=True), mv("n5", [62, 44]), dr("r10", "b1", [42, 38], delay=0.4)),
     S("Konter gestoppt", "Team Neon steht wieder eng vor dem eigenen Tor. Rot zehn findet keine Lücke, und Neon elf erobert den Ball zurück.",
       mv("n11", [42.6, 40.5]), dr("n11", "b1", [46, 35], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
