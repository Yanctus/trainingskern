import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 64-P6 (U15-U17, Woche 17 Phase 3): Ball Exchange Finishing Game. 30 x 35 Yards = 27 x 32 m (nach der Meter-Regel 25 x 30 m),
# hochkant wie im PDF (Verhältnis 1,17, kein langes Feld). Feld x 29-71, y 5-55; Endzonen 10 Yards (9 m) bis y 19.3 und ab y 40.7,
# Mittelzone 15 Yards (etwa 14 m). Großfeldtore (nur C- und B-Jugend) mit neutralen Torhütern oben und unten.
# Navy -> Team Neon (6, 7, 8, 9), Pink -> Team Rot (2, 3, 4, 5); im PDF ohne Nummern, vergeben. Die vier Gelben (drittes Team,
# "ball exchangers") sind Springer (team t, Label F). Ein Trainer statt zwei. Rote Markierungen an den Zonenlinien weggelassen
# (Zonen als gestrichelte Linien). Positionen in Spalten gesetzt (3D-Abstand), Springer etwas weiter außerhalb des Feldes.
# Ablauf nach der PDF-Skizze: Der Springer, der den neuen Ball reinspielt, steht an derselben Seitenlinie am anderen Ende der
# Mittelzone (im PDF-Text "opposite side"). Jeder Springer hat einen eigenen Ball (wer den Pass bekommt, hat keinen am Fuß).
# Wechsel der Springer nach einigen Minuten ist ergänzt (im Original nicht genannt).
# Fassungen: PDF Key Coaching Point (Verteidiger schauen weg vom Ball und verfolgen den Läufer) und Progression (drei Sekunden).
# Sichtkegel: im Video eingezeichnet beim Verteidiger ("Defender looks away from the ball to move to intercept"): Spieler neun
# schaut zum Läufer Spieler vier. In der Steigerung aus dem Ton ("constantly be aware of the ball's position"): Spieler acht
# schaut zum Springer, nimmt an, dann schwenkt der Kegel zum Läufer (bl mit von).
T = P("T", "c", 16, 56, "T")
ERSATZ = [B("s1", 12, 57.5), B("s2", 11, 53.5)]
TW = [P("k1", "t", 50, 6.5, "TW"), P("k2", "t", 50, 54, "TW")]
F = {"f1": (23, 22), "f2": (23, 39), "f3": (77, 22), "f4": (77, 39)}
POS = {"n6": (48.5, 31), "n7": (31.5, 23), "n8": (65.5, 21.5), "n9": (65.5, 38.5),
       "r2": (57, 22.5), "r3": (40, 24.5), "r4": (57, 38.5), "r5": (40, 40)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] \
        + [P(i, "t", x, y, "F") for i, (x, y) in F.items()] + TW + [T]
def fb(*wer): return [B("b" + i, round(F[i][0] + 0.6, 1), round(F[i][1] + 0.6, 1)) for i in wer]
LINES = [rect(29, 5, 42, 50), line(29, 19.3, 71, 19.3), line(29, 40.7, 71, 40.7)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 55, "side": "bottom", "size": "gross"}]
DIMS = dims(29, 71, 5, 55, "25 m", "30 m", rx=84)

