import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 87-P1: 20 x 15 Yards, gedreht: x 14-78, y 8-52, Minitor rechts. Raute: Start links, oben, unten, vorn.
T = P("T", "c", 6, 50, "T")
CB = [B("c1", 8.5, 50.6), B("c2", 5, 53.5)]
POS = {"n11": (24, 30), "n10": (15, 30), "n8": (42, 14), "n7": (42, 46), "n9": (60, 30)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T] + list(extra)
HUET = [C(26, 34), C(44, 10), C(44, 50), C(62, 34)]
TOR = [{"x": 78, "y": 30, "side": "right"}]
u = {"title": "Knack den Code", "code": "UE-111", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 5, "players_max": 8, "field_size": "18 x 14 m",
 "description": "Die Spieler stehen in einer Raute vor einem Minitor. Ein Spieler bekommt heimlich den Code: eine bestimmte Passfolge, die mit einem Torschuss endet. Nur er kennt sie und muss seine Mitspieler mit klaren Ansagen durch die Passfolge führen. Der Trainer hält sich zurück und hilft nur mit Fragen.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern mit vier Hütchen als Raute. Rechts steht ein Minitor.",
  "Verteilen: Je ein Spieler an den Hütchen oben, unten und vorn, am Start links zwei Spieler mit Bällen. Ein Spieler kennt den Code, zum Beispiel Spieler acht.",
  "Ablauf: Der Spieler mit dem Code sagt an, wer wohin spielt. Die anderen folgen seinen Ansagen, bis die Passfolge mit einem Torschuss endet. Danach folgt jeder seinem Pass, und der nächste Ball startet.",
  "Wechsel: Nach fünf bis acht Durchgängen bekommt ein anderer Spieler den Code. Er darf sich auch selbst eine Passfolge ausdenken."],
 "organisation_show": ORG,
 "coaching_points": ["Der Spieler mit dem Code gibt klare und ständige Ansagen", "Erkennen, wann das Spiel schneller oder langsamer werden muss", "Im richtigen Moment im freien Raum ankommen", "Den Pass an Entfernung und Position des Mitspielers anpassen, und der Anführer lobt und verbessert"],
 "materials": ["4 orange Hütchen", "1 Minitor", "Mehrere Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Knack den Code. Nur ein Spieler kennt die Passfolge und führt die anderen mit Ansagen bis zum Abschluss.",
 "board": {"lines": [rect(14, 8, 64, 44)], "cones": HUET, "goals": TOR, "players": sp(), "balls": [B("b1", 25.6, 30.6), B("b2", 16.6, 30.6)] + CB,
  "steps": [
   S("Doppelpass auf Ansage", "Spieler acht kennt den Code und ruft. Spieler elf spielt zu Spieler sieben und bekommt den Ball direkt zurück.",
     ps("b1", [40.4, 46.6]), ps("b1", [25.6, 30.6], after=True)),
   S("Langer Pass und Ablage", "Spieler elf spielt fest und flach zu Spieler neun vorn. Spieler neun legt den Ball zu Spieler acht ab.",
     ps("b1", [58.4, 30.6]), ps("b1", [43.6, 15.6], after=True)),
   S("Mitnehmen und Abschluss", "Spieler acht nimmt den Ball nach vorn mit und schießt ins Minitor. Das gibt einen Punkt für die Gruppe.",
     dr("n8", "b1", [54, 14]), ps("b1", [77.5, 29], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 78, "y2": 58.6, "text": "18 m"}, {"x1": 86, "y1": 8, "x2": 86, "y2": 52, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit Fragen statt Ansagen helfen.", "Was war das Problem?",
    "Geht ein Pass schief, ruft der Trainer Stopp und fragt: Was war das Problem bei diesem Pass? Die Spieler finden die Antwort selbst, zum Beispiel: zu weich. Über kurze Wege reicht ein weicher Pass, über lange Wege muss er fester und genauer kommen.",
    sp(), [B("b1", 43.6, 14.6), B("b2", 43.6, 46.6)] + CB,
    [S("Ein zu weicher Pass", "Spieler acht spielt zu Spieler neun, aber der Pass ist zu weich. Spieler neun muss dem Ball entgegenlaufen. Der Trainer ruft Stopp und fragt, was das Problem war.",
       ps("b1", [51, 21]), mv("n9", [53, 25], delay=0.4)),
     S("Jetzt fester", "Spieler neun geht zurück an sein Hütchen. Diesmal spielt Spieler sieben fest und flach, und der Ball kommt genau in den Fuß.",
       mv("n9", [60, 30]), ps("b2", [58.4, 30.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger kommt dazu.", "Mit Verteidiger",
    "Ein Verteidiger von Team Rot stört jetzt die Passfolge. Der Druck wird in drei Stufen erhöht. Bronze: Er verteidigt nur halb. Silber: Er greift richtig an, aber nur in der Zone vor dem Tor. Gold: Er greift überall an.",
    sp([P("r6", "b", 72, 42, "6")]), [B("b1", 25.6, 30.6), B("b2", 16.6, 30.6)] + CB,
    [S("Code unter Druck", "Spieler elf spielt zu Spieler neun, und Spieler neun legt zu Spieler acht ab.",
       ps("b1", [58.4, 30.6]), ps("b1", [43.6, 15.6], after=True)),
     S("In die Zone und Abschluss", "Spieler acht dribbelt in die Zone vor dem Tor. Gleichzeitig greift Rot sechs an, doch Spieler acht schießt vorher ins Minitor. Das gibt einen Punkt für die Gruppe.",
       dr("n8", "b1", [62, 15]), mv("r6", [70, 30], delay=0.2), ps("b1", [77.5, 28], after=True))],
    lines=[rect(14, 8, 64, 44), line(66, 8, 66, 52)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
