import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P3 (U12-U14, Einzeltraining): Heading Accuracy, Reactions and Speed (Ordner "Heading Reactions Sprints 1 to 1-P3").
# 10 x 20 Yards = Feld x 37.5-62.5, y 5-55 (9 x 18 m). Ausrichtung wie im Original (Stangen oben, Trainer unten, nicht gedreht).
# Spieler P -> Spieler sieben (Team Neon). Startquadrat aus vier Hütchen, drei Stangen oben. Im Original sind die Stangen blau,
# rot und gelb und der Trainer ruft eine Farbe. Stangen dürfen hier nur orange/neon sein: deshalb ruft der Trainer „links“,
# „Mitte“ oder „rechts“ (gleiche Reaktionsaufgabe). Die gelbe Markierung neben dem Trainer -> neon Hütchen.
# Keine Wertung im Original: Ziel statt Punkte (acht genaue Kopfbälle, dann Pause). 1 gegen 1: ein Spieler, players 1-1.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; „process colour information“ ist ein Zuruf, kein Schauen).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (genau köpfen, Ton: kurze und hohe Bälle; Sprinttempo halten).
T = P("T", "c", 52.5, 53.5, "T")
POS = {"n7": (50, 35)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 44.5, 52), B("s2", 42, 54)]
BAELLE = [B("b1", 53.1, 54.1)] + ERSATZ
LINES = [rect(37.5, 5, 25, 50)]
CONES = [C(40.5, 11, shape="stange"), C(50, 16, shape="stange"), C(59.5, 11, shape="stange"),
         C(46.5, 29), C(54, 29), C(46.5, 40), C(54, 40), C(48.5, 53.5, "neon")]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
RECHTS = [[51, 27], [57, 16], [57, 8], [61, 7], [62, 12]]
LINKS = [[49, 27], [43, 16], [43, 8], [39, 7], [38.5, 12]]
ZURUECK_R = [[52, 24], [50, 34]]
ZURUECK_L = [[48, 24], [50, 34]]

u = {"title": "Kopfball und Sprint auf Zuruf", "code": "UE-280", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Kondition"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "9 x 18 m",
 "description": "Ein Spieler trainiert allein mit dem Trainer Kopfball, Reaktion und Schnelligkeit. Der Trainer wirft den Ball hoch, und der Spieler köpft ihn genau in seine Hände zurück. Dann ruft der Trainer eine Stange, und der Spieler sprintet um diese Stange und zurück ins Quadrat. Nach acht Runden gibt es eine Pause.",
 "organisation": ["Aufbauen: Ein Feld von neun mal achtzehn Metern. In der Mitte liegt ein kleines Quadrat aus vier Hütchen, oben stehen drei Stangen: links, in der Mitte und rechts.",
  "Verteilen: Der Spieler steht im Quadrat. Der Trainer steht unten mit einem Ball in der Hand und weiteren Bällen daneben.",
  "Ablauf: Der Trainer wirft den Ball hoch, der Spieler köpft ihn zurück in seine Hände. Dann ruft der Trainer links, Mitte oder rechts. Der Spieler sprintet um diese Stange und zurück ins Quadrat.",
  "Wechsel: Nach acht Runden hat der Spieler eine Pause und erholt sich. Danach beginnt die nächste Serie."],
 "organisation_show": ORG,
 "coaching_points": ["Mit der Stirn köpfen und den Ball genau in die Hände des Trainers bringen", "Gut zuhören und sofort zur gerufenen Stange starten", "Eng um die Stange sprinten und schnell wieder bereit sein", "In der Pause ruhig durchatmen und erholen"],
 "materials": ["3 Stangen", "5 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Kopfball und Sprint auf Zuruf. Ein Spieler köpft dem Trainer den Ball zurück und sprintet dann um die Stange, die der Trainer ruft.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Ball hoch werfen", "Spieler sieben steht im Quadrat. Der Trainer wirft den Ball hoch zu ihm.",
     ps("b1", [50.6, 35.6])),
   S("Zurück köpfen", "Spieler sieben springt ab und köpft den Ball mit der Stirn genau zurück in die Hände des Trainers.",
     ps("b1", [53.1, 54.1])),
   S("Trainer ruft: rechts", "Sofort ruft der Trainer: rechts! Spieler sieben dreht sich und sprintet um die rechte Stange.",
     *weg("n7", RECHTS)),
   S("Zurück ins Quadrat", "Dann sprintet er zurück ins Quadrat und stellt sich für den nächsten Kopfball. So geht es acht Runden. Ziel ist, jeden Ball genau in die Hände zu köpfen. Danach hat Spieler sieben Pause, und dann ist er wieder dran.",
     *weg("n7", ZURUECK_R))],
  "dims": dims(37.5, 62.5, 5, 55, "9 m", "18 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau in die Hände köpfen.", "Genau in die Hände köpfen",
    "Der Trainer wirft mal kurz, mal hoch und mal zur Seite. Bei kurzen Bällen köpft der Spieler weich, bei hohen springt er ab. Jeder Kopfball soll genau in den Händen des Trainers landen, nicht zu kurz und nicht zu weit.",
    sp(), BAELLE,
    [S("Kurzer Ball", "Der Trainer wirft kurz. Spieler sieben geht nach vorn und köpft den Ball weich zurück in die Hände des Trainers.",
       ps("b1", [51.1, 38.1]), mv("n7", [50.5, 37.5]), ps("b1", [53.1, 54.1], after=True)),
     S("Hoher Ball", "Jetzt wirft der Trainer hoch über ihn. Spieler sieben geht zurück, springt ab und köpft den Ball fest und genau in die Hände.",
       mv("n7", [50, 32]), ps("b1", [50.6, 32.6]), ps("b1", [53.1, 54.1], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Volles Tempo bis zur letzten Runde.", "Volles Tempo bis zum Schluss",
    "Jeder Sprint geht mit vollem Tempo, auch in der achten Runde. Eng um die Stange laufen, kurz abbremsen und wieder Gas geben. Erholt wird erst in der Pause.",
    sp(), BAELLE,
    [S("Trainer ruft: links", "Der Trainer ruft: links! Spieler sieben startet sofort und sprintet mit vollem Tempo eng um die linke Stange.",
       *weg("n7", LINKS)),
     S("Mit Tempo zurück", "Mit vollem Tempo zurück ins Quadrat. Nach acht Runden darf er sich ausruhen, vorher nicht.",
       *weg("n7", ZURUECK_L))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
