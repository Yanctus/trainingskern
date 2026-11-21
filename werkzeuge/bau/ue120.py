import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-61: 30 x 25 Yards, gedreht (Minitore rechts): Feld x 14-86, y 8-52, Endzone ab x 75. Drei Dummys im Dreieck.
T = P("T", "c", 62, 4, "T")
CB = [B("c1", 64.5, 4.6), B("c2", 59, 5.5)]
DU = [P("d1", "t", 38, 24, "D"), P("d2", "t", 38, 40, "D"), P("d3", "t", 20, 32, "D")]
POS = {"n2": (53, 12), "n4": (44, 6), "n3": (35, 6), "n6": (47, 41), "r5": (70, 31)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + DU + [T]
LINES = [rect(14, 8, 72, 44), line(75, 8, 75, 52)]
TORE = [{"x": 86, "y": 21, "side": "right"}, {"x": 86, "y": 42, "side": "right"}]
u = {"title": "Doppelpass, dann eins gegen eins", "code": "UE-120", "kind": "Übungsform",
 "focuses": ["Passspiel", "Dribbling", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 8, "field_size": "23 x 27 m",
 "description": "Drei Dummys stehen im Dreieck, rechts stehen zwei Minitore. Nach einem Doppelpass dribbelt ein Spieler um den hinteren Dummy und spielt zum Startplatz. Von dort geht der Ball zum Angreifer, der im eins gegen eins gegen einen Verteidiger auf die Minitore spielt.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 27 Metern mit drei Dummys im Dreieck. Rechts stehen zwei Minitore, davor eine Endzone.",
  "Verteilen: Am Startplatz oben stehen Spieler von Team Neon mit Bällen. Ein Neon-Spieler steht am unteren Dummy, ein Verteidiger von Team Rot wartet in der Endzone.",
  "Ablauf: Neon zwei spielt einen Doppelpass mit Neon sechs, dribbelt um den hinteren Dummy und spielt zum Startplatz. Von dort geht der Ball zu Neon sechs. Sobald Neon sechs den Ball berührt, greift Rot fünf ein, und Neon sechs muss ihn im eins gegen eins schlagen und ins Minitor treffen.",
  "Wechsel: Nach dem Abschluss wird der Angreifer zum Verteidiger, der Verteidiger geht an den Startplatz. Nach einer ganzen Runde sprinten alle einmal um das Feld und erholen sich kurz."],
 "organisation_show": ORG,
 "coaching_points": ["Genau mit einem Kontakt passen", "Den Pass so spielen, dass der Mitspieler ihn im Lauf mitnehmen kann", "Den Ball eng am Fuß führen, mit beiden Füßen", "Mit Tricks den Verteidiger aus dem Gleichgewicht bringen und ruhig abschließen"],
 "materials": ["3 Dummys", "2 Minitore", "Hütchen für Feld und Endzone", "Mehrere Bälle", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Doppelpass, dann eins gegen eins. Erst sauber kombinieren, dann den Verteidiger ausspielen und abschließen.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 54.6, 12.6)] + CB,
  "steps": [
   S("Doppelpass", "Neon zwei spielt zu Neon sechs und startet zwischen die Dummys. Neon sechs spielt den Ball direkt in seinen Lauf.",
     ps("b1", [45.4, 41.6]), mv("n2", [46, 30], delay=0.3), ps("b1", [47.6, 30.6], after=True)),
   S("Um den Dummy und zurück", "Neon zwei dribbelt um den hinteren Dummy herum und spielt dann zu Neon vier am Startplatz.",
     dr("n2", "b1", [28, 38]), dr("n2", "b1", [14, 36], after=True), dr("n2", "b1", [15, 25], after=True), dr("n2", "b1", [26, 20], after=True), ps("b1", [42.4, 6.6], after=True)),
   S("Anspiel zum Angreifer", "Neon vier spielt zu Neon sechs. Sobald Neon sechs den Ball berührt, darf Rot fünf angreifen.",
     ps("b1", [48.6, 41.6]), mv("r5", [66, 38], delay=0.6)),
   S("Eins gegen eins", "Neon sechs dribbelt an Rot fünf vorbei und schießt ins untere Minitor. Das gibt einen Punkt für Neon sechs.",
     dr("n6", "b1", [60, 46]), dr("n6", "b1", [76, 40], after=True), ps("b1", [85.5, 42], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "23 m"}, {"x1": 94, "y1": 8, "x2": 94, "y2": 52, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Verteidiger mit einer Täuschung aus dem Gleichgewicht bringen.", "Täuschen und vorbei",
    "Im eins gegen eins täuscht der Angreifer eine Richtung an, zum Beispiel mit einem Schulter fallen lassen oder einem Übersteiger. Verlagert der Verteidiger sein Gewicht, zieht der Angreifer in die andere Richtung in den freien Raum und schließt mit Ruhe ab.",
    sp(n6=(58, 42), r5=(68, 34)), [B("g", 59.6, 42.6), B("b1", 54.6, 12.6)] + CB,
    [S("Antäuschen", "Rot fünf kommt auf Neon sechs zu. Neon sechs lässt die Schulter fallen und täuscht nach unten an.",
       mv("r5", [64, 40]), dr("n6", "g", [59, 46], delay=0.3)),
     S("In die andere Richtung", "Rot fünf fällt darauf herein. Neon sechs zieht nach oben in den freien Raum und schießt ins obere Minitor. Das gibt einen Punkt für Neon sechs.",
       dr("n6", "g", [60, 34]), dr("n6", "g", [72, 28], after=True), ps("g", [85.5, 22], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Pass in den Lauf spielen.", "Pass in den Lauf",
    "Beim Doppelpass kommt der Ball nicht in den Fuß, sondern ein Stück vor den Spieler, damit er ihn im Laufen mitnehmen kann. Dazu müssen Tempo und Richtung des Passes genau passen. So muss niemand abstoppen, und die Übung bleibt schnell.",
    sp(), [B("b1", 54.6, 12.6)] + CB,
    [S("Pass und Start", "Neon zwei spielt fest zu Neon sechs und startet sofort los.",
       ps("b1", [45.4, 41.6]), mv("n2", [48, 24], delay=0.3)),
     S("In den Lauf", "Neon sechs spielt den Ball direkt ein Stück vor Neon zwei. Der nimmt ihn im Laufen mit und dribbelt ohne Pause weiter.",
       mv("n2", [44, 32]), ps("b1", [42.4, 32.6], delay=0.1), dr("n2", "b1", [30, 37], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
