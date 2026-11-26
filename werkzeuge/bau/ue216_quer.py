# UE-216 quer legen (Inhaber, 24.11.2026, „Langes Feld QUER“). GRUPPE 2: schon eingesprochen, darum KEIN Sprechtext und keine
# Schrittzahl ändern, nur Koordinaten, Linien, Tore, Hütchen, Maßlinien.
#   python3 werkbank.py lesen UE-216 vorher.json && python3 bau/ue216_quer.py vorher.json ue216.json
# Eingabe = die aus der Datenbank gelesene Einheit (Hochformat, Feld x 32-68, y 3-57 = 18 x 27 m, drei Zonen, Jugendtor oben
# und unten). R() dreht um 90 Grad wie in ue317.py: oben -> rechts, unten -> links, links -> oben, rechts -> unten. Eine Drehung
# erhält den Drehsinn (bend und drehen(gegen=...) bleiben). Feld quer: x 13-85, y 4-51 (2,67 bzw. 2,61 Einheiten je Meter).
# Team Neon baut links auf und greift nach rechts an, die Zonengrenzen stehen senkrecht. Trainer unten an der Seitenlinie.
# Bälle am Fuß und Pässe zu einem Spieler (Spieler + 0,6) werden nach der Drehung wieder auf Spieler + 0,6 gesetzt.
# VERSATZ (Hochformat-Punkte, vor der Drehung): Wer im Hochformat nebeneinander stand, steht quer hintereinander und wird
# leicht versetzt (3D-Abstand). Jeder Punkt wird überall ersetzt (Startplatz, Laufziel, Pass zu ihm mit + 0,6).
import json, sys

X0, X1, Y0, Y1 = 32, 68, 3, 57          # Feld im Hochformat
FX0, FX1, FY0, FY1 = 13, 85, 4, 51      # Feld quer
VERSATZ = {
    # Nachtrag Passbahn (25.11.2026): Gegner neben die Passbahn, Ablauf und Sprechtext unverändert.
    (44, 32): (40.3, 31.9),   # Spieler sechs geht frontal auf Spieler vier zu (quer [46.5, 14.8]) statt in den Pass zu Spieler acht
    (56, 17): (53.8, 16.1),   # Spieler drei schiebt zu Spieler neun (quer [67.5, 32.5]) statt in die Ablage zu Spieler acht
}
# Trainer und Ersatzbälle unten an der Seitenlinie (vorher rechts neben dem Feld, das wäre quer unter der Tafel).
FEST = {"T": [40, 55.3], "s1": [43.5, 55.8], "s2": [46, 55.8]}  # id -> Platz quer
# Nachtrag (Koordinator, 24.11.2026): organisation wird nicht eingesprochen, darum nach dem Drehen angepasst (Tore links und rechts).
ORGANISATION = ["Aufbauen: Ein Feld von 18 mal 25 Metern in drei gleich große Zonen geteilt. Links und rechts steht je ein Jugendtor.",
 "Verteilen: Team Neon mit Torwart und zwei Innenverteidigern hinten, einem in der Mitte und einem Stürmer vorn. Team Rot mit einem Stürmer hinten, einem in der Mitte und zwei Verteidigern vorn. Rechts steht ein zweiter Torwart im Tor. Der Trainer steht unten an der Seitenlinie mit Bällen.",
 "Ablauf: Alle bleiben in ihren Zonen. Ein Innenverteidiger verlagert, rückt mit Ball in die Mitte auf und schafft so zwei gegen einen. Kommt der Ball nach vorn, darf der Mittelfeldspieler mit, dann ist es zwei gegen zwei.",
 "Wertung und Wechsel: Ein Treffer im rechten Tor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, kontert es auf das linke Tor, und ein Treffer gibt einen Punkt für Team Rot. Danach startet der Torwart von Team Neon mit einem neuen Ball."]
SEITE = {"top": "right", "right": "bottom", "bottom": "left", "left": "top"}
FORM = {"leiter": "leiter_ou", "leiter_ou": "leiter", "huerde": "huerde_ou", "huerde_ou": "huerde"}
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "25 m"}]  # nur die Länge (rechts steht das Tor)


