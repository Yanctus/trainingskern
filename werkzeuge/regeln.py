# Regelprüfung für neue Einheiten: alles, was am Rezept (README "Merkzettel: Übungen aus Video nachbauen") prüfbar ist.
# Läuft über `python3 werkbank.py pruefen datei.json` mit. Jeder Hinweis wird behoben oder im Bericht an den Inhaber begründet.
# Die Hinweise kommen aus echten Fehlern: überlappende Figuren in der 3D-Ansicht, Maßlinien unter Figuren, Zahlen im Sprechtext.
import math, re
import linienpruefung as lp

KINDS = {"Übungsform", "Spielform"}
FOCUSES = {"Dribbling", "Passspiel", "Ballannahme", "Torschuss", "1 gegen 1", "Zusammenspiel", "Umschalten", "Verteidigen",
           "Koordination", "Bewegung", "Schnelligkeit", "Kondition", "Erwärmung"}
AGES = {"Bambini", "F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend", "A-Jugend", "Amateure"}
MOVES = {"pass", "lauf", "dribbling", "blick"}  # blick = Schulterblick (Kegel, bewegt niemanden)
SAY_START = re.compile(r"^(Jetzt zum Coaching-Punkt|Der zweite Coaching-Punkt|Der dritte Coaching-Punkt|Und jetzt die (zweite |dritte )?Steigerung|Und jetzt das Umschalten)")


def dist_seg(p, a, b):
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if not L else max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L))
    return math.hypot(p[0] - (ax + t * dx), p[1] - (ay + t * dy))


# Felder, die das Entity-Schema (base44/entities/Einheit.jsonc) kennt. Alles andere löscht die Datenbank beim nächsten Speichern der Einheit
# stillschweigend, z. B. wenn der Inhaber die Stimme einspricht (UE-053: die ids der geworfenen Hütchen waren weg, nichts flog mehr).
# Neues Feld an der Tafel? Erst im Schema anlegen, dann benutzen.
ERLAUBT = {
    "lines": {"type", "dashed", "color", "x", "y", "w", "h", "x1", "y1", "x2", "y2", "r"}, "players": {"id", "team", "x", "y", "label"},
    "cones": {"x", "y", "color", "shape", "id"}, "goals": {"x", "y", "side", "size"}, "balls": {"id", "x", "y"}, "arrows": {"from", "to", "type", "bend"},
    "labels": {"x", "y", "text"}, "steps": {"label", "say", "moves"}, "dims": {"x1", "y1", "x2", "y2", "text"},
}
ERLAUBT_MOVE = {"who", "ball", "to", "from", "type", "bend", "delay", "after", "weite", "dauer"}
ERLAUBT_BOARD = set(ERLAUBT) | {"sketch_steps"}
ERLAUBT_UNIT = {"title", "code", "kind", "focuses", "age_groups", "altersbereiche", "zeit", "aufrufe", "duration_minutes", "players_min", "players_max", "field_size", "description",
                "organisation", "organisation_show", "coaching_points", "progression", "materials", "access", "hidden", "board", "say_intro",
                "versions", "audio", "id", "created_date", "updated_date", "created_by_id", "created_by", "is_sample"}
ERLAUBT_VERSION = {"label", "say", "title", "text", "board"}


def schema_regeln(b, name):
    out = []
    for k in b:
        if k not in ERLAUBT_BOARD:
            out.append(f"{name}: Tafel-Feld '{k}' steht nicht im Schema und geht beim Speichern verloren")
    for key, allowed in ERLAUBT.items():
        for it in b.get(key) or []:
            extra = set(it) - allowed
            if extra:
                out.append(f"{name}: {key}: Feld {sorted(extra)} steht nicht im Schema und geht beim Speichern verloren")
            if key == "steps":
                for m in it.get("moves") or []:
                    extra = set(m) - ERLAUBT_MOVE
                    if extra:
                        out.append(f"{name}: Schritt-Bewegung: Feld {sorted(extra)} steht nicht im Schema")
    return out


