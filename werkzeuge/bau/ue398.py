import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 51-P4 (U15-U17, Woche 35 Phase 3): Passing Combinations CDM-CM-FB (PDF: Build Up Combinations (CDM-CM-FB), Technical).
# 25 x 20 Yards = 23 x 18 m (gerundet 18 x 25 m). Feld wie im PDF quer: x 16-80, y 5-55 (Verhältnis 1,25, kein langes Feld).
# Ein Team (Pink -> Team Neon), Nummern wie im PDF (5-11). Sechs Dummys als Stangen. Ein Trainer statt zwei: Er steht links
# neben Spieler fünf (dort startet die Gegenrichtung, in der Steigerung spielt er nach dem Abschluss den nächsten Ball ein).
# Spieler neun startet mit eigenem Ball. Spieler neun etwas tiefer als im PDF (stand im PDF direkt unter Spieler sechs, 3D-Abstand).
# Rollen nach Ton: Spieler elf = Sechser (dreht auf), Spieler sieben = Achter (legt ab), Spieler acht = Außenverteidiger
# (löst sich von seiner Stange, bekommt die Ablage und spielt durch auf Spieler fünf, läuft dann zum Start).
# Fassung 1 = PDF Key Coaching Point (Weg gehen und zeigen, „go and show“; Ton: Doppelbewegung, offen annehmen auf dem hinteren Fuß).
# Fassung 2 = PDF Progression (zwei Minitore; Prallpass von Spieler fünf, Abschluss des Außenverteidigers, Trainer spielt nach).
# Sichtkegel: Kein Scannen im Original (Text, Ton und Video geprüft); Video „open body“, Ton „body shape … receive on the back
# foot“: Annehmen und Aufdrehen des Sechsers mit bl(von=...) und drehen() wie in ue300.py.
T = P("T", "c", 8, 42, "T")
ERSATZ = [B("s1", 8.6, 45.8), B("s2", 6, 46.5)]
POS = {"n8": (59.2, 17), "n7": (35.3, 24.9), "n6": (78, 24), "n9": (77, 41), "n11": (59.6, 38), "n5": (18.9, 36), "n10": (29.4, 46.1)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
DUMMYS = [C(56.3, 17.3, shape="stange"), C(32.7, 25.7, shape="stange"), C(73.5, 24.5, shape="stange"),
          C(56.3, 39.5, shape="stange"), C(21.7, 36, shape="stange"), C(32.7, 46, shape="stange")]
LINES = [rect(16, 5, 64, 50)]
TORE = [{"x": 16, "y": 13, "side": "left"}, {"x": 80, "y": 48.5, "side": "right"}]
DIMS = dims(16, 80, 5, 55, "25 m", "18 m", rx=90)
N9, N11, N7 = [77, 41], [62.5, 39.5], [35.3, 24.9]
AB = [46.3, 15.6]  # hier bekommt Spieler acht die Ablage
def acht_kommt(delay=None):
    return [mv("n8", [67, 15.5], delay=delay), mv("n8", [56, 11.5], after=True), mv("n8", AB, after=True)]

u = {"title": "Aufbaumuster über den Sechser", "code": "UE-398", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 7, "players_max": 9,
 "field_size": "18 x 25 m",
 "description": "Ein festes Passmuster zwischen sechs Dummys. Der Sechser löst sich von seiner Stange, nimmt offen an, dreht auf und spielt durch zum Achter. Der legt ab für den Außenverteidiger, der von seiner Stange kommt und auf die andere Seite durchspielt. Von dort läuft das Muster sofort in die Gegenrichtung.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern mit sechs Dummys, wie im Bild verteilt.",
  "Verteilen: Sieben Spieler. Sechs stehen an ihren Dummys, einer startet mit Ball außen. Der Trainer steht mit Ersatzbällen auf der anderen Seite am Rand.",
  "Ablauf: Pass nach innen zum Sechser, der dreht auf und spielt durch zum Achter. Der Achter legt ab für den Außenverteidiger, der von seiner Stange kommt. Der spielt durch auf die andere Seite.",
  "Wechsel: Wer den Ball dort bekommt, startet sofort in die Gegenrichtung. Der Außenverteidiger läuft nach seinem Pass zum Start. Nach ein paar Runden tauschen alle die Positionen."],
 "organisation_show": ORG,
 "coaching_points": ["Scharf passen, in den richtigen Fuß", "Erst weg von der Stange, dann zeigen", "Offen annehmen und mit dem ersten Kontakt aufdrehen", "Wenn es geht, direkt spielen"],
 "materials": ["6 Dummys", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbaumuster über den Sechser. Sechs Dummys, sieben Spieler, und der Ball läuft vom Sechser über den Achter zum Außenverteidiger. Danach geht es sofort in die andere Richtung.",
 "board": {"lines": LINES, "goals": [], "cones": DUMMYS, "players": sp(), "balls": [B("b1", 77.6, 41.6)] + ERSATZ,
  "steps": [
   S("Pass nach innen zum Sechser", "Spieler neun startet außen mit Ball. Spieler elf ist unser Sechser. Er kommt ein Stück von seiner Stange weg und schaut zum Ball. Dann kommt der flache Pass nach innen.",
     mv("n11", N11), bl("n11", N9, after=True), ps("b1", [63.1, 40.1], after=True)),
   S("Aufdrehen und durch zum Achter", "Spieler elf dreht mit dem ersten Kontakt auf und spielt durch zu Spieler sieben. Oben löst sich Spieler acht schon von seiner Stange.",
     bl("n11", N7, von=N9, dauer=1.3), drehen("n11", N7, gegen=True, delay=0.4), ps("b1", [35.9, 25.5], after=True), *acht_kommt(delay=0.3)),
   S("Ablage für den Außenverteidiger", "Spieler sieben ist der Achter. Er legt mit einem Kontakt ab, genau in den Lauf von Spieler acht. Gleichzeitig kommt Spieler fünf ein paar Schritte nach vorn.",
     ps("b1", [46.9, 16.2]), mv("n5", [19.5, 25], delay=0.4)),
   S("Durch auf die andere Seite", "Spieler acht spielt direkt durch zu Spieler fünf und läuft hinterher zum Start. Die Runde ist durch. Jetzt startet Spieler fünf mit diesem Ball sofort in die Gegenrichtung.",
     ps("b1", [20.1, 25.6]), mv("n8", [10.5, 20], delay=0.5))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst weg, dann zeigen.", "Erst weg, dann zeigen",
    "Wer an der Stange wartet, steht nicht still. Erst ein paar Schritte weg vom Ball, dann kurz und scharf heraus. So schüttelt man im Spiel den Gegenspieler ab. Der Sechser steht dabei offen und nimmt den Ball mit dem hinteren Fuß an.",
    sp(), [B("b1", 77.6, 41.6)] + ERSATZ,
    [S("Erst weg, dann scharf heraus", "Spieler elf geht erst ein paar Schritte weg vom Ball. Dann kommt er scharf heraus und zeigt sich. Jetzt erst spielt Spieler neun.",
       mv("n11", [57, 44.5]), mv("n11", N11, after=True), bl("n11", N9, after=True), ps("b1", [63.1, 40.1], after=True)),
     S("Hinterer Fuß, erster Kontakt nach vorn", "Er steht offen und nimmt mit dem hinteren Fuß an. Der erste Kontakt geht schon nach vorn, mit dem zweiten spielt er durch zu Spieler sieben.",
       bl("n11", N7, von=N9, dauer=1.3), drehen("n11", N7, gegen=True, delay=0.4), ps("b1", [35.9, 25.5], after=True)),
     S("Auch Spieler acht täuscht an", "Spieler acht macht es genauso. Erst weg von Spieler sieben, dann im Bogen zurück in den freien Raum. Da kommt die Ablage hin.",
       *acht_kommt(), ps("b1", [46.9, 16.2], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Zwei Minitore zum Abschluss.", "Mit Abschluss ins Minitor",
    "In zwei Ecken steht jetzt ein Minitor. Der Außenverteidiger spielt durch, bekommt den Ball von Spieler fünf prallen gelassen und schließt direkt ab. Sofort spielt der Trainer den nächsten Ball ein, und es geht auf das andere Minitor.",
    sp(n8=AB, n11=N11), [B("b1", 46.9, 16.2), B("b2", 8.6, 42.6)] + ERSATZ,
    [S("Durchspielen und weiterlaufen", "Spieler acht hat die Ablage bekommen. Er spielt durch zu Spieler fünf und läuft sofort weiter Richtung Minitor.",
       mv("n5", [19.5, 25]), ps("b1", [20.1, 25.6], delay=0.4), mv("n8", [29, 9], after=True)),
     S("Prallpass in den Lauf", "Spieler fünf lässt den Ball mit einem Kontakt prallen, genau in den Lauf von Spieler acht.",
       ps("b1", [29.6, 9.6])),
     S("Abschluss: Punkt", "Spieler acht schießt direkt ins Minitor, und das gibt einen Punkt für Spieler acht. Sofort spielt der Trainer den nächsten Ball zu Spieler fünf. Jetzt geht es auf das andere Minitor.",
       ps("b1", [16.4, 12.5]), ps("b2", [20.1, 25.6], after=True))], goals=TORE, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
