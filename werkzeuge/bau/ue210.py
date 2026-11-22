import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 33-P3 (U12-U14, Woche 29 Phase 3): One to One Finishing (Lose your Marker). 30 x 30 Yards = Feld x 26-74, y 5-53 (27 x 27 m),
# Mittellinie gestrichelt, oben und unten je ein Jugendtor mit neutralem Torwart. Gedreht (90 Grad): im PDF liegen die Tore
# links und rechts. Bogen und Strafraum-Rechteck aus der PDF-Skizze weggelassen. Pink -> Team Neon (9 Angreifer innen,
# 7, 8, 10, 11 außen), Navy -> Team Rot (4 Verteidiger innen, 5, 6 außen), Nummern wie im PDF; die sechs Außenspieler je drei
# links und rechts neben dem Feld (wegen der gedrehten Tore). Ein Trainer statt zwei. Wertung: Treffer = Punkt für den Angreifer
# (laut PDF "tally of goals"); Ballgewinn des Verteidigers = Punkt für Team Rot (ergänzt).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 8, 22, "T")
POS = {"k1": (50, 8.5), "k2": (50, 49.5), "n9": (59, 25), "r4": (44, 34),
       "n8": (20, 12), "r6": (20, 30), "n7": (20, 47), "r5": (80, 12), "n11": (80, 30), "n10": (80, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
AUSSEN = [B("b" + i[1:], POS[i][0] + 0.6, POS[i][1] + 0.6) for i in ("n8", "r6", "n7", "r5", "n11", "n10")]
ERSATZ = [B("s1", 11.6, 22.5), B("s2", 8, 26)]
LINES = [rect(26, 5, 48, 48), line(26, 29, 74, 29)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 53, "side": "bottom", "size": "jugend"}]

u = {"title": "Abschluss mit und ohne Gegner", "code": "UE-210", "kind": "Übungsform",
 "focuses": ["Torschuss", "1 gegen 1", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Ein Angreifer und ein Verteidiger stehen in der Mitte, sechs Spieler mit Ball stehen außen, und in beiden Toren steht ein Torwart. Ein Außenspieler ruft den Angreifer, spielt ihn an, und der schießt nach einer Ballannahme ohne Gegner auf eines der Tore. Nach drei Schüssen spielt der Verteidiger mit, und der Angreifer muss ihn im Eins gegen Eins abschütteln. Nach drei Duellen tauschen die beiden mit zwei Außenspielern.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern mit Mittellinie. Oben und unten je ein Jugendtor mit einem Torwart.",
  "Verteilen: Ein Angreifer von Team Neon und ein Verteidiger von Team Rot stehen in der Mitte. Sechs Spieler stehen mit Ball außen, drei links und drei rechts. Der Trainer steht links mit Bällen.",
  "Ablauf: Ein Außenspieler ruft den Angreifer und spielt ihn an. Der Angreifer nimmt den Ball an und schießt ohne Gegner auf ein Tor, dreimal hintereinander. Beim vierten Pass spielt der Verteidiger mit, und es geht dreimal eins gegen eins.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für den Angreifer. Erobert der Verteidiger den Ball, gibt das einen Punkt für Team Rot. Nach drei Duellen tauschen Angreifer und Verteidiger mit zwei Außenspielern, bis jeder in der Mitte war."],
 "organisation_show": ORG,
 "coaching_points": ["Erst weg vom Ball, dann schnell zum Ball anbieten", "Die erste Ballannahme schon in Richtung Tor", "Mutig ins Eins gegen Eins gehen und schnell schießen", "Als Verteidiger den richtigen Moment zum Angriff abwarten"],
 "materials": ["2 Jugendtore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Abschluss mit und ohne Gegner. Der Angreifer in der Mitte schießt erst dreimal ohne Gegner und dann dreimal gegen einen Verteidiger.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": AUSSEN + ERSATZ,
  "steps": [
   S("Weg und wieder hin", "Spieler acht ruft Spieler neun. Spieler neun läuft erst kurz weg und kommt dann schnell zum Ball. Spieler vier spielt noch nicht mit.",
     mv("n9", [63, 29]), mv("n9", [44, 17], after=True)),
   S("Ohne Gegner: Punkt", "Spieler acht spielt Spieler neun an. Der nimmt den Ball mit Richtung Tor und schießt am Torwart vorbei. Das gibt einen Punkt für Spieler neun. Das macht er dreimal, jedes Mal mit einem anderen Außenspieler.",
     ps("b8", [44.6, 17.6]), dr("n9", "b8", [47, 13], after=True), ps("b8", [44.5, 5.6], after=True)),
   S("Jetzt mit Gegner", "Beim vierten Mal ruft Spieler neun Spieler zehn und bekommt den Ball. Jetzt spielt Spieler vier mit und läuft sofort auf ihn zu.",
     mv("n9", [56, 33]), ps("b10", [56.6, 33.6], after=True), mv("r4", [49, 40], after=True)),
   S("Eins gegen eins: Punkt", "Spieler neun täuscht nach links an und zieht dann nach rechts an Spieler vier vorbei. Er schießt schnell, und das gibt einen Punkt für Spieler neun. Nach drei Duellen tauschen Spieler neun und Spieler vier mit Spieler zehn und Spieler sechs von außen.",
     dr("n9", "b10", [51, 36]), dr("n9", "b10", [61, 42], after=True), mv("r4", [53, 42], after=True), ps("b10", [55, 52.4], after=True))],
  "dims": dims(26, 74, 5, 53, "27 m", "27 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Verteidiger aus dem Gleichgewicht bringen.", "Antäuschen und weg",
    "Mit kurzen, schnellen Bewegungen bringt der Angreifer den Verteidiger aus dem Gleichgewicht. Er täuscht in eine Richtung an und zieht dann schnell in die andere. So bekommt er Platz und kann mutig schießen.",
    sp(n9=(54, 32), r4=(41, 40)), [B("b10", 54.6, 32.6)] + [b for b in AUSSEN if b["id"] != "b10"] + ERSATZ,
    [S("Antäuschen", "Spieler neun dribbelt ein kurzes Stück nach links. Spieler vier glaubt ihm und schiebt mit.",
       dr("n9", "b10", [50, 36]), mv("r4", [47, 41], delay=0.2)),
     S("Gegenrichtung: Punkt", "Jetzt zieht Spieler neun schnell nach rechts, ist an Spieler vier vorbei und schießt sofort. Das gibt einen Punkt für Spieler neun.",
       dr("n9", "b10", [61, 42]), mv("r4", [52, 44], delay=0.3), ps("b10", [55, 52.4], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Freilaufen und den Ball quer zum Körper mitnehmen.", "Mitnehmen und schießen",
    "Der Angreifer läuft erst weg vom Ball und kommt dann schnell zum Außenspieler. Den ersten Kontakt nimmt er quer vor dem Körper mit, weg vom Verteidiger und Richtung Tor. So kann er schießen, bevor der Verteidiger wieder bereit ist.",
    sp(n9=(52, 25), r4=(43, 30)), AUSSEN + ERSATZ,
    [S("Weg und wieder hin", "Spieler neun läuft erst weg vom Ball und kommt dann schnell zu Spieler elf. Spieler vier läuft hinterher.",
       mv("n9", [47, 28]), mv("n9", [60, 24], after=True), mv("r4", [52, 28], after=True)),
     S("Mitnehmen: Punkt", "Spieler elf spielt ihn an. Spieler neun nimmt den Ball quer vor dem Körper mit, weg von Spieler vier, und schießt sofort. Das gibt einen Punkt für Spieler neun.",
       ps("b11", [60.6, 24.6]), dr("n9", "b11", [58, 15], after=True), ps("b11", [55, 5.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
