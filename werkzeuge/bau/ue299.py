import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# PS-27 (U15-U17, Woche 1 Pre-Season): Dribbling, Shuttle Runs & 3 v 3 Game. 20 x 45 Yards = 18 x 41 m (gerundet 18 x 40 m).
# FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Im PDF hochkant (unten Pendelbereich, oben Spielzone mit Minitoren links und
# rechts). R() legt die Hochkant-Planung (Feld x 25-75 = Breite, y 5-55 = Länge) quer: unten -> links, oben -> rechts,
# links -> oben, rechts -> unten. Feld quer x 9-89 (40 m), y 4-51 (18 m; in der Tiefe etwas gestreckt, damit die sechs Bahnen
# den 3D-Abstand halten). Links die Grundlinie und der Pendelbereich mit drei senkrechten Reihen zu je fünf Hütchen, rechts die
# Spielzone. Die Minitore stehen wie im PDF an den Seitenlinien der Spielzone, quer also oben (Team Neon greift an) und unten
# (Team Rot greift an). Trainer unten an der Seitenlinie neben der Spielzone.
# 3D-Abstand quer: Die sechs Spieler standen hochkant nebeneinander an der Grundlinie und stehen jetzt in der Tiefe hintereinander.
# Darum starten sie versetzt: Team Neon steht an der Grundlinie, Team Rot gut drei Meter dahinter. Zurück gesprintet wird bei
# allen bis zur Grundlinie.
# Video gold / PDF pink -> Team Neon (6, 8, 10; gold 4 -> 8, weil die 4 doppelt ist), blau -> Team Rot (9, 4, 7).
# Ablauf nach PDF-Text und Skizze: Ball zu jeder Hütchenreihe dribbeln, liegen lassen, zurück zur Grundlinie sprinten.
# Im Video dribbeln die Spieler den Ball am Ende zurück zur Grundlinie; hier bleibt er an der dritten Reihe liegen.
# Fassungen: PDF Key Coaching Point 1 (erst alle drei in der Zone, dann der Ball; hier ist Team Rot zuerst komplett) und
# Key Coaching Point 2 (schnell kombinieren, beim Stand von eins zu eins entscheidet der nächste Treffer).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 25) / 50 * (FY1 - FY0), 1)]
T = h.P("T", "c", 82, 55.3, "T")  # unten an der Seitenlinie neben der Spielzone
ERSATZ = [h.B("s1", 85.5, 55.8), h.B("s2", 88, 55.8)]
BT = [82.6, 55.9]
# Bahnen (hochkant x 29, 37.4, ..., 71) liegen quer bei y = R(x, 0)[1]; Hütchenreihen hochkant y 46, 39, 32 -> quer x
Y = {i: R(x, 0)[1] for i, x in {"r9": 29, "n6": 37.4, "r4": 45.8, "n8": 54.2, "r7": 62.6, "n10": 71}.items()}
R1, R2, R3 = (R(0, y)[0] for y in (46, 39, 32))
GL = 11  # zurück bis an die Grundlinie
X0 = {i: 13 if i[0] == "n" else 4.6 for i in Y}  # Start versetzt (3D-Abstand)
NEON, ROT = ["n6", "n8", "n10"], ["r9", "r4", "r7"]
def sp(**k):
    d = {i: (X0[i], y) for i, y in Y.items()}; d.update(k)
    return [h.P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def baelle(x=None): return [h.B("b" + i[1:], round((x or X0[i]) + 0.6, 1), round(y + 0.6, 1)) for i, y in Y.items()]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(R(0, 30)[0], FY0, R(0, 30)[0], FY1)]
GX = R(0, 17.5)[0]
TORE = [{"x": GX, "y": FY0, "side": "top"}, {"x": GX, "y": FY1, "side": "bottom"}]
CONES = [C(x, round((Y[a] + Y[b]) / 2, 1)) for x in (R1, R2, R3) for a, b in zip(list(Y)[:-1], list(Y)[1:])]
DIMS = dims(FX0, FX1, FY0, FY1, "40 m", "18 m", rx=95)
# Sprint in die Spielzone: am eigenen, liegen gebliebenen Ball vorbei (durch die Lücke zwischen den Hütchen)
def um(i, x, y, **k): return [mv(i, [round(R3 - 2, 1), round(Y[i] - 2.2, 1)], **k), mv(i, [round(R3 + 3, 1), round(Y[i] - 2.2, 1)], after=True), mv(i, [x, y], after=True)]
def alle(f, wer=None, **k): return [m for i in (wer or Y) for m in f(i, Y[i], **k)]
# Stand in der Spielzone (quer)
ZONE = {"n6": (61.8, 15.7), "n8": (81, 31.4), "n10": (58.6, 47.2), "r9": (81, 7.8), "r7": (65, 39.3)}

