import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-106 (U15-U17, Woche 5 Pre-Season): SAQ Circuit and MSG. Ganzer Platz (65 x 100 m): eine Hälfte 8 gegen 8, die andere ein
# Laufzirkel mit drei Bahnen. GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Im PDF liegt der Zirkel oben, das Spiel unten.
# Quer gelegt: oben -> rechts, unten -> links, links -> oben, rechts -> unten. Feld x 7-91, y 3-52, massstab "gross".
# Zirkel rechts: oben die Ringe-Bahn (vier Ringe, dann Sprint zum Dummy), in der Mitte der Slalom mit Ball um drei Dummys mit
# Abschluss aufs große Tor, unten vier Minihürden und vier Stangen im Slalom. Das zweite Spielfeld-Tor steht wie im PDF auf der
# Mittellinie (side "right", öffnet zum Spiel). Dummys (Mannequins) als Stangen gezeichnet.
# Gelb -> Team Neon, Nummern 3, 4, 5, 6, 8, 9, 10 (die gelbe 2 weggelassen, damit es acht gegen acht mit Torwart ist).
# Pink -> Team Rot, neu nummeriert 11-17 (Nummern doppelt). Beide Torhüter neutral (k1, k2) wie bei UE-319, weil zwei
# Team-Torhüter mit Label TW als doppelte Nummer gelten; sie bleiben beim Wechsel im Tor (Annahme). Dunkelblau (Zirkelgruppe) ->
# neutrale Gruppe (team t) mit Nummern 18-22 wie bei UE-310; von sieben im PDF stehen fünf auf der Tafel, der Rest nur im Text.
# Aufstellung im Spiel für den 3D-Abstand in Spalten geordnet (grob wie im PDF). Ein Trainer statt zwei (unten an der Mittellinie).
# Reihenfolge im Zirkel gedeutet (PDF zeigt die drei Bahnen ohne Nummern): Slalom mit Abschluss -> Hürden und Stangen -> Ringe
# und Sprint zum Dummy -> zurück zum Slalom. Pro Bahn läuft immer einer, ist er durch, startet der Nächste (Text und Ton).
# Spielzug im Spiel wie im Video (Torwart -> 4 -> 8 -> 9). Wechsel nach Video („Losing team switches out“) und Ton
# (Gegentor: Ballbesitz für das Team, das es bekommen hat; Sieger bleibt drin).
# Fassungen: PDF Key Coaching Point 1 (schnell erholen und zur nächsten Station) und 2 (nach Ballgewinn in den Raum hinter der
# Abwehr). Sichtkegel aus dem Text von KCP 2 („recognise and attack the space in behind“): Der Balleroberer schaut in den Raum
# hinter der Kette, bevor er spielt. Im Video kein Kegel eingezeichnet.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
T = P("T", "c", 42, 55.3, "T")
ERSATZ = [B("s1", 45.5, 55.8), B("s2", 48, 55.8)]
NEON = {"k1": (9.5, 27.5), "n3": (15.5, 10), "n5": (15.5, 22), "n4": (15.5, 40), "n6": (21.5, 24),
        "n10": (27.5, 17), "n8": (27.5, 42), "n9": (33.5, 27)}
ROT = {"k2": (46, 27.5), "r16": (21.5, 12), "r17": (21.5, 36.5), "r13": (27.5, 5), "r14": (27.5, 29.5),
       "r15": (33.5, 45), "r11": (39.5, 16), "r12": (39.5, 38)}
ZIRKEL = {"t18": (52.5, 9), "t19": (46.5, 9), "t20": (55, 30), "t22": (54, 45), "t23": (48, 45)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(ZIRKEL); d.update(k)
    out = []
    for i, (x, y) in d.items():
        t = {"n": "a", "r": "b", "t": "t", "k": "t"}[i[0]]
        out.append(P(i, t, x, y, "TW" if i[0] == "k" else i[1:]))
    return out + [T]
def fuss(i, d=None): x, y = (d or {}).get(i) or {**NEON, **ROT, **ZIRKEL}[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"},
        {"x": MX, "y": MY, "side": "right", "size": "gross"}]
RINGE = [(58, 8), (62.5, 12), (67, 8), (71.5, 12)]
DUMMYS = [(60, 25), (66, 31), (72, 25)]
HUERDEN = [(58.5, 45), (61.5, 45), (64.5, 45), (67.5, 45)]
STANGEN = [(72, 42.5), (77, 47.5), (82, 42.5), (87, 47.5)]
CONES = [ring(x, y) for x, y in RINGE] + [C(84, 9.5, shape="stange")] + [C(x, y, shape="stange") for x, y in DUMMYS] \
    + [C(x, y, shape="huerde") for x, y in HUERDEN] + [C(x, y, shape="stange") for x, y in STANGEN]
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]
def weg(who, pkt, **k): return [mv(who, list(pkt[0]), **k)] + [mv(who, list(p), after=True) for p in pkt[1:]]
def dweg(who, ball, pkt, **k): return [dr(who, ball, list(pkt[0]), **k)] + [dr(who, ball, list(p), after=True) for p in pkt[1:]]
SLALOM = [(59.5, 30), (63, 26), (66, 25.5), (69, 30), (72, 30.5), (75.5, 25)]
RINGWEG = [list(r) for r in RINGE] + [[81.5, 10.5]]
HUERDENWEG = [(57, 45), (69, 45), (72, 46.5), (77, 43.5), (82, 46.5), (87, 43.5), (89.5, 45)]
TOR_R = [90.7, 25.5]
BAELLE = [B("b1", *fuss("k1")), B("b2", *fuss("t20"))] + ERSATZ

