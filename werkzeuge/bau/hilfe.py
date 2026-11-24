# Bausteine für Einheiten-JSON (kurz halten, keine null-Felder: die Datenbank füllt sie selbst)
def P(i, t, x, y, l): return {"id": i, "team": t, "x": x, "y": y, "label": l}
def B(i, x, y): return {"id": i, "x": x, "y": y}
def mv(who, to, typ="lauf", delay=None, after=None, bend=0, ball=None):
    m = {"who": who, "to": to, "type": typ}
    if bend: m["bend"] = bend
    if delay: m["delay"] = delay
    if after: m["after"] = True
    if ball: m["ball"] = ball
    return m
def dr(who, ball, to, **k): return mv(who, to, "dribbling", ball=ball, **k)
def ps(ball, to, **k): return mv(ball, to, "pass", **k)
# Aufdrehen: Drehpfeil im Bogen um den Spieler, endet in der Richtung to, in die er aufdreht. gegen=True dreht gegen den
# Uhrzeigersinn. NICHT den Blickkegel fürs Aufdrehen nehmen: bl() ist nur fürs Schauen/Scannen.
def drehen(who, to, gegen=False, **k):
    m = mv(who, to, "dreh", **k)
    if gegen: m["bend"] = -1
    return m
# Schulterblick: Kegel vom Spieler in Richtung to (Länge = Abstand). Zweimal mit after=True = links und rechts scannen.
def bl(who, to, weite=None, dauer=None, **k):
    m = mv(who, to, "blick", **k)
    if weite: m["weite"] = weite
    if dauer: m["dauer"] = dauer
    return m
def S(label, say, *moves): return {"label": label, "say": say, "moves": list(moves)}
def V(label, say, title, text, players, balls, steps, **extra):
    b = {"players": players, "balls": balls, "steps": steps}
    b.update(extra)
    return {"label": label, "say": say, "title": title, "text": text, "board": b}
def rect(x, y, w, h, dashed=False):
    r = {"type": "rect", "x": x, "y": y, "w": w, "h": h}
    if dashed: r["dashed"] = True
    return r
def line(x1, y1, x2, y2, dashed=True): return {"type": "line", "x1": x1, "y1": y1, "x2": x2, "y2": y2, "dashed": dashed}
def C(x, y, c="orange", **k): return {"x": x, "y": y, "color": c, **k}
# Geräte: C(x, y, shape="stange") Stange · "huerde"/"huerde_ou" Minihürde · "leiter" Koordinationsleiter (16 x 5 Einheiten,
# Mitte bei x/y, läuft von links nach rechts) · "leiter_ou" Leiter senkrecht (von oben nach unten) · "ring" Koordinationsring.
def leiter(x, y, senkrecht=False, c="orange"): return C(x, y, c, shape="leiter_ou" if senkrecht else "leiter")
def ring(x, y, c="orange"): return C(x, y, c, shape="ring")
def ecken(x, y, w, h): return [C(x, y), C(x + w, y), C(x, y + h), C(x + w, y + h)]
def dims(x1, x2, y1, y2, tb, tr, rx=None):
    return [{"x1": x1, "y1": 58.6, "x2": x2, "y2": 58.6, "text": tb}, {"x1": rx or x2 + 8, "y1": y1, "x2": rx or x2 + 8, "y2": y2, "text": tr}]
ORG = ["lines", "cones", "players", "balls,arrows"]
