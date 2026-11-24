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
        "r21": (49, 50.5), "r18": (54, 39), "r17": (56, 27), "r16": (60, 15), "r19": (36, 32.5), "r20": (33, 44)}
NEON3 = dict(GROSS, n9=(72, 31))


FREI, GASSE, WARN = 7.0, 4.5, []  # Mindestabstand des Passempfängers zum nächsten Gegner (Einheiten, etwa 8 m)


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
    def gasse(s, von, nach, was, zu=False):
        # Regel (Inhaber, 24.11.2026): Jeder Pass geht durch eine Lücke. Kein Gegner steht beim Abspiel näher als GASSE an der
        # Passbahn (sonst fängt er den Ball ab). Anspielstationen, die absichtlich zugestellt sind, tragen zu=True.
        if zu:
            return
        ax, ay = von; bx, by = nach
        for k2, (px, py) in s.p.items():
            if k2[0] != "r":
                continue
            dx, dy = bx - ax, by - ay
            t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / ((dx * dx + dy * dy) or 1)))
            d = ((ax + t * dx - px) ** 2 + (ay + t * dy - py) ** 2) ** 0.5
            if d < GASSE and 0.05 < t < 0.97:
                WARN.append(f"{was} {s.ball}->{nach}: Gegner {k2} steht {d:.1f} neben der Passbahn (mindestens {GASSE})")
    def opts(s, *ziele, delay=0.0, zu=()):
        for z in ziele:
            s.gasse(s.p[s.ball], s.p[z], "Anspielstation", zu=z in zu)
        return [opt(s.ball, list(s.p[z]), **({"after": True} if i else ({"delay": delay} if delay else {}))) for i, z in enumerate(ziele)]
    def pas(s, an, **k):
        # Regel (Inhaber, 24.11.2026): Wer angespielt wird, hat sich vorher vom Gegenspieler gelöst. Nie in einen Spieler passen,
        # der direkt am Gegner steht. Geprüft wird der Abstand zum nächsten Gegner im Moment des Passes (mindestens FREI).
        gegner = [(k2, v) for k2, v in s.p.items() if k2[0] == "r"]
        if an[0] in "nk" and gegner:
            d, wer = min((((v[0] - s.p[an][0]) ** 2 + (v[1] - s.p[an][1]) ** 2) ** 0.5, k2) for k2, v in gegner)
            if d < FREI:
                WARN.append(f"Pass zu {an}: nur {d:.1f} vom Gegner {wer} entfernt (mindestens {FREI})")
        s.abseits(an)
        if s.ball in s.p:
            s.gasse(s.p[s.ball], s.p[an], "Pass")
        s.ball = an
        return ps("b1", f(s.p[an]), **k)
    def abseits(s, an, lauf=None):
        # Regel (Inhaber, 24.11.2026): Im Moment des Passes steht niemand von Team Neon im Abseits. Team Neon greift nach rechts an
        # (Mittellinie MX). Abseits = in der gegnerischen Hälfte, näher am Tor als der Ball und als der vorletzte Gegner (Torwart zählt).
        rot = sorted((v[0] for k2, v in s.p.items() if k2[0] == "r" or k2 == "k2"), reverse=True)
        if len(rot) < 2 or s.ball not in s.p:
            return
        linie = max(rot[1], s.p[s.ball][0], MX)
        for k2, v in s.p.items():
            x = lauf[0] if (lauf and k2 == an) else v[0]
            if k2[0] == "n" and x > linie + 0.3:
                WARN.append(f"Abseits beim Pass zu {an}: {k2} steht bei x {x:.1f}, Abseitslinie {linie:.1f}")
    def steil(s, an, ziel, **k):
        # Steilpass in den Lauf: Beim Abspiel steht der Läufer noch auf Höhe (Abseitsprüfung mit seinem Startpunkt),
        # Lauf und Pass starten gemeinsam, der Ball kommt dort an, wo der Läufer hinläuft.
        s.abseits(an, lauf=s.p[an])
        s.gasse(s.p[s.ball], tuple(ziel), "Steilpass")
        s.ball = an
        s.p[an] = tuple(ziel)
        return [mv(an, list(ziel), **k), ps("b1", f(ziel), **k)]
    def dribbel(s, wer, ziel, **k):
        s.p[wer] = tuple(ziel)
        return dr(wer, "b1", list(ziel), **k)
    def spieler(s):
        return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in s.p.items()] + [T]


