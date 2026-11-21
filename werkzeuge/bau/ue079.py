import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P34: 20 x 20 Yards = x 30-72, y 13-55. Gefängnis als Zone oben (x 38-64, y 1-10). Räuber (Neon) starten links versetzt, Polizisten (Rot) in der Mitte.
T = P("T", "c", 86, 24, "T")
def zone(x, y, w, h): return {"type": "zone", "x": x, "y": y, "w": w, "h": h}
start = [("n1", 26, 17), ("n2", 35, 25), ("n3", 26, 33), ("n4", 35, 41), ("n5", 26, 49)]
lines = [rect(30, 13, 42, 42), zone(38, 1, 26, 9)]
cones = ecken(30, 13, 42, 42)
u = {"title": "Räuber und Polizist", "code": "UE-079", "kind": "Spielform",
 "focuses": ["Dribbling", "1 gegen 1", "Verteidigen"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 12, "field_size": "18 x 18 m",
 "description": "Fünf Räuber mit Ball wollen auf die andere Seite des Feldes dribbeln, zwei Polizisten ohne Ball wollen ihnen den Ball wegspielen. Wer seinen Ball verliert, muss ins Gefängnis am Rand. Der Räuber, der als Letzter übrig bleibt, gewinnt. Danach werden neue Polizisten bestimmt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern, daneben am Rand ein kleines Feld als Gefängnis.",
  "Verteilen: Fünf Räuber mit je einem Ball stehen an einer Seite. Zwei Polizisten ohne Ball stehen in der Mitte.",
  "Ablauf: Alle Räuber dribbeln gleichzeitig los und versuchen, auf die andere Seite zu kommen. Spielt ein Polizist einem Räuber den Ball weg, muss der Räuber ins Gefängnis. Wer es geschafft hat, dribbelt in der nächsten Runde zurück. Der letzte Räuber gewinnt.",
  "Wechsel: Nach jeder kompletten Runde zwei neue Polizisten bestimmen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell die Richtung wechseln, um den Polizisten auszuweichen", "Den Kopf heben und sehen, wo die Polizisten stehen", "Den eigenen Ball mit dem Körper schützen", "Kleine Kontakte beim Richtungswechsel, große Kontakte, um wegzulaufen"],
 "materials": ["4 orange Hütchen für das Feld", "4 Hütchen für das Gefängnis", "1 Ball für jeden Räuber", "Leibchen für die Polizisten"],
 "access": "frei", "hidden": True,
 "say_intro": "Räuber und Polizist. Die Räuber dribbeln auf die andere Seite, die Polizisten wollen sie fangen.",
 "board": {"lines": lines, "cones": cones,
  "players": [P(i, "a", x, y, i[1:]) for i, x, y in start] + [P("r6", "b", 58, 26, "6"), P("r7", "b", 58, 42, "7"), T],
  "balls": [B("b" + i[1:], x + 1.6, y + 0.6) for i, x, y in start],
  "steps": [
   S("Alle dribbeln gleichzeitig los", "Alle fünf Räuber dribbeln gleichzeitig los. Die beiden Polizisten laufen ihnen entgegen.",
     dr("n1", "b1", [44, 18]), dr("n2", "b2", [46, 27]), dr("n3", "b3", [44, 34]), dr("n4", "b4", [48, 44]), dr("n5", "b5", [44, 51]),
     mv("r6", [52, 26], delay=0.2), mv("r7", [56, 46], delay=0.2)),
   S("Ball weg: ab ins Gefängnis", "Polizist sechs spielt Räuber zwei den Ball weg. Räuber zwei muss ins Gefängnis. Die anderen dribbeln gleichzeitig weiter.",
     ps("b2", [41, 21]), mv("n2", [50, 6], delay=0.3),
     dr("n1", "b1", [62, 17]), dr("n3", "b3", [60, 34]), dr("n4", "b4", [54, 50]), dr("n5", "b5", [62, 52])),
   S("Auf der anderen Seite", "Vier Räuber kommen sicher auf der anderen Seite an. In der nächsten Runde dribbeln sie zurück, bis nur noch einer übrig ist.",
     dr("n1", "b1", [76, 18]), dr("n3", "b3", [76, 34]), dr("n4", "b4", [76, 44]), dr("n5", "b5", [76, 53]), mv("r7", [64, 46]))],
  "dims": [{"x1": 30, "y1": 58.6, "x2": 72, "y2": 58.6, "text": "18 m"}, {"x1": 93, "y1": 13, "x2": 93, "y2": 55, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Stehen die Polizisten weit auseinander, durch die Lücke in der Mitte dribbeln.", "Die Lücke in der Mitte",
    "Wer den Kopf hebt, sieht, wo die Polizisten stehen. Sind sie weit auseinander, ist in der Mitte eine Lücke. Genau dort schnell hindurchdribbeln, dann ist der Weg zur anderen Seite frei.",
    [P("n3", "a", 40, 34, "3"), P("n1", "a", 44, 5.5, "1"), P("n2", "a", 54, 5.5, "2"), P("r6", "b", 58, 22, "6"), P("r7", "b", 56, 48, "7"), T],
    [B("b3", 41.6, 34.6)],
    [S("Lücke sehen", "Die beiden Polizisten stehen weit auseinander. Räuber drei hebt den Kopf und sieht die Lücke in der Mitte.", dr("n3", "b3", [48, 33])),
     S("Durch die Mitte", "Räuber drei dribbelt schnell durch die Lücke. Die Polizisten kommen zu spät, und er ist sicher auf der anderen Seite.",
       dr("n3", "b3", [76, 32]), mv("r6", [62, 26], delay=0.3), mv("r7", [60, 41], delay=0.3))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Kommt ein Polizist, mit einem schnellen Haken ausweichen.", "Haken schlagen",
    "Kommt ein Polizist auf einen zu, hilft ein schneller Richtungswechsel. Mit kleinen Kontakten den Haken machen, dann mit einem großen Kontakt weg in den freien Raum. So bleibt der Ball beim Räuber, und er kommt sicher an.",
    [P("n2", "a", 40, 26, "2"), P("n1", "a", 44, 5.5, "1"), P("n3", "a", 53, 5.5, "3"), P("n4", "a", 62, 5.5, "4"), P("r6", "b", 50, 21, "6"), P("r7", "b", 52, 44, "7"), P("n5", "a", 36, 49, "5"), T],
    [B("b2", 41.6, 26.6), B("b5", 37.6, 49.6)],
    [S("Polizist kommt", "Räuber zwei dribbelt los, und Polizist sechs kommt direkt auf ihn zu.", dr("n2", "b2", [45, 27]), mv("r6", [48, 25])),
     S("Haken und weg", "Mit einem schnellen Haken zieht Räuber zwei zur Seite und dribbelt mit einem großen Kontakt in den freien Raum. Polizist sechs geht ins Leere.",
       dr("n2", "b2", [42, 33]), dr("n2", "b2", [58, 36], after=True), dr("n2", "b2", [76, 34], after=True), mv("r6", [46, 30], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
