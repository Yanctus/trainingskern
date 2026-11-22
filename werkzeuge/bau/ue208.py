import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P5 (U12-U14, Woche 28 Phase 5): The Back 4 Unit Stopping the Penetrating Pass. 25 x 40 Yards = Feld x 34-66, y 5-55
# (23 x 37 m), vier Zonen zu 10 Yards (gestrichelt bei y 17.5, 30, 42.5), an beiden Enden ein Minitor und zwei Stangen (Puppen).
# Um 180 Grad gedreht: im PDF spielen die Angreifer nach unten, hier nach oben (Tor oben). Dunkel (Angreifer) -> Team Neon
# (11, 10, 9, 7 von links), Pink (Verteidiger) -> Team Rot (2, 4, 5, 3 von links), Nummern wie im PDF. Rot verteidigt das obere
# Tor und greift nach Ballgewinn das untere an. Ein Trainer, er steht rechts (im PDF links) mit Bällen. Wertung wie im PDF:
# Minitor zwei Punkte, Stange ein Punkt. Positionen auf Abstand gesetzt (3D).
# Sichtkegel: Text "Recognise opportunities to play through", "Awareness of defensive angles and distances", Ton "positional
# awareness" -> Neon zehn schaut vor dem Pass in die Lücke der Viererkette (Grundform und erster Coaching-Punkt), Richtung aus
# dem Sinn (im Video kein Kegel eingezeichnet).
T = P("T", "c", 81, 40, "T")
POS = {"n11": (37, 37.5), "n10": (45.5, 40.5), "n9": (54.5, 40.5), "n7": (63, 37.5),
       "r2": (37, 21), "r4": (45.5, 22.5), "r5": (54.5, 22.5), "r3": (63, 21)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 82.6, 44), B("s2", 79, 44)]
LINES = [rect(34, 5, 32, 50), line(34, 17.5, 66, 17.5), line(34, 30, 66, 30), line(34, 42.5, 66, 42.5)]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 50, "y": 55, "side": "bottom"}]
KEGEL = [C(x, y, "neon", shape="stange") for x in (38.5, 61.5) for y in (9, 51)]

