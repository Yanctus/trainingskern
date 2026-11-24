import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 67-P8 (U15-U17, Woche 17 Phase 3): Quick Transitions to Defend and Attack (Wave). 40 x 40 Yards = 37 x 37 m (nach der
# Meter-Regel 35 x 35 m). Ausrichtung wie im PDF: Feld x 25-75, y 5-55. Links die kleine Zone (15 Yards breit, 30 lang) mit
# Großfeldtor oben, darunter die Wartezone (10 Yards); rechts die große Zone mit Großfeldtor unten. Zwei neutrale Torhüter.
# Pink -> Team Neon (Nummern wie im PDF: 9, 11 greifen an, 8, 10 warten; 7 und 6 nur im Text). Navy -> Team Rot, neu
# nummeriert (Nummern doppelt): Verteidiger 5 bleibt 5, die Angreifer der zweiten Welle 9 -> 2 und 7 -> 3; die Wartenden
# (11, 10, 6, 8) nur im Text. Ein Trainer statt zwei: Er steht oben an der Grundlinie zwischen den Zonen und spielt beide
# Bälle ein (im PDF kommt der erste Ball von einem zweiten Trainer an der linken Seitenlinie).
# Ablauf nach Video 0:13-0:37: Trainer auf Spieler neun, Querpass auf Spieler elf, Abschluss; sofort neuer Ball rechts auf
# Spieler zwei, Spieler drei kommt außen, Spieler fünf schließt sich an, Spieler neun und elf sprinten zurück; Pass nach außen,
# Hereingabe, Abschluss von Spieler fünf.
# Fassungen: PDF Key Coaching Point 1 (Verteidiger erobert und löst das drei gegen zwei sofort aus) und 2 (zu zweit verzögern,
# nach außen lenken, abfangen).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 49, 2.5, "T")
ERSATZ = [B("s1", 52.5, 2.2), B("s2", 45.8, 2.2)]
TW = [P("k1", "t", 35.3, 6.5, "TW"), P("k2", "t", 60.5, 52.5, "TW")]
POS = {"n9": (29, 38.5), "n11": (41.5, 38.5), "n8": (30, 54), "n10": (41, 54),
       "r5": (35, 22.5), "r2": (59, 7), "r3": (72.5, 7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + TW + [T]
LINES = [rect(25, 5, 50, 50), line(43.8, 5, 43.8, 55), line(25, 42.5, 75, 42.5), line(25, 17.5, 43.8, 17.5)]
TORE = [{"x": 35.3, "y": 5, "side": "top", "size": "gross"}, {"x": 60.5, "y": 55, "side": "bottom", "size": "gross"}]
DIMS = dims(25, 75, 5, 55, "35 m", "35 m")
B1 = B("b1", 49.6, 3.1)

u = {"title": "Zwei gegen eins, dann zurück", "code": "UE-347", "kind": "Spielform",
 "focuses": ["Umschalten", "Verteidigen", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 16,
 "field_size": "35 x 35 m",
 "description": "Eine Welle mit zwei Phasen. In der kleinen Zone greifen zwei Spieler von Team Neon gegen einen Verteidiger aufs Tor an. Sobald die Aktion vorbei ist, spielt der Trainer einen neuen Ball in die große Zone, und Team Rot kontert mit drei Spielern. Die beiden Angreifer von eben sprinten zurück und verteidigen zu zweit gegen drei.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 35 Metern, längs geteilt. Links eine kleine Zone mit Tor oben und darunter eine Wartezone, rechts eine große Zone mit Tor unten. In beiden Toren steht ein Torwart.",
  "Verteilen: Team Neon wartet zu zweit in der Wartezone, die ersten zwei stehen vorn in der kleinen Zone. Ein Verteidiger von Team Rot steht in der kleinen Zone, zwei Angreifer von Team Rot warten oben an der großen Zone. Der Trainer steht mit vielen Bällen oben zwischen den Zonen.",
  "Ablauf: Der Trainer spielt ein, und es läuft zwei gegen eins aufs obere Tor. Ist die Aktion vorbei, kommt sofort ein neuer Ball zu Team Rot in die große Zone. Der Verteidiger läuft mit nach vorn, die zwei Angreifer von Team Neon sprinten zurück. Drei gegen zwei aufs untere Tor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team, das trifft. Danach rücken die nächsten zwei von Team Neon nach, ein neuer Verteidiger von Team Rot kommt dazu, und es geht ohne Pause weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Ball weg? Sofort zurück zum Tor sprinten", "Verzögern, bis der zweite Mann da ist", "Die Mitte zu, nach außen lenken", "Mit Tempo angreifen, die Überzahl nutzen"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zwei gegen eins, dann zurück. Erst greift Team Neon zu zweit an. Danach kontert Team Rot zu dritt, und die zwei Angreifer müssen sofort zurück und verteidigen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B1] + ERSATZ,
  "steps": [
   S("Trainer spielt ein, zwei gegen eins", "Der Trainer spielt auf Spieler neun. Der nimmt den Ball mit und dribbelt Richtung Tor. Spieler fünf ist allein gegen zwei.",
     ps("b1", [29.6, 39.1]), dr("n9", "b1", [30, 29], after=True), mv("n11", [41.5, 24], delay=0.6)),
   S("Querpass, Spieler elf trifft: Punkt", "Spieler fünf geht auf Spieler neun. Der spielt quer auf Spieler elf, und Spieler elf schließt direkt ab. Das gibt einen Punkt für Team Neon.",
     mv("r5", [32.5, 26]), ps("b1", [42.1, 24.6], after=True), ps("b1", [38.5, 5.3], after=True)),
   S("Neuer Ball, sofort zurück", "Sofort spielt der Trainer einen neuen Ball rüber zu Spieler zwei. Spieler drei kommt außen mit, Spieler fünf läuft mit nach vorn. Spieler neun und Spieler elf drehen um und sprinten zurück, so schnell es geht.",
     mv("r2", [59.5, 12.5]), ps("s1", [60.1, 13.1], delay=0.3), mv("r3", [73, 22], delay=0.3), mv("r5", [50, 26], delay=0.3),
     mv("n11", [53, 34], delay=0.2), mv("n9", [61, 39], delay=0.2)),
   S("Verzögern, nach außen lenken", "Spieler elf läuft Spieler zwei von innen an und bremst ihn. Durch die Mitte geht nichts, also spielt Spieler zwei raus auf Spieler drei. Spieler neun schiebt mit nach außen.",
     dr("r2", "s1", [60, 25]), mv("n11", [57.5, 30.5], delay=0.2), mv("r3", [73, 33], delay=0.3), ps("s1", [73.6, 33.6], after=True), mv("n9", [68, 41.5], after=True)),
   S("Hereingabe, Spieler fünf trifft: Punkt", "Spieler drei spielt flach in die Mitte, und Spieler fünf ist mitgelaufen. Er trifft, und das gibt einen Punkt für Team Rot. Danach greifen Spieler acht und Spieler zehn in der kleinen Zone an, gegen einen neuen Verteidiger von Team Rot.",
     mv("r5", [56, 44]), ps("s1", [56.6, 44.6], delay=0.4), ps("s1", [57, 54.7], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ball erobert, sofort drei gegen zwei.", "Ball erobert, sofort los",
    "Gewinnt der Verteidiger im zwei gegen eins den Ball, wartet niemand auf den Trainer. Er spielt sofort rüber in die große Zone, und das drei gegen zwei läuft. Für Team Neon heißt das: Ball verloren, sofort zurück.",
    sp(), [B1] + ERSATZ,
    [S("Querpass abgefangen", "Der Trainer spielt auf Spieler neun, der dribbelt an. Spieler elf startet, und Spieler neun will quer spielen. Spieler fünf ahnt das und geht dazwischen.",
       ps("b1", [29.6, 39.1]), dr("n9", "b1", [30, 29], after=True), mv("n11", [42, 21], delay=0.6), mv("r5", [36, 25.5], delay=1.6),
       ps("b1", [36.6, 26.1], after=True)),
     S("Sofort rüber, Neon sprintet zurück", "Spieler drei kommt rein, und Spieler fünf spielt ihn sofort an. Spieler zwei und Spieler fünf laufen mit, drei gegen zwei. Spieler neun und Spieler elf drehen um und sprinten zurück, bevor es zu spät ist.",
       mv("r3", [70, 20]), ps("b1", [70.6, 20.6], delay=0.3), mv("r2", [60, 18], delay=0.3), mv("r5", [50, 26], after=True),
       mv("n11", [55, 33], delay=0.3), mv("n9", [62, 39], delay=0.3))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Zu zweit verzögern und nach außen lenken.", "Zu zweit nach außen lenken",
    "Die zwei Verteidiger arbeiten zusammen. Einer geht drauf und steht innen, der andere sichert dahinter. So bleibt der Gegner außen, und der Pass nach innen wird schwer. Wer ihn erwartet, fängt ihn ab.",
    sp(r2=(55, 18), r3=(73, 22), r5=(46, 22), n11=(56, 34), n9=(64.5, 36.5)), [B("b1", 55.6, 18.6)] + ERSATZ,
    [S("Einer geht drauf, einer sichert", "Spieler zwei dribbelt aufs Tor zu. Spieler elf geht drauf und steht innen, nur der Weg nach außen ist frei. Spieler neun sichert hinter ihm.",
       dr("r2", "b1", [56, 25]), mv("n11", [56.5, 30], delay=0.3), mv("n9", [62, 37], delay=0.3)),
     S("Nach außen gelenkt", "Spieler zwei muss raus auf Spieler drei. Jetzt schieben beide mit. Spieler neun geht nach außen, Spieler elf lässt sich in die Mitte fallen.",
       mv("r3", [73, 32]), ps("b1", [73.6, 32.6], delay=0.3), mv("n9", [69, 39], after=True), mv("n11", [57, 38], delay=1.0)),
     S("Pass nach innen abgefangen", "Spieler drei will flach nach innen auf Spieler fünf spielen. Darauf hat Spieler elf gewartet. Er geht dazwischen, und Team Neon hat den Ball.",
       mv("r5", [51, 40]), ps("b1", [57.6, 38.6], delay=0.5))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
