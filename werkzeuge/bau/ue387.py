import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 92-P10 (U15-U17, Woche 31 Phase 1): Building from the Back Under Pressure, Phase of Play. 50 x 80 Yards = 46 x 73 m
# (gerundet 45 x 75 m), Neun-gegen-neun-Platz. GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Feld x 7-91 (Länge),
# y 3-52 (Breite), großes Tor links (Team Neon baut von links auf), drei Minitore rechts. Koordinaten direkt aus der
# PDF-Skizze quer umgerechnet: PDF unten -> links, oben -> rechts, PDF links -> oben, PDF rechts -> unten.
# Platzlinien wie im PDF: Außenlinie, Mittellinie, Mittelkreis, Strafraum und Torraum am großen Tor, Strafraum auf der Seite der
# Minitore; dort die schräg abgeschnittenen Ecken und die Linie fünf Meter (6 Yards) vor der Grundlinie, an der das mittlere
# Minitor steht. Die zwei äußeren Minitore stehen auf den schrägen Linien (Richtung im Board nur „right“ möglich).
# Pink (Torwart 1, Kette 3, 5, 4, 2, Sechser 8 und 6, Zehner 10) -> Team Neon, Nummern wie im PDF, Torwart n1 „TW“.
# Blau -> Team Rot: 7, 9, 11 bleiben; neu nummeriert, weil die Nummern doppelt sind: Blau 6 -> 12, Blau 8 -> 13, Blau 10 -> 14.
# Ein Trainer statt zwei, unten an der Seitenlinie nahe dem großen Tor (er spielt den Ball zum Torwart).
# Grundform nach PDF und Video (0:14-0:40): Torwart -> Spieler 5, Spieler 9 läuft an, Pass auf den freien Sechser 6, der annimmt,
# aufdreht und über die Mittellinie dribbelt; dann zwei gegen zwei mit Spieler 10 aufs Minitor (im Video außen rechts).
# Der Konter von Team Rot (Ballgewinn, über die Mittellinie aufs große Tor) steht nur im Text.
# Fassungen = PDF-Progressionen: 1 der zweite Sechser von Team Rot presst mit (Video 0:56-1:30: Innenverteidiger dribbelt in die
# Mitte, Pass durch die Linie, Ablage auf den dritten Mann; der Zehner kommt als Wandspieler entgegen), 2 drei gegen drei vorn,
# der Außenverteidiger rückt bei der Verlagerung ein (Positionen aus der Skizze der Progression 2, Nummern 3 und 5 wie in der
# Grundform: 5 Innenverteidiger, 3 Außenverteidiger).
# Sichtkegel aus dem PDF („Scan to find the free man“), im Video nicht eingezeichnet: Spieler 5 schaut vor dem Pass zum freien
# Sechser; der Sechser schaut zum Passgeber, nimmt an, dann schwenkt der Kegel nach vorn (bl mit von) und er dreht auf (drehen).
# In Fassung 1 sieht Spieler 5 den entgegenkommenden Zehner, in Fassung 2 schaut der Außenverteidiger zum Torwart und dreht auf.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = 49, (FY0 + FY1) / 2
T = P("T", "c", 22, 55.3, "T")  # unten an der Seitenlinie nahe dem großen Tor
ERSATZ = [B("s1", 25.5, 55.8), B("s2", 28, 55.8)]
NEON = {"n1": (11.5, 27.5), "n5": (14, 12.9), "n4": (14, 42), "n3": (32.7, 8.3), "n2": (33.9, 48.7),
        "n8": (45.4, 18.7), "n6": (43.7, 32.5), "n10": (75.5, 27.9)}
ROT = {"r9": (27.6, 28.2), "r7": (39, 12.2), "r11": (41, 44), "r14": (52.5, 27.9), "r12": (68.5, 17.5), "r13": (69, 38.5)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
# Platzlinien (quer)
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 5.6},
         rect(FX0, 10.7, 19.4, 33.7), rect(FX0, 19, 7.3, 17),
         rect(73.6, 12.3, 17.4, 30.5),
         line(71.9, FY0, 84.7, 19.8, dashed=False), line(84.7, 19.8, 84.7, 35.2, dashed=False), line(84.7, 35.2, 71.9, FY1, dashed=False)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"},
        {"x": 84.7, "y": MY, "side": "right"}, {"x": 76.4, "y": 8.9, "side": "right"}, {"x": 76.4, "y": 46.1, "side": "right"}]
