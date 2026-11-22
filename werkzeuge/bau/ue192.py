import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-40 (U12-U14, Woche 22 Phase 5): Protect Your Bib Warm Up. 25 x 20 Yards = Feld x 25-75, y 6-45 (23 x 18 m).
# Im PDF drei Vierergruppen (dunkel) mit je einem Fänger (pink): hier zwei Gruppen auf der Tafel (Neon 2-5 und 6-9), die
# Fänger sind Team Rot (10, 11); die dritte Gruppe nur im Text. Die Vierer stehen als enges Rechteck statt im Kreis
# (3D-Abstand), sie halten sich an den Händen und drehen sich gemeinsam. Leibchen: Neon zwei und Neon sieben (nur im Text).
# Fangen statt "grab": Wer das Leibchen aus der Hose zieht, hat gefangen. Ein Trainer an der Seite.
# Sichtkegel: Ton/Text "constant scanning", "players facing forward should take the lead" und im Video der Ruf "LEFT!" -> der
# Spieler, der dem Fänger gegenüber steht, schaut zu ihm und sagt die Richtung an (im Video kein Kegel eingezeichnet, die
# grünen Dreiecke dort sind die Leibchen; Richtung aus dem Sinn).
T = P("T", "c", 80, 12, "T")
A = {"n2": (33.8, 13.25), "n3": (42.2, 13.25), "n4": (33.8, 28.75), "n5": (42.2, 28.75)}
GB = {"n6": (59, 25.25), "n7": (67.4, 25.25), "n8": (59, 40.75), "n9": (67.4, 40.75)}
POS = dict(A, r10=(50.6, 24), **GB, r11=(50.6, 43))
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 15.5), B("s2", 80, 15.5)]
LINES = [rect(25, 6, 50, 39)]
# Ecken der Gruppen: oben links, oben rechts, unten rechts, unten links
EA = [(33.8, 13.25), (42.2, 13.25), (42.2, 28.75), (33.8, 28.75)]
EB = [(59, 25.25), (67.4, 25.25), (67.4, 40.75), (59, 40.75)]
def dreh(ecken, wer, schritt, **k):
    # wer[i] steht auf ecken[i]; schritt +1 = im Uhrzeigersinn (auf dem Bildschirm), -1 = gegen den Uhrzeigersinn
    return [mv(w, list(ecken[(i + schritt) % 4]), **k) for i, w in enumerate(wer)]

