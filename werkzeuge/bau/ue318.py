import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-49 (U15-U17, Woche 15): Technical Passing Circuit. 15 x 20 Yards = 14 x 18 m, Feld x 28-72, y 5-55. Ausrichtung wie im PDF
# (Start unten, Ball läuft über links nach oben und rechts außen zurück). Ein Team (Neon), im PDF ohne Nummern:
# Start 6, Wartender 7, am Dummy 10, links 8, oben 9, rechts 11. Ein Trainer statt zwei.
# Dummy (Mannequin) und die drei Stangen als shape "stange". Starthütchen etwas nach rechts unten gerückt (Passweg frei),
# Wartender Spieler sieben weiter rechts (3D-Abstand). Weiterrücken: Jeder läuft nach seiner Aktion eine Station weiter.
# Fassung 1 = PDF Key Coaching Point (außen offen annehmen, mit bl(von=...) und drehen()), Fassung 2 = PDF Progression
# (Lösen vom Dummy, Pass zur Spitze, Steilpass durch die Hütchengasse).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft); der Kegel in Fassung 1 gehört zum Annehmen und Aufdrehen.
T = P("T", "c", 12, 12, "T")
ERSATZ = [B("s1", 15.6, 15.5), B("s2", 12, 15.5)]
POS = {"n6": (46, 48), "n7": (57.5, 51), "n10": (53.5, 31), "n8": (31.5, 22), "n9": (46, 8.5), "n11": (69, 21)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
B7 = B("b2", 58.1, 51.6)
CONES = [C(49.5, 30, shape="stange", id="d"), C(36, 19, shape="stange", id="p1"), C(49.5, 11, shape="stange", id="p2"),
         C(64, 21, shape="stange", id="p3"), C(51, 49.5, id="h0")]
GASSE = [C(58.5, 29, "neon", id="g1"), C(67, 28, "neon", id="g2")]
LINES = [rect(28, 5, 44, 50)]
def zurueck(**k): return [dr("n11", "b1", [70.5, 28], **k), dr("n11", "b1", [47, 47.5], after=True)]

u = {"title": "Passzirkel um drei Stangen", "code": "UE-318", "kind": "Übungsform",
 "focuses": ["Passspiel", "Erwärmung", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 6, "players_max": 8,
 "field_size": "14 x 18 m",
 "description": "Ein Passzirkel zum Aufwärmen mit einem Dummy in der Mitte und drei Stangen. Der Ball läuft vom Start über den Dummy nach links, mit zwei Doppelpässen um die Stangen nach oben und rechts außen wieder raus. Der Letzte dribbelt mit Tempo zurück zum Start. Nach jeder Aktion rückt jeder eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. In der Mitte steht ein Dummy, links, oben und rechts je eine Stange. Unten markiert ein Hütchen den Start.",
  "Verteilen: Je ein Spieler steht am Dummy und an den drei Stangen. Die anderen stehen mit Ball am Start. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass mit dem Spieler am Dummy, dann raus nach links. Ablage nach innen und Doppelpass um die linke Stange. Weiter nach oben, Doppelpass um die mittlere Stange, Pass nach rechts außen. Der Spieler rechts dribbelt außen an der Stange vorbei zurück zum Start.",
  "Wechsel: Jeder rückt nach seiner Aktion eine Station weiter, vom Start zum Dummy, dann nach links, nach oben und nach rechts. Dribbelt der Letzte zurück, startet der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und mit Druck passen", "Außen offen stehen und mit Tempo rausgehen", "Doppelpass mit einem Kontakt, genau in den Lauf", "Nach dem Pass sofort nachrücken"],
 "materials": ["1 Dummy", "3 Stangen", "3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passzirkel um drei Stangen. Zum Aufwärmen läuft der Ball einmal durch alle Stationen, mit zwei Doppelpässen um die Stangen. Der Letzte dribbelt zurück, und jeder rückt eine Station weiter.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 46.6, 48.6), B7] + ERSATZ,
  "dims": dims(28, 72, 5, 55, "14 m", "18 m", rx=85),
  "steps": [
   S("Doppelpass am Dummy", "Spieler sechs startet unten. Er spielt flach zu Spieler zehn am Dummy, und der lässt den Ball direkt zurückprallen.",
     ps("b1", [54.1, 31.6]), ps("b1", [46.6, 48.6], after=True)),
   S("Raus nach links", "Jetzt geht der Ball nach links außen zu Spieler acht. Spieler zehn löst sich schon vom Dummy und kommt ihm entgegen.",
     ps("b1", [32.1, 22.6]), mv("n10", [53, 26], delay=0.3), mv("n10", [46, 23], after=True)),
   S("Doppelpass um die linke Stange", "Spieler acht legt nach innen ab und läuft außen an der Stange vorbei. Spieler zehn spielt ihm den Ball mit einem Kontakt in den Lauf. Unten rückt Spieler sechs zum Dummy nach.",
     ps("b1", [46.6, 23.6]), mv("n8", [31.5, 16], delay=0.2), mv("n8", [33.5, 13], after=True), ps("b1", [34.1, 13.6], delay=0.9),
     mv("n6", [53.5, 31], delay=0.4)),
   S("Doppelpass um die mittlere Stange", "Weiter nach oben zu Spieler neun. Der legt kurz zurück und dreht um die Stange nach rechts. Spieler acht ist nachgelaufen und spielt ihm den Ball wieder in den Lauf.",
     ps("b1", [46.6, 9.1]), mv("n8", [44, 16], delay=0.2), ps("b1", [44.6, 16.6], after=True),
     mv("n9", [52, 6.5], delay=0.9), mv("n9", [57, 12.5], after=True), ps("b1", [57.6, 13.1], delay=1.7), mv("n10", [31.5, 22], delay=0.5)),
   S("Rechts raus, mit Ball zurück", "Spieler neun spielt nach rechts außen. Spieler elf nimmt den Ball außen an der Stange mit und dribbelt mit Tempo zurück zum Start.",
     ps("b1", [69.6, 21.6]), *zurueck(after=True)),
   S("Weiterrücken, der Nächste startet", "Der Ball ist wieder am Start, die Runde ist durch. Spieler acht rückt nach oben, Spieler neun nach rechts. Und Spieler sieben ist schon dran. Er startet, sobald Spieler elf losdribbelt.",
     mv("n8", [46, 8.5]), mv("n9", [66, 15]), mv("n9", [69, 21], after=True), ps("b2", [54.1, 31.6], delay=0.3), ps("b2", [58.1, 51.6], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Außen offen annehmen und mit Tempo raus.", "Offen annehmen, Tempo raus",
    "Der Spieler rechts außen steht seitlich und schaut zum Ball. Er nimmt den Pass mit dem hinteren Fuß an. So dreht er in einer Bewegung auf und geht mit dem ersten Kontakt Richtung Start.",
    sp(n6=(53.5, 31), n10=(31.5, 22), n8=(44, 16), n9=(57, 12.5)), [B("b1", 57.6, 13.1), B7] + ERSATZ,
    [S("Seitlich stehen, Blick zum Ball", "Spieler elf steht seitlich an der Stange und schaut zu Spieler neun. Der Pass kommt flach auf seinen hinteren Fuß.",
       bl("n11", [57, 12.5]), ps("b1", [69.6, 21.6], after=True)),
     S("Aufdrehen und los", "Erst jetzt dreht er auf, der Blick geht Richtung Start. Der erste Kontakt führt außen an der Stange vorbei, dann zieht er das Tempo an bis zum Starthütchen.",
       bl("n11", [62, 37], von=[57, 12.5], dauer=1.3), drehen("n11", [62, 37], gegen=True, delay=0.4), *zurueck(after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Eine neue Passfolge, und am Ende geht der Ball steil durch die Gasse.", "Steilpass durch die Gasse",
    "Der Ball geht vom Start direkt nach links außen. Der Spieler am Dummy täuscht kurz an, löst sich und bekommt die Ablage in der Mitte. Er spielt hoch zur Spitze, und von dort kommt der Steilpass durch die Hütchengasse. Der Spieler rechts läuft in den Ball und dribbelt zum Start.",
    sp(), [B("b1", 46.6, 48.6), B7] + ERSATZ,
    [S("Nach außen, antäuschen, Ablage", "Spieler sechs spielt direkt nach links außen. Spieler zehn täuscht einen Schritt zum Ball an, geht dann weg vom Dummy nach vorn und bekommt die Ablage von Spieler acht.",
       ps("b1", [32.1, 22.6]), mv("n10", [53.5, 36], delay=0.2), mv("n10", [55, 28], after=True), mv("n10", [50, 22.5], after=True), ps("b1", [50.6, 23.1], delay=1.9)),
     S("Hoch zur Spitze", "Oben kommt Spieler neun um die Stange herum und zeigt sich. Spieler zehn spielt ihn flach an.",
       mv("n9", [52, 6.5]), mv("n9", [56.5, 12.5], after=True), ps("b1", [57.1, 13.1], delay=0.9)),
     S("Steil durch die Gasse", "Jetzt kommt der Steilpass genau zwischen den beiden Hütchen durch. Spieler elf startet rechts außen, läuft in den Ball und dribbelt zurück zum Start. Dann beginnt Spieler sieben.",
       mv("n11", [71, 29]), mv("n11", [66.5, 39.5], after=True), ps("b1", [67.1, 40.1], delay=0.4), dr("n11", "b1", [47, 47.5], after=True))],
    cones=CONES + GASSE)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
