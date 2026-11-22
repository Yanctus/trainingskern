import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 28-P12 (U12-U14, Woche 37 Phase 1): Play Out from the Back (Technical Pattern). 25 x 35 Yards = Feld x 32-68, y 5-55 (23 x 32 m).
# Gedreht (PDF: Spiel von links nach rechts), hier Spiel von unten nach oben: Innenverteidiger unten, Flügelspieler oben.
# Pink -> Team Neon (alle in einem Team, Nummern wie im PDF). Acht Stationen mit je einem Hütchen; an der ersten Station stehen zwei
# (Spieler sechs mit Ball, Spieler neun wartet daneben, 3D-Abstand). Hütchen je nach Station leicht versetzt (Laufwege frei). Ein Trainer. Kein Duplikat von UE-147 (28-P5, Pressing-Spiel
# mit Torwart und Minitoren) oder UE-110 (28-P3, Rondo vier gegen drei mit Übergabe): hier ein Passmuster ohne Gegner.
# Grundform = Breakdown 1 und 2 (Video 0:06-0:24): 6 -> 5 -> 4 -> 10 -> zurück zu 2 -> 7 -> quer zu 11, dann zurück 11 -> 4 -> 5 ->
# 3 -> 9 (erste Station). "Jeder folgt seinem Pass": Nachlaufen bis kurz vor die Station, die Station wird frei, sobald der dortige
# Spieler weitergespielt hat (im Rückweg nur im Text). "4 und 3 bleiben im Kreislauf" vereinfacht: alle wechseln nach einer Weile.
# Fassungen: Coaching-Punkt "Go and show movement - losing markers" (Video 0:26-0:37) und Progression (Doppelpässe, PDF Seite 2).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; im Video nur ein Markierungskreis beim Freilaufen).
T = P("T", "c", 24, 54, "T")
ST = {"A": (41.5, 50), "B": (58.5, 50), "C": (50, 36.5), "D": (50, 20.5), "E": (60.5, 30), "F": (59, 9), "G": (41, 9), "H": (39.5, 30)}
POS = {"n6": ST["A"], "n9": (33, 47), "n5": ST["B"], "n4": ST["C"], "n10": ST["D"], "n2": ST["E"], "n7": ST["F"], "n11": ST["G"], "n3": ST["H"]}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fb(p): return [p[0] + 0.6, p[1] + 0.6]
ERSATZ = [B("s1", 25.6, 50.5), B("s2", 22, 50.5)]
LINES = [rect(32, 5, 36, 50)]
OFF = {"A": (-2, 2), "B": (2, 2), "C": (-2, 2), "D": (2, -2), "E": (2, 2), "F": (2, -2), "G": (-2, -2), "H": (-2, -2)}
CONES = [C(x + OFF[k][0], y + OFF[k][1]) for k, (x, y) in ST.items()]

