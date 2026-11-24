import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-110 (U15-U17, Woche 5 Pre-Season): Dribbling, Passing and SAQ. 45 x 50 Yards = 41 x 46 m (gerundet 40 x 45 m).
# UM 90 GRAD GEDREHT (im Uhrzeigersinn): Im PDF steht das Minitor links, hier oben (Tor oben). Aus der PDF-Skizze umgerechnet:
# PDF links -> oben, PDF oben -> rechts, PDF unten -> links, PDF rechts -> unten. Feld x 21-79 (45 m), y 4-55 (40 m), gleicher
# Maßstab in beiden Richtungen. Stangen-Slalom läuft damit von oben nach unten, die Hürden unten von links nach rechts, die
# Leiter rechts von unten nach oben. Dummys (Mannequins) als Stangen gezeichnet. Nummern wie im PDF (nur ein Team, Neon).
# Die Wartenden 11 und 7 stehen links neben dem Feld, Spieler 5 rechts neben dem Feld, Spieler 9 etwas weiter von 2 weg
# (3D-Abstand). Ein Trainer statt zwei (links neben dem Feld). Stangen in einer Reihe statt leicht versetzt.
# Ablauf nach PDF (Organisation 1-3), Ton und Video: Slalom -> Pass und Ablage mit 8 -> Pass am Dummy vorbei, 8 läuft um den Dummy
# -> 8 zentral auf 2, 8 über die Hürden -> 2 quer auf 6, 2 sprintet zum Dummy und tippt ihn an -> 6 legt für 8 ab -> 8 auf 2 ->
# 6 durch die Leiter -> Steilpass von 2 -> Abschluss ins Minitor. Wechsel im PDF nur „before rotating positions“: Weiterrücken
# einer Station ergänzt (Slalom -> Ablegen -> Hürden/Leiter -> Start), in der Mitte wechseln sich 2 und 9 ab.
# Sichtkegel aus Text („scan often“, „Back Foot Receiving – Open body“): Spieler 2 schaut zum Passgeber 8, nimmt an, dann schwenkt
# derselbe Kegel zu Spieler 6 (bl mit von) und er dreht mit dem Drehpfeil auf. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 11, 40, "T")
ERSATZ = [B("s1", 8.5, 45), B("s2", 13.5, 45.5)]
POS = {"n3": (29, 6), "n11": (13, 6), "n7": (13, 22), "n8": (31, 51), "n9": (40, 12), "n2": (49, 28), "n6": (65, 48.5), "n5": (87, 50)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
STANGEN = [(31.5, 11), (31.5, 18), (31.5, 25), (31.5, 32)]
D_UNTEN, D_OBEN, D_MITTE = (37.2, 42.6), (50.2, 6.1), (61, 36.7)
HUERDEN = [(46, 49.5), (49, 49.5), (52, 49.5), (55, 49.5)]
CONES = [C(x, y, shape="stange") for x, y in STANGEN + [D_UNTEN, D_OBEN, D_MITTE]] + [C(x, y, shape="huerde") for x, y in HUERDEN] \
    + [leiter(68.3, 37, senkrecht=True), C(26, 6, "neon"), C(34.5, 52.5, "neon"), C(71.5, 49.5, "neon"), C(45.5, 30, "neon")]
LINES = [rect(21, 4, 58, 51)]
TOR = [{"x": 65.9, "y": 4, "side": "top"}]
DIMS = dims(21, 79, 4, 55, "45 m", "40 m", rx=94)
def weg(who, pkt, **k): return [mv(who, list(pkt[0]), **k)] + [mv(who, list(p), after=True) for p in pkt[1:]]
def dweg(who, ball, pkt, **k): return [dr(who, ball, list(pkt[0]), **k)] + [dr(who, ball, list(p), after=True) for p in pkt[1:]]
SLALOM = [(28, 11), (35, 18), (28, 25), (35, 32), (33, 36)]
UM_DUMMY = [(38, 48.5), (43, 44)]
HUERDENWEG = [(44, 49.5), (57.5, 49.5), (58, 51.5)]
LEITERWEG = [(68.3, 46.5), (68.3, 28), (67.2, 22.9)]
BAELLE = [B("b1", *f(POS["n3"])), B("b11", *f(POS["n11"])), B("b7", *f(POS["n7"]))] + ERSATZ
# Stand vor dem Steilpass (Start der Fassungen)
NACH = {"n3": (33, 36), "n8": (58, 51.5), "n2": (53, 27)}

u = {"title": "Passzirkel mit Hürden und Leiter", "code": "UE-331", "kind": "Übungsform",
 "focuses": ["Passspiel", "Dribbling", "Schnelligkeit"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "45 x 40 m",
 "description": "Ein Zirkel für die Vorbereitung, in dem Technik und Laufarbeit ineinandergreifen. Es beginnt mit einem Slalom durch Stangen und einem Doppelpass um einen Dummy. Danach läuft der Ball über die Mitte und die Seite, während die Spieler über Hürden springen, zum Dummy sprinten und durch die Leiter gehen. Am Ende steht ein Steilpass und der Abschluss ins Minitor.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 40 Metern mit einem Minitor. Am Start vier Stangen für den Slalom, daneben ein Dummy. Unten vier Minihürden, rechts eine Leiter, ein Dummy in der Mitte und einer oben nahe dem Tor. Hütchen markieren die Stationen.",
  "Verteilen: Mindestens acht Spieler. Drei mit Ball am Start, einer zum Ablegen unten, zwei in der Mitte, zwei an der Leiter. Der Trainer steht mit Ersatzbällen neben dem Feld.",
  "Ablauf: Slalom, Doppelpass und Pass am Dummy vorbei. Der Ball geht in die Mitte, dann quer zur Leiter-Station und wieder zurück in die Mitte. Dazwischen springen, sprinten und laufen die Spieler durch die Geräte. Zum Schluss Steilpass und Abschluss.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für den Schützen. Danach rückt jeder eine Station weiter, vom Slalom zum Ablegen, vom Ablegen über die Hürden zur Leiter, nach dem Abschluss zurück an den Start. In der Mitte wechseln sich zwei Spieler ab."],
 "organisation_show": ORG,
 "coaching_points": ["Früh da sein, bevor der Ball kommt", "Offen stehen und mit dem hinteren Fuß annehmen", "In den Lauf passen, nicht in die Füße", "Sauber bleiben, auch wenn die Beine schwer werden"],
 "materials": ["1 Minitor", "4 Stangen", "3 Dummys", "4 Minihürden", "1 Koordinationsleiter", "4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passzirkel mit Hürden und Leiter. Technik und Laufarbeit wechseln sich ab, bis am Ende der Abschluss ins Minitor kommt.",
 "board": {"lines": LINES, "goals": TOR, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Slalom und Doppelpass", "Spieler drei startet mit Ball und dribbelt im Slalom durch die Stangen. Dann spielt er zu Spieler acht. Der kommt kurz entgegen und legt direkt zurück.",
     *dweg("n3", "b1", SLALOM), ps("b1", f(POS["n8"]), after=True), ps("b1", f(NACH["n3"]), after=True)),
   S("Am Dummy vorbei", "Jetzt geht der Ball auf der einen Seite am Dummy vorbei. Spieler acht läuft auf der anderen Seite herum und holt ihn sich.",
     ps("b1", f(UM_DUMMY[1])), *weg("n8", UM_DUMMY, delay=0.1)),
   S("Zentral auf Spieler zwei", "Spieler zwei schaut zum Ball. Spieler acht spielt ihn flach in die Mitte und geht sofort über die Hürden.",
     bl("n2", f(UM_DUMMY[1])), ps("b1", f(POS["n2"]), after=True), *weg("n8", HUERDENWEG, delay=0.8)),
   S("Aufdrehen, quer zu Spieler sechs", "Spieler zwei nimmt mit dem hinteren Fuß an, dreht auf und spielt quer zu Spieler sechs. Dann sprintet er zum Dummy und tippt ihn an. Spieler sechs legt den Ball für Spieler acht ab, der gerade von den Hürden kommt.",
     bl("n2", f(POS["n6"]), von=f(UM_DUMMY[1]), dauer=1.3), drehen("n2", f(POS["n6"]), delay=0.4), ps("b1", f(POS["n6"]), after=True),
     mv("n2", [50.5, 9], after=True), ps("b1", f(NACH["n8"]), after=True)),
   S("Zurück in die Mitte", "Spieler zwei kommt vom Dummy zurück und bekommt den Ball von Spieler acht. Gleichzeitig geht Spieler sechs durch die Leiter.",
     mv("n2", list(NACH["n2"])), ps("b1", f(NACH["n2"]), delay=0.6), *weg("n6", LEITERWEG[:2], delay=0.2)),
   S("Steilpass und Abschluss: Punkt", "Spieler zwei spielt steil in den Lauf von Spieler sechs. Der schießt direkt ins Minitor, und das gibt einen Punkt für Spieler sechs. Danach rückt jeder eine Station weiter, und Spieler elf startet mit dem nächsten Ball.",
     mv("n6", list(LEITERWEG[2])), ps("b1", f(LEITERWEG[2]), delay=0.2), ps("b1", [65.9, 4.4], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Offen stehen und mit dem hinteren Fuß annehmen.", "Offen stehen, hinterer Fuß",
    "Spieler zwei steht nicht frontal zum Passgeber, sondern seitlich. So sieht er den Ball und schon das nächste Ziel. Er nimmt mit dem Fuß an, der weiter weg ist, und hat den Ball damit gleich in der neuen Richtung.",
    sp(n3=NACH["n3"], n8=UM_DUMMY[1]), [B("b1", *f(UM_DUMMY[1])), B("b11", *f(POS["n11"])), B("b7", *f(POS["n7"]))] + ERSATZ,
    [S("Seitlich stehen, zum Ball schauen", "Spieler zwei dreht sich halb auf, Gesicht zum Ball, Schulter Richtung Spieler sechs. Spieler acht spielt flach zu ihm.",
       bl("n2", f(UM_DUMMY[1])), ps("b1", f(POS["n2"]), after=True)),
     S("Hinterer Fuß, gleich weiter", "Er nimmt mit dem hinteren Fuß an, der Ball läuft gleich in die neue Richtung. Ein Kontakt zum Aufdrehen, der zweite ist schon der Pass zu Spieler sechs.",
       bl("n2", f(POS["n6"]), von=f(UM_DUMMY[1]), dauer=1.3), drehen("n2", f(POS["n6"]), delay=0.4), ps("b1", f(POS["n6"]), after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: In den Lauf passen.", "In den Lauf passen",
    "Ein Pass in die Füße bremst den Mitspieler. Der Ball kommt dahin, wo er in zwei, drei Schritten sein wird. Dann kann er mit Tempo weiterlaufen oder direkt abschließen.",
    sp(**{**NACH, "n8": (55.5, 52)}), [B("b1", *f(NACH["n2"])), B("b11", *f(POS["n11"])), B("b7", *f(POS["n7"]))] + ERSATZ,
    [S("Durch die Leiter, Blick zum Ball", "Spieler sechs kommt aus der Leiter. Spieler zwei hat den Ball und wartet nicht, bis er stehen bleibt.",
       *weg("n6", LEITERWEG[:2])),
     S("Ball in den Lauf: Punkt", "Der Pass geht vor Spieler sechs in den Raum. Er läuft in den Ball und schließt direkt ab, und das gibt einen Punkt für Spieler sechs.",
       mv("n6", list(LEITERWEG[2])), ps("b1", f(LEITERWEG[2])), ps("b1", [65.9, 4.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
