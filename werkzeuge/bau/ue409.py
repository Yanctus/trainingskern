import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 32-P12 (U15-U17, Woche 39 Phase 2): Diamond Technical Passing and Movement. 15 x 15 Yards = 14 x 14 m, Feld x 25-75, y 5-55.
# Ausrichtung wie im PDF (Start unten, die Raute öffnet sich nach oben, erster Pass nach rechts). Nur Team Neon, Nummern wie im
# Video: Start 4 (mit Ball), dahinter 7 und 6, rechts 8, oben 10, links 11. Je ein Hütchen an jeder Station, außen neben dem
# Spieler (im PDF innen daneben; dort lägen sie in den Lauf- und Passwegen). Wartende versetzt nebeneinander (3D-Abstand).
# Ein Trainer statt einem mit Bällen rechts außen, hier rechts oben neben dem Feld.
# Ablauf nach PDF, Ton und Video: 4 spielt zu 8, Prallpass zurück in den Lauf von 4, 4 spielt durch auf 10 (oben), 10 legt ab für
# 8, der nach innen gekommen ist, 8 spielt quer zu 11, 11 spielt den letzten Pass zurück zum Start, und Spieler sieben beginnt.
# Jeder folgt seinem Pass zur nächsten Station (4 nach rechts, 8 nach oben, 10 nach links, 11 ans Ende der Schlange).
# Der PDF-Text sagt „restart from the other side“; im Video beginnt jede Runde wieder unten mit dem Pass nach rechts. Wie im Video.
# Keine Punkte (Technik): Die Runde ist fertig, wenn der Ball wieder am Start ist.
# Fassungen: Coaching-Punkt = PDF Key Coaching Point (erst vom Ball weg täuschen, dann antreten und im freien Raum annehmen),
# Steigerung = PDF Progression (anderes Passmuster: 8 dreht ab und bekommt den Ball im Lauf, 10 täuscht und bekommt ihn im freien
# Raum, dann geht es zu 11 auf die andere Seite).
# Sichtkegel aus Text („Visualise next pass destination“): Spieler vier schaut vor dem Steilpass zu Spieler zehn; Spieler acht schaut
# zum Ball und schwenkt nach der Annahme zu Spieler elf (bl mit von). Kein Aufdrehen auf der Stelle, darum kein Drehpfeil.
# Keine Dublette: UE-239 (45-P12, V aus fünf Stationen), UE-392 (WU-37, Y-Form), UE-384 (34-P4, vier Quadrate) und
# UE-374 (87-P5, Rondo in der Raute) haben andere Aufstellung und andere Abläufe. UE-408 (32-P8) ist ein Rondo mit Gegnern.
T = P("T", "c", 81, 9, "T")
ERSATZ = [B("s1", 84.5, 6.5), B("s2", 84.5, 12)]
POS = {"n4": (52, 51), "n7": (43.5, 52), "n6": (35, 52.5), "n8": (71, 30), "n10": (50, 9), "n11": (29, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(25, 5, 50, 50)]
CONES = [C(56, 54), C(74.5, 34), C(45, 6.5), C(25.5, 34)]
DIMS = dims(25, 75, 5, 55, "14 m", "14 m", rx=91)
MITTE = (57, 38)   # dort bekommt Spieler vier den Prallpass
INNEN = (63, 20)   # dort bekommt Spieler acht die Ablage

u = {"title": "Passmuster in der Raute", "code": "UE-409", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 6, "players_max": 8,
 "field_size": "14 x 14 m",
 "description": "Eine Passfolge ohne Gegner, vier Stationen stehen als Raute wie im Mittelfeld. Der Ball geht vom Start nach rechts, kommt zurück, wird steil nach oben gespielt, abgelegt und quer auf die andere Seite gespielt. Von dort geht er zurück zum Start, und der Nächste beginnt. Jeder läuft seinem Pass hinterher zur nächsten Station, möglichst mit einem Kontakt.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern. Vier Hütchen als Raute, unten der Start, rechts, oben und links je eine Station.",
  "Verteilen: Je ein Spieler steht rechts, oben und links. Alle anderen warten am Start unten, der Erste hat den Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass nach rechts, Prallpass zurück, steil nach oben. Oben wird abgelegt für den Spieler von rechts, der quer nach links spielt. Von links geht der Ball zurück zum Start.",
  "Wechsel: Jeder läuft seinem Pass hinterher zur nächsten Station, der Spieler links geht ans Ende der Schlange. Am Start ist Zeit zum Durchatmen. Ist der Ball zurück, beginnt der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Mit einem Kontakt spielen, wo es geht", "Passe so, dass der Mitspieler direkt weiterspielen kann", "Schon vorher wissen, wohin der nächste Pass geht", "Mal links, mal rechts passen und laut ansagen"],
 "materials": ["4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passmuster in der Raute. Vier Stationen wie im Mittelfeld, der Ball läuft einmal durch die Raute und zurück zum Start. Jeder folgt seinem Pass.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", *f(POS["n4"]))] + ERSATZ,
  "steps": [
   S("Pass nach rechts, Prallpass", "Spieler vier spielt flach nach rechts zu Spieler acht und startet sofort hinterher Richtung Mitte. Der Ball kommt direkt zurück in seinen Lauf.",
     ps("b1", f(POS["n8"])), mv("n4", list(MITTE), delay=0.3), ps("b1", f(MITTE), after=True)),
   S("Steil nach oben", "Spieler vier hebt den Kopf und spielt steil nach oben zu Spieler zehn. Spieler acht kommt schon nach innen.",
     bl("n4", list(POS["n10"])), ps("b1", f(POS["n10"]), after=True), mv("n8", list(INNEN), delay=0.4)),
   S("Ablegen und quer", "Spieler zehn legt mit einem Kontakt ab auf Spieler acht. Der schaut zum Ball, nimmt ihn mit und spielt sofort quer zu Spieler elf.",
     bl("n8", list(POS["n10"])), ps("b1", f(INNEN), after=True), bl("n8", list(POS["n11"]), von=list(POS["n10"]), dauer=1.3, after=True),
     ps("b1", f(POS["n11"]), after=True)),
   S("Zurück zum Start, alle rücken weiter", "Spieler sieben geht an den Start, und Spieler elf spielt ihm den Ball. Jeder läuft seinem Pass hinterher. Spieler vier geht nach rechts, Spieler acht nach oben, Spieler zehn nach links, Spieler elf ans Ende. Gezählt wird nichts, und jetzt startet Spieler sieben.",
     mv("n7", list(POS["n4"])), ps("b1", f(POS["n4"]), after=True), mv("n4", list(POS["n8"]), delay=0.3), mv("n8", list(POS["n10"]), delay=0.3),
     mv("n10", list(POS["n11"]), delay=0.3), mv("n11", [42, 44], delay=1.2), mv("n11", list(POS["n7"]), after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst täuschen, dann antreten.", "Erst täuschen, dann antreten",
    "Oben wartet der Spieler nicht einfach auf den Ball. Er geht erst ein paar Schritte weg, als wolle er den Pass dort haben. Dann tritt er im richtigen Moment an und nimmt den Ball im freien Raum an.",
    sp(n4=MITTE, n8=INNEN), [B("b1", *f(MITTE))] + ERSATZ,
    [S("Erst weg vom Ball", "Spieler vier hat den Prallpass bekommen. Spieler zehn geht oben ein paar Schritte nach links, als wolle er den Ball dort.",
       mv("n10", [40, 11])),
     S("Antreten in den freien Raum", "Jetzt tritt er an, mit vollem Tempo zurück zur Mitte. Genau in diesem Moment kommt der Pass von Spieler vier in seinen Lauf.",
       mv("n10", [50, 10]), ps("b1", [50.6, 10.6], delay=0.3)),
     S("Ablage für Spieler acht", "Spieler zehn legt direkt ab auf Spieler acht, und der Ball läuft weiter wie gewohnt.",
       ps("b1", f(INNEN)))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein neues Passmuster.", "Neues Passmuster",
    "Das Muster ändert sich. Spieler acht dreht nach dem Prallpass ab und bekommt den Ball im Lauf nach vorn. Spieler zehn täuscht kurz an und nimmt den Ball im freien Raum an. Von dort geht es auf die andere Seite zu Spieler elf.",
    sp(), [B("b1", *f(POS["n4"]))] + ERSATZ,
    [S("Pass und Prallpass", "Wie gehabt, Spieler vier spielt zu Spieler acht und bekommt den Ball direkt zurück.",
       ps("b1", f(POS["n8"])), mv("n4", list(MITTE), delay=0.3), ps("b1", f(MITTE), after=True)),
     S("Abdrehen, Ball im Lauf", "Spieler acht dreht sofort ab und sprintet nach vorn. Spieler vier spielt ihm den Ball in den Lauf. Oben täuscht Spieler zehn kurz zum Ball hin an.",
       mv("n8", [66, 17]), ps("b1", [66.6, 17.6], delay=0.5), mv("n10", [56, 10], delay=0.2)),
     S("Im freien Raum annehmen", "Jetzt geht Spieler zehn weg in den freien Raum nach links. Spieler acht spielt ihn dort an.",
       mv("n10", [40, 12]), ps("b1", [40.6, 12.6], delay=0.4)),
     S("Auf die andere Seite", "Spieler zehn spielt weiter zu Spieler elf. Von dort startet die nächste Runde, jetzt über die andere Seite.",
       ps("b1", f(POS["n11"])))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
