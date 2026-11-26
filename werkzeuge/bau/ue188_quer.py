# UE-188 quer legen (Inhaber, 24.11.2026, „Langes Feld QUER“). GRUPPE 2: schon eingesprochen, darum KEIN Sprechtext und keine
# Schrittzahl ändern, nur Koordinaten, Linien, Tore, Hütchen, Maßlinien.
#   python3 werkbank.py lesen UE-188 vorher.json && python3 bau/ue188_quer.py vorher.json ue188_quer.json
# Eingabe = die aus der Datenbank gelesene Einheit (Hochformat, Feld x 32-68, y 5-55 = 23 x 32 m, Jugendtore oben und unten,
# Trainer links neben dem Feld).
# Drehung um 90 Grad, diesmal andersherum als R() in ue317.py, damit der Trainer von selbst unten an der Seitenlinie steht:
# oben -> links, unten -> rechts, links -> unten, rechts -> oben. Eine Drehung erhält den Drehsinn (bend und drehen(gegen=...)
# bleiben). Team Neon greift jetzt nach links an (Tor von k1 links).
# Feld quer: x 14-84, y 4-51 (70 x 47 Einheiten: 2,19 bzw. 2,04 Einheiten je Meter, fast derselbe Maßstab; bei 23 x 32 m füllt
# das Feld die Tafel in der Höhe, in der Länge bleibt links und rechts Platz für die Tore).
# Bälle am Fuß und Pässe zu einem Spieler (Spieler + 0,6) liegen nach der Drehung wieder bei Spieler + 0,6.
# NEU: Plätze, die nach der Drehung für den 3D-Abstand in der Länge versetzt sind (Hochformat-Punkt -> Platz quer). Jeder Punkt
# wird überall ersetzt (Startplatz, Laufziel, Pass zu ihm mit + 0,6).
import json, sys

X0, X1, Y0, Y1 = 32, 68, 5, 55           # Feld im Hochformat
FX0, FX1, FY0, FY1 = 14, 84, 4, 51       # Feld quer
DREH = "B"                               # B: oben -> links, links -> unten
NEU = {
    (24, 18): [32, 55.3],       # Trainer unten an der Seitenlinie (der Ball am Fuß folgt ihm), Ersatzbälle siehe FEST
    (50.5, 37): [62, 26.8],     # Spieler sechs etwas weiter von Spieler vier und Spieler acht weg (standen quer hintereinander)
    (67.5, 28): [44.5, 4.7],    # Spieler sieben etwas weiter von Spieler acht weg
    (53, 33.5): [53.2, 22.7],   # Spieler sechs geht zum Kopfball so nah an den Ball wie im Hochformat (der Abpraller geht nicht durch ihn)
    (30, 23): [39.5, 49.5],     # Blick von Spieler vier genau zum Trainer (der steht quer etwas anders)
    # Nachtrag Passbahn (25.11.2026): Der hohe Ball kommt bei Spieler sechs runter (nicht bei Spieler acht), sonst fliegt der
    # Kopfball aus Schritt 2 von Spieler acht aus durch Spieler sechs. Spieler acht steht 2,5 dahinter.
    (55.6, 31.6): [52.7, 22.0],
}
FEST = {"s1": [28.5, 55.8], "s2": [26, 55.8]}
# Eckhütchen kommen mit der Drehung auf die neuen Ecken.
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "30 m"}]  # nur die Länge (links und rechts stehen Tore)

SEITE = {"A": {"top": "right", "right": "bottom", "bottom": "left", "left": "top"},
         "B": {"top": "left", "left": "bottom", "bottom": "right", "right": "top"}}[DREH]
FORM = {"leiter": "leiter_ou", "leiter_ou": "leiter", "huerde": "huerde_ou", "huerde_ou": "huerde"}


def R(x, y):
    if DREH == "A":
        return [round(FX0 + (Y1 - y) / (Y1 - Y0) * (FX1 - FX0), 1), round(FY0 + (x - X0) / (X1 - X0) * (FY1 - FY0), 1)]
    return [round(FX0 + (y - Y0) / (Y1 - Y0) * (FX1 - FX0), 1), round(FY0 + (X1 - x) / (X1 - X0) * (FY1 - FY0), 1)]


def nah(a, b): return abs(a[0] - b[0]) < 0.05 and abs(a[1] - b[1]) < 0.05


def platz(p):
    for a, b in NEU.items():
        if nah(p, a): return list(b)
    return R(*p)


def punkt(p, anker):
    """Punkt drehen; liegt er bei einem Spieler + 0,6 (Ball am Fuß, Pass zu ihm), bleibt er quer bei Spieler + 0,6."""
    for a in NEU:
        if nah(p, a): return list(NEU[a])
    for a in anker:
        if nah(p, [a[0] + 0.6, a[1] + 0.6]):
            q = platz(a)
            return [round(q[0] + 0.6, 1), round(q[1] + 0.6, 1)]
    return R(*p)


def drehe_board(b, anker, fest):
    for p in b.get("players") or []:
        p["x"], p["y"] = fest.get(p["id"]) or platz([p["x"], p["y"]])
    for o in b.get("balls") or []:
        o["x"], o["y"] = fest.get(o["id"]) or punkt([o["x"], o["y"]], anker)
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
            l["r"] = round(l["r"] * (FY1 - FY0) / (X1 - X0), 1)
        else:
            (l["x1"], l["y1"]), (l["x2"], l["y2"]) = R(l["x1"], l["y1"]), R(l["x2"], l["y2"])
    for a in b.get("arrows") or []:
        for k in ("from", "to"):
            if a.get(k) and len(a[k]) == 2: a[k] = R(*a[k])
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


u = json.load(open(sys.argv[1]))
u = u[0] if isinstance(u, list) else u
grund = json.loads(json.dumps(u["board"]))
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    drehe_board(b, anker_von(b, grund) + anker_von(grund, grund), FEST)
# Meterangaben gerundet (Darstellung, 26.11.2026): ab 20 m auf Fünfer, unter 20 m genau.
u["field_size"] = "25 x 30 m"
u["organisation"][0] = u["organisation"][0].replace("23 mal 32 Metern", "25 mal 30 Metern")
json.dump(u, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
