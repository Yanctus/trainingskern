import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 45-P5 (U15-U17, Woche 39 Phase 2): Short Combination Play (Opposed Possession, 4 Goal Possession). 25 x 25 Yards = 23 x 23 m
# (gerundet 25 x 25 m), Feld x 28-72, y 6-50, in vier Viertel geteilt (gestrichelt). Ausrichtung wie im PDF (nicht gedreht).
# An jeder Seite ein Minitor wie im PDF: oben in der linken Hälfte, rechts in der oberen, links in der unteren, unten in der rechten.
# PDF pink (Raute, 4-4-2 mit Raute) -> Team Neon mit den Nummern aus dem Video: 10 oben, 8 links, 6 rechts, 4 unten.
# PDF gold (vier Verteidiger, je einer pro Viertel) -> Team Rot, neu nummeriert wegen doppelter Nummern (gold 8, 4, 9, 10 ->
# 2 oben links, 3 oben rechts, 5 unten links, 7 unten rechts). PDF blau (vier außen) -> Springer F (f1 oben, f2 links, f3 rechts,
# f4 unten). Alle Figuren auf einem Spaltenraster (3D-Abstand), die Springer oben und unten etwas aus der Mitte gerückt, damit sie
# nicht hinter Spieler zehn bzw. Spieler vier stehen. Ein Trainer statt einem, rechts unten neben dem Feld.
# Grundform nach PDF-Skizze und Ton: Springer unten spielt rein auf Spieler vier, über Spieler sechs zu Spieler zehn, der zum
# Springer links spielt; der legt ab, und Spieler acht schließt mit dem ersten Kontakt ins Minitor links ab.
# Ergänzt: Nach ein paar Minuten tauschen die Teams die Rollen (im Original nicht genannt).
# Fassungen: PDF Key Coaching Point 1 (ohne Ball weglaufen und den Verteidiger mitziehen) und 2 (ständig Winkel schaffen,
# Anspielstationen als dünne Pfeile).
# Sichtkegel aus Text („Awareness of floaters positioning“): Spieler zehn schaut zum Ball und schwenkt nach der Annahme zum
# Springer links (bl mit von). Im Video kein Kegel eingezeichnet. Kein Aufdrehen auf der Stelle, darum kein Drehpfeil.
# Keine Dublette: UE-151 (32-P6, fünf in einer inneren Zone, Verteidiger aus den Ecken), UE-395 (17-P1, Rondo in vier Vierteln
# auf ein Minitor), UE-224 (59-P5, 5 gegen 2) und UE-240 (87-P8, vier Dreiecke) haben andere Organisation und Abläufe.
T = P("T", "c", 79, 50, "T")
ERSATZ = [B("s1", 82.5, 52.5), B("s2", 82.5, 47)]
NEON = {"n10": (52.5, 12), "n8": (31, 26), "n6": (69.5, 31), "n4": (50, 44)}
ROT = {"r2": (40, 21), "r3": (61, 19), "r5": (39.5, 37.5), "r7": (58.5, 37)}
SPR = {"f1": (44, 2.5), "f2": (22.5, 26), "f3": (78, 31), "f4": (41, 53.5)}
def sp(**k):
    d = dict(NEON); d.update(ROT); d.update(SPR); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(28, 6, 44, 44), line(50, 6, 50, 50), line(28, 28, 72, 28)]
TORE = [{"x": 36, "y": 6, "side": "top"}, {"x": 72, "y": 17, "side": "right"}, {"x": 28, "y": 39, "side": "left"},
        {"x": 61, "y": 50, "side": "bottom"}]
CONES = ecken(28, 6, 44, 44)
DIMS = dims(28, 72, 6, 50, "25 m", "25 m", rx=89)
N = lambda i: NEON[i]