u = {"title": "Passmuster von hinten heraus", "code": "UE-235", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "23 x 32 m",
 "description": "Ein festes Passmuster ohne Gegner, mit dem die Kinder das Herausspielen von hinten üben. Der Ball geht von den Innenverteidigern über Sechser und Zehner zum Außenverteidiger, auf den Flügel und quer zum anderen Flügel. Von dort läuft das Muster zurück bis zur ersten Station. Jeder läuft seinem Pass hinterher zur nächsten Station.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern mit acht Hütchen als Stationen.",
  "Verteilen: An jeder Station ein Spieler, an der ersten Station zwei. Spieler sechs hat den Ball. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Spieler sechs spielt quer zu Spieler fünf, dann geht der Ball über Spieler vier und Spieler zehn zurück zu Spieler zwei, auf den Flügel zu Spieler sieben und quer zu Spieler elf. Dann läuft das Muster zurück bis zur ersten Station.",
  "Wechsel: Jeder läuft seinem Pass hinterher zur nächsten Station. Nach einer festen Zeit wechseln die Spieler, die länger im Kreislauf bleiben."],
 "organisation_show": ORG,
 "coaching_points": ["Scharf und genau passen, etwas vor den Mitspieler", "Erst weglaufen, dann anbieten, wie im Spiel gegen einen Gegner", "Laut miteinander reden und beide Füße benutzen", "Mit einem oder zwei Kontakten spielen und das Muster kennen"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Passmuster von hinten heraus. Der Ball läuft in einem festen Muster von den Innenverteidigern bis auf den Flügel und wieder zurück.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 42.1, 50.6)] + ERSATZ,
  "steps": [
   S("Hinten anfangen", "Spieler sechs spielt quer zu Spieler fünf und läuft hinterher. Spieler fünf spielt direkt in die Mitte zu Spieler vier und läuft auch hinterher. Spieler neun rückt an die erste Station.",
     ps("b1", fb(ST["B"])), mv("n6", [50, 50], delay=0.2), ps("b1", fb(ST["C"]), after=True), mv("n5", [55, 43], delay=0.2), mv("n9", ST["A"], delay=0.2)),
   S("Durch die Mitte", "Spieler vier spielt nach vorn zu Spieler zehn, und der legt den Ball zurück zu Spieler zwei. Gleichzeitig rücken Spieler sechs und Spieler fünf auf die freien Stationen.",
     ps("b1", fb(ST["D"])), mv("n6", ST["B"], delay=0.2), mv("n5", ST["C"], delay=0.4), mv("n4", [50, 28.5], delay=0.2),
     ps("b1", fb(ST["E"]), after=True), mv("n10", [55, 24.5], delay=0.2)),
   S("Auf den Flügel", "Spieler zwei spielt auf den Flügel zu Spieler sieben, und der spielt quer zu Spieler elf. Auch hier läuft jeder seinem Pass hinterher.",
     ps("b1", fb(ST["F"])), mv("n4", ST["D"], delay=0.2), mv("n10", ST["E"], delay=0.4), mv("n2", [60, 19], delay=0.2),
     ps("b1", fb(ST["G"]), after=True), mv("n7", [50, 5], delay=0.2)),
   S("Und zurück", "Jetzt läuft das Muster zurück. Spieler elf spielt zu Spieler vier in der Mitte, und der legt zurück zu Spieler fünf. Spieler drei kommt nach innen.",
     ps("b1", fb(ST["D"])), mv("n2", ST["F"], delay=0.2), ps("b1", fb(ST["C"]), after=True), mv("n3", [41, 32], delay=0.2)),
   S("Wieder am Anfang", "Spieler fünf spielt zu Spieler drei, und der spielt zurück zur ersten Station zu Spieler neun. Damit ist die Runde geschafft. Jetzt beginnt Spieler neun von vorn, und alle laufen weiter ihrem Pass hinterher.",
     ps("b1", fb((41, 32))), ps("b1", fb(ST["A"]), after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst weglaufen, dann anbieten.", "Erst weg, dann zeigen",
    "Im Spiel steht ein Gegner hinter dem Sechser. Darum läuft der Sechser zuerst ein paar Schritte weg und nimmt den Gegner mit. Dann kommt er schnell zurück, bietet sich offen an und spielt mit einem Kontakt weiter.",
    sp(), [B("b1", 59.1, 50.6)] + ERSATZ,
    [S("Erst weg", "Spieler fünf hat den Ball. Spieler vier läuft zuerst ein paar Schritte weg vom Ball, so als würde er einen Gegner mitnehmen.",
       mv("n4", [46, 30])),
     S("Dann zeigen", "Jetzt kommt Spieler vier schnell zurück und bietet sich offen an. Spieler fünf spielt ihn an.",
       mv("n4", [51, 38]), ps("b1", [51.6, 38.6], delay=0.4)),
     S("Mit einem Kontakt", "Spieler vier spielt direkt weiter zu Spieler zehn. So geht das Muster ohne Pause weiter.",
       ps("b1", fb(ST["D"])))]),
  V("Steigerung", "Und jetzt die Steigerung: Doppelpässe einbauen.", "Mit Doppelpässen",
    "Jetzt kommen Doppelpässe in das Muster. Der Ball geht kurz hin und zurück, bevor er weiterläuft. Das bringt mehr Ballkontakte und mehr Tempo. Danach geht es auf der anderen Seite genauso zurück.",
    sp(), [B("b1", 59.1, 50.6)] + ERSATZ,
    [S("Doppelpass in der Mitte", "Spieler fünf spielt zu Spieler vier und läuft nach vorn. Spieler vier spielt direkt zurück in seinen Lauf.",
       ps("b1", fb(ST["C"])), mv("n5", [58, 41], after=True), ps("b1", [58.6, 41.6], delay=0.2)),
     S("Zum Zehner", "Spieler fünf spielt zu Spieler zehn, und der legt den Ball zurück zu Spieler zwei.",
       ps("b1", fb(ST["D"])), ps("b1", fb(ST["E"]), after=True)),
     S("Doppelpass am Flügel", "Spieler zwei spielt zu Spieler sieben und startet nach vorn. Spieler sieben spielt direkt zurück, und Spieler zwei spielt quer zu Spieler elf.",
       ps("b1", fb(ST["F"])), mv("n2", [62, 18], after=True), ps("b1", [62.6, 18.6], delay=0.2), ps("b1", fb(ST["G"]), after=True))])]}
u["board"]["dims"] = dims(32, 68, 5, 55, "23 m", "32 m")
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
