# Gemeinsame Bauhilfe für Taktik-Erklärungen (kind "Taktik"), aus TA-001 übernommen (Inhaber, 24.11.2026).
# Einbinden:  import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# Enthält: Großfeld quer (LINES, TORE, DIMS, Trainer T, ERSATZ), f() = Ball am Fuß, die Klasse Lage mit allen Prüfungen
# (Empfänger frei, Abseits, Passbahn frei) und fertig(), das die Warnungen ausgibt. Vorbild für den Ablauf: ta001.py.
# Team Neon baut links auf und greift nach rechts an. Von Team Neon aus ist oben die linke Seite, unten die rechte.
import sys
from hilfe import *
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


def fertig():
    """Am Ende des Bauskripts aufrufen: gibt alle Regelverstöße aus (FREI:, ABSEITS:, PASSBAHN:). Ziel: keine Ausgabe."""
    for w in WARN:
        print("TAKTIK:", w)
    return not WARN
