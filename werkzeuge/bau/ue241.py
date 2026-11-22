import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 83-P3 (U12-U14, Woche 39 Phase 2): Switch and Penetrate Game. 25 x 20 Yards = Feld x 25-75, y 9-49 (23 x 18 m), oben und unten
# je zwei Minitore an den Seiten, die zwei Springer (im PDF gelb F) oben und unten mittig an der Linie. Orientierung wie im PDF:
# Blau (Angreifer, 2 und 5 Außenverteidiger, 8 und 6 Mittelfeld) -> Team Neon, greift die oberen Tore an. Pink (Verteidiger)
# -> Team Rot, Nummern neu (im PDF doppelt): 6 -> 3, 10 bleibt, 8 -> 4. Positionen auf ein Spaltenraster gesetzt (3D-Abstand),
# Springer etwas weiter außerhalb. Ein Trainer statt zwei. Grundform wie im PDF (2-8-6-5, Abschluss rechts oben).
# Coaching-Punkt aus dem Video ("Recognise gaps between defenders - link with floater to switch play"), Steigerung = Progression
# (Außenzonen, jede Ballannahme dort ein Punkt, gesichert erst mit Treffer; ob das Tor selbst noch zählt, steht nicht im Original).
# Sichtkegel aus Text und Ton ("Spot gaps to play into neutral", "identifying opportunities", "recognise the moment"); im Video
# kein Kegel eingezeichnet: in der Grundform schaut Spieler acht vor dem Seitenwechsel nach rechts, im Coaching-Punkt schaut
# Spieler sechs durch die Lücke zum oberen Springer.
T = P("T", "c", 17, 44, "T")
POS = {"n2": (28, 31), "n8": (45, 37), "n6": (62, 36), "n5": (70.5, 28), "r3": (36.5, 24), "r10": (45, 21), "r4": (53.5, 24),
       "f1": (50, 5), "f2": (50, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 20.6, 47.5), B("s2", 17, 47.5)]
LINES = [rect(25, 9, 50, 40)]
TORE = [{"x": 34, "y": 9, "side": "top"}, {"x": 66, "y": 9, "side": "top"}, {"x": 34, "y": 49, "side": "bottom"}, {"x": 66, "y": 49, "side": "bottom"}]
ZONEN = [{"type": "zone", "x": 25, "y": 9, "w": 8, "h": 40}, {"type": "zone", "x": 67, "y": 9, "w": 8, "h": 40}]

