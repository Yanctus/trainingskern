import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-7 (GK-P7, U12-U14, Torwarttraining): Goalkeeper Reactions Diving Distribution. 45 x 18 Yards = Strafraum, Feld x 10-90,
# y 5-55 (41 x 16 m), gedreht: im PDF liegt das Tor links, hier oben wie im Video. Torraum, Jugendtor oben, zwei Hütchen kurz
# vor den Pfosten, zwei Minitore links und rechts im Strafraum (im PDF schräg, hier gerade mit Öffnung zur Mitte).
# Drei Torhüter: grüner Torwart 1 -> k1 im Tor, pinker Torwart (wartet links neben dem Tor) -> k2. Der dritte Torwart wartet
# hier rechts neben dem Tor (dort steht im Original ein zweiter Trainer, der nichts tut). Orange 13 unten links (im Video
# Zuspieler mit Bällen) -> Spieler sieben von Team Neon, der Trainer unten rechts. Schussgeber nach dem Video: nach dem linken
# Hütchen schießt der Trainer zum rechten Pfosten, nach dem rechten Hütchen Spieler sieben zum linken Pfosten. Den hohen Ball
# wirft im Video Spieler 13; hier wirft ihn der Trainer
# (der Torwart rollt jeden gehaltenen Ball zum Schützen zurück).
# Wertung wie im PDF: Paraden und Treffer ins Minitor zählen, je ein Punkt; wer am wenigsten hat, macht eine kleine Strafaufgabe.
# Sichtkegel: PDF "make a quick decision and throw the ball into one of the mini goals" -> der Torwart schaut vor dem Abwurf
# nach links und rechts zu den Minitoren. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Fassungen: zwei Coaching-Punkte nach PDF Seite 2 (genau abwerfen, hohen Ball sicher fangen).
T = P("T", "c", 62, 46, "T")
POS = {"k1": (50, 10), "k2": (36, 2), "k3": (64, 2), "n7": (30, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else "a", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 65.6, 48.5), B("s2", 58.4, 48.5)]
LINES = [rect(10, 5, 80, 50), rect(30, 5, 40, 15)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 10, "y": 38, "side": "left"}, {"x": 90, "y": 38, "side": "right"}]
KEGEL = [C(40, 8), C(60, 8)]

