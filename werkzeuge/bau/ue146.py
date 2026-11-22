import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 26-P4 (U12-U14, Woche 7 Phase 1): Goalkeeper Playing Out From the Back. 15 x 30 Yards = Feld x 37-63, y 5-57 (14 x 27 m),
# zwei Minitore oben, drei Dummys (zwei Stürmer, ein Mittelfeldspieler). Torwart unten, Neon 4 rechts, Neon 6 links, Neon 5 oben.
# Der zweite Torwart wartet nur im Text (er löst nach jedem Durchgang ab). Neon 5 steht seitlich neben dem oberen Dummy,
# Neon 4 und 6 etwas weiter von den Dummys weg (3D-Abstand). Ein Trainer. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 28, 46, "T")
POS = {"n1": (50.5, 51.3), "n4": (59, 35), "n6": (42, 35), "n5": (55, 14)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 29.6, 49.5), B("s2", 26, 49.5)]
LINES = [rect(37, 5, 26, 52), line(37, 20, 63, 20), line(37, 42, 63, 42)]
KEGEL = [C(50.2, 12.8, shape="stange"), C(44.7, 29.7, shape="stange"), C(55.4, 29.7, shape="stange")]
TORE = [{"x": 42, "y": 5, "side": "top"}, {"x": 58.5, "y": 5, "side": "top"}]
DRITTER = [mv("n6", [39.5, 29]), mv("n6", [41, 22], after=True)]

u = {"title": "Aufbau mit dem dritten Mann", "code": "UE-146", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 5, "players_max": 6, "field_size": "14 x 27 m",
 "description": "Ein festes Passmuster für den Spielaufbau mit dem Torwart. Drei Dummys stehen für zwei Stürmer und einen Mittelfeldspieler, die pressen. Der Torwart spielt nach außen, bekommt den Ball zurück und spielt steil in die Mitte. Von dort geht der Ball direkt in den Lauf des dritten Mannes, der ins Minitor schießt. Danach rücken alle eine Position weiter, die beiden Torhüter wechseln sich ab.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 27 Metern in drei Zonen, oben zwei Minitore. Drei Dummys: zwei in der Mitte, einer oben.",
  "Verteilen: Ein Torwart unten mit Ball, der zweite wartet daneben. Neon vier steht rechts, Neon sechs links, Neon fünf oben neben dem Dummy. Der Trainer steht links mit Bällen.",
  "Ablauf: Pass nach außen zu Neon vier, zurück zum Torwart, steil zu Neon fünf. Der legt direkt in den Lauf von Neon sechs, und der schießt ins Minitor.",
  "Wechsel: Nach dem Abschluss rücken alle eine Position weiter, und der zweite Torwart ist dran. Jedes Tor ist ein Punkt. Später auf der anderen Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Genau passen, damit der Ablauf flüssig bleibt", "Offen annehmen: so kann man aufdrehen oder zurücklegen", "Mit einer Doppelbewegung vom Gegenspieler lösen", "Den Ball in den Lauf des dritten Mannes spielen"],
 "materials": ["3 Dummys", "2 Minitore", "4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufbau mit dem dritten Mann. Der Torwart spielt mit, und mit einem festen Passmuster kommt der Ball an drei Gegnern vorbei bis zum Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 51.1, 51.9)] + ERSATZ,
  "steps": [
   S("Pass nach außen", "Neon vier läuft nach außen, und der Torwart spielt ihn an. Dann rückt der Torwart ein Stück nach vorn.",
     mv("n4", [61.5, 30.5]), ps("b1", [62.1, 31.1], delay=0.3), mv("n1", [51, 40], after=True)),
   S("Zurück zum Torwart", "Neon vier legt den Ball zurück zum Torwart. Gleichzeitig kommt Neon fünf dem Ball entgegen.",
     ps("b1", [51.6, 40.6]), mv("n5", [51, 21], delay=0.2)),
   S("Steil auf Neon fünf", "Der Torwart spielt steil zu Neon fünf, an den beiden Stürmern vorbei. Neon sechs startet schon nach vorn.",
     ps("b1", [51.6, 21.6]), mv("n6", [39.5, 29], delay=0.3)),
   S("Dritter Mann: Punkt", "Neon fünf legt den Ball direkt in den Lauf von Neon sechs, und der schießt ins linke Minitor. Das gibt einen Punkt für Team Neon. Dann rücken alle eine Position weiter, und der zweite Torwart ist dran.",
     mv("n6", [41, 22]), ps("b1", [41.6, 22.6], delay=0.2), ps("b1", [42, 5.3], after=True))],
  "dims": dims(37, 63, 5, 57, "14 m", "27 m", rx=70)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Doppelbewegung.", "Doppelbewegung",
    "Wer einfach stehen bleibt, wird vom Gegner zugestellt. Neon fünf läuft deshalb erst vom Ball weg, als wolle er in die Tiefe, und kommt dann scharf entgegen. So löst er sich vom Gegner und ist frei.",
    sp(n1=(51, 40), n4=(61.5, 30.5)), [B("b1", 51.6, 40.6)] + ERSATZ,
    [S("Erst weg vom Ball", "Der Torwart hat den Ball zurück. Neon fünf läuft zuerst weg, als wolle er in die Tiefe.",
       mv("n5", [58.5, 9])),
     S("Dann entgegen: Punkt", "Dann kommt er scharf entgegen und ist frei. Der Torwart spielt ihn an, er legt direkt auf Neon sechs, und der trifft ins Minitor. Das gibt einen Punkt für Team Neon.",
       mv("n5", [51, 21]), ps("b1", [51.6, 21.6], after=True), *DRITTER, ps("b1", [41.6, 22.6], after=True), ps("b1", [42, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Das Muster auf der anderen Seite.", "Andere Seite",
    "Jetzt läuft alles spiegelverkehrt: Neon sechs geht links nach außen, und Neon vier ist der dritte Mann. So übt jeder beide Seiten und beide Füße.",
    sp(), [B("b1", 51.1, 51.9)] + ERSATZ,
    [S("Links heraus, zurück", "Neon sechs läuft links nach außen und bekommt den Ball vom Torwart. Der rückt nach vorn, und Neon sechs legt zurück. Neon fünf kommt entgegen.",
       mv("n6", [38.5, 30.5]), ps("b1", [39.1, 31.1], delay=0.3), mv("n1", [51, 40], after=True), ps("b1", [51.6, 40.6], after=True), mv("n5", [51, 21], delay=0.6)),
     S("Dritter Mann rechts: Punkt", "Der Torwart spielt steil zu Neon fünf, der legt in den Lauf von Neon vier, und Neon vier trifft ins rechte Minitor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [51.6, 21.6]), mv("n4", [60.5, 28]), mv("n4", [59, 22], after=True), ps("b1", [59.6, 22.6], after=True), ps("b1", [58.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
