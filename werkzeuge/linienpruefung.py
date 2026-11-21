# Linienprüfung für Übungstafeln (Einheit.board und versions[].board).
#
# Prüft jeden Laufweg, Pass und jedes Dribbling genau so, wie die Seite die Kurve zeichnet
# (src/lib/playbook.js: quadratische Kurve, Kontrollpunkt = Mitte + Normale * bend), gegen alles,
# was in diesem Schritt stehen bleibt: Dummies, Spieler, Trainer, Hütchen, Stangen, liegende Bälle.
# Start- und Zielpunkt dürfen an einem Objekt liegen (Pass zum Spieler), Tore/Gassen zwischen zwei
# Hindernissen gelten als gewollt.
#
# Benutzung (Export der Einheiten als JSON-Liste mit code, board, versions):
#   python3 tools/linienpruefung.py einheiten.json          -> listet Treffer
#   python3 tools/linienpruefung.py einheiten.json --fix    -> sucht je Linie die kleinste Krümmung,
#                                                              die sauber vorbeiführt, und schreibt
#                                                              einheiten.korrigiert.json
# Pflicht beim Import neuer Übungen: erst --fix, dann prüfen, dass 0 Treffer übrig sind.
# Hütchen mit "id" (z. B. "k1") dürfen Schritte haben (type pass = geworfen) und sind danach Hindernis an ihrem neuen Platz.
import copy, json, math, sys

R = {"dummy": 2.9, "player": 2.8, "coach": 2.8, "cone": 1.9, "stange": 1.7, "ball": 1.4}


def ctrl(f, t, b):
    dx, dy = t[0] - f[0], t[1] - f[1]
    L = math.hypot(dx, dy) or 1
    return [(f[0] + t[0]) / 2 - dy / L * b, (f[1] + t[1]) / 2 + dx / L * b]


def q(f, c, t, s):
    u = 1 - s
    return [u * u * f[0] + 2 * u * s * c[0] + s * s * t[0], u * u * f[1] + 2 * u * s * c[1] + s * s * t[1]]


def pts_of(f, t, b, n=80):
    c = ctrl(f, t, b)
    return [q(f, c, t, s / n) for s in range(n + 1)]


def merge(base, ver):
    out = dict(base or {})
    for k, v in (ver or {}).items():
        if (len(v) if isinstance(v, list) else v is not None):
            out[k] = v
    return out


def side(f, t, o):
    return (t[0] - f[0]) * (o[1] - f[1]) - (t[1] - f[1]) * (o[0] - f[0])


def on_board(path):
    return all(-0.5 <= p[0] <= 100.5 and -0.5 <= p[1] <= 60.5 for p in path)


def objects(board):
    pos, kind = {}, {}
    for i, p in enumerate(board.get("players") or []):
        pid = p.get("id") or f"p{i + 1}"
        pos[pid] = [p["x"], p["y"]]
        kind[pid] = {"t": "dummy", "c": "coach"}.get(p.get("team"), "player")
    for i, b in enumerate(board.get("balls") or []):
        bid = b.get("id") or f"b{i + 1}"
        pos[bid] = [b["x"], b["y"]]
        kind[bid] = "ball"
    # Hütchen mit id sind beweglich (geworfene Hütchen): wie Spieler und Bälle mit Position und Schritten.
    # Hütchen ohne id stehen fest.
    cones = []
    for i, c in enumerate(board.get("cones") or []):
        kd = "stange" if c.get("shape") == "stange" else "cone"
        if c.get("id"):
            pos[c["id"]] = [c["x"], c["y"]]
            kind[c["id"]] = kd
        else:
            cones.append(("cone%d" % i, kd, [c["x"], c["y"]]))
    return pos, kind, cones


