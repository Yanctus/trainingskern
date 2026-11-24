import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P8 (U15-U17, Woche 21 Phase 2): Build-Up and Supporting Attacking Runs (Wave). 25 x 40 Yards = 23 x 37 m (gerundet 25 x 35 m).
# LANGES FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51), Tore links
# und rechts mit neutralem Torwart (Großfeldtor, nur C- und B-Jugend). Die erste Gruppe greift von links nach rechts an
# (im PDF von unten nach oben). Koordinaten direkt quer gesetzt: PDF oben -> rechts, PDF links -> oben.
# PDF blau (drei Gruppen zu drei Angreifern: 4, 8, 2 / 9, 10, 11 / 14, 12, 7) -> Team Neon mit den Nummern aus dem PDF.
# PDF pink (drei Mittelfeldspieler 4, 8, 10, spielen für jede Welle) -> drei Springer (F, team t): Nummern wären doppelt, und sie
# helfen jeder Gruppe. Im Text „der Springer außen“ (PDF pink 4), „der Springer in der Mitte“ (pink 8), „der Springer vorn“ (pink 10).
# Zehn Puppen als Stangen an den Plätzen aus dem PDF. Strafraum rechts gestrichelt wie im PDF. Ein Trainer an der Seitenlinie unten.
# Wartende Gruppen hinter den Grundlinien, in der Tiefe auseinander (3D-Abstand); Spieler acht und zwei etwas auseinandergerückt.
# Grundform = Passfolge aus dem PDF: Torwart -> 8 -> Springer außen (klatscht) -> 2 -> steil Springer vorn -> Ablage Springer Mitte
# -> steil auf den Läufer 4 -> Flanke, 2 und 8 sprinten in den Strafraum. Wer abschließt, ist im Original offen (hier Spieler acht).
# Fassungen: PDF Progression 1 (freie Kombinationen, im Video „scan to see teammates runs“) und Progression 2 (der Springer außen
# wird beim Pass nach außen zum Verteidiger, wie im Video).
# Sichtkegel: Ton Progression 1 „communication and scanning are essential … constantly checking positions“, Video-Text
# „scan to see teammates runs“: Springer in der Mitte schaut zum Passgeber, nach der Annahme schwenkt der Kegel zum Läufer
# (bl mit von plus drehen). In der Grundform kein Kegel im Original.
T = P("T", "c", 36, 55.3, "T")
ERSATZ = [B("s1", 39.5, 55.8), B("s2", 42, 55.8)]
POS = {"k1": (13.8, 25.6), "k2": (85, 27.5), "n4": (25.3, 10.7), "n8": (15, 43), "n2": (24.5, 50.5),
       "f4": (47.7, 45.8), "f8": (48.5, 27), "f10": (66.4, 29.2),
       "n9": (94, 9), "n10": (94, 40), "n11": (94, 56), "n14": (4, 9), "n12": (4, 38), "n7": (4, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "f": "t", "k": "t"}[i[0]], x, y, {"n": i[1:], "f": "F", "k": "TW"}[i[0]]) for i, (x, y) in d.items()] + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
PUPPEN = [(70.8, 21.5), (70.8, 33.3), (55.7, 13.8), (55.7, 27), (56.5, 41.6), (42.1, 14.1), (42.1, 27.2), (42.8, 41.7),
          (24.7, 21.2), (24.7, 33.1)]
CONES = [C(x, y, shape="stange") for x, y in PUPPEN]
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
MY = (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), rect(73.6, 14.3, 15.4, 25.8, dashed=True)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DIMS = dims(FX0, FX1, FY0, FY1, "35 m", "25 m")[:1]
BAELLE = [B("b1", *fuss("k1")), B("b2", *fuss("k2"))] + ERSATZ

