import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 56-P9 (U15-U17, Woche 29 Phase 3): Striker-Winger Combinations to Attack (Function). 50 x 45 Yards = 46 x 41 m
# (gerundet 45 x 40 m), Annahmezone 8 Yards = 7 m quer durchs Feld, etwas unterhalb der Mitte (gestrichelt, Hütchen an den Enden).
# Ausrichtung wie im PDF: großes Tor mit neutralem Torwart oben (Großfeldtor, nur C- und B-Jugend), zwei Minitore unten in den
# Ecken (im PDF schräg, hier gerade). Feld x 23-77, y 4-52, in beiden Richtungen fast derselbe Maßstab. Kein Großfeld und kein
# langes Feld (Verhältnis 1,1). Strafraum und Torraum in den Maßen der Skizze.
# Navy (Angreifer) -> Team Neon mit den Nummern aus dem PDF (9, 11, 7; Wartende 3 und 2 neben der Zone, 4, 10 und 6 nur im Text).
# Pink (Verteidiger) -> Team Rot, neu nummeriert (Nummern doppelt): 4 -> 12, 6 -> 13, 5 bleibt.
# Ein Trainer statt zwei, unten in der Mitte (PDF: „coach positioned at the base of the pitch initiates play“).
# 3D-Abstand: Spieler fünf und Spieler neun stehen nicht hintereinander wie im PDF, Spieler neun steht halbrechts.
# Grundform nach der Skizze: Trainer auf Spieler sieben in der Zone, Andribbeln nach innen, Spieler neun läuft schräg, Pass in den
# Lauf, Abschluss. Konter von Team Rot auf die Minitore im Text und in der zweiten Steigerung.
# Fassungen: Progression 1 (drei senkrechte Bahnen, jede immer besetzt, Rotation) und Progression 2 (Springer nur auf den
# Außenbahnen, kontert mit Team Rot).
# Sichtkegel: Ton „Effective positioning and awareness are crucial to receiving in space“, im Video nicht eingezeichnet.
# Richtung aus dem Sinn: der Flügelspieler schaut vor dem Pass zum Lauf der Spitze.
T = P("T", "c", 50, 55.5, "T")  # unten in der Mitte hinter der Linie
ERSATZ = [B("s1", 53.5, 56), B("s2", 56, 56)]
TW = P("k", "t", 50, 6, "TW")
POS = {"r5": (50, 21.5), "r12": (35, 22), "r13": (67, 22), "n9": (58.5, 25), "n11": (26.5, 28), "n7": (75.5, 35.5),
       "n3": (15, 36), "n2": (85, 36)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + list(extra) + [TW, T]
ZY0, ZY1 = 31.8, 39.6
LINES = [rect(23, 4, 54, 48), rect(32.5, 4, 35, 13), rect(41.2, 4, 17.6, 5.2), line(23, ZY0, 77, ZY0), line(23, ZY1, 77, ZY1)]
BAHNEN = [line(41, 4, 41, 52), line(59, 4, 59, 52)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}, {"x": 30, "y": 52, "side": "bottom"}, {"x": 70, "y": 52, "side": "bottom"}]
CONES = [C(23, ZY0), C(77, ZY0), C(23, ZY1), C(77, ZY1)]
DIMS = dims(23, 77, 4, 52, "45 m", "40 m", rx=92)
BT = [50.6, 56.1]
F = P("f", "t", 75.5, 13, "F")

