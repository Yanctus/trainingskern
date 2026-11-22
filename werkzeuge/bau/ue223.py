import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-36 (U12-U14, Woche 33 Phase 2): Scanning and Dribbling Warm Up. 15 x 20 Yards = Feld x 31.25-68.75, y 5-55 (14 x 18 m).
# Gedreht (180 Grad): im PDF steht der Trainer oben und die Minitore unten; hier Minitore oben, Trainer unten. Die beiden
# schrägen Ecktore als gerade Minitore oben links und rechts. Zwei Puppen als Stangen, ein Hütchen als Startmarke.
# Pink (Angreifer) -> Team Neon 4 (aktiv), 7, 8, 9 (wartend); Blau (Verteidiger) -> Team Rot, neu nummeriert (im Video doppelte
# 4): 6 (aktiv), 2, 3, 5 (wartend). Wartende in einer Reihe neben dem Feld (3D-Abstand), Verteidiger startet leicht versetzt.
# Wertung: Treffer = Punkt für den Angreifer (ergänzt, im Original nur "finish").
# Sichtkegel aus Text, Ton und Video ("scan to see defenders position", "check their shoulders"): Spieler vier schaut vor der
# Annahme über die Schulter zum Verteidiger hinter ihm (im PDF/Video als Kegel eingezeichnet, Richtung zum Verteidiger).
# Steigerung (Doppelpass): Spieler sieben steht als Anspieler am Ende neben dem Trainer.
T = P("T", "c", 50, 51.5, "T")
POS = {"n4": (50, 24), "r6": (41.5, 13), "n7": (76, 30), "n8": (84.5, 30), "n9": (93, 30),
       "r2": (24, 30), "r3": (15.5, 30), "r5": (7, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 53.5), B("s2", 46, 53.5)]
LINES = [rect(31.25, 5, 37.5, 50)]
TORE = [{"x": x, "y": 5, "side": "top"} for x in (37, 50, 63)]
CONES = [C(43.75, 39, shape="stange"), C(56.25, 39, shape="stange"), C(50, 19)]