def hits(path, f, t, obs, ignore=()):
    out = []
    for oid, kd, o in obs:
        if oid in ignore:
            continue
        r = R[kd]
        if math.dist(f, o) < r + 0.6 or math.dist(t, o) < r + 0.6:
            continue
        d = min(math.dist(p, o) for p in path)
        if d < r:
            out.append((oid, kd, o, d))
    keep = []
    for h in out:
        # Eine Gasse zwischen zwei Hindernissen gilt nur bei Hütchen und Stangen als gewollt, nie bei Spielern, Dummys oder Bällen
        gate = h[1] in ("cone", "stange") and any(oid != h[0] and oid not in ignore and math.dist(o, h[2]) < 9
                   and side(f, t, o) * side(f, t, h[2]) < 0
                   and min(math.dist(p, o) for p in path) > 0.9 and h[3] > 0.9
                   for oid, kd, o in obs)
        if not gate:
            keep.append(h)
    if not on_board(path):
        keep.append(("rand", "cone", [0, 0], 0))
    return keep


def check(board, name, fix=False):
    pos, kind, cones = objects(board)
    issues = []
    for si, st in enumerate(board.get("steps") or []):
        moves = st.get("moves") or []
        movers = {m.get("who") for m in moves} | {m.get("ball") for m in moves if m.get("ball")}
        obs = [(k, kind[k], pos[k][:]) for k in kind if k not in movers] + cones
        for mi, m in enumerate(moves):
            w = m.get("who")
            f = m["from"] if m.get("from") and len(m["from"]) == 2 else pos.get(w)
            t = m.get("to")
            if not f or not t:
                continue
            b = m.get("bend") or 0
            ign = (w, m.get("ball"))
            hs = hits(pts_of(f, t, b), f, t, obs, ign)
            if hs:
                issue = {"name": name, "step": si + 1, "label": st.get("label", ""), "who": w, "type": m.get("type"),
                         "bend": b, "hits": [(h[0], h[1], round(h[3], 2)) for h in hs]}
                if fix:
                    # Die Krümmung ist Teil der Aussage (Bogenlauf, Kurve um einen Gegner): --fix ändert sie höchstens um 1,5.
                    # Reicht das nicht, bleibt der Treffer stehen und der Weg wird von Hand mit Zwischenpunkten gebaut
                    # (mehrere "lauf"-Schritte mit "after": true).
                    for nb in sorted([x / 2 for x in range(-40, 41)], key=lambda x: (abs(x - b), abs(x))):
                        if abs(nb - b) > 1.5:
                            break
                        if not hits(pts_of(f, t, nb), f, t, obs, ign):
                            m["bend"] = issue["fix_bend"] = nb
                            break
                issues.append(issue)
            pos[w] = t
            if m.get("ball") and m["ball"] in pos:
                dx, dy = t[0] - f[0], t[1] - f[1]
                L = math.hypot(dx, dy) or 1
                pos[m["ball"]] = [t[0] + dx / L * 1.6, t[1] + dy / L * 1.6]
    return issues


def check_unit(u, fix=False):
    base = u.get("board") or {}
    out = check(base, u["code"] + " Grundform", fix)
    for v in u.get("versions") or []:
        vb = v.get("board") or {}
        if fix and not vb.get("steps") and check(copy.deepcopy(merge(base, vb)), "x"):
            vb["steps"] = copy.deepcopy(base.get("steps") or [])
            v["board"] = vb
        out += check(merge(base, vb), u["code"] + " " + v.get("label", "Fassung"), fix)
    return out


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    units = data if isinstance(data, list) else data.get("entities", [data])
    fix = "--fix" in sys.argv
    total = 0
    for u in units:
        for i in check_unit(u, fix):
            total += 1
            print(f"{i['name']} | Schritt {i['step']} '{i['label']}' | {i['who']} ({i['type']}) bend {i['bend']}"
                  + (f" -> {i.get('fix_bend')}" if fix else "") + f" | {i['hits']}")
    if fix:
        out = sys.argv[1].rsplit(".", 1)[0] + ".korrigiert.json"
        json.dump(units, open(out, "w"), ensure_ascii=False)
        rest = sum(len(check_unit(u)) for u in units)
        print(f"{total} Linien bearbeitet, Rest-Treffer: {rest}, gespeichert in {out}")
    else:
        print(f"{total} Treffer")
