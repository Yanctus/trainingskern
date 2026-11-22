import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P27 (U12-U14, Einzeltraining): SAQ Activation. Fläche 2 x 2 Yards (ca. 2 x 2 m), stark vergrößert gezeichnet:
# Feld x 30-70, y 10-50. Ausrichtung wie im PDF: Grundform läuft von links nach rechts (nicht nach oben gedreht, damit die
# Seitschritte unter den Hürden wie im Original liegen). Blauer Spieler -> Spieler sieben (Team Neon). Im Original ist kein
# Trainer zu sehen, er steht hier links neben der Fläche (Pflichtfigur). Zwei Minihürden ("huerde", quer überlaufen), etwa
# einen Meter auseinander. Ablauf nach PDF und Video (0:13-0:28): einbeinig über die erste Hürde, Hop über die zweite, beidbeinig
# landen, schnelle Seitschritte im Zickzack zurück zum Start. Reine Koordinationsübung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: Coaching-Punkt "Explode immediately after landing" (PDF Seite 1, Ton 1:03), Steigerung (PDF Seite 2, Video
# 0:33-0:45): Hürden umgestellt, eine liegt quer unten rechts ("huerde_ou", von unten nach oben überlaufen), eine links in der
# Mitte. Hop über die untere Hürde, schnelle Füße nach oben, Hop zur linken Hürde, mit links darüber, beidbeinig zurück,
# schnelle Füße zurück zum Start. Die Reihenfolge im PDF-Bild ist nicht ganz eindeutig, hier nach Text und Video.
T = P("T", "c", 20, 44, "T")
def sp(x, y): return [P("n7", "a", x, y, "7"), T]
ERSATZ = [B("s1", 23.5, 48.5), B("s2", 23.5, 51)]
LINES = [rect(30, 10, 40, 40)]
HUERDEN = [C(44, 30, shape="huerde"), C(55, 30, shape="huerde")]
ZICKZACK = [[57, 39], [53, 35], [49, 39], [45, 35], [41, 39]]

u = {"title": "Hürdensprünge, seitlich zurück", "code": "UE-291", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "ca. 2 x 2 m",
 "description": "Eine kleine Aktivierung für Schnelligkeit, Wendigkeit und schnelle Füße. Der Spieler springt einbeinig über die erste Hürde, hüpft über die zweite und landet auf beiden Füßen. Dann geht es mit schnellen Seitschritten zurück zum Start. Nach einigen Runden gibt es eine Pause.",
 "organisation": ["Aufbauen: Zwei Minihürden, etwa einen Meter auseinander, auf einer Fläche von zwei mal zwei Metern.",
  "Verteilen: Spieler sieben steht links vor der ersten Hürde. Der Trainer steht daneben und schaut auf die Technik.",
  "Ablauf: Einbeinig über die erste Hürde, Hop über die zweite, beidbeinig landen. Dann mit schnellen Seitschritten im Zickzack zurück zum Start.",
  "Wechsel: Je nach Alter einige Runden am Stück, dann eine Pause. Bei zwei Spielern ist in der Pause der andere dran."],
 "organisation_show": ORG,
 "coaching_points": ["Jede Bewegung mit sauberer Technik", "Tempo und Rhythmus die ganze Zeit halten", "Kurze, schnelle Seitschritte mit flinken Füßen", "Nach der Landung sofort in die nächste Bewegung starten"],
 "materials": ["2 Minihürden"],
 "access": "abo", "hidden": True,
 "say_intro": "Hürdensprünge, seitlich zurück. Spieler sieben springt über zwei Hürden und kommt mit schnellen Seitschritten zurück.",
 "board": {"lines": LINES, "cones": HUERDEN, "players": sp(37, 30), "balls": ERSATZ,
  "steps": [
   S("Einbeinig über die Hürde", "Spieler sieben springt auf einem Bein über die erste Hürde.",
     mv("n7", [49.5, 30])),
   S("Hop und beidbeinig landen", "Gleich danach hüpft er über die zweite Hürde und landet auf beiden Füßen.",
     mv("n7", [61, 30])),
   S("Schnelle Seitschritte", "Jetzt geht es mit kurzen, schnellen Seitschritten im Zickzack zurück, unter den Hürden entlang.",
     *[mv("n7", p, after=(i > 0) or None) for i, p in enumerate(ZICKZACK)]),
   S("Zurück zum Start: Ziel", "Am Start beginnt er sofort die nächste Runde. Das Ziel: jede Runde sauber und schnell. Nach einigen Runden gibt es eine Pause, dann ist Spieler sieben wieder dran.",
     mv("n7", [37, 30]))],
  "dims": dims(30, 70, 10, 50, "2 m", "2 m", rx=76)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach der Landung sofort weiter.", "Landen und sofort weiter",
    "Der Spieler landet auf beiden Füßen und bleibt nicht stehen. Ohne Pause geht er direkt in die Seitschritte. So bleibt das Tempo hoch.",
    sp(49.5, 30), ERSATZ,
    [S("Beidbeinig landen", "Spieler sieben hüpft über die zweite Hürde und landet auf beiden Füßen, die Knie leicht gebeugt.",
       mv("n7", [61, 30])),
     S("Sofort zur Seite", "Ohne anzuhalten startet er sofort in die schnellen Seitschritte. Das Ziel: keine Pause zwischen Landung und Seitschritt.",
       *[mv("n7", p, after=(i > 0) or None) for i, p in enumerate(ZICKZACK[:3])])]),
  V("Steigerung", "Und jetzt die Steigerung: Die Hürden stehen anders.", "Neuer Hürden-Parcours",
    "Jetzt liegt eine Hürde quer unten rechts, die andere links in der Mitte. Der Spieler hüpft über die untere Hürde, macht schnelle Füße nach oben und hüpft zur linken Hürde. Dort steigt er mit links darüber, springt beidbeinig zurück und läuft mit schnellen Füßen zum Start.",
    sp(57, 47), ERSATZ,
    [S("Hop über die untere Hürde", "Spieler sieben hüpft auf dem rechten Bein über die untere Hürde.",
       mv("n7", [57, 36])),
     S("Schnelle Füße und Hop", "Mit schnellen Füßen geht es nach oben, dann hüpft er nach links zur zweiten Hürde.",
       mv("n7", [57, 30]), mv("n7", [47, 30], after=True)),
     S("Darüber und zurück", "Er steigt mit dem linken Fuß über die Hürde und springt beidbeinig wieder zurück.",
       mv("n7", [35, 30]), mv("n7", [47, 30], after=True)),
     S("Schnelle Füße zum Start: Ziel", "Mit schnellen Füßen läuft er an der unteren Hürde vorbei zurück zum Start. Das Ziel: den neuen Ablauf ohne Fehler und im Tempo schaffen.",
       mv("n7", [62, 36]), mv("n7", [62, 44], after=True), mv("n7", [57, 47], after=True))],
    cones=[C(41, 30, shape="huerde", id="h1"), C(57, 42, shape="huerde_ou", id="h2")])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