u = {"title": "Flügel und Spitze im 3 gegen 3", "code": "UE-383", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Torschuss", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 7, "players_max": 12,
 "field_size": "45 x 40 m",
 "description": "Drei Angreifer spielen gegen drei Verteidiger auf ein großes Tor mit Torwart. Der Trainer spielt einen Flügelspieler in einer Zone an, der sofort auf die Abwehr zudribbelt. Mit Läufen der Spitze und Kombinationen über den Flügel spielen sich die Angreifer zum Abschluss. Erobert Team Rot den Ball, kontert es auf zwei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 40 Metern mit einem großen Tor und Torwart. An der Linie gegenüber stehen zwei Minitore in den Ecken. Etwas unterhalb der Mitte markieren vier Hütchen quer durchs Feld eine Zone von 7 Metern Tiefe.",
  "Verteilen: Team Neon mit drei Angreifern, zwei außen und einer in der Mitte, gegen drei Verteidiger von Team Rot. Weitere Flügelspieler warten außen neben der Zone. Der Trainer steht mit den Bällen in der Mitte zwischen den Minitoren.",
  "Ablauf: Der Trainer spielt einen Flügelspieler in der Zone an. Der dribbelt auf die Abwehr zu, und die drei Angreifer spielen sich bis zum Abschluss durch. Erobert Team Rot den Ball, kontert es sofort auf eines der beiden Minitore.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt, für Team Neon im großen Tor, für Team Rot in einem Minitor. Nach jedem Angriff kommen neue Flügelspieler rein, und der Trainer spielt abwechselnd auf beide Seiten an."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem Ball sofort auf die Abwehr zu", "Die Spitze läuft schräg hinter den Verteidiger", "Kopf hoch, dann der Pass in den Lauf", "Ball verloren? Sofort zurück"],
 "materials": ["1 großes Tor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Flügel und Spitze im drei gegen drei. Der Flügelspieler bekommt den Ball, zieht nach innen und spielt mit der Spitze zum Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *BT)] + ERSATZ,
  "steps": [
   S("Trainer spielt in die Zone", "Der Trainer spielt den Ball zu Spieler sieben in die Zone auf dem Flügel. Ab jetzt läuft das drei gegen drei.",
     ps("b1", [76.1, 36.1])),
   S("Andribbeln nach innen", "Spieler sieben dribbelt sofort nach innen auf die Abwehr zu. Spieler dreizehn muss raus. Genau jetzt startet Spieler neun schräg hinter ihn, und auf der anderen Seite geht Spieler elf Richtung Tor.",
     dr("n7", "b1", [65, 28.5]), mv("r13", [69, 25.5], delay=0.3), mv("n9", [60, 13], delay=0.4), mv("n11", [29, 14], delay=0.4)),
   S("Kopf hoch, Pass in den Lauf", "Spieler sieben nimmt den Kopf hoch, sieht den Lauf und spielt flach in den Raum hinter Spieler dreizehn.",
     bl("n7", [60, 13]), ps("b1", [60.6, 13.6], after=True)),
   S("Abschluss: Punkt", "Spieler neun nimmt mit und schießt flach ins kurze Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer auf die andere Seite, und die nächsten Flügelspieler kommen rein.",
     ps("b1", [55, 4.3]))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Drei Bahnen, und jede muss besetzt sein.", "Drei Bahnen, immer besetzt",
    "Zwei Linien teilen das Feld in drei Bahnen. In jeder Bahn muss immer ein Angreifer sein. Zieht einer mit dem Ball in eine andere Bahn, muss der Spieler dort raus und eine freie Bahn besetzen. So bleibt das Spiel breit, und die Abwehr muss sich ständig neu sortieren.",
    sp(), [B("b1", *BT)] + ERSATZ,
    [S("Spieler sieben zieht in die Mitte", "Der Trainer spielt Spieler sieben an. Der dribbelt nach innen in die mittlere Bahn. Also muss Spieler neun raus, und er geht nach außen in die freie Bahn.",
       ps("b1", [76.1, 36.1]), dr("n7", "b1", [55, 28], after=True), mv("n9", [70, 14], delay=0.6)),
     S("Pass nach außen, Lauf in die Mitte", "Spieler sieben spielt raus zu Spieler neun. Spieler elf bleibt in seiner Bahn und läuft Richtung langer Pfosten.",
       ps("b1", [70.6, 14.6]), mv("n11", [29, 17], delay=0.2), mv("n11", [39, 10.5], after=True)),
     S("Flach zurück: Punkt", "Spieler neun spielt flach zurück vor das Tor. Spieler elf schiebt ein, und das gibt einen Punkt für Team Neon.",
       ps("b1", [39.6, 11.1]), ps("b1", [45, 4.3], after=True))],
    lines=LINES + BAHNEN, dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Springer spielt außen mit.", "Ein Springer auf dem Flügel",
    "Ein Springer spielt nur auf den Außenbahnen. Er hilft dem Team mit Ball bei Doppelpässen am Flügel und schafft dort Überzahl. Erobert Team Rot den Ball, kontert der Springer mit Team Rot auf die Minitore.",
    sp(extra=[F]), [B("b1", *BT)] + ERSATZ,
    [S("Spieler sieben spielt den Springer an", "Der Trainer spielt Spieler sieben an. Der spielt sofort weiter zum Springer, der weiter vorn an der Linie steht.",
       ps("b1", [76.1, 36.1]), ps("b1", [76.1, 13.6], after=True)),
     S("Pass nach innen, abgefangen", "Spieler sieben startet nach innen, und der Springer will ihm den Ball zurückgeben. Doch Spieler dreizehn läuft dazwischen und hat den Ball.",
       mv("n7", [66, 27]), ps("b1", [69.4, 18.6], delay=0.6), mv("r13", [69, 18], delay=0.5)),
     S("Konter mit dem Springer: Punkt", "Jetzt kontert Team Rot. Spieler dreizehn spielt sofort zum Springer, der die Linie runtersprintet. Der schießt ins Minitor, und das gibt einen Punkt für Team Rot.",
       mv("f", [74, 40]), ps("b1", [74.6, 40.6], delay=0.4), dr("f", "b1", [71.5, 47.5], after=True), ps("b1", [70, 51.6], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
