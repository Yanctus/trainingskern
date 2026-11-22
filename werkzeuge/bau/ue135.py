import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-79 (U12-U14, Woche 3 Pre-Season): Develop Fitness with 2 v 2 Games (2 v 2 Competition). 20 x 30 Yards hochkant
# = Feld x 33.3-66.7, y 5-55 (18 x 27 m), drei Zonen übereinander (Liga 1 oben, 2 Mitte, 3 unten), je Zone ein Minitor links und rechts.
# Sechs Paare in eigenen Farben -> je Zone Neon gegen Rot (Neon spielt nach rechts), Nummern 2-13. Ein Trainer statt zwei.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 24, 30, "T")
POS = {"n2": (38, 11), "n3": (46.5, 15.5), "r8": (55, 11), "r9": (63.5, 15.5),
       "n4": (38, 27.7), "n5": (46.5, 32.2), "r10": (55, 27.7), "r11": (63.5, 32.2),
       "n6": (38, 44.4), "n7": (46.5, 48.9), "r12": (55, 44.4), "r13": (63.5, 48.9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 25.6, 33.6), B("s2", 22, 34)]
BAELLE = [B("b1", 38.6, 11.6), B("b2", 55.6, 28.3), B("b3", 38.6, 45)] + ERSATZ
LINES = [rect(33.3, 5, 33.4, 50), line(33.3, 21.7, 66.7, 21.7), line(33.3, 38.3, 66.7, 38.3)]
TORE = [{"x": 33.3, "y": y, "side": "left"} for y in (13.3, 30, 46.7)] + [{"x": 66.7, "y": y, "side": "right"} for y in (13.3, 30, 46.7)]

