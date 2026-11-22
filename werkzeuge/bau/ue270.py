import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P9 (U12-U14, Einzeltraining): Agility Ball Mastery Circuit (im PDF "Agility and Dribbling Circuit 1 to 1-P9").
# 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m). Ausrichtung wie im PDF: Leiter oben (waagrecht, von links nach rechts),
# drei Ringe links senkrecht, vier Stangen schräg in der Mitte, letzte Stange unten rechts, Ball in der Mitte vor der ersten Stange.
# Pinker Spieler -> Spieler sieben (Team Neon). Im Original zwei Trainer (oben rechts und unten links): hier genau ein Trainer.
# Er startet oben rechts und läuft, während Spieler sieben zurücksprintet und durch die Ringe hüpft, außen nach unten links.
# Dort liegt der zweite Ball schon bereit. Die zwei Markierungshütchen an den Trainer-Plätzen weggelassen (nur Standort-Marken).
# Ablauf nach PDF und Video (0:06-0:38). Reine Technik- und Koordinationsübung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen = die zwei Key Coaching Points aus PDF Seite 2: Prallpass mit beiden Füßen, Ball eng am Fuß durch die Stangen.
T = P("T", "c", 70, 8, "T")
POS = {"n7": (29, 13)}
def sp(**k):
    d = dict(POS); d.update(k)
    t = dict(T); t["x"], t["y"] = d.pop("T", (T["x"], T["y"]))
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [t]
def ersatz(x1, y1, x2, y2): return [B("s1", x1, y1), B("s2", x2, y2)]
LINES = [rect(25, 5, 50, 50)]
STANGEN = [(41, 24), (45.5, 28), (50, 32), (54.5, 36), (64, 46)]
GERAET = ([leiter(43, 13)] + [ring(30, y) for y in (19, 24.8, 30.6)] + [C(x, y, shape="stange") for x, y in STANGEN]
          + [C(25.5, 9), C(55, 9), C(25.5, 35.5)])
TU = (28.5, 51)
B7R = [30.6, 35.6]

