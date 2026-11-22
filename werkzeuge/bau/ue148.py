import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 25-P1 (U12-U14, Woche 8 Phase 4): 3 v 3 High Pressing Game. 25 x 28 Yards = Feld x 28-72, y 5-55 (23 x 26 m),
# Pressingzone unten (12 Yards, gestrichelt), oben ein Jugendtor (mittleres Tor), unten zwei Minitore. Kein Torwart.
# Blau/Gelb (Pressing) -> Neon 7, 9, 11; Pink/Rot (mit Ball) -> Rot 8, 6, 10. Wartende Gruppen nur im Text. Ein Trainer statt zwei.
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 19, 38, "T")
POS = {"n7": (32.2, 27.3), "n9": (50, 27.6), "n11": (67.4, 30.2), "r8": (28.1, 52.2), "r6": (50.4, 55.1), "r10": (70.8, 50.8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 20.6, 41.5), B("s2", 17, 41.5)]
LINES = [rect(28, 5, 44, 50), line(28, 33.6, 72, 33.6)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 36, "y": 55, "side": "bottom"}, {"x": 64.5, "y": 55, "side": "bottom"}]
BAELLE = [B("b8", 28.7, 52.8), B("b6", 51, 55.7), B("b10", 71.4, 51.4)]

u = {"title": "Hoch pressen, drei Duelle", "code": "UE-148", "kind": "Spielform",
 "focuses": ["Verteidigen", "1 gegen 1", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 12, "field_size": "23 x 26 m",
 "description": "Drei Eins-gegen-eins-Duelle gleichzeitig, dann drei gegen drei. Auf Zuruf dribbeln drei Spieler von Team Rot mit Ball ins Feld, drei Spieler von Team Neon pressen sofort, jeder gegen seinen Gegenspieler. Erobert Neon den Ball, schießt es in eines der beiden Minitore. Kommt Rot am Pressing vorbei, dribbelt es nach vorn und schießt aufs große Tor. Nach jeder Runde tauschen die Teams.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 26 Metern. Unten die Pressingzone (11 Meter, gestrichelt) mit zwei Minitoren, oben ein Jugendtor.",
  "Verteilen: Drei von Team Neon stehen in der Mitte, drei von Team Rot mit Ball unten an der Linie. Die nächsten Gruppen warten an den Seiten. Der Trainer steht links mit Bällen.",
  "Ablauf: Auf Zuruf dribbeln die drei Roten ins Feld, die drei von Neon pressen sofort, jeder gegen einen. Neon erobert und schießt ins Minitor, Rot will vorbei und aufs große Tor.",
  "Wertung und Wechsel: Jedes Tor ist ein Punkt. Nach jeder Runde tauschen die Teams die Rollen, dann sind die nächsten Gruppen dran."],
 "organisation_show": ORG,
 "coaching_points": ["Sofort Druck auf den Ball, mit Tempo anlaufen", "Außen die Seitenlinie als zusätzlichen Verteidiger nutzen", "Mit dem Körper die Richtung vorgeben", "Als Einheit pressen und absichern, Läufe in die Tiefe mitgehen"],
 "materials": ["1 Jugendtor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Hoch pressen, drei Duelle. Drei gegen drei, und jeder presst seinen Gegenspieler, sobald der mit Ball ins Feld kommt.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Auf Zuruf hinein", "Auf Zuruf dribbeln Spieler acht, Spieler sechs und Spieler zehn gleichzeitig ins Feld. Sofort pressen Spieler sieben, Spieler neun und Spieler elf, jeder gegen seinen Gegenspieler.",
     dr("r8", "b8", [34, 45]), dr("r6", "b6", [50, 47]), dr("r10", "b10", [66, 46]),
     mv("n7", [35, 38.5], delay=0.2), mv("n9", [50, 39.5], delay=0.2), mv("n11", [64, 38.5], delay=0.2)),
   S("An die Linie drängen", "Wir schauen auf Spieler sieben. Er läuft schräg von innen an und drängt Spieler acht an die Seitenlinie.",
     dr("r8", "b8", [30.5, 40]), mv("n7", [34, 36], delay=0.1)),
   S("Ball erobert: Punkt", "Dann greift er zu, erobert den Ball und schießt sofort ins linke Minitor. Das gibt einen Punkt für Team Neon.",
     dr("n7", "b8", [34, 47]), ps("b8", [36, 54.7], after=True)),
   S("Durchgebrochen: Punkt", "Rechts ist Spieler zehn schneller als Spieler elf, dribbelt außen vorbei und trifft ins große Tor. Das gibt einen Punkt für Team Rot. Nach der Runde tauschen die Teams, und die nächsten Gruppen sind dran.",
     dr("r10", "b10", [71, 38]), dr("r10", "b10", [58, 18], after=True), ps("b10", [52, 5.3], after=True))],
  "dims": dims(28, 72, 5, 55, "23 m", "26 m", rx=82)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Drei gegen drei als Einheit.", "Drei gegen drei",
    "Jetzt darf Team Rot auch passen. Wer den Ballführenden presst, geht bis auf einen Schritt heran. Die anderen rücken mit ein und achten auf die Passwege. Kommt der Pass, presst der Nächste, und der Erste sichert ab.",
    sp(r8=(34, 47), r6=(50, 49), r10=(66, 46), n7=(35, 30), n9=(50, 32), n11=(65, 29)), [B("b6", 50.6, 49.6)] + ERSATZ,
    [S("Sofort Druck", "Spieler sechs hat den Ball. Spieler neun läuft sofort an, bis auf einen Schritt heran. Spieler sieben und Spieler elf rücken mit ein.",
       mv("n9", [50, 41.5]), mv("n7", [40, 36], delay=0.1), mv("n11", [60, 35], delay=0.1)),
     S("Pass abfangen: Punkt", "Spieler sechs will zu Spieler zehn passen. Spieler elf ahnt den Pass, läuft in den Passweg und fängt ihn ab. Dann schießt er ins rechte Minitor, und das gibt einen Punkt für Team Neon.",
       mv("n11", [60, 47.8]), ps("b6", [60.6, 48.4], delay=0.3), dr("n11", "b6", [63, 52], after=True), ps("b6", [64.5, 54.7], after=True))]),
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Seitenlinie hilft mit.", "Die Linie hilft",
    "Außen ist die Seitenlinie wie ein zusätzlicher Verteidiger. Der Verteidiger läuft schräg von innen an, damit der Gegner nicht in die Mitte kann. Dann wartet er auf den richtigen Moment, zum Beispiel einen zu weiten Kontakt, und greift zu.",
    sp(r8=(34, 45), n7=(35, 29), r6=(50, 47), n9=(50, 31), r10=(66, 46), n11=(65, 29)), [B("b8", 34.6, 45.6)] + ERSATZ,
    [S("Schräg anlaufen", "Spieler sieben läuft schräg von innen an. Spieler acht kann nicht in die Mitte und dribbelt an die Seitenlinie.",
       mv("n7", [37, 38.5]), dr("r8", "b8", [30.5, 40], delay=0.2)),
     S("Zugreifen: Punkt", "Spieler acht legt sich den Ball zu weit vor. Genau jetzt greift Spieler sieben zu, erobert den Ball und trifft ins linke Minitor. Das gibt einen Punkt für Team Neon.",
       dr("r8", "b8", [30.5, 33]), mv("n7", [35.5, 31], after=True), dr("n7", "b8", [35, 47], after=True), ps("b8", [36, 54.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
