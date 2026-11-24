import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-30 (U15-U17, Woche 10): Passing and Dribbling Activation, Warm Up. 30 x 35 Yards = 27 x 32 m, gerundet 25 x 30 m.
# Hochkant wie im PDF, Feld x 25-75, y 5-55 (in der Breite gestreckt für den 3D-Abstand). Nicht gedreht.
# Zwei Stangenreihen mit je acht Stangen (vier je Hälfte), in gerader Linie wie im Video (im PDF leicht versetzt).
# PDF: je vier Spieler an vier Stationen, Nummern in beiden Farben gleich. Hier oben Team Neon (7 und 10 links, 4 und 11
# rechts, nächste Paare 9/8 und 2/3 warten neben dem Feld), unten Team Rot neu nummeriert (5/6 links, 12/13 rechts);
# die vier weiteren Wartenden unten stehen nur im Text. Ein Trainer statt zwei.
# Fassungen: PDF Key Coaching Point (nicht in den Rücken, sondern in den Lauf passen; Video "play the ball on front foot")
# und Progression (allein im Slalom dribbeln, an der Mitte ans andere Ende passen, vier gleichzeitig).
# Sichtkegel: im Video nicht eingezeichnet; Video-Einblendung "Head up, assess space in front", Ton "aware of the opposite
# player", Text "stay aware of the opposite runner": in der Steigerung schaut der Dribbler vor der Mitte zum Entgegenkommenden.
T = P("T", "c", 9, 30, "T")
ERSATZ = [B("s1", 12.6, 33.5), B("s2", 9, 33.5)]
L, R = 37, 63                       # Stangenreihen
OBEN, UNTEN = [9.5, 15, 20.5, 26], [34, 39.5, 45, 50.5]
CONES = [C(x, y, shape="stange") for x in (L, R) for y in OBEN + UNTEN] + [C(L, 5, "neon"), C(R, 5, "neon"), C(L, 55, "neon"), C(R, 55, "neon")]
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
DIMS = dims(25, 75, 5, 55, "25 m", "30 m", rx=93)
def pl(d): return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [p[0] + 0.6, p[1] + 0.6]
# Grundform: Paare links/rechts der Stange, x-Versatz 4.5
POS = {"n7": (32.5, 10), "n10": (41.5, 10), "n4": (58.5, 10), "n11": (67.5, 10),
       "r5": (32.5, 50), "r6": (41.5, 50), "r12": (58.5, 50), "r13": (67.5, 50),
       "n9": (15.5, 4), "n8": (24, 4), "n2": (76, 4), "n3": (84.5, 4)}
def sp(**k):
    d = dict(POS); d.update(k); return pl(d)
# je Reihe: (linker Spieler, rechter Spieler, Ball, x-Mitte)
OB = [("n7", "n10", "b1", L), ("n4", "n11", "b2", R)]
UN = [("r5", "r6", "b1", L), ("r12", "r13", "b2", R)]
def runter(a, b, ball, x):          # drei direkte Pässe von oben bis zur Mitte
    return [mv(a, [x - 4.5, 19.5]), mv(b, [x + 4.5, 14]), mv(b, [x + 4.5, 25], after=True),
            ps(ball, f([x + 4.5, 14]), delay=0.5), ps(ball, f([x - 4.5, 19.5]), after=True), ps(ball, f([x + 4.5, 25]), after=True)]
def hoch(a, b, ball, x):            # drei direkte Pässe von unten bis zur Mitte
    return [mv(b, [x + 4.5, 40]), mv(a, [x - 4.5, 45.5]), mv(a, [x - 4.5, 34.5], after=True),
            ps(ball, f([x - 4.5, 45.5]), delay=0.5), ps(ball, f([x + 4.5, 40]), after=True), ps(ball, f([x - 4.5, 34.5]), after=True)]

