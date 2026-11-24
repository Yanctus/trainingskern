import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 09-P11 (U15-U17, Woche 29 Phase 3): Attacking Transitions to Finish (Medium Sided Game). 55 x 45 Yards = 50 x 41 m
# (gerundet 50 x 40 m), eine Platzhälfte über die volle Breite. Acht gegen acht plus zwei Torhüter.
# KEIN GROSSFELD QUER: halbes Feld mit 41 m Länge (AUFTRAG: „Halbes Feld und kleiner bleibt wie bisher“). Das Feld ist breiter
# als lang, die lange Seite liegt also schon waagrecht. Ausrichtung wie im PDF: großes Tor oben (Grundlinie, sechs gegen vier),
# großes Tor unten (auf der Mittellinie, Konter vier gegen zwei). Feld x 14-86, y 4-52, Strafraum und Torraum oben,
# gestrichelte Linie zwischen den beiden Bereichen (im PDF gepunktet). Mittelkreis-Halbkreis unten weggelassen (läge außerhalb der Tafel).
# Navy/Video gelb (sechs Angreifer + zwei Verteidiger hinten) -> Team Neon mit den Nummern aus dem PDF.
# Pink/Video rot -> Team Rot, neu nummeriert (Nummern doppelt): 4 -> 2, 5 -> 3, 6 -> 12, 8 -> 13, 7 -> 14, 11 -> 15, 10 -> 16, 9 -> 17.
# Beide Torhüter neutral (k1 oben, k2 unten). Ein Trainer statt zwei, links an der Seitenlinie zwischen den Bereichen
# (spielt das sechs gegen vier und den Konter an).
# 3D-Abstand: Figuren in Spalten 8,5 Einheiten auseinander, in einer Spalte mindestens 15,5 tief versetzt. Dafür stehen die
# Spieler etwas breiter als im PDF; navy 8 und 6 sind getauscht (Spieler acht rechts hinten, Spieler sechs rechts vorn), damit
# Spieler sechzehn (pink 10) links nah am Trainer steht.
# Grundform: Angriff sechs gegen vier mit Flanke ohne Treffer, dann Konter vier gegen zwei (PDF-Ablauf).
# Fassungen: Key Coaching Point (freien Spieler finden, Doppelpass am Strafraum, Video „Quick 1-2's around the box“) und
# Progression aus dem Ton (Sperre für die Flügelspieler fällt weg, „go to show, show to go“).
# Sichtkegel: Ton „get their head up and communicate to find that spare teammate“, im Video nicht eingezeichnet.
# Richtung aus dem Sinn: der Ballführer schaut vor dem Pass zum freien Mitspieler.
T = P("T", "c", 7.5, 29.5, "T")  # links an der Seitenlinie zwischen den Bereichen
ERSATZ = [B("s1", 5.5, 34), B("s2", 8, 35.5)]
POS = {"k1": (50, 5), "r2": (41.5, 10.5), "r3": (58.5, 10.5), "n9": (50, 20.5), "n10": (33, 17), "n6": (67, 17),
       "r12": (41.5, 26.5), "r13": (58.5, 26.5), "r14": (16, 24), "r15": (84, 24),
       "n11": (24.5, 33), "n7": (75.5, 33), "r16": (33, 34), "n8": (67, 34),
       "r17": (50, 36), "n5": (41.5, 43.5), "n4": (58.5, 43.5), "k2": (50, 51.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(14, 4, 72, 48), rect(21, 4, 58, 19.3), rect(37, 4, 26, 6.4), line(14, 29.5, 86, 29.5)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}, {"x": 50, "y": 52, "side": "bottom", "size": "gross"}]
DIMS = dims(14, 86, 4, 52, "50 m", "40 m", rx=93)
BT = [8.1, 30.1]  # Ball beim Trainer

