import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 66-P8 (U15-U17, Woche 35 Phase 3): 3rd Man Run Attacking Play (PDF: Third Man Run Attacking Play, Wave of Play).
# 80 x 50 Yards = 73 x 46 m (gerundet 45 x 75 m). GROSSFELD QUER (Vorbild ue319.py): Feld x 7-91 (Länge), y 3-52 (Breite),
# Tore links und rechts, Mittellinie, Mittelkreis, Strafräume und Torräume wie im PDF (dort kleiner als auf einem echten Platz),
# die zwei gepunkteten Linien um die Mitte gestrichelt. massstab "gross". Positionen aus dem PDF quer umgerechnet
# (PDF unten -> links, oben -> rechts, PDF links -> oben, rechts -> unten) und direkt als Querkoordinaten eingetragen.
# Pink -> Team Neon (Nummern wie im PDF), greift nach rechts an. Navy -> Team Rot, greift nach links an, neu nummeriert
# (Nummer + 10, also 4 -> 14, 6 -> 16 usw.; Nummern doppelt). Beide Torhüter neutral (k1 links = PDF 1, k2 rechts = PDF 13).
# Vier Dummys (Stangen) in der Raute um den Mittelkreis. Gezeigt werden je Team sieben Spieler: die Mittelfeldspieler,
# die Spitzen, die Flügelspieler und je ein Verteidiger an der Seitenlinie (Spieler sechzehn für Team Rot, Spieler fünf für
# Team Neon). Die übrigen Wartenden (PDF pink 2, 3, 6 und navy 2, 3, 8) nur im Text. Team Rot hat seine zwei Mittelfeldspieler
# (vierzehn, fünfzehn) schon gespiegelt im Feld stehen (im PDF warten sie hinter der Torlinie). Ein Trainer statt zwei,
# unten an der Seitenlinie nahe dem linken Tor (er versorgt den Torwart mit Bällen).
# Grundform nach PDF Seite 1 (Torwart -> vier -> Spitze neun -> Ablage auf acht -> Steilpass für den Flügel sieben,
# Eins gegen Eins gegen Spieler sechzehn, Abschluss). Fassung 1 = PDF Key Coaching Point (Timing des Laufs, nicht im Abseits).
# Fassung 2 = PDF Progression (Mittelfeldspieler als dritter Mann in die Tiefe); im Video läuft der Ball über mehr Stationen,
# hier vereinfacht: Spieler vier eröffnet, läuft weiter und bekommt den Steilpass von Spieler acht. Verteidiger dort ist Spieler
# dreizehn (PDF navy 3, an der oberen Seitenlinie).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 20, 55.3, "T")  # unten an der Seitenlinie nahe dem linken Tor
ERSATZ = [B("s1", 23.5, 55.8), B("s2", 26, 55.8)]
POS = {"k1": (10.7, 27.5), "k2": (87.3, 27.5),
       "n4": (29.2, 12.8), "n8": (27.3, 43.2), "n9": (52.9, 27.8), "n10": (61.8, 27.8), "n11": (44.4, 12.3), "n7": (46.4, 48),
       "n5": (21.5, 1.5),
       "r14": (70.7, 11.8), "r15": (68.5, 35.5), "r17": (54.1, 12.3), "r21": (54.5, 45), "r20": (44.6, 27.8), "r19": (36.5, 27.8),
       "r16": (76.5, 53.5)}
