import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 13-P11 (U15-U17, Woche 24 Phase 6): Defending the Overload (Overload Game). Eine Spielfeldhälfte in voller Breite,
# großes Tor mit Torwart, zwei Minitore an der Mittellinie für den Konter der Verteidiger. Keine Maßlinien, das PDF nennt
# keine Maße (field_size „Halbes Spielfeld“).
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): umgebaut vom Hochformat (Tor oben) auf
# die Hälfte wie im Fernsehbild, mit bau/halbfeld.py. Hier greift Team Rot auf das große Tor an und Team Neon verteidigt
# und kontert auf die Minitore. Damit Team Neon wie überall nach rechts spielt, liegt das große Tor LINKS
# (F = Halbfeld(tor="links")), die Mittellinie mit den Minitoren rechts, Team Rot greift nach links an. Echte Linien
# (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Gegenüber dem PDF (großes Tor unten) im
# Uhrzeigersinn gedreht, nicht gespiegelt (PDF links = oben).
# Positionen neu in Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie). Wartende stehen neben
# dem Feld in Tafelkoordinaten: Verteidiger an der Torlinie und dahinter (in zwei Reihen, 3D-Abstand), Angreifer hinter der
# Mittellinie in zwei Reihen (nicht vor den Minitoren).
# Pink/rot (Verteidiger, wird trainiert) -> Team Neon mit den Nummern aus PDF und Video (2, 3, 4, 5, 6, 8), Torwart n1 „TW“.
# Blau/gelb (Angreifer) -> Team Rot, Nummern aus dem Video (7, 9, 10, 11), doppelte neu: 2 -> 12, 3 -> 13, 4 -> 14, 8 -> 15.
# Ein Trainer statt zwei (unten an der Seitenlinie, mit Pfeife).
# Ablauf nach PDF und Video: zwei gegen eins, Pfiff -> vier gegen zwei (Grundform), Pfiff -> sechs gegen vier (Steigerung 1),
# Pfiff -> acht gegen sechs (Steigerung 2, mit Überlaufen außen wie im Video). Reihenfolge, wer bei welchem Pfiff dazukommt,
# angenommen. Wertung: Laut PDF spielen die Verteidiger nach Ballgewinn ins Minitor (im Text erst beim acht gegen sechs, im
# Coaching-Punkt „Quick combos to play out into mini-goals after turnover“ allgemein): hier in jeder Stufe, Minitor = Punkt
# für Team Neon, Treffer ins große Tor = Punkt für Team Rot (ergänzt).
# Sichtkegel aus Text und Ton („Awareness to recognise the overload situation“): Beim Pfiff schaut Spieler fünf, wer von der
# Mittellinie dazukommt (Richtung aus dem Sinn, im Video kein Kegel eingezeichnet).
F = hf.Halbfeld(tor="links")           # 50 x 65 m, Tor links (x 10), Mittellinie rechts (x 90), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
T = h.P("T", "c", 44, 55.3, "T")       # unten an der Seitenlinie
ERSATZ = [h.B("s1", 47.5, 55.8), h.B("s2", 50, 55.8)]
# Wartende in Tafelkoordinaten: Verteidiger an der Torlinie (x 10) und dahinter (x 3,5), wer zuerst reinkommt, steht vorn, Angreifer hinter der Mittellinie
WARTE = {"n6": (10, 4), "n2": (3.5, 10), "n4": (10, 41), "n3": (3.5, 46.5), "n8": (10, 52.5),
         "r13": (98, 4), "r15": (98, 15.2), "r11": (92, 16.5), "r7": (92, 38.9), "r12": (98, 37.6), "r14": (98, 48.8)}
