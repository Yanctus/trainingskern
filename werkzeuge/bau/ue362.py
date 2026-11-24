import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 49-P5 (U15-U17, Woche 22 Phase 5): Transitional Rondo (Develop Ball Retention Under Pressure). 15 x 25 Yards = 14 x 23 m
# (gerundet 14 x 25 m). FELD QUER (langes Feld, Verhältnis 1,7; Vorbild ue317.py): x 9-89 (25 m), y 4-51 (14 m), Minitore an den
# kurzen Seiten links und rechts. Direkt quer geplant (kein R()): PDF oben -> rechts, unten -> links, links -> oben, rechts -> unten.
# Gelb (Mittelfeld-Drei 10, 8, 4, Nummern wie im PDF) -> Team Neon, Navy (fünf Spieler am Ball) -> Team Rot, neu nummeriert
# (4, 8, 10 doppelt): 4 -> 3, 8 -> 7, 10 -> 11; 6 und 9 bleiben. Vier Hütchen an den Seitenlinien markieren wie im PDF die
# spätere Druckzone. Ein Trainer, unten an der Seitenlinie. Positionen leicht verschoben (3D-Abstand).
# Annahme: In der Steigerung kontert Team Neon nach dem Ballgewinn in der Zone auf das Minitor auf der Seite, von der Team Rot
# kommt (im PDF nur "breakout & finish"). Fassungen: PDF Progression (Druckzone in der Mitte, gerichtetes Spiel) als
# Steigerung und PDF Key Coaching Point (alle Passwege nach vorn zu) als Coaching-Punkt, mit Anspielstationen (opt).
# Sichtkegel aus Text und Ton ("Recognise the right trigger to press", "quick break"); im Video nicht eingezeichnet, Richtung
# aus dem Sinn: Spieler acht schaut auf den kurzen Pass (Auslöser), Spieler zehn schaut nach dem Abfangen zu Spieler vier
# (Kegel mit von, Drehpfeil).
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
T = P("T", "c", 63, 55.3, "T")
ERSATZ = [B("s1", 66.5, 55.8), B("s2", 69, 55.8)]
POS = {"r11": (28, 33), "r9": (48, 49), "r7": (48, 6), "r3": (51, 28), "r6": (75, 33),
       "n10": (60.5, 17), "n8": (61, 38), "n4": (40, 26)}
POS1 = {"r6": (83, 33), "r3": (64, 27), "r7": (41, 9), "r11": (45.4, 45.8), "r9": (23, 27),
        "n10": (54, 15), "n8": (54, 38), "n4": (39, 26.4)}
POS2 = {"r6": (75, 27), "r3": (62, 28), "r7": (44, 8), "r11": (44, 47), "r9": (23, 27),
        "n10": (53, 18), "n8": (53, 37.5), "n4": (44, 27.5)}
def sp(pos=POS):
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in pos.items()] + [T]
ZX0, ZX1 = 35.4, 61
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
LINES1 = LINES + [{"type": "zone", "x": ZX0, "y": FY0, "w": ZX1 - ZX0, "h": FY1 - FY0}]
MY = (FY0 + FY1) / 2
TORE = [{"x": FX0, "y": MY, "side": "left"}, {"x": FX1, "y": MY, "side": "right"}]
CONES = [C(ZX0, FY0), C(ZX1, FY0), C(ZX0, FY1), C(ZX1, FY1)]
# Nur die Länge als Maßlinie (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "14 m")[:1]

