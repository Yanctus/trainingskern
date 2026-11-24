import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 51-P7 (U15-U17, Woche 23 Phase 3): False 9 Combinations to Penetrate (Technical Pattern). 30 x 20 Yards = 27 x 18 m
# (gerundet 18 x 25 m). LANGES FELD QUER (Vorbild ue317.py): Das Tor liegt rechts (im PDF oben), der Start links (im PDF unten).
# Direkt in Querkoordinaten geplant: Feld x 9-89, y 4-51. PDF links -> oben, PDF rechts -> unten.
# Ein Team (Pink -> Team Neon), Nummern wie im PDF (4, 6, 7, 8, 9, 10). Grüner Torwart -> neutraler Torwart (TW), Großfeldtor
# (nur C- und B-Jugend). Die zwei Mannequins sind Dummys (Stange), die Stange in der Mitte ist der Gegenspieler der Spitze.
# Wartende Spieler sechs und vier stehen an der Grundlinie hinter dem Start, weit auseinander (3D-Abstand). Ein Trainer statt zwei.
# Grundform = PDF-Ablauf (Pass auf die Spitze, raus auf den Flügel, Doppelpass hinter den Dummy, Abschluss) mit Wechsel.
# Fassung 1 = Key Coaching Point (Schulterblick vor der Annahme und Doppelbewegung an der Stange).
# Fassung 2 = Progression (Doppelpass mit dem einen Flügel, Pass in die Spitze, Steilpass für den anderen Flügel).
# Sichtkegel: im Video eingezeichnet (Coaching-Punkt: Kegel der Spitze über die Schulter Richtung Tor), Text/Ton "scan before
# receiving". Annehmen und Aufdrehen mit bl(von=...) und drehen() (half-turn, back foot).
T = P("T", "c", 30, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 33.5, 55.8), B("s2", 36, 55.8)]
TW = P("k", "t", 85, 27.5, "TW")
POS = {"n8": (17, 27.5), "n9": (39, 31), "n10": (57.5, 10.8), "n7": (57.5, 44), "n6": (7.5, 11.5), "n4": (7.5, 43.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
WARTE = [B("b6", 8.1, 12.1), B("b4", 8.1, 44.1)]
def baelle(x=17.6, y=28.1): return [B("b1", x, y)] + WARTE + ERSATZ
LINES = [rect(9, 4, 80, 47)]
TORE = [{"x": 89, "y": 27.5, "side": "right", "size": "gross"}]
STANGE = (45.5, 27.5)
CONES = [C(62.5, 15.2, shape="stange"), C(62.5, 38.5, shape="stange"), C(*STANGE, shape="stange"), C(12.5, 27.5)]
DIMS = dims(9, 89, 4, 51, "25 m", "18 m")[:1]  # Tor rechts: nur die Längen-Maßlinie
AN = [43, 19.5]      # hier nimmt die Spitze an, neben der Stange
RAUS = [55, 36.5]    # hier kommt Spieler sieben dem Ball entgegen

u = {"title": "Falsche Neun spielt Doppelpass", "code": "UE-363", "kind": "Übungsform",
 "focuses": ["Zusammenspiel", "Passspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 6, "players_max": 10,
 "field_size": "18 x 25 m",
 "description": "Ein festes Passmuster für die falsche Neun vor dem Tor. Die Spitze löst sich von der Stange, nimmt den Pass aus dem Mittelfeld halb aufgedreht an und spielt auf den Flügel. Mit einem Doppelpass schickt sie den Flügelspieler hinter den Dummy, und der schließt gegen den Torwart ab. Nach jedem Angriff wechseln die Rollen und die Seite.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern mit einem großen Tor und Torwart. In der Mitte steht eine Stange als Gegenspieler, weiter vorn auf beiden Seiten je ein Dummy. Am Start liegt ein Hütchen.",
  "Verteilen: Eine Spitze an der Stange, zwei Flügelspieler außen neben den Dummys. Die übrigen Spieler warten mit Ball am Start. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass vom Start auf die Spitze, die sich von der Stange löst. Sie dreht auf und spielt auf den Flügel, bekommt den Ball zurück und spielt den Flügelspieler hinter dem Dummy frei. Der schließt ab.",
  "Wechsel: Wer am Start gepasst hat, geht an die Stange, die Spitze geht auf den Flügel, der Schütze stellt sich am Start an. Nach jedem Angriff ist die andere Seite dran. Jeder Treffer gibt einen Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Erst weg, dann an die Stange kommen", "Vor dem Ball über die Schulter schauen", "Halb aufgedreht mit dem hinteren Fuß annehmen", "Genau passen, wenig Kontakte"],
 "materials": ["1 großes Tor", "1 Stange", "2 Dummys", "1 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Falsche Neun spielt Doppelpass. Die Spitze kommt von der Stange weg, dreht auf und schickt den Flügelspieler mit einem Doppelpass hinter den Dummy.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle(), "dims": DIMS,
  "steps": [
   S("Weg von der Stange, dann entgegen", "Spieler acht hat am Start den Ball. Spieler neun geht erst zwei Schritte Richtung Tor. Dann kommt er schnell neben die Stange zurück und schaut zum Ball. Jetzt kommt der Pass, flach in den Fuß.",
     mv("n9", [43.5, 34.5]), mv("n9", AN, after=True), bl("n9", [24, 25.4], after=True), ps("b1", [43.6, 20.1], after=True)),
   S("Halb aufgedreht raus auf den Flügel", "Spieler neun nimmt mit dem hinteren Fuß an und ist schon halb aufgedreht. Auf der anderen Seite kommt Spieler sieben ein paar Schritte nach innen. Da geht der Ball hin.",
     bl("n9", RAUS, von=[24, 25.4], dauer=1.3), drehen("n9", RAUS, gegen=True, delay=0.4), mv("n7", RAUS, delay=0.3),
     ps("b1", [55.6, 37.1], after=True)),
   S("Doppelpass hinter den Dummy", "Spieler neun läuft in die Mitte nach. Spieler sieben legt zurück und startet sofort außen um den Dummy. Spieler neun spielt ihm den Ball direkt in den Lauf.",
     mv("n9", [54, 26]), ps("b1", [54.6, 26.6], after=True), mv("n7", [62, 46.5], after=True), mv("n7", [70.5, 37], after=True),
     ps("b1", [71.1, 37.6], after=True)),
   S("Abschluss: Punkt", "Spieler sieben schießt flach am Torwart vorbei, und das gibt einen Punkt für Spieler sieben. Dann wird gewechselt. Spieler acht geht an die Stange, Spieler neun auf den Flügel, Spieler sieben stellt sich am Start an. Der nächste Angriff läuft über die andere Seite.",
     ps("b1", [88.5, 31]), mv("n8", [39, 31], delay=1.0), mv("n9", [57.5, 44], delay=1.0), mv("n7", [66, 33], delay=1.2), mv("n7", [16, 45], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst über die Schulter schauen, dann zweimal bewegen.", "Schauen, weg und entgegen",
    "Bevor der Ball kommt, schaut die Spitze über die Schulter. Wo steht der Gegenspieler, wo ist Platz? Dann geht sie erst weg und kommt mit Tempo zurück an die Stange. Angenommen wird halb aufgedreht mit dem hinteren Fuß, damit der nächste Pass sofort nach vorn geht.",
    sp(), baelle(),
    [S("Schulterblick, weg und zurück", "Spieler neun schaut zuerst über die Schulter Richtung Tor, dann zum Ball. Erst zwei Schritte weg, dann mit Tempo zurück neben die Stange. Genau in diesem Moment spielt Spieler acht.",
       bl("n9", [24, 25.4], von=[58, 23]), mv("n9", [43.5, 34.5], after=True), mv("n9", AN, after=True), ps("b1", [43.6, 20.1], after=True)),
     S("Hinterer Fuß, sofort nach vorn", "Spieler neun nimmt mit dem hinteren Fuß an, der Körper ist schon halb offen. Ein Kontakt zum Drehen, dann geht der Pass sofort raus zu Spieler sieben.",
       bl("n9", RAUS, von=[24, 25.4], dauer=1.3), drehen("n9", RAUS, gegen=True, delay=0.4), mv("n7", RAUS, delay=0.3),
       ps("b1", [55.6, 37.1], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Ball geht zum Flügelspieler auf der anderen Seite.", "Steil auf den anderen Flügel",
    "Jetzt spielt Spieler acht zuerst einen Doppelpass mit dem einen Flügelspieler. Danach geht der Ball in die Spitze. Die Spitze legt ihn sich vor und spielt steil auf die andere Seite, wo der zweite Flügelspieler hinter den Dummy startet. Der Steilpass kommt überraschend, die Spitze verrät vorher nicht, wohin sie spielt.",
    sp(), baelle(),
    [S("Doppelpass mit Spieler sieben", "Spieler sieben kommt vom Flügel entgegen und bekommt den Ball von Spieler acht. Spieler acht geht ein paar Schritte nach vorn und kriegt ihn gleich wieder.",
       mv("n7", [49, 42]), ps("b1", [49.6, 42.6], after=True), mv("n8", [30, 35], delay=0.6), ps("b1", [30.6, 35.6], after=True)),
     S("Pass in die Spitze", "Jetzt spielt Spieler acht in die Spitze. Spieler neun kommt von der Stange weg und schaut zum Ball.",
       mv("n9", [44, 33.5]), bl("n9", [30, 35], after=True), ps("b1", [44.6, 34.1], after=True)),
     S("Steil auf Spieler zehn: Punkt", "Spieler neun legt sich den Ball vor, dreht auf und spielt steil auf die andere Seite. Spieler zehn startet hinter dem Dummy, nimmt mit und trifft, und das gibt einen Punkt für Spieler zehn. Dann wird gewechselt, und es geht über die andere Seite.",
       bl("n9", [61.8, 20.6], von=[30, 35], dauer=1.3), drehen("n9", [61.8, 20.6], delay=0.4), mv("n10", [71, 14], delay=0.5),
       ps("b1", [71.6, 14.6], after=True), ps("b1", [88.5, 24], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
