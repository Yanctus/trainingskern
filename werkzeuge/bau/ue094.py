import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-18: Bahnen von 20 Yards, gedreht (Start links, Minitore rechts). Zwei von drei Bahnen gezeigt: Neon (y 20) und Rot (y 40).
# Paare sitzen hintereinander: Spieler eins und zwei, drei und vier, fünf und sechs (Rot: sieben bis zwölf).
T = P("T", "c", 60, 3, "T")
X = [9, 17.5, 26, 34.5, 43, 51.5]
NEON = ["n1", "n2", "n3", "n4", "n5", "n6"]; ROT = ["r7", "r8", "r9", "r10", "r11", "r12"]
def sp(): return [P(k, "a", X[i], 20, k[1:]) for i, k in enumerate(NEON)] + [P(k, "b", X[i], 40, k[1:]) for i, k in enumerate(ROT)] + [T]
def bahn(ids, y, ball):
    p = {k: X[i] for i, k in enumerate(ids)}
    o = 7
    run = lambda who, x, d: [mv(who, [p[who] + 2, y + o], delay=d), mv(who, [x - 2, y + o], after=True), mv(who, [x, y], after=True)]
    s1 = [ps(ball, [p[ids[3]] + 1.2, y + 1.2], bend=8)] + run(ids[0], 60, 0.2) + run(ids[1], 68.5, 0.2)
    s2 = [ps(ball, [p[ids[2]] + 1.2, y + 1.2]), ps(ball, [p[ids[5]] + 1.2, y + 1.2], after=True, bend=8)] + run(ids[2], 77, 0.3) + run(ids[3], 85.5, 0.3)
    s3 = [ps(ball, [86.7, y + 1.2], bend=8), ps(ball, [91, y], after=True)]
    return s1, s2, s3
n1, n2, n3 = bahn(NEON, 20, "b1"); r1, r2, r3 = bahn(ROT, 40, "b2")
lines = [rect(5, 10, 85, 40), line(5, 30, 90, 30), line(76, 10, 76, 50)]
goals = [{"x": 90, "y": 20, "side": "right"}, {"x": 90, "y": 40, "side": "right"}]
u = {"title": "Wurfstaffel im Team", "code": "UE-094", "kind": "Spielform",
 "focuses": ["Erwärmung", "Koordination", "Schnelligkeit"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 12, "players_max": 18, "field_size": "18 x 18 m",
 "description": "Eine Staffel zum Aufwärmen, bei der mit den Händen geworfen wird. Jede Mannschaft sitzt paarweise in einer Reihe. Der Ball wird nach vorn geworfen, und das Paar, das gerade geworfen hat, sprintet an die Spitze der Reihe. So wandert die Mannschaft Richtung Minitor. Am Ende wirft der vorderste Spieler ins Tor, dann laufen alle zurück zum Start.",
 "organisation": ["Aufbauen: Pro Mannschaft eine Bahn von etwa 18 Metern Länge, am Ende ein Minitor.",
  "Verteilen: Drei Mannschaften mit je drei Paaren. Alle sitzen in ihrer Bahn hintereinander auf dem Boden, die Partner nebeneinander.",
  "Ablauf: Der hinterste Spieler wirft zum vierten Spieler, dann sprintet er mit seinem Partner nach vorn an die Spitze. Der Fänger wirft zu seinem Partner, der weiter zum nächsten Paar, und auch dieses Paar sprintet nach vorn. Am Ende bekommt der vorderste Spieler den Ball und wirft ins Minitor.",
  "Sieger: Trifft der Werfer nicht, holen die anderen schnell den Ball für den nächsten Wurf. Die Mannschaft, die zuerst trifft und mit allen Spielern zurück am Start ist, gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Miteinander sprechen, im Paar und in der Mannschaft", "Lieber genau als hastig werfen", "Nach dem Wurf mit Vollgas an die Spitze sprinten", "Die eigene Mannschaft laut anfeuern"],
 "materials": ["3 Minitore", "3 Bälle", "Hütchen für die Bahnen"],
 "access": "frei", "hidden": True,
 "say_intro": "Wurfstaffel im Team. Werfen, sprinten, wieder werfen, bis der Ball im Minitor ist.",
 "board": {"lines": lines, "cones": ecken(5, 10, 85, 40), "goals": goals, "players": sp(), "balls": [B("b1", 10.2, 21.2), B("b2", 10.2, 41.2)],
  "steps": [
   S("Wurf zum Vierten", "Beide Mannschaften starten gleichzeitig. Der hinterste Spieler wirft zum vierten Spieler, dann sprintet er mit seinem Partner nach vorn.", *n1, *r1),
   S("Zum Partner und weiter", "Gleichzeitig wirft der Fänger zu seinem Partner, und der wirft weiter nach vorn. Auch dieses Paar sprintet an die Spitze.", *n2, *r2),
   S("Wurf ins Tor: Punkt", "Am Ende bekommt der vorderste Spieler den Ball und wirft ins Minitor. Neon trifft zuerst, und das gibt einen Punkt für Neon.", *n3, *r3)],
  "dims": [{"x1": 5, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Wurf mit Vollgas an die Spitze sprinten.", "Vollgas nach vorn",
    "Wer geworfen hat, steht sofort auf und sprintet mit seinem Partner an die Spitze der Reihe. Je schneller das Paar vorne ist, desto schneller kann der nächste Wurf kommen. So bleibt das Tempo hoch.",
    sp(), [B("b1", 10.2, 21.2), B("b2", 10.2, 41.2)],
    [S("Werfen", "Gleichzeitig werfen die beiden hintersten Spieler zum vierten Spieler ihrer Reihe.", n1[0], r1[0]),
     S("Sprint an die Spitze", "Sofort sprinten die Werfer mit ihren Partnern nach vorn. Neon ist schneller und ist zuerst wieder bereit.", *n1[1:], *r1[1:])]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Daneben geworfen heißt schnell holen, und am Ende zählt, wer zuerst zurück ist.", "Holen und zurück",
    "Trifft der Werfer nicht, holen die Mitspieler den Ball sofort für den nächsten Wurf. Hat eine Mannschaft getroffen, sprinten alle zurück zum Start. Erst wenn alle Spieler zurück sind, hat die Mannschaft gewonnen.",
    [P(k, "a", x, 20, k[1:]) for k, x in zip(NEON, [26, 34.5, 43, 51.5, 60, 68.5])] + [P(k, "b", x, 40, k[1:]) for k, x in zip(ROT, [26, 34.5, 43, 51.5, 60, 68.5])] + [T],
    [B("b1", 69.7, 21.2), B("b2", 69.7, 41.2)],
    [S("Treffer und daneben", "Neon trifft ins Minitor, und das gibt einen Punkt für Neon. Der Wurf von Rot geht daneben, und Rot holt den Ball.",
       ps("b1", [91, 20]), ps("b2", [92, 33]), mv("r12", [88, 34], delay=0.3)),
     S("Alle zurück zum Start", "Jetzt sprinten alle Neonspieler gleichzeitig zurück zum Start. Erst wenn alle dort sind, hat Neon gewonnen.",
       *[mv(k, [9 + i * 0.01, 20]) if False else mv(k, [X[i], 20]) for i, k in enumerate(NEON)])])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
