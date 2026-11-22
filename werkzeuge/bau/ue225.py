import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P3 (U12-U14, Woche 34 Phase 5): Defending Crosses (Technical Defending). 45 x 35 Yards = Feld x 14-86, y 4-56 (41 x 32 m),
# quer wie im Video (im PDF hochkant gedreht), in zwei Hälften geteilt (Mittellinie x 50 gestrichelt).
# Abweichung: Im Video stehen die zwei Minitore Rücken an Rücken oben in der Mitte (Öffnung nach links und rechts); hier steht in
# jeder Hälfte ein Minitor oben, etwas zur Mitte hin, mit Öffnung ins Feld (so fliegt auch kein Ball in die andere Hälfte, wie im Ton
# empfohlen). Koordinationsleitern waagrecht zur Mitte hin, Puppen als Stangen. Ein Trainer statt zwei (links mit Bällen).
# Pink/rot (Verteidiger) -> Team Neon 5, 2 (links) und 6, 3 (rechts), Nummern wie im Video. Orange (Angreifer) -> Team Rot:
# Flügel 11 und 7, Mittelfeld 8, 4 (links) und 10, 6 -> Rot 9 (rechts, neu nummeriert wegen Neon 6). Die wartenden Flügelspieler
# (im Video 3 und 2 außen) nur im Text. Wertung ergänzt (im Original keine): Abwehr = Punkt für Team Neon, Treffer = Punkt für Rot.
# Sichtkegel aus dem PDF ("Keep your head up to recognise the crosser's position and body shape"): im Coaching-Punkt schaut Spieler
# fünf beim Zurücksprinten zum Flankengeber (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
# Leitern als Leiter gezeichnet (22.11.2026).
T = P("T", "c", 7, 50, "T")
POS = {"n5": (24, 28), "n2": (45.8, 12), "r11": (22, 45), "r4": (32, 52), "r8": (41, 52),
       "n6": (76, 28), "n3": (54.2, 12), "r7": (78, 45), "r9": (68, 52), "r10": (59, 52)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 7.6, 53.5), B("s2", 4, 53.5)]
def baelle(b8=(41.6, 52.6), b10=(59.6, 52.6)):
    return [B("b8", *b8), B("b10", *b10), B("b4", 32.6, 52.6), B("b9", 68.6, 52.6)] + ERSATZ
LINES = [rect(14, 4, 72, 52), line(50, 4, 50, 56)]
CONES = ecken(14, 4, 72, 52) + [C(50, 4), C(50, 56)] \
      + [leiter(34, 28), leiter(66, 28)] \
      + [C(22, 33, "neon", shape="stange"), C(78, 33, "neon", shape="stange")]
TORE = [{"x": 38, "y": 4, "side": "top"}, {"x": 62, "y": 4, "side": "top"}]

