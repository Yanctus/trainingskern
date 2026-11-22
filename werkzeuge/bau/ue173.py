import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 89-P1 (U12-U14, Woche 14 Phase 4): Possession Winning Rondo (CDM). Maße nach der PDF-Skizze 10 x 16 Yards (Text: 15 x 20, Ton:
# 15 x 10) = Feld x 34.4-65.6, y 5-55 (9 x 15 m), quer geteilt (gestrichelt bei y 30): zwei Rondos vier gegen eins, die gleichzeitig
# spielen. Pink (im Video rot) -> Neon, Gelb (im Video gold) -> Rot; N (neutral) -> Springer (team t, F). Nummern neu (im PDF doppelt):
# oben Gelb 4 -> Rot 5 (Verteidiger), Pink 6 -> Neon 6 (am Ball); unten Pink 4 -> Neon 4 (Verteidiger), Gelb 6 -> Rot 7 (am Ball).
# Steigerung ohne Springer: oben Pink 7, 8, 11 -> Neon 2, 8, 11; unten Gelb 11, 8, 7 -> Rot 9, 10, 12.
# Positionen als versetzte Raute (3D-Abstand), Spielidee wie im PDF. Ein Trainer statt zwei.
# Sichtkegel: Im Ton "read players' body shape and recognise when to press" (im Video kein Kegel eingezeichnet): bl() vom
# Verteidiger zum Passgeber (Grundform und Coaching-Punkt).
T = P("T", "c", 76, 30, "T")
POS = {"f1": (55, 7), "f2": (36.5, 19), "f3": (55, 26), "n6": (63.5, 19), "r5": (46, 18),
       "f4": (45, 34), "f5": (45, 53), "f6": (63, 42), "r7": (36.5, 43), "n4": (54, 42)}
def sp(pos=POS):
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in pos.items()] + [T]
POS2 = {{"f1": "n2", "f2": "n8", "f3": "n11", "f4": "r9", "f5": "r12", "f6": "r10"}.get(i, i): p for i, p in POS.items()}
ERSATZ = [B("s1", 77.6, 33.5), B("s2", 74, 33.5)]
BAELLE = [B("b1", 64.1, 19.6), B("b2", 37.1, 43.6)]
LINES = [rect(34.4, 5, 31.2, 50), line(34.4, 30, 65.6, 30)]

