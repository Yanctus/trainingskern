import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 9v9-P5: 30 x 20 Yards, gedreht (Tor unten -> links, Minitore oben -> rechts): x 14-86, y 6-54. Blau (mit Torwart) -> Neon, Pink -> Rot.
T = P("T", "c", 7, 52, "T"); cb = [B("c1", 8.5, 48.5), B("c2", 5, 48.5)]
lines = [rect(14, 6, 72, 48), line(50.3, 6, 50.3, 54), line(14, 21.9, 86, 21.9), line(14, 30.4, 86, 30.4), line(14, 39, 86, 39)]
goals = [{"x": 14, "y": 30.4, "side": "left"}, {"x": 86, "y": 11.9, "side": "right"}, {"x": 86, "y": 46.1, "side": "right"}]
GK = lambda x, y: P("tw", "a", x, y, "1")
u = {"title": "Steil auf den Stürmer", "code": "UE-071", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 9, "field_size": "27 x 18 m",
 "description": "Team Neon spielt mit Torwart, einem Sechser als Libero, zwei Innenverteidigern und einem Stürmer gegen drei Angreifer von Team Rot. Neon spielt flache Steilpässe auf den Stürmer, der den Ball mit höchstens zwei Kontakten für einen nachrückenden Verteidiger ablegt, und der schließt in eines der beiden Minitore ab, das gibt einen Punkt. Die Verteidiger bleiben in ihren Längszonen, nur der Sechser darf zwischen zwei Zonen pendeln. Team Rot presst mit einem, zwei oder drei Spielern und hat nach einer Balleroberung fünf Sekunden für einen Treffer aufs große Tor.",
 "organisation": ["Feld abstecken: 27 mal 18 Meter, in der Mitte geteilt. Drei gestrichelte Linien teilen das Feld der Länge nach in vier Zonen.",
  "Tore stellen: Links steht das große Tor mit Torwart von Team Neon, rechts zwei Minitore.",
  "Aufstellung: Team Neon mit Torwart, drei Verteidigern und einem Stürmer, die Verteidiger bleiben in ihren Zonen. Drei Spieler von Team Rot pressen. Ich stehe mit Bällen an der Seite.",
  "Wertung: Steilpass auf den Stürmer, Ablage für einen nachrückenden Verteidiger, Abschluss ins Minitor: Punkt. Erobert Team Rot den Ball, hat es fünf Sekunden für ein Tor."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und schnell passen, damit der Gegner verschieben muss", "Die Lücke für den Steilpass auf den Stürmer erkennen", "Den Steilpass scharf spielen", "Nur ein Verteidiger rückt nach und unterstützt den Stürmer, alle anderen halten ihre Zone"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Zonen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Steil auf den Stürmer. Hier spielt die Abwehr flache Steilpässe auf den Stürmer, und ein Verteidiger rückt zum Abschluss nach.",
 "board": {"lines": lines, "goals": goals, "cones": ecken(14, 6, 72, 48),
  "players": [GK(16.8, 33.6), P("n5", "a", 37.2, 9, "5"), P("n4", "a", 26.9, 28.2, "4"), P("n6", "a", 33.9, 51.4, "6"), P("n9", "a", 75.2, 28.8, "9"),
              P("r8", "b", 54.5, 13.7, "8"), P("r10", "b", 54.5, 46.1, "10"), P("r11", "b", 44.1, 29.4, "11"), T],
  "balls": [B("b1", 18.4, 34.2), *cb],
  "steps": [
   S("Torwart auf den Verteidiger", "Der Torwart spielt den Ball auf Spieler sechs.", ps("b1", [32.3, 50.6])),
   S("Quer auf die Vier", "Spieler sechs spielt quer auf Spieler vier, und Spieler elf läuft an.", ps("b1", [28.4, 29.8]), mv("r11", [37.5, 24.5], delay=0.2)),
   S("Steilpass auf den Stürmer", "Spieler neun kommt entgegen, und Spieler vier spielt ihn flach und scharf an.", mv("n9", [70.5, 35.5]), ps("b1", [69, 36.2], delay=0.2)),
   S("Ein Verteidiger rückt nach", "Spieler sechs rückt außen nach, als einziger Verteidiger, und Spieler zehn kommt zu spät.", mv("n6", [74, 50]), mv("r10", [62, 44], delay=0.3)),
   S("Ablage und Abschluss: Punkt", "Spieler neun legt für Spieler sechs ab, und der trifft ins Minitor, das gibt einen Punkt für Team Neon.",
     ps("b1", [72.6, 49.6]), ps("b1", [88, 46.1], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 93, "y1": 6, "x2": 93, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Direkt auf den Stürmer und direkt abgeschlossen, das gibt drei Punkte.", "Zweimal direkt: drei Punkte",
    "Spielt der Verteidiger den Ball mit einem Kontakt in den Stürmer und schließt die Ablage danach ebenfalls mit einem Kontakt ab, bekommt das Team drei Punkte. Das belohnt schnelles Spiel nach vorn und gutes Nachrücken.",
    [GK(19, 31), P("n5", "a", 37.5, 9.6, "5"), P("n4", "a", 28.5, 24, "4"), P("n6", "a", 33.2, 48.2, "6"), P("n9", "a", 60.7, 30.3, "9"),
     P("r8", "b", 54.7, 13.6, "8"), P("r10", "b", 46, 47, "10"), P("r11", "b", 37.5, 32.5, "11"), T],
    [B("b1", 20.6, 31.6), *cb],
    [S("Torwart auf den Verteidiger", "Der Torwart spielt auf Spieler sechs.", ps("b1", [34.6, 48])),
     S("Direkt in den Stürmer", "Spieler sechs spielt den Ball mit einem Kontakt in den Stürmer und rückt sofort nach.",
       ps("b1", [59.3, 31]), mv("n6", [48, 53], delay=0.15), mv("n6", [75, 49], after=True)),
     S("Ablage, direkt abgeschlossen: drei Punkte", "Spieler neun legt ab, Spieler sechs schließt direkt ab, und das gibt drei Punkte für Team Neon.",
       ps("b1", [73.6, 48.5]), ps("b1", [88, 46.1], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Torwart spielt den Steilpass direkt auf den Stürmer.", "Torwart direkt auf den Stürmer",
    "Nach einem Rückpass spielt der Torwart den Ball selbst flach und scharf direkt auf den Stürmer. Der legt für einen nachrückenden Mitspieler ab, und der schließt ins Minitor ab. Vorher schauen alle, wo die Gegner stehen.",
    [GK(16, 26), P("n5", "a", 35, 8, "5"), P("n4", "a", 25, 40, "4"), P("n6", "a", 34, 53.5, "6"), P("n9", "a", 60.9, 30.3, "9"),
     P("r8", "b", 43.5, 14, "8"), P("r11", "b", 31, 24, "11"), P("r10", "b", 42.5, 44, "10"), T],
    [B("b1", 36.6, 8.6), *cb],
    [S("Rückpass zum Torwart", "Spieler fünf spielt den Ball zurück zum Torwart.", ps("b1", [17.6, 26.4])),
     S("Torwart flach auf den Stürmer", "Der Torwart spielt den Ball flach und scharf direkt auf den Stürmer.", ps("b1", [59.4, 30.6])),
     S("Der Verteidiger rückt nach", "Spieler sechs rückt außen nach.", mv("n6", [68, 47.5])),
     S("Ablage und Abschluss: Punkt", "Spieler neun legt für Spieler sechs ab, und der trifft ins Minitor, das gibt einen Punkt für Team Neon.",
       ps("b1", [67.6, 46.6]), ps("b1", [88, 46.1], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
