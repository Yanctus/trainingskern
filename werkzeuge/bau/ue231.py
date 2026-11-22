import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 101-P8 (U12-U14, Woche 36 Phase 6): Sprints, Heading and 1 v 1 Games. 20 x 25 Yards = Feld x 30.4-69.6, y 5-55 (18 x 23 m),
# Ausrichtung wie im Original (nicht gedreht): oben und unten je ein Jugendtor mit neutralem Torwart, links und rechts je zwei
# Stangen. Pink -> Neon (Werfer 10 unten, Läufer 5, Wartende 8, 4), Navy/Blau -> Rot (Werfer 2 oben, Läufer 9, Wartende 11, 6).
# Nummern neu (im Video doppelt): Blau 4 (Werfer) -> Rot 2. Grüne Torhüter 1 und 13 -> neutrale Torhüter TW.
# Wartende außerhalb des Feldes (3D-Abstand). Ein Trainer statt zwei: er spielt den Ball in die Mitte.
# Wie im Video köpft Neon ins untere Tor (Werfer unten) und greift im 1 gegen 1 das obere Tor an, Rot umgekehrt.
# Punkte für Kopfball und 1 gegen 1 im Original nicht genannt (dort nur Wettkampf der zwei Teams), hier ergänzt.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: Coaching-Punkt aus PDF und Ton (genau ins Ziel köpfen) und aus dem Ton (Körpertäuschung im 1 gegen 1).
T = P("T", "c", 24, 36, "T")
POS = {"n5": (33, 50), "n8": (24.5, 52), "n4": (16, 52), "n10": (41.5, 55.5), "k1": (50, 51),
       "r9": (67.5, 19), "r11": (76.5, 12), "r6": (76.5, 28), "r2": (59, 2), "k2": (50, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else ("a" if i[0] == "n" else "b"), x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 20.4, 39.5), B("s2", 16.8, 39.5)]
