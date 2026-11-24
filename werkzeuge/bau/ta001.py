import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# TA-001: Taktik-Erklärung (kind "Taktik", Inhaber 24.11.2026). Aufbau im 4-3-3 von hinten über den Torwart.
# Für Trainer U12 bis U17, etwa fünf Minuten, drei Kapitel: 1 Grundordnung und Aufbau ohne Gegner, 2 gegen zwei anlaufende
# Stürmer (4-4-2: Sechser kippt ab, freier Mann, locken, dritter Mann), 3 Verschieben und Seitenwechsel über den Torwart.
# LEBENDIG (Inhaber, 24.11.2026, zweite Fassung): Bei jedem Ballweg verschieben alle mit, Neon und Rot. Vor jedem Pass zeigt
# opt() zwei bis vier Anspielstationen (dünne Pfeile), dann kommt die Wahl mit Begründung. Muster: Dreieck auf der Seite,
# Sechser kippt ab, freier Mann, andribbeln und locken, dritter Mann, Seitenwechsel über den Torwart.
# EINER KOMMT, EINER GEHT (Inhaber, 24.11.2026): Kommt ein Spieler zum Ball (Achter, Sechser, Stürmer), geht im selben Moment
# ein anderer weg (Flügel in die Tiefe, Achter in den Sechserraum). In jedem Kapitel mindestens einmal gezeigt und gesagt.
# Großfeld quer wie UE-319 (massstab "gross"): Team Neon baut links auf und spielt nach rechts. Von Team Neon aus gesehen ist
# oben die linke Seite (Linksverteidiger 3, Linksaußen 11), unten die rechte (Rechtsverteidiger 2, Rechtsaußen 7).
# Nummern wie im klassischen 4-3-3: 2 RV, 3 LV, 4 und 5 Innenverteidiger, 6 Sechser, 8 und 10 Achter, 7 RA, 9 Stürmer, 11 LA.
# Team Rot (4-4-2) neu nummeriert 12-21, beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Ein Trainer.
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]
T = P("T", "c", 16, 55.3, "T")
ERSATZ = [B("s1", 19.5, 55.8), B("s2", 22, 55.8)]
f = lambda p: [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]  # Ball am Fuß

GRUND = {"k1": (10.5, 27.5), "n5": (24, 21), "n4": (24, 34), "n3": (30, 8), "n2": (30, 47), "n6": (35, 27.5),
         "n10": (46, 17), "n8": (46, 38), "n11": (60, 7), "n7": (60, 48), "n9": (66, 27.5)}
GROSS = {"k1": (10.5, 27.5), "n5": (19, 13.5), "n4": (19, 41.5), "n3": (40, 5), "n2": (40, 50), "n6": (30, 27.5),
         "n10": (44, 18), "n8": (44, 37), "n11": (68, 5), "n7": (68, 50), "n9": (72, 27.5)}
ROT = {"k2": (88, 27.5), "r12": (80, 46), "r15": (80, 34), "r14": (80, 21), "r13": (80, 9),
       "r21": (54, 47), "r18": (54, 34), "r17": (54, 21), "r16": (54, 8), "r19": (27, 15), "r20": (27, 40)}
ROT3 = {"k2": (88, 27.5), "r12": (80, 49), "r15": (80, 37), "r14": (80, 25.5), "r13": (83, 14),
        "r21": (49, 50.5), "r18": (54, 39), "r17": (56, 27), "r16": (60, 15), "r19": (26, 39.5), "r20": (33, 44)}
NEON3 = dict(GROSS, n9=(72, 31))


class Lage:
    """Merkt sich, wo alle stehen und wer den Ball hat. Erzeugt die Laufwege fürs Verschieben, die Anspielstationen und Pässe."""
    def __init__(s, *pos, ball=None):
        s.p = {}
        for d in pos: s.p.update({k: tuple(v) for k, v in d.items()})
        s.ball = ball
    def schieb(s, neu, delay=0.0):
        out = []
        for k, v in neu.items():
            if tuple(v) != s.p[k]:
                out.append(mv(k, list(v), delay=delay) if delay else mv(k, list(v)))
                s.p[k] = tuple(v)
        return out
    def opts(s, *ziele, delay=0.0):
        return [opt(s.ball, list(s.p[z]), **({"after": True} if i else ({"delay": delay} if delay else {}))) for i, z in enumerate(ziele)]
    def pas(s, an, **k):
        s.ball = an
        return ps("b1", f(s.p[an]), **k)
    def dribbel(s, wer, ziel, **k):
        s.p[wer] = tuple(ziel)
        return dr(wer, "b1", list(ziel), **k)
    def spieler(s):
        return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in s.p.items()] + [T]


