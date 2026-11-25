import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 78-P13 (U15-U17, Woche 28 Phase 5): The Back 4 Unit Advanced Lead. Kein PDF und kein Text: alles aus Video und Ton.
# Platzhälfte bis zur Mittellinie: Länge im Video 10 + 40 Yards = 46 m (gerundet 45 m), Breite nach dem Video etwa 58 Yards = 53 m
# (gerundet 55 m).
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): Hälfte wie im Fernsehbild, echte Linien
# (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Abbildung mit bau/halbfeld.py, Positionen in
# Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie), Feld 45 x 55 m.
# Lage: großes Tor LINKS (Halbfeld(tor="links")). Die Übung erzählt aus Sicht der Viererkette (Team Neon, „unsere Kette“), die
# vom eigenen Tor weg herausrückt und nach dem Ballgewinn auf die Minitore an der Mittellinie kontert: Team Neon spielt nach
# rechts, Team Rot greift nach links an. Gegenüber dem Video (Tor unten) im Uhrzeigersinn gedreht, nicht gespiegelt
# (Video links = oben): Spieler 3 und 7 oben, 2 und 11 unten. Die Drehpfeile (drehen, gegen=...) bleiben wie im Original.
# Rot (Viererkette) + grüner Torwart -> Team Neon (n1 TW, 2, 4, 5, 3), Blau (6, 8, 10 im Mittelfeld, 7 und 11 außen, 9 vorn)
# -> Team Rot; Nummern wie im Video (eindeutig). Großfeldtor (nur C- und B-Jugend).
# Mittelfeldzone (10 Yards = 9 m) an der Mittellinie gestrichelt, darin die zwei Minitore in den Ecken auf der Mittellinie; die
# zwei roten Puppen auf der Zonenlinie als Stangen; Flügelzonen (d 25-36 m, 6 m breit) als Zonen von Team Rot (orange), dazu
# die gestrichelte Linie wie im Video (25 m vor dem Tor). Ein Trainer unten an der Seitenlinie an der Mittellinie (spielt ins
# Mittelfeld). Für den 3D-Abstand stehen die Außenverteidiger beim Herausrücken etwas höher als die Innenverteidiger, Spieler neun
# steht torseitig hinter der Kette (Abseits).
# Grundform nach Ton und Video (0:07-0:50): Mittelfeld passt, Kette schiebt; Pass auf den Flügel, Außenverteidiger presst; der
# Flügelspieler dreht ab und spielt zurück nach innen (ab dann frei); Kette rückt gemeinsam raus, Spieler neun im Abseits.
# Ballgewinn und Treffer ins Minitor als Ergebnis (Ton: „If defenders win possession … finish in either of the two mini goals“);
# Punkt für Team Rot bei einem Treffer ins große Tor ergänzt.
# Fassungen: Coaching-Punkt aus dem Video („Full back must press winger …, but drop to cover“, „Over press leaves space in
# behind“) und Steigerung aus Ton/Video (zwei Mittelfeldspieler greifen mit an, fünf gegen vier; Torwart steht hoch und läuft
# den Ball hinter der Kette ab).
# Sichtkegel: Video-Schlussfolie „Awareness of runners moving in behind - checks“: Spieler vier schaut vor dem Herausrücken
# zu Spieler neun (aus dem Sinn). In der Steigerung ist im Video beim Torwart ein Kegel eingezeichnet („GK plays as a sweeper
# with high line“): Der Torwart schaut nach vorn zum Ball.
# Keine Dublette: UE-166 (03-P3), UE-177 (78-P3), UE-204, UE-206 (10-P7), UE-208 (78-P5), UE-212 (78-P6), UE-242 (78-P7),
# UE-250 (78-P12), UE-302, UE-320 (78-P4), UE-368, UE-370 (78-P8) haben kein Mittelfeld-Dreieck mit Schattenphase, keine
# Flügelzonen und keinen Start „live nach dem Rückpass nach innen“.
F = hf.Halbfeld(tief=45, breit=55, tor="links")   # Tor links (x 10), Mittellinie rechts (x 90), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
def schau(who, p, ziel, weit=20, **k): return h.bl(who, hf.richt(X(p), X(ziel), weit), **k)
T = h.P("T", "c", 85, 55.3, "T")       # unten an der Seitenlinie, an der Mittellinie
ERSATZ = [h.B("s1", 88.5, 55.8), h.B("s2", 91, 55.8)]
POS = {"n1": (3, 27.5), "n3": (21, 7), "n5": (17, 20), "n4": (17, 35), "n2": (21, 48),
       "r9": (24, 27.5), "r6": (41.5, 29), "r10": (39, 42), "r8": (39, 15), "r11": (34, 52), "r7": (34, 3)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "n1" else i[1:]) for i, p in d.items()] + [T]
