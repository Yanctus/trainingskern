import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 71-P5 (U15-U17, Woche 21 Phase 2): Possession to Penetrate (Rondo). 20 x 20 Yards = 18 x 18 m, Feld x 25-75, y 5-55.
# Ausrichtung wie im PDF (nicht gedreht). Vier Minitore Rücken an Rücken in der Mitte, Öffnungen nach außen (oben, unten,
# links, rechts), als kompakter Block wie im PDF.
# PDF pink (sieben Spieler in Ballbesitz: 8, 4, 3, 2, 10, 6, 5) -> Team Neon mit den Nummern aus dem PDF. PDF blau (drei
# Verteidiger) -> Team Rot, neu nummeriert, weil 8, 4 und 6 doppelt sind: 8 -> 7, 4 -> 9, 6 -> 11.
# Positionen leicht verschoben (3D-Abstand): Spieler acht weiter nach links, Spieler zehn rechts oben vor die Tore,
# Verteidiger um die Tore verteilt. Trainer links statt rechts (rechts steht die Maßlinie).
# Grundform: sechs Pässe (5-6-3-8-4-10-2, im PDF ab Spieler drei eingezeichnet) geben einen Punkt und öffnen die Minitore,
# dann spielt Spieler zwei ins Minitor (zwei Punkte) wie im PDF.
# Fassungen: PDF Progression 1 (keine Passvorgabe, sichern oder durchstecken) und Progression 2 (nach einem Treffer ins Minitor
# sind die Tore zu, fünf Pässe geben zwei Punkte, die Verteidiger pressen).
# Sichtkegel: Text KCP „Scan to recognise defenders positions - play through/around“, Ton „scan early to recognise defender
# positions“: Spieler zehn schaut zum Passgeber, nach der Annahme schwenkt der Kegel zu Spieler zwei (mit Drehpfeil);
# in Steigerung eins schaut Spieler fünf vor dem Pass zum Minitor. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 13, 45, "T")
ERSATZ = [B("s1", 16.6, 48.5), B("s2", 13, 48.8)]
POS = {"n8": (34, 5), "n4": (64, 5), "n3": (25, 28.5), "n2": (75, 26.5), "n10": (57, 21), "n6": (40.5, 54), "n5": (63.5, 54),
       "r7": (43, 16), "r9": (34, 31), "r11": (52, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def F(i): return fuss(POS[i])
LINES = [rect(25, 5, 50, 50)]
# Mitte bei (50, 30), wie im PDF ein kompakter Block: Öffnung rechts bei x 57.2, links bei x 42.8 (Netze bis x 54 bzw. 46),
# oben bei y 26.8, unten bei y 33.2 (die Netze treffen sich in der Mitte)
TORE = [{"x": 57.2, "y": 30, "side": "left"}, {"x": 42.8, "y": 30, "side": "right"},
        {"x": 50, "y": 26.8, "side": "bottom"}, {"x": 50, "y": 33.2, "side": "top"}]
DIMS = dims(25, 75, 5, 55, "18 m", "18 m")

u = {"title": "Sechs Pässe, dann ins Minitor", "code": "UE-359", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "18 x 18 m",
 "description": "Ein Rondo sieben gegen drei mit vier Minitoren in der Mitte. Team Neon hält den Ball, alle sechs Pässe gibt es einen Punkt. Nach den ersten sechs Pässen sind die Minitore offen, und ein Pass in eines davon gibt zwei Punkte. Erobert Team Rot den Ball, spielt es ihn aus dem Feld oder zum Trainer.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. In der Mitte stehen vier Minitore Rücken an Rücken, die Öffnungen zeigen nach außen.",
  "Verteilen: Team Neon spielt mit sieben Spielern, sechs außen an den Linien und einer innen. Team Rot verteidigt zu dritt rund um die Tore. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Team Neon lässt den Ball laufen und zählt die Pässe. Nach sechs Pässen sind die Minitore offen. Jetzt entscheidet Team Neon, ob es den Ball weiter hält oder in ein Minitor spielt.",
  "Wertung und Wechsel: Sechs Pässe geben einen Punkt, ein Pass ins Minitor gibt zwei Punkte. Erobert Team Rot den Ball und spielt ihn aus dem Feld oder zum Trainer, gibt das einen Punkt für Team Rot. Der Trainer bringt sofort einen neuen Ball. Nach ein paar Minuten werden die Verteidiger getauscht."],
 "organisation_show": ORG,
 "coaching_points": ["Breit machen, die Überzahl ausnutzen", "Vor der Annahme schauen, wo die Verteidiger stehen", "Halten oder durchstecken? Erst schauen, dann entscheiden", "Kurze, scharfe Pässe und immer einen Winkel anbieten"],
 "materials": ["4 Minitore", "4 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechs Pässe, dann ins Minitor. Sieben halten den Ball gegen drei. Wer sechs Pässe schafft, darf in die Minitore in der Mitte spielen.",
 "board": {"lines": LINES, "goals": TORE, "cones": ecken(25, 5, 50, 50), "players": sp(), "balls": [B("b1", *F("n5"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Pass eins und zwei", "Team Neon hält den Ball und zählt mit. Spieler fünf spielt quer zu Spieler sechs, der gleich weiter zu Spieler drei. Das sind zwei.",
     ps("b1", F("n6")), ps("b1", F("n3"), after=True), mv("r9", [33, 35], delay=0.6), mv("r11", [46, 46], delay=0.2)),
   S("Pass drei und vier", "Spieler drei spielt hoch zu Spieler acht, und der Ball geht direkt weiter auf die andere Seite zu Spieler vier. Spieler sieben läuft hinterher.",
     ps("b1", F("n8")), ps("b1", F("n4"), after=True), mv("r9", [34, 31], delay=0.3), mv("r7", [52, 12], delay=0.5)),
   S("Kopf hoch vor der Annahme", "Spieler zehn bietet sich innen an. Bevor der Ball kommt, schaut er zum Ball und sieht, wo die Verteidiger stehen. Spieler vier spielt ihn an. Das ist Pass fünf.",
     bl("n10", F("n4")), ps("b1", F("n10"), after=True)),
   S("Sechs Pässe: Punkt, Tore offen", "Nach der Annahme dreht er auf und spielt raus zu Spieler zwei. Sechs Pässe, das gibt einen Punkt für Team Neon. Jetzt sind die Minitore offen.",
     bl("n10", F("n2"), von=F("n4"), dauer=1.3), drehen("n10", F("n2"), delay=0.4), ps("b1", F("n2"), after=True), mv("r7", [58, 16], delay=0.6)),
   S("Ins Minitor: zwei Punkte", "Spieler zwei sieht, dass vor ihm keiner steht, und spielt flach ins Minitor. Das gibt zwei Punkte für Team Neon. Der Trainer bringt einen neuen Ball, und das Zählen beginnt von vorn.",
     ps("b1", [56.3, 30.3]), mv("r11", [55, 40], delay=0.2))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Minitore sind immer offen.", "Halten oder durchstecken",
    "Jetzt gibt es keine Passvorgabe mehr, die Minitore sind von Anfang an offen. Team Neon entscheidet selbst, wann es durchsteckt. Die Verteidiger stellen die Wege zu den Toren zu und lauern auf den Fehlpass.",
    sp(r9=(34, 30)), [B("b1", *F("n3"))] + ERSATZ,
    [S("Weg zu, also sichern", "Spieler drei will ins Minitor, aber Spieler neun steht genau im Weg. Also sichert er den Ball und spielt runter zu Spieler sechs.",
       mv("r9", [33, 29.5]), ps("b1", F("n6"), delay=0.3), mv("r11", [44, 46], delay=0.6)),
     S("Verteidiger schiebt rüber", "Spieler elf schiebt zum Ball. Spieler sechs spielt sofort weiter zu Spieler fünf. Der schaut kurz, und der Weg zum Minitor unten ist frei.",
       ps("b1", F("n5")), mv("r11", [47, 47], delay=0.2), bl("n5", [50, 34], after=True)),
     S("Jetzt durch: zwei Punkte", "Jetzt ist der richtige Moment. Spieler fünf spielt flach ins Minitor, und das gibt zwei Punkte für Team Neon.",
       ps("b1", [50.3, 32.6]), mv("r11", [52, 44], delay=0.2))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Nach einem Treffer ins Minitor sind die Tore zu.", "Tore zu, fünf Pässe zählen",
    "Nach einem Treffer ins Minitor sind die Tore zu. Jetzt geben schon fünf Pässe zwei Punkte, und danach sind die Tore wieder offen. Die Verteidiger müssen also hart pressen. Wer das Pressing überspielt, findet wieder Platz.",
    sp(), [B("b1", *F("n3"))] + ERSATZ,
    [S("Rot presst hart", "Die Tore sind zu, also geht Team Rot drauf. Spieler neun läuft Spieler drei an. Der spielt sofort zu Spieler acht, und von dort geht es weiter zu Spieler vier. Zwei Pässe.",
       mv("r9", [30, 27]), mv("r7", [38, 12], delay=0.2), ps("b1", F("n8"), delay=0.3), ps("b1", F("n4"), after=True)),
     S("Raus aus dem Druck", "Spieler sieben kommt zu spät. Spieler vier spielt in die Mitte auf Spieler zehn, der gleich klatschen lässt zu Spieler zwei. Das sind vier.",
       mv("r7", [56, 10]), ps("b1", F("n10"), delay=0.2), ps("b1", F("n2"), after=True)),
     S("Fünf Pässe: zwei Punkte", "Spieler zwei spielt runter zu Spieler fünf. Fünf Pässe, und das gibt zwei Punkte für Team Neon. Jetzt sind die Minitore wieder offen.",
       ps("b1", F("n5")), mv("r11", [58, 47], delay=0.3))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
