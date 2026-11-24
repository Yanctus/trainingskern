import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 51-P10 (U15-U17, Woche 15): Break Through Pressure to Attack. 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m).
# Hochkant wie im PDF, Aufbau unten, Angriff nach oben. Feld x 25-75, y 5-55, in der Breite gestreckt (3D-Abstand).
# Zwei Großfeldtore mit Torwart (nur C- und B-Jugend). PDF blau -> Team Neon (4, 5, 6, 8, 10 wie im PDF),
# pink -> Team Rot, grüne Torhüter -> neutrale Torhüter (k1 unten, k2 oben). Team Rot neu nummeriert, weil die Nummern doppelt sind: 2 -> 2, 6 -> 3, 4 -> 7, 8 -> 9, 10 -> 11. Ein Trainer statt zwei.
# Positionen leicht auseinandergezogen (3D-Abstand), Spieler acht und Spieler sieben stehen knapp über der Mittellinie.
# Fassung 1 = PDF Key Coaching Point 1 (Innenverteidiger breit, Zehner zieht weg, Sechser in die Lücke; Annehmen und Aufdrehen
# mit bl(von=...) und drehen()). Fassung 2 = Key Coaching Point 2 (außen annehmen, hinterlaufen, flanken); im PDF/Video zeigt
# das die pinke Mannschaft im Angriff nach unten, hier spielt es Team Neon nach oben.
# Sichtkegel: Text/Ton „Recognise space early“, „Identify and use the free player“; im Video nicht eingezeichnet,
# Richtung aus dem Sinn: Spieler vier schaut vor dem Steilpass in den Raum hinter der Kette, vor der Flanke in die Mitte.
T = P("T", "c", 12, 46, "T")
ERSATZ = [B("s1", 15.6, 49.5), B("s2", 12, 49.5)]
POS = {"k1": (50, 53.5), "n5": (29, 46.5), "n4": (59, 49), "n6": (46.5, 36.5), "n10": (29, 31), "n8": (73, 27),
       "k2": (50, 7.5), "r2": (37.5, 27), "r3": (55, 33), "r7": (64.5, 27), "r9": (38, 43), "r11": (67.5, 43)}
POS2 = {"k1": (50, 53), "n5": (29, 47), "n4": (71, 46.5), "n6": (50, 31), "n8": (67, 26), "n10": (33, 24),
        "k2": (50, 7.5), "r2": (41.5, 20), "r3": (58.5, 31), "r7": (58.5, 15), "r9": (40, 42), "r11": (62.5, 46.5)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(25, 5, 50, 50), line(25, 30, 75, 30)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 55, "side": "bottom", "size": "gross"}]
CONES = ecken(25, 5, 50, 50) + [C(25, 30), C(75, 30)]
DIMS = dims(25, 75, 5, 55, "25 m", "40 m", rx=88)

