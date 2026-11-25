# Halbes Feld QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py): eine Platzhälfte wie im Fernsehbild.
# Großes Tor rechts (oder links), die Platzbreite von oben nach unten, die Mittellinie am anderen Rand, echte Linien der Hälfte.
#
# Abbildung: Die Hälfte (etwa 50 m tief, 65 m breit) füllt die Tafel und ist deshalb in der Waagerechten gestreckt. Damit Strafraum
# und Tor nicht verzerrt wirken, wächst die Streckung gleichmäßig vom Tor zur Mittellinie (quadratisch, ohne Knick): An der Torlinie
# ist ein Meter in der Tiefe 1,05 Einheiten (1,39-mal die 0,75 Einheiten je Meter der Breite), an der Mittellinie rund
# 2,2 Einheiten. Senkrecht gilt überall derselbe Maßstab (65 m = y 3-52, wie beim Großfeld UE-319).
#
# Benutzung im Bauskript (Koordinaten in Metern planen oder aus dem alten Hochformat umrechnen):
#   import halbfeld as hf
#   F = hf.Halbfeld()                     # 50 x 65 m, Tor rechts bei x 90, Mittellinie links bei x 10, y 3-52
#   F = hf.Halbfeld(tief=35, breit=55)    # kürzeres Feld: steht mittig, gleiche Streckung; tor="links" für Tor links
#   F(d, q) -> [x, y]                     # d = Meter vor der Torlinie (0 = Torlinie, 50 = Mittellinie),
#                                         # q = Meter von der oberen Seitenlinie (beim Tor rechts = links aus Sicht des
#                                         # Angreifers; beim Tor links ist oben rechts aus seiner Sicht)
#   R = F.von_hochkant(x0, y0, x1, y1)    # altes Hochkant-Feld (Tor oben bei y0) -> R(x, y) = neue Tafelkoordinate
#   LINES = F.linien()                    # Außenlinie, Strafraum, Torraum, Strafraumbogen, Teil des Mittelkreises
#   TORE = [F.tor()] + F.minitore(15, 50) # Großfeldtor + Minitore an der Mittellinie (q in Metern)
#   P, B, C, mv, ps, dr, drehen, bl = hf.umrechnen(R)   # Bausteine aus hilfe.py, die jede Koordinate durch R schicken
# Im Haupt-board immer "massstab": "gross" (Figuren 0,72-mal so groß, 3D-Abstand |dx| >= 5,9 oder |dy| >= 11,2).
import math
import hilfe as h

# Streckung der Tiefe im Verhältnis zur Breite: an der Torlinie 1,39-mal (Strafraum und Torraum sehen fast echt aus),
# im Mittel 2,15-mal (so füllt eine 50 m tiefe Hälfte die Tafel von x 10 bis 90).
STRECK_TOR, STRECK_MITTEL = 1.39, 2.15


