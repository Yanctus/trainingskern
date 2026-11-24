import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 51-P10 (U15-U17, Woche 15): Break Through Pressure to Attack. 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m).
# FELD QUER (Inhaber, 24.11.2026): Das lange Feld liegt quer und füllt die Tafel, Tore links und rechts. Team Neon baut links
# auf und greift nach rechts an. Geplant im Hochformat wie im PDF (x 25-75 Breite, y 5-55 Länge, Angriff nach oben);
# R() legt jede Koordinate quer: unten -> links, oben -> rechts, links -> oben, rechts -> unten. Feld quer: x 9-89, y 4-51.
# Zwei Großfeldtore mit Torwart (nur C- und B-Jugend). PDF blau -> Team Neon (4, 5, 6, 8, 10 wie im PDF),
# pink -> Team Rot, grüne Torhüter -> neutrale Torhüter (k1 links, k2 rechts). Team Rot neu nummeriert, weil die Nummern doppelt sind: 2 -> 2, 6 -> 3, 4 -> 7, 8 -> 9, 10 -> 11. Ein Trainer statt zwei.
# Fassung 1 = PDF Key Coaching Point 1 (Innenverteidiger breit, Zehner zieht weg, Sechser in die Lücke; Annehmen und Aufdrehen
# mit bl(von=...) und drehen()). Fassung 2 = Key Coaching Point 2 (außen annehmen, hinterlaufen, flanken); im PDF/Video zeigt
# das die pinke Mannschaft, hier spielt es Team Neon.
# Sichtkegel: Text/Ton „Recognise space early“, „Identify and use the free player“; im Video nicht eingezeichnet,
# Richtung aus dem Sinn: Spieler vier schaut vor dem Steilpass in den Raum hinter der Kette, vor der Flanke in die Mitte.
# Texte ohne oben/unten/links/rechts, wo es geht (Seite, außen, die andere Seite).
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 25) / 50 * (FY1 - FY0), 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def C(x, y, *a, **k): return h.C(*R(x, y), *a, **k)
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 40, 55.3, "T")  # unten an der Seitenlinie (quer gesetzt)
ERSATZ = [h.B("s1", 43.5, 55.8), h.B("s2", 46, 55.8)]
# Quer stehen die Spieler, die im Hochformat nebeneinander standen, in der Tiefe hintereinander: Positionen dafür leicht
# in der Länge versetzt (3D-Abstand).
POS = {"k1": (50, 53.5), "n5": (29, 48), "n4": (59, 48), "n6": (46.5, 37), "n10": (29, 31.8), "n8": (73, 29.8),
       "k2": (50, 7.5), "r2": (37.5, 26.2), "r3": (55, 31.5), "r7": (64.5, 24.2), "r9": (38, 42.5), "r11": (67.5, 42.5)}
