import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 24.11.2026: Spieler acht scannt erst zum Ball (oben), nimmt an, und ERST DANN schwenkt der Kegel nach links zum Passziel (bl mit von im nächsten Schritt); das Aufdrehen ist ein Drehpfeil (drehen), kein Kegel.
# PS-83 (U15-U17, Woche 1 Pre-Season): Passing, Agility and Speed Circuit. 40 x 30 Yards = 36 x 27 m (gerundet 35 x 25 m).
# Ausrichtung wie im PDF (Start unten, Ball läuft gegen den Uhrzeigersinn). Nummern wie im PDF (4-11, nur ein Team).
# Start, Spieler 9 und die Wartenden 4/5 ein Stück nach links gerückt, damit Spieler 9 in 3D nicht vor den Ringen steht;
# Ringe gestreckt (Ringabstand), Spieler 8 etwas tiefer (verdeckt sonst die Leiter).
# Hütchen von Spieler 8 liegt über ihm statt links unten (sonst läuft der Pass nach links durch das Hütchen).
# Ein Trainer statt zwei. Spieler 8 bleibt in der Mitte (im PDF kein Laufweg zu einer anderen Station).
# Sichtkegel: Text KCP 1 „open body shape … vision forward“, Ton „keep your head up“; im Video nicht eingezeichnet,
# Richtung aus dem Sinn: Spieler 8 schaut vor der Annahme nach links zu Spieler 6 an den Hürden.
# FELD FÜLLT DIE TAFEL (Inhaber, 24.11.2026): Das Feld lag schon quer, war aber zu klein (x 20-76, y 8-50). Geplant bleibt alles
# im alten Raster; R() zieht es auf x 11-87, y 4-51 auf (in der Länge 1,36-fach, in der Tiefe 1,12-fach, die Tafel ist flacher
# als das Feld). Geräte behalten ihre Form und Größe, nur ihre Plätze werden umgerechnet. Der Trainer steht jetzt unten an der
# Seitenlinie statt links. Bälle am Fuß und Pässe zum Spieler setzt am_fuss() wieder genau auf Spieler + 0,6.
SX, SY = 76 / 56, 47 / 42
def R(x, y): return [round(11 + (x - 20) * SX, 1), round(4 + (y - 8) * SY, 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def C(x, y, *a, **k): return h.C(*R(x, y), *a, **k)
def ring(x, y): return h.ring(*R(x, y))
def leiter(x, y, **k): return h.leiter(*R(x, y), **k)
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
def am_fuss(u, r=2.0):
    # Ball am Fuß und Pass zum Spieler: genau Spieler + 0,6 (nach dem Aufziehen stimmt der Versatz sonst nicht mehr)
    base = u["board"]
    def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
    for b in [base] + [v["board"] for v in u.get("versions") or []]:
        pos = {p["id"]: [p["x"], p["y"]] for p in b.get("players") or base["players"]}
        for ba in b.get("balls") or []:
            p = min(pos.values(), key=lambda p: math.dist(p, [ba["x"], ba["y"]]))
            if math.dist(p, [ba["x"], ba["y"]]) < r:
                ba["x"], ba["y"] = fuss(p)
        for st in b.get("steps") or []:
            ziele = list(pos.values()) + [m["to"] for m in st["moves"] if m["who"] in pos and m["type"] in ("lauf", "dribbling")]
            for m in st["moves"]:
                if m["type"] == "pass":
                    p = min(ziele, key=lambda p: math.dist(p, m["to"]))
                    if math.dist(p, m["to"]) < r:
                        m["to"] = fuss(p)
            for m in st["moves"]:
                if m["who"] in pos and m["type"] in ("lauf", "dribbling"):
                    pos[m["who"]] = m["to"]
T = h.P("T", "c", 40, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [h.B("s1", 43.5, 55.8), h.B("s2", 46, 55.8)]
POS = {"n6": (27.4, 10.9), "n7": (51.5, 11.1), "n9": (64, 32), "n8": (42.9, 30), "n10": (27.1, 41.5), "n11": (55.8, 41.5),
       "n5": (64, 47.6), "n4": (72.4, 47.6)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
WARTE = [B("b5", 64.6, 48.2), B("b4", 73, 48.2)]
RINGE = [(70.4, 26.5), (73.6, 22.5), (70.4, 18.5), (73.6, 14.5), (70.4, 10.5)]
HUERDEN = [(25.2, 15), (25.2, 18.5), (25.2, 22), (25.2, 25.5)]
CONES = [C(52.8, 42), C(66.5, 35.4), C(60, 13.5), C(55.5, 8.6), C(23, 10.5), C(40.2, 27.4), C(24.3, 43.5), C(41, 48.3)] \
    + [ring(x, y) for x, y in RINGE] + [leiter(38.5, 11.3)] + [C(x, y, shape="huerde_ou") for x, y in HUERDEN]
LINES = [rect(11, 4, 76, 47)]
def ringe(delay=0.3):
    return [mv("n9", list(RINGE[0]), delay=delay)] + [mv("n9", list(r), after=True) for r in RINGE[1:]] + [mv("n9", [61.5, 11], after=True)]
def huerden(delay=None):
    return [mv("n6", [25.2, 13], delay=delay), mv("n6", [25.2, 27.5], after=True), mv("n6", [24.5, 30.5], after=True)]
def leiterlauf(delay=None):
    return [mv("n7", [46.5, 11.3], delay=delay), mv("n7", [30.5, 11.3], after=True), mv("n7", [28, 11.2], after=True)]

u = {"title": "Passzirkel mit Tempo", "code": "UE-300", "kind": "Übungsform",
 "focuses": ["Passspiel", "Koordination", "Schnelligkeit"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "35 x 25 m",
 "description": "Ein Rundlauf mit sechs Stationen für die Vorbereitung. Der Ball läuft vom Start über rechts nach oben, durch die Mitte nach links und unten herum zurück zum Start. Nach seinem Pass läuft jeder zur nächsten Station, durch die Ringe, durch die Leiter oder über die Hürden. Das Tempo bleibt hoch, Luft holen die Spieler nur am Start.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 25 Metern. Rechts liegen fünf Ringe, oben liegt eine Leiter, links stehen vier Minihürden. Acht Hütchen markieren die Stationen.",
  "Verteilen: Je ein Spieler steht an den vier Hütchen außen, einer steht in der Mitte. Alle anderen warten mit Ball am Start unten. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass am Start, steil nach oben, Pass in die Mitte, raus nach links und tief nach unten. Nach einem zweiten Doppelpass geht es mit Ball zurück zum Start. Wer gepasst hat, läuft durch das Gerät zur nächsten Station.",
  "Wechsel: Jeder rückt nach seiner Aktion eine Station weiter. Der Spieler in der Mitte bleibt und wird nach einigen Runden getauscht. Ist der Ball zurück am Start, beginnt der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch vor dem Pass", "Flach und scharf passen, auch mit müden Beinen", "Seitlich stehen und mit dem ersten Kontakt aufdrehen", "Sauber durch die Geräte, dann Vollgas bis zum Hütchen"],
 "materials": ["8 Hütchen", "5 Ringe", "1 Koordinationsleiter", "4 Minihürden", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passzirkel mit Tempo. Ein Rundlauf für die Vorbereitung. Der Ball läuft einmal ums Feld, und nach jedem Pass geht es durch Ringe, Leiter oder Hürden zur nächsten Station.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 56.4, 42.1)] + WARTE + ERSATZ,
  "steps": [
   S("Doppelpass am Start", "Spieler elf startet unten. Er spielt zu Spieler neun und läuft sofort nach. Der Ball kommt mit einem Kontakt zurück.",
     ps("b1", [64.6, 32.6]), mv("n11", [56.3, 33], delay=0.3), ps("b1", [56.9, 33.6], after=True)),
   S("Steil nach oben, ab in die Ringe", "Jetzt geht es steil nach oben zu Spieler sieben. Spieler neun springt durch die Ringe und sprintet bis zum Hütchen.",
     ps("b1", [52.1, 11.7]), *ringe()),
   S("Pass in die Mitte, über die Hürden", "Spieler acht in der Mitte schaut kurz nach links, dann kommt der Pass von Spieler sieben. Drüben springt Spieler sechs schon über die Hürden.",
     bl("n8", [51.5, 13.5]), ps("b1", [43.5, 30.6], after=True), *huerden(delay=0.6), mv("n11", [64, 32], delay=0.2)),
   S("Aufdrehen, Pass nach links", "Spieler acht dreht auf und spielt nach links raus, genau in den Lauf von Spieler sechs. Oben geht Spieler sieben durch die Leiter, Spieler neun rückt nach.",
     bl("n8", [25.1, 31.1], von=[51.5, 13.5], dauer=1.3), drehen("n8", [25.1, 31.1], gegen=True, delay=0.4), ps("b1", [25.1, 31.1], after=True), *leiterlauf(delay=0.2), mv("n9", [51.5, 11.1], delay=0.8)),
   S("Tief und Doppelpass", "Weiter nach unten zu Spieler zehn. Der spielt gleich den Doppelpass mit Spieler acht, der ihm ein paar Schritte entgegenkommt.",
     ps("b1", [27.7, 42.1]), mv("n8", [35.2, 35.7], delay=0.2), ps("b1", [35.8, 36.3], after=True)),
   S("Mit Ball zurück zum Start", "Spieler acht legt in den Lauf ab, und Spieler zehn dribbelt mit Tempo zurück zum Start. Alle sind eine Station weitergerückt, nur Spieler acht bleibt in der Mitte. Jetzt startet Spieler fünf.",
     mv("n10", [43.6, 45]), ps("b1", [44.2, 45.6], delay=0.3), dr("n10", "b1", [55.8, 45.5], after=True),
     mv("n8", [42.9, 30], delay=0.8), mv("n6", [27.1, 41.5], delay=1.0))],
  "dims": dims(11, 87, 4, 51, "35 m", "25 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Offen stehen und schnell aufdrehen.", "Offen stehen, schnell drehen",
    "Der Spieler in der Mitte steht seitlich zum Ball und sieht so beide Seiten. Vor dem Pass geht der Kopf hoch. Mit dem ersten Kontakt dreht er auf, mit dem zweiten spielt er weiter.",
    sp(), [B("b1", 52.1, 11.7)] + WARTE + ERSATZ,
    [S("Seitlich stehen, Kopf hoch", "Spieler acht steht seitlich und nicht mit dem Rücken zum Feld. Bevor der Ball kommt, schaut er nach links zu den Hürden. Dann spielt Spieler sieben.",
       bl("n8", [51.5, 13.5]), ps("b1", [43.5, 30.6], after=True)),
     S("Erster Kontakt dreht, zweiter passt", "Der erste Kontakt geht schon in die neue Richtung. Mit dem zweiten spielt er flach in den Lauf von Spieler sechs, der gerade über die letzte Hürde kommt.",
       *huerden(), bl("n8", [25.1, 31.1], von=[51.5, 13.5], dauer=1.3, delay=0.2), drehen("n8", [25.1, 31.1], gegen=True, delay=0.6), ps("b1", [25.1, 31.1], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Sauber durch die Geräte, auch wenn die Beine schwer werden.", "Sauber durch die Geräte",
    "In den Ringen, in der Leiter und über den Hürden bleibt die Bewegung sauber. Kurz auf dem Boden, Arme mitnehmen, Oberkörper aufrecht. Wer müde wird, macht die Schritte trotzdem ordentlich und nimmt kein Tempo raus.",
    sp(), [B("b1", 52.1, 11.7)] + WARTE + ERSATZ,
    [S("Durch die Ringe, dann Sprint", "Spieler neun hat abgelegt und geht in die Ringe. Jeder Fuß trifft einen Ring, die Arme arbeiten mit. Nach dem letzten Ring zieht er den Sprint bis zum Hütchen durch.",
       *ringe(delay=None)),
     S("Leiter und Hürden", "Spieler sieben spielt in die Mitte und läuft durch die Leiter, in jedes Feld ein Fuß. Gleichzeitig nimmt Spieler sechs die Hürden, Knie hoch und ohne Zwischenschritt.",
       ps("b1", [43.5, 30.6]), *leiterlauf(delay=0.3), *huerden(delay=0.3))])]}
am_fuss(u)
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