u = {"title": "Locken und Seite wechseln", "code": "UE-241", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "23 x 18 m",
 "description": "Vier gegen drei mit zwei Springern oben und unten an der Linie. Team Neon greift die zwei oberen Minitore an den Seiten an und soll das verteidigende Team auf eine Seite locken. Dann wird schnell auf die freie Seite verlagert und dort getroffen, mit oder ohne Springer. Erobert Team Rot den Ball, kontert es auf die zwei unteren Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern. Oben und unten stehen je zwei Minitore an den Seiten.",
  "Verteilen: Team Neon mit vier Spielern, zwei außen und zwei in der Mitte, gegen drei von Team Rot. Ein Springer steht oben, einer unten an der Linie. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon lässt den Ball geduldig laufen, lockt Team Rot auf eine Seite und verlagert dann schnell auf die andere. Die Springer spielen mit dem Team am Ball.",
  "Wertung und Wechsel: Ein Treffer in ein oberes Minitor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, kontert es auf die unteren Minitore. Nach ein paar Angriffen wechseln die Springer."],
 "organisation_show": ORG,
 "coaching_points": ["Den Gegner auf eine Seite locken, dann schnell verlagern", "Geduldig bleiben und auf den richtigen Moment warten", "Lücken zwischen den Verteidigern sehen und über den Springer spielen", "Den Ball beim ersten Kontakt schon in Richtung der freien Seite mitnehmen"],
 "materials": ["4 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Locken und Seite wechseln. Team Neon zieht die Verteidiger auf eine Seite und trifft dann auf der anderen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 28.6, 31.6)] + ERSATZ,
  "steps": [
   S("Den Gegner locken", "Spieler zwei hat links den Ball, und Team Rot schiebt zu ihm hin. Spieler zwei lässt sich Zeit und spielt dann zu Spieler acht.",
     mv("r3", [34, 25]), ps("b1", [45.6, 37.6], delay=0.4)),
   S("Seite wechseln", "Spieler acht schaut nach rechts und sieht: Dort ist Platz. Er spielt direkt weiter zu Spieler sechs, und der sofort zu Spieler fünf. Team Rot kommt zu spät.",
     bl("n8", [63, 30]), ps("b1", [62.6, 36.6], after=True), ps("b1", [71.1, 28.6], after=True),
     mv("r4", [60, 22], delay=0.8), mv("r10", [52, 19], delay=0.8)),
   S("Rechts treffen: Punkt", "Spieler fünf dribbelt nach oben und schießt ins rechte obere Minitor. Das gibt einen Punkt für Team Neon. Dann bringt der Trainer einen neuen Ball, und Team Neon greift wieder an.",
     dr("n5", "b1", [70, 17]), ps("b1", [66.5, 9.4], after=True))],
  "dims": dims(25, 75, 9, 49, "23 m", "18 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Lücke sehen und über den Springer spielen.", "Über den Springer",
    "Ahnen die Verteidiger den Seitenwechsel und ziehen auseinander, entsteht zwischen ihnen eine Lücke. Wer sich umschaut, sieht sie und spielt durch die Lücke zum Springer. Der legt weiter auf die Seite, und der Außenspieler trifft.",
    sp(n6=(55, 36), n5=(72, 30), r4=(63.5, 23)), [B("b1", 45.6, 37.6)] + ERSATZ,
    [S("Lücke sehen", "Spieler acht spielt zu Spieler sechs. Spieler sechs hebt den Kopf und sieht eine Lücke zwischen Spieler zehn und Spieler vier.",
       ps("b1", [55.6, 36.6]), bl("n6", [53, 18], after=True)),
     S("Über den Springer", "Er spielt durch die Lücke zum oberen Springer. Spieler fünf startet nach oben, und der Springer legt ihm den Ball in den Lauf.",
       ps("b1", [50.6, 5.6]), mv("n5", [71, 16], delay=0.3), ps("b1", [71.6, 16.6], after=True)),
     S("Abschluss: Punkt", "Spieler fünf schießt direkt ins rechte obere Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [66.5, 9.4]))]),
  V("Steigerung", "Und jetzt die Steigerung: Punkte in den Außenzonen.", "Punkte in den Außenzonen",
    "Links und rechts gibt es jetzt eine Außenzone. Jede Ballannahme von Team Neon in einer Außenzone gibt einen Punkt. Aber die Punkte zählen erst, wenn der Angriff mit einem Treffer endet. So lohnt es sich, die Breite zu nutzen und mutig zu verlagern.",
    sp(), [B("b1", 45.6, 37.6)] + ERSATZ,
    [S("Links: ein Punkt", "Spieler acht spielt nach links zu Spieler zwei in die Außenzone, und das gibt einen Punkt für Team Neon. Team Rot schiebt nach links, und Spieler zwei spielt zurück.",
       ps("b1", [28.6, 31.6]), mv("r3", [33.5, 25], delay=0.3), ps("b1", [45.6, 37.6], after=True)),
     S("Rechts: zwei Punkte", "Spieler acht verlagert über Spieler sechs nach rechts zu Spieler fünf in die andere Außenzone, und das gibt noch einen Punkt für Team Neon.",
       ps("b1", [62.6, 36.6]), ps("b1", [71.1, 28.6], after=True), mv("r4", [60, 22], delay=0.8)),
     S("Treffer: Punkte sicher", "Spieler fünf dribbelt nach oben und trifft ins rechte obere Minitor. Der Treffer gibt einen Punkt für Team Neon, und jetzt zählen auch die zwei Zonenpunkte. Ohne Treffer wären sie weg.",
       dr("n5", "b1", [70, 17]), ps("b1", [66.5, 9.4], after=True))],
    lines=LINES + ZONEN)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
