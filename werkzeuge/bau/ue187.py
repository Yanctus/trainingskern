import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 25-P5 (U12-U14, Woche 20 Phase 4): How to Press to Win Possession. 20 x 20 Yards = Feld x 30-70, y 10-50 (18 x 18 m),
# Diagonalen gestrichelt (vier Dreiecke), Hütchen an den Ecken und in der Mitte. Ausrichtung wie im PDF.
# Pink (im Video rot) -> Neon 4, 5, 11 (Nummern wie im PDF). Navy (im Video blau) -> Rot; Rot 4 -> Rot 7 (Nummer im PDF doppelt).
# Gelbe Floater -> Springer (F). Statt zwei Trainern einer. Positionen leicht auseinandergezogen (3D-Abstand).
# Wertung nach PDF: drei Pässe in einem Dreieck = Punkt (im Ton "ein Pass in jedem Dreieck"). Steigerung: Springer werden
# Außenspieler je Team (Video: Rot 9 und 8 -> Neon 2 und 3, Blau 6 und 5 -> Rot 6 und 10).
# Sichtkegel aus dem Ton der Steigerung ("ask outside players to see the space where they can take their first touch into"):
# Neon zwei schaut vor der Annahme in den Raum im Feld. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 20, 7, "T")
POS = {"n11": (40, 22), "n4": (36, 40), "n5": (53, 36), "r7": (44.5, 38), "r8": (52, 20), "r9": (62, 20),
       "f1": (26, 30), "f2": (52, 4), "f3": (74, 30), "f4": (50, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 16, 7), B("s2", 16, 10.6)]
AUSSEN = [p for p in sp(n2=(26, 24), n3=(74, 34), r10=(52, 4), r6=(50, 55)) if p["team"] != "t"]
LINES = [rect(30, 10, 40, 40), line(30, 10, 70, 50), line(70, 10, 30, 50)]
CONES = ecken(30, 10, 40, 40) + [C(50, 30)]

u = {"title": "Dreiecke halten und pressen", "code": "UE-187", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 18 m",
 "description": "Ein Ballbesitzspiel drei gegen drei mit vier Springern außen. Das Feld ist durch die Diagonalen in vier Dreiecke geteilt. Wer drei Pässe in einem Dreieck schafft, bekommt einen Punkt. Das andere Team presst gemeinsam, erobert den Ball und spielt dann selbst mit den Springern.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Hütchen an den Ecken und in der Mitte, die Diagonalen teilen das Feld in vier Dreiecke.",
  "Verteilen: Team Neon und Team Rot je zu dritt im Feld. An jeder Seite steht ein Springer außen. Der Trainer steht an der Ecke mit Bällen.",
  "Ablauf: Das Team am Ball spielt mit den Springern und versucht, drei Pässe in einem Dreieck zu schaffen. Das andere Team presst und will den Ball erobern.",
  "Wertung und Wechsel: Drei Pässe in einem Dreieck geben einen Punkt. Wer den Ball erobert, spielt sofort mit den Springern weiter. Wer nach der Spielzeit mehr Punkte hat, gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Gute Passwinkel schaffen und Dreiecke bilden", "Einer bietet sich immer außerhalb des Dreiecks an", "Schnell mit ein oder zwei Kontakten spielen", "Gemeinsam pressen und laut miteinander reden"],
 "materials": ["5 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Dreiecke halten und pressen. Team Neon will drei Pässe in einem Dreieck schaffen, Team Rot presst gemeinsam.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 40.6, 22.6)] + ERSATZ,
  "steps": [
   S("Ins linke Dreieck", "Neon elf spielt zum Springer links, und der spielt gleich weiter zu Neon vier. Rot sieben läuft Neon vier an.",
     ps("b1", [26.6, 30.6]), ps("b1", [36.6, 40.6], after=True), mv("r7", [39.5, 42.5], delay=0.6)),
   S("Dritter Pass: Punkt", "Neon fünf läuft ins Dreieck und bekommt den Ball. Das sind drei Pässe im linken Dreieck, und das gibt einen Punkt für Team Neon. Neon bleibt am Ball.",
     mv("n5", [43, 31]), ps("b1", [43.6, 31.6], delay=0.4)),
   S("Abgefangen", "Neon fünf will nach oben zum Springer spielen. Aber Rot acht liest den Pass und fängt ihn ab.",
     mv("r8", [50, 15]), ps("b1", [50.6, 15.6], delay=0.2)),
   S("Rot ist dran", "Rot acht spielt sofort zum Springer oben, der legt auf Rot neun ab. Jetzt ist Team Rot am Ball. Schafft Rot drei Pässe in einem Dreieck, gibt das einen Punkt für Team Rot.",
     ps("b1", [52.6, 4.6]), mv("r9", [58, 24]), ps("b1", [58.6, 24.6], after=True))],
  "dims": dims(30, 70, 10, 50, "18 m", "18 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Gemeinsam pressen.", "Gemeinsam pressen",
    "Die Verteidiger pressen zusammen und lassen keine großen Lücken zwischen sich. Einer läuft den Ballführenden an, die anderen rücken nach und stellen die Passwege zu. Nach der Eroberung wird sofort schnell weitergespielt.",
    sp(), [B("b1", 40.6, 22.6)] + ERSATZ,
    [S("Zusammen anlaufen", "Rot acht läuft Neon elf an. Rot sieben und Rot neun rücken nach und machen die Räume zwischen sich klein.",
       mv("r8", [45, 21]), mv("r7", [41, 33], delay=0.2), mv("r9", [52, 24], delay=0.2)),
     S("Ball erobert", "Neon elf will zu Neon fünf passen. Rot neun steht schon im Passweg und fängt den Ball ab.",
       mv("r9", [45.4, 27.8]), ps("b1", [46, 28.4], delay=0.2)),
     S("Schnell weiter", "Rot neun spielt sofort zum Springer unten. Jetzt ist Team Rot am Ball und will drei Pässe in einem Dreieck, denn das gibt einen Punkt für Team Rot.",
       ps("b1", [50.6, 55.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Außenspieler für jedes Team.", "Außenspieler rotieren",
    "Statt der Springer hat jedes Team zwei eigene Spieler außen. Bekommt ein Außenspieler den Ball, nimmt er ihn ins Feld mit, und ein Mitspieler tauscht mit ihm nach außen. Für drei Pässe in einem Dreieck gibt es einen Punkt, wer zuerst in allen vier Dreiecken drei Pässe hat, gewinnt.",
    AUSSEN,
    [B("b1", 40.6, 22.6)] + ERSATZ,
    [S("Raum sehen", "Neon zwei steht außen und schaut schon vor dem Pass ins Feld. Wo ist Platz für die erste Ballmitnahme? Dann spielt Neon elf zu ihm.",
       bl("n2", [40, 30]), ps("b1", [26.6, 24.6], after=True)),
     S("Rein und raus", "Neon zwei nimmt den Ball mit dem ersten Kontakt ins Feld. Gleichzeitig läuft Neon vier nach außen und ist jetzt Außenspieler.",
       dr("n2", "b1", [33, 27]), mv("n4", [26, 42])),
     S("Drei Pässe: Punkt", "Neon zwei spielt zu Neon vier, und Neon vier spielt zu Neon fünf ins Dreieck. Das sind drei Pässe im linken Dreieck, und das gibt einen Punkt für Team Neon. Jetzt geht es ins nächste Dreieck.",
       ps("b1", [26.6, 42.6]), mv("n5", [43, 33]), ps("b1", [43.6, 33.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
