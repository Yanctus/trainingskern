# UE-138 quer legen (Inhaber, 24.11.2026, „Langes Feld QUER“). GRUPPE 2: schon eingesprochen, darum KEIN Sprechtext und keine
# Schrittzahl ändern, nur Koordinaten, Linien, Tore, Hütchen, Maßlinien.
#   python3 werkbank.py lesen UE-138 vorher.json && python3 bau/ue138_quer.py vorher.json ue138_quer.json
# Eingabe = die aus der Datenbank gelesene Einheit (Hochformat, Feld x 35-65, y 6-56 = 14 x 23 m, Jugendtor mit Torwart oben,
# Start und Wartende links und rechts neben dem Tor).
# Drehung um 90 Grad wie R() in ue317.py: oben -> rechts, unten -> links, links -> oben, rechts -> unten. Eine Drehung erhält den
# Drehsinn (bend und drehen(gegen=...) bleiben). Das Tor steht jetzt rechts, gespielt wird nach rechts.
# Feld quer: x 13-86, y 6.5-51 (73 x 44,5 Einheiten, derselbe Maßstab in beiden Richtungen: 3,17 bzw. 3,18 Einheiten je Meter).
# Oben bleibt etwas Platz für Spieler neun am Start (er stand im Hochformat links neben dem Feld).
# Bälle am Fuß und Pässe zu einem Spieler (Spieler + 0,6) liegen nach der Drehung wieder bei Spieler + 0,6.
# NEU: Plätze, die nach der Drehung versetzt sind (Hochformat-Punkt -> Platz quer). Jeder Punkt wird überall ersetzt
# (Startplatz, Laufziel, Pass zu ihm mit + 0,6). Im Hochformat standen alle Wartenden in einer Reihe neben dem Tor; quer
# stünden sie hintereinander außerhalb der Tafel. Darum: Die Verteidiger am Start stehen oben und unten an der Torlinie,
# die Wartenden dahinter hinter der Torlinie, je zwei oben und unten neben dem Tor. Der Torwart steht auf der Linie,
# sonst verdeckt er in 3D die Angreifer am Start.
import json, sys

X0, X1, Y0, Y1 = 35, 65, 6, 56           # Feld im Hochformat
FX0, FX1, FY0, FY1 = 13, 86, 6.5, 51     # Feld quer
DREH = "A"                               # A: oben -> rechts, links -> oben
NEU = {
    (50, 9): [85.5, 28.8],      # Torwart auf der Linie
    (32, 12): [86, 3.3],        # Spieler neun am Start oben an der Torlinie
    (68, 12): [86, 55],         # Spieler acht am Start unten an der Torlinie
    (22, 12): [95, 3.3],        # Wartende hinter der Torlinie: Spieler drei und Spieler elf oben
    (13, 12): [95, 19],
    (78, 12): [95, 55],         # Spieler sechs und Spieler sieben unten
    (87, 12): [95, 39],
    (74, 32): [48, 55.3],       # Trainer unten an der Seitenlinie
    # Spieler vier kommt nach dem Lauf um die Stange wieder an seinen Ball (im Hochformat lag der Ball direkt vor ihm;
    # gedreht läge er sonst auf der falschen Seite). So startet er auch in beiden Coaching-Punkten.
    (42.5, 30): [53.9, 15.4],
    (42.5, 30.5): [53.9, 15.4],
}
FEST = {"s1": [51.5, 55.8], "s2": [54, 55.8]}
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "25 m"}]  # nur die Länge (rechts steht das Tor)

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
ORGANISATION = {0: 'Aufbauen: Ein Feld von 14 mal 25 Metern, an einer kurzen Seite ein Jugendtor mit Torwart. Weiter vom Tor weg steht auf jeder Seite eine Stange, nah am Tor zwei Hütchen als Start.', 1: 'Verteilen: Team Neon greift an, Team Rot verteidigt. Je ein Angreifer und ein Verteidiger starten auf beiden Seiten am Tor, die anderen warten hinter der Torlinie neben dem Tor. Der Trainer steht am Rand mit Bällen.', 2: 'Ablauf: Ein Angreifer passt quer zum anderen, der nimmt an und lässt den Ball liegen. Beide Angreifer sprinten um ihre Stange, holen den Ball und kombinieren zum Abschluss. Die Verteidiger sprinten gleichzeitig hinterher und stören.'}

u = json.load(open(sys.argv[1]))
u = u[0] if isinstance(u, list) else u
grund = json.loads(json.dumps(u["board"]))
for b in [u["board"]] + [v["board"] for v in u.get("versions") or []]:
    drehe_board(b, anker_von(b, grund) + anker_von(grund, grund), FEST)
for i, t in ORGANISATION.items():
    u["organisation"][i] = t
# Meterangaben gerundet (Darstellung, 26.11.2026): ab 20 m auf Fünfer, unter 20 m genau.
u["field_size"] = "14 x 25 m"
json.dump(u, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
