import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 26-P3 (U12-U14, Woche 13 Phase 1): 4 V 3 Opposed Build-Up Game. 20 x 26 Yards = Feld x 31.25-68.75, y 5-55 (18 x 24 m),
# drei Zonen zu 8 Yards (gestrichelt) und unten eine Endzone von 2 Yards (orange Zone, Ziel von Team Rot), oben zwei Minitore.
# Ausrichtung wie im PDF (Neon spielt nach oben). Pink -> Neon (Torwart 1, Verteidiger 4 und 5, Sechser 6), dunkel -> Rot.
# Nummern neu: Rot 4 -> Rot 8 (im PDF doppelt mit Neon 4). Positionen auf ein Spaltenraster gesetzt (3D-Abstand).
# Nähe zu UE-052 "Spielaufbau 3 gegen 2" (gleiche Feldaufteilung, aber ohne Torwart und 3 gegen 2): hier eigene Einheit,
# Schwerpunkt Torwart im Spielaufbau, 4 gegen 3, Coaching-Punkt "Pass verstecken", Steigerung in beide Richtungen mit Springer.
# Sichtkegel: Im Video (Coaching-Punkt "Disguise pass to CDM") ist ein Kegel vom Torwart zum Verteidiger rechts eingezeichnet,
# im Ton "orienting their hips and eyes toward a trap pass": bl() vom Torwart zu Neon vier, dann Pass in den Sechser.
T = P("T", "c", 24, 44, "T")
POS = {"n1": (50, 51), "n5": (33.4, 41), "n4": (66.6, 41), "n6": (50, 22),
       "r8": (41.7, 16), "r9": (41.7, 36), "r10": (58.3, 35)}
def sp(**k):
    d = dict(POS); d.update(k)
    out = []
    for i, (x, y) in d.items():
        t = "t" if i[0] == "f" else ("a" if i[0] == "n" else "b")
        l = "TW" if i == "n1" else ("F" if i[0] == "f" else i[1:])
        out.append(P(i, t, x, y, l))
    return out + [T]
ERSATZ = [B("s1", 21, 47.5), B("s2", 24.6, 47.5)]
LINES = [rect(31.25, 5, 37.5, 50), line(31.25, 20.38, 68.75, 20.38), line(31.25, 35.77, 68.75, 35.77),
         {"type": "zone", "x": 31.25, "y": 51.15, "w": 37.5, "h": 3.85, "color": "orange"}]
TORE = [{"x": 37, "y": 5, "side": "top"}, {"x": 63, "y": 5, "side": "top"}]
TORE2 = TORE + [{"x": 37, "y": 55, "side": "bottom"}, {"x": 63, "y": 55, "side": "bottom"}]

