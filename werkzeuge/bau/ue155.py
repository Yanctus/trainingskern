import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P4 (U12-U14, Woche 10 Phase 5): Defending to Force Direction. 15 x 20 Yards = Feld x 31.25-68.75, y 5-55 (14 x 18 m),
# drei Bahnen (gestrichelt), oben Minitor in der Mitte (3 Punkte) und je ein Hütchentor außen (1 Punkt, etwas breiter gesetzt).
# Blau (Verteidiger und Außenspieler) -> Neon 4, 5 und 2, 3; Pink (Angreifer) -> Rot 7, 9, 11. Wartende Angreifer nur im Text.
# Ein Trainer rechts. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 76.5, 35, "T")
POS = {"n4": (42.7, 21), "n5": (57.3, 21), "n2": (29.8, 12.5), "n3": (70.1, 12.9),
       "r7": (35.7, 48), "r9": (50.2, 49.3), "r11": (63.7, 48)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 80.6, 38.5), B("s2", 77, 38.5)]
LINES = [rect(31.25, 5, 37.5, 50), line(44.8, 5, 44.8, 55), line(55.5, 5, 55.5, 55)]
KEGEL = [C(33.9, 5), C(40.6, 5), C(59.4, 5), C(66.1, 5)]
TORE = [{"x": 50.2, "y": 5, "side": "top"}]

u = {"title": "Zu zweit nach außen drängen", "code": "UE-155", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 11, "field_size": "14 x 18 m",
 "description": "Drei Angreifer gegen zwei Verteidiger. Oben steht ein Minitor in der Mitte, das drei Punkte bringt, und außen je ein Hütchentor für einen Punkt. Die Verteidiger schützen zuerst die Mitte: Einer presst, der andere sichert ab, und gemeinsam drängen sie die Angreifer nach außen. Erobern sie den Ball oder geht er ins Aus, bekommen sie zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern in drei Bahnen. Oben in der Mitte ein Minitor, außen links und rechts je ein Tor aus zwei Hütchen.",
  "Verteilen: Zwei Verteidiger von Team Neon oben, drei Angreifer von Team Rot unten, die nächsten Angreifer warten dahinter. Zwei Außenspieler von Team Neon stehen neben dem Feld. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Der Trainer spielt einen Angreifer an. Die Angreifer wollen ins Minitor oder durch ein Hütchentor, die Verteidiger schützen zuerst die Mitte.",
  "Wertung und Wechsel: Minitor drei Punkte, Hütchentor ein Punkt, Ballgewinn oder Aus zwei Punkte für die Verteidiger. Nach jeder Runde kommen drei neue Angreifer, die Verteidiger bleiben zwei Runden drin."],
 "organisation_show": ORG,
 "coaching_points": ["Zuerst die Mitte schützen", "Laut absprechen: Wer presst, wer sichert ab", "Kompakt bleiben und die Angreifer nach außen drängen", "Den Angriff verzögern statt blind hineinzugrätschen"],
 "materials": ["1 Minitor", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zu zweit nach außen drängen. Drei gegen zwei, und die Verteidiger halten die Mitte zu und lenken den Angriff nach außen.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 77.1, 35.6)] + ERSATZ,
  "steps": [
   S("Anspiel", "Der Trainer spielt Rot neun in der Mitte an. Neon vier presst sofort, Neon fünf sichert die Mitte ab.",
     ps("b1", [50.8, 49.9]), mv("n4", [48, 37], delay=0.3), mv("n5", [52.5, 27], delay=0.3)),
   S("Nach außen drängen", "Rot neun kommt nicht durch die Mitte und spielt nach rechts zu Rot elf. Neon fünf schiebt von innen hinüber, Neon vier sichert jetzt die Mitte.",
     ps("b1", [64.3, 48.6]), mv("n5", [57, 33], delay=0.2), mv("n4", [50, 30], delay=0.3)),
   S("Außen: nur ein Punkt", "Rot elf kommt nur noch außen durch und spielt durch das rechte Hütchentor. Das gibt einen Punkt für Team Rot, das Minitor in der Mitte bleibt zu. Dann kommen drei neue Angreifer.",
     dr("r11", "b1", [62.5, 14]), ps("b1", [62.75, 4.7], after=True))],
  "dims": dims(31.25, 68.75, 5, 55, "14 m", "18 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, einer sichert.", "Pressen und sichern",
    "Der eine Verteidiger geht auf den Ball und macht den Weg in die Mitte zu. Der andere steht schräg dahinter, sichert ab und lauert auf den Pass. So wird der Angreifer zu einem Pass gezwungen, den man abfangen kann.",
    sp(), [B("b1", 50.8, 49.9)] + ERSATZ,
    [S("Pressen und sichern", "Rot neun hat den Ball. Neon vier presst ihn direkt, Neon fünf steht schräg dahinter und sichert ab.",
       mv("n4", [50, 43.5]), mv("n5", [57, 40], delay=0.2)),
     S("Abfangen: Punkte", "Rot neun will zu Rot elf passen, aber Neon fünf ahnt es und fängt den Ball ab. Das gibt zwei Punkte für Team Neon.",
       mv("n5", [57.5, 48.6]), ps("b1", [58.1, 49.2], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Ballgewinn raus zum Außenspieler.", "Konter nach außen",
    "Erobern die Verteidiger den Ball, spielen sie ihn sofort hinaus zu einem Außenspieler neben dem Feld, wie zu einem Außenverteidiger im Spiel. So lernen sie, nach dem Ballgewinn schnell umzuschalten.",
    sp(), [B("b1", 36.3, 48.6)] + ERSATZ,
    [S("Ballgewinn", "Rot sieben dribbelt links nach vorn. Neon vier presst, drängt ihn an die Linie und erobert den Ball.",
       dr("r7", "b1", [37, 35]), mv("n4", [40, 30], delay=0.2), dr("n4", "b1", [40, 26], after=True)),
     S("Raus zu Neon zwei: Punkte", "Sofort spielt Neon vier den Ball hinaus zu Neon zwei. Der Konter ist geglückt, und das gibt zwei Punkte für Team Neon.",
       ps("b1", [30.4, 13.1]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
