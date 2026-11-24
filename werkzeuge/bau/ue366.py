import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 13-P11 (U15-U17, Woche 24 Phase 6): Defending the Overload (Overload Game). Eine Spielfeldhälfte in voller Breite
# (Feld x 9-89, y 4-51), großes Tor mit Torwart, zwei Minitore an der Mittellinie für den Konter der Verteidiger.
# Kein Großfeld quer: halbes Feld (AUFTRAG „Halbes Feld und kleiner bleibt wie bisher“, wie UE-314/UE-340). Keine Maßlinien,
# das PDF nennt keine Maße (field_size „Halbes Spielfeld“).
# Um 180 Grad gedreht: im PDF liegt das große Tor unten, hier oben, Team Rot greift nach oben an.
# Pink/rot (Verteidiger, wird trainiert) -> Team Neon mit den Nummern aus PDF und Video (2, 3, 4, 5, 6, 8), Torwart n1 „TW“.
# Blau/gelb (Angreifer) -> Team Rot, Nummern aus dem Video (7, 9, 10, 11), doppelte neu: 2 -> 12, 3 -> 13, 4 -> 14, 8 -> 15.
# Strafraum und Torraum durchgezogen, Teilkreise und Mittelkreis weggelassen. Ein Trainer statt zwei (rechts neben dem Feld).
# Wartende Verteidiger auf der Torlinie neben dem Tor, wartende Angreifer hinter der Mittellinie (3D-Abstand).
# Ablauf nach PDF und Video: zwei gegen eins, Pfiff -> vier gegen zwei (Grundform), Pfiff -> sechs gegen vier (Steigerung 1),
# Pfiff -> acht gegen sechs (Steigerung 2, mit Überlaufen außen wie im Video). Reihenfolge, wer bei welchem Pfiff dazukommt,
# angenommen. Wertung: Laut PDF spielen die Verteidiger nach Ballgewinn ins Minitor (im Text erst beim acht gegen sechs, im
# Coaching-Punkt „Quick combos to play out into mini-goals after turnover“ allgemein): hier in jeder Stufe, Minitor = Punkt
# für Team Neon, Treffer ins große Tor = Punkt für Team Rot (ergänzt).
# Sichtkegel aus Text und Ton („Awareness to recognise the overload situation“): Beim Pfiff schaut Spieler fünf, wer von der
# Mittellinie dazukommt (Richtung aus dem Sinn, im Video kein Kegel eingezeichnet).
T = P("T", "c", 94.5, 28, "T")  # rechts neben dem Feld
ERSATZ = [B("s1", 95.1, 31.6), B("s2", 97.6, 31.6)]
LINES = [rect(9, 4, 80, 47), rect(24.2, 4, 49.6, 15.5), rect(37.8, 4, 22.5, 5.2)]
TORE = [{"x": 49, "y": 4, "side": "top", "size": "gross"}, {"x": 17, "y": 51, "side": "bottom"}, {"x": 81, "y": 51, "side": "bottom"}]
# Startplätze: wartende Verteidiger auf der Torlinie, wartende Angreifer hinter der Mittellinie
WARTE = {"n8": (16, 4), "n3": (25, 4), "n4": (34, 4), "n6": (64, 4), "n2": (73, 4),
         "r14": (25, 55.5), "r12": (33.5, 55.5), "r7": (42, 55.5), "r11": (56, 55.5), "r15": (64.5, 55.5), "r13": (73, 55.5)}
START = {"n1": (49, 8.5), "n5": (49, 24.5), "r10": (40, 37), "r9": (58, 37)}
def sp(**k):
    d = dict(WARTE); d.update(START); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
MT_L, MT_R = [17, 50.5], [81, 50.5]

