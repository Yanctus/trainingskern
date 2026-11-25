import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-1 (U15-U17, Woche 2 Pre-Season): Speed & Reactions Game. Kreis 20 x 20 Yards = 18 m Durchmesser (Mitte 50/30, r 26).
# Sechs Paare wie im PDF, aber nicht gleichmäßig verteilt: Stationen bei 0, 45, 135, 180, 225 und 315 Grad (oben und unten
# frei), außen Team Neon, innen Team Rot; die seitlichen Paare stehen etwas weiter außen. Grund: 3D-Abstand (zwölf Spieler und
# der Trainer in der Mitte, bei gleichmäßiger Verteilung verdecken sich die inneren Spieler).
# PDF navy -> Team Neon (2, 3, 5, 6, 8, 10 wie im PDF), pink -> Team Rot neu nummeriert, weil die Nummern doppelt sind:
# 4 -> 4, 9 -> 9, 10 -> 11, 6 -> 7, 5 -> 12, 3 -> 13.
# Rotes Hütchen -> oranges Hütchen (Ruf „Orange“), gelbes Hütchen -> neon Hütchen (Ruf „Gelb“), weißes Leibchen auf der Stange
# (auf der Tafel nicht darstellbar, nur im Text, Ruf „Leibchen“).
# Seitlich nach links: Außen und innen bewegen sich gegenläufig je eine Station weiter (wie im Video), so gibt es neue Paare.
# Punkt für den Schnelleren ergänzt (Original: wer zuerst greift, gewinnt).
# Sichtkegel: Text „Eyes Forward, Head Up – Maintain vision and awareness“, im Video beim Coaching-Punkt eingezeichnet (Blick
# nach vorn zur Stange) und in der Steigerung (Blick von der Stange weg). Umdrehen in der Steigerung mit drehen().
# Neue Kegel-Regel (25.11.2026): Reaktionsspiel ohne Ball, niemand passt danach, daher alle Kegel gestrichen (Blick nur im Text).
T = P("T", "c", 50, 30, "T")
ERSATZ = [B("s1", 52.6, 33.5), B("s2", 47.4, 33.5)]
WIN = [0, 45, 135, 180, 225, 315]
RO = {0: 25.5, 180: 25.5}; RI = {0: 17, 180: 17}
def ro(a): return RO.get(a, 25)
def ri(a): return RI.get(a, 12)
def pt(a, r): return [round(50 + r * math.cos(math.radians(a)), 1), round(30 - r * math.sin(math.radians(a)), 1)]
def stange(a): return pt(a, (ro(a) + ri(a)) / 2)
def tang(a, d):
    s = stange(a); return [round(s[0] + d * math.sin(math.radians(a)), 1), round(s[1] + d * math.cos(math.radians(a)), 1)]
def kegel(a, farbe): return tang(a, 3.3 if farbe == "orange" else -3.3)
AUSSEN = {0: "n8", 45: "n10", 135: "n2", 180: "n3", 225: "n6", 315: "n5"}
INNEN = {0: "r11", 45: "r9", 135: "r4", 180: "r13", 225: "r12", 315: "r7"}
def sp(aussen=AUSSEN, innen=INNEN):
    return [P(i, "a", *pt(a, ro(a)), i[1:]) for a, i in aussen.items()] + \
           [P(i, "b", *pt(a, ri(a)), i[1:]) for a, i in innen.items()] + [T]