START = {"n1": (2.5, 32.5), "n5": (18, 32.5), "r10": (34, 40), "r9": (34, 24)}   # in Metern
def sp(**k):
    d = {i: tuple(p) for i, p in WARTE.items()}
    d.update({i: tuple(X(p)) for i, p in START.items()})
    d.update({i: tuple(X(p)) for i, p in k.items()})
    return [h.P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = F.linien()
MT = (6.5, 58.5)                       # Minitore an der Mittellinie (q in Metern)
TORE = [F.tor()] + F.minitore(*MT)
MT_OBEN, MT_UNTEN = X((50.6, MT[0])), X((50.6, MT[1]))   # Ball im Minitor
V1 = dict(n4=(17, 41), n5=(17, 24), r7=(34, 55), r10=(34, 40), r9=(39, 26), r11=(34, 11))
V2 = dict(n3=(17, 53), n4=(17, 38), n5=(17, 23), n6=(17, 8),
          r7=(32, 62), r10=(32, 42), r11=(32, 8), r12=(37, 52), r9=(37, 32), r15=(37, 16))
FANG1 = (26, 41)     # dort fängt Spieler fünf den Pass ab
FANG2 = (33.9, 17)   # dort fängt Spieler zwei den Pass ab

u = {"title": "Überzahl wächst mit jedem Pfiff", "code": "UE-366", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 15,
 "field_size": "Halbes Spielfeld",
 "description": "Auf einer Spielfeldhälfte greift Team Rot immer in Überzahl auf das große Tor an. Es beginnt mit zwei gegen eins, und mit jedem Pfiff kommen Angreifer und Verteidiger dazu, bis acht gegen sechs gespielt wird. Team Neon verteidigt das Tor, verschiebt als Einheit und lenkt die Angreifer nach außen. Erobert Team Neon den Ball, spielt es schnell in eines der beiden Minitore an der Mittellinie.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite mit dem großen Tor. An der Mittellinie stehen zwei Minitore, jeweils nahe an der Seitenlinie.",
  "Verteilen: Team Neon mit Torwart und sechs Verteidigern, einer steht schon vor dem Strafraum, die anderen warten an der Torlinie. Team Rot mit acht Angreifern an der Mittellinie, zwei davon mit Ball. Der Trainer steht mit einer Pfeife und Bällen an der Seitenlinie.",
  "Ablauf: Zwei Angreifer starten gegen einen Verteidiger. Auf Pfiff kommen zwei Angreifer und ein Verteidiger dazu, also vier gegen zwei. Beim nächsten Pfiff kommen je zwei dazu, sechs gegen vier, und beim letzten Pfiff acht gegen sechs.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Rot. Erobert Team Neon den Ball und trifft ein Minitor, gibt das einen Punkt für Team Neon. Danach gehen alle zurück, und die nächsten zwei Angreifer starten."],
 "organisation_show": ORG,
 "coaching_points": ["Im zwei gegen eins verzögern, nicht reingrätschen", "Einer drückt, der Nächste sichert schräg dahinter", "Als Kette zum Ball schieben, die Mitte bleibt eng", "Ball erobert? Schnell raus aufs Minitor"],
 "materials": ["1 großes Tor", "2 Minitore", "Leibchen in zwei Farben", "Viele Bälle", "1 Pfeife"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Überzahl wächst mit jedem Pfiff. Team Rot greift immer mit mehr Spielern an, als Team Neon hinten hat. Mit jedem Pfiff kommen welche dazu, bis acht gegen sechs gespielt wird.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", *fu(START["r10"]))] + ERSATZ,
  "steps": [
   S("Zwei gegen eins, Spieler fünf wartet", "Spieler zehn und Spieler neun laufen mit Ball auf Spieler fünf zu. Der geht nicht rein. Er bleibt zwischen den beiden, macht kleine Schritte zurück und wartet, bis er den Ballführer zur Seite drücken kann.",
     h.dr("r10", "b1", X((27, 38))), lauf("r9", (26, 25), delay=0.2), lauf("n5", (15, 34), delay=0.4)),
   S("Pfiff: vier gegen zwei", "Pfiff vom Trainer. Von der Mittellinie kommen Spieler sieben und Spieler elf dazu, von der Torlinie sprintet Spieler vier ins Feld. Spieler fünf schaut sofort, wer da kommt.",
     lauf("r7", (31, 50)), lauf("r11", (31, 14)), lauf("n4", (16, 43), delay=0.2), h.bl("n5", hf.richt(X((15, 34)), X((31, 50)), 20), delay=0.5)),
   S("Einer drückt, einer sichert", "Spieler zehn spielt raus zu Spieler sieben. Spieler vier läuft ihn an und stellt den Weg nach innen zu. Spieler fünf rückt schräg dahinter und sichert ab.",
     zu("b1", (31, 50)), lauf("n4", (25, 46), delay=0.3), lauf("n5", (19, 40), delay=0.4)),
   S("Abgefangen, ins Minitor: Punkt", "Spieler sieben will zurück in die Mitte spielen. Darauf hat Spieler fünf gewartet. Er geht dazwischen und spielt den Ball sofort ins Minitor, und das gibt einen Punkt für Team Neon. Dann starten die nächsten zwei Angreifer.",
     zu("b1", FANG1), lauf("n5", FANG1, delay=0.1), h.ps("b1", MT_UNTEN, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Sechs gegen vier.", "Sechs gegen vier",
    "Beim zweiten Pfiff kommen zwei Angreifer und zwei Verteidiger dazu. Hinten steht jetzt eine Viererkette. Die schiebt immer gemeinsam zum Ball, einer läuft an, die anderen rücken eng zusammen. Verlagert Team Rot, schiebt die ganze Kette mit rüber.",
    sp(**V1), [h.B("b1", *fu(V1["r10"]))] + ERSATZ,
    [S("Pfiff: sechs gegen vier", "Wieder ein Pfiff. Spieler zwölf und Spieler fünfzehn kommen von der Mittellinie. Hinten sprinten Spieler drei und Spieler sechs rein, jetzt steht eine Viererkette.",
       lauf("r12", (43, 47)), lauf("r15", (43, 18)), lauf("n3", (14, 52), delay=0.2), lauf("n6", (14, 13), delay=0.2),
       lauf("n4", (16, 39), delay=0.4), lauf("n5", (16, 26), delay=0.4)),
     S("Ball nach außen, Kette schiebt", "Spieler zehn spielt raus zu Spieler sieben. Die ganze Kette schiebt mit. Spieler drei läuft an, die anderen rücken zusammen und machen die Mitte eng.",
       zu("b1", V1["r7"]), lauf("n3", (28, 54), delay=0.3), lauf("n4", (18, 45), delay=0.3), lauf("n5", (17, 36), delay=0.3), lauf("n6", (16, 27), delay=0.3)),
     S("Verlagerung, Kette schiebt rüber", "Team Rot spielt über Spieler zehn auf die andere Seite zu Spieler elf. Jetzt schiebt die Kette genauso schnell rüber. Spieler sechs läuft an, und die Abstände bleiben klein.",
       zu("b1", V1["r10"]), zu("b1", V1["r11"], after=True),
       lauf("n6", (25, 13), delay=0.8), lauf("n5", (17, 22), delay=0.8), lauf("n4", (17, 31), delay=0.8), lauf("n3", (18, 40), delay=0.8))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Acht gegen sechs.", "Acht gegen sechs",
    "Beim letzten Pfiff spielen alle mit. Zwei Verteidiger sichern jetzt vor der Kette. Team Rot sucht außen die Überzahl und läuft hinterher. Team Neon bleibt eng, übergibt die Läufer und wartet auf den Pass nach innen. Nach dem Ballgewinn geht es mit wenigen Kontakten ins Minitor.",
    sp(**V2), [h.B("b1", *fu(V2["r15"]))] + ERSATZ,
    [S("Letzter Pfiff: acht gegen sechs", "Letzter Pfiff, jetzt sind alle drin. Spieler vierzehn und Spieler dreizehn kommen nach vorn. Von der Torlinie sprinten Spieler acht und Spieler zwei rein und sichern vor der Kette.",
       lauf("r14", (44, 44)), lauf("r13", (44, 21)), lauf("n8", (24, 40), delay=0.2), lauf("n2", (24, 21), delay=0.2)),
     S("Außen überlaufen", "Spieler fünfzehn spielt raus zu Spieler elf und läuft außen hinterher. Spieler sechs übernimmt den Läufer. Spieler zwei kommt aus der Mitte und läuft Spieler elf an, die Kette schiebt nach.",
       zu("b1", V2["r11"]), lauf("r15", (35, 2), delay=0.2), lauf("r15", (22, 2), after=True),
       lauf("n6", (19, 6), delay=0.3), lauf("n2", (28, 10), delay=0.3), lauf("n5", (18, 16), delay=0.4), lauf("n4", (18, 28), delay=0.4), lauf("n3", (18, 40), delay=0.4)),
     S("Ballgewinn, ins Minitor: Punkt", "Spieler elf will nach innen zu Spieler neun spielen. Spieler zwei ist schneller, fängt den Pass ab und spielt sofort ins Minitor. Das gibt einen Punkt für Team Neon.",
       lauf("n2", FANG2), zu("b1", FANG2, delay=0.2), h.ps("b1", MT_OBEN, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
