import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 25-P11 (U15-U17, Woche 8 Phase 4): High Press in the Attacking Third. Volle Platzbreite x 45 Yards (41 m, gerundet 40 m),
# großes Tor mit Torwart an einem Ende, zwei Minitore am anderen Ende, davor eine Endzone für den Zehner von Gold.
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): umgebaut vom Hochformat (Tor oben) auf
# die Hälfte wie im Fernsehbild, mit bau/halbfeld.py (F = Halbfeld(tief=40, breit=65): kürzeres Feld, gleich gestreckt, mittig).
# Großes Tor RECHTS, Minitore und Endzone links, Platzbreite von oben nach unten, echte Linien (Strafraum, Torraum,
# Strafraumbogen; kein Mittelkreis, das Feld endet 40 m vor dem Tor), "massstab": "gross", nur die Tiefen-Maßlinie unten.
# Team Neon presst und greift nach rechts an. Gegenüber dem PDF (großes Tor unten) gegen den Uhrzeigersinn gedreht, nicht gespiegelt.
# Pink (presst, wird trainiert) -> Team Neon mit den Nummern aus dem PDF (2, 3, 4, 7, 8, 9, 10, 11).
# Gold (Ballbesitz, mit Torwart) -> Team Rot, neu nummeriert wegen doppelter Nummern: 2 -> 12, 3 -> 13, 4 -> 14, 8 -> 15,
# 10 -> 16; 5 und 6 bleiben, Torwart r1 „TW“. Großes Tor „gross“ (nur C- und B-Jugend).
# Positionen neu in Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie), grob wie im PDF, für den
# 3D-Abstand in der Tiefe versetzt. Gestrichelt: Mittellinie des Spielfelds im PDF (bei etwa 22 m, knapp hinter dem
# Strafraumbogen) und Endzone vor den Minitoren (ab 34 m). Ein Trainer statt zwei (unten an der Seitenlinie).
# Grundform nach PDF und Video: Torwart kurz auf Gold 6, erster Pass nach vorn auf Gold 8 = Signal, drei Pinke kreisen ein.
# Ballgewinn und Abschluss ergänzt (Text: „attack quickly to finish“). Fassungen: PDF Key Coaching Point 1 (mehrere Linien Druck
# um den Ball) und 2 (schnell unterstützen, Überzahl, Läufe in die Tiefe).
# Ton „identify key triggers, like a poor pass or a heavy touch“: früher Kegel bei Spieler elf (beobachtet die Annahme), nach der
# Regel des Inhabers (25.11.2026) gestrichen, er spielt danach nicht selbst; im Video kein Kegel eingezeichnet. Kegel in Fassung 2 aus dem Text („forward runs“):
# Spieler zwei schaut nach dem Ballgewinn zum startenden Spieler sieben.
# Keine Dublette von UE-314 (10-P11: kein Zehner in einer Endzone, Pressing nach kurzem Abstoß) oder UE-148/UE-236.
F = hf.Halbfeld(tief=40, breit=65)     # 40 x 65 m, Tor rechts (x 82,5), Feldende links (x 17,5), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
T = h.P("T", "c", 58, 55.3, "T")       # unten an der Seitenlinie
ERSATZ = [h.B("s1", 61.5, 55.8), h.B("s2", 64, 55.8)]
POS = {"r1": (2, 32.5), "r6": (8, 22), "r5": (9, 44), "r12": (13, 3), "r13": (14, 62), "r14": (18, 33), "r15": (19, 14),
       "r16": (37, 40),
       "n11": (23, 6), "n9": (24, 24), "n7": (21, 49), "n10": (28, 34.5), "n8": (30, 19), "n2": (27, 59), "n4": (33.5, 27),
       "n3": (31, 3)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "r1" else i[1:]) for i, p in d.items()] + [T]
LINES = F.linien() + [line(*X((22, 0)), *X((22, 65))), line(*X((34, 0)), *X((34, 65)))]
TORE = [F.tor()] + F.minitore(7, 58)
DIMS = F.masslinie("40 m")
FANG = (21, 20)      # dort fängt Spieler acht den Pass ab
N9 = (17, 20)        # Spieler neun kommt von vorn

