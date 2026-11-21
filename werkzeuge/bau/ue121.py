import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 24-P5: 45 x 20 Yards, gedreht (Tor rechts): Feld x 6-94, y 12-48, Zonengrenzen x 25, 49.5, 73. Minitore für den Konter links.
T = P("T", "c", 4, 5, "T")
CB = [B("c1", 6.5, 5.6), B("c2", 2, 7.5)]
POS = {"n10": (20, 20), "n9": (20, 40), "r4": (35, 28), "r6": (60, 32), "r5": (80, 30), "r2": (40, 5), "r3": (60, 5), "r8": (78, 5)}
def sp(d=None):
    d = dict(d or POS)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k", "t", 90, 30, "TW"), T]
LINES = [rect(6, 12, 88, 36)] + [line(x, 12, x, 48) for x in (25, 49.5, 73)]
TORE = [{"x": 94, "y": 30, "side": "right"}, {"x": 6, "y": 17, "side": "left"}, {"x": 6, "y": 43, "side": "left"}]
u = {"title": "Zwei gegen eins durch drei Zonen", "code": "UE-121", "kind": "Spielform",
 "focuses": ["Dribbling", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 9, "players_max": 12, "field_size": "41 x 18 m",
 "description": "Zwei Angreifer von Team Neon spielen sich durch drei Zonen bis zum Tor. In jeder Zone wartet ein Verteidiger von Team Rot, sodass immer zwei gegen eins gespielt wird. Ein geschlagener Verteidiger darf nicht zurück. Erobert ein Verteidiger den Ball, kontert er auf eines der beiden Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 18 Metern, in eine Startzone und drei Zonen geteilt. Rechts ein großes Tor mit Torhüter, links zwei Minitore für den Konter.",
  "Verteilen: Die Angreifer von Team Neon starten paarweise links. In jeder der drei Zonen steht ein Verteidiger von Team Rot, weitere warten am Rand. Der Trainer hat die Bälle.",
  "Ablauf: Das Paar dribbelt und kombiniert durch die drei Zonen. In jeder Zone wird der Verteidiger aktiv, sobald die Angreifer hineinkommen, und darf nicht in die nächste Zone folgen. In der letzten Zone schließen sie ab. Ein Tor gibt einen Punkt.",
  "Wechsel: Erobert ein Verteidiger den Ball, darf er auf eines der Minitore kontern. Nach zwei Angriffen wechseln die drei Verteidiger."],
 "organisation_show": ORG,
 "coaching_points": ["Im zwei gegen eins entschlossen angreifen", "Als Verteidiger so stehen, dass der Weg nach vorn zu ist", "Im letzten Drittel kaltschnäuzig abschließen", "Geduld oder Tempo: die Lage lesen und genau passen"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für Feld und Zonen", "Mehrere Bälle beim Trainer", "Leibchen in drei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Zwei gegen eins durch drei Zonen. Ein Angreiferpaar überspielt nacheinander drei Verteidiger und schließt ab.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 21.6, 20.6)] + CB,
  "steps": [
   S("Erste Zone", "Neon neun startet in die erste Zone, und Neon zehn spielt ihn an. Rot vier wird aktiv und greift Neon neun an.",
     mv("n9", [34, 41]), ps("b1", [35.6, 41.6], delay=0.3), mv("r4", [37, 36], delay=0.5)),
   S("Zweite Zone", "Neon neun dribbelt in die zweite Zone, Rot vier darf nicht folgen. Gleichzeitig läuft Neon zehn oben mit. Rot sechs greift Neon neun an, der zu Neon zehn spielt.",
     dr("n9", "b1", [54, 44]), mv("n10", [66, 20]), mv("r6", [52, 38], delay=0.3), ps("b1", [67.6, 20.6], after=True)),
   S("Letzte Zone und Abschluss", "Neon zehn dribbelt in die letzte Zone, Rot fünf kommt heraus. Neon zehn spielt quer zu Neon neun, der ins Tor schießt. Das gibt einen Punkt für Team Neon.",
     dr("n10", "b1", [76, 22]), mv("r5", [78, 26], delay=0.2), mv("n9", [80, 40]), ps("b1", [81.6, 40.6], after=True), ps("b1", [93.5, 35], after=True))],
  "dims": [{"x1": 6, "y1": 58.6, "x2": 94, "y2": 58.6, "text": "41 m"}, {"x1": 98, "y1": 12, "x2": 98, "y2": 48, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Läuft der Verteidiger zu früh in den Passweg, dribbelt der Angreifer selbst.", "Täuschen statt passen",
    "Rechnet der Verteidiger zu früh mit dem Pass und läuft in den Passweg, täuscht der Angreifer den Pass nur an. Dann dribbelt er in den frei gewordenen Raum und kommt ohne Gegner in die nächste Zone.",
    sp(dict(POS, n10=(24, 24), n9=(24, 44), r4=(35, 30))), [B("b1", 25.6, 24.6)] + CB,
    [S("Pass angetäuscht", "Neon zehn täuscht den Pass zu Neon neun an. Rot vier läuft sofort in den Passweg.",
       mv("r4", [31, 38]), dr("n10", "b1", [27, 25], delay=0.2)),
     S("Rein in den Raum", "Jetzt ist vorn alles frei. Neon zehn dribbelt mit Tempo in die zweite Zone.",
       dr("n10", "b1", [40, 22]), dr("n10", "b1", [54, 20], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der erste Verteidiger darf in die zweite Zone zurück.", "Zwei gegen zwei",
    "Der Verteidiger aus der ersten Zone darf jetzt in die zweite Zone nachlaufen. Dort wird zwei gegen zwei gespielt. Die Angreifer müssen das merken und schnell durchbrechen, bevor der zweite Verteidiger da ist. Die Verteidiger stehen dabei eng zusammen.",
    sp(dict(POS, n10=(44, 22), n9=(42, 42), r4=(30, 30))), [B("b1", 45.6, 22.6)] + CB,
    [S("Verteidiger läuft nach", "Gleichzeitig sprintet Rot vier in die zweite Zone zurück, und Neon zehn spielt schnell zu Neon neun.",
       mv("r4", [50, 27]), ps("b1", [43.6, 42.6], delay=0.2)),
     S("Schnell durchbrechen", "Neon neun dribbelt sofort an Rot sechs vorbei in die letzte Zone, bevor die beiden Verteidiger zusammenstehen.",
       dr("n9", "b1", [62, 45]), dr("n9", "b1", [75, 42], after=True), mv("r6", [58, 37], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