# ---------- Kapitel 1: Grundordnung, Feld groß machen, Aufbau ohne Gegner ----------
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 4-3-3", "Der Trainer spielt dem Torwart den Ball. Wir stehen im Vier-drei-drei. Hinten die Viererkette, also zwei Innenverteidiger und außen die zwei Außenverteidiger. Davor der Sechser, daneben die zwei Achter. Vorn der Stürmer mit den beiden Flügelspielern.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Das Feld groß machen", "Hat der Torwart den Ball, machen wir das Feld groß. Die Innenverteidiger gehen breit bis an die Ecken vom Strafraum. Die Außenverteidiger schieben hoch an die Seitenlinie. Vorn bleiben die Flügel ganz breit, und der Stürmer drückt die Abwehr nach hinten.",
            *L.schieb(GROSS)))
s3 = L.opts("n5", "n6", "n4")
s3.append(L.pas("n4", after=True))
s3 += L.schieb({"n5": (22, 19), "n6": (29, 32), "n2": (45, 50), "n8": (42, 40), "n10": (46, 24), "n3": (40, 9), "n11": (66, 10), "n9": (72, 33)}, delay=2.0)
k1.append(S("Drei Möglichkeiten für den Torwart", "Der Torwart hat drei Möglichkeiten: beide Innenverteidiger und den Sechser. Er spielt nach rechts. Und mit dem Ball schiebt die ganze Mannschaft ein Stück auf diese Seite, auch die Spieler weit weg vom Ball.", *s3))
s4 = L.opts("n2", "n8", "n6")
s4.append(L.pas("n2", after=True))
s4 += L.schieb({"n8": (52, 42), "n7": (76, 50), "n6": (34, 38), "n4": (26, 46), "n5": (24, 25), "n10": (50, 29), "n9": (74, 36), "n3": (42, 13), "n11": (66, 15)}, delay=2.0)
k1.append(S("Der Innenverteidiger wählt außen", "Auch der Innenverteidiger hat mehrere Anspielstationen: außen, schräg innen den Achter oder den Sechser. Er wählt außen, da ist am meisten Platz. Jetzt gilt: Einer kommt, einer geht. Der Achter kommt schräg vor den Ball, dafür geht der Flügelspieler nach vorn in die Tiefe. Der Sechser sichert dahinter ab.", *s4))
s5 = L.opts("n7", "n8", "n6", "n4")
s5 += [bl("n8", f(L.p["n2"]), after=True), L.pas("n8", after=True)]
s5 += L.schieb({"n7": (82, 48), "n9": (78, 34), "n10": (57, 30), "n11": (70, 17), "n6": (40, 38)}, delay=3.0)
k1.append(S("Vier Wege vom Außenverteidiger", "Jetzt hat der Außenverteidiger vier Wege. Die Linie entlang zum Flügel, schräg in den Achter, zurück zum Sechser oder zum Innenverteidiger. Der Achter steht offen und schaut zum Ball, also bekommt er ihn. Der Flügelspieler ist schon unterwegs in die Tiefe.", *s5))
von = f(L.p["n2"])
s6 = [bl("n8", list(L.p["n7"]), von=von, dauer=1.3), drehen("n8", list(L.p["n7"]), delay=0.4)]
s6 += L.opts("n7", "n9", "n10", delay=1.5)
s6.append(L.pas("n7", after=True))
s6 += L.schieb({"n9": (82, 33), "n10": (66, 30), "n11": (78, 19), "n2": (54, 50), "n6": (46, 36)}, delay=3.2)
k1.append(S("Aufdrehen, dann entscheiden", "Erst nach der Annahme dreht der Achter auf. Vor ihm hat er wieder drei Möglichkeiten: den Flügel in der Tiefe, den Stürmer oder den zweiten Achter. Der Flügel ist frei, also geht der Ball in seinen Lauf. Die anderen rücken nach und laufen in den Strafraum.", *s6))

# ---------- Kapitel 2: gegen zwei Stürmer (Gegner im 4-4-2) ----------
L2 = Lage(GROSS, ROT, ball="k1")
k2 = []
a = L2.schieb({"r19": (25, 17), "r20": (25, 38), "r16": (46, 9), "r17": (44, 21), "r18": (44, 34), "r21": (46, 46),
               "r13": (70, 9), "r14": (66, 21), "r15": (66, 34), "r12": (70, 46)})
a += L2.schieb({"n6": (19, 27.5), "n5": (16, 9), "n4": (16, 46), "n3": (48, 5), "n2": (48, 50), "n10": (56, 14),
                "n8": (34, 32), "n9": (76, 27.5), "n11": (74, 5), "n7": (74, 50)}, delay=0.3)
