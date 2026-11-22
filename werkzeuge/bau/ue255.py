import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P3 (U12-U14, Torwarttraining): Goalkeeper Handling and Quick Feet. 30 x 45 Yards, gedreht: im PDF liegen die Minitore
# links, hier oben. Feld x 8-92, y 4-56 (41 x 27 m), die Linie zwischen Wurf- und Laufzone gestrichelt bei y 32.5.
# Drei Bahnen nebeneinander (links x 22, Mitte x 50, rechts x 78), je Bahn ein Minitor oben, ein Zuspieler daneben, eine Puppe
# (Stange) in der Mitte und zwei Hütchen (neon) zum Fangen und Hechten. Laufstationen wie im PDF: unten im PDF Hütchen-Slalom
# (hier links), Mitte Koordinationsleiter (Mitte), oben Minihürden (rechts). Torhüter grün 1, pink 1, gelb 13 -> k1 (links),
# k2 (Mitte), k3 (rechts), im Text "der linke/mittlere/rechte Torwart". Drei Trainer im Original: ein Trainer (Mitte) und zwei
# Spieler von Team Neon als Zuspieler (Spieler sieben links, Spieler acht rechts; im Ton: "coach or fellow teammate").
# Abstände leicht vereinfacht (Hütchen symmetrisch zur Puppe). Wertung aus dem Ton ("Set challenges and scores"): Wurf ins
# Minitor gibt einen Punkt für den Torwart.
# Sichtkegel aus dem Text ("anticipate when they are about to strike"): Der Torwart schaut vor dem Volley zum Schützen
# (Grundform und erster Coaching-Punkt). Im Video kein Kegel eingezeichnet; Richtung aus dem Sinn.
T = P("T", "c", 55, 9, "T")
LANES = {"k1": 22, "k2": 50, "k3": 78}
SCHUETZE = {"k1": ("n7", "b7"), "k2": ("T", "b1"), "k3": ("n8", "b8")}
POS = {"k1": (22, 53.5), "k2": (50, 53.5), "k3": (78, 53.5), "n7": (27, 9), "n8": (83, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 59.5, 7), B("s2", 59.5, 10)]
BAELLE = [B("b7", 27.6, 9.6), B("b1", 55.6, 9.6), B("b8", 83.6, 9.6)] + ERSATZ
LINES = [rect(8, 4, 84, 52), line(8, 32.5, 92, 32.5)]
CONES = ([C(22, y) for y in (37, 41, 45, 49)] + [leiter(50, 42, senkrecht=True)] + [C(78, y, shape="huerde_ou") for y in (37, 41, 45, 49)]
         + [C(L + d, 30, "neon") for L in LANES.values() for d in (7, -7)] + [C(L, 20, shape="stange") for L in LANES.values()])
TORE = [{"x": L - 5, "y": 5, "side": "top"} for L in LANES.values()]

def station(k):
    L = LANES[k]
    if k == "k1":  # Slalom durch die Hütchen
        return [mv(k, [25, 49]), mv(k, [19, 45], after=True), mv(k, [25, 41], after=True), mv(k, [19, 37], after=True), mv(k, [22, 33], after=True)]
    return [mv(k, [L, 33])]
def volley(k, blick=True):
    L = LANES[k]; s, b = SCHUETZE[k]
    out = [mv(k, [L + 7, 28.5])]
    if blick: out.append(bl(k, [L + 5, 11], after=True))
    return out + [ps(b, [L + 7.6, 29.1], after=True)]
def zurueck(k):
    L = LANES[k]; s, b = SCHUETZE[k]
    return [ps(b, [L + 5.6, 9.6]), mv(k, [L + 2.5, 22], after=True), mv(k, [L - 7, 28.5], after=True)]
def hechten(k):
    L = LANES[k]; s, b = SCHUETZE[k]
    return [ps(b, [L - 10.4, 29.6]), mv(k, [L - 11, 29], delay=0.3)]
def wurf(k):
    L = LANES[k]; s, b = SCHUETZE[k]
    return [ps(b, [L - 5, 5.5], delay=0.4)]
def alle(f, **k):
    return [m for kk in LANES for m in f(kk, **k)]

