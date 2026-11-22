import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 65-P6 (U12-U14, Woche 19 Phase 1): Timing of Forward Passes SSG (PDF: How to Penetrate the High Line to Finish).
# 25 x 35 Yards = Feld x 32.15-67.85, y 5-55 (23 x 32 m), Endzonen je 10 Yards (wie im Ton, gestrichelt), an beiden Enden zwei
# Minitore. Gespiegelt: Pink (greift im PDF nach unten an) -> Neon greift nach oben an, Gelb -> Rot. Keine Nummern im PDF:
# Neon 6-10, Rot 2-5 und 11. Positionen auf ein Spaltenraster gesetzt (3D-Abstand, fünf Spalten mit zwei Reihen), Spielidee
# wie im PDF (acht Pässe, dann Steilpass in die Endzone, Abschluss ins Minitor). Ein Trainer (rechts) statt zwei.
# Steigerung = Progression aus PDF/Ton (Ballgewinn vor acht Pässen gibt den Verteidigern einen Punkt).
# Sichtkegel: Text "See gaps early to play forward passes" / "awareness of runners", im Video kein Kegel eingezeichnet:
# Grundform bl() von Spieler sieben zur Lücke vor dem Steilpass, Coaching-Punkt bl() von Spieler acht zum Läufer (Richtung aus dem Sinn).
T = P("T", "c", 76, 30, "T")
POS = {"n6": (33.9, 39.5), "n9": (42.15, 20), "n8": (50.4, 40), "n10": (58.65, 20), "n7": (66.9, 39.5),
       "r2": (33.9, 23), "r3": (42.15, 36), "r4": (50.4, 24), "r5": (58.65, 36), "r11": (66.9, 23.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 79.6, 33.5), B("s2", 76, 33.5)]
LINES = [rect(32.15, 5, 35.7, 50), line(32.15, 19.3, 67.85, 19.3), line(32.15, 40.7, 67.85, 40.7)]
TORE = [{"x": x, "y": 5, "side": "top"} for x in (37.9, 62.1)] + [{"x": x, "y": 55, "side": "bottom"} for x in (37.9, 62.1)]