def sp(extra=None, **k):
    d = dict(POS); d.update(extra or {}); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = 49, 27.5
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 7},
         rect(FX0, 12.5, 17.5, 30), rect(FX1 - 17.5, 12.5, 17.5, 30), rect(FX0, 20, 6.5, 15), rect(FX1 - 6.5, 20, 6.5, 15),
         line(35.5, FY0, 35.5, FY1), line(62.5, FY0, 62.5, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DUMMYS = [C(57.8, 27.8, shape="stange"), C(41.5, 27.8, shape="stange"), C(49.9, 12.5, shape="stange"), C(49.7, 43, shape="stange")]
# Nur die Länge als Maßlinie: Rechts neben dem Tor ist kein Platz, die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "75 m", "45 m")[:1]
BALL = [B("b1", 11.3, 28.1)] + ERSATZ
N9, N8 = [51, 23.5], [39.5, 38.5]  # hier nimmt die Spitze an, hier bekommt Spieler acht die Ablage
LAUF7 = [[57, 49.5], [63, 40.5]]  # Lauf des Flügelspielers in die Tiefe (außen an Spieler einundzwanzig vorbei)
def eroeffnung():
    return [ps("b1", [29.8, 13.4]), mv("n9", N9, delay=0.8), ps("b1", [N9[0] + 0.6, N9[1] + 0.6], after=True), mv("n8", N8, delay=1.2)]

u = {"title": "Dritter Mann in die Tiefe", "code": "UE-396", "kind": "Übungsform",
 "focuses": ["Zusammenspiel", "Passspiel", "1 gegen 1"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 18, "players_max": 22,
 "field_size": "45 x 75 m",
 "description": "Angriffswellen auf einem großen Feld, immer abwechselnd in beide Richtungen. Der Torwart eröffnet, der Ball geht über den Mittelfeldspieler auf die Spitze und wird zum zweiten Mittelfeldspieler abgelegt. Der spielt steil in den Lauf des Flügelspielers, der hinter die Dummys startet. Danach geht es ins Eins gegen Eins und zum Abschluss.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 75 Metern mit zwei großen Toren und Strafräumen. Vier Dummys stehen als Raute um den Mittelkreis.",
  "Verteilen: Zwei Teams und zwei Torhüter. Jedes Team hat zwei Mittelfeldspieler vor dem eigenen Strafraum, eine Spitze in der Mitte und zwei Flügelspieler an den Dummys. Die Verteidiger warten an den Seitenlinien. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart spielt den Mittelfeldspieler an, der spielt auf die Spitze. Die Spitze legt ab für den zweiten Mittelfeldspieler, und der schickt den Flügelspieler in die Tiefe. Ein Verteidiger kommt von der Seitenlinie, es gibt ein Eins gegen Eins mit Abschluss.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Danach greift sofort das andere Team in die Gegenrichtung an. Gewinnt der Verteidiger den Ball, spielt er zu seinem Torwart, und sein Team kontert sofort."],
 "organisation_show": ORG,
 "coaching_points": ["Scharf und genau passen, durch die Linien", "Den Lauf nicht zu früh starten", "Im Eins gegen Eins mutig sein und abschließen", "Schnell spielen, mit Spieltempo"],
 "materials": ["2 große Tore", "4 Dummys", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Dritter Mann in die Tiefe. Angriffswellen über den ganzen Platz. Über die Spitze und eine Ablage kommt der Steilpass, und der Flügelspieler startet hinter die Dummys.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": DUMMYS, "players": sp(), "balls": BALL,
  "steps": [
   S("Torwart eröffnet, Pass auf die Spitze", "Der Torwart spielt flach zu Spieler vier. Spieler neun kommt aus der Mitte entgegen, und Spieler vier spielt ihn sofort an.",
     *eroeffnung()),
   S("Ablage auf Spieler acht", "Spieler acht ist schon nach vorn gerückt. Spieler neun legt mit einem Kontakt ab, genau in seinen Lauf.",
     ps("b1", [N8[0] + 0.6, N8[1] + 0.6])),
   S("Steil in den Lauf von Spieler sieben", "Jetzt startet Spieler sieben, außen an Spieler einundzwanzig vorbei. Spieler acht spielt den Ball steil in den freien Raum. Von der Seitenlinie kommt Spieler sechzehn.",
     mv("n7", LAUF7[0]), mv("n7", LAUF7[1], after=True), ps("b1", [63.6, 41.1], delay=1.0), mv("r16", [74, 41], delay=0.8)),
   S("Eins gegen Eins: Punkt", "Spieler sieben geht mit Tempo auf Spieler sechzehn zu und außen vorbei. Er schließt ab, und das gibt einen Punkt für Team Neon. Sofort geht es in die andere Richtung: Der andere Torwart eröffnet für Team Rot.",
     dr("n7", "b1", [72.5, 46.5]), dr("n7", "b1", [79, 45], after=True), dr("n7", "b1", [83, 37], after=True), mv("r16", [75, 44], delay=0.3), ps("b1", [90.7, 30.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Lauf nicht zu früh starten.", "Nicht zu früh starten",
    "Der Flügelspieler wartet auf einer Höhe mit seinem Gegenspieler. Er startet erst, wenn der Ball zum Ablegen unterwegs ist. So steht er nicht im Abseits und bekommt den Ball im vollen Lauf. Der Pass kommt in den Raum vor ihm, nicht in die Füße.",
    sp(n9=N9), [B("b1", N9[0] + 0.6, N9[1] + 0.6)] + ERSATZ,
    [S("Warten auf einer Höhe", "Spieler neun hat den Ball. Spieler sieben läuft noch nicht. Er geht nur mit bis auf die Höhe von Spieler einundzwanzig.",
       mv("n8", N8), mv("n7", [51.5, 49], delay=0.4)),
     S("Mit der Ablage starten", "Erst wenn Spieler neun ablegt, zieht Spieler sieben an. Spieler acht spielt direkt in den Raum vor ihm.",
       ps("b1", [N8[0] + 0.6, N8[1] + 0.6]), mv("n7", [57, 49.5], delay=0.5), mv("n7", LAUF7[1], after=True), ps("b1", [63.6, 41.1], after=True)),
     S("Im vollen Lauf zum Abschluss: Punkt", "Spieler sieben nimmt den Ball im Lauf mit und zieht in Richtung Tor. Er trifft, und das gibt einen Punkt für Team Neon.",
       dr("n7", "b1", [80, 37]), ps("b1", [90.7, 30.5], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Der Mittelfeldspieler läuft als dritter Mann in die Tiefe.", "Mittelfeld läuft mit",
    "Jetzt startet ein Mittelfeldspieler hinter die Dummys. Spieler vier eröffnet und läuft nach seinem Pass sofort weiter nach vorn. Die Spitze legt ab, und der Steilpass kommt in seinen Lauf. Von der Seitenlinie verteidigt Spieler dreizehn.",
    sp(extra={"r13": (80, 1.5)}), BALL,
    [S("Eröffnen und anspielen", "Wie gehabt spielt der Torwart zu Spieler vier, und Spieler vier spielt die Spitze an.",
       *eroeffnung()),
     S("Ablage, Spieler vier läuft weiter", "Spieler neun legt ab auf Spieler acht. Spieler vier bleibt nicht stehen. Er läuft weiter, an Spieler elf und den Dummys vorbei.",
       ps("b1", [N8[0] + 0.6, N8[1] + 0.6]), mv("n4", [40, 19.5], delay=0.2), mv("n4", [56, 19.5], after=True)),
     S("Steilpass für den dritten Mann", "Spieler acht spielt steil in den Lauf von Spieler vier. Spieler dreizehn kommt von der Seitenlinie und stellt sich ihm.",
       mv("n4", [65, 17]), ps("b1", [65.6, 17.6], delay=0.5), mv("r13", [74, 13], delay=0.5)),
     S("Eins gegen Eins: Punkt", "Spieler vier geht innen an Spieler dreizehn vorbei und schließt ab, und das gibt einen Punkt für Team Neon.",
       dr("n4", "b1", [72, 22]), dr("n4", "b1", [80, 23], after=True), mv("r13", [76, 17], delay=0.3), ps("b1", [90.7, 25], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
