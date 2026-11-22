import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 78-P12 (U12-U14, Woche 42 Phase 6): Develop the Defensive Unit (Back 4). 50 Yards breit, ca. 33 tief = Feld x 10-90, y 4-56
# (46 x 30 m). Gespiegelt: im PDF liegt das große Tor unten, hier oben. Strafraum und Torraum nach der PDF-Skizze, Halbkreis und die
# schrägen Linien um den Strafraum weggelassen. Drei Minitore unten (links, Mitte, rechts; im PDF schräg, hier gerade mit Öffnung
# ins Feld). Rot (Viererkette 3, 5, 4, 2) + grüner Torwart -> Team Neon (n1 TW), Blau (Angreifer 7, 9, 10, 11) -> Team Rot,
# Nummern wie im PDF. Gelb (drittes Team mit Bällen an den Seiten, im PDF 2, 8, 6, 3) -> vier neutrale Springer F: sie spielen
# den Ball ein und in der Steigerung für das Team am Ball mit (PDF-Progression 1). Angreifer und Springer für den 3D-Abstand
# etwas auseinandergerückt. PDF-Progression 2 (Abseitslinie, zehn Pässe gleich ein Treffer) nicht gebaut.
# Kein Dubletten-Fall: UE-166 (Trainer spielt ein, zwei Minitore), UE-177 (Ballgewinn zum Trainer), UE-208 (zwei Ketten in Zonen),
# UE-212 (Kette schützt drei Minitore, kein großes Tor) und UE-242 (kleines Feld zwischen zwei Springern) sind anders organisiert.
# Sichtkegel aus dem Video ("Awareness to distribute quickly", Markierung am freien Springer in der Progression): in der Steigerung
# schaut der Torwart nach dem Fangen zum freien Springer links, bevor er schnell abspielt. Im Video kein Kegel, nur ein Kreis.
T = P("T", "c", 46, 54, "T")
POS = {"n1": (50, 8.5), "n3": (28, 22), "n5": (41, 19), "n4": (59, 19), "n2": (71, 21),
       "r7": (24, 38), "r9": (50, 24.5), "r10": (58, 40.5), "r11": (76, 37),
       "f1": (13, 10), "f2": (33, 41), "f3": (67, 41), "f4": (87, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "TW" if i == "n1" else "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 49.6, 57.5), B("s2", 42.4, 57.5)]
def baelle(b1=(33.6, 41.6)):
    return [B("b1", *b1), B("b2", 13.6, 10.6), B("b3", 67.6, 41.6), B("b4", 87.6, 9.6)] + ERSATZ
LINES = [rect(10, 4, 80, 52), rect(25.2, 4, 49.6, 17.6), rect(37.4, 4, 25.2, 7.3)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "jugend"}, {"x": 16, "y": 42, "side": "bottom"}, {"x": 50, "y": 46, "side": "bottom"}, {"x": 84, "y": 42, "side": "bottom"}]

u = {"title": "Viererkette mit Torwart kontert", "code": "UE-250", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 13, "players_max": 13, "field_size": "46 x 30 m",
 "description": "Eine Viererkette mit Torwart verteidigt das große Tor gegen vier Angreifer. Der Trainer ruft einen Springer auf, und der spielt den Ball zu den Angreifern. Die Kette bleibt eng zusammen: Einer presst, die anderen sichern ab. Erobert die Kette den Ball, schaltet sie schnell um und spielt auf drei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 46 mal 30 Metern mit Strafraum und einem Jugendtor oben. Unten stehen drei Minitore: links, in der Mitte und rechts.",
  "Verteilen: Team Neon verteidigt mit vier Spielern und einem Torwart. Team Rot greift mit vier Spielern an. Vier Springer stehen mit Bällen an den Seiten. Der Trainer steht unten.",
  "Ablauf: Der Trainer ruft einen Springer auf. Der spielt den Ball sofort zu Team Rot, und vier gegen vier geht los. Team Neon presst, sichert ab und hält die Kette eng. Erobert Team Neon den Ball, spielt es auf die Minitore.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Rot, ein Treffer ins Minitor einen Punkt für Team Neon. Dann ruft der Trainer den nächsten Springer auf. Nach ein paar Runden wechselt das angreifende Team mit den Springern."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, die anderen sichern ab und schließen die Lücke", "Eng zusammenbleiben, damit kein Pass durch die Kette kommt", "Nach dem Ballgewinn schnell umschalten, sonst den Ball über Kette und Torwart laufen lassen", "Laut reden und schnell auf die Plätze, wenn ein neuer Springer aufgerufen wird"],
 "materials": ["1 Jugendtor", "3 Minitore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Viererkette mit Torwart kontert. Die Kette verteidigt das große Tor und kontert nach dem Ballgewinn auf drei Minitore.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": baelle(),
  "steps": [
   S("Zuruf und Zuspiel", "Der Trainer ruft einen Springer auf, hier den Springer links unten. Er spielt den Ball sofort zu Spieler zehn, und vier gegen vier geht los.",
     ps("b1", [58.6, 41.1])),
   S("Einer presst", "Spieler zehn spielt zu Spieler neun. Spieler vier presst ihn sofort. Spieler fünf, Spieler drei und Spieler zwei schieben ein und sichern ab.",
     ps("b1", [50.6, 25.1]), mv("n4", [54, 21], delay=0.3), mv("n5", [45, 16], delay=0.3), mv("n3", [34, 19], delay=0.3), mv("n2", [65, 18], delay=0.3)),
   S("Abgefangen", "Spieler neun will nach rechts zu Spieler elf passen. Spieler zwei liest den Pass und fängt ihn ab.",
     mv("n2", [66, 30]), ps("b1", [66.6, 30.6], delay=0.2)),
   S("Konter: Punkt", "Team Neon schaltet sofort um. Spieler vier startet, Spieler zwei spielt ihn an, und Spieler vier trifft ins mittlere Minitor. Das gibt einen Punkt für Team Neon. Dann ruft der Trainer den nächsten Springer auf.",
     mv("n4", [53, 36]), ps("b1", [53.6, 36.6], after=True), ps("b1", [50, 46.4], after=True))],
  "dims": dims(10, 90, 4, 56, "46 m", "30 m", rx=95)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball laufen lassen.", "Ball laufen lassen",
    "Nach dem Ballgewinn geht es schnell nach vorn. Ist vorn alles zu, spielt die Kette den Ball ruhig über den Torwart auf die andere Seite. Dort ist meist Platz, und dann geht es zum Minitor.",
    sp(), baelle(b1=(41.6, 19.6)),
    [S("Zurück zum Torwart", "Spieler fünf hat den Ball erobert. Spieler neun presst sofort, und vorn ist alles zu. Spieler fünf spielt ruhig zurück zum Torwart.",
       mv("r9", [46, 22]), ps("b1", [50.6, 9.1], delay=0.3)),
     S("Auf die andere Seite", "Der Torwart spielt weiter zu Spieler vier, und Spieler vier spielt zu Spieler zwei. Spieler zwei hat Platz und dribbelt nach vorn.",
       ps("b1", [59.6, 19.6]), ps("b1", [71.6, 21.6], after=True), dr("n2", "b1", [80, 30], after=True)),
     S("Ins Minitor: Punkt", "Spieler zwei schießt ins rechte Minitor. Das gibt einen Punkt für Team Neon.",
       ps("b1", [84, 42.4]))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Springer spielen mit.", "Springer spielen mit",
    "Jetzt spielen die Springer für das Team, das gerade den Ball hat. Fängt der Torwart den Ball, schaut er sofort, wo ein Springer frei ist, und spielt schnell zu ihm. So kommt Team Neon schnell nach vorn.",
    sp(), baelle(b1=(58.6, 41.1)),
    [S("Torwart fängt", "Spieler zehn schießt aufs Tor, aber der Torwart fängt den Ball. Spieler sieben läuft nach innen.",
       ps("b1", [50.6, 9.1]), mv("r7", [30, 28])),
     S("Umschauen", "Der Torwart schaut sofort, wo ein Springer frei ist. Der Springer links ist frei, und Spieler drei startet nach außen.",
       bl("n1", [39.8, 28]), mv("n3", [22, 32], after=True)),
     S("Über den Springer: Punkt", "Der Torwart spielt schnell zum Springer. Der Springer spielt jetzt für Team Neon und legt in den Lauf von Spieler drei. Spieler drei trifft ins linke Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [33.6, 41.6]), ps("b1", [22.6, 32.6], after=True), ps("b1", [16, 42.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
