import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-63 (U15-U17, Woche 3 Pre-Season): Short Combinations, Quick Feet & Finishing. 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m).
# Langes Feld QUER (Vorbild ue317.py): Im PDF hochkant mit Tor unten; hier liegt das Tor links (PDF unten -> links, oben -> rechts,
# links -> oben, rechts -> unten), Feld x 9-89, y 4-51. Koordinaten aus dem PDF umgerechnet. Nur die Längen-Maßlinie.
# Ein Team (Team Neon, Nummern wie im PDF), Großfeldtor mit neutralem Torwart (nur C- und B-Jugend). Gezeigt: Start 6 (dahinter
# wartet 3), Doppelpass-Spieler 8 und 7, Ableger 2, an der Leiter 9 (dahinter 10). Spieler 11, 5 und 4 nur im Text.
# Puppen/Stangen: vier Slalomstangen. Leiter quer (im PDF senkrecht), drei Minihürden, fünf Hütchen im Zickzack zum Antippen.
# Ein Trainer statt zwei, unten an der Seitenlinie. Rotation steht im PDF nicht genau: Dribbler wird Ableger, Ableger läuft durch
# Hütchen und Hürden zur Leiter, der Schütze holt den Ball und stellt sich am Start an (aus Skizze und Video abgeleitet).
# Fassungen = PDF Key Coaching Point 1 (Gewicht der Ablage) und 2 (kurze Kontakte im Slalom).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 24, 55.3, "T")
ERSATZ = [B("s1", 27.5, 55.8), B("s2", 30, 55.8)]
TW = P("k", "t", 13.5, 27, "TW")
POS = {"n6": (13, 45), "n3": (4.2, 41), "n8": (30.8, 37.7), "n7": (42, 49.5), "n2": (40, 21.4), "n9": (84, 26.7), "n10": (93, 26.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 47)]
TORE = [{"x": 9, "y": 27.5, "side": "left", "size": "gross"}]
STANGEN = [(54, 46), (59.5, 43), (65, 40), (70.5, 37)]
ZICK = [(30.3, 8.2), (36.8, 12.5), (43.5, 8.2), (51, 12.5), (56.4, 8.2)]
HUERDEN = [(64, 11.5), (70, 11.5), (76, 11.5)]
CONES = [C(x, y, shape="stange") for x, y in STANGEN] + [C(x, y) for x, y in ZICK] + [C(x, y, shape="huerde") for x, y in HUERDEN] \
    + [leiter(70.4, 26.7), C(10.5, 49), C(27.5, 36), C(46.5, 51.5), C(35, 22.5)]
DIMS = dims(9, 89, 4, 51, "40 m", "25 m")[:1]
BAELLE = [B("b1", *f(POS["n6"])), B("b3", *f(POS["n3"]))] + ERSATZ
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
def drw(who, ball, pkt, **k): return [dr(who, ball, pkt[0], **k)] + [dr(who, ball, p, after=True) for p in pkt[1:]]
SLALOM = [[52.3, 42.9], [61.2, 46.1], [63.3, 36.9], [72.2, 40.1], [75, 35]]
LEITER = [[78.4, 26.7], [62.4, 26.7]]
ABSCHLUSS = [33, 28]
# Hütchen antippen: jeweils knapp neben dem Hütchen vorbei, dann über die drei Hürden und zur Leiter
AGIL = [[30.3, 10.6], [36.8, 10.1], [43.5, 10.6], [51, 10.1], [56.4, 10.6], [60, 11.5], [64, 11.5], [70, 11.5], [76, 11.5], [80, 14], [86, 22]]