u = {"title": "Schulterblick und losdribbeln", "code": "UE-223", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Dribbling", "Erwärmung"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 8, "field_size": "14 x 18 m",
 "description": "Ein Aufwärmspiel für den Schulterblick. Ein Angreifer läuft dem Trainer entgegen, ein Verteidiger läuft eng hinterher. Vor der Annahme schaut der Angreifer über die Schulter, nimmt den Ball weg vom Verteidiger um die andere Puppe mit und schießt in ein Minitor. Danach wird der Verteidiger zum Angreifer.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. Oben drei Minitore, in der Mitte zwei Puppen oder Stangen nebeneinander, darunter ein Hütchen als Start.",
  "Verteilen: Team Neon wartet rechts, Team Rot links neben dem Feld. Ein Angreifer und ein Verteidiger sind im Feld. Der Trainer steht unten im Feld mit Bällen.",
  "Ablauf: Der Angreifer läuft dem Trainer entgegen, der Verteidiger bleibt eng dran, greift aber nicht an. Der Angreifer schaut über die Schulter, nimmt den Ball um die andere Puppe mit und schießt in ein Minitor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für den Angreifer. Dann wird der Verteidiger zum Angreifer, und ein neuer Spieler aus dem anderen Team verteidigt."],
 "organisation_show": ORG,
 "coaching_points": ["Kurz über die Schulter schauen, wo der Verteidiger steht", "Den Körper früh öffnen, damit du alles siehst", "Mit dem ersten Kontakt um die Puppe, weg vom Gegner", "Den Ball eng führen und genau ins Minitor schießen"],
 "materials": ["3 Minitore", "2 Puppen oder Stangen", "1 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Schulterblick und losdribbeln. Erst schauen, wo der Verteidiger ist, dann mit dem Ball weg von ihm und ab ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 52.1)] + ERSATZ,
  "steps": [
   S("Anbieten", "Spieler vier läuft dem Trainer entgegen. Spieler sechs läuft eng hinterher. Er bleibt dicht dran, greift aber nicht an.",
     mv("n4", [50, 36]), mv("r6", [45, 29], delay=0.3)),
   S("Schulterblick", "Bevor der Ball kommt, schaut Spieler vier über die Schulter. Er sieht: Spieler sechs kommt von links. Dann spielt ihm der Trainer den Ball.",
     bl("n4", [40, 22]), ps("b1", [50.6, 36.6], after=True)),
   S("Weg vom Gegner", "Spieler vier nimmt den Ball mit dem ersten Kontakt nach rechts mit, weg von Spieler sechs. Er dribbelt um die rechte Puppe herum.",
     dr("n4", "b1", [55, 45]), dr("n4", "b1", [62, 42], after=True), dr("n4", "b1", [62, 26], after=True), mv("r6", [53, 31], delay=0.5)),
   S("Abschluss: Punkt", "Spieler vier schießt ins rechte Minitor, und das gibt einen Punkt für Spieler vier. Dann ist Spieler sechs der Angreifer, und Spieler sieben aus Team Neon wird der neue Verteidiger.",
     ps("b1", [63, 5.3]), mv("r6", [57, 24], delay=0.2))],
  "dims": dims(31.25, 68.75, 5, 55, "14 m", "18 m", rx=72)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst schauen, dann entscheiden.", "Erst schauen, dann drehen",
    "Der Verteidiger kommt nicht immer von derselben Seite. Nur wer vor der Annahme über die Schulter schaut, weiß, wohin der erste Kontakt gehen muss. Wer nicht schaut, dreht oft genau in den Gegner hinein.",
    sp(r6=(58.5, 13)), [B("b1", 50.6, 52.1)] + ERSATZ,
    [S("Wo ist der Gegner?", "Diesmal kommt Spieler sechs von rechts. Spieler vier läuft dem Trainer entgegen, schaut über die Schulter und sieht ihn rechts hinter sich. Dann kommt der Ball.",
       mv("n4", [50, 36]), mv("r6", [55, 29], delay=0.3), bl("n4", [60, 22], after=True), ps("b1", [50.6, 36.6], after=True)),
     S("Links herum: Punkt", "Also nimmt Spieler vier den Ball nach links mit, um die linke Puppe herum, und schießt ins linke Minitor. Das gibt einen Punkt für Spieler vier.",
       dr("n4", "b1", [45, 45]), dr("n4", "b1", [38, 42], after=True), dr("n4", "b1", [38, 26], after=True), ps("b1", [37, 5.3], after=True),
       mv("r6", [47, 31], delay=0.5))]),
  V("Steigerung", "Und jetzt die Steigerung: Doppelpass mit dem Spieler am Ende.", "Mit Doppelpass",
    "Jetzt spielt ein Mitspieler am Ende den Ball. Der Angreifer lässt ihn zurückprallen, setzt sich ab und schaut dabei über die Schulter. Den Rückpass nimmt er mit dem ersten Kontakt weg vom Verteidiger und schießt in ein beliebiges Minitor.",
    sp(n7=(40, 51.5)), [B("b1", 40.6, 52.1)] + ERSATZ,
    [S("Doppelpass", "Spieler vier läuft dem Ball entgegen, Spieler sechs bleibt dicht dran. Spieler sieben spielt zu Spieler vier, und der lässt den Ball direkt zurückprallen.",
       mv("n4", [50, 40]), mv("r6", [45, 32], delay=0.3), ps("b1", [50.6, 40.6], after=True), ps("b1", [40.6, 52.1], after=True)),
     S("Absetzen und schauen", "Spieler vier setzt sich nach rechts ab und schaut über die Schulter: Spieler sechs steht links. Dann spielt Spieler sieben den Ball in den Lauf.",
       mv("n4", [54, 35]), bl("n4", [38, 30], after=True), ps("b1", [54.6, 35.6], after=True)),
     S("Erster Kontakt weg: Punkt", "Spieler vier nimmt den Ball mit dem ersten Kontakt weg vom Gegner, dribbelt los und schießt ins rechte Minitor. Das gibt einen Punkt für Spieler vier.",
       dr("n4", "b1", [61, 26]), ps("b1", [63, 5.3], after=True), mv("r6", [52, 30], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
