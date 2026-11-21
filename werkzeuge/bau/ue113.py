import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 79-P5: 30 x 20 Yards, gedreht (Tor rechts): Feld x 10-90, y 12-52, Linien wie im Original (x 42, x 58, y 32).
T = P("T", "c", 32, 48, "T")
CB = [B("c1", 34.5, 48.6), B("c2", 31, 51.5)]
POS = {"n8": (29, 32), "n7": (20, 32), "n9": (48, 32), "r11": (48, 6), "r10": (39, 6)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(10, 12, 80, 40), line(42, 12, 42, 52, dashed=False), line(58, 12, 58, 52, dashed=False), line(10, 32, 90, 32, dashed=False)]
TOR = [{"x": 90, "y": 32, "side": "right"}]
u = {"title": "Stürmer löst sich und trifft", "code": "UE-113", "kind": "Übungsform",
 "focuses": ["Bewegung", "1 gegen 1", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 8, "field_size": "27 x 18 m",
 "description": "Ein Stürmer spielt einen Prallpass und setzt sich sofort ab, um den Ball auf dem hinteren Fuß anzunehmen. Ein Verteidiger kommt von der Seite und greift an. Im eins gegen eins muss der Stürmer seinen Körper richtig stellen, einen Winkel finden und ins Minitor abschließen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern mit einem Minitor rechts. Ein Hütchen am unteren Rand zeigt, wohin sich der Stürmer absetzt.",
  "Verteilen: Zwei Passgeber von Team Neon links, ein Stürmer von Team Neon in der Mitte, zwei Verteidiger von Team Rot warten oben. Der Trainer steht mit Bällen im Feld.",
  "Ablauf: Prallpass vom Passgeber zum Stürmer und zurück. Der Stürmer setzt sich ab, bekommt den Ball in den Lauf und spielt eins gegen eins gegen den Verteidiger, der von oben kommt, bis zum Abschluss.",
  "Wechsel: Die Spieler rotieren im Uhrzeigersinn, also Passgeber, Stürmer, Verteidiger. Nach einigen Durchgängen wird die Seite gewechselt, damit beide Füße drankommen."],
 "organisation_show": ORG,
 "coaching_points": ["Offen stehen, um anzunehmen und nach vorn zu gehen", "Auf dem hinteren Fuß annehmen, weg vom Verteidiger in den freien Raum", "Vor der Annahme umschauen und erkennen, wie der Verteidiger kommt", "Je nach Laufweg des Verteidigers innen oder außen vorbei und genau abschließen"],
 "materials": ["1 Minitor", "Hütchen für Feld und Linien", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Stürmer löst sich und trifft. Prallpass, absetzen, auf dem hinteren Fuß annehmen und im eins gegen eins abschließen.",
 "board": {"lines": LINES, "cones": [C(48, 52)], "goals": TOR, "players": sp(), "balls": [B("b1", 30.6, 32.6)] + CB,
  "steps": [
   S("Prallpass", "Neon acht spielt zu Neon neun, und Neon neun lässt den Ball direkt zurückprallen.",
     ps("b1", [46.4, 32.6]), ps("b1", [30.6, 32.6], after=True)),
   S("Absetzen und anspielen", "Neon neun setzt sich sofort nach unten ab. Gleichzeitig startet Rot elf von oben, und Neon acht spielt Neon neun in den Lauf.",
     mv("n9", [48, 47]), mv("r11", [48, 24], delay=0.2), ps("b1", [49.6, 47.6], delay=0.5)),
   S("Eins gegen eins und Abschluss", "Neon neun nimmt den Ball auf dem hinteren Fuß an, zieht weg von Rot elf und schießt ins Minitor. Das gibt einen Punkt für Neon neun.",
     dr("n9", "b1", [64, 46]), dr("n9", "b1", [70, 40], after=True), mv("r11", [60, 34], delay=0.2), ps("b1", [89.5, 32], after=True))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "27 m"}, {"x1": 96, "y1": 12, "x2": 96, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Vor der Annahme umschauen und den Verteidiger lesen.", "Innen oder außen?",
    "Bevor der Ball kommt, schaut der Stürmer über die Schulter: Wie kommt der Verteidiger? Läuft er innen an, geht der Stürmer außen vorbei. Läuft er außen an, geht es innen vorbei. Angenommen wird immer auf dem hinteren Fuß, damit der erste Kontakt schon vom Verteidiger wegführt.",
    sp(n9=(48, 47), r11=(48, 24)), [B("b1", 30.6, 32.6)] + CB,
    [S("Umschauen", "Neon acht spielt in den Lauf. Gleichzeitig schaut Neon neun über die Schulter und sieht, dass Rot elf innen anläuft.",
       ps("b1", [49.6, 47.6]), mv("r11", [52, 38], delay=0.2)),
     S("Außen vorbei", "Neon neun nimmt den Ball auf dem hinteren Fuß außen mit, geht an Rot elf vorbei und schießt genau ins Minitor. Das gibt einen Punkt für Neon neun.",
       dr("n9", "b1", [62, 50]), dr("n9", "b1", [74, 44], after=True), ps("b1", [89.5, 33], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Stürmer darf einen Doppelpass mit dem Passgeber spielen.", "Doppelpass oder allein",
    "Jetzt entscheidet der Stürmer: Steht der Verteidiger weit weg, nimmt er an, dreht auf und geht allein. Steht der Verteidiger eng, legt er den Ball zum Passgeber ab und startet hinter den Verteidiger, um den Ball zurückzubekommen.",
    sp(n9=(48, 46), r11=(48, 26)), [B("b1", 30.6, 32.6)] + CB,
    [S("Verteidiger steht eng", "Neon acht spielt zu Neon neun. Gleichzeitig läuft Rot elf ganz eng heran.",
       ps("b1", [46.4, 46.6]), mv("r11", [48, 36], delay=0.2)),
     S("Doppelpass hinter den Verteidiger", "Neon acht kommt entgegen, Neon neun legt direkt ab und startet hinter Rot elf. Neon acht spielt ihm den Ball sofort zurück in den Lauf.",
       mv("n8", [36, 40]), ps("b1", [37.6, 40.6], delay=0.3), mv("n9", [60, 42], after=True), ps("b1", [61.6, 42.6], after=True)),
     S("Abschluss", "Neon neun nimmt den Ball mit und schießt ins Minitor. Das gibt einen Punkt für Neon neun.",
       dr("n9", "b1", [70, 40]), ps("b1", [89.5, 32], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
