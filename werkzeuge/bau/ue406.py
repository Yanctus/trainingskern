import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 81-P3 (U15-U17, Woche 38 Phase 4): Winning the 1st/2nd Ball (Ordner „Winning the 1st2nd Ball 81-P3“). 20 x 30 Yards =
# 18 x 27 m (gerundet 18 x 25 m). LANGES FELD QUER (Verhältnis 1,5, Vorbild ue317.py): Im PDF hochkant, hier liegt die Länge
# waagrecht, Feld x 9-89, y 4-51. Umgerechnet: PDF unten -> links, oben -> rechts, PDF links -> oben, PDF rechts -> unten.
# Die vier Minitore stehen wie im PDF im Feld, zwei auf jeder Seite, Öffnung zur Mitte. Drei Spalten mit je zwei Paaren
# (quer jetzt drei Reihen): das Werferpaar an der einen Seite, das Paar, das um den Ball kämpft, gegenüber.
# Gelb -> Team Neon (Nummern wie im PDF: 5, 7, 11, 2, 9, 10), Rot -> Team Rot. Rot neu nummeriert, weil die Nummern doppelt
# sind: Rot 10 -> 3, Rot 5 -> 12, Rot 11 -> 13 (Rot 6, 8, 4 bleiben). Ein Trainer, unten an der Seitenlinie (im PDF links
# daneben, also quer oben); er hat nur die Ersatzbälle. Werfer und Partner stehen quer hintereinander (3D-Abstand), der vordere
# Spieler des Kampfpaars steht etwas zur Seite versetzt (in der Mitte Werfer und Zielspieler), damit der hohe Ball auf der Tafel
# nicht durch ihn hindurchgeht.
# Ablauf nach PDF, Ton und Video: Der Werfer wirft den Ball hoch zum Paar gegenüber, beide kämpfen darum, das Werferpaar
# kommt sofort zur Unterstützung. Das Team des Werfers spielt auf das Minitor auf der Seite des Werfers, das andere Team auf
# das Minitor gegenüber. In der Mitte sagt der Trainer, auf welche zwei Minitore gespielt wird. Danach tauschen die Paare die
# Plätze (im Video gehen Kämpfer und Werfer jeweils auf die andere Seite).
# Fassung 1 = PDF Key Coaching Point 2 / Ton („supporting players must be sharp, reacting quickly to knockdowns or second
# balls“), gezeigt in der Mitte. Fassung 2 = PDF Progression und Ton (Mittelzone, nur ein Verteidiger darf hinein; Doppelpass
# oder Dribbling zum Abschluss). Mittelzone wie im Video als zwei gestrichelte Linien.
# Sichtkegel aus dem Text („must look to combine with the teammate“), im Video nicht eingezeichnet: Spieler fünf schaut nach
# der Ballsicherung zu Spieler sieben, bevor er ihn anspielt.
# Keine Dublette: UE-188 (81-P6) ist ein 5 gegen 5 mit Torhütern, in das der Trainer die Bälle spielt.
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def richt(a, b, d=20):
    l = math.dist(a, b)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n5": (82, 8), "r3": (73.5, 12), "n7": (23.5, 8), "r6": (14.5, 8),
       "r12": (82, 24), "n11": (73.5, 28.4), "r13": (23.5, 24), "n2": (14.5, 28.4),
       "n9": (82, 47), "r8": (73.5, 44), "n10": (23.5, 47), "r4": (14.5, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b1", *fu(POS["n7"])), B("b2", *fu(POS["r13"])), B("b3", *fu(POS["n10"]))] + ERSATZ
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
ZONE = [line(39, FY0, 39, FY1), line(61, FY0, 61, FY1)]
GL, GR, GO, GU = 21, 78, 18, 39  # Minitore: links/rechts im Feld, Reihe oben/unten
TORE = [{"x": GL, "y": GO, "side": "left"}, {"x": GL, "y": GU, "side": "left"},
        {"x": GR, "y": GO, "side": "right"}, {"x": GR, "y": GU, "side": "right"}]
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "18 m", rx=95)
SIEBEN = (52, 14)    # dorthin kommt Spieler sieben zur Unterstützung
LAUF5 = (43, 25)     # Spieler fünf läuft nach seinem Pass in den freien Raum

