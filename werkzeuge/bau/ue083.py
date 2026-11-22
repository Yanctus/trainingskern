import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P32: 15 x 20 Yards, gedreht: Feld x 14-86, y 6-54. Zwei gespiegelte Strecken (Neon oben, Rot unten, y -> 60 - y), Minitor in der Mitte (Öffnung nach rechts), Hütchen rechts.
T = P("T", "c", 92, 15, "T")
def m(p): return [p[0], round(60 - p[1], 1)]
ringe = [(20.3, 13.1), (26.6, 11.7), (32.1, 15.1)]
lines = [rect(14, 6, 72, 48)] + [{"type": "circle", "x": x, "y": y, "r": 3} for x, y in ringe] + [{"type": "circle", "x": x, "y": 60 - y, "r": 3} for x, y in ringe]
cones = [C(47.4, 13.4, "neon", shape="stange"), C(74.8, 13.4, "neon", shape="stange"), C(47.4, 46.6, "neon", shape="stange"), C(74.8, 46.6, "neon", shape="stange"), C(79, 30)]
goals = [{"x": 53.3, "y": 30, "side": "left"}]
def spieler(n1=(11.5, 12), r5=(11.5, 48)):
    return [P("n1", "a", *n1, "1"), P("n2", "a", 3, 14, "2"), P("r5", "b", *r5, "5"), P("r6", "b", 3, 46, "6"), T]
def lauf(who, pts, typ="lauf", ball=None):
    out = []
    for i, p in enumerate(pts):
        q = p if who[0] == "n" else m(p)
        out.append(mv(who, q, typ, after=i > 0 or None, ball=ball))
    return out
r1 = [(20.3, 13.1), (26.6, 11.7), (32.1, 15.1)]
r2 = [(44, 18), (50, 16.5), (50.5, 10), (56, 12.5), (61.4, 12.8)]
r3 = [(70, 9), (78, 10), (78.5, 18), (77, 26)]
u = {"title": "Das große Autorennen", "code": "UE-083", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Dribbling", "Torschuss"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 4, "players_max": 12, "field_size": "18 x 14 m",
 "description": "Ein Wettrennen eins gegen eins auf zwei gleichen Strecken. Die Kinder hüpfen durch Reifen, laufen um eine Stange, holen sich den Ball, dribbeln um die letzte Stange bis zum Hütchen und schießen aufs Minitor in der Mitte. Wer zuerst trifft, gewinnt das Rennen. Treffen beide nicht, holen sie schnell den Ball und schießen noch einmal.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern mit zwei gleichen Strecken nebeneinander: je drei Reifen, eine Stange, ein Ball und eine zweite Stange. In der Mitte ein Minitor, davor ein Hütchen.",
  "Verteilen: Zwei Mannschaften, jede stellt sich an den Start ihrer Strecke.",
  "Ablauf: Auf das Startzeichen rennen die beiden Ersten gleichzeitig los: durch die Reifen hüpfen, um die Stange laufen, den Ball holen, um die letzte Stange dribbeln und am Hütchen aufs Minitor schießen.",
  "Sieger: Wer zuerst trifft, holt einen Punkt für seine Mannschaft. Die Mannschaft mit den meisten Siegen gewinnt. Zusatzpunkte gibt es fürs laute Anfeuern, und Motorengeräusche sind ausdrücklich erlaubt."],
 "organisation_show": ORG,
 "coaching_points": ["Sauber und schnell durch die Reifen hüpfen", "Eng um die Stange laufen, zur Not mit der Hand an der Stange", "Den Ball beim Dribbeln eng am Fuß führen", "Genau schießen statt hetzen, und die Mitspieler feuern laut an"],
 "materials": ["6 Reifen", "4 Stangen", "1 Minitor", "1 Hütchen", "Bälle für jede Strecke"],
 "access": "frei", "hidden": True,
 "say_intro": "Das große Autorennen. Zwei Kinder rennen gleichzeitig, und wer zuerst ins Minitor trifft, gewinnt.",
 "board": {"lines": lines, "cones": cones, "goals": goals, "players": spieler(), "balls": [B("b1", 63, 13.4), B("b5", 63, 46.6), B("c1", 94.5, 16)],
  "steps": [
   S("Durch die Reifen", "Auf los rennen beide gleichzeitig los und hüpfen durch die drei Reifen.", *lauf("n1", r1), *lauf("r5", r1)),
   S("Um die Stange zum Ball", "Gleichzeitig laufen beide einmal um die Stange und holen sich ihren Ball.", *lauf("n1", r2), *lauf("r5", r2)),
   S("Um die letzte Stange", "Mit dem Ball dribbeln beide um die letzte Stange bis zum Hütchen.", *lauf("n1", r3, "dribbling", "b1"), *lauf("r5", r3, "dribbling", "b5")),
   S("Wer trifft zuerst", "Beide schießen aufs Minitor. Spieler eins trifft zuerst, und das gibt einen Punkt für Neon.",
     ps("b1", [54.5, 28.5]), ps("b5", [56, 38], delay=0.3))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "18 m"}, {"x1": 99, "y1": 6, "x2": 99, "y2": 54, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ganz eng und schnell um die Stange laufen.", "Eng um die Stange",
    "An der Stange wird das Rennen entschieden. Wer eng und schnell herumläuft, notfalls mit einer Hand an der Stange, ist früher am Ball und hat beim Dribbeln einen Vorsprung. Wer einen weiten Bogen läuft, verliert Zeit.",
    spieler((33, 15), (33, 45)), [B("b1", 63, 13.4), B("b5", 63, 46.6), B("c1", 94.5, 16)],
    [S("Eng herum", "Spieler eins läuft ganz eng um die Stange. Spieler fünf läuft gleichzeitig einen weiten Bogen.",
       *lauf("n1", [(45, 17), (49.5, 15.5), (49.5, 11), (52, 12.5)]), *lauf("r5", [(42, 17), (50, 20), (54, 14), (50, 6.5)])),
     S("Vorsprung beim Ball", "Spieler eins ist zuerst am Ball und dribbelt schon los, Spieler fünf kommt später.",
       mv("n1", [61.4, 12.8]), dr("n1", "b1", [70, 9], after=True), mv("r5", [61.4, 47.2], delay=0.4))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Treffen beide nicht, schnell den Ball holen und noch einmal schießen.", "Daneben, also schnell holen",
    "Geht der Schuss daneben, ist das Rennen noch nicht vorbei. Sofort hinterher, den Ball holen, zurück zum Hütchen dribbeln und noch einmal schießen. Wer schneller reagiert und dann genau schießt, gewinnt.",
    spieler((71, 24), (80, 36)), [B("b1", 72.6, 24.6), B("b5", 78.4, 36.6), B("c1", 94.5, 16)],
    [S("Beide daneben", "Beide schießen gleichzeitig, und beide Bälle gehen am Minitor vorbei.", ps("b1", [56, 20]), ps("b5", [57, 41])),
     S("Schnell holen", "Gleichzeitig rennen beide hinterher, holen ihren Ball und dribbeln zurück zum Hütchen.",
       mv("n1", [58, 20]), dr("n1", "b1", [72, 24], after=True), mv("r5", [59, 42]), dr("r5", "b5", [72, 38], after=True)),
     S("Wer zuerst trifft", "Spieler eins schießt zuerst und trifft, und das gibt einen Punkt für Neon.", ps("b1", [54.5, 28.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