k2.append(S("Zwei Stürmer laufen an", "Jetzt laufen zwei Stürmer an, und der Gegner rückt mit allen hoch. Unser Sechser lässt sich zwischen die Innenverteidiger fallen, die gehen noch breiter. Hinten sind wir drei plus Torwart gegen zwei. Einer kommt, einer geht: Der Sechser kommt nach hinten, dafür rückt ein Achter in seinen Raum. Der andere Achter sucht die Lücke zwischen den Linien.", *a))
b2 = L2.opts("n5", "n6", "n4")
b2.append(L2.pas("n6", after=True))
b2 += L2.schieb({"r19": (22, 24), "r20": (22, 36)}, delay=2.0)
k2.append(S("Wer ist frei?", "Der Torwart hat drei Anspielstationen. Er spielt den Sechser an, und sofort laufen die zwei Stürmer auf ihn zu. Das ist gut für uns, denn jetzt ist außen einer frei.", *b2))
c2 = L2.opts("n5", "n4", "n10")
c2.append(L2.pas("n5", after=True))
c2 += L2.schieb({"r16": (40, 11), "r17": (42, 18), "r18": (44, 30), "r21": (48, 40), "r13": (68, 8), "r14": (64, 18),
                 "r15": (64, 30), "r12": (68, 42), "n3": (52, 4), "n10": (54, 17), "n9": (72, 24), "n11": (76, 7),
                 "n8": (40, 33), "n2": (52, 47), "n6": (22, 26)}, delay=2.0)
k2.append(S("Der freie Mann", "Der Sechser sieht beide Innenverteidiger und den Achter. Links ist frei, also geht der Ball dorthin. Jetzt verschiebt der Gegner auf diese Seite, und wir schieben mit: Der Außenverteidiger bleibt breit, der Achter steht in der Lücke.", *c2))
d2 = [L2.dribbel("n5", (30, 10))]
d2 += L2.schieb({"r16": (36, 12)}, delay=0.6)
d2 += L2.opts("n3", "n10", "n9", delay=1.6)
d2 += L2.schieb({"n9": (62, 21), "r14": (62, 20), "n11": (82, 10)}, delay=2.4)
k2.append(S("Andribbeln und locken", "Der Innenverteidiger hat Platz und dribbelt an, bis ein Gegner kommt. Kommt einer, wird ein anderer frei: außen der Außenverteidiger, innen der Achter, vorn der Stürmer. Der Stürmer kommt entgegen, und der Flügel geht hinter die Kette. Einer kommt, einer geht.", *d2))
e2 = [L2.pas("n9")]
e2 += L2.schieb({"n10": (62, 12)}, delay=0.2)
e2.append(L2.pas("n10", after=True))
e2 += L2.schieb({"r17": (52, 18), "r16": (46, 10)}, delay=1.4)
k2.append(S("Der dritte Mann", "Er wählt den Stürmer. Der lässt den Ball direkt prallen auf den Achter, der in seinem Rücken mitläuft. Das ist der dritte Mann: Er bekommt den Ball schon mit Blick nach vorn.", *e2))
g2 = L2.opts("n11", "n3", "n8")
g2 += L2.schieb({"n11": (86, 12), "n3": (64, 4), "n8": (70, 38), "n9": (78, 24), "n7": (80, 46)}, delay=0.1)
g2.append(L2.pas("n11", after=True))
g2 += L2.schieb({"r13": (82, 12), "r14": (76, 20), "r15": (74, 32)}, delay=1.8)
k2.append(S("Hinter die Kette", "Jetzt geht alles nach vorn. Der Achter hat den Flügel in der Tiefe, den Außenverteidiger außen und den anderen Achter. Der Flügel ist am schnellsten, also bekommt er den Ball. Mit wenigen Pässen ist das Pressing überspielt.", *g2))

# ---------- Kapitel 3: verschieben und Seitenwechsel über den Torwart ----------
L3 = Lage(NEON3, ROT3, ball="n2")
k3 = []
a = L3.schieb({"r21": (44, 50.5), "r18": (50, 41), "r20": (25, 43), "r17": (52, 31), "r12": (74, 50), "r16": (58, 20)})
a += L3.schieb({"n7": (62, 47), "n8": (48, 43), "n4": (22, 44), "n6": (30, 34), "n10": (46, 26)}, delay=0.3)
a += L3.opts("n7", "n8", "n4", delay=1.8)
k3.append(S("Der Gegner schiebt zum Ball", "Unser rechter Außenverteidiger hat den Ball, und der Gegner schiebt mit allen auf diese Seite. Wir bieten uns kurz an, aber der Flügel und der Achter sind zugestellt. Frei ist nur der Weg zurück. Auf der anderen Seite bleiben unser Außenverteidiger und der Flügelspieler breit.", *a))
b3 = [L3.pas("n4"), L3.pas("k1", after=True)]
b3 += L3.schieb({"r20": (22, 38), "r19": (20, 32), "r21": (40, 46), "n6": (26, 27.5), "n5": (17, 10), "n2": (44, 50)}, delay=0.6)
k3.append(S("Zurück über den Torwart", "Also kein Pass in die enge Seite. Der Ball geht zurück zum Innenverteidiger und weiter zum Torwart. Die zwei Stürmer laufen hinterher, und unser Sechser stellt sich mittig hin. Das ist kein Rückschritt, so verlagern wir das Spiel.", *b3))
c3 = L3.opts("n5", "n6")
c3 += [L3.pas("n5", after=True), L3.pas("n3", after=True)]
c3 += L3.schieb({"r16": (54, 9), "r17": (54, 20), "r18": (54, 32), "r21": (54, 44), "r13": (78, 10), "r14": (78, 21),
                 "r15": (78, 32), "r12": (78, 44), "r19": (24, 22), "r20": (28, 36)}, delay=2.4)
