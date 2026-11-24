import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-11 (U15-U17, Woche 3 Pre-Season): Developing 1st Touch, Acceleration & Speed. 20 x 30 Yards = 18 x 27 m (gerundet 18 x 25 m).
# Langes Feld QUER wie im PDF, Maße Breite x Länge (Vorbild ue317.py): Feld x 9-89, y 4-51, kein Tor, nur die Längen-Maßlinie (rechts warten Spieler).
# Ausrichtung wie im PDF. Drei Puppen als Stangen. Zwei Runden laufen gleichzeitig und spiegelbildlich: oben Team Neon (8 rechts
# oben spielt zu 10 in der Mitte unten, 10 diagonal zu 7 links oben, 7 dribbelt oben zurück), unten Team Rot (4 -> 9 -> 11,
# 11 dribbelt unten zurück). Im Original haben alle eine Farbe; zwei Teams nur, damit man die beiden Runden auseinanderhält.
# Nummern wie im PDF. Je Ecke rechts nur ein Wartender (2 und 6), die Spieler 5 und 3 nur im Text (3D-Abstand am Rand).
# Ein Trainer statt zwei, unten an der Seitenlinie. Original ohne Wertung: Ziel statt Punkte.
# Sichtkegel: PDF Key Coaching Point 1 „Stay aware of teammates crossing over“ (im Video nicht eingezeichnet). Grundform:
# Spieler zehn schaut zum Passgeber, nimmt an, dreht auf (bl mit von + drehen) und spielt diagonal. Coaching-Punkt 1: erst
# zu Spieler neun, der kreuzt, dann zum Passziel (ein Kegel mit von).
T = P("T", "c", 45, 55.3, "T")
ERSATZ = [B("s1", 48.5, 55.8), B("s2", 51, 55.8)]
POS = {"n7": (11.5, 6.5), "n8": (82.5, 6.5), "n10": (57.5, 36), "n2": (93.5, 6.5),
       "r11": (12, 48.5), "r4": (82.5, 49), "r9": (56, 17.5), "r6": (93.5, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def f(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(9, 4, 80, 47)]
PUPPEN = [C(50, 18.5, shape="stange"), C(33, 25.5, shape="stange"), C(49, 35, shape="stange")]
CONES = ecken(9, 4, 80, 47) + PUPPEN
WARTE = [B("b3", *f(POS["n2"])), B("b4", *f(POS["r6"]))]
DIMS = dims(9, 89, 4, 51, "25 m", "18 m")[:1]
M10, M9 = [43, 22.5], [43, 30]          # wohin die beiden mit dem ersten Kontakt nach innen mitnehmen
V10 = [[32, 33], [14, 11]]           # Spieler zehn: scharf unter der Puppe weg, dann Sprint zum Hütchen links oben
V9 = [[32, 18], [14, 43.5]]            # Spieler neun spiegelbildlich über der Puppe
ZU8, ZU7 = [71.5, 19.5], [39, 24]   # Blickziele in Richtung Spieler acht / Spieler sieben (Kegel nicht zu lang)
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Erster Kontakt und Antritt", "code": "UE-324", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Schnelligkeit"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "18 x 25 m",
 "description": "Zwei Runden laufen gleichzeitig und spiegelbildlich. Von außen geht der Ball in die Mitte, der Mittelspieler nimmt ihn mit dem ersten Kontakt nach innen mit und spielt diagonal in die andere Ecke. Dann zieht er scharf um die Puppe und sprintet zum Hütchen. Wer den Pass bekommen hat, dribbelt mit Tempo zurück zur ersten Station.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern. In jeder Ecke ein Hütchen, in der Mitte drei Puppen.",
  "Verteilen: Mindestens acht Spieler. In beiden Ecken links steht einer, rechts warten die anderen mit Ball. Zwei Mittelspieler stehen neben den Puppen. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Beide Runden starten gleichzeitig. Pass von außen in die Mitte und hinterherlaufen. Der Mittelspieler nimmt nach innen mit und spielt diagonal in die Ecke links. Danach zieht er scharf um die Puppe und sprintet zum Hütchen. Der Spieler aus der Ecke dribbelt mit Ball zurück nach rechts.",
  "Wechsel: Jeder rückt nach seiner Aktion eine Station weiter. Wer reinspielt, wird Mittelspieler, der Mittelspieler geht in die Ecke, der aus der Ecke stellt sich mit Ball rechts an."],
 "organisation_show": ORG,
 "coaching_points": ["Erster Kontakt nach innen, weg vom Passgeber", "Kopf hoch, wer kreuzt gerade?", "Scharf um die Puppe, dann Vollgas", "Mit Tempo dribbeln, der Ball bleibt nah"],
 "materials": ["4 Hütchen", "3 Puppen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Erster Kontakt und Antritt. Zwei Runden laufen gleichzeitig. Pass in die Mitte, mitnehmen, diagonal spielen und dann um die Puppe sprinten.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(),
  "balls": [B("b1", *f(POS["n8"])), B("b2", *f(POS["r4"]))] + WARTE + ERSATZ, "dims": DIMS,
  "steps": [
   S("Pass in die Mitte", "Beide Runden starten gleichzeitig. Oben spielt Spieler acht flach zu Spieler zehn in die Mitte, unten spielt Spieler vier zu Spieler neun. Spieler zehn schaut zum Ball, bis er ihn hat.",
     bl("n10", ZU8), ps("b1", f(POS["n10"]), after=True), ps("b2", f(POS["r9"]))),
   S("Nach innen mitnehmen, diagonal spielen", "Jetzt dreht Spieler zehn auf. Sein erster Kontakt geht nach innen, und schon kommt der Pass diagonal in die Ecke zu Spieler sieben. Spieler neun macht dasselbe nach unten zu Spieler elf. Die beiden Passgeber laufen in die Mitte nach.",
     bl("n10", ZU7, von=ZU8, dauer=1.3), drehen("n10", ZU7, gegen=True, delay=0.4),
     dr("n10", "b1", M10, after=True), ps("b1", f(POS["n7"]), after=True),
     dr("r9", "b2", M9, delay=0.9), ps("b2", f(POS["r11"]), after=True),
     mv("n8", POS["n10"], delay=1.2), mv("r4", POS["r9"], delay=1.2)),
   S("Um die Puppe, Sprint zum Hütchen", "Spieler zehn zieht scharf unter der Puppe weg und sprintet zum Hütchen links oben. Spieler neun kreuzt über der Puppe und sprintet nach unten. Gleichzeitig dribbeln Spieler sieben und Spieler elf los.",
     *weg("n10", V10), *weg("r9", V9, delay=0.4),
     dr("n7", "b1", [45, 8], delay=0.3), dr("r11", "b2", [45, 47.5], delay=0.3)),
   S("Mit Ball zurück zur Station", "Spieler sieben und Spieler elf dribbeln mit Tempo zurück in die Ecken rechts. Jetzt ist jeder eine Station weiter. Spieler zwei und Spieler sechs spielen den nächsten Ball rein, zu Spieler acht und Spieler vier in der Mitte.",
     dr("n7", "b1", [80, 7]), dr("r11", "b2", [80, 48.5]))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Augen auf, wer kreuzt gerade?", "Augen auf, wer kreuzt?",
    "In der Mitte kreuzen sich zwei Spieler mit Ball. Darum schaut jeder vor dem Mitnehmen, wo der andere gerade hinläuft. Einer geht zuerst, der andere wartet einen Moment. Kurzer Ruf, dann gibt es keinen Zusammenstoß, und das Tempo bleibt hoch.",
    sp(), [B("b1", *f(POS["n10"])), B("b2", *f(POS["r9"]))] + WARTE + ERSATZ,
    [S("Erst schauen, wer kommt", "Beide haben den Ball in der Mitte. Spieler zehn schaut erst zu Spieler neun, dann zu Spieler sieben in die Ecke. Er ruft und nimmt zuerst mit. Spieler neun wartet einen Moment.",
       bl("n10", ZU7, von=POS["r9"], dauer=1.3), dr("n10", "b1", M10, after=True), dr("r9", "b2", M9, delay=1.8)),
     S("Hintereinander kreuzen", "Die Pässe gehen in die Ecken. Spieler zehn läuft zuerst unter der Puppe durch. Spieler neun kreuzt erst danach über der Puppe.",
       ps("b1", f(POS["n7"])), ps("b2", f(POS["r11"]), delay=0.5), *weg("n10", V10, delay=0.3), *weg("r9", V9, delay=1.0))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Mit Tempo dribbeln, der Ball bleibt nah.", "Tempo mit Ball am Fuß",
    "Auf dem Weg zurück dribbelt der Spieler im vollen Lauf. Ist vorn Platz, darf der Ball etwas weiter vorgelegt werden. Vor der Station und vor den anderen werden die Kontakte kürzer. Der Ball springt nie weg.",
    sp(n10=M10, r9=(31, 29)), [B("b1", *f(M10)), B("b2", *f(POS["r11"]))] + WARTE + ERSATZ,
    [S("Pass in die Ecke", "Spieler zehn spielt diagonal in die Ecke. Spieler sieben nimmt den Ball gleich mit dem ersten Kontakt nach vorn mit.",
       ps("b1", f(POS["n7"])), dr("n7", "b1", [24, 7.5], after=True)),
     S("Erst länger, dann kurz", "Vorn ist Platz, also legt er sich den Ball etwas weiter vor. Vor der Station rechts werden die Kontakte kurz. Er kommt mit dem Ball eng am Fuß an.",
       dr("n7", "b1", [52, 8]), dr("n7", "b1", [68, 8], after=True), dr("n7", "b1", [80, 7], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