WURF = [B("b1", 42.1, 56.1), B("b2", 59.6, 2.6)]
LINES = [rect(30.4, 5, 39.2, 50)]
KEGEL = [C(x, y, shape="stange") for x, y in ((35.5, 17), (35.5, 28), (65, 29), (65, 40.5))]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Stangensprint und Hechtkopfball", "code": "UE-231", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Torschuss", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "18 x 23 m",
 "description": "Ein Staffel-Wettkampf zwischen zwei Teams: Aus jedem Team sprintet ein Spieler zweimal um zwei Stangen und läuft dann schräg zum Tor. Dort wirft ihm ein Mitspieler den Ball zu, und er köpft ihn im Hechtsprung aufs Tor. Danach springen beide schnell auf und sprinten zur Mitte, wo der Trainer einen Ball hineinspielt. Im Eins gegen Eins geht es um den Treffer am Torwart vorbei.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern, oben und unten ein Jugendtor mit Torwart. Links und rechts stehen je zwei Stangen hintereinander.",
  "Verteilen: Zwei Teams zu viert. Team Neon startet unten links, sein Werfer steht unten am Tor. Team Rot startet oben rechts, sein Werfer steht oben am Tor. Der Trainer steht links an der Seite mit Bällen.",
  "Ablauf: Je ein Spieler aus jedem Team sprintet gleichzeitig zweimal um seine Stangen, dann schräg zum Tor und köpft den Ball vom Werfer aufs Tor. Danach spielt der Trainer in die Mitte, und es gibt ein Eins gegen Eins: Team Neon greift oben an, Team Rot unten.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für sein Team. Ist das Eins gegen Eins vorbei, starten die nächsten zwei. Der Werfer tauscht nach dem zweiten Läufer. Nach jeder Runde drei Minuten Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Mit vollem Tempo um die Stangen sprinten", "Kurz und scharf wenden: abbremsen und wieder beschleunigen", "Beim Hechtkopfball das Tor treffen: Stirn, Augen offen", "Schnell aufstehen, zum Ball sprinten und mit einer Finte vorbei"],
 "materials": ["2 Jugendtore", "4 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Stangensprint und Hechtkopfball. Zwei Teams treten gegeneinander an: Sprint um die Stangen, Kopfball aufs Tor und danach ein Eins gegen Eins.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": WURF + [B("b3", 24.6, 36.6)] + ERSATZ,
  "steps": [
   S("Um die Stangen", "Spieler fünf und Spieler neun sprinten gleichzeitig los, jeder um seine zwei Stangen und wieder zurück.",
     *weg("n5", [[32.5, 14], [38.5, 14], [38.5, 31], [33, 48]]), *weg("r9", [[68, 44], [62, 44], [62, 26], [67.5, 21]])),
   S("Zweite Runde, zum Tor", "Gleich noch einmal um die Stangen. Dann laufen beide schräg zum Tor: Spieler fünf zum unteren, Spieler neun zum oberen.",
     *weg("n5", [[32.5, 14], [38.5, 14], [44, 44]]), *weg("r9", [[68, 44], [62, 44], [56, 16]])),
   S("Hechtkopfball", "Gleichzeitig werfen Spieler zehn und Spieler zwei den Ball hoch. Beide köpfen im Hechtsprung am Torwart vorbei, und jeder Treffer gibt einen Punkt für sein Team.",
     ps("b1", [44.6, 44.6]), ps("b1", [45.5, 54.7], after=True), ps("b2", [56.6, 16.6]), ps("b2", [54.5, 5.3], after=True)),
   S("Sprint zur Mitte", "Beide springen sofort auf und sprinten zur Mitte. Der Trainer spielt einen Ball hinein, und Spieler fünf ist zuerst dran.",
     ps("b3", [48.6, 33.6]), mv("n5", [48, 33], delay=0.2), mv("r9", [53, 26], delay=0.2)),
   S("Eins gegen eins: Punkt", "Spieler fünf dribbelt an Spieler neun vorbei und schießt ins obere Tor, und das gibt einen Punkt für Team Neon. Jetzt starten Spieler acht und Spieler elf.",
     dr("n5", "b3", [42, 24]), dr("n5", "b3", [44, 13], after=True), mv("r9", [48, 18], delay=0.4), ps("b3", [45.5, 5.3], after=True))],
  "dims": dims(30.4, 69.6, 5, 55, "18 m", "23 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Genau ins Ziel köpfen.", "Genau ins Ziel köpfen",
    "Beim Hechtkopfball zählt, dass der Ball aufs Tor geht. Den richtigen Moment zum Absprung abwarten, mit der Stirn köpfen und die Augen offen lassen. Lieber genau als hart.",
    sp(r9=(58.5, 22)), [B("b1", 42.1, 56.1), B("b2", 59.6, 2.6), B("b3", 24.6, 36.6)] + ERSATZ,
    [S("Absprung abwarten", "Spieler zwei wirft den Ball hoch. Spieler neun wartet auf den richtigen Moment und springt dann ab.",
       ps("b2", [59.1, 22.6])),
     S("Ins Ziel: Punkt", "Spieler neun köpft mit der Stirn genau in die Ecke, am Torwart vorbei. Das gibt einen Punkt für Team Rot.",
       ps("b2", [54.5, 5.3]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit einer Finte vorbei.", "Mit einer Finte vorbei",
    "Im Eins gegen Eins hilft eine Körpertäuschung oder ein Übersteiger. Der Verteidiger kommt aus dem Gleichgewicht, und mit einem schnellen Antritt geht es an ihm vorbei.",
    sp(n5=(48, 33), r9=(57, 25)), [B("b1", 42.1, 56.1), B("b2", 59.6, 2.6), B("b3", 48.6, 33.6)] + ERSATZ,
    [S("Antäuschen", "Spieler fünf hat den Ball. Er täuscht mit dem Körper nach rechts an, und Spieler neun geht mit.",
       dr("n5", "b3", [51, 30]), mv("r9", [54, 27], delay=0.2)),
     S("Vorbei: Punkt", "Dann zieht Spieler fünf schnell nach links an ihm vorbei und schießt ins obere Tor. Das gibt einen Punkt für Team Neon.",
       dr("n5", "b3", [44, 22]), dr("n5", "b3", [45, 13], after=True), ps("b3", [45.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
