import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P17 (U12-U14, Torwarttraining): Quick Reactions to Make Saves. Feld 50 x 45 Yards = x 14-86, y 5-55 (46 x 41 m), Tor oben
# wie im PDF und im Video. Strafraum x 24-76, y 5-23.8 und Torraum x 38-62, y 5-11.3 nach den Anteilen der PDF-Skizze
# (Halbkreis weggelassen). Puppe als Stange vor dem Torraum etwas links von der Mitte. Jugendtor mit Torwart k1.
# Zwei Trainer im Original: der Flankengeber links wird Spieler sieben (Team Neon), der Schütze an der Strafraumkante ist der
# Trainer. Der zweite Torwart k2 (lila im PDF) wartet links neben dem Tor und ist in der nächsten Runde dran.
# Steigerung (Progression 1): Im Original volleyen zwei Trainer von beiden Seiten, und der Rückpass geht zum passiven zweiten
# Torwart an der Strafraumkante, der abschließt. Hier: Spieler sieben links, Trainer rechts, Spieler acht (Team Neon) schließt
# an der Strafraumkante ab (Regel: Schützen sind Trainer oder Spieler von Team Neon). Der zweite Torwart wartet weiter neben dem Tor.
# Keine Wertung im Original: Ziel statt Punkte.
# Sichtkegel aus Text und Ton ("eyes focused on the ball", "eye contact with the ball", "sharp scanning", "adjust your
# positioning and scanning when the cutback is played"): Grundform und Coaching-Punkt schaut der Torwart zum Ball, in der
# Steigerung nach dem Rückpass zu Spieler acht. Im Video kein Kegel eingezeichnet; Richtung aus dem Sinn.
T = P("T", "c", 50, 27, "T")
POS = {"k1": (44, 7.5), "n7": (17.5, 13.5), "k2": (30, 2.5)}
def sp(T=T, **k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i[0] == "k" else "a", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
def baelle(**k):
    d = {"b7": (18.1, 14.1), "b1": (50.6, 27.6), "s1": (53.6, 30.5), "s2": (46.4, 30.5)}
    d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()]
