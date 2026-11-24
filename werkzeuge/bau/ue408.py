import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 32-P8 (U15-U17, Woche 39 Phase 2): Developing the Diamond in Possession (Wave of Play, Rondo to Finish). 20 x 25 Yards =
# 18 x 23 m (gerundet 18 x 25 m), Feld x 30-70, y 5-55, Mittellinie gestrichelt, oben und unten ein Großfeldtor (C- und B-Jugend)
# mit Torwart. Verhältnis 1,25: hochkant wie im PDF, nicht gedreht (Start unten, der Ball geht nach oben). Kein Großfeld.
# PDF/Video weiß-blau (Ballbesitz) -> Team Neon mit den Nummern aus dem Video: unten 4, 6 und 11 (Spitze der Raute an der
# Mittellinie), oben 8 und 2. Grüne Torhüter -> neutrale Torhüter (k1 oben, k2 unten); sie spielen in der Raute ihrer Hälfte mit
# und halten das Tor. PDF/Video rot (Verteidiger) -> Team Rot, neu nummeriert wegen doppelter Nummern: innen 10 und 9 wie im Video,
# an den Seiten 6 -> 5, 8 -> 7, 4 -> 12, 3 bleibt. Die Spieler an der Seite stehen nicht als Paar an der Mittellinie, sondern
# je einer pro Hälfte (3D-Abstand). Alle Figuren auf einem Spaltenraster (x 33, 41.5, 50, 58.5, 67), ein Trainer statt zwei.
# Grundform nach PDF-Schritten 1-5 und Video: 4 gegen 2 unten, sechs Pässe, Pass nach oben, Spieler elf wechselt die Hälfte,
# zwei Verteidiger von der Seite kommen rein (die zwei von unten gehen an die Seite), Ballgewinn und Abschluss oben.
# Im PDF spielt der rechte Spieler den Ball nach oben; hier ist der sechste Pass der zu Spieler elf, der aufdreht und nach oben spielt
# (in der Raute landet der Ball nach einer geraden Zahl von Pässen am Rand wieder beim Torwart oder bei der Spitze).
# Rollenwechsel nach jedem Treffer oder nach einer festen Zeit wie im PDF (wer genau tauscht, zeigt das Original nicht).
# Fassungen: PDF Key Coaching Point 1 (Verteidiger zu weit auseinander, Steilpass durch die Lücke) und 2 (die Raute schafft
# Passwinkel, Anspielstationen als dünne Pfeile).
# Sichtkegel aus Text und Ton („See gaps early to play through to other area“, „observe defenders leaving space open“): Spieler elf
# schaut vor der Annahme zum Passgeber und schwenkt danach nach oben (bl mit von plus drehen); im Coaching-Punkt schaut der Torwart
# vor dem Steilpass zu Spieler elf. Im Video kein Kegel eingezeichnet.
# Keine Dublette: UE-151 (32-P6, innere Zone mit Minitoren), UE-374 (87-P5, Raute 4 gegen 2 mit Umschalten ins 6 gegen 4),
# UE-236 (25-P8, Pressingwelle 3 gegen 3), UE-390 (36-P8, Welle in drei Zonen) haben andere Organisation und Abläufe.
# UE-409 (32-P12) ist eine Passfolge ohne Gegner in der Raute, ganz anderer Ablauf.
T = P("T", "c", 24, 55.5, "T")
ERSATZ = [B("s1", 20, 54.5), B("s2", 20.5, 58)]
TW = {"k1": (50, 7.5), "k2": (50, 52.5)}
NEON = {"n4": (33, 42), "n6": (67, 42), "n11": (50, 32.5), "n8": (33, 17), "n2": (67, 17)}
ROT = {"r10": (41.5, 41), "r9": (58.5, 41), "r5": (24, 21), "r7": (24, 39), "r3": (76, 21), "r12": (76, 39)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(TW); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(30, 5, 40, 50), line(30, 30, 70, 30)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 55, "side": "bottom", "size": "gross"}]
CONES = ecken(30, 5, 40, 50) + [C(30, 30), C(70, 30)]
DIMS = dims(30, 70, 5, 55, "18 m", "25 m", rx=90)
N = lambda i: NEON[i]

