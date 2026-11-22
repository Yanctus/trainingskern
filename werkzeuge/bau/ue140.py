import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-97 (U12-U14, Woche 5 Pre-Season): SAQ Circuit with Crossing to Finish. Halbes Spielfeld nach der PDF-Skizze: Feld x 12-88, y 5-57,
# Tor oben (Jugendtor, D-Jugend dabei) mit neutralem Torwart. Ein Team (Neon), Nummern wie in der Skizze.
# Vereinfacht: Der erste Doppelpass (8 mit 11) fehlt, dafür geht der Ball von 8 direkt quer zu 10. Wartende verschoben (3D-Abstand),
# ein Trainer statt zwei. Sichtkegel aus dem Text ("Head up before delivery to see attackers movement"): Flankengeber schaut zum Stürmer.
T = P("T", "c", 93, 31, "T")
TW = P("k", "t", 50.9, 7.3, "TW")
POS = {"n3": (18.9, 30.8), "n8": (33.8, 33), "n7": (52.1, 43.6), "n10": (61, 56), "n6": (84, 53.7), "n2": (70, 55.5),
       "n5": (20.4, 6.9), "n9": (30, 3), "n4": (39, 2)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
ERSATZ = [B("s1", 94.6, 34.5), B("s2", 96, 28)]
LINES = [rect(12, 5, 76, 52), rect(26, 5, 48.1, 17.6), rect(39, 5, 22, 5.7)]
KEGEL = [C(18.9, 5.3), C(14.7, 12.3), C(23.2, 12.3), C(14.7, 20.6), C(23.2, 20.6), C(18.9, 34),
         C(53, 21.3), C(44.1, 25.5), C(53, 30.5), C(44.3, 34.1), C(53, 39.9)] \
      + [C(34.3, y, shape="huerde_ou") for y in (39.5, 43, 46.5)] + [C(84.1, y, shape="huerde_ou") for y in (35, 38.6, 43.1)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
STUERMER = [[51, 40.2], [46.3, 34], [51, 30.6], [46.1, 25.5], [51, 21.6], [47, 13]]
FLUEGEL = [[84, 47], [84, 31], [83, 25]]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Kreislauf mit Flanke", "code": "UE-140", "kind": "Übungsform",
 "focuses": ["Passspiel", "Torschuss", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 14, "field_size": "Halbes Spielfeld",
 "description": "Ein Kreislauf auf der halben Platzhälfte, der mit einer Flanke und einem Abschluss endet. Der Ball wandert über mehrere Stationen nach vorn, dazwischen laufen die Spieler durch Hütchen, Leiter und Hürden. Ein Doppelpass mit dem Stürmer, ein Steilpass auf den Flügelspieler, der über die Hürden kommt, dann schaut der Flügelspieler auf, flankt, und der Stürmer schließt ab.",
 "organisation": ["Aufbauen: Eine halbe Platzhälfte mit Tor und Torwart. Links oben ein Quadrat aus Hütchen, links in der Mitte eine Leiter, in der Mitte eine Reihe Hütchen im Zickzack bis vor den Strafraum, rechts außen drei Minihürden.",
  "Verteilen: Ein Team verteilt sich auf die Stationen, links beginnt einer mit Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass nach vorn, der Passgeber tippt die Hütchen im Quadrat an. Pass quer in die Mitte, der Passgeber läuft durch die Leiter. Doppelpass mit dem Stürmer, der danach die Hütchen in der Mitte antippt und in den Strafraum läuft. Steilpass auf den Flügel, Flanke, Abschluss.",
  "Wechsel: Nach jedem Durchgang rückt jeder eine Station weiter. Jedes Tor ist ein Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen, vor allem nach außen", "Saubere Technik in Leiter und Hürden, nichts umstoßen", "Vor der Flanke den Kopf heben und den Lauf des Stürmers sehen", "Eiskalt abschließen und mit gutem Timing in den Strafraum laufen"],
 "materials": ["12 Hütchen", "1 Koordinationsleiter", "3 Minihürden", "1 Jugendtor", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Kreislauf mit Flanke. Pässe, Leiter, Hürden und ein Doppelpass, und am Ende eine Flanke zum Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 19.5, 31.4)] + ERSATZ,
  "steps": [
   S("Pass, dann Hütchen antippen", "Neon drei passt nach vorn zu Neon acht und sprintet zum Quadrat oben links, um die Hütchen anzutippen.",
     ps("b1", [34.4, 33.6]), *weg("n3", [[19.5, 22.5], [16.5, 14], [20.5, 9]], after=True)),
   S("Quer, dann durch die Leiter", "Neon acht spielt quer in die Mitte zu Neon zehn und läuft durch die Leiter.",
     ps("b1", [61.6, 56.6]), *weg("n8", [[34.3, 37], [34.3, 49], [38, 52]], after=True)),
   S("Doppelpass, Stürmer läuft los", "Neon zehn spielt einen Doppelpass mit Neon sieben. Der tippt danach im Zickzack die Hütchen an und läuft in den Strafraum. Gleichzeitig springt Neon sechs rechts über die Hürden.",
     ps("b1", [52.7, 44.2]), mv("n10", [66, 49.5], after=True), ps("b1", [66.6, 50.1], after=True), *weg("n7", STUERMER, after=True),
     *weg("n6", FLUEGEL, delay=0.5)),
   S("Steilpass auf den Flügel", "Neon zehn spielt den Ball steil in den Lauf von Neon sechs.",
     ps("b1", [83.6, 25.6])),
   S("Kopf hoch, Flanke: Punkt", "Neon sechs hebt den Kopf, sieht Neon sieben im Strafraum und flankt. Neon sieben schießt direkt ins Tor, und das gibt einen Punkt. Dann rückt jeder eine Station weiter, und Neon fünf beginnt den nächsten Durchgang.",
     bl("n6", [47, 13]), ps("b1", [47.6, 13.6], after=True), ps("b1", [46, 4.7], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Pass auf den Flügel.", "Der Pass nach außen",
    "Der Steilpass auf den Flügel muss so kommen, dass der Flügelspieler ihn im Lauf mit dem ersten oder zweiten Kontakt flanken kann. Zu kurz, und er muss abbremsen, zu lang, und der Ball geht ins Aus.",
    sp(n10=(61, 47), n6=(84, 40), n7=(42, 23)), [B("b1", 61.6, 47.6)] + ERSATZ,
    [S("In den Lauf", "Neon sechs startet, und Neon zehn spielt ihm den Ball genau in den Lauf.",
       mv("n6", [83, 25]), ps("b1", [83.6, 25.6], delay=0.3), mv("n7", [47, 13], delay=0.3)),
     S("Direkt flanken: Punkt", "So kann Neon sechs mit dem ersten Kontakt flanken. Neon sieben trifft, und das gibt einen Punkt.",
       bl("n6", [47, 13]), ps("b1", [47.6, 13.6], after=True), ps("b1", [46, 4.7], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Doppelbewegung im Strafraum.", "Doppelbewegung",
    "Der Stürmer läuft nicht einfach geradeaus in den Strafraum. Er täuscht erst einen Lauf zum ersten Pfosten an und zieht dann scharf zurück in den freien Raum. So hat er Platz und das richtige Timing für den Abschluss.",
    sp(n6=(83, 25), n7=(42, 23)), [B("b1", 83.6, 25.6)] + ERSATZ,
    [S("Antäuschen zum Pfosten", "Neon sieben läuft zuerst Richtung erster Pfosten.",
       mv("n7", [55, 14])),
     S("Zurückziehen, Abschluss: Punkt", "Dann zieht er scharf zurück in den freien Raum. Neon sechs hebt den Kopf, sieht die Bewegung und flankt genau dorthin. Neon sieben trifft, und das gibt einen Punkt.",
       mv("n7", [45, 17]), bl("n6", [45, 17], after=True), ps("b1", [45.6, 17.6], after=True), ps("b1", [46.5, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