u = {"title": "Raute kombiniert mit Springern", "code": "UE-410", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 12,
 "field_size": "25 x 25 m",
 "description": "Vier Mittelfeldspieler stehen als Raute im Feld, vier Verteidiger von Team Rot stehen dazwischen, und außen warten vier Springer. An jeder Seite steht ein Minitor. Team Neon kombiniert kurz mit einem Springer und schließt mit dem ersten Kontakt ab. Erobert Team Rot den Ball, darf es nach fünf Pässen am Stück auf jedes Minitor schießen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern, in vier Viertel geteilt. An jeder Seite steht ein Minitor, jedes in einer anderen Hälfte.",
  "Verteilen: Team Neon steht mit vier Spielern als Raute im Feld, Team Rot mit vier Verteidigern, einer in jedem Viertel. Vier Springer stehen außen, einer an jeder Seite. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Ein Springer spielt den Ball rein. Team Neon kombiniert kurz, spielt einen Springer an und schließt nach seiner Ablage mit dem ersten Kontakt auf ein Minitor ab. Team Rot verteidigt gemeinsam und schützt die Tore.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon. Erobert Team Rot den Ball, braucht es fünf Pässe am Stück, dann darf es auf jedes Minitor schießen, und das gibt einen Punkt für Team Rot. Nach ein paar Minuten tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Kopf hoch, wo stehen die Springer?", "Kurz kombinieren und direkt abschließen", "In der Raute die Plätze tauschen", "Ohne Ball weglaufen und Platz schaffen"],
 "materials": ["4 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Raute kombiniert mit Springern. Team Neon spielt als Raute gegen vier Verteidiger, außen helfen vier Springer. Nach der Ablage vom Springer geht der Ball direkt ins Minitor, und das gibt einen Punkt für Team Neon.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *f(SPR["f4"]))] + ERSATZ,
  "steps": [
   S("Der Springer spielt rein", "Der Springer unten hat den Ball. Spieler vier zeigt sich einen Schritt zur Seite und bekommt den Pass.",
     mv("n4", [54, 45]), ps("b1", f([54, 45]), delay=0.4)),
   S("Kurz über rechts nach oben", "Sofort weiter nach rechts zu Spieler sechs. Oben löst sich Spieler zehn von Spieler drei, und Spieler sechs spielt ihn an. Der schaut dabei schon zum Ball.",
     ps("b1", f(N("n6"))), mv("n10", [47, 13], delay=0.3), bl("n10", list(N("n6")), after=True), ps("b1", [47.6, 13.6], after=True)),
   S("Raus zum Springer", "Spieler zehn schaut nach links, wo der Springer steht, und spielt ihn an. Gleichzeitig startet Spieler acht Richtung Minitor unten links.",
     mv("n8", [34, 40]), bl("n10", list(SPR["f2"]), von=list(N("n6")), dauer=1.3), ps("b1", f(SPR["f2"]), after=True)),
   S("Ablage, direkt: Punkt", "Der Springer legt direkt ab, und Spieler acht schießt mit dem ersten Kontakt ins Minitor. Das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu einem Springer, und es geht sofort weiter.",
     ps("b1", f([34, 40])), ps("b1", [28.4, 39], after=True), mv("r5", [37, 40], delay=0.3))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ohne Ball weglaufen und Platz schaffen.", "Weglaufen, Platz schaffen",
    "Ein Lauf ohne Ball zieht einen Verteidiger mit. Dort, wo er vorher stand, ist jetzt Platz. Genau in diesen Raum startet ein Mitspieler.",
    sp(), [B("b1", *f(N("n4")))] + ERSATZ,
    [S("Weglaufen, Gegner zieht mit", "Spieler vier hat den Ball. Spieler sechs sprintet nach oben weg, und Spieler sieben läuft mit. Rechts unten ist plötzlich Platz.",
       mv("n6", [68, 20]), mv("r7", [63, 27], delay=0.3)),
     S("Zum Springer, rein in die Lücke", "Spieler vier spielt zum Springer rechts und startet sofort in den freien Raum.",
       ps("b1", f(SPR["f3"])), mv("n4", [64, 41], delay=0.3)),
     S("Ablage, direkt: Punkt", "Der Springer legt in den Lauf, und Spieler vier schießt direkt ins Minitor unten. Das gibt einen Punkt für Team Neon.",
       ps("b1", f([64, 41])), ps("b1", [61, 49.7], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ständig neue Winkel schaffen.", "Ständig neue Winkel schaffen",
    "Wer ohne Ball stehen bleibt, steht bald im Deckungsschatten. Darum bewegen sich alle ständig mit dem Ball mit. Dann hat der Ballführer immer eine Anspielstation nach vorn oder zur Seite.",
    sp(), [B("b1", *f(N("n4")))] + ERSATZ,
    [S("Die Wege nach vorn sind zu", "Spieler vier hat den Ball. Spieler fünf und Spieler sieben rücken zusammen und machen die Wege nach vorn zu.",
       mv("r5", [43, 38]), mv("r7", [57, 38], delay=0.1)),
     S("Neue Winkel, drei Stationen", "Jetzt bewegen sich die anderen. Spieler zehn kommt in die Lücke zwischen beide, Spieler sechs lässt sich fallen, der Springer unten geht mit. Spieler vier hat auf einmal drei Anspielstationen.",
       mv("n10", [50, 23]), mv("n6", [68, 41], delay=0.1), mv("f4", [55, 53.5], delay=0.2),
       opt("n4", [50.6, 23.6], after=True), opt("n4", [68.6, 41.6], after=True), opt("n4", [55.6, 54.1], after=True)),
     S("Steil in die Lücke", "Spieler vier spielt durch die Lücke auf Spieler zehn. Zwei Verteidiger sind mit einem Pass raus, und Team Neon greift oben an.",
       ps("b1", [50.6, 23.6]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
