import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 11-P7 (U12-U14, Woche 36 Phase 6): Midfielders Pressing to Regain / How to Win Possession as a Midfield Unit. 25 x 30 Yards
# = Feld x 28.7-71.3, y 5-55 (23 x 27 m). Um 180 Grad gedreht: die zwei Minitore stehen oben (im Original unten).
# Pink (Ballbesitz in der Raute) -> Rot, Navy/Gold (pressendes Mittelfeld plus Stürmer neun) -> Neon 6, 8, 10, 9.
# Nummern neu (im PDF doppelt): Rot 4 (Pink 6), 5 (Pink 8), 7, 11. Hütchen der Raute leicht nach außen neben die Spieler gesetzt,
# Positionen auf 3D-Abstand gesetzt. Ein Trainer statt zwei.
# Sichtkegel aus dem Text ("Head up to see pass after winning possession", Key Coaching Point 3 im Video): nach dem Ballgewinn
# schaut der Eroberer zum Stürmer neun (Grundform und Steigerung). Im Video kein Kegel eingezeichnet.
# Fassungen: Coaching-Punkt aus dem PDF (einer presst, zwei sichern die Passwege), Steigerung aus PDF und Ton
# (Spieler sechs deckt den Mittelfeldspieler von hinten).
T = P("T", "c", 79, 30, "T")
POS = {"r4": (50, 13), "r7": (33, 30), "r11": (67, 30), "r5": (50, 49),
       "n6": (50, 28.5), "n8": (41.5, 40), "n10": (58.5, 40), "n9": (59, 8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 82.6, 33.5), B("s2", 79, 33.5)]
LINES = [rect(28.7, 5, 42.6, 50)]
KEGEL = [C(50, 10.3), C(30.6, 30), C(69.4, 30), C(50, 51.8)]
TORE = [{"x": 36.5, "y": 5, "side": "top"}, {"x": 63.5, "y": 5, "side": "top"}]

u = {"title": "Zu dritt pressen in der Raute", "code": "UE-230", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "23 x 27 m",
 "description": "Vier Spieler halten den Ball auf den Hütchen einer Raute, drei Mittelfeldspieler pressen gemeinsam. Jeder Pass quer durch die Mitte der Raute gibt einen Punkt für die Ballbesitzer. Erobern die drei den Ball, spielen sie sofort zum Stürmer, der auf zwei Minitore abschließt. Nach jedem Treffer tauschen die Teams die Aufgaben.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 27 Metern. In der Mitte vier Hütchen als Raute, oben zwei Minitore.",
  "Verteilen: Team Rot steht zu viert auf den Hütchen der Raute. Drei Spieler von Team Neon pressen in der Mitte, der Stürmer von Team Neon wartet vor den Minitoren. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Rot hält den Ball und darf innen und außen um die Raute passen. Team Neon presst zu dritt, erobert den Ball und spielt sofort zum Stürmer.",
  "Wertung und Wechsel: Jeder Pass durch die Mitte gibt einen Punkt für Team Rot, jeder Treffer des Stürmers einen Punkt für Team Neon. Nach einem Treffer tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Als Einheit pressen und die Passwege zustellen", "Kompakt bleiben, damit kein Pass durch die Mitte geht", "Laut rufen: schieben, pressen, Schulter", "Nach dem Ballgewinn den Kopf heben und den Stürmer suchen"],
 "materials": ["2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zu dritt pressen in der Raute. Drei Mittelfeldspieler arbeiten zusammen, erobern den Ball und spielen schnell zum Stürmer.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 50.6, 13.6)] + ERSATZ,
  "steps": [
   S("Ball halten", "Team Rot hält den Ball in der Raute, und jeder Pass quer durch die Mitte gibt einen Punkt für Team Rot. Spieler vier spielt zu Spieler elf. Team Neon schiebt gemeinsam: Spieler zehn läuft an, Spieler sechs und Spieler acht machen die Mitte eng.",
     ps("b1", [67.6, 30.6]), mv("n10", [64, 25], delay=0.3), mv("n6", [53, 30], delay=0.3), mv("n8", [48, 38], delay=0.3)),
   S("Abgefangen", "Spieler elf will zu Spieler fünf passen. Aber Spieler acht ahnt den Pass, startet und fängt den Ball ab.",
     mv("n8", [57, 41.5]), ps("b1", [57.6, 42.1], delay=0.2)),
   S("Kopf hoch", "Spieler acht hebt sofort den Kopf und sieht Spieler neun vorn bei den Minitoren. Er spielt schnell zu ihm.",
     bl("n8", [58.5, 23]), ps("b1", [59.6, 8.6], after=True)),
   S("Abschluss: Punkt", "Spieler neun schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Dann tauschen die Teams die Aufgaben: Jetzt hält Team Neon den Ball in der Raute, und Team Rot presst.",
     ps("b1", [63.5, 5.3]))],
  "dims": dims(28.7, 71.3, 5, 55, "23 m", "27 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, zwei sichern ab.", "Einer presst, zwei sichern",
    "Einer läuft den Ballführenden an, die beiden anderen stellen die Passwege zu. So bleibt die Form zu dritt erhalten. Der Gegner findet keinen freien Mitspieler und macht einen Fehler.",
    sp(), [B("b1", 33.6, 30.6)] + ERSATZ,
    [S("Passwege zu", "Spieler sieben hat den Ball. Spieler acht läuft ihn an und macht den Weg nach vorn zu. Spieler sechs stellt die Mitte zu, und Spieler zehn sichert den Pass nach hinten.",
       mv("n8", [37, 26]), mv("n6", [46, 29], delay=0.2), mv("n10", [46, 44], delay=0.2)),
     S("Fehler erzwungen: Punkt", "Spieler sieben spielt doch zu Spieler fünf, und Spieler zehn fängt den Ball ab. Er spielt sofort zu Spieler neun, und der trifft. Das gibt einen Punkt für Team Neon.",
       ps("b1", [46.6, 44.6]), ps("b1", [59.6, 8.6], after=True), ps("b1", [63.5, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Spieler sechs deckt von hinten.", "Von hinten decken",
    "Spieler sechs steht jetzt hinter dem Mittelfeldspieler von Team Rot und deckt ihn ganz eng. Der muss sich vorn freilaufen und direkt spielen. Die beiden anderen Pressingspieler müssen dafür mehr Raum abdecken.",
    sp(r5=(47, 48), n6=(55.5, 53.5), n8=(41.5, 32), n10=(58.5, 32)), [B("b1", 50.6, 13.6)] + ERSATZ,
    [S("Mehr Raum abdecken", "Spieler sechs steht hinter Spieler fünf. Spieler vier spielt zu Spieler sieben. Spieler acht läuft an, und Spieler zehn schiebt zur Mitte.",
       ps("b1", [33.6, 30.6]), mv("n8", [37.5, 28], delay=0.3), mv("n10", [55, 34], delay=0.3)),
     S("Von hinten erobert", "Spieler sieben spielt zu Spieler fünf. Spieler sechs kommt von hinten, läuft vor ihn und fängt den Ball ab.",
       mv("n6", [49, 44]), mv("n6", [43.5, 43.5], after=True), ps("b1", [44.1, 44.1], delay=0.4)),
     S("Konter: Punkt", "Spieler sechs hebt den Kopf, sieht Spieler neun und spielt sofort zu ihm. Spieler neun trifft, und das gibt einen Punkt für Team Neon.",
       bl("n6", [51.5, 25.5]), ps("b1", [59.6, 8.6], after=True), ps("b1", [63.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
