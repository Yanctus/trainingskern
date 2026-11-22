import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-6 (im PDF GK-P6, U12-U14, Torwarttraining): Goalkeeper Quick Feet Handling Passing (Passing, Handling and Quick Feet).
# 20 x 15 Yards = Feld x 14-86, y 4-56 (18 x 14 m), Ausrichtung wie im PDF (Vierecke oben, Zuspieler unten), kein Tor.
# Zwei Vierecke aus je vier Hütchen: diagonal gleiche Farben, orange (im Original rot) und neongelb (im Original gelb).
# Je Viereck ein Torwart innen, unten ein Volley-Schütze und ein zweiter Torwart als Passgeber, wie im PDF.
# Abweichung: Im Original stehen zwei Trainer. Hier volleyt links der Trainer (genau einer) und rechts Spieler sieben von Team Neon.
# Torhüter: k1 links im Viereck, k2 links Passgeber, k3 rechts im Viereck, k4 rechts Passgeber. Beide Stationen laufen gleichzeitig.
# Grundform ohne Punkte (Technik), Ziel: jeden Ball fangen und jeden Pass genau spielen. Steigerung aus dem Ton
# ("Add competition between players, rewarding passing and handling technique, as well as reaction speed"): wer zuerst sauber fertig ist, bekommt einen Punkt.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 41, 42, "T")
POS = {"k1": (33.5, 18), "k2": (22, 42), "k3": (69.5, 18), "k4": (80, 42), "n7": (62, 45)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "t", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 42.6, 45.5), B("s2", 39, 45.5)]
def baelle(**k):
    d = {"b1": (41.6, 42.6), "b2": (22.6, 42.6), "b3": (62.6, 45.6), "b4": (80.6, 42.6)}; d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(14, 4, 72, 52)]
def viereck(x): return [C(x - 7.5, 11), C(x + 7.5, 11, "neon"), C(x - 7.5, 25, "neon"), C(x + 7.5, 25)]
CONES = viereck(33.5) + viereck(69.5)
def weg(who, punkte, erst_after=False):
    return [mv(who, punkte[0], after=erst_after or None)] + [mv(who, p, after=True) for p in punkte[1:]]
