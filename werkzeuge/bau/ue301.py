import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 71-P6 (U15-U17, Woche 10): Defensive Shape, Build Up and Finishing, Small Sided Game. 25 x 35 Yards = 23 x 32 m, gerundet
# 25 x 30 m. Hochkant wie im PDF, großes Tor oben, zwei Minitore unten. Feld x 25-75, y 5-55 (in der Breite gestreckt, damit
# elf Spieler den 3D-Abstand halten). PDF pink (5, 6, 7, 8, 11) = Team Neon greift das große Tor an, PDF dunkel (2, 3, 4, 9, 10)
# = Team Rot verteidigt und kontert. Torwart neutral. Positionen für den 3D-Abstand in Spalten verschoben. Ein Trainer statt zwei.
# PDF zeigt drei Pässe (6-8-11-7) und den Abschluss; hier werden alle sechs Pässe gezeigt (drei quer hinten davor).
# Fassungen: PDF Key Coaching Point (Abschluss aus der Distanz, wenn keiner rausrückt) und Progression (erst beide Minitore,
# der nächste Angriff dann aufs große Tor; im Video spielt der Trainer dafür den Ball zu Spieler 3).
# Sichtkegel: im Video nicht eingezeichnet; aus Text/Ton ("Identify opportunities when defenders are drawn to the ball",
# "recognize when defenders sit off", "Awareness"): Spieler 11 schaut in die Lücke, Spieler 8 schaut vor dem Distanzschuss nach vorn.
T = P("T", "c", 14, 12, "T")
TB = [14.6, 12.6]
ERSATZ = [B("s1", 17.6, 15.5), B("s2", 14, 15.5)]
TW = P("k", "t", 50, 7, "TW")
POS = {"n6": (33, 46.5), "n5": (60.5, 44), "n8": (51, 38), "n11": (30, 26), "n7": (62, 23),
       "r2": (39.5, 15), "r3": (70.5, 15.5), "r4": (50, 22.5), "r10": (41.5, 37), "r9": (70.5, 32)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
LINES = [rect(25, 5, 50, 50), line(25, 48, 75, 48)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 37, "y": 55, "side": "bottom"}, {"x": 63, "y": 55, "side": "bottom"}]
CONES = [C(25, 48), C(75, 48)]
DIMS = dims(25, 75, 5, 55, "25 m", "30 m", rx=90)

