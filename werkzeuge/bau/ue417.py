import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 03-P14 (U15-U17, Woche 42 Phase 6): 11 v 11 Game Defend in the Defending Third. Ganzer Platz (Full Length x Full Width),
# 11 gegen 11 (65 x 100 m wie bei UE-319). Navy (PDF) / Weiß (Video), das trainierte Team im 4-2-3-1, ist Team Neon mit
# Nummern wie im Video (Kette 3, 6, 5, 2; Sechser 8, 4; dahinter 7, 10, 11; Spitze 9).
# Pink (PDF) / Orange (Video) ist Team Rot, neu nummeriert, weil alle Nummern doppelt sind: n -> n + 10
# (2 -> 12 ... 11 -> 21). Der PDF-Text nennt ein 4-3-3, Skizze und Video zeigen ein 3-4-3 (drei hinten, vier im Mittelfeld,
# drei vorn): so aufgestellt. Beide Torhüter neutral (k1, k2) wie bei UE-319 (zwei TW-Nummern gehen nicht). Ein Trainer statt zwei.
# GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Das Video liegt schon quer, Team Neon verteidigt links und kontert
# nach rechts. Feld x 7-91, y 3-52, massstab "gross", echte Platzlinien (ohne Drittel-Linien, die hat das Original nicht).
# Nur die Längen-Maßlinie. Trainer unten an der Seitenlinie in der Hälfte von Team Neon, nah an der Stelle, wo er einspielt.
# Grundform nach Video (0:05-0:21, „Forcing play wide“, „Get tight“, „Keep wide“, „(4) Protect inside“, „Takeover“): Mitte zu,
# Pass nach außen, Außenverteidiger eng dran und innen, der Sechser sichert nach innen, Spieler elf läuft den Hinterlaufenden
# mit zurück, Flanke geblockt, zweiter Ball (PDF „win second balls“), Konter. Die Wertung (jeder Treffer ein Punkt) und den
# Konter bis zum Abschluss gibt das Original nicht genau vor; ergänzt, damit die Runde ein Ende hat. Spieler zehn dreht nach
# der Annahme mit dem Drehpfeil auf (kein Blickkegel, im Original wird dort nicht gescannt).
# Fassungen: PDF Key Coaching Point (mit Druck auf den Ball rückt die Kette raus, Abseits; Video Progression 2) und PDF
# Progression (Trainer gibt Flanken vor, Läufer mitnehmen, erster Kontakt klärt, zweiter Ball; Video Progression 1 und 3).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Keine Dublette: UE-319 (08-P14, tiefer Block mit Konter), UE-356 (10-P14, Pressing), UE-098 (03-P6, kleines Spiel),
# UE-378 (03-P5, zentral als Paar), UE-399 (03-P10, zwei Viererketten gegen sieben), UE-400 (03-P9, Dreierkette und zwei Sechser).
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
T = P("T", "c", 37, 55.3, "T")  # unten an der Seitenlinie in der Hälfte von Team Neon
ERSATZ = [B("s1", 40.5, 55.8), B("s2", 43, 55.8)]
POS = {"k1": (11.5, 27.5), "n3": (24, 9), "n6": (22, 21.5), "n5": (22, 33.5), "n2": (24, 46),
       "n8": (37, 21), "n4": (37, 34), "n7": (50.5, 8), "n10": (50.5, 27.5), "n11": (50.5, 47), "n9": (61, 27.5),
       "r21": (30.5, 12), "r19": (30.5, 27.5), "r17": (30.5, 41),
       "r12": (44, 4.5), "r18": (44, 16.5), "r20": (44, 33), "r13": (44, 49.5),
       "r15": (68, 14), "r16": (68, 30), "r14": (68, 43), "k2": (84, 27.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]

u = {"title": "Elf gegen elf, nach außen lenken", "code": "UE-417", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Elf gegen elf auf dem ganzen Platz. Team Neon verteidigt im 4-2-3-1 das eigene Drittel gegen Team Rot im 3-4-3. Die Mitte bleibt zu, der Angriff wird nach außen gelenkt, und dort geht der Außenverteidiger eng drauf, damit keine Flanke kommt. Nach dem Ballgewinn holt Team Neon den zweiten Ball und kontert schnell.",
 "organisation": ["Aufbauen: Der ganze Platz mit zwei großen Toren. Der Trainer steht mit vielen Bällen an der Seitenlinie in der Hälfte von Team Neon.",
  "Verteilen: Team Neon mit Torwart im 4-2-3-1, die Viererkette steht vor dem eigenen Strafraum. Team Rot mit Torwart im 3-4-3, die drei Spitzen stehen schon hoch.",
  "Ablauf: Der Trainer spielt den Ball zu Team Rot ins Mittelfeld. Team Neon macht die Mitte zu und lenkt den Angriff nach außen. Der Außenverteidiger geht eng drauf, ein Sechser sichert nach innen ab, und nach dem Ballgewinn geht es schnell nach vorn.",
  "Wertung: Jeder Treffer gibt einen Punkt für das Team, das trifft. Nach jedem Angriff spielt der Trainer sofort den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Mitte zu, nach außen lenken", "Außenverteidiger eng dran, keine Flanke", "Läufer mitnehmen, der erste Kontakt gehört uns", "Zweite Bälle holen, mit Druck rückt die Kette raus"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Elf gegen elf, nach außen lenken. Team Neon verteidigt auf dem ganzen Platz das eigene Drittel, lenkt den Gegner nach außen und lässt dort keine Flanke zu.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 37.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein, die Mitte ist zu", "Der Trainer spielt Spieler zwanzig im Mittelfeld an. Team Neon steht kompakt vor dem eigenen Strafraum. Spieler acht und Spieler vier rücken zusammen, Spieler zehn läuft von vorn an. Durch die Mitte geht jetzt nichts.",
     ps("b1", fu(POS["r20"])), mv("n8", [38, 24.5], delay=0.4), mv("n4", [39, 31], delay=0.4), mv("n10", [48, 30], delay=0.4)),
   S("Raus nach außen, Kette schiebt", "Also geht der Ball raus zu Spieler siebzehn. Spieler zwei ist sofort da und stellt sich innen an ihn. Spieler vier sichert den Weg nach innen ab. Die Viererkette schiebt mit zur Ballseite.",
     ps("b1", fu(POS["r17"])), mv("n2", [27.5, 39], delay=0.2), mv("n4", [33.5, 36], delay=0.3),
     mv("n5", [22, 35.5], delay=0.3), mv("n6", [21, 26], delay=0.3), mv("n3", [21.5, 17.5], delay=0.3)),
   S("Außen halten, Spieler elf läuft mit", "Spieler siebzehn will nach innen ziehen. Geht nicht, Spieler zwei steht eng und lässt ihn nur außen lang. Hinten kommt Spieler dreizehn hinterlaufen. Den übernimmt Spieler elf und läuft den ganzen Weg mit zurück.",
     dr("r17", "b1", [26, 49]), mv("n2", [24.5, 45.5], delay=0.2), mv("r13", [35, 50.5], delay=0.2), mv("n11", [39, 47], delay=0.4)),
   S("Flanke geblockt, zweiter Ball", "Jetzt will er flanken. Spieler zwei ist so nah dran, dass er den Ball blockt. Der springt zurück ins Feld, und Spieler vier ist als Erster am zweiten Ball. Spieler zehn bietet sich schon an.",
     ps("b1", [31.6, 40.6]), mv("n4", [31, 40], delay=0.2), mv("n10", [45, 21], delay=0.5)),
   S("Schnell nach vorn: Punkt", "Spieler vier spielt sofort zu Spieler zehn. Der dreht auf, Spieler neun startet hinter die Abwehr, und der Ball kommt steil. Er trifft, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Team Rot.",
     ps("b1", fu([45, 21])), mv("n9", [75, 17], delay=0.6), drehen("n10", [75.6, 17.6], delay=0.2, after=True),
     ps("b1", fu([75, 17]), after=True), ps("b1", [90.5, 24], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Steht Druck auf dem Ball, rückt die Kette raus.", "Mit Druck die Kette hoch",
    "Kann der Gegner mit dem Ball nicht nach vorn spielen, weil zwei drauf sind, rückt die ganze Viererkette gemeinsam raus. Einer gibt das Kommando, alle vier schieben gleichzeitig. Der Raum vor dem Tor wird klein, und die Spitzen von Team Rot stehen im Abseits.",
    sp(), [B("b1", *fu(POS["r18"]))] + ERSATZ,
    [S("Zwei gehen auf den Ball", "Spieler achtzehn hat den Ball im Mittelfeld. Spieler acht und Spieler zehn gehen gleichzeitig drauf. Er hat keinen freien Blick nach vorn.",
       mv("n8", [40.5, 19.5]), mv("n10", [48.5, 20.5], delay=0.1)),
     S("Die ganze Kette rückt raus", "Das ist das Zeichen. Spieler sechs ruft raus, und alle vier schieben gleichzeitig hoch. Der Torwart geht ein paar Meter mit. Die drei Spitzen von Team Rot stehen plötzlich hinter der Linie.",
       mv("n3", [33, 7.5]), mv("n6", [33, 21]), mv("n5", [33, 34]), mv("n2", [33, 46.5]), mv("k1", [16, 27.5], delay=0.2)),
     S("Steilpass ins Abseits", "Spieler achtzehn spielt trotzdem steil auf Spieler einundzwanzig. Der steht im Abseits, der Trainer pfeift, und Team Neon hat den Ball.",
       ps("b1", fu(POS["r21"])))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer schickt den Ball auf den Flügel, und es kommt eine Flanke.", "Flanke verteidigen",
    "Der Trainer spielt den Flügelspieler frei an, und der flankt. Jeder Verteidiger nimmt seinen Läufer mit und bleibt zwischen ihm und dem Tor. Wer zuerst am Ball ist, klärt weit raus. Den zweiten Ball holt sich ein Sechser.",
    sp(r17=(30.5, 47.5)), [B("b1", 37.6, 55.9)] + ERSATZ,
    [S("Trainer spielt auf den Flügel", "Der Trainer spielt Spieler siebzehn ganz außen an. Spieler zwei geht raus, kommt aber nicht mehr ganz heran.",
       ps("b1", fu([30.5, 47.5])), mv("n2", [26, 47.5], delay=0.3)),
     S("Läufer mitnehmen", "Spieler neunzehn und Spieler einundzwanzig laufen in den Strafraum, Spieler zwanzig kommt hinterher. Jeder Verteidiger nimmt seinen Mann mit und bleibt zwischen ihm und unserem Tor stehen.",
       mv("r19", [16, 30]), mv("n5", [13.5, 31], delay=0.2), mv("r21", [17, 21]), mv("n6", [14, 23], delay=0.2),
       mv("r20", [26, 31], delay=0.3), mv("n4", [24, 33], delay=0.4)),
     S("Erster Kontakt, zweiter Ball", "Die Flanke kommt an den ersten Pfosten. Spieler fünf ist vor seinem Gegenspieler dran und köpft weit raus. Spieler vier holt sich den zweiten Ball.",
       ps("b1", fu([13.5, 31])), ps("b1", [28, 40], after=True), mv("n4", [27.4, 39.4], delay=0.8))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