def board_regeln(b, name, fassung):
    out = schema_regeln(b, name)
    pl, ba, co = b.get("players") or [], b.get("balls") or [], b.get("cones") or []
    # Kennungen eindeutig, jeder Schritt zeigt auf etwas, das es gibt
    ids = [p.get("id") for p in pl] + [x.get("id") for x in ba] + [c.get("id") for c in co if c.get("id")]
    if None in ids[:len(pl) + len(ba)]:
        out.append(f"{name}: Spieler und Bälle brauchen eine id")
    dup = {i for i in ids if i and ids.count(i) > 1}
    if dup:
        out.append(f"{name}: doppelte ids {sorted(dup)}")
    for si, st in enumerate(b.get("steps") or []):
        if not st.get("label") or not st.get("say"):
            out.append(f"{name}: Schritt {si + 1} braucht label und say")
        for m in st.get("moves") or []:
            for key in ("who", "ball"):
                if m.get(key) and m[key] not in ids:
                    out.append(f"{name}: Schritt {si + 1}: {key} '{m[key]}' gibt es nicht")
            if m.get("type") not in MOVES:
                out.append(f"{name}: Schritt {si + 1}: type '{m.get('type')}' ist ungültig")
        if len(st.get("label", "")) > 48:
            out.append(f"{name}: Schritt {si + 1}: label ist zu lang für den Bildschirm ({len(st['label'])} Zeichen)")
    # Rückennummern: keine doppelten auf dem Feld (Neon und Rot), ein Trainer
    nums = [p.get("label") for p in pl if p.get("team") in ("a", "b")]
    if len(nums) != len(set(nums)):
        out.append(f"{name}: doppelte Rückennummern {sorted({n for n in nums if nums.count(n) > 1})}")
    if sum(1 for p in pl if p.get("team") == "c") != 1:
        out.append(f"{name}: genau ein Trainer (team c) nötig")
    # Alles liegt auf der Tafel
    for kind, items in (("Spieler", pl), ("Ball", ba), ("Hütchen", co)):
        for it in items:
            if not (1 <= it["x"] <= 99 and 1 <= it["y"] <= 59):
                out.append(f"{name}: {kind} {it.get('id') or it.get('label') or ''} liegt am Rand der Tafel ({it['x']}, {it['y']})")
    # 3D-Ansicht: Figuren stehen aufrecht, sind ca. 8,6 breit und erscheinen ca. 15 Einheiten tief; stehen zwei dicht beieinander, verdecken sie sich
    figs = [p for p in pl]
    for i, a in enumerate(figs):
        for c in figs[i + 1:]:
            if abs(a["x"] - c["x"]) < 8.2 and abs(a["y"] - c["y"]) < 15.5:
                out.append(f"{name}: {a.get('label')} und {c.get('label')} stehen zu dicht ({a['x']},{a['y']} / {c['x']},{c['y']}): in der 3D-Ansicht verdecken sie sich")
    # Maßlinien dürfen keine Figur berühren
    for d in b.get("dims") or []:
        for p in pl:
            if dist_seg([p["x"], p["y"]], [d["x1"], d["y1"]], [d["x2"], d["y2"]]) < 2.8:
                out.append(f"{name}: Maßlinie '{d['text']}' berührt Spieler {p.get('label')}")
        mx, my = (d["x1"] + d["x2"]) / 2, (d["y1"] + d["y2"]) / 2
        if not (0 <= mx <= 100 and 0 <= my + 1 <= 60):
            out.append(f"{name}: Maßlinie '{d['text']}' liegt außerhalb der Tafel")
    # Beschriftungen auf dem Feld: weder unter einer stehenden Figur (die verdeckt in der 3D-Ansicht alles, was bis ca. 15 Einheiten
    # hinter ihren Füßen liegt) noch auf einem Laufweg. Breite je Zeichen ca. 1,3 Einheiten (Großbuchstaben).
    pos, kind, _ = lp.objects(b)
    paths = []
    for st in b.get("steps") or []:
        for m in st.get("moves") or []:
            f = m["from"] if m.get("from") and len(m["from"]) == 2 else pos.get(m.get("who"))
            t = m.get("to")
            if f and t and m.get("type") != "blick":  # ein Blick ist kein Weg, der Spieler bleibt stehen
                paths.append((m.get("who"), lp.pts_of(f, t, m.get("bend") or 0, 40)))
                pos[m["who"]] = t
    for lb in b.get("labels") or []:
        half = 1.3 * len(lb["text"]) / 2
        x0, x1, y0, y1 = lb["x"] - half, lb["x"] + half, lb["y"] - 2.5, lb["y"] + 0.5
        for p in pl:
            if x0 - 4.3 < p["x"] < x1 + 4.3 and 0 < p["y"] - lb["y"] < 15:
                out.append(f"{name}: Beschriftung '{lb['text']}' liegt hinter Figur {p.get('label')}: sie verdeckt sie in der 3D-Ansicht")
        for who, pts in paths:
            if any(x0 - 1 < q[0] < x1 + 1 and y0 - 1 < q[1] < y1 + 1 for q in pts):
                out.append(f"{name}: Beschriftung '{lb['text']}' liegt auf dem Weg von {who}")
    # Steht im Text "Bogen" oder "herum", muss der Weg wirklich ein Bogen sein: mindestens zwei Teilstücke (Zwischenpunkte) oder eine starke Krümmung
    for si, st in enumerate(b.get("steps") or []):
        text = ((st.get("label") or "") + " " + (st.get("say") or "")).lower()
        if "bogen" in text or "herum" in text:
            legs = {}
            for m in st.get("moves") or []:
                if m.get("type") in ("lauf", "dribbling"):
                    legs.setdefault(m["who"], []).append(abs(m.get("bend") or 0))
            if legs and all(len(v) < 2 and max(v) < 3 for v in legs.values()):
                out.append(f"{name}: Schritt {si + 1} spricht von einem Bogen, der Weg ist aber fast gerade: Zwischenpunkte setzen (mehrere lauf-Teilstücke mit after: true)")
    return out


