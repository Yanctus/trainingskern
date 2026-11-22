import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 10-P4 (U12-U14, Woche 32 Phase 4): Defensive Pressure Technical / How to develop Angles of Approach. Dreieck 20 x 15 Yards:
# Ecken (25,50), (75,50) und Spitze (50,6), Feld 18 x 14 m. Im Original alle Spieler pink: Station oben -> Team Rot (7 verteidigt,
# 6 wartet), Stationen unten -> Team Neon (links 9 und 5, rechts 4 und 8). Je ein dritter Spieler pro Station (10, 3) nur im Text
# (3D-Abstand). Stationen leicht neben die Ecken gesetzt, damit Pass und Dribbling nicht durch die Hütchen gehen; Dribbling mit
# Zwischenpunkt außen um das Hütchen links unten. Trainer in der Mitte wie im PDF.
# Sichtkegel aus dem Text ("Eyes on the ball not the player when defending"): im Coaching-Punkt schaut Spieler sieben auf den Ball.
# Im Video kein Kegel eingezeichnet.
T = P("T", "c", 50, 36, "T")
POS = {"r7": (44, 5), "r6": (57, 6), "n9": (22, 55), "n5": (13.5, 57), "n4": (78, 55), "n8": (86.5, 57)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 32.5), B("s2", 46.4, 32.5)]
LINES = [line(25, 50, 75, 50, dashed=False), line(25, 50, 50, 6, dashed=False), line(75, 50, 50, 6, dashed=False)]
CONES = [C(25, 50), C(75, 50), C(50, 6)]

u = {"title": "Den Dribbler begleiten", "code": "UE-219", "kind": "Übungsform",
 "focuses": ["Verteidigen", "1 gegen 1", "Dribbling"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 9, "field_size": "18 x 14 m",
 "description": "Drei Stationen bilden ein Dreieck. Ein Spieler passt zur nächsten Station, und der Empfänger dribbelt mit Tempo zur Spitze. Ein Verteidiger von dort läuft ihm früh entgegen und begleitet ihn rückwärts bis zu seiner Station. So lernen die Kinder, schräg zu stehen und mit schnellen Füßen dranzubleiben.",
 "organisation": ["Aufbauen: Ein Dreieck aus drei Hütchen, unten 18 Meter breit und 14 Meter hoch.",
  "Verteilen: An jeder Ecke stehen zwei bis drei Spieler. Oben Team Rot, unten links und unten rechts Team Neon. Der Trainer steht in der Mitte mit Bällen.",
  "Ablauf: Spieler vier passt nach links zu Spieler neun und läuft hinterher. Spieler neun dribbelt zur Spitze, Spieler sieben läuft ihm entgegen und begleitet ihn rückwärts bis zu seiner Station.",
  "Wechsel: Spieler neun passt zu Spieler sechs, und der passt nach rechts unten. Dann dribbelt der Nächste zur nächsten Ecke, und von dort kommt der neue Verteidiger. So kommt jeder einmal dran."],
 "organisation_show": ORG,
 "coaching_points": ["Schräg stehen, nie gerade vor dem Dribbler", "Mit schnellen, kleinen Schritten rückwärts laufen", "Die Augen auf dem Ball, nicht auf dem Körper", "Als Dribbler den Ball eng am Fuß führen"],
 "materials": ["3 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Den Dribbler begleiten. Ein Spieler dribbelt mit Tempo, und ein Verteidiger läuft ihm entgegen und begleitet ihn rückwärts.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 78.6, 55.6)] + ERSATZ,
  "steps": [
   S("Pass und hinterher", "Spieler vier passt nach links zu Spieler neun und läuft seinem Pass hinterher.",
     ps("b1", [22.6, 55.6]), mv("n4", [30, 58], delay=0.3)),
   S("Dribbeln und anlaufen", "Spieler neun nimmt den Ball mit und dribbelt außen am Dreieck entlang zur Spitze. Gleichzeitig läuft Spieler sieben früh los und kommt ihm auf halbem Weg entgegen.",
     dr("n9", "b1", [19, 46]), dr("n9", "b1", [30, 33], after=True), mv("r7", [34, 26], delay=0.2)),
   S("Rückwärts begleiten", "Spieler sieben steht schräg und läuft mit kleinen Schritten rückwärts. Er bleibt vor Spieler neun und begleitet ihn bis zu seiner Station.",
     mv("r7", [41, 10]), dr("n9", "b1", [36, 18])),
   S("Weiter im Dreieck", "Spieler sieben ist nicht ausgespielt worden und hat seine Aufgabe geschafft. Spieler neun passt zu Spieler sechs, und der passt nach rechts unten zu Spieler acht. Jetzt dribbelt Spieler acht nach links, und von dort kommt der nächste Verteidiger.",
     ps("b1", [57.6, 6.6]), ps("b1", [87.1, 57.6], after=True))],
  "dims": [{"x1": 25, "y1": 58.6, "x2": 75, "y2": 58.6, "text": "18 m"}, {"x1": 93, "y1": 6, "x2": 93, "y2": 50, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schräg stehen und auf den Ball schauen.", "Ball im Blick",
    "Der Verteidiger steht nie gerade vor dem Dribbler, sondern schräg mit einem Fuß vorn. So kann er schnell nach beiden Seiten reagieren. Seine Augen bleiben auf dem Ball und nicht auf dem Körper.",
    sp(n9=(24, 44), r7=(36, 24)), [B("b1", 24.6, 44.6)] + ERSATZ,
    [S("Entgegenlaufen", "Spieler neun dribbelt zur Spitze. Spieler sieben läuft ihm entgegen und wird kurz vorher langsamer.",
       dr("n9", "b1", [29, 35]), mv("r7", [34, 27])),
     S("Ball im Blick", "Jetzt steht Spieler sieben schräg und schaut genau auf den Ball, nicht auf den Körper von Spieler neun.",
       bl("r7", [29.6, 35.6])),
     S("Rückwärts begleiten", "Spieler neun dribbelt weiter, Spieler sieben läuft mit schnellen, kleinen Schritten rückwärts. Spieler neun kommt nicht vorbei, und Spieler sieben hat seine Aufgabe geschafft.",
       dr("n9", "b1", [36, 18]), mv("r7", [41, 10]))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Verteidiger läuft erst zum Trainer.", "Erst zum Trainer",
    "Der Verteidiger muss zuerst zum Trainer in der Mitte laufen. Erst dann darf er den Dribbler anlaufen. So kommt er aus einem anderen Winkel, wie im Spiel, und muss sein Timing finden.",
    sp(), [B("b1", 78.6, 55.6)] + ERSATZ,
    [S("Erst zum Trainer", "Spieler vier passt zu Spieler neun und läuft hinterher. Gleichzeitig sprintet Spieler sieben zuerst zum Trainer in die Mitte.",
       ps("b1", [22.6, 55.6]), mv("n4", [30, 58], delay=0.3), mv("r7", [45, 30])),
     S("Neuer Winkel", "Spieler neun dribbelt außen am Dreieck entlang. Spieler sieben kommt jetzt von der Seite und läuft ihn schräg an.",
       dr("n9", "b1", [19, 46]), dr("n9", "b1", [29, 34], after=True), mv("r7", [36, 29], delay=0.3)),
     S("Rückwärts begleiten", "Spieler sieben bleibt vor Spieler neun und begleitet ihn rückwärts bis zur Station. Hat er das geschafft, geht es mit dem Pass zu Spieler sechs weiter.",
       mv("r7", [41, 10]), dr("n9", "b1", [36, 18]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
