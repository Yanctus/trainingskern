import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-112 (U12-U14, Woche 1 Pre-Season): SAQ Circuit and 1 v 1 Games. 30 x 20 Yards = Feld x 12-84, y 6-54.
# Links Koordinationsparcours (Leitern und Hürden -> Minihürden, Stangen oben und unten), Mitte 1-gegen-1-Zone mit Minitor oben
# und unten, rechts Dribbelparcours (Dummys -> neongelbe Stangen). Gelb + Dunkelblau (Parcours, verteidigen) -> Neon 4, 5, 6, 8;
# Pink + Hellblau (Dribbler, greifen an) -> Rot 2, 3, 9, 7 (Hellblau 4 neu nummeriert: 9). Wartende neben dem Feld (3D-Abstand).
# Ein Trainer rechts mit Ersatzbällen. Kein Schulterblick im Original (Text, Ton und Video geprüft).
T = P("T", "c", 91, 30, "T")
POS = {"n4": (17, 51), "n5": (5, 51), "n6": (15, 9), "n8": (5, 9),
       "r2": (74, 8), "r3": (91, 9), "r9": (74, 52), "r7": (91, 51)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 94.5, 33.5)]
BAELLE = [B("b2", 75.4, 9.2), B("b9", 75.4, 53.2)] + ERSATZ
LINES = [rect(12, 6, 72, 48), line(34, 6, 34, 54), line(61, 6, 61, 54)]
KEGEL = [C(25, 12, shape="stange"), C(25, 46, shape="stange")] + [C(21.5, y, shape="huerde_ou") for y in (18, 23, 28, 33, 38)] \
      + [C(73.5, 13.5, shape="stange"), C(73.5, 46.5, shape="stange"),
         C(76.5, 21, "neon", shape="stange"), C(68.5, 29.5, "neon", shape="stange"), C(76.5, 38, "neon", shape="stange")]
OBEN, UNTEN = [47.5, 5.7], [47.5, 54.3]
TORE = [{"x": 47.5, "y": 6, "side": "top"}, {"x": 47.5, "y": 54, "side": "bottom"}]
def kette(f, who, wege, first=None, **k):
    return [f(who, wege[0], **(first or {}))] + [f(who, w, after=True) for w in wege[1:]]
def lauf(who, wege, **k): return kette(lambda w, t, **a: mv(w, t, **a), who, wege, **k)
def drib(who, ball, wege, **k): return kette(lambda w, t, **a: dr(w, ball, t, **a), who, wege, **k)
# Spieler vier: unten an der Stange vorbei, über die Minihürden nach oben, um die obere Stange herum
N_HOCH = [[21.5, 42], [21.5, 16], [24, 8.5], [28.5, 11]]
# Spieler zwei: im Slalom um die drei Dummys nach unten
R_RUNTER = [[81, 14], [81.5, 22], [72, 25.5], [64, 27.5], [64, 32.5], [72, 34], [82, 37], [80, 43]]

