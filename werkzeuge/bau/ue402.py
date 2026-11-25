import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 18-P11 (U15-U17, Woche 37 Phase 1): Playing Through the Thirds (Medium Sided Game). 7 gegen 7 plus Torwart auf einer
# ganzen Platzhälfte in voller Breite.
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): Die Hälfte liegt wie im Fernsehbild,
# großes Tor rechts (Großfeldtor, nur C- und B-Jugend), Mittellinie links mit zwei Minitoren für den Konter, Platzbreite von oben
# nach unten, echte Linien (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Team Neon baut an der
# Mittellinie auf und greift nach rechts an. Abbildung mit bau/halbfeld.py (Hälfte 50 x 65 m): Positionen in Metern neu geplant
# (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie), nach der PDF-Skizze im Uhrzeigersinn gedreht (PDF links =
# oben). Das alte Hochformat-Skript war nicht metergenau und wurde nicht umgerechnet.
# Zonengrenzen (Drittel) gestrichelt quer zur Spielrichtung bei 18 m und 34 m vor dem Tor (im PDF etwa ein Drittel und zwei
# Drittel; die erste Linie absichtlich nicht auf der Strafraumlinie bei 16,5 m), Hütchen an beiden Enden auf den Seitenlinien.
# PDF pink (3, 4, 6 hinten, 11, 8, 7 Mitte, 9 vorn) -> Team Neon, Nummern wie im PDF. PDF blau -> Team Rot mit Torwart r1
# (im PDF grün), neu nummeriert, weil die Nummern doppelt sind: 4 -> 2, 5 -> 5, 8 -> 13, 6 -> 12, 10 -> 10, 9 -> 14, 11 -> 15.
# Für den 3D-Abstand stehen Gegenspieler in der Tiefe versetzt (Verteidiger torseitig), leicht gegenüber dem PDF verschoben.
# Ein Trainer statt zwei, unten an der Mittellinie (spielt den neuen Ball zu den drei Spielern hinten).
# Grundform nach PDF und Video 0:03-0:23: 6 -> 4 -> 3, steil auf 8 in der Mitte, raus auf 11, Pass in die Endzone auf 9,
# 11 und 7 laufen mit ein ("support run"). Abschluss vereinfacht: Die Verteidiger gehen mit den Läufern mit, 9 dreht auf und schießt.
# Fassungen: PDF Key Coaching Point (Verteidiger dribbelt in die Mittelzone, vier gegen zwei; im Video als Regel "defender can
# dribble into middle zone", darum Steigerung) und Progression (mindestens zwei Spieler je Zone und Team).
# Die Zwischenstufe aus dem Video (ein Verteidiger von Team Rot darf in eine tiefere Zone helfen) nur im Bericht.
# Sichtkegel: Text/Ton "Recognise whether to advance", "spatial awareness", "fully aware of team mates' positioning"; im Video
# nicht eingezeichnet. Richtung aus dem Sinn: Spieler acht schaut zum Passgeber, nimmt an und schwenkt den Blick beim Aufdrehen
# nach außen (bl mit von + drehen, Vorbild ue300); Spieler neun genauso vor dem Abschluss; in den Steigerungen schaut Spieler vier
# (Kegel auf etwa 20 Einheiten gekürzt) vor dem Andribbeln bzw. vor dem Nachrücken nach vorn.
# Kein Dublette: UE-234 (43-P11) ist auch ein halbes Feld mit drei Zonen und Konter auf Minitore, aber 8 gegen 8 mit 2 gegen 1
# hinten und anderer Regel (Dribbling in die Mitte öffnet das Spiel); hier 3 gegen 3, 3 gegen 2, Anspiel in jeder Zone Pflicht.
F = hf.Halbfeld()                      # 50 x 65 m, Tor rechts (x 90), Mittellinie links (x 10), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
def schau(who, p, ziel, weit=20, von=None, **k):
    return h.bl(who, hf.richt(X(p), X(ziel), weit), von=hf.richt(X(p), X(von)) if von else None, **k)
