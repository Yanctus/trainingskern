import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 89-P5 (U12-U14, Woche 12 Phase 6): Defend the Gate CDM. 24 x 32 Yards = Feld x 20-80, y 7.5-52.5 (29 x 22 m). Gedreht (90 Grad
# gegen den Uhrzeigersinn): Im PDF liegen die Hälften oben/unten und es wird zur Seite gespielt; hier linke/rechte Hälfte, links
# spielt Team Neon nach oben auf das Hütchentor am oberen Rand, rechts Team Rot nach unten auf das Hütchentor am unteren Rand.
# Bänder (gestrichelt) nach der PDF-Skizze: Endzone, Mittelzone, Aufbauzone. Pink -> Team Neon, dunkel -> Team Rot. Keine Nummern im
# PDF: Neon 2, 3, 4 (Aufbau), 9 (Angreifer), 6 (Verteidiger rechts); Rot 5, 7, 8 (Aufbau), 11 (Angreifer), 10 (Verteidiger links);
# in der Steigerung zwei dazu: Rot 12, 14 und Neon 13, 15. Ein Trainer statt zwei (rechts an der Seite).
# Punkt für den Angreifer beim Dribbling durchs Hütchentor: im PDF nicht ausdrücklich genannt, aus dem Sinn ergänzt.
# Positionen auf Abstand gesetzt (3D); in der zweiten Steigerung stehen die Aufbauspieler am Rand, die Presser vorn in der Aufbauzone.
# Sichtkegel: PDF "Quick scans to check player positions when 2 v 1", Ton "body shape ... to see attacker and ball", Video
# "Anticipate pass - see ball and player": bl() vom Verteidiger Spieler zehn zum Angreifer und zum mitlaufenden Spieler.
T = P("T", "c", 86, 30, "T")
POS = {"n2": (25.2, 44), "n3": (35.4, 47.9), "n4": (45.2, 43.3), "n9": (22.5, 24), "r10": (35, 30),
       "r7": (54.3, 16), "r8": (64.4, 11.7), "r5": (75, 15.9), "r11": (77.5, 33), "n6": (65, 30)}
POS2 = {"n2": (25, 51.6), "n3": (35.5, 51.6), "n4": (45.5, 51.6), "r12": (27.5, 36), "r14": (44.5, 36), "r10": (36, 27), "n9": (22.5, 20),
        "r7": (55, 8.5), "r8": (65, 8.5), "r5": (75, 8.5), "n13": (57.5, 24.1), "n15": (74.5, 24.1), "n6": (66, 32), "r11": (77.5, 40)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 89.6, 33.5), B("s2", 86, 33.5)]
LINES = [rect(20, 7.5, 60, 45), line(50, 7.5, 50, 52.5), line(20, 19.2, 80, 19.2), line(20, 39.9, 80, 39.9)]
KEGEL = [C(28.7, 7.5), C(39.6, 7.5), C(60.6, 52.5), C(71.4, 52.5)]