DIMS = dims(FX0, FX1, FY0, FY1, "75 m", "45 m")[:1]
# Stand nach dem Auffächern der Innenverteidiger
BREIT = {"n5": (22, 14.9), "n4": (21.1, 38.8)}

u = {"title": "Freien Sechser im Aufbau finden", "code": "UE-387", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "45 x 75 m",
 "description": "Team Neon baut mit Torwart, Viererkette und zwei Sechsern von hinten auf, vier Angreifer von Team Rot pressen. Gesucht ist immer der freie Sechser. Er nimmt an, dreht auf und dribbelt über die Mittellinie. Dahinter spielt er mit Spieler zehn zwei gegen zwei auf drei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 75 Metern, etwa ein Neun-gegen-neun-Platz. Auf der einen Seite steht ein großes Tor mit Torwart. Auf der anderen Seite stehen drei Minitore, das mittlere 5 Meter vor der Grundlinie, die Ecken sind schräg abgeschnitten.",
  "Verteilen: Team Neon mit Torwart, Viererkette und zwei Sechsern in der eigenen Hälfte, Spieler zehn vorn. Team Rot presst mit drei Angreifern und einem Zehner, seine zwei Sechser warten in der anderen Hälfte. Der Trainer steht mit Bällen an der Seitenlinie nahe dem großen Tor.",
  "Ablauf: Der Torwart eröffnet, und Team Neon spielt sich sieben gegen vier aus der Abwehr. Der freie Sechser nimmt an, dreht auf und dribbelt über die Mittellinie. Dort spielen er und Spieler zehn zwei gegen zwei auf die drei Minitore.",
  "Wertung: Jeder Treffer in ein Minitor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, dribbelt ein Spieler über die Mittellinie und greift das große Tor an, ein Treffer gibt einen Punkt für Team Rot. Danach spielt der Trainer den nächsten Ball zum Torwart."],
 "organisation_show": ORG,
 "coaching_points": ["Lösen und einen Winkel zum Ball anbieten", "Ball laufen lassen, bis die Lücke aufgeht", "Kopf hoch, wo ist der freie Mann?", "Erst langsam locken, dann scharf durch die Linie"],
 "materials": ["1 Großfeldtor", "3 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Freien Sechser im Aufbau finden. Team Neon spielt sich unter Druck von hinten heraus. Der freie Sechser nimmt den Ball mit nach vorn, und dann geht es zwei gegen zwei auf die Minitore.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 12.1, 28.1)] + ERSATZ,
  "steps": [
   S("Breit machen, Torwart eröffnet", "Der Torwart hat den Ball. Spieler fünf und Spieler vier gehen breit an die Ecken vom Strafraum. Dann spielt der Torwart flach zu Spieler fünf.",
     mv("n5", list(BREIT["n5"])), mv("n4", list(BREIT["n4"])), ps("b1", fuss(BREIT["n5"]), after=True)),
   S("Locken, Kopf hoch, freier Sechser", "Spieler neun läuft Spieler fünf an. Spieler acht ist zugestellt, aber drüben steht Spieler sechs frei. Spieler fünf schaut hoch und spielt ihn flach an. Spieler sechs schaut zum Ball.",
     mv("r9", [24.5, 22.5]), bl("n5", [37.6, 27.5], delay=0.3), bl("n6", [24.7, 17.1], delay=0.3), ps("b1", fuss(NEON["n6"]), after=True)),
   S("Aufdrehen und über die Linie", "Spieler sechs nimmt mit dem hinteren Fuß an und dreht dabei auf. Mit dem Ball geht er über die Mittellinie. Jetzt ist es zwei gegen zwei.",
     bl("n6", [57, 38], von=[24.7, 17.1], dauer=1.3), drehen("n6", [57, 38], delay=0.4), dr("n6", "b1", [57, 38], after=True),
     mv("r13", [64, 40], delay=0.8), mv("r12", [66, 28], delay=0.8), mv("n10", [70, 33], delay=0.8)),
   S("Zwei gegen zwei: Punkt", "Spieler dreizehn kommt raus. Sofort spielt Spieler sechs in den Lauf von Spieler zehn, und der schiebt ins Minitor außen. Das gibt einen Punkt für Team Neon. Dann spielt der Trainer den nächsten Ball zum Torwart.",
     mv("r13", [61, 39]), mv("n10", [72.5, 42], delay=0.2), ps("b1", [73.1, 42.6], delay=0.5), ps("b1", [75.6, 46.1], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der zweite Sechser von Team Rot presst mit.", "Zweiter Sechser presst mit",
    "Spieler zwölf darf jetzt aus der anderen Hälfte zurück und deckt Spieler sechs. Damit sind beide Sechser zugestellt. Team Neon hat hinten aber zwei Innenverteidiger gegen einen Stürmer. Einer dribbelt mit Ball in die Mitte, zieht einen Gegner auf sich und findet den freien Mann direkt oder über den Zehner.",
    sp(r12=(51.5, 40), r14=(51.5, 13.5), n10=(71, 27.5), r13=(79, 33), **BREIT), [B("b1", 22.6, 15.5)] + ERSATZ,
    [S("Andribbeln und Druck ziehen", "Spieler zwölf klebt an Spieler sechs, Spieler vierzehn an Spieler acht. Spieler fünf dribbelt mit Ball in die Mitte. Spieler neun muss raus und läuft ihn an.",
       dr("n5", "b1", [29, 23]), mv("r9", [33.5, 29], delay=0.3)),
     S("Durch die Linie, Ablage", "Spieler zehn kommt entgegen. Spieler fünf sieht ihn und spielt scharf durch die Linie. Spieler zehn legt direkt ab auf Spieler acht.",
       mv("n10", [58, 23]), mv("n8", [46, 27], delay=0.4), bl("n5", [49, 23], delay=0.2), ps("b1", [58.6, 23.6], after=True), ps("b1", [46.6, 27.6], after=True)),
     S("Mit Ball nach vorn: Punkt", "Spieler acht nimmt den Ball mit über die Mittellinie. Spieler zehn dreht ab, bekommt den Ball zurück und trifft ins mittlere Minitor. Das gibt einen Punkt für Team Neon.",
       dr("n8", "b1", [60, 30]), mv("n10", [73, 22], delay=0.3), ps("b1", [73.6, 22.6], after=True), ps("b1", [84.1, 27.5], after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Vorn ist es drei gegen drei, und der Außenverteidiger rückt ein.", "Drei gegen drei vorn",
    "Beide Sechser von Team Neon spielen jetzt vorn mit, dort ist es drei gegen drei. Hinten wird es enger. Bei der Verlagerung über den Torwart rückt der Außenverteidiger in den freien Raum vor die Kette ein. Er nimmt offen an und dribbelt mit Tempo nach vorn.",
    sp(n1=(12.6, 27.7), n5=(14.2, 12.9), n4=(14.8, 48.5), n3=(31, 14.6), n2=(32.8, 48.5), n8=(63, 10.3), n10=(66.5, 27.7), n6=(63, 45.7),
       r12=(72.5, 39.5), r14=(72, 16.5), r13=(80, 27.4), r7=(39.6, 6.5), r11=(41, 44.5), r9=(28.5, 33.5)),
    [B("b1", 33.4, 49.1)] + ERSATZ,
    [S("Zurück zum Torwart", "Spieler zwei kommt außen nicht weiter. Er spielt zurück auf Spieler vier, und der legt gleich weiter zum Torwart.",
       mv("r11", [37, 46]), ps("b1", [15.4, 49.1], delay=0.3), ps("b1", [13.2, 28.3], after=True)),
     S("Außenverteidiger rückt ein", "Auf der anderen Seite rückt Spieler drei ein, Spieler fünf geht dafür breit. Spieler drei schaut zum Torwart, und der spielt ihn flach an.",
       mv("n3", [39, 24.1]), mv("n5", [25.3, 7.1], delay=0.2), bl("n3", [15.9, 27.3], after=True), ps("b1", [39.6, 24.7], after=True)),
     S("Aufdrehen, drei gegen drei: Punkt", "Spieler drei dreht auf und dribbelt über die Mittellinie. Vorn spielt er Spieler acht frei. Der trifft ins Minitor außen, und das gibt einen Punkt für Team Neon.",
       bl("n3", [56, 22], von=[15.9, 27.3], dauer=1.3), drehen("n3", [56, 22], delay=0.4), dr("n3", "b1", [56, 22], after=True),
       mv("n8", [71, 12.5], delay=0.6), ps("b1", [71.6, 13.1], after=True), ps("b1", [75.6, 9.5], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