# ---------- Kapitel 1: Grundordnung, Feld groß machen, Aufbau ohne Gegner ----------
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 4-3-3", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Vier-drei-drei. Hinten die Viererkette, also zwei Innenverteidiger und außen die beiden Außenverteidiger. Davor der Sechser, neben ihm die zwei Achter. Und ganz vorn der Stürmer mit seinen zwei Flügelspielern.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Das Feld groß machen", "Sobald der Torwart den Ball hat, machen wir das Feld groß. Die Innenverteidiger gehen raus, bis an die Ecken vom Strafraum. Die Außenverteidiger schieben hoch an die Linie. Vorn bleiben die Flügel schön breit, und der Stürmer drückt die Abwehr nach hinten. So hat der Gegner richtig viel Platz zu verteidigen.",
            *L.schieb(GROSS)))
s3 = L.opts("n5", "n6", "n4")
s3.append(L.pas("n4", after=True))
s3 += L.schieb({"n5": (22, 19), "n6": (29, 32), "n2": (45, 50), "n8": (42, 40), "n10": (46, 24), "n3": (40, 9), "n11": (66, 10), "n9": (72, 33)}, delay=2.0)
k1.append(S("Drei Möglichkeiten für den Torwart", "Jetzt schau auf den Torwart. Er hat drei Möglichkeiten: die beiden Innenverteidiger oder den Sechser in der Mitte. Er spielt nach rechts. Und mit dem Ball schiebt die ganze Mannschaft ein Stück rüber. Auch die, die weit weg sind.", *s3))
s4 = L.opts("n2", "n8", "n6")
s4.append(L.pas("n2", after=True))
s4 += L.schieb({"n8": (52, 42), "n7": (76, 50), "n6": (34, 38), "n4": (26, 46), "n5": (24, 25), "n10": (50, 29), "n9": (74, 36), "n3": (42, 13), "n11": (66, 15)}, delay=2.0)
k1.append(S("Der Innenverteidiger wählt außen", "Auch der Innenverteidiger hat wieder Optionen. Außen, schräg innen den Achter, oder den Sechser. Außen ist am meisten Platz, also geht der Ball dahin. Und jetzt pass auf: Einer kommt, einer geht. Der Achter kommt schräg vor den Ball. Dafür geht der Flügelspieler in die Tiefe. Der Sechser sichert hinten ab.", *s4))
s5 = L.opts("n7", "n8", "n6", "n4")
s5 += [bl("n8", f(L.p["n2"]), after=True), L.pas("n8", after=True)]
s5 += L.schieb({"n7": (82, 48), "n9": (78, 34), "n10": (57, 30), "n11": (70, 17), "n6": (40, 38)}, delay=3.0)
k1.append(S("Vier Wege vom Außenverteidiger", "Der Außenverteidiger hat jetzt vier Wege. Die Linie runter, schräg in den Achter, oder zurück zum Sechser oder zum Innenverteidiger. Der Achter steht offen und schaut zum Ball. Also kriegt er ihn. Und der Flügel? Der ist schon unterwegs.", *s5))
von = f(L.p["n2"])
s6 = [bl("n8", list(L.p["n7"]), von=von, dauer=1.3), drehen("n8", list(L.p["n7"]), delay=0.4)]
s6 += L.opts("n7", "n9", "n10", delay=1.5)
s6.append(L.pas("n7", after=True))
s6 += L.schieb({"n9": (82, 33), "n10": (66, 30), "n11": (78, 19), "n2": (54, 50), "n6": (46, 36)}, delay=3.2)
k1.append(S("Aufdrehen, dann entscheiden", "Erst nach der Annahme dreht der Achter auf. Vor ihm wieder drei Möglichkeiten: der Flügel in der Tiefe, der Stürmer oder der zweite Achter. Der Flügel ist frei, also ab in seinen Lauf. Und die anderen? Die rücken nach und gehen in den Strafraum.", *s6))

