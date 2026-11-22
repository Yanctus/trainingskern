import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 43-P11 (U12-U14, Woche 37 Phase 1): Build from the Back and Penetrate. Halbes Spielfeld nach der PDF-Skizze: Feld x 15-85,
# y 4-57, Jugendtor mit Torwart oben, zwei Minitore unten (Konter). Drei Zonen (gestrichelt): Angriffszone bis y 23 (Strafraum),
# Mittelzone y 23-41, Aufbauzone y 41-57. Ausrichtung wie im PDF (Team Neon spielt nach oben).
# Pink (Ballbesitz: 5, 4, 3, 2, 6, 10, 8, 9) -> Neon, Dunkelblau -> Rot mit Torwart r1. Rot neu nummeriert (doppelte Nummern):
# Blau 9 -> Spieler elf, Blau 8 -> Spieler sieben, Blau 10 -> Spieler siebzehn, Blau 2 -> zwölf, Blau 3 -> dreizehn,
# Blau 4 -> vierzehn, Blau 5 -> fünfzehn. Positionen auf ein Spaltenraster gesetzt (3D-Abstand), Rot 13 und Neon 2 außen
# übereinander. Ein Trainer statt zwei. Grundform nach PDF/Video 0:05-0:31 (2 gegen 1, Innenverteidiger dribbelt in die Mitte,
# Angriff 3 gegen 2); der genaue Abschluss ist vereinfacht (Stürmer schließt ab, Zehner und Achter laufen mit ein).
# Fassungen: "If 10 presses the CB - find the free man using the full back" (Video 0:44-0:58) und Progression 2
# ("Midfielder can press opposite CB", Video 1:46-2:00; im Video drückt Blau 10, hier der zentrale Spieler sieben).
# Progression 1 (Innenverteidiger presst den freien Spieler) und "If 10 presses the 6 / stays in" nur im Text bzw. Bericht.
# Sichtkegel: im Video nicht eingezeichnet (nur Markierungskreise); aus Text/Ton ("find the free player"): im Coaching-Punkt schaut
# Spieler zwei vor der Annahme nach innen zum freien Spieler acht.
T = P("T", "c", 8, 50, "T")
POS = {"r1": (50, 5), "r14": (41, 12), "r15": (59, 12), "n9": (50, 21),
       "n3": (16.5, 30), "r12": (24.9, 26), "n10": (33.2, 31), "n6": (41.6, 38), "r7": (58.3, 30), "r17": (66.6, 28),
       "n8": (75, 30), "r13": (83.4, 24), "n2": (83.4, 40),
       "n5": (33, 53), "r11": (50, 47), "n4": (67, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 9.6, 46.5), B("s2", 6, 46.5)]
LINES = [rect(15, 4, 70, 53), rect(28, 4, 44, 19), rect(40, 4, 20, 6), line(15, 23, 85, 23), line(15, 41, 85, 41)]
CONES = [C(15, 23), C(85, 23), C(15, 41), C(85, 41)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "jugend"}, {"x": 33, "y": 57, "side": "bottom"}, {"x": 67, "y": 57, "side": "bottom"}]

