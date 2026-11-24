# Werkbank für den Übungs-Import aus Google Drive (Video + PDF -> Einheit).
# Läuft in der Claude-Code-Umgebung (braucht curl, ffmpeg, pdftotext, pdftoppm, python3; für "bild" Playwright).
# Google Drive muss in der Umgebung freigegeben sein (drive.google.com, drive.usercontent.google.com).
# tools/linienpruefung.py und tools/regeln.py müssen im selben Ordner liegen. Anleitung: README, "Merkzettel: Übungen aus Video nachbauen".
#
#   python3 werkbank.py liste                      -> alle Wochen-Ordner mit ihren Übungen
#   python3 werkbank.py holen Woche-19-Passing     -> lädt Video+PDF jeder Übung der Woche nach ./import/<Woche>/<Name>/
#                                                     und legt daneben: text.txt (PDF-Text), pdf-1.png/pdf-2.png,
#                                                     uebersicht.png (25 Bilder übers ganze Video), anfang.png
#                                                     (die ersten 25 Sekunden, 1 Bild/s: hier steht meist der Ablauf)
#   python3 werkbank.py pruefen datei.json [--fix] -> Linienprüfung + Regelprüfung (regeln.py); --fix biegt Linien zurecht und schreibt die Datei zurück
#                                                     Fertig ist eine Einheit erst bei "Rest: 0" UND "Regeln: 0 Hinweise"
#   python3 werkbank.py bild datei.json            -> Kontrollbild datei.png: Grundform + alle Fassungen mit Laufwegen
#   python3 werkbank.py bild3d datei.json          -> datei-3d-<Code>-<n>.png: Näherung der 3D-Ansicht der Einheiten-Seite (Figuren stehen,
#                                                     Papierfiguren wie in der App). Ansehen: stehen alle Figuren, verdecken sie sich, liegt
#                                                     eine Maßlinie oder Beschriftung unter einer Figur? Die echte Seite ist maßgeblich, siehe README.
#
#   python3 werkbank.py lesen UE-061 [UE-062 ...] datei.json -> Einheiten aus der Datenbank holen (kostenlos, ohne Metafelder)
#   python3 werkbank.py patch db.json neu.json      -> {"$set": ...} nur mit den geänderten Stellen, für update_entities (Korrekturen billig)
#   python3 werkbank.py blatt datei.json            -> datei-blatt.png: 2D mit Laufwegen + 3D-Näherung aller Tafeln in EINEM Bild
#   python3 werkbank.py ton <Ordner> [modell]      -> <Ordner>/ton.txt: gesprochene Erklärung aus dem Video als Text mit Zeitstempeln (zuerst lesen!)
#   python3 werkbank.py vorgaben "<Übungsname>"     -> feste Regel für age_groups und duration_minutes (stehen nicht im PDF)
#   python3 werkbank.py dauer <Ordner>             -> Länge des Videos in Sekunden (Ordner = import/<Woche>/<Übung>)
#   python3 werkbank.py szene <Ordner> <von> <bis> [fps] -> <Ordner>/szene-<von>-<bis>.png: 16 Bilder aus diesem Abschnitt (Standard 2 je Sekunde).
#                                                     PFLICHT für jeden Laufweg, jede Fassung und jede Steigerung: die Übersicht ist zu grob.
#   python3 werkbank.py vergleichen datei.json gelesen.json -> Pflicht nach dem Anlegen: gelesen.json = Einheit, wieder aus der Datenbank gelesen
#                                                     (query_entities, nach einem zweiten, harmlosen Speichern). Meldet jedes Feld, das in der
#                                                     Datei steht, aber in der Datenbank fehlt oder anders ist (die Datenbank löscht Felder,
#                                                     die nicht im Schema stehen).
#
# datei.json = eine Einheit (Objekt) oder eine Liste von Einheiten, genau so, wie sie in die Datenbank geht.

import copy, html, json, os, re, subprocess, sys

# Drive-Ordner der Pläne: U9-U11 (erster Plan) und U12-U14 (ab 22.11.2026). Umschalten mit TK_PLAN=u12 (Standard: u12)
ORDNER = {"u9": "1PAVZ8RM1mk7ADyzNj-AlE-SmivHmAgYY", "u12": "1toSAscipZG3m0iyo2vHFqI68R1XH7lz8", "u15": "1mgpocVZ0OriqoNZwBsCF7dAvOaFm8KTu"}
ROOT_FOLDER = ORDNER[os.environ.get("TK_PLAN", "u12")]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def sh(*args, **kw):
    return subprocess.run(list(args), capture_output=True, text=True, **kw)


def ordner(fid):
    page = sh("curl", "-sL", "-m", "40", f"https://drive.google.com/embeddedfolderview?id={fid}").stdout
    out = []
    for href, name in re.findall(r'<a href="([^"]+)"[^>]*>.*?<div class="flip-entry-title">(.*?)</div>', page, re.S):
        m = re.search(r"/folders/([^/?]+)", href) or re.search(r"/d/([^/?]+)", href)
        out.append((html.unescape(name), m.group(1) if m else href, "/folders/" in href))
    return out


