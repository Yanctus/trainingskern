import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 86-P6: 20 x 25 Yards, gedreht: Feld x 14-86, y 7-53, Tore links/rechts. Neon (Torwart 1) spielt nach rechts, Rot (Torwart 5) nach links.
T = P("T", "c", 8, 52, "T")
goals = [{"x": 14, "y": 30, "side": "left"}, {"x": 86, "y": 30, "side": "right"}]
def sp(**k):
    d = dict(n1=(17, 30), n2=(32.2, 19.7), n3=(58, 13.3), n4=(58.3, 35.3), r5=(83, 30), r6=(41.7, 23.5), r7=(67, 17), r8=(67, 40)); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
cb = [B("c1", 10.6, 52.6), B("c2", 6, 55)]
u = {"title": "Punkte statt Tore", "code": "UE-082", "kind": "Spielform",
 "focuses": ["Torschuss", "Zusammenspiel", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "23 x 18 m",
 "description": "Drei gegen drei mit Torwart auf zwei Tore. Jeder Feldspieler ist zu Beginn drei Punkte wert: Trifft er, bekommt seine Mannschaft drei Punkte. Danach ist er nur noch zwei Punkte wert, nach dem nächsten Tor einen Punkt, weniger als einen Punkt aber nie. Es gewinnt nicht die Mannschaft mit den meisten Toren, sondern die mit den meisten Punkten.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 18 Metern mit einem Tor an jedem Ende.",
  "Verteilen: Zwei Mannschaften mit je drei Feldspielern und einem Torwart. Der Trainer steht mit Bällen am Rand.",
  "Punkte: Jeder Feldspieler startet mit drei Punkten pro Tor. Nach jedem eigenen Tor ist er einen Punkt weniger wert, aber nie weniger als einen Punkt. Jeder merkt sich seinen Wert.",
  "Sieger: Nach der Spielzeit gewinnt die Mannschaft mit den meisten Punkten, nicht mit den meisten Toren."],
 "organisation_show": ORG,
 "coaching_points": ["Durch schnelles Zusammenspiel Chancen herausspielen", "Die Spieler mit vielen Punkten in Schussposition bringen", "Wissen, welcher Gegner gerade viele Punkte wert ist, und ihn eng decken", "Vor dem Tor eiskalt abschließen und viel miteinander sprechen"],
 "materials": ["2 Tore", "4 orange Hütchen", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Punkte statt Tore. Wer trifft, ist danach weniger wert, und am Ende zählt, wer mehr Punkte gesammelt hat.",
 "board": {"lines": [rect(14, 7, 72, 46)], "cones": ecken(14, 7, 72, 46), "goals": goals, "players": sp(), "balls": [B("b1", 33.8, 20.3)] + cb,
  "steps": [
   S("Zusammenspielen", "Spieler zwei spielt zu Spieler drei. Gleichzeitig startet Spieler vier vor dem Tor in den freien Raum.",
     ps("b1", [59.6, 13.9]), mv("n4", [69, 30], delay=0.4)),
   S("Pass in den Lauf", "Spieler drei spielt den Ball genau in den Lauf von Spieler vier.", ps("b1", [70.6, 30.6])),
   S("Abschluss: zwei Punkte", "Spieler vier hat schon einmal getroffen und ist nur noch zwei Punkte wert. Sein Tor gibt zwei Punkte für Neon, danach ist er nur noch einen Punkt wert.",
     ps("b1", [86, 34.5]))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "23 m"}, {"x1": 94, "y1": 7, "x2": 94, "y2": 53, "text": "18 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ein Spieler ist nie weniger als einen Punkt wert, also trotzdem schießen, wenn er frei ist.", "Ein Punkt ist besser als keiner",
    "Auch wer schon zweimal getroffen hat, ist noch einen Punkt wert. Steht er frei vor dem Tor, soll er schießen. Ein sicherer Punkt ist besser als ein riskanter Pass. Trotzdem immer überlegen, ob ein wertvoller Mitspieler genauso gut frei steht.",
    sp(n2=(36, 18), n3=(56, 14), n4=(64, 36), r6=(46, 28), r7=(66, 18), r8=(55.5, 44)), [B("b1", 57.6, 14.6)] + cb,
    [S("Frei vor dem Tor", "Spieler vier ist nur noch einen Punkt wert, steht aber frei. Spieler drei spielt ihn an.", mv("n4", [70, 40]), ps("b1", [71.6, 40.6], delay=0.3)),
     S("Trotzdem abschließen", "Spieler vier schießt sofort, und das gibt einen Punkt für Neon.", ps("b1", [86, 34.5]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Kopf hoch und den Mitspieler mit den meisten Punkten suchen.", "Den wertvollsten Spieler suchen",
    "Wer den Ball hat, hebt den Kopf und schaut, wer frei ist und wie viele Punkte er wert ist. Stehen zwei Mitspieler frei, bekommt der mit mehr Punkten den Ball. So holt die Mannschaft aus jeder Chance das Meiste heraus.",
    sp(n2=(50, 20), n3=(64, 12), n4=(62, 32), r6=(40, 30), r7=(73, 22), r8=(52, 44)), [B("b1", 65.6, 12.6)] + cb,
    [S("Kopf hoch", "Spieler sieben kommt auf Spieler drei zu. Spieler drei hebt den Kopf: Spieler zwei ist einen Punkt wert, Spieler vier ist noch drei Punkte wert.", mv("r7", [70, 16])),
     S("Zum wertvollsten Spieler", "Spieler drei spielt zu Spieler vier, dem Spieler mit drei Punkten.", ps("b1", [63.6, 32.6])),
     S("Abschluss: drei Punkte", "Spieler vier trifft, und das gibt drei Punkte für Neon.", ps("b1", [86, 34.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
