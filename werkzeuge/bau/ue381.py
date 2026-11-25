import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
import halbfeld as hf
# 09-P11 (U15-U17, Woche 29 Phase 3): Attacking Transitions to Finish (Medium Sided Game). Acht gegen acht plus zwei Torhüter.
# Feld: PDF „full half“ und „full width“ (die Skizze hat die Maße einer echten Hälfte, Strafraum über 62 % der Breite); der Ton
# nennt 55 x 45 Yards „which can be adjusted by age group“. Für U15-U17 die ganze Hälfte, 50 x 65 m, field_size „Halbes Spielfeld“.
# HALBES FELD QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Regel in AUFTRAG.md): Hälfte wie im Fernsehbild, echte Linien
# (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), "massstab": "gross". Abbildung mit bau/halbfeld.py, Positionen in
# Metern geplant (d = Meter vor der Torlinie, q = Meter von der oberen Seitenlinie).
# Lage mit zwei Toren: Das Haupttor mit echtem Strafraum steht RECHTS auf der Grundlinie (Regelfall: Team Neon greift dort im
# sechs gegen vier nach rechts an, das ist der größte Teil der Übung). Das zweite große Tor steht wie im PDF auf der Mittellinie
# am linken Rand (side left, ragt bis x 5,5), umrahmt vom halben Mittelkreis wie in der Skizze; darauf kontert Team Rot nach
# links. Ein Tor links mit Strafraum und das andere rechts ginge nicht: Auf der Mittellinie gibt es keinen Strafraum, und das
# Hauptspiel sechs gegen vier braucht den echten Strafraum.
# Gegenüber der PDF-Skizze (Grundlinientor oben) im Uhrzeigersinn gedreht, nicht gespiegelt (PDF links = oben): Flügel von
# Neon 11 und Rot 7 (hier r14) oben, Neon 7 und Rot 11 (hier r15) unten. Darum spielt der Trainer jetzt Spieler sieben an
# (unten, nahe an der Seitenlinie, wo der Trainer steht) statt wie bisher Spieler elf.
# Gestrichelte Linie zwischen den Bereichen 26 m vor dem Grundlinientor (im PDF gepunktet, etwa 24 m; im Text gerundet 25 m). Den Mittelkanal (im PDF
# grau, so breit wie der Strafraum) nicht gezeichnet: er läge genau auf den Strafraumlinien; die Sperre für die Flügel steht im Text.
# Navy/Video gelb (sechs Angreifer + zwei Verteidiger hinten) -> Team Neon mit den Nummern aus dem PDF.
# Pink/Video rot -> Team Rot, neu nummeriert (Nummern doppelt): 4 -> 2, 5 -> 3, 6 -> 12, 8 -> 13, 7 -> 14, 11 -> 15, 10 -> 16, 9 -> 17.
# Beide Torhüter neutral (k1 Grundlinientor, k2 Tor auf der Mittellinie). Ein Trainer statt zwei, unten an der Seitenlinie im
# Konterbereich (spielt das sechs gegen vier und den Konter an).
# 3D-Abstand (massstab gross): Figuren in Spalten (gleiche Tiefe) mindestens 15 m in der Breite auseinander, die Spalten mindestens
# 5,9 Einheiten versetzt. Darum stehen die vier Mittelfeldspieler von Neon in einer Reihe 28 m vor dem Tor, Spieler sechzehn und
# siebzehn hintereinander dahinter, Spieler neun und zehn hintereinander vor dem Strafraum.
# Grundform: Angriff sechs gegen vier mit Flanke ohne Treffer, dann Konter vier gegen zwei (PDF-Ablauf).
# Fassungen: Key Coaching Point (freien Spieler finden, Doppelpass am Strafraum, Video „Quick 1-2's around the box“) und
# Progression aus dem Ton (Sperre für die Flügelspieler fällt weg, „go to show, show to go“).
# Sichtkegel: Ton „get their head up and communicate to find that spare teammate“, im Video nicht eingezeichnet.
# Richtung aus dem Sinn: der Ballführer schaut vor dem Pass zum freien Mitspieler.
F = hf.Halbfeld()                      # 50 x 65 m, Tor rechts (x 90), Mittellinie links (x 10), y 3-52
def X(p): return F(*p)                 # Meter -> Tafel
def fu(p): return hf.am_fuss(F(*p))    # Pass zum Spieler / Ball am Fuß
def zu(ball, p, **k): return h.ps(ball, fu(p), **k)
def lauf(who, p, **k): return h.mv(who, X(p), **k)
def schau(who, p, ziel, weit=20, **k): return h.bl(who, hf.richt(X(p), X(ziel), weit), **k)
T = h.P("T", "c", 45.5, 55.3, "T")     # unten an der Seitenlinie im Konterbereich
ERSATZ = [h.B("s1", 51.5, 55.8), h.B("s2", 54, 55.8)]
POS = {"k1": (2.5, 32.5), "r2": (8, 24), "r3": (8, 39.5), "n9": (13, 32.5), "n10": (18, 32.5),
       "r12": (23.5, 25), "r13": (23.5, 40), "r14": (23.5, 3), "r15": (23.5, 61),
       "n11": (28, 7), "n8": (28, 22), "n6": (28, 37), "n7": (28, 52),
       "r16": (32.5, 32.5), "r17": (38.5, 32.5), "n5": (44, 25), "n4": (44, 40), "k2": (48, 32.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [h.P(i, "t", *X(p), "TW") if i[0] == "k" else h.P(i, "a" if i[0] == "n" else "b", *X(p), i[1:]) for i, p in d.items()] + [T]
def li(a, b):
    p, q = X(a), X(b)
    return line(p[0], p[1], q[0], q[1])
LINES = F.linien() + [li((26, 0), (26, 65))]   # zwischen den Spalten bei 23,5 und 28 m
TORE = [F.tor()] + F.minitore(32.5, size="gross")   # Grundlinientor rechts, zweites großes Tor auf der Mittellinie links
BT = hf.am_fuss([T["x"], T["y"]])                    # Ball beim Trainer
B2 = [49, 55.8]                                      # zweiter Ball für den Konter

u = {"title": "Sechs gegen vier, dann Konter", "code": "UE-381", "kind": "Spielform",
 "focuses": ["Umschalten", "Torschuss", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 18, "players_max": 18,
 "field_size": "Halbes Spielfeld",
 "description": "Acht gegen acht plus zwei Torhüter auf einer Platzhälfte mit zwei Bereichen. Am Tor auf der Grundlinie greift Team Neon mit sechs Spielern gegen vier Verteidiger an und muss nach spätestens sechs Pässen schießen. Geht der Schuss vorbei oder kommt keiner, spielt der Trainer sofort einen Ball in den anderen Bereich, und Team Rot kontert vier gegen zwei auf das Tor an der Mittellinie. So wechseln Abschluss und schnelles Umschalten ständig.",
 "organisation": ["Aufbauen: Eine ganze Platzhälfte über die volle Breite, ein großes Tor auf der Grundlinie und eins auf der Mittellinie. Eine gestrichelte Linie 25 Meter vor dem Tor auf der Grundlinie teilt das Feld in den Bereich für das sechs gegen vier und den Bereich für den Konter.",
  "Verteilen: Am Tor auf der Grundlinie greifen sechs Spieler von Team Neon gegen vier Verteidiger von Team Rot an. Die zwei Flügelspieler von Team Rot dürfen nicht mit verteidigen. Im Konterbereich warten zwei Spitzen von Team Rot gegen zwei Verteidiger von Team Neon. In jedem Tor steht ein Torwart, der Trainer steht mit vielen Bällen an der Seitenlinie.",
  "Ablauf: Der Trainer spielt ins sechs gegen vier, Team Neon hat höchstens sechs Pässe bis zum Abschluss. Geht der Schuss vorbei oder kommt keiner, spielt der Trainer einen neuen Ball in den Konterbereich, und die vier Angreifer von Team Rot kontern gegen zwei. Erobert ein Verteidiger den Ball, spielt er ihn sofort zu seinen Angreifern.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach spielt der Trainer wieder im sechs gegen vier an. Nach einigen Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Bewegen, bis einer frei ist", "Spätestens nach sechs Pässen schießen", "Ball erobert? Sofort nach vorn", "Kurze Doppelpässe am Strafraum"],
 "materials": ["2 große Tore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechs gegen vier, dann Konter. Am Tor auf der Grundlinie greift Team Neon in Überzahl an. Klappt es nicht, kontert Team Rot sofort auf der anderen Seite.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", *BT), h.B("b2", *B2)] + ERSATZ,
  "steps": [
   S("Trainer spielt ins sechs gegen vier", "Der Trainer spielt Spieler sieben auf dem Flügel an. Am Tor auf der Grundlinie hat Team Neon jetzt sechs gegen vier, denn die Flügelspieler von Team Rot dürfen nicht mit zurück. Nach spätestens sechs Pässen muss der Schuss kommen.",
     zu("b1", POS["n7"])),
   S("Andribbeln, vier gehen in den Strafraum", "Spieler sieben dribbelt an der Seitenlinie Richtung Grundlinie. Vier Mitspieler laufen in den Strafraum, zwei Verteidiger gehen mit. Spieler acht bleibt hinter dem Strafraum für den zweiten Ball.",
     h.dr("n7", "b1", X((14, 54))), lauf("n10", (6, 14), delay=0.3), lauf("n9", (11, 31), delay=0.3), lauf("n11", (13, 18), delay=0.3),
     lauf("n6", (6, 41), delay=0.3), lauf("n8", (19, 30), delay=0.3), lauf("r12", (14, 25), delay=0.5), lauf("r13", (14, 40), delay=0.5)),
   S("Kopf hoch, Flanke, knapp vorbei", "Spieler sieben nimmt den Kopf hoch und sieht Spieler neun in der Mitte. Flanke, Spieler neun schießt direkt, knapp vorbei. Ein Treffer hätte einen Punkt für Team Neon gegeben.",
     schau("n7", (14, 54), (11, 31)), zu("b1", (11, 31), after=True), h.ps("b1", [91, 32.5], after=True)),
   S("Kein Treffer, der Konter läuft", "Kein Treffer, also spielt der Trainer sofort einen neuen Ball zu Spieler sechzehn. Jetzt kontert Team Rot vier gegen zwei auf das Tor an der Mittellinie. Die beiden Flügelspieler sprinten mit.",
     zu("b2", POS["r16"]), h.dr("r16", "b2", X((34.5, 30)), after=True), lauf("r14", (40, 10), delay=0.4), lauf("r15", (40, 55), delay=0.4)),
   S("Vier gegen zwei: Punkt", "Spieler sechzehn spielt kurz zu Spieler siebzehn. Spieler fünf geht drauf, also legt Spieler siebzehn raus auf Spieler fünfzehn. Der schießt aus vollem Lauf, und das gibt einen Punkt für Team Rot. Danach spielt der Trainer wieder im sechs gegen vier an.",
     zu("b2", POS["r17"]), lauf("n5", (40.5, 28), delay=0.2), zu("b2", (40, 55), after=True), h.ps("b2", [10.3, 30], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den freien Mitspieler finden.", "Den freien Mann finden",
    "Sechs gegen vier heißt, zwei sind immer frei. Der Ballführer nimmt den Kopf hoch und sucht sie. Die anderen bewegen sich so, dass ein Verteidiger rausmuss und hinter ihm Platz entsteht. Rund um den Strafraum hilft ein schneller Doppelpass.",
    sp(), [h.B("b1", *fu(POS["n8"])), h.B("b2", *B2)] + ERSATZ,
    [S("Kopf hoch, wer ist frei?", "Spieler acht dribbelt an. Spieler zwölf muss raus und geht auf ihn drauf. Damit ist Spieler zehn frei. Spieler acht schaut hoch, sieht ihn und spielt.",
       h.dr("n8", "b1", X((26.5, 22))), lauf("r12", (25, 19), delay=0.3), schau("n8", (26.5, 22), POS["n10"], after=True), zu("b1", POS["n10"], after=True)),
     S("Doppelpass am Strafraum", "Spieler zehn spielt direkt in die Mitte zu Spieler neun und startet sofort in den Strafraum. Spieler neun lässt den Ball mit einem Kontakt in seinen Lauf prallen.",
       zu("b1", POS["n9"]), lauf("n10", (10, 14), delay=0.3), zu("b1", (10, 14), after=True)),
     S("Abschluss: Punkt", "Spieler zehn schießt flach ins kurze Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball ins sechs gegen vier.",
       h.ps("b1", [90.3, 25.3]))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Flügelspieler von Team Rot verteidigen mit.", "Flügel verteidigen jetzt mit",
    "Die Sperre fällt weg. Die Flügelspieler von Team Rot dürfen zurück, es steht sechs gegen sechs. Jetzt müssen die Angreifer ihre Verteidiger bewegen. Erst kurz zum Ball kommen, dann in die Tiefe starten, und die Lücke ist offen.",
    sp(), [h.B("b1", *BT), h.B("b2", *B2)] + ERSATZ,
    [S("Die Flügel laufen mit zurück", "Der Trainer spielt Spieler sieben an. Sofort laufen beide Flügelspieler von Team Rot mit zurück. Spieler fünfzehn stellt Spieler sieben.",
       zu("b1", POS["n7"]), lauf("r15", (26, 52), delay=0.3), lauf("r14", (18, 8), delay=0.3)),
     S("Kurz zeigen, dann in die Tiefe", "Spieler neun kommt kurz zum Ball, und Spieler drei geht mit. Dann dreht Spieler neun ab und startet in die Tiefe. Spieler sieben schaut hoch und spielt in den Lauf.",
       lauf("n9", (16, 38)), lauf("r3", (14, 41), delay=0.3), lauf("n9", (8, 30), after=True), schau("n7", POS["n7"], (8, 30), after=True),
       zu("b1", (8, 30), after=True)),
     S("Allein vor dem Torwart: Punkt", "Spieler neun ist durch und schiebt am Torwart vorbei ins Eck, und das gibt einen Punkt für Team Neon. Danach geht es weiter wie gehabt.",
       lauf("k1", (4, 28)), h.ps("b1", [90.3, 29.8], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