def liste():
    wochen = {}
    for name, fid, is_dir in ordner(ROOT_FOLDER):
        if is_dir:
            wochen[name] = ordner(fid)
    return wochen


def uebungen(dateien):
    """Video und PDF mit gleichem Namen gehören zusammen."""
    paare = {}
    for name, fid, _ in dateien:
        stamm, ext = os.path.splitext(name)
        paare.setdefault(stamm, {})[ext.lower().lstrip(".")] = fid
    return paare


def laden(fid, ziel):
    if os.path.exists(ziel) and os.path.getsize(ziel) > 1000:
        return
    sh("curl", "-sL", "-m", "600", "-o", ziel,
       f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t")


def holen(woche):
    w = liste()
    if woche not in w:
        sys.exit("Woche nicht gefunden. Vorhanden: " + ", ".join(w))
    for stamm, f in uebungen(w[woche]).items():
        d = os.path.join("import", woche, re.sub(r"[^\w\- ]", "", stamm).strip())
        os.makedirs(d, exist_ok=True)
        if "pdf" in f:
            p = os.path.join(d, "quelle.pdf")
            laden(f["pdf"], p)
            open(os.path.join(d, "text.txt"), "w").write(re.sub(r"[ \t]{2,}", " ", sh("pdftotext", "-layout", p, "-").stdout))
            sh("pdftoppm", "-r", "50", "-png", p, os.path.join(d, "pdf"))
        if "mp4" in f:
            v = os.path.join(d, "video.mp4")
            laden(f["mp4"], v)
            dur = float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v).stdout.strip() or 60)
            sh("ffmpeg", "-v", "error", "-y", "-i", v, "-vf", f"fps={25 / dur:.4f},scale=400:-2,tile=5x5", "-frames:v", "1", os.path.join(d, "uebersicht.png"))
            sh("ffmpeg", "-v", "error", "-y", "-t", "25", "-i", v, "-vf", "fps=1,scale=400:-2,tile=5x5", "-frames:v", "1", os.path.join(d, "anfang.png"))
        print("fertig:", d, "| Dateien:", ", ".join(sorted(os.listdir(d))))


def einheiten(pfad):
    data = json.load(open(pfad))
    return data, (data if isinstance(data, list) else [data])


def pruefen(pfad, fix):
    import linienpruefung as lp
    data, units = einheiten(pfad)
    n = 0
    for u in units:
        for i in lp.check_unit(u, fix):
            n += 1
            print(f"{i['name']} | Schritt {i['step']} '{i['label']}' | {i['who']} ({i['type']}) bend {i['bend']}"
                  + (f" -> {i.get('fix_bend')}" if fix else "") + f" | {i['hits']}")
    if fix:
        json.dump(data, open(pfad, "w"), ensure_ascii=False, indent=1)
    rest = sum(len(lp.check_unit(copy.deepcopy(u))) for u in units)
    print(f"{n} Treffer{' bearbeitet' if fix else ''}, Rest: {rest}")
    import regeln
    hinweise = [h for u in units for h in regeln.regeln(u)]
    for h in hinweise:
        print("Regel:", h)
    print(f"Regeln: {len(hinweise)} Hinweise")