u = {"title": "Steilpass zur richtigen Zeit", "code": "UE-162", "kind": "Spielform",
 "focuses": ["Passspiel", "Bewegung", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "23 x 32 m",
 "description": "Fünf gegen fünf in der Mitte, an beiden Enden eine Endzone mit zwei Minitoren. Das Team am Ball muss erst acht Pässe spielen, dann darf ein Steilpass in die Endzone kommen. Ein Angreifer startet hinein, nimmt den Ball mit und schießt ins Minitor. Die Verteidiger dürfen nicht in die Endzone und müssen die Passwege gemeinsam zumachen.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern. An beiden Enden eine Endzone von 9 Metern, gestrichelt abgeteilt. Auf jeder Grundlinie zwei Minitore.",
  "Verteilen: Zwei Teams zu fünft in der Mitte. Team Neon greift die oberen Minitore an, Team Rot die unteren. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Nach acht Pässen darf der Steilpass in die Endzone kommen. Nur Angreifer dürfen in die Endzone laufen, Verteidiger nicht. Abschluss mit ein oder zwei Kontakten.",
  "Wertung und Wechsel: Ein Treffer ins Minitor gibt einen Punkt. Erobert das andere Team den Ball oder geht der Ball ins Aus, wechseln die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Lücken früh sehen und den Pass nach vorn spielen", "Den Steilpass genau und mit dem richtigen Tempo in den Lauf spielen", "Den Lauf richtig timen und ruhig abschließen", "Als Abwehr zusammen verschieben und Passwege zumachen"],
 "materials": ["4 Minitore", "Hütchen für Feld und Endzonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Steilpass zur richtigen Zeit. Fünf gegen fünf, und nach acht Pässen darf der Ball steil in die Endzone zum Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 34.5, 40.1)] + ERSATZ,
  "steps": [
   S("Acht Pässe", "Team Neon greift nach oben an und muss erst acht Pässe spielen. Spieler sechs passt zu Spieler acht, der weiter zu Spieler sieben. Team Rot verschiebt gemeinsam mit.",
     ps("b1", [51.0, 40.6]), ps("b1", [67.5, 40.1], after=True), mv("r3", [46, 35], delay=0.3), mv("r5", [61, 35], delay=0.6)),
   S("Lücke sehen", "Die acht Pässe sind geschafft. Spieler sieben hebt den Kopf und sieht die Lücke zwischen Spieler vier und Spieler elf. Er spielt nach vorn zu Spieler zehn.",
     bl("n7", [60, 22]), ps("b1", [59.25, 20.6], after=True)),
   S("Steil in die Zone", "Spieler neun startet in die Endzone, und Spieler zehn spielt ihm den Ball mit einem Kontakt in den Lauf. Die Verteidiger dürfen nicht hinterher in die Zone.",
     mv("n9", [47, 12]), ps("b1", [47.6, 12.6], delay=0.4)),
   S("Abschluss: Punkt", "Spieler neun nimmt den Ball mit und schießt ins linke Minitor, und das gibt einen Punkt für Team Neon. Dann wechseln die Rollen, der Trainer bringt einen neuen Ball, und Team Rot greift nach unten an.",
     dr("n9", "b1", [44.5, 10]), ps("b1", [37.9, 5.3], after=True))],
  "dims": dims(32.15, 67.85, 5, 55, "23 m", "32 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Lauf richtig timen.", "Lauf richtig timen",
    "Der Läufer startet nicht zu früh, sondern genau dann, wenn der Passgeber den Kopf hebt und ihn sieht. Der Pass kommt scharf und genau in den Lauf. Der erste Kontakt geht nach vorn, dann schießt der Läufer ruhig ins Minitor.",
    sp(), [B("b1", 51.0, 40.6)] + ERSATZ,
    [S("Kopf hoch", "Spieler acht hat den Ball und hebt den Kopf. Er sieht Spieler neun, der kurz entgegenkommt und seinen Gegner weglockt.",
       bl("n8", [44, 24]), mv("n9", [40, 25], delay=0.2)),
     S("Jetzt starten", "Genau jetzt startet Spieler neun in die Endzone. Spieler acht spielt ihm den Ball scharf in den Lauf.",
       mv("n9", [44, 12]), ps("b1", [44.6, 12.6], delay=0.4)),
     S("Ruhig ins Tor: Punkt", "Spieler neun nimmt den Ball nach vorn mit und schießt ruhig ins linke Minitor. Das gibt einen Punkt für Team Neon.",
       dr("n9", "b1", [42, 9]), ps("b1", [37.9, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein schneller Ballgewinn gibt einen Punkt für die Verteidiger.", "Hoch pressen",
    "Erobert Team Rot den Ball, bevor Team Neon acht Pässe geschafft hat, gibt das einen Punkt für Team Rot. Darum pressen die Verteidiger jetzt höher. Dadurch wird aber hinten Platz frei, den die Angreifer nutzen können.",
    sp(), [B("b1", 34.5, 40.1)] + ERSATZ,
    [S("Hoch pressen", "Spieler sechs passt zu Spieler acht. Sofort rücken Spieler vier und Spieler fünf heraus und pressen.",
       ps("b1", [51.0, 40.6]), mv("r4", [50.4, 32], delay=0.3), mv("r5", [57, 37], delay=0.3)),
     S("Ballgewinn: Punkt", "Spieler acht will zu Spieler sieben passen, aber Spieler fünf fängt den Ball ab. Das waren keine acht Pässe, und das gibt einen Punkt für Team Rot. Jetzt greift Team Rot an.",
       mv("r5", [59, 40]), ps("b1", [59.6, 40.6], delay=0.4))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
