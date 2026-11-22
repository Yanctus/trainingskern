import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 82-P2 (U12-U14, Woche 41 Phase 3): Finishing & Speed Circuit. 25 x 35 Yards = Feld x 32.1-67.9, y 5-55 (23 x 32 m).
# Gedreht: im PDF liegt das Tor links, hier um 90 Grad im Uhrzeigersinn gedreht (Tor oben; die erste Station oben im PDF liegt
# hier rechts, die Passstation unten im PDF hier links, die Stürmerstation rechts im PDF hier unten).
# Pink -> Team Neon mit den Nummern aus dem PDF: 8 läuft (Doppelpass mit 4, Hürde), 10 passt quer, 9 ist Stürmer. Wartende
# (6 an Station eins, 3 und 7 an der Passstation, 11 und 5 an der Stürmerstation) nur im Text (3D-Abstand). Grüne Torhüter 1 und 13
# -> neutraler Torwart TW (der zweite nur im Text). Spieler acht und vier leicht auseinandergerückt (3D-Abstand), Stations-Hütchen
# leicht versetzt (sonst im Passweg). Eine Minihürde (huerde, Stange senkrecht, der Lauf geht quer darüber). Zwei Puppen als Stangen.
# Ein Trainer statt zwei, er steht rechts neben dem Feld. Der Stationswechsel wird nur gesagt, nicht gezeigt.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: Coaching-Punkt eng dribbeln und flach ins Eck (PDF Seite 2, Ton 0:24-0:38), Steigerung Passgeber wird passiver
# Verteidiger (PDF Seite 2, Ton und Video ab 0:39; die Rufe "eins"/"zwei" für aktiv/passiv nur im Text).
T = P("T", "c", 75, 46, "T")
POS = {"k": (50, 7.5), "n4": (71.5, 20), "n8": (63, 20), "n10": (37.5, 17), "n9": (55, 42)}
def sp(ohne=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i == "k" else "a", x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items() if i not in ohne] + [T]
ERSATZ = [B("s1", 78.6, 49.5), B("s2", 75, 49.5)]
LINES = [rect(32.1, 5, 35.8, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
KEGEL = [C(52.2, 27.9, shape="stange"), C(47.7, 27.9, shape="stange"), C(59.5, 20, shape="huerde"),
         C(72, 25), C(34.5, 21), C(51, 44.5)]
UM_DIE_PUPPE = [(49, 33), (43.5, 29.5), (44, 22)]

u = {"title": "Doppelpass, Hürde, Abschluss", "code": "UE-247", "kind": "Übungsform",
 "focuses": ["Torschuss", "Passspiel", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 12, "field_size": "23 x 32 m",
 "description": "Ein Kreislauf mit drei Stationen vor einem Tor mit Torwart. Ein Spieler spielt einen Doppelpass, springt über eine Hürde und bekommt den Ball von der anderen Seite. Er legt für den Stürmer ab, der um die Puppen dribbelt und ins Eck schießt. Danach rückt jeder eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern mit einem Jugendtor oben. Rechts die erste Station mit einer Minihürde, links die Passstation, unten die Stürmerstation, in der Mitte zwei Puppen.",
  "Verteilen: An jeder Station stehen zwei bis drei Spieler, an der ersten und an der Passstation mit Bällen. Ein Torwart steht im Tor, ein zweiter wartet. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Doppelpass an der ersten Station, Sprung über die Hürde, Pass quer von der Passstation, Ablage für den Stürmer. Der Stürmer dribbelt um die Puppen und schließt ab.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Der Ableger sprintet zur Passstation, der Passgeber geht zur Stürmerstation, der Stürmer zur ersten Station. Die Torhüter wechseln nach zwei bis drei Schüssen."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und hart in die Ecken schießen", "Den Ball beim Dribbling um die Puppen eng führen", "Genau und mit dem richtigen Tempo passen", "Mit vollem Tempo durch den Kreislauf, schnell über die Hürde"],
 "materials": ["1 Jugendtor", "2 Stangen als Puppen", "1 Minihürde", "3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Doppelpass, Hürde, Abschluss. Ein schneller Kreislauf mit drei Stationen, und am Ende schließt der Stürmer ab.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(),
  "balls": [B("b1", 72.1, 20.6), B("b2", 38.1, 17.6)] + ERSATZ,
  "steps": [
   S("Doppelpass", "Spieler vier passt zu Spieler acht, und der spielt direkt zurück. Das ist der Doppelpass.",
     ps("b1", [63.6, 20.6]), ps("b1", [72.1, 20.6], after=True)),
   S("Hürde, Pass quer", "Spieler acht springt über die Hürde und sprintet weiter. Spieler zehn passt ihm den Ball quer in den Lauf.",
     mv("n8", [56, 19.5]), ps("b2", [56.6, 20.1], delay=0.5)),
   S("Ablage zum Stürmer", "Spieler neun kommt entgegen, und Spieler acht legt ihm den Ball mit einem Kontakt ab.",
     mv("n9", [57, 33]), ps("b2", [57.6, 33.6], after=True)),
   S("Um die Puppe: Punkt", "Spieler neun dribbelt eng um die Puppe und schießt flach ins lange Eck, und das gibt einen Punkt. Dann sprintet Spieler acht zur Passstation, Spieler zehn geht zur Stürmerstation, und Spieler neun stellt sich an der ersten Station an. Der Nächste von der ersten Station ist dran.",
     *[dr("n9", "b2", list(p), after=True if i else None) for i, p in enumerate(UM_DIE_PUPPE)],
     mv("k", [47.5, 8], after=True), ps("b2", [54.5, 5.4], after=True))],
  "dims": dims(32.1, 67.9, 5, 55, "23 m", "32 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Eng am Ball und flach ins Eck.", "Eng am Ball, flach ins Eck",
    "Der Stürmer führt den Ball um die Puppe mit vielen kleinen Kontakten, so bleibt er immer nah am Fuß. Beim Schuss ist der Kopf über dem Ball. Er schießt flach und hart in die Ecke, Genauigkeit ist wichtiger als Wucht.",
    sp(ohne=("n8",), n9=(57, 33)), [B("b2", 57.6, 33.6)] + ERSATZ,
    [S("Eng um die Puppe", "Spieler neun führt den Ball mit vielen kleinen Kontakten eng um die Puppe.",
       *[dr("n9", "b2", list(p), after=True if i else None) for i, p in enumerate(UM_DIE_PUPPE)]),
     S("Flach ins Eck: Punkt", "Der Kopf ist über dem Ball. Spieler neun schießt flach ins lange Eck, genau statt mit Wucht, und das gibt einen Punkt.",
       mv("k", [47.5, 8]), ps("b2", [54.5, 5.4], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Ableger wird zum Verteidiger.", "Ableger wird Verteidiger",
    "Nach der Ablage dreht Spieler acht um und stellt sich dem Stürmer in den Weg. Ruft der Trainer „zwei“, verteidigt er nur passiv, ruft er „eins“, greift er richtig an. Der Stürmer muss schnell reagieren und an ihm vorbei abschließen.",
    sp(n8=(58.5, 23.5)), [B("b2", 59.1, 24.1)] + ERSATZ,
    [S("Ablage, dann verteidigen", "Spieler neun kommt entgegen, und Spieler acht legt ab. Dann dreht Spieler acht sofort um und stellt sich dem Stürmer in den Weg.",
       mv("n9", [57, 33]), ps("b2", [57.6, 33.6], after=True), mv("n8", [48, 22], after=True)),
     S("Vorbei und rein: Punkt", "Spieler neun dribbelt rechts an der Puppe vorbei. Spieler acht verteidigt passiv und kommt nicht an den Ball. Spieler neun schießt flach ins Eck, und das gibt einen Punkt.",
       dr("n9", "b2", [57, 26]), dr("n9", "b2", [54, 21], after=True), mv("n8", [51, 22], delay=0.4), mv("k", [53, 8], after=True),
       ps("b2", [45, 5.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