T = h.P("T", "c", 12, 55.3, "T")       # unten an der Mittellinie
ERSATZ = [h.B("s1", 15.5, 55.8), h.B("s2", 18, 55.8)]
POS = {"r1": (2.5, 34.5), "r2": (9, 24), "r5": (9, 41), "n9": (14, 33),
       "n11": (27, 6), "r13": (23.5, 24), "n8": (30, 33), "r12": (24, 44), "n7": (29, 57),
       "r10": (40, 13), "r14": (38.5, 37), "r15": (42, 57), "n3": (47.5, 8), "n4": (43.5, 33), "n6": (47, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", *X(p), "TW" if i == "r1" else i[1:]) for i, p in d.items()] + [T]
D1, D2 = 18, 34                        # Zonengrenzen in Metern vor der Torlinie
LINES = F.linien() + [line(*X((D1, 0)), *X((D1, 65))), line(*X((D2, 0)), *X((D2, 65)))]
CONES = [h.C(*X((d, q))) for d in (D1, D2) for q in (0, 65)]
TORE = [F.tor()] + F.minitore(12, 53)
SCHUSS = [90.4, 25.3]                  # flach ins Eck, oben am Torwart vorbei
N9 = (16, 30)                          # Spieler neun kommt in der Endzone kurz

u = {"title": "Sieben gegen sieben in Dritteln", "code": "UE-402", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 15, "field_size": "Halbes Spielfeld",
 "description": "Sieben gegen sieben plus Torwart auf einer ganzen Platzhälfte, geteilt in drei Zonen. Team Neon spielt sich von der Mittellinie Zone für Zone nach vorn und greift das große Tor an. In die nächste Zone darf der Ball nur, wenn ein Mitspieler in seiner Zone angespielt wurde. Erobert Team Rot den Ball, kontert es auf zwei Minitore an der Mittellinie.",
 "organisation": ["Aufbauen: Eine Platzhälfte in voller Breite mit großem Tor und Torwart. Zwei gestrichelte Linien quer über das Feld teilen sie in drei Zonen: hinten an der Mittellinie, Mitte und die Endzone vor dem Tor. Auf der Mittellinie stehen zwei Minitore.",
  "Verteilen: Team Neon mit drei Spielern hinten, drei in der Mitte und einem Stürmer vorn. Team Rot mit Torwart, zwei Verteidigern vorn, zwei Spielern in der Mitte und drei Spielern hinten. Hinten ist es drei gegen drei, in der Mitte drei gegen zwei, vorn einer gegen zwei. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Team Neon baut hinten auf. Der Ball geht erst in die nächste Zone, wenn dort ein Mitspieler angespielt wurde. Wer angespielt ist, darf nach vorn nachrücken. Vorn laufen die Mittelfeldspieler mit in die Endzone und helfen dem Stürmer.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und trifft in ein Minitor, gibt das einen Punkt für Team Rot. Danach spielt der Trainer einen neuen Ball zu den drei Spielern hinten."],
 "organisation_show": ORG,
 "coaching_points": ["Passen oder andribbeln? Erst schauen, dann entscheiden", "Ist vor dir Platz, nimm den Ball mit", "Geht einer nach vorn, sichert ein anderer ab", "Ball weg? Sofort umschalten"],
 "materials": ["1 großes Tor", "2 Minitore", "4 Hütchen für die Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sieben gegen sieben in Dritteln. Team Neon spielt sich auf einer Platzhälfte von der Mittellinie durch drei Zonen bis vor das große Tor. Team Rot verteidigt und kontert auf zwei Minitore.",
 "board": {"massstab": "gross", "lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": [h.B("b1", *fu(POS["n6"]))] + ERSATZ,
  "steps": [
   S("Hinten drei gegen drei", "Spieler sechs eröffnet hinten an der Mittellinie. Über Spieler vier geht der Ball weiter zu Spieler drei. Hier hinten hat jeder einen Gegenspieler, also schnell spielen.",
     zu("b1", POS["n4"]), lauf("r14", (41, 35), delay=0.3), zu("b1", POS["n3"], after=True)),
   S("Steil in die Mittelzone", "Spieler acht zeigt sich in der Mitte und schaut zum Ball. Spieler drei spielt flach und steil zu ihm. Wer in seiner Zone angespielt wird, darf weiter nach vorn.",
     schau("n8", POS["n8"], POS["n3"]), zu("b1", POS["n8"], after=True)),
   S("Aufdrehen, raus nach außen", "Erst jetzt dreht Spieler acht auf, und der Blick geht nach außen. Spieler dreizehn kommt zu spät. Der Ball geht raus zu Spieler elf.",
     schau("n8", POS["n8"], POS["n11"], von=POS["n3"], dauer=1.3), h.drehen("n8", X(POS["n11"]), delay=0.4),
     lauf("r13", (26, 28), delay=0.6), zu("b1", POS["n11"], after=True)),
   S("Pass in die Endzone", "Spieler neun kommt kurz und schaut zum Ball. Spieler elf spielt ihn in der Endzone an und läuft sofort hinterher. Auf der anderen Seite startet Spieler sieben. Die beiden Verteidiger gehen mit.",
     lauf("n9", N9), schau("n9", N9, POS["n11"], delay=0.5), zu("b1", N9, after=True),
     lauf("n11", (10, 12), after=True), lauf("r2", (7, 17), after=True), lauf("n7", (10, 52), delay=1.2), lauf("r5", (7, 47), delay=1.5)),
   S("Aufdrehen, Abschluss: Punkt", "Spieler neun dreht auf und hat freie Bahn. Er schießt flach ins Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu den drei Spielern hinten.",
     h.bl("n9", SCHUSS, von=hf.richt(X(N9), X(POS["n11"])), dauer=1.3), h.drehen("n9", SCHUSS, delay=0.4), h.ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Spieler von hinten darf mit Ball in die Mittelzone dribbeln.", "Vier gegen zwei in der Mitte",
    "Jetzt darf ein Spieler von hinten mit Ball in die Mittelzone dribbeln. Dann stehen dort vier gegen zwei. Team Rot zieht sich zurück und stellt den Raum zu, statt sofort zu pressen. Team Neon hat so mehr Zeit am Ball.",
    sp(), [h.B("b1", *fu(POS["n4"]))] + ERSATZ,
    [S("Kopf hoch, Platz sehen", "Spieler vier hat den Ball. Vor ihm ist frei, Spieler vierzehn steht zu weit weg. Er schaut kurz hoch und dribbelt los in die Mittelzone.",
       schau("n4", POS["n4"], (32, 24)), h.dr("n4", "b1", X((32, 24)), after=True), lauf("n8", (27, 40), delay=0.8)),
     S("Vier gegen zwei ausspielen", "Jetzt sind es in der Mitte vier gegen zwei. Spieler dreizehn und Spieler zwölf ziehen sich zurück. Spieler vier spielt zu Spieler acht, und der spielt sofort in die Endzone auf Spieler neun.",
       lauf("r13", (20, 24)), lauf("r12", (20.5, 43)), zu("b1", (27, 40), delay=0.6), zu("b1", POS["n9"], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: In jeder Zone stehen immer mindestens zwei Spieler von jedem Team.", "Zwei Spieler in jeder Zone",
    "Jedes Team hat in jeder Zone immer mindestens zwei Spieler. Geht einer nach vorn, rückt ein anderer nach. So muss jeder wissen, wo seine Mitspieler stehen. Die Abstände bleiben gut, und hinten ist immer einer zum Absichern da.",
    sp(n7=(12, 57)), [h.B("b1", *fu(POS["n3"]))] + ERSATZ,
    [S("Einer geht vor, einer rückt nach", "Spieler drei spielt steil auf Spieler elf. Gleichzeitig startet Spieler acht in die Endzone. Jetzt fehlt in der Mitte einer. Spieler vier schaut nach vorn, sieht das und rückt sofort nach.",
       zu("b1", POS["n11"]), lauf("n8", (16, 38), delay=0.3), schau("n4", POS["n4"], (30, 33), delay=0.8), lauf("n4", (31, 27), after=True)),
     S("In die Endzone: Punkt", "Spieler elf spielt in die Endzone auf Spieler acht. Der legt quer zu Spieler neun, und Spieler neun schießt. Das gibt einen Punkt für Team Neon.",
       zu("b1", (16, 38)), zu("b1", POS["n9"], after=True), h.ps("b1", SCHUSS, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
