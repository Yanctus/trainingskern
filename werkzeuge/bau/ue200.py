import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 77-P3 (U12-U14, Woche 25 Phase 1): Heads Up Rondo. 15 x 20 Yards = Feld x 31.25-68.75, y 5-55 (14 x 18 m), Ausrichtung wie im PDF.
# Drei Teams zu dritt: Gelb (4, 5, 7) -> Neon, Pink (6, 7, 8) -> Rot, Blau (Überzahl-Team: oben 4, unten 9, innen 6) -> neutrale
# Springer F. Doppelte Nummer 7: Pink 7 heißt hier Spieler zwei. Positionen leicht verschoben (3D-Abstand). Ein Trainer statt zwei.
# Grundform nach PDF/Video (0:10-0:20): Springer unten -> Neon 4 -> Springer innen -> Springer oben. Punkt-Regel ergänzt (im Original
# ohne Zählweise): Ball von einem Springer an der Grundlinie zum anderen = Punkt. Fassungen: "Split opposition midfield / play on
# shoulder" (Video 0:20-0:45) und Progression 1 (Ballverlust = verteidigen). Progression 2 (acht Pässe in Folge) nur im Bericht.
# Sichtkegel (Kern der Übung, "scan / head up to see teammates"): im Video Kegel ab 0:50 und 1:20 (Spieler schaut vor der Annahme zum
# Mitspieler bzw. "head up to recognize attacking team"). Eingebaut: Neon 4 und Springer innen vor der Annahme, Neon 4 vor dem Pass
# durch die Lücke, Rot 8 nach dem Ballgewinn.
T = P("T", "c", 23, 9, "T")
POS = {"f1": (50, 5), "f2": (50, 55), "f3": (60, 22), "n4": (31.5, 38), "n5": (38, 20), "n7": (68.5, 40),
       "r8": (47, 22), "r6": (41, 39), "r2": (58.5, 39)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 24.6, 5.5), B("s2", 21, 5.5)]
LINES = [rect(31.25, 5, 37.5, 50)]
CONES = ecken(31.25, 5, 37.5, 50)

u = {"title": "Rondo mit Kopf hoch", "code": "UE-200", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "14 x 18 m",
 "description": "Ein Rondo mit drei Teams zu dritt. Team Neon spielt mit drei Springern gegen Team Rot und will den Ball vom Springer unten zum Springer oben bringen. Die Teams tragen nur farbige Kappen oder Stirnbänder, deshalb muss jeder genau hinschauen, bevor der Ball kommt. Nach zwei Minuten tauschen Neon und Rot die Aufgaben.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. Statt Leibchen tragen die Teams farbige Kappen oder Stirnbänder.",
  "Verteilen: Drei Teams zu dritt. Je ein Springer steht auf der Grundlinie oben und unten, einer im Feld. Team Neon spielt mit den Springern, Team Rot verteidigt. Der Trainer steht an der Ecke mit Bällen.",
  "Ablauf: Team Neon und die Springer halten den Ball und spielen ihn von einem Springer an der Grundlinie zum anderen. Team Rot will den Ball erobern.",
  "Wertung und Wechsel: Kommt der Ball von unten nach oben oder von oben nach unten, gibt das einen Punkt. Erobert Rot den Ball, spielt der Trainer neu an. Nach zwei Minuten tauschen Neon und Rot die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Vor jeder Ballannahme umschauen: Wo sind Mitspieler, Platz und Gegner?", "Auf der Schulter des Gegners anbieten und mit dem ersten Kontakt die Linie überspielen", "Die Springer früh anspielen und die Überzahl nutzen", "Die Lücke zwischen zwei Gegnern sehen und hindurchspielen"],
 "materials": ["4 Hütchen", "Viele Bälle", "Kappen oder Stirnbänder in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Rondo mit Kopf hoch. Team Neon spielt mit drei Springern gegen Team Rot, und jeder muss ständig schauen, wo die Mitspieler sind.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 55.6)] + ERSATZ,
  "steps": [
   S("Kopf hoch", "Der Springer unten hat den Ball. Bevor der Pass kommt, schaut Spieler vier sich um: Wo ist der Springer in der Mitte, wo sind die Gegner? Dann kommt der Ball.",
     bl("n4", [50, 28]), ps("b1", [32.1, 38.6], after=True)),
   S("Zum Springer in der Mitte", "Auch der Springer in der Mitte schaut sich um und weiß schon, wo der Springer oben steht. Spieler vier spielt ihn sofort an.",
     bl("f3", [52, 8]), ps("b1", [60.6, 22.6], after=True)),
   S("Nach oben: Punkt", "Der Springer in der Mitte spielt weiter zum Springer oben. Der Ball ist von unten nach oben gekommen, und das gibt einen Punkt für Team Neon. Jetzt spielt Team Neon wieder nach unten, und Team Rot jagt weiter den Ball.",
     ps("b1", [50.6, 5.6]))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Mitte teilen.", "Die Mitte teilen",
    "Der Springer in der Mitte stellt sich seitlich hinter einen Gegner, auf dessen Schulter. So kann er den Ball halb gedreht annehmen. Der Passgeber schaut, sieht die Lücke zwischen zwei Gegnern und spielt flach hindurch.",
    sp(), [B("b1", 32.1, 38.6)] + ERSATZ,
    [S("Auf die Schulter", "Spieler vier hat den Ball. Der Springer in der Mitte stellt sich seitlich hinter Spieler acht. Spieler vier hebt den Kopf und sieht die Lücke zwischen Spieler sechs und Spieler acht.",
       mv("f3", [55, 28]), bl("n4", [50, 31], after=True)),
     S("Durch die Lücke: Punkt", "Spieler vier spielt flach durch die Lücke. Der Springer nimmt den Ball mit dem ersten Kontakt nach vorn mit und spielt zum Springer oben. Das gibt einen Punkt für Team Neon.",
       ps("b1", [55.6, 28.6]), dr("f3", "b1", [57, 17], after=True), ps("b1", [50.6, 5.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ball verloren, sofort verteidigen.", "Ball weg, umschalten",
    "Jetzt gilt: Wer den Ball verliert, verteidigt sofort. Erobert Team Rot den Ball, spielt Rot mit den Springern, und Team Neon jagt den Ball. Die Springer spielen immer mit dem Team am Ball, deshalb muss jeder ständig schauen, wer gerade angreift.",
    sp(), [B("b1", 38.6, 20.6)] + ERSATZ,
    [S("Ball erobert", "Spieler fünf will zum Springer oben passen, aber Spieler acht fängt den Ball ab. Ab jetzt greift Team Rot an.",
       mv("r8", [45, 12]), ps("b1", [45.6, 12.6], delay=0.3)),
     S("Wer greift an?", "Spieler acht hebt sofort den Kopf und sucht den Springer. Gleichzeitig schaltet Team Neon um: Spieler fünf presst, Spieler vier und Spieler sieben machen die Passwege zu, und Spieler zwei läuft sich frei.",
       bl("r8", [60, 22]), mv("n5", [40, 14]), mv("n4", [40, 33]), mv("n7", [63, 33]), mv("r2", [60, 47])),
     S("Nach unten: Punkt", "Spieler acht spielt zum Springer in der Mitte, und der spielt weiter zum Springer unten. Das gibt einen Punkt für Team Rot. Jetzt verteidigt Team Neon, bis es den Ball zurückerobert.",
       ps("b1", [60.6, 22.6]), ps("b1", [50.6, 55.6], after=True))])]}
u["board"]["dims"] = dims(31.25, 68.75, 5, 55, "14 m", "18 m", rx=78)
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
