import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 25-P11 (U15-U17, Woche 8 Phase 4): High Press in the Attacking Third. Volle Platzbreite x 45 Yards (41 m, gerundet 40 m),
# großes Tor mit Torwart an einem Ende, zwei Minitore am anderen Ende, davor eine Endzone für den Zehner von Gold.
# Kein Großfeld quer: halbes Feld (40 m lang, AUFTRAG „Halbes Feld und kleiner bleibt wie bisher“, wie UE-314). Das Feld ist
# breiter als lang und liegt deshalb quer über die ganze Tafel (x 9-89, y 4-51), Figuren normal groß.
# Um 180 Grad gedreht, damit Team Neon nach oben spielt: großes Tor oben, Minitore und Endzone unten.
# Pink (presst, wird trainiert) -> Team Neon mit den Nummern aus dem PDF (2, 3, 4, 7, 8, 9, 10, 11).
# Gold (Ballbesitz, mit Torwart) -> Team Rot, neu nummeriert wegen doppelter Nummern: 2 -> 12, 3 -> 13, 4 -> 14, 8 -> 15,
# 10 -> 16; 5 und 6 bleiben, Torwart r1 „TW“. Großes Tor „gross“ (nur C- und B-Jugend).
# Positionen grob wie im PDF, für den 3D-Abstand in Spalten geordnet. Gestrichelt: Mittellinie des Spielfelds im PDF (Höhe 22
# Yards) und Endzone vor den Minitoren; Strafraum und Torraum durchgezogen, Teilkreis weggelassen. Ein Trainer statt zwei
# (unten an der Seitenlinie).
# Grundform nach PDF und Video: Torwart kurz auf Gold 6, erster Pass nach vorn auf Gold 8 = Signal, drei Pinke kreisen ein.
# Ballgewinn und Abschluss ergänzt (Text: „attack quickly to finish“). Fassungen: PDF Key Coaching Point 1 (mehrere Linien Druck
# um den Ball) und 2 (schnell unterstützen, Überzahl, Läufe in die Tiefe).
# Sichtkegel aus dem Ton („identify key triggers, like a poor pass or a heavy touch“): Spieler elf beobachtet die Annahme von
# Spieler fünfzehn, bevor er anläuft. Im Video kein Kegel eingezeichnet. Zweiter Kegel in Fassung 2 aus dem Text („forward runs“):
# Spieler zwei schaut nach dem Ballgewinn zum startenden Spieler sieben.
# Keine Dublette von UE-314 (10-P11: kein Zehner in einer Endzone, Pressing nach kurzem Abstoß) oder UE-148/UE-236.
T = P("T", "c", 68, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 71.5, 55.8), B("s2", 74, 55.8)]
POS = {"r1": (48, 6.5), "r6": (39, 12), "r5": (57, 14), "r12": (12, 18), "r13": (84, 20), "r14": (48, 23), "r15": (30, 24), "r16": (57, 48),
       "n11": (21, 28), "n9": (39, 28), "n7": (66, 26), "n10": (48, 39), "n8": (30, 42), "n2": (84, 37), "n4": (39, 45), "n3": (12, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 47), rect(24.2, 4, 49.6, 19.3), rect(37.8, 4, 22.5, 6.4), line(9, 27.9, 89, 27.9), line(9, 43.8, 89, 43.8)]
TORE = [{"x": 49, "y": 4, "side": "top", "size": "gross"}, {"x": 17.6, "y": 51, "side": "bottom"}, {"x": 80.4, "y": 51, "side": "bottom"}]
DIMS = dims(9, 89, 4, 51, "Volle Breite", "40 m", rx=95)

