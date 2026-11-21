import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P27: 15 x 15 Yards (Feld 26/6, 48 x 48). Zwei Spieler je Ecke (oben links, unten rechts), drei Stangen diagonal.
T = P("T", "c", 88, 30, "T")
STANGEN = [C(42, 22, "neon", shape="stange"), C(50, 30, "neon", shape="stange"), C(58, 38, "neon", shape="stange")]
HUET = [C(27.5, 16), C(72.5, 44)]
POS = {"n2": (30, 10), "n3": (30, 26), "n4": (70, 50), "n5": (70, 34)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def b(i, x, y): return B(i, round(x + 1.6, 1), round(y + 0.6, 1))
CB = [B("c1", 90.5, 31), B("c2", 87, 33.5)]
VORW = [(39.2, 24.8), (52.8, 27.2), (55.2, 40.8)]   # Slalom von oben links
RUECKW = [(60.8, 35.2), (47.2, 32.8), (44.8, 19.2)]  # Slalom von unten rechts
def slalom(k, ball, pts, ende): return [dr(k, ball, list(p), after=i > 0 or None) for i, p in enumerate(list(pts) + [ende])]
feld = rect(26, 6, 48, 48)
u = {"title": "Slalom und Doppelpass", "code": "UE-104", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Koordination"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 4, "players_max": 8, "field_size": "14 x 14 m",
 "description": "In zwei gegenüberliegenden Ecken stehen je zwei Spieler, dazwischen drei Stangen. Aus beiden Ecken dribbelt gleichzeitig ein Spieler im Slalom durch die Stangen. Am Ende spielt er mit dem Partner in der Ecke einen Doppelpass und legt ihm den Ball in den Lauf. Der Partner dribbelt los, und alles beginnt von vorn.",
 "organisation": ["Aufbauen: Ein Feld von etwa 14 mal 14 Metern. Oben links und unten rechts je ein Hütchen als Ecke, dazwischen drei Stangen schräg durchs Feld.",
  "Verteilen: An jeder Ecke stehen zwei Spieler, je einer davon mit Ball. Bei mehr Kindern stellen sich die übrigen an den Ecken an.",
  "Ablauf: Aus beiden Ecken dribbelt gleichzeitig ein Spieler im Slalom durch die Stangen. Am Ende spielt er mit dem Partner einen Doppelpass und legt ihm den Ball in den Lauf. Der dribbelt dann zurück.",
  "Wechsel: Wer den Ball abgegeben hat, bleibt in der Ecke und ist beim nächsten Mal der Partner. Nach einer Weile eine kurze Pause machen."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball im Slalom ganz nah am Fuß halten", "Mit beiden Füßen dribbeln, innen und außen", "Den Doppelpass schnell und genau spielen", "Vor dem Pass hochschauen und den Partner rufen"],
 "materials": ["3 Stangen", "2 orange Hütchen", "Mehrere Bälle beim Trainer", "2 Minitore für die Steigerung"],
 "access": "frei", "hidden": True,
 "say_intro": "Slalom und Doppelpass. Aus zwei Ecken dribbeln die Kinder gleichzeitig durch die Stangen und spielen am Ende einen Doppelpass.",
 "board": {"lines": [feld], "cones": STANGEN + HUET, "players": sp(), "balls": [b("b2", 30, 10), b("b4", 70, 50)] + CB,
  "steps": [
   S("Slalom aus beiden Ecken", "Gleichzeitig dribbeln Spieler zwei von oben links und Spieler vier von unten rechts im Slalom durch die drei Stangen.",
     *slalom("n2", "b2", VORW, [61, 46]), *slalom("n4", "b4", RUECKW, [39, 14])),
   S("Doppelpass mit dem Partner", "Am Ende spielt jeder zum Partner in der Ecke und bekommt den Ball direkt zurück. Spieler zwei spielt mit Spieler fünf, Spieler vier gleichzeitig mit Spieler drei.",
     ps("b2", [71.6, 34.6]), ps("b2", [62.6, 46.6], after=True), ps("b4", [31.6, 26.6]), ps("b4", [40.6, 14.6], after=True)),
   S("In den Lauf, der Nächste dribbelt", "Jetzt legen beide den Ball dem Partner in den Lauf und gehen in die Ecke. Spieler fünf und Spieler drei dribbeln gleichzeitig im Slalom zurück.",
     ps("b2", [67.6, 40.6]), mv("n5", [66, 40], delay=0.2), ps("b4", [33.6, 20.6]), mv("n3", [32, 20], delay=0.2),
     mv("n2", [70, 50], after=True), mv("n4", [30, 10], after=True),
     *[dr("n5", "b2", list(p), after=True) for p in RUECKW + [(39, 14)]], *[dr("n3", "b4", list(p), after=True) for p in VORW + [(61, 46)]])],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "14 m"}, {"x1": 80, "y1": 6, "x2": 80, "y2": 54, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im Slalom bleibt der Ball ganz nah am Fuß.", "Ball nah am Fuß",
    "Im Slalom führen die Kinder den Ball mit vielen kleinen Kontakten, mit beiden Füßen, mal innen, mal außen. So bleibt der Ball nah am Fuß, und die Stangen werden nicht berührt. Vor dem Doppelpass schauen sie kurz hoch und rufen den Partner.",
    sp(), [b("b2", 30, 10), b("b4", 70, 50)] + CB,
    [S("Kleine Kontakte", "Spieler zwei und Spieler vier dribbeln gleichzeitig mit vielen kleinen Kontakten um die Stangen, mal mit rechts, mal mit links.",
       *slalom("n2", "b2", VORW, [61, 46]), *slalom("n4", "b4", RUECKW, [39, 14])),
     S("Hochschauen und rufen", "Vor dem Pass schauen beide hoch, rufen den Partner und spielen dann genau in den Fuß.",
       ps("b2", [71.6, 34.6]), ps("b4", [31.6, 26.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Minitore, und nach jedem zweiten Slalom wird aufs Tor geschossen.", "Abschluss ins Minitor",
    "Im Feld stehen zwei Minitore. Nach jedem zweiten Slalom gibt es keinen Doppelpass, sondern einen Torschuss. Es zählt Genauigkeit statt Kraft: Ein Treffer gibt einen Punkt, ein Treffer in die Ecke gibt einen Extrapunkt. Die Kinder in den Ecken feuern ihre Mitspieler an.",
    sp(), [b("b2", 30, 10), b("b4", 70, 50), b("b3", 30, 26), b("b5", 70, 34)] + CB,
    [S("Slalom aus beiden Ecken", "Gleichzeitig dribbeln Spieler zwei und Spieler vier im Slalom durch die drei Stangen.",
       *slalom("n2", "b2", VORW, [61, 46]), *slalom("n4", "b4", RUECKW, [39, 14])),
     S("Abschluss ins Minitor", "Beide schießen gleichzeitig mit Gefühl ins nächste Minitor. Jeder Treffer gibt einen Punkt, und in die Ecke gibt es einen Extrapunkt.",
       ps("b2", [44, 50.5]), ps("b4", [60, 10.5])),
     S("Die Nächsten starten", "Spieler zwei und Spieler vier gehen in die Ecke. Gleichzeitig dribbeln Spieler fünf und Spieler drei mit ihrem eigenen Ball los.",
       mv("n2", [70, 50]), mv("n4", [30, 10]),
       *slalom("n5", "b5", RUECKW, [39, 14]), *slalom("n3", "b3", VORW, [61, 46]))],
    goals=[{"x": 60, "y": 10, "side": "top"}, {"x": 44, "y": 50, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
