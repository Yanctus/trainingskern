import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 06-P2: 30 x 15 Yards, gedreht: Feld x 14-86, y 12-48, Mittellinie x 50. Links 5 gegen 2 (Neon hält den Ball, Rot 7+8 pressen), rechts warten Rot 9-11.
T = P("T", "c", 72, 55, "T")
cb = [B("c1", 74.6, 55.4), B("c2", 69.6, 55.6)]
lines = [rect(14, 12, 72, 36), line(50, 12, 50, 48)]
cones = ecken(14, 12, 72, 36) + [C(50, 12), C(50, 48)]
def sp(n=None, r=None):
    nn = dict(n2=(20, 16), n3=(20, 44), n4=(30, 38), n5=(49, 16), n6=(49, 44)); nn.update(n or {})
    rr = dict(r7=(31, 22), r8=(40, 30), r9=(62, 22), r10=(78, 30), r11=(62, 40)); rr.update(r or {})
    return [P(k, "a", *v, k[1:]) for k, v in nn.items()] + [P(k, "b", *v, k[1:]) for k, v in rr.items()] + [T]
b0 = [B("b1", 21.6, 44.6)] + cb
u = {"title": "Zu zweit kompakt verteidigen", "code": "UE-080", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 14 m",
 "description": "Ein Feld mit zwei Hälften. In der einen Hälfte spielen fünf gegen zwei: Die fünf halten den Ball, die zwei Verteidiger pressen gemeinsam als Paar. Erobern sie den Ball, spielen sie ihn sofort zu ihren drei Mitspielern in der anderen Hälfte und werden zur Passmannschaft. Dann wechseln zwei Spieler der anderen Mannschaft hinüber und pressen dort als neues Paar.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 14 Metern, in der Mitte geteilt in zwei gleich große Hälften.",
  "Verteilen: Zwei Mannschaften mit je fünf Spielern. Mannschaft Neon hat alle fünf in der linken Hälfte. Von Mannschaft Rot pressen zwei in der linken Hälfte, die anderen drei warten rechts.",
  "Ablauf: Neon hält den Ball, das rote Paar presst gemeinsam. Erobert Rot den Ball, spielt es ihn sofort in die andere Hälfte. Jetzt hat Rot dort fünf Spieler, und zwei Neonspieler wechseln hinüber, um als Paar zu pressen.",
  "Trainer: Geht der Ball ins Aus, spielt der Trainer sofort einen neuen Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem Ball Platz schaffen: nach dem Ballgewinn schnell auseinanderlaufen", "Als Paar kompakt bleiben, Abstände und Winkel ständig prüfen", "Gemeinsam entscheiden, ob nach innen oder außen gelenkt wird", "Auslöser zum Pressen erkennen: langsamer Pass, schlechte Annahme, ungenauer Pass"],
 "materials": ["6 orange Hütchen", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Zu zweit kompakt verteidigen. Fünf gegen zwei, und das Paar presst immer gemeinsam.",
 "board": {"lines": lines, "cones": cones, "players": sp(), "balls": b0,
  "steps": [
   S("Fünf gegen zwei", "Neon spielt sich den Ball zu, Neon drei passt zu Neon vier. Gleichzeitig verschieben Rot sieben und Rot acht gemeinsam und bleiben dicht beieinander.",
     ps("b1", [31.6, 38.6]), mv("r7", [30, 28], delay=0.2), mv("r8", [38, 33], delay=0.2)),
   S("Auslöser: langsamer Pass", "Neon vier spielt einen zu langsamen Pass. Das ist das Signal: Rot acht sprintet hinein und fängt ihn ab.",
     ps("b1", [42.6, 27.6]), mv("r8", [42, 26.5], delay=0.2)),
   S("Sofort verlagern", "Rot acht spielt den Ball sofort hinüber zu Rot elf in die andere Hälfte. Jetzt hat Rot den Ball.", ps("b1", [60.4, 40.6])),
   S("Rollen tauschen", "Gleichzeitig laufen Rot sieben und Rot acht zu ihren Mitspielern, und Neon fünf und Neon sechs wechseln hinüber. Sie pressen jetzt als neues Paar.",
     mv("r7", [70, 14]), mv("r8", [80, 44]), mv("n5", [58, 28], delay=0.2), mv("n6", [66, 32], delay=0.2))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 96, "y1": 12, "x2": 96, "y2": 48, "text": "14 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Passmannschaft tauscht ständig die Positionen, das Paar lenkt das Spiel auf eine Seite.", "Rotieren und lenken",
    "Die Spieler mit Ball bleiben in Bewegung und tauschen die Positionen, damit das Spiel flüssig bleibt. Das verteidigende Paar stellt den Weg in die Mitte zu und lenkt das Spiel auf eine Seite. Dort ist es eng, und ein Pass lässt sich leichter abfangen.",
    sp(), b0,
    [S("Positionen tauschen", "Neon drei spielt zu Neon zwei. Gleichzeitig tauschen Neon drei und Neon vier die Plätze, damit das Spiel in Bewegung bleibt.",
       ps("b1", [21.6, 16.6]), mv("n3", [30, 40], delay=0.2), mv("n4", [21, 44], delay=0.2)),
     S("Auf eine Seite lenken", "Das rote Paar verschiebt gemeinsam nach oben und stellt den Weg in die Mitte zu. Neon zwei bleibt nur der Pass an der Seite entlang.",
       mv("r7", [28, 21]), mv("r8", [36, 27])),
     S("Abfangen", "Neon zwei spielt an der Seite entlang zu Neon fünf. Rot sieben rechnet damit und fängt den Ball ab.",
       ps("b1", [35.4, 17.2]), mv("r7", [35, 18.5], delay=0.2))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein dritter Verteidiger kommt dazu, jetzt heißt es fünf gegen drei.", "Mit drittem Verteidiger",
    "Ein Spieler aus der anderen Hälfte darf mitpressen, zum Beispiel nach drei Pässen der Passmannschaft oder als Belohnung, wenn das Paar das Spiel gut auf eine Seite gelenkt hat. Fünf gegen drei ist für die Passmannschaft deutlich schwerer: schneller entscheiden, genauer passen, mehr umschauen.",
    sp(), b0,
    [S("Der Dritte kommt", "Neon drei spielt zu Neon vier. Gleichzeitig sprintet Rot neun aus der anderen Hälfte herüber und presst mit.",
       ps("b1", [31.6, 38.6]), mv("r9", [46, 20], delay=0.1), mv("r7", [30, 28], delay=0.2), mv("r8", [38, 33], delay=0.2)),
     S("Kompakt zu dritt", "Die drei Roten stehen jetzt eng zusammen. Neon vier findet keinen freien Mitspieler und spielt ungenau, Rot acht erobert den Ball.",
       ps("b1", [39.6, 33.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