# ---------- Kapitel 2: gegen zwei Stürmer (Gegner im 4-4-2) ----------
L2 = Lage(GROSS, ROT, ball="k1")
k2 = []
a = L2.schieb({"r19": (25, 17), "r20": (25, 38), "r16": (46, 9), "r17": (44, 21), "r18": (44, 34), "r21": (46, 46),
               "r13": (70, 9), "r14": (66, 21), "r15": (66, 34), "r12": (70, 46)})
a += L2.schieb({"n6": (19, 27.5), "n5": (16, 9), "n4": (16, 46), "n3": (48, 5), "n2": (48, 50), "n10": (56, 14),
                "n8": (34, 32), "n9": (68, 27.5), "n11": (67, 5), "n7": (67, 50)}, delay=0.3)
k2.append(S("Zwei Stürmer laufen an", "Jetzt wird's ernst. Zwei Stürmer laufen an, und der Gegner rückt mit allen hoch. Unser Sechser lässt sich zwischen die Innenverteidiger fallen, und die gehen noch breiter. Hinten sind wir jetzt zu dritt plus Torwart, gegen zwei. Und auch hier: Einer kommt, einer geht. Der Sechser kommt nach hinten, also rückt ein Achter in seinen Raum. Der andere Achter sucht sich die Lücke zwischen den Linien.", *a))
b2 = L2.opts("n5", "n6", "n4")
b2.append(L2.pas("n6", after=True))
b2 += L2.schieb({"r19": (24, 30), "r20": (25, 38)}, delay=2.0)
k2.append(S("Wer ist frei?", "Der Torwart hat drei Anspielstationen. Er spielt den Sechser an. Und sofort laufen die Stürmer auf ihn zu. Genau das wollen wir, denn jetzt ist außen einer frei.", *b2))
c2 = L2.opts("n5", "n4", "n8", zu=("n8",))
c2.append(L2.pas("n5", after=True))
c2 += L2.schieb({"r16": (42, 8), "r17": (44, 24), "r18": (46, 34), "r21": (48, 42), "r13": (68, 4), "r14": (64, 18),
                 "r15": (64, 30), "r12": (68, 42), "n3": (52, 4), "n10": (54, 17), "n9": (66, 24), "n11": (67, 7),
                 "n8": (40, 33), "n2": (52, 47), "n6": (22, 26)}, delay=2.0)
k2.append(S("Der freie Mann", "Der Sechser schaut kurz hoch. Beide Innenverteidiger sind frei, den Achter verdeckt der Stürmer, der ihn anläuft. Links ist am meisten Platz, also geht der Ball dahin. Der Gegner verschiebt, und wir schieben mit. Der Außenverteidiger bleibt breit, der Achter steht in der Lücke.", *c2))
d2 = [L2.dribbel("n5", (30, 10))]
d2 += L2.schieb({"r16": (36, 6)}, delay=0.6)
d2 += L2.opts("n3", "n10", "n9", delay=1.6, zu=("n3",))
d2 += L2.schieb({"n9": (62, 21), "r14": (69, 24), "n11": (67, 11)}, delay=2.4)
k2.append(S("Andribbeln und locken", "Der Innenverteidiger hat Platz. Also dribbelt er an, so lange, bis einer kommt. Der Gegner kommt von außen und macht den Weg zum Außenverteidiger zu. Dafür ist innen jetzt was frei: der Achter und der Stürmer. Der Stürmer kommt entgegen, und der Flügel geht an die letzte Linie. Bereit für den Lauf in die Tiefe.", *d2))
e2 = [L2.pas("n9")]
e2 += L2.schieb({"n10": (62, 12)}, delay=0.2)
e2.append(L2.pas("n10", after=True))
e2 += L2.schieb({"r17": (52, 18), "r16": (46, 10)}, delay=1.4)
k2.append(S("Der dritte Mann", "Er nimmt den Stürmer. Der lässt den Ball direkt prallen, auf den Achter, der in seinem Rücken mitläuft. Das nennt man den dritten Mann. Er kriegt den Ball und hat den Blick schon nach vorn.", *e2))
g2 = L2.opts("n11", "n3", "n9")
g2 += L2.steil("n11", (84, 12), delay=1.6)
g2 += L2.schieb({"n3": (64, 4), "n9": (78, 24), "n7": (80, 46)}, delay=1.6)
g2 += L2.schieb({"r13": (82, 12), "r14": (76, 20), "r15": (74, 32)}, delay=1.8)
k2.append(S("Hinter die Kette", "Jetzt geht alles nach vorn. Der Achter hat den Flügel, den Außenverteidiger und den Stürmer. Der Flügel startet genau mit dem Pass, so steht er nicht im Abseits. Und der Ball kommt genau in seinen Lauf. Ein paar Pässe, und das Pressing ist überspielt.", *g2))

