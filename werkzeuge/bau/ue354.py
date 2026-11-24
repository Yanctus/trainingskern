import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 10-P10 (U15-U17, Woche 20 Phase 4): High Press Rondos. 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m): zwei Zonen von
# 20 x 30 Yards, dazwischen eine neutrale Zone von 5 Yards mit zwei Großfeldtoren Rücken an Rücken (je ein Torwart).
# FELD QUER (langes Feld, Vorbild ue317.py): wie im Video (dort quer), im PDF hochkant. Feld x 9-89, y 4-51; Zonengrenzen
# gestrichelt bei x 44.6 und 53.4. Das Tor der linken Zone steht an ihrer Grenze zur Mitte und öffnet nach links (side "right"),
# das Tor der rechten Zone öffnet nach rechts (side "left").
# Drei Teams zu sechst: Verteidiger (im PDF gelb) -> Team Neon 2, 5, 10 (wie im Video; die anderen drei warten in der
# Mittelzone, nur im Text: 3D-Abstand). Ballbesitz-Team in der rechten Zone (PDF pink/Video rot) -> Team Rot, neu nummeriert
# 11-16 (Nummern doppelt). Team in der linken Zone (PDF/Video blau) -> „das dritte Team“, neutrale Farbe (team t) mit
# Nummern 17-22 wie bei UE-341. Beide Torhüter neutral (k1, k2). Ein Trainer statt zwei, unten rechts an der Ecke.
# Ablauf nach PDF, Ton und Video (0:09-0:40): Trainer spielt in eine Zone, drei Verteidiger pressen (6 gegen 3); zehn Pässe,
# dann Abschluss; Ballgewinn -> sofort in die andere Zone, das Team mit dem Ballverlust schickt drei zum Pressen hinüber.
# Annahme: Beim Ballgewinn tauschen das ballverlierende Team und die Verteidiger die Rollen (übrige drei in die Mittelzone).
# Fassungen: PDF Key Coaching Point (nicht überpressen, kompakt bleiben) und Progression (Springer, Abschluss nur direkt nach
# Springer-Ablage). In der Steigerung nach dem Ton (1:03) vier je Team plus zwei Springer je Zone, weil sechs plus zwei
# Springer auf der Tafel keinen 3D-Abstand halten; im Text steht, dass es mit mehr Spielern auch sechs plus zwei geht.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 91.5, 55.3, "T")  # unten rechts an der Ecke, neben der Zone von Team Rot
ERSATZ = [B("s1", 94.5, 55.8), B("s2", 97, 55.8)]
NEON = {"n2": (49, 5), "n10": (49, 37), "n5": (49, 52.5)}
ROT = {"r11": (58.5, 12), "r12": (74, 6), "r13": (86, 15), "r14": (86, 38), "r15": (73, 48), "r16": (60, 48.5)}
DRITT = {"t17": (31, 6), "t18": (14, 10), "t19": (11.5, 29.5), "t20": (14, 47), "t21": (31, 48), "t22": (24, 27.5)}
TW = {"k1": (40.5, 27.5), "k2": (57.5, 27.5)}
def team(i): return {"n": "a", "r": "b", "t": "t", "k": "t", "f": "t"}[i[0]]
def lab(i): return "TW" if i[0] == "k" else "F" if i[0] == "f" else i[1:]
def sp(pos=None, **k):
    d = dict(pos or {**TW, **NEON, **ROT, **DRITT}); d.update(k)
    return [P(i, team(i), x, y, lab(i)) for i, (x, y) in d.items()] + [T]
def fu(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(9, 4, 80, 47), line(44.6, 4, 44.6, 51), line(53.4, 4, 53.4, 51)]
TORE = [{"x": 44.6, "y": 27.5, "side": "right", "size": "gross"}, {"x": 53.4, "y": 27.5, "side": "left", "size": "gross"}]
# Nur die Längen-Maßlinie (rechts stünde die Breite in der 3D-Ansicht neben Spieler vierzehn), die Breite steht in field_size
DIMS = dims(9, 89, 4, 51, "40 m", "25 m")[:1]
# Steigerung: vier je Team plus zwei Springer je Zone
POS2 = {**TW, "n2": (66, 27.5), "n10": (77, 24), "n5": (78.5, 40),
        "r12": (74, 6), "r13": (86, 15), "r14": (87.5, 36), "r15": (69, 49), "f1": (60, 10), "f2": (60, 46),
        "t17": (14, 10), "t18": (12, 30), "t19": (22, 47), "t20": (22, 26), "f3": (31, 10), "f4": (31, 45)}

