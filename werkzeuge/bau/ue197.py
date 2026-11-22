import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 62-P3 (U12-U14, Woche 24 Phase 6): 1 v 1 Defensive Recovery Runs. 15 x 15 Yards = Feld x 30-70, y 5-45 (14 x 14 m), längs
# geteilt (gestrichelt bei x 50), in jeder Hälfte ein Minitor. Gedreht (180 Grad): im PDF liegen die Minitore unten, hier oben.
# Je Hälfte ein Starthütchen und ein Hütchen gut 4 m (5 Yards) vor dem Tor als Marke (im PDF rot, hier orange).
# Im PDF sind alle Spieler pink (eine Gruppe pro Hälfte): linke Gruppe -> Team Neon (7, 4, 5), rechte Gruppe -> Team Rot (10, 8, 9),
# Nummern frei vergeben, je drei statt vier Spieler pro Gruppe (3D-Abstand), Wertung für Verteidiger ergänzt (Block/Ballgewinn = Punkt).
# Start des Zweiten wie im Ton: sobald der Erste an der Marke vorbei ist. Steigerung (schräges Tor) wie im PDF: das linke Minitor
# steht unten (hier kommt es unten links dazu, das obere bleibt stehen: Regel Fassungen ergänzen Tore), Team Neon startet oben links (wartende Spieler links neben dem Feld), Rot schießt zuerst und sprintet schräg zurück.
# Sichtkegel: Text "Attackers must get head up to see defenders position" (im Video kein Kegel eingezeichnet): bl() vom
# Angreifer zum heranlaufenden Verteidiger (Grundform, Coaching-Punkt, Steigerung).
T = P("T", "c", 20, 25, "T")
POS = {"n7": (41, 38), "n4": (33, 54), "n5": (42, 54), "r10": (59, 38), "r8": (58, 54), "r9": (67, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 28.5), B("s2", 20, 28.5)]
WARTE = [B("b3", 33.6, 54.6), B("b4", 42.6, 54.6), B("b5", 58.6, 54.6), B("b6", 67.6, 54.6)]
LINES = [rect(30, 5, 40, 40), line(50, 5, 50, 45)]
TORE = [{"x": 40, "y": 5, "side": "top"}, {"x": 60, "y": 5, "side": "top"}]
CONES = [C(36, 40), C(36, 18), C(64, 40), C(64, 18)]