u = {"title": "Den Steilpass verhindern", "code": "UE-208", "kind": "Spielform",
 "focuses": ["Verteidigen", "Passspiel", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "23 x 37 m",
 "description": "Zwei Viererketten stehen sich in zwei Zonen in der Mitte gegenüber. Das Team am Ball spielt sich den Ball zu und sucht eine Lücke, um flach durch die andere Kette zu passen: ins Minitor dahinter oder an eine Stange. Die verteidigende Kette schiebt eng zusammen mit, sichert ab und fängt den Pass ab. Wer den Ball erobert, greift sofort in die andere Richtung an.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 37 Metern in vier Zonen. In den beiden Endzonen je ein Minitor und zwei Stangen.",
  "Verteilen: Team Neon zu viert in der unteren Mittelzone, Team Rot zu viert in der oberen. Jedes Team bleibt in seiner Zone. Der Trainer steht rechts an der Seite mit Bällen.",
  "Ablauf: Das Team am Ball passt sich den Ball zu und hat höchstens sieben Pässe, dann muss es durch die andere Kette spielen, nur flach. Die verteidigende Kette schiebt mit, einer presst, die anderen sichern ab.",
  "Wertung und Wechsel: Ein Pass ins Minitor gibt zwei Punkte, ein Treffer an die Stange gibt einen Punkt. Wer den Ball erobert, greift in die andere Richtung an. Wer zuerst acht oder zehn Punkte hat, gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und gemeinsam als Kette zur Seite schieben", "Abstände kurz halten, damit keine Lücke entsteht", "Den Pressenden immer schräg dahinter absichern", "Viel reden und mit Zeichen zeigen, um eng zu bleiben"],
 "materials": ["2 Minitore", "4 Stangen", "12 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Den Steilpass verhindern. Zwei Viererketten spielen gegeneinander, und die verteidigende Kette bleibt eng zusammen.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 63.6, 38.1)] + ERSATZ,
  "steps": [
   S("Ball laufen lassen", "Team Neon hat den Ball. Neon sieben spielt zu Neon neun und der zu Neon zehn. Gleichzeitig schiebt Team Rot als Kette mit zur Seite.",
     ps("b1", [55.1, 41.1]), ps("b1", [46.1, 41.1], after=True), mv("r3", [59, 21], delay=0.4), mv("r5", [51.5, 23], delay=0.4), mv("r2", [38, 22], delay=0.4)),
   S("Pressen und absichern", "Rot vier presst Neon zehn bis an den Rand seiner Zone. Rot fünf sichert schräg dahinter ab. Neon zehn schaut, ob es eine Lücke für einen Steilpass gibt.",
     mv("r4", [45.5, 29]), mv("r5", [49.5, 21]), mv("n9", [52.5, 43]), bl("n10", [50, 22], after=True)),
   S("Pass abgefangen", "Neon zehn spielt den Steilpass, aber Rot fünf steht genau richtig und fängt den Ball ab.",
     ps("b1", [50.1, 21.6])),
   S("Zur Stange: Punkt", "Jetzt ist Team Rot am Ball. Rot fünf spielt sofort flach durch die Neon-Kette an die Stange unten rechts, und das gibt einen Punkt für Team Rot. Danach bekommt Team Neon einen neuen Ball vom Trainer.",
     ps("b1", [60.8, 50.2]))],
  "dims": dims(34, 66, 5, 55, "23 m", "37 m", rx=73)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Eng zusammen bleiben.", "Eng zusammen",
    "Stehen die Verteidiger zu weit auseinander, entsteht eine Lücke. Die Angreifer sehen sie und spielen den Ball hindurch. Deshalb bleibt die Kette eng zusammen und schiebt gemeinsam.",
    sp(r2=(35.5, 20.5), r4=(44, 22), r5=(56, 21), r3=(64.5, 22), n10=(45.5, 40.5)), [B("b1", 46.1, 41.1)] + ERSATZ,
    [S("Die Lücke sehen", "Rot vier und Rot fünf stehen zu weit auseinander. Neon zehn schaut hoch und sieht die Lücke zwischen den beiden.",
       bl("n10", [50, 22])),
     S("Durch die Lücke: Punkt", "Neon zehn spielt flach durch die Lücke ins Minitor, und das gibt zwei Punkte für Team Neon. Darum: eng zusammen bleiben!",
       ps("b1", [50, 5.8]))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger darf in die andere Zone.", "Hoch pressen",
    "Jetzt darf immer ein Verteidiger in die Zone der Angreifer laufen und pressen. Die anderen drei sichern dahinter ab. Ein Ballgewinn weit vorn bringt schnell Punkte, aber wer zu früh rausläuft, öffnet eine Lücke.",
    sp(), [B("b1", 63.6, 38.1)] + ERSATZ,
    [S("Schlechte Ballannahme", "Neon sieben spielt zu Neon neun. Der Ball springt ihm vom Fuß. Sofort sprintet Rot fünf in die Zone von Neon und presst, Rot vier und Rot drei schieben nach innen und sichern ab.",
       ps("b1", [55.1, 41.1]), ps("b1", [52.5, 36.5], after=True), mv("r5", [52, 36], delay=0.8), mv("r4", [48.5, 24], delay=0.8), mv("r3", [58, 22], delay=0.8)),
     S("Ball erobert: Punkt", "Rot fünf erobert den Ball, dribbelt an Neon neun vorbei und schießt flach ins untere Minitor, und das gibt zwei Punkte für Team Rot. Danach bekommt Team Neon einen neuen Ball vom Trainer.",
       dr("r5", "b1", [49.5, 47]), ps("b1", [50, 54.2], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
