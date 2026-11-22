import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P11 (U12-U14, Einzeltraining): Dribbling Physical Training (PDF: Dribbling at Speed and Sprints). 10 x 15 Yards =
# Feld x 33-67, y 8-52 (9 x 14 m; auf der Tafel etwas breiter gezeichnet, wie im PDF, damit die Wege lesbar bleiben).
# Ausrichtung wie im PDF (Start unten rechts, Trainer rechts außen). Pinker Spieler P -> Spieler sieben (Team Neon).
# Vier gelbe Stangen in den Ecken, die Puppe in der Mitte als Stange gezeichnet. Laufweg nach PDF und Video (0:05-0:45) als
# liegende Acht: zur Puppe, links herum, um die Stange oben links, quer hinüber, um die Stange oben rechts, zurück über die
# Puppe (rechts herum), um die Stange unten links und quer zurück zum Start. Dann Ball ablegen und die Runde ohne Ball sprinten.
# Reine Technik- und Laufübung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; im Video nur Kreise um den Spieler).
# Fassungen: Coaching-Punkt kleine Kontakte an der Stange (PDF Seite 2 KCP 1, Video ab 0:45), zweiter Coaching-Punkt schnell um
# die Puppe (KCP-Zusammenfassung "Quick shift around the mannequins", Video-Schlusstafel). KCP 2 (ohne Ball sprinten) ist schon
# Teil der Grundform.
T = P("T", "c", 77, 42, "T")
POS = {"n7": (65.5, 47.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 80.5, 45.5), B("s2", 80.5, 48)]
LINES = [rect(33, 8, 34, 44)]
CONES = [C(x, y, shape="stange") for x, y in [(38, 15), (62, 15), (38, 46), (62, 46), (50, 29)]]
W1 = [[65, 43], [58, 36], [53, 33]]
W2 = [[46, 30], [48, 24.5], [42, 19]]
W3 = [[35.5, 16.5], [36, 11.5], [50, 11], [64, 11.5], [65, 17.5]]
W4 = [[57, 21], [54, 25], [54, 29.5], [51, 34], [45, 38], [35.5, 44.5]]
W5 = [[36, 49.5], [50, 50.5], [65.5, 47.5]]
def weg(pkte):
    return [dr("n7", "b1", p, after=(i > 0) or None) for i, p in enumerate(pkte)]

u = {"title": "Dribbel-Acht, dann Sprintrunde", "code": "UE-276", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Kondition"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "9 x 14 m",
 "description": "Der Spieler dribbelt eine liegende Acht um vier Stangen und eine Puppe in der Mitte. An der Puppe legt er sich den Ball schnell vorbei, an den Stangen dreht er mit kleinen Kontakten. Danach legt er den Ball ab und sprintet dieselbe Runde ohne Ball. Nach zwei Runden gibt es eine Pause.",
 "organisation": ["Aufbauen: Ein Feld von neun mal vierzehn Metern. In jeder Ecke eine Stange, in der Mitte eine Puppe.",
  "Verteilen: Spieler sieben startet mit Ball an der Stange unten rechts. Der Trainer steht rechts außen mit Ersatzbällen.",
  "Ablauf: Zur Puppe, schnell links vorbei, um die Stange oben links, quer hinüber, um die Stange oben rechts. Dann dasselbe andersherum zurück zum Start. Ball ablegen und die ganze Runde ohne Ball sprinten.",
  "Wechsel: Nach zwei Runden gibt es eine Pause. Sind zwei Spieler da, startet der zweite, während der erste Pause macht."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball eng führen und trotzdem schnell sein", "An der Puppe den Ball schnell zur Seite legen", "An den Stangen kleine, schnelle Kontakte", "Ohne Ball mit vollem Tempo sprinten und nach zwei Runden gut erholen"],
 "materials": ["5 Stangen", "1 Puppe", "Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Dribbel-Acht, dann Sprintrunde. Spieler sieben dribbelt eine Acht um die Stangen und sprintet danach dieselbe Runde ohne Ball.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(),
  "balls": [B("b1", 66.1, 48.1)] + ERSATZ,
  "steps": [
   S("Zur Puppe", "Spieler sieben startet unten rechts an der Stange. Er dribbelt mit Tempo zur Puppe in der Mitte.",
     *weg(W1)),
   S("Schnell um die Puppe", "An der Puppe legt er sich den Ball schnell zur Seite, dribbelt links herum und weiter zur Stange oben links.",
     *weg(W2)),
   S("Quer hinüber", "Mit kleinen, schnellen Kontakten dribbelt er um die Stange, quer hinüber und um die Stange oben rechts.",
     *weg(W3)),
   S("Jetzt andersherum", "Jetzt dasselbe in die andere Richtung: wieder schnell um die Puppe, diesmal rechts herum, und weiter zur Stange unten links.",
     *weg(W4)),
   S("Zurück zum Start", "Er dribbelt um die Stange unten links und quer hinüber zurück zum Start.",
     *weg(W5)),
   S("Ohne Ball sprinten: Ziel", "Am Start legt Spieler sieben den Ball ab und sprintet dieselbe Runde ohne Ball. Das Ziel: die ganze Runde mit vollem Tempo. Nach zwei solchen Runden gibt es eine Pause, dann ist er wieder dran.",
     *[mv("n7", p, after=(i > 0) or None) for i, p in enumerate(W1 + W2 + W3 + W4 + W5)])],
  "dims": dims(33, 67, 8, 52, "9 m", "14 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kleine, schnelle Kontakte an der Stange.", "Eng um die Stange drehen",
    "An den Stangen dreht der Spieler mit vielen kleinen, schnellen Kontakten. Der Ball bleibt dabei ganz nah am Fuß. So schafft er die Richtungsänderung schnell und ohne Ballverlust.",
    sp(n7=(47.5, 23.5)), [B("b1", 48.1, 24.1)] + ERSATZ,
    [S("Kleine Kontakte", "Spieler sieben kommt zur Stange oben links. Mit kleinen, schnellen Kontakten dreht er eng um die Stange.",
       *weg([W2[2]] + W3[:2])),
     S("Eng bleiben", "Der Ball bleibt nah am Fuß. Dann dribbelt er quer hinüber und dreht genauso eng um die Stange oben rechts.",
       *weg(W3[2:]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Puppe schnell umspielen.", "Schnell an der Puppe vorbei",
    "Kurz vor der Puppe legt der Spieler den Ball mit einem schnellen Kontakt zur Seite. Dann geht es sofort weiter, ohne abzubremsen. Nach dem Ablegen geht es mit vollem Tempo weiter zur nächsten Stange.",
    sp(n7=(65, 43)), [B("b1", 65.6, 43.6)] + ERSATZ,
    [S("Auf die Puppe zu", "Spieler sieben dribbelt mit Tempo auf die Puppe zu.",
       *weg(W1[1:])),
     S("Schnell zur Seite", "Kurz vor der Puppe legt er den Ball schnell zur Seite, dribbelt vorbei und gleich weiter zur Stange oben links.",
       *weg(W2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