def svg(board, titel):
    import linienpruefung as lp
    o = [f'<div><h3 style="margin:6px 4px;font:600 15px sans-serif">{html.escape(titel)}</h3><svg viewBox="0 0 1000 600" width="620" style="background:#1d3b2a">']
    for l in board.get("lines") or []:
        t = l.get("type")
        if t == "rect" and l.get("w"):
            o.append(f'<rect x="{l["x"]*10}" y="{l["y"]*10}" width="{l["w"]*10}" height="{l["h"]*10}" fill="none" stroke="#fff9" stroke-width="3"/>')
        elif t == "zone" and l.get("w"):
            o.append(f'<rect x="{l["x"]*10}" y="{l["y"]*10}" width="{l["w"]*10}" height="{l["h"]*10}" fill="{"#ff550050" if l.get("color") == "orange" else "#d4ff0030"}"/>')
        elif t == "circle" and l.get("r"):
            o.append(f'<circle cx="{l["x"]*10}" cy="{l["y"]*10}" r="{l["r"]*10}" fill="none" stroke="#fff9" stroke-width="3"/>')
        elif t == "line" and l.get("x1") is not None:
            dash = ' stroke-dasharray="12 10"' if l.get("dashed") else ""
            o.append(f'<path d="M{l["x1"]*10},{l["y1"]*10} L{l["x2"]*10},{l["y2"]*10}" stroke="#fff7" stroke-width="3"{dash}/>')
    for g in board.get("goals") or []:
        o.append(f'<path d="{goal(g)}" fill="none" stroke="#ff7a1a" stroke-width="6"/>')
    pos, kind, cones = lp.objects(board)
    for si, st in enumerate(board.get("steps") or []):
        for m in st.get("moves") or []:
            f = m["from"] if m.get("from") and len(m["from"]) == 2 else pos.get(m.get("who"))
            t = m.get("to")
            if not f or not t:
                continue
            if m.get("type") == "dreh":
                # Aufdrehen: Drehpfeil um den Spieler
                import math
                s = -1 if (m.get("bend") or 0) < 0 else 1; th = math.atan2(t[1] - f[1], t[0] - f[0]); R = 40
                a0, a1 = th - s * math.radians(200), th - s * math.radians(25)
                q0 = (f[0] * 10 + R * math.cos(a0), f[1] * 10 + R * math.sin(a0)); q1 = (f[0] * 10 + R * math.cos(a1), f[1] * 10 + R * math.sin(a1))
                o.append(f'<path d="M{q0[0]:.1f},{q0[1]:.1f} A{R},{R} 0 0 {1 if s > 0 else 0} {q1[0]:.1f},{q1[1]:.1f}" fill="none" stroke="#d4ff00" stroke-width="6"/>'
                         f'<circle cx="{q1[0]:.1f}" cy="{q1[1]:.1f}" r="8" fill="#d4ff00"/>')
                continue
            if m.get("type") == "option":
                # Anspielstation: dünne gestrichelte Linie, niemand bewegt sich
                o.append(f'<path d="M{f[0]*10},{f[1]*10} L{t[0]*10},{t[1]*10}" fill="none" stroke="#d4ff00" stroke-width="2.5" stroke-dasharray="6 6" opacity=".8"/>')
                continue
            if m.get("type") == "blick":
                # Schulterblick: halbtransparenter Kegel, der Spieler bleibt stehen
                import math
                L = math.hypot(t[0] - f[0], t[1] - f[1]) * 10; h = math.radians((m.get("weite") or 70) / 2); th = math.atan2(t[1] - f[1], t[0] - f[0])
                p1 = (f[0] * 10 + L * math.cos(th - h), f[1] * 10 + L * math.sin(th - h)); p2 = (f[0] * 10 + L * math.cos(th + h), f[1] * 10 + L * math.sin(th + h))
                o.append(f'<path d="M{f[0]*10},{f[1]*10} L{p1[0]:.1f},{p1[1]:.1f} A{L:.1f},{L:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f} Z" fill="#d4ff0040" stroke="#d4ff00" stroke-width="3"/>'
                         f'<text x="{(f[0]+t[0])*5}" y="{(f[1]+t[1])*5-8}" fill="#fff" font-size="22" font-family="sans-serif">{si+1}</text>')
                continue
            c = lp.ctrl(f, t, m.get("bend") or 0)
            col = {"pass": "#fff", "lauf": "#ffe14d", "dribbling": "#7df"}.get(m.get("type"), "#f0f")
            dash = ' stroke-dasharray="14 9"' if m.get("type") == "lauf" else ""
            o.append(f'<path d="M{f[0]*10},{f[1]*10} Q{c[0]*10},{c[1]*10} {t[0]*10},{t[1]*10}" fill="none" stroke="{col}" stroke-width="4"{dash}/>'
                     f'<text x="{(f[0]+t[0])*5}" y="{(f[1]+t[1])*5-8}" fill="#fff" font-size="22" font-family="sans-serif">{si+1}</text>')
            pos[m["who"]] = t
            if m.get("ball"):
                pos[m["ball"]] = t
    for c in board.get("cones") or []:
        x, y = c["x"] * 10, c["y"] * 10
        col = "#c6ff3d" if c.get("color") == "neon" else "#ff7a1a"
        if str(c.get("shape", "")).startswith("leiter"):
            rot = ' transform="rotate(90 %s %s)"' % (x, y) if c.get("shape") == "leiter_ou" else ""
            o.append(f'<g{rot}>' + "".join(f'<rect x="{x+dx-3}" y="{y-21}" width="7" height="42" fill="{col}" stroke="#000"/>' for dx in (-64, -32, 0, 32, 64))
                     + f'<rect x="{x-80}" y="{y-27}" width="160" height="8" fill="{col}" stroke="#000"/><rect x="{x-80}" y="{y+19}" width="160" height="8" fill="{col}" stroke="#000"/></g>')
            continue
        if c.get("shape") == "ring":
            o.append(f'<circle cx="{x}" cy="{y}" r="19" fill="none" stroke="{col}" stroke-width="8"/>')
            continue
        if str(c.get("shape", "")).startswith("huerde"):
            rot = ' transform="rotate(90 %s %s)"' % (x, y) if c.get("shape") == "huerde" else ""
            o.append(f'<g{rot}><rect x="{x-24}" y="{y-9}" width="9" height="18" fill="{col}"/><rect x="{x+15}" y="{y-9}" width="9" height="18" fill="{col}"/>'
                     f'<rect x="{x-22}" y="{y-4}" width="44" height="8" fill="{col}" stroke="#000"/></g>')
            continue
        o.append(f'<rect x="{x-5}" y="{y-26}" width="10" height="34" fill="{col}"/>' if c.get("shape") == "stange"
                 else f'<path d="M{x-12},{y+10} L{x},{y-14} L{x+12},{y+10}Z" fill="{col}"/>')
    for p in board.get("players") or []:
        col = {"a": "#c6ff3d", "b": "#ff5a3a", "t": "#eee", "c": "#fff"}.get(p.get("team"), "#999")
        o.append(f'<circle cx="{p["x"]*10}" cy="{p["y"]*10}" r="23" fill="{col}" stroke="#000" stroke-width="2"/>'
                 f'<text x="{p["x"]*10}" y="{p["y"]*10+8}" text-anchor="middle" font-size="22" font-family="sans-serif">{html.escape(str(p.get("label","")))}</text>')
    for b in board.get("balls") or []:
        o.append(f'<circle cx="{b["x"]*10}" cy="{b["y"]*10}" r="9" fill="#fff" stroke="#000" stroke-width="2"/>')
    for t in board.get("labels") or []:
        o.append(f'<text x="{t["x"]*10}" y="{t["y"]*10}" text-anchor="middle" fill="#d4ff00" font-size="22" font-family="sans-serif">{html.escape(t["text"])}</text>')
    o.append("</svg></div>")
    return "".join(o)


