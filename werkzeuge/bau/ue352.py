import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 36-P11 (U15-U17, Woche 19 Phase 1): Developing the 433: Midfield Rotations, Medium Sided Game. Halbes Spielfeld in voller Breite.
# HALBES FELD QUER (Inhaber, 25.11.2026; dieses Skript ist das Vorbild, Regel in AUFTRAG.md): Die Hälfte liegt wie im Fernsehbild,
# großes Tor rechts, Mittellinie links mit zwei Minitoren, Platzbreite von oben nach unten, echte Linien (Strafraum, Torraum,
# Strafraumbogen, halber Mittelkreis), "massstab": "gross". Team Neon baut an der Mittellinie auf und greift nach rechts an.
# Abbildung mit bau/halbfeld.py: Positionen in Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie,
# Hälfte 50 x 65 m), F(d, q) rechnet auf die Tafel um (x 10-90, y 3-52, in der Tiefe zum Tor hin weniger gestreckt).
# Positionen nach der PDF-Skizze, im Uhrzeigersinn gedreht (PDF links = oben). Für den 3D-Abstand stehen die Mittelfeldspieler
# von Team Rot etwas tiefer als die von Team Neon (torseitig, wie beim Verteidigen). Ein Trainer statt zwei, an der Mittellinie.
# Mittelzone aus vier Quadraten gestrichelt (wie im PDF etwa 33 x 22 m, kurz vor dem Strafraum). Großfeldtor (nur C- und B-Jugend).
# Pink (Aufbau im 4-3-3) -> Team Neon, Nummern wie im PDF (2-11). Blau (mit Torwart) -> Team Rot, neu nummeriert, weil alle
# Nummern doppelt sind: jeweils plus zehn (4 -> 14, 5 -> 15, 6 -> 16, 7 -> 17, 8 -> 18, 9 -> 19, 10 -> 20, 11 -> 21), Torwart r1 „TW“.
# Grundform nach der PDF-Skizze: 6 auf 5, 5 in die Zone auf 4, 4 dreht auf und spielt auf den einrückenden Stürmer 9 (zusätzlicher
# Spieler, vier gegen drei), 9 legt auf 8 ab (zentraler Pass), 8 raus auf 7, Flanke, 9 schließt ab. Im PDF spielt 9 direkt auf 7;
# der Umweg über 8 zeigt den zentralen Pass. Abschluss ergänzt („crossing and finishing“).
# Fassung 1 = PDF Progression 1 (Innenverteidiger dribbelt an, 9 kommt, 10 rotiert hinter die Mittelfeldlinie),
# Fassung 2 = Progression 2 (Flügelspieler 11 rückt ein, 10 geht nach außen, 4 zieht weg, Pass von 5 auf 11).
# Sichtkegel: In Text, Ton und Video kein Scannen. Beim Annehmen und Aufdrehen nach ZUSATZ_U15 (Vorbild ue300) schaut der Spieler
# zum Passgeber und nach der Annahme schwenkt der Kegel zum Passziel (bl mit von), dazu der Drehpfeil (drehen).
F = hf.Halbfeld()                      # 50 x 65 m, Tor rechts (x 90), Mittellinie links (x 10), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
def schau(who, p, ziel, weit=20, von=None, **k):
    return h.bl(who, hf.richt(X(p), X(ziel), weit), von=hf.richt(X(p), X(von)) if von else None, **k)
T = h.P("T", "c", 12, 55.3, "T")  # unten an der Mittellinie
ERSATZ = [h.B("s1", 15.5, 55.8), h.B("s2", 18, 55.8)]
POS = {"r1": (2.5, 31.5), "r14": (8, 22), "r15": (8, 43), "n9": (13, 33),
       "n11": (21, 9), "n7": (19, 61), "r17": (30, 8), "r21": (29, 59),
       "n10": (25, 19), "r18": (21, 24.5), "r16": (20.5, 40), "n8": (25, 46),
       "n4": (35.5, 31.5), "r20": (32, 37), "n3": (41, 8), "n2": (39, 61),
       "r19": (43, 28), "n6": (48, 20.5), "n5": (47.5, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "r1" else i[1:]) for i, p in d.items()] + [T]