CONES = [C(*stange(a), shape="stange") for a in WIN] + [C(*kegel(a, "orange")) for a in WIN] + [C(*kegel(a, "neon"), "neon") for a in WIN]
LINES = [{"type": "circle", "x": 50, "y": 30, "r": 26}]
DIMS = [{"x1": 24, "y1": 58.6, "x2": 76, "y2": 58.6, "text": "18 m"}]
# Seitlich nach links: außen eine Station im Uhrzeigersinn, innen eine gegen den Uhrzeigersinn (auf dem Kreis entlang)
def bogen(who, a0, a1, rad, **k):
    d = (a1 - a0 + 540) % 360 - 180
    n = 2 if abs(d) > 60 else 1
    pts = [pt(a0 + d * j / (n + 1), rad(a0) + (rad(a1) - rad(a0)) * j / (n + 1)) for j in range(1, n + 1)] + [pt(a1, rad(a1))]
    return [mv(who, pts[0], **k)] + [mv(who, p, after=True) for p in pts[1:]]
def links():
    m = []
    for j, a in enumerate(WIN):
        m += bogen(AUSSEN[a], a, WIN[j - 1], ro)
        m += bogen(INNEN[a], a, WIN[(j + 1) % 6], ri)
    return m
NACH_AUSSEN = {WIN[j - 1]: AUSSEN[a] for j, a in enumerate(WIN)}
NACH_INNEN = {WIN[(j + 1) % 6]: INNEN[a] for j, a in enumerate(WIN)}
def zum(von, ziel, d):
    # Weg vom Spieler zum Hütchen, endet d vor dem Hütchen
    dx, dy = ziel[0] - von[0], ziel[1] - von[1]; l = math.hypot(dx, dy)
    return [round(ziel[0] - dx / l * d, 1), round(ziel[1] - dy / l * d, 1)]
def rennen(farbe, aussen, innen, sieger, ziel=None):
    m = []
    for a in WIN:
        z = ziel(a) if ziel else kegel(a, farbe)
        for i, p in ((aussen[a], pt(a, ro(a))), (innen[a], pt(a, ri(a)))):
            if i in sieger: m.append(mv(i, zum(p, z, 1.6), delay=0.1))
            else: m.append(mv(i, zum(p, z, 3.6), delay=0.3))
    return m
def zurueck(aussen, innen):
    return [mv(i, pt(a, ro(a))) for a, i in aussen.items()] + [mv(i, pt(a, ri(a))) for a, i in innen.items()]
SIEGER = {"n10", "r11", "n3", "r4", "n5", "r12"}