def goal(g):
    # Minitor (Standard), Jugendtor (size "jugend") oder Großfeldtor (size "gross"), wie TOR_MASS in der App (Sketch.jsx)
    w, d = {"jugend": (70, 45), "gross": (100, 55)}.get(g.get("size"), (40, 32))
    x, y = g["x"] * 10, g["y"] * 10
    return {"left": f"M{x},{y-w} h{-d} v{2*w} h{d}", "right": f"M{x},{y-w} h{d} v{2*w} h{-d}",
            "top": f"M{x-w},{y} v{-d} h{2*w} v{d}"}.get(g.get("side"), f"M{x-w},{y} v{d} h{2*w} v{-d}")


def bild(pfad):
    import linienpruefung as lp
    _, units = einheiten(pfad)
    teile = []
    for u in units:
        teile.append(svg(u["board"], f'{u.get("code","")} Grundform'))
        for v in u.get("versions") or []:
            teile.append(svg(lp.merge(u["board"], v.get("board")), f'{u.get("code","")} {v.get("label","")}: {v.get("title","")}'))
    h = pfad.rsplit(".", 1)[0] + ".html"
    open(h, "w").write('<html><body style="margin:0;display:grid;grid-template-columns:1fr 1fr">' + "".join(teile) + "</body></html>")
    js = h + ".js"
    open(js, "w").write("const { chromium } = require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1260,height:800}});"
                        f"await p.goto('file://{os.path.abspath(h)}');await p.screenshot({{path:'{os.path.abspath(pfad.rsplit('.',1)[0]+'.png')}',fullPage:true}});await b.close();}})();")
    print(sh("node", js).stderr or ("Kontrollbild: " + pfad.rsplit(".", 1)[0] + ".png"))