u = {"title": "Abfangen im Rondo", "code": "UE-173", "kind": "Spielform",
 "focuses": ["Verteidigen", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "9 x 15 m",
 "description": "Zwei kleine Rondos spielen gleichzeitig vier gegen eins. Der Verteidiger in der Mitte will den Ball erobern: Fängt er ihn ab und behält ihn, gibt das zwei Punkte für sein Team. Spitzelt er ihn nur ins Aus, gibt das einen Punkt. Nach jedem Ballgewinn tauschen der Verteidiger und der Gegenspieler die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 15 Metern, quer in der Mitte geteilt. So entstehen zwei kleine Felder.",
  "Verteilen: In jedem Feld drei Springer am Rand, ein Spieler am Ball und ein Verteidiger in der Mitte. Oben verteidigt Rot fünf gegen Neon sechs, unten Neon vier gegen Rot sieben. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Beide Rondos spielen gleichzeitig vier gegen eins. Die Springer spielen immer mit dem Team am Ball. Der Verteidiger lauert und presst bei einem schlechten Pass oder einer schlechten Annahme.",
  "Wertung und Wechsel: Abgefangen und behalten gibt zwei Punkte, ins Aus gespitzelt einen Punkt. Nach jedem Ballgewinn tauschen die beiden die Rollen. Das Team mit mehr Punkten nach der Spielzeit gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Mit vollem Tempo den Ball erobern wollen", "So stellen, dass der Gegner in eine Richtung spielen muss", "Schnelle Füße, immer mit dem Ball mitgehen", "Den richtigen Moment erkennen: schlechte Annahme oder schlechter Pass"],
 "materials": ["6 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Abfangen im Rondo. Zwei Rondos vier gegen eins, und der Verteidiger in der Mitte jagt den Ball.",
 "board": {"lines": LINES, "cones": [], "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Vier gegen eins", "Beide Rondos spielen gleichzeitig. Wir schauen nach oben: Neon sechs spielt zum Springer, und Rot fünf schiebt nach. Unten spielt Rot sieben zum Springer, und Neon vier schiebt genauso nach.",
     ps("b1", [55.6, 7.6]), mv("r5", [49, 13], delay=0.3), ps("b2", [45.6, 34.6]), mv("n4", [50, 39], delay=0.3)),
   S("Abgefangen", "Rot fünf liest die Körperhaltung des Springers. Der spielt einen ungenauen Pass nach links, und Rot fünf fängt den Ball ab.",
     bl("r5", [57, 4.5]), ps("b1", [49.6, 11.5], after=True), mv("r5", [49, 10.9], after=True)),
   S("Ball behalten: Punkte", "Rot fünf behält den Ball und spielt sauber zum Springer, und das gibt zwei Punkte für Team Rot. Jetzt tauschen die beiden: Neon sechs verteidigt in der Mitte, Rot fünf spielt außen.",
     ps("b1", [55.6, 26.6]), mv("n6", [47, 17], after=True), mv("r5", [63, 18], after=True))],
  "dims": dims(34.4, 65.6, 5, 55, "9 m", "15 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Abfangen zählt doppelt.", "Abfangen zählt doppelt",
    "Ein Ball ins Aus gibt nur einen Punkt. Wer den Ball sauber abfängt und behält, bekommt zwei Punkte. Darum lauert der Verteidiger auf den richtigen Moment und geht dann entschlossen drauf.",
    sp(), [B("b1", 64.1, 19.6), B("b2", 63.6, 42.6)] + ERSATZ,
    [S("Lauern", "Wir schauen nach unten. Neon vier beobachtet den Springer rechts. Der spielt zum Springer unten, und Neon vier schiebt nach.",
       bl("n4", [68, 42]), ps("b2", [45.6, 53.6], after=True), mv("n4", [49, 47], delay=0.3, after=True)),
     S("Ins Aus: Punkt", "Der Springer nimmt den Ball schlecht an. Neon vier presst sofort und spitzelt den Ball ins Aus, und das gibt einen Punkt für Team Neon. Hätte er den Ball abgefangen und behalten, gäbe es zwei Punkte.",
       mv("n4", [47, 50.5]), ps("b2", [32, 49], delay=0.4))]),
  V("Steigerung", "Und jetzt die Steigerung: Alle verteidigen.", "Alle verteidigen",
    "Jetzt gibt es keine Springer mehr. Oben spielen vier von Team Neon gegen einen von Team Rot, unten umgekehrt. Wer den Ball erobert, tauscht mit dem Spieler, der ihn verloren hat.",
    sp(POS2), BAELLE + ERSATZ,
    [S("Vier gegen eins", "Beide Rondos spielen gleichzeitig. Oben spielt Neon sechs zu Neon zwei, und Rot fünf schiebt nach. Unten spielt Rot sieben zu Rot neun.",
       ps("b1", [55.6, 7.6]), mv("r5", [49, 13], delay=0.3), ps("b2", [45.6, 34.6]), mv("n4", [50, 39], delay=0.3)),
     S("Abgefangen", "Neon zwei will zu Neon acht passen, aber Rot fünf fängt den Ball ab und behält ihn.",
       ps("b1", [49.6, 11.5]), mv("r5", [49, 10.9])),
     S("Tauschen: Punkte", "Das gibt zwei Punkte für Team Rot. Jetzt tauscht Rot fünf mit Neon zwei: Neon zwei läuft in die Mitte und verteidigt, und Rot fünf geht mit dem Ball nach außen.",
       mv("n2", [54, 15]), mv("n2", [47, 18], after=True), dr("r5", "b1", [55, 6.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