u = {"title": "Welle durch die Puppen", "code": "UE-357", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "25 x 35 m",
 "description": "Eine Welle mit drei Angreifergruppen auf zwei Tore. Zehn Puppen stehen als Gegenspieler im Feld, dazwischen helfen drei Springer im Mittelfeld. Der Ball läuft mit ein, zwei Kontakten durch die Puppen bis zum Läufer außen. Die anderen zwei Angreifer sprinten in den Strafraum, und gleich danach kommt die nächste Gruppe aus der anderen Richtung.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 35 Metern mit einem großen Tor auf jeder Grundlinie. Zehn Puppen stehen verteilt im Feld, vor dem Tor ist der Strafraum markiert.",
  "Verteilen: In jedem Tor steht ein Torwart. Team Neon spielt in drei Gruppen zu drei Angreifern, eine im Feld und je eine hinter den Toren. Drei Springer stehen zwischen den Puppen. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart spielt die erste Gruppe an. Über die Springer läuft der Ball mit ein, zwei Kontakten durch die Puppen, bis der Steilpass auf den Läufer außen kommt. Der flankt, die anderen zwei Angreifer sind im Sprint im Strafraum.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon. Ist der Angriff vorbei, startet sofort die nächste Gruppe in die andere Richtung. Die Springer bleiben im Feld und werden nach ein paar Minuten getauscht."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem Pass sofort Vollgas in den Strafraum", "Ein, zwei Kontakte, dann ist der Ball weg", "Kurz weg von der Puppe, dann anbieten", "Auch mit müden Beinen ruhig flanken und abschließen"],
 "materials": ["2 große Tore", "10 Puppen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Welle durch die Puppen. Drei Angreifer spielen sich mit den Springern durch die Puppen, und nach dem Steilpass geht es im Sprint in den Strafraum. Dann kommt sofort die nächste Gruppe von der anderen Seite.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BAELLE, "dims": DIMS,
  "steps": [
   S("Torwart eröffnet auf Spieler acht", "Der Torwart spielt flach zu Spieler acht, damit läuft die erste Gruppe. Gleichzeitig löst sich der Springer außen kurz von seiner Puppe.",
     ps("b1", fuss("n8")), mv("f4", [45, 48.5], delay=0.3)),
   S("Klatschen lassen auf Spieler zwei", "Spieler acht spielt den Springer an. Der lässt den Ball direkt klatschen, und Spieler zwei kommt ihm entgegen.",
     ps("b1", [45.6, 49.1]), mv("n2", [31, 51], delay=0.3), ps("b1", [31.6, 51.6], after=True)),
   S("Steil auf den Springer vorn", "Jetzt kommt der Steilpass. Spieler zwei spielt durch die Puppen auf den Springer vorn. Außen startet schon Spieler vier.",
     mv("f10", [63, 33.5]), ps("b1", [63.6, 34.1], delay=0.4), mv("n4", [48, 8.5], delay=0.4)),
   S("Ablage und durch auf Spieler vier", "Der Springer vorn legt zurück auf den Springer in der Mitte. Der spielt sofort durch auf Spieler vier, genau in den Lauf. Spieler acht und Spieler zwei sprinten los.",
     mv("f8", [51, 21]), ps("b1", [51.6, 21.6], delay=0.3), mv("n4", [70, 8.5], after=True), ps("b1", [70.6, 9.1]),
     mv("n2", [48, 35], delay=0.3), mv("n8", [38, 51.5], delay=0.3)),
   S("Flanke und Abschluss: Punkt", "Spieler vier flankt in den Strafraum. Spieler zwei kommt an den ersten Pfosten, Spieler acht an den zweiten und schiebt ein. Das gibt einen Punkt für Team Neon. Sofort startet die nächste Gruppe mit Spieler neun, zehn und elf in die andere Richtung.",
     mv("n2", [64, 37]), mv("n2", [78, 22], after=True), mv("n8", [64, 50], delay=0.1), mv("n8", [80, 35], after=True),
     dr("n4", "b1", [79, 8.6], delay=0.2), ps("b1", [80.6, 35.6], after=True), ps("b1", [88.4, 31], after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Spieler kombinieren frei.", "Frei kombinieren",
    "Die Passfolge ist nicht mehr fest. Die Angreifer tauschen die Plätze, die Springer bieten sich immer wieder neu an. Vor jeder Annahme geht der Kopf hoch: Wo läuft mein Mitspieler hin? Und alle reden miteinander.",
    sp(), BAELLE,
    [S("Neuer Weg über die Mitte", "Diesmal geht es anders los. Der Torwart spielt raus auf Spieler zwei. Der Springer in der Mitte kommt ihm entgegen und schaut zum Ball. Dann kommt der Pass.",
       ps("b1", fuss("n2")), mv("f8", [48.5, 34.5], delay=0.3), bl("f8", fuss("n2"), after=True), ps("b1", [49.1, 35.1], after=True)),
     S("Annehmen, aufdrehen, Läufer sehen", "Erst nach der Annahme dreht er auf. Der Blick geht nach vorn, und da sieht er Spieler vier, der außen startet. Der Ball kommt in seinen Lauf.",
       bl("f8", [62, 9], von=fuss("n2"), dauer=1.3), drehen("f8", [62, 9], gegen=True, delay=0.4), mv("n4", [62, 8.5], delay=0.3),
       ps("b1", [62.6, 9.1], after=True)),
     S("Plätze getauscht: Punkt", "Spieler acht und Spieler zwei haben die Seiten getauscht und sind im Sprint vorn. Spieler vier spielt flach in die Mitte, Spieler zwei trifft. Das gibt einen Punkt für Team Neon.",
       mv("n2", [40, 51.5]), mv("n2", [66, 49], after=True), mv("n2", [79, 35], after=True), mv("n8", [34, 37]), mv("n8", [49, 35], after=True), mv("n8", [77, 21], after=True),
       dr("n4", "b1", [76, 8.6], delay=0.3), ps("b1", [79.6, 35.6], after=True), ps("b1", [88.4, 30], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein Springer wird zum Verteidiger.", "Springer wird Verteidiger",
    "Sobald der Ball nach außen gespielt wird, sprintet der Springer außen zurück in den Strafraum und verteidigt die Flanke. Die Angreifer müssen jetzt noch schneller nachrücken. Wer zu spät kommt, hat gegen ihn keine Chance.",
    sp(), BAELLE,
    [S("Aufbau wie gewohnt", "Der Torwart spielt Spieler acht an. Der spielt den Springer in der Mitte an, der kurz entgegenkommt.",
       ps("b1", fuss("n8")), mv("f8", [48.5, 34.5], delay=0.3), ps("b1", [49.1, 35.1], after=True)),
     S("Pass nach außen ist das Signal", "Der Springer in der Mitte spielt nach außen auf Spieler zwei, der durchgestartet ist. Genau das ist das Signal. Der Springer außen dreht um und sprintet in den Strafraum.",
       mv("n2", [44, 51.5]), mv("n2", [66, 50.5], after=True), ps("b1", [66.6, 51.1], delay=1.2),
       mv("f4", [60, 47.5], delay=1.2), mv("f4", [79, 31], after=True), mv("n8", [34, 37], delay=0.4), mv("n8", [49, 35], after=True), mv("n4", [48, 8.5], delay=0.4)),
     S("Schneller sein: Punkt", "Spieler zwei flankt. Spieler acht ist vor dem Verteidiger am Ball und schiebt ein. Das gibt einen Punkt für Team Neon. Klärt der Verteidiger, ist der Angriff vorbei.",
       mv("n8", [64, 30]), mv("n8", [78, 22], after=True), mv("n4", [76, 12], delay=0.1), dr("n2", "b1", [77, 49.5], delay=0.2),
       ps("b1", [78.6, 22.6], after=True), ps("b1", [88.4, 25], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
