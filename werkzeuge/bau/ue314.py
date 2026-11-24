import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 10-P11 (U15-U17, Woche 14): High Press to Win Possession. Halbes Großfeld in voller Breite = Feld x 10-90, y 5-55,
# großes Tor oben (Großfeldtor, C- und B-Jugend), zwei Minitore auf der gestrichelten Linie kurz vor der Mittellinie.
# Ausrichtung wie im PDF: Team Neon (im PDF Pink) presst nach oben, Team Rot (im PDF Blau) baut vom Torwart aus auf.
# Neon behält die Nummern aus dem PDF (2, 3, 6, 8, 9, 10, 11). Rot neu nummeriert, weil alle Nummern doppelt wären:
# Blau 6 -> 5, Blau 4 -> 4, Blau 2 -> 12, Blau 8 -> 14, Blau 5 -> 7, Blau 10 -> 15, Blau 3 -> 13, Torwart = r1 "TW".
# Die Paare aus dem PDF stehen etwas weiter auseinander (3D-Abstand). Mittelkreis weggelassen. Ein Trainer statt zwei.
# Grundform = Szene aus PDF und Video ("FB presses - CM covers"): Abstoß kurz nach rechts, Spieler zwei läuft an,
# Spieler acht sichert und fängt den Pass die Linie entlang ab. Fassung 1 = Gegenbeispiel aus dem Ton (Außenspieler presst
# zu früh allein, der Weg außen ist offen). Fassung 2 = "High press forces GK error" aus dem Video.
# Sichtkegel: im Video keiner eingezeichnet; aus dem Ton ("even if they are able to get their head up to switch, as we
# can see from our keeper"): Der Torwart hebt unter Druck den Kopf und sucht die Verlagerung (Fassung 2).
# Kein Dubletten-Fall: UE-148 (3 gegen 3 in Duellen), UE-236 (Pressingwelle 3 gegen 3), UE-243 (Dreierkette) sind andere Formen.
T = P("T", "c", 4.5, 30, "T")
ERSATZ = [B("s1", 6.1, 33.5), B("s2", 2.5, 33.5)]
NEON = {"n11": (41.5, 19), "n9": (59.5, 20), "n3": (23.5, 28), "n10": (41.5, 35), "n8": (68, 34), "n6": (50, 46), "n2": (76.5, 41.5)}
ROT = {"r5": (33, 15), "r4": (68, 17), "r12": (15, 24), "r14": (50, 26), "r7": (77, 26), "r15": (58.5, 41.5), "r13": (85.5, 32)}
def sp(**k):
    n = dict(NEON); r = dict(ROT); tw = k.pop("r1", (50.9, 7.3))
    for i, v in k.items(): (n if i in n else r)[i] = v
    return [P("r1", "b", tw[0], tw[1], "TW")] + [P(i, "b", x, y, i[1:]) for i, (x, y) in r.items()] \
        + [P(i, "a", x, y, i[1:]) for i, (x, y) in n.items()] + [T]
LINES = [rect(10, 5, 80, 50), rect(24.9, 5, 50.7, 16.8), rect(38.6, 5, 23.1, 5.5), line(10, 49, 90, 49)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 20.4, "y": 49, "side": "bottom"}, {"x": 78.8, "y": 49, "side": "bottom"}]