u = {"title": "Rondo 5 gegen 3 mit Minitoren", "code": "UE-362", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 8,
 "field_size": "14 x 25 m",
 "description": "Ein Rondo fünf gegen drei mit einem Minitor an jedem Ende. Die drei Mittelfeldspieler von Team Neon arbeiten zusammen, machen die Passwege zu und pressen, sobald ein Pass zu kurz ist oder die Annahme springt. Nach dem Ballgewinn kontern sie sofort auf eins der beiden Minitore. Schafft Team Rot zehn Pässe am Stück, darf Team Rot auch abschließen.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 25 Metern. An jeder kurzen Seite steht ein Minitor. Vier Hütchen an den Seitenlinien teilen die Mitte ab.",
  "Verteilen: Team Rot hat fünf Spieler und den Ball, Team Neon verteidigt mit drei. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Team Rot lässt den Ball laufen. Team Neon schiebt als Dreierkette mit, stellt die Passwege zu und presst auf ein Zeichen. Nach dem Ballgewinn geht es sofort auf ein Minitor. Nach zehn Pässen am Stück darf Team Rot selbst auf ein Minitor schießen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach jedem Treffer spielt der Trainer einen neuen Ball zu Team Rot. Nach ein paar Minuten tauschen drei andere Spieler in die Mitte, das Team mit weniger Punkten macht zehn Liegestütze."],
 "organisation_show": ORG,
 "coaching_points": ["Zu kurzer Pass oder schlechte Annahme? Drauf!", "Zu dritt die Passwege zumachen", "Ball gewonnen? Sofort aufs Minitor", "Eng bleiben, durch uns geht kein Pass"],
 "materials": ["2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rondo fünf gegen drei mit Minitoren. Drei Mittelfeldspieler machen zusammen die Passwege zu, holen sich den Ball und kontern sofort auf ein Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 28.6, 33.6)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Ball läuft, die Drei schiebt", "Team Rot lässt den Ball laufen. Spieler elf spielt zu Spieler neun an die Seite. Die Drei schiebt sofort mit zum Ball.",
     ps("b1", [48.6, 49.6]), mv("n4", [44, 33], delay=0.3), mv("n8", [58, 39], delay=0.3), mv("n10", [57, 22], delay=0.3)),
   S("Weiter auf die andere Seite", "Spieler neun spielt weiter zu Spieler sechs. Wieder schieben alle drei mit, keiner rennt allein los.",
     ps("b1", [75.6, 33.6]), mv("n8", [66, 37], delay=0.3), mv("n10", [64, 24], delay=0.3), mv("n4", [46, 31], delay=0.3)),
   S("Kurzer Pass, das Zeichen", "Spieler acht hat den Ball im Blick. Spieler sechs spielt einen kurzen Pass zu Spieler drei. Das ist das Zeichen. Spieler acht und Spieler vier gehen sofort drauf.",
     bl("n8", [51, 28]), ps("b1", [51.6, 28.6], after=True), mv("n8", [57, 31], after=True), mv("n4", [45, 29], delay=1.2)),
   S("Pass abgefangen", "Unter Druck will Spieler drei raus zu Spieler sieben. Spieler zehn hat darauf gewartet. Er geht in den Passweg und hat den Ball.",
     mv("n10", [50, 16]), ps("b1", [50.6, 16.6], delay=0.3)),
   S("Konter aufs Minitor: Punkt", "Spieler zehn dreht auf, und Spieler vier startet Richtung Minitor. Der Pass kommt in den Lauf. Spieler vier schiebt ein, und das gibt einen Punkt für Team Neon. Dann spielt der Trainer einen neuen Ball zu Team Rot.",
     bl("n10", [31, 21.8], von=[51, 28], dauer=1.3), drehen("n10", [24, 24], delay=0.4), mv("n4", [24, 24], delay=0.3),
     ps("b1", [24.6, 24.6], after=True), ps("b1", [9.3, 27.5], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Eine Druckzone in der Mitte.", "Druckzone in der Mitte",
    "Die Drei verteidigt jetzt nur in der Zone in der Mitte. Team Rot spielt gerichtet, von einer Seite auf die andere. Kommt ein Pass durch die Zone, darf Team Rot auf das Minitor am anderen Ende schießen. Erobert die Drei den Ball in der Zone, kontert sie sofort.",
    sp(POS1), [B("b1", 83.6, 33.6)] + ERSATZ,
    [S("Von einer Seite auf die andere", "Spieler sechs startet auf dieser Seite und spielt zu Spieler drei. Die Drei schiebt in der Zone zum Ball.",
       ps("b1", [64.6, 27.6]), mv("n10", [58, 19], delay=0.3), mv("n8", [58, 38], delay=0.3), mv("n4", [47, 27], delay=0.3)),
     S("Kein Pass durch die Zone", "Spieler drei sucht Spieler neun hinter der Zone. Spieler vier steht genau im Weg. Also will er zu Spieler elf, und Spieler acht fängt den Ball ab.",
       mv("n8", [55, 37.5], delay=0.4), ps("b1", [55.6, 38.1], delay=0.6)),
     S("Ballgewinn in der Zone: Punkt", "Sofort geht Spieler zehn in die Tiefe. Spieler acht spielt ihn an, und er trifft ins Minitor. Das gibt einen Punkt für Team Neon.",
       mv("n10", [76, 21]), ps("b1", [76.6, 21.6], delay=0.6), ps("b1", [88.7, 27.5], after=True))],
    lines=LINES1, dims=DIMS),
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Alle Passwege nach vorn sind zu.", "Alle Wege nach vorn zu",
    "Die Drei steht so eng, dass jeder einen Passweg nach vorn zumacht. Team Rot findet keine Lücke und muss quer oder zurück spielen. Wer es trotzdem versucht, verliert den Ball. Dann geht es sofort nach vorn.",
    sp(POS2), [B("b1", 62.6, 28.6)] + ERSATZ,
    [S("Drei Wege, alle zu", "Spieler drei hat den Ball und schaut nach vorn. Drei Möglichkeiten hat er. Vor jeder steht ein Spieler von Team Neon.",
       opt("r3", [44, 8]), opt("r3", [44, 47], after=True), opt("r3", [23, 27], after=True)),
     S("Trotzdem durch die Mitte", "Spieler drei versucht es trotzdem durch die Mitte zu Spieler neun. Spieler vier steht im Weg und hat den Ball. Jetzt geht es schnell nach vorn.",
       ps("b1", [44.6, 28.1]))],
    lines=LINES1, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
