import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-40 (U15-U17, Woche 2 Pre-Season): Agility Stations and 2 v 2 Games. 25 x 30 Yards = 23 x 27 m (gerundet 25 x 25 m).
# Hochkant wie im PDF (Verhältnis unter 1,3), Feld x 22-78, y 4-52 (nicht ganz maßstäblich, etwas breiter, damit an jeder
# Seite zwei Gerätereihen Platz haben). In der Mitte die Spielzone mit zwei Großfeldtoren (je ein neutraler Torwart, nur C- und
# B-Jugend). An jeder Seite zwei Reihen: Leiter und drei Hürden, versetzt wie im PDF; Leitern als leiter(), Hürden huerde_ou.
# Teams: PDF pink -> Team Neon (4, 9, 3, 11 wie im PDF; startet oben, läuft nach unten, greift das obere Tor an),
# navy -> Team Rot neu nummeriert, weil 3 und 11 doppelt sind: 3 -> 5, 11 -> 6, 7 -> 7, 2 -> 2 (startet unten, läuft nach oben,
# greift das untere Tor an). Im Video greift das Team, das nach oben läuft, das untere Tor an; hier genauso, nur mit
# vertauschten Farben, damit Team Neon nach oben spielt. Ein Trainer (unten) statt zwei; die Wartenden stehen neben dem Feld.
# Spielerpositionen in der Spielzone links und rechts der Torhüter (3D-Abstand: zwischen den beiden Torhütern ist kein Platz).
# Fassungen: PDF Key Coaching Point 1 (Einzelaktion schafft das 2 gegen 1) und 2 (ruhig aufbauen, locken, Doppelpass hinter
# die Verteidiger). Konter nach Ballgewinn aus dem Ton übernommen (nur im Text).
# Sichtkegel: Text KCP 2 „This develops awareness“, Ton „recognize when to slow down and speed up attacks“; im Video nicht
# eingezeichnet, Richtung aus dem Sinn: Spieler elf schaut beim Doppelpass in den Lauf von Spieler neun hinter den Verteidiger,
# dann spielt er zurück (Kegel beim Passgeber, Regel vom 25.11.2026).
T = P("T", "c", 40.5, 55.5, "T")
GB = B("b0", 41.1, 56.1)
ERSATZ = [B("s1", 44, 56), B("s2", 46.5, 56)]
K1, K2 = P("k1", "t", 50, 16.5, "TW"), P("k2", "t", 50, 38.5, "TW")
POS = {"n9": (26.5, 5), "n11": (68, 5), "r5": (32, 51), "r7": (73.5, 51),
       "n4": (14, 5), "n3": (86, 5), "r6": (14, 51), "r2": (86, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [K1, K2, T]
LINES = [rect(22, 4, 56, 48), rect(36, 14, 28, 27)]
TORE = [{"x": 50, "y": 14, "side": "top", "size": "gross"}, {"x": 50, "y": 41, "side": "bottom", "size": "gross"}]
def hu(x, ys): return [C(x, y, shape="huerde_ou") for y in ys]
CONES = [leiter(26.5, 15, senkrecht=True), leiter(32, 41, senkrecht=True), leiter(68, 15, senkrecht=True), leiter(73.5, 41, senkrecht=True)] \
    + hu(26.5, (30, 34, 38)) + hu(32, (18, 22, 26)) + hu(68, (30, 34, 38)) + hu(73.5, (18, 22, 26)) \
    + [C(32, 5.5), C(26.5, 50.5), C(73.5, 5.5), C(68, 50.5)]
DIMS = dims(22, 78, 4, 52, "25 m", "25 m", rx=93)
FELD = {"n9": (40, 33.5), "n11": (60, 33.5), "r5": (40, 17.5), "r7": (60, 17.5)}
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
WARTE = [B("b4", 14.6, 5.6), B("b3", 86.6, 5.6)]

u = {"title": "Leiter, Hürden, 2 gegen 2", "code": "UE-323", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Koordination", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 10, "players_max": 14,
 "field_size": "25 x 25 m",
 "description": "Vier Spieler laufen gleichzeitig durch Leiter und Hürden an den Seiten des Feldes, zwei von Team Neon nach unten, zwei von Team Rot nach oben. Danach sprinten alle in die Spielzone in der Mitte. Das Team mit dem ersten Spieler im Feld bekommt den Ball vom Trainer, und es wird zwei gegen zwei auf zwei Tore mit Torwart gespielt. Wer am Ende die meisten Punkte hat, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern, in der Mitte die Spielzone mit zwei Toren. An jeder Seite liegen zwei Reihen mit je einer Leiter und drei Hürden, versetzt. In den Ecken markiert ein Hütchen das Ende jeder Reihe.",
  "Verteilen: Zwei Teams zu viert, je zwei Spieler oben und unten an den Ecken. Team Neon startet oben, Team Rot unten. In jedem Tor ein Torwart. Der Trainer steht mit Bällen unten am Rand.",
  "Ablauf: Auf Pfiff laufen vier Spieler gleichzeitig durch Leiter und Hürden bis zum Hütchen und sprinten dann in die Spielzone. Wer zuerst drin ist, bekommt den Ball. Team Neon greift das obere Tor an, Team Rot das untere. Wer den Ball erobert, kontert sofort.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Ist die Aktion vorbei, starten die nächsten vier. Wer gerade gespielt hat, erholt sich an der ersten Station."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle Füße in der Leiter, Knie hoch über die Hürden", "Sauber bleiben, wer stolpert, fehlt seinem Team", "Als Erster in die Spielzone", "Im zwei gegen zwei schnell kombinieren und abschließen"],
 "materials": ["2 Tore", "4 Koordinationsleitern", "12 Minihürden", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Leiter, Hürden, zwei gegen zwei. Erst durch die Geräte, dann wird gespielt. Wer zuerst in der Spielzone ist, bekommt den Ball.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [GB] + WARTE + ERSATZ,
  "steps": [
   S("Alle vier durch die Leiter", "Auf Pfiff laufen vier Spieler gleichzeitig los. Spieler neun und Spieler elf gehen oben in die Leiter, Spieler fünf und Spieler sieben unten. Schnelle Füße, in jedes Feld ein Kontakt.",
     mv("n9", [26.5, 24]), mv("n11", [68, 24]), mv("r5", [32, 32]), mv("r7", [73.5, 32])),
   S("Über die Hürden, ab ins Feld", "Weiter über die drei Hürden bis zum Hütchen. Dort drehen alle ab und sprinten diagonal in die Spielzone. Spieler neun ist am schnellsten.",
     mv("n9", [26.5, 47.5]), mv("n9", list(FELD["n9"]), after=True),
     mv("n11", [68, 47.5], delay=0.2), mv("n11", list(FELD["n11"]), after=True),
     mv("r5", [32, 7.5], delay=0.4), mv("r5", list(FELD["r5"]), after=True),
     mv("r7", [73.5, 7.5], delay=0.3), mv("r7", list(FELD["r7"]), after=True)),
   S("Wer zuerst drin ist, kriegt den Ball", "Spieler neun war als Erster im Feld. Also spielt der Trainer ihm den Ball, und Team Neon greift das obere Tor an.",
     ps("b0", fuss(FELD["n9"]))),
   S("Zwei gegen zwei", "Spieler neun dribbelt auf Spieler fünf zu und zieht ihn auf sich. Spieler sieben rückt zur Mitte. Dann der Pass nach außen zu Spieler elf.",
     dr("n9", "b0", [42, 28]), mv("r5", [43, 23], delay=0.2), mv("r7", [52, 24], delay=0.3), mv("n11", [59, 27]), ps("b0", [59.6, 27.6], after=True)),
   S("Abschluss: Punkt", "Spieler elf schießt sofort, und das gibt einen Punkt für Team Neon. Jetzt starten die nächsten vier, Spieler vier, Spieler drei, Spieler sechs und Spieler zwei. Wer gespielt hat, erholt sich an der ersten Station.",
     ps("b0", [55.5, 14.3]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer geht vorbei.", "Einer geht vorbei",
    "Wer im zwei gegen zwei seinen Gegenspieler ausspielt, macht daraus ein zwei gegen eins. Dann muss der zweite Verteidiger raus, und der Mitspieler wird frei. Mut zum Dribbling, und danach den Kopf hoch.",
    sp(n9=(40, 35), n11=(61, 35), r5=(40, 19), r7=(60, 19)), [B("b0", 61.6, 35.6)] + WARTE + ERSATZ,
    [S("Eins gegen eins außen", "Spieler elf geht mit Ball auf Spieler sieben zu. Kurz antäuschen, dann mit Tempo außen vorbei.",
       dr("n11", "b0", [62, 29]), mv("r7", [59, 25], delay=0.2), dr("n11", "b0", [65, 25], after=True), dr("n11", "b0", [61, 19.5], after=True)),
     S("Jetzt zwei gegen eins", "Spieler sieben ist geschlagen. Spieler fünf muss raus zu Spieler elf, und Spieler neun läuft sich frei. Der Pass kommt quer.",
       mv("r5", [55, 26]), mv("n9", [42, 24]), ps("b0", [42.6, 24.6], after=True)),
     S("Freier Mann trifft: Punkt", "Spieler neun schießt direkt, und das gibt einen Punkt für Team Neon.",
       ps("b0", [46, 14.3]))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Locken, dann Doppelpass.", "Locken, dann Doppelpass",
    "Nicht jeder Angriff muss sofort schnell sein. Team Neon spielt sich den Ball ruhig zu, bis die Verteidiger herauskommen und pressen. Dann geht es schnell, mit einem Doppelpass in den Raum hinter ihnen.",
    sp(**FELD), [B("b0", *fuss(FELD["n9"]))] + WARTE + ERSATZ,
    [S("Ruhig aufbauen, Gegner locken", "Spieler neun und Spieler elf spielen sich den Ball ruhig zu. Spieler fünf und Spieler sieben rücken heraus und pressen. Hinter Spieler fünf wird Platz frei.",
       ps("b0", fuss(FELD["n11"])), mv("r7", [59, 27], delay=0.3), ps("b0", fuss(FELD["n9"]), after=True), mv("r5", [41, 28.5], delay=1.0)),
     S("Doppelpass hinter die Abwehr", "Jetzt schnell. Pass zu Spieler elf, und Spieler neun startet an Spieler fünf vorbei. Spieler elf schaut in den Lauf und spielt direkt zurück.",
       ps("b0", fuss(FELD["n11"])), mv("n9", [45, 32], delay=0.2), mv("n9", [47, 23], after=True), bl("n11", [47, 23], delay=0.75), ps("b0", [47.6, 23.6], after=True)),
     S("Hinter der Abwehr: Punkt", "Spieler neun ist durch und schließt sofort ab, und das gibt einen Punkt für Team Neon.",
       ps("b0", [45, 14.3]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
