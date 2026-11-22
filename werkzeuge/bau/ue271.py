import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P1 (U12-U14, Einzeltraining): Ball Mastery Circuit / Dribbling Between Cones Circuit. 15 x 15 Yards = Feld x 25-75,
# y 5-55 (14 x 14 m). Ausrichtung wie im PDF: Start oben, vier Hütchen oben, drei Stangen quer in der Mitte, vier Hütchen unten.
# Spieler (P, pink) -> Spieler sieben von Team Neon, Trainer C rechts neben dem Feld mit zwei Ersatzbällen.
# Reihenfolge wie im PDF: obere Hütchen -> Stange rechts (im Original "pole on their left side", der Spieler dribbelt nach unten,
# also aus Sicht der Tafel rechts) -> untere Hütchen und zurück zur Mitte -> Stange links -> zurück zum Start.
# Abweichung: Im PDF läuft der Spieler unten um das letzte Hütchen herum und links zurück; hier dreht er nach dem letzten Hütchen
# (links daran vorbei) und dribbelt links gerade zurück zur Mitte (gleicher Weg, ohne Schleife). Hütchen mit 5,5 Abstand, damit
# die Slalom-Wege sauber an den Hütchen vorbeiführen.
# Kein Wettbewerb (reine Technikübung): statt Punkten ein Ziel (sauber und schnell durch den Parcours).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: zwei Coaching-Punkte aus PDF Seite 2 (beide Füße im Slalom, kurze schnelle Schritte an der Stange).
T = P("T", "c", 86, 30, "T")
START = (50, 5)
def sp(x=START[0], y=START[1]):
    return [P("n7", "a", x, y, "7"), T]
ERSATZ = [B("s1", 86.6, 33.6), B("s2", 89.6, 33.6)]
LINES = [rect(25, 5, 50, 50)]
OBEN = [9, 14.5, 20, 25.5]
UNTEN = [34.5, 40, 45.5, 51]
CONES = ([C(50, y) for y in OBEN] + [C(50, y) for y in UNTEN]
         + [C(29, 30, shape="stange"), C(50, 30, shape="stange"), C(71, 30, shape="stange")])
def ball(x, y): return [B("b1", x + 0.6, y + 0.6)] + ERSATZ
def weg(punkte, erst=False):
    return [dr("n7", "b1", list(p), after=(None if (erst and k == 0) else True)) for k, p in enumerate(punkte)]
SLALOM_OBEN = [(46, 9), (54, 14.5), (46, 20), (54, 25.5)]
RECHTS = [(68, 27), (73.5, 28), (73.5, 32), (68, 33), (55, 33)]
SLALOM_UNTEN = [(54, 34.5), (46, 40), (54, 45.5), (46, 51), (46, 33)]
LINKS = [(32, 33), (26.5, 32), (26.5, 28), (32, 27), (46, 27.5)]
ZURUECK = [(46, 8), START]

u = {"title": "Hütchen-Slalom und drei Stangen", "code": "UE-271", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 12, "players_min": 1, "players_max": 1,
 "field_size": "14 x 14 m",
 "description": "Ein Dribbel-Parcours für einen Spieler mit dem Trainer. Der Spieler dribbelt durch vier Hütchen, mit Tempo um eine Stange und zurück, durch vier weitere Hütchen und um die zweite Stange. Danach dribbelt er zurück zum Start und macht eine kurze Pause. So bekommt er sehr viele Ballkontakte mit beiden Füßen.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern. Oben und unten je vier Hütchen in einer Reihe, dazwischen quer drei Stangen: links, in der Mitte und rechts.",
  "Verteilen: Der Spieler startet oben mit Ball vor den Hütchen. Der Trainer steht rechts neben dem Feld mit Bällen.",
  "Ablauf: Durch die oberen Hütchen, um die rechte Stange und zurück zur Mitte, durch die unteren Hütchen und zurück, um die linke Stange und zurück, dann zurück zum Start.",
  "Wechsel: Nach jeder Runde macht der Spieler eine kurze Pause. Dann startet die nächste Runde, wenn der Trainer es sagt."],
 "organisation_show": ORG,
 "coaching_points": ["Mit beiden Füßen durch die Hütchen dribbeln", "Mit Tempo zur Stange und wieder zurück", "Kurze, schnelle Schritte um die Stangen", "Die ganze Runde mit vollem Einsatz, dann kurz erholen"],
 "materials": ["8 Hütchen", "3 Stangen", "Einige Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Hütchen-Slalom und drei Stangen. Spieler sieben dribbelt allein durch einen Parcours aus Hütchen und Stangen.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": ball(*START),
  "steps": [
   S("Obere Hütchen", "Spieler sieben startet oben und dribbelt im Slalom durch die vier Hütchen. Er nimmt dabei beide Füße.",
     *weg(SLALOM_OBEN, erst=True)),
   S("Rechte Stange", "Jetzt dribbelt er mit Tempo zur rechten Stange, macht kleine Schritte um die Stange und dribbelt zurück zur Mitte.",
     *weg(RECHTS, erst=True)),
   S("Untere Hütchen", "Dann geht es im Slalom durch die vier unteren Hütchen. Danach dreht er und dribbelt zurück zur Mitte.",
     *weg(SLALOM_UNTEN, erst=True)),
   S("Linke Stange", "Jetzt mit Tempo zur linken Stange, eng um die Stange herum und wieder zurück zur Mitte.",
     *weg(LINKS, erst=True)),
   S("Zurück zum Start: Pause", "Zum Schluss dribbelt Spieler sieben zurück zum Start. Die Runde ist geschafft. Er macht eine kurze Pause, dann ist er wieder dran.",
     *weg(ZURUECK, erst=True))],
  "dims": dims(25, 75, 5, 55, "14 m", "14 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Beide Füße benutzen.", "Mit beiden Füßen",
    "Im Slalom nimmt der Spieler den Ball abwechselnd mit dem linken und dem rechten Fuß mit. Erst sauber und langsam, dann schneller. So wird er mit beiden Füßen sicher am Ball.",
    sp(), ball(*START),
    [S("Links und rechts", "Am ersten Hütchen nimmt Spieler sieben den Ball mit dem linken Fuß mit, am zweiten mit dem rechten Fuß.",
       *weg(SLALOM_OBEN[:2], erst=True)),
     S("Erst sauber, dann schnell", "So geht es weiter, immer abwechselnd. Erst kommt die Technik, dann das Tempo. Am Ende ist er an der Mitte.",
       *weg(SLALOM_OBEN[2:], erst=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Kurze, schnelle Schritte an der Stange.", "Klein um die Stange",
    "Zur Stange hin darf der Spieler den Ball weiter vorlegen und Tempo machen. An der Stange macht er ganz kurze, schnelle Schritte und hält den Ball eng am Fuß. Danach wieder mit Tempo zurück.",
    sp(*SLALOM_OBEN[-1]), ball(*SLALOM_OBEN[-1]),
    [S("Mit Tempo hin", "Spieler sieben legt sich den Ball weiter vor und dribbelt mit Tempo zur rechten Stange.",
       dr("n7", "b1", list(RECHTS[0]))),
     S("Kurze Schritte", "An der Stange macht er kurze, schnelle Schritte. Der Ball bleibt ganz eng am Fuß.",
       *weg(RECHTS[1:4], erst=True)),
     S("Mit Tempo zurück", "Dann legt er den Ball wieder weiter vor und dribbelt mit Tempo zurück zur Mitte.",
       dr("n7", "b1", list(RECHTS[4])))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
