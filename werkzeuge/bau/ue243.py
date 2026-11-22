import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 10-P13 (U12-U14, Woche 40 Phase 5): Defensive Pressure (Back 3). 30 x 35 Yards = Feld x 28.9-71.1, y 5-55 (27 x 32 m), drei Zonen
# (10, 15 und 10 Yards, gestrichelt bei y 19.3 und 40.7), oben ein Jugendtor mit Torwart, unten in den Ecken der Mittelzone zwei
# Minitore (im PDF schräg gestellt, hier gerade mit Öffnung nach oben). Ausrichtung wie im PDF (Tor oben).
# Dunkel (Dreierkette 2, 6, 4) + grüner Torwart -> Team Neon (n1 TW, Nummern wie im PDF); Pink (Angreifer) -> Team Rot: 8 und 10
# wie im PDF, der Anspieler 4 heißt hier 9 (im PDF doppelt mit Dunkel 4), der neue Anspieler der Steigerung (im PDF Pink 6) heißt 7.
# Wartende (Dunkel 5, Pink 6, 7, 11) nur im Text. Ein Trainer statt zwei (im PDF rechts oben und links unten), er steht links
# unten mit Bällen. Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video (6 fängt ab, passt zu 4, 4 trifft rechts).
# Sichtkegel: Text "Recognise when to apply a high press (pressing triggers)", Ton "Recognise when to drop if the player on the
# ball has time to play in behind" -> Grundform: Spieler zwei schaut zum Ball, bevor er presst; Coaching-Punkt: Spieler sechs
# schaut zum Anspieler mit Zeit am Ball, bevor die Kette zurückgeht (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 20, 47, "T")
POS = {"n1": (50, 6.5), "n2": (38, 18), "n6": (50, 22), "n4": (62, 18),
       "r8": (36.5, 34.5), "r10": (63.5, 34.5), "r9": (48, 48)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 23.6, 50.5), B("s2", 20, 50.5)]
LINES = [rect(28.9, 5, 42.2, 50), line(28.9, 19.3, 71.1, 19.3), line(28.9, 40.7, 71.1, 40.7)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 33, "y": 40.7, "side": "bottom"}, {"x": 67, "y": 40.7, "side": "bottom"}]

