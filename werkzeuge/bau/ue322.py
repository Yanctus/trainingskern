import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-114 (U15-U17, Woche 2 Pre-Season): Dribble, Set and Finish! 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m), letztes Drittel.
# FELD QUER (langes Feld, Vorbild ue317.py): Im PDF hochkant mit Tor oben; hier liegt die Länge waagrecht, Tor rechts
# (Großfeldtor mit neutralem Torwart, nur C- und B-Jugend). Die Gruppe rechts im PDF steht quer unten, die Gruppe links oben.
# Strafraum und Torraum wie im PDF, den Halbkreis am Strafraum weggelassen. Koordinaten direkt quer gesetzt (x 9-89, y 4-51).
# PDF pink -> Team Neon (9, 5, 6 wie im PDF; die zweite Wartende 8 nur im Text), gelb -> Team Rot neu nummeriert, weil die
# Nummern doppelt sind: 10 -> 10, 9 -> 11, 5 -> 7, 8 -> 8 (Verteidiger in den Steigerungen). Je Seite nur ein Wartender auf
# der Tafel (3D-Abstand hinter der Grundlinie), die übrigen im Text. Ein Trainer.
# Die Slalomstangen liegen versetzt in zwei Reihen (drei je Seite). Am Ende des Slaloms steht das Hütchen neben dem Strafraum,
# dort dreht der Dribbler auf (drehen) und spielt zurück in die Mitte.
# Sichtkegel wie im Video („Check GK's positioning“, Text „Scan the goalkeeper's position before deciding where to shoot“):
# Der Abschlussspieler schaut erst zum Passgeber (Annahme), dann schwenkt der Kegel zum Torwart (bl mit von).
# Fassungen: PDF Progression 1 (2 gegen 1 mit Hinterlaufen, Video: „Caught on outside, dribble inside“) und Progression 2
# (2 gegen 2, Start mit Pass und Hinterlaufen, Video: „Draw the defender inside“). Beide als Steigerung.
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
T = P("T", "c", 30, 55.3, "T")
ERSATZ = [B("s1", 33.5, 55.8), B("s2", 36, 55.8)]
GK = P("k", "t", 85, 27.5, "TW")
POS = {"n9": (19.1, 46.3), "n5": (6, 49), "n6": (20.2, 27.5), "r10": (17, 9.7), "r11": (3, 9), "r7": (11.5, 26.4)}
def sp(extra=(), ohne=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items() if i not in ohne] + list(extra) + [GK, T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
STANGEN = [(30.6, 48.5), (38.6, 41), (46.6, 48.5), (30.6, 6.5), (38.6, 14), (46.6, 6.5)]
CONES = [C(x, y, shape="stange") for x, y in STANGEN] + [C(68.2, 45.8), C(68.2, 8.9)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), rect(60.7, 8.9, 28.3, 37.4), rect(79.7, 19, 9.3, 17)]
TORE = [{"x": FX1, "y": 27.5, "side": "right", "size": "gross"}]
DIMS = [{"x1": FX0, "y1": 58.6, "x2": FX1, "y2": 58.6, "text": "40 m"}]
def slalom_unten(who, ball, **k):
    pk = [[30.6, 44.2], [38.6, 45.3], [46.6, 44.2], [64.5, 44]]
    return [dr(who, ball, pk[0], **k)] + [dr(who, ball, p, after=True) for p in pk[1:]]
def slalom_oben(who, ball, **k):
    pk = [[30.6, 10.8], [38.6, 9.7], [46.6, 10.8], [64.5, 11]]
    return [dr(who, ball, pk[0], **k)] + [dr(who, ball, p, after=True) for p in pk[1:]]
WENDE = [64.5, 44]
ANNAHME = [36, 27.5]
BLICK = [53.3, 37.5]  # Richtung Passgeber am Hütchen, Kegel kürzer als der ganze Weg
BALLS = [B("b1", *fuss("n9")), B("b5", *fuss("n5")), B("b10", *fuss("r10")), B("b11", *fuss("r11"))] + ERSATZ

