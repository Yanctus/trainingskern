import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P4 (U12-U14, Einzeltraining): Enhancing Dribbling, Drive & Awareness (Ordner "Dribbling at Speed 1 to 1-P4").
# Kreis mit 15 Yards Durchmesser (ca. 14 m) = Kreis Mitte 50/30, r 24. Ausrichtung wie im Original (nicht gedreht).
# Acht Hütchen gleichmäßig am Rand, in der Mitte eine Puppe (Stange). Spieler P -> Spieler sieben (Team Neon) startet oben
# mit Ball, Bälle an den Hütchen links, rechts und unten (zusammen vier Bälle). Trainer C steht rechts oben außerhalb.
# Bälle liegen leicht innen neben ihrem Hütchen, damit die Laufwege nicht durch die Hütchen gehen.
# Keine Wertung im Original: Ziel statt Punkte (alle vier Bälle schnell umlegen, keinen Ball zweimal).
# Sichtkegel: Titel "Dribbling, Drive & AWARENESS", Video "Remember which balls have been moved" / "Sprint to next available
# ball": Spieler sieben schaut nach dem Ablegen zum nächsten freien Ball (Richtung aus dem Sinn, im Video kein Kegel).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (scharf um die Puppe drehen; merken, welche Bälle schon bewegt wurden).
T = P("T", "c", 82, 12, "T")
POS = {"n7": (50, 9.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 86, 15), B("s2", 86, 9)]
KREIS = {"type": "circle", "x": 50, "y": 30, "r": 24}
CONES = [C(50, 6), C(66.97, 13.03), C(74, 30), C(66.97, 46.97), C(50, 54), C(33.03, 46.97), C(26, 30), C(33.03, 13.03),
         C(50, 30, shape="stange")]
