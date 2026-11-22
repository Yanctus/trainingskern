import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P29 (U12-U14, Einzeltraining): 3-Phase Finishing - ST. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m), Tor oben
# wie im PDF. Drei Puppen als Stangen: Mitte (vor dem Stürmer), links schräg, eine mittig im Tor (knapp vor der Torlinie, steht
# für den Torwart; deshalb Jugendtor, aber ohne Torwart-Figur). Blauer Stürmer -> Spieler neun (Team Neon), ein Trainer.
# Trainer etwas nach links gesetzt (3D-Abstand zum Stürmer), Ballhaufen als zwei Ersatzbälle, dazu ein dritter Ball für Phase drei.
# Grundform = die drei Phasen nach PDF und Video (0:08-0:56): 1) auf die Puppe dribbeln, rechts vorbei, links ins Tor;
# 2) zwischen den Puppen annehmen, ablegen, außen um die linke Puppe, Steilpass rechts, Abschluss lange Ecke;
# 3) breit nach rechts, halb offen annehmen, Kontakt nach vorn, Abschluss lange Ecke. Reine Technikübung: Ziel statt Punkte.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: Coaching-Punkt halb offen annehmen (Key Coaching Point, Ton 0:43-0:54), Steigerung Puppen umgestellt und
# Schuss mit Effet ins rechte Eck (PDF Seite 2, Video ab 0:48).
T = P("T", "c", 41, 53, "T")
POS = {"n9": (50, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 35.5, 55), B("s2", 35.5, 52)]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
def puppen(um=False):
    if um: return [C(50, 6, shape="stange", id="k1"), C(35, 32, shape="stange", id="k2"), C(49, 37, shape="stange", id="k3")]
    return [C(50, 6, shape="stange", id="k1"), C(50, 27, shape="stange", id="k2"), C(37, 32, shape="stange", id="k3")]
BT = [41.6, 53.6]
LINKS = [45, 5.4]

