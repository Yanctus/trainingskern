import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 92-P6: 40 x 20 Yards, gedreht (Spiel von links nach rechts): Feld x 8-92, y 8-52, vier Zonen je 21 breit, Tore links und rechts.
T = P("T", "c", 3, 50, "T")
CB = [B("c1", 5.5, 50.6), B("c2", 2, 53.5)]
X0 = (8, 29, 50, 71)
POS = {}
for z, x0 in enumerate(X0):
    POS[f"n{2 + 2 * z}"] = (x0 + 6, 15); POS[f"n{3 + 2 * z}"] = (x0 + 6, 45); POS[f"r{10 + z}"] = (x0 + 15, 30)
POS["r13"] = (86, 40)
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(8, 8, 84, 44)] + [line(x, 8, x, 52) for x in (29, 50, 71)]
TORE = [{"x": 8, "y": 30, "side": "left"}, {"x": 92, "y": 30, "side": "right"}]
u = {"title": "Zwei gegen eins in vier Zonen", "code": "UE-109", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "37 x 18 m",
 "description": "Das Feld ist in vier Zonen geteilt, an beiden Enden steht ein Tor. In jeder Zone spielen zwei Spieler von Team Neon gegen einen Verteidiger von Team Rot. Team Neon spielt sich von Zone zu Zone nach vorn, und in jeder Zone müssen beide Angreifer den Ball berührt haben. Erobert Team Rot den Ball, kontert es auf eines der beiden Tore.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 18 Metern, in vier gleich große Zonen geteilt. Links und rechts steht je ein Tor.",
  "Verteilen: In jeder Zone zwei Spieler von Team Neon und ein Verteidiger von Team Rot. Alle bleiben in ihrer Zone. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Team Neon baut von links nach rechts auf. In jeder Zone berühren beide Angreifer den Ball, bevor er in die nächste Zone geht, und vor dem Tor braucht es mindestens sechs Pässe. Zuerst darf nur nach vorn gepasst werden.",
  "Wechsel: Erobert Team Rot den Ball, darf ein zweiter Verteidiger in die Zone kommen und beide kontern auf ein Tor. Trifft Team Rot, tauscht es mit vier Angreifern. Jedes Tor gibt einen Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Gute Passwinkel für den Mitspieler anbieten", "Schnelle Kombinationen, um nach vorn zu kommen", "Mit einem Kontakt genau abschließen", "Den Pass mit dem richtigen Tempo und genau spielen und die Unterstützung richtig timen"],
 "materials": ["2 Tore", "Hütchen für Feld und Zonen", "Mehrere Bälle beim Trainer", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Zwei gegen eins in vier Zonen. In jeder Zone die Überzahl nutzen und den Ball von links nach rechts bis ins Tor spielen.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 15.6, 15.6)] + CB,
  "steps": [
   S("Zone eins", "Neon drei läuft nach vorn, und Neon zwei spielt ihn an. Beide haben den Ball berührt, also spielt Neon drei weiter in die zweite Zone zu Neon fünf.",
     mv("n3", [22, 47]), ps("b1", [23.6, 47.6], delay=0.4), ps("b1", [33.4, 45.6], after=True)),
   S("Zone zwei", "Neon vier löst sich nach vorn, Neon fünf spielt zu ihm. Neon vier spielt weiter in die dritte Zone zu Neon sechs.",
     mv("n4", [40, 14]), ps("b1", [41.6, 14.6], delay=0.4), ps("b1", [54.4, 15.6], after=True)),
   S("Zone drei", "Neon sieben startet nach vorn und bekommt den Ball von Neon sechs. Dann spielt er in die letzte Zone zu Neon neun.",
     mv("n7", [62, 46]), ps("b1", [63.6, 46.6], delay=0.4), ps("b1", [75.4, 45.6], after=True)),
   S("Abschluss mit einem Kontakt", "Rot dreizehn greift Neon neun an. Neon neun spielt zu Neon acht, der in die Mitte läuft und direkt ins Tor schießt. Das gibt einen Punkt für Team Neon.",
     mv("r13", [83, 41]), mv("n8", [84, 21]), ps("b1", [85.6, 21.6], delay=0.5), ps("b1", [91.5, 29], after=True))],
  "dims": [{"x1": 8, "y1": 58.6, "x2": 92, "y2": 58.6, "text": "37 m"}, {"x1": 97, "y1": 8, "x2": 97, "y2": 52, "text": "18 m"}]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Unter Druck darf der Ball zurückgespielt werden.", "Zurückspielen erlaubt",
    "Jetzt dürfen die Angreifer unter Druck auch nach hinten in die vorige Zone spielen. Das nimmt den Druck heraus, und der Mitspieler muss sich so anbieten, dass der Ball sofort wieder nach vorn kommt. So lernen die Spieler Ruhe am Ball, Übersicht und gute Entscheidungen.",
    sp(), [B("b1", 57.6, 15.6)] + CB,
    [S("Zurück unter Druck", "Rot zwölf greift Neon sechs an. Neon sechs spielt zurück zu Neon vier in die zweite Zone.",
       mv("r12", [61, 21]), ps("b1", [36.6, 15.6], delay=0.4)),
     S("Und wieder nach vorn", "Gleichzeitig dreht Neon sechs weg in den freien Raum, und Neon vier spielt ihm den Ball sofort wieder in den Lauf.",
       mv("n6", [66, 11]), ps("b1", [64.4, 11.6], delay=0.3))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei Verteidiger dürfen in eine Zone.", "Zwei Verteidiger in einer Zone",
    "Die Verteidiger dürfen jetzt zu zweit in einer Zone angreifen. So entsteht dort ein zwei gegen zwei, und die Angreifer stehen mehr unter Druck. Dafür ist hinter den Verteidigern eine Zone frei. Die Angreifer schauen deshalb nach einer Lücke und spielen schnell nach vorn.",
    sp(), [B("b1", 36.6, 45.6)] + CB,
    [S("Zwei Verteidiger kommen", "Gleichzeitig greifen Rot elf und Rot zwölf Neon fünf an. In der dritten Zone steht jetzt kein Verteidiger mehr.",
       mv("r11", [38, 36]), mv("r12", [47, 46], delay=0.2)),
     S("Raum hinter den Verteidigern", "Neon fünf spielt an beiden vorbei zu Neon sechs, der frei in der dritten Zone steht und nach vorn dribbelt.",
       ps("b1", [54.4, 15.6]), dr("n6", "b1", [66, 20], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
