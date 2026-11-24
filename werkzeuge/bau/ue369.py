import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 61-P11 (U15-U17, Woche 25 Phase 1): 5 v 4 + 3 Possession Transfer Rondo (Ordnername "4 v 4 3 Possession Transfer Rondo").
# 45 x 30 Yards nach Text und Ton = 41 x 27 m, gerundet 40 x 25 m (die Skizze schreibt 35 Yards an die Breite; Text und Ton gehen vor).
# LANGES FELD QUER (Vorbild ue317.py): Im PDF hochkant, die Aufbauhälfte unten, die Stürmerhälfte oben. Quer: Aufbauhälfte links,
# Stürmerhälfte rechts, Feld x 9-87, y 4-51 (fast gleicher Maßstab in beiden Richtungen), Mittellinie gestrichelt bei x 48.
# Gelb (Ballbesitz, 4-3-3) -> Team Neon, Nummern wie im Video (4, 3, 2, 10, 8 links; 7, 9, 11 rechts). Blau -> Team Rot,
# neu nummeriert wegen doppelter Nummern: oben im PDF 5 und 6 bleiben, 4 -> 12, 8 -> 13; unten 11 -> 14, 9 -> 15, 10 -> 16, 7 -> 17.
# Drei Springer (pink F): einer in der Mitte der Aufbauhälfte, zwei außen an der Mittellinie (die "wide floaters").
# Positionen auf ein Spaltenraster gesetzt (3D-Abstand). Ein Trainer statt zwei, unten an der Seitenlinie.
# Grundform nach Video (0:12-0:30): 4 -> 2 -> Springer Mitte -> 10 -> Springer außen -> 7, dazu schieben 10, 8 und der mittlere
# Springer in die andere Hälfte (gestrichelte Pfeile im Video). Die zehn Pässe stehen nur im Text.
# Fassungen wie die PDF-Progressionen: 1 Zonen (je Hälfte zwei mal drei, gestrichelt; zwei Spieler von Team Neon in einer Zone geben
# einen Punkt für Team Rot, wie im Ton), 2 ein zusätzlicher Verteidiger von der anderen Seite presst; Ballgewinn mit Pass zum Springer
# außen gibt einen Punkt für Team Rot (Ton: Team Rot darf den Ball behalten und selbst verlagern).
# Sichtkegel: Text "Constant scanning for floaters to switch play": Spieler 10 schaut zum Springer in der Mitte, nimmt an und
# schwenkt dann zum Springer außen (bl mit von, Drehpfeil). In der zweiten Steigerung ("Defenders must react quickly after regaining
# possession to find a floater") schaut Spieler 17 nach der Annahme zum Springer außen.
# Keine Dublette: UE-125 (61-P4) und UE-201 (61-P6) sind andere Übungen (Prallen und Abdrehen bzw. Spiel in sechs Feldern).
FX0, FX1, FY0, FY1, MX = 9, 87, 4, 51, 48
T = P("T", "c", 57.5, 55.3, "T")
ERSATZ = [B("s1", 61, 55.8), B("s2", 63.5, 55.8)]
NEON = {"n4": (10.5, 27.5), "n3": (19, 8), "n2": (19, 47), "n10": (40, 11.5), "n8": (40, 44.5), "n7": (77.5, 9), "n9": (85, 27.5), "n11": (77.5, 46)}
ROT = {"r14": (19, 27.5), "r15": (31.5, 11), "r16": (31.5, 44), "r17": (40, 28), "r13": (57, 27.5), "r5": (65.5, 14), "r6": (66, 40), "r12": (74.5, 27.5)}
FS = {"fm": (31.5, 27.5), "fo": (48.5, 4.5), "fu": (48.5, 50.5)}
POS = {**NEON, **ROT, **FS}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "F") if i[0] == "f" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(i): return [round(POS[i][0] + 0.6, 1), round(POS[i][1] + 0.6, 1)]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1)]
ZY = [round(FY0 + (FY1 - FY0) / 3, 1), round(FY0 + 2 * (FY1 - FY0) / 3, 1)]
ZONEN = LINES + [line(28.5, FY0, 28.5, FY1), line(67.5, FY0, 67.5, FY1)] + [line(FX0, y, FX1, y) for y in ZY]
CONES = [C(FX0, FY0), C(MX, FY0), C(FX1, FY0), C(FX0, FY1), C(MX, FY1), C(FX1, FY1)]
DIMS = dims(FX0, FX1, FY0, FY1, "40 m", "25 m", rx=93)
FM_WEG = [[35, 36], [45, 36], [52, 32]]

