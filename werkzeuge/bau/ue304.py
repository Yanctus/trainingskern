import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 100-P8 (U15-U17, Woche 11): Exploit the Overload to Finish (Wave). 20 x 30 Yards = 18 m tief, 27 m breit (gerundet 25 m).
# Um 90 Grad gedreht: das große Tor mit Torwart liegt oben (im PDF rechts), die zwei Minitore unten (im PDF links).
# PDF pink -> Team Neon (9, 8, 11, wartend 2), blau -> Team Rot. Rot neu nummeriert, weil 9, 4 und 5
# doppelt sind: blau 9 -> 7, blau 10 bleibt, wartend 3 und 6. Von den Wartenden nur drei gezeichnet (3D-Abstand).
# Ein Trainer statt zwei: Er steht in Phase eins als Wandspieler in der Mitte und geht danach zu den Ersatzbällen am Rand.
# Fassungen aus Text und Ton: Doppelpass am Verteidiger vorbei ("quick 1-2 combinations to play around defenders") und
# Konter der Verteidiger nach Ballgewinn ("if the defenders win possession they counter-attack and finish").
# Sichtkegel: im Video nicht eingezeichnet; aus Text und Ton ("identify and use the overload", "find the free player"):
# Der Ballführende schaut in Phase drei zum freien Mitspieler, bevor er passt.
# FELD FÜLLT DIE TAFEL (Inhaber, 24.11.2026): Das Feld lag schon quer, war aber zu klein (x 20-80, y 8-48). Geplant bleibt alles
# im alten Raster; R() zieht es auf x 13-87, y 7-51 auf (in der Länge 1,23-fach, in der Tiefe 1,1-fach; mehr Tiefe geht nicht,
# weil Team Rot über und Team Neon unter dem Feld wartet). Spieler zwei rückt dichter an die Grundlinie (Maßlinie unten),
# der Trainer geht nach Phase eins an den Rand links. Bälle am Fuß und Pässe zum Spieler setzt am_fuss() wieder genau auf +0,6.
SX, SY = 74 / 60, 1.1
def R(x, y): return [round(13 + (x - 20) * SX, 1), round(7 + (y - 8) * SY, 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
def rect(x, y, w, hh): return h.rect(*R(x, y), round(w * SX, 1), round(hh * SY, 1))
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
TW = P("k", "t", 50.9, 10.3, "TW")
ERSATZ = [h.B("s1", 4.4, 34), h.B("s2", 8, 34)]
TR = (14.3, 28.9)  # quer (6, 30): links neben dem Feld
POS = {"n9": (50, 51), "n8": (24, 51), "n11": (76, 51), "n2": (65.5, 51.9),
       "r7": (32, 6), "r10": (68, 6), "r3": (23, 6), "r6": (77, 6)}
def sp(t=TR, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, P("T", "c", t[0], t[1], "T")]
def baelle(**k):
    d = {"b1": (50.6, 51.6), "b2": (32.6, 6.6), "b3": (24.6, 51.6), "b4": (66.1, 52.5)}; d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(20, 8, 60, 40), rect(33.5, 8, 33, 9)]
def tor(x, y, side, **k): return {"x": R(x, y)[0], "y": R(x, y)[1], "side": side, **k}
TORE = [tor(50, 8, "top", size="gross"), tor(40.5, 48, "bottom"), tor(59.5, 48, "bottom")]
DIMS = dims(13, 87, 7, 51, "25 m", "18 m", rx=93)

u = {"title": "Drei Wellen in Überzahl", "code": "UE-304", "kind": "Übungsform",
 "focuses": ["Torschuss", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 14,
 "field_size": "25 x 18 m",
 "description": "Drei Angriffe folgen direkt aufeinander. Zuerst schießt ein Angreifer nach der Ablage des Trainers direkt aufs große Tor. Sofort danach greifen zwei Gegner ihn im zwei gegen eins auf die Minitore an. Zum Schluss kommen zwei Mitspieler dazu, und es geht drei gegen zwei zurück aufs große Tor.",
 "organisation": ["Aufbauen: Ein Feld, 25 Meter breit und 18 Meter tief. Oben steht ein großes Tor mit Torwart, unten stehen zwei Minitore nebeneinander.",
  "Verteilen: Team Neon wartet unten an der Grundlinie, links, rechts und in der Mitte zwischen den Minitoren. Team Rot wartet oben links und rechts neben dem großen Tor. Alle haben Bälle. Der Trainer steht zuerst in der Mitte des Feldes.",
  "Ablauf: Phase eins, Pass zum Trainer, Ablage, Schuss aufs große Tor. Phase zwei, zwei Spieler von Team Rot greifen den Schützen im zwei gegen eins auf die Minitore an. Phase drei, zwei Spieler von Team Neon kommen dazu und spielen drei gegen zwei aufs große Tor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobern die Verteidiger den Ball, kontern sie sofort auf die andere Seite. Nach Phase drei gehen alle raus, und der Nächste startet wieder mit Phase eins."],
 "organisation_show": ORG,
 "coaching_points": ["Den ersten Schuss voll durchziehen", "Kopf hoch, wo ist der freie Mann", "Mit Tempo auf den Verteidiger zu, dann abspielen", "Ball weg, sofort umschalten"],
 "materials": ["1 großes Tor", "2 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Drei Wellen in Überzahl. Erst ein Schuss, dann zwei gegen eins, dann drei gegen zwei. Wer gerade noch angegriffen hat, verteidigt im nächsten Moment.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(t=(48, 28)), "balls": baelle(),
  "steps": [
   S("Phase eins: Pass und Ablage", "Spieler neun startet unten in der Mitte. Er spielt flach zum Trainer und läuft sofort nach. Der Trainer legt ihm den Ball zur Seite auf.",
     ps("b1", [48.6, 28.6]), mv("n9", [55, 34], delay=0.3), ps("b1", [55.6, 34.6], after=True)),
   S("Direkt aufs Tor: Punkt", "Ohne Annahme zieht Spieler neun ab. Der Ball schlägt links unten ein, und das gibt einen Punkt für Team Neon. Mit dem Schuss läuft schon Phase zwei.",
     ps("b1", [45, 8.3])),
   S("Phase zwei: zwei gegen eins", "Von oben kommen jetzt Spieler sieben mit Ball und Spieler zehn. Sie greifen die Minitore an. Spieler neun dreht sich um und verteidigt allein. Der Trainer geht raus an den Rand.",
     dr("r7", "b2", [35.5, 20]), mv("r10", [64, 22], delay=0.2), mv("n9", [45, 31], delay=0.3), mv("T", list(TR))),
   S("Querpass, Minitor: Punkt", "Spieler neun läuft Spieler sieben an. Genau dann kommt der Querpass. Spieler zehn hat freie Bahn und schiebt ins rechte Minitor ein, und das gibt einen Punkt für Team Rot.",
     mv("n9", [41, 25]), ps("b2", [64.6, 22.6], delay=0.3), dr("r10", "b2", [61, 38], after=True), ps("b2", [59.5, 47.7], after=True)),
   S("Phase drei: drei gegen zwei", "Sofort geht es zurück. Spieler acht dribbelt von links unten ins Feld, rechts kommt Spieler elf dazu. Spieler neun läuft nach vorn. Team Rot muss jetzt zu zweit verteidigen. Spieler acht hebt den Kopf. Wer ist frei?",
     dr("n8", "b3", [30, 38]), mv("n11", [72, 36], delay=0.2), mv("n9", [42, 22], delay=0.2),
     mv("r7", [38.5, 38], delay=0.3), mv("r10", [63, 27], delay=0.3), bl("n8", [42, 22], after=True)),
   S("Freier Mann, Abschluss: Punkt", "In der Mitte steht Spieler neun frei. Der Pass kommt flach in den Fuß, er schießt, und das gibt einen Punkt für Team Neon. Danach gehen alle raus, und Spieler zwei startet wieder mit Phase eins.",
     ps("b3", [42.6, 22.6]), ps("b3", [45, 8.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Doppelpass am Verteidiger vorbei.", "Doppelpass am Verteidiger",
    "Zwei gegen eins heißt, einer ist immer frei. Der Ballführende geht mit Tempo auf den Verteidiger zu und bindet ihn. Dann spielt er ab und läuft sofort weiter. Der Ball kommt direkt in seinen Lauf zurück.",
    sp(n9=(44, 31), r7=(35.5, 20), r10=(64, 22)), baelle(b1=(45, 8.3), b2=(36.1, 20.6)),
    [S("Verteidiger binden, abspielen", "Spieler sieben dribbelt direkt auf Spieler neun zu. Erst kurz vor ihm spielt er quer zu Spieler zehn und startet links am Verteidiger vorbei.",
       dr("r7", "b2", [38, 25]), mv("n9", [41.5, 31.2], delay=0.2), ps("b2", [64.6, 22.6], after=True), mv("r7", [34, 31], after=True), mv("r7", [36, 39], after=True)),
     S("Direkt in den Lauf: Punkt", "Spieler zehn lässt den Ball nur prallen, genau in den Lauf. Spieler sieben ist durch und trifft ins linke Minitor, und das gibt einen Punkt für Team Rot.",
       ps("b2", [36.6, 39.6]), mv("n9", [46.5, 30.5], delay=0.2), ps("b2", [40.5, 47.7], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ball erobert, sofort kontern.", "Ball erobert, sofort kontern",
    "Wer in Unterzahl verteidigt, lauert auf den Fehler. Fängt ein Verteidiger den Pass ab, geht es ohne Pause in die andere Richtung. Die Angreifer müssen dann sofort zurück.",
    sp(n8=(30, 38), n9=(42, 22), n11=(72, 36), r7=(38.5, 38), r10=(63, 27)), baelle(b1=(45, 8.3), b2=(59.5, 47.7), b3=(30.6, 38.6)),
    [S("Pass abgefangen", "Spieler acht will durch die Mitte zu Spieler neun spielen. Spieler sieben ahnt das. Er macht einen Schritt in den Passweg und hat den Ball.",
       mv("r7", [36.5, 30.5]), ps("b3", [37.1, 31.1], delay=0.3)),
     S("Konter aufs Minitor: Punkt", "Jetzt schaltet Team Rot um. Spieler sieben nimmt den Ball mit und geht an Spieler acht vorbei. Der kommt nicht mehr hin. Schuss ins linke Minitor, und das gibt einen Punkt für Team Rot.",
       dr("r7", "b3", [39, 41]), mv("n8", [33, 42], delay=0.3), mv("r10", [58, 38], delay=0.2), mv("n9", [44, 30], delay=0.4), ps("b3", [40.5, 47.7], after=True))], dims=DIMS)]}
am_fuss(u)
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
