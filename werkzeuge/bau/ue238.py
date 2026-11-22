import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 11-P9 (U12-U14, Woche 38 Phase 4): Winning Possession in Midfield. 50 x 30 Yards = Feld x 10-90, y 6-54 (46 x 27 m),
# zwei Zonen je 25 Yards (Mittellinie gestrichelt). Gedreht wie im Video (PDF hochkant): großes Tor rechts, zwei Minitore
# links, Team Neon spielt nach rechts. Navy (vorne drei) -> Neon 11, 9, 7; Pink -> Rot 2, 4, 8, 3 (links) und 5, 6
# (Innenverteidiger rechts), Torwart Grün 1 -> Rot r1 "TW". Strafraum als Rechteck. Ein Trainer statt zwei.
# Grundform nach PDF: 3 passt zu 8, 8 will zu 4, Spieler neun fängt ab, Konter drei gegen zwei
# (Abschluss vereinfacht: Spieler neun dribbelt, Spieler elf ist frei). Fassungen: Coaching-Punkt 1
# (zusammen verschieben, Passwege zu) und Steigerung aus Text/Ton (Innenverteidiger erobern und kontern zu viert auf die Minitore).
# Sichtkegel aus Text ("recognise the 3 v 2 overload ... find the free player", "identify when ... apply pressure"):
# Spieler neun schaut vor dem Pass zum freien Spieler elf, im Coaching-Punkt schaut Spieler sieben auf den Passweg.
# Im Video kein Kegel eingezeichnet.
T = P("T", "c", 4, 30, "T")
POS = {"n11": (34, 12), "n9": (31, 30), "n7": (40, 40), "r2": (44, 12), "r4": (22, 20), "r8": (20, 40), "r3": (49, 50),
       "r5": (66, 22), "r6": (67, 38), "r1": (87, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 5.6, 33.5), B("s2", 2, 33.5)]
LINES = [rect(10, 6, 80, 48), line(50, 6, 50, 54), rect(75, 15, 15, 30)]
TORE = [{"x": 90, "y": 30, "side": "right", "size": "jugend"}, {"x": 10, "y": 18, "side": "left"}, {"x": 10, "y": 42, "side": "left"}]

