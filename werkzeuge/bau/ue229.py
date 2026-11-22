import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 21-P1 (U12-U14, Woche 35 Phase 3): Shooting in and around the box Technical (PDF: Technical Finishing Combinations in the Box).
# Halbes Feld nach der PDF-Skizze = Feld x 20-80, y 5-53 (gleicher Maßstab wie im PDF, ca. 65 x 52 m), oben Jugendtor mit
# neutralem Torwart (im PDF grün -> "k" TW), Strafraum und Torraum als Linien. Orientierung wie im PDF (Tor oben).
# Zwei Dummys als Stangen vor den Strafraumecken, außen je fünf Hütchen im Zickzack für die schnellen Füße.
# Blau (linke Seite) -> Team Neon 2 (Grundlinie, Spieler eins im Ton), 3 (Strafraumecke, Spieler zwei), 4 (im Strafraum, Spieler drei);
# Pink (rechte Seite) -> Team Rot 5, 6, 7. Spieler vier und sieben etwas weiter vom Tor weg gesetzt (3D-Abstand zum Torwart).
# Zwei Trainer im PDF (oben rechts und unten) -> ein Trainer unten in der Mitte mit Bällen (spielt in der Steigerung zu).
# Grundform aus Ton/Video: Pass von der Grundlinie, direkt weiter, Sprint außen um die Stange, Ablage, Abschluss; Spieler eins
# sprintet danach durch die Hütchen. Coaching-Punkt = PDF Seite 2 links, Steigerung = PDF Seite 2 rechts / Ton (umdrehen,
# Ball vom Trainer, mit dem schwächeren Fuß in ein Minitor; Ausbruchzone und Minitore nur in der Steigerung).
# Sichtkegel: Text "Take a quick look up to identify the goalkeeper's position", Kegel im PDF eingezeichnet (Schütze -> Torwart):
# bl() des Schützen zum Torwart vor dem Abschluss.
T = P("T", "c", 50, 48.5, "T")
POS = {"n2": (29.7, 3.5), "n3": (32.9, 19.5), "n4": (41.5, 16.6), "r5": (70.3, 3.5), "r6": (67.1, 19.5), "r7": (58.5, 16.6)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k", "t", 50, 8.5, "TW"), T]
ERSATZ = [B("s1", 53.6, 52), B("s2", 50, 52), B("s3", 70.9, 4.1)]
LINES = [rect(20, 5, 60, 48), rect(31.3, 5, 37.4, 13.1), rect(40.5, 5, 19, 5.7)]
KEGEL = [C(35.2, 23.5, shape="stange"), C(64.8, 23.5, shape="stange"),
         C(27.5, 8.6), C(22.8, 12.4), C(27.5, 15.3), C(22.9, 19.3), C(27.5, 23.2),
         C(72.5, 8.6), C(77.2, 12.4), C(72.5, 15.3), C(77.1, 19.3), C(72.5, 23.2)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Kombination im Strafraum", "code": "UE-229", "kind": "Übungsform",
 "focuses": ["Torschuss", "Passspiel", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 9, "field_size": "65 x 52 m",
 "description": "Drei Spieler kombinieren schnell mit direkten Pässen am Strafraum und schließen gegen den Torwart ab. Der Passgeber an der Strafraumecke spielt weiter und sprintet sofort um eine Stange, dann bekommt er den Ball in den Lauf zurück. Vor dem Schuss schaut er kurz zum Torwart und zielt flach in eine Ecke. Danach ist die andere Seite dran.",
 "organisation": ["Aufbauen: Ein Jugendtor mit Torwart, davor der Strafraum. Vor beiden Strafraumecken eine Stange, außen je fünf Hütchen im Zickzack.",
  "Verteilen: Links drei Spieler von Team Neon, rechts drei von Team Rot: einer an der Grundlinie mit Bällen, einer an der Strafraumecke, einer im Strafraum. Der Trainer steht weiter hinten mit Bällen.",
  "Ablauf: Pass von der Grundlinie zur Strafraumecke, direkt weiter in den Strafraum, Sprint um die Stange, Ablage in den Lauf und Abschluss. Der erste Passgeber sprintet danach durch die Hütchen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach rücken die drei eine Position weiter, und die andere Seite beginnt."],
 "organisation_show": ORG,
 "coaching_points": ["Möglichst mit einem Kontakt spielen", "Schnell und eng um die Stange sprinten", "Vor dem Schuss kurz zum Torwart schauen", "Genau und flach in die Ecken schießen, nicht nur hart"],
 "materials": ["1 Jugendtor", "2 Stangen", "10 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Kombination im Strafraum. Drei Spieler passen direkt, einer sprintet um die Stange und schließt gegen den Torwart ab.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 30.3, 4.1)] + ERSATZ,
  "steps": [
   S("Anspiel", "Spieler zwei spielt von der Grundlinie zu Spieler drei an der Strafraumecke.",
     ps("b1", [33.5, 20.1])),
   S("Direkt weiter", "Spieler drei spielt direkt zu Spieler vier und sprintet sofort außen um die Stange.",
     ps("b1", [42.1, 17.2]), mv("n3", [31.5, 25], after=True), mv("n3", [37, 28], after=True), mv("n3", [46, 21.5], after=True)),
   S("Ablage in den Lauf", "Spieler vier legt den Ball direkt in den Lauf von Spieler drei. Gleichzeitig sprintet Spieler zwei schnell durch die Hütchen.",
     ps("b1", [46.6, 22.1]), mv("n2", [25.2, 6]), mv("n2", [24.6, 10.5], after=True), mv("n2", [25.6, 13.9], after=True),
     mv("n2", [24.6, 17.3], after=True), mv("n2", [25.4, 21.2], after=True)),
   S("Abschluss: Punkt", "Spieler drei schaut kurz hoch zum Torwart und schießt direkt flach ins Eck. Das gibt einen Punkt für Team Neon. Danach rücken die drei eine Position weiter, und die rechte Seite mit Team Rot ist dran.",
     bl("n3", [50.5, 4.5]), ps("b1", [55.5, 5.3], after=True))],
  "dims": dims(20, 80, 5, 53, "65 m", "52 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor dem Schuss kurz zum Torwart schauen.", "Erst schauen, dann zielen",
    "Bevor der Ball kommt, schaut der Schütze kurz hoch: Wo steht der Torwart? Dann zielt er genau in die freie Ecke. Genauigkeit ist wichtiger als Kraft.",
    sp(n3=(50, 26)), [B("b1", 42.1, 17.2)] + ERSATZ,
    [S("Ablegen und schauen", "Spieler vier legt den Ball in den Lauf von Spieler drei. Spieler drei schaut kurz hoch und sieht, dass der Torwart etwas nach links gegangen ist.",
       ps("b1", [48.6, 22.6]), mv("n3", [48, 22]), mv("k", [47.5, 8.5], delay=0.3), bl("n3", [50.5, 5], after=True)),
     S("Ins freie Eck: Punkt", "Spieler drei schießt flach und genau ins rechte Eck, weg vom Torwart. Das gibt einen Punkt für Team Neon.",
       ps("b1", [55.5, 5.3]))]),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Schuss umdrehen und aufs Minitor.", "Umdrehen und Minitor",
    "Nach dem Abschluss dreht sich der Schütze sofort um und sprintet in die Zone vor den beiden Minitoren. Der Trainer spielt ihm einen zweiten Ball zu, und er schießt mit dem schwächeren Fuß in ein Minitor. So übt er schnelles Umdrehen und das Gleichgewicht unter Zeitdruck.",
    sp(n3=(50, 24.5)), [B("b1", 42.1, 17.2), B("b2", 50.6, 49.1)] + ERSATZ,
    [S("Abschluss", "Spieler vier legt ab, und Spieler drei schießt direkt ins große Tor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 25.1]), ps("b1", [55.5, 5.3], after=True)),
     S("Umdrehen und sprinten", "Sofort dreht sich Spieler drei um und sprintet in die Zone vor den Minitoren. Der Trainer spielt ihm einen zweiten Ball zu.",
       mv("n3", [50, 33]), ps("b2", [50.6, 33.6], delay=0.5)),
     S("Schwacher Fuß: Punkt", "Spieler drei schießt mit seinem schwächeren Fuß in das rechte Minitor. Das gibt noch einen Punkt für Team Neon. Danach ist Team Rot dran.",
       ps("b2", [59.5, 45.2]))],
    lines=LINES + [rect(38.3, 25.7, 23.4, 18.4, dashed=True)],
    goals=TORE + [{"x": 40, "y": 45.5, "side": "bottom"}, {"x": 60, "y": 45.5, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
