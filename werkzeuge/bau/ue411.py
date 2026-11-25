import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 78-P10 (U15-U17, Woche 40 Phase 5): Defend as a Back 4 - Phase of Play. 7 gegen 7 auf 60 x 40 Yards = 55 x 37 m (gerundet
# 35 x 55 m). Kein Großfeld (kein ganzer Platz, kein Dreiviertelfeld, 7 gegen 7), aber ein langes Feld (Verhältnis 1,5):
# LANGES FELD QUER wie bau/ue317.py. Tore links und rechts, normale Figuren. Geplant im Hochformat wie im PDF (x 25-75 Breite,
# y 5-55 Länge, Tor von Team Neon unten); R() legt quer: unten -> links, oben -> rechts, links -> oben, rechts -> unten.
# Feld quer: x 9-89, y 4-51. Team Neon verteidigt links und kontert nach rechts.
# Pink (Viererkette 3, 4, 5, 2, dazu 8 und 9) -> Team Neon, Nummern wie im PDF. Blau (2-3-1) -> Team Rot, neu nummeriert,
# weil die Nummern doppelt sind: 2 -> 12, 3 -> 13, 4 -> 14, 5 -> 15, 8 -> 18, 9 -> 19. Grüne Torhüter -> neutrale Torhüter
# (k1 rechts, baut für Team Rot auf; k2 links), wie bei UE-317/UE-319. Ein Trainer an der Seitenlinie unten (im PDF rechts an
# der Mittellinie). Drittel wie im PDF als zwei gestrichelte Linien von Strafraum zu Strafraum (die Drittel liegen an den
# Strafraumkanten, das mittlere ist breiter). Mittellinie durchgezogen, Torräume weggelassen.
# Grundform nach PDF, Ton und Video (0:20-0:30): Torwart eröffnet, Pass auf den Flügel, die Kette schiebt zur Ballseite,
# Außenverteidiger und Mittelfeldspieler doppeln, Ballgewinn und schneller Konter aufs andere Tor.
# Fassungen: PDF Key Coaching Point 1 (das weite Drittel frei lassen) und 2 (Innenverteidiger rückt ins Mittelfeld, die Spitze
# lässt sich fallen, 4-2-Block, innen stehen, Ton 0:52-1:12). Das Video zeigt noch „Force play wide“ (in der Grundform enthalten).
# Sichtkegel: PDF „Defenders must always be aware of the free player“: im ersten Coaching-Punkt schaut Spieler zwei über die
# Schulter zum freien Spieler dreizehn im weiten Drittel (im Video markiert, Richtung aus dem Sinn).
# Neue Kegel-Regel (25.11.2026): Spieler zwei passt danach nicht selbst, der Kegel ist gestrichen (kein passender Passgeber).
# Positionen für den 3D-Abstand gestaffelt: Außenverteidiger etwas höher als die Innenverteidiger, Spitze von Team Rot
# zwischen den Außenverteidigern.
# Keine Dublette: UE-166, 177, 204, 206, 208 (78-P5), 212 (78-P6), 242 (78-P7), 250 (78-P12), 302, 320 (78-P4), 368, 370 (78-P8),
# 380 (78-P13) haben kein 7 gegen 7 mit Dritteln und Aufbau im 2-3-1.
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 25) / 50 * (FY1 - FY0), 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *R(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
def am_fuss(u, r=2.5):
    # Ball am Fuß und Pass zum Spieler: genau Spieler + 0,6 (nach dem Querlegen stimmt der Versatz sonst nicht mehr)
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
T = h.P("T", "c", 60, 55.3, "T")  # unten an der Seitenlinie in der Hälfte von Team Rot (quer gesetzt)
ERSATZ = [h.B("s1", 63.5, 55.8), h.B("s2", 66, 55.8)]
POS = {"k1": (50, 8), "r15": (41, 24), "r14": (59, 24), "r18": (60, 29.5), "r12": (29, 35), "r13": (71, 35), "r19": (50, 42),
       "n9": (42, 29.5), "n8": (48, 35), "n3": (32, 42), "n2": (68, 42), "n4": (41.5, 47.5), "n5": (58.5, 47.5), "k2": (50, 53.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
# Strafräume nach der PDF-Skizze (Breite x 37-63, Tiefe 8,7), Drittel-Linien an den Strafraumkanten
SX0, SX1 = R(0, 13.7)[0], R(0, 46.3)[0]
D1, D2 = R(37, 0)[1], R(63, 0)[1]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False),
         rect(FX0, D1, SX1 - FX0, D2 - D1), rect(SX0, D1, FX1 - SX0, D2 - D1),
         line(SX1, D1, SX0, D1), line(SX1, D2, SX0, D2)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
# Nur die Länge als Maßlinie (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "55 m", "35 m")[:1]

u = {"title": "Viererkette in drei Dritteln", "code": "UE-411", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "35 x 55 m",
 "description": "Sieben gegen sieben auf einem Feld mit zwei großen Toren. Team Rot baut vom Torwart aus im 2-3-1 auf, Team Neon verteidigt mit einer Viererkette. Zwei gestrichelte Linien teilen das Feld der Länge nach in drei Drittel, daran richtet sich die Kette aus. Sie schiebt gemeinsam zum Ball, lässt das weite Drittel frei, erobert den Ball und kontert aufs andere Tor.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 55 Metern mit Mittellinie, zwei Strafräumen und zwei großen Toren. Zwei gestrichelte Linien von Strafraum zu Strafraum teilen das Feld in drei Drittel.",
  "Verteilen: Team Rot spielt im 2-3-1, Team Neon mit einer Viererkette, einem Mittelfeldspieler und einer Spitze. In jedem Tor steht ein Torwart. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet für Team Rot, Team Rot baut auf und greift an. Die Kette schiebt gemeinsam zum Ball und besetzt zwei Drittel, das weite Drittel bleibt frei. Erobert Team Neon den Ball, kontert es sofort aufs andere Tor.",
  "Wertung: Jeder Treffer gibt einen Punkt für das Team, das trifft. Nach jedem Angriff bringt der Trainer den nächsten Ball zum Torwart von Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Das weite Drittel frei lassen, die Mitte bleibt zu", "Rückt ein Innenverteidiger vor, kommt die Spitze zurück", "Innen stehen, kein Pass durch die Mitte", "Nach außen lenken und zu zweit drauf"],
 "materials": ["2 große Tore", "Linien oder Hütchen für die Drittel", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette in drei Dritteln. Sieben gegen sieben mit zwei Toren. Team Rot baut von hinten auf, unsere Viererkette schiebt gemeinsam, bleibt eng und kontert nach dem Ballgewinn.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50, 8)] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Der Torwart eröffnet", "Team Rot baut vom Torwart aus auf. Er spielt flach zu Spieler vierzehn. Vorn läuft Spieler neun ein Stück an, der Rest von Team Neon steht kompakt.",
     ps("b1", [59, 24]), mv("n9", [50, 27.5], delay=0.4)),
   S("Raus auf den Flügel, die Kette schiebt", "Spieler vierzehn spielt raus zu Spieler dreizehn. Sofort schiebt die ganze Kette zur Ballseite. Spieler zwei geht drauf, die anderen rücken eng nach, und Spieler acht kommt mit.",
     ps("b1", [71, 35]), mv("n2", [70, 39.5], delay=0.3), mv("n5", [62, 46], delay=0.4), mv("n4", [51, 47.5], delay=0.4),
     mv("n3", [41, 44.5], delay=0.4), mv("n8", [58, 37], delay=0.4)),
   S("Nach außen lenken, zu zweit drauf", "Spieler zwei lässt ihn nicht nach innen. Spieler dreizehn muss an der Linie entlang, und da wartet schon Spieler acht. Zu zweit holen sie den Ball.",
     dr("r13", "b1", [73, 40.5]), mv("n2", [70, 43], delay=0.2), mv("n8", [66.5, 39], delay=0.3), ps("b1", [66.5, 39], after=True)),
   S("Schnell nach vorn: Punkt", "Jetzt schnell nach vorn. Spieler neun startet in den Raum hinter Spieler vierzehn, und Spieler acht spielt ihn sofort an. Er schießt flach ins Eck, und das gibt einen Punkt für Team Neon. Danach bringt der Trainer den nächsten Ball zum Torwart von Team Rot.",
     mv("n9", [64, 14]), ps("b1", [64, 14], delay=0.6), ps("b1", [54, 5.3], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Das weite Drittel bleibt frei.", "Das weite Drittel frei",
    "Ist der Ball außen, schiebt die Kette so weit rüber, dass sie zwei Drittel besetzt. Das dritte Drittel bleibt leer, und der Flügelspieler dort ist frei. Das ist gewollt, so bleibt die Mitte zu. Der Außenverteidiger auf der anderen Seite schaut immer wieder nach ihm.",
    sp(), [B("b1", 41, 24)] + ERSATZ,
    [S("Ball auf den Flügel, Kette schiebt", "Der Ball geht raus zu Spieler zwölf. Die ganze Kette schiebt mit. Spieler drei geht drauf, und Spieler zwei rückt bis ins mittlere Drittel ein.",
       ps("b1", [29, 35]), mv("n3", [30.5, 39.5], delay=0.3), mv("n4", [39, 46], delay=0.4), mv("n5", [49, 47], delay=0.4),
       mv("n2", [58, 44.5], delay=0.4), mv("n8", [38, 37], delay=0.3)),
     S("Das weite Drittel bleibt frei", "Ganz drüben steht Spieler dreizehn jetzt frei. Das lassen wir zu. Spieler zwei bleibt eng bei der Kette. Kommt doch der lange Ball, ist er schnell drüben."),
     S("Zu zweit drauf, Ball erobert", "Spieler zwölf will an der Linie vorbei. Spieler drei lässt ihn nicht nach innen, und Spieler acht kommt dazu. Zu zweit holen sie den Ball, bevor der lange Ball rüber kommt.",
       dr("r12", "b1", [27, 38]), mv("n8", [33, 37.5], delay=0.2), ps("b1", [30.5, 39.5], after=True))],
    dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Rückt ein Innenverteidiger vor, kommt die Spitze zurück.", "Spitze lässt sich fallen",
    "Dribbelt ein Innenverteidiger von Team Rot ins Mittelfeld, hat Team Rot dort einen Spieler mehr. Dann lässt sich Spieler neun fallen und stellt sich neben Spieler acht. Hinten stehen vier, davor zwei. Die beiden stehen innen und machen den Pass durch die Mitte zu.",
    sp(), [B("b1", 59, 24)] + ERSATZ,
    [S("Innenverteidiger rückt ins Mittelfeld", "Jetzt ändert Team Rot den Aufbau. Spieler vierzehn dribbelt aus der Abwehr ins Mittelfeld, Spieler achtzehn macht ihm Platz. Im Mittelfeld hat Team Rot jetzt einen Spieler mehr.",
       mv("r18", [67, 30]), dr("r14", "b1", [56, 31], delay=0.3)),
     S("Spieler neun lässt sich fallen", "Spieler neun sieht das und lässt sich fallen. Er stellt sich neben Spieler acht. Jetzt stehen vier hinten und zwei davor, und der Ball bleibt vor uns.",
       mv("n9", [55, 37]), mv("n8", [45, 37], delay=0.2)),
     S("Innen stehen, Pass abgefangen", "Spieler vierzehn will durch die Mitte auf Spieler neunzehn spielen. Spieler neun steht innen, macht einen Schritt in den Passweg und fängt den Ball ab.",
       mv("n9", [53, 36.5], delay=0.2), ps("b1", [53, 36.5], delay=0.3))],
    dims=DIMS)]}
am_fuss(u)
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