u = {"title": "Rauten-Rondo über zwei Hälften", "code": "UE-408", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "18 x 25 m",
 "description": "Ein Rondo in zwei Hälften mit je einem Tor und Torwart. Unten spielen vier gegen zwei in einer Raute, der Torwart spielt mit. Nach sechs Pässen am Stück darf der Ball in die andere Hälfte, die Spitze der Raute wechselt mit, und zwei neue Verteidiger kommen von der Seite. Erobern die Verteidiger den Ball, schließen sie sofort aufs Tor ab.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern, in der Mitte geteilt. Oben und unten ein Tor mit Torwart.",
  "Verteilen: Unten bilden der Torwart, Spieler vier, Spieler sechs und Spieler elf eine Raute, Spieler elf steht an der Mittellinie. Oben warten der Torwart, Spieler acht und Spieler zwei. Zwei Verteidiger von Team Rot jagen unten den Ball, vier weitere warten an den Seiten. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Vier gegen zwei unten. Nach sechs Pässen am Stück darf der Ball nach oben. Spieler elf wechselt mit in die obere Hälfte, zwei Verteidiger von der Seite kommen rein, die zwei von unten gehen raus. Oben geht es wieder mit sechs Pässen los, dann zurück nach unten.",
  "Wertung und Wechsel: Erobern die Verteidiger den Ball, spielen sie schnell zusammen und schließen auf das Tor ihrer Hälfte ab. Jeder Treffer gibt einen Punkt für Team Rot. Nach jedem Treffer oder nach ein paar Minuten tauschen Team Neon und Team Rot die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und genau passen, durch die Lücke zwischen zwei Verteidigern", "Breit stehen, damit die Raute Passwinkel hat", "Kopf hoch, früh die Lücke nach oben sehen", "Verteidiger laufen zusammen an und machen die Winkel zu"],
 "materials": ["2 Großfeldtore", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rauten-Rondo über zwei Hälften. Vier gegen zwei in einer Raute, nach sechs Pässen geht der Ball in die andere Hälfte. Erobern die Verteidiger den Ball, schießen sie sofort aufs Tor, und ein Treffer gibt einen Punkt für Team Rot.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *f(TW["k2"]))] + ERSATZ,
  "steps": [
   S("Vier gegen zwei unten", "Unten steht die Raute. Der Torwart, Spieler vier, Spieler sechs und vorn an der Mittellinie Spieler elf. Der Torwart spielt zu Spieler vier, Spieler zehn läuft an. Weiter geht es über Spieler elf zu Spieler sechs.",
     ps("b1", f(N("n4"))), mv("r10", [36, 47], delay=0.3), ps("b1", f(N("n11")), after=True), ps("b1", f(N("n6")), after=True)),
   S("Sechs Pässe am Stück", "Spieler neun rückt raus, der Ball geht zurück zum Torwart und gleich wieder zu Spieler vier. Spieler elf schaut zum Ball, und schon kommt der Pass zu ihm. Das ist der sechste Pass.",
     mv("r9", [61, 46.5]), ps("b1", f(TW["k2"]), delay=0.3), mv("r10", [41.5, 44], delay=0.4), ps("b1", f(N("n4")), after=True),
     bl("n11", list(N("n4")), after=True), ps("b1", f(N("n11")), after=True)),
   S("Aufdrehen, Pass nach oben", "Sechs Pässe, der Ball darf nach oben. Spieler elf dreht auf und spielt zu Spieler zwei. Dann wechselt er selbst in die obere Hälfte. Spieler fünf und Spieler drei kommen von der Seite rein, Spieler zehn und Spieler neun gehen raus.",
     bl("n11", list(N("n2")), von=list(N("n4")), dauer=1.3), drehen("n11", list(N("n2")), delay=0.4), ps("b1", f(N("n2")), after=True),
     mv("n11", [50, 26], after=True), mv("r5", [41.5, 21], delay=1.6), mv("r3", [58.5, 21], delay=1.6),
     mv("r10", [21, 48], delay=1.8), mv("r9", [72, 50], delay=1.8), mv("r9", [79, 49], after=True)),
   S("Oben vier gegen zwei", "Oben läuft jetzt das Gleiche. Spieler zwei spielt zum Torwart, der zu Spieler acht. Spieler acht will flach in die Mitte zu Spieler elf. Spieler fünf steht im Passweg und fängt den Ball ab.",
     ps("b1", f(TW["k1"])), ps("b1", f(N("n8")), after=True), mv("r5", [41.5, 23.5], delay=1.2), ps("b1", [42.1, 24.1], after=True)),
   S("Ballgewinn, Abschluss: Punkt", "Spieler fünf zieht sofort Richtung Tor und schießt flach ins Eck, und das gibt einen Punkt für Team Rot. Danach tauschen Team Neon und Team Rot die Rollen, und der Torwart unten startet mit dem nächsten Ball.",
     dr("r5", "b1", [44, 14]), ps("b1", [45.5, 5.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Lücke sehen und steil durchspielen.", "Lücke sehen, steil spielen",
    "Laufen die zwei Verteidiger nicht zusammen, entsteht zwischen ihnen eine Lücke. Wer sie früh sieht, spielt den Ball senkrecht durch. Ein Pass, und beide Verteidiger sind aus dem Spiel.",
    sp(), [B("b1", *f(TW["k2"]))] + ERSATZ,
    [S("Zu weit auseinander", "Spieler zehn läuft Spieler vier an, Spieler neun geht zu Spieler sechs. Jeder läuft für sich. In der Mitte ist die Lücke riesig.",
       mv("r10", [37.5, 46.5]), mv("r9", [62.5, 46.5], delay=0.1)),
     S("Steil durch die Lücke", "Der Torwart sieht Spieler elf frei an der Mittellinie. Flach und scharf spielt er durch die Lücke. Beide Verteidiger sind mit einem Pass raus.",
       bl("k2", list(N("n11"))), ps("b1", f(N("n11")), after=True)),
     S("Aufdrehen und nach oben", "Spieler elf dreht auf. Die sechs Pässe sind voll, also geht der Ball sofort nach oben zu Spieler acht. Danach wechselt Spieler elf in die obere Hälfte.",
       bl("n11", list(N("n8")), von=list(TW["k2"]), dauer=1.3), drehen("n11", list(N("n8")), gegen=True, delay=0.4),
       ps("b1", f(N("n8")), after=True), mv("n11", [50, 26], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Raute gibt Passwinkel.", "Die Raute gibt Passwinkel",
    "Die Raute steht breit und tief. So hat der Ballführer immer mehrere Anspielstationen, nach vorn, zur Seite oder zurück. Kommt Druck, läuft der Ball einfach um den Verteidiger herum.",
    sp(), [B("b1", *f(TW["k2"]))] + ERSATZ,
    [S("Druck auf den Torwart", "Spieler zehn läuft den Torwart an. Der hat trotzdem zwei freie Anspielstationen, links und rechts. Die Raute steht breit genug.",
       mv("r10", [43.5, 47.5]), opt("k2", f(N("n4")), delay=0.5), opt("k2", f(N("n6")), delay=0.5)),
     S("Am Druck vorbei", "Der Torwart spielt zu Spieler sechs. Spieler neun kommt, aber vorn wartet Spieler elf. Ein Kontakt, und der Ball ist an Spieler neun vorbei.",
       ps("b1", f(N("n6"))), mv("r9", [62, 45], delay=0.3), opt("n6", f(N("n11")), after=True), ps("b1", f(N("n11")), after=True)),
     S("Nach vorn, zur Seite, zurück", "Spieler elf hat wieder drei Möglichkeiten. Er legt quer auf Spieler vier, Spieler zehn kommt zu spät. So läuft der Ball, bis die sechs Pässe voll sind.",
       opt("n11", f(N("n4"))), opt("n11", f(N("n6"))), opt("n11", f(TW["k2"])), ps("b1", f(N("n4")), after=True), mv("r10", [38, 44], delay=0.3))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