POS2 = {"k1": (50, 53), "n5": (29, 47.2), "n4": (71, 49.2), "n6": (50, 35), "n8": (67, 23.8), "n10": (33, 24.8),
        "k2": (50, 7.5), "r2": (41.5, 19.2), "r3": (58.5, 29.2), "r7": (58.5, 15), "r9": (40, 41.8), "r11": (62.5, 43.8)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
CONES = [h.C(FX0, FY0), h.C(FX1, FY0), h.C(FX0, FY1), h.C(FX1, FY1), h.C(MX, FY0), h.C(MX, FY1)]
# Nur die Länge als Maßlinie (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "40 m", "25 m")[:1]

u = {"title": "Durch den Druck nach vorn", "code": "UE-317", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "25 x 40 m",
 "description": "Fünf gegen fünf plus Torhüter auf einem schmalen, langen Feld. Team Neon baut vom Torwart aus auf, Team Rot läuft früh an. Hinter der Kette von Team Rot ist viel Platz, zur Seite kaum. Wer den Druck überspielt und einen Mitspieler in der Tiefe findet, kommt zum Abschluss.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern mit Mittellinie. Auf jeder Grundlinie steht ein großes Tor.",
  "Verteilen: Team Neon und Team Rot spielen mit je fünf Feldspielern, in jedem Tor steht ein Torwart. Alle Feldspieler stehen zu Beginn in der Hälfte von Team Neon. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart links eröffnet für Team Neon. Team Neon spielt sich durch das Anlaufen und sucht den Pass in die Tiefe. Dann geht es ohne Pause zum Abschluss aufs andere Tor. Erobert Team Rot den Ball, greift es sofort selbst an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach einem Treffer oder wenn der Torwart den Ball hält, eröffnet der Torwart auf der anderen Seite, und das andere Team baut auf."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo ist der Platz hinter der Kette?", "Nach vorn spielen, wenig Kontakte", "Ruhig bleiben, wenn der Gegner anläuft", "Den freien Mann finden und anspielen"],
 "materials": ["2 große Tore", "6 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Durch den Druck nach vorn. Fünf gegen fünf plus Torhüter auf einem schmalen, langen Feld. Team Neon baut hinten auf, Team Rot läuft an, und hinter der Kette wartet der Platz für den Angriff.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 50.6, 54.1)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Torwart eröffnet", "Der Torwart links hat den Ball, Team Neon baut auf. Er spielt flach zu Spieler fünf an die Seite. Spieler neun läuft sofort an.",
     ps("b1", [29.6, 48.6]), mv("r9", [36, 44.5], delay=0.3)),
   S("Quer auf die freie Seite", "Auf dieser Seite wird es eng. Also geht der Ball quer zu Spieler vier, der auf der anderen Seite Zeit hat. Spieler elf kommt zu spät.",
     ps("b1", [59.6, 48.6]), mv("r11", [66, 45.5], delay=0.4), mv("r9", [40, 45], delay=0.4)),
   S("Kopf hoch, steil in die Tiefe", "Spieler vier hebt den Kopf und sieht den Platz hinter der Kette. Vorn löst sich Spieler zehn im Rücken von Spieler zwei. Der Pass kommt flach durch die Mitte, genau in seinen Lauf.",
     bl("n4", [51, 31]), mv("n10", [31, 24], delay=0.3), mv("n10", [44, 21], after=True), ps("b1", [44.6, 21.6], delay=1.0)),
   S("Abschluss: Punkt", "Spieler zehn nimmt den Ball mit und schießt flach ins Eck. Das gibt einen Punkt für Team Neon. Danach eröffnet der Torwart rechts, und Team Rot baut auf.",
     dr("n10", "b1", [45, 14]), ps("b1", [45, 4.7], after=True), mv("r2", [40, 19], delay=0.2), mv("r3", [53, 22], delay=0.2),
     mv("n8", [66, 16], delay=0.2), mv("r7", [61, 20], delay=0.4))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Platz schaffen für den Mitspieler.", "Platz schaffen in der Mitte",
    "Spieler fünf geht breit und bekommt den Ball vom Torwart. Spieler zehn läuft nach außen und zieht seinen Gegner mit. In die Lücke kommt Spieler sechs, dreht auf und spielt sofort nach vorn.",
    sp(), [B("b1", 50.6, 54.1)] + ERSATZ,
    [S("Breit gehen, wegziehen", "Spieler fünf geht ganz nach außen, und der Torwart spielt ihn an. Gleichzeitig läuft Spieler zehn zur Seite weg. Spieler zwei geht mit, in der Mitte ist jetzt Platz.",
       mv("n5", [27, 50]), ps("b1", [27.6, 50.6], delay=0.4), mv("n10", [27, 25], delay=0.3), mv("r2", [35.5, 22.5], delay=0.6), mv("r9", [41, 46], delay=0.5)),
     S("Spieler sechs kommt in die Lücke", "Spieler sechs sieht das und läuft in den freien Raum. Er schaut zum Ball, und Spieler fünf spielt ihn flach an.",
       mv("n6", [42, 33]), bl("n6", [27, 50], delay=0.7), ps("b1", [42.6, 33.6], after=True)),
     S("Aufdrehen und nach vorn", "Jetzt erst dreht er auf, der Blick geht nach vorn. Auf der anderen Seite startet Spieler acht hinter die Kette, und der Ball kommt in seinen Lauf.",
       bl("n6", [66.6, 19.6], von=[27, 50], dauer=1.3), drehen("n6", [66.6, 19.6], delay=0.4), mv("n8", [66, 19], delay=0.8), ps("b1", [66.6, 19.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Außen annehmen, abspielen und hinterlaufen.", "Außen frei, hinterlaufen",
    "Ist außen Platz, bietet sich Spieler vier dort an. Nach seinem Pass bleibt er nicht stehen, er läuft außen an Spieler acht vorbei. So bekommt er den Ball an der Grundlinie wieder und kann flach in die Mitte flanken.",
    sp(POS2), [B("b1", 71.6, 49.8)] + ERSATZ,
    [S("Außen annehmen, steil spielen", "Spieler vier hat außen Platz und den Ball. Er spielt steil zu Spieler acht und läuft sofort hinterher.",
       ps("b1", [67.6, 24.4]), mv("n4", [73, 33], delay=0.3)),
     S("Außen vorbei", "Spieler sieben rückt auf Spieler acht. Dahinter ist die Bahn frei. Spieler vier läuft außen vorbei und bekommt den Ball in den Lauf. In der Mitte starten Spieler zehn und Spieler sechs.",
       mv("r7", [64, 21]), mv("n4", [73, 15]), ps("b1", [73.6, 15.6], delay=0.5), mv("n10", [44, 12], delay=0.6), mv("n6", [54, 20], delay=0.6)),
     S("Flanke und Abschluss: Punkt", "Kurz hochschauen, wer ist frei? Die Flanke kommt flach vor das Tor, Spieler zehn hält den Fuß hin, und das gibt einen Punkt für Team Neon.",
       bl("n4", [56, 14]), ps("b1", [44.6, 12.6], after=True), ps("b1", [45, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
