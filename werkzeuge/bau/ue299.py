import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-27 (U15-U17, Woche 1 Pre-Season): Dribbling, Shuttle Runs & 3 v 3 Game. 20 x 45 Yards = 18 x 41 m, hochkant wie im PDF:
# unten der Pendelbereich mit drei Reihen zu je fünf Hütchen, oben die Spielzone mit Minitoren links und rechts (wie im PDF,
# darum wird quer gespielt und nicht nach oben). Feld x 25-75, y 5-55: in der Breite gestreckt (18 m auf 50 Einheiten), damit
# sechs Spieler nebeneinander den 3D-Abstand halten. Trainer rechts neben der Spielzone statt oben (oben kein Platz auf der Tafel).
# Video gold / PDF pink -> Team Neon (6, 8, 10; gold 4 -> 8, weil die 4 doppelt ist), blau -> Team Rot (9, 4, 7).
# Ablauf nach PDF-Text und Skizze: Ball zu jeder Hütchenreihe dribbeln, liegen lassen, zurück zur Grundlinie sprinten.
# Im Video dribbeln die Spieler den Ball am Ende zurück zur Grundlinie; hier bleibt er an der dritten Reihe liegen.
# Fassungen: PDF Key Coaching Point 1 (erst alle drei in der Zone, dann der Ball; hier ist Team Rot zuerst komplett) und
# Key Coaching Point 2 (schnell kombinieren, beim Stand von eins zu eins entscheidet der nächste Treffer).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 82, 10, "T")
ERSATZ = [B("s1", 85.6, 13.5), B("s2", 82, 13.5)]
BT = [82.6, 10.6]
X = {"r9": 29, "n6": 37.4, "r4": 45.8, "n8": 54.2, "r7": 62.6, "n10": 71}
NEON, ROT = ["n6", "n8", "n10"], ["r9", "r4", "r7"]
Y0, R1, R2, R3 = 53, 46, 39, 32
def sp(**k):
    d = {i: (x, Y0) for i, x in X.items()}; d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def baelle(y): return [B("b" + i[1:], x + 0.6, y + 0.6) for i, x in X.items()]
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
TORE = [{"x": 25, "y": 17.5, "side": "left"}, {"x": 75, "y": 17.5, "side": "right"}]
CONES = [C(x, y) for y in (R1, R2, R3) for x in (33.2, 41.6, 50, 58.4, 66.8)]
DIMS = dims(25, 75, 5, 55, "18 m", "41 m", rx=93)
# Sprint in die Spielzone: links am eigenen, liegen gebliebenen Ball vorbei
def um(i, x, y, **k): return [mv(i, [x - 3, R3 + 2], **k), mv(i, [x - 3, R3 - 2], after=True), mv(i, [x, y], after=True)]
def alle(f, wer=None, **k): return [m for i in (wer or X) for m in f(i, X[i], **k)]

