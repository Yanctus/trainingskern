import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 52-P5 (U12-U14, Woche 31 Phase 1): Centre Backs Playing Out From the Back. 20 x 30 Yards hochkant = Feld x 32-68, y 3-57
# (18 x 27 m), drei gleiche Zonen (Grenzen y 21 und 39 gestrichelt), oben und unten ein Jugendtor mit Torwart. Ausrichtung wie im
# PDF: Blau (greift an) -> Team Neon spielt nach oben, Pink (verteidigt) -> Team Rot. Nummern im PDF doppelt: Blau behält
# 4, 5 (Innenverteidiger), 8 (Mitte), 9 (Stürmer), Torwart 13 -> n1 "TW"; Pink neu: Stürmer 9 -> 11, Mitte 8 -> 6, Verteidiger
# 4/5 -> 2/3. Der Torwart oben (pink 1) steht als Torwart k ("TW", team t) im Tor, weil zwei Team-Torwarte mit "TW" doppelte
# Rückennummern wären; er hält nur und spielt nicht mit. Positionen leicht verschoben (3D-Abstand). Ein Trainer rechts neben dem Feld.
# Dass Team Rot nach Ballgewinn auf das untere Tor kontern darf ("Break to score", "react to losing possession"), ist ergänzt.
# Sichtkegel aus dem Ton ("help centre backs recognise when to step forward"): Spieler vier schaut nach dem Seitenwechsel ins
# Mittelfeld, in der Fassung Spieler fünf. Im Video sind nur Spieler hervorgehoben, kein Kegel eingezeichnet.
T = P("T", "c", 80, 30, "T")
ERSATZ = [B("s1", 83.6, 33.5), B("s2", 80, 33.5)]
POS = {"n1": (50, 55.5), "n4": (40, 47), "n5": (60, 47), "n8": (59, 30), "n9": (50, 20.6),
       "k": (50, 5), "r2": (41.5, 13), "r3": (58.5, 13), "r6": (41, 30), "r11": (50, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i in ("n1", "k") else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(32, 3, 36, 54), line(32, 21, 68, 21), line(32, 39, 68, 39)]
TORE = [{"x": 50, "y": 3, "side": "top", "size": "jugend"}, {"x": 50, "y": 57, "side": "bottom", "size": "jugend"}]

u = {"title": "Aufrücken und Überzahl schaffen", "code": "UE-216", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 27 m",
 "description": "Team Neon baut von hinten auf, Team Rot verteidigt. Das Feld hat drei Zonen: hinten drei gegen einen, in der Mitte eins gegen eins, vorn eins gegen zwei. Erst wenn ein Innenverteidiger mit Ball in die Mitte aufrückt, entsteht dort Überzahl. Kommt der Ball nach vorn, darf der Mittelfeldspieler mit, und es geht auf das Tor.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern in drei gleich große Zonen geteilt. Oben und unten steht je ein Jugendtor.",
  "Verteilen: Team Neon mit Torwart und zwei Innenverteidigern hinten, einem in der Mitte und einem Stürmer vorn. Team Rot mit einem Stürmer hinten, einem in der Mitte und zwei Verteidigern vorn. Oben steht ein zweiter Torwart im Tor. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Alle bleiben in ihren Zonen. Ein Innenverteidiger verlagert, rückt mit Ball in die Mitte auf und schafft so zwei gegen einen. Kommt der Ball nach vorn, darf der Mittelfeldspieler mit, dann ist es zwei gegen zwei.",
  "Wertung und Wechsel: Ein Treffer oben gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, kontert es auf das untere Tor, und ein Treffer gibt einen Punkt für Team Rot. Danach startet der Torwart von Team Neon mit einem neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Erst die Seite wechseln, dann aufrücken", "Mit dem hinteren Fuß annehmen und gleich Tempo aufnehmen", "Mutig in die Mitte dribbeln und Überzahl schaffen", "Breit stehen und nach Ballverlust sofort nachsetzen"],
 "materials": ["4 Hütchen", "2 Jugendtore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufrücken und Überzahl schaffen. Team Neon baut von hinten auf, und ein Innenverteidiger dribbelt mit Ball ins Mittelfeld.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(32, 3, 36, 54), "players": sp(), "balls": [B("b1", 60.6, 47.6)] + ERSATZ,
  "steps": [
   S("Drei gegen einen", "Spieler fünf hat den Ball. Spieler elf läuft ihn an. Alle bleiben in ihren Zonen: hinten drei gegen einen, in der Mitte eins gegen eins, vorn eins gegen zwei.",
     mv("r11", [55, 43])),
   S("Seite wechseln", "Spieler fünf spielt quer zu Spieler vier. Spieler vier nimmt mit dem hinteren Fuß an und schaut nach vorn: Vor ihm ist Platz.",
     ps("b1", [40.6, 47.6]), bl("n4", [50, 30], after=True)),
   S("Aufrücken", "Spieler vier dribbelt mutig in die Mitte. Jetzt sind es dort zwei gegen einen. Spieler sechs geht auf ihn zu, also spielt Spieler vier zu Spieler acht.",
     dr("n4", "b1", [40, 36]), mv("r6", [44, 32], delay=0.4), ps("b1", [59.6, 30.6], after=True)),
   S("Vorn zwei gegen zwei: Punkt", "Spieler acht spielt zu Spieler neun und läuft mit nach vorn. Spieler neun legt ab, und Spieler acht trifft. Das gibt einen Punkt für Team Neon. Dann startet der Torwart von Team Neon mit einem neuen Ball.",
     ps("b1", [50.6, 21.2]), mv("n8", [63, 16], delay=0.3), mv("r3", [56, 17], delay=0.3), ps("b1", [63.6, 16.6], after=True), ps("b1", [55, 3.4], after=True))],
  "dims": dims(32, 68, 3, 57, "18 m", "27 m", rx=74)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Breit stehen und über den Torwart verlagern.", "Über den Torwart",
    "Die Innenverteidiger stehen weit auseinander. So kann ein Stürmer nicht beide zustellen. Presst er einen, geht der Ball über den Torwart zum anderen, und der rückt sofort auf.",
    sp(), [B("b1", 40.6, 47.6)] + ERSATZ,
    [S("Zurück zum Torwart", "Spieler vier hat den Ball, und Spieler elf presst ihn. Spieler vier spielt zurück zum Torwart.",
       mv("r11", [45, 42]), ps("b1", [50.6, 56.1], delay=0.3)),
     S("Zum freien Spieler", "Spieler elf läuft dem Ball hinterher. Der Torwart spielt zu Spieler fünf, und der schaut sofort nach vorn ins Mittelfeld.",
       mv("r11", [50, 49]), ps("b1", [60.6, 47.6], delay=0.3), bl("n5", [60, 30], after=True)),
     S("Hinein in die Mitte", "Spieler fünf dribbelt in die Mitte. Spieler sechs kommt zu spät, und Spieler fünf spielt zu Spieler acht. Der spielt weiter nach vorn zu Spieler neun.",
       dr("n5", "b1", [61, 38]), mv("r6", [52, 33], delay=0.3), mv("n8", [65, 27], delay=0.3), ps("b1", [65.6, 27.6], after=True), ps("b1", [50.6, 21.2], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Team Rot verteidigt frei.", "Rot verteidigt frei",
    "Jetzt darf Team Rot über alle Zonen verteidigen und sich immer wieder anders aufstellen. Team Neon bleibt in den Zonen, bis ein Innenverteidiger aufrückt oder der Ball nach vorn kommt. Die Innenverteidiger müssen erkennen, wo die Lücke ist.",
    sp(n4=(37, 47), n5=(61, 47), n8=(59, 31), r11=(46, 40), r6=(37, 31)), [B("b1", 37.6, 47.6)] + ERSATZ,
    [S("Rot presst", "Spieler sechs verlässt die Mitte und presst Spieler vier, Spieler elf rückt nach. Spieler vier spielt quer zu Spieler fünf.",
       mv("r6", [38, 40]), mv("r11", [46, 43.5]), ps("b1", [61.6, 47.6], delay=0.3)),
     S("Hineindribbeln", "Spieler fünf dribbelt nach innen ins Mittelfeld. Spieler elf geht auf ihn, also ist Spieler acht frei und bekommt den Ball.",
       dr("n5", "b1", [55, 38]), mv("r11", [50, 39], delay=0.3), mv("n8", [62, 24], delay=0.3), ps("b1", [62.6, 24.6], after=True)),
     S("Nach vorn: Punkt", "Spieler acht spielt zu Spieler neun, und der schießt. Das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 21.2]), ps("b1", [46, 3.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