u = {"title": "Doppelpass, Leiter, Direktschuss", "code": "UE-326", "kind": "Übungsform",
 "focuses": ["Passspiel", "Torschuss", "Koordination"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "25 x 40 m",
 "description": "Ein Rundlauf mit fünf Stationen vor einem Tor mit Torwart. Der Starter spielt zwei Doppelpässe und dribbelt durch die Stangen. Dann spielt er zum Ableger, und der legt für den Spieler ab, der gerade aus der Leiter kommt. Der schließt direkt ab, und der Ableger läuft durch Hütchen und Hürden zurück an die Leiter.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern mit einem großen Tor und Torwart. Vor dem Tor liegen zwei Hütchen für die Doppelpässe, daneben vier Stangen für den Slalom. Weiter hinten eine Leiter, außen fünf Hütchen im Zickzack und drei Minihürden.",
  "Verteilen: Mindestens acht Spieler. Die meisten warten mit Ball am Start neben dem Tor, zwei oder drei an der Leiter. Je ein Spieler steht an den beiden Doppelpass-Hütchen und einer als Ableger in der Mitte. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass, zweiter Doppelpass, Slalom durch die Stangen und Pass zum Ableger. Gleichzeitig läuft der Erste an der Leiter durch die Leiter. Der Ableger legt ihm ab, und er schießt direkt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Der Dribbler wird Ableger, der Ableger läuft durch Hütchen und Hürden an die Leiter, der Schütze holt seinen Ball und stellt sich am Start an. Die Doppelpass-Spieler wechseln nach ein paar Runden."],
 "organisation_show": ORG,
 "coaching_points": ["Doppelpass mit einem Kontakt", "Im Slalom kurze Kontakte, der Ball bleibt nah", "Ablage genau in den Lauf, nicht zu fest", "Direkt abschließen, flach ins Eck"],
 "materials": ["1 großes Tor", "9 Hütchen", "4 Stangen", "1 Koordinationsleiter", "3 Minihürden", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Doppelpass, Leiter, Direktschuss. Ein Rundlauf mit fünf Stationen. Zwei Doppelpässe, Slalom, Ablage und Abschluss mit einem Kontakt, dazu Leiter, Hütchen und Hürden.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BAELLE, "dims": DIMS,
  "steps": [
   S("Erster Doppelpass", "Spieler sechs startet am Tor. Er spielt flach zu Spieler acht und läuft sofort an ihm vorbei. Der Ball kommt mit einem Kontakt zurück.",
     ps("b1", f(POS["n8"])), mv("n6", [27, 46.5], delay=0.3), ps("b1", [27.6, 47.1], after=True)),
   S("Zweiter Doppelpass", "Gleich der nächste. Pass zu Spieler sieben, der legt direkt zurück in den Lauf.",
     ps("b1", f(POS["n7"])), mv("n6", [51, 43], delay=0.3), ps("b1", [51.6, 43.6], after=True)),
   S("Slalom, Leiter läuft mit", "Jetzt dribbelt Spieler sechs eng durch die Stangen. Gleichzeitig startet Spieler neun in die Leiter, kleine schnelle Schritte.",
     *drw("n6", "b1", SLALOM), *weg("n9", LEITER, delay=0.8)),
   S("Pass zum Ableger, Ablage", "Spieler sechs spielt zu Spieler zwei in die Mitte. Spieler neun kommt aus der Leiter und läuft Richtung Tor. Spieler zwei legt ihm mit einem Kontakt in den Lauf.",
     ps("b1", f(POS["n2"])), mv("n9", ABSCHLUSS, delay=0.2), ps("b1", f(ABSCHLUSS), after=True)),
   S("Direktschuss: Punkt", "Spieler neun schießt direkt flach ins Eck, und das gibt einen Punkt für Team Neon. Spieler zwei tippt die Hütchen an, springt über die Hürden und stellt sich an der Leiter an. Spieler sechs wird Ableger, und Spieler drei startet.",
     ps("b1", [9.3, 23]), *weg("n2", AGIL, delay=0.4), mv("n6", POS["n2"], delay=0.6))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Ablage muss passen.", "Die Ablage muss passen",
    "Der Ableger spielt den Ball nicht zum Schützen, sondern dorthin, wo er gleich ist. Nicht zu fest und nicht zu weich, damit der Schütze ohne Annahme schießen kann. So bleibt das Tempo der ganzen Runde hoch.",
    sp(n6=(75, 35)), [B("b1", *f((75, 35))), B("b3", *f(POS["n3"]))] + ERSATZ,
    [S("Ablage in den Lauf", "Spieler sechs spielt zu Spieler zwei. Spieler neun läuft schon Richtung Tor. Spieler zwei legt den Ball weich ein Stück vor ihn, genau in den Lauf.",
       ps("b1", f(POS["n2"])), mv("n9", ABSCHLUSS, delay=0.2), ps("b1", f(ABSCHLUSS), delay=1.2)),
     S("Ohne Annahme: Punkt", "Der Ball liegt richtig, also schießt Spieler neun ohne Annahme. Flach ins Eck, und das gibt einen Punkt für Team Neon.",
       ps("b1", [9.3, 23]))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Im Slalom bleibt der Ball nah am Fuß.", "Kurze Kontakte im Slalom",
    "Zwischen den Stangen ist wenig Platz. Darum viele kleine Kontakte mit Innen- und Außenseite. Der Körper bleibt tief, so kann der Spieler schnell die Richtung wechseln. Erst nach der letzten Stange spielt er weiter.",
    sp(n6=(51, 43)), [B("b1", 51.6, 43.6), B("b3", *f(POS["n3"]))] + ERSATZ,
    [S("Eng um jede Stange", "Spieler sechs dribbelt in den Slalom. An jeder Stange ein, zwei kurze Kontakte, dann die Richtung wechseln. Der Ball springt nie weiter als einen Schritt weg.",
       *drw("n6", "b1", SLALOM)),
     S("Raus und weiterspielen", "Nach der letzten Stange spielt er sofort flach zu Spieler zwei.",
       ps("b1", f(POS["n2"])))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
