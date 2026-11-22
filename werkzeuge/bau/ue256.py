import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P4 (U12-U14, Torwarttraining): Goalkeeper Handling and Shot Stopping. Strafraum 45 x 18 Yards = Feld x 5-95, y 5-42
# (41 x 16 m), Torraum x 30-70, y 5-17. Gedreht: im PDF liegt das Tor links, hier oben (wie im Video). Halbkreis weggelassen.
# Die Querstange zwischen zwei Stangen am linken Torraumeck als zwei Stangen plus orange Linie (Querstange) gezeichnet.
# Grüner Torwart 1 -> k1 (arbeitet). Die beiden anderen Torhüter des Originals (pink 1 wirft/schießt den Volley, gelb 13 schießt
# flach) sind nach der Torwart-Regel als Schützen von Team Neon gezeichnet: Spieler sieben (pink 1, neu nummeriert, sonst doppelt
# mit dem Torwart) und Spieler dreizehn. Der Trainer vorn schießt hoch. Der zweite Trainer (rechts neben dem Tor, ohne Aufgabe)
# und die weiße Markierung vor dem Tor sind weggelassen.
# Wertung aus dem Ton ("rewarding scores after each completed set ... forfeit"): Jeder gehaltene Ball gibt einen Punkt für den
# Torwart; wer am Ende die wenigsten Punkte hat, holt die Bälle (kindgerechte Aufgabe statt "forfeit").
# Keine Steigerung im Original: zwei Coaching-Punkte. Sichtkegel aus dem Text ("sets", "Bounce on toes to set for saves"):
# Der Torwart stellt sich und schaut zum Schützen, bevor der Schuss kommt. Im Video kein Kegel eingezeichnet; Richtung aus dem Sinn.
T = P("T", "c", 54, 35, "T")
POS = {"k1": (42, 21), "n7": (28, 34), "n13": (13, 13)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 58, 36), B("s2", 58, 39)]
def baelle(**k):
    d = {"b7": (28.6, 34.6), "b13": (13.6, 13.6), "b1": (54.6, 35.6)}; d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(5, 5, 90, 37), rect(30, 5, 40, 12), {"type": "line", "x1": 33, "y1": 13, "x2": 28.5, "y2": 20.5, "color": "orange"}]