c3 += L3.schieb({"n10": (50, 14), "n11": (70, 6), "n9": (72, 24), "n8": (50, 34), "n7": (68, 46)}, delay=2.6)
k3.append(S("Seitenwechsel", "Der Torwart spielt zum linken Innenverteidiger, und der sofort weiter auf den Außenverteidiger. Der Gegner muss quer über das ganze Feld schieben und kommt zu spät. Unser Außenverteidiger hat Zeit und Platz.", *c3))
d3 = L3.opts("n11", "n10", "n9")
d3.append(L3.pas("n10", after=True))
d3 += L3.schieb({"n11": (80, 8), "n9": (78, 22), "n3": (54, 6), "n8": (58, 38), "n6": (40, 24), "n2": (52, 46), "n4": (28, 40)}, delay=1.9)
k3.append(S("Auf der freien Seite", "Der Außenverteidiger hat drei Wege: die Linie entlang, innen den Achter oder den Stürmer. Er spielt den Achter an, der zum Ball kommt. Einer kommt, einer geht: Dafür startet der Flügelspieler in die Tiefe, und die ganze Mannschaft schiebt auf die neue Seite.", *d3))
e3 = [L3.pas("n11")]
e3 += L3.schieb({"r13": (84, 12), "r14": (80, 18)}, delay=0.6)
k3.append(S("Angriff, wo der Gegner nicht ist", "Der Achter steckt durch auf den Flügel. So greifen wir dort an, wo der Gegner gerade nicht ist.", *e3))

u = {"title": "Aufbau im 4-3-3 über den Torwart", "code": "TA-001", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 4-3-3 von hinten auf? Zuerst siehst du, wer wo steht, wie die Mannschaft das Feld groß macht und mit jedem Pass verschiebt. Bei jedem Ballbesitz gibt es mehrere Anspielstationen, und du siehst, warum welche gewählt wird. Dann presst ein Gegner, und zum Schluss geht es um den Seitenwechsel über den Torwart.",
 "organisation": ["Grundordnung: Torwart, Viererkette, ein Sechser, zwei Achter, vorn ein Stürmer und zwei Flügelspieler.",
  "Hinten: Beim Aufbau gehen die Innenverteidiger breit bis an die Ecken vom Strafraum, die Außenverteidiger schieben hoch, der Torwart spielt mit.",
  "Mittelfeld: Der Sechser bietet sich zentral an oder lässt sich zwischen die Innenverteidiger fallen, die Achter stehen in den Halbräumen und zwischen den Linien.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball. Einer kommt, einer geht: Kommt ein Spieler zum Ball, läuft ein anderer in die Tiefe."],
 "organisation_show": ORG,
 "coaching_points": ["Feld groß machen: breit und tief stehen", "Einer kommt, einer geht", "Immer zwei Anspielstationen anbieten", "Eine Seite zu? Über den Torwart verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Vier-drei-drei über den Torwart. Diesmal keine Übung, sondern das System. Wer steht wo, wie bewegen sich alle mit dem Ball, und welche Wege gibt es nach vorn?",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Gegen zwei Stürmer",
    "Jetzt presst ein Gegner im 4-4-2 mit zwei Stürmern. Der Sechser lässt sich zwischen die Innenverteidiger fallen, hinten ist dann immer einer frei. Wer am Ball ist, lockt einen Gegner an und spielt dann den frei gewordenen Mitspieler an. Über den dritten Mann kommen wir mit Blick nach vorn durch das Pressing.",
    Lage(GROSS, ROT).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Verschieben und Seitenwechsel.", "Verlagern über den Torwart",
    "Der Gegner schiebt mit allen auf unsere Ballseite. Dort ist es eng, auf der anderen Seite ist Platz. Wir spielen zurück über den Innenverteidiger zum Torwart und verlagern auf die freie Seite. Danach schiebt die ganze Mannschaft mit.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 40.6, 50.6)] + ERSATZ, k3)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