def R(x, y):
    return [round(FX0 + (Y1 - y) / (Y1 - Y0) * (FX1 - FX0), 1), round(FY0 + (x - X0) / (X1 - X0) * (FY1 - FY0), 1)]


def nah(a, b): return abs(a[0] - b[0]) < 0.05 and abs(a[1] - b[1]) < 0.05


def vs(p):
    for a, b in VERSATZ.items():
        if nah(p, a): return list(b)
    return list(p)


def punkt(p, anker):
    """Punkt drehen; liegt er bei einem Spieler + 0,6 (Ball am Fuß, Pass zu ihm), bleibt er quer bei Spieler + 0,6."""
    for a in anker:
        if nah(p, [a[0] + 0.6, a[1] + 0.6]):
            q = R(*vs(a))
            return [round(q[0] + 0.6, 1), round(q[1] + 0.6, 1)]
    return R(*vs(p))


def drehe_board(b, anker):
    for p in b.get("players") or []:
        p["x"], p["y"] = FEST.get(p["id"]) or R(*vs([p["x"], p["y"]]))
    for o in b.get("balls") or []:
        o["x"], o["y"] = FEST.get(o["id"]) or punkt([o["x"], o["y"]], anker)
    for c in b.get("cones") or []:
        c["x"], c["y"] = R(c["x"], c["y"])
        if c.get("shape") in FORM: c["shape"] = FORM[c["shape"]]
    for g in b.get("goals") or []:
        g["x"], g["y"] = R(g["x"], g["y"])
        g["side"] = SEITE[g["side"]]
    for l in b.get("labels") or []:
        l["x"], l["y"] = R(l["x"], l["y"])
    for l in b.get("lines") or []:
        if l["type"] in ("rect", "zone"):
            a, c = R(l["x"], l["y"]), R(l["x"] + l["w"], l["y"] + l["h"])
            l["x"], l["y"], l["w"], l["h"] = min(a[0], c[0]), min(a[1], c[1]), round(abs(a[0] - c[0]), 1), round(abs(a[1] - c[1]), 1)
        elif l["type"] == "circle":
            l["x"], l["y"] = R(l["x"], l["y"])
            l["r"] = round(l["r"] * (FX1 - FX0) / (Y1 - Y0), 1)
        else:
            (l["x1"], l["y1"]), (l["x2"], l["y2"]) = R(l["x1"], l["y1"]), R(l["x2"], l["y2"])
    for a in b.get("arrows") or []:
        for k in ("from", "to"):
            if a.get(k): a[k] = R(*a[k])
    for st in b.get("steps") or []:
        for m in st.get("moves") or []:
            for k in ("to", "from", "von"):
                if m.get(k) and len(m[k]) == 2:
                    m[k] = punkt(m[k], anker)
    if b.get("dims"): b["dims"] = DIMS


def anker_von(b, grund):
    """Plätze, an denen ein Spieler steht oder ankommt (Hochformat)."""
    ids = {p["id"] for p in (b.get("players") or grund.get("players") or [])}
    pts = [[p["x"], p["y"]] for p in (b.get("players") or [])]
    for st in b.get("steps") or []:
        for m in st.get("moves") or []:
            if m["who"] in ids and m.get("type") in ("lauf", "dribbling") and m.get("to"):
                pts.append(m["to"])
    return pts


def sauber(x):
    if isinstance(x, dict): return {k: sauber(v) for k, v in x.items() if v is not None and not (k == "from" and v == [])}
    if isinstance(x, list): return [sauber(v) for v in x]
    return x


u = json.load(open(sys.argv[1]))
u = u[0] if isinstance(u, list) else u
grund = json.loads(json.dumps(u["board"]))
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    drehe_board(b, anker_von(b, grund) + anker_von(grund, grund))
u["board"] = sauber(u["board"])
u["versions"] = sauber(u["versions"])
u["organisation"] = ORGANISATION
json.dump(u, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
