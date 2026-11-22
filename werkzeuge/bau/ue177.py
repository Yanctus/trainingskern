import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P3 (U12-U14, Woche 16 Phase 5): Defend the Edge of the Box (Back 4). Feld 25 x 45 Yards = x 20-80, y 6-39.6 (41 x 23 m),
# Strafraum und Torraum nach der PDF-Skizze, oben ein Jugendtor mit Torwart. Gedreht: im PDF liegt das Tor rechts, hier oben;
# der Trainer (im PDF links, "top of the pitch") steht unten vor dem Feld. Pink (Verteidiger) + grüner Torwart -> Team Neon
# (n1 TW, 2, 3, 4, 5), dunkel (Angreifer) -> Team Rot (7, 9, 10, 11), Nummern wie im PDF. Die zweite Viererkette (gelb, wartet
# neben dem Tor) steht nur im Text. Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video.
# Sichtkegel: Ton "Players should also recognise pressing triggers, such as a poor pass or a heavy touch" -> in der Grundform
# bl() von Spieler vier zum ballführenden Spieler zehn (zu weiter Kontakt), bevor er presst (im Video kein Kegel eingezeichnet,
# Richtung aus dem Sinn).
T = P("T", "c", 50, 46, "T")
POS = {"n1": (50, 8.5), "n2": (33, 24), "n4": (41.5, 22), "n5": (58.5, 22), "n3": (67, 24),
       "r9": (50, 25), "r11": (24.5, 31), "r10": (41.5, 38), "r7": (75.5, 31)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 53.6, 49.5), B("s2", 50, 49.5)]
LINES = [rect(20, 6, 60, 33.6), rect(26.2, 6, 47.6, 14.6), rect(37.7, 6, 24.6, 5.6)]
TORE = [{"x": 50, "y": 6, "side": "top", "size": "jugend"}]
MINI = [{"x": 24, "y": 39.6, "side": "bottom"}, {"x": 76, "y": 39.6, "side": "bottom"}]

u = {"title": "Vor dem Strafraum verteidigen", "code": "UE-177", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 13, "field_size": "41 x 23 m",
 "description": "Vier Angreifer spielen gegen eine Viererkette und einen Torwart auf das große Tor. Die Verteidiger bleiben am Strafraum eng zusammen: Einer presst, die anderen drei sichern ab. Erobern sie den Ball und spielen ihn zum Trainer, bekommen sie zwei Punkte. Nach zwei Angriffen kommt die nächste Viererkette ins Feld.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 23 Metern mit Strafraum und einem Jugendtor oben. Der Trainer steht unten vor dem Feld mit vielen Bällen.",
  "Verteilen: Team Neon verteidigt mit vier Spielern und einem Torwart. Team Rot greift mit vier Spielern an. Eine zweite Viererkette wartet neben dem Tor.",
  "Ablauf: Der Trainer spielt den Ball zu Team Rot, und vier gegen vier geht es los. Team Neon hält die Kette eng und presst gemeinsam. Nach einem Ballgewinn spielt Team Neon den Ball schnell zum Trainer.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Rot. Ballgewinn und Pass zum Trainer gibt zwei Punkte für Team Neon. Nach zwei Angriffen wechselt die Viererkette."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, die anderen drei sichern ab", "Die Kette eng halten, damit keine Lücken entstehen", "Erkennen, wann die Kette stehen bleibt, rausrückt oder zurückläuft", "Nach dem Ballgewinn schnell nach vorn spielen"],
 "materials": ["1 Jugendtor", "2 Minitore für die Steigerung", "Hütchen für Feld und Strafraum", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Vor dem Strafraum verteidigen. Vier gegen vier vor dem großen Tor, und Team Neon verteidigt als enge Viererkette.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 46.6)] + ERSATZ,
  "steps": [
   S("Ball zu Team Rot", "Der Trainer spielt den Ball zu Spieler zehn. Team Rot greift das große Tor an, Team Neon verteidigt am Strafraum.",
     ps("b1", [42.1, 38.6])),
   S("Einer presst", "Spieler zehn dribbelt an, aber der Ball springt ihm zu weit weg. Spieler vier sieht das und presst sofort. Gleichzeitig schieben Spieler zwei, fünf und drei nach und sichern ab.",
     dr("r10", "b1", [41.5, 32]), bl("n4", [41.5, 32]), mv("n4", [41.5, 27], after=True),
     mv("n5", [54, 21.5], delay=0.9), mv("n3", [62.5, 23], delay=0.9), mv("n2", [33, 26], delay=0.9)),
   S("Abgefangen", "Spieler zehn will zu Spieler elf passen. Spieler zwei geht dazwischen und fängt den Ball ab.",
     mv("n2", [30.4, 31.4]), ps("b1", [31, 32], delay=0.3)),
   S("Zum Trainer: zwei Punkte", "Spieler zwei spielt den Ball sofort zum Trainer, und das gibt zwei Punkte für Team Neon. Dann spielt der Trainer den nächsten Ball zu Team Rot. Nach zwei Angriffen ist die nächste Viererkette dran.",
     ps("b1", [50.6, 46.6]))],
  "dims": dims(20, 80, 6, 39.6, "41 m", "23 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, die anderen sichern ab.", "Einer presst, drei sichern",
    "Nur ein Verteidiger läuft den Ball an. Die anderen drei bleiben nah hinter und neben ihm und machen die Passwege zu. So bleibt die Kette eng, und der Angreifer muss nach hinten spielen.",
    sp(), [B("b1", 42.1, 38.6)] + ERSATZ,
    [S("Spieler vier presst", "Spieler zehn hat den Ball. Spieler vier läuft raus und presst. Gleichzeitig rücken Spieler zwei, fünf und drei eng an ihn heran.",
       mv("n4", [41.5, 31]), mv("n2", [34, 25.5], delay=0.2), mv("n5", [55, 21], delay=0.2), mv("n3", [63, 23], delay=0.2)),
     S("Kein Weg nach vorn", "Spieler zehn findet keine Lücke und dreht nach hinten ab. Die Kette steht weiter eng zusammen.",
       dr("r10", "b1", [36, 37]))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Ballgewinn kontert Team Neon auf zwei Minitore.", "Konter auf die Minitore",
    "Unten in den Ecken stehen zwei Minitore. Erobert Team Neon den Ball, spielt es schnell über außen und schießt in ein Minitor. Das gibt zwei Punkte für Team Neon.",
    sp(), [B("b1", 50.6, 25.6)] + ERSATZ,
    [S("Abgefangen", "Spieler neun will zu Spieler zehn passen. Spieler vier geht dazwischen und fängt den Ball ab.",
       mv("n4", [46.5, 30.4]), ps("b1", [47.1, 31], delay=0.3)),
     S("Über außen", "Spieler drei läuft sofort nach außen. Spieler vier spielt ihm den Ball in den Lauf.",
       mv("n3", [70, 35]), ps("b1", [70.6, 35.6], delay=0.3)),
     S("Minitor: zwei Punkte", "Spieler drei schießt ins rechte Minitor, und das gibt zwei Punkte für Team Neon. Dann spielt der Trainer den nächsten Ball zu Team Rot.",
       ps("b1", [76, 39.3]))],
    goals=TORE + MINI)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
