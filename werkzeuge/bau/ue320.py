import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P4 (U15-U17, Woche 16): The Compact Back 4 Unit. 24 x 30 Yards = 22 x 27 m, gerundet 20 x 25 m. Feld x 27-73, y 5-55,
# drei Zonen wie im PDF (Linien bei y 22 und 38). Ausrichtung wie im PDF: Kette in der Mitte, je zwei Angreifer oben und unten.
# Pink (Kette 3, 4, 5, 2) -> Team Neon. Blau (3, 4 oben, 5, 2 unten) -> Team Rot, neu nummeriert 7, 8 oben und 9, 10 unten
# (Nummern waren doppelt). Ein Trainer statt zwei.
# Fassungen wie im PDF: Progression 1 (Minitore, Konter vier gegen zwei, laut Ton zwei Punkte) und Progression 2
# (Außenverteidiger darf bei der Verlagerung aus der Zone pressen).
# Sichtkegel: im Video keiner eingezeichnet. Aus Video-Einblendung "Recognise the switch to press, FB awareness to press"
# und Ton "improving their ability to read the game": Spieler zwei schaut in der zweiten Steigerung zum Passempfänger.
# Kein Dubletten-Fall: UE-166, UE-177, UE-250 (Tor mit Torwart), UE-212 (drei Minitore, vier gegen vier), UE-242 (vier gegen
# vier zwischen zwei Springern), UE-203 und UE-208 geprüft, überall andere Organisation.
T = P("T", "c", 15, 40, "T")
ERSATZ = [B("s1", 18.6, 43.5), B("s2", 15, 43.5)]
POS = {"n3": (35, 29), "n4": (45, 31), "n5": (55, 31), "n2": (65, 29),
       "r7": (37, 13), "r8": (63, 13), "r9": (40, 47), "r10": (60, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def kette(x3, x4, x5, x2, ya=29, yi=31, **k):
    return [mv("n3", [x3, ya], **k), mv("n4", [x4, yi], **k), mv("n5", [x5, yi], **k), mv("n2", [x2, ya], **k)]
LINES = [rect(27, 5, 46, 50), line(27, 22, 73, 22), line(27, 38, 73, 38)]
TORE = [{"x": 35, "y": 5, "side": "top"}, {"x": 65, "y": 5, "side": "top"},
        {"x": 35, "y": 55, "side": "bottom"}, {"x": 65, "y": 55, "side": "bottom"}]
DIMS = dims(27, 73, 5, 55, "20 m", "25 m", rx=83)

u = {"title": "Viererkette in der Mittelzone", "code": "UE-320", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 8,
 "field_size": "20 x 25 m",
 "description": "Eine Viererkette steht in der Mittelzone und macht die Wege zu. Oben und unten stehen je zwei Angreifer, die den Ball durch die Kette auf die andere Seite spielen wollen. Jeder Pass durch die Kette gibt einen Punkt für die Angreifer, jeder abgefangene Ball einen Punkt für die Kette. Die vier schieben gemeinsam zum Ball und halten die Abstände eng.",
 "organisation": ["Aufbauen: Ein Feld von 20 mal 25 Metern, quer in drei Zonen geteilt. Die Mittelzone ist etwas schmaler als die beiden Außenzonen.",
  "Verteilen: Team Neon steht als Viererkette in der Mittelzone. Von Team Rot stehen zwei Spieler in der oberen und zwei in der unteren Zone. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Team Rot lässt den Ball in seiner Zone laufen und sucht die Lücke. Der Pass soll durch die Kette zu den Mitspielern auf der anderen Seite. Team Neon bleibt in der Mittelzone, schiebt zum Ball und fängt die Pässe ab.",
  "Wertung und Wechsel: Ein Pass durch die Kette gibt einen Punkt für Team Rot. Ein abgefangener Ball gibt einen Punkt für Team Neon. Nach jeder Runde von zwei bis drei Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Eng bleiben, keine Lücke in der Kette", "Alle vier schieben zusammen zum Ball", "Seitlich stehen, dann bist du schneller am Pass", "Redet miteinander: schieben, halten, raus"],
 "materials": ["Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben", "4 Minitore für die Steigerung"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette in der Mittelzone. Vier Verteidiger stehen in der Mitte und lassen keinen Ball durch. Die Angreifer oben und unten suchen die Lücke.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": [B("b1", 63.6, 13.6)] + ERSATZ,
  "steps": [
   S("Ball läuft quer, Kette schiebt", "Team Rot hat oben den Ball. Spieler acht spielt quer zu Spieler sieben. Die Kette von Team Neon schiebt sofort mit nach links, alle vier zusammen.",
     ps("b1", [37.6, 13.6]), *kette(30, 39.5, 49, 58.5, delay=0.2)),
   S("Kein Weg durch, zurück nach rechts", "Spieler sieben findet keine Lücke. Also geht der Ball zurück zu Spieler acht. Jetzt muss die Kette schnell rüber. Spieler zwei schiebt weit raus, aber Spieler fünf kommt zu spät nach.",
     ps("b1", [63.6, 13.6]), mv("n2", [70.5, 29], delay=0.2), mv("n5", [53.5, 31], delay=0.5), mv("n4", [44.5, 31], delay=0.5), mv("n3", [35.5, 29], delay=0.5)),
   S("Durch die Lücke: Punkt", "Zwischen Spieler fünf und Spieler zwei ist die Lücke offen. Spieler acht spielt flach durch zu Spieler zehn, und das gibt einen Punkt für Team Rot.",
     ps("b1", [60.6, 47.6])),
   S("Unten weiter, Kette dreht sich um", "Es geht direkt weiter. Die Kette dreht sich zum Ball. Unten spielt Spieler zehn quer zu Spieler neun, und diesmal schieben alle vier eng zusammen rüber.",
     ps("b1", [40.6, 47.6]), *kette(31, 40.5, 50, 59.5, ya=30, yi=30, delay=0.2)),
   S("Abgefangen: Punkt", "Spieler neun versucht es trotzdem durch die Mitte. Spieler vier steht seitlich, macht einen Schritt in den Passweg und fängt den Ball ab, und das gibt einen Punkt für Team Neon. Der Trainer spielt den nächsten Ball zu Team Rot. Nach der Runde tauschen die Teams.",
     ps("b1", [39.3, 32.2]), mv("n4", [38.7, 31.6], delay=0.2))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Vier Minitore, und die Kette darf kontern.", "Konter auf die Minitore",
    "An jeder Grundlinie stehen jetzt zwei Minitore. Fängt die Kette den Ball ab, greift sie zu viert gegen die zwei Angreifer an, von denen der Pass kam. Ein Treffer ins Minitor gibt zwei Punkte. Verliert die Kette den Ball, geht sie zurück in die Mittelzone.",
    sp(n3=(30, 29), n4=(39.5, 31), n5=(49, 31), n2=(58.5, 29)), [B("b1", 37.6, 13.6)] + ERSATZ,
    [S("Pass abgefangen", "Spieler sieben hat oben den Ball und will steil durch die Kette spielen. Spieler vier ahnt den Pass und geht dazwischen.",
       ps("b1", [39.4, 30.1]), mv("n4", [38.8, 29.5], delay=0.2)),
     S("Sofort zu viert nach vorn", "Jetzt schaltet Team Neon um. Spieler vier dribbelt nach vorn in die obere Zone, und Spieler sieben muss ihn stellen. Links läuft Spieler drei mit, rechts kommen Spieler fünf und Spieler zwei nach.",
       dr("n4", "b1", [43, 21]), mv("r7", [40.5, 15.5], delay=0.3), mv("n3", [30, 15], delay=0.2), mv("n5", [53, 22], delay=0.3), mv("n2", [64, 20], delay=0.3), mv("r8", [58, 12], delay=0.4)),
     S("Querpass, Minitor: zwei Punkte", "Spieler vier legt quer auf Spieler drei. Der schiebt den Ball ins linke Minitor, und das gibt zwei Punkte für Team Neon.",
       ps("b1", [30.6, 15.6]), ps("b1", [34, 4.7], after=True))],
    goals=TORE, dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Außenverteidiger darf raus.", "Außenverteidiger rückt raus",
    "Verlagern die Angreifer den Ball auf die andere Seite, darf der Außenverteidiger dort die Mittelzone verlassen und pressen. Er muss erkennen, wann er rechtzeitig ankommt. Kommt er zu spät, ist hinter ihm die Lücke offen. Die drei anderen schieben deshalb sofort nach.",
    sp(n3=(31, 30), n4=(40.5, 30), n5=(50, 30), n2=(59.5, 30)), [B("b1", 40.6, 47.6)] + ERSATZ,
    [S("Verlagerung erkennen, raus", "Unten hat Spieler neun den Ball, die Kette steht auf seiner Seite. Spieler zwei sieht, dass der Querpass zu Spieler zehn kommt. Der Ball ist noch unterwegs, da läuft er schon los.",
       bl("n2", [60, 47]), ps("b1", [60.6, 47.6], after=True), mv("n2", [62, 41], delay=1.2),
       mv("n5", [56, 31], delay=1.4), mv("n4", [47, 31], delay=1.4), mv("n3", [38, 30], delay=1.4)),
     S("Pass geblockt, Ball erobert", "Spieler zehn will sofort nach oben durchspielen. Spieler zwei steht schon vor ihm und blockt den Pass. Der Ball gehört Team Neon.",
       ps("b1", [62.6, 41.6])),
     S("Aufs nächste Minitor: zwei Punkte", "Spieler zwei geht mit dem Ball außen an Spieler zehn vorbei und trifft ins rechte Minitor, und das gibt zwei Punkte für Team Neon.",
       dr("n2", "b1", [68, 49]), ps("b1", [65.5, 55.3], after=True), mv("n5", [55, 41], delay=0.3))],
    goals=TORE, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
