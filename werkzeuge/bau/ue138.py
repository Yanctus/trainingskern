import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-58 (U12-U14, Woche 4 Pre-Season): Quick Sprints to Combine and Finish (2 v 2 Sprints to Finish). 15 x 25 Yards hochkant
# = Feld x 35-65, y 6-56 (14 x 23 m), Jugendtor oben mit neutralem Torwart (D-Jugend dabei). Pink (Angreifer) -> Neon 4, 5, 3, 6;
# Blau (Verteidiger) -> Rot 9, 8, 11, 7. Je Seite nur ein wartendes Paar gezeigt, Wartende neben dem Feld (3D-Abstand).
# Ein Trainer statt zwei. Sichtkegel aus dem Text ("Head up to see teammate"): vor dem Querpass schaut der Angreifer zum Mitspieler.
T = P("T", "c", 74, 32, "T")
TW = P("k", "t", 50, 9, "TW")
POS = {"n4": (41, 12), "n5": (59, 12), "r9": (32, 12), "r8": (68, 12), "n3": (22, 12), "r11": (13, 12), "n6": (78, 12), "r7": (87, 12)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
ERSATZ = [B("s1", 75.6, 35.5), B("s2", 77.5, 31)]
BALL_AB = [41.6, 28.6]  # hier lässt der Angreifer den Ball liegen
LINES = [rect(35, 6, 30, 50)]
KEGEL = [C(38.5, 15.5), C(61.5, 15.5), C(42.4, 38.2, "neon", shape="stange"), C(57.3, 37.5, "neon", shape="stange")]
TORE = [{"x": 50, "y": 6, "side": "top", "size": "jugend"}]
N4 = [[39, 36], [42.4, 42.3], [46, 37.5], [42.5, 30]]
N5 = [[58.5, 30], [61, 35], [57.3, 42], [54, 37], [53, 23]]
R9 = [[37, 26], [38.5, 36.5], [42.4, 43.5], [46.5, 38.5]]
R8 = [[63, 26], [61.5, 35.5], [57.3, 43.5], [53.5, 39]]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Stangen-Sprint zum Abschluss", "code": "UE-138", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 13, "field_size": "14 x 23 m",
 "description": "Zwei Angreifer gegen zwei Verteidiger auf ein Tor mit Torwart. Ein Angreifer passt seinem Partner den Ball zu, der ihn annimmt und liegen lässt. Dann sprinten beide Angreifer um ihre Stange, holen sich den Ball und spielen zusammen bis zum Abschluss. Die Verteidiger sprinten vom Start hinterher, machen Druck und wollen den Ball erobern oder den Schuss blocken. Nach jeder Runde tauschen die Teams die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 23 Metern, oben ein Jugendtor mit Torwart. Weiter unten stehen links und rechts zwei Stangen, oben zwei Hütchen als Start.",
  "Verteilen: Team Neon greift an, Team Rot verteidigt. Je ein Angreifer und ein Verteidiger starten links und rechts neben dem Tor, die anderen warten dahinter. Der Trainer steht am Rand mit Bällen.",
  "Ablauf: Der rechte Angreifer passt zum linken, der nimmt an und lässt den Ball liegen. Beide Angreifer sprinten um ihre Stange, holen den Ball und kombinieren zum Abschluss. Die Verteidiger sprinten gleichzeitig hinterher und stören.",
  "Wertung: Jedes Tor ist ein Punkt für die Angreifer, jeder eroberte Ball ein Punkt für die Verteidiger. Nach zwei vollen Runden tauschen die Rollen. Das Verliererteam macht eine kleine Fitnessaufgabe, die die Sieger aussuchen."],
 "organisation_show": ORG,
 "coaching_points": ["Den ersten Pass so spielen, dass der Partner ihn gut annehmen kann", "Kurze, schnelle Schritte um die Stange, mit hohem Tempo", "Kopf hoch, den Mitspieler sehen und so passen, dass er mit ein oder zwei Kontakten abschließen kann", "Eiskalt abschließen und in die Ecken zielen"],
 "materials": ["1 Jugendtor", "2 Stangen", "2 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Stangen-Sprint zum Abschluss. Zwei Angreifer sprinten um ihre Stangen, holen sich den Ball und schließen ab, und zwei Verteidiger jagen hinterher.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b5", 59.6, 12.6)] + ERSATZ,
  "steps": [
   S("Pass löst den Angriff aus", "Neon fünf passt quer zu Neon vier, der dem Ball entgegenläuft, ihn annimmt und liegen lässt.",
     mv("n4", [41, 28]), ps("b5", BALL_AB, delay=0.2)),
   S("Sprint um die Stangen", "Jetzt sprinten beide Angreifer gleichzeitig um ihre Stange. Rot neun und Rot acht sprinten vom Start hinterher.",
     *weg("n4", N4), *weg("n5", N5), *weg("r9", R9, delay=0.2), *weg("r8", R8, delay=0.2)),
   S("Kopf hoch, querlegen", "Neon vier ist zuerst am Ball, hebt den Kopf, sieht Neon fünf frei vor dem Tor und legt ihm den Ball in den Lauf.",
     bl("n4", [53, 23]), ps("b5", [53.6, 22.6], after=True)),
   S("Abschluss: Punkt", "Neon fünf schießt mit dem ersten Kontakt in die Ecke, und das gibt einen Punkt für Team Neon. Dann ist das nächste Paar dran, und nach jeder Runde tauschen die Teams die Rollen.",
     ps("b5", [53, 5.7]))],
  "dims": [{"x1": 35, "y1": 58.6, "x2": 65, "y2": 58.6, "text": "14 m"}, {"x1": 92, "y1": 6, "x2": 92, "y2": 56, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kopf hoch, den Mitspieler sehen.", "Kopf hoch",
    "Wer am Ball nur nach unten schaut, sieht den freien Mitspieler nicht. Deshalb vor dem Pass kurz den Kopf heben: Wo steht mein Partner, wo die Verteidiger? Dann den Ball so vorlegen, dass er direkt abschließen kann.",
    sp(n4=(42.5, 30), n5=(54, 25), r9=(33, 38), r8=(63, 41)), [B("b5", 41.6, 28.6)] + ERSATZ,
    [S("Kopf hoch", "Neon vier steht am Ball und hebt den Kopf. Er sieht: Neon fünf ist frei, Rot acht ist noch hinten.",
       bl("n4", [54, 25]), mv("r9", [38, 33], delay=0.3), mv("r8", [57, 32], delay=0.3)),
     S("Pass in den Lauf: Punkt", "Er legt den Ball genau vor Neon fünf, der direkt in die Ecke schießt, und das gibt einen Punkt für Team Neon.",
       ps("b5", [54.6, 25.6]), ps("b5", [53, 5.7], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Immer mit Tempo bleiben.", "Zu langsam",
    "Die Angreifer müssen die ganze Zeit Tempo machen. Wer um die Stange trödelt, gibt dem Verteidiger Zeit, sich zwischen Ball und Mitspieler zu stellen, und schon ist der Ball weg.",
    sp(n4=(42.5, 30.5), n5=(61, 40), r8=(52, 25), r9=(33, 38)), [B("b5", 41.6, 28.6)] + ERSATZ,
    [S("Zu langsam", "Neon fünf trödelt um die Stange. Rot acht ist schon zurück und stellt sich in den Passweg.",
       mv("n5", [58, 33]), mv("r8", [50, 30], delay=0.2)),
     S("Abgefangen: Punkt", "Neon vier spielt trotzdem zu Neon fünf, aber Rot acht fängt den Ball ab, und das gibt einen Punkt für Team Rot. Dann ist das nächste Paar dran.",
       ps("b5", [50.3, 30.6]), dr("r8", "b5", [55, 21], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