u = {"title": "Pendeln mit Ball ins 3 gegen 3", "code": "UE-299", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 6, "players_max": 6,
 "field_size": "18 x 41 m",
 "description": "Zwei Teams zu dritt pendeln zuerst mit Ball. Jeder dribbelt zur ersten Hütchenreihe, lässt den Ball liegen, sprintet zurück zur Grundlinie und holt ihn für die nächste Reihe wieder ab. Nach der dritten Reihe sprinten alle ohne Ball in die Spielzone. Das Team, das zuerst mit allen drei Spielern drin ist, bekommt den Ball, und es wird drei gegen drei auf zwei Minitore gespielt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 41 Metern, in der Mitte quer geteilt. Unten liegen drei Reihen mit je fünf Hütchen. Oben ist die Spielzone mit je einem Minitor links und rechts.",
  "Verteilen: Zwei Teams zu dritt. Alle sechs stehen mit Ball an der Grundlinie, abwechselnd Team Rot und Team Neon. Der Trainer steht mit Bällen neben der Spielzone.",
  "Ablauf: Auf Pfiff dribbelt jeder zur ersten Reihe, lässt den Ball liegen und sprintet zurück zur Grundlinie. Dann wieder zum Ball, weiter zur zweiten Reihe und zurück, danach genauso zur dritten Reihe. Nach dem letzten Sprint zur Grundlinie geht es ohne Ball hoch in die Spielzone. Das Team, das zuerst mit allen drei Spielern drin ist, bekommt den Ball vom Trainer.",
  "Wertung und Wechsel: Drei gegen drei. Team Neon greift das linke Minitor an, Team Rot das rechte. Jeder Treffer gibt einen Punkt, und wer zuerst zwei Punkte hat, gewinnt die Runde. Danach drei bis fünf Minuten Pause, dann startet die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Kleine Kontakte, der Ball bleibt eng am Fuß", "Ohne Ball voll sprinten und an der Linie schnell umdrehen", "Wer schon drin ist, feuert die anderen an", "Im drei gegen drei schnell spielen und den Abschluss suchen"],
 "materials": ["15 Hütchen", "2 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pendeln mit Ball ins drei gegen drei. Erst pendeln alle mit Ball, bis die Beine schwer werden. Das Team, das zuerst komplett in der Spielzone steht, bekommt den Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle(Y0) + [B("b0", *BT)] + ERSATZ,
  "steps": [
   S("Ball zur ersten Reihe", "Alle sechs starten gleichzeitig an der Grundlinie, jeder in seiner Bahn. Mit Tempo bis zur ersten Hütchenreihe dribbeln, den Ball stoppen und liegen lassen.",
     *alle(lambda i, x: [dr(i, "b" + i[1:], [x, R1])])),
   S("Zurück zur Linie, wieder zum Ball", "Ohne Ball geht es im Sprint zurück zur Grundlinie. Dort umdrehen und sofort wieder vor zum Ball.",
     *alle(lambda i, x: [mv(i, [x, Y0]), mv(i, [x, R1], after=True)])),
   S("Weiter zur zweiten Reihe", "Jetzt nimmt jeder seinen Ball mit bis zur zweiten Reihe. Ball stoppen, und wieder zurück zur Grundlinie.",
     *alle(lambda i, x: [dr(i, "b" + i[1:], [x, R2]), mv(i, [x, Y0], after=True)])),
   S("Dritte Reihe, Neon liegt vorn", "Das Gleiche noch einmal bis zur dritten Reihe, dort bleibt der Ball liegen. Team Neon ist schon wieder an der Grundlinie. Team Rot legt den Ball gerade erst ab.",
     *alle(lambda i, x: [mv(i, [x, R2]), dr(i, "b" + i[1:], [x, R3], after=True), mv(i, [x, Y0], after=True)], NEON),
     *alle(lambda i, x: [mv(i, [x, R2], delay=0.5), dr(i, "b" + i[1:], [x, R3], after=True)], ROT)),
   S("Team Neon ist zuerst komplett", "Von der Grundlinie sprintet Team Neon durch bis in die Spielzone. Alle drei sind drin, Spieler vier fehlt bei Team Rot noch. Also spielt der Trainer den Ball zu Spieler acht.",
     *um("n6", 37.4, 22), *um("n8", 54.2, 10), *um("n10", 71, 24),
     mv("r9", [29, Y0]), *um("r9", 29, 10, after=True), mv("r7", [62.6, Y0]), *um("r7", 62.6, 20, after=True),
     mv("r4", [45.8, Y0], delay=0.4), mv("r4", [45.8, 41], after=True), ps("b0", [54.8, 10.6], after=True)),
   S("Drei gegen drei: Punkt", "Jetzt läuft das drei gegen drei auf die Minitore. Spieler acht spielt zu Spieler sechs. Der geht noch ein Stück aufs linke Minitor zu und trifft, und das gibt einen Punkt für Team Neon. Der Trainer bringt sofort den nächsten Ball. Wer zuerst zwei Punkte hat, gewinnt die Runde.",
     ps("b0", [38, 22.6]), *um("r4", 45.8, 25), dr("n6", "b0", [37.4, 18.5], after=True), ps("b0", [24.7, 17.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Alle drei müssen drin sein.", "Alle drei müssen drin sein",
    "Zwei schnelle Spieler in der Zone bringen noch nichts. Der Trainer spielt den Ball erst, wenn ein Team komplett drin ist. Wer schon oben steht, feuert den Letzten an.",
    sp(n6=(37.4, 22), n10=(71, 24), r9=(29, 10), r7=(62.6, 12), r4=(45.8, 41)), baelle(R3) + [B("b0", *BT)] + ERSATZ,
    [S("Zwei reichen nicht", "Spieler sechs und Spieler zehn stehen schon in der Spielzone. Spieler acht läuft aber erst an der Grundlinie los. Der Ball bleibt beim Trainer, und Spieler vier zieht vorbei.",
       mv("n8", [54.2, 42]), *um("r4", 45.8, 25)),
     S("Team Rot ist komplett", "Team Rot ist jetzt mit allen drei drin. Der Trainer spielt den Ball zu Spieler sieben, und Team Rot greift das rechte Minitor an. Spieler acht kommt zu spät.",
       ps("b0", [63.2, 12.6]), *um("n8", 54.2, 28))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell kombinieren.", "Schnell kombinieren",
    "Es steht eins zu eins, der nächste Treffer entscheidet. Mit müden Beinen hilft kein langes Dribbling. Abspielen, in den freien Raum starten und den Ball dort wieder bekommen.",
    sp(n10=(50, 9), n8=(47, 28.5), n6=(71, 22), r4=(41.5, 13), r7=(60, 24), r9=(33, 28)), baelle(R3) + [B("b0", 50.6, 9.6)] + ERSATZ,
    [S("Abspielen und starten", "Spieler zehn hat den Ball, und Spieler vier steht vor ihm. Kurzer Pass zu Spieler acht. Sofort startet Spieler zehn hinter Spieler vier vorbei in den freien Raum.",
       ps("b0", [47.6, 29.1]), mv("n10", [41.5, 5.8], delay=0.2), mv("n10", [30, 12], after=True)),
     S("In den Lauf: Punkt", "Spieler acht spielt den Ball direkt in den Lauf. Spieler zehn trifft ins linke Minitor, und das gibt einen Punkt für Team Neon. Damit gewinnt Team Neon die Runde.",
       ps("b0", [30.6, 12.6]), mv("r4", [38.5, 11], delay=0.2), ps("b0", [24.7, 17.5], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