u = {"title": "Nach dem Schuss verteidigen", "code": "UE-197", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "14 x 14 m",
 "description": "Ein Spieler dribbelt nach vorn und schießt ins Minitor. Sobald er an der Marke vorbei ist, startet auf der anderen Seite der Nächste. Der Schütze sprintet sofort hinüber und verteidigt das andere Minitor. So lernen die Kinder, nach dem eigenen Schuss blitzschnell umzuschalten.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern, längs in zwei Hälften geteilt. In jeder Hälfte oben ein Minitor, unten ein Starthütchen und gut 4 Meter vor dem Tor ein Hütchen als Marke.",
  "Verteilen: Team Neon wartet unten links, Team Rot unten rechts, jeder Spieler mit einem Ball. Der Trainer steht links neben dem Feld mit Bällen.",
  "Ablauf: Der Erste dribbelt nach vorn und schießt ins Minitor. Ist er an der Marke vorbei, dribbelt der Erste der anderen Seite los. Der Schütze sprintet sofort hinüber und verteidigt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das eigene Team. Blockt oder erobert der Verteidiger den Ball, gibt das einen Punkt für sein Team. Dann startet der Nächste, bis alle Bälle gespielt sind."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem Schuss sofort umschalten und zurück sprinten", "Seitlich stehen und den Angreifer in eine Richtung lenken", "Nicht hineinspringen, bei spätem Kommen den Schuss blocken", "Als Angreifer den Kopf heben und den Verteidiger sehen"],
 "materials": ["2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Nach dem Schuss verteidigen. Erst schießt ein Spieler ins Minitor, dann sprintet er sofort hinüber und verteidigt gegen den Nächsten.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 41.6, 38.6), B("b2", 59.6, 38.6)] + WARTE + ERSATZ,
  "steps": [
   S("Losdribbeln", "Links wartet Team Neon, rechts Team Rot, jeder mit einem Ball. Spieler sieben dribbelt schnell nach vorn, am Hütchen vorbei.",
     dr("n7", "b1", [42, 20])),
   S("Abschluss: Punkt", "Spieler sieben schießt ins Minitor, und das gibt einen Punkt für Team Neon. Weil er an der Marke vorbei ist, dribbelt Spieler zehn auf der anderen Seite los.",
     ps("b1", [40, 5.3]), dr("r10", "b2", [58, 28], delay=0.3)),
   S("Hinüber sprinten", "Gleich nach dem Schuss sprintet Spieler sieben hinüber zum rechten Minitor. Spieler zehn hebt den Kopf und sieht, wo der Verteidiger ist.",
     mv("n7", [53, 15]), bl("r10", [46, 18], delay=0.2), dr("r10", "b2", [58, 23], after=True)),
   S("Schuss geblockt: Punkt", "Spieler sieben stellt sich seitlich in den Weg und blockt den Schuss von Spieler zehn. Das gibt einen Punkt für Team Neon, ein Treffer gäbe einen Punkt für Team Rot. Danach startet Spieler vier, und Spieler zehn sprintet hinüber und verteidigt.",
     mv("n7", [56, 13]), ps("b2", [56.6, 13.6], delay=0.4))],
  "dims": dims(30, 70, 5, 45, "14 m", "14 m", rx=76)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit einer Finte den Verteidiger täuschen.", "Mit einer Finte vorbei",
    "Der Angreifer hebt den Kopf und sieht, wo der Verteidiger steht. Mit einem Übersteiger täuscht er eine Richtung an. Dann zieht er schnell in die andere Richtung und schießt ins Minitor.",
    sp(n7=(53, 12), r10=(59, 30)), [B("b2", 59.6, 30.6)] + WARTE + ERSATZ,
    [S("Kopf hoch", "Spieler zehn dribbelt auf das Tor zu. Er hebt den Kopf und sieht, wo Spieler sieben steht.",
       dr("r10", "b2", [59, 26]), bl("r10", [53, 12], after=True)),
     S("Übersteiger", "Spieler zehn täuscht mit einem Übersteiger nach links an. Spieler sieben fällt darauf herein und geht mit nach links.",
       dr("r10", "b2", [56, 23]), mv("n7", [49, 13], delay=0.3)),
     S("Andere Richtung: Punkt", "Jetzt zieht Spieler zehn schnell nach rechts und schießt ins Minitor. Das gibt einen Punkt für Team Rot.",
       dr("r10", "b2", [60.5, 20]), ps("b2", [60, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Das Tor schräg gegenüber verteidigen.", "Das Tor schräg gegenüber",
    "Unten links kommt ein Minitor dazu, und Team Neon startet jetzt oben und schießt nach unten. Nach dem Schuss muss der Verteidiger schräg über das ganze Feld sprinten. Der Nächste darf erst los, wenn der Ball geschossen ist.",
    sp(n7=(42, 11), n4=(22, 9), n5=(13, 9)),
    [B("b1", 42.6, 11.6), B("b2", 59.6, 38.6), B("b3", 22.6, 9.6), B("b4", 13.6, 9.6), B("b5", 58.6, 54.6), B("b6", 67.6, 54.6)] + ERSATZ,
    [S("Abschluss oben: Punkt", "Spieler zehn dribbelt am Hütchen vorbei und schießt ins Minitor oben. Das gibt einen Punkt für Team Rot.",
       dr("r10", "b2", [58, 20]), ps("b2", [60, 5.3], after=True)),
     S("Schräg zurück", "Mit dem Schuss dribbelt Spieler sieben oben links los. Spieler zehn sprintet schräg über das Feld zum Minitor unten. Spieler sieben hebt den Kopf und sieht ihn kommen.",
       dr("n7", "b1", [42, 22]), mv("r10", [51, 31]), bl("n7", [51, 32], after=True)),
     S("Schuss geblockt: Punkt", "Spieler zehn läuft zum Tor und stellt sich in den Weg. Er blockt den Schuss von Spieler sieben, und das gibt einen Punkt für Team Rot. Danach startet Spieler acht, und Spieler sieben sprintet zurück.",
       dr("n7", "b1", [42, 30]), mv("r10", [43, 39]), ps("b1", [43.6, 39.6], after=True))],
    goals=TORE + [{"x": 40, "y": 45, "side": "bottom"}],
    cones=[C(36, 9, id="c1"), C(36, 32, id="c2"), C(64, 40, id="c3"), C(64, 18, id="c4")])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