# ---------- Kapitel 3: verschieben und Seitenwechsel über den Torwart ----------
L3 = Lage(NEON3, ROT3, ball="n2")
k3 = []
a = L3.schieb({"r21": (44, 50.5), "r18": (50, 41), "r20": (28, 38), "r17": (52, 31), "r12": (74, 50), "r16": (58, 20)})
a += L3.schieb({"n7": (62, 47), "n8": (48, 43), "n4": (22, 44), "n6": (30, 34), "n10": (46, 26)}, delay=0.3)
a += L3.opts("n7", "n8", "n4", delay=1.8, zu=("n7", "n8"))
k3.append(S("Der Gegner schiebt zum Ball", "Neue Situation. Unser rechter Außenverteidiger hat den Ball, und der Gegner schiebt mit allen rüber. Wir bieten uns kurz an, aber Flügel und Achter sind zugestellt. Frei ist nur der Weg zurück. Auf der anderen Seite bleiben unser Außenverteidiger und der Flügel trotzdem breit. Da ist jetzt der Platz.", *a))
b3 = [L3.pas("n4"), L3.pas("k1", after=True)]
b3 += L3.schieb({"r20": (22, 38), "r19": (20, 32), "r21": (40, 46), "n6": (26, 27.5), "n5": (17, 10), "n2": (44, 50)}, delay=0.6)
k3.append(S("Zurück über den Torwart", "Also kein Pass in die enge Seite. Der Ball geht zurück zum Innenverteidiger, und weiter zum Torwart. Die Stürmer laufen hinterher, und unser Sechser stellt sich mittig hin. Das ist kein Rückschritt. So verlagern wir das Spiel.", *b3))
c3 = L3.opts("n5", "n6")
c3 += [L3.pas("n5", after=True), L3.pas("n3", after=True)]
c3 += L3.schieb({"r16": (56, 7), "r17": (54, 20), "r18": (54, 32), "r21": (54, 44), "r13": (78, 10), "r14": (78, 21),
                 "r15": (78, 32), "r12": (78, 44), "r19": (24, 22), "r20": (28, 36)}, delay=2.4)
c3 += L3.schieb({"n10": (50, 14), "n11": (70, 6), "n9": (72, 24), "n8": (50, 34), "n7": (68, 46)}, delay=2.6)
k3.append(S("Seitenwechsel", "Der Torwart spielt auf den linken Innenverteidiger, und der direkt weiter auf den Außenverteidiger. Jetzt muss der Gegner quer übers ganze Feld schieben. Und er kommt zu spät. Unser Außenverteidiger hat Zeit und Platz.", *c3))
d3 = L3.opts("n11", "n10", "n9", zu=("n11",))
d3.append(L3.pas("n10", after=True))
d3 += L3.schieb({"n11": (77, 6), "n9": (77, 22), "n3": (54, 6), "n8": (58, 38), "n6": (40, 24), "n2": (52, 46), "n4": (28, 40)}, delay=1.9)
k3.append(S("Auf der freien Seite", "Die Linie runter ist zu. Aber innen ist der Achter frei, und der Stürmer bietet sich an. Er spielt den Achter an, der ihm entgegenkommt. Einer kommt, einer geht: Dafür geht der Flügel an die letzte Linie. Und die ganze Mannschaft schiebt auf die neue Seite.", *d3))
e3 = L3.steil("n11", (88, 16))
e3 += L3.schieb({"r13": (84, 12), "r14": (82, 20)}, delay=0.6)
k3.append(S("Angriff, wo der Gegner nicht ist", "Mit dem Pass startet der Flügel, also kein Abseits. Der Achter steckt durch, genau in die Lücke zwischen zwei Verteidigern. Und so greifen wir dort an, wo der Gegner gerade nicht ist.", *e3))