# ---------- Näherung der 3D-Ansicht (Scroll-Story der Einheiten-Seite) ----------
CSS3D = """
:root{--neon:#d4ff00;--cone:#ff5500;--ink:#0d0d0b;--paper:#f8f4e9;--fiber:#efe9d8}
body{margin:0;background:#11140d}
.pin{position:relative;width:1000px;height:560px;overflow:hidden;background:#11140d}
.scene{position:absolute;inset:0;perspective:1700px;perspective-origin:50% 30%}
.plane{position:absolute;left:50%;top:50%;width:1000px;height:600px;transform-style:preserve-3d}
.plane-turf{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.plane-turf .f{fill:#11140d;stroke:#0a0b08;stroke-width:16}
.plane-turf .l{fill:none;stroke:#ece5d3;stroke-width:6}.plane-turf .l.dash{stroke-dasharray:18 16;opacity:.75}
.plane-turf .z{fill:#d4ff00;opacity:.16}.plane-turf .g{fill:none;stroke:#d4ff00;stroke-width:10}
.plane-turf .dm{fill:none;stroke:#d4ff00;stroke-width:4;stroke-dasharray:14 10}
.plane-turf .dt{fill:#d4ff00;font:800 34px sans-serif;text-anchor:middle}
.plane-turf .lb{font:800 19px sans-serif;letter-spacing:.14em;fill:#ece5d3;opacity:.75;text-anchor:middle}
.tok{position:absolute;left:0;top:0;width:0;height:0;transform-style:preserve-3d;--up:1;--bib:var(--paper)}
.tok.t-a{--bib:var(--neon)}.tok.t-b{--bib:var(--cone)}.tok.t-c{--bib:var(--ink)}
.tok .up{position:absolute;transform-origin:50% 100%;transform:rotateX(calc(var(--up) * -90deg))}
.tok .up svg{display:block;width:100%;height:100%;overflow:visible}
.tok.fig .up{left:-43px;top:-143px;width:86px;height:143px}.tok.fig.t-c .up{left:-49px;top:-163px;width:98px;height:163px}
.tok.cone .up{left:-22px;top:-52px;width:44px;height:52px}.tok.cone.pole .up{left:-14px;top:-80px;width:28px;height:80px}.tok.cone.hurdle .up{left:-30px;top:-36px;width:60px;height:36px}
.tok.ball .up{left:-14px;top:-29px;width:28px;height:28px}
.tok .disc{position:absolute;left:-27px;top:-15px;width:54px;height:30px;border-radius:50%;background:var(--bib);box-shadow:0 0 0 3px var(--ink)}
.tok.t-c .disc{box-shadow:0 0 0 3px var(--neon)}.tok.ball .disc{left:-13px;top:-5px;width:26px;height:11px;background:rgba(0,0,0,.6);box-shadow:none}
.tok.cone .disc{display:none}
.plane.gross .tok.fig .up{left:-31px;top:-103px;width:62px;height:103px}.plane.gross .tok.fig.t-c .up{left:-35px;top:-117px;width:70px;height:117px}
.plane.gross .tok .disc{left:-19px;top:-11px;width:38px;height:22px}.plane.gross .tok.cone:not(.goal):not(.flat):not(.pole):not(.hurdle) .up{left:-16px;top:-37px;width:32px;height:37px}
.plane.gross .tok.ball .up{left:-10px;top:-21px;width:20px;height:20px}.plane.gross .tok.ball .disc{left:-9px;top:-4px;width:19px;height:8px}
.tok .cut{fill:var(--fiber);stroke:var(--fiber);stroke-width:8;stroke-linejoin:round}
.tok .leg{fill:var(--paper);stroke:var(--ink);stroke-width:2.2}.tok .shoe,.tok .short,.tok .dot{fill:var(--ink)}
.tok .bib{fill:var(--bib);stroke:var(--ink);stroke-width:2.6}.tok .head{fill:var(--paper);stroke:var(--ink);stroke-width:2.6}
.tok text{font:900 17px sans-serif;fill:var(--ink);text-anchor:middle}.tok.t-c text{fill:var(--neon);font-size:20px}
.tok .cone{fill:var(--cone);stroke:var(--ink);stroke-width:2.2}.tok.neon .cone{fill:var(--neon)}
.tok .band{fill:var(--fiber)}.tok .ball{fill:var(--fiber);stroke:var(--ink);stroke-width:2.4}
h3{position:absolute;margin:6px 10px;font:600 15px sans-serif;color:#fff;z-index:2}
"""
FIG = ('<svg viewBox="0 0 60 100"><g class="cut"><circle cx="30" cy="15" r="10"/><path d="M19,28 Q30,33 41,28 L51,40 L44,46 L42,43 V72 H39 V90 H45 V96 H15 V90 H21 V72 H18 V43 L16,46 L9,40 Z"/></g>'
       '<path class="leg" d="M21,70 h7 v21 h-7 z M32,70 h7 v21 h-7 z"/><path class="shoe" d="M16,90 h13 v6 h-13 z M31,90 h13 v6 h-13 z"/>'
       '<path class="short" d="M18,57 h24 v16 h-10 l-2,-7 l-2,7 h-10 z"/><path class="bib" d="M19,28 Q30,33 41,28 L51,40 L44,46 L42,43 V60 H18 V43 L16,46 L9,40 Z"/>'
       '<circle class="head" cx="30" cy="15" r="10"/><text x="30" y="53">%s</text></svg>')
BALL = '<svg viewBox="0 0 24 24"><circle class="ball" cx="12" cy="12" r="10"/><path class="dot" d="M12,7.5 L16,10.5 L14.5,15.5 H9.5 L8,10.5 Z"/></svg>'
HURDLE = ('<svg viewBox="0 0 60 36"><path class="cut" d="M4,30 H20 V35 H4 Z M40,30 H56 V35 H40 Z M9,8 H15 V31 H9 Z M45,8 H51 V31 H45 Z M5,6 Q5,3 8,3 H52 Q55,3 55,6 V11 Q55,13 52,13 H8 Q5,13 5,11 Z"/>'
          '<path class="cone" d="M9,8 H15 V31 H9 Z M45,8 H51 V31 H45 Z M4,30 H20 V35 H4 Z M40,30 H56 V35 H40 Z"/>'
          '<path class="cone" d="M5,6 Q5,3 8,3 H52 Q55,3 55,6 V11 Q55,13 52,13 H8 Q5,13 5,11 Z"/><path class="band" d="M18,4.5 H25 V11.5 H18 Z M35,4.5 H42 V11.5 H35 Z"/></svg>')
CONE = ('<svg viewBox="0 0 34 40"><path class="cut" d="M4,34 H30 V39 H4 Z M10,34 L15,5 Q17,2 19,5 L24,34 Z"/><path class="cone" d="M10,34 L15,5 Q17,2 19,5 L24,34 Z"/>'
        '<path class="band" d="M12.6,19 H21.4 L22.4,25 H11.6 Z"/><path class="cone" d="M4,34 H30 V39 H4 Z"/></svg>')


