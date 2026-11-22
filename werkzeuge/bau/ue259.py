import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P14 (U12-U14, Torwarttraining): Goalkeeper Passing and First Touches ("Goalkeeper Passing and 1st Touches GK-14").
# 10 x 10 Yards -> 9 x 9 m, Viereck x 30-70, y 10-50, Ausrichtung wie im PDF und Video. Vier Puppen als Stangen innen an den Ecken.
# Vier Torhüter neutral: k1 links (grün 1), k2 oben (gelb 1), k3 rechts (hellblau 13), k4 unten (dunkelblau 13); die Nummern sind
# im Original doppelt und hier weggelassen (Label TW). Ein Trainer außen links mit Bällen (im PDF unten rechts, im Video links).
# Passfolge wie im PDF: links -> rechts (Pass), rechts -> unten (zwei Kontakte), unten -> oben (direkt), dann weiter im Wechsel.
# Steigerung aus dem PDF und Video: vier Minitore außen an den Ecken (im Video schräg, hier gerade: oben mit Öffnung nach unten,
# unten mit Öffnung nach oben); der Trainer ruft ein Tor, der Torwart am Ball passt hinein. Keine Wertung (Ziel statt Punkte).
# Sichtkegel aus dem Text ("Scan to see next pass available"): in der Grundform schaut der untere Torwart vor der Annahme zum
# oberen, im Coaching-Punkt zum rechten Torwart. Im Video ist kein Kegel eingezeichnet (nur ein Kreis um den Torwart).
T = P("T", "c", 18, 42, "T")
POS = {"k1": (32, 30), "k2": (50, 12), "k3": (68, 30), "k4": (50, 48)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 21.6, 43.5), B("s2", 14.4, 43.5)]
def baelle(b1=(32.6, 30.6)):
    return [B("b1", *b1)] + ERSATZ
LINES = [rect(30, 10, 40, 40)]
CONES = [C(38, 20, shape="stange"), C(62, 20, shape="stange"), C(38, 40, shape="stange"), C(62, 40, shape="stange")]
MINITORE = [{"x": 27, "y": 6, "side": "top"}, {"x": 73, "y": 6, "side": "top"}, {"x": 27, "y": 54, "side": "bottom"}, {"x": 73, "y": 54, "side": "bottom"}]

u = {"title": "Passviereck der Torhüter", "code": "UE-259", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 4, "players_max": 4,
 "field_size": "9 x 9 m",
 "description": "Vier Torhüter stehen zwischen vier Puppen in einem kleinen Viereck und passen sich den Ball zu. Dabei wechseln sie ab: einmal mitnehmen und passen, einmal direkt spielen. Vor jeder Annahme schauen sie, wohin der nächste Pass geht, und nehmen den Ball auf dem hinteren Fuß an. Das geht so lange, bis der Trainer Pause ruft.",
 "organisation": ["Aufbauen: Ein Viereck von 9 mal 9 Metern, innen an den Ecken vier Puppen oder Stangen.",
  "Verteilen: Auf jeder Seite steht ein Torwart zwischen zwei Puppen. Der Trainer steht außen mit Bällen.",
  "Ablauf: Die Torhüter passen sich den Ball zu, abwechselnd mit zwei Kontakten und direkt, mal mit links, mal mit rechts. Vor der Annahme schauen, wohin der nächste Pass geht.",
  "Wechsel: Es geht weiter, bis der Trainer Pause ruft. Geht ein Ball verloren, gibt der Trainer einen neuen ins Spiel."],
 "organisation_show": ORG,
 "coaching_points": ["Saubere erste Ballkontrolle auf dem hinteren Fuß", "Genau passen, auf den hinteren Fuß des Mitspielers", "Vor der Annahme schauen, wohin der nächste Pass geht", "Füße zum Ball stellen, beide Füße benutzen und viel reden"],
 "materials": ["4 Puppen oder Stangen", "4 Minitore für die Steigerung", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Passviereck der Torhüter. Vier Torhüter lassen den Ball zwischen vier Puppen laufen, abwechselnd mit zwei Kontakten und direkt.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Pass quer", "Der linke Torwart passt quer durch das Viereck zum rechten Torwart.",
     ps("b1", [68.6, 30.6])),
   S("Mitnehmen und passen", "Der rechte Torwart nimmt den Ball mit dem ersten Kontakt nach innen mit. Der untere Torwart schaut schon, wo der obere steht. Dann kommt mit dem zweiten Kontakt der Pass zum unteren Torwart.",
     dr("k3", "b1", [64, 31]), bl("k4", [50, 30], after=True), ps("b1", [50.6, 48.6], after=True)),
   S("Direkt weiter", "Der untere Torwart spielt den Ball direkt, mit nur einem Kontakt, zum oberen Torwart.",
     ps("b1", [50.6, 12.6])),
   S("Immer weiter bis zur Pause", "Der obere nimmt den Ball wieder mit und passt zum linken Torwart. So läuft der Ball immer weiter, abwechselnd mit zwei Kontakten und direkt, mal mit links, mal mit rechts. Ruft der Trainer Pause, ist die Runde vorbei, und danach fängt ein anderer Torwart an.",
     dr("k2", "b1", [47, 15]), ps("b1", [32.6, 30.6], after=True))],
  "dims": dims(30, 70, 10, 50, "9 m", "9 m", rx=79)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Körper öffnen und auf dem hinteren Fuß annehmen.", "Auf dem hinteren Fuß",
    "Der Torwart schaut vor dem Pass, wohin er weiterspielen will, und öffnet seinen Körper dorthin. Er nimmt den Ball mit dem Fuß an, der weiter vom Passgeber weg ist. So sieht er das ganze Viereck und hält das Tempo hoch.",
    sp(), baelle(),
    [S("Körper öffnen", "Der untere Torwart schaut zum rechten Torwart und öffnet seinen Körper zu ihm. Dann passt der linke Torwart zu ihm.",
       bl("k4", [64, 36]), ps("b1", [50.6, 48.6], after=True)),
     S("Hinterer Fuß", "Er nimmt den Ball mit dem hinteren Fuß mit, gleich in Richtung des rechten Torwarts, und passt sofort weiter. So bleibt das Tempo hoch.",
       dr("k4", "b1", [54, 44]), ps("b1", [68.6, 30.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Auf Zuruf ins Minitor.", "Auf Zuruf ins Minitor",
    "Außen an den Ecken stehen jetzt vier Minitore. Die Torhüter passen weiter wie bisher. Ruft der Trainer ein Tor, nimmt der Torwart am Ball ihn auf dem hinteren Fuß an und passt genau in dieses Minitor.",
    sp(), baelle(),
    [S("Weiter passen", "Der linke Torwart passt zum oberen, und der obere passt weiter zum rechten Torwart.",
       ps("b1", [50.6, 12.6]), ps("b1", [68.6, 30.6], after=True)),
     S("Ins Minitor", "Der Trainer ruft: Rechts oben! Der rechte Torwart nimmt den Ball auf dem hinteren Fuß an und passt genau ins Minitor rechts oben.",
       dr("k3", "b1", [68, 25]), ps("b1", [72.5, 7], after=True)),
     S("Neuer Ball", "Der Trainer spielt einen neuen Ball zum linken Torwart, und es geht weiter.",
       ps("s1", [32.6, 30.6]))], goals=MINITORE)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