u = {"title": "Pass raus, neuer Ball rein", "code": "UE-345", "kind": "Spielform",
 "focuses": ["Torschuss", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "25 x 30 m",
 "description": "Zwei Teams spielen vier gegen vier in der Mittelzone, ein drittes Team steht als Springer außen an den Seitenlinien. Wer den Ball hat, sucht den Pass zu einem Springer. Sobald der ankommt, spielt ein anderer Springer sofort einen neuen Ball rein, ein Spieler nimmt ihn im Lauf mit, zieht in die Endzone und schließt gegen den Torwart ab. Beide Teams dürfen auf beide Tore spielen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit drei Zonen. In der Mitte liegt eine Zone von etwa 14 Metern, an beiden Enden eine Endzone von 9 Metern mit Großfeldtor und Torwart.",
  "Verteilen: Drei Teams zu viert. Team Neon und Team Rot spielen in der Mittelzone. Das dritte Team steht als Springer außen, zwei an jeder Seitenlinie, jeder mit Ball. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Vier gegen vier plus vier. Das Team mit Ball passt zu einem Springer. Sofort spielt ein anderer Springer einen neuen Ball rein. Ein Mitspieler nimmt ihn im Lauf mit, zieht in die Endzone und schließt ab. Gewinnt das andere Team den Ball, greift es selbst über die Springer an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Wer trifft, behält den Ball und greift wieder an, auf welches Tor er will. Nach einigen Minuten tauschen die Springer mit einem der Teams."],
 "organisation_show": ORG,
 "coaching_points": ["Pass nach außen? Sofort starten", "Ohne Ball laufen, schnell zum Abschluss", "Verteidiger: weg vom Ball, Läufer verfolgen", "In der Endzone eiskalt abschließen"],
 "materials": ["2 Großfeldtore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pass raus, neuer Ball rein. Vier gegen vier in der Mitte, vier Springer stehen außen. Kommt der Pass bei einem Springer an, spielt ein anderer Springer sofort einen neuen Ball rein, und vorn wird abgeschlossen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 49.1, 31.6)] + fb("f1", "f2", "f3") + ERSATZ,
  "steps": [
   S("Ball in der Mitte", "Team Neon hat den Ball in der Mittelzone. Spieler sechs spielt flach rüber zu Spieler neun. Spieler vier schiebt mit.",
     ps("b1", [66.1, 39.1]), mv("r4", [60, 41.5], delay=0.4)),
   S("Pass zum Springer ist das Signal", "Spieler neun legt raus zum Springer an der Seitenlinie. Das ist das Signal. Spieler acht startet sofort schräg nach innen.",
     ps("b1", [77.6, 39.6]), mv("n8", [60, 18.5], delay=0.4)),
   S("Neuer Ball in den Lauf", "Im selben Moment spielt der andere Springer auf dieser Seite seinen Ball rein, genau in den Lauf von Spieler acht. Der nimmt ihn mit und zieht in die Endzone. Spieler zwei kommt zu spät.",
     ps("bf3", [60.6, 19.1]), dr("n8", "bf3", [55, 11.5], after=True), mv("r2", [59, 16.5], delay=0.8)),
   S("Abschluss: Punkt", "Spieler acht schließt flach am Torwart vorbei ab, und das gibt einen Punkt für Team Neon. Team Neon behält den Ball und greift sofort wieder an, gern auch auf das andere Tor.",
     ps("bf3", [54, 5.3]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Weg vom Ball schauen und den Läufer verfolgen.", "Läufer im Blick behalten",
    "Zuerst verhindern die Verteidiger den Pass nach außen. Kommt er trotzdem an, schauen sie weg vom Ball und suchen den Läufer. Wer ihn findet und mitgeht, fängt den Pass nach innen ab. Dann greift das eigene Team sofort an.",
    sp(n8=(66, 27.5), n9=(66, 43)), [B("b1", 57.6, 23.1)] + fb("f1", "f2", "f4") + ERSATZ,
    [S("Rot spielt raus zum Springer", "Jetzt hat Team Rot den Ball. Spieler zwei spielt raus zum Springer. Sofort schaut Spieler neun weg vom Ball und sucht Spieler vier.",
       ps("b1", [77.6, 22.6]), bl("n9", [50, 41], after=True)),
     S("Mitgehen und abfangen", "Spieler vier startet in die Endzone, und Spieler neun geht mit. Der andere Springer spielt seinen Ball nach innen. Spieler neun ist zuerst dran.",
       mv("r4", [51, 47]), mv("n9", [58, 46.5], delay=0.2), ps("bf4", [58.6, 47.1], after=True)),
     S("Ball erobert, Neon greift an", "Ball erobert. Jetzt ist Team Neon dran. Spieler neun dribbelt raus aus der Endzone und spielt zu Spieler sechs, und das Spiel über die Springer beginnt von vorn.",
       dr("n9", "bf4", [62, 38]), ps("bf4", [49.1, 31.6], after=True))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Drei Sekunden bis zum Abschluss.", "Drei Sekunden zum Abschluss",
    "Nach dem Pass zum Springer bleiben nur drei Sekunden. In dieser Zeit muss der Ball in die Endzone und rein. Wer den neuen Ball bekommt, spielt sofort weiter auf einen Läufer, der an ihm vorbei startet. Klappt das nicht, behält das Team den Ball und baut neu auf.",
    sp(), [B("b1", 66.1, 39.1)] + fb("f1", "f2", "f3") + ERSATZ,
    [S("Raus zum Springer, Uhr läuft", "Spieler neun spielt raus zum Springer. Ab jetzt zählen drei Sekunden.",
       ps("b1", [77.6, 39.6])),
     S("Neuer Ball, Läufer startet", "Der andere Springer spielt sofort rein auf Spieler acht. Der schaut zum Ball. Gleichzeitig startet Spieler sieben an allen vorbei in die Endzone.",
       bl("n8", [77, 22]), ps("bf3", [66.1, 22.1], after=True), mv("n7", [46, 12], delay=0.3)),
     S("Direkt in die Endzone: Punkt", "Spieler acht nimmt den Kopf hoch und spielt mit einem Kontakt in die Endzone. Spieler sieben schließt ab, alles in drei Sekunden, und das gibt einen Punkt für Team Neon.",
       bl("n8", [46, 12], von=[77, 22], dauer=1.3), ps("bf3", [46.6, 12.6], after=True), ps("bf3", [45, 5.3], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
