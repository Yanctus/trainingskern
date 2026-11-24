import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 08-P14 (U15-U17, Woche 16): Direct Counter From Deep (Low Block), 11 gegen 11 auf dem Großfeld (65 x 100 m).
# Das trainierte Team (Pink, 4-4-2) ist Team Neon, Blau (4-3-3) ist Team Rot, neu nummeriert 12-21 (Nummern doppelt).
# Beide Torhüter neutral (k1, k2). Ein Trainer statt zwei.
# GROSSFELD QUER (Inhaber, 24.11.2026): Ein ganzer Platz liegt quer wie im Fernsehbild, Tore links und rechts, mit
# Mittellinie, Mittelkreis, Strafräumen und Torräumen. Team Neon verteidigt links und kontert nach rechts.
# Die Aufstellung ist im Hochformat geplant (x 12-88 Breite, y 4-56 Länge, Team Rot oben); R() legt jede Koordinate
# quer: oben -> rechts, unten -> links, links -> oben, rechts -> unten. Feld quer: x 7-91 (100 m), y 3-52 (65 m).
# Drittel-Linien gestrichelt wie im PDF. Trainer unten an der Seitenlinie in der Hälfte von Team Rot.
# Fassungen: PDF Key Coaching Point 1 (nach Ballgewinn sofort steil auf die Spitze) und 2 (kompakt, nach außen lenken).
# Sichtkegel: aus Ton und PDF ("quickly look for that direct ball into strikers"): Der Balleroberer schaut zur Spitze.
# Im ersten Coaching-Punkt nimmt Spieler neun an und dreht auf: Blick mit von und Drehpfeil.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
def R(x, y): return [round(FX0 + (56 - y) / 52 * (FX1 - FX0), 1), round(FY0 + (x - 12) / 76 * (FY1 - FY0), 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 76, 55.3, "T")  # unten an der Seitenlinie in der Hälfte von Team Rot (quer gesetzt)
ERSATZ = [h.B("s1", 79.5, 55.8), h.B("s2", 82, 55.8)]
NEON = {"k2": (50, 54.5), "n3": (23.5, 48), "n4": (41, 48.5), "n5": (59, 48.5), "n2": (76.5, 48),
        "n7": (23.5, 33), "n6": (41, 33), "n8": (59, 33), "n11": (76.5, 33), "n9": (41, 17.5), "n10": (59, 17.5)}
ROT = {"k1": (50, 7), "r13": (15, 19), "r14": (32.5, 11), "r15": (67.5, 11), "r12": (85, 19),
       "r18": (32, 27), "r16": (50, 23), "r20": (68, 27), "r21": (15, 42), "r19": (50, 39), "r17": (85, 42)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14),
         line(FX0 + 28, FY0, FX0 + 28, FY1), line(FX1 - 28, FY0, FX1 - 28, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
# Nur die Länge als Maßlinie: Rechts neben dem Tor ist kein Platz, die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]
def schieben(dx, wer, **k): return [mv(i, [NEON[i][0] + dx, NEON[i][1]], **k) for i in wer]
MITTE, KETTE = ["n7", "n6", "n8", "n11"], ["n3", "n4", "n5", "n2"]

u = {"title": "Tiefer Block, steiler Konter", "code": "UE-319", "kind": "Spielform",
 "focuses": ["Umschalten", "Verteidigen", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Elf gegen elf auf dem ganzen Platz. Team Neon steht im 4-4-2 tief und eng vor dem eigenen Strafraum und lässt nur die beiden Spitzen vorn. Team Rot baut im 4-3-3 von hinten auf und greift an. Erobert Team Neon den Ball, geht er sofort steil auf eine Spitze, und das Mittelfeld rückt im Sprint nach.",
 "organisation": ["Aufbauen: Das ganze Großfeld mit zwei Toren. Der Trainer steht mit vielen Bällen an der Seitenlinie in der Hälfte von Team Rot.",
  "Verteilen: Team Neon im 4-4-2 mit zwei engen Viererketten in der eigenen Hälfte und zwei Spitzen vorn. Team Rot im 4-3-3, die Außenverteidiger schieben beim Angriff hoch.",
  "Ablauf: Der Trainer spielt den Ball zu einem Verteidiger von Team Rot. Team Rot baut gegen die zwei Spitzen auf und greift an. Team Neon lenkt nach außen und fängt den Pass in die Mitte ab. Dann geht der Ball direkt auf eine Spitze, und der Konter läuft.",
  "Wertung: Jeder Treffer gibt einen Punkt. Nach jedem Angriff bringt der Trainer den nächsten Ball wieder zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Eng stehen, die Mitte bleibt zu", "Ball gewonnen? Kopf hoch und steil auf die Spitze", "Spitzen bleiben anspielbar, auch wenn wir verteidigen", "Mittelfeld im Sprint hinterher"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Tiefer Block, steiler Konter. Elf gegen elf auf dem ganzen Platz. Team Neon steht tief und kontert nach dem Ballgewinn direkt über die beiden Spitzen.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", 76.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein, Rot baut auf", "Der Trainer spielt den Ball zu Spieler fünfzehn. Team Rot baut hinten zu viert gegen unsere zwei Spitzen auf. Die beiden Spitzen schieben mit zum Ball.",
     ps("b1", [68.1, 11.6]), mv("n10", [62, 16], delay=0.5), mv("n9", [47, 18], delay=0.5)),
   S("Nach außen lenken, Block schiebt", "Weiter geht es nach außen zu Spieler zwölf, der hoch aufgerückt ist. Genau da wollen wir den Ball haben. Beide Viererketten schieben eng zusammen auf die Ballseite.",
     ps("b1", [85.6, 19.6]), *schieben(4, MITTE, delay=0.3), *schieben(4, KETTE, delay=0.3), mv("r20", [60, 26], delay=0.4), mv("n10", [66, 20], delay=0.3)),
   S("Pass in die Mitte abgefangen", "Spieler zwölf will flach in die Mitte auf Spieler neunzehn spielen. Spieler acht steht richtig, geht in den Passweg und hat den Ball.",
     ps("b1", [63.6, 33.2]), mv("n8", [63, 32.6], delay=0.2)),
   S("Kopf hoch, steil auf die Spitze", "Jetzt muss es schnell gehen. Spieler acht nimmt sofort den Kopf hoch. Spieler zehn startet in den Raum hinter Spieler zwölf, und da kommt der Ball hin.",
     bl("n8", [76, 14]), mv("n10", [76, 14], delay=0.6), ps("b1", [76.6, 14.6], after=True)),
   S("Mittelfeld rückt nach", "Spieler fünfzehn stellt Spieler zehn. Kein Problem, von hinten kommt Spieler acht im Sprint und bekommt den Ball zurück. Vorn läuft Spieler neun zwischen die Innenverteidiger.",
     mv("r15", [72, 12]), mv("n8", [66, 24], delay=0.2), mv("n11", [82, 25], delay=0.2), mv("n6", [50, 28], delay=0.3),
     mv("n9", [55, 13], delay=0.3), mv("r14", [45, 11], delay=0.4), ps("b1", [66.6, 24.6], delay=1.2)),
   S("Durchgesteckt: Punkt", "Spieler acht steckt durch auf Spieler neun. Der schiebt am Torwart vorbei ein, und das gibt einen Punkt für Team Neon. Danach bringt der Trainer den nächsten Ball wieder zu Team Rot.",
     mv("n9", [57, 9.5]), ps("b1", [57.6, 10.1]), ps("b1", [54.5, 3.7], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Ballgewinn sofort steil.", "Sofort steil auf die Spitze",
    "Der erste Pass nach dem Ballgewinn geht nach vorn auf eine Spitze, nicht quer und nicht zurück. Team Rot ist aufgerückt und braucht ein paar Sekunden, um sich zu ordnen. In dieser Zeit muss der Ball vorn sein. Die zweite Spitze startet sofort in die Tiefe.",
    sp(), [B("b1", 15.6, 42.6)] + ERSATZ,
    [S("Tief am Strafraum erobert", "Team Rot ist weit aufgerückt. Spieler einundzwanzig spielt von außen flach in die Mitte. Spieler sechs läuft dazwischen und holt sich den Ball.",
       ps("b1", [40.6, 40.9]), mv("n6", [40, 40.3], delay=0.2)),
     S("Kopf hoch, steil auf Spieler neun", "Kein Querpass, kein Rückpass. Spieler sechs schaut hoch und spielt flach und scharf durch die Mitte auf Spieler neun. Der zeigt sich schon und schaut zum Ball.",
       bl("n6", [41, 17.5]), ps("b1", [41.6, 18.1], after=True)),
     S("Aufdrehen, durchstecken: Punkt", "Spieler neun nimmt an und dreht auf. Spieler zehn ist schon in die Tiefe gestartet und bekommt den Ball in den Lauf. Er trifft, und das gibt einen Punkt für Team Neon.",
       bl("n9", [58, 11], von=[40, 40.3], dauer=1.3), drehen("n9", [58, 11], delay=0.4), mv("n10", [58, 11], delay=0.6),
       ps("b1", [58.6, 11.6], after=True), ps("b1", [54.5, 3.7], after=True))],
    dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Eng stehen und nach außen lenken.", "Eng stehen, nach außen lenken",
    "Beide Viererketten stehen eng, durch die Mitte kommt kein Pass. Team Rot muss außen herum spielen. Dort schiebt der ganze Block zum Ball, einer läuft an, die anderen lauern auf den Pass nach innen. Wer ihn abfängt, schaut sofort nach vorn zu den Spitzen.",
    sp(), [B("b1", 50.6, 23.6)] + ERSATZ,
    [S("Die Mitte ist zu", "Spieler sechzehn hat den Ball im Zentrum. Unsere Mittelfeldkette zieht sich eng zusammen. Durch die Mitte geht nichts, also spielt er raus auf Spieler dreizehn.",
       mv("n6", [44.5, 32]), mv("n8", [55.5, 32]), mv("n7", [30, 33]), mv("n11", [70, 33]), ps("b1", [15.6, 19.6], delay=0.8)),
     S("Außen anlaufen, alle schieben", "Spieler sieben läuft Spieler dreizehn an und macht die Linie zu. Der ganze Block schiebt mit nach links. Spieler sechs stellt sich in den Weg nach innen.",
       dr("r13", "b1", [15, 24.5]), mv("n7", [20.5, 29.5], delay=0.2), mv("n6", [26, 32.5], delay=0.3), mv("n8", [42, 32], delay=0.3), mv("n11", [58, 33], delay=0.3),
       *schieben(-5, KETTE, delay=0.4)),
     S("Pass nach innen abgefangen", "Spieler dreizehn bleibt nur der Pass nach innen auf Spieler achtzehn. Darauf hat Spieler sechs gewartet. Er geht dazwischen, hat den Ball, und der Konter kann starten.",
       ps("b1", [25.1, 26.6]), mv("n6", [24.5, 26], delay=0.2))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
