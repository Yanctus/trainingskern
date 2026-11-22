import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 84-P6 (U12-U14, Woche 33 Phase 2): Keep Possession to Lock in Goals (Maintain Possession to Lock in Goals). 30 x 35 Yards =
# Feld x 28.6-71.4, y 5-55 (27 x 32 m), oben und unten je ein Jugendtor. Gedreht (180 Grad): im PDF schießt Pink auf das untere
# Tor, hier greift Team Neon nach oben an. Pink -> Team Neon 4, 5, 8, 10; Blau -> Team Rot 6, 9, 11 und 2 (im PDF doppelte 4).
# Die Torhüter sind im PDF grün (eigene Farbe): als k1 (oben, Torwart von Team Rot) und k2 (unten, Torwart von Team Neon) mit
# team "t" und Label "TW" (zwei Team-Torhüter mit "TW" meldet pruefen als doppelte Nummer). Positionen auf ein Spaltenraster (3D),
# ein Trainer statt zwei. Grundform: Treffer, dann Ball vom Trainer, sechs Pässe, erst dann zählt der Punkt. Neustart danach
# durch den Torwart von Team Rot (im Original nur "play starts as normal").
# Sichtkegel aus dem Text (Progression 2: "increasing intensity and awareness"): in der zweiten Steigerung schaut Spieler neun
# zum freien Gegner und fängt den Pass ab. Im Video und im Ton kein Kegel.
# Keine Dublette von UE-092 (94-P6: vier Minitore mit Springern, Tore zusperren), hier Treffer mit sechs Pässen sichern.
T = P("T", "c", 16, 40, "T")
POS = {"k1": (50, 8), "k2": (50, 52), "r2": (40.5, 15), "r6": (59, 18.4), "r11": (49, 27), "r9": (57.5, 34),
       "n10": (40.5, 31), "n8": (67.5, 24), "n5": (32, 42), "n4": (66, 42)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 19.6, 43.5), B("s2", 16, 43.5)]
