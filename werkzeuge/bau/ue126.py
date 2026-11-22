import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P45: 25 x 20 Yards, gedreht: Feld x 10-90, y 8-52, Endzonen links (x 10-26) und rechts (x 74-90), Minitore links und rechts.
T = P("T", "c", 70, 2, "T")
CB = [B("c1", 72.5, 2.6)]
POS = {"n9": (24, 26), "r2": (24, 44), "r3": (33, 35), "n7": (42, 18), "n8": (42, 46), "r6": (51, 32), "r11": (56, 16), "n5": (66, 26), "r10": (60, 46), "n4": (70, 42)}
def sp(d=None):
    d = dict(d or POS)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
Z = [{"type": "zone", "x": 10, "y": 8, "w": 16, "h": 44}, {"type": "zone", "x": 74, "y": 8, "w": 16, "h": 44}]
LINES = [rect(10, 8, 80, 44)] + Z
TORE = [{"x": 10, "y": 30, "side": "left"}, {"x": 90, "y": 30, "side": "right"}]
u = {"title": "In die Zone und herausdrehen", "code": "UE-126", "kind": "Spielform",
 "focuses": ["Dribbling", "1 gegen 1", "Torschuss"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 8, "players_max": 10, "field_size": "23 x 18 m",
 "description": "Zwei Teams spielen fünf gegen fünf auf ein Feld mit einer Endzone an jedem Ende. Das Team am Ball versucht, dass ein Kind mit Ball in eine Endzone dribbelt und sich schnell wieder herausdreht, obwohl ein Gegner folgen darf. Danach greift es das andere Ende an und schießt aufs Minitor.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern mit einer Endzone von etwa 4,5 Metern an jedem Ende und einem Minitor links und rechts.",
  "Verteilen: Zwei Teams mit je fünf Kindern, Team Neon und Team Rot. Der Trainer hat Bälle am Rand.",
  "Ablauf: Team Neon will mit einem Kind in eine Endzone dribbeln und sich schnell wieder herausdrehen. In die Endzone darf nur ein Gegner folgen. Danach geht es zum anderen Ende, und dort wird aufs Minitor geschossen.",
  "Wechsel: Für das Herausdrehen gibt es einen Punkt, für das Tor danach zwei Punkte. Dann greift Team Rot an."],
 "organisation_show": ORG,
 "coaching_points": ["In der Endzone schnell drehen, um dem Gegner zu entkommen", "Vor dem Drehen über die Schulter schauen und in die andere Richtung drehen", "Mutig dribbeln und das eins gegen eins suchen", "Genau aufs Tor schießen, miteinander sprechen und sich verteilen"],
 "materials": ["2 Minitore", "Hütchen für Feld und Endzonen", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "In die Zone und herausdrehen. Erst in der Endzone drehen, dann am anderen Ende aufs Tor schießen.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 71.6, 42.6)] + CB,
  "steps": [
   S("Pass nach vorn", "Spieler vier spielt einen langen Pass zu Spieler sieben.",
     ps("b1", [43.6, 18.6])),
   S("In die Endzone und raus", "Spieler sieben dribbelt in die linke Endzone. Spieler drei folgt ihm, doch Spieler sieben dreht scharf und dribbelt wieder heraus. Das gibt einen Punkt für Team Neon.",
     dr("n7", "b1", [22, 16]), mv("r3", [26, 22], delay=0.3), dr("n7", "b1", [30, 11], after=True)),
   S("Am anderen Ende abschließen", "Jetzt spielt Spieler sieben weit zu Spieler fünf, und Spieler fünf schießt ins rechte Minitor. Das gibt zwei Punkte für Team Neon.",
     ps("b1", [64.4, 26.6]), ps("b1", [89.5, 31], after=True))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "23 m"}, {"x1": 96, "y1": 8, "x2": 96, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Scharf drehen und den Ball abschirmen.", "Scharf drehen",
    "In der Endzone dreht das Kind mit Ball scharf und hält den Ball eng am Fuß. Den Körper stellt es zwischen Ball und Gegner, damit der Gegner nicht an den Ball kommt. Dann geht es schnell aus der Zone in den freien Raum.",
    sp(dict(POS, n7=(20, 16), r3=(29, 24), n9=(32, 42), r2=(18, 46))), [B("g", 21.6, 16.6)] + CB,
    [S("Gegner kommt", "Spieler drei kommt in die Endzone und greift Spieler sieben an. Spieler sieben stellt seinen Körper dazwischen.",
       mv("r3", [25, 20])),
     S("Drehen und raus", "Spieler sieben dreht scharf weg und dribbelt aus der Zone in den freien Raum. Das gibt einen Punkt für Team Neon.",
       dr("n7", "g", [17, 11]), dr("n7", "g", [32, 9], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Vor dem Drehen über die Schulter schauen.", "Erst schauen, dann drehen",
    "Bevor das Kind in der Endzone dreht, schaut es über die Schulter. So sieht es, auf welcher Seite der Gegner kommt, und dreht in die andere Richtung. Dort ist Platz, und der Ball bleibt sicher.",
    sp(dict(POS, n7=(32, 28), r3=(21, 40), n9=(42, 10), r2=(12, 48))), [B("g", 33.6, 28.6)] + CB,
    [S("Schulterblick", "Spieler sieben dribbelt in die Endzone und schaut über die Schulter. Spieler drei kommt von unten.",
       dr("n7", "g", [22, 28]), mv("r3", [21, 35], delay=0.2)),
     S("In die andere Richtung", "Spieler sieben dreht nach oben weg, also auf die Seite ohne Gegner, und dribbelt aus der Zone. Das gibt einen Punkt für Team Neon.",
       dr("n7", "g", [24, 18]), dr("n7", "g", [32, 20], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
