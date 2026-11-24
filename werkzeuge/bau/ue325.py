import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-113 (U15-U17, Woche 3 Pre-Season): Transitions, Overloads and Recovery. 20 x 30 Yards = 18 x 27 m (gerundet 18 x 25 m),
# drei Zonen 12 / 6 / 12 Yards (11 / 5,5 / 11 m), Zonengrenzen gestrichelt.
# Langes Feld QUER (Vorbild ue317.py): Im PDF hochkant mit Toren oben und unten; hier Tore links und rechts, Feld x 9-89, y 4-51.
# PDF unten -> links, oben -> rechts. Zwei Großfeldtore mit neutralem Torwart (nur C- und B-Jugend). Nur die Längen-Maßlinie.
# PDF pink -> Team Neon (Nummern wie im PDF: 6 und 9 außen, 10 vorn, 3 und 7 warten, 4 hinten in der Steigerung),
# blau -> Team Rot, neu nummeriert, weil die Nummern doppelt sind: 4 -> 2 (hinten), 7 -> 5 (Mitte), 10 -> 8, 3 -> 12, 9 -> 14.
# Grüne Torhüter 13 und 1 -> neutrale Torhüter k2 (links) und k1 (rechts). Ein Trainer statt zwei, unten an der Seitenlinie.
# Grundform ohne Spieler 4 (Neon) und Spieler 8 (Rot) in der linken Zone; sie stehen nur in der Steigerung (dort brauchen wir sie).
# Wartende: nur Spieler 3, 7 (Neon) und 14 (Rot) unter dem Feld, die anderen nur im Text (Rot 12 kommt in der Steigerung dazu).
# Fassung 1 = PDF Key Coaching Point (Anlaufen, Passweg zustellen, nach außen lenken), Fassung 2 = PDF Progression (3 gegen 3,
# die Außen von Team Neon werden sofort Verteidiger, Team Rot greift in die Gegenrichtung an; Ton: Stürmer hält den Verteidiger
# fest und legt ab). Spieler 10, 2 und 5 sind in der Steigerung draußen.
# Sichtkegel: Text/Ton „Find the spare player quickly“, „find the free player“; im Video nicht eingezeichnet. Richtung aus dem
# Sinn: Spieler sechs schaut vor dem Pass zum freien Spieler neun; im Coaching-Punkt schaut Spieler neun zu Spieler sechs, der Weg ist zu.
T = P("T", "c", 14, 55.3, "T")
ERSATZ = [B("s1", 17.5, 55.8), B("s2", 20, 55.8)]
K1, K2 = P("k1", "t", 86.6, 27.5, "TW"), P("k2", "t", 12.2, 28, "TW")
POS = {"n6": (46, 8), "n9": (50, 45), "n10": (69, 29), "n3": (30, 55.3), "n7": (64, 55.3),
       "r5": (49, 27), "r2": (78, 27), "r14": (80, 55.3)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [K1, K2, T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 47), line(41, 4, 41, 51), line(57, 4, 57, 51)]
TORE = [{"x": 9, "y": 27.5, "side": "left", "size": "gross"}, {"x": 89, "y": 27.5, "side": "right", "size": "gross"}]
CONES = [C(9, 4), C(89, 4), C(9, 51), C(89, 51), C(41, 4), C(57, 4), C(41, 51), C(57, 51)]
DIMS = dims(9, 89, 4, 51, "25 m", "18 m")[:1]