u = {"title": "Farbe hören, schneller greifen", "code": "UE-321", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 16,
 "field_size": "Kreis, 18 m Durchmesser",
 "description": "Ein Reaktionsspiel für die Vorbereitung. Je zwei Spieler stehen sich im Kreis gegenüber, dazwischen eine Stange mit einem orangen und einem gelben Hütchen und einem Leibchen obendrauf. Auf Zuruf gehen alle seitlich zur nächsten Station, dann ruft der Trainer eine Farbe. Wer das richtige Teil zuerst greift, holt einen Punkt für sein Team.",
 "organisation": ["Aufbauen: Ein Kreis mit 18 Metern Durchmesser. Darin stehen sechs Stangen im Kreis verteilt, an jeder ein oranges und ein gelbes Hütchen und oben auf der Stange ein Leibchen.",
  "Verteilen: Zwei Teams zu sechst. An jeder Stange ein Paar, Team Neon steht außen, Team Rot innen, beide schauen zur Stange. Der Trainer steht in der Mitte.",
  "Ablauf: Alle stehen tief und mittig. Ruft der Trainer links oder rechts, gehen alle seitlich zur nächsten Stange, mal langsam, mal schnell. Außen und innen laufen dabei gegeneinander, so wechselt der Gegner. Ruft er orange, gelb oder Leibchen, greift jeder sofort zu.",
  "Wertung und Wechsel: Wer das richtige Teil zuerst hat, holt einen Punkt für sein Team. Dann alles zurück an die Stange und die nächste Ansage. Nach einigen Runden tauschen außen und innen."],
 "organisation_show": ORG,
 "coaching_points": ["Tief stehen, Gewicht auf den Fußballen", "Kopf hoch, Augen nach vorn", "Seitlich gehen, Füße nicht kreuzen", "Der erste Schritt ist explosiv"],
 "materials": ["6 Stangen", "6 orange Hütchen", "6 gelbe Hütchen", "6 Leibchen", "Hütchen für den Kreis"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Farbe hören, schneller greifen. Ein Reaktionsspiel zu zweit. Der Trainer ruft eine Farbe, und wer zuerst das richtige Teil an der Stange hat, gewinnt das Duell.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Tief stehen, Augen nach vorn", "Je zwei Spieler stehen sich gegenüber, dazwischen die Stange. Team Neon außen, Team Rot innen. Alle stehen tief, die Knie gebeugt, und schauen nach vorn zur Stange."),
   S("Ruf links: eine Station weiter", "Der Trainer ruft links. Alle gehen seitlich zur nächsten Stange, ohne die Füße zu kreuzen. Außen und innen laufen gegeneinander, und jeder hat einen neuen Gegner.",
     *links()),
   S("Ruf orange: alle greifen zu", "Jetzt ruft er orange. Sofort sprinten alle los zum orangen Hütchen an ihrer Stange. Schauen wir auf Spieler zehn und Spieler sieben.",
     *rennen("orange", NACH_AUSSEN, NACH_INNEN, SIEGER)),
   S("Wer zuerst greift: Punkt", "Spieler zehn hat das Hütchen zuerst, und das gibt einen Punkt für Team Neon. Alle stellen das Hütchen zurück und gehen wieder an ihre Stange. Dann kommt die nächste Ansage.",
     *zurueck(NACH_AUSSEN, NACH_INNEN))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Tief und mittig stehen.", "Tief und mittig stehen",
    "Wer aufrecht steht, verliert den ersten Schritt. Die Knie sind gebeugt, das Gewicht liegt auf den Fußballen, der Körper steht mittig zwischen beiden Hütchen. Der Blick geht nach vorn, nicht zum Trainer.",
    sp(), ERSATZ,
    [S("Tief, mittig, Blick nach vorn", "Spieler acht steht tief und genau mittig vor seiner Stange. Er schaut nach vorn, nicht zum Trainer. Gegenüber steht Spieler elf noch zu aufrecht."),
     S("Ruf gelb: Punkt", "Der Trainer ruft gelb. Spieler acht ist mit dem ersten Schritt sofort weg und greift das gelbe Hütchen vor Spieler elf, und das gibt einen Punkt für Team Neon.",
       *rennen("neon", AUSSEN, INNEN, {"n8", "r9", "n2", "r13", "n6", "r7"}))]),
  V("Steigerung", "Und jetzt die Steigerung: Mit dem Rücken zur Stange.", "Mit dem Rücken zur Stange",
    "Jetzt stehen alle mit dem Rücken zur Stange, Team Neon schaut nach außen, Team Rot zum Trainer. Auf den Ruf drehen sie sich um, finden ihre Stange und greifen zu. Ruft der Trainer Leibchen, geht es nach oben zum Leibchen auf der Stange.",
    sp(), ERSATZ,
    [S("Rücken zur Stange", "Alle drehen der Stange den Rücken zu. Spieler acht schaut nach außen, Spieler elf schaut in die Mitte. Sehen können sie die Stange jetzt nicht mehr."),
     S("Ruf Leibchen: umdrehen", "Der Trainer ruft Leibchen. Alle drehen sich blitzschnell um und suchen ihre Stange.",
       *[drehen(i, stange(a)) for a, i in AUSSEN.items()], *[drehen(i, stange(a), gegen=True) for a, i in INNEN.items()]),
     S("Wer das Leibchen hat: Punkt", "Dann hoch zum Leibchen. Spieler elf reißt es vor Spieler acht von der Stange, und das gibt einen Punkt für Team Rot.",
       *rennen("leibchen", AUSSEN, INNEN, {"r11", "n10", "r4", "n3", "r12", "n5"}, ziel=stange))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