u = {"title": "Pressen als Dreierkette", "code": "UE-243", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 32 m",
 "description": "Drei Verteidiger und ein Torwart verteidigen das große Tor gegen zwei Angreifer in der Mitte und einen Anspieler von hinten. Die Dreierkette bleibt eng zusammen: Einer presst, die anderen zwei schieben mit und sichern ab. Erobert die Kette den Ball, schießt sie auf eines der zwei Minitore. Nach zwei Angriffen wird gewechselt.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 32 Metern in drei Zonen: oben und unten je neun Meter, in der Mitte vierzehn Meter. Oben ein Jugendtor, unten in den Ecken der Mittelzone zwei Minitore.",
  "Verteilen: Team Neon mit Torwart und drei Verteidigern in der oberen Zone. Zwei Angreifer von Team Rot in der Mitte, ein Anspieler in der unteren Zone. Die anderen warten neben dem Feld. Der Trainer steht links unten mit Bällen.",
  "Ablauf: Der Anspieler passt in die Mitte, und drei gegen zwei geht es los. Die Angreifer dürfen den Anspieler höchstens zweimal nutzen. Team Neon presst, schiebt und sichert ab.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Rot. Ein Treffer ins Minitor gibt einen Punkt für Team Neon. Nach zwei Angriffen wechseln ein Verteidiger und alle drei Angreifer."],
 "organisation_show": ORG,
 "coaching_points": ["Eng zusammenbleiben und die Angreifer einengen", "Viel reden beim Pressen und Absichern", "Schnell zur Seite schieben und Lücken schließen", "Erkennen, wann man presst und wann man zurückgeht"],
 "materials": ["1 Jugendtor", "2 Minitore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pressen als Dreierkette. Drei Verteidiger bleiben eng zusammen und erobern den Ball gegen die Angreifer.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 48.6, 48.6)] + ERSATZ,
  "steps": [
   S("Pass in die Mitte", "Spieler neun passt aus der unteren Zone zu Spieler acht. Jetzt geht es drei gegen zwei los.",
     ps("b1", [37.1, 35.1])),
   S("Einer presst", "Spieler zwei sieht den Ball bei Spieler acht und presst ihn. Gleichzeitig schieben Spieler sechs und Spieler vier eng zu ihm und sichern ab. Spieler zehn läuft zur Mitte.",
     bl("n2", [37, 33]), mv("n2", [37, 28], after=True),
     mv("n6", [46, 24], delay=1.0), mv("n4", [56, 21], delay=1.0), mv("r10", [57, 28.5], delay=1.0)),
   S("Abgefangen", "Spieler acht will zu Spieler zehn passen. Spieler sechs geht dazwischen und fängt den Ball ab.",
     mv("n6", [48, 32.5]), ps("b1", [48.6, 33.1], delay=0.3)),
   S("Minitor: Punkt", "Spieler vier läuft nach rechts unten, Spieler sechs passt zu ihm. Spieler vier schießt ins rechte Minitor, und das gibt einen Punkt für Team Neon. Nach zwei Angriffen wechseln ein Verteidiger und alle drei Angreifer.",
     mv("n4", [66, 33]), ps("b1", [66.6, 33.6], after=True), ps("b1", [67, 40.4], after=True))],
  "dims": dims(28.9, 71.1, 5, 55, "27 m", "32 m", rx=80)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ball zurück heißt vorrücken, Zeit am Ball heißt zurückgehen.", "Vorrücken oder zurückgehen",
    "Spielen die Angreifer den Ball zurück, rücken alle drei Verteidiger zusammen nach vorn und machen das Feld eng. Hat der Spieler am Ball aber Zeit und kann hinter die Kette spielen, gehen alle drei ein paar Schritte zurück. In die obere Zone dürfen sie dabei nicht mehr.",
    sp(), [B("b1", 37.1, 35.1)] + ERSATZ,
    [S("Ball zurück, vorrücken", "Spieler acht spielt den Ball zurück zu Spieler neun. Sofort rücken alle drei Verteidiger gleichzeitig nach vorn und machen das Feld eng.",
       ps("b1", [48.6, 48.6]), mv("n2", [39, 25], delay=0.3), mv("n6", [50, 28.5], delay=0.3), mv("n4", [61, 25], delay=0.3)),
     S("Zeit am Ball, zurück", "Spieler neun hat viel Zeit am Ball. Spieler sechs sieht das und ruft: Zurück! Alle drei gehen gleichzeitig ein paar Schritte zurück, damit kein Ball hinter sie fliegt.",
       bl("n6", [48.5, 46]), mv("n2", [38, 21], after=True), mv("n6", [50, 23.5], delay=1.0), mv("n4", [62, 21], delay=1.0))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein dritter Angreifer kommt in die Mitte.", "Drei gegen drei",
    "Ein dritter Angreifer kommt in die Mittelzone, und unten hilft ein neuer Anspieler. Jetzt spielen drei gegen drei. Die Kette muss noch enger stehen, und der Torwart passt auf Bälle hinter die Kette auf.",
    sp(r8=(32, 34.5), r9=(50, 38), r10=(68, 34.5), r7=(41, 49)), [B("b1", 41.6, 49.6)] + ERSATZ,
    [S("Drei gegen drei", "Spieler sieben spielt von unten zu Spieler neun in der Mitte. Spieler sechs presst ihn. Gleichzeitig schieben Spieler zwei und Spieler vier eng zur Mitte.",
       ps("b1", [50.6, 38.6]), mv("n6", [54, 31], delay=0.3), mv("n2", [41, 21], delay=0.3), mv("n4", [59, 21], delay=0.3)),
     S("Torwart räumt ab", "Spieler neun spielt steil hinter die Kette, Spieler acht läuft hinterher. Der Torwart ist schon herausgekommen und fängt den Ball ab. Jetzt hat Team Neon den Ball.",
       mv("r8", [37, 14]), mv("n1", [42, 11.5]), ps("b1", [42.6, 12.1], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
