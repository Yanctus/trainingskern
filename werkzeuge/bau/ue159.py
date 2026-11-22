import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 100-P6 (U12-U14, Woche 11 Phase 3): Precision Finishing SSG. 20 x 35 Yards = Feld x 35.7-64.3, y 5-55 (18 x 32 m), an beiden
# Enden ein großes Tor (im Original "large goal", ohne Torwart; hier Jugendtor), je zwei Hütchen auf der Torlinie teilen es in
# linke Ecke (3 Punkte), Mitte (1 Punkt), rechte Ecke (3 Punkte). Abschlusszonen nach der PDF-Skizze (gestrichelt, ca. 12 m statt
# 15 Yards). Gespiegelt: Blau (greift im PDF nach unten an) -> Neon greift nach oben an, Pink -> Rot. Keine Nummern im PDF:
# Neon 6-9, Rot 3, 4, 5, 10. Positionen auf ein Spaltenraster gesetzt (3D-Abstand), Spielidee wie im PDF. Trainer rechts.
# Sichtkegel: Im Video sind Winkel-Kegel eingezeichnet ("difficult finish on the angle" / "pass across for easier finish"),
# im Ton "lift their head and look for free teammates": im Coaching-Punkt bl() vom Spieler am spitzen Winkel zum freien Mitspieler.
T = P("T", "c", 70.5, 35, "T")
POS = {"n6": (62.2, 50), "n8": (37.3, 41.5), "n7": (37.3, 25.5), "n9": (53.9, 27),
       "r3": (45.6, 15), "r5": (62.2, 14), "r4": (45.6, 31.5), "r10": (53.9, 43)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 74.1, 38.5), B("s2", 70.5, 38.5)]
LINES = [rect(35.7, 5, 28.6, 50), line(35.7, 24.5, 64.3, 24.5), line(35.7, 35.5, 64.3, 35.5)]
KEGEL = [C(47.6, 5), C(52.4, 5), C(47.6, 55), C(52.4, 55)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Präzise in die Ecken", "code": "UE-159", "kind": "Spielform",
 "focuses": ["Torschuss", "Zusammenspiel", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 10, "field_size": "18 x 32 m",
 "description": "Vier gegen vier auf zwei Tore. Zwei Hütchen teilen jedes Tor in drei Teile: Ein Treffer in eine Ecke gibt drei Punkte, ein Treffer durch die Mitte einen Punkt. Geschossen werden darf erst in der Abschlusszone vor dem Tor, darum muss sich das Team mit Pässen in die Zone spielen. Wer nach der Spielzeit mehr Punkte hat, gewinnt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 32 Metern mit einem Jugendtor an jedem Ende. Je zwei Hütchen auf der Torlinie teilen das Tor in drei Teile. Vor jedem Tor eine Abschlusszone von 12 Metern.",
  "Verteilen: Zwei Teams zu viert. Team Neon greift das obere Tor an, Team Rot das untere. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Freies Spiel vier gegen vier. Geschossen wird nur aus der Abschlusszone. Wer den Ball erobert, greift sofort das andere Tor an.",
  "Wertung: Ecke drei Punkte, Mitte ein Punkt. Wer nach der Spielzeit mehr Punkte hat, gewinnt. Nach jedem Treffer bringt der Trainer einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Erst schauen, dann in den wertvollsten Teil des Tores schießen", "Schnell kombinieren, um in die Abschlusszone zu kommen", "Sich frei laufen und gute Anspielwinkel anbieten", "Genau schießen und auf die Ecken zielen"],
 "materials": ["2 Jugendtore", "4 Hütchen für die Tore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Präzise in die Ecken. Vier gegen vier, und ein Treffer in die Ecke gibt drei Punkte, durch die Mitte nur einen Punkt.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 62.8, 50.6)] + ERSATZ,
  "steps": [
   S("Kombinieren", "Team Neon greift nach oben an. Spieler sechs passt nach links zu Spieler acht, und der spielt direkt weiter zu Spieler sieben.",
     ps("b1", [37.9, 42.1]), ps("b1", [37.9, 26.1], after=True), mv("r4", [42, 33], delay=0.4)),
   S("In die Zone", "Spieler neun startet in die Abschlusszone. Spieler sieben spielt ihm den Ball in den Lauf.",
     mv("n9", [51, 16]), ps("b1", [51.6, 16.6], delay=0.4), mv("r5", [58, 17], delay=0.3)),
   S("Ins Eck: Punkte", "Spieler neun nimmt den Ball mit und schießt genau ins linke Eck, und das gibt drei Punkte für Team Neon. Dann bringt der Trainer einen neuen Ball, und Team Rot greift an.",
     dr("n9", "b1", [50, 13]), ps("b1", [45.2, 5.3], after=True))],
  "dims": dims(35.7, 64.3, 5, 55, "18 m", "32 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kopf hoch, wenn der Winkel schwer ist.", "Kopf hoch am Tor",
    "Wer ganz außen am Tor steht, hat einen schweren Winkel und trifft höchstens die Mitte. Darum hebt er den Kopf und sucht einen freien Mitspieler. Ein Pass quer vor das Tor bringt die Chance auf drei Punkte.",
    sp(n9=(61, 12), r5=(52.5, 9), n7=(44, 22), r3=(35.8, 14), r4=(45.6, 38)), [B("b1", 61.6, 12.6)] + ERSATZ,
    [S("Kopf hoch", "Spieler neun steht ganz außen, der Winkel ist schwer. Er hebt den Kopf und sieht Spieler sieben, der sich in der Mitte frei läuft.",
       bl("n9", [46, 17]), mv("n7", [46, 15], delay=0.2)),
     S("Quer und ins Eck: Punkte", "Spieler neun passt quer zu Spieler sieben. Der schießt direkt ins linke Eck, und das gibt drei Punkte für Team Neon.",
       ps("b1", [46.6, 15.6]), ps("b1", [45.2, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Schwacher Fuß, Kopfball oder Direktschuss zählen doppelt.", "Doppelte Punkte",
    "Trifft ein Spieler mit seinem schwachen Fuß, mit dem Kopf oder direkt ohne Annahme, zählt der Treffer doppelt. Ein Direktschuss in die Ecke gibt also sechs Punkte. So überlegen die Spieler nicht nur, wohin, sondern auch, wie sie schießen.",
    sp(), [B("b1", 37.9, 26.1)] + ERSATZ,
    [S("In den Lauf", "Spieler sieben hat den Ball. Spieler neun startet in die Abschlusszone, und Spieler sieben spielt ihm den Ball in den Lauf.",
       mv("n9", [51, 16]), ps("b1", [51.6, 16.6], delay=0.4)),
     S("Direkt ins Eck: Punkte", "Spieler neun schießt direkt, ohne Annahme, ins rechte Eck. Der Treffer zählt doppelt, und das gibt sechs Punkte für Team Neon.",
       ps("b1", [54.8, 5.3]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