# Mittelzone aus vier Quadraten: Tiefe 18-40 m (mit Abstand zur Strafraumlinie), Breite 15-48 m, geteilt bei 29 m und 31,5 m
Z0, Z1 = X((40, 15)), X((18, 48))
ZM = X((29, 31.5))
LINES = F.linien() + [rect(Z0[0], Z0[1], round(Z1[0] - Z0[0], 1), round(Z1[1] - Z0[1], 1), dashed=True),
                      line(ZM[0], Z0[1], ZM[0], Z1[1]), line(Z0[0], ZM[1], Z1[0], ZM[1])]
TORE = [F.tor()] + F.minitore(10, 55)
DROP9 = (27, 27)        # dort nimmt Spieler neun in der Mittelzone an
BOX9 = (9, 35)          # Spieler neun im Strafraum
SCHUSS = [90.4, 33]

u = {"title": "Rotieren im Mittelfeld", "code": "UE-352", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 16, "players_max": 20,
 "field_size": "Halbes Spielfeld",
 "description": "Zehn gegen neun auf einer Hälfte. Team Neon baut im 4-3-3 von hinten auf und muss den Ball durch eine Mittelzone aus vier Quadraten spielen. Dort stehen von jedem Team drei Spieler, ein vierter Angreifer darf dazukommen. Mit Rotationen und Freilaufen schaffen sich die Mittelfeldspieler Platz für den Weg zum Tor.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite. Auf der Torlinie steht das große Tor, auf der Mittellinie zwei Minitore. In der Mitte ist eine Zone aus vier Quadraten abgesteckt.",
  "Verteilen: Team Neon mit zehn Feldspielern im 4-3-3, Team Rot mit Torwart und acht Feldspielern. In der Mittelzone stehen von jedem Team drei Spieler. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Team Neon baut über die Innenverteidiger auf. Der Ball muss in die Mittelzone und dort einmal zentral gespielt werden, bevor er sie verlässt. Ein zusätzlicher Angreifer darf in die Zone, dann heißt es vier gegen drei. Erobert Team Rot den Ball, spielt es durch die Mitte auf ein Minitor.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Neon, ein Treffer in ein Minitor gibt einen Punkt für Team Rot. Nach jedem Angriff bringt der Trainer einen neuen Ball zu den Innenverteidigern von Team Neon."],
 "organisation_show": ORG,
 "coaching_points": ["Rein in die Zone, raus aus der Zone: rotieren", "Freilaufen, damit es in der Mitte frei wird", "Beim Tauschen laut ansagen", "Über außen durch und scharf flanken"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Mittelzone", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rotieren im Mittelfeld. Zehn gegen neun auf einer Hälfte. Team Neon baut im Vier-Drei-Drei auf und muss durch die Mittelzone, wo die Mittelfeldspieler ständig die Plätze tauschen.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", *fu(POS["n6"]))] + ERSATZ,
  "steps": [
   S("Aufbau über die Innenverteidiger", "Spieler sechs hat den Ball. Er spielt quer zu Spieler fünf, und Team Rot schiebt mit.",
     zu("b1", POS["n5"]), lauf("r19", (43, 36), delay=0.4)),
   S("Rein in die Mittelzone", "Spieler vier kommt in der Zone entgegen und schaut zum Ball. Spieler fünf spielt ihn flach an.",
     lauf("n4", (37, 33)), schau("n4", (37, 33), POS["n5"], after=True), zu("b1", (37, 33), after=True)),
   S("Aufdrehen, Spieler neun kommt", "Vorn lässt sich Spieler neun in die Zone fallen. Jetzt sind es vier gegen drei. Spieler vier dreht auf und spielt ihn an.",
     lauf("n9", DROP9), schau("n4", (37, 33), DROP9, von=POS["n5"], dauer=1.3, delay=0.3),
     h.drehen("n4", X(DROP9), delay=0.7), zu("b1", DROP9, after=True)),
   S("Zentral ablegen, raus auf den Flügel", "Spieler neun legt direkt ab auf Spieler acht. Das ist der Pass durch die Mitte. Spieler acht spielt sofort raus auf Spieler sieben, und Spieler neun startet in den Strafraum.",
     zu("b1", POS["n8"]), zu("b1", POS["n7"], after=True), lauf("n9", BOX9, delay=0.6)),
   S("Flanke und Abschluss: Punkt", "Spieler sieben flankt scharf vors Tor. Spieler neun ist da und trifft, und das gibt einen Punkt für Team Neon. Danach bringt der Trainer den nächsten Ball zu den Innenverteidigern.",
     zu("b1", BOX9), h.ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Innenverteidiger dribbelt an, und vorn wird rotiert.", "Andribbeln und rotieren",
    "Der Innenverteidiger dribbelt mit Ball in die Mittelzone und zieht einen Gegenspieler auf sich. Im selben Moment kommt der Stürmer entgegen, und der Zehner rotiert hinter die Mittelfeldlinie von Team Rot. Genau dort bekommt er den Ball und kann direkt auf die Abwehrkette gehen.",
    sp(), [h.B("b1", *fu(POS["n5"]))] + ERSATZ,
    [S("Spieler fünf dribbelt an", "Spieler fünf dribbelt in die Zone, Spieler zwanzig muss raus zu ihm. Spieler vier macht ihm Platz und zieht weg.",
       h.dr("n5", "b1", X((38, 40))), lauf("r20", (34.5, 44), delay=0.4), lauf("n4", (41, 27), delay=0.2),
       lauf("r18", (21, 26.5), delay=0.4)),
     S("Neun kommt, Zehn geht", "Jetzt die Rotation. Spieler neun lässt sich fallen, und Spieler zehn läuft hinter die Mittelfeldlinie. Er schaut zum Ball.",
       lauf("n9", (24, 36)), lauf("n10", (15, 13), delay=0.2), schau("n10", (15, 13), (38, 40), after=True)),
     S("Pass hinter die Linie", "Spieler fünf spielt flach durch auf Spieler zehn. Die ganze Mittelfeldlinie von Team Rot ist überspielt.",
       zu("b1", (15, 13))),
     S("Aufdrehen, durchstecken: Punkt", "Spieler zehn dreht auf und steckt durch auf Spieler elf, der hinter die Abwehr startet. Spieler elf trifft, und das gibt einen Punkt für Team Neon.",
       schau("n10", (15, 13), (8, 7), 12, von=(38, 40), dauer=1.3), h.drehen("n10", X((8, 7)), delay=0.4),
       lauf("n11", (8, 7), delay=0.4), zu("b1", (8, 7), after=True), h.ps("b1", [90.4, 20], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Flügelspieler rückt ein, der Zehner geht nach außen.", "Flügel rein, Zehner raus",
    "Der Flügelspieler kommt nach innen und tauscht mit dem Zehner, der nach außen geht. Der Sechser zieht auf die Ballseite weg und nimmt seinen Gegenspieler mit. So wird der Weg in die Mitte frei, und außen steht der Zehner ohne Gegenspieler.",
    sp(), [h.B("b1", *fu(POS["n5"]))] + ERSATZ,
    [S("Tauschen auf der Seite", "Spieler elf rückt nach innen, Spieler zehn geht dafür nach außen. Spieler vier zieht zur Ballseite weg, und Spieler zwanzig geht mit.",
       lauf("n11", (25, 23)), lauf("n10", (16, 6), delay=0.1), lauf("n4", (37, 41), delay=0.2), lauf("r20", (33.5, 40), delay=0.4)),
     S("Diagonal auf Spieler elf", "Der Weg ist frei. Spieler elf schaut zum Ball, und Spieler fünf spielt diagonal in die Mitte.",
       schau("n11", (25, 23), POS["n5"]), zu("b1", (25, 23), after=True)),
     S("Aufdrehen, raus auf Spieler zehn", "Spieler elf dreht auf und spielt raus auf Spieler zehn. Der ist außen frei und kann flanken.",
       schau("n11", (25, 23), (16, 6), 14, von=POS["n5"], dauer=1.3), h.drehen("n11", X((16, 6)), delay=0.4),
       zu("b1", (16, 6), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
