import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 69-P10 (U15-U17, Woche 22 Phase 5): Defending as a Midfield Three (Phase of Play). 50 x 45 Yards = 46 x 41 m (gerundet
# 45 x 40 m) = Feld x 22-78, y 5-55. Kein Großfeld (unter 60 m) und kein langes Feld (Verhältnis 1,1): hochkant wie im PDF.
# Oben das große Tor mit Strafraum und Torraum (Strafraum-Halbkreis weggelassen), unten vier Minitore (sie stehen für eine
# tiefe Viererkette). Zwei Zonenlinien gestrichelt wie im PDF. Ausrichtung wie im PDF: Team Rot baut vom eigenen Tor oben auf
# und greift die Minitore unten an, Team Neon verteidigt und kontert nach oben aufs große Tor.
# Pink (Verteidiger: Spitzen 10, 9, Mittelfeld-Drei 6, 4, 8, Nummern wie im PDF) -> Team Neon, Navy -> Team Rot,
# neu nummeriert (6, 8, 10 doppelt): 6 -> 7, 8 -> 11, 10 -> 12; 2, 3, 5 bleiben. Grüner Torwart ist der Torwart von Team Rot
# (r1, TW). Großes Tor "gross" (nur C- und B-Jugend). Ein Trainer statt zwei. Positionen leicht verschoben (3D-Abstand),
# der Torwart steht etwas links der Tormitte.
# Fassungen: PDF Progression 1 (Spitzen dürfen im tiefsten Drittel pressen) und Progression 2 (getroffenes Minitor ist zu,
# Team Neon lenkt dorthin; ein neonfarbenes Hütchen vor dem Minitor zeigt "zu", im Video gelb markiert).
# Sichtkegel aus Ton und PDF ("spatial awareness", "transitioning quickly to counter attack"); im Video nicht eingezeichnet,
# Richtung aus dem Sinn: Nach dem Ballgewinn schaut Spieler sechs nach vorn zu Spieler zehn.
T = P("T", "c", 13, 12, "T")
ERSATZ = [B("s1", 13, 16.5), B("s2", 16, 15)]
POS = {"r1": (45, 8), "r3": (56, 16), "r2": (28, 20), "r5": (74, 19), "r7": (47, 28), "r11": (28, 40), "r12": (73, 40),
       "n10": (37, 27), "n9": (64.5, 28), "n6": (42, 44), "n4": (51, 48), "n8": (60, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(22, 5, 56, 50), rect(32, 5, 36, 13.5), rect(41, 5, 18, 5.4), line(22, 26.4, 78, 26.4), line(22, 37.2, 78, 37.2)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"},
        {"x": 24.5, "y": 55, "side": "bottom"}, {"x": 40.5, "y": 55, "side": "bottom"},
        {"x": 59.5, "y": 55, "side": "bottom"}, {"x": 75.5, "y": 55, "side": "bottom"}]
DIMS = dims(22, 78, 5, 55, "45 m", "40 m", rx=87)
BALL = [B("b1", 45.6, 8.6)] + ERSATZ

u = {"title": "Zu dritt das Zentrum schützen", "code": "UE-361", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "45 x 40 m",
 "description": "Team Rot baut vom Torwart aus auf und will auf eins der vier Minitore treffen, die für eine tiefe Viererkette stehen. Team Neon verteidigt mit zwei Spitzen und einer Mittelfeld-Drei. Die Drei steht eng, lässt keinen Pass durch die Mitte und lockt Team Rot nach außen in die Falle. Nach dem Ballgewinn kontert Team Neon schnell aufs große Tor.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 40 Metern, mit zwei Linien in drei Zonen geteilt. Oben steht ein großes Tor mit Strafraum, unten stehen vier Minitore nebeneinander.",
  "Verteilen: Team Rot spielt mit Torwart und sechs Feldspielern. Team Neon hat zwei Spitzen und drei Mittelfeldspieler. Team Neon darf nur in den beiden Zonen pressen, die näher an den Minitoren liegen. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart von Team Rot eröffnet. Team Rot spielt nach vorn und schießt auf die Minitore. Team Neon bleibt kompakt, lenkt nach außen und presst, wenn ein Pass schlecht kommt oder ein Ball verspringt. Nach dem Ballgewinn geht es sofort aufs große Tor.",
  "Wertung: Ein Treffer in ein Minitor gibt einen Punkt für Team Rot. Ein Treffer aufs große Tor gibt einen Punkt für Team Neon. Nach jedem Treffer oder wenn der Ball ins Aus geht, startet wieder der Torwart."],
 "organisation_show": ORG,
 "coaching_points": ["Die Drei bleibt eng, kein Pass durch die Mitte", "Nach außen lenken, dann zuschnappen", "Reden, reden, reden", "Schlechter Pass oder schlechte Annahme? Drauf!"],
 "materials": ["1 großes Tor", "4 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zu dritt das Zentrum schützen. Team Neon verteidigt mit zwei Spitzen und drei Mittelfeldspielern. Die Drei hält die Mitte zu, lockt Team Rot nach außen und kontert nach dem Ballgewinn sofort nach vorn.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BALL, "dims": DIMS,
  "steps": [
   S("Torwart eröffnet nach außen", "Der Torwart von Team Rot spielt raus zu Spieler fünf. Spieler neun läuft an, aber von innen. So bleibt der Weg zurück in die Mitte zu. Die Drei schiebt ein Stück mit.",
     ps("b1", [74.6, 19.6]), mv("n9", [68, 26], delay=0.4), mv("n8", [63, 43], delay=0.5), mv("n4", [54, 47], delay=0.5), mv("n6", [45, 43], delay=0.5)),
   S("Pass in die Mitte, die Drei bleibt eng", "Spieler fünf spielt doch in die Mitte zu Spieler sieben. Spieler zehn drückt von hinten. Die Drei rückt eng zusammen, durch die Mitte geht kein Pass.",
     ps("b1", [47.6, 28.6]), mv("n10", [42, 26], delay=0.3), mv("n6", [44, 40], delay=0.4), mv("n4", [51, 42], delay=0.4), mv("n8", [58, 40], delay=0.4)),
   S("Raus nach außen, die Falle", "Spieler sieben weicht nach außen aus, zu Spieler elf. Genau da wollen wir ihn haben. Spieler sechs geht sofort drauf, Spieler vier sichert, Spieler acht schiebt nach.",
     ps("b1", [28.6, 40.6]), mv("n6", [33, 42], delay=0.3), mv("n4", [42, 45], delay=0.4), mv("n8", [51, 43], delay=0.4)),
   S("Annahme verspringt, Ball erobert", "Spieler elf springt der Ball vom Fuß. Das ist das Zeichen. Spieler sechs ist da und hat ihn. Er nimmt sofort den Kopf hoch, und Spieler zehn startet in die Tiefe.",
     ps("b1", [32, 44.5]), mv("n6", [31.4, 43.9], delay=0.2), mv("n10", [40, 16], delay=0.6), bl("n6", [39.5, 18.5], delay=0.8)),
   S("Schneller Konter: Punkt", "Spieler sechs spielt steil in den Lauf. Spieler zehn schließt ab und trifft, und das gibt einen Punkt für Team Neon. Danach eröffnet wieder der Torwart von Team Rot.",
     ps("b1", [40.6, 16.6]), ps("b1", [47, 5.3], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Spitzen pressen bis ganz vorn.", "Spitzen pressen ganz vorn",
    "Jetzt dürfen die Spitzen auch in der Zone vor dem großen Tor pressen. Sie laufen so an, dass Team Rot auf eine Seite muss. Dort wartet die Drei. Team Rot hat weniger Zeit und muss schneller entscheiden.",
    sp(), BALL,
    [S("Im Bogen anlaufen", "Der Torwart spielt kurz zu Spieler drei. Spieler neun läuft im Bogen an und macht die Seite zu Spieler fünf zu. Es bleibt nur der Weg nach links.",
       ps("b1", [56.6, 16.6]), mv("n9", [65, 21], delay=0.3), mv("n9", [60, 19], after=True)),
     S("Spieler zehn presst ganz vorn", "Spieler drei spielt zu Spieler zwei. Jetzt darf Spieler zehn bis ganz vorn und läuft ihn sofort an. Die Drei schiebt mit nach links.",
       ps("b1", [28.6, 20.6]), mv("n10", [33, 22], delay=0.3), mv("n6", [34, 37], delay=0.4), mv("n4", [43, 42], delay=0.4), mv("n8", [52, 41], delay=0.4)),
     S("Hektischer Pass, abgefangen", "Unter Druck spielt Spieler zwei hektisch nach vorn zu Spieler elf. Spieler sechs geht dazwischen und hat den Ball. Bis zum großen Tor ist es jetzt nicht mehr weit.",
       ps("b1", [29.6, 33.6]), mv("n6", [29, 33], delay=0.2))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Treffer schließt das Minitor.", "Minitore werden geschlossen",
    "Trifft Team Rot ein Minitor, ist es für die nächsten Runden zu. Hier ist das Minitor ganz außen links schon zu, das Hütchen davor zeigt es. Team Neon lenkt das Spiel genau dorthin. Schließt Team Rot alle vier Minitore, gewinnt Team Rot.",
    sp(), BALL,
    [S("Hin zum geschlossenen Tor", "Der Torwart spielt zu Spieler drei. Spieler neun läuft von außen an. Der Ball muss nach links, dorthin, wo das Minitor schon zu ist.",
       ps("b1", [56.6, 16.6]), mv("n9", [65, 21], delay=0.3), mv("n9", [60, 19], after=True)),
     S("Alle schieben zum Ball", "Über Spieler zwei kommt der Ball zu Spieler elf. Die Drei schiebt ganz nach links. Spieler zwölf auf der anderen Seite bleibt frei, der Pass dorthin ist zu weit.",
       ps("b1", [28.6, 20.6]), ps("b1", [28.6, 40.6], after=True), mv("n10", [34, 24], delay=0.3), mv("n6", [31, 45], delay=0.8), mv("n4", [39, 41], delay=0.8), mv("n8", [47, 43], delay=0.8)),
     S("Überzahl am Ball", "Am Ball hat Team Neon jetzt Überzahl. Spieler sechs drückt, Spieler vier kommt dazu und erobert den Ball. Die offenen Minitore sind weit weg.",
       mv("n6", [29.5, 43]), mv("n4", [32, 39], delay=0.3), ps("b1", [32.6, 39.6], delay=0.6))],
    cones=[C(28, 51, "neon", id="z1")], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
