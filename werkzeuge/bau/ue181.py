import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 98-P2 (U12-U14, Woche 17 Phase 3): Evade Defenders When Outnumbered. 20 x 15 Yards = Feld x 31.25-68.75, y 5-55 (14 x 18 m),
# vier Minitore in den Ecken (je zwei oben und unten). Ausrichtung wie im PDF (der Angreifer schließt oben links ab).
# Pink (Angreifer) -> Team Neon (7 im Feld, 9 wartet oben), Blau (Verteidiger) -> Team Rot (4 verteidigt, 5 passt von unten
# und sprintet nach). Nummern ergänzt (im PDF ohne Nummern). Der wartende Spieler von Team Rot steht nur im Text.
# Ein Trainer links an der Seite mit Bällen (im PDF rechts; links, weil er in der Steigerung als zweiter Anspielpartner dient
# und rechts der Mitspieler steht).
# Sichtkegel: Text „Scan early to recognise defenders positions" und „constant scanning and awareness", Ton „scan early to
# understand defender positioning"; im Video ist in der Steigerung ein Kegel vom Angreifer zum Mitspieler außen eingezeichnet
# (Pass antäuschen). Eingebaut: Grundform Blick zu den Verteidigern vor der Annahme, Steigerung Blick zum Mitspieler außen.
T = P("T", "c", 22, 30, "T")
POS = {"n7": (55, 34), "n9": (50, 2), "r4": (45, 22), "r5": (50, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 22, 33.5), B("s2", 25.6, 33.5)]
LINES = [rect(31.25, 5, 37.5, 50)]
TORE = [{"x": 37, "y": 5, "side": "top"}, {"x": 63, "y": 5, "side": "top"},
        {"x": 37, "y": 55, "side": "bottom"}, {"x": 63, "y": 55, "side": "bottom"}]

