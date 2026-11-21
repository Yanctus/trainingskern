import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 50-P5: 25 x 35 Yards, gedreht: Feld x 14-86, y 6-54. Links großes Tor (Neon verteidigt), rechts drei Minitore (Rot verteidigt, ein Torwart pendelt).
T = P("T", "c", 6, 6, "T")
goals = [{"x": 14, "y": 30, "side": "left"}, {"x": 86, "y": 12, "side": "right"}, {"x": 86, "y": 30, "side": "right"}, {"x": 86, "y": 48, "side": "right"}]
lines = [rect(14, 6, 72, 48)]
def sp(**k):
    d = dict(n2=(28.6, 14.9), n3=(28.4, 46.2), n4=(46.4, 27.8), n5=(58.6, 12.3), n6=(57.8, 50.9), r7=(37, 14), r8=(37.5, 43), r9=(55, 30), r10=(68.4, 13.1), r11=(67, 39.8)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k1", "t", 18, 30, "TW"), P("k2", "t", 80.8, 30, "TW"), T]
def bp(x, y): return [round(x + 1.6, 1), round(y + 0.6, 1)]
cb = [B("c1", 8.6, 6.6)]
u = {"title": "Verlagern und treffen", "code": "UE-101", "kind": "Spielform",
 "focuses": ["Passspiel", "Torschuss", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "32 x 23 m",
 "description": "Fünf gegen fünf mit Torhütern. Eine Mannschaft greift drei Minitore an, die andere verteidigt sie und hat selbst ein großes Tor als Ziel. Erst nach fünf Pässen darf auf eines der Minitore geschossen werden, und ein Torwart pendelt zwischen allen dreien. Wer den Gegner auf eine Seite lockt und dann schnell verlagert, findet das freie Tor.",
 "organisation": ["Aufbauen: Ein Feld von 32 mal 23 Metern. An einem Ende ein großes Tor, am anderen Ende drei Minitore nebeneinander.",
  "Verteilen: Zwei Mannschaften mit je fünf Spielern. Ein Torwart im großen Tor, ein zweiter Torwart pendelt zwischen den drei Minitoren.",
  "Ablauf: Die angreifende Mannschaft beginnt mit Ball. Nach fünf Pässen darf sie auf ein beliebiges Minitor schießen, jedes Tor gibt einen Punkt.",
  "Ballgewinn: Erobert die andere Mannschaft den Ball, kontert sie sofort auf das große Tor."],
 "organisation_show": ORG,
 "coaching_points": ["Genau passen und sich bewegen, um den Ball zu halten", "Den Gegner auf eine Seite locken und dann zum freien Spieler verlagern", "Immer wissen, wo die Tore stehen und welches frei ist", "Mit schnellen Doppelpässen Platz schaffen"],
 "materials": ["1 großes Tor", "3 Minitore", "4 Hütchen", "Leibchen in zwei Farben", "Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Verlagern und treffen. Fünf Pässe, dann aufs Minitor, und am besten dorthin, wo der Torwart gerade nicht steht.",
 "board": {"lines": lines, "cones": ecken(14, 6, 72, 48), "goals": goals, "players": sp(), "balls": [B("b1", 19.6, 30.6)] + cb,
  "steps": [
   S("Aufbau", "Der Torwart spielt Neon zwei an, der passt weiter zu Neon vier. Das sind zwei Pässe.", ps("b1", bp(28.6, 14.9)), ps("b1", bp(46.4, 27.8), after=True)),
   S("Auf eine Seite locken", "Neon vier spielt zu Neon fünf, und der spielt zurück. Gleichzeitig verschiebt Rot nach oben, und der Torwart geht zum oberen Minitor.",
     ps("b1", bp(58.6, 12.3)), ps("b1", bp(46.4, 27.8), after=True), mv("r10", [66, 18], delay=0.2), mv("r9", [56, 21], delay=0.4), mv("k2", [81, 15], delay=0.3)),
   S("Verlagern", "Jetzt verlagert Neon vier schnell auf die andere Seite zu Neon sechs. Das ist der fünfte Pass.", ps("b1", bp(57.8, 50.9))),
   S("Abschluss: Punkt", "Neon sechs dribbelt kurz an und schießt ins freie Minitor unten, und das gibt einen Punkt für Neon.",
     dr("n6", "b1", [70, 49]), ps("b1", [87, 48], after=True), mv("k2", [81, 30], delay=0.3))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "32 m"}, {"x1": 94, "y1": 6, "x2": 94, "y2": 54, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erobert die andere Mannschaft den Ball, kontert sie sofort auf das große Tor los.", "Konter aufs große Tor",
    "Die verteidigende Mannschaft lauert auf Fehlpässe. Ist der Ball erobert, geht es sofort nach vorn auf das große Tor, bevor sich die Angreifer wieder ordnen. Wenige Kontakte, schnelle Pässe.",
    sp(), [B("b1", 48, 28.4)] + cb,
    [S("Pass abgefangen", "Neon vier will zu Neon fünf passen, doch Rot sieben geht dazwischen.", ps("b1", [43, 19]), mv("r7", [42, 18.5], delay=0.1)),
     S("Schnell nach vorn", "Rot sieben spielt sofort weiter zu Rot acht, der Richtung Tor startet.", mv("r8", [30, 36]), ps("b1", [31.6, 36.6], delay=0.3)),
     S("Konter: Punkt", "Rot acht schießt aufs große Tor, und das gibt einen Punkt für Rot.", ps("b1", [14, 33]))]),
  V("Steigerung", "Und jetzt die Steigerung: Geschossen wird nur aus der Endzone vor den Minitoren.", "Nur aus der Endzone",
    "Vor den Minitoren entsteht eine Endzone. Nur wer mit dem Ball in diese Zone kommt, darf schießen. Die Angreifer müssen deshalb Spieler im freien Raum finden, die in die Zone laufen. Noch schwerer wird es, wenn in der Endzone nur direkt geschossen werden darf.",
    sp(r9=(55, 28), r11=(70, 36), n5=(60, 11)), [B("b1", 48, 28.4)] + cb,
    [S("Lauf in die Endzone", "Neon sechs startet in die Endzone, und Neon vier spielt ihn genau in den Lauf an.", mv("n6", [76, 50]), ps("b1", [77.6, 50.6], delay=0.4)),
     S("Direkt ins Minitor: Punkt", "Neon sechs schießt direkt ins Minitor unten, und das gibt einen Punkt für Neon.", ps("b1", [87, 48]))],
    lines=lines + [{"type": "zone", "x": 72, "y": 6, "w": 14, "h": 48}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
