import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 31-P10 (U15-U17, Woche 13 Phase 1): Beat The Press to Attack (433), Phase of Play. 30 x 25 Yards (27 x 23 m, nach der
# Meter-Regel 25 x 25 m) = Feld x 20-80, y 4.5-55.5. Um 180 Grad gedreht: im PDF steht das große Tor oben und es wird nach
# unten aufgebaut, hier steht es unten und Team Neon spielt nach oben auf die zwei Minitore. Strafraum und Torraum nach der
# PDF-Skizze, Halbkreis weggelassen, Außenbahnen (6 Yards = 5,5 m) gestrichelt. Großfeldtor (nur C- und B-Jugend).
# Navy (Aufbau, 1, 4, 5, 6, 7, 11) -> Team Neon, Nummern wie im PDF, Grün 1 -> Torwart von Team Neon. Gelbe 9 (neutraler
# Stürmer) -> Springer F. Pink (pressen) -> Team Rot 9, 10, 8 wie im PDF, Pink 11 -> Rot 3 und Pink 7 -> Rot 2 (Nummern
# im PDF doppelt). Positionen im Strafraum und im Zentrum auseinandergezogen (3D-Abstand). Ein Trainer statt zwei.
# Grundform = Muster aus PDF-Skizze und Video 0:12-0:28. Coaching-Punkt = Key Coaching Point (Klatschpass über die Sechs),
# Steigerung = Progression (Ballgewinn und Treffer: Rollen tauschen).
# Sichtkegel aus dem Text ("scan and assess passing options before receiving the ball"): Spieler sechs schaut zum Passgeber,
# nimmt an, dann schwenkt der Kegel zum Springer (bl mit von) und er dreht auf (drehen). Im Video kein Kegel eingezeichnet.
T = P("T", "c", 9, 14, "T")
ERSATZ = [B("s1", 12.6, 17.5), B("s2", 9, 17.5)]
POS = {"n4": (67, 46), "n5": (30.5, 46), "n6": (47.5, 34), "n7": (76, 30), "n11": (24, 27),
       "r9": (58.5, 40.5), "r10": (39, 40.5), "r8": (56, 25), "r3": (67, 20.5), "r2": (33, 20.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P("n1", "a", 50, 52, "TW")] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] \
        + [P("f", "t", 50, 8, "F"), T]
LINES = [rect(20, 4.5, 60, 51), rect(32, 41.5, 36, 14), rect(40.3, 50, 19.4, 5.5), line(32, 4.5, 32, 41.5), line(68, 4.5, 68, 41.5)]
TORE = [{"x": 50, "y": 55.5, "side": "bottom", "size": "gross"}, {"x": 32, "y": 4.5, "side": "top"}, {"x": 68, "y": 4.5, "side": "top"}]
START = [B("b1", 50.6, 52.6)] + ERSATZ

u = {"title": "Raus aus dem Pressing", "code": "UE-311", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 14,
 "field_size": "25 x 25 m",
 "description": "Team Neon baut vom eigenen Torwart aus auf, Team Rot presst hoch mit fünf Spielern. Der Ball muss über den Springer ganz vorn laufen, erst dann darf Team Neon aus einer Außenbahn auf eines der zwei Minitore abschließen. Erobert Team Rot den Ball, kontert es sofort auf das große Tor. So lernen die Aufbauspieler, den Druck zu lesen und den freien Mann zu finden.",
 "organisation": ["Aufbauen: Ein Feld von etwa 25 mal 25 Metern. Unten steht ein großes Tor mit Strafraum, oben stehen zwei Minitore. Zwei gestrichelte Linien trennen links und rechts je eine Außenbahn von 5,5 Metern ab.",
  "Verteilen: Team Neon mit Torwart, zwei Innenverteidigern, einem Sechser und zwei Außenspielern. Team Rot presst mit fünf Spielern. Ganz vorn steht ein Springer als Stürmer. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Jeder Angriff beginnt beim Torwart von Team Neon. Der Ball muss einmal zum Springer, der legt nach außen ab. Abgeschlossen wird aus einer der Außenbahnen auf ein Minitor.",
  "Wertung: Ein Treffer in ein Minitor gibt einen Punkt für Team Neon. Gewinnt Team Rot den Ball und trifft ins große Tor, gibt das einen Punkt für Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, bevor der Ball kommt", "Läuft der Stürmer den Torwart an, ist der Innenverteidiger frei", "Passweg zu? Dann über den Sechser klatschen lassen", "Mitte dicht? Dann raus auf den Flügel"],
 "materials": ["1 Tor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Raus aus dem Pressing. Team Neon baut vom Torwart aus auf, Team Rot läuft hoch an. Der Weg nach vorn führt über den Springer.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(20, 4.5, 60, 51), "players": sp(), "balls": START,
  "steps": [
   S("Torwart spielt den Innenverteidiger an", "Der Torwart hat den Ball, und Spieler neun läuft ihn direkt an. Damit ist Spieler vier frei. Der Torwart spielt ihn flach an.",
     mv("r9", [53.5, 46.5]), ps("b1", [67.6, 46.6], delay=0.5)),
   S("Raus auf den Flügel", "Weiter nach außen zu Spieler sieben. Spieler drei schiebt raus und stellt ihn. In der Mitte löst sich Spieler sechs und kommt dem Ball entgegen.",
     ps("b1", [76.6, 30.6]), mv("r3", [72, 24], delay=0.3), mv("n6", [64, 32], delay=0.3), mv("r8", [57, 27], delay=0.6)),
   S("Pass nach innen", "Spieler sechs schaut zum Ball, und Spieler sieben spielt ihn flach an.",
     bl("n6", [76, 30]), ps("b1", [64.6, 32.6], after=True)),
   S("Aufdrehen, steil auf den Springer", "Erst jetzt geht der Blick nach vorn. Spieler sechs dreht auf und spielt steil auf den Springer. Auf der anderen Seite startet Spieler elf die Linie entlang.",
     bl("n6", [50.6, 8.6], von=[76, 30], dauer=1.3), drehen("n6", [50.6, 8.6], gegen=True, delay=0.4), ps("b1", [50.6, 8.6], after=True),
     mv("n11", [27, 14], delay=1.2)),
   S("Ablage nach außen: Punkt", "Der Springer legt nach außen ab, in den Lauf von Spieler elf. Der schiebt aus der Außenbahn ins Minitor, und das gibt einen Punkt für Team Neon. Danach beginnt der Torwart von Team Neon mit dem nächsten Ball.",
     ps("b1", [27.6, 14.6]), ps("b1", [31.5, 5], after=True))],
  "dims": dims(20, 80, 4.5, 55.5, "25 m", "25 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ist der Passweg zu, lassen wir über den Sechser klatschen.", "Über die Sechs klatschen",
    "Läuft der Stürmer von der Seite des Innenverteidigers an, ist der direkte Pass zu. Dann spielt der Torwart den Sechser an. Der lässt mit einem Kontakt auf den Innenverteidiger klatschen. Das zieht die Gegner in die Mitte, und außen wird es frei.",
    sp(), START,
    [S("Der Stürmer stellt den Passweg zu", "Spieler neun läuft diesmal von außen an. Der Pass zu Spieler vier ist damit zu.",
       mv("r9", [61.5, 45]), mv("r9", [56, 49.5], after=True)),
     S("Über den Sechser klatschen lassen", "Der Torwart spielt in die Mitte zu Spieler sechs. Spieler acht kommt von hinten, aber Spieler sechs lässt sofort klatschen auf Spieler vier, der sich nach vorn abgesetzt hat.",
       mv("n4", [69, 37]), ps("b1", [48.1, 34.6]), mv("r8", [52.5, 29], delay=0.3), ps("b1", [69.6, 37.6], after=True)),
     S("Andribbeln, dann nach außen", "Spieler vier hat Platz und dribbelt an. Jetzt muss Spieler drei auf ihn raus, und Spieler sieben ist außen frei.",
       dr("n4", "b1", [68, 28]), mv("r3", [66, 24.5], delay=0.4), mv("n7", [76, 18], delay=0.4), ps("b1", [76.6, 18.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball erobert und trifft, baut danach selbst auf.", "Erobern, treffen, tauschen",
    "Gewinnt Team Rot den Ball und trifft ins große Tor, tauschen die Teams die Rollen. Team Rot baut jetzt vom Torwart aus auf, und Team Neon presst. Das Umschalten geht ohne Pause, jeder muss sofort wissen, wo er hingehört.",
    sp(), START,
    [S("Spieler acht fängt den Pass ab", "Der Torwart will Spieler sechs anspielen. Spieler acht ahnt das, läuft vor ihm in den Pass und hat den Ball.",
       mv("r8", [50, 38.5]), ps("b1", [50.6, 39.1], delay=0.2)),
     S("Sofort abschließen: Punkt", "Kein Zögern, Spieler acht schließt flach ab, und das gibt einen Punkt für Team Rot. Ab jetzt baut Team Rot vom Torwart aus auf, und Team Neon läuft an.",
       ps("b1", [44.5, 55.3]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
