import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 80-P5 (U12-U14, Woche 9 Phase 2): Possession to Penetrate. 15 x 15 Yards = Feld x 25-75, y 5-55 (14 m), Dreieck aus drei
# Hütchen in der Mitte (gestrichelt). Pink (6 Ballbesitz) -> Neon 8, 4, 3, 2, 6, 5; Blau (3 Verteidiger) -> Rot, neu nummeriert
# 7, 9, 11 (Nummern im PDF doppelt). Verteidiger leicht verschoben (3D-Abstand), Trainer rechts.
# Sichtkegel aus dem Text ("scan to find gaps", "Scan early and often", Steigerung "scanning"): Neon 4 schaut vor dem Pass
# durchs Dreieck, Neon 3 sucht in der Steigerung den Verbindungsspieler. Im Video kein Kegel.
T = P("T", "c", 84, 50, "T")
POS = {"n8": (38.3, 5), "n4": (61.8, 5.8), "n3": (24.8, 28.3), "n2": (74.9, 27.3), "n6": (40.7, 54), "n5": (61.8, 54.3),
       "r7": (47, 15), "r9": (66, 22), "r11": (52, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 85.6, 53.5), B("s2", 82, 53.5)]
D1, D2, D3 = (51.1, 22.1), (41.6, 37.8), (59.5, 37.9)
LINES = [rect(25, 5, 50, 50), line(*D1, *D2), line(*D2, *D3), line(*D3, *D1)]
KEGEL = [C(*D1), C(*D2), C(*D3)]

u = {"title": "Durch das Dreieck spielen", "code": "UE-152", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 10, "field_size": "14 x 14 m",
 "description": "Sechs gegen drei im Quadrat, in der Mitte ein Dreieck aus Hütchen. Team Neon hält den Ball und sucht die Lücke: Jeder Pass durch das Dreieck ist ein Punkt. Die Verteidiger dürfen das Dreieck nicht durchqueren. Erobern sie den Ball, brauchen sie fünf Pässe in Folge für einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern, in der Mitte ein Dreieck aus drei Hütchen.",
  "Verteilen: Sechs von Team Neon verteilen sich am Rand, drei von Team Rot verteidigen innen. Der Trainer steht am Rand mit Bällen.",
  "Ablauf: Team Neon hält den Ball, zieht das Feld breit und spielt durch das Dreieck, sobald die Lücke da ist. Die Verteidiger dürfen nicht durch das Dreieck laufen.",
  "Wertung: Jeder Pass durch das Dreieck ist ein Punkt für Team Neon. Erobert Team Rot den Ball, sind fünf Pässe in Folge ein Punkt für Team Rot. Team Neon presst sofort, um den Ball zurückzuholen."],
 "organisation_show": ORG,
 "coaching_points": ["Das ganze Feld nutzen und die Verteidiger auseinanderziehen", "Früh und oft den Kopf heben, um die Lücke zu sehen", "Den Pass durch das Dreieck scharf spielen", "Nach Ballverlust sofort pressen"],
 "materials": ["7 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Durch das Dreieck spielen. Sechs gegen drei, und Team Neon sucht immer wieder den Pass durch die Mitte.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 25.4, 28.9)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Team Neon lässt den Ball am Rand laufen. Neon drei spielt zu Neon acht, der weiter zu Neon vier. Rot sieben läuft hinterher.",
     ps("b1", [38.9, 5.6]), ps("b1", [62.4, 6.4], after=True), mv("r7", [54, 11], delay=0.8)),
   S("Kopf hoch", "Neon vier hebt den Kopf und sieht: Die Verteidiger stehen weit auseinander, durch das Dreieck ist der Weg zu Neon sechs frei.",
     bl("n4", [51.5, 30])),
   S("Durch das Dreieck: Punkt", "Neon vier spielt scharf durch das Dreieck zu Neon sechs, und das gibt einen Punkt für Team Neon. Team Neon behält den Ball und sucht gleich die nächste Lücke.",
     ps("b1", [41.3, 54.6]))],
  "dims": dims(25, 75, 5, 55, "14 m", "14 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ballverlust und sofort pressen.", "Ballgewinn",
    "Erobert Team Rot den Ball, braucht es fünf Pässe in Folge für einen Punkt. Durch das Dreieck dürfen die Verteidiger nicht spielen. Team Neon presst sofort, um den Ball schnell zurückzuholen.",
    sp(), [B("b1", 75.5, 27.9)] + ERSATZ,
    [S("Abgefangen", "Neon zwei will zu Neon fünf passen, aber Rot elf läuft dazwischen und fängt den Ball ab.",
       mv("r11", [67, 44]), ps("b1", [67.6, 44.6], delay=0.3)),
     S("Fünf Pässe: Punkt", "Rot elf spielt zu Rot neun, der weiter zu Rot sieben. Schafft Team Rot fünf Pässe in Folge, gibt das einen Punkt für Team Rot. Darum pressen Neon vier und Neon acht sofort.",
       ps("b1", [66.6, 22.6]), ps("b1", [47.6, 15.6], after=True), mv("n4", [54, 9], delay=0.8), mv("n8", [40, 9], delay=0.8))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Spieler im Dreieck.", "Spieler im Dreieck",
    "Jetzt steht ein Spieler von Team Neon im Dreieck. Wird er angespielt und spielt den Ball auf die andere Seite weiter, ist das ein Punkt. Dafür muss jeder am Rand früh schauen, ob der Weg in die Mitte frei ist.",
    sp(r11=(31, 44), n10=(50.5, 32)), [B("b1", 25.4, 28.9)] + ERSATZ,
    [S("Mitte sehen", "Neon drei hebt den Kopf und sieht Neon zehn frei im Dreieck. Er spielt ihn an.",
       bl("n3", [50.5, 32]), ps("b1", [51.1, 32.6], after=True)),
     S("Auf die andere Seite: Punkt", "Neon zehn spielt direkt weiter auf die andere Seite zu Neon zwei, und das gibt einen Punkt für Team Neon.",
       ps("b1", [75.5, 27.9]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