u = {"title": "Pendeln mit Ball ins 3 gegen 3", "code": "UE-299", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 6, "players_max": 6,
 "field_size": "18 x 40 m",
 "description": "Zwei Teams zu dritt pendeln zuerst mit Ball. Jeder dribbelt zur ersten Hütchenreihe, lässt den Ball liegen, sprintet zurück zur Grundlinie und holt ihn für die nächste Reihe wieder ab. Nach der dritten Reihe sprinten alle ohne Ball in die Spielzone. Das Team, das zuerst mit allen drei Spielern drin ist, bekommt den Ball, und es wird drei gegen drei auf zwei Minitore gespielt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 40 Metern, in der Mitte geteilt. In der ersten Hälfte liegen drei Reihen mit je fünf Hütchen. Die zweite Hälfte ist die Spielzone, dort steht an jeder Seitenlinie ein Minitor.",
  "Verteilen: Zwei Teams zu dritt. Alle sechs stehen mit Ball an der Grundlinie, abwechselnd Team Rot und Team Neon. Der Trainer steht mit Bällen neben der Spielzone.",
  "Ablauf: Auf Pfiff dribbelt jeder zur ersten Reihe, lässt den Ball liegen und sprintet zurück zur Grundlinie. Dann wieder zum Ball, weiter zur zweiten Reihe und zurück, danach genauso zur dritten Reihe. Nach dem letzten Sprint zur Grundlinie geht es ohne Ball durch bis in die Spielzone. Das Team, das zuerst mit allen drei Spielern drin ist, bekommt den Ball vom Trainer.",
  "Wertung und Wechsel: Drei gegen drei. Jedes Team greift eins der beiden Minitore an. Jeder Treffer gibt einen Punkt, und wer zuerst zwei Punkte hat, gewinnt die Runde. Danach drei bis fünf Minuten Pause, dann startet die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Kleine Kontakte, der Ball bleibt eng am Fuß", "Ohne Ball voll sprinten und an der Linie schnell umdrehen", "Wer schon drin ist, feuert die anderen an", "Im drei gegen drei schnell spielen und den Abschluss suchen"],
 "materials": ["15 Hütchen", "2 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pendeln mit Ball ins drei gegen drei. Erst pendeln alle mit Ball, bis die Beine schwer werden. Das Team, das zuerst komplett in der Spielzone steht, bekommt den Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle() + [h.B("b0", *BT)] + ERSATZ,
  "steps": [
   S("Ball zur ersten Reihe", "Alle sechs starten gleichzeitig an der Grundlinie, jeder in seiner Bahn. Mit Tempo bis zur ersten Hütchenreihe dribbeln, den Ball stoppen und liegen lassen.",
     *alle(lambda i, y: [dr(i, "b" + i[1:], [R1, y])])),
   S("Zurück zur Linie, wieder zum Ball", "Ohne Ball geht es im Sprint zurück zur Grundlinie. Dort umdrehen und sofort wieder vor zum Ball.",
     *alle(lambda i, y: [mv(i, [GL, y]), mv(i, [R1, y], after=True)])),
   S("Weiter zur zweiten Reihe", "Jetzt nimmt jeder seinen Ball mit bis zur zweiten Reihe. Ball stoppen, und wieder zurück zur Grundlinie.",
     *alle(lambda i, y: [dr(i, "b" + i[1:], [R2, y]), mv(i, [GL, y], after=True)])),
   S("Dritte Reihe, Neon liegt vorn", "Das Gleiche noch einmal bis zur dritten Reihe, dort bleibt der Ball liegen. Team Neon ist schon wieder an der Grundlinie. Team Rot legt den Ball gerade erst ab.",
     *alle(lambda i, y: [mv(i, [R2, y]), dr(i, "b" + i[1:], [R3, y], after=True), mv(i, [GL, y], after=True)], NEON),
     *alle(lambda i, y: [mv(i, [R2, y], delay=0.5), dr(i, "b" + i[1:], [R3, y], after=True)], ROT)),
   S("Team Neon ist zuerst komplett", "Von der Grundlinie sprintet Team Neon durch bis in die Spielzone. Alle drei sind drin, Spieler vier fehlt bei Team Rot noch. Also spielt der Trainer den Ball zu Spieler acht.",
     *um("n6", *ZONE["n6"]), *um("n8", *ZONE["n8"]), *um("n10", *ZONE["n10"]),
     mv("r9", [GL, Y["r9"]]), *um("r9", *ZONE["r9"], after=True), mv("r7", [GL, Y["r7"]]), *um("r7", *ZONE["r7"], after=True),
     mv("r4", [GL, Y["r4"]], delay=0.4), mv("r4", [31.4, Y["r4"]], after=True), ps("b0", [81.6, 32], after=True)),
   S("Drei gegen drei: Punkt", "Jetzt läuft das drei gegen drei auf die Minitore. Spieler acht spielt zu Spieler sechs. Der geht noch ein Stück aufs Minitor zu und trifft, und das gibt einen Punkt für Team Neon. Der Trainer bringt sofort den nächsten Ball. Wer zuerst zwei Punkte hat, gewinnt die Runde.",
     ps("b0", [62.4, 16.3]), *um("r4", 57, Y["r4"]), dr("n6", "b0", [66.5, 11], after=True), ps("b0", [GX, FY0 + 0.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Alle drei müssen drin sein.", "Alle drei müssen drin sein",
    "Zwei schnelle Spieler in der Zone bringen noch nichts. Der Trainer spielt den Ball erst, wenn ein Team komplett drin ist. Wer schon drin ist, feuert den Letzten an.",
    sp(n6=ZONE["n6"], n10=ZONE["n10"], r9=ZONE["r9"], r7=(77.8, Y["r7"]), r4=(31.4, Y["r4"])), baelle(R3) + [h.B("b0", *BT)] + ERSATZ,
    [S("Zwei reichen nicht", "Spieler sechs und Spieler zehn stehen schon in der Spielzone. Spieler acht läuft aber erst an der Grundlinie los. Der Ball bleibt beim Trainer, und Spieler vier zieht vorbei.",
       mv("n8", [29.8, Y["n8"]]), *um("r4", 57, Y["r4"])),
     S("Team Rot ist komplett", "Team Rot ist jetzt mit allen drei drin. Der Trainer spielt den Ball zu Spieler sieben, und Team Rot greift sein Minitor an. Spieler acht kommt zu spät.",
       ps("b0", [78.4, Y["r7"] + 0.6]), *um("n8", 52.2, Y["n8"]))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Schnell kombinieren.", "Schnell kombinieren",
    "Es steht eins zu eins, der nächste Treffer entscheidet. Mit müden Beinen hilft kein langes Dribbling. Abspielen, in den freien Raum starten und den Ball dort wieder bekommen.",
    sp(n10=(72, 33), n8=(55, 33), n6=(86, 38), r4=(72, 17), r7=(63.5, 48), r9=(56, 16.5)), baelle(R3) + [h.B("b0", 72.6, 33.6)] + ERSATZ,
    [S("Abspielen und starten", "Spieler zehn hat den Ball, und Spieler vier steht vor ihm. Kurzer Pass zu Spieler acht. Sofort startet Spieler zehn an Spieler vier vorbei in den freien Raum.",
       ps("b0", [55.6, 33.6]), mv("n10", [64, 22], delay=0.2), mv("n10", [66, 11], after=True)),
     S("In den Lauf: Punkt", "Spieler acht spielt den Ball direkt in den Lauf. Spieler zehn trifft ins Minitor, und das gibt einen Punkt für Team Neon. Damit gewinnt Team Neon die Runde.",
       ps("b0", [66.6, 11.6]), mv("r4", [70, 15], delay=0.2), ps("b0", [GX, FY0 + 0.3], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
