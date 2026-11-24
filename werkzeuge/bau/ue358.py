import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 36-P10 (U15-U17, Woche 21 Phase 2): Midfield Link Play to Attack (Medium Sided Game). 30 x 40 Yards = 27 x 37 m
# (gerundet 25 x 35 m). Zonen 15 / 10 / 15 Yards, im Text auf 35 m umgelegt (etwa 13 / 9 / 13 m).
# LANGES FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51), Tore links
# und rechts (Großfeldtore, nur C- und B-Jugend), Zonengrenzen gestrichelt bei x 39 und x 59. Team Neon greift nach rechts an
# (im PDF Pink nach oben). Koordinaten direkt quer gesetzt: PDF oben -> rechts, PDF links -> oben.
# PDF pink -> Team Neon mit den Nummern aus dem PDF (5, 4, 6, 8, 10, 9). PDF blau -> Team Rot, neu nummeriert, weil alle
# Nummern doppelt sind: 5 -> 2, 6 -> 3, 4 -> 7, 10 -> 11, 8 -> 12, 9 -> 13. Beide Torhüter neutral (k1 links für Team Neon,
# k2 rechts für Team Rot), weil zweimal TW als doppelte Nummer gilt (wie ue317). Ein Trainer statt zwei.
# Positionen gegenüber dem PDF leicht in der Tiefe und Länge versetzt (3D-Abstand bei 14 Figuren).
# Passfolge nach PDF und Text: Torwart -> 6 -> 4 (rückt in die Mitte ein, 3 gegen 2) -> 8 -> 10 (zwei Pässe in der Mitte)
# -> 9 in der Angriffszone, Ablage auf den nachrückenden 10, Abschluss. Im PDF spielt 4 direkt auf 10, dafür fehlt dort der zweite Pass.
# Fassungen: PDF Progression 1 (Überzahl nur bei Pass in die nächste Zone binnen drei Sekunden) und Progression 2
# (Rückpass in die Aufbauzone erlaubt, der Torwart spielt mit).
# Sichtkegel: Text/Ton KCP 1 „Scan before receiving – can you turn or set?“: Spieler zehn schaut vor der Annahme zum Passgeber,
# nach der Annahme schwenkt der Kegel zur Spitze, dazu der Drehpfeil (Vorbild ue300). In der zweiten Steigerung schaut
# Spieler zehn vor dem Pass in die Spitze. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 45, 55.5, "T")
ERSATZ = [B("s1", 48.5, 56), B("s2", 51, 56)]
POS = {"k1": (12, 27.5), "n5": (21, 10), "n6": (21, 45), "n4": (34.5, 22), "n8": (45, 12), "n10": (54, 40), "n9": (68, 27.5),
       "k2": (85, 27.5), "r2": (72, 10), "r3": (72, 45), "r7": (53.5, 22), "r11": (44, 28), "r12": (34, 42), "r13": (25.5, 28)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def F(i): return fuss(POS[i])
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
MY = (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(39, FY0, 39, FY1), line(59, FY0, 59, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DIMS = dims(FX0, FX1, FY0, FY1, "35 m", "25 m")[:1]

u = {"title": "Über die Mitte in die Überzahl", "code": "UE-358", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "25 x 35 m",
 "description": "Sieben gegen sieben mit Torhütern auf einem Feld mit drei Zonen. Der Ball muss durch die Mittelzone, bevor es in die Angriffszone geht. Ein Spieler aus der Abwehr darf in die Mitte nachrücken, dort spielen dann drei gegen zwei. Nach mindestens zwei Pässen in der Mitte geht es nach vorn, und die Mittelfeldspieler rücken im Sprint mit in die Spitze.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 35 Metern mit einem großen Tor auf jeder Grundlinie. Zwei gestrichelte Linien teilen es in drei Zonen: Aufbau, Mitte und Angriff. Die Mittelzone ist etwa 9 Meter breit, die beiden anderen etwa 13 Meter.",
  "Verteilen: Je Team ein Torwart, drei Verteidiger in der Aufbauzone, zwei Mittelfeldspieler in der Mitte und ein Stürmer vorn. Die beiden Stürmer von Team Rot stehen in der Aufbauzone von Team Neon. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet, hinten spielen vier gegen zwei. Ein Verteidiger darf in die Mitte nachrücken. Dort sind mindestens zwei Pässe Pflicht, dann geht der Ball in die Angriffszone. Jetzt rücken die Mittelfeldspieler mit nach, und vorn wird es drei gegen zwei.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Verliert ein Team den Ball, kontert das andere sofort mit denselben Regeln. Nach einem Treffer eröffnet der Torwart auf der anderen Seite für das andere Team."],
 "organisation_show": ORG,
 "coaching_points": ["Vor der Annahme schauen: aufdrehen oder klatschen lassen?", "Platz für den Mitspieler machen, nicht nur für dich", "Schräg anbieten, im richtigen Moment, schnell kombinieren", "Erkennen, wann sichern und wann nach vorn"],
 "materials": ["2 große Tore", "Hütchen für die Zonen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Über die Mitte in die Überzahl. Sieben gegen sieben mit drei Zonen. Der Ball muss durch die Mitte, und wer dort nachrückt, schafft vorn die Überzahl.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *F("k1"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Torwart eröffnet, vier gegen zwei", "Der Torwart links eröffnet für Team Neon zu Spieler sechs. Hinten spielen vier gegen zwei, da ist immer einer frei. Spieler zwölf läuft an, aber zu spät.",
     ps("b1", F("n6")), mv("r12", [29, 41], delay=0.4)),
   S("Spieler vier rückt in die Mitte", "Spieler sechs spielt Spieler vier an. Der nimmt den Ball mit und dribbelt in die Mittelzone. Jetzt sind es dort drei gegen zwei.",
     ps("b1", F("n4")), dr("n4", "b1", [41, 19], after=True), mv("r11", [46, 24], delay=0.6)),
   S("Erster Pass in der Mitte", "Spieler vier spielt zu Spieler acht. Das ist der erste Pass in der Mitte. Spieler sieben schiebt zum Ball.",
     ps("b1", F("n8")), mv("r7", [52, 18], delay=0.3)),
   S("Kopf hoch vor der Annahme", "Spieler zehn bietet sich schräg an und schaut zum Ball. Dann kommt der zweite Pass. Jetzt darf es nach vorn gehen.",
     bl("n10", F("n8")), ps("b1", F("n10"), after=True)),
   S("Aufdrehen und in die Spitze", "Er hat vorher gesehen, dass hinter ihm Platz ist. Also dreht er auf und spielt in die Spitze auf Spieler neun. Spieler acht startet sofort mit nach vorn.",
     bl("n10", [68.6, 28.1], von=F("n8"), dauer=1.3), drehen("n10", [68.6, 28.1], gegen=True, delay=0.4), ps("b1", F("n9"), after=True),
     mv("n8", [66, 12], delay=0.8)),
   S("Drei gegen zwei vorn: Punkt", "Spieler neun lässt klatschen auf Spieler zehn, der nachgerückt ist. Der schießt flach ins Eck, und das gibt einen Punkt für Team Neon. Danach eröffnet der Torwart auf der anderen Seite für Team Rot.",
     mv("n10", [64, 38]), mv("r3", [70, 40], delay=0.2), mv("r2", [69, 18], delay=0.2), ps("b1", [64.6, 38.6], delay=0.6), ps("b1", [88.4, 31], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Überzahl gibt es nur mit Tempo.", "Überzahl nur mit Tempo",
    "Ein Spieler darf nur dann in die nächste Zone nachrücken, wenn der Ball innerhalb von drei Sekunden dorthin gespielt wird. Dauert es länger, bleibt es zwei gegen zwei. Das gilt in der Mitte und vorn in der Angriffszone.",
    sp(), [B("b1", *F("n5"))] + ERSATZ,
    [S("Schnell in die Mitte", "Spieler fünf hat den Ball und spielt sofort in die Mitte auf Spieler acht. Das ging schnell, also darf Spieler vier mit nachrücken.",
       ps("b1", F("n8")), mv("n4", [42, 20], delay=0.5), mv("r11", [49, 16], delay=0.5)),
     S("Zwei schnelle Pässe", "Spieler acht legt ab auf Spieler vier, der spielt direkt auf Spieler zehn. Zwei Pässe, wenig Zeit verloren.",
       ps("b1", [42.6, 20.6]), ps("b1", F("n10"), after=True), mv("r7", [52, 30], delay=0.4)),
     S("Sofort nach vorn: Punkt", "Spieler zehn spielt gleich in die Spitze und sprintet hinterher. Auch das ging schnell, also wird es vorn drei gegen zwei. Spieler neun legt auf, Spieler zehn trifft. Das gibt einen Punkt für Team Neon.",
       ps("b1", F("n9")), mv("n10", [64, 38], delay=0.3), ps("b1", [64.6, 38.6], after=True), ps("b1", [88.4, 31], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Ball darf zurück in die Aufbauzone.", "Zurück und neu aufbauen",
    "Geht es in der Mitte nicht schnell genug nach vorn, dürfen die Mittelfeldspieler den Ball zurück in die Aufbauzone spielen. Dann wird über zwei Zonen gespielt, und der Torwart baut mit auf. Die Mittelfeldspieler bekommen so Zeit, sich neu freizulaufen.",
    sp(r7=(53.5, 14)), [B("b1", *F("n8"))] + ERSATZ,
    [S("In der Mitte zu", "Spieler acht hat den Ball, aber Spieler elf und Spieler sieben machen die Wege zu. Nach vorn geht nichts. Also spielt er zurück zu Spieler fünf.",
       mv("r11", [47, 18]), mv("r7", [50, 14], delay=0.1), ps("b1", F("n5"), delay=0.4)),
     S("Torwart spielt mit", "Spieler fünf spielt zum Torwart, der verlagert gleich auf Spieler sechs. Spieler zehn löst sich in der Mitte und schaut schon nach vorn.",
       ps("b1", F("k1")), ps("b1", F("n6"), after=True), mv("n10", [47, 47], delay=0.6), bl("n10", [68.6, 28.1], after=True)),
     S("Neuer Anlauf: Punkt", "Spieler sechs spielt in die Mitte auf Spieler zehn, der direkt in die Spitze weiterleitet. Spieler neun nimmt den Ball mit und trifft. Das gibt einen Punkt für Team Neon.",
       ps("b1", [47.6, 47.6]), ps("b1", F("n9"), after=True), dr("n9", "b1", [76, 24], after=True), ps("b1", [88.4, 22], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