LINES = [rect(14, 5, 72, 50), rect(24, 5, 52, 18.8), rect(38, 5, 24, 6.3)]
CONES = [C(47, 13.5, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
T2 = P("T", "c", 77, 11, "T")

u = {"title": "Erst parieren, dann um die Puppe", "code": "UE-267", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 4, "field_size": "46 x 41 m",
 "description": "Torwarttraining für schnelle Reaktionen nach der ersten Parade. Spieler sieben spielt flach von der Seite in Richtung Puppe, und der Torwart taucht ab und lenkt den Ball zur Seite weg. Dann steht er sofort auf, läuft hinter der Puppe herum und hält den Schuss des Trainers von der Strafraumkante.",
 "organisation": ["Aufbauen: Im Strafraum vor einem Jugendtor. Vor dem Torraum steht etwas links von der Mitte eine Puppe oder Stange.",
  "Verteilen: Der Torwart steht am linken Pfosten. Spieler sieben steht links außen mit Bällen, der Trainer an der Strafraumkante mit Bällen. Der zweite Torwart wartet neben dem Tor.",
  "Ablauf: Spieler sieben spielt flach in Richtung Puppe. Der Torwart taucht ab und lenkt den Ball zur Seite weg. Dann steht er auf, läuft hinter der Puppe herum, und der Trainer schießt sofort aufs Tor.",
  "Wechsel: Nach jeder Runde ist der zweite Torwart dran. Die Torhüter loben sich gegenseitig für gute Paraden."],
 "organisation_show": ORG,
 "coaching_points": ["Leicht auf den Zehen stehen, Gewicht nach vorn", "Hände tief halten und die Augen immer am Ball", "Den ersten Ball zur Seite weg lenken, nie in die Mitte", "Sofort aufstehen und schnell wieder vors Tor"],
 "materials": ["1 Jugendtor", "1 Puppe oder Stange", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Erst parieren, dann um die Puppe. Der Torwart lenkt eine flache Hereingabe weg und muss gleich danach den nächsten Schuss halten.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": baelle(),
  "steps": [
   S("Bereit am Pfosten", "Der Torwart steht am linken Pfosten, leicht auf den Zehen, das Gewicht nach vorn. Er schaut genau auf den Ball bei Spieler sieben.",
     bl("k1", [20, 13.5])),
   S("Flach von der Seite", "Spieler sieben spielt flach in Richtung Puppe. Der Torwart taucht ab und lenkt den Ball weg vom Tor zur Seite.",
     ps("b7", [43.6, 12.1]), mv("k1", [43, 11.5], delay=0.3), ps("b7", [30, 22], after=True)),
   S("Hinter der Puppe herum", "Sofort steht der Torwart auf und läuft hinter der Puppe herum auf die andere Seite.",
     mv("k1", [47, 9.5]), mv("k1", [52.5, 10.5], after=True)),
   S("Zweiter Schuss gehalten", "Der Trainer schießt direkt aufs Tor, und der Torwart hält den Ball. Die Runde ist vorbei, und jetzt ist der zweite Torwart dran.",
     bl("k1", [50.6, 26]), ps("b1", [53.1, 11.1], after=True))],
  "dims": dims(14, 86, 5, 55, "46 m", "41 m", rx=93)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Hände tief, Augen am Ball.", "Hände tief, Augen am Ball",
    "Flache, harte Schüsse kommen schnell. Der Torwart hält die Hände deshalb tief und schaut immer auf den Ball, bis er ihn in den Händen hat. So kann er schneller reagieren.",
    sp(k1=(52.5, 10.5)), baelle(b7=(30, 22)),
    [S("Augen am Ball", "Der Torwart ist hinter der Puppe herum. Er steht leicht auf den Zehen, die Hände tief, und schaut genau auf den Ball beim Trainer.",
       bl("k1", [50.6, 26])),
     S("Flach gehalten", "Der Trainer schießt flach und hart. Der Torwart geht mit tiefen Händen zum Ball und hält ihn fest.",
       ps("b1", [56.1, 10.6]), mv("k1", [55.5, 10], delay=0.2))]),
  V("Steigerung", "Und jetzt die Steigerung: Rückpass an die Strafraumkante.", "Rückpass an die Kante",
    "Spieler sieben steht links, der Trainer rechts, Spieler acht an der Strafraumkante. Beide spielen dem Torwart den Ball abwechselnd in die Hände, und er schiebt schnell von einer Seite zur anderen. Bei einem Ball spielt der Trainer überraschend zurück zu Spieler acht, und der schießt sofort.",
    sp(T=T2, k1=(40, 12.5), n8=(50, 27)), baelle(b1=(77.6, 11.6), s1=(80.6, 14.5), s2=(77, 15)),
    [S("Volley von links", "Spieler sieben spielt dem Torwart den Ball in die Hände. Der Torwart fängt ihn und wirft ihn zurück.",
       ps("b7", [40.6, 13.1]), ps("b7", [18.1, 14.1], after=True)),
     S("Rüber nach rechts", "Sofort läuft der Torwart hinter der Puppe herum auf die rechte Seite.",
       mv("k1", [47, 9.5]), mv("k1", [56, 12.5], after=True)),
     S("Rückpass", "Der Trainer spielt aber nicht zum Torwart, sondern zurück zu Spieler acht. Der Torwart schaut sofort zu Spieler acht.",
       ps("b1", [50.6, 27.6]), bl("k1", [50, 26], after=True)),
     S("Schnell vors Tor", "Spieler acht schießt sofort. Der Torwart schiebt schnell zurück vor das Tor und hält den Ball. Dann ist der zweite Torwart dran.",
       ps("b1", [53.6, 7.6]), mv("k1", [53, 7]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