u = {"title": "Hoch pressen nach dem Signal", "code": "UE-340", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 18,
 "field_size": "Volle Breite x 40 m",
 "description": "Acht gegen acht auf einer Hälfte in voller Breite. Team Rot baut mit dem Torwart auf und will den Ball zu seinem Zehner in der Endzone bringen, der auf zwei Minitore abschließt. Team Neon wartet, bis Team Rot den ersten Pass nach vorn spielt. Dann pressen alle gemeinsam, erobern den Ball und gehen schnell aufs große Tor.",
 "organisation": ["Aufbauen: Eine Hälfte in voller Breite, etwa 40 Meter lang. Oben steht das große Tor mit Torwart, unten zwei Minitore. Davor ist eine Endzone für den Zehner von Team Rot abgesteckt.",
  "Verteilen: Team Rot mit Torwart und sieben Feldspielern, einer davon wartet als Zehner in der Endzone. Team Neon presst mit acht Spielern. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet. Sobald Team Rot den ersten Pass nach vorn spielt, presst Team Neon gemeinsam. Nach dem Ballgewinn schnell abschließen oder den Ball sichern und ruhig aufbauen. Kommt Team Rot durch, spielt es auf den Zehner, und der schließt auf ein Minitor ab.",
  "Wertung: Jeder Treffer von Team Neon ins große Tor gibt einen Punkt. Trifft der Zehner ein Minitor, gibt das einen Punkt für Team Rot. Der Trainer startet neu, mal beim Torwart, mal mit einem Ball von der Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Erster Pass nach vorn, jetzt pressen alle", "Zu dritt um den Ball, keiner jagt allein", "Der Sechser stellt den Weg zum Zehner zu", "Kommt Rot durch, sofort zurück und neu ordnen"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Endzone", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Hoch pressen nach dem Signal. Acht gegen acht auf einer Hälfte. Team Rot baut vom Torwart aus auf, und mit dem ersten Pass nach vorn geht bei Team Neon die Jagd los.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 48.6, 7.1)] + ERSATZ,
  "steps": [
   S("Torwart eröffnet kurz", "Der Torwart spielt kurz auf Spieler sechs. Noch presst keiner. Team Neon steht und wartet auf den ersten Pass nach vorn.",
     ps("b1", fu(POS["r6"]))),
   S("Erster Pass nach vorn: das Signal", "Jetzt spielt Spieler sechs nach vorn auf Spieler fünfzehn. Das ist das Signal. Spieler elf schaut genau hin, wie der Ball ankommt, und läuft an. Von vorn kommt Spieler neun, von hinten Spieler acht.",
     ps("b1", fu(POS["r15"])), bl("n11", [30, 24], delay=0.4), mv("n11", [24.5, 23.5], after=True), mv("n9", [35, 20], delay=0.8),
     mv("n8", [31, 32.5], delay=0.8), mv("n4", [43, 36], delay=1.0), mv("n10", [51, 31], delay=1.0)),
   S("Eingekreist, Ball erobert", "Spieler fünfzehn ist eingekreist. Der Weg zum Zehner ist zu, Spieler vier steht im Passweg. Er versucht es trotzdem durch die Mitte, und Spieler acht hat den Ball.",
     ps("b1", [33.5, 31.5]), mv("n8", [33, 31], delay=0.2), mv("r14", [52, 27], delay=0.3)),
   S("Schnell abschließen: Punkt", "Kein langes Spiel jetzt. Spieler acht legt sofort auf Spieler neun, und der schießt aus der Drehung ins lange Eck. Das gibt einen Punkt für Team Neon. Danach startet der Trainer den nächsten Angriff, mal beim Torwart, mal von der Seite.",
     ps("b1", [35.6, 20.6]), ps("b1", [53, 4.3], after=True), mv("r1", [46, 6.5], delay=0.3))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mehrere Leute um den Ball.", "Mehrere Leute um den Ball",
    "Einer allein holt den Ball nicht. Der Erste läuft an, der Zweite kommt von der Seite, der Dritte steht dahinter. So hat der Ballführer keinen freien Pass mehr und muss etwas riskieren.",
    sp(), [B("b1", 39.6, 12.6)] + ERSATZ,
    [S("Pass in die Mitte", "Spieler sechs spielt in die Mitte auf Spieler vierzehn. Sofort schiebt Team Neon zusammen. Spieler zehn kommt von vorn, Spieler neun von hinten.",
       ps("b1", fu(POS["r14"])), mv("n10", [49, 30.5], delay=0.4), mv("n9", [43, 21], delay=0.4), mv("n7", [57, 24], delay=0.6), mv("n8", [36, 34], delay=0.6)),
     S("Kein Weg frei, abgefangen", "Spieler vierzehn hat keinen freien Pass mehr. Er will raus auf Spieler fünf, aber Spieler sieben ist dazwischen und hat den Ball.",
       ps("b1", [55.5, 18.5]), mv("n7", [55, 18], delay=0.2)),
     S("Direkt zum Tor: Punkt", "Spieler sieben ist schon im Strafraum. Zwei Schritte, Schuss, und das gibt einen Punkt für Team Neon.",
       dr("n7", "b1", [52, 12.5]), mv("r1", [45, 6.5], delay=0.4), ps("b1", [51.5, 4.3], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell nachrücken und die Überzahl nutzen.", "Schnell nachrücken",
    "Ist der Ball erobert, rücken die Nächsten sofort nach. So entsteht in Ballnähe eine Überzahl. Einer startet in die Tiefe, und der Ball geht schnell nach vorn, bevor Team Rot sich ordnen kann.",
    sp(), [B("b1", 84.6, 20.6)] + ERSATZ,
    [S("Außen erobert", "Spieler dreizehn hat den Ball außen. Spieler zwei läuft ihn von hinten an, nimmt ihm den Ball ab und hat ihn am Fuß.",
       mv("n2", [83, 26]), dr("n2", "b1", [78, 29], after=True)),
     S("Nachrücken, Spieler sieben startet", "Sofort rücken Spieler zehn und Spieler sieben nach. Spieler zwei schaut hoch, Spieler sieben startet in die Tiefe hinter Spieler fünf.",
       mv("n10", [70, 33]), mv("n7", [64, 14], delay=0.3), bl("n2", [64, 14], delay=0.3), mv("n9", [44, 17], delay=0.4)),
     S("Steil in den Lauf: Punkt", "Spieler zwei spielt steil in den Lauf. Spieler sieben ist frei vor dem Torwart und trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", fu([64, 14])), ps("b1", [51, 4.3], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