def html3d(board, titel):
    import math
    b = board
    K = 10
    o = ['<svg class="plane-turf" viewBox="0 0 1000 600"><rect class="f" width="1000" height="600"/>']
    for l in b.get("lines") or []:
        t = l.get("type")
        if t == "rect" and l.get("w"):
            o.append(f'<rect class="l" x="{l["x"]*K}" y="{l["y"]*K}" width="{l["w"]*K}" height="{l["h"]*K}"/>')
        elif t == "zone" and l.get("w"):
            o.append(f'<rect class="z" style="{"fill:#ff5500" if l.get("color") == "orange" else ""}" x="{l["x"]*K}" y="{l["y"]*K}" width="{l["w"]*K}" height="{l["h"]*K}"/>')
        elif t == "circle" and l.get("r"):
            o.append(f'<circle class="l" cx="{l["x"]*K}" cy="{l["y"]*K}" r="{l["r"]*K}"/>')
        elif t == "line" and l.get("x1") is not None:
            o.append(f'<path class="l{" dash" if l.get("dashed") else ""}" d="M{l["x1"]*K},{l["y1"]*K} L{l["x2"]*K},{l["y2"]*K}"/>')
    for g in b.get("goals") or []:
        o.append(f'<path class="g" d="{goal(g)}"/>')
    for m in b.get("dims") or []:
        x1, y1, x2, y2 = [m[k] * K for k in ("x1", "y1", "x2", "y2")]
        o.append(f'<path class="dm" d="M{x1},{y1} L{x2},{y2}"/><text class="dt" x="{(x1+x2)/2}" y="{(y1+y2)/2+9}">{html.escape(m["text"])}</text>')
    for t in b.get("labels") or []:
        o.append(f'<text class="lb" x="{t["x"]*K}" y="{t["y"]*K}">{html.escape(t["text"])}</text>')
    o.append("</svg>")
    for c in b.get("cones") or []:
        hu = str(c.get("shape", "")).startswith("huerde")
        sh = c.get("shape", "")
        if sh in ("leiter", "leiter_ou", "ring"):
            # Leiter und Ring liegen flach auf dem Rasen (wie in der App: kein Hochklappen)
            col = "#d4ff00" if c.get("color") == "neon" else "#ff5500"
            w, h = (160, 54) if sh != "ring" else (48, 48)
            rot = "rotate(90deg)" if sh == "leiter_ou" else ""
            inner = ("".join(f'<rect x="{dx}" y="8" width="7" height="38" fill="{col}" stroke="#000" stroke-width="2"/>' for dx in (14, 46, 77, 108, 139))
                     + f'<rect x="2" y="2" width="156" height="8" fill="{col}" stroke="#000" stroke-width="2"/><rect x="2" y="44" width="156" height="8" fill="{col}" stroke="#000" stroke-width="2"/>'
                     if sh != "ring" else f'<circle cx="24" cy="24" r="19" fill="none" stroke="{col}" stroke-width="8"/>')
            o.append(f'<div style="position:absolute;left:0;top:0;transform:translate3d({c["x"]*K}px,{c["y"]*K}px,1px)"><svg style="position:absolute;left:{-w/2}px;top:{-h/2}px;transform:{rot}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg></div>')
            continue
        cls = "tok cone" + (" neon" if c.get("color") == "neon" else "") + (" hurdle" if hu else "")
        o.append(f'<div class="{cls}" style="transform:translate3d({c["x"]*K}px,{c["y"]*K}px,0)"><div class="up">{HURDLE if hu else CONE}</div></div>')
    for p in b.get("balls") or []:
        o.append(f'<div class="tok ball" style="transform:translate3d({p["x"]*K}px,{p["y"]*K}px,0)"><i class="disc"></i><div class="up">{BALL}</div></div>')
    for p in b.get("players") or []:
        o.append(f'<div class="tok fig t-{p.get("team","t")}" style="transform:translate3d({p["x"]*K}px,{p["y"]*K}px,0)"><i class="disc"></i><div class="up">{FIG % html.escape(str(p.get("label","")))}</div></div>')
    W, H = 1000, 560
    sc = min(W * 0.88 / 1000, H * 0.84 / (600 * math.cos(math.radians(52)) + 190))
    return (f'<html><head><meta charset="utf-8"><style>{CSS3D}</style></head><body><div class="pin"><h3>{html.escape(titel)}</h3><div class="scene">'
            f'<div class="plane{" gross" if b.get("massstab") == "gross" else ""}" style="transform:translate(-50%,-50%) translateY(7%) scale({sc:.4f}) rotateX(52deg)">{"".join(o)}</div></div></div></body></html>')


