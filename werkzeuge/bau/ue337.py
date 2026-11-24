import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 22-P10 (U15-U17, Woche 7 Phase 1): How to Beat the Press (Possession). 30 x 50 Yards = 27 x 46 m (gerundet 25 x 45 m).
# FELD QUER (Langes Feld, Inhaber 24.11.2026, Vorbild ue317.py): Im PDF hochkant, Angriff nach oben. Hier quer wie im Video:
# Team Neon baut links auf und greift nach rechts an. Feld x 9-89 (45 m), y 4-51 (25 m). Direkt quer geplant (keine R()-Umrechnung).
# Drei Zonen wie im PDF (erste Zone 40 %, Mittelzone 20 %, Abschlusszone 40 %), Zonengrenzen gestrichelt bei x 41.8 und 58.3.
# Je zwei Minitore an beiden Enden (Team Neon trifft rechts, Team Rot links).
# PDF dunkelblau -> Team Neon (2, 3, 4, 5, 6, 9, 10 wie im PDF), pink -> Team Rot, neu nummeriert, weil Nummern doppelt sind:
# 7 -> 7, 8 -> 8, 11 -> 11, 9 -> 12, 4 -> 13, 6 -> 14, 5 -> 15. Gelbe Springer -> neutrale Springer (team t, F): f1 hinten bei
# Team Neon (mit Ball), f2 in der Mittelzone, f3 am anderen Ende (Springer von Team Rot nach Ballgewinn). Ein Trainer statt zwei,
# unten an der Seitenlinie neben der Abschlusszone.
# 3D-Abstand: Spieler in Spalten geordnet (erste Zone x 14 / 22.5 / 31 / 39.5, Mittelzone x 48 / 56.5), grob wie im PDF.
# Ablauf der Grundform wie die Linien im PDF: Springer -> 6 -> 3 -> 4 -> Springer Mitte -> Lauf von Spieler 10 in die Abschlusszone.
# Neustart nach einem Treffer und Rollentausch der Teams sind im Original nicht genannt (Annahme: wieder beim Springer hinten,
# Teams tauschen nach einigen Minuten die Aufgaben).
# Fassungen: PDF Key Coaching Points „Quick 1-2 combinations to get in behind“ (Ton: front three draw defenders in to play quick
# one-two combinations) und „Quick transitions when possession is won“ (Text: Ballgewinn in der ersten Zone abschließen oder
# zum eigenen Springer zurück und selbst aufbauen; Video „Keep ball - build own attack“).
# Sichtkegel: Video „Can they see space for the pass? Awareness“, Ton „Can deeper players see this space“: Spieler vier schaut
# erst zum Passgeber (drei), nimmt an, dann schwenkt der Kegel zum Springer in der Mitte (bl mit von) und er dreht auf (drehen).
# In Fassung 2 schaut der Balleroberer erst zu den Minitoren, dann zurück Richtung eigener Springer (ein Kegel mit von).
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
Z1, Z2 = 41.8, 58.3
T = P("T", "c", 72, 55.3, "T")
ERSATZ = [B("s1", 75.5, 55.8), B("s2", 78, 55.8)]
POS = {"f1": (5.5, 29), "n6": (14, 21), "n5": (14, 40), "r12": (22.5, 25), "r11": (22.5, 44), "n3": (31, 8), "r8": (31, 26),
       "n2": (31, 47), "r7": (39.5, 12), "n4": (39.5, 29), "r13": (39.5, 46), "n10": (48, 12), "f2": (48, 29), "n9": (48, 46),
       "r14": (56.5, 16), "r15": (56.5, 40), "f3": (93, 28)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i): return [round(POS[i][0] + 0.6, 1), round(POS[i][1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(Z1, FY0, Z1, FY1), line(Z2, FY0, Z2, FY1)]
TORE = [{"x": FX0, "y": 11.5, "side": "left"}, {"x": FX0, "y": 43.5, "side": "left"},
        {"x": FX1, "y": 11.5, "side": "right"}, {"x": FX1, "y": 43.5, "side": "right"}]
CONES = [C(x, y) for x in (FX0, Z1, Z2, FX1) for y in (FY0, FY1)]
# Nur die Länge als Maßlinie (rechts neben den Toren ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "45 m", "25 m")[:1]

u = {"title": "Das Pressing in Zonen knacken", "code": "UE-337", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 17, "players_max": 17,
 "field_size": "25 x 45 m",
 "description": "Ein langes Feld mit drei Zonen und je zwei Minitoren an beiden Enden. Team Neon baut in der ersten Zone fünf gegen fünf mit einem Springer auf und spielt sich durch das Pressing von Team Rot. In der Mittelzone wartet ein Springer, dort ist Team Neon zu dritt gegen zwei. Von dort startet ein Angreifer in die Abschlusszone und schließt auf ein Minitor ab.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 45 Metern, in drei Zonen geteilt. Die erste und die letzte Zone sind gleich groß, die Mittelzone ist schmal. An beiden Enden stehen zwei Minitore.",
  "Verteilen: In der ersten Zone stehen fünf Spieler von Team Neon gegen fünf von Team Rot. In der Mittelzone sind es zwei gegen zwei mit einem Springer. Je ein weiterer Springer steht hinter beiden Enden, der hintere hat den Ball. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Springer hinten eröffnet. Team Neon spielt sich durch die erste Zone und bringt den Ball in die Mittelzone. Von dort startet ein Angreifer in die Abschlusszone, bekommt den Ball in den Lauf und schließt ab. Erobert Team Rot den Ball in der ersten Zone, darf es sofort auf die Minitore dort schießen oder zum eigenen Springer am anderen Ende zurückspielen und selbst aufbauen.",
  "Wertung und Wechsel: Jeder Treffer in ein Minitor gibt einen Punkt. Danach eröffnet wieder der Springer hinten. Nach einigen Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Schräg anbieten, nie hinter dem Gegner verstecken", "Den Pass durch die Linie suchen", "Erst starten, wenn der Ball kommt", "Doppelpass, und schon bist du durch"],
 "materials": ["4 Minitore", "8 Hütchen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Das Pressing in Zonen knacken. Team Neon spielt sich durch das Pressing von Team Rot, bringt den Ball in die Mittelzone und startet von dort in die Abschlusszone.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *fuss("f1"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Springer eröffnet", "Der Springer hinten hat den Ball und spielt flach zu Spieler sechs. Sofort läuft Spieler zwölf an.",
     ps("b1", fuss("n6")), mv("r12", [20, 23], delay=0.4)),
   S("Weiter über Spieler drei", "Spieler sechs spielt außen auf Spieler drei. Spieler vier schaut zum Ball und bietet sich schräg dahinter an. Der Pass kommt flach zu ihm.",
     ps("b1", fuss("n3")), mv("r7", [36, 7], delay=0.5), bl("n4", list(POS["n3"]), delay=0.4), ps("b1", fuss("n4"), after=True)),
   S("Aufdrehen, Pass in die Mitte", "Spieler vier dreht mit dem ersten Kontakt auf. Er sieht den Springer in der Mittelzone frei stehen und spielt durch die Linie zu ihm.",
     bl("n4", list(POS["f2"]), von=list(POS["n3"]), dauer=1.3), drehen("n4", list(POS["f2"]), delay=0.4), ps("b1", fuss("f2"), after=True),
     mv("r8", [36, 25], delay=1.2)),
   S("Lauf in die Abschlusszone", "Jetzt startet Spieler zehn an Spieler vierzehn vorbei in die Abschlusszone. Der Springer spielt ihm den Ball genau in den Lauf.",
     mv("n10", [56, 8]), mv("n10", [66, 10], after=True), ps("b1", [66.6, 10.6], delay=0.7), mv("r14", [62, 16], delay=0.9)),
   S("Abschluss: Punkt", "Spieler zehn nimmt den Ball mit und schiebt ins Minitor, und das gibt einen Punkt für Team Neon. Danach eröffnet wieder der Springer hinten.",
     dr("n10", "b1", [79, 12]), ps("b1", [88.6, 11.5], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit dem Doppelpass hinter die Kette.", "Doppelpass hinter die Kette",
    "Spieler neun lockt seinen Gegenspieler aus der Kette. Er legt direkt ab und startet sofort in den Rücken des Gegners. Der Ball kommt mit dem nächsten Kontakt zurück in seinen Lauf.",
    sp(), [B("b1", *fuss("n4"))] + ERSATZ,
    [S("Pass auf Spieler neun", "Spieler vier spielt steil auf Spieler neun in die Mittelzone. Spieler fünfzehn geht mit und drückt.",
       ps("b1", fuss("n9")), mv("r15", [53, 43], delay=0.5)),
     S("Ablegen und starten", "Spieler neun legt direkt auf den Springer ab und startet an Spieler fünfzehn vorbei. Der Springer spielt mit einem Kontakt in seinen Lauf.",
       ps("b1", fuss("f2")), mv("n9", [55, 50], delay=0.2), mv("n9", [66, 46], after=True), ps("b1", [66.6, 46.6], delay=0.9)),
     S("Abschluss: Punkt", "Spieler neun ist durch, nimmt den Ball mit und trifft ins Minitor, und das gibt einen Punkt für Team Neon.",
       dr("n9", "b1", [79, 44]), ps("b1", [88.6, 43.5], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Nach dem Ballgewinn schnell umschalten.", "Ballgewinn, schnell umschalten",
    "Fängt Team Rot den Ball in der ersten Zone ab, darf es sofort auf die beiden Minitore dort schießen. Sind sie zu, spielt Team Rot zurück zum eigenen Springer am anderen Ende und baut in Ruhe selbst auf.",
    sp(), [B("b1", *fuss("n3"))] + ERSATZ,
    [S("Der Pass wird abgefangen", "Spieler drei will zu Spieler vier spielen. Spieler acht ahnt das, geht dazwischen und hat den Ball.",
       mv("r8", [33.5, 19], delay=0.1), ps("b1", [34.1, 19.6], delay=0.3)),
     S("Die Minitore sind zu", "Spieler acht schaut zuerst auf die Minitore. Spieler sechs und Spieler fünf sind schon davor. Also dreht er auf und spielt weit zurück zum eigenen Springer.",
       mv("n6", [14, 13]), mv("n5", [14, 39]), bl("r8", [55, 22], von=[16, 14], dauer=1.3, delay=0.3),
       drehen("r8", [55, 22], delay=0.7), ps("b1", [93.6, 28.6], after=True)),
     S("Team Rot baut auf", "Der Springer hat den Ball sicher. Jetzt baut Team Rot von dort auf und greift die Minitore auf der Seite von Team Neon an.",
       mv("r14", [62, 20]), mv("r15", [62, 38]), ps("b1", [62.6, 20.6], delay=0.5))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
