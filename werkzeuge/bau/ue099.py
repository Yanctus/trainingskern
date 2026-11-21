import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 19-P4: 15 x 30 Yards, gedreht: Feld x 10-90, y 10-50. Rote Passspieler an beiden langen Seiten, vier Dummys in der Mitte (y 30).
# Neon vier und Neon fünf verteidigen als Paar: einer presst, der andere sichert am Dummy ab.
T = P("T", "c", 94, 44, "T")
OBEN = dict(r10=(23.6, 12.3), r8=(47.8, 11.4), r6=(59.9, 12.4), r2=(80.4, 12.3))
UNTEN = dict(r7=(24.8, 46.4), r11=(41.4, 48.4), r9=(60.9, 46.6), r3=(80.6, 46.4))
def sp(**k):
    d = dict(OBEN); d.update(UNTEN); d.update(n5=(13, 22), n4=(13, 40)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def bp(k): x, y = {**OBEN, **UNTEN}[k]; return [round(x + 1.6, 1), round(y + 0.6, 1)]
cones = [C(x, 30, "neon", shape="stange") for x in (19.7, 35.8, 54.7, 70.6)] + ecken(10, 10, 80, 40)
cb = [B("c1", 96.6, 44.6)]
u = {"title": "Pressen und absichern", "code": "UE-099", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 14 m",
 "description": "Zwei Verteidiger lernen, als Paar zu pressen und abzusichern. Acht Spieler an den Seiten spielen sich den Ball quer und nach vorn zu. Der Verteidiger, der dem Ball am nächsten ist, presst sofort, der andere sichert hinter ihm am Dummy ab. Wechselt der Ball die Seite, tauschen auch die beiden ihre Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 14 Metern, an beiden langen Seiten je vier Hütchen als Stationen, in der Mitte vier Dummys hintereinander.",
  "Verteilen: An jeder Station ein Passspieler, ein Spieler mit Ball beginnt. Zwei Verteidiger stehen am Anfang des Feldes.",
  "Ablauf: Der Ball wird quer über das Feld und an der Seite entlang weitergespielt. Der nächste Verteidiger presst bis auf einen Meter heran, der andere sichert am Dummy ab. Kommt der Ball auf die andere Seite, tauscht das Paar die Rollen.",
  "Zurück: Ist der Ball am Ende angekommen, geht es in die andere Richtung zurück. Die Verteidiger laufen rückwärts mit, wieder presst der nächste und der andere sichert."],
 "organisation_show": ORG,
 "coaching_points": ["So schnell wie möglich bis auf einen Meter heran pressen", "Nach jedem Pass sofort in die Absicherung gehen", "Bei langen Pässen schnell herausrücken, kurz vorher abbremsen und seitlich stehen", "Viel miteinander sprechen, zum Beispiel mit Rufen wie „Ich gehe!“ und „Ich sichere!“"],
 "materials": ["4 Dummys", "8 Hütchen", "Leibchen in zwei Farben", "Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Pressen und absichern. Einer presst den Ballführenden, der andere sichert dahinter ab.",
 "board": {"lines": [rect(10, 10, 80, 40)], "cones": cones, "players": sp(), "balls": [B("b1", *bp("r10"))] + cb,
  "steps": [
   S("Pass quer, Druck", "Rot zehn passt quer zu Rot sieben. Gleichzeitig presst Neon vier, und Neon fünf sichert am Dummy ab.",
     ps("b1", bp("r7")), mv("n4", [24, 39], delay=0.2), mv("n5", [22, 26], delay=0.2)),
   S("An der Seite weiter", "Rot sieben spielt an der Seite weiter zu Rot elf. Neon vier bleibt dran, Neon fünf rückt zum nächsten Dummy.",
     ps("b1", bp("r11")), mv("n4", [41, 41], delay=0.2), mv("n5", [37, 27], delay=0.2)),
   S("Ball quer: Rollen tauschen", "Rot elf spielt quer zu Rot acht. Jetzt presst Neon fünf, und Neon vier sichert ab.",
     ps("b1", bp("r8")), mv("n5", [47, 19], delay=0.2), mv("n4", [40, 33], delay=0.3))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "27 m"}, {"x1": 4, "y1": 10, "x2": 4, "y2": 50, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Auf dem Rückweg wechselt der Presser, und die Wege werden länger.", "Wechseln auf dem Rückweg",
    "Ist der Ball am Ende des Feldes, geht es zurück. Jetzt wird jeder Pass von einem anderen Verteidiger angelaufen, und die Wege werden länger. Wer sichert, ruft, wer presst. Kurz vor dem Gegenspieler abbremsen, tief gehen und seitlich stehen, um ihn in eine Richtung zu lenken.",
    sp(n4=(72, 40), n5=(63, 28)), [B("b1", *bp("r3"))] + cb,
    [S("Rückwärts und pressen", "Rot drei spielt zurück zu Rot neun. Neon fünf sprintet heraus und presst, Neon vier wechselt in die Absicherung.",
       ps("b1", bp("r9")), mv("n5", [66, 42], delay=0.2), mv("n4", [70, 33], delay=0.2)),
     S("Langer Weg", "Rot neun spielt quer zu Rot sechs. Jetzt muss Neon vier den langen Weg gehen und pressen, Neon fünf sichert ab.",
       ps("b1", bp("r6")), mv("n4", [60, 19], delay=0.2), mv("n5", [52, 33], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Auch Pässe schräg und an der Seite entlang sind erlaubt.", "Auch schräg passen",
    "Die Passspieler dürfen jetzt auch schräg über das Feld spielen. Die Pässe kommen unberechenbarer und die Wege werden länger. Das Paar muss noch schneller reagieren und sich ständig absprechen.",
    sp(n4=(33, 20), n5=(33, 36)), [B("b1", *bp("r10"))] + cb,
    [S("Schräger Pass", "Rot zehn spielt schräg zu Rot elf. Neon fünf presst sofort, Neon vier sichert ab.",
       ps("b1", bp("r11")), mv("n5", [41, 42], delay=0.2), mv("n4", [40, 30], delay=0.2)),
     S("Wieder schräg", "Rot elf spielt schräg zu Rot sechs. Neon vier muss weit hinaus und pressen, Neon fünf sichert ab.",
       ps("b1", bp("r6")), mv("n4", [59, 19], delay=0.2), mv("n5", [50, 34], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