u = {"title": "Hoch pressen nach dem Signal", "code": "UE-340", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 18,
 "field_size": "Volle Breite x 40 m",
 "description": "Acht gegen acht auf einer Hälfte in voller Breite. Team Rot baut mit dem Torwart auf und will den Ball zu seinem Zehner in der Endzone bringen, der auf zwei Minitore abschließt. Team Neon wartet, bis Team Rot den ersten Pass nach vorn spielt. Dann pressen alle gemeinsam, erobern den Ball und gehen schnell aufs große Tor.",
 "organisation": ["Aufbauen: Eine Hälfte in voller Breite, etwa 40 Meter lang. Auf der Torlinie steht das große Tor mit Torwart, am anderen Ende zwei Minitore. Davor ist eine Endzone für den Zehner von Team Rot abgesteckt.",
  "Verteilen: Team Rot mit Torwart und sieben Feldspielern, einer davon wartet als Zehner in der Endzone. Team Neon presst mit acht Spielern. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet. Sobald Team Rot den ersten Pass nach vorn spielt, presst Team Neon gemeinsam. Nach dem Ballgewinn schnell abschließen oder den Ball sichern und ruhig aufbauen. Kommt Team Rot durch, spielt es auf den Zehner, und der schließt auf ein Minitor ab.",
  "Wertung: Jeder Treffer von Team Neon ins große Tor gibt einen Punkt. Trifft der Zehner ein Minitor, gibt das einen Punkt für Team Rot. Der Trainer startet neu, mal beim Torwart, mal mit einem Ball von der Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Erster Pass nach vorn, jetzt pressen alle", "Zu dritt um den Ball, keiner jagt allein", "Der Sechser stellt den Weg zum Zehner zu", "Kommt Rot durch, sofort zurück und neu ordnen"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Endzone", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Hoch pressen nach dem Signal. Acht gegen acht auf einer Hälfte. Team Rot baut vom Torwart aus auf, und mit dem ersten Pass nach vorn geht bei Team Neon die Jagd los.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", *fu(POS["r1"]))] + ERSATZ,
  "steps": [
   S("Torwart eröffnet kurz", "Der Torwart spielt kurz auf Spieler sechs. Noch presst keiner. Team Neon steht und wartet auf den ersten Pass nach vorn.",
     zu("b1", POS["r6"])),
   S("Erster Pass nach vorn: das Signal", "Jetzt spielt Spieler sechs nach vorn auf Spieler fünfzehn. Das ist das Signal. Spieler elf läuft sofort an. Von vorn kommt Spieler neun, von hinten Spieler acht.",
     zu("b1", POS["r15"]), lauf("n11", (20.5, 10), delay=0.6), lauf("n9", N9, delay=0.8),
     lauf("n8", (23, 15), delay=0.8), lauf("n4", (29, 30), delay=1.0), lauf("n10", (22, 34), delay=1.0)),
   S("Eingekreist, Ball erobert", "Spieler fünfzehn ist eingekreist. Der Weg zum Zehner ist zu, Spieler vier steht im Passweg. Er versucht es trotzdem durch die Mitte, und Spieler acht hat den Ball.",
     zu("b1", FANG), lauf("n8", FANG, delay=0.2), lauf("r14", (17, 37), delay=0.3)),
   S("Schnell abschließen: Punkt", "Kein langes Spiel jetzt. Spieler acht legt sofort auf Spieler neun, und der schießt aus der Drehung ins lange Eck. Das gibt einen Punkt für Team Neon. Danach startet der Trainer den nächsten Angriff, mal beim Torwart, mal von der Seite.",
     zu("b1", N9), h.ps("b1", [82.9, 29.6], after=True), lauf("r1", (2, 29), delay=0.3))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mehrere Leute um den Ball.", "Mehrere Leute um den Ball",
    "Einer allein holt den Ball nicht. Der Erste läuft an, der Zweite kommt von der Seite, der Dritte steht dahinter. So hat der Ballführer keinen freien Pass mehr und muss etwas riskieren.",
    sp(), [h.B("b1", *fu(POS["r6"]))] + ERSATZ,
    [S("Pass in die Mitte", "Spieler sechs spielt in die Mitte auf Spieler vierzehn. Sofort schiebt Team Neon zusammen. Spieler neun kommt von vorn, Spieler zehn von hinten.",
       zu("b1", POS["r14"]), lauf("n10", (22, 34), delay=0.4), lauf("n9", (15, 28), delay=0.4), lauf("n7", (15, 42), delay=0.6), lauf("n8", (24, 26), delay=0.6)),
     S("Kein Weg frei, abgefangen", "Spieler vierzehn hat keinen freien Pass mehr. Er will raus auf Spieler fünf, aber Spieler sieben ist dazwischen und hat den Ball.",
       zu("b1", (14, 41)), lauf("n7", (14, 41), delay=0.2)),
     S("Direkt zum Tor: Punkt", "Spieler sieben ist schon im Strafraum. Zwei Schritte, Schuss, und das gibt einen Punkt für Team Neon.",
       h.dr("n7", "b1", X((10, 37))), lauf("r1", (2, 37), delay=0.4), h.ps("b1", [82.9, 25.4], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell nachrücken und die Überzahl nutzen.", "Schnell nachrücken",
    "Ist der Ball erobert, rücken die Nächsten sofort nach. So entsteht in Ballnähe eine Überzahl. Einer startet in die Tiefe, und der Ball geht schnell nach vorn, bevor Team Rot sich ordnen kann.",
    sp(), [h.B("b1", *fu(POS["r13"]))] + ERSATZ,
    [S("Außen erobert", "Spieler dreizehn hat den Ball außen. Spieler zwei läuft ihn von hinten an, nimmt ihm den Ball ab und hat ihn am Fuß.",
       lauf("n2", (17, 61)), h.dr("n2", "b1", X((19, 56)), after=True)),
     S("Nachrücken, Spieler sieben startet", "Sofort rücken Spieler zehn und Spieler sieben nach. Spieler zwei schaut hoch, Spieler sieben startet in die Tiefe zwischen Spieler fünf und Spieler sechs.",
       lauf("n10", (22, 48)), lauf("n7", (8, 33), delay=0.3), h.bl("n2", hf.richt(X((19, 56)), X((8, 33)), 20), delay=0.3), lauf("n9", (16, 28), delay=0.4)),
     S("Steil in den Lauf: Punkt", "Spieler zwei spielt steil in den Lauf. Spieler sieben ist frei vor dem Torwart und trifft, und das gibt einen Punkt für Team Neon.",
       zu("b1", (8, 33)), lauf("r1", (2.5, 28), delay=0.3), h.ps("b1", [82.9, 30], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
