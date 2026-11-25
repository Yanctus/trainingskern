import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 94-P5 (U15-U17, Woche 24 Phase 6): One Touch - Two Touch Game (Possession). 30 x 35 Yards = 27 x 32 m (gerundet 25 x 30 m).
# Feld x 26-74, y 5-55 (in der Breite leicht gestreckt, damit zehn Spieler den 3D-Abstand halten). Nicht gedreht.
# Vier Eckhütchen wie im PDF (dort rot, hier orange). Ein Trainer statt zwei, links neben dem Feld mit Bällen.
# Blau (beginnt mit Ball) -> Team Neon mit den Nummern aus PDF und Video (2, 4, 5, 8, 9).
# Pink/rot -> Team Rot, neu nummeriert (Nummern doppelt): 4 -> 6, 5 -> 7, 8 -> 10, 9 -> 11; 3 bleibt.
# Positionen grob wie im PDF, für den 3D-Abstand in drei Reihen geordnet; Spieler zehn steht oben am Rand (sonst läuft der
# erste Pass durch ihn), Spieler sieben unten (sonst steht er zwischen Spieler vier und Spieler acht).
# Ablauf nach PDF und Video: Eröffnung, dann im Wechsel ein Kontakt, zwei Kontakte. Im Video nimmt der Direktspieler einen
# zweiten Kontakt und der Ball geht ans andere Team; hier passiert das Spieler acht. Keine Punkte im Original: Wertung als
# Ballbesitz-Wechsel (Ziel: den Ball in der Reihenfolge halten), nichts ergänzt.
# Fassungen: Coaching-Punkt aus PDF Key Coaching Point 2 und Video („Provide support in possession, create effective passing
# angles“, Team Rot nach dem Ballwechsel), Steigerung aus PDF Key Coaching Point 2 (Reihenfolge ändern: zwei, zwei, eins).
# Sichtkegel aus dem Text („Constant scanning for options and available space“), im Video nicht eingezeichnet, Richtung aus dem
# Sinn: Spieler neun schaut vor dem Direktpass zu Spieler vier (Grundform); Spieler sechs schaut vor dem Pass zum freien
# Spieler elf (Coaching-Punkt).
T = P("T", "c", 16, 20, "T")  # links neben dem Feld
ERSATZ = [B("s1", 16.6, 23.6), B("s2", 19.1, 23.6)]
POS = {"n9": (33, 12), "r10": (49, 7), "n2": (59.5, 12), "r3": (69, 12),
       "r6": (40, 28), "n5": (62, 28),
       "n4": (32, 44), "r7": (42, 50), "n8": (52, 44), "r11": (63, 44.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fu(i): x, y = POS[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(26, 5, 48, 50)]
CONES = ecken(26, 5, 48, 50)
DIMS = dims(26, 74, 5, 55, "25 m", "30 m")

u = {"title": "Direkt, dann zwei Kontakte", "code": "UE-367", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "25 x 30 m",
 "description": "Fünf gegen fünf auf Ballbesitz in einem Feld von 25 mal 30 Metern. Das Team am Ball muss eine feste Reihenfolge spielen: ein Pass direkt, der nächste mit zwei Kontakten, dann wieder direkt. Wer einen Kontakt zu viel nimmt oder den Ball verliert, gibt ihn sofort ab. Dann spielt das andere Team in derselben Reihenfolge.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit vier Hütchen an den Ecken.",
  "Verteilen: Zwei Teams mit je fünf Spielern, alle im Feld verteilt. Team Neon beginnt mit Ball. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der erste Pass startet das Spiel. Danach gilt die Reihenfolge: direkt, zwei Kontakte, direkt, zwei Kontakte. Team Rot versucht, den Ball zu erobern.",
  "Wechsel: Ein Kontakt zu viel oder ein Ballverlust, und der Ball gehört dem anderen Team. Das spielt sofort in derselben Reihenfolge weiter. Geht der Ball ins Aus, spielt der Trainer einen neuen Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Vor dem Pass schauen, wo der Nächste steht", "Schräg anbieten, nicht hinter dem Gegner verstecken", "Mitzählen: Wer muss jetzt direkt spielen?", "Ball weg? Sofort nachsetzen"],
 "materials": ["4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Direkt, dann zwei Kontakte. Fünf gegen fünf auf Ballbesitz. Das Team am Ball spielt eine feste Reihenfolge, und wer sich verzählt, gibt den Ball ab.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 60.1, 12.6)] + ERSATZ,
  "steps": [
   S("Eröffnung, Spieler neun direkt", "Spieler zwei eröffnet zu Spieler neun. Der muss direkt spielen, also schaut er schon vorher, wo Spieler vier steht. Der Ball geht sofort weiter.",
     bl("n9", [32.5, 32]), ps("b1", fu("n9"), after=True), mv("r10", [40, 9], delay=0.3), ps("b1", fu("n4"), after=True)),
   S("Spieler vier hat zwei Kontakte", "Jetzt darf Spieler vier annehmen. Erster Kontakt zur Seite, mit dem zweiten spielt er zu Spieler acht. Spieler sieben läuft ihn an, kommt aber zu spät.",
     dr("n4", "b1", [35, 44]), mv("r7", [36, 48.5], delay=0.2), ps("b1", fu("n8"), after=True)),
   S("Ein Kontakt zu viel: Ballwechsel", "Spieler acht müsste direkt spielen. Er stoppt den Ball aber erst. Ein Kontakt zu viel, also gehört der Ball jetzt Team Rot. Spieler elf geht dazwischen und nimmt ihn mit. Ab jetzt spielt Team Rot in derselben Reihenfolge.",
     dr("n8", "b1", [53.5, 42.5]), mv("r11", [54.5, 41.5], delay=0.6), dr("r11", "b1", [58, 37], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Anbieten, und zwar schräg.", "Schräg anbieten",
    "Der Ballführer braucht immer zwei, drei Anspielstationen. Wer hinter einem Gegner steht, ist nicht anspielbar. Also in die Lücke laufen, schräg zum Ball und mit Abstand zum Mitspieler. Der Ballführer hebt den Kopf und sucht den freien Mann.",
    sp(), [B("b1", 40.6, 28.6)] + ERSATZ,
    [S("Drei laufen sich frei", "Team Rot hat den Ball, Spieler sechs führt ihn. Sofort laufen sich drei Mitspieler in die Lücken zwischen den Gegnern. So hat er drei Möglichkeiten.",
       mv("r10", [46, 16]), mv("r11", [57, 38]), mv("r7", [33.5, 36], delay=0.2),
       opt("r6", [46.6, 16.6], after=True), opt("r6", [57.6, 38.6]), opt("r6", [34.1, 36.6])),
     S("Pass in den freien Winkel", "Spieler sechs hebt den Kopf und sieht Spieler elf frei. Er hat zwei Kontakte und spielt zu ihm. Spieler elf muss direkt spielen, und Spieler sieben steht schon bereit.",
       bl("r6", [57, 38]), ps("b1", [57.6, 38.6], after=True), ps("b1", [34.1, 36.6], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Eine neue Reihenfolge.", "Zwei, zwei, dann direkt",
    "Der Trainer ändert die Reihenfolge. Jetzt heißt es zwei Kontakte, zwei Kontakte, ein Kontakt, und dann wieder von vorn. Alle müssen mitzählen, auch die Spieler ohne Ball.",
    sp(), [B("b1", 60.1, 12.6)] + ERSATZ,
    [S("Zweimal zwei Kontakte", "Spieler zwei nimmt den Ball mit und spielt zu Spieler fünf. Auch der hat zwei Kontakte. Annehmen, weiter zu Spieler acht.",
       dr("n2", "b1", [60.5, 16]), ps("b1", fu("n5"), after=True), dr("n5", "b1", [60, 31.5], after=True), ps("b1", fu("n8"), after=True)),
     S("Dann direkt, und von vorn", "Spieler acht ist der Dritte und spielt direkt zu Spieler vier. Danach beginnt die Reihe von vorn, Spieler vier hat also wieder zwei Kontakte.",
       ps("b1", fu("n4")), mv("r7", [38, 47], delay=0.3), dr("n4", "b1", [33, 40], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