u = {"title": "Sechs gegen vier, dann Konter", "code": "UE-381", "kind": "Spielform",
 "focuses": ["Umschalten", "Torschuss", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 18, "players_max": 18,
 "field_size": "50 x 40 m",
 "description": "Acht gegen acht plus zwei Torhüter auf einer Platzhälfte mit zwei Bereichen. Vorn greift Team Neon mit sechs Spielern gegen vier Verteidiger an und muss nach spätestens sechs Pässen schießen. Geht der Schuss vorbei oder kommt keiner, spielt der Trainer sofort einen Ball nach hinten, und Team Rot kontert vier gegen zwei auf das andere Tor. So wechseln Abschluss und schnelles Umschalten ständig.",
 "organisation": ["Aufbauen: Eine Platzhälfte von 50 mal 40 Metern über die volle Breite, ein großes Tor auf der Grundlinie und eins auf der Mittellinie. Eine gestrichelte Linie teilt das Feld in den Bereich für das sechs gegen vier und den Bereich für den Konter.",
  "Verteilen: Vorn greifen sechs Spieler von Team Neon gegen vier Verteidiger von Team Rot an. Die zwei Flügelspieler von Team Rot dürfen nicht mit verteidigen. Hinten warten zwei Spitzen von Team Rot gegen zwei Verteidiger von Team Neon. In jedem Tor steht ein Torwart, der Trainer steht mit vielen Bällen an der Seitenlinie.",
  "Ablauf: Der Trainer spielt ins sechs gegen vier, Team Neon hat höchstens sechs Pässe bis zum Abschluss. Geht der Schuss vorbei oder kommt keiner, spielt der Trainer einen neuen Ball nach hinten, und die vier Angreifer von Team Rot kontern gegen zwei. Erobert ein Verteidiger den Ball, spielt er ihn sofort nach vorn zu seinen Angreifern.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach spielt der Trainer wieder im sechs gegen vier an. Nach einigen Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Bewegen, bis einer frei ist", "Spätestens nach sechs Pässen schießen", "Ball erobert? Sofort nach vorn", "Kurze Doppelpässe am Strafraum"],
 "materials": ["2 große Tore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechs gegen vier, dann Konter. Vorn greift Team Neon in Überzahl an. Klappt es nicht, kontert Team Rot sofort auf der anderen Seite.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *BT)] + ERSATZ,
  "steps": [
   S("Trainer spielt ins sechs gegen vier", "Der Trainer spielt Spieler elf auf dem Flügel an. Vorn hat Team Neon jetzt sechs gegen vier, denn die Flügelspieler von Team Rot dürfen nicht mit zurück. Nach spätestens sechs Pässen muss der Schuss kommen.",
     ps("b1", [25.1, 33.6])),
   S("Andribbeln, vier gehen in den Strafraum", "Spieler elf dribbelt die Linie runter. Vier Mitspieler laufen in den Strafraum. Spieler acht bleibt hinter dem Strafraum für den zweiten Ball.",
     dr("n11", "b1", [24, 14]), mv("n10", [37, 9], delay=0.3), mv("n9", [50, 15], delay=0.3), mv("n6", [60, 6.5], delay=0.3),
     mv("n7", [70, 17], delay=0.3), mv("n8", [52, 30], delay=0.3), mv("r12", [36, 23], delay=0.5)),
   S("Kopf hoch, Flanke, knapp vorbei", "Spieler elf nimmt den Kopf hoch und sieht Spieler neun in der Mitte. Flanke, Spieler neun schießt direkt, knapp vorbei. Ein Treffer hätte einen Punkt für Team Neon gegeben.",
     bl("n11", [44, 14.8]), ps("b1", [50.6, 15.6], after=True), ps("b1", [58.5, 2.5], after=True)),
   S("Kein Treffer, der Konter läuft", "Kein Treffer, also spielt der Trainer sofort nach hinten zu Spieler sechzehn. Jetzt kontert Team Rot vier gegen zwei. Die beiden Flügelspieler sprinten mit nach vorn.",
     ps("b2", [33.6, 34.6]), dr("r16", "b2", [37, 40], after=True), mv("r14", [24, 44], delay=0.4), mv("r15", [74, 44], delay=0.4)),
   S("Vier gegen zwei: Punkt", "Spieler sechzehn spielt in die Mitte zu Spieler siebzehn. Spieler fünf geht drauf, also legt Spieler siebzehn raus auf Spieler fünfzehn. Der schießt aus vollem Lauf, und das gibt einen Punkt für Team Rot. Danach spielt der Trainer wieder im sechs gegen vier an.",
     ps("b2", [50.6, 36.6]), mv("n5", [46, 39.5], delay=0.2), ps("b2", [74.6, 44.6], after=True), ps("b2", [54, 51.7], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den freien Mitspieler finden.", "Den freien Mann finden",
    "Sechs gegen vier heißt, zwei sind immer frei. Der Ballführer nimmt den Kopf hoch und sucht sie. Die anderen bewegen sich so, dass ein Verteidiger rausmuss und hinter ihm Platz entsteht. Rund um den Strafraum hilft ein schneller Doppelpass.",
    sp(), [B("b1", 67.6, 34.6)] + ERSATZ,
    [S("Kopf hoch, wer ist frei?", "Spieler acht dribbelt an. Spieler dreizehn muss raus und geht auf ihn drauf. Damit ist Spieler sechs frei. Spieler acht schaut hoch, sieht ihn und spielt.",
       dr("n8", "b1", [62, 31]), mv("r13", [59.5, 28], delay=0.3), bl("n8", [67, 17], after=True), ps("b1", [67.6, 17.6], after=True)),
     S("Doppelpass am Strafraum", "Spieler sechs spielt direkt in die Mitte zu Spieler neun und startet sofort in den Strafraum. Spieler neun lässt den Ball mit einem Kontakt in seinen Lauf prallen.",
       ps("b1", [50.6, 21.1]), mv("n6", [64, 10], delay=0.3), ps("b1", [64.6, 10.6], after=True)),
     S("Abschluss: Punkt", "Spieler sechs schießt flach ins kurze Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball ins sechs gegen vier.",
       ps("b1", [55, 4.3]))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Die Flügelspieler von Team Rot verteidigen mit.", "Flügel verteidigen jetzt mit",
    "Die Sperre fällt weg. Die Flügelspieler von Team Rot dürfen zurück, es steht sechs gegen sechs. Jetzt müssen die Angreifer ihre Verteidiger bewegen. Erst kurz zum Ball kommen, dann in die Tiefe starten, und die Lücke ist offen.",
    sp(), [B("b1", *BT)] + ERSATZ,
    [S("Die Flügel laufen mit zurück", "Der Trainer spielt Spieler elf an. Sofort laufen beide Flügelspieler von Team Rot mit zurück. Spieler vierzehn stellt Spieler elf.",
       ps("b1", [25.1, 33.6]), mv("r14", [21, 27.5], delay=0.3), mv("r15", [79.5, 20], delay=0.3)),
     S("Kurz zeigen, dann in die Tiefe", "Spieler neun kommt kurz zum Ball, und Spieler zwölf geht mit. Dann dreht Spieler neun ab und startet in die Tiefe. Spieler elf schaut hoch und spielt in den Lauf.",
       mv("n9", [46, 24.5]), mv("r12", [43, 23.5], delay=0.3), mv("n9", [51, 12], after=True), bl("n11", [42, 19], after=True),
       ps("b1", [51.6, 12.6], after=True)),
     S("Allein vor dem Torwart: Punkt", "Spieler neun ist durch und schiebt am Torwart vorbei ins Eck, und das gibt einen Punkt für Team Neon. Danach geht es weiter wie gehabt.",
       ps("b1", [45.5, 4.3]))], dims=DIMS)]}
u["board"]["balls"].append(B("b2", 5.8, 31))
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
