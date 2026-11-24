# UE-067 quer legen (Inhaber, 24.11.2026, „Langes Feld QUER“). GRUPPE 2: schon eingesprochen, darum KEIN Sprechtext und keine
# Schrittzahl ändern, nur Koordinaten, Linien, Tore, Hütchen, Maßlinien (organisation/description dürfen angepasst werden).
#   python3 werkbank.py lesen UE-067 vorher.json && python3 bau/ue067_quer.py vorher.json ue067_quer.json
# Eingabe = die aus der Datenbank gelesene Einheit (Hochformat, Feld x 31-71.5, y 3-57 = 27 x 37 m). Besonderheit: Das Tor mit
# Strafraum steht hier an der LANGEN Seite (rechts), gespielt wird über die 27 m auf das Tor zu. Quer gelegt (lange Seite
# waagrecht) steht das Tor darum oben in der Mitte, gespielt wird nach oben.
# Drehung um 90 Grad: oben -> links, rechts -> oben, unten -> rechts, links -> unten (andersherum als R() in ue317.py, damit das
# Tor oben steht und unten an der Seitenlinie Platz für den Trainer bleibt). Eine Drehung erhält den Drehsinn (bend bleibt).
# Feld quer: x 20-86, y 5-51 (66 x 46 Einheiten: 1,78 bzw. 1,70 Einheiten je Meter, fast derselbe Maßstab; oben braucht das Tor
# Platz, links neben dem Feld warten die Spieler am Start, rechts steht die Breiten-Maßlinie).
# Bälle am Fuß und Pässe zu einem Spieler (Spieler + 0,6) liegen nach der Drehung wieder bei Spieler + 0,6.
# NEU: Plätze, die nach der Drehung versetzt sind (Hochformat-Punkt -> Platz quer). Jeder Punkt wird überall ersetzt
# (Startplatz, Laufziel, Pass zu ihm mit + 0,6). Die Spieler an den Stangen standen im Hochformat nebeneinander, quer stehen sie
# hintereinander: Damit sie sich in 3D nicht verdecken, steht jeder zweite auf der anderen Seite seiner Stange.
import json, sys

X0, X1, Y0, Y1 = 31, 71.5, 3, 57         # Feld im Hochformat
FX0, FX1, FY0, FY1 = 20, 86, 5, 51       # Feld quer
DREH = "B"                               # B: oben -> links, rechts -> oben
NEU = {
    (60, 3.3): [20.4, 14.5],    # Spieler neun am Start etwas näher zum Tor (3D-Abstand zu Spieler fünf)
    (60, 4.9): [21.0, 15.1],    # sein Ball
    (68.5, 3.3): [11.5, 9],     # Wartende am Start links neben dem Feld (vorher hinter der Torlinie, quer wäre das über der Tafel)
    (77, 3.3): [3, 22],
    (78.5, 19): [3, 40],
    (87, 10): [10.5, 56],       # Trainer unten an der Seitenlinie beim Start, Ersatzbälle daneben
    (89, 13): [14, 55.8],
    (89.5, 7.5): [16.5, 55.8],
    # Spieler an den Stangen: Quer stünden sie in ihrer Reihe hintereinander und verdeckten sich in 3D. Darum stehen
    # Spieler fünf und Spieler acht auf der Innenseite ihrer Stange (zur anderen Reihe hin), Spieler zwei etwas weiter außen.
    (49, 5.5): [27.9, 30.6],    # Spieler fünf
    (49.8, 6.0): [28.5, 31.2],  # Pass zu Spieler fünf
    (44.2, 24.3): [36.6, 36],   # Spieler acht
    (45.0, 23.6): [37.2, 36.6], # Pass zu Spieler acht
    (39.6, 5.5): [19.5, 41.2],  # Spieler zwei
    (40.3, 6.0): [20.1, 41.8],  # Pass zu Spieler zwei
    (54.8, 24.3): [45.8, 24],   # Spieler elf und Spieler zehn dicht hinter ihrer Stange (wie im Hochformat)
    (34.4, 24.3): [45.8, 47.1],
    # Slalom: die Wendepunkte so dicht an den Hütchen wie im Hochformat
    (39, 41.2): [66.2, 41.9], (43.1, 36.6): [61.6, 37.3], (47.5, 41.2): [66.2, 32.3], (52.1, 36.6): [61.6, 27.0],
    # Steigerung: Spieler elf an der Stange etwas weiter vom Torwart weg
    (57.8, 25.4): [44.9, 22.4], (57.6, 23.8): [45.5, 23.0],
}
# Biegung gegen Stangen im Weg (Schritt-Label, wer) -> bend: Spieler zwei dribbelt außen an seiner Stange vorbei
BIEGUNG = {("Ablage auf die Zehn", "n2"): 5}
FEST = {}
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "37 m"}, {"x1": FX1 + 8, "y1": FY0, "x2": FX1 + 8, "y2": FY1, "text": "27 m"}]

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
ORGANISATION = {1: 'Verteilen: Je ein Spieler steht an jeder Stange, die übrigen warten mit Bällen am Start neben dem Strafraum. Ich stehe mit weiteren Bällen an der Seitenlinie.'}

u = json.load(open(sys.argv[1]))
u = u[0] if isinstance(u, list) else u
grund = json.loads(json.dumps(u["board"]))
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    for st in b.get("steps") or []:
        for m in st.get("moves") or []:
            if (st["label"], m["who"]) in BIEGUNG and m.get("type") == "dribbling":
                m["bend"] = BIEGUNG[(st["label"], m["who"])]
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    drehe_board(b, anker_von(b, grund) + anker_von(grund, grund), FEST)
for i, t in ORGANISATION.items():
    u["organisation"][i] = t
json.dump(u, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
