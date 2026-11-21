import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 49-P3: Eine der zwei gleichen Bahnen (15 x 30 Yards) gedreht: Start links, Tor rechts. Feld x 10-90, y 10-50.
T = P("T", "c", 50, 53.5, "T")
def sp(n1=(6, 39), tw=(86, 28)): return [P("n1", "a", *n1, "1"), P("n2", "a", 6, 55, "2"), P("k1", "t", *tw, "TW"), T]
cones = [C(15.1, 39.2), C(21.4, 39.2), C(27.4, 39.2), C(47, 20), C(60.8, 25.6, "neon", shape="stange")] + ecken(10, 10, 80, 40)
goals = [{"x": 90, "y": 25, "side": "right"}]
cb = [B("c2", 52.6, 54.1)]
slalom = [dr("n1", "b1", p, after=i > 0 or None) for i, p in enumerate([[15.1, 35.3], [21.4, 43], [27.4, 35.3], [32, 42]])]
u = {"title": "Slalom, Doppelpass, Abschluss", "code": "UE-100", "kind": "Übungsform",
 "focuses": ["Dribbling", "Torschuss", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 6, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Der Spieler dribbelt durch einen Hütchenslalom, spielt einen Doppelpass mit dem Trainer an der Seite, nimmt den Ball gut an und dribbelt mit Tempo auf einen Dummy zu. Kurz davor legt er sich den Ball zur Seite und schließt eins gegen eins gegen den Torwart ab. Zwei gleiche Bahnen laufen gleichzeitig in entgegengesetzte Richtungen, nach dem Abschluss stellt sich jeder auf der anderen Seite an.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, längs in zwei Bahnen geteilt. In jeder Bahn drei Hütchen als Slalom, ein Dummy und am Ende ein Tor mit Torwart. Die Bahnen laufen in entgegengesetzte Richtungen.",
  "Verteilen: An jedem Start eine Schlange mit Bällen. Neben jeder Bahn steht ein Trainer oder ein Spieler für den Doppelpass.",
  "Ablauf: Mit kleinen Kontakten durch den Slalom dribbeln, Doppelpass mit dem Trainer, gut annehmen, mit Tempo auf den Dummy zu, den Ball zur Seite legen und abschließen. Jedes Tor gibt einen Punkt.",
  "Wechsel: Nach dem Abschluss stellt sich der Spieler auf der anderen Seite an. Für mehr Spannung Punkte zählen und auch den schwächeren Fuß benutzen lassen."],
 "organisation_show": ORG,
 "coaching_points": ["Mit kleinen Kontakten dribbeln, Innen- und Außenseite benutzen", "Genau passen und den Rückpass gut annehmen", "Mit Tempo auf den Dummy zudribbeln", "Sauber abschließen, am besten flach in die Ecke"],
 "materials": ["2 Tore", "8 Hütchen", "2 Dummys", "Viele Bälle"],
 "access": "frei", "hidden": True,
 "say_intro": "Slalom, Doppelpass, Abschluss. Durch die Hütchen, ein Doppelpass mit dem Trainer und dann eins gegen eins gegen den Torwart.",
 "board": {"lines": [rect(10, 10, 80, 40)], "cones": cones, "goals": goals, "players": sp(), "balls": [B("b1", 7.6, 39.6)] + cb,
  "steps": [
   S("Durch den Slalom", "Spieler eins dribbelt mit kleinen Kontakten durch die Hütchen.", *slalom),
   S("Doppelpass mit dem Trainer", "Er passt zum Trainer an der Seite, startet sofort nach vorn und bekommt den Ball zurück.",
     ps("b1", [48.4, 52.4]), mv("n1", [42, 25], delay=0.2), ps("b1", [43.6, 25.6], after=True)),
   S("Auf den Dummy zu", "Spieler eins nimmt den Ball gut an, dribbelt mit Tempo auf den Dummy zu und legt ihn sich kurz davor zur Seite.",
     dr("n1", "b1", [55, 26]), dr("n1", "b1", [59, 33], after=True), dr("n1", "b1", [64, 35], after=True)),
   S("Abschluss: Punkt", "Spieler eins schießt flach ins Eck, und das gibt einen Punkt für Spieler eins.", ps("b1", [90, 22]))],
  "dims": [{"x1": 10, "y1": 58.6, "x2": 90, "y2": 58.6, "text": "27 m"}, {"x1": 96, "y1": 10, "x2": 96, "y2": 50, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Am Dummy den Ball schnell zu beiden Seiten verlegen.", "Schnell zur Seite legen",
    "Kurz vor dem Dummy entscheidet eine kurze, schnelle Bewegung. Den Ball blitzschnell auf eine Seite legen, und zwar mal links, mal rechts. So entsteht Platz und ein guter Winkel zum Tor.",
    sp((50, 26), (86, 25)), [B("b1", 51.6, 26.6)] + cb,
    [S("Auf den Dummy zu", "Spieler eins dribbelt mit Tempo direkt auf den Dummy zu.", dr("n1", "b1", [55, 26])),
     S("Kurz und schnell zur Seite", "Kurz davor legt er den Ball blitzschnell auf die andere Seite und ist am Dummy vorbei.",
       dr("n1", "b1", [59, 18]), dr("n1", "b1", [66, 17], after=True)),
     S("Abschluss: Punkt", "Er schießt sofort, und das gibt einen Punkt für Spieler eins.", ps("b1", [90, 21]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Vor dem Schuss den Kopf heben und auf den Torwart schauen.", "Kopf hoch, in die Ecke",
    "Wer vor dem Abschluss kurz den Kopf hebt, sieht, wo der Torwart steht. Dann in die Ecke schießen, die er nicht abdeckt. Genau statt hart, so fallen die meisten Tore.",
    sp((64, 36), (86, 28)), [B("b1", 65.6, 36.6)] + cb,
    [S("Kopf hoch", "Spieler eins dribbelt aufs Tor zu und hebt den Kopf. Der Torwart steht zu weit in seiner Ecke.",
       dr("n1", "b1", [69, 34]), mv("k1", [86, 29], delay=0.2)),
     S("Ab in die freie Ecke", "Spieler eins schießt flach in die freie Ecke, und das gibt einen Punkt für Spieler eins.", ps("b1", [90, 21.5]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