LINES = [rect(28.6, 5, 42.8, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Treffer mit Pässen sichern", "code": "UE-222", "kind": "Spielform",
 "focuses": ["Torschuss", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 32 m",
 "description": "Vier gegen vier mit zwei Torhütern auf zwei Tore. Wer trifft, hat den Punkt noch nicht sicher: Der Trainer spielt dem Team sofort einen neuen Ball zu, und es muss sechs Pässe in Folge schaffen. Erst dann zählt der Treffer. Erobert der Gegner vorher den Ball, wird der Treffer gestrichen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 32 Metern mit einem Jugendtor an jedem Ende.",
  "Verteilen: Team Neon und Team Rot je zu viert plus Torwart. Team Neon greift nach oben an, Team Rot nach unten. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Freies Spiel vier gegen vier. Nach einem Treffer spielt der Trainer dem Team, das getroffen hat, einen neuen Ball zu. Jetzt braucht es sechs Pässe in Folge, der Torwart darf mitspielen.",
  "Wertung: Sechs Pässe geschafft, dann gibt der Treffer einen Punkt. Erobert der Gegner vorher den Ball, wird der Treffer gestrichen. Danach geht das Spiel normal weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Gut zusammenspielen, um zum Abschluss zu kommen", "Den Torwart beim Ballhalten mit einbeziehen", "Nach dem Treffer ruhig und genau passen", "Als Team hoch pressen und laut miteinander reden"],
 "materials": ["2 Jugendtore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Treffer mit Pässen sichern. Ein Treffer zählt erst, wenn das Team danach sechs Pässe in Folge schafft.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(28.6, 5, 42.8, 50), "players": sp(), "balls": [B("b1", 66.6, 42.6)] + ERSATZ,
  "steps": [
   S("Zusammenspielen", "Team Neon greift nach oben an. Spieler vier spielt zu Spieler acht, und Spieler acht dribbelt nach innen. Spieler zehn läuft mit nach vorn.",
     ps("b1", [68.1, 24.6]), dr("n8", "b1", [63, 12], after=True), mv("n10", [44, 24], delay=0.5), mv("r6", [60, 20], delay=0.5)),
   S("Abschluss", "Spieler acht schießt aufs Tor und trifft. Aber der Treffer zählt noch nicht.",
     ps("b1", [53, 5.3])),
   S("Ball vom Trainer", "Der Trainer spielt sofort einen neuen Ball zu Spieler fünf. Jetzt braucht Team Neon sechs Pässe in Folge. Pass eins zum Torwart, Pass zwei zu Spieler vier.",
     ps("s1", [32.6, 42.6]), ps("s1", [50.6, 52.6], after=True), ps("s1", [66.6, 42.6], after=True), mv("r9", [61, 38], delay=0.5)),
   S("Weiter passen", "Team Rot presst. Pass drei zu Spieler acht, Pass vier zu Spieler zehn, Pass fünf zurück zu Spieler fünf.",
     ps("s1", [63.6, 12.6]), ps("s1", [44.6, 24.6], after=True), ps("s1", [32.6, 42.6], after=True), mv("r11", [45, 30], delay=0.5), mv("r2", [36, 34], delay=1)),
   S("Sechs Pässe: Punkt", "Pass sechs zum Torwart. Geschafft! Jetzt ist der Treffer sicher, und das gibt einen Punkt für Team Neon. Danach geht das Spiel normal weiter, und der Torwart von Team Rot spielt den nächsten Ball ab.",
     ps("s1", [50.6, 52.6]))],
  "dims": dims(28.6, 71.4, 5, 55, "27 m", "32 m", rx=88)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Mehr Pässe zum Sichern.", "Acht Pässe zum Sichern",
    "Jetzt braucht das Team nach dem Treffer acht Pässe in Folge. Je nach Können dürfen es auch mehr oder weniger sein. Das verlangt Ruhe, genaue Pässe und schnelle Entscheidungen.",
    sp(), [B("b1", 32.6, 42.6)] + ERSATZ,
    [S("Ruhig bleiben", "Team Neon hat getroffen und braucht jetzt acht Pässe. Spieler fünf spielt zum Torwart, der Torwart zu Spieler vier, Spieler vier zu Spieler acht.",
       ps("b1", [50.6, 52.6]), ps("b1", [66.6, 42.6], after=True), ps("b1", [68.1, 24.6], after=True), mv("r9", [61, 36], delay=0.5), mv("r11", [46, 37], delay=0.5)),
     S("Acht Pässe: Punkt", "So geht es weiter, bis acht Pässe geschafft sind. Spieler acht spielt zu Spieler zehn, und der weiter zu Spieler fünf. Erst nach dem achten Pass gibt das einen Punkt für Team Neon.",
       ps("b1", [41.1, 31.6]), ps("b1", [32.6, 42.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ballgewinn wird belohnt.", "Ballgewinn wird belohnt",
    "Erobert das verteidigende Team den Ball, bevor die Pässe geschafft sind, bekommt es selbst einen Punkt. Dazu gibt es ein Zeitlimit für die Pässe. Das macht das Pressing wichtiger und zwingt das Team am Ball zu schnellen Entscheidungen.",
    sp(), [B("b1", 32.6, 42.6)] + ERSATZ,
    [S("Hoch pressen", "Team Neon hat getroffen und muss schnell passen. Team Rot presst als Team. Spieler zwei läuft Spieler fünf an, und Spieler neun schaut, wo der freie Gegner steht.",
       mv("r2", [35, 36]), mv("r11", [45, 34], delay=0.2), bl("r9", [70, 46], after=True)),
     S("Ballgewinn: Punkt", "Spieler fünf spielt zu Spieler vier, aber Spieler neun läuft in den Passweg und fängt den Ball ab. Der Treffer von Team Neon ist gestrichen, und das gibt einen Punkt für Team Rot.",
       mv("r9", [57.4, 42]), ps("b1", [58, 42.6], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
