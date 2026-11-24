import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 85-P8 (U15-U17, Woche 11): Three Phases of Attacks (Opposed Skill). 15 x 15 Yards = 14 x 14 m, Feld x 22-70, y 8-52.
# Ausrichtung wie im PDF: je zwei Minitore oben und unten. PDF blau -> Team Neon (greift nach oben an), pink -> Team Rot
# (greift nach unten an). Nur die aktive Achtergruppe gezeichnet, die zweite Gruppe wartet und steht nur im Text (3D-Abstand).
# Nummern: Neon 9, 5, 7, 11 wie im PDF; Rot neu, weil 9 doppelt ist: pink 9 -> 2, dazu 4, 10, 6 wie im PDF.
# Trainer rechts neben das Feld gerückt (im PDF an der rechten Linie zwischen den Außenspielern).
# Phase eins: Beide dribbeln zur Mitte, lassen den Ball liegen, tippen ihren Verteidiger an (oben bzw. unten), holen den Ball
# und spielen eins gegen eins. Phase zwei: Eckspieler dribbeln mit zwei Bällen ein. Phase drei: Ball vom Trainer, zwei
# Außenspieler kommen dazu, vier gegen vier. "Finish in either mini goal": Neon auf die zwei oberen, Rot auf die zwei unteren.
# Kein Dubletten-Fall: UE-245 (Drei Muster zum Abschluss) ist eine Abschlussübung mit Puppen und einem Tor mit Torwart.
# Sichtkegel: im Video nicht eingezeichnet; Ton zu Phase drei "this phase demands awareness, communication": Spieler fünf
# schaut erst zum Trainer (Ball kommt), nach der Annahme zum einlaufenden Außenspieler.
T = P("T", "c", 84, 30, "T")
ERSATZ = [B("s1", 87.6, 33.5), B("s2", 84, 33.5)]
POS = {"n9": (17, 22), "n5": (46, 55), "n7": (22, 55), "n11": (75, 22), "r2": (17, 38), "r4": (46, 5), "r10": (70, 5), "r6": (75, 38)}
BALL = {"b1": (17.6, 22.6), "b2": (17.6, 38.6), "b3": (22.6, 55.6), "b4": (70.6, 5.6), "b5": (84.6, 30.6)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def baelle(**k):
    d = dict(BALL); d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(22, 8, 48, 44)]
TORE = [{"x": 34.5, "y": 8, "side": "top"}, {"x": 57.5, "y": 8, "side": "top"}, {"x": 34.5, "y": 52, "side": "bottom"}, {"x": 57.5, "y": 52, "side": "bottom"}]
DIMS = dims(22, 70, 8, 52, "14 m", "14 m", rx=94)