def bild3d(pfad):
    import linienpruefung as lp
    _, units = einheiten(pfad)
    base = pfad.rsplit(".", 1)[0]
    boards = []
    for u in units:
        boards.append((f'{u.get("code","")} Grundform', u["board"], f'{u.get("code","")}-1'))
        for i, v in enumerate(u.get("versions") or []):
            boards.append((f'{u.get("code","")} {v.get("label","")}: {v.get("title","")}', lp.merge(u["board"], v.get("board")), f'{u.get("code","")}-{i+2}'))
    js = [f"const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1000,height:560}}}});"]
    for titel, bd, key in boards:
        h = f"{base}-3d-{key}.html"
        open(h, "w").write(html3d(bd, titel))
        js.append(f"await p.goto('file://{os.path.abspath(h)}');await p.screenshot({{path:'{os.path.abspath(f'{base}-3d-{key}.png')}'}});")
    js.append("await b.close();})();")
    jsf = base + "-3d.js"
    open(jsf, "w").write("".join(js))
    print(sh("node", jsf).stderr or ("3D-Kontrollbilder: " + ", ".join(f"{base}-3d-{k}.png" for _, _, k in boards)))


def _diff(a, b, pfad, out):
    if isinstance(a, dict):
        for k, v in a.items():
            if v is None:
                continue  # null und fehlend sind gleich
            if not isinstance(b, dict) or k not in b:
                out.append(f"{pfad}.{k}: fehlt in der Datenbank")
            else:
                _diff(v, b[k], f"{pfad}.{k}", out)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            out.append(f"{pfad}: Liste hat {len(a)} Einträge, in der Datenbank {len(b) if isinstance(b, list) else 'keine'}")
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                _diff(x, y, f"{pfad}[{i}]", out)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if abs(a - b) > 1e-9:
            out.append(f"{pfad}: {a} in der Datei, {b} in der Datenbank")
    elif a != b:
        out.append(f"{pfad}: '{str(a)[:40]}' in der Datei, '{str(b)[:40]}' in der Datenbank")


def vergleichen(datei, gelesen):
    _, units = einheiten(datei)
    raw = json.load(open(gelesen))
    db = raw.get("entities", raw) if isinstance(raw, dict) else raw
    db = db if isinstance(db, list) else [db]
    by = {u.get("code"): u for u in db}
    n = 0
    for u in units:
        out = []
        if u.get("code") not in by:
            print(f"{u.get('code')}: nicht in der Datenbank gefunden")
            n += 1
            continue
        _diff({k: v for k, v in u.items() if k != "audio"}, by[u["code"]], u["code"], out)
        for o in out:
            print("ABWEICHUNG:", o)
        n += len(out)
    print(f"Vergleich: {n} Abweichungen")


def szene(ordner, start, ende, fps="2"):
    """Bilder aus einem Abschnitt des Videos (Sekunden), 4 x 4 auf einem Blatt: für Laufwege, die in der Übersicht nicht zu erkennen sind."""
    v = os.path.join(ordner, "video.mp4")
    out = os.path.join(ordner, f"szene-{start}-{ende}.png")
    r = sh("ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(float(ende) - float(start)), "-i", v,
           "-vf", f"fps={fps},scale=500:-2,tile=4x4", "-frames:v", "1", out)
    print(r.stderr or f"Szene: {out}")


def dauer(ordner):
    v = os.path.join(ordner, "video.mp4")
    print(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v).stdout.strip(), "Sekunden")


# ---------- Schnellweg (Stand 21.11.2026): wenig Tokens, alles geprüft ----------
APP = "6afec076c6c4a55a7cb4995e"
META = ("id", "created_date", "updated_date", "created_by_id", "created_by", "is_sample")


def lesen(codes, ziel):
    """Einheiten über die öffentliche Leseschnittstelle holen (kostet keine Tokens), ohne Metafelder."""
    import urllib.parse
    q = urllib.parse.quote(json.dumps({"code": {"$in": codes}}))
    data = json.loads(sh("curl", "-s", "-m", "40", f"https://app.base44.com/api/apps/{APP}/entities/Einheit?q={q}").stdout or "[]")
    data = sorted(data, key=lambda u: u.get("code", ""))
    ids = {u["code"]: u.get("id") for u in data}
    for u in data:
        for k in META:
            u.pop(k, None)
    json.dump(data if len(data) != 1 else data[0], open(ziel, "w"), ensure_ascii=False, indent=1)
    print(f"gelesen: {', '.join(f'{c} ({i})' for c, i in ids.items()) or 'nichts'} -> {ziel}")


def _patch(a, b, pfad, out):
    """kleinste $set-Liste, die a (Datenbank) in b (Datei) verwandelt"""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in b:  # nur was in der neuen Datei steht; fehlende Felder gelten als unverändert
            if k in META or k == "audio" or (b[k] is None and a.get(k) in (None, [], "")):
                continue
            _patch(a.get(k), b.get(k), f"{pfad}.{k}" if pfad else k, out)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b) and a and isinstance(a[0], (dict, list)):
        for i, (x, y) in enumerate(zip(a, b)):
            _patch(x, y, f"{pfad}.{i}", out)
    elif a != b and not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) < 1e-9):
        out[pfad] = b