u = {"title": "Leiter, Sprint, Flanke abwehren", "code": "UE-225", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "41 x 32 m",
 "description": "Ein Verteidiger läuft durch die Koordinationsleiter und spielt einen Doppelpass mit dem Mittelfeldspieler. Der spielt sofort einen langen Ball nach außen zum Flügelspieler. Der Verteidiger dreht um und sprintet vor das Minitor, denn gleich kommt die flache Flanke. Blockt er sie, gibt das einen Punkt für Team Neon.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 32 Metern, in der Mitte geteilt. In jeder Hälfte oben ein Minitor, in der Mitte eine Koordinationsleiter und außen eine Puppe oder Stange.",
  "Verteilen: In jeder Hälfte zwei Verteidiger von Team Neon und vier Angreifer von Team Rot: zwei Mittelfeldspieler unten mit Bällen und zwei Flügelspieler an der Puppe. Der Trainer steht links mit Bällen.",
  "Ablauf: Der Verteidiger läuft durch die Leiter und spielt einen Doppelpass. Der Flügelspieler täuscht an der Puppe an und startet nach außen. Der lange Ball kommt zu ihm, und er flankt flach aufs Minitor. Der Verteidiger sprintet zurück und blockt.",
  "Wertung und Wechsel: Blockt der Verteidiger die Flanke, gibt das einen Punkt für Team Neon. Trifft die Flanke ins Minitor, gibt das einen Punkt für Team Rot. Danach sind der nächste Verteidiger und die nächsten Angreifer dran."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell zurück vor das Minitor, um die Flanke abzuwehren", "Den langen Ball genau und mit dem richtigen Tempo nach außen spielen", "Schnell annehmen und sofort flanken, damit der Verteidiger kaum Zeit hat", "Mit schnellen, kleinen Schritten durch die Leiter"],
 "materials": ["2 Minitore", "2 Koordinationsleitern", "2 Stangen oder Puppen", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": False,
 "say_intro": "Leiter, Sprint, Flanke abwehren. Der Verteidiger muss nach der Leiter schnell zurück vor sein Minitor.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": baelle(),
  "steps": [
   S("Durch die Leiter", "Spieler fünf läuft mit schnellen Füßen durch die Leiter. Gleichzeitig täuscht Spieler elf an der Puppe an und startet nach außen.",
     mv("n5", [43.5, 28]), mv("r11", [21, 38]), mv("r11", [15, 40], after=True)),
   S("Doppelpass", "Spieler acht spielt zu Spieler fünf, und Spieler fünf spielt den Ball direkt zurück.",
     ps("b8", [44.1, 28.6]), ps("b8", [41.6, 52.6], after=True)),
   S("Langer Ball nach außen", "Jetzt spielt Spieler acht einen langen Ball nach außen. Spieler elf sprintet hin und nimmt ihn an. Spieler fünf dreht sofort um und sprintet zurück vor das Minitor.",
     ps("b8", [16.6, 12.6], bend=-6), mv("r11", [16, 12]), mv("n5", [37.5, 9], delay=0.3)),
   S("Flanke geblockt: Punkt", "Spieler elf flankt flach aufs Minitor. Spieler fünf steht schon davor und blockt den Ball, und das gibt einen Punkt für Team Neon. Trifft die Flanke, gibt das einen Punkt für Team Rot. Dann ist Spieler zwei dran.",
     ps("b8", [38.1, 9.6]))],
  "dims": dims(14, 86, 4, 56, "41 m", "32 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Beim Zurücklaufen den Kopf heben.", "Kopf hoch beim Zurücklaufen",
    "Der Verteidiger schaut beim Zurücksprinten zum Flankengeber. So sieht er, wo der Ball herkommt und wie der Gegner steht. Dann stellt er seine Füße schnell ein und blockt die Flanke.",
    sp(n5=(43.5, 28), r11=(16, 12)), baelle(b8=(16.6, 12.6)),
    [S("Zurück und schauen", "Spieler elf hat den langen Ball angenommen. Spieler fünf sprintet zurück und schaut dabei zu Spieler elf.",
       mv("n5", [39, 17]), bl("n5", [17, 13], after=True)),
     S("Füße einstellen: Punkt", "Spieler fünf stellt sich schnell vor das Minitor. Spieler elf flankt flach, aber Spieler fünf blockt den Ball. Das gibt einen Punkt für Team Neon.",
       mv("n5", [37.5, 9]), ps("b8", [38.1, 9.6], delay=0.5))]),
  V("Steigerung", "Und jetzt die Steigerung: Beide Seiten gleichzeitig.", "Beide Seiten gleichzeitig",
    "Jetzt laufen beide Hälften gleichzeitig. Links und rechts startet je ein Verteidiger durch die Leiter. Jeder muss sein eigenes Minitor schützen, und keine Seite darf zu spät sein.",
    sp(), baelle(),
    [S("Beide in die Leiter", "Spieler fünf und Spieler sechs laufen gleichzeitig durch ihre Leitern. Spieler elf und Spieler sieben starten nach außen. Dann gibt es auf beiden Seiten einen Doppelpass.",
       mv("n5", [43.5, 28]), mv("n6", [56.5, 28]), mv("r11", [21, 38]), mv("r7", [79, 38]),
       mv("r11", [15, 40], after=True), mv("r7", [85, 40], after=True),
       ps("b8", [44.1, 28.6], after=True), ps("b10", [57.1, 28.6], after=True), ps("b8", [41.6, 52.6], after=True), ps("b10", [59.6, 52.6], after=True)),
     S("Lange Bälle", "Spieler acht und Spieler zehn spielen gleichzeitig lang nach außen. Spieler fünf und Spieler sechs sprinten zurück vor ihr Minitor.",
       ps("b8", [16.6, 12.6], bend=-6), ps("b10", [84.6, 12.6], bend=6), mv("r11", [16, 12]), mv("r7", [84, 12]),
       mv("n5", [37.5, 9], delay=0.3), mv("n6", [62.5, 9], delay=0.3)),
     S("Beide geblockt: Punkte", "Beide Flügelspieler flanken flach. Spieler fünf und Spieler sechs blocken die Flanken, und das gibt zwei Punkte für Team Neon.",
       ps("b8", [38.1, 9.6]), ps("b10", [63.1, 9.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
