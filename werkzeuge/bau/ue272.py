import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P2 (U12-U14, Einzeltraining): Control Turn Drive / First Touch, Sharp Turns and Speed. 10 x 20 Yards = Feld x 37.5-62.5,
# y 5-55 (9 x 18 m). Ausrichtung wie im PDF: Trainer unten auf einem Hütchen mit Bällen, Quadrat aus vier Hütchen in der Mitte,
# zwei Stangen oben. Spieler (P, pink) -> Spieler sieben von Team Neon. Quadrat etwas größer gezeichnet als im PDF (sonst zu eng
# für Figur und Ball).
# Ablauf wie im PDF: hoher Pass (Chip) vom Trainer, Annahme im Quadrat, aufdrehen, um eine der beiden Stangen (Grundform links wie
# im PDF, im zweiten Coaching-Punkt rechts) und zurück ins Quadrat, dann Pass oder Chip zurück zum Trainer.
# Kein Wettbewerb (reine Technikübung): statt Punkten ein Ziel (Ball im Quadrat behalten, genau zurückspielen).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; im Video nur "Too heavy!" mit dunklem Kreis um den Spieler).
# Fassungen: zwei Coaching-Punkte. Erstens weich annehmen und im Quadrat behalten (PDF Seite 2, Video "Focus on 1st touch to
# remain in square"), zweitens Seite wählen, große Ballkontakte hin und zurück, kleine um die Stange (PDF Zusammenfassung).
T = P("T", "c", 52, 51, "T")
SPIELER = (50, 29)
def sp(x=SPIELER[0], y=SPIELER[1]):
    return [P("n7", "a", x, y, "7"), T]
ERSATZ = [B("s1", 56.5, 50.5), B("s2", 58.5, 52.5)]
LINES = [rect(37.5, 5, 25, 50)]
CONES = ([C(45.5, 25), C(54.5, 25), C(45.5, 33), C(54.5, 33), C(47.5, 51.5)]
         + [C(41.5, 10, shape="stange"), C(58.5, 10, shape="stange")])
TBALL = [52.6, 51.6]
def weg(punkte):
    return [dr("n7", "b1", list(p), after=(True if k else None)) for k, p in enumerate(punkte)]
LINKS = [(44, 12.5), (43.5, 7.5), (39.5, 7.5), (39.5, 12)]
RECHTS = [(56, 12.5), (56.5, 7.5), (60.5, 7.5), (60.5, 12)]

u = {"title": "Hohen Ball annehmen und los", "code": "UE-272", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Dribbling", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "9 x 18 m",
 "description": "Der Trainer spielt einen hohen Ball zum Spieler, der in einem kleinen Quadrat steht. Der Spieler nimmt den Ball mit Kopf, Brust, Oberschenkel oder Fuß an und behält ihn im Quadrat. Dann dreht er auf, dribbelt mit Tempo um eine der beiden Stangen und zurück. Zum Schluss passt oder chippt er den Ball zurück zum Trainer.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 18 Metern. In der Mitte ein kleines Quadrat aus vier Hütchen, oben zwei Stangen, unten ein Hütchen für den Trainer.",
  "Verteilen: Der Spieler steht im Quadrat. Der Trainer steht unten auf dem Hütchen mit den Bällen.",
  "Ablauf: Der Trainer chippt den Ball zum Spieler. Der Spieler nimmt ihn im Quadrat an, dreht auf, dribbelt um eine Stange und zurück ins Quadrat und spielt den Ball zum Trainer zurück.",
  "Wechsel: Es geht immer weiter, Ball für Ball, bis der Trainer eine kurze Pause ruft."],
 "organisation_show": ORG,
 "coaching_points": ["Weich annehmen, damit der Ball im Quadrat bleibt", "Nach der Annahme schnell aufdrehen und eine Seite wählen", "Kleine Ballkontakte um die Stange, große auf dem Weg hin und zurück", "Genau zurück zum Trainer passen oder chippen"],
 "materials": ["5 Hütchen", "2 Stangen", "Einige Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Hohen Ball annehmen und los. Spieler sieben nimmt einen hohen Ball im Quadrat an und dribbelt mit Tempo um eine Stange.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", *TBALL)] + ERSATZ,
  "steps": [
   S("Hoher Pass", "Der Trainer chippt den Ball hoch zu Spieler sieben ins Quadrat.",
     ps("b1", [50.6, 29.6])),
   S("Im Quadrat annehmen", "Spieler sieben nimmt den Ball mit Brust, Oberschenkel oder Fuß an. Der Ball bleibt im Quadrat.",
     dr("n7", "b1", [49, 27.5])),
   S("Aufdrehen und los", "Jetzt dreht er schnell auf und dribbelt mit Tempo zur linken Stange.",
     *weg(LINKS[:1])),
   S("Um die Stange", "Mit kleinen Schritten geht es eng um die Stange. Dann dribbelt er mit Tempo zurück ins Quadrat.",
     *weg(LINKS[1:] + [(42, 29), (49, 29)])),
   S("Zurück zum Trainer", "Spieler sieben chippt den Ball genau zurück zum Trainer. Das war eine Runde. Dann kommt gleich der nächste hohe Ball, bis der Trainer eine Pause ruft.",
     ps("b1", TBALL))],
  "dims": dims(37.5, 62.5, 5, 55, "9 m", "18 m", rx=70)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Weich annehmen.", "Weich annehmen",
    "Der erste Kontakt entscheidet. Der Spieler nimmt den Ball weich mit dem Körperteil an, das am besten passt. Ist der Kontakt zu fest, springt der Ball aus dem Quadrat.",
    sp(), [B("b1", *TBALL)] + ERSATZ,
    [S("Der hohe Ball", "Der Trainer chippt den Ball hoch zu Spieler sieben. Er schaut, wie der Ball kommt: Kopf, Brust, Oberschenkel oder Fuß?",
       ps("b1", [50.6, 29.6])),
     S("Weich, nicht zu fest", "Spieler sieben gibt mit der Brust etwas nach. So fällt der Ball direkt vor seine Füße und bleibt im Quadrat. Zu fest wäre der Ball weg.",
       dr("n7", "b1", [49.5, 28]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Seite wählen und Tempo machen.", "Seite wählen, Tempo",
    "Nach der Annahme entscheidet der Spieler schnell, um welche Stange er dribbelt. Hin und zurück nimmt er große Ballkontakte und macht Tempo. Um die Stange macht er kleine Kontakte.",
    sp(51, 27.5), [B("b1", 51.6, 28.1)] + ERSATZ,
    [S("Nach rechts", "Diesmal dreht Spieler sieben nach rechts auf und legt sich den Ball weit vor. Mit Tempo geht es zur rechten Stange.",
       dr("n7", "b1", list(RECHTS[0]))),
     S("Kleine Kontakte", "Um die Stange macht er ganz kleine Kontakte, der Ball bleibt eng am Fuß.",
       *weg(RECHTS[1:])),
     S("Mit Tempo zurück", "Dann wieder große Kontakte und mit Tempo zurück ins Quadrat. Von dort spielt er den Ball zum Trainer.",
       *weg([(58, 29), (51, 29)]), ps("b1", TBALL, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