u = {"title": "Aufbauen, durchbrechen, treffen", "code": "UE-234", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 16, "players_max": 16, "field_size": "Halbes Spielfeld",
 "description": "Ein Spiel auf dem halben Feld in drei Zonen. Team Neon baut hinten mit zwei Innenverteidigern gegen einen Stürmer auf, spielt in der Mitte mit Überzahl und greift vorn drei gegen zwei auf das große Tor an. Erobert Team Rot den Ball, kontert es auf zwei Minitore. Jeder Angriff beginnt wieder bei den zwei Innenverteidigern.",
 "organisation": ["Aufbauen: Ein halbes Spielfeld mit Jugendtor oben und zwei Minitoren unten, in drei Zonen geteilt: Aufbauzone, Mittelzone und Angriffszone bis zum Strafraum.",
  "Verteilen: Team Neon mit zwei Innenverteidigern hinten, zwei Außenverteidigern und drei Mittelfeldspielern in der Mitte und einem Stürmer vorn. Team Rot mit Torwart, zwei Verteidigern vorn, vier Spielern in der Mitte und einem Stürmer hinten. Der Trainer steht unten an der Seite mit Bällen.",
  "Ablauf: Die Innenverteidiger spielen sich zwei gegen eins am Stürmer vorbei. Dribbelt einer in die Mittelzone, ist das Spiel offen. Team Neon spielt nach vorn und greift drei gegen zwei an.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und trifft in ein Minitor, gibt das einen Punkt für Team Rot. Danach beginnen wieder die zwei Innenverteidiger."],
 "organisation_show": ORG,
 "coaching_points": ["Den Stürmer auf eine Seite locken und quer zum freien Innenverteidiger spielen", "Presst ein Gegner den Innenverteidiger, den freien Mann über den Außenverteidiger finden", "Bleibt der Gegner innen, den Sechser anspielen und in der Mitte Überzahl schaffen", "Vorn schnell kombinieren und die Überzahl ausspielen"],
 "materials": ["1 Jugendtor", "2 Minitore", "4 Hütchen für die Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Aufbauen, durchbrechen, treffen. Team Neon spielt sich von hinten durch drei Zonen bis vor das große Tor und schließt dort ab.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": [B("b1", 33.6, 53.6)] + ERSATZ,
  "steps": [
   S("Zwei gegen eins", "Spieler fünf hat den Ball, und Spieler elf läuft ihn an. Spieler fünf spielt quer zu Spieler vier, der jetzt frei ist.",
     mv("r11", [41, 48]), ps("b1", [67.6, 53.6], delay=0.4)),
   S("In die Mitte", "Spieler vier dribbelt in die Mittelzone. Jetzt ist das Spiel offen, und alle dürfen mitspielen. Spieler vier spielt zu Spieler zehn.",
     dr("n4", "b1", [67, 40]), ps("b1", [33.8, 31.6], after=True)),
   S("Drei gegen zwei", "Spieler zehn spielt nach vorn zum Stürmer. Gleichzeitig laufen Spieler zehn und Spieler acht mit in die Angriffszone. Jetzt sind es drei gegen zwei.",
     ps("b1", [50.6, 21.6]), mv("n10", [32, 18], after=True), mv("n8", [68, 17], after=True)),
   S("Abschluss: Punkt", "Spieler neun dreht auf und schießt zwischen den zwei Verteidigern aufs Tor, und das gibt einen Punkt für Team Neon. Dann beginnen wieder die zwei Innenverteidiger mit einem neuen Ball vom Trainer.",
     ps("b1", [46.5, 4.6]))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Presst ein Gegner den Innenverteidiger, den freien Mann über den Außenverteidiger finden.", "Freier Mann über außen",
    "Kommt ein Mittelfeldspieler von Team Rot heraus und presst den Innenverteidiger, ist hinter ihm ein Spieler frei. Der Innenverteidiger spielt zum Außenverteidiger. Der schaut schon vor dem Pass nach innen und spielt sofort zum freien Mann.",
    sp(n4=(66.6, 45)), [B("b1", 67.2, 45.6)] + ERSATZ,
    [S("Gegner presst", "Spieler vier dribbelt in die Mittelzone. Spieler siebzehn kommt heraus und presst ihn. Damit ist Spieler acht hinter ihm frei.",
       dr("n4", "b1", [66.6, 39]), mv("r17", [66.6, 33], delay=0.3)),
     S("Über außen", "Spieler zwei schaut schon vor dem Pass nach innen und sieht Spieler acht. Spieler vier spielt zu Spieler zwei.",
       bl("n2", [73, 28]), ps("b1", [84, 40.6], after=True)),
     S("Der freie Mann", "Spieler zwei spielt sofort nach innen zu Spieler acht. Der dreht auf und spielt nach vorn zum Stürmer.",
       ps("b1", [75.6, 30.6]), ps("b1", [50.6, 21.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Mittelfeldspieler darf in der Aufbauzone mitpressen.", "Zwei gegen zwei hinten",
    "Jetzt darf ein Mittelfeldspieler von Team Rot in die Aufbauzone kommen und den zweiten Innenverteidiger pressen. Hinten ist es dann zwei gegen zwei, und der Querpass ist zu. Dafür fehlt Team Rot in der Mitte ein Spieler. Team Neon muss schneller entscheiden und sofort nach vorn spielen.",
    sp(), [B("b1", 67.6, 53.6)] + ERSATZ,
    [S("Zwei gegen zwei", "Spieler vier hat den Ball. Gleichzeitig läuft Spieler elf ihn an, und Spieler sieben kommt zurück und stellt sich vor Spieler fünf. Der Querpass ist zu.",
       mv("r11", [59, 50]), mv("r7", [42, 48])),
     S("Schnell nach vorn", "Spieler acht kommt dem Ball entgegen, und Spieler vier spielt sofort zu ihm.",
       mv("n8", [75, 36]), ps("b1", [75.6, 36.6], delay=0.3)),
     S("Überzahl in der Mitte", "In der Mitte fehlt jetzt ein Gegner. Spieler acht spielt zu Spieler sechs, und der spielt weiter nach vorn zum Stürmer.",
       ps("b1", [42.2, 38.6]), ps("b1", [50.6, 21.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
