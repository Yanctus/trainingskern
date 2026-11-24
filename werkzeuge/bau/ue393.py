import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 08-P10 (U15-U17, Woche 34 Phase 5): Organised Defending to Counter (Phase of Play), 8 gegen 8 auf zwei Dritteln des Platzes.
# GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Feld quer wie im PDF und im Video, Tor links, drei Minitore rechts.
# Feld x 7-91 = 70 m (zwei Drittel eines Platzes von 105 m, so breit wie der Platz, 65 m), y 3-52, massstab "gross".
# Spielzone 40 x 40 Yards laut PDF und Ton; hier 35 m lang (ab der gestrichelten Drittellinie bei x 49) und über die ganze Breite
# wie in Skizze und Video. Mittellinie bei x 70 mit Mittelkreis, links Strafraum und Torraum, Großfeldtor (C- und B-Jugend).
# Direkt quer geplant (kein R()), Positionen aus dem PDF umgerechnet und leicht verschoben (3D-Abstand). Nicht gedreht.
# PDF pink (verteidigt im 4-3-1, Nummern 2-10 wie im PDF) -> Team Neon. Blau -> Team Rot, neu nummeriert, weil die Nummern
# doppelt sind: 2 -> 12, 3 -> 13, 4 -> 14, 5 -> 15, 6 -> 16, 8 -> 18, 9 -> 19, 10 -> 20; der grüne Torwart ist der Torwart
# von Team Rot (r1, TW). Ein Trainer statt zwei, unten an der Seitenlinie bei der Spielzone.
# Grundform nach der Zerlegung im Video: Aufbau, Pass nach außen, Pass zwischen die Linien, Spieler fünf fängt ab, schneller
# Konter über Spieler neun ins drei gegen zwei.
# Fassungen: PDF Key Coaching Point 1 (als Block schieben, außen zumachen, nach innen lenken, dort erobern) und 2 (im drei gegen
# zwei den freien Spieler finden und schnell abschließen).
# Sichtkegel: Text „Awareness of attacking players positions to counter after turnover“, im Video nicht eingezeichnet:
# Spieler fünf schaut nach dem Ballgewinn zu Spieler neun. Im zweiten Coaching-Punkt („Find the free player“) nimmt Spieler
# neun an, der Kegel schwenkt vom Passgeber zum freien Spieler acht, dazu der Drehpfeil.
# Keine Dublette: UE-319 (08-P14, elf gegen elf, tiefer Block mit 4-4-2, ganzer Platz, zwei große Tore) und UE-122 (08-P1,
# Dribbelbahnen) sind andere Übungen.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MY = 27.5
T = h.P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie bei der Spielzone
ERSATZ = [h.B("s1", 53.5, 55.8), h.B("s2", 56, 55.8)]
NEON = {"n2": (81, 8), "n5": (85, 20), "n6": (85, 35), "n3": (80.5, 47), "n8": (67, 16.5), "n4": (72, 30.5),
        "n10": (65.5, 39), "n9": (55, 26)}