class Halbfeld:
    def __init__(self, tief=50, breit=65, tor="rechts", x_tor=None, x_mitte=None, y0=3, y1=52, s_tor=None):
        # tief/breit in Metern (Torlinie bis Mittellinie bzw. Grundlinie der Übung, Seitenlinie bis Seitenlinie).
        # Ohne x_tor/x_mitte: Länge auf der Tafel L = 2,15 * Maßstab der Breite * tief, höchstens 80, Feld mittig
        # (Hälfte 50 x 65 m: Tor rechts bei x 90, Mittellinie bei x 10; ein 35 m tiefes Feld wird kürzer und steht mittig).
        self.tief, self.breit, self.tor_seite = tief, breit, tor
        self.sy = (y1 - y0) / breit
        L = min(80, round(STRECK_MITTEL * self.sy * tief))
        rechts = tor == "rechts"
        if x_tor is None:
            x_tor = (50 + L / 2) if rechts else (50 - L / 2)
        if x_mitte is None:
            x_mitte = x_tor - L if rechts else x_tor + L
        x_tor = int(x_tor) if float(x_tor).is_integer() else x_tor
        self.x_tor, self.x_mitte, self.y0, self.y1 = x_tor, x_mitte, y0, y1
        self.L = abs(x_tor - x_mitte)
        s = round(STRECK_TOR * self.sy, 2) if s_tor is None else s_tor
        self.a = min(s, self.L / tief)  # Einheiten je Meter Tiefe an der Torlinie
        self.b = (self.L - self.a * tief) / tief ** 2  # f(d) = a*d + b*d², f(tief) = L
        self.dir = -1 if rechts else 1      # Richtung vom Tor zur Mittellinie auf der Tafel

    def f(self, d):
        # Abstand von der Torlinie auf der Tafel; außerhalb der Hälfte geradlinig weiter (Trainer, Wartende)
        if d < 0:
            return self.a * d
        if d > self.tief:
            return self.L + (self.a + 2 * self.b * self.tief) * (d - self.tief)
        return self.a * d + self.b * d * d

    def tiefe(self, x):
        # Umkehrung: Tafel-x -> Meter vor der Torlinie
        u = (x - self.x_tor) * self.dir
        if u < 0:
            return u / self.a
        if u > self.L:
            return self.tief + (u - self.L) / (self.a + 2 * self.b * self.tief)
        return (-self.a + math.sqrt(self.a ** 2 + 4 * self.b * u)) / (2 * self.b) if self.b else u / self.a

    def __call__(self, d, q):
        return [round(self.x_tor + self.dir * self.f(d), 1), round(self.y0 + q * self.sy, 1)]

    def mitte_y(self):
        return (self.y0 + self.y1) / 2

    def von_hochkant(self, x0, y0, x1, y1, tor="oben"):
        # Altes Hochkant-Feld (x0..x1 Breite, y0..y1 Tiefe, Tor oben bei y0 bzw. unten bei y1) -> neue Lage.
        # Eine Drehung, keine Spiegelung (bend und drehen(gegen=...) bleiben): Tor rechts = im Uhrzeigersinn (links im
        # Hochformat wird oben), Tor links = gegen den Uhrzeigersinn (links im Hochformat wird unten).
        def R(x, y):
            d = (y - y0) / (y1 - y0) * self.tief if tor == "oben" else (y1 - y) / (y1 - y0) * self.tief
            q = (x - x0) / (x1 - x0) * self.breit if tor == "oben" else (x1 - x) / (x1 - x0) * self.breit
            if self.tor_seite == "links":
                q = self.breit - q  # Drehung gegen den Uhrzeigersinn: links im Hochformat wird unten
            return self(d, q)
        return R

    def _bogen(self, dm, qm, r, w0, w1, n):
        # Kreisbogen in Metern (Mittelpunkt dm/qm, Winkel in Grad, 0 = Richtung Mittellinie) als kurze Linienstücke
        pts = [self(dm + r * math.cos(math.radians(w0 + (w1 - w0) * i / n)), qm + r * math.sin(math.radians(w0 + (w1 - w0) * i / n)))
               for i in range(n + 1)]
        return [h.line(*p, *q, dashed=False) for p, q in zip(pts, pts[1:])]

    def _rect(self, d0, d1, q0, q1):
        a, b = self(d0, q0), self(d1, q1)
        x, y = min(a[0], b[0]), min(a[1], b[1])
        return h.rect(x, y, round(abs(a[0] - b[0]), 1), round(abs(a[1] - b[1]), 1))

    def linien(self, strafraum=True, bogen=True, mittelkreis=True):
        # Echte Linien der Hälfte. Die linke (bzw. rechte) Kante des Außen-Rechtecks ist die Mittellinie.
        qm = self.breit / 2
        out = [self._rect(0, self.tief, 0, self.breit)]
        if strafraum:
            out += [self._rect(0, 16.5, qm - 20.15, qm + 20.15), self._rect(0, 5.5, qm - 9.15, qm + 9.15)]
        if bogen:
            # Strafraumbogen: Kreis um den Elfmeterpunkt (11 m, Radius 9,15 m), nur der Teil vor dem Strafraum
            w = math.degrees(math.acos(5.5 / 9.15))
            out += self._bogen(11, qm, 9.15, -w, w, 6)
        if mittelkreis and self.tief >= 45:
            # Halber Mittelkreis an der Mittellinie (nur wenn die Hälfte bis zur Mittellinie geht). Dort ist die Streckung am
            # größten, ein umgerechneter Kreis wäre ein langes Oval. Darum rund gezeichnet: Radius 9,15 m im Maßstab der Breite.
            # Nur Zierde (zeigt die Mittellinie), Spieler nicht daran ausrichten.
            r, ym = 9.15 * self.sy, self.mitte_y()
            pts = [[round(self.x_mitte - self.dir * r * math.sin(math.radians(180 * i / 10)), 1),
                    round(ym - r * math.cos(math.radians(180 * i / 10)), 1)] for i in range(11)]
            out += [h.line(*p, *q, dashed=False) for p, q in zip(pts, pts[1:])]
        return out

    def tor(self, size="gross"):
        return {"x": self.x_tor, "y": self.mitte_y(), "side": "right" if self.tor_seite == "rechts" else "left", "size": size}

    def minitore(self, *qs, d=None, size=None):
        # Tore an der Mittellinie (oder bei d Metern), q = Meter von der oberen Seitenlinie
        d = self.tief if d is None else d
        out = []
        for q in qs:
            x, y = self(d, q)
            g = {"x": x, "y": y, "side": "left" if self.tor_seite == "rechts" else "right"}
            if size:
                g["size"] = size
            out.append(g)
        return out

    def masslinie(self, text):
        # Nur die Tiefe als Maßlinie unten (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
        return [{"x1": min(self.x_tor, self.x_mitte), "y1": 58.6, "x2": max(self.x_tor, self.x_mitte), "y2": 58.6, "text": text}]


def am_fuss(p):
    # Ball am Fuß / Pass zu einem Spieler: Tafelpunkt p (x, y) -> (x + 0,6, y + 0,6)
    return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]


def richt(a, b, d=20):
    # Blickkegel nicht zu lang: Tafelpunkt in Richtung b, höchstens d Einheiten von a entfernt
    l = math.dist(a, b)
    d = min(d, l)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]


DREH = {"huerde": "huerde_ou", "huerde_ou": "huerde", "leiter": "leiter_ou", "leiter_ou": "leiter"}


def umrechnen(R, gedreht=True):
    # Bausteine aus hilfe.py, die jede Koordinate (Position, Ziel, von) durch R schicken. Was schon in Tafelkoordinaten
    # steht (Trainer, Ersatzbälle), direkt mit hilfe.P / hilfe.B setzen. gedreht=True (R aus von_hochkant): Hürden und
    # Leitern drehen mit (huerde <-> huerde_ou, leiter <-> leiter_ou). Bei R = Halbfeld in Metern gedreht=False.
    def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
    def B(i, x, y): return h.B(i, *R(x, y))
    def C(x, y, *a, **k):
        if gedreht and k.get("shape") in DREH:
            k["shape"] = DREH[k["shape"]]
        return h.C(*R(x, y), *a, **k)
    def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
    def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
    def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
    def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
    def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
    return P, B, C, mv, ps, dr, drehen, bl