BAELLE = [B("b1", 50.6, 10.1), B("b2", 28.6, 30.6), B("b3", 71.6, 30.6), B("b4", 50.6, 50.6)] + ERSATZ
def weg(f, who, ball, pkt): return [f(who, ball, pkt[0])] + [f(who, ball, p, after=True) for p in pkt[1:]]
def lw(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Bälle umlegen um die Puppe", "code": "UE-277", "kind": "Übungsform",
 "focuses": ["Dribbling", "Schnelligkeit", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "Kreis, 14 m Durchmesser",
 "description": "Ein Spieler trainiert allein mit dem Trainer Dribbling mit Tempo und Merkfähigkeit. Er dribbelt mit dem Ball scharf um die Puppe in der Mitte und legt ihn an einem freien Hütchen ab. Dann sprintet er zum nächsten Ball, der in dieser Runde noch nicht bewegt wurde. Die Runde ist vorbei, wenn alle vier Bälle an einem neuen Hütchen liegen.",
 "organisation": ["Aufbauen: Ein Kreis mit etwa 14 Metern Durchmesser. Acht Hütchen gleichmäßig am Rand, in der Mitte eine Puppe oder Stange.",
  "Verteilen: Drei Bälle liegen an den Hütchen links, rechts und unten. Der Spieler startet oben mit dem vierten Ball. Der Trainer steht außen.",
  "Ablauf: Der Spieler dribbelt scharf um die Puppe und legt den Ball an einem freien Hütchen ab. Dann sprintet er zum nächsten Ball, der noch nicht bewegt wurde, und macht weiter.",
  "Wechsel: Liegen alle vier Bälle an einem neuen Hütchen, ist die Runde vorbei. Kein Ball darf zweimal bewegt werden. Nach einer kurzen Pause startet die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball eng am Fuß führen und dabei Tempo machen", "Scharf und eng um die Puppe drehen", "Merken, welche Bälle schon bewegt wurden", "Schnell zum nächsten Ball sprinten und beide Füße benutzen"],
 "materials": ["8 Hütchen", "1 Puppe oder Stange", "4 Bälle", "2 Ersatzbälle beim Trainer"],
 "access": "abo", "hidden": True,
 "say_intro": "Bälle umlegen um die Puppe. Mit Tempo um die Puppe dribbeln, den Ball an einem freien Hütchen ablegen und dir merken, welche Bälle du schon bewegt hast.",
 "board": {"lines": [KREIS], "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Um die Puppe", "Spieler sieben dribbelt mit Tempo zur Puppe in der Mitte und dreht scharf um sie herum.",
     *weg(dr, "n7", "b1", [[54, 22], [56, 30], [51, 36], [44, 34]])),
   S("Ball ablegen", "Dann dribbelt er zu einem freien Hütchen unten links und legt den Ball dort ab.",
     dr("n7", "b1", [35, 44])),
   S("Schauen und sprinten", "Spieler sieben schaut, welcher Ball noch nicht bewegt wurde. Er sieht den Ball links und sprintet hin.",
     bl("n7", [28, 30]), mv("n7", [28, 30], after=True)),
   S("Zweiter Ball", "Mit dem zweiten Ball dribbelt er wieder scharf um die Puppe und legt ihn am freien Hütchen oben links ab.",
     *weg(dr, "n7", "b2", [[44, 24], [54, 25], [55, 33], [47, 36], [42, 27], [36, 16]])),
   S("Runde vorbei", "So geht es weiter mit dem Ball rechts und dem Ball unten. Liegen alle vier Bälle an einem neuen Hütchen, ist die Runde vorbei. Nach einer kurzen Pause startet Spieler sieben die nächste Runde.",
     *lw("n7", [[46, 18], [71, 30]]))],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Scharf und eng um die Puppe drehen.", "Scharf um die Puppe",
    "Die Drehung um die Puppe ist wie ein Haken gegen einen Gegenspieler. Der Ball bleibt mit kleinen Kontakten ganz nah am Fuß, und nach der Drehung geht es sofort mit Tempo weiter. Dabei mal mit links, mal mit rechts drehen.",
    sp(n7=(71, 30)), [B("b1", 35.6, 44.6), B("b2", 36.6, 16.6), B("b3", 71.6, 30.6), B("b4", 50.6, 50.6)] + ERSATZ,
    [S("Kleine Kontakte", "Spieler sieben dribbelt mit dem Ball von rechts zur Puppe. Kurz davor macht er kleine Kontakte.",
       dr("n7", "b3", [56, 27])),
     S("Eng drehen", "Er dreht ganz eng um die Puppe, der Ball bleibt nah am Fuß. Dann geht es mit Tempo zum freien Hütchen oben rechts.",
       *weg(dr, "n7", "b3", [[50, 24.5], [44.5, 30], [50, 35.5], [55.5, 31], [64, 17]]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Merk dir, welche Bälle du schon bewegt hast.", "Merken, was schon bewegt ist",
    "Ein Ball darf in einer Runde nur einmal bewegt werden. Der Spieler muss sich merken, welche Bälle er schon abgelegt hat. Er schaut sich kurz um und sprintet sofort zum nächsten freien Ball.",
    sp(n7=(35, 44)), [B("b1", 35.6, 44.6), B("b2", 36.6, 16.6), B("b3", 64.6, 17.6), B("b4", 50.6, 50.6)] + ERSATZ,
    [S("Schon bewegt", "Spieler sieben steht unten links. Dieser Ball wurde in dieser Runde schon abgelegt. Er schaut, welcher Ball noch frei ist.",
       bl("n7", [50, 50])),
     S("Zum freien Ball", "Er sprintet zum Ball unten. Den hat er noch nicht bewegt.",
       mv("n7", [50, 50])),
     S("Weiter um die Puppe", "Mit diesem Ball dribbelt er scharf um die Puppe und legt ihn am freien Hütchen rechts unten ab. Jetzt liegen alle vier Bälle an einem neuen Hütchen.",
       *weg(dr, "n7", "b4", [[46, 37], [44, 29], [50, 24.5], [56, 30], [64, 44]]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