ROT = {"r1": (11, 27.5), "r13": (60, 10), "r20": (74, 13), "r15": (48.5, 19.5), "r14": (61, 27.5), "r19": (79, 27),
       "r16": (48.5, 38), "r18": (74, 42), "r12": (59, 50)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(k)
    return [P(i, "b", x, y, "TW") if i == "r1" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(70, FY0, 70, FY1, dashed=False), {"type": "circle", "x": 70, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.2, 19.8, 30.4), rect(FX0, MY - 6.9, 6.6, 13.8), line(49, FY0, 49, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"},
        {"x": FX1, "y": 11, "side": "right"}, {"x": FX1, "y": MY, "side": "right"}, {"x": FX1, "y": 44, "side": "right"}]
DIMS = dims(FX0, FX1, FY0, FY1, "70 m", "65 m")[:1]  # nur die Länge (rechts neben den Toren ist kein Platz)
# Stand im zweiten Coaching-Punkt: Konter läuft, drei gegen zwei im letzten Drittel
KONTER = {"n8": (36, 15.5), "n9": (31, 28), "n10": (32, 40), "r15": (24.7, 24.5), "r16": (25, 37), "r1": (10.6, 27.2),
          "r13": (50, 9), "r20": (58, 14), "r14": (42.7, 26.7), "r19": (62.8, 26.6), "r18": (68, 38), "r12": (48.5, 41.3),
          "n2": (66.5, 9), "n5": (73.3, 21.2), "n6": (74.5, 32.6), "n3": (63, 50), "n4": (56.4, 26.7)}

u = {"title": "Kompakt stehen, schnell kontern", "code": "UE-393", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 17, "players_max": 17,
 "field_size": "65 x 70 m",
 "description": "Acht gegen acht auf zwei Dritteln des Platzes. Team Rot hat den Ball und will die Ordnung von Team Neon verschieben und in eins von drei Minitoren treffen. Team Neon steht kompakt, macht außen zu und erobert den Ball innen. Dann geht es schnell ins letzte Drittel, wo drei Angreifer gegen zwei Verteidiger und den Torwart spielen.",
 "organisation": ["Aufbauen: Ein Feld über zwei Drittel des Platzes, 70 Meter lang und so breit wie der Platz. Rund um die Mittellinie die Spielzone, 35 Meter lang, mit drei Minitoren an der Endlinie. Davor das letzte Drittel mit Strafraum und großem Tor.",
  "Verteilen: Team Neon mit Viererkette, drei Mittelfeldspielern und einer Spitze in der Spielzone vor den Minitoren. Team Rot mit sechs Spielern in der Spielzone, zwei Verteidigern an der Drittellinie und dem Torwart im großen Tor. Der Trainer steht mit vielen Bällen an der Seitenlinie.",
  "Ablauf: Der Trainer spielt zu Team Rot. Team Rot lässt den Ball laufen und will durch den Block in ein Minitor. Team Neon schiebt als Block, macht außen zu und erobert den Ball innen. Danach geht es schnell ins letzte Drittel, drei gegen zwei auf das große Tor.",
  "Wertung: Jeder Treffer gibt einen Punkt für das Team, das trifft. Erobert Team Rot den Ball im letzten Drittel, kontert es sofort auf die Minitore. Nach jedem Abschluss bringt der Trainer den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Als Block schieben, außen zumachen", "Laut ansagen, wann wir schieben und wann eng machen", "Ball erobert? Kopf hoch, wo steht die Spitze", "Im drei gegen zwei schnell abschließen"],
 "materials": ["1 Großfeldtor", "3 Minitore", "Hütchen für die Drittellinie", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Kompakt stehen, schnell kontern. Acht gegen acht auf zwei Dritteln des Platzes. Team Neon verteidigt als Block und kontert nach dem Ballgewinn ins drei gegen zwei.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein, Rot baut auf", "Der Trainer spielt zu Spieler sechzehn, und der gibt weiter zu Spieler fünfzehn. Unsere Spitze, Spieler neun, macht den Weg durch die Mitte zu.",
     ps("b1", f(48.5, 38)), ps("b1", f(48.5, 19.5), after=True), mv("n9", [54, 24], delay=1.2)),
   S("Pass nach außen, der Block schiebt", "Spieler fünfzehn spielt raus zu Spieler dreizehn. Sofort schiebt der ganze Block mit zur Seite. Spieler zwei läuft an und macht den Weg die Linie entlang zu.",
     ps("b1", f(60, 10)), mv("n2", [67, 5], delay=0.4), mv("n8", [66, 17], delay=0.4), mv("n5", [83, 16], delay=0.5),
     mv("n6", [83, 30], delay=0.5), mv("n3", [79, 41], delay=0.5), mv("n4", [71, 29], delay=0.5), mv("n10", [66, 34], delay=0.5), mv("r14", [62, 33], delay=0.5)),
   S("Pass nach innen, abgefangen", "Außen ist zu. Spieler dreizehn spielt nach innen auf Spieler zwanzig zwischen unsere Linien. Der will weiter zu Spieler neunzehn, aber Spieler fünf ist schneller und fängt den Pass ab.",
     ps("b1", f(74, 13)), mv("n5", [77, 21], delay=0.6), ps("b1", f(77, 21), after=True)),
   S("Kopf hoch, schnell nach vorn", "Spieler fünf hebt sofort den Kopf und sucht Spieler neun. Flach zu ihm, und los. Spieler acht und Spieler zehn sprinten mit nach vorn. Die zwei Verteidiger von Team Rot laufen zurück.",
     bl("n5", [61, 23.2]), ps("b1", f(54, 24), after=True), mv("n8", [50, 12], delay=0.5), mv("n8", [36, 12], after=True),
     mv("n10", [55, 45], delay=0.5), mv("n10", [38, 40], after=True), mv("r15", [30, 22], delay=0.7), mv("r16", [30, 34], delay=0.7)),
   S("Drei gegen zwei: Punkt", "Drei gegen zwei im letzten Drittel. Spieler neun dribbelt an, und Spieler fünfzehn muss raus. Der Pass geht zu Spieler acht, der frei ist und trifft, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball wieder zu Team Rot.",
     dr("n9", "b1", [40, 26]), mv("r15", [34, 24], delay=0.5), mv("n8", [28, 16], delay=0.5), ps("b1", f(28, 16), after=True), ps("b1", [7.3, 24.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Als Block schieben und nach innen lenken.", "Als Block schieben",
    "Kommt der Ball nach außen, schiebt der ganze Block mit. Der äußere Spieler läuft so an, dass der Weg die Linie entlang zu ist. Dann bleibt nur der Pass nach innen, und dort stehen wir eng und erobern den Ball.",
    sp(), [B("b1", *f(48.5, 19.5))] + ERSATZ,
    [S("Pass nach außen, alle schieben", "Spieler fünfzehn spielt raus zu Spieler dreizehn. Sofort schiebt der ganze Block zur Seite. Spieler zwei läuft von außen an, damit der Weg die Linie entlang zu ist.",
       ps("b1", f(60, 10)), mv("n2", [67, 5], delay=0.4), mv("n8", [66, 17], delay=0.4), mv("n5", [82, 15], delay=0.5),
       mv("n6", [83, 29], delay=0.5), mv("n3", [80, 41], delay=0.5), mv("n4", [68, 28], delay=0.5), mv("n10", [66, 35], delay=0.5)),
     S("Nach innen gelenkt, Ball erobert", "Außen geht nichts, also spielt Spieler dreizehn nach innen auf Spieler vierzehn. Genau da wollen wir ihn haben. Spieler vier und Spieler neun gehen zu zweit drauf, und Spieler vier erobert den Ball.",
       ps("b1", f(61, 27.5)), mv("n4", [63.5, 29.5], after=True), mv("n9", [58.5, 27.5], delay=0.8), dr("n4", "b1", [67, 33], after=True))],
    dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Im drei gegen zwei den Freien finden.", "Den Freien finden",
    "Im letzten Drittel ist immer einer frei, wenn alle drei mitlaufen. Wer den Ball hat, bindet einen Verteidiger. Der nächste schaut schon vor der Annahme, wo der Freie steht. Schnell spielen und schnell abschließen, bevor Team Rot zurück ist.",
    sp(**KONTER), [B("b1", *f(32, 40))] + ERSATZ,
    [S("Spieler zehn bindet einen", "Drei gegen zwei im letzten Drittel. Spieler zehn kommt mit Ball, und Spieler sechzehn muss raus zu ihm. Spieler neun zeigt sich und schaut zum Ball. Spieler acht läuft in den freien Raum.",
       mv("r16", [28, 37.5]), bl("n9", [32, 40], delay=0.3), ps("b1", f(31, 28), after=True), mv("n8", [27, 17], delay=0.6)),
     S("Kopf hoch, der Freie trifft: Punkt", "Spieler fünfzehn geht auf Spieler neun. Der hat Spieler acht schon gesehen, dreht auf und spielt quer. Spieler acht trifft, und das gibt einen Punkt für Team Neon.",
       mv("r15", [28, 26.5]), bl("n9", [27, 17], von=[32, 40], dauer=1.3), drehen("n9", [27, 17], delay=0.4),
       ps("b1", f(27, 17), after=True), ps("b1", [7.3, 24], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