u = {"title": "Pressingfalle am Flügel", "code": "UE-314", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 18,
 "field_size": "Halbes Spielfeld",
 "description": "Sieben gegen sieben auf einer Spielfeldhälfte, dazu ein Torwart. Team Rot baut mit einem kurzen Abstoß auf und will eines der zwei Minitore treffen. Team Neon presst hoch, lenkt den Ball auf eine Seite und schnappt dort gemeinsam zu. Nach dem Ballgewinn geht es sofort auf das große Tor.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite. Oben steht das große Tor, kurz vor der Mittellinie stehen zwei Minitore.",
  "Verteilen: Team Rot baut mit Torwart und sieben Feldspielern auf. Team Neon presst mit sieben Feldspielern, jeder hat einen Gegenspieler. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart eröffnet mit einem kurzen Abstoß. Team Neon lenkt den Ball auf eine Seite und greift dort gemeinsam zu. Nach dem Ballgewinn geht es sofort zum Abschluss.",
  "Wertung: Ein Treffer von Team Neon ins große Tor gibt einen Punkt. Spielt sich Team Rot frei und trifft ein Minitor, gibt das einen Punkt für Team Rot. Weiter geht es immer beim Torwart, auf Kommando des Trainers."],
 "organisation_show": ORG,
 "coaching_points": ["Erst stehen alle, dann pressen alle", "Außen anlaufen, dahinter sichert der Sechser", "Rückpass zustellen, den langen Ball erzwingen", "Nach dem Ballgewinn sofort zum Tor"],
 "materials": ["1 großes Tor", "2 Minitore", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pressingfalle am Flügel. Sieben gegen sieben auf einer Hälfte. Team Rot baut vom Torwart aus auf, Team Neon presst hoch und holt sich den Ball außen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 51.5, 7.9)] + ERSATZ,
  "steps": [
   S("Kurzer Abstoß nach rechts", "Team Neon steht hoch, jeder hat seinen Gegenspieler. Der Torwart spielt den Abstoß kurz nach rechts, Spieler sieben kommt dem Ball entgegen.",
     mv("r7", [82, 16]), ps("b1", [82.6, 16.6], delay=0.4)),
   S("Zwei läuft an, Acht sichert", "Das ist das Signal. Spieler zwei sprintet von innen auf Spieler sieben. Vorne stellt Spieler neun den Rückpass zu, und hinter Spieler zwei schiebt Spieler acht nach außen.",
     mv("n2", [78.5, 19]), mv("n9", [72, 22], delay=0.2), mv("n8", [80, 31], delay=0.4), mv("n11", [50, 17], delay=0.4), mv("n10", [47, 31], delay=0.4)),
   S("Pass die Linie runter, abgefangen", "Spieler sieben bleibt nur der Pass die Linie entlang. Genau darauf wartet Spieler acht. Er geht dazwischen und hat den Ball.",
     ps("b1", [84.7, 26]), mv("n8", [84.1, 25.4], delay=0.2), mv("r1", [53.5, 7.3], delay=0.3)),
   S("Schnell zum Abschluss: Punkt", "Jetzt schnell. Spieler acht spielt flach auf Spieler neun, der zieht nach innen und schießt ins lange Eck. Das gibt einen Punkt für Team Neon. Der nächste Ball liegt wieder beim Torwart, und los geht es erst auf Kommando des Trainers.",
     ps("b1", [72.6, 22.6]), dr("n9", "b1", [64, 22], after=True), ps("b1", [47.5, 5.3], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst stehen alle, dann pressen alle.", "Erst stehen, dann pressen",
    "Gepresst wird nur, wenn alle bereit stehen. Läuft einer zu früh allein los, ist hinter ihm der Weg frei, und mit zwei Pässen ist das Pressing überspielt. Also erst die Abstände prüfen und dann gemeinsam starten.",
    sp(r7=(82, 16)), [B("b1", 82.6, 16.6)] + ERSATZ,
    [S("Zwei presst allein", "So geht es schief. Spieler zwei rennt allein los. Hinter ihm rückt keiner nach, und außen ist alles offen.",
       mv("n2", [78.5, 19])),
     S("Außen durch: Punkt für Team Rot", "Ein Pass die Linie entlang, und Spieler dreizehn hat freie Bahn. Spieler acht kommt zu spät. Der Ball rollt ins Minitor, und das gibt einen Punkt für Team Rot.",
       ps("b1", [86.1, 32.6]), dr("r13", "b1", [84, 42], after=True), mv("n8", [78, 36], delay=0.8), ps("b1", [79.2, 49.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den langen Ball erzwingen.", "Langen Ball erzwingen",
    "Sind die kurzen Wege zu, muss der Torwart lang spielen. Ein langer Ball unter Druck kommt selten genau. Darum bleiben die Spieler auf der anderen Seite wach und gehen früh dazwischen.",
    sp(), [B("b1", 68.6, 17.6)] + ERSATZ,
    [S("Rückpass zum Torwart", "Spieler vier hat den Ball. Spieler neun läuft ihn an, und es bleibt nur der Rückpass zum Torwart.",
       mv("n9", [64.5, 19]), ps("b1", [51.5, 7.9], delay=0.4)),
     S("Torwart unter Druck, Kopf hoch", "Spieler neun läuft durch bis zum Torwart. Spieler elf stellt den kurzen Pass nach links zu. Der Torwart hebt den Kopf und sucht die Verlagerung.",
       mv("n9", [56, 10.5]), mv("n11", [41, 11.5], delay=0.2), bl("r1", [31, 21], delay=0.6)),
     S("Langer Ball, abgefangen", "Er schlägt den Ball lang nach links. Unter Druck wird der Pass ungenau. Spieler drei ist vor Spieler zwölf am Ball, und von hier ist der Weg zum Tor kurz.",
       ps("b1", [23.6, 31.6]), mv("r12", [16, 34], delay=0.2), mv("n3", [23, 31], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
