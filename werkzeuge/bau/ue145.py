import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 26-P2 (U12-U14, Woche 7 Phase 1): Beat the Press to Play Out Rondo - GK. Box 10 x 15 Yards = Feld x 36-64, y 6-48 (9 x 14 m).
# Torwart unten, Neon 6 oben (Sechser oder zweiter Torwart), Neon 5 und 4 an den Seiten, Rot 8 und 9 pressen in der Mitte.
# Im PDF 5/4 dunkel und TW/6 pink, hier alle Ballbesitzer Neon. Außenspieler tiefer gesetzt (3D-Abstand). Ein Trainer.
# Sichtkegel aus Video und Text ("scan constantly", "Scan defenders positioning - play through or around?"): Torwart schaut
# auf die Lücke zwischen den beiden Verteidigern; in Steigerung 2 schaut er nach der Ballmitnahme am Dummy vorbei nach oben.
T = P("T", "c", 27, 22, "T")
POS = {"n1": (50, 48), "n6": (50, 6), "n5": (36, 44), "n4": (64, 44), "r8": (45.5, 27), "r9": (54.5, 27)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 28.6, 25.5), B("s2", 25, 25.5)]
LINES = [rect(36, 6, 28, 42)]
DUMMYS = [C(51, 34, shape="stange", id="d1"), C(43, 9, shape="stange", id="d2")]

u = {"title": "Torwart-Rondo gegen Pressing", "code": "UE-145", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 8, "field_size": "9 x 14 m",
 "description": "Ein Rondo für den Spielaufbau mit Torwart. Der Torwart steht unten, ein Sechser oben, zwei Spieler an den Seiten. Zwei Verteidiger pressen in der Mitte. Das Team bringt den Ball von unten nach oben und wieder zurück, entweder außen herum oder durch die Lücke zwischen den Verteidigern. Der Torwart hebt dabei immer wieder den Kopf und entscheidet: außen herum oder durch die Mitte.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern. Der Torwart steht an der unteren Linie, ein Sechser oder zweiter Torwart an der oberen.",
  "Verteilen: Zwei Spieler stehen links und rechts an den Seiten, zwei Verteidiger in der Mitte. Der Trainer steht am Rand mit Bällen.",
  "Ablauf: Der Ball soll von einer Seite zur anderen. Ist die Lücke zwischen den Verteidigern zu, geht es außen herum, ist sie offen, durch die Mitte.",
  "Wertung und Wechsel: Kommt der Ball auf der anderen Seite an, gibt das einen Punkt. Erobern die Verteidiger den Ball, tauschen sie mit den Spielern an den Seiten. Die Torhüter bleiben."],
 "organisation_show": ORG,
 "coaching_points": ["Offen stehen, nach vorn schauen und immer wieder den Kopf heben", "Den Druck lesen: außen herum, wenn die Lücke zu ist, durch die Mitte, wenn sie offen ist", "Feste, genaue Pässe, damit das Tempo bleibt", "Mit dem hinteren Fuß annehmen und vom Gegner weg mitnehmen"],
 "materials": ["4 Hütchen", "2 Dummys", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Torwart-Rondo gegen Pressing. Der Torwart spielt mit, und das Team bringt den Ball an zwei Verteidigern vorbei von unten nach oben.",
 "board": {"lines": LINES, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 48.6)] + ERSATZ,
  "steps": [
   S("Kopf hoch", "Der Torwart hat den Ball. Er hebt den Kopf und schaut, wie die beiden Verteidiger stehen. Die Lücke zwischen ihnen ist zu.",
     bl("n1", [50, 27])),
   S("Zur Seite", "Also spielt er nicht durch die Mitte, sondern zur Seite zu Spieler fünf. Spieler acht läuft sofort auf ihn zu.",
     ps("b1", [36.6, 44.6]), mv("r8", [43, 39], delay=0.3)),
   S("Hoch zu Spieler sechs: Punkt", "Spieler fünf spielt direkt hoch zu Spieler sechs. Der Ball ist auf der anderen Seite, und das gibt einen Punkt für Team Neon.",
     ps("b1", [50.6, 6.6]), mv("r8", [45.5, 27], delay=0.3)),
   S("Ballgewinn: Tausch", "Jetzt geht es zurück nach unten. Spieler sechs spielt zu Spieler vier, aber Spieler neun fängt den Ball ab. Dann tauschen die Verteidiger mit Spieler vier und Spieler fünf, und es geht von vorn los.",
     mv("r9", [56, 21]), ps("b1", [56.6, 21.6], delay=0.2))],
  "dims": dims(36, 64, 6, 48, "9 m", "14 m", rx=72)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Durch die Mitte gibt es zwei Punkte.", "Durch die Lücke",
    "Außen herum gibt es einen Punkt, durch die Lücke zwischen den Verteidigern zwei. Aber nicht erzwingen: Erst wenn die Verteidiger auseinandergehen, ist die Lücke offen. Dann direkt durchspielen.",
    sp(r8=(42, 27), r9=(58, 27)), [B("b1", 50.6, 48.6)] + ERSATZ,
    [S("Lücke offen", "Die Verteidiger stehen weit auseinander. Der Torwart hebt den Kopf und sieht: Die Lücke in der Mitte ist offen.",
       bl("n1", [50, 27])),
     S("Durch die Mitte: Punkte", "Er spielt den Ball flach durch die Lücke zu Spieler sechs, und das gibt zwei Punkte für Team Neon. Dann geht es zurück nach unten.",
       ps("b1", [50.6, 6.6]), mv("r8", [46, 24], delay=0.2), mv("r9", [54, 24], delay=0.2))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Hinter dem Dummy annehmen.", "Am Dummy vorbei",
    "Vor dem Torwart und vor Spieler sechs steht ein Dummy. Wer den Ball gerade vor sich annimmt, spielt in den Dummy. Also mit dem hinteren Fuß annehmen und den Ball seitlich am Dummy vorbei mitnehmen. Dann ist der Passweg frei.",
    sp(r8=(41, 27), r9=(59, 27)), [B("b1", 64.6, 44.6)] + ERSATZ,
    [S("Annehmen, mitnehmen", "Spieler vier spielt zum Torwart. Der nimmt den Ball mit dem hinteren Fuß an und nimmt ihn seitlich am Dummy vorbei mit.",
       ps("b1", [50.6, 48.6]), dr("n1", "b1", [45, 48], after=True)),
     S("Passweg frei: Punkt", "Jetzt hebt er den Kopf, der Weg nach oben ist frei, und er spielt zu Spieler sechs. Das gibt einen Punkt für Team Neon.",
       bl("n1", [49, 20]), ps("b1", [50.6, 6.6], after=True))],
    cones=DUMMYS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