u = {"title": "Vom 1 gegen 1 zum 4 gegen 4", "code": "UE-306", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 16,
 "field_size": "14 x 14 m",
 "description": "Drei Phasen gehen ohne Pause ineinander über. Es beginnt mit zwei Duellen eins gegen eins. Dann dribbeln zwei Eckspieler mit je einem Ball ein, und es läuft drei gegen drei mit zwei Bällen. Zum Schluss spielt der Trainer einen Ball ein, zwei weitere Spieler kommen dazu, und es wird vier gegen vier auf vier Minitore gespielt.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern. Oben und unten stehen je zwei Minitore.",
  "Verteilen: Zwei Teams, aufgeteilt in zwei Gruppen zu je acht Spielern, vier von jedem Team. Links startet von jedem Team ein Spieler mit Ball. Oben und unten wartet je ein Verteidiger, in zwei Ecken ein Spieler mit Ball, rechts von jedem Team ein Außenspieler. Der Trainer steht rechts mit Bällen. Die zweite Gruppe wartet neben dem Feld.",
  "Ablauf: Phase eins, zur Mitte dribbeln, Ball liegen lassen, den Verteidiger antippen, Ball holen und eins gegen eins abschließen. Phase zwei, die Eckspieler dribbeln mit zwei Bällen ein, drei gegen drei. Phase drei, der Trainer spielt einen Ball ein, die Außenspieler kommen dazu, vier gegen vier.",
  "Wertung und Wechsel: Team Neon greift die oberen Minitore an, Team Rot die unteren. Jeder Treffer gibt einen Punkt. Nach Phase drei kommt die zweite Achtergruppe und beginnt wieder mit Phase eins."],
 "organisation_show": ORG,
 "coaching_points": ["Im eins gegen eins antäuschen und dann Tempo", "Außen wach sein, die nächste Phase startet sofort", "Schnell angreifen, bevor der Gegner steht", "Auch ohne Ball sofort nach hinten arbeiten"],
 "materials": ["4 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Vom eins gegen eins zum vier gegen vier. Drei Phasen ohne Pause, und in jeder kommen neue Spieler und neue Bälle dazu.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": baelle(),
  "steps": [
   S("Phase eins: Ball in die Mitte", "Links starten Spieler neun und Spieler zwei gleichzeitig. Beide dribbeln zur Mitte und lassen den Ball dort liegen.",
     dr("n9", "b1", [41.5, 27]), dr("r2", "b2", [50.5, 33])),
   S("Verteidiger antippen", "Ohne Ball geht es weiter. Spieler neun sprintet nach oben und tippt Spieler vier an. Spieler zwei läuft nach unten zu Spieler fünf. Damit sind die Verteidiger im Spiel.",
     mv("n9", [43.5, 10.5]), mv("r2", [48.5, 49.5])),
   S("Zurück zum Ball, eins gegen eins", "Schnell zurück zum Ball, der Verteidiger kommt schon hinterher. Spieler neun nimmt den Ball mit, zieht rechts an Spieler vier vorbei und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Unten trifft Spieler zwei genauso gegen Spieler fünf, das gibt einen Punkt für Team Rot.",
     mv("n9", [41.5, 27]), mv("r4", [45, 17], delay=0.4), dr("n9", "b1", [54, 22], after=True), ps("b1", [57.5, 8.3], after=True),
     mv("r2", [50.5, 33]), mv("n5", [47, 43], delay=0.4), dr("r2", "b2", [58, 40], after=True), ps("b2", [57.5, 51.7], after=True)),
   S("Phase zwei: zwei Bälle im Feld", "Sofort kommen die Eckspieler. Spieler sieben dribbelt von links unten ein, Spieler zehn von rechts oben. Jetzt läuft drei gegen drei mit zwei Bällen. Spieler sieben spielt steil auf Spieler neun, und der schließt oben links ab. Auch Team Rot greift mit seinem Ball an.",
     dr("n7", "b3", [30, 36]), dr("r10", "b4", [63, 20]), mv("n9", [38, 22], delay=0.2), mv("n5", [44, 34], delay=0.3), mv("r4", [41, 13], delay=0.5),
     ps("b3", [38.6, 22.6], after=True), ps("b3", [34.5, 8.3], after=True)),
   S("Phase drei: Ball vom Trainer", "Der Trainer entscheidet, wer den dritten Ball bekommt. Er spielt zu Spieler fünf. Von rechts kommen Spieler elf und Spieler sechs dazu. Jetzt ist es vier gegen vier.",
     bl("n5", [66, 32]), ps("b5", [44.6, 34.6], after=True), mv("n11", [60, 26], delay=0.3), mv("r6", [66, 41], delay=0.3), mv("n9", [50, 14], delay=0.6)),
   S("Vier gegen vier: Punkt", "Spieler fünf hebt den Kopf und findet Spieler elf. Der spielt sofort steil. Spieler neun trifft oben rechts, und das gibt einen Punkt für Team Neon. Danach gehen alle acht raus, und die zweite Gruppe beginnt wieder mit Phase eins.",
     bl("n5", [60, 26], von=[66, 32], dauer=1.3), ps("b5", [60.6, 26.6], after=True), ps("b5", [50.6, 14.6], after=True), ps("b5", [57.5, 8.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Antäuschen, dann vorbei.", "Antäuschen, dann vorbei",
    "Im eins gegen eins geht der Angreifer mit Tempo auf den Verteidiger zu. Eine Körpertäuschung zur einen Seite, dann mit dem ersten schnellen Kontakt zur anderen. Wer wartet, bis der Verteidiger steht, hat es schwer.",
    sp(n9=(41.5, 27), r4=(44.5, 11), r2=(50.5, 33), n5=(47, 49)), baelle(b1=(42.1, 27.6), b2=(51.1, 33.6)),
    [S("Auf den Verteidiger zu, antäuschen", "Spieler neun dribbelt direkt auf Spieler vier zu. Kurz vor ihm täuscht er mit dem Oberkörper nach links an. Spieler vier macht den Schritt mit.",
       dr("n9", "b1", [41, 20]), mv("r4", [41.5, 14.5], delay=0.2), mv("r4", [37.5, 15.5], after=True)),
     S("Rechts vorbei: Punkt", "Ein schneller Kontakt nach rechts, und Spieler neun ist vorbei. Er schiebt ins rechte Minitor ein, und das gibt einen Punkt für Team Neon.",
       dr("n9", "b1", [49, 16]), mv("r4", [43, 14], delay=0.4), ps("b1", [57.5, 8.3], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Außen wach bleiben.", "Außen wach bleiben",
    "Die nächste Phase beginnt in dem Moment, in dem die alte endet. Wer außen wartet, schaut zu und startet sofort. Dann sind die Verteidiger noch nicht sortiert, und der Angriff hat Platz.",
    sp(n9=(54, 22), r4=(45, 17), r2=(58, 40), n5=(47, 43)), baelle(b1=(57.5, 8.3), b2=(57.5, 51.7)),
    [S("Schuss gefallen, sofort rein", "Der Ball aus Phase eins liegt im Tor. Spieler sieben dribbelt schon los, bevor sich Team Rot umgedreht hat. Spieler neun löst sich nach links und bietet sich an.",
       dr("n7", "b3", [30, 36]), mv("n9", [38, 22], delay=0.2), dr("r10", "b4", [63, 20], delay=0.5)),
     S("Schnell gespielt: Punkt", "Der Pass kommt steil, Spieler vier ist noch zu weit weg. Spieler neun trifft oben links, und das gibt einen Punkt für Team Neon.",
       ps("b3", [38.6, 22.6]), mv("r4", [42, 18], delay=0.3), ps("b3", [34.5, 8.3], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
