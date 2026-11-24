# UE-174 quer legen (Inhaber, 24.11.2026, „Langes Feld QUER“). GRUPPE 2: schon eingesprochen, darum KEIN Sprechtext und keine
# Schrittzahl ändern, nur Koordinaten, Linien, Tore, Hütchen, Maßlinien.
#   python3 werkbank.py lesen UE-174 vorher.json && python3 bau/ue174_quer.py vorher.json ue174_quer.json
# Eingabe = die aus der Datenbank gelesene Einheit (Hochformat, Feld x 32.1-67.9, y 5-55 = 23 x 32 m, Jugendtore oben und unten).
# Drehung um 90 Grad wie R() in ue317.py: oben -> rechts, unten -> links, links -> oben, rechts -> unten. Eine Drehung erhält den
# Drehsinn (bend und drehen(gegen=...) bleiben). Team Neon greift jetzt nach rechts an (Tor von k1 rechts), Team Rot nach links.
# Feld quer: x 14-84, y 4-51 (70 x 47 Einheiten: 2,19 bzw. 2,04 Einheiten je Meter, fast derselbe Maßstab; bei 23 x 32 m füllt
# das Feld die Tafel in der Höhe, in der Länge bleibt links und rechts Platz für die Tore).
# Bälle am Fuß und Pässe zu einem Spieler (Spieler + 0,6) liegen nach der Drehung wieder bei Spieler + 0,6.
# NEU: Plätze, die nach der Drehung für den 3D-Abstand in der Länge versetzt sind (Hochformat-Punkt -> Platz quer). Jeder Punkt
# wird überall ersetzt (Startplatz, Laufziel, Pass zu ihm mit + 0,6).
import json, sys

X0, X1, Y0, Y1 = 32.1, 67.9, 5, 55       # Feld im Hochformat
FX0, FX1, FY0, FY1 = 14, 84, 4, 51       # Feld quer
DREH = "A"                               # A: oben -> rechts, links -> oben
NEU = {
    (41.7, 12): [73.5, 16.6],   # Spieler vier etwas weiter weg vom Torwart (standen quer hintereinander)
    (58.3, 7): [73, 38.4],      # Spieler acht ebenso
    (50, 22.3): [50.5, 27.5],   # Spieler neun etwas zur Mitte, sonst steht er in 3D vor Spieler sieben
    (58.3, 43): [29.5, 38.4],   # Spieler fünf etwas weiter von Spieler zehn weg
    (33.4, 43): [34, 5.7],      # Spieler drei etwas weiter von Spieler sechs weg
    (73, 33): [45.8, 55],       # Steigerung: Spieler zwei als Anspieler draußen -> quer unten, über der Maßlinie
}
# Trainer und Ersatzbälle unten an der Seitenlinie (vorher rechts neben dem Feld, auf Höhe von Spieler vier).
FEST = {"T": [74, 55.3], "s1": [77.5, 55.8], "s2": [80, 55.8]}
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "32 m"}]  # nur die Länge (links und rechts stehen Tore)

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


# organisation wird nicht eingesprochen (Koordinator, 24.11.2026): Sätze mit oben/unten/links/rechts an die Querlage angepasst.
ORGANISATION = {1: 'Verteilen: Zwei Teams zu fünft, dazu in jedem Tor ein Torwart. Jedes Team greift auf ein Tor an und verteidigt das andere. Der Trainer steht an der Seite mit Bällen.'}

u = json.load(open(sys.argv[1]))
u = u[0] if isinstance(u, list) else u
grund = json.loads(json.dumps(u["board"]))
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    drehe_board(b, anker_von(b, grund) + anker_von(grund, grund), FEST)
for i, t in ORGANISATION.items():
    u["organisation"][i] = t
json.dump(u, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
