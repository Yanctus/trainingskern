import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 99-P9 (U15-U17, Woche 9 Phase 2): Break Out to Penetrate. 30 x 20 Yards = 27 x 18 m (gerundet 18 x 25 m).
# FELD QUER (langes Feld, Inhaber 24.11.2026, Vorbild ue317.py): Im PDF hochkant, hier quer, Minitore links und rechts.
# Team Neon spielt im Rondo links und bricht nach rechts aus. Feld x 9-89, y 4-51, Sperrzonen (2 Yards) an beiden Enden
# gestrichelt bei x 14.3 und 83.7, Mittellinie bei x 49. Positionen direkt quer geplant (Raster für den 3D-Abstand).
# PDF pink -> Team Neon (2, 6, 8, 10 wie im PDF), gelb 9 -> Springer F, blau -> Team Rot, neu nummeriert (doppelt):
# 10 -> 3, 8 -> 5, 6 -> 7, der einzelne Verteidiger 4 bleibt 4. Ein Trainer statt zwei (unten an der Seitenlinie).
# Ablauf im PDF: 6 spielt in den Lauf von 8, der in die andere Zone ausbricht. Hier dreht der Springer in der Mitte auf
# (bl mit von, drehen) und spielt in den Lauf von Spieler sechs (Raster/3D-Abstand), Abschluss auf das freie Minitor.
# Fassung 1 = PDF Key Coaching Point (als Einheit verteidigen, im PDF nach dem Rollentausch gezeigt; hier verteidigt Team Rot
# in derselben Zone, Inhalt gleich). Fassung 2 = PDF Progression (der einzelne Verteidiger kommt mit in den Rondo, 5 gegen 4).
# Annahme: In der Steigerung steht danach niemand mehr vor den Minitoren; die Verteidiger laufen nach dem Ausbruch hinterher.
# Sichtkegel: kein Kegel im Video eingezeichnet; aus Text und Ton ("recognise the right moment", "recognise where the
# available space is", "find free player"): Der Springer schaut erst zum Passgeber, dann in die andere Zone (bl mit von).
T = P("T", "c", 62, 55.3, "T")
ERSATZ = [B("s1", 65.5, 55.8), B("s2", 68, 55.8)]
POS = {"n2": (16, 28), "n8": (24.5, 8), "n10": (24.5, 46), "n6": (47.5, 22),
       "r3": (24.5, 25), "r5": (33, 12), "r7": (41.5, 46), "r4": (68, 27), "f9": (33, 33)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 47), line(14.3, 4, 14.3, 51), line(83.7, 4, 83.7, 51), line(49, 4, 49, 51)]
TORE = [{"x": 9, "y": 12.5, "side": "left"}, {"x": 9, "y": 41.6, "side": "left"},
        {"x": 89, "y": 12.5, "side": "right"}, {"x": 89, "y": 41.6, "side": "right"}]
KEGEL = [C(x, y) for x in (9, 14.3, 49, 83.7, 89) for y in (4, 51)]
DIMS = dims(9, 89, 4, 51, "25 m", "18 m")[:1]  # rechts stehen Minitore: nur die Länge
BALL = [B("b1", *fuss("n2"))] + ERSATZ