def li(a, b):
    p, q = X(a), X(b)
    return line(p[0], p[1], q[0], q[1])
def zone(d0, d1, q0, q1):
    a, b = X((d0, q0)), X((d1, q1))
    return {"type": "zone", "x": min(a[0], b[0]), "y": min(a[1], b[1]), "w": round(abs(a[0] - b[0]), 1), "h": round(abs(a[1] - b[1]), 1), "color": "orange"}
MITTE, FLUEGEL = 36, 25                # Linie der Mittelfeldzone (9 m vor der Mittellinie) und Beginn der Flügelzonen
LINES = F.linien() + [li((MITTE, 0), (MITTE, 55)), li((FLUEGEL, 0), (FLUEGEL, 55)), zone(FLUEGEL, MITTE, 0, 6), zone(FLUEGEL, MITTE, 49, 55)]
TORE = [F.tor()] + F.minitore(5, 50)
CONES = [C(*X((MITTE, q)), shape="stange") for q in (20.5, 34.5)]
MINI_OBEN = [round(X((45, 5))[0] - 0.3, 1), X((45, 5))[1]]
ABFANG = (29, 26)                      # dort geht Spieler fünf dazwischen

u = {"title": "Viererkette mit hoher Linie", "code": "UE-380", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 13,
 "field_size": "55 x 45 m",
 "description": "Die Viererkette mit Torwart verteidigt das große Tor gegen sechs Angreifer. Erst lassen drei Mittelfeldspieler den Ball laufen, und die Kette schiebt mit dem Ball. Geht der Pass auf einen Flügel, presst der Außenverteidiger, und nach dem Rückpass nach innen ist das Spiel frei. Die Kette rückt gemeinsam raus, stellt die Angreifer ins Abseits und kontert nach dem Ballgewinn auf zwei Minitore.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte, etwa 55 mal 45 Meter, mit großem Tor und Strafraum. An der Mittellinie eine Zone von 9 Metern Tiefe mit zwei Minitoren in den Ecken und zwei Stangen davor, außen zwei schmale Flügelzonen.",
  "Verteilen: Team Neon mit Torwart und Viererkette vor dem eigenen Strafraum. Team Rot mit drei Spielern in der Mittelfeldzone, je einem Flügelspieler in den Flügelzonen und einer Spitze. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Der Trainer spielt ins Mittelfeld, und die drei lassen den Ball laufen. Der Pass auf einen Flügel ist das Signal für den Außenverteidiger. Der Flügelspieler dreht ab und spielt zurück nach innen, ab dann ist das Spiel frei und die Kette rückt gemeinsam raus.",
  "Wertung: Ein Treffer von Team Rot ins große Tor gibt einen Punkt für Team Rot, ein Treffer von Team Neon in ein Minitor einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball ins Mittelfeld."],
 "organisation_show": ORG,
 "coaching_points": ["Die Kette schiebt immer mit dem Ball", "Außen pressen, aber nicht zu weit raus", "Über die Schulter schauen, wo die Läufer sind", "Zusammen raus, laut rufen"],
 "materials": ["1 Großfeldtor", "2 Minitore", "2 Stangen", "Hütchen für die Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette mit hoher Linie. Die Kette verteidigt gegen sechs Angreifer, schiebt mit dem Ball, presst außen und rückt gemeinsam raus.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [h.B("b1", *hf.am_fuss([T["x"], T["y"]]))] + ERSATZ,
  "steps": [
   S("Mittelfeld lässt den Ball laufen", "Der Trainer spielt zu Spieler sechs, und der gibt weiter zu Spieler zehn. Noch greift keiner an. Unsere Kette schiebt mit dem Ball zur Seite, alle vier zusammen.",
     zu("b1", POS["r6"]), zu("b1", POS["r10"], after=True),
     lauf("n2", (21.5, 50), delay=1.0), lauf("n4", (17.5, 38), delay=1.0), lauf("n5", (17.5, 23), delay=1.0), lauf("n3", (21.5, 11), delay=1.0)),
   S("Pass auf den Flügel, Spieler zwei presst", "Spieler zehn spielt raus auf Spieler elf. Das ist das Signal. Spieler zwei läuft ihn an, die anderen drei rücken nach und schieben zur Ballseite.",
     zu("b1", POS["r11"]), lauf("n2", (30, 50), delay=0.4), lauf("n4", (20.5, 38), delay=0.6), lauf("n5", (19, 24), delay=0.6), lauf("n3", (23, 13), delay=0.6)),
   S("Rückpass nach innen, die Kette rückt raus", "Spieler elf dreht ab und spielt zurück zu Spieler zehn. Ab jetzt ist das Spiel frei. Spieler vier schaut kurz, wo Spieler neun steht, und ruft. Die ganze Kette rückt zusammen raus, Spieler neun steht im Abseits.",
     h.drehen("r11", X(POS["r10"])), zu("b1", POS["r10"], after=True), schau("n4", (20.5, 38), POS["r9"], delay=0.4),
     lauf("n2", (31, 47), delay=1.6), lauf("n4", (27.5, 36), delay=1.6), lauf("n5", (27.5, 22), delay=1.6), lauf("n3", (31, 12), delay=1.6)),
   S("Abgefangen, ins Minitor: Punkt", "Spieler zehn spielt trotzdem steil. Spieler fünf ist näher dran, geht dazwischen und hat den Ball. Er dribbelt außen vorbei und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Spieler sechs.",
     zu("b1", ABFANG), lauf("n5", ABFANG, delay=0.2), h.dr("n5", "b1", X((33, 12)), after=True), h.ps("b1", MINI_OBEN, after=True))],
  "dims": F.masslinie("45 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Außen pressen, aber nicht zu weit.", "Pressen, nicht zu weit",
    "Kommt der Ball auf den Flügel, läuft der Außenverteidiger an, so nah, dass der Flügelspieler nicht aufdrehen kann. Spielt der Flügelspieler zurück, geht der Außenverteidiger sofort zurück in die Kette. Läuft er weiter hinterher, ist hinter ihm ein großes Loch.",
    sp(), [h.B("b1", *fu(POS["r8"]))] + ERSATZ,
    [S("Pass raus, Spieler drei presst", "Spieler acht spielt raus auf Spieler sieben. Spieler drei läuft ihn an, aber nicht blind. Er bleibt so nah, dass Spieler sieben nicht aufdrehen kann. Die anderen schieben rüber.",
       zu("b1", POS["r7"]), lauf("n3", (30, 5), delay=0.4), lauf("n5", (17, 17), delay=0.6), lauf("n4", (17, 32), delay=0.6), lauf("n2", (21, 43), delay=0.6)),
     S("Sofort zurück in die Kette", "Spieler sieben dreht ab und spielt zurück. Jetzt läuft Spieler drei nicht weiter hinterher. Er geht sofort zurück in die Kette, sonst ist hinter ihm ein großes Loch.",
       h.drehen("r7", X(POS["r8"]), gegen=True), zu("b1", POS["r8"], after=True), lauf("n3", (21.5, 7), after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei aus dem Mittelfeld greifen mit an.", "Fünf gegen vier",
    "Nach dem Pass auf die Spitze dürfen zwei Mittelfeldspieler mit angreifen, und es steht fünf gegen vier. Die Kette muss jetzt genauer entscheiden, wann sie rausrückt. Weil sie hoch steht, steht auch der Torwart hoch und läuft Bälle hinter der Kette ab.",
    sp(), [h.B("b1", *fu(POS["r10"]))] + ERSATZ,
    [S("Steil, prallen lassen, nachrücken", "Spieler zehn spielt steil auf Spieler neun. Der lässt den Ball prallen auf Spieler sechs, der nachrückt. Jetzt greifen Spieler sechs und Spieler zehn mit an. Fünf gegen vier.",
       zu("b1", POS["r9"]), lauf("n5", (20, 24), delay=0.4), lauf("r6", (33, 30), delay=0.2), zu("b1", (33, 30), after=True), lauf("r10", (29, 40), delay=0.6)),
     S("Torwart steht hoch", "Unser Torwart rückt mit der Kette auf und steht vor dem Tor, nicht auf der Linie. Er schaut, was Spieler sechs vorhat.",
       lauf("n1", (12, 27.5)), schau("n1", (12, 27.5), (33, 30), after=True)),
     S("Ball hinter die Kette, Torwart ist da", "Spieler sechs spielt den Ball hinter die Kette, Spieler elf startet. Der Torwart ist zuerst am Ball und fängt ihn. Jetzt geht es schnell auf die Minitore.",
       lauf("r11", (20, 53)), lauf("r11", (11, 45), after=True), h.ps("b1", X((9, 42)), delay=0.3),
       h.mv("n1", [round(X((9, 42))[0] - 0.6, 1), round(X((9, 42))[1] - 0.6, 1)], delay=0.5))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