# ---------- Kapitel 4: Muster: innen-außen, eine Reihe überspielen, klatschen lassen, verlagern ----------
# Gegner im 4-4-2-Mittelfeldpressing (Stürmer an der Mittellinie unserer Hälfte, Mittelfeldreihe, Abwehrreihe)
NEON4 = {"k1": (10.5, 27.5), "n5": (22, 15), "n4": (22, 40), "n6": (32, 27.5), "n3": (44, 5), "n2": (44, 50),
         "n10": (62, 17), "n8": (62, 40), "n11": (68, 6), "n7": (68, 49), "n9": (68, 27.5)}
ROT4 = {"k2": (88, 27.5), "r13": (74, 10), "r14": (74, 22), "r15": (74, 34), "r12": (74, 46),
        "r16": (54, 9), "r17": (54, 21), "r18": (54, 33), "r21": (54, 46), "r19": (38, 20), "r20": (38, 35)}
L4 = Lage(NEON4, ROT4, ball="n4")
k4 = []
a = L4.opts("n2", "n6", "n8")
a.append(L4.pas("n6", after=True))
a += L4.schieb({"r20": (36, 23), "r19": (34, 14), "r18": (48, 30), "r21": (50, 40), "r17": (50, 21)}, delay=2.0)
k4.append(S("Erst innen", "Zum Schluss zwei Muster, die du immer wieder siehst. Der Innenverteidiger hat drei Möglichkeiten. Er spielt zuerst innen, auf den Sechser. Und der Gegner? Der will ihn stellen und zieht sich zur Mitte zusammen.", *a))
b4 = L4.opts("n2", "n4", "n8", zu=("n8",))
b4.append(L4.pas("n2", after=True))
b4 += L4.schieb({"r21": (50, 51), "r12": (70, 48), "n7": (72, 50)}, delay=1.9)
k4.append(S("Dann außen", "Genau dadurch wird's außen frei. Innen ist jetzt zu. Also spielt der Sechser sofort raus auf den Außenverteidiger. Erst innen, dann außen. Der Ball ist einfach schneller als der Gegner.", *b4))
c4 = L4.schieb({"n9": (66, 31), "n8": (66, 42)})
c4 += L4.opts("n7", "n9", "n6", delay=1.2, zu=("n7",))
c4.append(L4.pas("n9", after=True))
c4 += L4.schieb({"r15": (70, 33), "r18": (54, 31)}, delay=2.8)
k4.append(S("Eine Reihe überspielen", "Jetzt läuft der Gegner raus zum Außenverteidiger und macht die Linie zu. Also umgekehrt: außen, dann innen. Der Stürmer kommt entgegen, und der Ball geht flach durch die Mittelfeldreihe, direkt in seinen Fuß. Eine ganze Reihe überspielt.", *c4))
d4 = L4.schieb({"n10": (61, 25)})
d4.append(L4.pas("n10", delay=0.6))
d4 += L4.schieb({"r17": (56, 24), "r18": (56, 30), "r14": (70, 25), "r13": (72, 15), "r16": (52, 14)}, delay=1.3)
d4 += L4.schieb({"n11": (71, 5), "n3": (58, 4)}, delay=1.3)
k4.append(S("Klatschen lassen", "Der Stürmer lässt klatschen, direkt auf den Achter, der sich daneben freigelaufen hat. Der steht mit Blick nach vorn. Und der Gegner zieht sich jetzt komplett in die Mitte.", *d4))
e4 = L4.opts("n11", "n3", "n9")
e4.append(L4.pas("n11", after=True))
e4.append(L4.dribbel("n11", (84, 8), after=True))
e4 += L4.schieb({"n9": (82, 22), "n7": (82, 40), "n8": (74, 44)}, delay=1.6)
e4 += L4.schieb({"r13": (82, 12), "r14": (80, 22)}, delay=2.2)
k4.append(S("Und verlagern", "Auf der anderen Seite ist alles frei. Der Achter verlagert sofort auf den Flügel. Der nimmt den Ball mit und geht direkt in die Tiefe. Überspielen, klatschen lassen, verlagern. So kommen wir dahin, wo der Gegner nicht ist.", *e4))

