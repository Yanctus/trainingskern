import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 13-P4 (U12-U14, Woche 16 Phase 5): How to Defend Overloaded (Jockeying). 30 x 30 Yards = Feld x 26-74, y 5-53 (27 x 27 m),
# Mittellinie und Mittelachse gestrichelt, oben ein Jugendtor mit Torwart. Gedreht (180 Grad): im PDF liegt das Tor unten.
# Neben dem Feld links und rechts je eine Hütchenreihe zum Rückwärtslaufen (Jockeying), an den Ecken der Torlinie je ein
# Hütchen zum Berühren (im PDF rot, hier neon). Pink/gold (Verteidiger) + grüner Torwart -> Team Neon (n1 TW, 3, 4, 5, 6),
# blau (Angreifer) -> Team Rot (7, 10, 11 im Feld, Nummern wie im Video; die wartenden Angreifer 8, 9 und der sechste stehen nur im Text, wegen der Maßlinie).
# Ein Trainer statt zwei (der zweite Trainer im PDF entfällt). Wertung im Original nicht genannt: hier Treffer = Punkt für Rot,
# Ballgewinn oder Torwart hält = Punkt für Neon (ergänzt, damit die Runde ein Ergebnis hat).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 6.5, 44.5, "T")
POS = {"n1": (50, 8.5), "n6": (15, 28), "n3": (6.5, 28), "n4": (85, 28), "n5": (93.5, 28),
       "r10": (50, 51.5), "r7": (38, 44), "r11": (62, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 10.1, 48), B("s2", 6.5, 48)]
LINES = [rect(26, 5, 48, 48), line(26, 29, 74, 29), line(50, 5, 50, 53)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(20, y) for y in (22, 17, 12)] + [C(80, y) for y in (22, 17, 12)] + [C(26, 5, "neon"), C(74, 5, "neon")]