def patch(alt, neu):
    """Druckt das update_entities-Datenfeld {"$set": {...}} mit nur den geänderten Stellen (Pfade wie versions.1.board.steps.0.moves.2.to)."""
    a, b = json.load(open(alt)), json.load(open(neu))
    out = {}
    _patch(a, b, "", out)
    print(json.dumps({"$set": out}, ensure_ascii=False, separators=(",", ":")) if out else "keine Änderung")


def blatt(pfad):
    """Ein einziges Kontrollbild: oben 2D-Tafeln mit Laufwegen, darunter die 3D-Näherung jeder Tafel (spart Bildaufrufe)."""
    bild(pfad)
    bild3d(pfad)
    base = pfad.rsplit(".", 1)[0]
    import glob
    d3 = sorted(glob.glob(base + "-3d-*.png"))
    html = (f'<html><body style="margin:0;background:#fff"><img src="file://{os.path.abspath(base + ".png")}" style="width:1260px;display:block">'
            + "".join(f'<img src="file://{os.path.abspath(f)}" style="width:415px">' for f in d3) + "</body></html>")
    h = base + "-blatt.html"
    open(h, "w").write(html)
    js = h + ".js"
    open(js, "w").write("const { chromium } = require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1260,height:800}});"
                        f"await p.goto('file://{os.path.abspath(h)}');await p.waitForTimeout(300);await p.screenshot({{path:'{os.path.abspath(base + '-blatt.png')}',fullPage:true}});await b.close();}})();")
    print(sh("node", js).stderr or ("Blatt: " + base + "-blatt.png"))


# Die PDFs enthalten keine Altersstufen, Dauer oder Spielerzahl. Feste Regel, damit alle Einheiten einheitlich sind (vom Inhaber änderbar):
VORGABEN = [
    ("Mini Ballers", ["Bambini", "F-Jugend"], 10),
    ("Warm Up", ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], 10),
    ("WU-", ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], 10),
    ("BM-", ["E-Jugend", "D-Jugend", "C-Jugend"], 12),
    ("Ball Mastery", ["E-Jugend", "D-Jugend", "C-Jugend"], 12),
    ("", ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], 15),
]


def vorgaben(name):
    for key, ages, mins in VORGABEN:
        if key in name:
            print(json.dumps({"age_groups": ages, "duration_minutes": mins}, ensure_ascii=False))
            return



def ton(ordner, modell="small.en"):
    """Tonspur des Videos als Text mit Zeitstempeln (Spracherkennung, läuft lokal): <Ordner>/ton.txt.
    Der Sprecher erklärt im Video Ablauf, Laufwege und Coaching-Punkte. Zuerst ton.txt lesen, dann nur die nötigen Szenen ansehen.
    Einmalig: pip install faster-whisper (lädt beim ersten Lauf das Modell, ca. 500 MB)."""
    from faster_whisper import WhisperModel
    v = os.path.join(ordner, "video.mp4")
    m = WhisperModel(modell, device="cpu", compute_type="int8")
    import numpy as np  # Ton mit ffmpeg auslesen (16 kHz mono), nicht über PyAV: dessen Version passt oft nicht
    roh = subprocess.run(["ffmpeg", "-v", "error", "-i", v, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(roh, np.int16).astype(np.float32) / 32768.0, beam_size=1, vad_filter=True)
    zeilen = [f"[{int(x.start)//60}:{int(x.start)%60:02d}-{int(x.end)//60}:{int(x.end)%60:02d}] {x.text.strip()}" for x in segs]
    open(os.path.join(ordner, "ton.txt"), "w").write("\n".join(zeilen) + "\n")
    print(f"Ton: {os.path.join(ordner, 'ton.txt')} ({len(zeilen)} Sätze)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "liste":
        for w, d in liste().items():
            print(w, "|", " ; ".join(uebungen(d)))
    elif cmd == "holen":
        holen(sys.argv[2])
    elif cmd == "pruefen":
        pruefen(sys.argv[2], "--fix" in sys.argv)
    elif cmd == "bild":
        bild(sys.argv[2])
    elif cmd == "bild3d":
        bild3d(sys.argv[2])
    elif cmd == "vergleichen":
        vergleichen(sys.argv[2], sys.argv[3])
    elif cmd == "szene":
        szene(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "2")
    elif cmd == "dauer":
        dauer(sys.argv[2])
    elif cmd == "lesen":
        lesen(sys.argv[2:-1], sys.argv[-1])
    elif cmd == "patch":
        patch(sys.argv[2], sys.argv[3])
    elif cmd == "blatt":
        blatt(sys.argv[2])
    elif cmd == "ton":
        ton(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "small.en")
    elif cmd == "vorgaben":
        vorgaben(" ".join(sys.argv[2:]))
    else:
        print(open(__file__).read().split("import copy")[0])