u = {"title": "Zehn Pässe, dann verlagern", "code": "UE-369", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 19, "players_max": 19,
 "field_size": "40 x 25 m",
 "description": "Ein Rondo in zwei Hälften, so wie Team Neon im Vier-Drei-Drei aufbaut. In der einen Hälfte spielen fünf Spieler mit drei Springern gegen vier, in der anderen warten die drei Stürmer gegen vier Verteidiger. Nach zehn Pässen in Folge geht der Ball über einen Springer außen auf die andere Seite, und zwei Mittelfeldspieler schieben mit. Erobert Team Rot den Ball, sucht es sofort einen Springer außen.",
 "organisation": ["Aufbauen: Ein Feld von 40 mal 25 Metern, in der Mitte in zwei gleich große Hälften geteilt.",
  "Verteilen: In der Aufbauhälfte stehen fünf Spieler von Team Neon gegen vier von Team Rot, in der anderen Hälfte die drei Stürmer von Team Neon gegen vier Verteidiger. Ein Springer steht in der Mitte der Aufbauhälfte, je einer außen an der Mittellinie. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Team Neon spielt mit den Springern zehn Pässe in Folge. Dann geht der Ball über einen Springer außen in die andere Hälfte. Zwei Mittelfeldspieler und der Springer aus der Mitte schieben mit, und drüben geht es wieder fünf gegen vier plus drei. Erobert Team Rot den Ball, spielt es schnell zu einem Springer außen.",
  "Wertung und Wechsel: Jeder gelungene Seitenwechsel gibt einen Punkt für Team Neon. Ein Ballgewinn mit Pass zum Springer außen gibt einen Punkt für Team Rot. Der Trainer zählt mit und tauscht nach einigen Minuten Angreifer und Verteidiger."],
 "organisation_show": ORG,
 "coaching_points": ["Breit stehen, das Feld groß machen", "Schnell und genau passen, ein oder zwei Kontakte", "Kopf hoch: Wo steht der Springer außen?", "Ball erobert? Sofort den Springer suchen"],
 "materials": ["6 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zehn Pässe, dann verlagern. Ein Rondo in zwei Hälften. Team Neon hält den Ball, und nach zehn Pässen geht er über einen Springer auf die andere Seite.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *f("n4"))] + ERSATZ,
  "steps": [
   S("Fünf gegen vier plus drei", "Team Neon hat in der Aufbauhälfte den Ball. Fünf Spieler und drei Springer gegen vier von Team Rot. Spieler vier spielt raus zu Spieler zwei, und der legt auf den Springer in der Mitte.",
     ps("b1", f("n2")), ps("b1", f("fm"), after=True)),
   S("Zehn Pässe, dann zu zehn", "So läuft der Ball, bis zehn Pässe in Folge geschafft sind. Jetzt spielt der Springer zu Spieler zehn. Der schaut zum Ball, bis er ihn hat.",
     bl("n10", POS["fm"]), ps("b1", f("n10"), after=True)),
   S("Aufdrehen, raus zum Springer", "Mit dem ersten Kontakt dreht Spieler zehn auf. Sein Blick geht sofort zum Springer außen an der Mittellinie, und da spielt er hin.",
     bl("n10", POS["fo"], von=POS["fm"], dauer=1.3), drehen("n10", POS["fo"], delay=0.4), ps("b1", f("fo"), after=True)),
   S("Seitenwechsel: Punkt", "Der Springer spielt den langen Ball rüber zu Spieler sieben. Der Seitenwechsel gibt einen Punkt für Team Neon. Spieler zehn, Spieler acht und der Springer aus der Mitte schieben mit rüber, und drüben geht es wieder mit zehn Pässen weiter.",
     ps("b1", f("n7")), mv("n10", [56.5, 12], delay=0.3), mv("n8", [56.5, 44.5], delay=0.3),
     mv("fm", FM_WEG[0], delay=0.3), *[mv("fm", p, after=True) for p in FM_WEG[1:]])],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Das Feld ist in Zonen geteilt.", "Ein Spieler pro Zone",
    "Jede Hälfte ist in sechs Zonen geteilt. In jeder Zone darf nur ein Spieler von Team Neon stehen, die Springer und Team Rot dürfen überall hin. Stehen zwei von Team Neon in einer Zone, gibt das einen Punkt für Team Rot. Der Trainer unterbricht nicht, die Spieler regeln das selbst.",
    sp(), [B("b1", *f("n2"))] + ERSATZ,
    [S("Breit in den Zonen", "Spieler zwei spielt zum Springer in der Mitte. Spieler zehn und Spieler acht gehen in ihren Zonen ganz nach außen und machen das Feld breit.",
       ps("b1", f("fm")), mv("n10", [43, 8], delay=0.2), mv("n8", [43, 47], delay=0.2)),
     S("Zwei in einer Zone: Punkt für Rot", "Spieler drei kommt nach innen und will sich anbieten. Aber in dieser Zone steht schon Spieler vier. Zwei in einer Zone, das gibt einen Punkt für Team Rot.",
       mv("n3", [22, 22])),
     S("Besser: in der eigenen Zone", "Besser so. Spieler drei bleibt außen in seiner Zone. Dort hat er Platz und bekommt den Ball vom Springer.",
       mv("n3", list(POS["n3"])), ps("b1", f("n3"), after=True))], lines=ZONEN),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Verteidiger mehr presst.", "Ein Verteidiger mehr",
    "Ein Verteidiger von der anderen Seite darf jetzt mit rüber und pressen. Team Neon hat weniger Zeit. Die Spieler müssen sich schneller anbieten oder mit einem längeren Pass den freien Springer suchen. Erobert Team Rot den Ball, behält es ihn und verlagert selbst über einen Springer.",
    sp(), [B("b1", *f("n2"))] + ERSATZ,
    [S("Spieler dreizehn kommt rüber", "Spieler zwei spielt zum Springer in der Mitte. Sofort kommt Spieler dreizehn von der anderen Seite rüber und presst mit.",
       ps("b1", f("fm")), mv("r13", [47, 18], delay=0.2)),
     S("Ball erobert", "Der Springer spielt zu Spieler zehn. Spieler dreizehn ist schon da, geht dazwischen und erobert den Ball.",
       ps("b1", f("n10")), mv("r13", [41.5, 14.5], delay=0.4), dr("r13", "b1", [44, 19], after=True)),
     S("Ablegen auf siebzehn", "Spieler dreizehn legt sofort ab auf Spieler siebzehn. Der schaut zum Ball, bis er ihn hat.",
       bl("r17", [44, 19]), ps("b1", f("r17"), after=True)),
     S("Schnell zum Springer: Punkt", "Spieler siebzehn dreht auf, sieht den Springer außen und spielt hin. Das gibt einen Punkt für Team Rot. Jetzt hat Team Rot den Ball und verlagert selbst.",
       bl("r17", POS["fu"], von=[44, 19], dauer=1.3), drehen("r17", POS["fu"], delay=0.4), ps("b1", f("fu"), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
