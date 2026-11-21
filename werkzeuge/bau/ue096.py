import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 16-P6: 20 x 30 Yards, gedreht: Feld x 14-86, y 6-54. Linke Hälfte Neon (Ballbesitz), rechte Hälfte Rot. Minitore in allen vier Ecken.
# Sechs gegen drei: fünf Neon plus ein Springer gegen drei rote Presser. Zwei Rote warten in der eigenen Hälfte.
T = P("T", "c", 93, 30, "T")
def zone(x, y, w, h, c=None):
    z = {"type": "zone", "x": x, "y": y, "w": w, "h": h}
    if c: z["color"] = c
    return z
lines = [rect(14, 6, 72, 48), line(50, 6, 50, 54), zone(14, 6, 36, 48), zone(50, 6, 36, 48, "orange")]
goals = [{"x": 14, "y": 11, "side": "left"}, {"x": 14, "y": 49, "side": "left"}, {"x": 86, "y": 11, "side": "right"}, {"x": 86, "y": 49, "side": "right"}]
def sp(**k):
    d = dict(n4=(19, 15), n8=(46, 10), n9=(47, 50), n10=(18, 50), n11=(30, 30), f=(40, 28), r5=(37, 46), r3=(28, 14), r7=(21, 32), r2=(62, 16), r6=(72, 40)); d.update(k)
    return [P(i, "t" if i == "f" else ("a" if i[0] == "n" else "b"), x, y, "F" if i == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
cb = [B("c1", 95.6, 30.6), B("c2", 95, 33.5)]
u = {"title": "Pressen, erobern, kontern", "code": "UE-096", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 11, "players_max": 11, "field_size": "27 x 18 m",
 "description": "Sechs gegen drei in einer Hälfte: Fünf Spieler und ein Springer halten den Ball, drei Gegner pressen gemeinsam. Erobern die drei den Ball, schießen sie sofort auf eines der beiden Minitore in dieser Hälfte oder spielen den Ball zu ihren zwei Mitspielern in der anderen Hälfte. Bei jedem Ballwechsel wechselt auch der Springer die Mannschaft.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern, in der Mitte geteilt. In allen vier Ecken ein Minitor.",
  "Verteilen: Zwei Mannschaften mit je fünf Spielern und ein Springer. Eine Mannschaft hat alle fünf Spieler und den Springer in ihrer Hälfte. Drei Spieler der anderen Mannschaft pressen dort, zwei warten in der anderen Hälfte.",
  "Ablauf: Die Mannschaft mit Ball nutzt ihre Überzahl und hält den Ball in der eigenen Hälfte. Erobern die Presser den Ball, schießen sie auf ein Minitor dieser Hälfte, und das gibt einen Punkt, oder sie spielen den Ball in ihre eigene Hälfte.",
  "Umschalten: Nach einem Tor startet der Trainer in der anderen Hälfte neu. Der Springer wechselt immer zur Mannschaft am Ball, und drei Spieler der anderen Mannschaft laufen hinüber zum Pressen."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Spieltempo pressen und als Einheit Passwege zustellen", "Sich ohne Ball frei laufen, um im freien Raum anzunehmen", "Nach Ballgewinn schnell abschließen oder schnell verlagern", "Am Ball konzentriert bleiben und unnötige Ballverluste vermeiden"],
 "materials": ["4 Minitore", "Hütchen", "Leibchen in drei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Pressen, erobern, kontern. Sechs gegen drei, und wer den Ball erobert, schießt sofort oder spielt ihn hinüber.",
 "board": {"lines": lines, "cones": ecken(14, 6, 72, 48), "goals": goals, "players": sp(), "balls": [B("b1", 20.6, 15.6)] + cb,
  "steps": [
   S("Ball halten", "Neon vier spielt zu Neon elf. Gleichzeitig verschieben die drei Roten gemeinsam und stellen Passwege zu.",
     ps("b1", [31.6, 30.6]), mv("r3", [27, 21], delay=0.2), mv("r7", [24, 36], delay=0.2), mv("r5", [36, 40], delay=0.2)),
   S("Pass abgefangen", "Neon elf will zu Neon zehn passen, doch Rot sieben ahnt den Pass und fängt ihn ab.",
     ps("b1", [22.4, 42.6]), mv("r7", [21, 42], delay=0.2)),
   S("Sofort aufs Minitor", "Rot sieben schießt sofort auf das Minitor unten links, und das gibt einen Punkt für Rot.", ps("b1", [13, 49])),
   S("Neustart drüben", "Der Trainer spielt in der anderen Hälfte zu Rot sechs. Gleichzeitig wechselt der Springer hinüber, und drei Neonspieler laufen zum Pressen nach drüben.",
     ps("c1", [70.4, 40.6]), mv("f", [62, 30], delay=0.2), mv("n8", [64, 10], delay=0.3), mv("n11", [58, 22], delay=0.3), mv("n9", [60, 46], delay=0.3))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 5, "y1": 6, "x2": 5, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Als Einheit pressen und die Passwege zustellen.", "Gemeinsam pressen",
    "Die drei Presser arbeiten zusammen. Einer geht auf den Ballführenden, die anderen beiden stellen die nächsten Passwege zu. So muss der Gegner einen schwierigen Pass spielen, und die Presser können ihn abfangen. Wer nur allein hinterherläuft, wird leicht ausgespielt.",
    sp(), [B("b1", 31.6, 30.6)] + cb,
    [S("Zusammen zustellen", "Rot fünf läuft auf Neon elf zu. Gleichzeitig stellen Rot drei und Rot sieben die Wege zu Neon vier und Neon zehn zu.",
       mv("r5", [34, 38]), mv("r3", [25, 23]), mv("r7", [21, 40])),
     S("Schwieriger Pass", "Neon elf bleibt nur der Pass zum Springer, und Rot fünf geht dazwischen.",
       ps("b1", [38.4, 28.6]), mv("r5", [37, 30], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Nach Ballgewinn den Ball schnell in die eigene Hälfte spielen.", "Ball hinüberspielen",
    "Statt zu schießen, können die Presser den Ball auch zu ihren zwei Mitspielern in der anderen Hälfte spielen. Dann sprinten sie sofort hinterher und helfen, den Ball zu halten. Der Springer wechselt mit, und jetzt hat die andere Mannschaft die Überzahl.",
    sp(r5=(39, 34), n11=(30, 40), f=(37.5, 18), n9=(48, 50)), [B("b1", 40.6, 34.6)] + cb,
    [S("Ball erobert und hinüber", "Rot fünf hat den Ball erobert und spielt sofort hinüber zu Rot zwei.", ps("b1", [63.6, 16.6])),
     S("Alle sprinten hinüber", "Gleichzeitig sprinten die drei Roten und der Springer in die andere Hälfte, und drei Neonspieler laufen zum Pressen mit.",
       mv("r5", [62, 30]), mv("r3", [58, 46]), mv("r7", [76, 24]), mv("f", [70, 8], delay=0.1), mv("n8", [56, 12], delay=0.3), mv("n11", [54, 36], delay=0.3), mv("n9", [66, 50], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