u = {"title": "Überzahl wächst mit jedem Pfiff", "code": "UE-366", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 15,
 "field_size": "Halbes Spielfeld",
 "description": "Auf einer Spielfeldhälfte greift Team Rot immer in Überzahl auf das große Tor an. Es beginnt mit zwei gegen eins, und mit jedem Pfiff kommen Angreifer und Verteidiger dazu, bis acht gegen sechs gespielt wird. Team Neon verteidigt das Tor, verschiebt als Einheit und lenkt die Angreifer nach außen. Erobert Team Neon den Ball, spielt es schnell in eines der beiden Minitore an der Mittellinie.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite mit dem großen Tor. An der Mittellinie stehen links und rechts zwei Minitore.",
  "Verteilen: Team Neon mit Torwart und sechs Verteidigern, einer steht schon vor dem Strafraum, die anderen warten auf der Torlinie. Team Rot mit acht Angreifern an der Mittellinie, zwei davon mit Ball. Der Trainer steht mit einer Pfeife und Bällen an der Seitenlinie.",
  "Ablauf: Zwei Angreifer starten gegen einen Verteidiger. Auf Pfiff kommen zwei Angreifer und ein Verteidiger dazu, also vier gegen zwei. Beim nächsten Pfiff kommen je zwei dazu, sechs gegen vier, und beim letzten Pfiff acht gegen sechs.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Rot. Erobert Team Neon den Ball und trifft ein Minitor, gibt das einen Punkt für Team Neon. Danach gehen alle zurück, und die nächsten zwei Angreifer starten."],
 "organisation_show": ORG,
 "coaching_points": ["Im zwei gegen eins verzögern, nicht reingrätschen", "Einer drückt, der Nächste sichert schräg dahinter", "Als Kette zum Ball schieben, die Mitte bleibt eng", "Ball erobert? Schnell raus aufs Minitor"],
 "materials": ["1 großes Tor", "2 Minitore", "Leibchen in zwei Farben", "Viele Bälle", "1 Pfeife"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Überzahl wächst mit jedem Pfiff. Team Rot greift immer mit mehr Spielern an, als Team Neon hinten hat. Mit jedem Pfiff kommen welche dazu, bis acht gegen sechs gespielt wird.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 40.6, 37.6)] + ERSATZ,
  "steps": [
   S("Zwei gegen eins, Spieler fünf wartet", "Spieler zehn und Spieler neun laufen mit Ball auf Spieler fünf zu. Der geht nicht rein. Er bleibt zwischen den beiden, macht kleine Schritte zurück und wartet, bis er den Ballführer zur Seite drücken kann.",
     dr("r10", "b1", [43, 30]), mv("r9", [60, 28], delay=0.2), mv("n5", [47.5, 18], delay=0.4)),
   S("Pfiff: vier gegen zwei", "Pfiff vom Trainer. Von der Mittellinie kommen Spieler sieben und Spieler elf dazu, von der Torlinie sprintet Spieler vier ins Feld. Spieler fünf schaut sofort, wer da kommt.",
     mv("r7", [28, 34]), mv("r11", [72, 33]), mv("n4", [37, 19], delay=0.2), bl("n5", [30, 30], delay=0.5)),
   S("Einer drückt, einer sichert", "Spieler zehn spielt raus zu Spieler sieben. Spieler vier läuft ihn an und stellt den Weg nach innen zu. Spieler fünf rückt schräg dahinter und sichert ab.",
     ps("b1", [28.6, 34.6]), mv("n4", [31, 28], delay=0.3), mv("n5", [40, 22], delay=0.4)),
   S("Abgefangen, ins Minitor: Punkt", "Spieler sieben will zurück in die Mitte spielen. Darauf hat Spieler fünf gewartet. Er geht dazwischen und spielt den Ball sofort ins Minitor, und das gibt einen Punkt für Team Neon. Dann starten die nächsten zwei Angreifer.",
     ps("b1", [36.6, 32.6]), mv("n5", [36, 32], delay=0.1), ps("b1", MT_L, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Sechs gegen vier.", "Sechs gegen vier",
    "Beim zweiten Pfiff kommen zwei Angreifer und zwei Verteidiger dazu. Hinten steht jetzt eine Viererkette. Die schiebt immer gemeinsam zum Ball, einer läuft an, die anderen rücken eng zusammen. Verlagert Team Rot, schiebt die ganze Kette mit rüber.",
    sp(n4=(37, 20), n5=(58, 20), r7=(22, 36), r10=(40, 36), r9=(56, 41), r11=(76, 36)), [B("b1", 40.6, 36.6)] + ERSATZ,
    [S("Pfiff: sechs gegen vier", "Wieder ein Pfiff. Spieler zwölf und Spieler fünfzehn kommen von der Mittellinie. Hinten sprinten Spieler drei und Spieler sechs rein, jetzt steht eine Viererkette.",
       mv("r12", [31, 45]), mv("r15", [67, 45]), mv("n3", [24, 18], delay=0.2), mv("n6", [70, 18], delay=0.2),
       mv("n4", [42, 19], delay=0.4), mv("n5", [55, 19], delay=0.4)),
     S("Ball nach außen, Kette schiebt", "Spieler zehn spielt raus zu Spieler sieben. Die ganze Kette schiebt mit. Spieler drei läuft an, die anderen rücken zusammen und machen die Mitte eng.",
       ps("b1", [22.6, 36.6]), mv("n3", [21, 28], delay=0.3), mv("n4", [32, 21], delay=0.3), mv("n5", [43, 20], delay=0.3), mv("n6", [55, 19], delay=0.3)),
     S("Verlagerung, Kette schiebt rüber", "Team Rot spielt über Spieler zehn auf die andere Seite zu Spieler elf. Jetzt schiebt die Kette genauso schnell rüber. Spieler sechs läuft an, und die Abstände bleiben klein.",
       ps("b1", [40.6, 36.6]), ps("b1", [76.6, 36.6], after=True),
       mv("n6", [73, 28], delay=0.8), mv("n5", [62, 20], delay=0.8), mv("n4", [51, 20], delay=0.8), mv("n3", [40, 21], delay=0.8))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Acht gegen sechs.", "Acht gegen sechs",
    "Beim letzten Pfiff spielen alle mit. Zwei Verteidiger sichern jetzt vor der Kette. Team Rot sucht außen die Überzahl und läuft hinterher. Team Neon bleibt eng, übergibt die Läufer und wartet auf den Pass nach innen. Nach dem Ballgewinn geht es mit wenigen Kontakten ins Minitor.",
    sp(n4=(40, 20), n5=(58, 20), n3=(24, 20), n6=(74, 20), r7=(14, 36), r12=(30, 36), r10=(44, 36), r9=(57, 36), r15=(70, 36), r11=(84, 36)),
    [B("b1", 70.6, 36.6)] + ERSATZ,
    [S("Letzter Pfiff: acht gegen sechs", "Letzter Pfiff, jetzt sind alle drin. Spieler vierzehn und Spieler dreizehn kommen nach vorn. Von der Torlinie sprinten Spieler acht und Spieler zwei rein und sichern vor der Kette.",
       mv("r14", [36, 46]), mv("r13", [63, 46]), mv("n8", [38, 29], delay=0.2), mv("n2", [60, 29], delay=0.2)),
     S("Außen überlaufen", "Spieler fünfzehn spielt raus zu Spieler elf und läuft außen hinterher. Spieler sechs übernimmt den Läufer. Spieler zwei kommt aus der Mitte und läuft Spieler elf an, die Kette schiebt nach.",
       ps("b1", [84.6, 36.6]), mv("r15", [80, 31], delay=0.2), mv("r15", [87, 25], after=True),
       mv("n6", [82, 23], delay=0.3), mv("n2", [78, 32], delay=0.3), mv("n5", [67, 21], delay=0.4), mv("n4", [55, 21], delay=0.4), mv("n3", [42, 21], delay=0.4)),
     S("Ballgewinn, ins Minitor: Punkt", "Spieler elf will nach innen zu Spieler neun spielen. Spieler zwei ist schneller, fängt den Pass ab und spielt sofort ins Minitor. Das gibt einen Punkt für Team Neon.",
       mv("n2", [72, 36]), ps("b1", [72.6, 36.6], delay=0.2), ps("b1", MT_R, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