u = {"title": "Torwart baut das Spiel auf", "code": "UE-169", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 7, "field_size": "18 x 24 m",
 "description": "Der Torwart, zwei Verteidiger und ein Sechser von Team Neon spielen sich gegen drei Spieler von Team Rot von hinten heraus. Der Torwart ist dabei der vierte Feldspieler: Er lockt einen Gegner an und spielt dann in die Lücke. Team Neon will durch alle Zonen in eines der beiden Minitore treffen. Erobert Team Rot den Ball, dribbelt es in die Endzone hinter dem Torwart.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 24 Metern, längs in drei gleich große Zonen geteilt. Unten eine schmale Endzone von zwei Metern, oben zwei Minitore.",
  "Verteilen: Team Neon mit Torwart, zwei Verteidigern und einem Sechser. Team Rot mit drei Spielern: zwei Stürmer vorn, einer hinter dem Sechser. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Jede Runde beginnt beim Torwart. Team Neon spielt sich von hinten durch die Zonen nach oben. Team Rot presst und will den Ball erobern.",
  "Wertung und Wechsel: Treffer ins Minitor gibt einen Punkt für Team Neon. Ein Dribbling von Team Rot in die Endzone gibt einen Punkt für Team Rot. Nach einigen Runden tauschen die Feldspieler die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Der Torwart steht mittig, damit er beide Verteidiger anspielen kann", "Die Verteidiger stehen versetzt und breit, so gibt es mehr Passwege", "Schnell und genau passen, sobald ein Spieler frei ist", "Der Sechser sucht sich die freie Lücke zwischen den Gegnern"],
 "materials": ["2 Minitore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Torwart baut das Spiel auf. Vier gegen drei, und der Torwart hilft mit, sich von hinten herauszuspielen.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(31.25, 5, 37.5, 50), "players": sp(), "balls": [B("b1", 50.6, 51.6)] + ERSATZ,
  "steps": [
   S("Zum Verteidiger", "Team Neon spielt nach oben. Der Torwart passt nach rechts zu Neon vier, und Rot zehn läuft ihn sofort an.",
     ps("b1", [67.2, 41.6]), mv("r10", [62, 38.5], delay=0.3)),
   S("Zurück zum Torwart", "Neon vier spielt zurück. Der Torwart geht ein Stück nach rechts und nimmt den Ball an.",
     mv("n1", [56, 50]), ps("b1", [56.6, 50.6], delay=0.2)),
   S("In die Lücke", "Rot zehn ist jetzt weit rechts. Der Torwart spielt flach durch die Lücke zu Neon sechs.",
     ps("b1", [50.6, 22.6])),
   S("Fünf startet", "Neon fünf startet nach vorn. Neon sechs spielt ihm den Ball in den Lauf.",
     mv("n5", [36, 27]), ps("b1", [36.6, 27.6], delay=0.4), mv("r8", [40, 21], delay=0.3)),
   S("Minitor: Punkt", "Neon fünf dribbelt in die letzte Zone und trifft ins linke Minitor, und das gibt einen Punkt für Team Neon. Holt Team Rot den Ball und dribbelt in die Endzone, gibt das einen Punkt für Team Rot. Danach beginnt der Torwart mit einem neuen Ball vom Trainer.",
     dr("n5", "b1", [35, 12]), ps("b1", [37, 5.3], after=True))],
  "dims": dims(31.25, 68.75, 5, 55, "18 m", "24 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Pass verstecken.", "Den Pass verstecken",
    "Der Torwart schaut zum Verteidiger und dreht die Hüfte dorthin, als ob er ihn anspielt. Der Stürmer glaubt das und läuft los. Jetzt ist in der Mitte eine Lücke, und der Torwart spielt in den Sechser.",
    sp(), [B("b1", 50.6, 51.6)] + ERSATZ,
    [S("Zu Vier schauen", "Der Torwart schaut zu Neon vier und dreht die Hüfte dorthin. Rot zehn glaubt das und läuft zu Neon vier.",
       bl("n1", [65, 40]), mv("r10", [61.5, 39.5], delay=0.4)),
     S("Doch in die Mitte", "Doch der Torwart spielt flach in die Mitte zu Neon sechs. Neon vier startet nach vorn.",
       ps("b1", [50.6, 22.6]), mv("n4", [64, 28], delay=0.3)),
     S("Minitor: Punkt", "Neon sechs spielt zu Neon vier. Der dribbelt hoch und trifft ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [64.6, 28.6]), dr("n4", "b1", [63, 12], after=True), ps("b1", [63, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Beide Teams greifen an.", "In beide Richtungen",
    "Jetzt stehen auch unten zwei Minitore. Der Torwart spielt als Springer mit dem Team am Ball, so ist es immer vier gegen drei. Erobert Team Rot den Ball, greift es sofort die unteren Tore an. Nach jedem Punkt spielt der Trainer einen neuen Ball ein.",
    [p for p in sp(f1=(50, 47), n5=(33.4, 38), n4=(66.6, 38), n6=(50, 19), r8=(41.7, 13), r9=(41.7, 30), r10=(58.3, 30)) if p["id"] != "n1"],
    [B("b1", 34, 38.6)] + ERSATZ,
    [S("Ball erobert", "Neon fünf will zu Neon sechs passen. Rot neun läuft in den Pass und erobert den Ball.",
       mv("r9", [39.5, 33]), ps("b1", [40.1, 33.6], delay=0.3)),
     S("Springer hilft Rot", "Jetzt greift Team Rot die unteren Tore an, und der Springer spielt mit Rot. Rot neun passt zum Springer, Rot zehn startet nach unten.",
       ps("b1", [50.6, 47.6]), mv("r10", [60, 45], delay=0.2), mv("n4", [66, 46], delay=0.4)),
     S("Unten: Punkt", "Der Springer spielt Rot zehn an, und der trifft ins rechte untere Minitor. Das gibt einen Punkt für Team Rot. Dann spielt der Trainer einen neuen Ball ein.",
       ps("b1", [60.6, 45.6]), ps("b1", [63, 54.7], after=True))],
    goals=TORE2)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
