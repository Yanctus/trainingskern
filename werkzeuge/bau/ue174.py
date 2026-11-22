import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 70-P6 (U12-U14, Woche 14 Phase 4): Win the Ball Back Within 6 Seconds SSG. 25 x 35 Yards = Feld x 32.1-67.9, y 5-55 (23 x 32 m),
# an jedem Ende ein Jugendtor mit Torwart. Pink (im PDF ohne Nummern, im Video 4, 8, 7, 11, 10) -> Neon mit den Video-Nummern,
# greift nach oben an. Blau (im Video türkis 4, 2, 3, 5, 6) -> Rot; Blau 4 -> Rot 9 (im Video doppelt). Torhüter im PDF grün
# (neutral) -> k1 oben, k2 unten (team t, TW) wie bei UE-101. Positionen auf ein Spaltenraster gesetzt (3D-Abstand), Spielidee wie im PDF. Ein Trainer statt zwei.
# Steigerung: Rot zwei steht als Anspieler außerhalb des Feldes (rechts), zwei Kontakte, dann Pass zurück ins Feld.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 78, 12, "T")
POS = {"n4": (41.7, 12), "n8": (58.3, 7), "n7": (58.3, 23), "n11": (33.4, 27), "n10": (50, 37.9),
       "r9": (50, 22.3), "r2": (66.7, 30), "r3": (33.4, 43), "r5": (58.3, 43), "r6": (41.7, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P("k1", "t", 50, 6.5, "TW")] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k2", "t", 50, 53.5, "TW"), T]
ERSATZ = [B("s1", 79.6, 15.5), B("s2", 76, 15.5)]
LINES = [rect(32.1, 5, 35.8, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Sechs Sekunden Gegenpressing", "code": "UE-174", "kind": "Spielform",
 "focuses": ["Umschalten", "Verteidigen", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 32 m",
 "description": "Fünf gegen fünf mit Torwart auf zwei Jugendtore. Das Team am Ball braucht fünf Pässe, bevor es aufs Tor schießen darf. Verliert ein Team den Ball, hat es sechs Sekunden, um ihn zurückzuerobern. Gelingt das, gibt das einen Punkt, und das andere Team muss jetzt selbst sofort pressen.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern mit einem Jugendtor an jedem Ende.",
  "Verteilen: Zwei Teams zu fünft, dazu in jedem Tor ein Torwart. Team Neon greift nach oben an, Team Rot nach unten. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Ein Team beginnt mit dem Ball und braucht fünf Pässe, dann darf es schießen. Bei Ballverlust pressen alle sofort gemeinsam und wollen den Ball in sechs Sekunden zurück.",
  "Wertung: Ein Treffer gibt einen Punkt. Ball in sechs Sekunden zurückerobert gibt auch einen Punkt. Danach presst das andere Team. Nach jedem Treffer bringt der Trainer einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Gemeinsam auf die Signale reagieren: schlechter Pass, schlechte Annahme", "Nach Ballverlust sofort mit vollem Tempo pressen", "Als Team verteidigen, nicht allein", "Mit dem Ball schnell spielen und gute Anspielwinkel anbieten"],
 "materials": ["2 Jugendtore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Sechs Sekunden Gegenpressing. Fünf gegen fünf, und wer den Ball verliert, will ihn in sechs Sekunden zurück.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 42.3, 12.6)] + ERSATZ,
  "steps": [
   S("Fünf Pässe", "Team Neon hat den Ball und braucht fünf Pässe, dann darf es aufs Tor schießen. Neon vier spielt zu Neon acht, der weiter zu Neon sieben.",
     ps("b1", [58.9, 7.6]), ps("b1", [58.9, 23.6], after=True)),
   S("Abgefangen", "Neon sieben will zu Neon zehn passen, aber Rot neun fängt den Ball ab und spielt sofort zu Rot fünf.",
     mv("r9", [55.8, 27.5]), ps("b1", [56.4, 28.1]), ps("b1", [58.9, 43.6], after=True)),
   S("Sechs Sekunden", "Ballverlust! Jetzt hat Team Neon sechs Sekunden. Neon zehn, Neon sieben und Neon elf sprinten gleichzeitig los und machen Rot fünf eng.",
     mv("n10", [54, 45]), mv("n7", [63.5, 38]), mv("n11", [50, 47])),
   S("Zurückerobert: Punkt", "Neon zehn erobert den Ball nach vier Sekunden zurück, und das gibt einen Punkt für Team Neon. Jetzt muss Team Rot sofort pressen und hat selbst sechs Sekunden.",
     mv("n10", [57.5, 44.5]), dr("n10", "b1", [53, 36], after=True))],
  "dims": dims(32.1, 67.9, 5, 55, "23 m", "32 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Gemeinsam pressen.", "Gemeinsam pressen",
    "Nach dem Ballverlust pressen alle zusammen. Einer geht auf den Ball, die anderen stellen die Passwege zu. So muss der Gegner unter Druck passen, und der Ball ist schnell wieder da.",
    sp(), [B("b1", 50.6, 22.9)] + ERSATZ,
    [S("Alle zusammen", "Rot neun hat gerade den Ball erobert. Sofort laufen Neon zehn, Neon sieben und Neon vier gleichzeitig los. Neon sieben stellt den Pass zu Rot zwei zu.",
       mv("n10", [52.5, 30]), mv("n7", [61.5, 27]), mv("n4", [46, 17])),
     S("Abgefangen: Punkt", "Rot neun muss unter Druck schnell passen. Neon elf fängt den Pass zu Rot drei ab, und das gibt einen Punkt für Team Neon.",
       mv("n11", [44.3, 29.4]), ps("b1", [44.9, 30], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Anspieler draußen.", "Anspieler draußen",
    "Rot zwei steht jetzt außerhalb des Feldes als Anspieler. Er darf den Ball zweimal berühren und muss dann zurück ins Feld passen. Team Neon muss noch schneller pressen und diesen Pass verhindern.",
    sp(r2=(73, 33)), [B("b1", 58.9, 23.6)] + ERSATZ,
    [S("Abgefangen", "Neon sieben will zu Neon zehn passen, aber Rot neun fängt den Ball ab.",
       mv("r9", [55.8, 27.5]), ps("b1", [56.4, 28.1])),
     S("Raus zum Anspieler", "Rot neun spielt sofort raus zu Rot zwei. Neon zehn sprintet los und stellt den Pass zurück ins Feld zu.",
       ps("b1", [73.6, 33.6]), mv("n10", [62.4, 40.2], delay=0.2)),
     S("Abgefangen: Punkt", "Rot zwei passt nach zwei Kontakten zu Rot fünf, aber Neon zehn fängt den Ball ab. Das gibt einen Punkt für Team Neon, und jetzt presst Team Rot.",
       ps("b1", [63, 40.8]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
