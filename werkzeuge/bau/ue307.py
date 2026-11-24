import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 69-P5 (U15-U17, Woche 12): Compact Midfield to Stop Forward Passes. 16 x 32 Yards = 15 x 29 m (gerundet 15 x 30 m), hochkant
# wie im PDF, Feld x 20-80, y 5-55: in der Breite gestreckt (15 m auf 60 Einheiten), damit die Dreierkette, der Springer und
# die Außenspieler den 3D-Abstand halten. Mittelzone (5 Yards) y 26-34 mit vier Minitoren, je zwei pro Hälfte, Rücken an Rücken.
# PDF blau -> Team Neon: außen unten 5, 2, 3, Dreierkette oben 6, 10, 8. PDF pink -> Team Rot, neu nummeriert, weil 5, 6, 3, 10
# und 8 doppelt wären: außen oben 7 (PDF 5), 4, 9 (PDF 6), Dreierkette unten 11 (PDF 10), 12 (PDF 3), 13 (PDF 8).
# Ein Trainer statt zwei. Nicht gedreht. Die Tafel zeigt den Ablauf unten, oben läuft gleichzeitig dasselbe mit.
# Steigerung eins nach PDF Progression 1 (Ballverlust = sofort den Weg zum Minitor zustellen), Steigerung zwei nach Progression 2
# (ein Springer in der Mittelzone verlagert auf die andere Seite). Im Original werden die Minitore dort entfernt; eine Fassung
# kann Tore nicht ausblenden (leere goals-Liste zeigt die der Grundform), darum bleiben sie stehen und der Text sagt, dass sie nicht zählen.
# Sichtkegel: Text Progression 1 „maintaining defensive awareness“; im Video nicht eingezeichnet, Richtung aus dem Sinn:
# Spieler fünf schaut nach dem Ballverlust zum Minitor, das er zustellen muss. In Steigerung zwei nimmt der Springer in der
# Mittelzone an und dreht auf (Kegel mit von + Drehpfeil).
T = P("T", "c", 8, 50, "T")
ERSATZ = [B("s1", 11.6, 53.5), B("s2", 8, 53.5)]
POS = {"n5": (20, 46), "n2": (80, 46), "n3": (56, 54.5), "r11": (37.5, 39), "r12": (54.5, 38.5), "r13": (71, 39.5),
       "r7": (20, 14), "r4": (80, 14), "r9": (44, 5.5), "n6": (30, 21.5), "n10": (47, 22), "n8": (64, 21.5)}
F1, F2 = (46, 49), (55.5, 12.5)
def sp(f1=F1, f2=F2, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("f1", "t", *f1, "F"), P("f2", "t", *f2, "F"), T]
def b(i, d=POS): return [d[i][0] + 0.6, d[i][1] + 0.6]
LINES = [rect(20, 5, 60, 50), line(20, 26, 80, 26), line(20, 34, 80, 34)]
TORE = [{"x": 31, "y": 34, "side": "top"}, {"x": 69, "y": 34, "side": "top"}, {"x": 31, "y": 26, "side": "bottom"}, {"x": 69, "y": 26, "side": "bottom"}]
CONES = [C(20, 30), C(80, 30)]
DIMS = dims(20, 80, 5, 55, "15 m", "30 m", rx=92)
# Stand nach dem Schieben nach links (Ball bei Spieler fünf)
LINKS = {"r11": (29, 42), "r12": (37.5, 39), "r13": (55, 38.5)}

