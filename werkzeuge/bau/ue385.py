import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-80 (U15-U17, Woche 32 Phase 4, Pre-Season): Rewarding the High Press. 20 x 25 Yards = 18 x 23 m, Feld x 30-70, y 5-55,
# Mittellinie gestrichelt, oben und unten ein Großfeldtor (C- und B-Jugend) mit Torwart. Halbes Feld und kleiner, kein Großfeld quer;
# Verhältnis 1,25, also hochkant wie im PDF.
# Oben/unten gespiegelt: Im PDF baut Pink unten vom Torwart auf und Blau presst nach unten. Hier presst Team Neon (Blau, Nummern
# 4, 6, 8, 9, 10 wie im PDF, Torwart Grün 13 -> n1) nach oben in der Hälfte von Team Rot und greift das obere Tor an.
# Team Rot (Pink, Torwart Grün 1 -> r1) neu nummeriert (4, 6, 9, 10 doppelt): Pink 4 -> 2, 5 -> 3, 6 -> 5, 9 -> 7, 10 -> 11.
# Positionen auf einem Raster aus fünf Spalten (3D-Abstand), grob wie im PDF; Spieler sieben von Team Rot steht etwas tiefer.
# Ein Trainer statt zwei (links an der Mittellinie mit Bällen).
# Wertung wie im Original: Ballgewinn in der Hälfte des Gegners und Treffer = zwei Punkte ("two goals"), Treffer nach normalem
# Aufbau = ein Punkt; wer zuerst fünf Punkte hat, gewinnt, das Verliererteam sprintet eine Runde ums Feld. Rollenwechsel nach
# jedem Angriff wie im Ton ("If the defending team is unable to win possession, or the attackers score, the roles switch").
# Fassungen = Key Coaching Point 1 (schlechtes Pressing, ein Pass durch die Lücke, Team Rot trifft nach normalem Aufbau: ein Punkt)
# und Key Coaching Point 2 (Spielstand, Verlierer sprinten eine Runde).
# Sichtkegel aus Text ("Recognise pressing triggers to press high") und Ton ("works together to press"): Spieler zehn beobachtet den
# Abstoß des Torwarts zu Spieler zwei, das ist das Signal zum Anlaufen. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Keine Dublette (UE-174 Gegenpressing in sechs Sekunden, UE-204 Kette erobert, UE-236 Wellenspiel, UE-340 Endzone/Minitore).
T = P("T", "c", 20, 30, "T")
ERSATZ = [B("s1", 20.6, 34.5), B("s2", 18, 34.5)]
NEON = {"n10": (33.6, 26), "n9": (41.8, 18), "n6": (41.8, 37), "n8": (58.2, 20), "n4": (58.2, 39), "n1": (50, 52.5)}
ROT = {"r1": (50, 7), "r2": (33.6, 10), "r7": (33.6, 42), "r5": (50, 25), "r3": (66.4, 10), "r11": (66.4, 30)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i[1:] == "1" else i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(30, 5, 40, 50), line(30, 30, 70, 30)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 55, "side": "bottom", "size": "gross"}]
CONES = ecken(30, 5, 40, 50)
DIMS = dims(30, 70, 5, 55, "18 m", "23 m", rx=78)
# Runde ums Feld (gegen den Uhrzeigersinn auf der Tafel), außen herum, vom Platz des Spielers aus
RUNDE = [[73, 2.5], [27, 2.5], [27, 57.5], [73, 57.5], [73, 2.5]]
def runde(who, start, delay):
    erster = 0 if start[0] > 50 else 1
    pkt = RUNDE[erster:] + RUNDE[1:erster + 1] if erster else RUNDE
    return [mv(who, pkt[0], delay=delay)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Hohes Pressing zählt doppelt", "code": "UE-385", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "18 x 23 m",
 "description": "Fünf gegen fünf mit Torwart auf zwei Tore, das Feld ist in zwei Hälften geteilt. Das Team ohne Ball presst sofort hoch in der Hälfte des Gegners. Wer den Ball dort erobert und trifft, bekommt zwei Punkte, ein Treffer nach normalem Aufbau gibt einen Punkt. Wer zuerst fünf Punkte hat, gewinnt, und die Verlierer sprinten eine Runde ums Feld.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern mit Mittellinie. Oben und unten ein Tor mit Torwart.",
  "Verteilen: Zwei Teams mit je fünf Feldspielern und einem Torwart. Der Trainer steht an der Mittellinie mit vielen Bällen.",
  "Ablauf: Ein Torwart spielt den Ball zu seinem Team. Das andere Team läuft sofort gemeinsam an und presst in der Hälfte des Gegners. Erobert es den Ball, schließt es schnell ab. Kommt der Gegner durch, spielt er normal auf das andere Tor.",
  "Wertung und Wechsel: Ballgewinn in der Hälfte des Gegners und Treffer gibt zwei Punkte, ein Treffer nach normalem Aufbau gibt einen Punkt. Nach jedem Angriff wechseln die Rollen. Wer zuerst fünf Punkte hat, gewinnt, und die Verlierer sprinten eine Runde ums Feld."],
 "organisation_show": ORG,
 "coaching_points": ["Auf das Signal achten und dann zusammen los", "Als Einheit pressen, keine Lücke lassen", "Ohne Ball freilaufen, damit der Pass durchgeht", "Nach dem Ballgewinn schnell und sauber abschließen"],
 "materials": ["2 Großfeldtore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Hohes Pressing zählt doppelt. Fünf gegen fünf mit Torwart. Wer den Ball vorn in der Hälfte des Gegners erobert und trifft, bekommt zwei Punkte.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *f(ROT["r1"]))] + ERSATZ,
  "steps": [
   S("Abstoß ist das Signal", "Der Torwart von Team Rot spielt kurz raus zu Spieler zwei. Spieler zehn sieht den Pass kommen. Das ist das Signal.",
     bl("n10", [34, 12]), ps("b1", f(ROT["r2"]), delay=0.3)),
   S("Alle laufen zusammen an", "Jetzt läuft Spieler zehn Spieler zwei an. Spieler neun macht den Weg zurück zum Torwart zu, Spieler acht rückt zu Spieler fünf. Von hinten schieben Spieler sechs und Spieler vier bis an die Mittellinie.",
     mv("n10", [35, 16]), mv("n9", [42, 11], delay=0.1), mv("n8", [55, 23], delay=0.2),
     mv("n6", [43, 31], delay=0.3), mv("n4", [57, 32], delay=0.3), mv("r11", [64, 37], delay=0.3)),
   S("In der Hälfte von Rot erobert", "Spieler zwei steht unter Druck und will in die Mitte zu Spieler fünf spielen. Spieler acht ist schon da und fängt den Ball ab.",
     ps("b1", [47.6, 21.6]), mv("n8", [47, 21], delay=0.2)),
   S("Schnell abschließen: zwei Punkte", "Spieler acht spielt sofort zu Spieler neun, und der schießt flach ins Eck. Der Ball wurde in der Hälfte von Team Rot erobert, also gibt das zwei Punkte für Team Neon. Jetzt wechseln die Rollen. Der Torwart von Team Neon spielt den nächsten Ball raus, und Team Rot presst.",
     mv("n9", [43, 14]), ps("b1", f([43, 14]), delay=0.2), ps("b1", [45, 5.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Keine Lücke beim Pressing.", "Keine Lücke beim Pressing",
    "Läuft jeder für sich an, entsteht in der Mitte eine Lücke. Ein einziger Pass hebelt dann drei Spieler aus. Darum laufen alle zusammen an und bleiben eng beieinander.",
    sp(), [B("b1", *f(ROT["r1"]))] + ERSATZ,
    [S("Jeder läuft für sich", "Team Neon presst, aber jeder läuft zu seinem eigenen Gegner. Spieler zehn geht nach außen zu Spieler zwei, Spieler acht zu Spieler drei. In der Mitte ist plötzlich viel Platz.",
       mv("n10", [34, 15]), mv("n8", [64, 16], delay=0.1), mv("n9", [38, 12], delay=0.2)),
     S("Ein Pass durch die Lücke", "Der Torwart sieht die Lücke und spielt flach durch die Mitte zu Spieler fünf. Drei Spieler von Team Neon sind mit einem Pass aus dem Spiel.",
       bl("r5", [50, 9]), ps("b1", f(ROT["r5"]), after=True)),
     S("Aufdrehen, ein Punkt für Rot", "Spieler fünf dreht auf und spielt zu Spieler elf. Der zieht aufs Tor und trifft. Das war ein normaler Aufbau, und das gibt einen Punkt für Team Rot.",
       bl("r5", [62, 37], von=[50, 9], dauer=1.3), drehen("r5", [62, 37], delay=0.4), ps("b1", f([66.4, 30]), after=True),
       dr("r11", "b1", [63, 41], after=True), ps("b1", [56, 54.7], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Wer verliert, sprintet.", "Wer verliert, sprintet",
    "Nach einer festen Zeit schaut der Trainer auf den Spielstand, oder ein Team hat fünf Punkte. Das Verliererteam sprintet eine Runde ums Feld, danach geht es sofort weiter. So bleibt das Tempo hoch, und jeder Zweikampf zählt.",
    sp(), [B("b1", *f(NEON["n8"]))] + ERSATZ,
    [S("Der fünfte Punkt", "Team Neon führt vier zu drei. Spieler acht hat den Ball in der Hälfte von Team Rot erobert und spielt zu Spieler zehn. Der trifft, und das gibt einen Punkt für Team Neon. Fünf Punkte, Team Neon gewinnt.",
       ps("b1", f(NEON["n10"])), mv("n10", [36, 18], delay=0.2), ps("b1", f([36, 18]), delay=0.3), ps("b1", [44, 5.3], after=True)),
     S("Team Rot sprintet eine Runde", "Alle Feldspieler von Team Rot sprinten jetzt gemeinsam eine Runde außen ums Feld. Team Neon holt sich kurz Luft. Danach bringt der Trainer den nächsten Ball, und das neue Spiel startet.",
       *runde("r2", ROT["r2"], None), *runde("r7", ROT["r7"], 0.2), *runde("r5", ROT["r5"], 0.4), *runde("r3", ROT["r3"], 0.1), *runde("r11", ROT["r11"], 0.3))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
