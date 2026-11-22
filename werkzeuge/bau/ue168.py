import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 68-P3 (U12-U14, Woche 12 Phase 6): Technical Passing & 1 v 1 Defending. 30 x 35 Yards = Feld x 28.6-71.4, y 5-55 (27 x 32 m),
# im PDF breiter gezeichnet. Ausrichtung wie im PDF: Die Angreifer spielen nach oben auf zwei Minitore an der gestrichelten Linie,
# darüber links und rechts je ein Hütchen-Slalom (sechs Hütchen im Zickzack). Dunkel (Angreifer) -> Team Neon (9, 7, 8, 10, 4 wie im
# PDF; die wartenden Angreifer oben 3, 6, 11, 2 nur im Text), pink (Verteidiger) -> Team Rot, neu nummeriert (im PDF doppelt): links
# 12, 13, rechts 15, 16 (je eine Figur weniger als im PDF). Rote Dummys im PDF -> Stangen; der Dummy oben in der Mitte fehlt (Platz).
# Ein Trainer statt zwei. Gezeigt wird die linke Seite, die rechte läuft danach genauso. Steigerung: zwei Endzonen unten (farbig).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 20, 38, "T")
POS = {"n9": (52, 6.5), "n7": (49.5, 22.5), "n8": (54, 41), "n10": (41.7, 52.6), "n4": (62.5, 52.6),
       "r12": (25.5, 10), "r13": (17, 10), "r15": (74.5, 10), "r16": (83, 10)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 41.5), B("s2", 20, 41.5)]
LINES = [rect(28.6, 5, 42.8, 50), line(28.6, 20.9, 71.4, 20.9)]
TORE = [{"x": 35.6, "y": 20.9, "side": "top"}, {"x": 64.4, "y": 20.9, "side": "top"}]
SLALOM = [C(x, 10) for x in (28.8, 34.2, 40)] + [C(x, 14.5) for x in (31.9, 37, 42.3)] + \
         [C(x, 10) for x in (71.2, 65.8, 60)] + [C(x, 14.5) for x in (68.1, 63, 57.7)]
DUMMYS = [C(58, 37, shape="stange"), C(36, 52, shape="stange"), C(68, 52, shape="stange")]
ZONEN = [{"type": "zone", "x": 29.3, "y": 41.7, "w": 5.7, "h": 7.7, "color": "orange"},
         {"type": "zone", "x": 65, "y": 41.7, "w": 5.7, "h": 7.7, "color": "orange"}]