u = {"title": "Hütchen kippen, hechten, werfen", "code": "UE-265", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 4, "field_size": "41 x 16 m (Strafraum)",
 "description": "Der Torwart läuft schnell zu einem Hütchen neben dem Pfosten, kippt es um und hechtet zum Schuss an den anderen Pfosten. Das wiederholt er auf der anderen Seite. Dann fängt er einen hohen Ball und wirft ihn schnell in eines der zwei Minitore. Jede Parade und jeder Treffer ins Minitor gibt einen Punkt, danach ist der nächste Torwart dran.",
 "organisation": ["Aufbauen: Ein Strafraum mit Jugendtor. Kurz vor beiden Pfosten steht je ein Hütchen. Links und rechts im Strafraum steht je ein Minitor.",
  "Verteilen: Ein Torwart steht im Tor, zwei Torhüter warten links und rechts neben dem Tor. Spieler sieben steht unten links, der Trainer unten rechts, beide mit Bällen.",
  "Ablauf: Hütchen links umkippen, Schuss vom Trainer an den rechten Pfosten halten. Hütchen rechts umkippen, Schuss von Spieler sieben an den linken Pfosten halten. Dann hohen Ball fangen und in ein Minitor werfen.",
  "Wertung und Wechsel: Jede Parade und jeder Treffer ins Minitor gibt einen Punkt. Nach jedem Durchgang ist der nächste Torwart dran. Wer am Ende die wenigsten Punkte hat, macht eine kleine Strafaufgabe."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle Füße zum Hütchen und sofort umdrehen", "Beim Hechten mit der richtigen Hand zum Ball", "Hohen Ball mit Knie hoch am höchsten Punkt fangen und laut rufen", "Schnell entscheiden und genau ins Minitor werfen"],
 "materials": ["1 Jugendtor", "2 Minitore", "2 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Hütchen kippen, hechten, werfen. Der Torwart kippt ein Hütchen um, hält zwei Schüsse, fängt einen hohen Ball und wirft ihn ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(),
  "balls": [B("b1", 62.6, 46.6), B("b2", 30.6, 40.6)] + ERSATZ,
  "steps": [
   S("Links kippen, rechts halten", "Der Torwart läuft schnell zum linken Hütchen und kippt es um. Sofort dreht er sich um, der Trainer schießt an den rechten Pfosten, und der Torwart hechtet hinüber und hält den Ball. Dann rollt er ihn zurück zum Trainer.",
     mv("k1", [42.2, 10.2]), mv("k1", [55, 9.5], after=True), ps("b1", [55.6, 10.1], delay=0.9), ps("b1", [62.6, 46.6], after=True)),
   S("Rechts kippen, links halten", "Jetzt die andere Seite: Der Torwart kippt das rechte Hütchen um. Spieler sieben schießt an den linken Pfosten, und der Torwart hechtet hinüber, hält und rollt den Ball zurück.",
     mv("k1", [57.8, 10.2]), mv("k1", [45, 9.5], after=True), ps("b2", [45.6, 10.1], delay=0.9), ps("b2", [30.6, 40.6], after=True)),
   S("Hohen Ball fangen", "Der Torwart kommt nach vorn. Der Trainer wirft den Ball hoch vor das Tor. Der Torwart ruft laut und fängt ihn ganz oben mit beiden Händen.",
     mv("k1", [50, 21]), ps("b1", [50.6, 21.6], delay=0.3)),
   S("Abwurf ins Minitor: Punkt", "Der Torwart schaut schnell nach links und nach rechts und entscheidet sich. Er wirft den Ball genau ins rechte Minitor, und das gibt einen Punkt für ihn. Dann ist der Torwart links neben dem Tor dran.",
     bl("k1", [32, 29]), bl("k1", [68, 29], after=True), ps("b1", [89.4, 38], after=True))],
  "dims": dims(10, 90, 5, 55, "41 m", "16 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau abwerfen.", "Genau abwerfen",
    "Der Torwart entscheidet schnell, welches Minitor frei ist und welche Technik passt. Für weite Würfe nimmt er den Überarmwurf, auf kurze Wege rollt er den Ball, und manchmal passt auch ein Schuss. Wichtig ist, dass der Ball genau im Minitor landet.",
    sp(k1=(50, 21)), [B("g", 50.6, 21.6), B("b1", 62.6, 46.6), B("b2", 30.6, 40.6)] + ERSATZ,
    [S("Schauen und entscheiden", "Der Torwart hat den Ball gefangen. Er schaut nach rechts und nach links und entscheidet sich für das linke Minitor.",
       bl("k1", [68, 29]), bl("k1", [32, 29], after=True)),
     S("Genau werfen: Punkt", "Mit einem schnellen Überarmwurf wirft er den Ball genau ins linke Minitor, und das gibt einen Punkt für ihn.",
       ps("g", [10.6, 38]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Den hohen Ball sicher fangen.", "Hohen Ball sicher fangen",
    "Der Torwart springt vom Boden ab, zieht ein Knie hoch und fängt den Ball mit beiden Händen am höchsten Punkt. Dabei ruft er laut „Torwart“, damit alle wissen, dass er den Ball holt.",
    sp(), [B("b1", 62.6, 46.6), B("b2", 30.6, 40.6)] + ERSATZ,
    [S("Laut rufen", "Der Trainer wirft den Ball hoch vor das Tor. Der Torwart ruft laut Torwart und startet nach vorn.",
       ps("b1", [50.6, 21.6]), mv("k1", [50, 16])),
     S("Am höchsten Punkt fangen", "Er springt ab, zieht ein Knie hoch und fängt den Ball mit beiden Händen ganz oben.",
       mv("k1", [50, 21]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