u = {"title": "Leiter, Ringe, Stangenslalom", "code": "UE-270", "kind": "Übungsform",
 "focuses": ["Koordination", "Dribbling", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 12, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Spieler läuft einen Parcours mit Leiter, Ringen und Stangen. Nach schnellen Füßen durch die Leiter spielt er einen Prallpass mit dem Trainer und sprintet zurück. Dann hüpft er durch die Ringe, spielt den zweiten Prallpass und dribbelt mit dem Ball durch die Stangen. Um die letzte Stange herum geht es zurück zum Start.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben eine Leiter, links drei Ringe untereinander, in der Mitte vier Stangen schräg und unten rechts eine letzte Stange. Vor der ersten Stange liegt ein Ball.",
  "Verteilen: Spieler sieben startet oben links am Hütchen. Der Trainer steht oben rechts mit Bällen, unten links liegt ein zweiter Ball.",
  "Ablauf: Schnelle Füße durch die Leiter, Prallpass mit dem Trainer, Sprint zurück. Dann durch die Ringe, zweiter Prallpass, zum Ball sprinten und durch die Stangen dribbeln. Um die letzte Stange und zurück zum Start.",
  "Wechsel: Am Start erholt sich Spieler sieben kurz. Dann beginnt die nächste Runde. Die Prallpässe abwechselnd mit rechts und links spielen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle Füße und saubere Haltung in Leiter und Ringen", "Genaue Prallpässe direkt zurück zum Trainer", "Den Ball beim Dribbeln eng am Fuß führen", "Mit hohem Tempo und mit beiden Füßen arbeiten"],
 "materials": ["1 Koordinationsleiter", "3 Ringe", "5 Stangen", "3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Leiter, Ringe, Stangenslalom. Spieler sieben läuft einen Parcours mit zwei Prallpässen und dribbelt am Ende durch die Stangen.",
 "board": {"lines": LINES, "cones": GERAET, "players": sp(),
  "balls": [B("b1", 70.6, 8.6), B("b2", 29.1, 51.6), B("b3", 37, 19)] + ersatz(66, 5.5, 63, 5.5),
  "steps": [
   S("Leiter, Prallpass", "Spieler sieben läuft mit schnellen Füßen durch die Leiter bis zum Hütchen. Der Trainer passt zu ihm, und er spielt direkt zurück.",
     mv("n7", [54.5, 13]), ps("b1", [55.1, 13.6], after=True), ps("b1", [70.6, 8.6], after=True)),
   S("Zurück, durch die Ringe", "Spieler sieben dreht sich um und sprintet zurück zum Start. Dann hüpft er durch die Ringe. Gleichzeitig läuft der Trainer außen nach unten links.",
     mv("n7", [30, 15.5]), mv("n7", [30, 35], after=True), mv("T", [76, 12]), mv("T", [76, 51], after=True), mv("T", [28.5, 51], after=True)),
   S("Zweiter Prallpass", "Unten links wartet der Trainer mit dem zweiten Ball. Er passt zu Spieler sieben, und der spielt direkt zurück.",
     ps("b2", B7R), ps("b2", [29.1, 51.6], after=True)),
   S("Zum Ball, Slalom", "Spieler sieben sprintet zum Ball in der Mitte. Dann dribbelt er eng am Fuß durch die Stangen.",
     mv("n7", [36.4, 18.4]), dr("n7", "b3", [38.5, 26.5], after=True), dr("n7", "b3", [47.5, 25.5], after=True),
     dr("n7", "b3", [47.5, 34.5], after=True), dr("n7", "b3", [57, 33], after=True)),
   S("Um die Stange: Ziel", "Spieler sieben dribbelt um die letzte Stange herum und zurück zum Start. Das Ziel: der ganze Parcours schnell und sauber, ohne den Ball zu verlieren. Am Start erholt er sich kurz, dann beginnt die nächste Runde.",
     dr("n7", "b3", [67, 43]), dr("n7", "b3", [67.5, 49], after=True), dr("n7", "b3", [60, 49.5], after=True),
     dr("n7", "b3", [40, 45], after=True), dr("n7", "b3", [35, 30], after=True), dr("n7", "b3", [29, 13], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=83)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Prallpässe mit beiden Füßen.", "Prallpass mit beiden Füßen",
    "Beim Prallpass kommt es auf Genauigkeit an. Spieler sieben spielt den Ball direkt und flach zurück in die Füße des Trainers. Mal mit rechts, mal mit links, damit beide Füße sicher werden.",
    sp(n7=(30, 35), T=TU), [B("b2", 29.1, 51.6)] + ersatz(32.5, 54.5, 35.5, 54.5),
    [S("Mit rechts zurück", "Der Trainer passt zu Spieler sieben. Er spielt den Ball mit rechts direkt und genau zurück.",
       ps("b2", B7R), ps("b2", [29.1, 51.6], after=True)),
     S("Mit links zurück: Ziel", "Beim nächsten Mal spielt Spieler sieben mit links zurück. Das Ziel: jeder Prallpass kommt genau beim Trainer an.",
       ps("b2", B7R), ps("b2", [29.1, 51.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den Ball eng am Fuß führen.", "Eng am Fuß durch die Stangen",
    "Durch die Stangen führt Spieler sieben den Ball mit vielen kleinen Kontakten. Er nimmt Innen- und Außenseite und beide Füße. Erst wenn die Technik sauber ist, wird er schneller.",
    sp(n7=(36.4, 18.4), T=TU), [B("b3", 37, 19)] + ersatz(32.5, 54.5, 35.5, 54.5),
    [S("Kleine Kontakte", "Spieler sieben dribbelt mit kleinen Kontakten an den ersten zwei Stangen vorbei. Der Ball bleibt eng am Fuß.",
       dr("n7", "b3", [38.5, 26.5]), dr("n7", "b3", [47.5, 25.5], after=True)),
     S("Schneller werden: Ziel", "Bei den nächsten Stangen nimmt er die andere Seite des Fußes und wird schneller. Das Ziel: an keiner Stange den Ball verlieren.",
       dr("n7", "b3", [47.5, 34.5]), dr("n7", "b3", [57, 33], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
