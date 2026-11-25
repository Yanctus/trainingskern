import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 10-P11 (U15-U17, Woche 14): High Press to Win Possession. Halbes Großfeld in voller Breite, großes Tor (Großfeldtor, C- und
# B-Jugend), zwei Minitore auf einer gestrichelten Linie zehn Meter vor der Mittellinie (im PDF etwa bei 36 m, hier bei 40 m).
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): umgebaut vom Hochformat (Tor oben) auf
# die Hälfte wie im Fernsehbild. Großes Tor RECHTS, Mittellinie links, Platzbreite von oben nach unten, echte Linien
# (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Team Neon presst und greift nach rechts an,
# Team Rot baut vom Torwart am großen Tor aus auf. Gedreht im Uhrzeigersinn (PDF links = oben), nicht gespiegelt.
# Positionen neu in Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie, Hälfte 50 x 65 m),
# F(d, q) rechnet auf die Tafel um. Die Paare aus dem PDF stehen für den 3D-Abstand in der Tiefe versetzt.
# Neon behält die Nummern aus dem PDF (2, 3, 6, 8, 9, 10, 11). Rot neu nummeriert, weil alle Nummern doppelt wären:
# Blau 6 -> 5, Blau 4 -> 4, Blau 2 -> 12, Blau 8 -> 14, Blau 5 -> 7, Blau 10 -> 15, Blau 3 -> 13, Torwart = r1 "TW".
# Ein Trainer statt zwei (unten an der Seitenlinie, nahe beim Tor, wo der Torwart neu beginnt).
# Grundform = Szene aus PDF und Video ("FB presses - CM covers"): Abstoß kurz nach außen (im PDF auf die rechte Seite des
# Angreifers, hier unten), Spieler zwei läuft an, Spieler acht sichert und fängt den Pass die Linie entlang ab.
# Fassung 1 = Gegenbeispiel aus dem Ton (Außenspieler presst zu früh allein, der Weg außen ist offen).
# Fassung 2 = "High press forces GK error" aus dem Video.
# Sichtkegel: im Video keiner eingezeichnet; aus dem Ton ("even if they are able to get their head up to switch, as we
# can see from our keeper"): Der Torwart hebt unter Druck den Kopf und sucht die Verlagerung (Fassung 2).
# Kein Dubletten-Fall: UE-148 (3 gegen 3 in Duellen), UE-236 (Pressingwelle 3 gegen 3), UE-243 (Dreierkette) sind andere Formen.
F = hf.Halbfeld()                      # 50 x 65 m, Tor rechts (x 90), Mittellinie links (x 10), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
T = h.P("T", "c", 84, 55.3, "T")       # unten an der Seitenlinie, nahe beim Tor
ERSATZ = [h.B("s1", 87.5, 55.8), h.B("s2", 90, 55.8)]
POS = {"r1": (2, 32.5), "r5": (10, 18), "r4": (8, 40), "r12": (20, 4), "r14": (22, 32.5), "r7": (21, 56),
       "r15": (36, 40), "r13": (28, 61.5),
       "n11": (16, 25), "n9": (16, 41), "n3": (25, 9), "n10": (31, 24), "n8": (30, 46), "n6": (42, 33), "n2": (37, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "r1" else i[1:]) for i, p in d.items()] + [T]
MT = (8.5, 56.5)                       # Minitore (q in Metern) auf der Linie bei 40 m
LINES = F.linien() + [line(*X((40, 0)), *X((40, 65)))]
TORE = [F.tor()] + F.minitore(*MT, d=40)
R7 = (12, 59)        # dort nimmt Spieler sieben den Abstoß an
N9 = (11, 50)        # Spieler neun stellt den Rückpass zu
FREI9 = (16, 46)     # dort löst sich Spieler neun nach dem Ballgewinn
FANG = (21, 59.5)    # dort fängt Spieler acht den Pass ab
SCHUSS = [90.4, 25.8]  # langes Eck (oberer Pfosten); Spieler neun zieht dafür bis q 34 nach innen, damit der Schuss nicht durch Spieler vier geht (Passbahn 25.11.)