u = {"title": "Hechten und ins Minitor werfen", "code": "UE-255", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 5, "players_max": 5,
 "field_size": "41 x 27 m",
 "description": "Drei Torhüter arbeiten gleichzeitig auf drei Bahnen. Jeder läuft zuerst durch eine Laufstation mit Hütchen, Leiter oder Hürden und fängt dann einen Volley. Danach läuft er um eine Puppe, hechtet auf einen flachen Schuss und hält den Ball fest. Zum Schluss steht er schnell auf und wirft den Ball ins Minitor, das gibt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 27 Metern mit drei Bahnen. Unten je eine Laufstation: Hütchen-Slalom, Koordinationsleiter, Minihürden. Oben je eine Puppe, zwei Hütchen und ein Minitor.",
  "Verteilen: Drei Torhüter stehen unten an den Laufstationen. Oben neben jedem Minitor steht ein Schütze mit Bällen: links Spieler sieben, in der Mitte der Trainer, rechts Spieler acht.",
  "Ablauf: Alle drei laufen gleichzeitig durch ihre Station, gehen seitlich zum ersten Hütchen und fangen den Volley. Sie rollen den Ball zurück, laufen zur Puppe und weiter zum zweiten Hütchen. Dort hechten sie auf den flachen Schuss und werfen den Ball dann ins Minitor.",
  "Wertung und Wechsel: Jeder Wurf ins Minitor gibt einen Punkt für den Torwart. Danach joggen alle locker zurück, machen eine kurze Pause und wechseln die Bahn."],
 "organisation_show": ORG,
 "coaching_points": ["Sauber und mit schnellen Füßen durch die Laufstation", "Den Schuss ahnen und den Volley fest fangen", "Schnell hechten und den Ball festhalten", "Schnell aufstehen und genau ins Minitor werfen"],
 "materials": ["3 Minitore", "3 Puppen oder Stangen", "1 Koordinationsleiter", "4 Minihürden", "10 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Hechten und ins Minitor werfen. Drei Torhüter laufen gleichzeitig durch ihre Station, fangen, hechten und werfen den Ball ins Minitor.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Durch die Stationen", "Alle drei Torhüter starten gleichzeitig. Der linke läuft Slalom durch die Hütchen, der mittlere durch die Leiter und der rechte springt über die Hürden.",
     *alle(station)),
   S("Volley fangen", "Jetzt gehen alle seitlich zum ersten Hütchen und schauen zum Schützen. Der Volley kommt, und jeder Torwart fängt ihn fest.",
     *alle(volley)),
   S("Zurück und zur Puppe", "Jeder rollt den Ball zurück zum Schützen. Dann laufen alle zur Puppe und seitlich weiter zum zweiten Hütchen.",
     *alle(zurueck)),
   S("Hechten und halten", "Jetzt kommt ein flacher Schuss zur Seite. Jeder Torwart hechtet und hält den Ball fest.",
     *alle(hechten)),
   S("Ins Minitor: Punkt", "Schnell aufstehen und den Ball ins Minitor werfen. Jeder Treffer gibt einen Punkt für den Torwart. Dann joggen alle locker zurück, und nach einer kurzen Pause wechselt jeder auf die nächste Bahn.",
     *alle(wurf))],
  "dims": dims(8, 92, 4, 56, "41 m", "27 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Schuss ahnen.", "Den Schuss ahnen",
    "Der Torwart schaut genau auf den Schützen. Holt der aus, steht der Torwart schon still und ist bereit. So fängt er den Volley sicher und lässt ihn nicht abprallen.",
    sp(k2=(50, 33)), BAELLE,
    [S("Hinschauen", "Der mittlere Torwart geht seitlich zum ersten Hütchen. Er schaut genau auf den Trainer: Wann holt er aus?",
       mv("k2", [57, 28.5]), bl("k2", [55, 11], after=True)),
     S("Bereit: fangen", "Der Trainer holt aus, und der Torwart steht schon still auf den Zehenspitzen. Er fängt den Volley fest mit beiden Händen.",
       ps("b1", [57.6, 29.1]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Hechten, festhalten, genau werfen.", "Hechten und genau werfen",
    "Beim Hechten landet der Torwart auf der Seite und drückt den Ball mit beiden Händen fest auf den Boden. Dann steht er sofort auf. Er wirft mit einer langen Armbewegung genau ins Minitor, so wie im Spiel beim Abwurf.",
    sp(k2=(43, 28.5)), BAELLE,
    [S("Hechten und halten", "Der Trainer schießt flach zur Seite. Der mittlere Torwart hechtet, landet auf der Seite und hält den Ball mit beiden Händen fest.",
       ps("b1", [39.6, 29.6]), mv("k2", [39, 29], delay=0.3)),
     S("Genau werfen: Punkt", "Er steht sofort auf und wirft mit langem Arm genau ins Minitor. Das gibt einen Punkt für den mittleren Torwart.",
       ps("b1", [45, 5.5], delay=0.4))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