u = {"title": "Slalom, Pass in den Fuß, Schuss", "code": "UE-322", "kind": "Übungsform",
 "focuses": ["Torschuss", "Dribbling", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "25 x 40 m",
 "description": "Abschluss mit Tempo für die Vorbereitung. Ein Spieler dribbelt durch den Stangenslalom, dreht am Hütchen scharf auf und spielt flach in den Fuß des Mitspielers in der Mitte. Der nimmt den Ball mit einem Kontakt mit, schaut zum Torwart und schließt ab. Die beiden Seiten wechseln sich ab, so läuft die Übung ohne Pause.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern im letzten Drittel mit Strafraum und Tor. Auf beiden Seiten stehen drei Stangen versetzt für den Slalom, am Ende jeder Bahn ein Hütchen neben dem Strafraum.",
  "Verteilen: Zwei Teams, je drei Spieler mit Ball an ihrer Slalombahn und einer in der Mitte. Ein neutraler Torwart im Tor. Der Trainer steht mit Ersatzbällen an der Seitenlinie.",
  "Ablauf: Slalom mit Ball, am Hütchen aufdrehen, flacher Pass in die Mitte. Der Mittelspieler legt sich den Ball vor und schießt. Dann startet die andere Seite.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team. Der Schütze holt sich einen neuen Ball und stellt sich an seiner Bahn hinten an, der Passgeber geht in die Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Enge Kontakte durch die Stangen", "Am Hütchen scharf aufdrehen", "Flach und scharf in den Fuß passen", "Vor dem Schuss zum Torwart schauen"],
 "materials": ["1 Tor", "6 Stangen", "2 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Slalom, Pass in den Fuß, Schuss. Erst mit Ball durch die Stangen, dann flach in die Mitte, und der Mitspieler schließt ab. Immer im Wechsel, von beiden Seiten.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BALLS,
  "steps": [
   S("Slalom durch die Stangen", "Spieler neun startet mit Ball. Enge Kontakte, links und rechts an den Stangen vorbei, und mit Tempo raus bis zum Hütchen.",
     *slalom_unten("n9", "b1")),
   S("Aufdrehen und Pass in die Mitte", "Am Hütchen dreht er scharf auf. Spieler sechs kommt ihm ein paar Schritte entgegen und schaut zum Ball. Flach und scharf in den Fuß.",
     drehen("n9", ANNAHME, gegen=True), mv("n6", ANNAHME, delay=0.2), bl("n6", BLICK, after=True), ps("b1", [36.6, 28.1], after=True)),
   S("Blick zum Torwart, Abschluss", "Spieler sechs legt sich den Ball mit dem ersten Kontakt vor. Kopf hoch, wo steht der Torwart? Dann schießt er flach ins lange Eck.",
     bl("n6", [56, 26], von=BLICK, dauer=1.3), dr("n6", "b1", [50, 24], delay=0.4), ps("b1", [88.7, 33], after=True)),
   S("Punkt, dann die andere Seite", "Drin, und das gibt einen Punkt für Team Neon. Spieler sechs holt sich einen neuen Ball und stellt sich hinter Spieler fünf an, Spieler neun geht in die Mitte. Und schon startet auf der anderen Seite Spieler zehn.",
     mv("n6", [30, 34]), mv("n6", [4, 42], after=True), mv("n9", [40, 36], delay=0.2), mv("n9", [20.2, 27.5], after=True),
     *slalom_oben("r10", "b10", delay=0.6))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei gegen eins mit Hinterlaufen.", "Zwei gegen eins, hinterlaufen",
    "Ein Verteidiger von Team Rot wartet vor dem Strafraum. Nach seinem Pass in die Mitte hinterläuft der Passgeber den Mitspieler und kommt auf der anderen Seite mit. Der Ballführer dribbelt nach innen, nicht nach außen, dann hat er beide Seiten offen.",
    sp(extra=[P("r8", "b", 59.7, 23.1, "8")], n9=(64.5, 44)), [B("b1", 65.1, 44.6), B("b5", *fuss("n5")), B("b10", *fuss("r10")), B("b11", *fuss("r11"))] + ERSATZ,
    [S("Pass in die Mitte, hinterlaufen", "Spieler neun hat aufgedreht und spielt in die Mitte zu Spieler sechs. Sofort hinterläuft er ihn, hinten herum auf die andere Seite.",
       mv("n6", [34, 28]), ps("b1", [34.6, 28.6], after=True), mv("n9", [48, 37], delay=0.6), mv("n9", [32, 35], after=True),
       mv("n9", [25, 27], after=True), mv("n9", [30, 17], after=True)),
     S("Nach innen andribbeln", "Spieler sechs dribbelt nach innen, genau auf Spieler acht zu. Der muss raus und kann nicht beide decken. Außen kommt Spieler neun mit.",
       dr("n6", "b1", [47, 26]), mv("r8", [54, 25], delay=0.3), mv("n9", [42, 18]), mv("n9", [52, 13], after=True)),
     S("Querpass: Punkt", "Jetzt der Pass zu Spieler neun. Der ist frei und schießt direkt, und das gibt einen Punkt für Team Neon.",
       ps("b1", [52.6, 13.6]), ps("b1", [88.7, 24.5], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei gegen zwei.", "Zwei gegen zwei",
    "Jetzt verteidigen zwei Spieler von Team Rot. Der Slalom fällt weg, es geht los mit Pass und Hinterlaufen. Der Ballführer dribbelt in die Lücke zwischen beide Verteidiger und zieht sie zu sich, dann spielt er ab. Nach höchstens drei Kontakten soll der Abschluss kommen.",
    sp(extra=[P("r8", "b", 61.5, 16.1, "8"), P("r11", "b", 65.6, 35.1, "11")], ohne=("r11",), n9=(23.4, 23.6), n6=(36.7, 30.9), r10=(14, 6.5)),
    [B("b1", 24, 24.2), B("b5", *fuss("n5")), B("b10", 14.6, 7.1)] + ERSATZ,
    [S("Pass und hinterlaufen", "Spieler neun spielt zu Spieler sechs und hinterläuft ihn sofort außen.",
       ps("b1", [37.3, 31.5]), mv("n9", [30, 37], delay=0.3), mv("n9", [44, 37.5], after=True)),
     S("In die Lücke dribbeln", "Spieler sechs zieht in die Lücke zwischen beide Verteidiger. Spieler acht und Spieler elf gehen beide auf ihn. Außen ist jetzt Platz für Spieler neun.",
       dr("n6", "b1", [52, 26]), mv("r8", [56, 21], delay=0.3), mv("r11", [58, 31], delay=0.3), mv("n9", [56, 43])),
     S("Abspielen und abschließen: Punkt", "Jetzt der Pass nach außen. Spieler neun schießt sofort, und das gibt einen Punkt für Team Neon.",
       ps("b1", [56.6, 43.6]), ps("b1", [88.7, 31], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
