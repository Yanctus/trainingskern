import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-38: 25 x 20 Yards = x 20-80, y 5-53. Hindernisse wie im PDF verteilt: 2 Minitore, 3 Stangen, 4 Hürden (orange Hütchen), 2 Fahnen (gelbe Hütchen).
T = P("T", "c", 12, 52, "T")
hind = [C(41.7, 21.3, "neon", shape="stange"), C(61.4, 36, "neon", shape="stange"), C(48.6, 29, "neon", shape="stange"),
        C(37.4, 8.1), C(24.9, 21.6), C(73.5, 36.7), C(58, 50), C(30.9, 14.7, "neon"), C(67.4, 41.8, "neon")]
goals = [{"x": 62.3, "y": 15.5, "side": "top"}, {"x": 35.8, "y": 40.6, "side": "bottom"}]
warte = [P("n3", "a", 11, 20, "3"), P("n4", "a", 11, 36, "4"), P("r6", "b", 88, 48, "6"), P("r7", "b", 88, 16, "7")]
u = {"title": "Fangen mit Hindernissen", "code": "UE-078", "kind": "Spielform",
 "focuses": ["Erwärmung", "Schnelligkeit", "Koordination"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 6, "players_max": 16, "field_size": "23 x 18 m",
 "description": "Ein Fangspiel zum Aufwärmen in einem Feld voller Hindernisse. Ein Läufer versucht fünfzehn Sekunden lang, nicht von seinem Fänger berührt zu werden. Dabei nutzt er die Hindernisse, schlägt Haken und täuscht an. Schafft er es, gewinnt er die Runde, wird er berührt, bekommt der Fänger einen Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern, darin verteilt Hindernisse wie Minitore, Stangen, kleine Hürden und Hütchen.",
  "Verteilen: Zwei Gruppen. Die Läufer warten an einer Ecke, die Fänger an der gegenüberliegenden Ecke.",
  "Ablauf: Immer ein Läufer gegen einen Fänger. Auf das Zeichen starten beide gleichzeitig. Bleibt der Läufer fünfzehn Sekunden lang unberührt, gewinnt er die Runde. Berührt ihn der Fänger, bekommt der Fänger einen Punkt.",
  "Wechsel: Nach zwei Durchgängen pro Spieler tauschen die Gruppen die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell die Richtung wechseln und mit Finten den Fänger abschütteln", "Ständig umschauen, um freien Raum zu finden", "Nach dem Haken explosiv wegsprinten, vorher kontrolliert abbremsen", "Den Fänger beobachten und den besten Fluchtweg wählen"],
 "materials": ["2 Minitore", "3 Stangen", "4 kleine Hürden oder Hütchen", "2 gelbe Hütchen", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Fangen mit Hindernissen. Ein Läufer gegen einen Fänger, und fünfzehn Sekunden muss er durchhalten.",
 "board": {"lines": [rect(20, 5, 60, 48)], "cones": hind, "goals": goals,
  "players": [P("n2", "a", 22, 8, "2"), P("r5", "b", 78, 50, "5")] + warte + [T],
  "balls": [],
  "steps": [
   S("Beide starten gleichzeitig", "Auf das Zeichen des Trainers starten beide gleichzeitig: Neon zwei läuft los, Rot fünf jagt ihn. Fünfzehn Sekunden muss Neon zwei durchhalten.",
     mv("n2", [30, 18]), mv("r5", [64, 49]), mv("r5", [52, 38], after=True)),
   S("Um die Hindernisse", "Neon zwei läuft um die Stange herum und bringt sie zwischen sich und den Fänger. Rot fünf muss den Umweg mitlaufen.",
     mv("n2", [36, 27]), mv("n2", [46, 25], after=True), mv("n2", [52, 12], after=True), mv("r5", [44, 32]), mv("r5", [46, 18], after=True)),
   S("Haken am Minitor: geschafft", "Am Minitor schlägt Neon zwei einen Haken und sprintet weg. Die fünfzehn Sekunden sind um, Neon zwei wurde nicht berührt und gewinnt die Runde.",
     mv("n2", [58, 8]), mv("n2", [70, 10], after=True), mv("n2", [72, 24], after=True), mv("r5", [54, 10], delay=0.3), mv("r5", [64, 8], after=True))],
  "dims": [{"x1": 20, "y1": 58.6, "x2": 80, "y2": 58.6, "text": "23 m"}, {"x1": 95, "y1": 5, "x2": 95, "y2": 53, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit Finten und schnellen Richtungswechseln den Fänger abschütteln.", "Finte und Haken",
    "Wer nur geradeaus rennt, wird schnell gefangen. Besser: kurz in eine Richtung antäuschen, den Fänger dorthin locken und dann blitzschnell in die andere Richtung starten. Die Hindernisse helfen dabei, sie verschaffen dem Läufer wertvolle Zeit.",
    [P("n2", "a", 70, 9, "2"), P("r5", "b", 56, 24, "5")] + warte + [T], [],
    [S("Antäuschen", "Neon zwei täuscht nach links an. Rot fünf fällt darauf herein und läuft mit.", mv("n2", [66, 12]), mv("r5", [54, 15], delay=0.2)),
     S("Haken und weg", "Dann schlägt Neon zwei einen Haken nach rechts und sprintet am Minitor vorbei davon. Rot fünf steht auf der falschen Seite.",
       mv("n2", [72, 18]), mv("n2", [74, 32], after=True), mv("r5", [58, 12], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Team fängt, das andere Team weicht aus, alle gleichzeitig.", "Team gegen Team",
    "Jetzt spielt ein ganzes Team als Fänger gegen ein Team von Läufern, alle gleichzeitig im Feld. So kommt der Druck von mehreren Seiten, manchmal jagen zwei oder drei Fänger einen Läufer. Die Uhr läuft, bis alle Läufer berührt sind. Dann wechseln die Rollen, und das Team mit der längeren Zeit gewinnt.",
    [P("n2", "a", 45, 25, "2"), P("n3", "a", 36, 37, "3"), P("n4", "a", 65, 25, "4"), P("r5", "b", 25, 28, "5"), P("r6", "b", 55, 42, "6"), P("r7", "b", 75, 10, "7"), T], [],
    [S("Alle laufen gleichzeitig", "Alle laufen gleichzeitig: Die Roten jagen, die Neonspieler weichen aus. Rot fünf und Rot sechs gehen beide auf Neon zwei.",
       mv("r5", [36, 28]), mv("r6", [52, 34]), mv("n2", [50, 14]), mv("n3", [28, 46]), mv("r7", [70, 18]), mv("n4", [74, 30])),
     S("Zwei gegen einen", "Neon zwei entkommt mit einem Haken am Minitor. Gleichzeitig berührt Rot sieben Neon vier, und die Uhr läuft weiter, bis alle Neonspieler berührt sind.",
       mv("n2", [56, 8]), mv("n2", [70, 6], after=True), mv("r5", [38, 16]), mv("r6", [52, 22]), mv("r7", [73, 26]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
