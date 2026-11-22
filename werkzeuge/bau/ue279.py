import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P7 (U12-U14, Einzeltraining): Dribbling, Passing and Endurance (Ordner "Driving at Speed and Passing 1 to 1-P7").
# Kreis mit 15 Yards Durchmesser (ca. 14 m) = Kreis Mitte 50/30, r 24. Ausrichtung wie im Original (nicht gedreht).
# Acht Hütchen gleichmäßig am Rand, in der Mitte eine Stange. Spieler P -> Spieler sieben (Team Neon) startet mit Ball an der
# Stange. Der Trainer C steht mit Ball außen am rechten Hütchen (zwei Ersatzbälle daneben) und wechselt nach jeder Passstation
# an ein anderes Hütchen (im Video nach oben rechts und oben).
# Keine Wertung im Original: Ziel statt Punkte (alle acht Hütchen andribbeln, Pässe mit beiden Füßen genau).
# Sichtkegel aus dem Ton ("players have to check shoulders and adjust positioning", der Trainer wechselt den Platz):
# Spieler sieben schaut nach dem Ablegen an der Stange, wo der Trainer jetzt steht (Richtung zum Trainer).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (enge Ballführung mit Tempo; genau passen auch mit dem schwächeren Fuß,
# im Video "Poor pass back" und Korrektur).
T = P("T", "c", 79, 34, "T")
POS = {"n7": (46, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) if i[0] == "n" else P(i, "c", x, y, "T") for i, (x, y) in d.items()] + ([] if "T" in k else [T])
ERSATZ = [B("s1", 82.5, 37.5), B("s2", 82.5, 30.5)]
KREIS = {"type": "circle", "x": 50, "y": 30, "r": 24}
CONES = [C(50, 6), C(66.97, 13.03), C(74, 30), C(66.97, 46.97), C(50, 54), C(33.03, 46.97), C(26, 30), C(33.03, 13.03),
         C(50, 30, shape="stange")]
def weg(who, ball, pkt): return [dr(who, ball, pkt[0])] + [dr(who, ball, p, after=True) for p in pkt[1:]]

