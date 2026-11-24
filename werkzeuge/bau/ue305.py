import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P9 (U15-U17, Woche 11): Possession to Finish Rondo. 20 x 20 Yards = 18 x 18 m, Feld x 22-78, y 8-52 (in der Breite
# gestreckt, damit 13 Figuren den 3D-Abstand halten). Ausrichtung wie im PDF: Tore links und rechts, darum wird quer gespielt.
# Mittelzone 5 x 5 Yards (4,5 m) als farbige Zone. PDF blau (sieben Spieler in Ballbesitz) -> Team Neon mit den Nummern aus dem
# PDF (2, 4, 5, 6, 8, 9, 10), pink (vier Verteidiger) -> Team Rot, neu nummeriert, weil 4, 5, 6 und 8 doppelt sind
# (6 -> 3, 4 -> 7, 5 -> 11, 8 -> 13). Beide Torhüter neutral (das Ballbesitzteam darf auf beide Tore abschließen).
# Positionen für den 3D-Abstand in Spalten gerückt, Trainer links oben statt oben in der Mitte.
# Sichtkegel: Text "Head up to spot gaps to find central player", Ton "constantly scan the area"; im Video nicht
# eingezeichnet, Richtung aus dem Sinn: Spieler acht schaut erst zum Passgeber, nach der Annahme in die Mittelzone.
# Aufdrehen nach ZUSATZ_U15 (Vorbild ue300): Kegel zum Passgeber, Annahme, dann Kegel mit von schwenken plus drehen().
T = P("T", "c", 10, 12, "T")
ERSATZ = [B("s1", 13.6, 15.5), B("s2", 10, 15.5)]
K = [P("k", "t", 24.5, 30, "TW"), P("k2", "t", 75.5, 30, "TW")]
POS = {"n6": (33, 31), "n5": (33, 47), "n2": (50, 13.5), "n10": (50, 30), "n8": (67, 24), "n9": (67, 40), "n4": (58.5, 48),
       "r3": (41.5, 27), "r13": (41.5, 43), "r7": (58.5, 31.5), "r11": (50, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + K + [T]
LINES = [rect(22, 8, 56, 44), {"type": "zone", "x": 44, "y": 24.5, "w": 12, "h": 11}]
TORE = [{"x": 22, "y": 30, "side": "left", "size": "gross"}, {"x": 78, "y": 30, "side": "right", "size": "gross"}]
DIMS = dims(22, 78, 8, 52, "18 m", "18 m", rx=91)

u = {"title": "Rondo 7 gegen 4 zum Abschluss", "code": "UE-305", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "18 x 18 m",
 "description": "Sieben Spieler halten den Ball gegen vier Verteidiger. Einer der sieben steht in einer kleinen Zone in der Mitte. Erst wenn er angespielt wurde, darf das Team auf eines der beiden Tore abschließen. Erobern die Verteidiger den Ball, bekommen sie sofort einen Punkt und dürfen selbst aufs Tor gehen.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Links und rechts steht je ein großes Tor mit Torwart. In der Mitte ist eine Zone von etwa viereinhalb mal viereinhalb Metern markiert.",
  "Verteilen: Team Neon spielt mit sieben Spielern, sechs außen herum und einer in der Mittelzone. Team Rot verteidigt mit vier Spielern. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Team Neon lässt den Ball laufen und sucht den Pass in die Mittelzone. Kommt der Ball von dort wieder heraus, darf Team Neon auf eines der beiden Tore schießen. Ist der Weg in die Mitte zu, läuft der Ball weiter außen herum.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Erobert Team Rot den Ball, gibt das sofort einen Punkt, und Team Rot darf zusätzlich auf eines der Tore abschließen. Mittelspieler, Angreifer und Verteidiger regelmäßig tauschen."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo ist die Lücke in die Mitte", "Ohne Ball bewegen und anspielbar sein", "Ist die Mitte zu, ruhig bleiben und verlagern", "Kommt der Ball aus der Mitte, sofort aufs Tor"],
 "materials": ["2 große Tore", "4 Hütchen für die Mittelzone", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rondo sieben gegen vier zum Abschluss. Team Neon hält den Ball und sucht den Mann in der Mitte. Erst nach dem Pass in die Mittelzone darf das Team abschließen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 59.1, 48.6)] + ERSATZ,
  "steps": [
   S("Der Ball läuft außen entlang", "Team Neon ist zu siebt, Team Rot verteidigt zu viert. Spieler vier beginnt unten und spielt nach rechts zu Spieler neun. Team Rot schiebt zum Ball.",
     ps("b1", [67.6, 40.6]), mv("r7", [61.5, 36], delay=0.2), mv("r11", [53, 44], delay=0.2)),
   S("Weiter zu Spieler acht", "Der Ball geht weiter nach oben. Spieler acht schaut zum Ball, bis er ihn hat.",
     bl("n8", [67, 40]), ps("b1", [67.6, 24.6], after=True), mv("r7", [61.5, 33], delay=0.5)),
   S("Kopf hoch, Pass in die Mitte", "Jetzt hebt Spieler acht den Kopf. Die Lücke ist offen. Er dreht auf und spielt flach in die Mittelzone zu Spieler zehn.",
     bl("n8", [50, 30], von=[67, 40], dauer=1.3), drehen("n8", [50, 30], delay=0.4), ps("b1", [50.6, 30.6], after=True)),
   S("Raus aus der Zone: Punkt", "Der Ball war in der Mitte, jetzt darf Team Neon abschließen. Spieler zehn legt nach oben ab, Spieler zwei schießt direkt aufs linke Tor und trifft, und das gibt einen Punkt für Team Neon. Der Trainer spielt sofort den nächsten Ball zu Spieler fünf.",
     ps("b1", [50.6, 14.1]), ps("b1", [22.3, 26], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ist die Mitte zu, Geduld haben.", "Mitte zu? Geduld",
    "Steht ein Verteidiger im Passweg, wird der Ball nicht in die Mitte gezwungen. Dann läuft er außen weiter, bis sich von einer anderen Seite eine Lücke auftut. Der Mittelspieler bewegt sich in seiner Zone mit und zeigt sich neu.",
    sp(r7=(58.5, 28)), [B("b1", 67.6, 24.6)] + ERSATZ,
    [S("Die Mitte ist zu", "Spieler acht schaut in die Mitte. Spieler sieben steht genau im Passweg. Also kein Risiko, der Ball geht zurück zu Spieler neun.",
       bl("n8", [50, 30]), ps("b1", [67.6, 40.6], after=True), mv("n10", [51.5, 32.5], delay=0.8)),
     S("Neuer Winkel, Lücke auf: Punkt", "Von hier ist der Weg frei. Spieler neun spielt in die Mittelzone und läuft ein paar Schritte nach. Spieler zehn lässt prallen, Spieler neun schießt aufs rechte Tor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [52.1, 33.1]), mv("n9", [69, 36], delay=0.2), ps("b1", [69.6, 36.6], after=True), ps("b1", [77.7, 36.5], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Erst zehn Pässe, dann der Abschluss.", "Erst zehn Pässe",
    "Team Neon muss zehn Pässe spielen, bevor es abschließen darf. Der Pass in die Mittelzone bleibt trotzdem Pflicht. Alle zählen laut mit und wissen, wann der Moment für den Pass in die Mitte da ist.",
    sp(), [B("b1", 59.1, 48.6)] + ERSATZ,
    [S("Laut mitzählen", "Der Ball läuft über rechts nach oben, und alle zählen laut mit. Acht, neun, zehn. Team Rot läuft hinterher.",
       ps("b1", [67.6, 40.6]), ps("b1", [67.6, 24.6], after=True), ps("b1", [50.6, 14.1], after=True),
       mv("r7", [61.5, 31], delay=0.4), mv("r3", [44, 20], delay=0.8)),
     S("Zehn voll, Ball in die Mitte", "Zehn Pässe sind voll. Spieler zwei spielt in die Mittelzone. Spieler zehn schaut zum Ball, bis er ihn hat.",
       bl("n10", [50, 13.5]), ps("b1", [50.6, 30.6], after=True)),
     S("Aufdrehen, Abschluss: Punkt", "Spieler zehn dreht nach links auf und legt raus zu Spieler sechs. Der schießt direkt aufs linke Tor, und das gibt einen Punkt für Team Neon.",
       bl("n10", [33, 31], von=[50, 13.5], dauer=1.3), drehen("n10", [33, 31], gegen=True, delay=0.4), ps("b1", [33.6, 31.6], after=True), ps("b1", [22.3, 36.5], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
