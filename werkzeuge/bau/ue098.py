import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 03-P6: 30 x 20 Yards (30 x 30 laut Text), gedreht: Feld x 14-86, y 6-54, Drittel bei x 38 und 62. Neon verteidigt das linke Tor, Rot greift an.
T = P("T", "c", 92, 54, "T")
goals = [{"x": 14, "y": 30, "side": "left"}, {"x": 86, "y": 30, "side": "right"}]
lines = [rect(14, 6, 72, 48), line(38, 6, 38, 54), line(62, 6, 62, 54)]
def sp(extra=(), **k):
    d = dict(n4=(52, 26.6), n5=(26, 40), n6=(26.4, 21.8), n8=(64, 32), r2=(74, 18), r3=(74, 46), r7=(56, 10), r9=(36, 30)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k1", "t", 17, 30, "TW"), P("k2", "t", 83, 30, "TW"), T] + list(extra)
cb = [B("c1", 94.6, 54.6)]
u = {"title": "Das eigene Drittel verteidigen", "code": "UE-098", "kind": "Spielform",
 "focuses": ["Verteidigen", "1 gegen 1", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 12, "field_size": "27 x 18 m",
 "description": "Vier gegen vier mit Torwart auf zwei Tore, das Feld ist in drei Drittel geteilt. Eine Mannschaft lernt, ihr Tor zu verteidigen: kompakt stehen, in jedem Drittel mindestens ein Spieler, gemeinsam entscheiden, wann gepresst und wann nur verzögert wird. Erobert sie den Ball, greift sie selbst an.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 18 Metern mit einem Tor und Torwart an jedem Ende. Mit Hütchen in drei Drittel teilen.",
  "Verteilen: Zwei Mannschaften mit je vier Feldspielern. Der Trainer gibt einer Mannschaft die Aufgabe zu verteidigen, die andere soll angreifen.",
  "Ablauf: Normales Spiel, jedes Tor gibt einen Punkt. Die verteidigende Mannschaft hat in jedem Drittel mindestens einen Spieler. Sie presst gemeinsam, wenn der Ball erobert werden kann, und verzögert, wenn sie das Tor schützen muss.",
  "Trainer: Geht der Ball ins Aus, spielt der Trainer schnell einen neuen Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Als Mannschaft kompakt bleiben, jeder kennt seine Aufgabe", "Im Eins gegen Eins nicht leicht ausspielen lassen und bei Bedarf schnell zurücklaufen", "Erkennen, wann alle gemeinsam pressen und wann verzögert wird", "Viel sprechen, um den Raum hinter der Abwehr klein zu halten"],
 "materials": ["2 Tore", "8 Hütchen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Das eigene Drittel verteidigen. Kompakt stehen, gemeinsam pressen und das Tor schützen.",
 "board": {"lines": lines, "cones": ecken(14, 6, 72, 48), "goals": goals, "players": sp(), "balls": [B("b1", 75.6, 18.6)] + cb,
  "steps": [
   S("Kompakt verschieben", "Rot zwei passt zu Rot sieben. Gleichzeitig verschiebt Neon als Einheit: Neon vier presst, die anderen rücken nach.",
     ps("b1", [57.6, 10.6]), mv("n4", [58, 16], delay=0.2), mv("n8", [62, 24], delay=0.2), mv("n6", [30, 18], delay=0.3), mv("n5", [30, 34], delay=0.3)),
   S("Pass nach vorn", "Rot sieben spielt nach vorn zu Rot neun. Neon sechs und Neon fünf schieben sofort von beiden Seiten heran.",
     ps("b1", [37.6, 30.6]), mv("n6", [33, 26], delay=0.2), mv("n5", [33, 35], delay=0.2)),
   S("Ball erobert", "Neon fünf spitzelt den Ball weg und spielt sofort zu Neon vier. Jetzt greift Neon an.",
     ps("b1", [53.6, 17.6]), mv("n4", [52, 17])),
   S("Gegenangriff: Punkt", "Neon vier spielt steil zu Neon acht, und der schießt ins Tor. Das gibt einen Punkt für Neon.",
     mv("n8", [72, 26]), ps("b1", [73.6, 26.6], delay=0.3), ps("b1", [86, 25], after=True))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 5, "y1": 6, "x2": 5, "y2": 54, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Gegner nach außen lenken und dort eine Falle stellen.", "Außen eine Falle stellen",
    "An der Seitenlinie ist wenig Platz. Der vordere Verteidiger läuft den Ballführenden so an, dass er nur nach außen kann. Die Mitspieler ahnen den nächsten Pass und warten schon darauf. So wird aus dem Flügel eine Falle.",
    sp(r2=(74, 10), n8=(65, 24)), [B("b1", 75.6, 10.6)] + cb,
    [S("Nach außen drängen", "Neon acht läuft Rot zwei von innen an. Rot zwei kann nur an der Linie entlang dribbeln.",
       mv("n8", [70, 15]), dr("r2", "b1", [64, 9], delay=0.2)),
     S("In die Falle", "Rot zwei passt zu Rot sieben, doch Neon vier hat darauf gewartet und fängt den Ball ab.",
       ps("b1", [53, 11]), mv("n4", [53, 12], delay=0.1))],
    lines=lines + [{"type": "zone", "x": 14, "y": 6, "w": 72, "h": 9}, {"type": "zone", "x": 14, "y": 45, "w": 72, "h": 9}]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Endspieler neben dem Tor helfen den Angreifern.", "Mit zwei Endspielern",
    "Neben dem Tor der Verteidiger stehen zwei Springer. Die Angreifer dürfen sie anspielen und mit ihnen kombinieren. Die Verteidiger müssen die Pässe nach vorn verhindern und ständig über die Schulter schauen, wer von hinten kommt.",
    sp([P("f1", "t", 10, 12, "F"), P("f2", "t", 10, 48, "F")], n6=(30, 13)), [B("b1", 37.6, 30.6)] + cb,
    [S("Pass zum Endspieler", "Rot neun spielt zum Springer oben und startet sofort. Neon sechs kommt zu spät.",
       ps("b1", [11.6, 12.6]), mv("r9", [28, 22], delay=0.2), mv("n6", [26, 16], delay=0.4)),
     S("Ablage und Abschluss", "Der Springer legt direkt ab, und Rot neun schießt ins Tor. Das gibt einen Punkt für Rot.",
       ps("b1", [29.6, 22.6]), ps("b1", [14, 27], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
