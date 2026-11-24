import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 97-P5 (U15-U17, Woche 31 Phase 1): Playing Out from the Back (4231), Build Up Play. 24 x 30 Yards = 22 x 27 m, gerundet
# 20 x 25 m. Ausrichtung wie im PDF (Team Neon baut von unten nach oben auf). Kein langes Feld (Verhältnis 1,25), daher hochkant;
# das Feld ist in der Breite gestreckt gezeichnet (x 20-77, y 6-52), sonst verdecken sich die zwölf Figuren in 3D. Die Spieler
# stehen dafür auf einem Spaltenraster, grob wie in der Skizze (Innenverteidiger 6 etwas weiter links).
# Drei Zonen wie im PDF (gestrichelt): unten die Aufbauzone, in der Mitte die schmale Zone der zwei Mittelfeldspieler, oben die
# Zone des pressenden Sechsers. Die Zielspieler stehen hinter den Grundlinien.
# Pink -> Team Neon, Nummern wie im PDF (Kette 3, 6, 5, 2, Mittelfeld 10 und 8, Zielspieler 9 oben).
# Blau -> Team Rot: 7 und 11 bleiben; neu nummeriert, weil die Nummern doppelt sind: Blau 8 -> 4, Blau 9 -> 12, Blau 10 -> 13.
# Ein Trainer statt zwei, rechts neben dem Feld.
# Grundform nach PDF und Video (0:06-0:22): 5 -> 2 -> 6 -> 3, Spieler 10 geht nach außen und bekommt den Ball, Spieler 4 presst,
# Pass auf den Zielspieler 9, Ablage auf Spieler 8, der über die Grundlinie dribbelt. Konter von Team Rot (Video 0:28-0:45:
# Ballgewinn, über den eigenen Zielspieler, über die andere Grundlinie dribbeln) und der schnelle Neustart des Trainers stehen
# nur im Text.
# Fassungen = PDF-Progressionen: 1 Steilpass durch die Mitte zählt (Verteidiger punkten nach zwei verhinderten Angriffen),
# 2 Spieler 4 darf im Aufbau mitpressen (vier gegen vier), zwei Spieler von Team Rot dürfen zurücklaufen.
# Sichtkegel aus PDF und Ton („find free player“, „identify and exploit this space“), im Video nicht eingezeichnet:
# Grundform Spieler 3 schaut zum freien Spieler 10; der schaut zum Passgeber, nimmt an, und der Kegel schwenkt zum Zielspieler
# (bl mit von), dazu der Drehpfeil. Fassung 1 Spieler 6 sieht die Lücke in der Mitte, Fassung 2 sieht er den freien Raum
# hinter dem pressenden Spieler 4.
T = P("T", "c", 84, 46, "T")
ERSATZ = [B("s1", 87.5, 46.6), B("s2", 87.5, 50)]
POS = {"n9": (40, 3.5), "n10": (40, 23), "n8": (57, 24), "n3": (23, 40), "n2": (74, 39), "n6": (31.5, 48), "n5": (57, 48),
       "r4": (48.5, 15.5), "r7": (31.5, 32.3), "r11": (65.5, 32.5), "r12": (48.5, 38.5), "r13": (40, 54.8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(20, 6, 57, 46), line(20, 19.5, 77, 19.5), line(20, 26.1, 77, 26.1)]
BAELLE = [B("b1", 57.6, 48.6)] + ERSATZ
DIMS = dims(20, 77, 6, 52, "20 m", "25 m", rx=93)
AUSSEN10 = [28, 23.5]   # Spieler zehn geht nach außen
def kreisen():
    return [ps("b1", fuss(POS["n2"])), mv("r11", [70, 35], delay=0.3), ps("b1", fuss(POS["n6"]), after=True), mv("r12", [46, 41.5], delay=1.0)]

u = {"title": "Aufbau mit Ablage der Spitze", "code": "UE-389", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 14,
 "field_size": "20 x 25 m",
 "description": "Eine Viererkette von Team Neon baut gegen drei Angreifer von Team Rot auf. Der Ball soll zu einem der zwei Mittelfeldspieler in der mittleren Zone. Von dort geht er auf die Spitze hinter der Grundlinie, die für den anderen Mittelfeldspieler ablegt. Der dribbelt über die Grundlinie, und das gibt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 20 mal 25 Metern, in drei Zonen geteilt. Unten die große Aufbauzone, in der Mitte eine schmale Zone, oben die letzte Zone. Hinter jeder Grundlinie steht ein Zielspieler.",
  "Verteilen: Team Neon mit Viererkette unten und zwei Mittelfeldspielern in der mittleren Zone, Spieler neun als Zielspieler oben. Team Rot presst mit drei Angreifern, Spieler vier wartet in der oberen Zone, Spieler dreizehn steht als Zielspieler unten. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Die Kette lässt den Ball laufen und spielt einen Mittelfeldspieler frei. Erst dann darf Spieler vier pressen. Der Ball geht auf die Spitze, sie legt für den anderen Mittelfeldspieler ab, und der dribbelt über die obere Grundlinie.",
  "Wertung: Das Dribbling über die Grundlinie gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, spielt es über seinen Zielspieler und dribbelt in sechs Sekunden über die untere Grundlinie, das gibt einen Punkt für Team Rot. Danach spielt der Trainer sofort den nächsten Ball. Die Zielspieler wechseln alle paar Runden."],
 "organisation_show": ORG,
 "coaching_points": ["Breit und tief stehen, dann gehen Lücken auf", "Locken, dann durch die Linie spielen", "Bewegen, damit du anspielbar bist", "Schnell kombinieren mit der Spitze"],
 "materials": ["Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau mit Ablage der Spitze. Die Viererkette spielt sich gegen drei Angreifer heraus, und über die Spitze geht es mit Ball über die Grundlinie.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": BAELLE,
  "steps": [
   S("Ball laufen lassen", "Die Kette lässt den Ball laufen. Spieler fünf spielt raus zu Spieler zwei, und der spielt gleich zurück in die Mitte zu Spieler sechs. Team Rot muss hinterher.",
     *kreisen()),
   S("Zehn geht raus, Pass nach außen", "Spieler zehn geht nach außen. Spieler sechs spielt zu Spieler drei. Der sieht Spieler zehn frei und spielt ihn an.",
     mv("n10", AUSSEN10), ps("b1", fuss(POS["n3"]), delay=0.3), bl("n3", AUSSEN10, after=True), bl("n10", [24.5, 34], after=True), ps("b1", fuss(AUSSEN10), after=True)),
   S("Auf die Spitze, Ablage", "Jetzt darf Spieler vier pressen. Spieler zehn dreht schnell auf und spielt hoch zu Spieler neun. Spieler acht startet, und Spieler neun legt ihm den Ball direkt in den Lauf.",
     mv("r4", [35, 21]), bl("n10", [36.5, 8.5], von=[24.5, 34], dauer=1.3), drehen("n10", [36.5, 8.5], delay=0.4),
     ps("b1", fuss(POS["n9"]), after=True), mv("n8", [49, 12], delay=0.6), ps("b1", [49.6, 12.6], after=True)),
   S("Über die Grundlinie: Punkt", "Spieler acht nimmt den Ball mit und dribbelt über die Grundlinie. Das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Spieler fünf.",
     dr("n8", "b1", [55, 3.5]))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Steilpass durch die Mitte gibt schon einen Punkt.", "Steilpass zählt als Punkt",
    "Geht ein flacher Pass durch die Linie der drei Angreifer auf einen Mittelfeldspieler, gibt das sofort einen Punkt. Schafft Team Rot es zweimal hintereinander, dass kein Pass durchgeht, gibt das einen Punkt für Team Rot. Die Angreifer machen die Mitte zu, also geht der Ball öfter über außen.",
    sp(), BAELLE,
    [S("Ball laufen lassen", "Spieler fünf spielt raus zu Spieler zwei. Der spielt zurück auf Spieler sechs, und Team Rot schiebt hinterher.",
       *kreisen()),
     S("Durch die Linie: Punkt", "Spieler sechs schaut hoch und sieht die Lücke zwischen Spieler sieben und Spieler zwölf. Flach und scharf geht der Ball durch auf Spieler acht. Das gibt einen Punkt für Team Neon.",
       bl("n6", [44, 34]), ps("b1", fuss(POS["n8"]), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Spieler vier darf schon im Aufbau mitpressen.", "Spieler vier presst mit",
    "Jetzt darf Spieler vier schon im Aufbau mitpressen, unten ist es vier gegen vier. Dafür ist hinter ihm Platz. Wer den Raum sieht und schnell spielt, kommt durch. Wird Team Rot überspielt, dürfen zwei Spieler zurücklaufen.",
    sp(), BAELLE,
    [S("Spieler vier presst mit", "Spieler fünf spielt quer zu Spieler sechs. Sofort kommt Spieler vier aus seiner Zone und läuft ihn an.",
       ps("b1", fuss(POS["n6"])), mv("r4", [47, 30], delay=0.3), mv("r4", [31, 40.5], after=True), mv("r12", [44, 42], delay=0.4)),
     S("Raum hinter vier erkennen", "Hinter Spieler vier ist jetzt alles frei. Spieler acht geht in den Raum, und Spieler sechs sieht ihn. Der Ball geht flach durch die Mitte.",
       mv("n8", [50, 21]), bl("n6", [44, 33], delay=0.3), ps("b1", [50.6, 21.6], after=True)),
     S("Zurücklaufen hilft nicht: Punkt", "Spieler vier und Spieler zwölf laufen zurück, aber zu spät. Spieler acht spielt auf Spieler neun und bekommt die Ablage in den Lauf. Er dribbelt über die Grundlinie, und das gibt einen Punkt für Team Neon.",
       mv("r4", [44, 26]), mv("r12", [48, 30], delay=0.2), ps("b1", fuss(POS["n9"]), delay=0.2), mv("n8", [52, 10], delay=0.4),
       ps("b1", [52.6, 10.6], after=True), dr("n8", "b1", [56, 3.5], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