u = {"title": "Aufbau im 4-3-3 über den Torwart", "code": "TA-001", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 4-3-3 von hinten auf? Zuerst siehst du, wer wo steht, wie die Mannschaft das Feld groß macht und mit jedem Pass verschiebt. Bei jedem Ballbesitz gibt es mehrere Anspielstationen, und du siehst, warum welche gewählt wird. Dann presst ein Gegner, danach geht es um den Seitenwechsel über den Torwart. Zum Schluss zwei Muster: innen-außen und eine Reihe überspielen, klatschen lassen, verlagern.",
 "organisation": ["Grundordnung: Torwart, Viererkette, ein Sechser, zwei Achter, vorn ein Stürmer und zwei Flügelspieler.",
  "Hinten: Beim Aufbau gehen die Innenverteidiger breit bis an die Ecken vom Strafraum, die Außenverteidiger schieben hoch, der Torwart spielt mit.",
  "Mittelfeld: Der Sechser bietet sich zentral an oder lässt sich zwischen die Innenverteidiger fallen, die Achter stehen in den Halbräumen und zwischen den Linien.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball. Einer kommt, einer geht: Kommt ein Spieler zum Ball, läuft ein anderer in die Tiefe."],
 "organisation_show": ORG,
 "coaching_points": ["Feld groß machen: breit und tief stehen", "Einer kommt, einer geht", "Immer zwei Anspielstationen anbieten", "Eine Seite zu? Über den Torwart verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Vier-drei-drei über den Torwart. Heute mal keine Übung, sondern das System dahinter. Wer steht wo? Wie bewegen sich alle mit dem Ball? Und welche Wege gibt's nach vorn? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Gegen zwei Stürmer",
    "Jetzt presst ein Gegner im 4-4-2 mit zwei Stürmern. Der Sechser lässt sich zwischen die Innenverteidiger fallen, hinten ist dann immer einer frei. Wer am Ball ist, lockt einen Gegner an und spielt dann den frei gewordenen Mitspieler an. Über den dritten Mann kommen wir mit Blick nach vorn durch das Pressing.",
    Lage(GROSS, ROT).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Verschieben und Seitenwechsel.", "Verlagern über den Torwart",
    "Der Gegner schiebt mit allen auf unsere Ballseite. Dort ist es eng, auf der anderen Seite ist Platz. Wir spielen zurück über den Innenverteidiger zum Torwart und verlagern auf die freie Seite. Danach schiebt die ganze Mannschaft mit.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 40.6, 50.6)] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Muster zum Herausspielen.", "Innen, außen, verlagern",
    "Zwei Muster, die immer wieder funktionieren. Erst innen, dann außen: Der Pass nach innen zieht den Gegner zusammen, dann ist außen Platz. Und: eine Reihe überspielen, klatschen lassen, verlagern. Dabei hat sich jeder, der angespielt wird, vorher vom Gegenspieler gelöst.",
    Lage(NEON4, ROT4).spieler(), [B("b1", 22.6, 40.6)] + ERSATZ, k4)]}
for w in WARN: print("FREI:", w)
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