u = {"title": "Zu dritt den Steilpass zustellen", "code": "UE-307", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "15 x 30 m",
 "description": "Ein Rondo vier gegen drei in zwei Hälften gleichzeitig. Außen lassen drei Spieler mit einem Springer den Ball laufen und suchen den Pass in eins der zwei Minitore hinter der Dreierkette. Die drei in der Mitte bleiben eng zusammen, schieben mit dem Ball und stellen die Passwege zu. Fangen sie den Ball ab, dribbeln sie aus dem Feld, und das gibt einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 15 mal 30 Metern mit einer Mittelzone von fünf Metern. In der Mittelzone stehen vier Minitore, zwei zeigen nach unten und zwei nach oben. Zwei Hütchen markieren die Zone.",
  "Verteilen: Zwei Teams zu sechst und zwei Springer. In jeder Hälfte stehen drei Spieler eines Teams außen, drei vom anderen Team verteidigen innen vor den Minitoren. Je ein Springer hilft den Außenspielern. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Die Außenspieler passen sich mit dem Springer den Ball zu und suchen die Lücke zum Minitor. Die Dreierkette schiebt mit, einer greift an, die anderen sichern. Bei Ballgewinn dribbelt die Kette sofort über eine Außenlinie aus dem Feld. Beide Hälften spielen gleichzeitig.",
  "Wertung und Wechsel: Ein Pass ins Minitor gibt einen Punkt für die Außenspieler. Dribbelt die Dreierkette nach Ballgewinn aus dem Feld, gibt das einen Punkt für ihr Team. Nach jeder Runde werden die Punkte gezählt, dann tauschen innen und außen."],
 "organisation_show": ORG,
 "coaching_points": ["Einer greift an, zwei sichern dahinter", "Eng bleiben und laut reden", "Schlechter erster Kontakt? Sofort drauf!", "Ball gewonnen, dann mit Tempo raus aus dem Feld"],
 "materials": ["4 Minitore", "2 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zu dritt den Steilpass zustellen. Ein Rondo vier gegen drei, in beiden Hälften gleichzeitig. Drei Mittelfeldspieler bleiben eng zusammen und lassen keinen Pass nach vorn durch.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(),
  "balls": [B("b1", *b("n3")), B("b2", *b("r9"))] + ERSATZ,
  "steps": [
   S("Ball nach außen, die Kette schiebt", "Unten spielt Spieler drei nach links zu Spieler fünf. Die drei von Team Rot schieben sofort mit rüber. Oben läuft das Gleiche, dort verteidigt Team Neon.",
     ps("b1", b("n5")), *[mv(i, list(p), delay=0.2) for i, p in LINKS.items()],
     ps("b2", b("r7")), mv("n6", [28.5, 18], delay=0.2), mv("n10", [40, 21], delay=0.2), mv("n8", [55, 21.5], delay=0.2)),
   S("Der Springer kommt entgegen", "Spieler fünf findet außen keinen Weg nach vorn und spielt zum Springer. Spieler zwölf rückt raus auf den Ball. Spieler elf lässt sich fallen und steht jetzt genau vor dem linken Minitor.",
     mv("f1", [41, 47.5]), ps("b1", [41.6, 48.1]), mv("r12", [42, 42], delay=0.2), mv("r11", [34, 39.5], delay=0.2), mv("r13", [53, 40], delay=0.2),
     ps("b2", b("r9"), delay=0.3), mv("n6", [33, 21.5], delay=0.5), mv("n10", [45, 19], delay=0.5), mv("n8", [60, 21.5], delay=0.5)),
   S("Der Weg nach vorn ist zu", "Der Springer versucht es trotzdem flach aufs linke Minitor. Spieler elf steht im Passweg und fängt den Ball ab.",
     ps("b1", [34.6, 40.1]), ps("b2", [F2[0] + 0.6, F2[1] + 0.6], delay=0.2)),
   S("Raus aus dem Feld: Punkt", "Jetzt geht es schnell. Spieler elf dribbelt links über die Außenlinie aus dem Feld, und das gibt einen Punkt für Team Rot. Der Trainer spielt den nächsten Ball zu Spieler drei, und Team Neon greift wieder an.",
     dr("r11", "b1", [15, 39.5]), mv("n5", [22, 42], delay=0.3), mv("f1", [36, 46], delay=0.3),
     ps("b2", b("r4"), delay=0.2), mv("n8", [70, 19], delay=0.4), mv("n10", [57, 21], delay=0.4), mv("n6", [42, 21.5], delay=0.4))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball verliert, setzt sofort nach.", "Nach Ballverlust nachsetzen",
    "Die Dreierkette darf nach dem Ballgewinn jetzt auch in ein Minitor ihrer Hälfte treffen. Die Außenspieler laufen sofort nach innen und stellen den Weg zum Minitor zu. Holen sie den Ball zurück, greifen sie weiter an. Trifft die Kette, gibt das einen Punkt, und innen und außen tauschen.",
    sp(**LINKS), [B("b1", *b("n5")), B("b2", *b("r9"))] + ERSATZ,
    [S("Ball weg, Blick zum Minitor", "Spieler fünf will zum Springer spielen, aber Spieler zwölf geht dazwischen und hat den Ball. Sofort schaut Spieler fünf zum linken Minitor. Dorthin will Spieler zwölf jetzt.",
       mv("r12", [39.5, 44.5]), ps("b1", [40.1, 45.1]), bl("n5", [31, 35], after=True)),
     S("Weg zum Minitor zustellen", "Spieler fünf sprintet nach innen und stellt sich vor das Minitor. Von hinten kommt Spieler drei dazu und nimmt Spieler zwölf den Ball wieder ab. Team Neon bleibt außen und greift weiter an.",
       mv("n5", [26, 40.5]), mv("n5", [33, 38.5], after=True), dr("r12", "b1", [38.5, 42], delay=0.3), mv("n3", [52, 46.5], delay=0.4), mv("n3", [43.5, 43.5], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Die Minitore zählen nicht mehr, dafür wird verlagert.", "Verlagern über die Mitte",
    "Die Minitore zählen nicht mehr, am besten räumt man sie weg. Ein Springer steht jetzt in der Mittelzone. Bekommt er den Ball, dreht er auf und spielt in die andere Hälfte, dort geht es weiter. Die Dreierkette will genau diesen Pass durch die Mitte verhindern.",
    sp(f2=(46, 30), n10=(54.5, 21.5), n6=(37.5, 21), n8=(71.5, 21.5)), [B("b1", *b("n3"))] + ERSATZ,
    [S("Erst nach außen locken", "Team Neon spielt wieder nach links zu Spieler fünf, und die Kette von Team Rot schiebt mit. Der Springer unten bietet sich an und bekommt den Ball.",
       ps("b1", b("n5")), *[mv(i, list(p), delay=0.2) for i, p in LINKS.items()], mv("f1", [43, 46.5], delay=0.6), ps("b1", [43.6, 47.1], after=True)),
     S("Durch die Lücke in die Mitte", "Zwischen Spieler zwölf und Spieler dreizehn ist die Lücke zu groß. Der Springer in der Mittelzone schaut zum Ball, und der Pass kommt flach durch.",
       bl("f2", [43, 46.5]), ps("b1", [46.6, 30.6], after=True)),
     S("Aufdrehen und verlagern", "Der Springer dreht auf und spielt nach oben links zu Spieler sieben. Jetzt läuft das Spiel in der anderen Hälfte, und Team Neon muss dort verschieben.",
       bl("f2", list(POS["r7"]), von=[43, 46.5], dauer=1.3), drehen("f2", list(POS["r7"]), delay=0.4), ps("b1", b("r7"), after=True),
       mv("n6", [29, 18], delay=1.6), mv("n10", [40, 21], delay=1.6), mv("n8", [56, 21.5], delay=1.6))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
