import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P19: 25 x 20 Yards, gedreht (Tor oben -> rechts): x 22-78, y 7.5-52.5. Blau (greift oben an) -> Neon nach rechts, Pink -> Rot. Je ein Torwart.
T = P("T", "c", 19, 3.5, "T"); cb = [B("c1", 22.5, 4.2), B("c2", 15.5, 4.2)]
GK1 = P("tw1", "b", 75.4, 30.4, "1"); GK13 = P("tw13", "a", 24.4, 30, "13")
goals = [{"x": 78, "y": 30, "side": "right"}, {"x": 22, "y": 30, "side": "left"}]
u = {"title": "Nur nach vorn 4 gegen 4", "code": "UE-069", "kind": "Spielform",
 "focuses": ["Dribbling", "1 gegen 1", "Passspiel"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 10, "players_max": 10, "field_size": "23 x 18 m",
 "description": "Zwei Teams mit je vier Spielern und einem Torwart spielen auf einem Feld von 23 mal 18 Metern auf zwei Tore. Erlaubt sind Pässe nach vorn. Geht ein Pass zur Seite oder nach hinten, muss der Spieler, der ihn bekommt, nach vorn dribbeln und einen Gegner ausspielen, wenn einer im Weg steht. Jedes Tor gibt einen Punkt, und wer nach der Spielzeit die meisten Punkte hat, gewinnt.",
 "organisation": ["Feld abstecken: 23 mal 18 Meter mit vier orangen Hütchen, an beiden Enden steht ein Tor mit Torwart.",
  "Teams einteilen: Je vier Feldspieler pro Team, Team Neon greift nach rechts an, Team Rot nach links. Ich stehe mit Bällen an der Ecke.",
  "Regel: Pässe nach vorn sind frei. Nach einem Pass zur Seite oder nach hinten muss der Empfänger nach vorn dribbeln und einen Gegner ausspielen.",
  "Wertung: Jedes Tor gibt einen Punkt. Bei jüngeren Kindern erinnere ich laut an die Regel, wenn ein Ball nach hinten geht."],
 "organisation_show": ORG,
 "coaching_points": ["Mutig und selbstbewusst am Ball sein", "Sich so bewegen, dass Pässe nach vorn möglich sind", "Laut miteinander sprechen", "Den Ball eng am Fuß führen, aufs Tor zielen und nachsetzen"],
 "materials": ["2 Tore", "4 orange Hütchen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Nur nach vorn, vier gegen vier. Hier spielen die Kinder nach vorn, und nach jedem Pass zur Seite heißt es: losdribbeln und den Gegner ausspielen.",
 "board": {"lines": [rect(22, 7.5, 56, 45)], "cones": ecken(22, 7.5, 56, 45), "goals": goals,
  "players": [GK1, GK13, P("n4", "a", 32, 47, "4"), P("n5", "a", 34, 16, "5"), P("n8", "a", 49.5, 31, "8"), P("n9", "a", 62, 23, "9"),
              P("r10", "b", 41, 48, "10"), P("r6", "b", 58, 42, "6"), P("r3", "b", 70.5, 14, "3"), P("r2", "b", 70.5, 46.5, "2"), T],
  "balls": [B("b1", 33.6, 46.2), *cb],
  "steps": [
   S("Pass zur Seite", "Spieler vier spielt quer zu Spieler fünf.", ps("b1", [34.6, 17.6])),
   S("Jetzt nach vorn dribbeln", "Nach dem Querpass gilt die Regel: Spieler fünf dribbelt mutig nach vorn.", dr("n5", "b1", [46, 18])),
   S("Steilpass nach vorn", "Dann spielt er den Ball nach vorn auf Spieler neun.", ps("b1", [60.6, 23.4]), mv("r3", [67, 18.5], delay=0.3)),
   S("Abschluss: Punkt", "Spieler neun schießt aufs Tor, und das gibt einen Punkt für Team Neon.", ps("b1", [80, 27.5]), mv("tw1", [75.4, 32], delay=0.15))],
  "dims": [{"x1": 22, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "23 m"}, {"x1": 86, "y1": 7.5, "x2": 86, "y2": 52.5, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach einem Rückpass sofort nach vorn dribbeln und den Gegner ausspielen.", "Rückpass: los nach vorn",
    "Kommt der Ball nach hinten oder zur Seite, erkennt der Empfänger das sofort. Er dribbelt mutig nach vorn, spielt seinen Gegenspieler aus und sucht danach den nächsten Weg zum Tor. So bleibt der Angriff im Schwung.",
    [GK1, GK13, P("n4", "a", 52.5, 48, "4"), P("n8", "a", 44, 32, "8"), P("n9", "a", 66, 36, "9"), P("n5", "a", 57, 12, "5"),
     P("r6", "b", 53, 30, "6"), P("r3", "b", 66.5, 14, "3"), P("r2", "b", 66, 52, "2"), P("r10", "b", 35, 47, "10"), T],
    [B("b1", 54.1, 47.2), *cb],
    [S("Rückpass", "Spieler vier spielt den Ball nach hinten zu Spieler acht.", ps("b1", [45.5, 32.8])),
     S("Losdribbeln und ausspielen", "Spieler acht dribbelt sofort nach vorn und spielt Spieler sechs mit einem Haken aus.",
       dr("n8", "b1", [50, 25]), dr("n8", "b1", [59, 25], after=True), mv("r6", [54, 27.5], delay=0.3)),
     S("Abschluss: Punkt", "Dann schießt er aufs Tor, und das gibt einen Punkt für Team Neon.", ps("b1", [80, 28]), mv("tw1", [75.4, 28.5], delay=0.1))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Immer nach Pässen nach vorn suchen, und die Mitspieler laufen sich frei.", "Freilaufen für den Pass nach vorn",
    "Der Spieler am Ball schaut zuerst nach vorn. Damit ein Pass nach vorn möglich ist, laufen sich die Mitspieler in die Lücken zwischen den Gegnern frei. So öffnen sich Passwege, und das Team kommt schnell zum Tor.",
    [GK1, GK13, P("n4", "a", 37, 20, "4"), P("n9", "a", 54, 42, "9"), P("n5", "a", 30, 47, "5"), P("n8", "a", 40, 49, "8"),
     P("r10", "b", 45.5, 15, "10"), P("r6", "b", 45.5, 33, "6"), P("r3", "b", 62, 20, "3"), P("r2", "b", 63, 50, "2"), T],
    [B("b1", 38.6, 20.6), *cb],
    [S("In die Lücke laufen", "Spieler neun läuft sich in die Lücke zwischen zwei Gegnern frei.", mv("n9", [62, 31])),
     S("Pass nach vorn", "Spieler vier sieht ihn und spielt den Ball nach vorn in den Lauf.", ps("b1", [60.6, 30.5])),
     S("Abschluss: Punkt", "Spieler neun schließt ab, und das gibt einen Punkt für Team Neon.", ps("b1", [80, 32]), mv("tw1", [75.4, 28.5], delay=0.1))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
