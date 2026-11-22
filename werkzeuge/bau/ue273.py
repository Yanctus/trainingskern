import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P25 (U12-U14, Einzeltraining): Create in the Final Third - CAM / Combine to Create in the Final Third. 20 x 20 Yards =
# Feld x 25-75, y 5-55 (18 x 18 m). Ausrichtung wie im PDF: zwei Minitore oben in den Ecken (im PDF schräg, hier gerade mit
# Öffnung nach unten), Puppe (passiver Verteidiger) als Stange gezeichnet in der Mitte, oben ein Hütchen, unten ein Stangentor aus zwei
# Stangen, darunter der Trainer auf einem Hütchen mit Bällen. Spieler (P, orange) -> Spieler sieben von Team Neon (Zehner).
# Spieler etwas höher und Trainer etwas tiefer als im PDF (3D-Abstand), Stangentor dafür auf Höhe des Spielers.
# Ablauf Grundform wie im PDF (rechte Seite): Prallpass mit dem Trainer, um die rechte Stange laufen, Pass vom Trainer mit dem
# hinteren Fuß annehmen, auf die Puppe zu dribbeln, Pass gegen die Laufrichtung (reverse pass) ins nahe Minitor rechts. Danach
# dieselbe Folge zur anderen Seite (nur im Text).
# Kein Wettbewerb (Technikübung): statt Punkten ein Ziel (Ball im Minitor).
# Sichtkegel: Video zeigt beim Pass gegen die Laufrichtung einen Kegel ("Disguise the reverse pass, use hips and eyes"): der
# Spieler schaut in seine Laufrichtung (an der Puppe vorbei zur anderen Seite) und spielt dann zur Gegenseite. Eingebaut in der
# Grundform (Blick nach links oben, Pass nach rechts) und in der zweiten Steigerung (Blick nach links, Pass an die Wand).
# Prallwand (bounce board) in den Steigerungen als kurze durchgezogene Linie oben in der Mitte (dort, wo in der Grundform das
# Hütchen steht); in den Steigerungen ist das obere Hütchen weg.
# Fassungen: Steigerung 1 Doppelpass mit der Prallwand und Abschluss ins linke Minitor (PDF Seite 2, Video ab 0:48),
# Steigerung 2 Pass an die Wand gegen die Laufrichtung und Abschluss ins rechte Minitor (PDF Seite 2, Video ab 1:25).
T = P("T", "c", 50, 52, "T")
def sp(x=50, y=36):
    return [P("n7", "a", x, y, "7"), T]
ERSATZ = [B("s1", 54, 53), B("s2", 56.5, 53)]
TBALL = [50.6, 52.6]
LINES = [rect(25, 5, 50, 50)]
WAND = line(47, 12, 53, 12, dashed=False)
TORE = [{"x": 32, "y": 5, "side": "top"}, {"x": 68, "y": 5, "side": "top"}]
FEST = [C(50, 23, shape="stange"), C(44, 37, shape="stange"), C(56, 37, shape="stange"), C(46, 53.5)]
CONES = FEST + [C(50, 14)]
FEST_ID = [dict(c, id="h%d" % i) for i, c in enumerate(FEST)]  # Fassungen ohne oberes Hütchen: dann brauchen alle Hütchen eine id
EMPFANG = (65, 40)

