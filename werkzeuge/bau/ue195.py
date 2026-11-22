import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 100-P3 (U12-U14, Woche 23 Phase 3): Improve Striker Movement Finishing 1 v 1. 35 x 40 Yards = Feld x 22.5-77.5, y 5-51
# (36 x 32 m). Gedreht (90 Grad): im PDF liegt das Tor rechts, hier oben. Jugendtor mit neutralem Torwart (grün -> k, TW),
# Strafraum als Rechteck, die Linie mit den drei Dummys (Stangen) gestrichelt. Blau (7, 10, 11, Neun) -> Team Neon, der passive
# Verteidiger pink 4 -> Rot vier. Im PDF-Text heißt der mittlere Spieler 11, in der Skizze 10: hier wie die Skizze (7 außen,
# 10 Mitte, 11 außen). Hütchen gelb -> neon, links neben den Spielern (sonst gehen die Pässe durch). Rot vier steht etwas höher
# als im PDF (3D-Abstand zur Neun). Ein Trainer statt zwei (der zweite am Tor entfällt), er steht links neben Neon sieben.
# Sichtkegel aus dem Text ("awareness of GK position"): Neon neun schaut vor dem Abschluss zum Torwart.
T = P("T", "c", 25, 55, "T")
POS = {"k": (50, 8.5), "r4": (41, 22), "n9": (45.5, 39), "n7": (37, 55), "n10": (50, 55), "n11": (63, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i == "k" else ("a" if i[0] == "n" else "b"), x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 21.4, 55), B("s2", 18, 55)]
LINES = [rect(22.5, 5, 55, 46), rect(34.5, 5, 31, 9), line(22.5, 35, 77.5, 35)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(39.3, 37, shape="stange"), C(50.3, 34, shape="stange"), C(62.5, 37, shape="stange"),
         C(34, 51.5, "neon"), C(47, 51.5, "neon"), C(60, 51.5, "neon")]

u = {"title": "Stürmer im Eins gegen Eins", "code": "UE-195", "kind": "Übungsform",
 "focuses": ["Torschuss", "1 gegen 1", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "36 x 32 m",
 "description": "Der Stürmer löst sich von einer Stange und bekommt den Ball nach zwei Pässen aus dem Mittelfeld. Mit dem ersten Kontakt dreht er sich nach vorn und geht ins Eins gegen Eins gegen einen Verteidiger, der nur mitläuft. Dann schließt er gegen den Torwart ab. Nach jedem Abschluss wird gewechselt, und der nächste Stürmer ist dran.",
 "organisation": ["Aufbauen: Ein Feld von 36 mal 32 Metern mit einem Jugendtor oben und einem Strafraum. Drei Stangen stehen in einer Reihe in der Mitte, drei Hütchen an der unteren Linie.",
  "Verteilen: Ein Torwart steht im Tor, Rot vier ist der Verteidiger und läuft nur mit. Neon neun ist der Stürmer an der mittleren Stange. Neon sieben, Neon zehn und Neon elf stehen unten an den Hütchen, der Trainer links mit Bällen.",
  "Ablauf: Der Trainer spielt zu Neon sieben, der legt nach innen zu Neon zehn ab. Neon zehn spielt nach vorn zu Neon neun. Neon neun dreht sich mit dem ersten Kontakt auf und geht ins Eins gegen Eins.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für den Stürmer. Danach geht der Stürmer auf ein Hütchen, und ein Mittelfeldspieler wird der neue Stürmer. Mal von links, mal von rechts beginnen."],
 "organisation_show": ORG,
 "coaching_points": ["Mit einer schnellen Doppelbewegung von der Stange lösen", "Der erste Kontakt geht nach vorn in den freien Raum", "Mutig ins Eins gegen Eins gehen", "Vor dem Schuss zum Torwart schauen und ruhig abschließen"],
 "materials": ["1 Jugendtor", "3 Stangen", "3 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Stürmer im Eins gegen Eins. Neon neun löst sich von der Stange, dreht auf und schließt gegen den Torwart ab.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 25.6, 55.6)] + ERSATZ,
  "steps": [
   S("Pass nach außen", "Der Trainer spielt den Ball zu Neon sieben.",
     ps("b1", [37.6, 55.6])),
   S("Nach innen ablegen", "Neon sieben legt den Ball nach innen zu Neon zehn. Gleichzeitig läuft Neon neun erst zum Tor und kommt dann schnell zurück.",
     ps("b1", [50.6, 55.6]), mv("n9", [44, 33.5]), mv("n9", [46, 40], after=True)),
   S("Aufdrehen", "Neon zehn spielt nach vorn zu Neon neun. Neon neun nimmt den Ball mit dem ersten Kontakt nach vorn mit.",
     ps("b1", [46.6, 40.6]), dr("n9", "b1", [58, 32], after=True)),
   S("Eins gegen eins: Punkt", "Rot vier kommt entgegen, aber Neon neun geht an ihm vorbei. Er schaut, wo der Torwart steht, und schießt ins lange Eck. Das gibt einen Punkt für Neon neun. Danach geht Neon neun auf ein Hütchen, und Neon zehn ist der neue Stürmer.",
     mv("r4", [53, 27]), dr("n9", "b1", [60, 22], delay=0.3), mv("k", [53, 9], delay=0.3),
     bl("n9", [50, 8.5], after=True), ps("b1", [46.5, 5.4], after=True))],
  "dims": dims(22.5, 77.5, 5, 51, "36 m", "32 m", rx=83)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit einer schnellen Doppelbewegung lösen.", "Doppelbewegung",
    "Der Stürmer täuscht zuerst einen Lauf zum Tor an. Dann stoppt er und kommt blitzschnell zurück, seitlich an der Stange vorbei. Er steht halb offen und kann den Ball gleich nach vorn mitnehmen.",
    sp(), [B("b1", 50.6, 55.6)] + ERSATZ,
    [S("Erst weg", "Neon zehn hat den Ball. Neon neun läuft erst schnell Richtung Tor, als wollte er hinter die Stange.",
       mv("n9", [44, 32.5])),
     S("Dann zurück", "Dann stoppt er und kommt blitzschnell zurück. Jetzt ist er frei, und Neon zehn spielt ihn an.",
       mv("n9", [45.5, 40]), ps("b1", [46.1, 40.6], delay=0.3)),
     S("Halb offen", "Neon neun steht halb offen. So nimmt er den Ball mit dem ersten Kontakt gleich nach vorn mit.",
       dr("n9", "b1", [58, 32]))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Mittelfeldspieler läuft hinterher und bekommt den Ball zurück.", "Doppelpass an der Stange",
    "Jetzt spielt Neon zehn nach vorn zu Neon neun und läuft sofort weiter an der Stange vorbei. Neon neun hält den Ball und spielt ihn zurück in den Lauf. Neon zehn schließt ab.",
    sp(), [B("b1", 50.6, 55.6)] + ERSATZ,
    [S("In die Spitze", "Neon zehn spielt nach vorn zu Neon neun.",
       ps("b1", [46.1, 39.6])),
     S("Hinterherlaufen", "Neon zehn läuft sofort weiter nach vorn, an der Stange vorbei. Neon neun hält so lange den Ball.",
       mv("n10", [56, 44]), mv("n10", [56.5, 31], after=True)),
     S("Doppelpass: Punkt", "Neon neun spielt den Ball in den Lauf von Neon zehn. Der schießt direkt ins kurze Eck, und das gibt einen Punkt für Neon zehn.",
       ps("b1", [57.1, 31.6]), ps("b1", [53, 5.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
