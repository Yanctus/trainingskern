import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 60-P1 (U12-U14, Woche 18 Phase 6): Defend the Goal 1 v 1. 30 x 35 Yards (Skizze; im Text 35 x 45) = Feld x 28.5-71.5, y 5-55
# (27 x 32 m), Verteidigungszone 15 x 10 Yards (14 x 9 m) vor dem Fünfmeterraum. Gespiegelt: Tor oben (im Original unten).
# Rollen wechseln jede Runde, die Farben stehen nur für einzelne Spieler. Blau -> Neon 9, 3, 6 (Passgeber), 5 (Verteidiger);
# Pink -> Rot 4, 10, dazu Pink 9 (Stürmer) -> Rot 7 und Pink 6 -> Rot 8 (Nummern im PDF doppelt). Grüner Torwart -> neutraler TW.
# Wartende in einer Reihe unten (einer rechts außerhalb des Feldes), Verteidiger seitlich versetzt (3D-Abstand), im Original
# direkt hinter dem Stürmer. Rot neun -> Rot sieben. Steigerung: Minitore an den Seitenlinien (im Original schräg in den Ecken).
# Sichtkegel: Coaching-Punkt im PDF "Attackers must constantly check their shoulders" -> Rot sieben schaut vor der Annahme
# über die Schulter zum Verteidiger. Im Video "Head up release early - GK distribution" mit eingezeichneter Linie zum rechten
# Minitor -> in der Steigerung schaut der Torwart hoch zum Minitor.
T = P("T", "c", 14, 30, "T")
TW = P("k", "t", 50, 8, "TW")
POS = {"r7": (50, 27), "n5": (41.5, 18), "n6": (58.5, 41),
       "r10": (21.5, 51), "n9": (30, 51), "r4": (38.5, 51), "n3": (47, 51), "r8": (67.5, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
ERSATZ = [B("s1", 15.6, 33.5), B("s2", 12, 33.5)]
WARTE = [B("q1", 22.1, 51.6), B("q2", 30.6, 51.6), B("q3", 39.1, 51.6), B("q4", 47.6, 51.6), B("q5", 68.1, 51.6)]
BAELLE = [B("b1", 59.1, 41.6)] + WARTE + ERSATZ
ZONE = {"type": "zone", "x": 39.25, "y": 14, "w": 21.5, "h": 14.3}
LINES = [rect(28.5, 5, 43, 50), rect(40, 5, 20, 8), ZONE]
KEGEL = [C(39.25, 14), C(60.75, 14), C(39.25, 28.3), C(60.75, 28.3), C(54, 44)]
TOR = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
MINI = [{"x": 28.5, "y": 36, "side": "left"}, {"x": 71.5, "y": 36, "side": "right"}]

u = {"title": "Eins gegen eins vor dem Tor", "code": "UE-183", "kind": "Übungsform",
 "focuses": ["Verteidigen", "1 gegen 1", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "27 x 32 m",
 "description": "Ein Stürmer und ein Verteidiger stehen in einer Zone vor dem Tor mit Torwart. Ein Passgeber spielt den Stürmer an, und der Verteidiger ist sofort eng dran, damit sich der Stürmer nicht drehen kann. Erobert der Verteidiger den Ball, blockt den Schuss oder drängt den Stürmer aus der Zone, gibt das einen Punkt für ihn. Danach wechseln die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 32 Metern mit einem Jugendtor oben. Vor dem Tor eine Zone von 14 mal 9 Metern mit vier Hütchen, unten ein Hütchen für den Passgeber.",
  "Verteilen: Ein Torwart im Tor. Ein Stürmer und ein Verteidiger in der Zone, ein Passgeber am Hütchen. Die anderen warten unten in einer Reihe, jeder mit Ball. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Passgeber spielt den Stürmer an. Der Stürmer will sich drehen und abschließen. Der Verteidiger ist früh eng dran und lässt ihn nicht drehen.",
  "Wertung und Wechsel: Ball erobert, Schuss geblockt oder Stürmer aus der Zone gedrängt gibt einen Punkt für den Verteidiger, ein Treffer gibt einen Punkt für den Stürmer. Dann wird der Stürmer Verteidiger, der Passgeber Stürmer, und der Verteidiger stellt sich hinten an."],
 "organisation_show": ORG,
 "coaching_points": ["Früh eng dran sein, damit sich der Stürmer nicht drehen kann", "Nicht zu eng und nicht auf eine Seite lehnen, sonst dreht er sich weg", "Mit dem Körper die Richtung vorgeben und den Stürmer nach außen drängen", "Im richtigen Moment den Ball wegspitzeln und schnell zurücklaufen, wenn er vorbei ist"],
 "materials": ["1 Jugendtor", "2 Minitore", "5 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Eins gegen eins vor dem Tor. Der Verteidiger ist sofort eng am Stürmer und lässt ihn nicht drehen.",
 "board": {"lines": LINES, "goals": TOR, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Pass zum Stürmer", "Neon sechs spielt den Ball zu Rot sieben in die Zone. Neon fünf läuft sofort los und ist eng dran, wenn der Ball ankommt.",
     ps("b1", [50.6, 27.6]), mv("n5", [48.5, 22], delay=0.2)),
   S("Nicht drehen lassen", "Rot sieben will sich drehen. Neon fünf bleibt tief in den Knien und geht mit. So kann sich Rot sieben nicht zum Tor drehen.",
     dr("r7", "b1", [55, 26]), mv("n5", [53.5, 21.5], delay=0.2)),
   S("Nach außen drängen", "Neon fünf drängt Rot sieben nach außen, weg vom Tor. Rot sieben muss mit dem Ball aus der Zone.",
     dr("r7", "b1", [64, 24]), mv("n5", [60, 20], delay=0.2)),
   S("Aus der Zone: Punkt", "Rot sieben ist aus der Zone, und das gibt einen Punkt für Neon fünf. Ein Treffer gäbe einen Punkt für Rot sieben. Jetzt wird Rot sieben Verteidiger, Neon sechs wird Stürmer, und Neon fünf stellt sich hinten an.",
     mv("n5", [76, 51]), mv("n6", [50, 27], delay=0.3), mv("r7", [41.5, 18], after=True))],
  "dims": dims(28.5, 71.5, 5, 55, "27 m", "32 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Eng dran, aber nicht zu eng.", "Eine Armlänge Abstand",
    "Der Stürmer schaut über die Schulter und spürt, wo der Verteidiger steht. Klebt der Verteidiger zu eng dran oder lehnt sich auf eine Seite, dreht sich der Stürmer an ihm vorbei. Darum bleibt er eine Armlänge weg, tief in den Knien und im Gleichgewicht.",
    sp(), BAELLE,
    [S("Schulterblick", "Bevor der Ball kommt, schaut Rot sieben über die Schulter und sieht, wo Neon fünf steht. Dann spielt Neon sechs ihn an, und Neon fünf läuft an.",
       bl("r7", [42, 13]), ps("b1", [50.6, 27.6], after=True), mv("n5", [47.5, 21.5], delay=0.9)),
     S("Im Gleichgewicht", "Neon fünf bleibt eine Armlänge weg und lehnt sich nicht auf eine Seite. Rot sieben versucht sich wegzudrehen, aber Neon fünf geht mit.",
       dr("r7", "b1", [45.5, 26]), mv("n5", [43.5, 21.5], delay=0.2)),
     S("Ball erobert: Punkt", "Jetzt spitzelt Neon fünf den Ball weg und holt ihn sich. Das gibt einen Punkt für Neon fünf.",
       ps("b1", [40.6, 22.6]), mv("n5", [40, 22], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Mit Minitoren herausspielen.", "Schnell herausspielen",
    "An den Seiten stehen zwei Minitore. Erobert der Verteidiger den Ball oder hält der Torwart einen Schuss, spielen sie den Ball schnell in ein Minitor. Der Torwart nimmt dafür sofort den Kopf hoch, wirft oder schießt, bevor der Stürmer wieder presst.",
    sp(), BAELLE,
    [S("Pass und Druck", "Neon sechs spielt zu Rot sieben, und Neon fünf ist sofort eng dran.",
       ps("b1", [50.6, 27.6]), mv("n5", [48.5, 22], delay=0.2)),
     S("Schuss gehalten", "Rot sieben dreht sich doch und schießt, aber der Torwart fängt den Ball.",
       dr("r7", "b1", [53, 24]), ps("b1", [50.6, 8.6], after=True)),
     S("Kopf hoch", "Der Torwart nimmt sofort den Kopf hoch und sieht das freie Minitor rechts.",
       bl("k", [61.5, 24])),
     S("Ins Minitor: Punkt", "Er wirft den Ball schnell ins rechte Minitor, bevor Rot sieben presst. Das gibt einen Punkt für Neon fünf. Erobert Neon fünf selbst den Ball, spielt er genauso schnell in ein Minitor.",
       ps("b1", [70.5, 36]))],
    goals=TOR + MINI)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
