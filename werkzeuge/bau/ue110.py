import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 28-P3: 32 x 16 Yards, gedreht: x 10-90, y 10-50. Endzonen je 8 Yards, Mittelzone 16 Yards (grau), Minitore links und rechts.
T = P("T", "c", 4, 50, "T")
CB = [B("c1", 6.5, 50.6), B("c2", 3, 53.5)]
POS = {"n2": (18, 16), "n3": (18, 44), "n6": (41, 44), "n8": (59, 16), "n4": (82, 16), "n5": (82, 44), "r7": (36, 22), "r9": (50, 30), "r10": (64, 38)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(10, 10, 80, 40), {"type": "zone", "x": 30, "y": 10, "w": 40, "h": 40}, line(30, 10, 30, 50), line(70, 10, 70, 50)]
TORE = [{"x": 10, "y": 30, "side": "left"}, {"x": 90, "y": 30, "side": "right"}]
u = {"title": "Vier gegen drei mit Übergabe", "code": "UE-110", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 9, "players_max": 11, "field_size": "29 x 15 m",
 "description": "Ein Paar von Team Neon steht in jeder Endzone, zwei Mittelfeldspieler von Team Neon und drei Verteidiger von Team Rot stehen in der Mittelzone. Das Paar am Ball will einen Pass durch die Reihe von Team Rot zu den Mittelfeldspielern spielen. Die drehen auf und geben den Ball an das Paar auf der anderen Seite weiter, und alles beginnt in die andere Richtung. Erobert Team Rot den Ball, kontert es auf ein Minitor.",
 "organisation": ["Aufbauen: Ein Feld von 29 mal 15 Metern. Links und rechts je eine Endzone von 7 Metern, dazwischen die Mittelzone. Hinter beiden Endzonen steht ein Minitor.",
  "Verteilen: In jeder Endzone ein Paar von Team Neon. In der Mittelzone zwei Mittelfeldspieler von Team Neon und drei Verteidiger von Team Rot.",
  "Ablauf: Zuerst darf niemand herauslaufen. Team Rot verschiebt in der Mittelzone und schließt die Lücken. Kommt der Pass zu einem Mittelfeldspieler durch, dreht er auf und spielt zum Paar auf der anderen Seite. Erobert Team Rot den Ball, spielt es drei gegen zwei auf ein Minitor.",
  "Wechsel: Nach zwei Minuten tauscht ein Paar mit den Verteidigern, damit jedes Paar einmal verteidigt. Für jedes Paar werden die Punkte gezählt."],
 "organisation_show": ORG,
 "coaching_points": ["Gute Pässe und die richtige Entscheidung, wann der Pass durch die Reihe geht", "Ohne Ball so bewegen, dass man anspielbar ist", "Schnell passen, damit die Verteidiger verschieben müssen und Lücken entstehen", "Den frei gewordenen Raum nutzen, wenn ein Verteidiger herausläuft"],
 "materials": ["2 Minitore", "Hütchen für Feld und Zonen", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Vier gegen drei mit Übergabe. Den Ball durch die Reihe von Team Rot spielen und auf die andere Seite bringen.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 19.6, 16.6)] + CB,
  "steps": [
   S("Ball laufen lassen", "Neon zwei spielt zu Neon drei. Gleichzeitig verschieben Rot sieben und Rot neun zur Ballseite.",
     ps("b1", [19.6, 44.6]), mv("r7", [36, 32], delay=0.2), mv("r9", [52, 38], delay=0.2)),
   S("Schnell zurück und durch", "Neon drei spielt schnell zurück zu Neon zwei. Oben ist jetzt eine Lücke, und Neon zwei spielt durch die Reihe zu Neon acht.",
     ps("b1", [19.6, 16.6]), ps("b1", [57.4, 16.6], after=True), mv("r7", [36, 26], after=True)),
   S("Übergabe zur anderen Seite", "Neon acht dreht auf und spielt zu Neon vier auf die andere Seite. Gleichzeitig drehen die Verteidiger um und verschieben nach rechts.",
     ps("b1", [80.4, 16.6]), mv("r7", [46, 24]), mv("r9", [56, 32]), mv("r10", [66, 40]))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "29 m"}, {"x1": 96, "y1": 10, "x2": 96, "y2": 50, "text": "15 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger darf aus der Mittelzone herauslaufen.", "Einer läuft heraus",
    "Jetzt darf ein Verteidiger von Team Rot herauslaufen und das Paar am Ball unter Druck setzen. Das Paar muss schneller entscheiden. Dafür entsteht in der Mittelzone eine Lücke, und ein Mittelfeldspieler bietet sich genau dort an.",
    sp(), [B("b1", 19.6, 16.6)] + CB,
    [S("Druck auf den Ball", "Rot sieben läuft heraus und greift Neon zwei an. Neon zwei spielt schnell zu Neon drei.",
       mv("r7", [26, 22]), ps("b1", [19.6, 44.6], delay=0.3)),
     S("In die Lücke", "Gleichzeitig läuft Neon sechs in die Lücke, die Rot sieben hinterlassen hat, und Neon drei spielt ihn an.",
       mv("n6", [36, 32]), ps("b1", [37.6, 32.6], delay=0.4)),
     S("Weiter nach vorn", "Neon sechs spielt zu Neon acht, und der gibt den Ball sofort an Neon vier auf der anderen Seite weiter.",
       ps("b1", [57.4, 16.6]), ps("b1", [80.4, 16.6], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Einer aus dem Paar gegenüber darf in die Mittelzone kommen.", "Pass auf die dritte Linie",
    "Ein Spieler aus dem Paar auf der anderen Seite darf jetzt in die Mittelzone kommen und hilft als zusätzliche Anspielstation. Das macht es leichter. Trotzdem sollen die Spieler den Kopf heben und schauen, ob der Ball sogar direkt bis zur dritten Linie, also bis zum Paar gegenüber, durchgeht.",
    sp(n6=(36, 44), r9=(48, 40)), [B("b1", 19.6, 44.6)] + CB,
    [S("Einer kommt entgegen", "Neon fünf kommt in die Mittelzone und bietet sich an. Gleichzeitig verschiebt Rot zehn zu ihm.",
       mv("n5", [68, 47]), mv("r10", [62, 42], delay=0.2)),
     S("Direkt auf die dritte Linie", "Neon drei hebt den Kopf, sieht die Lücke und spielt direkt durch zu Neon vier auf der anderen Seite.",
       ps("b1", [80.4, 16.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