def regeln(u):
    code = u.get("code", "?")
    out = []
    for k in u:
        if k not in ERLAUBT_UNIT:
            out.append(f"{code}: Feld '{k}' steht nicht im Schema und geht beim Speichern verloren")
    for v in u.get("versions") or []:
        for k in v:
            if k not in ERLAUBT_VERSION:
                out.append(f"{code} {v.get('label', 'Fassung')}: Feld '{k}' steht nicht im Schema und geht beim Speichern verloren")
    for key in ("title", "code", "kind", "focuses", "age_groups", "duration_minutes", "players_min", "players_max", "field_size",
                "description", "organisation", "organisation_show", "coaching_points", "materials", "say_intro", "board", "versions"):
        if not u.get(key):
            out.append(f"{code}: Feld {key} fehlt oder ist leer")
    # Die Überschrift der Einheit steht groß und läuft am Handy nicht um: Ein Wort mit mehr als 14 Buchstaben (z. B. „Zweierkombination“) wird abgeschnitten
    for w in re.findall(r"[^\s:,;.–-]+", u.get("title") or ""):
        # Breite Buchstaben (M, W, Ä, Ö, Ü) zählen anderthalbfach: „RÜCKWÄRTSLAUF“ (13) wurde am Handy abgeschnitten
        if len(w) + 0.5 * sum(ch in "MWÄÖÜmwäöü" for ch in w) > 14:
            out.append(f"{code}: Wort '{w}' im Titel ist zu lang für die Überschrift am Handy (höchstens 14 Buchstaben)")
    # Kurze Titel wie bei UE-001 bis UE-030 (meist unter 30 Zeichen): kein langer Untertitel nach dem Doppelpunkt
    if len(u.get("title") or "") > 32:
        out.append(f"{code}: Titel ist zu lang ({len(u['title'])} Zeichen), höchstens 32 wie bei den ersten Übungen")
    if u.get("kind") not in KINDS:
        out.append(f"{code}: kind muss Übungsform oder Spielform sein")
    if not set(u.get("focuses") or []) <= FOCUSES or not 2 <= len(u.get("focuses") or []) <= 3:
        out.append(f"{code}: 2-3 focuses aus den 13 vorhandenen")
    if not set(u.get("age_groups") or []) <= AGES:
        out.append(f"{code}: unbekannte age_groups")
    # Bereich des Trainingsplans, aus dem die Übung stammt (bis UE-141: U9-U11; Plan U12-U14 ab 22.11.2026)
    if not u.get("altersbereiche") or not set(u["altersbereiche"]) <= {"U9-U11", "U12-U14"}:
        out.append(f"{code}: altersbereiche fehlt (U9-U11 oder U12-U14, je nach Plan, aus dem die Übung stammt)")
    if not 10 <= (u.get("duration_minutes") or 0) <= 20:
        out.append(f"{code}: duration_minutes 10-20")
    if (u.get("players_min") or 0) > (u.get("players_max") or 0):
        out.append(f"{code}: players_min größer als players_max")
    # Nur 5 Übungen sind frei mit Konto, UE-001 offen; alles andere ist Pro (Inhaber, 22.11.2026)
    FREI = {"UE-004", "UE-005", "UE-007", "UE-008", "UE-011"}
    soll = "offen" if code == "UE-001" else "frei" if code in FREI else "abo"
    if u.get("access") != soll or u.get("hidden") is not False:
        out.append(f"{code}: access muss '{soll}' sein (neue Einheiten sind Pro, nur 5 sind frei) und hidden false")
    if not 3 <= len((u.get("description") or "").split(". ")) <= 6:
        out.append(f"{code}: description soll 3-4 Sätze haben")
    org = u.get("organisation") or []
    if len(org) != 4 or any(": " not in o for o in org):
        out.append(f"{code}: organisation = 4 Punkte 'Stichwort: Satz'")
    if u.get("organisation_show") != ["lines", "cones", "players", "balls,arrows"]:
        out.append(f"{code}: organisation_show = [lines, cones, players, balls,arrows]")
    if len(u.get("coaching_points") or []) != 4:
        out.append(f"{code}: genau 4 coaching_points")
    base = u.get("board") or {}
    if not 3 <= len(base.get("steps") or []) <= 6:
        out.append(f"{code}: Grundform braucht 3-6 Schritte")
    if base.get("sketch_steps") is not None and not base.get("sketch_steps"):
        out.append(f"{code}: sketch_steps = null (Skizze zeigt alle Schritte)")
    vs = u.get("versions") or []
    if not 2 <= len(vs) <= 3:
        out.append(f"{code}: 2-3 Fassungen")
    out += board_regeln(base, f"{code} Grundform", False)
    for v in vs:
        vb = v.get("board") or {}
        name = f"{code} {v.get('label', 'Fassung')}"
        if not SAY_START.match(v.get("say") or ""):
            out.append(f"{name}: say muss mit 'Jetzt zum Coaching-Punkt', 'Der zweite Coaching-Punkt', 'Und jetzt die Steigerung' (bei der zweiten: 'Und jetzt die zweite Steigerung') oder 'Und jetzt das Umschalten' beginnen")
        for key in ("lines", "goals"):
            # Erlaubt: die Fassung ergänzt Linien (z. B. Hälften in einer Steigerung), dann muss sie alle Linien der Grundform enthalten
            if vb.get(key) and not (all(l in vb[key] for l in base.get(key) or []) and len(vb[key]) > len(base.get(key) or [])):
                out.append(f"{name}: {key} leer lassen (wird geerbt) oder alle der Grundform übernehmen und ergänzen")
        if vb.get("cones") and not all(c.get("id") for c in vb["cones"]):
            out.append(f"{name}: cones leer lassen (wird geerbt)")
        if not 2 <= len(vb.get("steps") or []) <= 6:
            out.append(f"{name}: 2-6 Schritte")
        out += board_regeln(lp.merge(base, vb), name, True)
    # Sprechtexte: keine Ziffern, ein Ergebnis als Satz, nie nur das Wort am Ende
    texts = [(f"{code} say_intro", u.get("say_intro") or "")]
    for st in base.get("steps") or []:
        texts.append((f"{code} Schritt '{st.get('label')}'", st.get("say") or ""))
    for v in vs:
        texts.append((f"{code} {v.get('label')} say", v.get("say") or ""))
        for st in (v.get("board") or {}).get("steps") or []:
            texts.append((f"{code} {v.get('label')} Schritt '{st.get('label')}'", st.get("say") or ""))
    for where, t in texts:
        if re.search(r"\d", t):
            out.append(f"{where}: Ziffer im Sprechtext, Zahlen ausschreiben")
        if re.search(r"\b(Punkt|Tor|Punkte)\.$", t.strip()) and "gibt" not in t:
            out.append(f"{where}: Ergebnis als Satz sprechen ('das gibt einen Punkt für Team Neon')")
        # Vom Inhaber: Ein Tor zählt immer als Punkt für das Team oder den Spieler. Kinder fangen (berühren), sie schlagen nicht ab.
        if re.search(r"gibt ein Tor", t):
            out.append(f"{where}: 'das gibt einen Punkt' statt 'das gibt ein Tor'")
    for where, t in texts + [(f"{code} description", u.get("description") or ""), (f"{code} organisation", " ".join(u.get("organisation") or []))]:
        if re.search(r"(?i)abschlag|abgeschlagen|abschläg|schlägt .* ab|abzuschlagen", t):
            out.append(f"{where}: nicht 'abschlagen', sondern 'fangen' (berühren)")
    return out
