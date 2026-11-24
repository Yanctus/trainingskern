import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 14-P4 (U15-U17, Woche 25 Phase 1): Playing Out From The Back Technical (PDF: Passing Combinations to Play Out From the Back).
# 30 x 30 Yards = 27 x 27 m, gerundet 25 x 25 m = Feld x 25-75, y 5-55. Vier Dummys wie im PDF, ein Team (Neon), Nummern wie im PDF.
# Um 90 Grad gedreht: im PDF wird nach rechts gespielt (Abwehr links, Mittelfeld rechts), hier nach oben: Innenverteidiger 6 und 5
# unten, Außenverteidiger 3 links und 2 rechts, Mittelfeld 10 und 8 oben. Das PDF nennt "Dreierkette und zwei im Mittelfeld",
# Skizze und Video (4-2-3-1) zeigen vier hinten und zwei davor; gebaut nach der Skizze.
# Passfolge nach PDF (1-7): 6 -> 3 -> 8 -> 10 (kommt entgegen) -> 2 (startet nach vorn) -> 5 -> 8 (lässt sich in die Mitte fallen) -> 6.
# Spieler 2 nimmt den Ball nach innen mit, bevor er zu 5 spielt (im PDF knickt der Weg ab; sonst geht der Pass durch einen Dummy).
# Ein Dummy (Mitte unten) etwas versetzt, damit der letzte Pass von 8 zu 6 nicht durch ihn läuft. Ein Trainer statt zwei, links.
# Fassungen wie die PDF-Progressionen: 1 zweiter Ball, 2 kreativ kombinieren (Klatschen, Doppelpass, Pass um die Ecke; Folge nach
# der Skizze der Progression 2: 3 -> 10 -> 8 -> 10 -> 2 -> 8 -> 5).
# Sichtkegel: nur in Progression 1 ("maintain awareness of both balls", Ton "aware of both"): Spieler 8 schaut vor der Annahme,
# wo der zweite Ball ist (bei Spieler 2). Grundform und Progression 2 ohne Sichtkegel (Text, Ton und Video geprüft).
# Keine Dublette: UE-161 (94-P4, Viererkette und vier Mittelfeldspieler, Stangen), UE-235 (28-P12, acht Stationen, Spieler laufen
# nach) und UE-309 (WU-10) haben andere Organisation und andere Passfolgen.
T = P("T", "c", 17, 38, "T")
ERSATZ = [B("s1", 20, 41.5), B("s2", 16.5, 42.5)]
POS = {"n3": (29, 27.3), "n6": (38, 47.5), "n5": (61, 47.5), "n2": (71, 27), "n10": (39, 18), "n8": (57, 16.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(i): return [round(POS[i][0] + 0.6, 1), round(POS[i][1] + 0.6, 1)]
LINES = [rect(25, 5, 50, 50)]
CONES = [C(35, 29, shape="stange"), C(46, 34.5, shape="stange"), C(48.5, 15.5, shape="stange"), C(64, 26.5, shape="stange")]
N10K, N2V, N2I, N8M = [43, 25], [70, 19], [69, 30], [57, 30]  # 10 kommt entgegen, 2 startet vor, 2 zieht nach innen, 8 in die Mitte
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]

u = {"title": "Passfolge um vier Dummys", "code": "UE-371", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 6, "players_max": 6,
 "field_size": "25 x 25 m",
 "description": "Sechs Spieler stehen wie im Spielaufbau, vier hinten und zwei im Mittelfeld. Vier Dummys stehen als Gegenspieler im Feld. Der Ball läuft in einer festen Folge von hinten ins Mittelfeld, über rechts zurück in die Abwehr und durch die Mitte wieder zum Start. Jeder Pass kommt genau und mit Tempo, am besten mit ein oder zwei Kontakten.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern. Vier Dummys stehen verteilt im Feld und machen die Passwege eng.",
  "Verteilen: Hinten die Innenverteidiger sechs und fünf, außen links Spieler drei und rechts Spieler zwei. Davor im Mittelfeld Spieler zehn und Spieler acht. Spieler sechs hat den Ball, der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Sechs eröffnet zu drei, der spielt diagonal zu acht. Zehn kommt entgegen und spielt tief auf zwei. Zwei nimmt den Ball nach innen mit und spielt rüber zu fünf. Acht lässt sich in die Mitte fallen, bekommt den Ball und spielt zurück zu sechs.",
  "Wechsel: Ist der Ball wieder bei Spieler sechs, gehen alle auf ihre Plätze und die nächste Runde beginnt. Nach einigen Runden tauschen die Spieler die Positionen."],
 "organisation_show": ORG,
 "coaching_points": ["Pass mit Tempo, genau in den richtigen Fuß", "Ein oder zwei Kontakte, dann ist der Ball weg", "Vor dem Pass zeigen, wo du ihn haben willst", "Der erste Kontakt geht schon in die neue Richtung"],
 "materials": ["4 Dummys", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passfolge um vier Dummys. Sechs Spieler, ein Ball und eine feste Folge, so wie wir hinten herausspielen. Die Dummys stehen für die Gegner.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *f("n6"))] + ERSATZ,
  "steps": [
   S("Spieler sechs eröffnet", "Spieler sechs hat den Ball und eröffnet nach links zu Spieler drei. Flach und mit Tempo, auf den Fuß, der weg vom Dummy ist.",
     ps("b1", f("n3"))),
   S("Diagonal ins Mittelfeld", "Von Spieler drei geht der Ball diagonal hoch zu Spieler acht. Spieler zehn sieht das und kommt schon ein paar Schritte entgegen.",
     ps("b1", f("n8")), mv("n10", N10K, delay=0.6)),
   S("Klatschen und tief auf zwei", "Spieler acht spielt mit einem Kontakt zu Spieler zehn. Rechts startet Spieler zwei nach vorn, und Spieler zehn schickt ihn tief.",
     ps("b1", fu(N10K)), mv("n2", N2V, delay=0.5), ps("b1", fu(N2V), after=True)),
   S("Nach innen und rüber zu fünf", "Spieler zwei nimmt den Ball mit nach innen und spielt runter zu Spieler fünf. Gleichzeitig lässt sich Spieler acht in die Mitte fallen.",
     dr("n2", "b1", N2I), ps("b1", f("n5"), after=True), mv("n8", N8M, delay=0.4)),
   S("Über acht zurück: Runde geschafft", "Spieler fünf spielt zu Spieler acht, und der legt zurück auf Spieler sechs. Der Ball ist wieder am Start, die Runde ist geschafft. Alle gehen zurück auf ihre Plätze, und Spieler sechs eröffnet die nächste Runde.",
     ps("b1", fu(N8M)), ps("b1", f("n6"), after=True),
     mv("n10", list(POS["n10"]), after=True), mv("n2", list(POS["n2"]), delay=1.6), mv("n8", list(POS["n8"]), delay=1.6))],
  "dims": dims(25, 75, 5, 55, "25 m", "25 m")},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein zweiter Ball kommt dazu.", "Mit zweitem Ball",
    "Jetzt laufen zwei Bälle gleichzeitig durch die Folge. Der zweite startet bei Spieler zehn. Jeder muss immer wissen, wo beide Bälle sind, sonst kommen zwei auf einmal. Wer nicht hinschaut, steht im Weg.",
    sp(), [B("b1", *f("n6")), B("b2", *f("n10"))] + ERSATZ,
    [S("Zwei Bälle laufen los", "Spieler sechs eröffnet zu Spieler drei. Im selben Moment schickt Spieler zehn den zweiten Ball tief auf Spieler zwei, der dafür nach vorn startet.",
       ps("b1", f("n3")), mv("n2", N2V, delay=0.2), ps("b2", fu(N2V), delay=0.6, bend=3)),
     S("Kopf hoch: Wo ist Ball zwei?", "Bevor der Ball von Spieler drei kommt, schaut Spieler acht rüber zu Spieler zwei. Er muss wissen, wo der zweite Ball gerade ist. Dann kommt der Pass zu ihm.",
       bl("n8", N2V), ps("b1", f("n8"), after=True), dr("n2", "b2", N2I, delay=0.4)),
     S("Beide Bälle laufen weiter", "Spieler zehn kommt entgegen und bekommt den Ball von Spieler acht. Gleichzeitig geht Ball zwei rüber zu Spieler fünf. Spieler acht läuft sofort in die Mitte, denn gleich will Spieler fünf zu ihm spielen.",
       mv("n10", N10K), ps("b1", fu(N10K), delay=0.4), ps("b2", f("n5"), delay=0.4), mv("n8", N8M, after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Spieler kombinieren frei.", "Frei und kreativ kombinieren",
    "Die feste Folge ist aufgehoben. Die Spieler lassen den Ball klatschen, spielen Doppelpässe und Pässe um die Ecke. Wer den Ball hat, entscheidet selbst. Die anderen bieten sich so an, dass immer zwei Lösungen da sind.",
    sp(), [B("b1", *f("n3"))] + ERSATZ,
    [S("Klatschen lassen", "Spieler drei spielt zu Spieler zehn. Der lässt den Ball direkt klatschen, rüber zu Spieler acht.",
       ps("b1", f("n10")), ps("b1", f("n8"), after=True)),
     S("Doppelpass und tief", "Spieler zehn dreht sich sofort weg in den Raum zwischen die Dummys. Spieler acht spielt ihm den Ball zurück, und Spieler zehn schickt Spieler zwei tief.",
       mv("n10", [49, 24]), ps("b1", [49.6, 24.6], after=True), mv("n2", N2V, delay=0.6), ps("b1", fu(N2V), after=True)),
     S("Um die Ecke, dann weit rüber", "Spieler zwei legt quer auf Spieler acht. Der spielt den Ball um die Ecke und weit rüber zu Spieler fünf. Beim nächsten Mal sieht die Folge schon wieder anders aus.",
       ps("b1", f("n8")), ps("b1", f("n5"), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