u = {"title": "Drei Puppen, drei Abschlüsse", "code": "UE-269", "kind": "Übungsform",
 "focuses": ["Torschuss", "Dribbling", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Stürmer schließt aus drei verschiedenen Lagen ab. Zuerst dribbelt er auf eine Puppe zu, legt sich den Ball vorbei und schießt. Dann legt er für den Trainer ab, läuft außen um die zweite Puppe und schießt nach einem Steilpass ins lange Eck. Zum Schluss nimmt er außen halb offen an und schießt quer ins lange Eck.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern mit Jugendtor oben. Eine Puppe steht mittig im Tor, zwei Puppen davor: eine in der Mitte, eine links schräg.",
  "Verteilen: Spieler neun ist der Stürmer und startet unten mit Ball. Der Trainer steht unten links mit vielen Bällen.",
  "Ablauf: Phase eins: auf die Puppe dribbeln, vorbeilegen, abschließen. Phase zwei: ablegen, um die linke Puppe laufen, Steilpass, abschließen. Phase drei: außen halb offen annehmen, abschließen.",
  "Wechsel: Der Stürmer macht den ganzen Ablauf zweimal mit vollem Tempo. Dann folgt eine kurze Pause, danach geht es von vorn los."],
 "organisation_show": ORG,
 "coaching_points": ["Sauber schießen und die Ecken treffen", "Mit Tempo auf die Puppe zu und den Ball schnell vorbeilegen", "Halb offen annehmen, um schnell aufs Tor zu gehen", "Quer ins lange Eck schießen und das Tempo hochhalten"],
 "materials": ["1 Jugendtor", "3 Puppen oder Stangen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Drei Puppen, drei Abschlüsse. Spieler neun schießt in drei Phasen aus immer neuen Lagen, und jedes Mal zielt er genau in eine Ecke.",
 "board": {"lines": LINES, "goals": TORE, "cones": puppen(), "players": sp(),
  "balls": [B("b2", 50.6, 44.6), B("b1", *BT), B("b3", 45, 55.5)] + ERSATZ,
  "steps": [
   S("Phase eins: auf die Puppe", "Phase eins. Spieler neun dribbelt mit Tempo auf die Puppe in der Mitte zu.",
     dr("n9", "b2", [50, 34])),
   S("Vorbeilegen: Ziel", "Kurz vor der Puppe legt er sich den Ball schnell rechts vorbei. Dann schießt er links neben die Puppe im Tor. Das ist das Ziel.",
     dr("n9", "b2", [55.5, 32]), dr("n9", "b2", [57, 27], after=True), ps("b2", LINKS, after=True)),
   S("Phase zwei: Ablegen", "Phase zwei. Spieler neun läuft zwischen die beiden Puppen. Der Trainer passt zu ihm, und er legt den Ball direkt zurück.",
     mv("n9", [52, 35]), mv("n9", [44, 31], after=True), ps("b1", [44.6, 31.6], after=True), ps("b1", BT, after=True)),
   S("Um die Puppe, Steilpass", "Jetzt läuft Spieler neun außen um die linke Puppe herum und startet nach rechts. Der Trainer spielt ihm den Steilpass rechts neben die mittlere Puppe.",
     mv("n9", [38, 27.5]), mv("n9", [31.5, 31], after=True), mv("n9", [32, 38], after=True), mv("n9", [39, 41], after=True),
     mv("n9", [66, 30], after=True), ps("b1", [66.6, 30.6], delay=2.6)),
   S("Lange Ecke: Ziel", "Spieler neun schießt quer ins lange Eck. Das ist das Ziel.",
     ps("b1", LINKS)),
   S("Phase drei: Ziel", "Phase drei. Spieler neun geht breit nach rechts und nimmt den Pass halb offen an. Mit dem ersten Kontakt geht er nach vorn und schießt quer ins lange Eck. Das ist das Ziel. Den ganzen Ablauf macht er zweimal, dann gibt es eine kurze Pause.",
     mv("n9", [72, 37]), ps("b3", [72.6, 37.6], delay=0.5), dr("n9", "b3", [74, 29], after=True), ps("b3", LINKS, after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=83)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Halb offen annehmen.", "Halb offen annehmen",
    "Der Stürmer steht beim Annehmen nicht mit dem Rücken zum Tor. Er stellt sich halb offen hin, sieht Ball und Tor und nimmt den Ball mit dem ersten Kontakt nach vorn mit. So kann er sofort aufs Tor gehen und schnell abschließen.",
    sp(n9=(72, 37)), [B("b3", *BT)] + ERSATZ,
    [S("Halb offen hinstellen", "Spieler neun steht außen halb offen. Er sieht den Trainer und das Tor. Der Trainer passt zu ihm.",
       ps("b3", [72.6, 37.6])),
     S("Nach vorn, Schuss: Ziel", "Mit dem ersten Kontakt nimmt Spieler neun den Ball nach vorn mit. Dann schießt er sofort quer ins lange Eck. Das ist das Ziel.",
       dr("n9", "b3", [74, 29]), ps("b3", LINKS, after=True))],
    cones=puppen()),
  V("Steigerung", "Und jetzt die Steigerung: Die Puppen stehen anders, und Spieler neun schießt mit Effet.", "Mit Effet ins rechte Eck",
    "Die beiden Puppen vor dem Tor werden umgestellt. Der Stürmer startet links unten, dribbelt auf die Puppe zu und legt sich den Ball nach rechts vorbei. Dann schießt er mit Effet ins rechte Eck. So übt er Abschlüsse aus einem neuen Winkel.",
    sp(n9=(32, 44)), [B("b2", 32.6, 44.6), B("b1", *BT)] + ERSATZ,
    [S("Auf die Puppe", "Spieler neun dribbelt mit Tempo auf die linke Puppe zu.",
       dr("n9", "b2", [34, 39])),
     S("Mit Effet: Ziel", "Er legt sich den Ball nach rechts vorbei und schießt mit Effet ins rechte Eck. Das ist das Ziel. Dann kommt der nächste Ball.",
       dr("n9", "b2", [41.5, 34]), ps("b2", [56, 5.4], after=True, bend=-5))],
    cones=puppen(True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