u = {"title": "In Unterzahl verteidigen", "code": "UE-179", "kind": "Übungsform",
 "focuses": ["Verteidigen", "1 gegen 1", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 11, "field_size": "27 x 27 m",
 "description": "Ein Verteidiger läuft seitlich und rückwärts an einer Hütchenreihe entlang und übt so das Zurückweichen mit kleinen Schritten. Dann läuft er ins Feld und verteidigt gegen zwei Angreifer, die vorher im Dreieck gepasst haben. Er stellt sich seitlich, lenkt den Angreifer nach außen und auf den schwachen Fuß. Später verteidigen zwei Spieler gemeinsam gegen drei.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern mit Mittellinie und einem Jugendtor oben. Links und rechts neben dem Feld je eine Reihe aus drei Hütchen, an den Ecken der Torlinie je ein Hütchen.",
  "Verteilen: Team Neon wartet mit je zwei Verteidigern an beiden Seiten, ein Torwart steht im Tor. Team Rot steht unten, drei Angreifer im Feld, die anderen warten unter dem Feld. Der Trainer steht links mit Bällen.",
  "Ablauf: Der Verteidiger läuft rückwärts an den Hütchen entlang, berührt das Eckhütchen und läuft zur Mittellinie. Team Rot passt im Dreieck. Läuft der Verteidiger in die untere Hälfte, greifen zwei Angreifer an.",
  "Wertung und Wechsel: Ein Treffer gibt einen Punkt für Team Rot. Ballgewinn oder Torwart hält gibt einen Punkt für Team Neon. Danach startet der nächste Verteidiger von der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Seitlich stehen, Knie beugen, kleine Schritte", "Den Angreifer in eine Richtung lenken", "Den Angreifer auf seinen schwachen Fuß zwingen", "Zu zweit reden und die Passwege zumachen"],
 "materials": ["1 Jugendtor", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "In Unterzahl verteidigen. Ein Verteidiger übt das Zurückweichen und verteidigt dann allein gegen zwei Angreifer.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 52.1)] + ERSATZ,
  "steps": [
   S("Rückwärts an den Hütchen", "Spieler sechs läuft seitlich und rückwärts an den Hütchen entlang, mit kleinen Schritten und gebeugten Knien. Gleichzeitig passen sich Spieler zehn, Spieler sieben und Spieler elf den Ball im Dreieck zu.",
     mv("n6", [13.5, 22]), mv("n6", [15.5, 17], after=True), mv("n6", [13.5, 12], after=True), mv("n6", [15.5, 7.5], after=True),
     ps("b1", [38.6, 44.6]), ps("b1", [62.6, 44.6], after=True)),
   S("Hütchen und Mittellinie", "Spieler sechs berührt das Hütchen an der Ecke und läuft schnell zur Mittellinie.",
     mv("n6", [21.5, 6]), mv("n6", [38, 26], after=True)),
   S("Zwei gegen eins", "Spieler sechs läuft in die untere Hälfte. Das ist das Startsignal: Spieler elf dribbelt los, und Spieler sieben läuft mit nach vorn.",
     mv("n6", [46, 32]), dr("r11", "b1", [59, 34], delay=0.3), mv("r7", [36, 30], delay=0.3)),
   S("Nach außen lenken", "Spieler sechs stellt sich seitlich und lenkt Spieler elf nach außen. Spieler elf schießt aus spitzem Winkel, und der Torwart fängt den Ball. Das gibt einen Punkt für Team Neon. Jetzt startet Spieler vier auf der anderen Seite.",
     mv("n6", [54, 27]), dr("r11", "b1", [66, 22], delay=0.2), mv("n1", [55, 8.5], after=True), ps("b1", [55.6, 9.1], after=True))],
  "dims": dims(26, 74, 5, 53, "27 m", "27 m", rx=77)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Angreifer auf seinen schwachen Fuß lenken.", "Auf den schwachen Fuß",
    "Lässt der Verteidiger den Angreifer auf seinen starken Fuß, wird es gefährlich. Darum stellt er sich seitlich so hin, dass der Angreifer nur nach außen und mit dem schwachen Fuß weiterkommt. So hat der Angreifer weniger Möglichkeiten.",
    sp(n6=(48, 25), r11=(57, 35), r7=(38, 35)), [B("b1", 57.6, 35.6)] + ERSATZ,
    [S("Seitlich stellen", "Spieler elf dribbelt auf Spieler sechs zu. Spieler sechs steht seitlich und macht den Weg zur Mitte zu. Spieler elf muss nach außen, auf seinen schwachen Fuß.",
       dr("r11", "b1", [61, 29]), mv("n6", [53, 23], delay=0.2)),
     S("Ball erobert", "Mit dem schwachen Fuß legt sich Spieler elf den Ball zu weit vor. Spieler sechs geht dazwischen und erobert den Ball, und das gibt einen Punkt für Team Neon.",
       mv("n6", [61, 18.5]), ps("b1", [61.6, 19.1], delay=0.3))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Zu zweit die Passwege zumachen.", "Zu zweit verteidigen",
    "Jetzt starten zwei Verteidiger gleichzeitig, einer von jeder Seite, gegen drei Angreifer. Der erste stellt sich so, dass ein Passweg zu ist. Der zweite ahnt, wohin der Pass geht, und fängt ihn ab.",
    sp(n6=(58.5, 22), n4=(41.5, 22), r10=(50, 38), r11=(32, 38), r7=(68, 38)), [B("b1", 50.6, 38.6)] + ERSATZ,
    [S("Passweg zu", "Spieler zehn hat den Ball. Spieler sechs rückt heraus und stellt sich so, dass der Pass zu Spieler sieben nicht geht. Spieler vier schiebt mit.",
       mv("n6", [57, 31]), mv("n4", [43, 27], delay=0.2)),
     S("Abgefangen", "Spieler zehn muss zu Spieler elf passen. Spieler vier hat das geahnt, geht dazwischen und fängt den Ball ab. Das gibt einen Punkt für Team Neon.",
       mv("n4", [41, 38]), ps("b1", [41.6, 38.6], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
