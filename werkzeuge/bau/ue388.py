import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 34-P7 (U15-U17, Woche 31 Phase 1): Passing Combinations in a 433, Technical Pattern. 30 x 30 Yards = 27 x 27 m, gerundet
# 25 x 25 m = Feld x 25-75, y 5-55. Ausrichtung wie im PDF (Innenverteidiger unten, gespielt wird nach oben).
# Ein Team (Neon), Nummern wie im PDF: Innenverteidiger 5 und 6 (dahinter warten 3 und 2), Sechser 4 vor dem Dummy (Stange),
# Achter 8 und 10, Flügel 7 und 11. Die Wartenden 3 und 2 stehen neben den Innenverteidigern (3D-Abstand).
# Ein Trainer statt einem mit Bällen unten in der Mitte, hier links neben dem Feld (unten Platz für die Maßlinie).
# Passfolge nach PDF und Video (0:27-0:47): 5 -> 4, Ablage in den Lauf von 5, 5 -> 8, 8 -> 4, 4 -> 7, 7 -> 8 und Lauf an der
# Linie, 8 legt in den Lauf, 7 spielt zurück zum Innenverteidiger 6. Danach rückt jeder eine Station weiter (5 zum Sechser,
# 4 zum Achter, 8 auf den Flügel, 7 zu den Innenverteidigern, 3 auf die Startstation; so im Video 0:02-0:22), und 6 beginnt
# dieselbe Folge über die andere Seite (10, 11). Hütchen leicht neben die Spieler gerückt (Linienprüfung).
# Fassungen = PDF Key Coaching Point 1 (Gewicht der Ablage) und 2 (scharfer Pass raus auf den Flügel).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 16, 44, "T")
ERSATZ = [B("s1", 19.5, 44.6), B("s2", 17, 48.5)]
POS = {"n5": (37.9, 52), "n3": (29.5, 52.5), "n6": (61.8, 53), "n2": (70.5, 53), "n4": (50.7, 37.8), "n8": (66.5, 29.9),
       "n7": (72.1, 10.5), "n10": (32.6, 31), "n11": (29.2, 9.8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
CONES = [C(40.5, 54.8), C(59.3, 51.5), C(64.5, 27.3), C(72.4, 7.2), C(34.2, 28.2), C(28.5, 7.5), C(50.7, 34, shape="stange")]
LINES = [rect(25, 5, 50, 50)]
BAELLE = [B("b1", 38.5, 52.6)] + ERSATZ
LAUF5 = [45.4, 48.3]      # Spieler fünf startet nach der Ablage nach vorn
LAUF7 = [73.5, 22]        # Spieler sieben läuft an der Linie nach unten
def ablage(delay=None):
    return [ps("b1", fuss(POS["n4"]), delay=delay), mv("n5", LAUF5, delay=0.4), ps("b1", fuss(LAUF5), after=True)]

u = {"title": "Passmuster mit Achter und Flügel", "code": "UE-388", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 9, "players_max": 12,
 "field_size": "25 x 25 m",
 "description": "Neun Spieler stehen auf ihren Positionen im Vier-Drei-Drei. Der Ball läuft vom Innenverteidiger über den Sechser zum Achter, zurück in die Mitte und raus auf den Flügel. Nach einem Doppelpass außen geht er zurück zum anderen Innenverteidiger. Dann rückt jeder eine Station weiter, und die Folge läuft über die andere Seite.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern. Sechs Hütchen markieren die Stationen, in der Mitte steht eine Stange als Gegenspieler.",
  "Verteilen: Auf jeder Station steht ein Spieler, bei den beiden Innenverteidigern unten stehen zwei. Der Sechser steht vor der Stange. Die Bälle liegen beim ersten Innenverteidiger, der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Innenverteidiger zum Sechser, Ablage in den Lauf, steil auf den Achter. Der spielt zurück in die Mitte, und der Sechser spielt raus auf den Flügel. Doppelpass außen, dann geht der Ball zurück zum anderen Innenverteidiger.",
  "Wechsel: Jeder läuft seinem Pass nach und rückt eine Station weiter. Dann startet der andere Innenverteidiger dieselbe Folge über die andere Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Genau auf den Fuß, dann fließt es", "Die Ablage in den Lauf, nicht in die Füße", "Tempo hoch, wenn es geht direkt", "Mal links, mal rechts, und laut ansagen"],
 "materials": ["6 Hütchen", "1 Stange", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passmuster mit Achter und Flügel. Neun Spieler stehen wie im Vier-Drei-Drei, und der Ball läuft in einer festen Folge vom Innenverteidiger bis auf den Flügel und zurück.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Kurz rein, Ablage in den Lauf", "Spieler fünf spielt kurz rein zu Spieler vier und startet gleich nach vorn. Spieler vier legt direkt in seinen Lauf ab.",
     *ablage()),
   S("Steil auf den Achter", "Ohne den Ball zu stoppen, spielt Spieler fünf diagonal hoch zu Spieler acht.",
     ps("b1", fuss(POS["n8"]))),
   S("Rein zum Sechser, raus auf den Flügel", "Spieler acht spielt zurück in die Mitte. Spieler vier dreht nicht lange und spielt den langen Ball raus zu Spieler sieben.",
     ps("b1", fuss(POS["n4"])), ps("b1", fuss(POS["n7"]), after=True)),
   S("Doppelpass außen", "Spieler sieben spielt zu Spieler acht und läuft sofort die Linie runter. Spieler acht legt den Ball in seinen Lauf.",
     ps("b1", fuss(POS["n8"])), mv("n7", LAUF7, delay=0.3), ps("b1", fuss(LAUF7), after=True)),
   S("Zurück zu sechs, Runde geschafft", "Spieler sieben spielt flach zurück zu Spieler sechs, und die Runde ist geschafft. Jeder rückt eine Station weiter. Jetzt startet Spieler sechs dieselbe Folge über Spieler zehn und Spieler elf auf der anderen Seite.",
     ps("b1", fuss(POS["n6"])), mv("n7", [77.5, 56], delay=0.6), mv("n8", [72.1, 12.5], delay=0.6), mv("n4", [64.5, 30.5], delay=0.6),
     mv("n5", [49.5, 41], delay=0.6), mv("n3", [37.9, 52], delay=0.6))],
  "dims": dims(25, 75, 5, 55, "25 m", "25 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Ablage muss in den Lauf.", "Die Ablage in den Lauf",
    "Spieler fünf startet nach seinem Pass sofort nach vorn. Die Ablage vom Sechser kommt nicht hart in die Füße, sondern weich vor ihn in den Lauf. So kann er den nächsten Pass spielen, ohne abzubremsen.",
    sp(), BAELLE,
    [S("Pass und sofort los", "Spieler fünf spielt zu Spieler vier und läuft direkt los. Spieler vier legt den Ball weich vor ihn, nicht in die Füße.",
       *ablage()),
     S("Ohne abzubremsen weiter", "Spieler fünf muss nicht stoppen. Mit dem ersten Kontakt geht der Ball diagonal zu Spieler acht.",
       ps("b1", fuss(POS["n8"])))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Der lange Ball raus auf den Flügel kommt scharf.", "Scharf raus auf den Flügel",
    "Der Pass vom Sechser zum Flügel ist der weiteste in der Folge. Im Spiel geht er durch eine ganze Linie. Darum kommt er flach, scharf und genau, und der Flügelspieler kann ihn sofort verarbeiten.",
    sp(), [B("b1", 67.1, 30.5)] + ERSATZ,
    [S("Rein in die Mitte", "Spieler acht hat den Ball und spielt zurück in die Mitte. Spieler vier steht schon offen und weiß, wohin der Ball geht.",
       ps("b1", fuss(POS["n4"]))),
     S("Flach und scharf nach außen", "Jetzt kommt der lange Ball. Spieler vier spielt flach und scharf raus zu Spieler sieben, als ginge er durch eine ganze Linie. Spieler sieben spielt sofort weiter auf Spieler acht.",
       ps("b1", fuss(POS["n7"])), ps("b1", fuss(POS["n8"]), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