u = {"title": "Doppelpass und Eins gegen Eins", "code": "UE-168", "kind": "Übungsform",
 "focuses": ["Passspiel", "1 gegen 1", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 15, "field_size": "27 x 32 m",
 "description": "Erst ein Doppelpass, dann noch einer: Die Angreifer spielen sich mit kurzen Pässen nach vorn. Gleichzeitig läuft ein Verteidiger rückwärts durch einen Hütchen-Slalom und kommt ins Feld. Dann geht es eins gegen eins auf ein Minitor. Gearbeitet wird abwechselnd auf beiden Seiten.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 32 Metern. Oben links und rechts je ein Hütchen-Slalom, darunter eine gestrichelte Linie mit zwei Minitoren. Im Feld drei Dummys für die Doppelpässe.",
  "Verteilen: Team Neon greift an: ein Spieler oben mit Bällen, die anderen im Feld an den Dummys, weitere warten oben. Team Rot verteidigt und wartet links und rechts neben den Hütchen. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Neon neun passt zu Neon sieben, dann folgen zwei Doppelpässe. Gleichzeitig läuft ein Verteidiger rückwärts durch den Slalom und kommt ins Feld. Dann heißt es eins gegen eins auf das Minitor.",
  "Wertung und Wechsel: Trifft der Angreifer, gibt das einen Punkt für ihn. Erobert der Verteidiger den Ball, gibt das einen Punkt für ihn. Danach ist die andere Seite dran, und nach einigen Runden tauschen Angreifer und Verteidiger."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen", "Schnell durch den Hütchen-Slalom", "Als Verteidiger nah ran, tief bleiben, nicht reinspringen", "Mit Finten den Verteidiger aus dem Gleichgewicht bringen"],
 "materials": ["2 Minitore", "3 Dummys", "12 Hütchen für die Slaloms", "Hütchen für das Feld", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Doppelpass und Eins gegen Eins. Erst zwei Doppelpässe, dann geht der Angreifer allein gegen einen Verteidiger aufs Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": SLALOM + DUMMYS, "players": sp(), "balls": [B("b1", 52.6, 7.1)] + ERSATZ,
  "steps": [
   S("Anspiel", "Neon neun passt kurz zu Neon sieben, der sich aufdreht. Gleichzeitig läuft Rot zwölf rückwärts durch den Slalom und tippt jedes Hütchen an.",
     ps("b1", [50.1, 23.1]), mv("r12", [28.8, 7.6]), mv("r12", [31.9, 16.9], after=True), mv("r12", [34.2, 7.6], after=True)),
   S("Erster Doppelpass", "Neon sieben spielt zu Neon acht und läuft schräg nach vorn. Neon acht legt ihm den Ball direkt zurück. Rot zwölf läuft weiter durch den Slalom.",
     mv("r12", [37, 16.9]), mv("r12", [40, 7.6], after=True), mv("r12", [42.3, 16.9], after=True),
     ps("b1", [54.6, 41.6]), mv("n7", [45.5, 32.6], delay=0.3), ps("b1", [46.1, 33.2], after=True)),
   S("Zweiter Doppelpass", "Neon sieben passt zu Neon zehn. Neon zehn spielt zu Neon acht und startet nach vorn, und Neon acht legt ihm den Ball in den Lauf. Rot zwölf kommt ins Feld.",
     ps("b1", [42.3, 53.2]), mv("r12", [37, 27], delay=0.5), ps("b1", [54.6, 41.6], after=True), mv("n10", [36.5, 36.2], after=True), ps("b1", [37.1, 36.8], after=True)),
   S("Eins gegen eins: Punkt", "Neon zehn täuscht nach rechts an, Rot zwölf geht mit. Dann zieht Neon zehn links vorbei und schießt ins Minitor, und das gibt einen Punkt für Neon zehn. Danach ist die rechte Seite dran.",
     dr("n10", "b1", [39.5, 34]), mv("r12", [38, 30], delay=0.2), dr("n10", "b1", [32, 31], after=True), ps("b1", [35.6, 21.2], after=True))],
  "dims": dims(28.6, 71.4, 5, 55, "27 m", "32 m", rx=91)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit einer Finte am Verteidiger vorbei.", "Mit Finten vorbei",
    "Der Angreifer bringt den Verteidiger mit einer Finte aus dem Gleichgewicht: Übersteiger, Täuschung oder eine schnelle Körperdrehung. Geht der Verteidiger mit, ist auf der anderen Seite Platz. Dann schnell vorbei und abschließen.",
    sp(n10=(36.5, 40), r12=(37, 24), n7=(45.5, 32.6)), [B("b1", 37.1, 40.6)] + ERSATZ,
    [S("Übersteiger", "Neon zehn dribbelt auf Rot zwölf zu und macht einen Übersteiger nach rechts. Rot zwölf fällt darauf herein und geht mit.",
       dr("n10", "b1", [39, 33]), mv("r12", [40.5, 27], delay=0.4)),
     S("Vorbei: Punkt", "Dann zieht Neon zehn schnell links vorbei und schießt ins Minitor, und das gibt einen Punkt für Neon zehn.",
       dr("n10", "b1", [32.5, 29]), ps("b1", [35.6, 21.2], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Erobert der Verteidiger den Ball, dribbelt er in die Endzone.", "Konter in die Endzone",
    "Unten links und rechts liegt jetzt je eine Endzone. Erobert der Verteidiger den Ball, dribbelt er sofort in die Endzone, und das gibt einen Punkt für ihn. So wird aus dem Ballgewinn gleich ein Konter.",
    sp(n10=(36.5, 40), r12=(37, 24), n7=(45.5, 32.6)), [B("b1", 37.1, 40.6)] + ERSATZ,
    [S("Ball erobert", "Neon zehn dribbelt an. Rot zwölf kommt schnell heran, bleibt tief und springt nicht hinein. Dann spitzelt er Neon zehn den Ball weg.",
       dr("n10", "b1", [38, 32.5]), mv("r12", [36, 30], delay=0.3)),
     S("In die Endzone: Punkt", "Sofort dribbelt Rot zwölf in die Endzone, und das gibt einen Punkt für Rot zwölf. Danach ist die rechte Seite dran.",
       dr("r12", "b1", [33, 34]), dr("r12", "b1", [32.2, 45.5], after=True))],
    lines=LINES + ZONEN)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