def verschoben(punkte, dx): return [[x + dx, y] for x, y in punkte]
# schnelle Füße um die zwei orangen Hütchen (oben links, unten rechts) und um die zwei neongelben (oben rechts, unten links)
ORANGE = [[30, 8], [26, 7.2], [22.2, 11], [26, 14.8], [33.5, 18], [37.5, 28.5], [41, 28.8], [44.8, 25], [41, 21.2], [33.5, 18]]
NEON = [[37, 8], [41, 7.2], [44.8, 11], [41, 14.8], [33.5, 18], [29.5, 28.5], [26, 28.8], [22.2, 25], [26, 21.2], [33.5, 18]]
L_FUSS, R_FUSS = [34.1, 18.6], [70.1, 18.6]
u = {"title": "Fangen und passen im Viereck", "code": "UE-261", "kind": "Übungsform",
 "focuses": ["Koordination", "Ballannahme", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 5, "field_size": "18 x 14 m",
 "description": "Der Torwart steht in einem Viereck aus vier Hütchen. Er läuft mit schnellen Füßen um zwei Hütchen der gleichen Farbe und fängt in der Mitte einen Volley. Dann rollt er den Ball zurück und bekommt einen Pass auf den Fuß, den er annimmt und genau zurückspielt. Zwei Vierecke laufen gleichzeitig.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern. Oben zwei Vierecke aus je vier Hütchen, diagonal gegenüber die gleiche Farbe.",
  "Verteilen: In jedem Viereck ein Torwart. Unten vor dem linken Viereck stehen der Trainer und ein zweiter Torwart mit Bällen, vor dem rechten Spieler sieben und ein vierter Torwart.",
  "Ablauf: Der Torwart läuft um die zwei orangen Hütchen und fängt in der Mitte einen Volley. Er rollt den Ball zurück, nimmt einen Pass mit dem Fuß an und spielt genau zurück. Dann das Gleiche um die neongelben Hütchen.",
  "Wechsel: Nach einer festen Zeit tauschen die Torhüter im Viereck mit den Passgebern. Ziel: jeden Ball festhalten und jeden Pass genau spielen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle, kleine Schritte um die Hütchen", "Den Ball sicher fangen und genau zurückrollen", "Den Pass nah am Fuß annehmen und flach und genau zurückspielen", "Auch müde konzentriert bleiben und in der Pause gut erholen"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": False,
 "say_intro": "Fangen und passen im Viereck. Der Torwart läuft um zwei Hütchen, fängt einen Volley und spielt danach mit dem Fuß.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Schnelle Füße", "In beiden Vierecken geht es gleichzeitig los. Wir schauen auf den linken Torwart. Er läuft mit schnellen Füßen um das orange Hütchen oben, dann um das orange Hütchen unten und zurück in die Mitte.",
     *weg("k1", ORANGE), *weg("k3", verschoben(ORANGE, 36))),
   S("Volley fangen", "Der Trainer spielt einen Volley, und der Torwart fängt den Ball. Rechts spielt Spieler sieben den Volley zum anderen Torwart.",
     ps("b1", L_FUSS), ps("b3", R_FUSS)),
   S("Zurückrollen", "Der Torwart rollt den Ball genau zurück zum Trainer. Rechts genauso zu Spieler sieben.",
     ps("b1", [41.6, 42.6]), ps("b3", [62.6, 45.6])),
   S("Pass auf den Fuß", "Jetzt passt der zweite Torwart flach auf den Fuß. Der Torwart im Viereck nimmt den Ball an und spielt ihn genau zurück.",
     ps("b2", L_FUSS), ps("b4", R_FUSS), ps("b2", [22.6, 42.6], delay=0.75), ps("b4", [80.6, 42.6], delay=0.75)),
   S("Neongelbe Hütchen: Wechsel", "Dann geht es um die zwei neongelben Hütchen, wieder mit Volley, Zurückrollen und Pass. Ist jeder Ball gefangen und jeder Pass genau, ist das Ziel erreicht. Nach einer festen Zeit tauscht der Torwart im Viereck mit dem Passgeber.",
     *weg("k1", NEON), *weg("k3", verschoben(NEON, 36)))],
  "dims": dims(14, 86, 4, 56, "18 m", "14 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Annehmen und genau zurückpassen.", "Nah annehmen, genau passen",
    "Jeder Pass zählt, auch beim Torwart. Er nimmt den Ball nah am Fuß an, damit er ihn sofort weiterspielen kann. Dann spielt er flach und mit dem richtigen Tempo genau in den Fuß des Passgebers. Auch beim Zurückrollen und Werfen zielt er genau, nie über den Kopf.",
    sp(), baelle(),
    [S("Pass kommt", "Der zweite Torwart passt flach auf den Fuß des Torwarts im Viereck.",
       ps("b2", L_FUSS)),
     S("Nah annehmen", "Der Torwart nimmt den Ball mit der Innenseite an. Der Ball bleibt ganz nah am Fuß.",
       dr("k1", "b2", [32, 20])),
     S("Genau zurück", "Dann spielt er flach und fest genau in den Fuß des Passgebers. So geht kein Ball verloren.",
       ps("b2", [22.6, 42.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer ist zuerst fertig?", "Wer ist zuerst fertig?",
    "Jetzt ist es ein Wettkampf zwischen den zwei Torhütern in den Vierecken. Beide starten gleichzeitig. Wer zuerst die ganze Folge sauber schafft, also ohne Ball fallen lassen und mit genauem Pass, bekommt einen Punkt.",
    sp(), baelle(),
    [S("Gleichzeitig los", "Der Trainer ruft, und beide Torhüter starten gleichzeitig um ihre orangen Hütchen.",
       *weg("k1", ORANGE), *weg("k3", verschoben(ORANGE, 36))),
     S("Fangen und rollen", "Beide fangen den Volley und rollen den Ball genau zurück.",
       ps("b1", L_FUSS), ps("b3", R_FUSS), ps("b1", [41.6, 42.6], delay=0.75), ps("b3", [62.6, 45.6], delay=0.75)),
     S("Zuerst fertig: Punkt", "Dann kommt der Pass auf den Fuß. Der linke Torwart nimmt an und spielt zuerst genau zurück, und das gibt einen Punkt für ihn. Dann geht es um die neongelben Hütchen.",
       ps("b2", L_FUSS), ps("b4", R_FUSS, delay=0.3), ps("b2", [22.6, 42.6], delay=0.75), ps("b4", [80.6, 42.6], delay=1.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
