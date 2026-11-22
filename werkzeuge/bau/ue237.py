import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-34 (U12-U14, Woche 38 Phase 4): Pass and Press Activation. 15 x 15 Yards = Feld x 25-75, y 5-55 (14 x 14 m),
# kleines Viereck 4 Yards (x 43.5-56.5, y 23.5-36.5). Eine Vierergruppe (Gelb im Video -> Neon 10, 9, 8, 7), Stationen:
# oben rechts (Start mit Ball), oben, unten, rechts. Ablauf wie im Video ab 0:04: Pass nach oben und hinterher, Pass durchs
# Viereck und pressen, Ballannahme nach außen und Pass quer, Doppelpass mit dem Spieler in der Mitte, Neustart.
# Steigerung (Progression): größeres Viereck (7 Yards statt 4) und Richtung gewechselt, gespiegelt (Start oben links).
# Sichtkegel aus dem Ton ("always stay aware of the press"): Spieler acht schaut vor der Annahme zum pressenden Spieler.
# Im Video kein Kegel eingezeichnet (nur ein Kreis für die Körperstellung).
T = P("T", "c", 15, 10, "T")
POS = {"n10": (62, 16), "n9": (50, 12), "n8": (50, 48), "n7": (72, 33)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 16.6, 13.5), B("s2", 13, 13.5)]
LINES = [rect(25, 5, 50, 50)]
CONES = ecken(43.5, 23.5, 13, 13)
POS2 = {"n7": (35, 10), "n10": (50, 8), "n9": (50, 52), "n8": (28, 31)}
CONES2 = [dict(c, id="h%d" % (i + 1)) for i, c in enumerate(ecken(38.5, 18.5, 23, 23))]

u = {"title": "Passen und pressen im Viereck", "code": "UE-237", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Passspiel", "Ballannahme"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 4, "players_max": 4, "field_size": "14 x 14 m",
 "description": "Ein Aufwärmen mit Pass und Pressing um ein kleines Viereck. Vier Spieler passen sich den Ball zu, und nach dem Pass durchs Viereck läuft der Passgeber sofort hinterher und presst. Der Annehmende nimmt den Ball nach außen mit, weg vom Druck, und spielt quer weiter. Nach einem Doppelpass in der Mitte geht es von vorn los, und jeder ist eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 14 Metern, in der Mitte ein kleines Viereck von knapp 4 mal 4 Metern aus vier Hütchen.",
  "Verteilen: Vier Spieler: einer oben rechts mit Ball, einer oben, einer unten und einer rechts. Weitere Gruppen bekommen ein eigenes Feld. Der Trainer steht links mit Bällen.",
  "Ablauf: Pass nach oben und hinterherlaufen. Der Spieler oben spielt direkt durchs Viereck nach unten und presst sofort. Unten den Ball nach außen mitnehmen, quer nach rechts passen, dann Doppelpass mit dem Spieler in der Mitte.",
  "Wechsel: Jeder folgt seinem Weg auf die nächste Station. Nach dem Doppelpass startet der Spieler oben rechts die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Den ersten Kontakt weg vom pressenden Spieler mitnehmen", "Nach dem Pass schnell hinterher und echten Druck machen", "Genau und mit dem richtigen Tempo passen", "Mit links und rechts passen und dabei laut rufen"],
 "materials": ["4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Passen und pressen im Viereck. Vier Spieler passen um ein kleines Viereck, und nach dem Pass wird sofort gepresst.",
 "board": {"lines": LINES, "cones": CONES, "players": sp(), "balls": [B("b1", 62.6, 16.6)] + ERSATZ,
  "steps": [
   S("Pass nach oben", "Spieler zehn passt zu Spieler neun nach oben und läuft hinterher.",
     ps("b1", [50.6, 12.6]), mv("n10", [58, 8], delay=0.2)),
   S("Durch und pressen", "Spieler acht schaut schon, wo der Druck herkommt. Spieler neun spielt direkt durchs Viereck zu Spieler acht und sprintet sofort hinterher, um zu pressen.",
     bl("n8", [50, 31]), ps("b1", [50.6, 48.6], after=True), mv("n9", [48, 40], delay=0.2)),
   S("Weg vom Druck", "Spieler acht nimmt den Ball nach außen mit, weg von Spieler neun. Dann passt er quer zu Spieler sieben.",
     dr("n8", "b1", [40, 49]), ps("b1", [72.6, 33.6], after=True)),
   S("Doppelpass", "Spieler acht läuft in die Mitte des Vierecks. Spieler sieben spielt ihn an, und Spieler acht legt direkt zurück. Spieler sieben läuft dabei nach oben rechts.",
     mv("n8", [50, 30]), ps("b1", [50.6, 30.6], delay=0.4), mv("n7", [64, 21], after=True), ps("b1", [64.6, 21.6], delay=0.2)),
   S("Neu starten", "Jetzt ist jeder eine Station weiter. Spieler acht läuft nach rechts, und Spieler sieben startet die nächste Runde mit dem Pass nach oben zu Spieler zehn.",
     mv("n8", [72, 33]), ps("b1", [58.6, 8.6], delay=0.3))],
  "dims": dims(25, 75, 5, 55, "14 m", "14 m", rx=83)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt weg vom Druck.", "Weg vom Druck",
    "Wer den Ball bekommt, schaut vorher, woher der Druck kommt. Dann stellt er sich offen hin und nimmt den Ball mit dem ersten Kontakt zur Seite mit, weg vom pressenden Spieler. So hat er Zeit für den nächsten Pass.",
    sp(), [B("b1", 50.6, 12.6)] + ERSATZ,
    [S("Vorher schauen", "Spieler neun spielt durchs Viereck und presst sofort. Spieler acht schaut vorher, wo Spieler neun herkommt.",
       bl("n8", [50, 31]), ps("b1", [50.6, 48.6], after=True), mv("n9", [48, 38], delay=0.2)),
     S("Zur Seite mitnehmen", "Spieler acht nimmt den Ball mit dem ersten Kontakt nach links mit, weg von Spieler neun. Spieler neun kommt nicht mehr an den Ball.",
       dr("n8", "b1", [40, 49]), mv("n9", [45, 42], delay=0.2)),
     S("Quer weiter", "Jetzt hat Spieler acht Zeit und passt sauber quer zu Spieler sieben.",
       ps("b1", [72.6, 33.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Größeres Viereck, andere Richtung.", "Größer, andersherum",
    "Das Viereck wird größer, und es geht in die andere Richtung, also über links. Der pressende Spieler muss jetzt weiter laufen und noch schneller hinterher sein.",
    [P(i, "a", x, y, i[1:]) for i, (x, y) in POS2.items()] + [T], [B("b1", 35.6, 10.6)] + ERSATZ,
    [S("Pass nach oben", "Jetzt startet Spieler sieben oben links. Er passt zu Spieler zehn nach oben und läuft hinterher.",
       ps("b1", [50.6, 8.6]), mv("n7", [43, 6], delay=0.2)),
     S("Weiter pressen", "Spieler zehn spielt durchs große Viereck zu Spieler neun und sprintet den langen Weg hinterher.",
       ps("b1", [50.6, 52.6]), mv("n10", [54, 40], delay=0.2)),
     S("Nach außen und quer", "Spieler neun nimmt den Ball nach rechts mit, weg vom Druck, und passt quer zu Spieler acht. Dann geht es mit dem Doppelpass weiter wie vorher.",
       dr("n9", "b1", [60, 53]), ps("b1", [28.6, 31.6], after=True))],
    cones=CONES2)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
