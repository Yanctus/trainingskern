import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 100-P5 (U12-U14, Woche 11 Phase 3): Finishing Around the Penalty Spot. 18 x 20 Yards = Feld x 22.2-77.8, y 5-55 (18 x 16 m).
# Gedreht: im PDF liegt das Tor rechts, hier oben (Jugendtor mit neutralem Torwart 1 -> "k" TW). Vier Stangen als Raute um den
# Elfmeterpunkt: erste Stange unten (50, 42), links (42, 32), rechts (58, 32), vorne (50, 23). Dunkelblau 9, 11, 7 -> Neon.
# Trainer (C) oben rechts neben dem Tor mit Bällen. Grundform = Phase 1 und 2, Steigerung = Phase 3 und 4 (im Original macht
# ein Spieler alle vier Phasen nacheinander). Wartende Spieler links und rechts neben dem Start-Hütchen.
# Sichtkegel: Im Ton "promoting awareness" (Phase 4); im Video kein Kegel eingezeichnet. Darum im Coaching-Punkt ein Blick
# zum Torwart vor dem Abschluss (Richtung aus dem Sinn: nahes oder langes Eck wählen).
T = P("T", "c", 70, 7, "T")
POS = {"n9": (45, 52), "n11": (36, 55), "n7": (60.5, 55), "k": (50, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i == "k" else P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 74.1, 10.5), B("s2", 77.7, 10.5)]
BAELLE = [B("b1", 70.6, 7.6), B("b2", 66.8, 10)]
LINES = [rect(22.2, 5, 55.6, 50)]
KEGEL = [C(46, 56), C(50, 42, shape="stange"), C(42, 32, shape="stange"), C(58, 32, shape="stange"), C(50, 23, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Abschluss am Elfmeterpunkt", "code": "UE-158", "kind": "Übungsform",
 "focuses": ["Torschuss", "Bewegung", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 4, "players_max": 8, "field_size": "18 x 16 m",
 "description": "Vier Stangen stehen als Raute um den Elfmeterpunkt. Der Stürmer läuft mit schnellen Schritten um die Stangen und kommt jedes Mal an einer anderen Stelle frei. Der Trainer spielt ihm den Ball zu, und er schießt direkt aufs Tor mit Torwart. Jeder Treffer gibt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 16 Metern vor einem Jugendtor. Vier Stangen als Raute um den Elfmeterpunkt, unten ein Start-Hütchen.",
  "Verteilen: Ein neutraler Torwart im Tor. Die Spieler von Team Neon stehen am Start-Hütchen. Der Trainer steht rechts neben dem Tor mit vielen Bällen.",
  "Ablauf: Der Stürmer läuft um die Stangen, der Trainer spielt flach zu, und der Stürmer schießt direkt. Gleich danach läuft er zur nächsten Stelle und schießt noch einmal.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach seinen Abschlüssen holt der Stürmer einen Ball zurück, und der Nächste ist dran."],
 "organisation_show": ORG,
 "coaching_points": ["Direkt abschließen und auf die Ecken zielen", "Mit schnellen, kurzen Schritten um die Stangen", "Je nach Pass ins nahe oder lange Eck schießen", "Nach dem Schuss sofort zur nächsten Stelle laufen"],
 "materials": ["1 Jugendtor", "4 Stangen", "1 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Abschluss am Elfmeterpunkt. Der Stürmer läuft um vier Stangen, kommt frei und schießt direkt, und jeder Treffer gibt einen Punkt.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Finte, dann außen herum", "Spieler neun läuft zuerst auf die erste Stange zu, als wollte er links vorbei. Dann dreht er ab und läuft rechts an ihr vorbei nach außen.",
     mv("n9", [47, 46]), mv("n9", [53.5, 45.5], after=True), mv("n9", [63, 34], after=True)),
   S("Direkt geschossen: Punkt", "Der Trainer spielt flach in den Lauf. Spieler neun schießt direkt ins nahe Eck, und das gibt einen Punkt für Spieler neun.",
     ps("b1", [63.6, 34.6]), ps("b1", [55.5, 5.3], after=True)),
   S("Rückwärts um die Stange", "Sofort geht es weiter. Spieler neun läuft mit schnellen, kleinen Schritten rückwärts um die rechte Stange, der Blick bleibt nach vorn.",
     mv("n9", [61, 39]), mv("n9", [55, 37.5], after=True), mv("n9", [53.6, 30], after=True)),
   S("Zweiter Schuss: Punkt", "An der vorderen Stange kommt der nächste Pass. Spieler neun schießt direkt, und das gibt wieder einen Punkt für Spieler neun. Dann holt er einen Ball, und Spieler elf ist dran.",
     ps("b2", [54.2, 30.6]), ps("b2", [56, 5.3], after=True))],
  "dims": dims(22.2, 77.8, 5, 55, "18 m", "16 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst zum Torwart schauen, dann schießen.", "Erst schauen, dann schießen",
    "Auf dem Weg zum Ball schaut der Stürmer kurz zum Torwart. Steht der Torwart am nahen Pfosten, geht der Schuss ins lange Eck. Steht er in der Mitte, zielt der Stürmer in die Ecke, die näher ist.",
    sp(n9=(52, 45.5)), BAELLE + ERSATZ,
    [S("Blick zum Torwart", "Spieler neun läuft außen an der rechten Stange vorbei und schaut dabei zum Torwart. Der Torwart geht schon zum nahen Pfosten.",
       mv("n9", [63, 34]), bl("n9", [55, 15], after=True), mv("k", [54, 9], delay=0.6)),
     S("Ins lange Eck: Punkt", "Der Trainer spielt zu. Spieler neun schießt direkt ins lange Eck, weit weg vom Torwart, und das gibt einen Punkt für Spieler neun.",
       ps("b1", [63.6, 34.6]), ps("b1", [44, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Vier Abschlüsse hintereinander.", "Vier Abschlüsse am Stück",
    "Jetzt kommen zwei weitere Laufwege dazu. Nach den ersten beiden Schüssen läuft der Stürmer rückwärts um die erste Stange und schießt an der vorderen Stange. Zum Schluss läuft er links um die Raute und bekommt einen flachen Pass quer durch den Strafraum.",
    sp(n9=(55.5, 26)), [B("b1", 70.6, 7.6), B("b2", 70.5, 12.5)] + ERSATZ,
    [S("Rückwärts um die erste Stange", "Spieler neun läuft rückwärts nach unten und um die erste Stange herum. Dann kommt er durch die Mitte zur vorderen Stange zurück.",
       mv("n9", [55.5, 38]), mv("n9", [53.5, 46], after=True), mv("n9", [46.5, 45.5], after=True), mv("n9", [46, 37], after=True), mv("n9", [52.4, 26.4], after=True)),
     S("Dritter Schuss: Punkt", "Der Trainer spielt zu, und Spieler neun schießt direkt ins rechte Eck. Das gibt einen Punkt für Spieler neun.",
       ps("b1", [53, 27]), ps("b1", [56.5, 5.3], after=True)),
     S("Links herum, vierter Schuss: Punkt", "Zum Schluss läuft Spieler neun links um die äußere Stange. Der Trainer spielt flach quer durch den Strafraum, Spieler neun schießt direkt, und das gibt einen Punkt für Spieler neun. Dann ist Spieler elf dran.",
       mv("n9", [45.5, 36.5]), mv("n9", [39.5, 36.5], after=True), mv("n9", [37, 30], after=True), mv("n9", [41, 23.5], after=True), mv("n9", [46.7, 18.6], after=True),
       ps("b2", [47.3, 19.2], after=True), ps("b2", [45, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
