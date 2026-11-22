import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 61-P6 (U12-U14, Woche 25 Phase 1): Protect Possession to Build Attacks SSG (PDF: How to Protect Possession & 1 v 1's).
# 35 x 45 Yards = Feld x 30.55-69.45, y 5-55 (32 x 41 m), sechs gleiche Felder (gestrichelt), je zwei Minitore oben und unten.
# Um 180 Grad gedreht, damit nach oben angegriffen wird. Pink (Angreifer, 4, 5, 6, 8, 9, 10) -> Neon, Nummern wie im Video.
# Gelb -> Rot, neu nummeriert wegen doppelter Nummern: Gelb 9 -> Rot 2, Gelb 8 -> Rot 3, Gelb 5 -> Rot 12, Gelb 6 -> Rot 14
# (Gelb 7 und 11 bleiben). In jedem Feld Neon innen, Rot außen und etwas zum Tor hin versetzt (3D-Abstand). Ein Trainer statt zwei.
# Grundform nach PDF/Video (0:03-0:19): 6 -> 8 (drei Sekunden abschirmen) -> 4 -> 10, Eins gegen Eins und Abschluss.
# Fassungen = Coaching-Punkt 1 (abschirmen und abdrücken) und 2 (Gegner wegziehen, Video 0:56-1:10). In Fassung 2 tauschen
# Neon 8 und Rot 3 die Plätze, damit Rot 3 im Passweg steht.
# Sichtkegel: kein Kegel im Video eingezeichnet, aber im Text "Head up to spot teammates movement" und "Check shoulders" und im
# Ton "Scanning early": Neon 8 schaut beim Abschirmen zu Neon 4 (Grundform), Neon 10 schaut vor dem Pass über die Schulter (Fassung 2).
T = P("T", "c", 22, 30, "T")
POS = {"n10": (44.8, 15.3), "r14": (35.8, 10.3), "n9": (55.2, 15.3), "r12": (64.2, 10.3),
       "n8": (44.8, 32), "r3": (35.8, 27), "n4": (55.2, 32), "r11": (64.2, 27),
       "n5": (44.8, 48.7), "r7": (35.8, 43.7), "n6": (55.2, 48.7), "r2": (64.2, 43.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 33.5), B("s2", 20, 33.5)]
X0, X1, Y0, Y1 = 30.55, 69.45, 5, 55
LINES = [rect(X0, Y0, X1 - X0, Y1 - Y0), line(50, Y0, 50, Y1), line(X0, 21.67, X1, 21.67), line(X0, 38.33, X1, 38.33)]
CONES = ecken(X0, Y0, X1 - X0, Y1 - Y0) + [C(X0, 21.67), C(X1, 21.67), C(X0, 38.33), C(X1, 38.33), C(50, Y0), C(50, Y1)]
TORE = [{"x": 40.3, "y": Y0, "side": "top"}, {"x": 59.7, "y": Y0, "side": "top"},
        {"x": 40.3, "y": Y1, "side": "bottom"}, {"x": 59.7, "y": Y1, "side": "bottom"}]

u = {"title": "Ball behaupten und durchsetzen", "code": "UE-201", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Dribbling", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "32 x 41 m",
 "description": "Ein Spiel in sechs Feldern mit je einem Spieler von Team Neon und einem von Team Rot. Wer den Ball bekommt, muss ihn drei Sekunden lang abschirmen, bevor er weiterpasst oder im Eins gegen Eins aufs Minitor geht. Erobert der Verteidiger den Ball, schirmt er selbst ab und spielt mit seinem Team auf die anderen Tore. So lernen die Kinder, den Ball mit dem Körper zu schützen und sich durchzusetzen.",
 "organisation": ["Aufbauen: Ein Feld von 32 mal 41 Metern in sechs gleich großen Feldern. Oben und unten stehen je zwei Minitore.",
  "Verteilen: In jedem Feld ein Spieler von Team Neon und einer von Team Rot. Team Neon greift nach oben an, Team Rot nach unten. Der Trainer steht links mit Bällen.",
  "Ablauf: Team Neon beginnt mit dem Ball. Wer angespielt wird, schirmt drei Sekunden ab. Dann passt er zu einem Mitspieler oder geht im Eins gegen Eins aufs Minitor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobert Rot den Ball, schirmt Rot drei Sekunden ab und greift auf die unteren Tore an. Nach einigen Minuten wechseln alle das Feld."],
 "organisation_show": ORG,
 "coaching_points": ["Den Körper zwischen Ball und Gegner bringen und den Ball abschirmen", "Kopf hoch und über die Schulter schauen: Wo sind Mitspieler und Gegner?", "Mutig ins Eins gegen Eins gehen und abschließen", "Ohne Ball klug laufen und den Gegner wegziehen"],
 "materials": ["4 Minitore", "10 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Ball behaupten und durchsetzen. In sechs Feldern spielt jeder gegen einen Gegner und muss den Ball erst drei Sekunden abschirmen.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 55.8, 49.3)] + ERSATZ,
  "steps": [
   S("Anspiel", "Team Neon hat den Ball. Neon sechs passt schräg zu Neon acht. Rot drei läuft sofort hin und drückt.",
     ps("b1", [45.4, 32.6]), mv("r3", [40.5, 30], delay=0.4)),
   S("Drei Sekunden abschirmen", "Neon acht stellt den Körper zwischen Ball und Gegner und hält den Ball drei Sekunden. Dabei hebt er den Kopf und sieht, dass Neon vier frei ist.",
     dr("n8", "b1", [47, 35]), bl("n8", [62, 28], after=True)),
   S("Weiter zu Neon vier", "Neon acht spielt quer zu Neon vier. Rot elf drückt, aber auch Neon vier schirmt den Ball drei Sekunden ab.",
     ps("b1", [55.8, 32.6]), mv("r11", [60, 30], delay=0.4), dr("n4", "b1", [53, 35], after=True)),
   S("Hoch zu Neon zehn", "Dann spielt Neon vier hoch zu Neon zehn. Der steht jetzt im Eins gegen Eins mit Rot vierzehn.",
     ps("b1", [45.4, 15.9]), mv("r14", [42, 11.5], delay=0.4)),
   S("Eins gegen eins: Punkt", "Neon zehn schirmt ab, dreht sich schnell an Rot vierzehn vorbei und schießt ins Minitor. Das gibt einen Punkt für Team Neon. Dann bekommt Team Rot einen neuen Ball vom Trainer und greift auf die unteren Tore an.",
     dr("n10", "b1", [49, 10]), ps("b1", [41.5, 4.7], after=True))],
  "dims": dims(X0, X1, Y0, Y1, "32 m", "41 m", rx=77.5)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Abschirmen und abdrücken.", "Abschirmen und abdrücken",
    "Mit Körper und Arm hält der Spieler den Gegner auf Abstand. Er bleibt tief in den Knien und hält das Gleichgewicht. Im richtigen Moment drückt er sich ab, schafft sich Platz und schließt ab.",
    sp(), [B("b1", 45.4, 15.9)] + ERSATZ,
    [S("Abschirmen", "Neon zehn hat den Ball, Rot vierzehn drückt von hinten. Neon zehn macht sich breit, hält den Gegner mit Körper und Arm weg und schirmt den Ball ab.",
       mv("r14", [43.5, 11.5]), dr("n10", "b1", [47, 17], delay=0.3)),
     S("Abdrücken: Punkt", "Im richtigen Moment drückt sich Neon zehn ab, dreht sich weg und schießt ins Minitor. Das gibt einen Punkt für Team Neon.",
       dr("n10", "b1", [51, 12]), ps("b1", [41.5, 4.7], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Gegner wegziehen.", "Den Gegner wegziehen",
    "Ohne Ball klug laufen: Ein Spieler läuft weg und nimmt seinen Gegner mit. So wird der Passweg frei, und der vorderste Spieler bekommt den Ball. Vorher schaut er über die Schulter, damit er weiß, wo sein Gegner steht.",
    sp(n8=(35.8, 27), r3=(44.8, 31)), [B("b1", 45.4, 49.3)] + ERSATZ,
    [S("Wegziehen", "Neon fünf hat den Ball. Neon acht läuft schräg nach außen und zieht Rot drei mit. Jetzt ist der Weg nach oben frei. Neon zehn schaut über die Schulter, wo Rot vierzehn steht.",
       mv("n8", [33.5, 35]), mv("r3", [39, 34], delay=0.3), bl("n10", [37, 2], after=True)),
     S("Frei anspielen: Punkt", "Neon fünf spielt den langen Pass zu Neon zehn. Der weiß schon, wo sein Gegner steht, dreht sich weg und schießt ins Minitor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [45.4, 15.9]), dr("n10", "b1", [50, 11], after=True), ps("b1", [41.5, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
