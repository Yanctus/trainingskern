import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 54-P2 (U12-U14, Woche 17 Phase 3): Creating Angles to Receive. 10 x 15 Yards = Feld x 33.3-66.7, y 5-55 (9 x 14 m), zwei
# Stangen in einer Linie, oben und unten je ein Hütchen. Ausrichtung wie im PDF (Spiel nach oben). Vier Spieler, alle Team Neon:
# unten 4 (Start mit Ball), untere Stange 10, obere Stange 8, oben 6 (Nummern wie in der Grundform des PDF). In den Steigerungen
# hat das PDF andere Nummern; hier bleiben die Rollen gleich nummeriert (4 unten, 10 untere Stange, 8 obere Stange, 6 oben).
# Wertung im Original nicht genannt: ein sauber angekommener Ball beim Endspieler gibt einen Punkt für die Gruppe (ergänzt).
# Ein Trainer an der Seite mit Bällen (im PDF rechts). Mehr Spieler: mehrere Vierergruppen nebeneinander.
# Sichtkegel: Im Video ist bei „Check shoulders before receiving" ein Kegel von 10 nach oben zur Mitte eingezeichnet
# (auch Text: scan before receiving, Ton: check their shoulders). Eingebaut für 10 (vor der Annahme) und 8.
T = P("T", "c", 76, 30, "T")
POS = {"n6": (52, 5), "n8": (52.5, 21), "n10": (52, 38), "n4": (52, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 79.6, 33.5), B("s2", 76, 33.5)]
LINES = [rect(33.3, 5, 33.4, 50)]
CONES = [C(48.5, 19, shape="stange"), C(48.5, 36, shape="stange"), C(46.5, 5), C(46.5, 55)]

u = {"title": "Im Winkel anbieten", "code": "UE-180", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 4, "players_max": 12, "field_size": "9 x 14 m",
 "description": "Vier Spieler stehen in einer Linie, zwei davon an Stangen in der Mitte. Die beiden in der Mitte lösen sich gleichzeitig in entgegengesetzte Richtungen von ihrer Stange und bieten sich schräg an. So spielt der Ball über beide Mittelspieler bis zum Spieler am anderen Ende. Vor jeder Annahme schauen die Spieler über die Schulter und stellen sich halb offen hin.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 14 Metern. In der Mitte stehen zwei Stangen hintereinander, oben und unten je ein Hütchen.",
  "Verteilen: Vier Spieler von Team Neon, je einer an jedem Hütchen und an jeder Stange. Der Spieler unten hat den Ball. Bei mehr Spielern stehen mehrere Gruppen nebeneinander. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der untere Mittelspieler löst sich schräg von seiner Stange, der obere läuft gleichzeitig in die andere Richtung. Der Ball geht von unten über beide Mittelspieler nach oben. Dann startet der obere Spieler in die andere Richtung.",
  "Wertung und Wechsel: Kommt der Ball sauber beim Spieler am Ende an, gibt das einen Punkt für die Gruppe. Nach zwei Minuten tauschen die beiden in der Mitte mit den beiden außen."],
 "organisation_show": ORG,
 "coaching_points": ["Weg von der Stange und schräg anbieten", "Gegenbewegung: der eine geht nach rechts, der andere nach links", "Vor der Annahme über die Schulter schauen und halb offen stehen", "Feste, genaue Pässe in den Fuß, mit Tempo"],
 "materials": ["2 Stangen", "2 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Im Winkel anbieten. Die beiden Spieler in der Mitte laufen gleichzeitig in entgegengesetzte Richtungen und machen so den Passweg frei.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 52.6, 54.6)] + ERSATZ,
  "steps": [
   S("Gegenbewegung", "Neon zehn löst sich schräg nach rechts von seiner Stange. Gleichzeitig läuft Neon acht in die andere Richtung, nach links. Neon zehn schaut dabei über die Schulter nach oben.",
     mv("n10", [61, 32]), mv("n8", [39, 24]), bl("n10", [46, 22], after=True)),
   S("Pass in den Winkel", "Neon vier passt schräg zu Neon zehn. Neon zehn nimmt den Ball halb offen an.",
     ps("b1", [61.6, 32.6])),
   S("Pass in die Mitte", "Neon acht schaut kurz nach oben. Dann spielt Neon zehn den Ball quer in die Mitte zu Neon acht.",
     bl("n8", [50, 8]), ps("b1", [39.6, 24.6], after=True)),
   S("Durchspielen: Punkt", "Neon acht spielt durch zu Neon sechs. Der Ball ist sauber angekommen, und das gibt einen Punkt für die Gruppe. Jetzt startet Neon sechs den Ablauf in die andere Richtung, nach unten.",
     ps("b1", [52.6, 5.6]))],
  "dims": dims(33.3, 66.7, 5, 55, "9 m", "14 m", rx=71)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der erste Pass geht zum weiten Spieler.", "Pass zum weiten Spieler",
    "Neon vier passt jetzt gleich zum oberen Mittelspieler. Der legt den Ball ab zum unteren Mittelspieler, und der spielt durch zum Endspieler. Achtet auf das Timing, die Bewegung und genaue Pässe.",
    sp(), [B("b1", 52.6, 54.6)] + ERSATZ,
    [S("Gegenbewegung", "Neon acht löst sich nach rechts, Neon zehn gleichzeitig nach links. Neon acht schaut über die Schulter zu Neon zehn.",
       mv("n8", [61, 25]), mv("n10", [45, 41]), mv("n10", [40, 34], after=True), bl("n8", [45, 34], after=True)),
     S("Langer Pass", "Neon vier spielt den langen Pass zu Neon acht.",
       ps("b1", [61.6, 25.6])),
     S("Ablegen und durch: Punkt", "Neon acht legt direkt ab zu Neon zehn, und Neon zehn spielt durch zu Neon sechs. Das gibt einen Punkt für die Gruppe, und Neon sechs startet nach unten.",
       ps("b1", [40.6, 34.6]), ps("b1", [52.6, 5.6], after=True, bend=-3))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Doppelpass mit dem ersten Passgeber.", "Doppelpass zum Start",
    "Zu Beginn kommt ein Doppelpass dazu. Der untere Mittelspieler legt den Ball zurück zu Neon vier, der spielt zum oberen Mittelspieler. Der legt quer zum unteren Mittelspieler, und der spielt durch zum Endspieler. So gibt es mehr Pässe, und alle bleiben wach.",
    sp(), [B("b1", 52.6, 54.6)] + ERSATZ,
    [S("Anbieten", "Neon zehn löst sich nach rechts und schaut über die Schulter. Neon vier passt zu ihm.",
       mv("n10", [61, 40]), bl("n10", [50, 24], after=True), ps("b1", [61.6, 40.6], after=True)),
     S("Doppelpass", "Neon vier läuft schräg nach vorn, und Neon zehn legt den Ball zurück.",
       mv("n4", [45, 47]), ps("b1", [45.6, 47.6], after=True)),
     S("Pass zur Stange", "Neon acht löst sich nach links und bekommt den Pass von Neon vier. Gleichzeitig läuft Neon zehn rechts nach oben.",
       mv("n8", [39, 24]), mv("n10", [60, 28]), ps("b1", [39.6, 24.6], after=True)),
     S("Quer und durch: Punkt", "Neon acht legt quer zu Neon zehn, und der spielt durch zu Neon sechs. Das gibt einen Punkt für die Gruppe, und Neon sechs startet nach unten.",
       ps("b1", [60.6, 28.6]), ps("b1", [52.6, 5.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