u = {"title": "Das Hütchentor verteidigen", "code": "UE-167", "kind": "Übungsform",
 "focuses": ["Verteidigen", "1 gegen 1", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 14, "field_size": "29 x 22 m",
 "description": "In zwei Hälften spielen je drei Spieler den Ball hin und her, bis einer nach vorn zum Angreifer passt. Der Angreifer will durch ein Hütchentor dribbeln, ein Verteidiger des anderen Teams will das verhindern. Der Verteidiger stellt sich richtig hin, lenkt den Angreifer nach außen und fängt Pässe ab. Erobert er den Ball, dribbelt er durch das Hütchentor auf der anderen Seite und holt zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 29 mal 22 Metern, in eine linke und eine rechte Hälfte geteilt. Jede Hälfte hat drei Zonen: Aufbauzone, Mittelzone und Endzone. Am Rand jeder Endzone ein Hütchentor.",
  "Verteilen: Links spielen drei Neon-Spieler in der Aufbauzone, Spieler neun ist Angreifer und Spieler zehn verteidigt in der Mittelzone. Rechts ist es genau andersherum. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Die drei passen sich den Ball zu, bis einer nach vorn zum Angreifer spielt. Der Angreifer will durch das Hütchentor dribbeln, der Verteidiger will den Ball vorher erobern. Beide Hälften spielen gleichzeitig.",
  "Wertung: Dribbelt der Angreifer durch das Hütchentor, gibt das einen Punkt. Blockt der Verteidiger den Ball in der Endzone, gibt das einen Punkt für sein Team. Erobert er den Ball in der Mittelzone und dribbelt durch das Hütchentor auf der anderen Seite, gibt das zwei Punkte."],
 "organisation_show": ORG,
 "coaching_points": ["Je nach Ball richtig stehen", "Mit dem Körper den Angreifer nach außen lenken", "Den Pass vorausahnen und dazwischengehen", "Schnell schauen, wo Ball und Gegner sind"],
 "materials": ["4 Hütchen für zwei Hütchentore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Das Hütchentor verteidigen. Ein Verteidiger in der Mitte will verhindern, dass der Angreifer durch das Hütchentor dribbelt.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 45.8, 43.9), B("b2", 54.9, 16.6)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Beide Hälften spielen gleichzeitig. Wir schauen nach links: Spieler vier passt zu Spieler drei, der weiter zu Spieler zwei. Spieler zehn schiebt mit und schaut, wo Spieler neun steht.",
     ps("b1", [36, 48.5]), ps("b1", [25.8, 44.6], after=True), ps("b2", [65, 12.3]), mv("r10", [33, 31], delay=0.5), bl("r10", [22.5, 24], after=True)),
   S("Pass nach vorn", "Spieler zwei spielt nach vorn zu Spieler neun. Spieler zehn sprintet sofort hin und stellt sich zwischen Spieler neun und das Hütchentor.",
     ps("b1", [23.1, 24.6]), mv("r10", [29, 21], delay=0.3)),
   S("Erobert und durch: Punkte", "Spieler neun muss nach außen. Spieler zehn erobert den Ball noch in der Mittelzone und dribbelt durch das Hütchentor auf der anderen Seite, und das gibt zwei Punkte für Team Rot. Dann spielt der Trainer einen neuen Ball zu Team Neon.",
     dr("n9", "b1", [23, 20.5]), mv("r10", [24.5, 19.5], after=True), dr("r10", "b1", [44, 34], after=True), dr("r10", "b1", [66, 54.5], after=True))],
  "dims": dims(20, 80, 7.5, 52.5, "29 m", "22 m", rx=12)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei gegen eins in der Mitte.", "Zwei gegen eins",
    "Jetzt läuft ein zweiter Spieler aus der Aufbauzone mit nach vorn. In der Mitte steht es dann zwei gegen eins. Der Verteidiger schaut schnell über die Schulter, wo beide stehen, und lauert auf den Pass.",
    sp(), [B("b1", 25.8, 44.6), B("b2", 65, 12.3)] + ERSATZ,
    [S("Zwei gegen eins", "Spieler zwei spielt nach vorn zu Spieler neun, und Spieler drei läuft mit in die Mitte. Spieler zehn läuft Spieler neun an und schaut schnell über die Schulter zu Spieler drei.",
       ps("b1", [23.1, 24.6]), mv("n3", [44, 31], delay=0.3), mv("r10", [29, 24], delay=0.3), bl("r10", [44, 31], after=True)),
     S("Abgefangen: Punkte", "Spieler neun will zu Spieler drei passen. Spieler zehn ahnt den Pass, fängt ihn ab und dribbelt durch das Hütchentor auf der anderen Seite, und das gibt zwei Punkte für Team Rot.",
       mv("r10", [32.4, 27.2]), ps("b1", [33, 27.8], delay=0.2), dr("r10", "b1", [42, 36], after=True), dr("r10", "b1", [64, 44], after=True), dr("r10", "b1", [66, 54.5], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Drei gegen zwei in der Aufbauzone.", "Drei gegen zwei",
    "Jetzt pressen in der Aufbauzone zwei Gegner. Die drei Spieler müssen sich den Ball sicher zupassen, bevor einer nach vorn spielt. Dann läuft einer mit, und der Verteidiger muss Angreifer und Mitspieler im Blick behalten.",
    sp(POS2), [B("b1", 36.1, 52.2), B("b2", 65.6, 9.1)] + ERSATZ,
    [S("Drei gegen zwei", "Links pressen Spieler zwölf und Spieler vierzehn, und Spieler drei passt schnell zu Spieler zwei. Rechts spielt Team Rot gleichzeitig gegen Spieler dreizehn und Spieler fünfzehn.",
       ps("b1", [25.6, 52.2]), mv("r12", [30, 45], delay=0.2), mv("r14", [42, 46], delay=0.2), ps("b2", [75.6, 9.1]), mv("n15", [72, 15], delay=0.2)),
     S("Pass nach vorn", "Spieler zwei spielt nach vorn zu Spieler neun, und Spieler drei läuft mit in die Mitte. Spieler zehn schaut schnell zu beiden.",
       ps("b1", [23.1, 20.6]), mv("n3", [44, 30], delay=0.3), bl("r10", [36, 44], delay=0.3), bl("r10", [22.5, 20], after=True)),
     S("Abgefangen: Punkte", "Spieler neun will quer zu Spieler drei passen. Spieler zehn ahnt den Pass, fängt ihn ab und dribbelt durch das Hütchentor auf der anderen Seite, und das gibt zwei Punkte für Team Rot.",
       mv("r10", [32.4, 24.6]), ps("b1", [33, 25.2], delay=0.2), dr("r10", "b1", [42, 36], after=True), dr("r10", "b1", [64, 44], after=True), dr("r10", "b1", [66, 54.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
