import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P19 (U12-U14, Einzeltraining): How to Support the Build Up - CDM. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m),
# Orientierung wie im PDF (Minitor hinter dem Spieler oben, zwei Minitore und Trainer unten). Mittellinie gestrichelt wie im PDF.
# Orange (CDM) -> Neon 6 (Sechser). Acht Bälle beim Trainer: auf der Tafel zwei zum Spielen plus zwei Ersatzbälle.
# Ablauf nach PDF: links annehmen auf dem hinteren Fuß, aufdrehen, aufs obere Minitor; um den Dummy herum, vor dem Dummy
# direkt ins linke untere Minitor ablegen; dann rückwärts zur anderen Seite (Gegenrichtung zum Ablegen, Video). Im Video legt
# er zuerst nach rechts ab, hier wie im PDF nach links.
# Progression 1 (Trainer ruft das Tor: im Original rechts/links, Farbe oder 1/2; links/rechts ist im Video aus Sicht des Spielers
# vertauscht) hier mit "eins" (links) und "zwei" (rechts) als Steigerung. Progression 2 (Erleichterung: zwei Kontakte beim Ablegen)
# nur im Text der Steigerung. Progression 3 (Spieler entscheidet selbst und sagt es laut) als zweite Steigerung.
# Sichtkegel aus Text/Ton ("Effective Scanning", "habit of scanning", "scan both sides") und Video (Kegel beim Rückwärtslaufen
# mit offenem Körper): Schulterblick vor der Annahme, Blick zum Dummy beim Rückwärtslaufen, links und rechts in der Steigerung.
T = P("T", "c", 50, 47, "T")
POS = {"n6": (34, 22)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 52), B("s2", 46, 52)]
def baelle(b1=(50.6, 47.6)):
    return [B("b1", *b1), B("b2", 49, 49.4)] + ERSATZ
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 36, "y": 51, "side": "bottom"}, {"x": 64, "y": 51, "side": "bottom"}]
DUMMY = [C(50, 15, shape="stange")]

u = {"title": "Sechser dreht auf und legt ab", "code": "UE-294", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1, "field_size": "18 x 18 m",
 "description": "Der Sechser übt, im Spielaufbau anspielbar zu sein. Er nimmt den Pass des Trainers auf dem hinteren Fuß an, dreht auf und schießt aufs Minitor hinter sich. Dann läuft er um einen Dummy und legt den nächsten Ball direkt in eines der Minitore neben dem Trainer. Danach läuft er rückwärts zur anderen Seite, und alles beginnt mit dem anderen Fuß von vorn.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit drei Minitoren: eins oben in der Mitte, zwei unten links und rechts. In der oberen Hälfte steht ein Dummy als Gegenspieler.",
  "Verteilen: Der Spieler steht links neben dem Dummy. Der Trainer steht unten zwischen den zwei Minitoren und hat acht Bälle.",
  "Ablauf: Der Trainer spielt zum Spieler. Er nimmt auf dem hinteren Fuß an, dreht auf und schießt aufs obere Minitor. Dann läuft er um den Dummy, bekommt vor dem Dummy den zweiten Ball und legt ihn direkt ins untere Minitor.",
  "Wechsel: Nach dem Ablegen läuft der Spieler rückwärts zur anderen Seite, und dort geht es mit dem anderen Fuß weiter. Nach acht Bällen, also vier Durchgängen, ist Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Hohes Tempo: schnell umschalten und sauber ausführen", "Zum Aufdrehen offen stehen und auf dem hinteren Fuß annehmen", "Zum Ablegen kompakt stehen und mit beiden Füßen genau spielen", "Ständig umschauen, laut sprechen und schnell entscheiden"],
 "materials": ["3 Minitore", "1 Dummy", "8 Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Sechser dreht auf und legt ab. Spieler sechs nimmt an, dreht auf und schießt, dann legt er den nächsten Ball direkt ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": DUMMY, "players": sp(), "balls": baelle(),
  "steps": [
   S("Schulterblick und Pass", "Spieler sechs schaut über die Schulter nach hinten. Dann spielt der Trainer ihn an.",
     bl("n6", [42, 8]), ps("b1", [34.6, 22.6], after=True)),
   S("Aufdrehen und abschließen", "Spieler sechs steht offen und nimmt den Ball mit dem hinteren Fuß an. Er dreht auf und schießt aufs obere Minitor.",
     dr("n6", "b1", [38, 16]), ps("b1", [50, 5.6], after=True)),
   S("Um den Dummy", "Jetzt läuft er schnell hinten um den Dummy herum und kommt vorn wieder heraus.",
     mv("n6", [44, 9.5]), mv("n6", [56, 9.5], after=True), mv("n6", [57, 18], after=True), mv("n6", [50, 22], after=True)),
   S("Direkt ablegen", "Der Trainer spielt den zweiten Ball. Spieler sechs legt ihn direkt ins linke Minitor unten.",
     ps("b2", [50.6, 22.6]), ps("b2", [36, 50.4], after=True)),
   S("Rückwärts zur Seite", "Sofort läuft Spieler sechs rückwärts nach rechts, den Körper offen, und schaut zum Dummy. Hier geht es mit dem anderen Fuß weiter. Nach acht Bällen ist die Runde vorbei, dann hat er Pause.",
     mv("n6", [64, 22]), bl("n6", [53, 12], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft, wohin der Ball geht.", "Der Trainer ruft",
    "Das linke Minitor unten ist eins, das rechte zwei. Beim Pass ruft der Trainer die Nummer, und dorthin legt der Spieler ab. Er kommt mit gerader Hüfte an, so sieht er beide Seiten. Ist das noch zu schwer, darf er beim Ablegen zweimal den Ball berühren.",
    sp(n6=(57, 18)), baelle(), [
     S("Beide Seiten sehen", "Spieler sechs kommt vor den Dummy, die Hüfte gerade zum Trainer. Er schaut nach links und nach rechts.",
       mv("n6", [50, 22]), bl("n6", [40, 37], after=True), bl("n6", [60, 37], after=True)),
     S("Ruf: zwei", "Der Trainer spielt und ruft dabei zwei. Spieler sechs legt den Ball direkt ins rechte Minitor und läuft danach rückwärts nach links.",
       ps("b1", [50.6, 22.6]), ps("b1", [64, 50.4], after=True), mv("n6", [36, 22], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Spieler entscheidet selbst.", "Selbst entscheiden",
    "Jetzt entscheidet der Spieler: aufdrehen oder ablegen. Er schaut sich um und sagt laut, was er vorhat. Ist hinter ihm Platz, ruft er drehen, steht der Gegner im Rücken, ruft er ab.",
    sp(n6=(56, 21)), baelle(), [
     S("Schauen und rufen", "Spieler sechs schaut über die Schulter. Der Dummy steht direkt hinter ihm, Aufdrehen geht nicht. Also ruft er laut: Ab!",
       bl("n6", [48, 8])),
     S("Ablegen", "Der Trainer spielt ihn an, und Spieler sechs legt direkt ins linke Minitor ab. Danach läuft er rückwärts weg und bietet sich neu an.",
       ps("b1", [56.6, 21.6]), ps("b1", [36, 50.4], after=True), mv("n6", [66, 21], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