u = {"title": "Durch den Druck nach vorn", "code": "UE-317", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "25 x 40 m",
 "description": "Fünf gegen fünf plus Torhüter auf einem schmalen, langen Feld. Team Neon baut vom Torwart aus auf, Team Rot läuft früh an. Hinter der Kette von Team Rot ist viel Platz, zur Seite kaum. Wer den Druck überspielt und einen Mitspieler in der Tiefe findet, kommt zum Abschluss.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern mit Mittellinie. Auf jeder Grundlinie steht ein großes Tor.",
  "Verteilen: Team Neon und Team Rot spielen mit je fünf Feldspielern, in jedem Tor steht ein Torwart. Alle Feldspieler stehen zu Beginn in der Hälfte von Team Neon. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart unten eröffnet für Team Neon. Team Neon spielt sich durch das Anlaufen und sucht den Pass in die Tiefe. Dann geht es ohne Pause zum Abschluss aufs andere Tor. Erobert Team Rot den Ball, greift es sofort selbst an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach einem Treffer oder wenn der Torwart den Ball hält, eröffnet der Torwart auf der anderen Seite, und das andere Team baut auf."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo ist der Platz hinter der Kette?", "Nach vorn spielen, wenig Kontakte", "Ruhig bleiben, wenn der Gegner anläuft", "Den freien Mann finden und anspielen"],
 "materials": ["2 große Tore", "6 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Durch den Druck nach vorn. Fünf gegen fünf plus Torhüter auf einem schmalen, langen Feld. Team Neon baut hinten auf, Team Rot läuft an, und hinter der Kette wartet der Platz für den Angriff.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 54.1)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Torwart eröffnet", "Der Torwart unten hat den Ball, Team Neon baut auf. Er spielt flach nach links zu Spieler fünf. Spieler neun läuft sofort an.",
     ps("b1", [29.6, 47.1]), mv("r9", [36, 43.5], delay=0.3)),
   S("Quer auf die freie Seite", "Links wird es eng. Also geht der Ball quer zu Spieler vier, der rechts Zeit hat. Spieler elf kommt zu spät.",
     ps("b1", [59.6, 49.6]), mv("r11", [66, 45.5], delay=0.4), mv("r9", [40, 45], delay=0.4)),
   S("Kopf hoch, steil in die Tiefe", "Spieler vier hebt den Kopf und sieht den Platz hinter der Kette. Vorn löst sich Spieler zehn im Rücken von Spieler zwei. Der Pass kommt flach durch die Mitte, genau in seinen Lauf.",
     bl("n4", [51, 31]), mv("n10", [31, 24], delay=0.3), mv("n10", [44, 21], after=True), ps("b1", [44.6, 21.6], delay=1.0)),
   S("Abschluss: Punkt", "Spieler zehn nimmt den Ball mit und schießt flach ins linke Eck. Das gibt einen Punkt für Team Neon. Danach eröffnet der Torwart oben, und Team Rot baut auf.",
     dr("n10", "b1", [45, 14]), ps("b1", [45, 4.7], after=True), mv("r2", [40, 19], delay=0.2), mv("r3", [53, 22], delay=0.2),
     mv("n8", [66, 16], delay=0.2), mv("r7", [61, 20], delay=0.4))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Platz schaffen für den Mitspieler.", "Platz schaffen in der Mitte",
    "Spieler fünf geht breit und bekommt den Ball vom Torwart. Spieler zehn läuft nach außen und zieht seinen Gegner mit. In die Lücke kommt Spieler sechs, dreht auf und spielt sofort nach vorn.",
    sp(), [B("b1", 50.6, 54.1)] + ERSATZ,
    [S("Breit gehen, wegziehen", "Spieler fünf geht ganz nach außen, und der Torwart spielt ihn an. Gleichzeitig läuft Spieler zehn nach links weg. Spieler zwei geht mit, in der Mitte ist jetzt Platz.",
       mv("n5", [27, 50]), ps("b1", [27.6, 50.6], delay=0.4), mv("n10", [27, 25], delay=0.3), mv("r2", [35.5, 22.5], delay=0.6), mv("r9", [41, 46], delay=0.5)),
     S("Spieler sechs kommt in die Lücke", "Spieler sechs sieht das und läuft in den freien Raum. Er schaut zum Ball, und Spieler fünf spielt ihn flach an.",
       mv("n6", [42, 33]), bl("n6", [27, 50], delay=0.7), ps("b1", [42.6, 33.6], after=True)),
     S("Aufdrehen und nach vorn", "Jetzt erst dreht er auf, der Blick geht nach vorn. Rechts startet Spieler acht hinter die Kette, und der Ball kommt in seinen Lauf.",
       bl("n6", [66.6, 19.6], von=[27, 50], dauer=1.3), drehen("n6", [66.6, 19.6], delay=0.4), mv("n8", [66, 19], delay=0.8), ps("b1", [66.6, 19.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Außen annehmen, abspielen und hinterlaufen.", "Außen frei, hinterlaufen",
    "Ist außen Platz, bietet sich Spieler vier dort an. Nach seinem Pass bleibt er nicht stehen, er läuft außen an Spieler acht vorbei. So bekommt er den Ball an der Grundlinie wieder und kann flach in die Mitte flanken.",
    sp(POS2), [B("b1", 71.6, 47.1)] + ERSATZ,
    [S("Außen annehmen, steil spielen", "Spieler vier hat rechts außen Platz und den Ball. Er spielt steil zu Spieler acht und läuft sofort hinterher.",
       ps("b1", [67.6, 26.6]), mv("n4", [73, 33], delay=0.3)),
     S("Außen vorbei", "Spieler sieben rückt auf Spieler acht. Dahinter ist die Bahn frei. Spieler vier läuft außen vorbei und bekommt den Ball in den Lauf. In der Mitte starten Spieler zehn und Spieler sechs.",
       mv("r7", [64, 21]), mv("n4", [73, 15]), ps("b1", [73.6, 15.6], delay=0.5), mv("n10", [44, 12], delay=0.6), mv("n6", [54, 20], delay=0.6)),
     S("Flanke und Abschluss: Punkt", "Kurz hochschauen, wer ist frei? Die Flanke kommt flach vor das Tor, Spieler zehn hält den Fuß hin, und das gibt einen Punkt für Team Neon.",
       bl("n4", [56, 14]), ps("b1", [44.6, 12.6], after=True), ps("b1", [45, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