CONES = [C(33, 13, shape="stange"), C(28.5, 20.5, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Unter der Stange zum Hechtsprung", "code": "UE-256", "kind": "Übungsform",
 "focuses": ["Koordination", "Schnelligkeit", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 3, "players_max": 3,
 "field_size": "41 x 16 m",
 "description": "Ein Torwart hält drei Bälle hintereinander: einen Volley, einen flachen Schuss und einen hohen Schuss. Zwischen den Bällen taucht er unter einer Querstange durch und stellt sich jedes Mal neu. Jeder gehaltene Ball gibt einen Punkt für den Torwart. Danach tauschen alle drei reihum die Rollen.",
 "organisation": ["Aufbauen: Ein Jugendtor mit Torraum. Am linken Torraumeck liegt eine Querstange auf zwei Stangen, so hoch, dass man sich darunter ducken muss.",
  "Verteilen: Der Torwart steht im Torraum rechts neben der Querstange. Spieler sieben steht vorn links mit Bällen, Spieler dreizehn links neben dem Torraum, der Trainer vorn in der Mitte.",
  "Ablauf: Spieler sieben schießt einen Volley, der Torwart fängt und rollt zurück. Dann taucht er unter der Stange durch und hechtet auf den flachen Schuss von Spieler dreizehn. Zurück unter der Stange läuft er in die Mitte des Tores und hält den hohen Schuss vom Trainer.",
  "Wertung und Wechsel: Jeder gehaltene Ball gibt einen Punkt für den Torwart. Danach tauschen alle reihum die Rollen. Wer am Ende die wenigsten Punkte hat, holt die Bälle."],
 "organisation_show": ORG,
 "coaching_points": ["Vor jedem Schuss auf den Zehenspitzen federn und sich stellen", "Den Volley fest mit beiden Händen fangen", "Beim flachen Schuss seitlich hechten und den Ball auf den Boden drücken", "Mit schnellen Füßen quer durchs Tor und hohes Tempo halten"],
 "materials": ["1 Jugendtor", "2 Stangen mit Querstange", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Unter der Stange zum Hechtsprung. Der Torwart hält einen Volley, einen flachen und einen hohen Schuss und taucht dazwischen unter einer Querstange durch.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": baelle(),
  "steps": [
   S("Volley fangen", "Der Torwart stellt sich und schaut zu Spieler sieben. Spieler sieben schießt einen Volley, und der Torwart fängt ihn fest mit beiden Händen.",
     bl("k1", [30, 32]), ps("b7", [42.6, 21.6], after=True)),
   S("Unter der Stange durch", "Er rollt den Ball zurück zu Spieler sieben. Dann duckt er sich unter der Querstange durch, stellt sich und schaut zu Spieler dreizehn.",
     ps("b7", [28.6, 34.6]), mv("k1", [36, 18], after=True), mv("k1", [26, 15], after=True), bl("k1", [14, 13.5], after=True)),
   S("Flach: hechten", "Spieler dreizehn schießt flach zur Seite. Der Torwart hechtet und drückt den Ball mit beiden Händen auf den Boden.",
     ps("b13", [25.6, 9.6]), mv("k1", [25, 9], delay=0.3)),
   S("Zurück zur Mitte", "Er rollt den Ball zurück, steht schnell auf und duckt sich wieder unter der Stange durch. Mit schnellen Füßen läuft er in die Mitte des Tores und stellt sich.",
     ps("b13", [13.6, 13.6]), mv("k1", [26, 15], after=True), mv("k1", [36, 18], after=True), mv("k1", [50, 10], after=True),
     bl("k1", [53, 30], after=True)),
   S("Hoch: Punkt", "Der Trainer schießt hoch in die Ecke, und der Torwart hechtet und hält den Ball. Jeder gehaltene Ball gibt einen Punkt für den Torwart. Dann tauschen alle reihum die Rollen, und der Nächste ist im Tor.",
     ps("b1", [58.6, 7.6]), mv("k1", [58, 7], delay=0.3))],
  "dims": dims(5, 95, 5, 42, "41 m", "16 m", rx=98)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Auf den Zehen federn und sich stellen.", "Federn und stellen",
    "Bevor der Schuss kommt, federt der Torwart auf den Zehenspitzen und steht dann still. Die Füße stehen etwa schulterbreit, die Hände sind vor dem Körper. So kann er in jede Richtung springen.",
    sp(k1=(50, 10)), baelle(),
    [S("Federn", "Der Torwart steht in der Mitte des Tores. Er federt auf den Zehenspitzen und schaut zum Trainer.",
       bl("k1", [53, 30])),
     S("Stellen und halten", "Der Trainer holt aus, und der Torwart steht still und bereit. Der Schuss kommt hoch in die Ecke, und er hechtet und hält den Ball. Das gibt einen Punkt für den Torwart.",
       ps("b1", [58.6, 7.6]), mv("k1", [58, 7], delay=0.3))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Richtig hechten beim flachen Schuss.", "Richtig flach hechten",
    "Beim flachen Schuss macht der Torwart einen kleinen Schritt zur Seite und lässt sich seitlich fallen. Er landet auf der Seite, nicht auf dem Bauch. Eine Hand liegt hinter dem Ball, die andere oben drauf.",
    sp(k1=(26, 15)), baelle(),
    [S("Stellen", "Der Torwart ist unter der Stange durch und stellt sich. Er schaut zu Spieler dreizehn.",
       bl("k1", [14, 13.5])),
     S("Seitlich hechten", "Spieler dreizehn schießt flach. Der Torwart macht einen kleinen Schritt, landet auf der Seite und hält den Ball mit beiden Händen fest. Das gibt einen Punkt für den Torwart.",
       ps("b13", [25.6, 9.6]), mv("k1", [25, 9], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