u = {"title": "Erster Ball, zweiter Ball", "code": "UE-406", "kind": "Spielform",
 "focuses": ["Ballannahme", "Umschalten", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "18 x 25 m",
 "description": "Zwei gegen zwei um hohe Bälle. Ein Spieler wirft oder schießt den Ball hoch zu zwei Spielern gegenüber, einer von Team Neon, einer von Team Rot. Die beiden kämpfen um den ersten Ball, der Werfer und sein Gegenspieler kommen sofort dazu und holen sich den zweiten Ball. Wer den Ball hat, kombiniert schnell und schließt auf ein Minitor ab.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern. Auf jeder Seite stehen zwei Minitore im Feld, die Öffnung zeigt zur Mitte.",
  "Verteilen: Zwölf Spieler in Paaren, immer einer von Team Neon und einer von Team Rot. Auf jeder Seite stehen drei Paare, gegenüber vom Werferpaar steht das Paar, das um den Ball kämpft. Die Werfer haben die Bälle, der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Der Werfer wirft oder schießt den Ball hoch zum Paar gegenüber. Beide kämpfen um den Ball, der Werfer und sein Gegenspieler sprinten sofort zur Unterstützung. Das Team des Werfers spielt auf das Minitor auf seiner Seite, das andere Team auf das Minitor gegenüber. In der Mitte sagt der Trainer vorher, auf welche zwei Minitore gespielt wird.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach tauschen die beiden Paare die Plätze, und das nächste Paar ist dran."],
 "organisation_show": ORG,
 "coaching_points": ["Entschlossen zum ersten Ball gehen", "Körper zwischen Ball und Gegner", "Sofort auf den zweiten Ball reagieren", "Ruhig bleiben, kombinieren, dann abschließen"],
 "materials": ["4 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Erster Ball, zweiter Ball. Ein hoher Ball, zwei Spieler kämpfen darum, und zwei kommen von hinten dazu. Wer den Ball hat, spielt schnell aufs Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BAELLE,
  "steps": [
   S("Hoher Ball zu Spieler fünf", "Spieler sieben wirft den Ball hoch über das Feld. Drüben gehen Spieler fünf und Spieler drei beide zum Ball.",
     ps("b1", [79.6, 8.6]), mv("n5", [79, 8], delay=0.6), mv("r3", [70.5, 10], delay=0.6)),
   S("Ball sichern, zwei kommen dazu", "Spieler fünf setzt sich durch und schirmt den Ball mit dem Körper ab. Jetzt sprinten Spieler sieben und Spieler sechs nach vorn.",
     mv("n7", list(SIEBEN)), mv("r6", [43, 6], delay=0.3)),
   S("Zusammenspiel mit Spieler sieben", "Spieler fünf sucht seinen Mitspieler und spielt zu Spieler sieben. Sofort läuft er los in den freien Raum.",
     bl("n5", richt((79, 8), SIEBEN)), ps("b1", fu(SIEBEN), after=True), mv("n5", [62, 19], after=True), mv("n5", list(LAUF5), after=True),
     mv("r3", [60, 14], delay=0.6)),
   S("Abschluss: Punkt", "Spieler sieben spielt den Ball in den Lauf. Spieler fünf schießt ins Minitor auf der Seite von Spieler sieben, und das gibt einen Punkt für Team Neon. Danach tauschen die Paare die Plätze, und in der Mitte wirft Spieler dreizehn.",
     ps("b1", fu(LAUF5)), ps("b1", [GL + 0.4, GO + 0.6], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnell auf den zweiten Ball.", "Schnell auf den zweiten Ball",
    "Der erste Ball wird selten sauber angenommen. Er springt weg, wird verlängert oder weggeköpft. Wer dann zuerst da ist, hat den Ball. Die beiden, die von hinten kommen, laufen deshalb nicht zum Ball, sondern dahin, wo er hinfällt.",
    sp(), BAELLE,
    [S("Trainer ruft, hoher Ball", "Der Trainer sagt, auf welche Minitore die Mitte spielt. Spieler dreizehn wirft hoch zu Spieler zwölf und Spieler elf. Spieler zwei und Spieler dreizehn sprinten sofort hinterher.",
       ps("b2", [79.6, 24.6]), mv("r12", [79, 24], delay=0.6), mv("n2", [50, 24], delay=0.3), mv("r13", [41, 32], delay=0.5)),
     S("Der zweite Ball", "Spieler zwölf köpft den Ball, aber er springt weg in die Mitte. Spieler zwei ist am schnellsten da und holt ihn sich.",
       ps("b2", [60.6, 24.6]), mv("n2", [60, 24], delay=0.2), mv("r13", [50, 30], delay=0.4)),
     S("Gegenüber abschließen: Punkt", "Jetzt hat Team Neon den Ball und spielt auf das Minitor gegenüber. Spieler elf bietet sich an, bekommt den Pass und trifft, und das gibt einen Punkt für Team Neon.",
       mv("n11", [67, 34]), ps("b2", [67.6, 34.6], delay=0.4), ps("b2", [GR - 0.4, GU + 0.6], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: In der Mittelzone darf nur ein Verteidiger sein.", "Nur ein Verteidiger mittig",
    "In der Mitte liegt eine Zone, in die immer nur ein Verteidiger darf. Die Angreifer kommen deshalb früh hinein und spielen dort zwei gegen eins. Zum Abschluss kommen sie nur mit einem Doppelpass oder einem Dribbling am Gegner vorbei.",
    sp(), BAELLE,
    [S("Ball hoch, Spieler sieben kommt früh", "Spieler sieben wirft hoch, und Spieler fünf sichert den Ball. Spieler sieben sprintet sofort in die Mittelzone. Spieler sechs muss draußen bleiben, denn Spieler drei geht mit hinein.",
       ps("b1", fu(POS["n5"])), mv("n7", [50, 26], delay=0.3), mv("r6", [35, 6], delay=0.5)),
     S("Zwei gegen eins in der Zone", "Spieler fünf dribbelt in die Zone. Spieler drei stellt sich ihm in den Weg, und jetzt steht es zwei gegen eins.",
       dr("n5", "b1", [72, 15]), dr("n5", "b1", [60, 13], after=True), mv("r3", [51.5, 9], delay=0.3)),
     S("Doppelpass vorbei: Punkt", "Spieler fünf spielt zu Spieler sieben und läuft an Spieler drei vorbei. Der Ball kommt direkt zurück in den Lauf. Spieler fünf trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 26.6]), mv("n5", [53, 15.5], delay=0.2), mv("n5", [42, 16], after=True), ps("b1", [42.6, 16.6], after=True),
       ps("b1", [GL + 0.4, GO + 0.6], after=True))], lines=LINES + ZONE, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