u = {"title": "Zehner täuscht an der Puppe", "code": "UE-273", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Eine Übung für den Zehner mit dem Trainer. Nach einem Prallpass läuft der Spieler um eine Stange, nimmt den Pass vom Trainer offen an und dribbelt auf eine Puppe zu. Dort täuscht er mit Augen und Hüfte an und spielt den Ball gegen seine Laufrichtung ins nahe Minitor. Danach geht es zur anderen Seite.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben in den Ecken zwei Minitore, in der Mitte eine Puppe, unten ein Stangentor aus zwei Stangen.",
  "Verteilen: Der Spieler steht im Stangentor. Der Trainer steht unten auf einem Hütchen mit den Bällen.",
  "Ablauf: Prallpass mit dem Trainer, um eine Stange laufen, den Pass offen annehmen, auf die Puppe zu dribbeln und gegen die Laufrichtung ins nahe Minitor passen.",
  "Wechsel: Nach jedem Ball läuft der Spieler zurück zum Stangentor und macht dasselbe zur anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Augen und Hüfte täuschen, dann erst passen", "Den Körper öffnen und mit dem hinteren Fuß annehmen", "Im richtigen Moment passen, scharf und genau", "Schnell zurück und die Seite wechseln"],
 "materials": ["2 Stangen", "1 Puppe", "2 Minitore", "2 Hütchen", "1 Prallwand", "Einige Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Zehner täuscht an der Puppe. Spieler sieben dribbelt auf eine Puppe zu und spielt den Ball überraschend gegen seine Laufrichtung ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *TBALL)] + ERSATZ,
  "steps": [
   S("Prallpass", "Der Trainer passt zu Spieler sieben im Stangentor. Spieler sieben spielt direkt zurück.",
     ps("b1", [50.6, 36.6]), ps("b1", TBALL, after=True)),
   S("Um die Stange", "Jetzt läuft Spieler sieben um die rechte Stange und öffnet seinen Körper. Der Trainer passt, und er nimmt den Ball mit dem hinteren Fuß an.",
     mv("n7", [57.5, 32.5]), mv("n7", list(EMPFANG), after=True), ps("b1", [65.6, 40.6], after=True)),
   S("Auf die Puppe zu", "Spieler sieben dribbelt schräg nach innen direkt auf die Puppe zu.",
     dr("n7", "b1", [55, 29.5])),
   S("Gegen die Laufrichtung", "Er schaut nach links und tut so, als ob er dorthin spielt. Dann passt er nach rechts ins nahe Minitor. Ziel geschafft! Danach läuft er zurück zum Stangentor, und es geht zur anderen Seite.",
     bl("n7", [40, 16]), ps("b1", [68, 5.5], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=83)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Doppelpass mit der Prallwand.", "Doppelpass mit der Wand",
    "Oben in der Mitte steht jetzt eine Prallwand. An der Puppe spielt der Spieler mit dem Außenrist an die Wand und läuft an der Puppe vorbei. Er nimmt den Ball im Lauf mit und passt ins andere Minitor.",
    sp(*EMPFANG), [B("b1", 65.6, 40.6)] + ERSATZ,
    [S("Auf die Puppe zu", "Spieler sieben hat den Ball vom Trainer angenommen und dribbelt auf die Puppe zu.",
       dr("n7", "b1", [59, 29.5])),
     S("Doppelpass mit der Wand", "Mit dem Außenrist spielt er an die Prallwand und läuft sofort an der Puppe vorbei. Der Ball prallt zurück in seinen Lauf.",
       ps("b1", [50.3, 12.8]), mv("n7", [50, 29.5], after=True), mv("n7", [42, 27.5], after=True), ps("b1", [42.6, 28.1], after=True)),
     S("Ins linke Minitor", "Spieler sieben nimmt den Ball im Lauf mit und passt genau ins linke Minitor. Dann geht es zurück zum Stangentor.",
       ps("b1", [32, 5.5]))],
    lines=LINES + [WAND], cones=FEST_ID),
  V("Steigerung", "Und jetzt die zweite Steigerung: Erst täuschen, dann an die Wand.", "Täuschen, dann Wand",
    "Jetzt kommt beides zusammen. Der Spieler zieht nach links, täuscht und spielt den Ball gegen die Laufrichtung an die Prallwand. Dann läuft er an der Puppe vorbei und passt ins nahe Minitor.",
    sp(*EMPFANG), [B("b1", 65.6, 40.6)] + ERSATZ,
    [S("Nach links ziehen", "Spieler sieben dribbelt unter der Puppe vorbei nach links.",
       dr("n7", "b1", [58, 31.5]), dr("n7", "b1", [42, 28], after=True)),
     S("Täuschen, an die Wand", "Er schaut nach links, als ob er weiter dribbelt, und spielt dann gegen die Laufrichtung an die Prallwand. Sofort läuft er an der Puppe vorbei nach rechts.",
       bl("n7", [28, 18]), ps("b1", [50.3, 12.8], after=True), mv("n7", [50, 30.5], after=True), mv("n7", [58, 29.5], after=True), ps("b1", [58.6, 30.1], after=True)),
     S("Ins rechte Minitor", "Der Ball prallt in seinen Lauf, und Spieler sieben passt direkt ins nahe rechte Minitor. Dann geht es zurück zum Stangentor.",
       ps("b1", [68, 5.5]))],
    lines=LINES + [WAND], cones=FEST_ID)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
