import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-14 (U15-U17, Woche 36 Phase 6): Midfielder Passing Activation Warm Up. 10 x 12 Yards = 9 x 11 m, hochkant wie im PDF
# (Verhältnis 1,2, kein langes Feld), nicht gedreht. Sechs Spieler, alle Team Neon, Nummern wie im Video (6, 8, 10, 4, 2, 9).
# Ablauf nach PDF-Skizze (1 Pass, 2 Ablage, 3 Doppelpass über den Mittelspieler mit Lauf, 4 langer Pass) und Ton („switch of play
# from one side to the other … quick wall pass with the nearest central player before switching again“). Vereinfacht und
# klar gespiegelt: oben läuft die Folge 6 -> 8 -> 6 -> 10 -> 8 (startet nach außen) und dann diagonal auf die andere Seite zu 2,
# unten genauso 2 -> 9 -> 2 -> 4 -> 9 und diagonal zurück zu 6. Die Positionswechsel im Video (Rotation) stehen nur im Text.
# Ein Trainer am Rand mit Ersatzbällen. Steigerung = PDF-Progression (zweiter Ball, beide Seiten gleichzeitig).
# Sichtkegel: PDF „Scanning – awareness of surroundings“, Ton „scanning remains a core focus“, Video „Get head up before playing
# the pass“ (Kegel des Ballführers zum Mitspieler eingezeichnet): Der Läufer schaut erst zum Mittelspieler, nimmt an und
# schwenkt den Blick dann zum Passziel auf der anderen Seite (bl mit von). Kein Aufdrehen nötig (er läuft schon in Spielrichtung).
T = P("T", "c", 20, 30, "T")
ERSATZ = [B("s1", 19.5, 35), B("s2", 22.5, 35)]
POS = {"n6": (34, 9.5), "n8": (66, 9.5), "n10": (50, 22), "n4": (50, 38), "n2": (34, 50.5), "n9": (66, 50.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fu(i): x, y = POS[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
OBEN, UNTEN = [68.5, 6.5], [68.5, 53.5]  # wohin die Außenspieler starten
def fo(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def ri(a, b, L=22):
    # Blickziel: in Richtung b, aber nur L Einheiten weit (Kegel nicht zu lang)
    dx, dy = b[0] - a[0], b[1] - a[1]; d = (dx * dx + dy * dy) ** 0.5
    return [round(a[0] + dx / d * L, 1), round(a[1] + dy / d * L, 1)]
LINES = [rect(29.5, 5, 41, 50)]
CONES = [C(31, 12.5), C(69, 12.5), C(50, 18.5), C(50, 42.5), C(31, 47.5), C(69, 47.5)]
DIMS = dims(29.5, 70.5, 5, 55, "9 m", "11 m", rx=80)

u = {"title": "Passfolge mit Seitenwechsel", "code": "UE-401", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Passspiel", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 6, "players_max": 6,
 "field_size": "9 x 11 m",
 "description": "Ein kurzes Aufwärmen für das Mittelfeld auf engem Raum. Oben spielen zwei Außenspieler quer und lassen klatschen, dann folgt ein Doppelpass über den Spieler in der Mitte. Der Außenspieler, der gestartet ist, wechselt mit einem langen Pass auf die andere Seite. Unten läuft dieselbe Folge, und der Ball kommt wieder nach oben.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 11 Metern mit sechs Hütchen. Je zwei Hütchen stehen oben und unten in den Ecken, zwei in der Mitte hintereinander.",
  "Verteilen: Sechs Spieler, einer an jedem Hütchen. Der Spieler oben links hat den Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass quer, direkt zurück, Pass in die Mitte. Der Außenspieler startet nach außen und bekommt den Ball in den Lauf. Dann wechselt er diagonal auf die andere Seite, und dort läuft dieselbe Folge.",
  "Wechsel: Der Ball wandert ohne Pause von oben nach unten und zurück. Nach ein paar Runden tauschen die Spieler die Positionen, jeder spielt mal außen und mal in der Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Pass in den Lauf, nicht in die Füße", "Erst der Pass in die Mitte, dann der Start", "Kopf hoch, bevor der Ball kommt", "Zwei Kontakte, das Tempo bleibt hoch"],
 "materials": ["6 Hütchen", "Mehrere Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passfolge mit Seitenwechsel. Ein kurzes Aufwärmen für das Mittelfeld. Quer, zurück, Doppelpass über die Mitte, und dann geht der Ball lang auf die andere Seite.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *fu("n6"))] + ERSATZ,
  "steps": [
   S("Pass quer, direkt zurück", "Spieler sechs spielt flach rüber zu Spieler acht. Der lässt direkt klatschen, mit einem Kontakt.",
     ps("b1", fu("n8")), ps("b1", fu("n6"), after=True)),
   S("Doppelpass über die Mitte", "Jetzt geht der Ball in die Mitte zu Spieler zehn. In dem Moment startet Spieler acht nach außen und schaut zu Spieler zehn. Der spielt ihm den Ball in den Lauf.",
     ps("b1", fu("n10")), mv("n8", OBEN, delay=0.3), bl("n8", POS["n10"], after=True), ps("b1", fo(OBEN), after=True)),
   S("Kopf hoch, Seitenwechsel", "Spieler acht nimmt den Ball mit, hebt den Kopf und sieht Spieler zwei. Ein langer, flacher Pass diagonal auf die andere Seite.",
     bl("n8", ri(OBEN, POS["n2"]), von=POS["n10"], dauer=1.3), ps("b1", fu("n2"), after=True)),
   S("Unten das Gleiche", "Unten geht es genauso weiter. Spieler zwei spielt quer zu Spieler neun und bekommt den Ball direkt zurück. Oben trabt Spieler acht an sein Hütchen.",
     ps("b1", fu("n9")), ps("b1", fu("n2"), after=True), mv("n8", POS["n8"], delay=0.5)),
   S("Doppelpass und zurück nach oben", "Spieler zwei spielt in die Mitte zu Spieler vier, Spieler neun startet nach außen und bekommt den Ball in den Lauf. Er hebt den Kopf und spielt lang zu Spieler sechs. Oben geht es sofort wieder los, und nach ein paar Runden tauschen alle die Positionen.",
     ps("b1", fu("n4")), mv("n9", UNTEN, delay=0.3), ps("b1", fo(UNTEN), after=True),
     bl("n9", ri(UNTEN, POS["n6"]), von=POS["n4"], dauer=1.3, after=True), ps("b1", fu("n6"), after=True), mv("n9", POS["n9"], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball in den Lauf spielen.", "Pass in den Lauf",
    "Der Außenspieler startet erst, wenn der Ball in die Mitte geht. Der Mittelspieler spielt nicht in die Füße, sondern dorthin, wo der Läufer hinwill. So nimmt er den Ball im Tempo mit und kann sofort weiterspielen.",
    sp(), [B("b1", *fu("n6"))] + ERSATZ,
    [S("Erst der Pass, dann der Start", "Spieler acht wartet. Erst als Spieler sechs in die Mitte spielt, startet er nach außen. Zu früh los, und er steht schon da, wenn der Ball kommt.",
       ps("b1", fu("n10")), mv("n8", OBEN, delay=0.4)),
     S("Ball vor den Fuß, nicht in den Rücken", "Spieler zehn spielt den Ball einen Schritt vor Spieler acht. Der läuft drauf, nimmt ihn mit und spielt gleich lang zu Spieler zwei.",
       bl("n8", POS["n10"]), ps("b1", fo(OBEN), after=True), bl("n8", ri(OBEN, POS["n2"]), von=POS["n10"], dauer=1.3), ps("b1", fu("n2"), after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball, beide Seiten spielen gleichzeitig.", "Zwei Bälle gleichzeitig",
    "Oben und unten startet je ein Ball zur selben Zeit. Beide Seiten spielen ihre Folge und wechseln dann diagonal. Die Pässe kreuzen sich in der Mitte, also muss jeder vorher schauen, wo der andere Ball gerade ist.",
    sp(), [B("b1", *fu("n6")), B("b2", *fu("n2"))] + ERSATZ,
    [S("Oben und unten gleichzeitig", "Jetzt hat auch Spieler zwei einen Ball. Beide spielen gleichzeitig quer und bekommen den Ball direkt zurück.",
       ps("b1", fu("n8")), ps("b1", fu("n6"), after=True), ps("b2", fu("n9")), ps("b2", fu("n2"), after=True)),
     S("Zwei Doppelpässe über die Mitte", "Oben läuft der Doppelpass über Spieler zehn, unten über Spieler vier. Spieler acht und Spieler neun starten beide nach außen.",
       ps("b1", fu("n10")), mv("n8", OBEN, delay=0.3), ps("b1", fo(OBEN), after=True),
       ps("b2", fu("n4")), mv("n9", UNTEN, delay=0.3), ps("b2", fo(UNTEN), after=True)),
     S("Beide wechseln die Seite", "Kopf hoch. Spieler acht spielt lang zu Spieler zwei, kurz danach spielt Spieler neun lang zu Spieler sechs. Die Bälle kreuzen sich, und sofort geht es von vorn los.",
       bl("n8", ri(OBEN, POS["n2"]), von=POS["n10"], dauer=1.3), ps("b1", fu("n2"), after=True), mv("n8", POS["n8"], after=True),
       bl("n9", ri(UNTEN, POS["n6"]), von=POS["n4"], dauer=1.3, delay=0.8), ps("b2", fu("n6"), after=True), mv("n9", POS["n9"], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
