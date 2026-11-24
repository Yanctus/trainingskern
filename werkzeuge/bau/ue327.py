import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-111 (U15-U17, Woche 4 Pre-Season): Possession Transfer and Agility Game. 30 x 20 Yards = 27 x 18 m (gerundet 25 x 18 m).
# Feld quer wie im PDF (Verhältnis 1,5): x 9-87, y 5-51, Mittellinie gestrichelt, an beiden schmalen Seiten ein Streifen (im PDF
# weiß, ca. 4 m) mit je einer Minihürde auf der Mittellinie (gestrichelt eingezeichnet). Drei Teams zu viert:
# Gelb (4, 10, 6, 8) -> Team Neon (Ballbesitz, untere Hälfte), Blau (Verteidiger) -> Team Rot (7, 9 pressen; 8 -> 2 und 6 -> 5 an den
# Hürden, neu nummeriert wegen Doppelter), Pink (3, 8, 7, 9; obere Hälfte) -> Springer F wie bei UE-160 und UE-190
# (nur zwei Teams auf der Tafel). Die Springer-Gruppe bleibt deshalb in der Steigerung neutral: gezeigt wird, wie Team Neon den Ball
# verliert und Verteidiger wird (im PDF verliert Pink den Ball). Ein Trainer statt zwei, unten an der Seitenlinie.
# Positionen leicht verschoben (3D-Abstand). Ablauf nach PDF und Video: nach acht Pässen verlagern, dann pressen die beiden
# Hürdenspieler und die beiden Presser gehen an die Hürden; erobert Team Rot den Ball, spielt es ihn sofort zum am weitesten
# entfernten freien Spieler (Video "Fast passes to furthest player").
# Fassungen: PDF Key Coaching Point (Pass außen zugestellt, Verteidiger zu weit auseinander -> Pass durch die Lücke) und Progression
# (Steigerung: wer den Ball verliert, verteidigt; Auslöser schlechte Annahme wie im Ton "pressing triggers").
# Sichtkegel aus Text ("Identify wide gaps", "Recognise when to play through") und Video ("furthest player"): Spieler vier schaut vor
# dem Pass durch die Lücke zum Springer, der Balleroberer schaut zum am weitesten entfernten freien Spieler. Im Video kein Kegel.
FX0, FX1, FY0, FY1 = 9, 87, 5, 51
T = P("T", "c", 31, 55.5, "T")
ERSATZ = [B("s1", 34.5, 56), B("s2", 37, 56)]
POS = {"n4": (48, 48.5), "n10": (23.5, 40), "n6": (75, 44), "n8": (56, 27.5),
       "r7": (36, 37.2), "r9": (65, 41), "r2": (14.5, 31.5), "r5": (81, 24.5),
       "f1": (49.8, 6.5), "f2": (20.8, 15.3), "f3": (67, 14), "f4": (44.5, 27)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(FX0, 28, FX1, 28), line(20.6, FY0, 20.6, FY1), line(75.4, FY0, 75.4, FY1)]
CONES = ecken(FX0, FY0, FX1 - FX0, FY1 - FY0) + [C(14.5, 28, shape="huerde_ou"), C(81, 28, shape="huerde_ou")]
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "18 m", rx=95)
def springen(**k):
    # seitliche Sprünge über die Hürde und zurück
    return [mv("r2", [14.5, 24.5], **k), mv("r2", [14.5, 31.5], after=True), mv("r5", [81, 31.5], **k), mv("r5", [81, 24.5], after=True)]

