import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-105 (U12-U14, Woche 3 Pre-Season): Physical with Fun - Tag Game ("Pac-Man"). 10 x 15 Yards hochkant = Feld x 33.5-66.5, y 5-55
# (9 x 14 m). Laufen nur auf den Linien: Mittellinie senkrecht (x 50), zwei Querlinien (y 21.7 und 38.3).
# Pink (Läufer) -> Neon 6, 7, 8, 9; Blau (Fänger) -> Rot 2 und 3 (Blau 6 neu nummeriert: 3). Ein Trainer statt zwei.
# Sichtkegel wie im Video ("Constant scanning - recognize direction of pressure"): der Läufer schaut zu den Fängern, bevor er wegläuft.
T = P("T", "c", 25, 30, "T")
POS = {"n7": (41, 5), "n6": (59.1, 21.7), "n8": (41, 38.3), "n9": (56, 55), "r3": (50, 28.8), "r2": (66.5, 44.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(33.5, 5, 33, 50), line(50, 5, 50, 55, dashed=False), line(33.5, 21.7, 66.5, 21.7, dashed=False), line(33.5, 38.3, 66.5, 38.3, dashed=False)]
INSELN = [C(x, y, "neon", id=f"i{n}") for n, (x, y) in enumerate((x, y) for x in (33.5, 50, 66.5) for y in (5, 21.7, 38.3, 55))]

u = {"title": "Fangen nur auf den Linien", "code": "UE-133", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Koordination", "Erwärmung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "9 x 14 m",
 "description": "Ein Fangspiel auf einem kleinen Feld mit Linien, wie bei Pac-Man: Läufer und Fänger dürfen sich nur auf den Linien bewegen, also nur waagrecht oder senkrecht. Die Fänger von Team Rot versuchen, die Läufer von Team Neon zu fangen. Wer gefangen wird, muss raus und wartet außen. Der letzte Läufer, der übrig bleibt, gewinnt. Wer ständig schaut, wo die Fänger sind, entkommt am längsten.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern mit gut sichtbaren Linien: außen herum, eine Linie längs durch die Mitte und zwei Querlinien. Hütchen an den Kreuzungen braucht es erst in der Steigerung.",
  "Verteilen: Vier Läufer von Team Neon und zwei Fänger von Team Rot stehen auf den Linien verteilt. Der Trainer steht außen.",
  "Ablauf: Auf Pfiff laufen alle gleichzeitig los, aber nur auf den Linien. Die Fänger versuchen, einen Läufer zu berühren. Wer gefangen ist, verlässt sofort das Feld und wartet außen.",
  "Wertung: Gespielt wird, bis nur noch ein Läufer übrig ist. Der gewinnt die Runde. Dann sind zwei andere die Fänger."],
 "organisation_show": ORG,
 "coaching_points": ["Ständig umschauen und früh sehen, von wo die Fänger kommen", "Mit Körpertäuschungen den Fänger in die falsche Richtung schicken", "Schnell entscheiden, bevor man in einer Ecke festsitzt", "Auf den Fußballen bleiben, um blitzschnell die Richtung zu wechseln"],
 "materials": ["Linien oder Hütchenreihen für das Feld", "12 Hütchen für die Steigerung", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Fangen nur auf den Linien. Ein Fangspiel wie bei Pac-Man, bei dem alle nur waagrecht und senkrecht laufen dürfen.",
 "board": {"lines": LINES, "players": sp(), "balls": [],
  "steps": [
   S("Nur auf den Linien", "Auf Pfiff laufen alle gleichzeitig los, aber nur auf den Linien. Spieler drei jagt Spieler acht, der läuft nach links weg.",
     mv("r3", [50, 38.3]), mv("r3", [45, 38.3], after=True), mv("n8", [33.5, 38.3]), mv("n8", [33.5, 31], after=True),
     mv("n7", [33.5, 5], delay=0.2), mv("n7", [33.5, 13], after=True), mv("r2", [66.5, 32], delay=0.3), mv("n9", [50, 55], delay=0.3)),
   S("Umschauen, Druck erkennen", "Spieler sechs schaut sich um: Spieler zwei kommt von rechts unten, Spieler drei steht links unten. Also läuft er auf der Querlinie zur Mitte, weg von beiden.",
     bl("n6", [66.5, 32]), bl("n6", [45, 38.3], after=True), mv("n6", [50, 21.7], after=True), mv("r2", [66.5, 21.7], delay=0.8)),
   S("Gefangen: raus", "Spieler drei bleibt Spieler acht auf den Fersen und fängt ihn an der linken Linie. Spieler acht muss raus und wartet außen.",
     mv("r3", [33.5, 38.3]), mv("r3", [33.5, 33.3], after=True), mv("n8", [24, 42], after=True)),
   S("Der Letzte gewinnt", "Die anderen laufen weiter. Gespielt wird, bis nur noch ein Läufer übrig ist. Der gewinnt die Runde, und dann sind zwei andere die Fänger.",
     mv("n6", [50, 12]), mv("r2", [58, 21.7], delay=0.2), mv("n9", [50, 46], delay=0.1))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ständig umschauen.", "Ständig umschauen",
    "Wer nur nach vorn schaut, läuft einem Fänger direkt in die Arme. Jede Sekunde kurz umschauen: Wo sind die Fänger, aus welcher Richtung kommt der Druck? Dann dorthin laufen, wo keiner ist, bevor man in einer Ecke festsitzt.",
    sp(n6=(50, 21.7), r3=(50, 5), r2=(66.5, 30), n7=(33.5, 10)), [],
    [S("Erst schauen", "Spieler sechs steht auf der Kreuzung in der Mitte und schaut sich um: Spieler drei kommt von oben, Spieler zwei von rechts.",
       bl("n6", [50, 5]), bl("n6", [66.5, 30], after=True), mv("r3", [50, 12], delay=0.6)),
     S("Weg vom Druck", "Also läuft er nach links weg, dorthin, wo kein Fänger ist. Die beiden Fänger kommen zu spät, und Spieler sechs ist noch im Spiel.",
       mv("n6", [33.5, 21.7]), mv("n6", [33.5, 29], after=True), mv("r3", [50, 21.7], delay=0.2), mv("r2", [66.5, 21.7], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Täuschen und abhauen.", "Täuschen und abhauen",
    "Wer immer geradeaus wegläuft, ist leicht zu fangen. Besser: kurz in die eine Richtung antäuschen, den Fänger mitziehen und dann blitzschnell in die andere Richtung abbiegen. So gewinnt man den entscheidenden Schritt.",
    sp(n9=(50, 38.3), r2=(66.5, 38.3), n8=(41, 55), r3=(33.5, 28)), [],
    [S("Antäuschen", "Spieler neun läuft ein Stück nach unten, als wolle er dorthin. Spieler zwei läuft auf der Querlinie schon in diese Richtung.",
       mv("n9", [50, 44]), mv("r2", [56, 38.3], delay=0.1)),
     S("Abbiegen, entkommen", "Dann dreht Spieler neun blitzschnell um und läuft nach oben. Spieler zwei ist auf dem falschen Fuß und kommt nicht mehr hinterher, Spieler neun bleibt im Spiel.",
       mv("n9", [50, 30]), mv("n9", [50, 22.5], after=True), mv("r2", [50.5, 38.3], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Hütchen als sichere Inseln.", "Sichere Inseln",
    "Auf jede Kreuzung kommt ein Hütchen. Wer auf einem Hütchen steht, darf nicht gefangen werden, aber höchstens drei Sekunden lang. Die Fänger dürfen jetzt frei durchs Feld laufen und lauern zwischen den Hütchen.",
    sp(), [], [S("Sicher auf der Insel", "Spieler neun rettet sich zum Hütchen auf der unteren Linie, dort ist er sicher. Spieler zwei läuft jetzt quer durchs Feld auf ihn zu.",
       mv("n9", [52.1, 55]), mv("r2", [55, 49], delay=0.2), mv("n8", [35.6, 38.3], delay=0.1)),
     S("Nach drei Sekunden weiter", "Nach drei Sekunden muss Spieler neun weiter und sprintet zum nächsten Hütchen. Er ist schneller als Spieler zwei und schafft es, also bleibt er im Spiel. Dann sucht sich Spieler zwei einen anderen Läufer.",
       mv("n9", [50, 40.4]), mv("r2", [53, 44.5], delay=0.3), mv("r3", [38, 35], delay=0.2))], cones=INSELN)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
