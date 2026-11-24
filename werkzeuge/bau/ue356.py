import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# 10-P14 (U15-U17, Woche 20 Phase 4): Pressing as a Unit (433), 11 gegen 11 auf dem ganzen Platz, drei Zonen (65 x 100 m).
# Pink (4-3-3, presst als Einheit, im Ton „Reds“) -> Team Neon, Nummern wie im PDF. Navy (3-4-3, im Ton „Whites“) -> Team Rot,
# neu nummeriert, weil alle Nummern doppelt sind: Navy n -> n + 10 (2 -> 12 ... 11 -> 21). Beide Torhüter neutral (k1, k2)
# wie bei UE-319. Ein Trainer statt zwei.
# GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Geplant im Hochformat wie im PDF (x 12-88 Breite, y 4-56 Länge,
# Tor von Team Neon oben, Tor von Team Rot unten). R() legt quer, hier gegen den Uhrzeigersinn gedreht (eine Drehung, nicht
# gespiegelt): oben -> links, unten -> rechts, links -> unten, rechts -> oben. So steht der Trainer wie im PDF (dort links
# unten) unten an der Seitenlinie in der Hälfte von Team Rot und spielt kurz auf die Spitzen. Team Neon verteidigt links und
# greift nach rechts an. Feld x 7-91, y 3-52, massstab "gross". Zonengrenzen gestrichelt wie im PDF (dort nicht in Dritteln,
# sondern etwa ein Viertel, die Hälfte und ein Viertel), quer bei x 29.5 und x 68.5.
# Aufstellung nach PDF, für den 3D-Abstand in Reihen geordnet (in der Länge leicht versetzt).
# Ablauf Grundform nach PDF und Ton: Trainer spielt auf die drei Spitzen (3 gegen 3 mit Torwart), Team Rot fängt ab und spielt
# ins Mittelfeld (7 gegen 7), der Außenverteidiger presst hoch, Ballgewinn, Konter mit einem Mittelfeldspieler mehr (4 gegen 3).
# Fassungen: PDF Key Coaching Point 1 (Flügelspieler zieht nach innen, Schulterblick im Mittelfeld; im PDF der Fehler, hier
# die richtige Lösung, der Fehler steht im Text) und Key Coaching Point 2 (Konter gemeinsam unterstützen).
# Sichtkegel aus Text („Check shoulders to cover all defensive angles“) und Video (Kreis um die Mittelfeldspieler): Spieler zehn
# schaut über die Schulter zum einrückenden Spieler einundzwanzig (Fassung 1). In Fassung 2 schaut der Balleroberer vor dem
# Steilpass nach vorn (Ton: Konter einleiten).
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
def R(x, y): return [round(FX0 + (y - 4) / 52 * (FX1 - FX0), 1), round(FY1 - (x - 12) / 76 * (FY1 - FY0), 1)]
def RF(x, y): return [round(v + 0.6, 1) for v in R(x, y)]  # Ball am Fuß / Pass zum Spieler
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *RF(x, y))
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, R(*to), **k)
def pf(ball, to, **k): return h.ps(ball, RF(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 80, 55.3, "T")  # unten an der Seitenlinie in der Hälfte von Team Rot
ERSATZ = [h.B("s1", 83.5, 55.8), h.B("s2", 86, 55.8)]
NEON = {"k1": (50, 5.7), "n4": (34, 18.5), "n5": (66, 18.5), "n2": (14, 22.5), "n3": (86, 22.5), "n6": (50, 26.5),
        "n10": (36, 31), "n8": (62, 31), "n7": (33, 43.2), "n11": (67, 43.2), "n9": (50, 47)}
ROT = {"r19": (50, 22.5), "r21": (31, 26.5), "r17": (69, 26.5), "r13": (17, 35), "r18": (40, 35), "r20": (59, 35),
       "r12": (84, 35), "r15": (31, 50.8), "r14": (50, 50.8), "r16": (69, 50.8), "k2": (50, 54.6)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 6.5},
         rect(FX0, MY - 15.5, 14, 31), rect(FX1 - 14, MY - 15.5, 14, 31), rect(FX0, MY - 7, 4.6, 14), rect(FX1 - 4.6, MY - 7, 4.6, 14),
         line(29.5, FY0, 29.5, FY1), line(68.5, FY0, 68.5, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
# Nur die Länge als Maßlinie: Rechts neben dem Tor ist kein Platz, die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "100 m", "65 m")[:1]

u = {"title": "Drei Zonen, als Block pressen", "code": "UE-356", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Elf gegen elf auf dem ganzen Platz, eingeteilt in drei Zonen. Vorn spielen die drei Spitzen von Team Neon drei gegen drei gegen die Abwehr von Team Rot. Erobert Team Rot den Ball, baut es im Mittelfeld sieben gegen sieben auf, und Team Neon presst als ganzer Block. Nach dem Ballgewinn kontert Team Neon sofort, ein Mittelfeldspieler darf mit nach vorn.",
 "organisation": ["Aufbauen: Das ganze Großfeld mit zwei Toren, in drei Zonen geteilt. Vorn und hinten je etwa ein Viertel, in der Mitte die halbe Länge. Der Trainer steht mit vielen Bällen an der Seitenlinie bei Team Rot.",
  "Verteilen: Team Neon im 4-3-3, Team Rot im 3-4-3. Vorn drei Spitzen gegen drei Verteidiger mit Torwart. In der Mitte sieben gegen sieben, die Viererkette von Team Neon steht hoch.",
  "Ablauf: Der Trainer spielt auf die Spitzen von Team Neon. Erobert Team Rot den Ball, spielt es ins Mittelfeld und baut auf. Team Neon presst gemeinsam, die Außenverteidiger rücken hoch. Nach dem Ballgewinn geht es sofort nach vorn, ein Mittelfeldspieler darf mit, also vier gegen drei.",
  "Wertung: Jeder Treffer gibt einen Punkt. Nach jedem Angriff spielt der Trainer neu ein, entweder auf die Spitzen oder ins Mittelfeld zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Seite zumachen und in Überzahl zum Ball", "Alle machen mit: einer presst, die anderen sichern", "Schulterblick: Wer steht hinter mir?", "Torwart coacht laut: rüber, zusammen, zurück"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in zwei Farben", "Hütchen für die Zonen"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Drei Zonen, als Block pressen. Elf gegen elf auf dem ganzen Platz. Team Neon presst gemeinsam im Mittelfeld und kontert nach dem Ballgewinn sofort.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [h.B("b1", 80.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt die Spitzen an", "Der Trainer spielt auf Spieler sieben. Vorn heißt es drei gegen drei, unsere drei Spitzen gegen die Dreierkette von Team Rot mit Torwart. Spieler neun und Spieler elf bieten sich an.",
     pf("b1", NEON["n7"]), mv("r15", [33, 48.3], delay=0.5), mv("n9", [55, 48.5], delay=0.4), mv("n11", [64, 47.5], delay=0.4)),
   S("Abgefangen, Rot spielt raus", "Spieler sieben will zu Spieler elf. Spieler sechzehn geht dazwischen und hat den Ball. Sofort spielt er raus ins Mittelfeld zu Spieler zwölf.",
     mv("r16", [59.5, 46.5], delay=0.2), pf("b1", [59.5, 46.5]), pf("b1", ROT["r12"], after=True)),
   S("Außenverteidiger presst hoch", "Jetzt pressen wir als Block. Spieler drei rückt hoch und läuft Spieler zwölf an. Der spielt nach innen zu Spieler siebzehn, und genau da machen Spieler fünf und Spieler acht zu.",
     mv("n3", [84.5, 31]), pf("b1", ROT["r17"], delay=0.8), mv("n5", [71, 22.5], delay=1.3), mv("n8", [67.5, 30.5], delay=1.3),
     mv("n6", [57, 26], delay=1.3)),
   S("Pass nach innen abgefangen", "Spieler siebzehn ist eingeklemmt und spielt quer nach innen. Spieler zehn hat das kommen sehen. Er geht dazwischen, und der Konter läuft.",
     mv("n10", [44, 31.5], delay=0.3), pf("b1", [44, 31.5])),
   S("Vier gegen drei: Punkt", "Spieler zehn treibt den Ball in die vordere Zone, er ist der vierte Mann. Spieler vierzehn muss raus, und Spieler neun ist frei. Er schießt ins lange Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer neu ein, auf die Spitzen oder ins Mittelfeld zu Team Rot.",
     dr("n10", "b1", [47, 42.5]), mv("r14", [47.5, 46], delay=0.3), pf("b1", [55, 48.5], after=True),
     mv("k2", [53.5, 54.6], after=True), ps("b1", [46.5, 56], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schulterblick im Mittelfeld.", "Schulterblick im Mittelfeld",
    "Der Flügelspieler von Team Rot zieht nach innen, genau in den Rücken unseres Mittelfelds. Schaut dort keiner über die Schulter, kommt der Pass durch die Mitte, und unser Innenverteidiger muss raus. Dann ist hinten ein Loch. Wer früh schaut, stellt den Passweg zu, und Team Rot muss quer spielen.",
    sp(r21=(18, 28.5)), [B("b1", *ROT["r20"])] + ERSATZ,
    [S("Flügel rückt ein, Schulterblick", "Spieler einundzwanzig zieht von außen nach innen, in den Rücken von Spieler zehn. Spieler zehn schaut über die Schulter und sieht ihn. Sofort schiebt er sich in den Passweg.",
       mv("r21", [42, 28]), bl("n10", [44, 21], delay=0.4), mv("n10", [47.5, 30.5], after=True)),
     S("Der Ball muss quer", "Durch die Mitte geht nichts mehr. Spieler zwanzig spielt quer zu Spieler zwölf. Der Torwart ruft rüber, und der ganze Block schiebt mit. Spieler drei läuft an.",
       pf("b1", ROT["r12"]), mv("n3", [84.5, 31], delay=0.5), mv("n8", [68, 30.5], delay=0.6), mv("n6", [57, 26.5], delay=0.6),
       mv("n5", [70, 21], delay=0.6))],
    dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Konter gemeinsam tragen.", "Den Konter gemeinsam tragen",
    "Nach dem Ballgewinn schalten Mittelfeld und Spitzen zusammen um. Der erste Pass geht nach vorn, die Spitze legt ab, und von hinten kommt einer im Sprint. Kurze, scharfe Pässe, und immer ist einer anspielbar. So wird aus vier gegen drei ein Treffer.",
    sp(), [B("b1", *NEON["n6"])] + ERSATZ,
    [S("Ball erobert, sofort steil", "Spieler sechs hat den Ball erobert. Er nimmt den Kopf hoch und spielt sofort steil auf Spieler neun. Spieler acht sprintet gleich mit nach vorn.",
       bl("n6", [50, 38]), pf("b1", NEON["n9"], after=True), mv("n8", [66, 37], delay=0.3), mv("n8", [58, 43], after=True)),
     S("Ablage auf den Nachrückenden", "Spieler neun legt ab auf Spieler acht. Gleichzeitig startet Spieler elf hinter Spieler sechzehn in die Tiefe.",
       pf("b1", [58, 43]), mv("n11", [61, 51.5], delay=0.2)),
     S("Steckpass in den Lauf: Punkt", "Spieler acht steckt durch in den Lauf von Spieler elf. Der schießt flach am Torwart vorbei, und das gibt einen Punkt für Team Neon.",
       pf("b1", [61, 51.5]), mv("k2", [55, 54], delay=0.3), ps("b1", [47, 56], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