u = {"title": "Allein gegen zwei", "code": "UE-181", "kind": "Übungsform",
 "focuses": ["Dribbling", "1 gegen 1", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 4, "players_max": 8, "field_size": "14 x 18 m",
 "description": "Ein Angreifer spielt allein gegen zwei Verteidiger und darf in jedes der vier Minitore treffen. Der zweite Verteidiger spielt ihm den Ball zu und sprintet sofort nach. Mit Finten, Richtungswechseln und schnellen Ballkontakten bringt der Angreifer die Verteidiger aus dem Gleichgewicht. Erobern die Verteidiger den Ball, brauchen sie drei Pässe, bevor sie aufs Tor gehen dürfen.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern mit einem Minitor in jeder Ecke.",
  "Verteilen: Zwei Teams. Ein Angreifer von Team Neon steht in der Mitte, ein Verteidiger von Team Rot vor ihm. Der zweite Spieler von Team Rot steht unten mit Ball. Die anderen warten hinter den Toren. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Rot passt zum Angreifer und sprintet nach, dann ist es zwei gegen eins. Der Angreifer dribbelt an beiden vorbei und schießt in ein beliebiges Minitor. Erobert Team Rot den Ball, braucht es drei Pässe vor dem Torschuss.",
  "Wertung und Wechsel: Jeder Treffer ins Minitor gibt einen Punkt. Nach jedem Angriff tauschen die Rollen, dann greift Team Rot an und Team Neon verteidigt."],
 "organisation_show": ORG,
 "coaching_points": ["Früh umschauen: Wo stehen die Verteidiger, wo ist Platz?", "Mit Finten und Täuschungen die Verteidiger aus dem Gleichgewicht bringen", "Ist Platz da, entschlossen abschließen und nicht zu lange dribbeln", "Nach Ballverlust sofort pressen und den Ball zurückholen"],
 "materials": ["4 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Allein gegen zwei. Ein Angreifer spielt gegen zwei Verteidiger und darf in alle vier Minitore treffen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 53.6)] + ERSATZ,
  "steps": [
   S("Umschauen und Anspiel", "Spieler sieben schaut sich um: Wo steht der Verteidiger? Dann passt Spieler fünf zu Spieler sieben und sprintet sofort nach. Jetzt ist es zwei gegen eins.",
     bl("n7", [45, 24]), ps("b1", [55.6, 34.6], after=True), mv("r5", [53, 44], after=True)),
   S("Finte nach rechts", "Spieler sieben nimmt den Ball nach rechts mit. Beide Verteidiger laufen hinterher.",
     dr("n7", "b1", [61, 31]), mv("r4", [55, 25], delay=0.2), mv("r5", [58, 39], delay=0.2)),
   S("Haken nach links", "Spieler sieben macht einen schnellen Haken nach links und lässt beide Verteidiger stehen.",
     dr("n7", "b1", [44, 30]), mv("r4", [51, 24], delay=0.3)),
   S("Abschluss: Punkt", "Spieler sieben dribbelt nach oben und schießt ins Minitor oben links. Das gibt einen Punkt für Team Neon. Jetzt tauschen die Rollen: Team Rot greift an, und Team Neon passt und verteidigt.",
     dr("n7", "b1", [40, 15]), mv("r4", [47, 17], delay=0.2), ps("b1", [37, 5.3], after=True))],
  "dims": dims(31.25, 68.75, 5, 55, "14 m", "18 m", rx=78)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach Ballverlust sofort pressen.", "Sofort pressen",
    "Hat Team Rot den Ball erobert, braucht es drei Pässe, bevor es aufs Tor gehen darf. Der Angreifer gibt nicht auf, sondern presst sofort. Holt er den Ball zurück, darf er gleich wieder abschließen.",
    sp(n7=(50, 36), r4=(40, 22), r5=(62, 22)), [B("b1", 40.6, 22.6)] + ERSATZ,
    [S("Ball verloren", "Spieler vier hat den Ball erobert und passt zu Spieler fünf. Das ist der erste Pass. Spieler sieben presst sofort.",
       ps("b1", [61.6, 22.6]), mv("n7", [58, 30], delay=0.3)),
     S("Abgefangen", "Spieler fünf will zurückpassen, aber Spieler sieben läuft in den Passweg und fängt den Ball ab.",
       mv("n7", [53, 23]), ps("b1", [53.6, 23.6], delay=0.3)),
     S("Schneller Abschluss: Punkt", "Spieler sieben dribbelt sofort los und schießt ins Minitor oben rechts. Das gibt einen Punkt für Team Neon.",
       dr("n7", "b1", [58, 12]), ps("b1", [63, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Anspielpartner an den Seiten.", "Mit Anspielpartnern",
    "Jetzt stehen außen Anspielpartner: rechts ein Mitspieler, links der Trainer. Der Angreifer kann mit ihnen doppelpassen oder allein dribbeln. Rechnen die Verteidiger mit dem Pass, täuscht er ihn nur an und dribbelt in den freien Raum.",
    sp(n9=(73, 28)), [B("b1", 50.6, 53.6)] + ERSATZ,
    [S("Anspiel", "Spieler fünf passt zu Spieler sieben und sprintet nach.",
       ps("b1", [55.6, 34.6]), mv("r5", [53, 44], after=True)),
     S("Pass antäuschen", "Spieler sieben schaut zu Spieler neun und täuscht den Pass nach rechts an. Beide Verteidiger rechnen mit dem Pass und schieben nach rechts.",
       bl("n7", [72, 29]), mv("r4", [59, 26], after=True), mv("r5", [60, 40], after=True)),
     S("In den freien Raum: Punkt", "Spieler sieben dribbelt nach links in den freien Raum und schießt ins Minitor oben links. Das gibt einen Punkt für Team Neon. Dann tauschen die Rollen.",
       dr("n7", "b1", [44, 29]), dr("n7", "b1", [40, 15], after=True), ps("b1", [37, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