u = {"title": "Laufzirkel und 8 gegen 8", "code": "UE-330", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Umschalten", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 16, "players_max": 23,
 "field_size": "65 x 100 m",
 "description": "Der Platz ist zweigeteilt. Auf der einen Hälfte spielen Team Neon und Team Rot acht gegen acht, auf der anderen läuft eine dritte Gruppe einen Zirkel mit drei Bahnen: Slalom mit Ball und Abschluss, Hürden und Stangen, Ringe und Sprint zum Dummy. Sind alle aus dem Zirkel durch, wechselt das Team, das im Spiel hinten liegt, in den Zirkel. Die Zirkelgruppe spielt dann gegen den Sieger.",
 "organisation": ["Aufbauen: Ein ganzer Platz. In der einen Hälfte drei Bahnen nebeneinander: vier Ringe und dahinter ein Dummy, drei Dummys für den Slalom vor dem großen Tor, vier Minihürden und vier Stangen. In der anderen Hälfte steht ein zweites großes Tor auf der Mittellinie.",
  "Verteilen: Drei Gruppen zu sieben und zwei Torhüter. Team Neon und Team Rot spielen acht gegen acht, die beiden Torhüter sind neutral und bleiben immer im Tor. Die dritte Gruppe verteilt sich auf die drei Startpunkte des Zirkels. Der Trainer steht mit Bällen an der Mittellinie.",
  "Ablauf: Auf jeder Bahn läuft immer nur einer. Ist er durch, startet der Nächste, und er selbst trabt zur nächsten Bahn. Gleichzeitig läuft das Spiel. Wer ein Gegentor bekommt, bekommt sofort den Ball vom Torwart und spielt weiter.",
  "Wertung und Wechsel: Jeder Treffer im Spiel gibt einen Punkt. Sind alle aus dem Zirkel durch, sprintet das Team, das hinten liegt, in den Zirkel. Die Zirkelgruppe spielt gegen den Sieger, der auf dem Platz bleibt."],
 "organisation_show": ORG,
 "coaching_points": ["Vollgas im Zirkel und im Spiel", "Nach der Bahn im Laufen durchatmen, nicht stehen bleiben", "Ball gewonnen? Sofort in den Raum hinter der Abwehr", "Sauber annehmen und passen, auch mit schweren Beinen"],
 "materials": ["3 Großfeldtore", "4 Dummys", "4 Stangen", "4 Ringe", "4 Minihürden", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Laufzirkel und acht gegen acht. Auf der einen Hälfte wird gespielt, auf der anderen gelaufen. Wer verliert, muss in den Zirkel.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Zirkel: alle drei Bahnen laufen", "Wir fangen im Zirkel an. Spieler zwanzig dribbelt im Slalom um die drei Dummys. Oben hüpft Spieler achtzehn durch die Ringe, und unten springt Spieler zweiundzwanzig über die Hürden.",
     *dweg("t20", "b2", SLALOM[:5]), *weg("t18", RINGWEG[:4], delay=0.3), *weg("t22", HUERDENWEG[:2], delay=0.3)),
   S("Abschluss, Stangen, Sprint zum Dummy", "Nach dem letzten Dummy zieht Spieler zwanzig ab, flach ins lange Eck. Spieler achtzehn sprintet zum Dummy und tippt ihn an. Spieler zweiundzwanzig geht im Slalom durch die Stangen.",
     dr("t20", "b2", list(SLALOM[5])), ps("b2", TOR_R, after=True), mv("t18", RINGWEG[4], delay=0.3), *weg("t22", HUERDENWEG[2:], delay=0.3)),
   S("Weiter zur nächsten Bahn", "Wer durch ist, trabt zur nächsten Bahn und stellt sich an. Spieler zwanzig geht zu den Hürden, Spieler achtzehn zum Slalom, Spieler zweiundzwanzig zu den Ringen. Dort starten schon Spieler neunzehn und Spieler dreiundzwanzig.",
     mv("t20", [66, 39]), mv("t20", [52, 50], after=True), mv("t18", [57, 19]), mv("t18", [56, 31], after=True),
     mv("t22", [88, 18]), mv("t22", [76, 4.5], after=True), mv("t22", [53, 4.5], after=True),
     *weg("t19", [[52.5, 9]] + [list(r) for r in RINGE], delay=0.4), *weg("t23", [[54, 45]] + [list(h) for h in HUERDENWEG[:2]], delay=0.4)),
   S("Im Spiel: über außen nach vorn", "Jetzt zum Spiel acht gegen acht. Der Torwart links spielt flach zu Spieler vier. Der legt weiter auf Spieler acht, und Spieler acht spielt steil in die Mitte zu Spieler neun.",
     ps("b1", fuss("n4")), ps("b1", fuss("n8"), after=True), ps("b1", fuss("n9"), after=True)),
   S("Abschluss im Spiel: Punkt", "Spieler neun nimmt den Ball mit Richtung Tor und schließt ab. Der Torwart springt in die falsche Ecke, und das gibt einen Punkt für Team Neon. Team Rot bekommt sofort den nächsten Ball vom Torwart. Sind alle aus dem Zirkel durch, sprintet das Team, das hinten liegt, in den Zirkel, und die Zirkelgruppe spielt gegen den Sieger.",
     dr("n9", "b1", [40, 24]), mv("k2", [46, 31], delay=0.6), ps("b1", [48.6, 25.2], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schnell erholen und gleich zur nächsten Bahn.", "Schnell erholen, weiter",
    "Nach jeder Bahn geht es sofort weiter zur nächsten. Durchgeatmet wird im Laufen, nicht im Stehen. Wer trödelt, lässt die ganze Gruppe warten. Das ist wie im Spiel: Nach einem Sprint kommt sofort die nächste Aktion.",
    sp(t20=(69, 30)), [B("b1", *fuss("k1")), B("b2", 69.6, 30.6)] + ERSATZ,
    [S("Abschluss, dann sofort los", "Spieler zwanzig kommt um den letzten Dummy und schließt ab. Kein Jubeln, kein Stehenbleiben. Er dreht sich um und trabt sofort zu den Hürden.",
       dr("t20", "b2", [72, 30.5]), dr("t20", "b2", list(SLALOM[5]), after=True), ps("b2", TOR_R, after=True),
       mv("t20", [66, 39], after=True), mv("t20", [60, 50.5], after=True)),
     S("Im Laufen durchatmen", "Auf dem Weg atmet er tief durch. Spieler dreiundzwanzig ist schon dran und springt über die Hürden. Spieler zwanzig stellt sich direkt dahinter an und ist als Nächster bereit.",
       *weg("t22", HUERDENWEG[:3]), *weg("t23", [[54, 45], [57, 45]], delay=0.6), mv("t20", [48, 45], delay=0.6))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Nach dem Ballgewinn sofort in den Raum hinter der Abwehr.", "Ballgewinn, ab in die Tiefe",
    "Team Rot ist weit aufgerückt. Hinter der Abwehr ist viel Platz bis zum Tor. Wer den Ball erobert, schaut sofort dorthin. Die Mitspieler starten im selben Moment, schnell und genau gespielt ist der Konter durch.",
    sp(r16=(21.5, 12), r17=(21.5, 36.5), r13=(27.5, 5), r14=(27.5, 29), r11=(33.5, 12), r12=(33.5, 42), r15=(9.5, 44),
       n10=(27.5, 17), n8=(27.5, 41), n9=(33.5, 27)),
    [B("b1", 28.1, 29.6), B("b2", *fuss("t20"))] + ERSATZ,
    [S("Abgefangen", "Team Rot greift an. Spieler vierzehn will in die Mitte zu Spieler siebzehn spielen. Spieler acht läuft dazwischen und hat den Ball.",
       ps("b1", [23.8, 34.6]), mv("n8", [23.2, 34], delay=0.1)),
     S("Kopf hoch, Raum hinter der Kette", "Kopf hoch. Spieler acht sieht den freien Raum hinter der Abwehr. Spieler neun startet genau da hinein, und der Ball kommt flach in seinen Lauf.",
       bl("n8", [41, 33]), mv("n9", [41, 33], after=True), mv("n10", [38, 20], delay=0.6), ps("b1", [41.6, 33.6], delay=1.2)),
     S("Allein aufs Tor: Punkt", "Spieler neun nimmt den Ball mit und schiebt am Torwart vorbei ein, und das gibt einen Punkt für Team Neon. Team Rot war zu weit weg.",
       dr("n9", "b1", [43, 29]), mv("k2", [46, 25], delay=0.3), ps("b1", [48.6, 30], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