u = {"title": "Parcours, dann 1 gegen 1", "code": "UE-128", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 18 m",
 "description": "Zwei Spieler starten gleichzeitig von diagonal gegenüberliegenden Ecken. Der eine läuft links durch einen Koordinationsparcours mit Minihürden und Stangen, der andere dribbelt rechts im Slalom um drei Dummys. In der Mitte treffen sie sich zum 1 gegen 1: Der Dribbler greift das Minitor an, der Läufer verteidigt. Erobert der Verteidiger den Ball, kontert er aufs andere Minitor. Danach startet das nächste Paar von den anderen beiden Ecken.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern, geteilt in drei Zonen. Links ein Koordinationsparcours mit fünf Minihürden und je einer Stange oben und unten, in der Mitte die Duellzone mit einem Minitor oben und einem unten, rechts ein Dribbelparcours mit drei Dummys und zwei Stangen.",
  "Verteilen: Team Neon läuft den Parcours und verteidigt, Team Rot dribbelt und greift an. Je zwei Spieler stehen in jeder Ecke, die Roten haben die Bälle. Der Trainer steht rechts neben dem Feld mit Ersatzbällen.",
  "Ablauf: Auf Pfiff starten zwei Spieler aus diagonal gegenüberliegenden Ecken gleichzeitig. Neon von unten läuft den Parcours nach oben und verteidigt das obere Minitor, Rot von oben dribbelt den Slalom nach unten und greift das obere Minitor an. Danach starten Neon von oben und Rot von unten, dann geht es um das untere Minitor.",
  "Wertung: Jedes Tor ist ein Punkt für das Team. Erobert der Verteidiger den Ball, darf er sofort aufs andere Minitor kontern. Nach jedem Duell stellen sich beide wieder an."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und sauber durch den Parcours, mit kurzen Schritten", "Mit dem Außenrist eng um die Dummys dribbeln", "Im Duell zentral andribbeln, dann bleiben beide Seiten offen", "Als Verteidiger tief und seitlich stehen, geduldig bleiben und nach außen drängen"],
 "materials": ["5 Minihürden (oder 2 Koordinationsleitern)", "4 Stangen", "3 Dummys", "2 Minitore", "Mehrere Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Parcours, dann eins gegen eins. Erst Tempo und Koordination im Parcours, dann geht es in der Mitte direkt ins Duell.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Beide durch den Parcours", "Auf Pfiff starten Spieler vier und Spieler zwei gleichzeitig. Spieler vier läuft über die Minihürden nach oben und um die Stange herum, Spieler zwei dribbelt im Slalom um die Dummys nach unten.",
     *lauf("n4", N_HOCH), *drib("r2", "b2", R_RUNTER, first={"delay": 0.15})),
   S("Rein ins Duell", "Dann geht es in die Mitte: Spieler zwei dribbelt aufs obere Minitor zu, Spieler vier sprintet ihm entgegen und stellt sich ihm vor dem Minitor in den Weg.",
     *lauf("n4", [[46, 24], [51, 21]]), *drib("r2", "b2", [[70, 42.5], [62, 40], [59, 28]], first={"delay": 0.15})),
   S("Abschluss: Punkt", "Spieler zwei zieht am Verteidiger vorbei und schießt ins Minitor, und das gibt einen Punkt für Team Rot. Hätte Spieler vier den Ball erobert, dürfte er aufs untere Minitor kontern.",
     dr("r2", "b2", [56, 18]), ps("b2", OBEN, after=True)),
   S("Das nächste Paar", "Jetzt starten Spieler sechs und Spieler neun aus den anderen beiden Ecken: Spieler sechs läuft den Parcours nach unten, Spieler neun dribbelt nach oben. Ihr Duell geht ums untere Minitor, danach sind Spieler fünf und Spieler drei dran.",
     *lauf("n6", [[21.5, 17], [21.5, 40]]), *drib("r9", "b9", [[81, 46], [81.5, 38]], first={"delay": 0.15}))],
  "dims": dims(12, 84, 6, 54, "27 m", "18 m", rx=97)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Im Duell zentral andribbeln.", "Zentral andribbeln",
    "Wer an der Seite andribbelt, wird vom Verteidiger leicht nach außen gedrängt. Zieht der Angreifer zur Mitte, bleiben ihm beide Seiten offen, und der Verteidiger muss sich festlegen. Dann mit einer Finte oder einem schnellen Richtungswechsel auf die andere Seite gehen.",
    sp(n4=(46, 24), r2=(62, 40)), [B("b2", 62.6, 40.6), B("b9", 75.4, 53.2)] + ERSATZ,
    [S("Zur Mitte ziehen", "Spieler zwei dribbelt nicht an der Seite entlang, sondern zieht in die Mitte. Spieler vier muss sich festlegen und schiebt nach rechts.",
       dr("r2", "b2", [54, 32]), mv("n4", [54, 27], after=True)),
     S("Andere Seite, Punkt", "Spieler zwei geht mit einem schnellen Richtungswechsel links vorbei und schießt ins Minitor, und das gibt einen Punkt für Team Rot. Dann startet das nächste Paar.",
       dr("r2", "b2", [47, 28]), dr("r2", "b2", [46, 18], after=True), ps("b2", OBEN, after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Geduldig verteidigen und nach außen drängen.", "Geduldig verteidigen",
    "Der Verteidiger springt nicht blind in den Zweikampf. Er steht tief und seitlich, lenkt den Angreifer an die Seite weg vom Tor und wartet auf einen zu weiten Ballkontakt. Dann erobert er den Ball und kontert sofort aufs andere Minitor.",
    sp(n4=(46, 24), r2=(62, 40)), [B("b2", 62.6, 40.6), B("b9", 75.4, 53.2)] + ERSATZ,
    [S("Nach außen drängen", "Spieler vier stellt sich tief und seitlich vor Spieler zwei und drängt ihn an die Seite. Spieler zwei dribbelt an der Linie entlang nach oben.",
       mv("n4", [54, 26]), dr("r2", "b2", [59, 30], delay=0.15), dr("r2", "b2", [59.5, 23], after=True)),
     S("Ball erobern, Konter: Punkt", "Spieler zwei legt sich den Ball zu weit vor. Spieler vier erobert ihn, kontert sofort und schießt ins untere Minitor, und das gibt einen Punkt für Team Neon. Dann startet das nächste Paar.",
       ps("b2", [58.6, 15.6]), mv("n4", [58, 15.4], after=True), dr("n4", "b2", [50, 26], after=True), dr("n4", "b2", [48, 40], after=True), ps("b2", UNTEN, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Duelle gleichzeitig.", "Zwei Duelle gleichzeitig",
    "Jetzt starten alle vier zugleich, jeder läuft nur die halbe Strecke durch seinen Parcours. In der Mitte laufen zwei Duelle auf einmal, eins aufs obere und eins aufs untere Minitor. Es gibt weniger Platz und weniger Pause, und die Verteidiger müssen sofort den Raum zumachen.",
    sp(n4=(15, 24), n6=(15, 40), r2=(82, 38), r9=(82, 22)), [B("b2", 82.6, 38.6), B("b9", 82.6, 22.6)] + ERSATZ,
    [S("Alle vier starten", "Alle vier starten gleichzeitig. Spieler vier läuft nach oben, Spieler sechs nach unten, Spieler zwei dribbelt unten um den Dummy, Spieler neun oben.",
       *lauf("n4", [[21.5, 17], [24, 8.5], [28.5, 11], [44, 24]]), *lauf("n6", [[21.5, 42], [23, 50.5], [28.5, 48.5], [46, 36]]),
       *drib("r2", "b2", [[81, 44], [70, 42.5], [62, 40]], first={"delay": 0.15}), *drib("r9", "b9", [[80, 16], [62, 20]], first={"delay": 0.15})),
     S("Zwei Duelle auf einmal", "Spieler zwei greift das obere Minitor an, Spieler neun das untere. Spieler vier und Spieler sechs machen sofort den Raum vor ihrem Tor zu.",
       mv("n4", [51, 21]), mv("n6", [47, 40]), dr("r2", "b2", [59, 28], delay=0.15), dr("r9", "b9", [53, 26], delay=0.15), dr("r9", "b9", [52, 38], after=True)),
     S("Zwei Abschlüsse: Punkte", "Beide Roten setzen sich durch und treffen, und das gibt zwei Punkte für Team Rot. Dann starten Spieler fünf, Spieler acht, Spieler drei und Spieler sieben.",
       dr("r2", "b2", [56, 18]), ps("b2", OBEN, after=True), dr("r9", "b9", [55, 45], delay=0.15), ps("b9", UNTEN, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