u = {"title": "Acht Pässe, dann verlagern", "code": "UE-327", "kind": "Spielform",
 "focuses": ["Passspiel", "Verteidigen", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "25 x 18 m",
 "description": "Drei Teams zu viert spielen ein Rondo auf zwei Hälften. Team Neon hat den Ball in der einen Hälfte, die Springer warten in der anderen. Zwei Spieler von Team Rot pressen, die anderen zwei springen seitlich über ihre Hürde. Nach acht Pässen darf verlagert werden, und die Verteidiger tauschen ihre Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 18 Metern, in der Mitte geteilt. An beiden schmalen Seiten ein Streifen von etwa vier Metern, darin liegt auf der Mittellinie je eine Minihürde.",
  "Verteilen: Drei Teams zu viert. Team Neon steht in der einen Hälfte, die Springer in der anderen, von jedem Team einer an der Mittellinie. Von Team Rot pressen zwei, die anderen zwei stehen an den Hürden. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Vier gegen zwei in einer Hälfte. Nach acht Pässen darf der Ball in die andere Hälfte. Dann pressen dort die zwei von den Hürden, und die anderen zwei gehen an die Hürden. Erobert Team Rot den Ball, spielt es ihn sofort zum am weitesten entfernten freien Spieler.",
  "Wechsel: Jede Runde dauert fünf Minuten, dann wird ein anderes Team Verteidiger. Ziel ist, so oft wie möglich acht Pässe zu schaffen und zu verlagern."],
 "organisation_show": ORG,
 "coaching_points": ["Lücke zwischen den Verteidigern sehen und durchspielen", "Anbieten und freilaufen, damit immer einer frei ist", "Von der Hürde sofort explosiv ins Pressing", "Schlechte Annahme beim Gegner: sofort drauf"],
 "materials": ["2 Minihürden", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Acht Pässe, dann verlagern. Ein Rondo auf zwei Hälften für die Vorbereitung. Zwei Verteidiger pressen, zwei springen an der Hürde, und nach acht Pässen geht der Ball rüber.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 48.6, 49.1)] + ERSATZ,
  "steps": [
   S("Vier gegen zwei in einer Hälfte", "Team Neon hat den Ball in seiner Hälfte, die Springer warten drüben. Spieler sieben und Spieler neun von Team Rot pressen. Die anderen zwei von Team Rot springen gleichzeitig seitlich über ihre Hürde.",
     ps("b1", [24.1, 40.6]), mv("r7", [29, 44], delay=0.3), mv("r9", [62, 38], delay=0.3), *springen()),
   S("Acht Pässe zählen", "Flach und schnell weiter. Spieler zehn spielt zu Spieler acht an der Mittellinie, der gleich weiter zu Spieler sechs. Jeder Pass zählt, Team Neon braucht acht.",
     ps("b1", [56.6, 28.1]), ps("b1", [75.6, 44.6], after=True), mv("r9", [79, 38], delay=0.6), *springen()),
   S("Acht Pässe: verlagern", "Acht Pässe sind geschafft. Jetzt darf Team Neon verlagern. Spieler sechs spielt den langen Ball rüber zu den Springern.",
     ps("b1", [50.4, 7.1])),
   S("Die Hürdenspieler pressen", "Sofort tauschen die Rollen. Spieler zwei und Spieler fünf kommen von den Hürden und pressen die Springer. Spieler sieben und Spieler neun gehen an die Hürden. Drüben läuft der Ball schon weiter.",
     mv("r2", [31, 17]), mv("r5", [58, 18]), mv("r7", [19, 48]), mv("r7", [14.5, 35], after=True), mv("r9", [81, 31.5]), ps("b1", [21.4, 15.9], delay=0.4)),
   S("Ball erobert, weit spielen", "Spieler zwei erobert den Ball. Er schaut sofort, wer am weitesten weg und frei ist, das ist Spieler vier, und spielt ihn an. Jetzt pressen Spieler sieben und Spieler neun wieder in der Hälfte von Team Neon. Nach fünf Minuten wird ein anderes Team Verteidiger.",
     mv("r2", [22.8, 17.2]), bl("r2", [32, 33], after=True), ps("b1", [48.6, 49.1], after=True),
     mv("r7", [38, 40], after=True), mv("r9", [62, 42], delay=0.3))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Durch die Lücke spielen.", "Durch die Lücke spielen",
    "Stellt ein Verteidiger den Pass nach außen zu, steht er oft weit weg von seinem Partner. Dann ist in der Mitte eine Lücke. Wer sie sieht, spielt durch und überspielt beide auf einmal.",
    sp(r7=(35, 39.5), r9=(57, 46)), [B("b1", 48.6, 49.1)] + ERSATZ,
    [S("Der Pass nach außen ist zu", "Spieler vier hat den Ball. Spieler neun stellt den Pass zu Spieler sechs zu. Spieler sieben steht aber weit weg, in der Mitte ist eine Lücke.",
       opt("n4", [75, 44]), mv("r9", [61, 45], delay=0.3)),
     S("Durch die Lücke zum Springer", "Spieler vier sieht die Lücke und spielt flach durch zum Springer an der Mittellinie. Der legt direkt auf Spieler acht ab. Beide Verteidiger sind überspielt.",
       bl("n4", [45, 28]), ps("b1", [45.1, 27.6], after=True), ps("b1", [56.6, 28.1], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball verliert, verteidigt.", "Wer verliert, verteidigt",
    "Erobert Team Rot den Ball und bringt ihn rüber zu den Springern, wird Team Neon zum Verteidiger. Zwei pressen sofort, zwei gehen an die Hürden. Das Signal zum Pressen ist ein schlechter Pass oder eine schlechte Annahme.",
    sp(r7=(32.5, 40)), [B("b1", 24.1, 40.6)] + ERSATZ,
    [S("Schlechte Annahme: Rot presst", "Spieler zehn springt der Ball zu weit vom Fuß. Das ist das Signal. Spieler sieben ist sofort da und erobert den Ball.",
       ps("b1", [29.5, 44]), mv("n10", [26, 42], delay=0.2), mv("r7", [28.9, 43.4], delay=0.3)),
     S("Weit rüber zu den Springern", "Spieler sieben schaut hoch und spielt den Ball weit rüber zu den Springern.",
       bl("r7", [38.8, 26]), ps("b1", [50.4, 7.1], after=True)),
     S("Team Neon wird Verteidiger", "Jetzt verteidigt Team Neon. Spieler acht und Spieler vier pressen bei den Springern, Spieler zehn und Spieler sechs gehen an die Hürden. Team Rot kommt in die Hälfte und spielt mit den Springern zusammen.",
       mv("n8", [44, 13]), mv("n4", [57, 20]), mv("n10", [14.5, 33]), mv("n6", [81, 31.5]),
       mv("r2", [21, 45], delay=0.2), mv("r5", [70, 46], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