u = {"title": "Hohes Pressing im Zonenrondo", "code": "UE-354", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 20,
 "field_size": "25 x 40 m",
 "description": "Drei Teams zu sechst und zwei Torhüter. In jeder Zone hält ein Team den Ball, drei Verteidiger pressen dagegen, also sechs gegen drei. Nach zehn Pässen darf das Team aufs Tor schießen. Erobern die Verteidiger den Ball, spielen sie ihn sofort in die andere Zone, und das Team, das ihn verloren hat, muss jetzt selbst pressen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern mit zwei Zonen und einer schmalen Mittelzone von 4,5 Metern. In der Mittelzone stehen zwei große Tore Rücken an Rücken, in jedem ein Torwart.",
  "Verteilen: Team Rot steht in der einen Zone, das dritte Team in der anderen. Die sechs Verteidiger von Team Neon warten in der Mittelzone. Der Trainer steht mit Bällen an der Ecke.",
  "Ablauf: Der Trainer spielt in eine Zone, und drei Verteidiger laufen sofort rein. Nach zehn Pässen in Folge darf das Team im Ballbesitz aufs Tor schießen. Danach bringt der Trainer einen Ball in die andere Zone, und die anderen drei Verteidiger pressen dort.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobern die Verteidiger den Ball, spielen sie ihn sofort in die andere Zone und haben jetzt selbst den Ball. Das Team mit dem Ballverlust wird zu Verteidigern: Drei sprinten zum Pressen hinüber, drei gehen in die Mittelzone."],
 "organisation_show": ORG,
 "coaching_points": ["Zu dritt anlaufen, nicht jeder für sich", "Mit dem Körper eine Seite zumachen", "Vollgas, dann macht der Gegner Fehler", "Laut mitzählen, ab zehn Pässen darf geschossen werden"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Hohes Pressing im Zonenrondo. Sechs gegen drei in zwei Zonen, dazwischen zwei Tore. Wer den Ball erobert, spielt ihn sofort in die andere Zone, und das Team mit dem Ballverlust muss pressen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 92.1, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein, drei laufen rein", "Der Trainer spielt in die Zone von Team Rot, zu Spieler vierzehn. Sofort laufen drei Verteidiger von Team Neon aus der Mittelzone rein. Jetzt heißt es sechs gegen drei.",
     ps("b1", fu(86, 38)), mv("n2", [66, 9.5], delay=0.3), mv("n10", [70, 26], delay=0.3), mv("n5", [70, 38], delay=0.3)),
   S("Zusammen pressen, Seite zu", "Team Rot zählt laut mit. Spieler vierzehn spielt hoch zu Spieler dreizehn. Die drei schieben zusammen rüber, Spieler zwei läuft so an, dass der Weg zurück zu ist.",
     ps("b1", fu(86, 15)), mv("n2", [79, 12], delay=0.3), mv("n10", [75, 21], delay=0.3), mv("n5", [74, 32], delay=0.3)),
   S("Ballgewinn, ab in die andere Zone", "Spieler dreizehn bleibt nur der Pass zu Spieler zwölf. Den fängt Spieler zehn ab und spielt sofort lang in die andere Zone. Team Rot hat den Ball verloren, also sprinten drei von Team Rot hinüber und pressen dort.",
     ps("b1", [80, 10.5]), mv("n10", [79.4, 9.9], delay=0.1), ps("b1", fu(31, 6), after=True),
     mv("r11", [36, 14], delay=1.0), mv("r16", [35, 40], delay=1.0), mv("r15", [27, 38], delay=1.0)),
   S("Zehn Pässe, dann Abschluss: Punkt", "Jetzt hält das dritte Team den Ball. Nach zehn Pässen spielt Spieler siebzehn zu Spieler zweiundzwanzig, und der schießt am Torwart vorbei. Das gibt einen Punkt für das dritte Team. Danach bringt der Trainer einen Ball in die andere Zone, und die anderen drei von Team Rot pressen dort.",
     ps("b1", fu(24, 27.5)), ps("b1", [44.6, 21.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nicht alle auf den Ball, kompakt bleiben.", "Nicht überpressen",
    "Rennen alle drei auf den Ball, ist hinter ihnen alles frei. Ein Pass, und der Gegner hat Platz und Zeit zum Abschluss. Darum läuft einer an, die anderen zwei bleiben eng dahinter und machen die Mitte zu. Kontrolliert pressen, nicht wild.",
    sp(), [B("b1", *fu(86, 15))] + ERSATZ,
    [S("Alle drei in die Ecke", "So nicht. Spieler dreizehn hat den Ball in der Ecke, und alle drei Verteidiger rennen auf ihn drauf. Ein Pass quer durch die Zone, und Spieler sechzehn steht völlig frei und hat alle Zeit zum Schießen.",
       mv("n2", [80, 12.5]), mv("n10", [78, 19]), mv("n5", [79.5, 25]), ps("b1", fu(60, 48.5), delay=1.0),
       dr("r16", "b1", [64, 37], after=True)),
     S("Zurück und eng zusammen", "Jetzt schnell zurück. Spieler fünf läuft Spieler sechzehn an, die anderen zwei stellen sich eng zwischen Ball und Tor. So kommt kein freier Schuss mehr.",
       mv("n5", [66, 31.5]), mv("n10", [62, 24], delay=0.2), mv("n2", [71, 22], delay=0.2))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Springer pro Zone, geschossen wird nur direkt nach ihrer Ablage.", "Springer legen auf",
    "In jede Zone kommen zwei Springer, die immer für das Team mit dem Ball spielen. Wenig Spieler? Dann vier je Team, mit mehr Spielern sechs plus zwei Springer. Nach zehn Pässen darf nur direkt nach einer Ablage vom Springer geschossen werden. Die Verteidiger müssen pressen und gleichzeitig den Pass zum Springer zustellen.",
    sp(POS2), [B("b1", *fu(86, 15))] + ERSATZ,
    [S("Springer spielen mit", "Vier von Team Rot und zwei Springer gegen drei. Spieler dreizehn spielt hoch zu Spieler zwölf, und Spieler zehn läuft ihn an. Der Springer bietet sich an der Seite an.",
       ps("b1", fu(74, 6)), mv("n10", [76, 12.5], delay=0.3), mv("n2", [64, 24], delay=0.4)),
     S("Ablage, direkt geschossen: Punkt", "Die zehn Pässe sind voll. Spieler zwölf spielt zum Springer und startet sofort. Die Ablage kommt in den Lauf, und Spieler zwölf schießt direkt ins Tor. Das gibt einen Punkt für Team Rot.",
       ps("b1", fu(60, 10)), mv("r12", [68, 17], delay=0.4), ps("b1", fu(68, 17), after=True), ps("b1", [53.4, 22.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
