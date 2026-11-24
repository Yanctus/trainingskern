import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-37 (U15-U17, Woche 33 Phase 2): Y-Technical Combinations Warm Up. 20 x 35 Yards = 18 x 32 m (gerundet 18 x 30 m).
# LANGES FELD QUER (Vorbild ue317.py, Verhältnis 1,75): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51), Start links,
# das Y öffnet sich nach rechts (im PDF Start unten, Y nach oben). Koordinaten direkt quer gesetzt: PDF oben -> rechts,
# PDF rechts -> unten. Alle Spieler Team Neon mit den Nummern aus dem Video: Start 6 (mit Ball) und 11 (wartet mit Ball),
# Mitte 2, Arm oben 5 und 9, Arm unten 4 und 10. Je ein Hütchen neben jeder Station, außen neben den Wegen.
# Ein Trainer an der Seitenlinie unten. Grundform über den unteren Arm wie im PDF und Video (6-2 Doppelpass, steil auf 4,
# Ablage auf 2, durch auf 10, Doppelpass 10-4, 10 dribbelt zum Start). Rotation: jeder folgt seinem Pass (6 auf die Station
# von 4, 4 ans Ende), der Spieler in der Mitte bleibt und wird nach ein paar Runden getauscht (im Original nicht genau gezeigt).
# Fassungen: Steigerung = PDF/Video Progression „Diagonal passes“ (Pass aus der Mitte diagonal zum Ende des anderen Arms,
# Doppelpass mit dem Spieler, der abgelegt hat). Coaching-Punkt = PDF Key Coaching Point „Receive on the back foot“.
# Sichtkegel: Kein Scannen im Original (Text, Ton und Video geprüft). Im Coaching-Punkt nimmt Spieler zwei an und dreht auf:
# nach ZUSATZ_U15 schaut er zum Passgeber, nach der Annahme schwenkt der Kegel zum Passziel (bl mit von plus drehen).
# Keine Dublette: UE-239 (45-P12, V aus fünf Stationen, Prallpass und Querpass zur oberen Station der anderen Seite) und
# UE-215/UE-309/UE-344 haben andere Aufstellung und andere Passfolgen.
T = P("T", "c", 30, 55.3, "T")
ERSATZ = [B("s1", 33.5, 55.8), B("s2", 36, 55.8)]
POS = {"n6": (13, 27.5), "n11": (4.5, 31), "n2": (32, 27.5), "n5": (52, 17), "n4": (52, 38), "n9": (82, 10), "n10": (82, 45)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def kurz(a, b, L=22):
    # Blickkegel nicht zu lang: Punkt in derselben Richtung, höchstens L Einheiten vom Spieler entfernt
    import math
    d = math.dist(a, b)
    return list(b) if d <= L else [round(a[0] + (b[0] - a[0]) * L / d, 1), round(a[1] + (b[1] - a[1]) * L / d, 1)]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def F(i): return fuss(POS[i])
LINES = [rect(9, 4, 80, 47)]
CONES = [C(11, 23), C(32, 23.5), C(55.5, 14), C(52, 42.5), C(85.5, 7), C(85.5, 48)]
DIMS = dims(9, 89, 4, 51, "30 m", "18 m", rx=95)
NACH = dict(n6=(23, 37))  # Stand nach dem ersten Doppelpass: Spieler sechs ist schräg nach vorn gelaufen

u = {"title": "Passfolge im Y", "code": "UE-392", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 7, "players_max": 10,
 "field_size": "18 x 30 m",
 "description": "Sechs Stationen bilden ein Y. Am Start gibt es einen Doppelpass mit dem Spieler in der Mitte, dann geht der Ball steil in einen Arm, zurück in die Mitte und durch zum letzten Spieler. Der spielt noch einen Doppelpass und dribbelt zurück zum Start. Jeder rückt eine Station weiter, und die nächste Runde läuft über den anderen Arm.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 30 Metern. Sechs Hütchen bilden ein Y, Start und Mitte hintereinander, dann zwei Arme mit je zwei Stationen.",
  "Verteilen: An jedem Hütchen ein Spieler, am Start zwei Spieler mit Ball. Der Trainer steht mit Ersatzbällen an der Seite.",
  "Ablauf: Doppelpass mit der Mitte, steil auf die erste Station im Arm, Ablage in die Mitte und durch zur letzten Station. Dort folgt ein Doppelpass mit der ersten Station, dann geht es mit Ball zurück zum Start.",
  "Wechsel: Jeder folgt seinem Pass zur nächsten Station, der Spieler in der Mitte wird nach ein paar Runden getauscht. Die Runden wechseln zwischen den beiden Armen."],
 "organisation_show": ORG,
 "coaching_points": ["Pass mit dem richtigen Tempo, genau in den Fuß", "Ein Kontakt, höchstens zwei", "Rufen, bevor der Ball kommt", "Mit dem hinteren Fuß annehmen, dann sofort weiter"],
 "materials": ["6 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passfolge im Y. Ein Aufwärmen mit zwei Doppelpässen, einer Ablage und einem Pass durch in die Tiefe. Danach geht es über den anderen Arm.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", *F("n6")), B("b2", *F("n11"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Doppelpass mit der Mitte", "Spieler sechs startet mit Ball. Er spielt zu Spieler zwei in die Mitte, geht schräg nach vorn und bekommt den Ball direkt zurück.",
     ps("b1", F("n2")), mv("n6", [23, 37], delay=0.3), ps("b1", [23.6, 37.6], after=True)),
   S("Steil auf Spieler vier", "Jetzt geht der Ball steil zu Spieler vier. Spieler zwei rückt ein Stück nach vorn und bietet sich an.",
     ps("b1", F("n4")), mv("n2", [42, 28], delay=0.3)),
   S("Ablegen in die Mitte", "Spieler vier legt mit einem Kontakt zurück auf Spieler zwei.",
     ps("b1", [42.6, 28.6])),
   S("Durch zu Spieler zehn", "Spieler zwei spielt den Ball durch, raus zu Spieler zehn am Ende des Arms.",
     ps("b1", F("n10"))),
   S("Doppelpass außen", "Spieler zehn spielt zurück zu Spieler vier und startet an der Seite entlang. Spieler vier legt ihm den Ball direkt in den Lauf.",
     ps("b1", F("n4")), mv("n10", [68, 49], delay=0.3), ps("b1", [68.6, 49.6], after=True)),
   S("Mit Ball zurück zum Start", "Spieler zehn dribbelt mit dem Ball eng am Fuß zurück zum Start. Spieler sechs rückt auf den Platz von Spieler vier, und Spieler vier geht ans Ende. Die Runde ist geschafft, und Spieler elf startet die nächste über den anderen Arm, mit Spieler fünf und Spieler neun.",
     dr("n10", "b1", [14, 40]), mv("n4", [82, 45], delay=0.2), mv("n6", [52, 38], delay=0.4), mv("n2", [32, 27.5], delay=0.2))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Pass aus der Mitte geht diagonal auf die andere Seite.", "Diagonal auf die andere Seite",
    "Der Anfang bleibt gleich. Nach der Ablage spielt der Spieler in der Mitte aber diagonal zum Ende des anderen Arms. Der Spieler, der abgelegt hat, läuft schräg nach vorn und spielt dort den Doppelpass. So wechselt der Ball schnell die Seite.",
    sp(**NACH), [B("b1", *F("n4")), B("b2", *F("n11"))] + ERSATZ,
    [S("Ablage in die Mitte", "Der Anfang bleibt gleich. Spieler vier hat den Ball und legt ab auf Spieler zwei, der nach vorn kommt.",
       mv("n2", [42, 28]), ps("b1", [42.6, 28.6], delay=0.4)),
     S("Diagonal zu Spieler neun", "Jetzt spielt Spieler zwei nicht auf seine Seite, sondern diagonal rüber zu Spieler neun. Spieler vier läuft schräg nach vorn in die Mitte.",
       ps("b1", F("n9")), mv("n4", [68, 24], delay=0.3)),
     S("Doppelpass, zurück zum Start", "Spieler neun spielt zu Spieler vier und startet an der Seite entlang. Er bekommt den Ball direkt zurück und dribbelt zum Start.",
       ps("b1", [68.6, 24.6]), mv("n9", [68, 6], delay=0.3), ps("b1", [68.6, 6.6], after=True), dr("n9", "b1", [14, 18], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit dem hinteren Fuß annehmen und gleich weiterspielen.", "Mit dem hinteren Fuß annehmen",
    "Der Spieler in der Mitte steht offen, die Brust zeigt zur Seite und nicht zum Passgeber. So nimmt er den Ball mit dem hinteren Fuß an und dreht dabei schon auf. Ohne Zwischenschritt geht der Ball weiter, und das Spiel wird schneller.",
    sp(**NACH), [B("b1", *F("n4")), B("b2", *F("n11"))] + ERSATZ,
    [S("Offen stehen, Blick zum Ball", "Spieler zwei kommt nach vorn und steht offen, die Brust zur Seite. Er schaut zu Spieler vier, und der legt ab.",
       mv("n2", [42, 28]), bl("n2", POS["n4"], after=True), ps("b1", [42.6, 28.6], after=True)),
     S("Hinterer Fuß, sofort weiter", "Er nimmt mit dem hinteren Fuß an und dreht dabei auf. Ohne Zwischenschritt spielt er durch zu Spieler zehn. So geht es schneller.",
       bl("n2", kurz((42, 28), POS["n10"]), von=POS["n4"], dauer=1.3), drehen("n2", POS["n10"], gegen=True, delay=0.4), ps("b1", F("n10"), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