u = {"title": "Pressingfalle am Flügel", "code": "UE-314", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 18,
 "field_size": "Halbes Spielfeld",
 "description": "Sieben gegen sieben auf einer Spielfeldhälfte, dazu ein Torwart. Team Rot baut mit einem kurzen Abstoß auf und will eines der zwei Minitore treffen. Team Neon presst hoch, lenkt den Ball auf eine Seite und schnappt dort gemeinsam zu. Nach dem Ballgewinn geht es sofort auf das große Tor.",
 "organisation": ["Aufbauen: Eine Spielfeldhälfte in voller Breite. Auf der Torlinie steht das große Tor, zehn Meter vor der Mittellinie stehen zwei Minitore.",
  "Verteilen: Team Rot baut mit Torwart und sieben Feldspielern auf. Team Neon presst mit sieben Feldspielern, jeder hat einen Gegenspieler. Der Trainer steht mit Bällen an der Seitenlinie, nahe beim Tor.",
  "Ablauf: Der Torwart eröffnet mit einem kurzen Abstoß. Team Neon lenkt den Ball auf eine Seite und greift dort gemeinsam zu. Nach dem Ballgewinn geht es sofort zum Abschluss.",
  "Wertung: Ein Treffer von Team Neon ins große Tor gibt einen Punkt. Spielt sich Team Rot frei und trifft ein Minitor, gibt das einen Punkt für Team Rot. Weiter geht es immer beim Torwart, auf Kommando des Trainers."],
 "organisation_show": ORG,
 "coaching_points": ["Erst stehen alle, dann pressen alle", "Außen anlaufen, dahinter sichert der Sechser", "Rückpass zustellen, den langen Ball erzwingen", "Nach dem Ballgewinn sofort zum Tor"],
 "materials": ["1 großes Tor", "2 Minitore", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pressingfalle am Flügel. Sieben gegen sieben auf einer Hälfte. Team Rot baut vom Torwart aus auf, Team Neon presst hoch und holt sich den Ball außen.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", *fu(POS["r1"]))] + ERSATZ,
  "steps": [
   S("Kurzer Abstoß nach außen", "Team Neon steht hoch, jeder hat seinen Gegenspieler. Der Torwart spielt den Abstoß kurz nach außen, Spieler sieben kommt dem Ball entgegen.",
     lauf("r7", R7), zu("b1", R7, delay=0.4)),
   S("Zwei läuft an, Acht sichert", "Das ist das Signal. Spieler zwei sprintet von innen auf Spieler sieben. Vorne stellt Spieler neun den Rückpass zu, und hinter Spieler zwei schiebt Spieler acht nach außen.",
     lauf("n2", (15, 55.5)), lauf("n9", N9, delay=0.2), lauf("n8", (25, 57), delay=0.4), lauf("n11", (12, 31), delay=0.4), lauf("n10", (27, 29), delay=0.4)),
   S("Pass die Linie entlang, abgefangen", "Spieler sieben bleibt nur der Pass die Linie entlang. Genau darauf wartet Spieler acht. Er geht dazwischen und hat den Ball.",
     zu("b1", FANG), lauf("n8", FANG, delay=0.2), lauf("r1", (2, 37), delay=0.3)),
   S("Schnell zum Abschluss: Punkt", "Jetzt schnell. Spieler neun löst sich, und Spieler acht spielt flach auf ihn. Er zieht nach innen und schießt ins lange Eck. Das gibt einen Punkt für Team Neon. Der nächste Ball liegt wieder beim Torwart, und los geht es erst auf Kommando des Trainers.",
     lauf("n9", FREI9), zu("b1", FREI9, after=True), h.dr("n9", "b1", X((12, 34)), after=True), h.ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst stehen alle, dann pressen alle.", "Erst stehen, dann pressen",
    "Gepresst wird nur, wenn alle bereit stehen. Läuft einer zu früh allein los, ist hinter ihm der Weg frei, und mit zwei Pässen ist das Pressing überspielt. Also erst die Abstände prüfen und dann gemeinsam starten.",
    sp(r7=R7), [h.B("b1", *fu(R7))] + ERSATZ,
    [S("Zwei presst allein", "So geht es schief. Spieler zwei rennt allein los. Hinter ihm rückt keiner nach, und außen ist alles offen.",
       lauf("n2", (15, 55.5))),
     S("Außen durch: Punkt für Team Rot", "Ein Pass die Linie entlang, und Spieler dreizehn hat freie Bahn. Spieler acht kommt zu spät. Der Ball rollt ins Minitor, und das gibt einen Punkt für Team Rot.",
       zu("b1", POS["r13"]), h.dr("r13", "b1", X((36, 59)), after=True), lauf("n8", (31, 53), delay=0.8), h.ps("b1", X((40.6, MT[1])), after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den langen Ball erzwingen.", "Langen Ball erzwingen",
    "Sind die kurzen Wege zu, muss der Torwart lang spielen. Ein langer Ball unter Druck kommt selten genau. Darum bleiben die Spieler auf der anderen Seite wach und gehen früh dazwischen.",
    sp(), [h.B("b1", *fu(POS["r4"]))] + ERSATZ,
    [S("Rückpass zum Torwart", "Spieler vier hat den Ball. Spieler neun läuft ihn an, und es bleibt nur der Rückpass zum Torwart.",
       lauf("n9", (12, 36)), zu("b1", POS["r1"], delay=0.4)),
     S("Torwart unter Druck, Kopf hoch", "Spieler neun läuft durch bis zum Torwart. Spieler elf stellt den kurzen Pass zu Spieler fünf zu. Der Torwart hebt den Kopf und sucht die Verlagerung.",
       lauf("n9", (5, 35)), lauf("n11", (6, 22), delay=0.2), h.bl("r1", hf.richt(X(POS["r1"]), X((22, 8)), 20), delay=0.6)),
     S("Langer Ball, abgefangen", "Er spielt den Ball lang auf die andere Seite. Unter Druck wird der Pass ungenau. Spieler drei ist vor Spieler zwölf am Ball, und von hier ist der Weg zum Tor kurz.",
       zu("b1", (23, 10)), lauf("r12", (23, 5), delay=0.2), lauf("n3", (23, 10), delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