u = {"title": "Schütze das Leibchen", "code": "UE-192", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Koordination", "Zusammenspiel"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 10, "players_max": 15, "field_size": "23 x 18 m",
 "description": "Ein lustiges Fangspiel zum Aufwärmen. Vier Spieler halten sich an den Händen, einer von ihnen hat ein Leibchen hinten in der Hose. Ein Fänger will dieses Leibchen herausziehen, und die Gruppe dreht sich gemeinsam, damit er nicht herankommt. Wer dem Fänger gegenübersteht, schaut genau hin und sagt an, wohin sich die Gruppe drehen muss.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern. Bälle braucht es nicht.",
  "Verteilen: Gruppen zu viert halten sich an den Händen, einer steckt ein Leibchen hinten in die Hose. Zu jeder Gruppe gehört ein Fänger von Team Rot, der gegenüber vom Leibchen startet.",
  "Ablauf: Auf das Zeichen des Trainers spielen alle Gruppen gleichzeitig. Der Fänger läuft um die Gruppe herum, die Gruppe dreht sich und hält ihn auf der anderen Seite.",
  "Wechsel: Zieht der Fänger das Leibchen aus der Hose, hat er gefangen. Dann wird der Spieler mit dem Leibchen der neue Fänger, und der Fänger geht mit in die Gruppe."],
 "organisation_show": ORG,
 "coaching_points": ["Laut reden und die Richtung ansagen", "Wer dem Fänger gegenübersteht, schaut immer auf ihn", "Immer in Bewegung bleiben und schnell mitdrehen", "Abstand halten und mit dem Körper den Weg versperren"],
 "materials": ["1 Leibchen pro Gruppe", "4 Hütchen", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Schütze das Leibchen. Ein Fangspiel zum Aufwärmen, bei dem die ganze Gruppe zusammen das Leibchen schützt.",
 "board": {"lines": LINES, "goals": [], "cones": ecken(25, 6, 50, 39), "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Auf das Zeichen", "Auf das Zeichen des Trainers geht es los, und alle Gruppen spielen gleichzeitig. Rot zehn will das Leibchen von Neon zwei und läuft oben herum. Die Gruppe hält sich an den Händen und dreht sich, damit Neon zwei weit weg bleibt. Rot elf jagt das Leibchen von Neon sieben.",
     mv("r10", [48, 8]), mv("r10", [37, 8], after=True), *dreh(EA, ["n2", "n3", "n5", "n4"], -1, delay=0.4),
     mv("r11", [50.5, 33]), mv("r11", [56, 19], after=True), mv("r11", [64, 18.5], after=True), *dreh(EB, ["n6", "n7", "n9", "n8"], 1, delay=0.6)),
   S("Ansagen und drehen", "Rot zehn dreht um und läuft links herunter. Neon vier steht ihm gegenüber, schaut genau hin und ruft: Rechts herum! Die Gruppe dreht sich, und Neon zwei ist wieder weit weg.",
     mv("r10", [27.5, 12]), bl("n4", [28, 16], after=True), mv("r10", [27, 24], after=True), *dreh(EA, ["n3", "n5", "n4", "n2"], -1, delay=1.2),
     mv("r11", [73, 26]), mv("r11", [72.5, 34], after=True), *dreh(EB, ["n8", "n6", "n7", "n9"], 1, delay=0.6)),
   S("Gefangen", "Bei der anderen Gruppe ist Rot elf schneller. Er läuft unten herum und zieht Neon sieben das Leibchen aus der Hose. Gefangen! Jetzt ist Neon sieben der neue Fänger, und Rot elf geht mit in die Gruppe.",
     mv("r11", [70.5, 44]), mv("r11", [61.5, 44.5], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schauen und ansagen.", "Schauen und ansagen",
    "Wer dem Fänger gegenübersteht, sieht ihn am besten. Dieser Spieler schaut immer auf den Fänger und sagt laut an, wohin sich die Gruppe drehen muss. Alle drehen sofort zusammen, und der Fänger bleibt auf der anderen Seite.",
    sp(dict(A, r10=(50.6, 24))), ERSATZ,
    [S("Schauen", "Rot zehn läuft unten herum zum Leibchen von Neon zwei. Neon drei schaut genau auf ihn.",
       mv("r10", [51, 33]), mv("r10", [47.5, 37], after=True), bl("n3", [46, 32], after=True)),
     S("Ansagen und drehen", "Neon drei ruft: Links herum! Alle drehen sich sofort zusammen, und Neon zwei bleibt auf der anderen Seite.",
       mv("r10", [42, 38.5]), mv("r10", [36, 37], after=True), *dreh(EA, ["n2", "n3", "n5", "n4"], 1, delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Spielen zu zweit.", "Blocker zu zweit",
    "Jetzt gibt es Paare. Ein Paar hält sich an den Händen und hat das Leibchen, das andere Paar steht davor und blockt. Die Blocker bleiben immer zwischen Fänger und Leibchen, wie Verteidiger im Spiel. Alle Gruppen spielen gleichzeitig.",
    sp({"r10": (45.9, 8), "n4": (41.6, 24), "n5": (50, 24), "n3": (41.6, 40), "n2": (50, 40),
        "r11": (64.1, 8), "n6": (60, 24), "n7": (68.4, 24), "n8": (60, 40), "n9": (68.4, 40)}), ERSATZ,
    [S("Blocken", "Rot zehn will links vorbei zum Leibchen von Neon zwei. Neon vier und Neon fünf schieben gemeinsam mit und stehen im Weg. Das Paar mit dem Leibchen weicht nach rechts aus. Bei der anderen Gruppe passiert gleichzeitig das Gleiche.",
       mv("r10", [36.5, 17]), mv("n4", [37, 23], delay=0.2), mv("n5", [45.2, 23], delay=0.2), mv("n3", [46.5, 41], delay=0.3), mv("n2", [54.7, 41], delay=0.3),
       mv("r11", [55, 17]), mv("n6", [55.5, 23], delay=0.2), mv("n7", [63.7, 23], delay=0.2), mv("n8", [64.5, 41], delay=0.3), mv("n9", [72.7, 41], delay=0.3)),
     S("Kein Durchkommen", "Rot zehn macht einen Haken nach rechts, aber die Blocker schieben sofort mit, und das Paar mit dem Leibchen weicht nach links aus. Nach einer Minute wechseln Blocker und Leibchen-Paar die Rollen.",
       mv("r10", [50, 15]), mv("n4", [45, 23], delay=0.2), mv("n5", [53.2, 23], delay=0.2), mv("n3", [38, 41], delay=0.3), mv("n2", [46.2, 41], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