u = {"title": "2 gegen 2 mit Auf- und Abstieg", "code": "UE-135", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "1 gegen 1", "Kondition"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "18 x 27 m",
 "description": "Drei Spiele zwei gegen zwei laufen gleichzeitig in drei Zonen übereinander, jede Zone hat ein Minitor links und rechts. Die oberste Zone ist die erste Liga, dann die zweite und die dritte. Nach drei Minuten wird abgerechnet: Das Siegerpaar steigt eine Zone auf, das Verliererpaar steigt ab. Bei Gleichstand entscheidet ein schnelles eins gegen eins. Wer nach acht bis zehn Spielen am häufigsten in der ersten Liga gewonnen hat, ist Meister.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern, quer in drei gleiche Zonen geteilt. Jede Zone hat links und rechts ein Minitor. Oben ist die erste Liga, in der Mitte die zweite, unten die dritte.",
  "Verteilen: Sechs Paare, in jeder Zone spielen zwei Paare gegeneinander. Der Trainer steht mit vielen Bällen am Rand und spielt sofort einen neuen Ball ein.",
  "Ablauf: Alle drei Spiele laufen drei Minuten lang gleichzeitig. Dann gewinnt das Paar mit den meisten Toren und steigt auf, der Verlierer steigt ab. Oben bleibt der Sieger oben, unten bleibt der Verlierer unten.",
  "Gleichstand: Ein Münzwurf entscheidet, wer anfängt, dann gibt es ein schnelles eins gegen eins. Wer trifft, bleibt. Fällt kein Tor, verliert das Paar, das schon vorher in dieser Zone war."],
 "organisation_show": ORG,
 "coaching_points": ["Mit schnellen Doppelpässen durch die Abwehr", "Viel miteinander sprechen", "Den Gegner im Dribbling ausspielen und so ein zwei gegen eins schaffen", "Chancen eiskalt nutzen und die Angriffe abwechseln, mal schnell, mal geduldig"],
 "materials": ["6 Minitore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in mehreren Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Zwei gegen zwei mit Auf- und Abstieg. Drei Spiele laufen gleichzeitig, und nach jeder Runde steigt der Sieger auf und der Verlierer ab.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Drei Spiele zugleich", "In allen drei Zonen wird gleichzeitig gespielt. Team Neon spielt nach rechts, Team Rot nach links. Wir schauen auf die unterste Zone.",
     dr("n2", "b1", [45, 10]), mv("r8", [51, 12], delay=0.1), dr("r10", "b2", [48, 28], delay=0.1), mv("n4", [42, 29.5], delay=0.2),
     dr("n6", "b3", [44, 43.5], delay=0.2), mv("r12", [51, 43], delay=0.3)),
   S("Doppelpass: Punkt", "Unten spielt Spieler sechs einen Doppelpass mit Spieler sieben, läuft an Spieler zwölf vorbei und trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
     ps("b3", [47.1, 49.5]), mv("n6", [51, 38.8], after=True), mv("n6", [58, 42], after=True), ps("b3", [58.6, 42.6], after=True), ps("b3", [67, 46.7], after=True)),
   S("Auf- und Abstieg", "Nach drei Minuten wird abgerechnet. Spieler sechs und Spieler sieben haben unten gewonnen und steigen eine Zone auf, das Verliererpaar aus der Mitte steigt ab. Dann beginnen sofort die nächsten Spiele.",
     mv("n6", [72, 40]), mv("n6", [72, 33], after=True), mv("n7", [56, 54], delay=0.2), mv("n7", [72, 50], after=True))],
  "dims": [{"x1": 33.3, "y1": 58.6, "x2": 66.7, "y2": 58.6, "text": "18 m"}, {"x1": 80, "y1": 5, "x2": 80, "y2": 55, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Gleichstand, also eins gegen eins.", "Entscheidung im Duell",
    "Steht es nach drei Minuten unentschieden, entscheidet ein schnelles eins gegen eins. Ein Münzwurf bestimmt, wer anfängt. Wer trifft, bleibt in der Zone. Fällt kein Tor, verliert das Paar, das schon vorher in dieser Zone war.",
    sp(n3=(28, 8), r9=(72, 8)), [B("b1", 38.6, 11.6), B("b2", 55.6, 28.3), B("b3", 38.6, 45)] + ERSATZ,
    [S("Eins gegen eins", "Oben steht es unentschieden. Spieler zwei hat den Münzwurf gewonnen und dribbelt los, Spieler acht kommt ihm entgegen.",
       dr("n2", "b1", [47, 12]), mv("r8", [51, 15], delay=0.1)),
     S("Wer trifft, bleibt: Punkt", "Spieler zwei geht an Spieler acht vorbei und trifft, und das gibt einen Punkt für Team Neon. Damit bleibt sein Paar in der ersten Liga, und Spieler acht und Spieler neun steigen ab.",
       dr("n2", "b1", [56, 9.5]), ps("b1", [67, 13.3], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ausspielen und Überzahl schaffen.", "Zwei gegen eins schaffen",
    "Wer seinen Gegenspieler im Dribbling ausspielt, macht aus dem zwei gegen zwei ein zwei gegen eins. Dann muss der zweite Verteidiger heraus, und der Mitspieler wird frei. Jetzt schnell abspielen, bevor der Erste wieder da ist.",
    sp(), [B("b1", 38.6, 11.6), B("b2", 38.6, 28.3), B("b3", 38.6, 45)] + ERSATZ,
    [S("Den Ersten ausspielen", "In der mittleren Zone dribbelt Spieler vier auf Spieler zehn zu, täuscht an und geht an ihm vorbei.",
       mv("r10", [51, 28.5]), dr("n4", "b2", [47, 25], delay=0.1), dr("n4", "b2", [55, 23.5], after=True)),
     S("Zwei gegen eins: Punkt", "Jetzt muss Spieler elf heraus. Spieler vier spielt sofort quer zu Spieler fünf, der frei ist und ins rechte Minitor trifft, und das gibt einen Punkt für Team Neon.",
       mv("r11", [59, 26]), mv("n5", [56, 33], delay=0.1), ps("b2", [56.6, 33.6], after=True), ps("b2", [67, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