u = {"title": "Hütchen andribbeln und passen", "code": "UE-279", "kind": "Übungsform",
 "focuses": ["Dribbling", "Passspiel", "Kondition"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "Kreis, 14 m Durchmesser",
 "description": "Ein Spieler trainiert allein mit dem Trainer Dribbling mit Tempo, genaue Pässe und Ausdauer. Er dribbelt von der Stange in der Mitte zu einem Hütchen, dreht schnell und dribbelt zurück. Dann lässt er seinen Ball an der Stange liegen und spielt mit dem Trainer je einen Pass mit links und mit rechts. Der Trainer wechselt danach den Platz, und der Spieler muss sich neu orientieren.",
 "organisation": ["Aufbauen: Ein Kreis mit etwa 14 Metern Durchmesser. Acht Hütchen gleichmäßig am Rand, in der Mitte eine Stange.",
  "Verteilen: Der Spieler startet mit Ball an der Stange. Der Trainer steht mit einem Ball außen an einem Hütchen.",
  "Ablauf: Der Spieler dribbelt zu einem Hütchen, dreht schnell und dribbelt zurück zur Stange. Dort lässt er den Ball liegen, läuft zum Trainer und passt einmal mit links und einmal mit rechts zurück. Dann sprintet er zurück zu seinem Ball.",
  "Wechsel: Nach jeder Passstation geht der Trainer an ein anderes Hütchen. Hat der Spieler alle acht Hütchen angedribbelt, ist die Runde vorbei. Nach einer kurzen Pause beginnt die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball beim Dribbling eng am Fuß führen und Tempo machen", "Mit kurzen, schnellen Kontakten drehen", "Genau passen, mit links und mit rechts", "Den Ball an der Stange stoppen und schauen, wo der Trainer steht"],
 "materials": ["8 Hütchen", "1 Stange", "2 Bälle", "2 Ersatzbälle beim Trainer"],
 "access": "abo", "hidden": True,
 "say_intro": "Hütchen andribbeln und passen. Mit Tempo zum Hütchen und zurück, dann zwei genaue Pässe mit dem Trainer, und das acht Mal hintereinander.",
 "board": {"lines": [KREIS], "cones": CONES, "players": sp(), "balls": [B("b1", 46.6, 30.6), B("b2", 79.6, 34.6)] + ERSATZ,
  "steps": [
   S("Zum Hütchen", "Spieler sieben dribbelt mit Tempo von der Stange zum Hütchen unten.",
     dr("n7", "b1", [48, 49.5])),
   S("Drehen und zurück", "Kurz vor dem Hütchen dreht er mit kurzen, schnellen Kontakten. Dann dribbelt er zurück und stoppt den Ball neben der Stange.",
     *weg("n7", "b1", [[52, 48], [54, 34]])),
   S("Schauen, wo der Trainer ist", "Spieler sieben lässt den Ball liegen und schaut, wo der Trainer steht. Dann läuft er zu ihm.",
     bl("n7", [79, 34]), mv("n7", [69, 34], after=True)),
   S("Links und rechts passen", "Der Trainer spielt ihm den Ball zu, und Spieler sieben passt mit links zurück. Dann noch einmal, jetzt passt er mit rechts zurück.",
     ps("b2", [69.6, 34.6]), ps("b2", [79.6, 34.6], after=True), ps("b2", [69.6, 34.6], after=True), ps("b2", [79.6, 34.6], after=True)),
   S("Zurück zum Ball", "Spieler sieben sprintet zurück zu seinem Ball an der Stange. Gleichzeitig geht der Trainer an ein anderes Hütchen. Dann geht es zum nächsten Hütchen. Hat Spieler sieben alle acht Hütchen angedribbelt, ist die Runde vorbei, und nach einer kurzen Pause beginnt die nächste.",
     mv("n7", [54, 34]), dr("T", "b2", [72, 8]))],
  "dims": [{"x1": 26, "y1": 58.6, "x2": 74, "y2": 58.6, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Eng am Ball und mit Tempo, die ganze Runde lang.", "Eng am Ball, hohes Tempo",
    "Der Spieler führt den Ball beim Dribbling mit vielen kleinen Kontakten ganz nah am Fuß. Er bleibt die ganze Runde konzentriert und schnell, auch wenn er müde wird. Am Hütchen dreht er mit kurzen, schnellen Kontakten.",
    sp(n7=(54, 34), T=(72, 8)), [B("b1", 54.6, 34.6), B("b2", 72.6, 8.6), B("s1", 76, 5.5), B("s2", 76.5, 10.5)],
    [S("Mit Tempo nach links", "Spieler sieben dribbelt mit vielen kleinen Kontakten zum Hütchen links. Der Ball bleibt ganz nah am Fuß.",
       *weg("n7", "b1", [[46, 35], [30, 31]])),
     S("Kurz drehen, zurück", "Am Hütchen dreht er mit kurzen, schnellen Kontakten und dribbelt mit Tempo zurück zur Stange.",
       *weg("n7", "b1", [[31, 27], [45, 26.5]]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Genau passen, auch mit dem schwächeren Fuß.", "Genau mit beiden Füßen",
    "Der Spieler passt mit beiden Füßen genau zum Trainer. Gerade mit dem schwächeren Fuß geht ein Pass schnell daneben. Dann zeigt der Trainer kurz, wie es besser geht: Standbein neben den Ball, mit der Innenseite passen.",
    sp(n7=(52, 21), T=(62, 4)), [B("b1", 45.6, 27.1), B("b2", 62.6, 4.6), B("s1", 58.5, 2), B("s2", 65.5, 1.5)],
    [S("Pass daneben", "Der Trainer steht jetzt oben. Er spielt Spieler sieben den Ball zu. Spieler sieben passt mit dem schwächeren linken Fuß zurück, aber der Pass geht daneben.",
       bl("n7", [62, 4]), ps("b2", [52.6, 21.6], after=True), ps("b2", [72, 2], after=True)),
     S("Besser machen", "Der Trainer spielt einen Ersatzball. Spieler sieben stellt das Standbein neben den Ball und passt mit der Innenseite genau zurück.",
       ps("s1", [52.6, 21.6]), ps("s1", [62.6, 4.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
