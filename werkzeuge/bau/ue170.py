import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 92-P4 (U12-U14, Woche 13 Phase 1): Passing and Movement to Receive. 20 x 25 Yards = Feld x 30-70, y 5-55 (18 x 23 m).
# Ausrichtung wie im PDF: Start unten, der Ablauf geht nach oben und kommt im Slalom links zurück. Nummern wie im PDF
# (10 Start, 8 Mitte, 2 rechts, 7 oben rechts, 9 oben links); die Wartenden 6 (Start) und 4 (Mitte) nur im Text, nicht auf der Tafel.
# Puppen und Stangen als shape "stange". Ein Trainer statt zwei. Rechte Stange etwas nach innen gesetzt (Platz für Spieler zwei).
# Wechsel "jeder läuft seinem Pass hinterher" aus dem Breakdown-Bild abgeleitet (dort nicht ganz eindeutig).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 79, 50, "T")
POS = {"n10": (51.8, 53), "n8": (51.6, 32.4), "n2": (68.5, 31), "n7": (61.5, 9.6), "n9": (43.7, 7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items() if (x, y) != (0, 0)] + [T]
ERSATZ = [B("s1", 79.6, 53.5), B("s2", 76, 53.5)]
STANGEN = [C(34.4, 20, shape="stange"), C(34.4, 30, shape="stange"), C(59.2, 22.5, shape="stange"), C(64.5, 26, shape="stange"),
           C(45.8, 39, shape="stange"), C(54.7, 39, shape="stange")]
HUET = [C(48.5, 54), C(43.5, 9.8), C(57.5, 12.5), C(48.8, 34)]
LINES = [rect(30, 5, 40, 50)]

u = {"title": "Passen und Freilaufen", "code": "UE-170", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Dribbling"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 9, "field_size": "18 x 23 m",
 "description": "Ein Passkreislauf über fünf Stationen mit Doppelpässen, Ablagen und Pässen durch die Stangen. Jeder Spieler läuft sich vor dem Pass frei und bietet sich mit einer schnellen Bewegung an. Der letzte Spieler dribbelt im Slalom durch die Stangen zurück zum Start. Sobald er an der ersten Stange vorbei ist, beginnt der nächste Durchgang.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern mit Stangen und zwei Puppen wie auf dem Bild. Hütchen markieren die Stationen: Start, Mitte, rechts, oben rechts und oben links.",
  "Verteilen: Sieben Spieler. Zwei am Start mit Bällen, zwei in der Mitte, je einer rechts, oben rechts und oben links. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Doppelpass von Start und Mitte, Pass nach rechts, Pass nach innen, Pass durch die Stangen, Ablagen und ein Steilpass nach oben links. Der letzte Spieler dribbelt im Slalom zum Start.",
  "Wechsel: Jeder läuft nach seinem Pass zur Station, zu der er gespielt hat. Ist der Dribbler an der ersten Stange vorbei, startet der nächste Durchgang."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen", "Mit einer schnellen Bewegung freilaufen und einen guten Winkel anbieten", "Beim Dribbling den Ball eng am Fuß führen", "Mit einem oder zwei Kontakten spielen und dabei laut rufen"],
 "materials": ["6 Stangen oder Puppen", "6 Hütchen", "Viele Bälle", "1 Minitor für die Steigerung"],
 "access": "abo", "hidden": True,
 "say_intro": "Passen und Freilaufen. Ein Passkreislauf mit Doppelpässen, Ablagen und einem Slalom zurück zum Start.",
 "board": {"lines": LINES, "cones": STANGEN + HUET, "players": sp(), "balls": [B("b1", 52.4, 53.6)] + ERSATZ,
  "steps": [
   S("Doppelpass", "Spieler zehn passt zu Spieler acht, der dem Ball entgegenkommt. Spieler acht legt direkt ab, und Spieler zehn ist schon nach rechts gelaufen.",
     mv("n8", [49.6, 42.5]), ps("b1", [50.2, 43.1], delay=0.3), mv("n10", [57.4, 49.5], after=True), ps("b1", [58, 50.1], after=True)),
   S("Nach außen", "Spieler zehn spielt weit nach rechts zu Spieler zwei. Gleichzeitig läuft Spieler acht nach rechts in die Mitte.",
     ps("b1", [69.1, 31.6]), mv("n8", [52, 37]), mv("n8", [57.4, 31.8], after=True)),
   S("Nach innen und durch", "Spieler zwei passt nach innen zu Spieler acht. Spieler sieben startet, und Spieler acht spielt ihm den Ball durch die Stangen.",
     ps("b1", [58, 32.4]), mv("n7", [66, 14.9], delay=0.3), ps("b1", [66.6, 15.5], after=True)),
   S("Ablegen und quer", "Spieler sieben legt ab für Spieler zwei, der ein Stück hoch kommt. Spieler zwei spielt weit quer zu Spieler neun.",
     mv("n2", [69, 26.5]), ps("b1", [69.6, 27.1], delay=0.2), ps("b1", [44.3, 7.6], after=True), mv("n7", [60.4, 8.7], after=True)),
   S("Ablegen und steil", "Spieler neun legt für Spieler sieben ab. Der spielt sofort steil, und Spieler neun nimmt den Ball im Lauf mit.",
     ps("b1", [61, 9.3]), mv("n9", [36, 14.1], after=True), ps("b1", [36.6, 14.7], after=True)),
   S("Slalom zum Start", "Spieler neun dribbelt im Slalom durch die Stangen zurück zum Start. Ist er an der ersten Stange vorbei, startet der nächste Durchgang. Jeder läuft zur Station, zu der er gepasst hat.",
     dr("n9", "b1", [31.8, 17]), dr("n9", "b1", [31.6, 22.5], after=True), dr("n9", "b1", [37.4, 30], after=True), dr("n9", "b1", [33, 38.5], after=True),
     dr("n9", "b1", [38.3, 46.1], after=True), dr("n9", "b1", [46, 53], after=True))],
  "dims": dims(30, 70, 5, 55, "18 m", "23 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Scharf freilaufen.", "Scharf freilaufen",
    "Wer den Ball haben will, geht erst einen Schritt weg und kommt dann schnell entgegen. So hat er Platz und einen guten Winkel. Er ruft, und der Pass kommt flach und genau.",
    sp(), [B("b1", 52.4, 53.6)] + ERSATZ,
    [S("Erst weg", "Spieler acht geht erst einen Schritt weg vom Ball und ruft.",
       mv("n8", [52, 27.5])),
     S("Dann entgegen", "Dann kommt er schnell entgegen. Spieler zehn passt flach, und Spieler acht legt mit einem Kontakt ab.",
       mv("n8", [49.6, 42.5]), ps("b1", [50.2, 43.1], delay=0.4), mv("n10", [57.4, 49.5], delay=0.4), ps("b1", [58, 50.1], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Abschluss ins Minitor.", "Abschluss ins Minitor",
    "Unten links steht ein Minitor. Der Spieler oben links dribbelt an der ersten Stange vorbei und spielt einen Doppelpass mit dem Trainer. Dann schießt er ins Minitor. Danach geht es zurück zum Start.",
    sp(n9=(35, 11), T=(0, 0))[:-1] + [P("T", "c", 43.3, 27, "T")], [B("b1", 35.6, 11.6), B("s1", 47, 27.5), B("s2", 47, 24)],
    [S("Vorbei an der Stange", "Spieler neun dribbelt links an der ersten Stange vorbei und passt zum Trainer.",
       dr("n9", "b1", [31.6, 16]), dr("n9", "b1", [31.6, 24.5], after=True), ps("b1", [43.9, 27.6], after=True)),
     S("Doppelpass", "Spieler neun läuft weiter nach unten, und der Trainer spielt ihm den Ball zurück in den Lauf.",
       mv("n9", [31.5, 37]), ps("b1", [32.1, 37.6], delay=0.4)),
     S("Minitor: Punkt", "Spieler neun schießt ins Minitor, und das gibt einen Punkt für Spieler neun. Dann startet der Nächste.",
       ps("b1", [36, 54.7]))],
    goals=[{"x": 36, "y": 55, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