u = {"title": "Sechs Pässe bis zum Abschluss", "code": "UE-301", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Torschuss", "Verteidigen"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 11,
 "field_size": "25 x 30 m",
 "description": "Fünf gegen fünf auf ein großes Tor mit Torwart und zwei Minitore. Team Neon braucht sechs Pässe, erst dann darf es auf das große Tor abschließen. Erobert Team Rot den Ball, kontert es sofort auf eines der beiden Minitore. Vor den Minitoren liegt eine Zone, in die sich die Verteidiger nicht zurückziehen dürfen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern. Oben steht ein großes Tor, unten stehen zwei Minitore. Vor den Minitoren ist eine Zone von 5 Metern mit zwei Hütchen und einer Linie markiert.",
  "Verteilen: Fünf gegen fünf. Team Neon greift das große Tor an, Team Rot verteidigt es. Im Tor steht ein Torwart. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Team Neon spielt sechs Pässe und darf dann auf das große Tor schießen. Gewinnt Team Rot den Ball, kontert es auf die Minitore. Beim Konter darf kein Spieler von Team Neon in die Zone vor den Minitoren.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Steht beim Konter ein Verteidiger in der Zone, gibt das einen Punkt für Team Rot. Nach jedem Abschluss bringt der Trainer einen neuen Ball. Nach einigen Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Verteidiger rauslocken, dann durch die Lücke spielen", "Kopf hoch vor dem Pass in die Tiefe", "Mit dem ersten oder zweiten Kontakt abschließen", "Rückt keiner raus, schieß aus der Distanz"],
 "materials": ["1 großes Tor", "2 Minitore", "2 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechs Pässe bis zum Abschluss. Fünf gegen fünf, oben das große Tor, unten zwei Minitore. Team Neon muss sechs Pässe spielen, bevor es schießen darf. Holt sich Team Rot den Ball, geht es sofort auf die Minitore.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 33.6, 47.1)] + ERSATZ,
  "steps": [
   S("Hinten quer: eins, zwei, drei", "Team Neon lässt den Ball hinten laufen und zählt laut mit. Spieler sechs spielt in die Mitte zu Spieler acht. Der legt raus zu Spieler fünf, und von dort geht es quer zurück. Drei Pässe. Team Rot schiebt jedes Mal mit.",
     ps("b1", [51.6, 38.6]), ps("b1", [61.1, 44.6], after=True), ps("b1", [33.6, 47.1], after=True),
     mv("r9", [69, 38], delay=0.6), mv("r10", [39, 40], delay=1.6)),
   S("Vier und fünf über links", "Wieder rein zu Spieler acht, das ist der vierte. Dann raus auf Spieler elf, der fünfte. Jetzt rückt Team Rot nach links. Spieler zwei geht drauf, und Spieler vier schiebt hinterher.",
     ps("b1", [51.6, 38.6]), ps("b1", [30.6, 26.6], after=True), mv("r2", [33, 20.5], delay=0.9), mv("r4", [43, 26.5], delay=0.9)),
   S("Kopf hoch, der sechste Pass", "Spieler elf nimmt den Kopf hoch. In der Mitte ist die Lücke auf, weil Spieler vier rübergeschoben hat. Genau dort startet Spieler sieben hinein. Der sechste Pass kommt flach in seinen Lauf.",
     bl("n11", [51, 17]), mv("n7", [51, 17], delay=0.4), ps("b1", [51.6, 17.6], after=True), mv("r3", [64, 17], delay=1.0)),
   S("Abschluss: Punkt", "Spieler sieben nimmt den Ball mit und schießt mit dem zweiten Kontakt ins lange Eck, und das gibt einen Punkt für Team Neon. Der Trainer spielt sofort den nächsten Ball zu Team Neon.",
     ps("b1", [55.5, 5.3]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Rückt keiner raus, dann schieß.", "Schuss aus der Distanz",
    "Team Rot steht tief und eng vor dem großen Tor. Durch die Mitte kommt kein Pass mehr durch. Dafür hat der Spieler am Ball Zeit und Platz. Kommt nach dem sechsten Pass keiner auf ihn zu, schießt er aus der Distanz.",
    sp(r4=(53, 22.5)), [B("b1", 61.1, 44.6)] + ERSATZ,
    [S("Sechster Pass, Rot bleibt tief", "Fünf Pässe sind gespielt. Der sechste kommt von Spieler fünf in die Mitte zu Spieler acht. Team Rot bleibt hinten stehen, keiner rückt raus.",
       ps("b1", [51.6, 38.6])),
     S("Kopf hoch, Schuss: Punkt", "Spieler acht nimmt den Kopf hoch. Spieler vier bleibt stehen, der Weg zum Tor ist frei. Also schießt er aus der Distanz flach ins linke Eck, und das gibt einen Punkt für Team Neon.",
       bl("n8", [49, 20]), ps("b1", [44.5, 5.3], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Team Rot muss erst in beide Minitore treffen.", "Erst beide Minitore",
    "Team Rot bekommt jetzt den Ball vom Trainer und greift die Minitore an. Ein Treffer links und ein Treffer rechts, erst dann ist die Aufgabe erfüllt. Den nächsten Angriff muss Team Rot auf das große Tor abschließen. Team Neon verteidigt und darf nicht in die Zone vor den Minitoren.",
    sp(r3=(60.5, 11), n8=(52, 23), n7=(61, 27), r9=(70.5, 30), r4=(42, 30.5), n11=(30, 28), r2=(30, 45), n6=(38.5, 46.5),
       r10=(51, 42), n5=(59.5, 46.5)), [B("b1", *TB)] + ERSATZ,
    [S("Neuer Ball für Team Rot", "Ins linke Minitor hat Team Rot schon getroffen. Der Trainer spielt den nächsten Ball zu Spieler drei. Jetzt zählt nur noch das rechte Minitor.",
       ps("b1", [61.1, 11.6])),
     S("Steil, dann nach außen", "Spieler drei spielt steil auf Spieler zehn. Der legt sofort nach rechts raus, und Spieler neun läuft in den Ball. Spieler fünf will hinterher, aber an der Linie ist für ihn Schluss.",
       ps("b1", [51.6, 42.6]), mv("r9", [69, 39], delay=0.7), ps("b1", [69.6, 39.6], after=True), mv("n5", [61.5, 47], delay=1.4)),
     S("Rechtes Minitor: Punkt", "Spieler neun schiebt ins rechte Minitor ein, und das gibt einen Punkt für Team Rot. Beide Minitore sind getroffen. Den nächsten Angriff schließt Team Rot auf das große Tor ab.",
       ps("b1", [63, 55.3]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