u = {"title": "Drei Zonen, Überzahl, Rücklauf", "code": "UE-325", "kind": "Spielform",
 "focuses": ["Umschalten", "Zusammenspiel", "Verteidigen"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 10, "players_max": 15,
 "field_size": "18 x 25 m",
 "description": "Ein Wellenspiel über drei Zonen mit einem Tor und Torwart an jedem Ende. Der Torwart eröffnet für drei Angreifer, zwei außen und einer vorn. In der Mitte stehen die beiden Außen zu zweit gegen einen Verteidiger, vorn wird daraus ein drei gegen zwei, weil der Verteidiger zurücksprintet. In der Steigerung werden die Angreifer nach ihrer Welle sofort selbst zu Verteidigern.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern, in drei Zonen geteilt. Die mittlere Zone ist fünfeinhalb Meter breit. An beiden Enden steht ein großes Tor mit Torwart, daneben liegen Ersatzbälle.",
  "Verteilen: Zehn bis fünfzehn Spieler in zwei Teams. Team Neon greift an, zwei Außen in der mittleren Zone und ein Stürmer vorn. Team Rot hat einen Verteidiger in der Mitte und einen vorn in der letzten Zone. Die anderen warten außen an der mittleren Zone. Der Trainer steht am Rand.",
  "Ablauf: Der Torwart spielt einen der beiden Außen an. In der Mitte spielen sie zu zweit gegen einen und suchen den freien Mann. Dann geht es in die letzte Zone. Der Verteidiger aus der Mitte sprintet zurück, und vorn wird drei gegen zwei gespielt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach jeder Welle kommen zwei neue Außen und ein neuer Verteidiger in die Mitte, und der Torwart eröffnet die nächste Welle."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo ist der freie Mann?", "Ball weg, sofort zurücksprinten", "Anlaufen und dabei den Passweg zustellen", "Vorn den Verteidiger festhalten und ablegen"],
 "materials": ["2 große Tore", "8 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Drei Zonen, Überzahl, Rücklauf. Ein Wellenspiel. Erst zwei gegen einen in der Mitte, dann drei gegen zwei vor dem Tor, und der Verteidiger muss zurück.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 12.8, 28.6)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Torwart eröffnet", "Der Torwart links spielt flach zu Spieler sechs in die mittlere Zone. Spieler fünf läuft ihn sofort an.",
     ps("b1", f(POS["n6"])), mv("r5", [53, 12], delay=0.4)),
   S("Zwei gegen einen, Kopf hoch", "Zwei gegen einen in der Mitte. Spieler sechs hebt den Kopf und sieht Spieler neun frei auf der anderen Seite. Der startet nach vorn und bekommt den Ball.",
     bl("n6", [52, 30]), mv("n9", [54, 43], delay=0.3), ps("b1", [54.6, 43.6], after=True)),
   S("Rein ins letzte Drittel", "Spieler neun nimmt den Ball mit in die letzte Zone. Spieler fünf dreht um und sprintet zurück. Spieler sechs läuft vorn mit, und Spieler zehn hält Spieler zwei fest.",
     dr("n9", "b1", [64, 40]), mv("r5", [62, 26], delay=0.2), mv("n6", [70, 10], delay=0.2), mv("n10", [71, 31], delay=0.4)),
   S("Drei gegen zwei: Punkt", "Drei gegen zwei. Spieler neun spielt quer auf Spieler sechs, und der schießt ins lange Eck. Das gibt einen Punkt für Team Neon. Jetzt kommen Spieler drei und Spieler sieben als neue Außen rein, Spieler vierzehn verteidigt in der Mitte.",
     ps("b1", [70.6, 10.6]), ps("b1", [88.7, 23], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Anlaufen und den Passweg zustellen.", "Passweg zu, nach außen",
    "Der Verteidiger in der Mitte läuft nicht gerade auf den Ball. Er kommt im Bogen von innen und stellt den Pass zum anderen Außen zu. So muss der Angreifer an der Linie entlang. Dort wartet der zweite Verteidiger, und die beiden machen die Falle zu.",
    sp(), [B("b1", 12.8, 28.6)] + ERSATZ,
    [S("Im Bogen anlaufen", "Der Torwart spielt diesmal zu Spieler neun. Spieler fünf läuft im Bogen von innen an. Spieler neun schaut zu Spieler sechs, aber der Passweg ist zu.",
       ps("b1", f(POS["n9"])), mv("r5", [54.5, 31], delay=0.3), mv("r5", [51, 36.5], after=True), bl("n9", [47.8, 25], after=True)),
     S("An der Linie entlang", "Spieler neun muss nach außen an der Linie entlang. Spieler fünf bleibt dran. Spieler zwei kommt von vorn dazu.",
       dr("n9", "b1", [62, 48.5]), mv("r5", [59, 43], delay=0.2), mv("r2", [71, 41], delay=0.3)),
     S("Die Falle geht zu", "Jetzt sind zwei Verteidiger am Ball. Spieler zwei spitzelt ihn ins Aus. Die Welle ist vorbei, und die nächsten drei starten.",
       mv("r2", [64.5, 46]), ps("b1", [68, 54], delay=0.5))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Drei gegen drei, und die Angreifer werden sofort zu Verteidigern.", "Drei gegen drei im Wechsel",
    "Ist die Welle von Team Neon vorbei, eröffnet sofort der Torwart rechts für Team Rot. Die beiden Außen von Team Neon sprinten zurück und verteidigen. Vorn steht ein Stürmer von Team Rot, hält seinen Verteidiger fest und legt den Ball ab. So wird es drei gegen drei.",
    sp({"n6": (62, 10), "n9": (77.5, 44), "n4": (21.3, 28.3), "r12": (49, 5.5), "r14": (50, 50), "r8": (29.8, 27)}),
    [B("b1", 87.2, 28.1)] + ERSATZ,
    [S("Sofort in die Gegenrichtung", "Der Angriff ist vorbei, und schon wirft der Torwart rechts den Ball zu Spieler vierzehn. Spieler zwölf kommt von außen dazu. Spieler sechs und Spieler neun sprinten zurück.",
       mv("r14", [52, 40]), ps("b1", [52.6, 40.6], delay=0.3), mv("r12", [50, 14], delay=0.3), mv("n6", [45, 22], delay=0.3), mv("n9", [40, 41], delay=0.3)),
     S("Stürmer hält fest und legt ab", "Spieler acht steht vorn mit Spieler vier im Rücken. Spieler vierzehn spielt ihn an, und er legt sofort ab auf Spieler zwölf, der in den Raum startet.",
       ps("b1", [30.4, 27.6]), mv("r12", [36, 17], delay=0.3), ps("b1", [36.6, 17.6], after=True)),
     S("Abschluss: Punkt", "Spieler zwölf schießt direkt, und das gibt einen Punkt für Team Rot. Danach werden die Außen von Team Rot zu Verteidigern, und der Torwart links eröffnet für Team Neon.",
       ps("b1", [9.3, 24]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