u = {"title": "Direktpässe durch die Stangen", "code": "UE-303", "kind": "Übungsform",
 "focuses": ["Passspiel", "Dribbling", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 12, "players_max": 16,
 "field_size": "25 x 30 m",
 "description": "Ein Aufwärmen mit Ball an zwei Stangenreihen. Zwei Spieler traben links und rechts an den Stangen entlang und spielen sich den Ball direkt durch die Lücken zu. An der Mitte geht der Ball zum Paar am anderen Ende, und beide laufen zügig durch bis dorthin. Beide Reihen arbeiten gleichzeitig.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit einer Mittellinie. Zwei Reihen mit je acht Stangen laufen von oben nach unten, vier Stangen in jeder Hälfte. An beiden Enden jeder Reihe steht ein Hütchen als Start.",
  "Verteilen: An jedem der vier Hütchen stehen vier Spieler, immer zu zweit als Paar. Die beiden Paare oben haben je einen Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Das Paar trabt los, einer links und einer rechts der Stangen, und passt direkt durch die Lücken. An der Mitte geht der Ball zum Paar am anderen Ende. Das startet sofort in die Gegenrichtung, das erste Paar läuft außen durch und stellt sich dort hinten an.",
  "Wechsel: Jedes Paar läuft zweimal durch, dann gibt es eine kurze Pause. Danach kommt die Steigerung mit Dribbling."],
 "organisation_show": ORG,
 "coaching_points": ["Direkt spielen, flach und nicht zu hart", "In den Lauf passen, nie in den Rücken", "Ansagen, wann der Ball kommt", "Nach dem langen Pass zügig durchlaufen und außen bleiben"],
 "materials": ["16 Stangen", "4 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Direktpässe durch die Stangen. Ein Aufwärmen zu zweit. Im Traben wird direkt durch die Stangen gepasst, an der Mitte geht der Ball ans andere Ende.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(),
  "balls": [B("b1", *f(POS["n7"])), B("b2", *f(POS["n4"]))] + ERSATZ,
  "steps": [
   S("Direkt durch die Lücken", "Beide Reihen starten gleichzeitig. Spieler sieben und Spieler zehn traben los, einer links und einer rechts der Stangen. Der Ball geht direkt hin und her, immer durch die nächste Lücke. Rechts machen Spieler vier und Spieler elf dasselbe.",
     *[m for r in OB for m in runter(*r)]),
   S("An der Mitte: langer Pass", "An der Mittellinie ist Schluss mit den kurzen Pässen. Spieler zehn spielt flach nach unten zu Spieler sechs. Beide ziehen das Tempo an und laufen außen weiter. Oben rückt schon das nächste Paar an den Start.",
     ps("b1", f(POS["r6"])), ps("b2", f(POS["r13"])),
     mv("n7", [28, 38], delay=0.3), mv("n10", [45.5, 38], delay=0.3), mv("n4", [54.5, 38], delay=0.3), mv("n11", [72, 38], delay=0.3),
     mv("n8", [32.5, 10], delay=0.6), mv("n9", [30, 2], delay=0.6), mv("n9", [41.5, 2.5], after=True), mv("n9", [41.5, 10], after=True),
     mv("n2", [67.5, 10], delay=0.6), mv("n3", [70, 2], delay=0.6), mv("n3", [58.5, 2.5], after=True), mv("n3", [58.5, 10], after=True)),
   S("Das nächste Paar spielt zurück", "Jetzt kommen Spieler fünf und Spieler sechs von unten. Wieder direkt durch die Lücken, bis zur Mitte. Das erste Paar läuft außen an ihnen vorbei und stellt sich unten an. Von der Mitte geht der Ball hoch zu Spieler acht, und das nächste Paar startet. Nach zwei Durchgängen gibt es eine kurze Pause.",
     *[m for r in UN for m in hoch(*r)],
     ps("b1", f([32.5, 10]), after=True), ps("b2", f([58.5, 10]), after=True),
     mv("n7", [28, 52], delay=0.4), mv("n10", [45.5, 52], delay=0.4), mv("n4", [54.5, 52], delay=0.4), mv("n11", [72, 52], delay=0.4))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: In den Lauf, nie in den Rücken.", "In den Lauf passen",
    "Kommt der Pass hinter dem Mitspieler an, muss er bremsen und das Tempo ist weg. Darum geht der Ball immer ein Stück voraus, vor den vorderen Fuß. So bleiben beide im Traben und können direkt spielen.",
    sp(), [B("b1", *f(POS["n7"])), B("b2", *f(POS["n4"]))] + ERSATZ,
    [S("Pass in den Rücken", "Spieler zehn ist schon zwei Stangen weiter. Spieler sieben spielt aber zu kurz, der Ball kommt hinter ihm an. Spieler zehn muss abbremsen und zurück.",
       mv("n10", [41.5, 19.5]), ps("b1", f([41.5, 13.5]), delay=0.6), mv("n10", [41.5, 13.5], after=True)),
     S("Vor den vorderen Fuß", "So ist es richtig. Der Ball kommt eine Lücke weiter vorn an, genau in den Lauf von Spieler sieben. Der spielt direkt zurück, und beide bleiben in Bewegung.",
       mv("n7", [32.5, 19.5]), ps("b1", f([32.5, 19.5]), delay=0.4), mv("n10", [41.5, 25], delay=0.6), ps("b1", f([41.5, 25]), after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Jeder dribbelt allein durch die Stangen.", "Allein im Slalom",
    "An jedem Ende startet nur noch ein Spieler, also vier gleichzeitig. Jeder dribbelt im Slalom durch die Stangen bis zur Mitte und passt dann zum Nächsten am anderen Ende. An der Mitte kommt ihm einer entgegen, also Kopf hoch.",
    pl({"n7": (34, 7), "n10": (25.5, 7), "n4": (60, 7), "n11": (51.5, 7), "r6": (40, 53), "r5": (48.5, 53), "r13": (66, 53), "r12": (74.5, 53)}),
    [B("b1", 34.6, 7.6), B("b2", 60.6, 7.6), B("b3", 40.6, 53.6), B("b4", 66.6, 53.6)] + ERSATZ,
    [S("Vier dribbeln gleichzeitig", "Oben starten Spieler sieben und Spieler vier, unten Spieler sechs und Spieler dreizehn. Alle vier dribbeln im Slalom durch die Stangen. Kleine Kontakte, mal mit innen und mal mit außen, mit beiden Füßen.",
       *[m for who, ball, x in (("n7", "b1", 34), ("n4", "b2", 60)) for m in
         (dr(who, ball, [x, 10]), dr(who, ball, [x + 6, 14.5], after=True), dr(who, ball, [x + 6, 15.5], after=True), dr(who, ball, [x, 20], after=True))],
       *[m for who, ball, x in (("r6", "b3", 40), ("r13", "b4", 66)) for m in
         (dr(who, ball, [x, 50]), dr(who, ball, [x - 6, 45.5], after=True), dr(who, ball, [x - 6, 44.5], after=True), dr(who, ball, [x, 40], after=True))]),
     S("Kopf hoch vor der Mitte", "Vor der Mitte geht der Kopf hoch. Spieler sieben sieht Spieler sechs entgegenkommen. Beide bleiben auf ihrer Seite der Stangen, dann stößt keiner zusammen.",
       bl("n7", [39.5, 39]), bl("n4", [65.5, 39]),
       *[m for who, ball, x in (("n7", "b1", 34), ("n4", "b2", 60)) for m in
         (dr(who, ball, [x, 21], delay=0.9), dr(who, ball, [x + 6, 25.5], after=True), dr(who, ball, [x + 6, 28], after=True))],
       *[m for who, ball, x in (("r6", "b3", 40), ("r13", "b4", 66)) for m in
         (dr(who, ball, [x, 39], delay=0.9), dr(who, ball, [x - 6, 34.5], after=True), dr(who, ball, [x - 6, 32], after=True))]),
     S("Pass ans andere Ende, weiterlaufen", "An der Mitte spielt jeder flach zum Nächsten am anderen Ende. Spieler sieben passt nach unten zu Spieler fünf, Spieler sechs nach oben zu Spieler zehn. Dann laufen alle zügig durch und stellen sich drüben an. Die Nächsten dribbeln schon los.",
       ps("b1", f([48.5, 53])), ps("b2", f([74.5, 53])), ps("b3", f([25.5, 7])), ps("b4", f([51.5, 7])),
       mv("n7", [40, 53], delay=0.3), mv("n4", [66, 53], delay=0.3), mv("r6", [34, 7], delay=0.3), mv("r13", [60, 7], delay=0.3))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