u = {"title": "Aus dem Rondo in die Torzone", "code": "UE-342", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 9, "players_max": 9,
 "field_size": "18 x 25 m",
 "description": "Vier gegen drei plus Springer in einer Zone, in der anderen Zone wartet ein einzelner Verteidiger vor zwei Minitoren. Das Team am Ball lässt den Ball laufen, bis sich eine Lücke auftut. Dann bricht ein Spieler in die andere Zone aus und schließt ab. Erobert das verteidigende Team den Ball, bekommt es selbst einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern, in der Mitte geteilt in zwei Zonen. An beiden Enden eine Sperrzone von 2 Metern, dahinter je zwei Minitore.",
  "Verteilen: In der ersten Zone spielen vier Spieler von Team Neon mit dem Springer gegen drei von Team Rot. In der anderen Zone steht Spieler vier von Team Rot allein vor den Minitoren. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Team Neon lässt den Ball laufen und wartet auf den richtigen Moment. Dann geht der Pass in die andere Zone, ein Spieler bricht aus und schließt auf ein Minitor ab. Die Sperrzone darf niemand betreten.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobert Team Rot in einer der Zonen den Ball, gibt das einen Punkt für Team Rot. Nach jedem Treffer geht es in der anderen Zone weiter, und die Teams tauschen die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Ball schnell laufen lassen, bis die Lücke da ist", "Kopf hoch, wann ist der Moment zum Ausbrechen?", "Der Pass nach vorn muss sitzen", "Den freien Mann finden, wir sind in Überzahl"],
 "materials": ["4 Minitore", "10 Hütchen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aus dem Rondo in die Torzone. Vier gegen drei plus Springer in einer Zone, drüben wartet ein einzelner Verteidiger vor zwei Minitoren. Team Neon hält den Ball und bricht im richtigen Moment aus.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BALL, "dims": DIMS,
  "steps": [
   S("Ball laufen lassen", "Spieler zwei spielt nach außen zu Spieler zehn. Sofort läuft Spieler drei an. Der Springer steht in der Mitte und zeigt sich.",
     ps("b1", fuss("n10")), mv("r3", [20, 37], delay=0.4)),
   S("Springer bekommt den Ball", "Der Springer schaut zum Ball. Spieler zehn spielt flach in die Mitte, bevor Spieler drei da ist.",
     bl("f9", POS["n10"]), ps("b1", fuss("f9"), after=True), mv("r5", [33, 20], delay=0.3)),
   S("Aufdrehen, Pass in die andere Zone", "Jetzt ist die Lücke da. Der Springer dreht auf und sieht Spieler sechs, der in die andere Zone startet. Genau in seinen Lauf kommt der Pass.",
     bl("f9", [60, 28], von=POS["n10"], dauer=1.3), drehen("f9", [60, 28], gegen=True, delay=0.4), mv("n6", [60, 28], delay=0.3),
     ps("b1", [60.6, 28.6], after=True)),
   S("Ausgebrochen: Punkt", "Spieler vier kommt raus und macht das nähere Tor zu. Spieler sechs zieht zur anderen Seite vorbei und schießt ins freie Minitor, und das gibt einen Punkt für Team Neon. Danach geht es in dieser Zone weiter, mit Team Rot am Ball. Spieler zwei bleibt allein in der ersten Zone und verteidigt dort.",
     mv("r4", [71, 36]), dr("n6", "b1", [72, 18], delay=0.4), ps("b1", [88.4, 12.8], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Als Einheit verteidigen.", "Als Einheit verteidigen",
    "Die drei Verteidiger im Rondo schieben gemeinsam zum Ball und machen die Passwege zu. Auch der einzelne Verteidiger in der anderen Zone schiebt mit. So bleibt Team Neon nur der Rückpass, und irgendwann kommt der Ball in einen Fuß von Team Rot.",
    sp(), BALL,
    [S("Alle schieben zum Ball", "Spieler zwei spielt zu Spieler zehn. Jetzt schiebt Team Rot gemeinsam. Spieler drei läuft an, Spieler fünf geht in den Weg zum Springer. Drüben schiebt auch Spieler vier mit.",
       ps("b1", fuss("n10")), mv("r3", [20, 37], delay=0.3), mv("r5", [29, 30], delay=0.3), mv("r7", [38, 38], delay=0.3), mv("r4", [64, 33], delay=0.3)),
     S("Nur der Rückpass bleibt", "Nach vorn ist alles zu. Spieler zehn muss zurück zu Spieler zwei spielen. Spieler fünf rückt schon in die nächste Lücke.",
       ps("b1", fuss("n2")), mv("r3", [21, 36.5], delay=0.2), mv("r5", [27, 23], delay=0.4)),
     S("Abgefangen: Punkt für Team Rot", "Spieler zwei will zu Spieler sechs. Spieler fünf steht schon im Passweg und fängt den Ball ab, und das gibt einen Punkt für Team Rot.",
       ps("b1", [27.6, 26.6]), mv("r5", [27, 26], delay=0.2))]),
  V("Steigerung", "Und jetzt die Steigerung: Der einzelne Verteidiger kommt mit in den Rondo.", "Fünf gegen vier im Rondo",
    "Spieler vier verlässt die andere Zone und hilft im Rondo. Jetzt spielt Team Neon mit dem Springer fünf gegen vier. Der Ball muss noch schneller laufen, mit einem oder zwei Kontakten. Dafür ist drüben vor den Minitoren der Platz frei.",
    sp(), BALL,
    [S("Der Vierte kommt dazu", "Spieler vier sprintet aus der anderen Zone zurück in den Rondo. Spieler zwei spielt zu Spieler zehn, und der Druck ist gleich höher.",
       mv("r4", [42, 36]), ps("b1", fuss("n10"), delay=0.6), mv("r3", [20, 37], delay=0.8)),
     S("Direkt weiter", "Spieler zehn spielt direkt in die Mitte zum Springer. Spieler sechs schaut zum Ball, und der Springer legt mit einem Kontakt zu ihm.",
       ps("b1", fuss("f9")), bl("n6", POS["f9"], delay=0.3), ps("b1", fuss("n6"), after=True)),
     S("Aufdrehen und ausbrechen: Punkt", "Spieler sechs dreht auf und nimmt den Ball mit in die andere Zone. Spieler vier läuft hinterher, ist aber zu spät. Spieler sechs schießt ins Minitor, und das gibt einen Punkt für Team Neon.",
       bl("n6", [70, 20], von=POS["f9"], dauer=1.3), drehen("n6", [70, 20], gegen=True, delay=0.4), dr("n6", "b1", [70, 20], after=True),
       mv("r4", [58, 31], delay=0.8), ps("b1", [88.4, 13], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