u = {"title": "Vorne erobern, zu dritt kontern", "code": "UE-238", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "46 x 27 m",
 "description": "Drei Stürmer von Team Neon pressen gemeinsam gegen vier Spieler von Team Rot, die in der linken Hälfte den Ball halten. Erobern die drei den Ball, kontern sie sofort in die rechte Hälfte, drei gegen zwei Innenverteidiger und den Torwart. Erobert Team Rot den Ball, kontert es zu viert auf die zwei Minitore. So üben die Stürmer, als Einheit Druck zu machen und nach dem Ballgewinn schnell zu sein.",
 "organisation": ["Aufbauen: Ein Feld von 46 mal 27 Metern in zwei Hälften (gestrichelt). Rechts ein Jugendtor mit Strafraum, links zwei Minitore.",
  "Verteilen: Team Rot hat vier Spieler in der linken Hälfte, zwei Innenverteidiger und den Torwart rechts. Team Neon hat drei Stürmer in der linken Hälfte. Der Trainer steht links mit Bällen.",
  "Ablauf: Team Rot hält den Ball zu viert, die drei von Team Neon pressen gemeinsam. Nach dem Ballgewinn kontert Team Neon in die rechte Hälfte, drei gegen zwei.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Neon, ein Treffer ins Minitor einen Punkt für Team Rot. Nach jedem Angriff startet Team Rot wieder links mit Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Zu dritt als Einheit Druck machen", "Erkennen, wann der Moment zum Pressen da ist, zum Beispiel bei einem Pass zur Seite", "Zusammen verschieben, eng bleiben und Passwege zumachen", "Im Konter die Überzahl nutzen und den freien Spieler finden"],
 "materials": ["1 Jugendtor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Vorne erobern, zu dritt kontern. Drei Stürmer pressen gemeinsam gegen vier und kontern nach dem Ballgewinn sofort nach vorn.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(10, 6, 80, 48), "players": sp(), "balls": [B("b1", 49.6, 50.6)] + ERSATZ,
  "steps": [
   S("Vier gegen drei", "Team Rot hält den Ball zu viert. Spieler drei passt zu Spieler acht. Spieler sieben, neun und elf verschieben gleichzeitig mit und machen es eng.",
     ps("b1", [20.6, 40.6]), mv("n7", [30, 45], delay=0.3), mv("n9", [28, 29], delay=0.3), mv("n11", [30, 16], delay=0.3)),
   S("Abgefangen", "Spieler acht will zu Spieler vier passen. Spieler neun ahnt den Pass, läuft in den Passweg und fängt den Ball ab.",
     mv("n9", [21, 31]), ps("b1", [21.6, 31.6], delay=0.3)),
   S("Konter drei gegen zwei", "Sofort geht es nach vorn. Spieler neun dribbelt in die rechte Hälfte, Spieler elf und Spieler sieben laufen gleichzeitig außen mit. Jetzt sind es drei gegen zwei.",
     dr("n9", "b1", [56, 30]), mv("n11", [50, 19], delay=0.2), mv("n7", [68, 47], delay=0.2), mv("n11", [68, 12], after=True)),
   S("Abschluss: Punkt", "Spieler fünf geht auf Spieler neun, Spieler sechs bleibt bei Spieler sieben. Spieler neun schaut und sieht Spieler elf frei. Er spielt zu ihm, und Spieler elf trifft ins große Tor. Das gibt einen Punkt für Team Neon. Danach startet Team Rot wieder links mit Ball.",
     mv("r5", [60, 31]), mv("r6", [68, 41]), bl("n9", [66, 14], after=True), ps("b1", [68.6, 12.6], after=True), ps("b1", [89.7, 26], after=True))],
  "dims": dims(10, 90, 6, 54, "46 m", "27 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zusammen verschieben und Passwege zumachen.", "Zusammen verschieben",
    "Die drei Stürmer bewegen sich wie eine Einheit. Geht der Ball zur Seite, presst der Nächste, und die anderen rücken ein und machen die Passwege zu. So muss Team Rot einen schwierigen Pass spielen, und Team Neon fängt ihn ab.",
    sp(), [B("b1", 22.6, 20.6)] + ERSATZ,
    [S("Pass zur Seite", "Spieler vier passt zur Seite zu Spieler zwei. Jetzt pressen alle drei gleichzeitig: Spieler elf läuft Spieler zwei an, Spieler neun macht den Rückpass zu, und Spieler sieben rückt ein.",
       ps("b1", [44.6, 12.6]), mv("n11", [39, 17], delay=0.3), mv("n9", [33, 22], delay=0.3), mv("n7", [42, 33], delay=0.3)),
     S("Passweg zu", "Spieler zwei hat keinen kurzen Pass mehr und will lang zu Spieler drei spielen. Spieler sieben schaut auf den Passweg und läuft hinein.",
       bl("n7", [48, 47]), mv("n7", [47, 35], after=True), ps("b1", [47.6, 35.6], delay=0.4)),
     S("Abgefangen", "Spieler sieben fängt den Ball ab und dribbelt sofort nach vorn. Jetzt kontert Team Neon drei gegen zwei.",
       dr("n7", "b1", [60, 33]))]),
  V("Steigerung", "Und jetzt die Steigerung: Team Rot kontert zu viert.", "Rot kontert",
    "Erobern die Innenverteidiger von Team Rot den Ball, kontern sie mit den Mitspielern auf die zwei Minitore. Ein Treffer gibt einen Punkt für Team Rot. Die drei Stürmer von Team Neon müssen dann sofort zurücksprinten.",
    sp(n11=(66, 16), n9=(56, 30), n7=(66, 44), r5=(75, 22), r6=(76, 38)), [B("b1", 66.6, 16.6)] + ERSATZ,
    [S("Rot erobert", "Team Neon kontert. Spieler elf will zu Spieler neun passen, aber Spieler fünf geht dazwischen und erobert den Ball.",
       mv("r5", [62, 23]), ps("b1", [62.6, 23.6], delay=0.3)),
     S("Zu viert kontern", "Spieler fünf spielt sofort zu Spieler zwei. Team Rot kontert jetzt zu viert, und Spieler sieben, neun und elf sprinten gleichzeitig zurück.",
       ps("b1", [44.6, 12.6]), mv("n9", [38, 26], delay=0.2), mv("n11", [50, 20], delay=0.2), mv("n7", [48, 42], delay=0.2)),
     S("Minitor: Punkt", "Spieler zwei dribbelt nach vorn und schießt ins obere Minitor. Das gibt einen Punkt für Team Rot. Danach startet Team Rot wieder links mit Ball.",
       dr("r2", "b1", [28, 11]), ps("b1", [10.3, 17], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
