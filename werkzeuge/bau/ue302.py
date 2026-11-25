import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 60-P7 (U15-U17, Woche 10): Defensive Pressing & Covering, Defensive Shape. 35 x 40 Yards = 32 x 37 m, gerundet 35 m breit und
# 30 m tief. Ausrichtung wie im PDF (Tor oben), Feld x 20-80, y 5-55. Nicht gedreht.
# Video: erste Kette rot (2, 6, 5, 3), zweite Kette gold (2, 5, 4, 3), Angreifer blau (11, 4, 9, 8, 7).
# Hier: beide Ketten Team Neon (erste 2, 6, 5, 3; zweite neu nummeriert 12, 13, 14, 15, weil doppelt), Angreifer Team Rot.
# Torwart neutral. Ein Trainer (im Feld unten wie im PDF) statt zwei. Positionen für den 3D-Abstand leicht verschoben.
# Sprintweg: außen um das untere Hütchen und neben dem Feld hoch zur Torlinie (im Video quer durchs Feld gezeichnet).
# Fassungen: Coaching-Punkt aus dem Video ("Be careful pressing, don't both get sucked in"); der PDF-Coaching-Punkt (Sprint und
# Wechsel der Ketten) steckt schon im letzten Schritt der Grundform. Steigerung = PDF Progression (freies Spiel auf Kommando).
# Kein Dubletten-Fall: UE-099 ist ein Paar zwischen acht Passspielern mit Dummys, UE-166 ein 4 gegen 4 mit Kontertoren,
# UE-206 die Kette ohne Gegner mit Farbhütchen. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 50, 50, "T")
TB = [50.6, 50.6]
ERSATZ = [B("s1", 53.6, 53.5), B("s2", 50, 53.5)]
TW = P("k", "t", 50, 8, "TW")
POS = {"n2": (31, 22), "n6": (40.5, 20), "n5": (59, 22), "n3": (69, 22),
       "r11": (22.5, 33), "r4": (40.5, 36), "r9": (50, 27), "r8": (59.5, 38.5), "r7": (77.5, 33),
       "n12": (30, 2), "n13": (38.5, 2), "n14": (61.5, 2), "n15": (70, 2)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
LINES = [rect(20, 5, 60, 50), rect(32, 5, 36, 15), rect(41, 5, 18, 6)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}]
CONES = [C(20, 5), C(80, 5), C(20, 43), C(80, 43)]
DIMS = dims(20, 80, 5, 55, "35 m", "30 m", rx=96)
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Viererkette presst und sichert", "code": "UE-302", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Kondition"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "35 x 30 m",
 "description": "Eine Viererkette mit Torwart steht gegen fünf Angreifer. Der Trainer spielt einen Angreifer an, der nächste Verteidiger rückt raus und stellt ihn, die anderen drei schieben dahinter zusammen. Das wiederholt sich Ball für Ball. Auf Kommando sprintet die Kette um die Hütchen nach draußen, und die zweite Kette übernimmt sofort.",
 "organisation": ["Aufbauen: Ein Feld von 35 Metern Breite und 30 Metern Tiefe mit großem Tor und Strafraum. In den beiden oberen Ecken und unten an beiden Seitenlinien steht je ein Hütchen.",
  "Verteilen: Team Neon stellt zwei Viererketten. Die erste steht vor dem Strafraum, die zweite wartet an der Torlinie. Fünf Angreifer von Team Rot verteilen sich davor, im Tor steht ein Torwart. Der Trainer steht mit den Bällen unten im Feld.",
  "Ablauf: Der Trainer spielt einen Angreifer an. Der nächste Verteidiger rückt raus und stellt ihn, ohne den Ball zu erobern. Die anderen drei schieben zur Ballseite und sichern ab. Der Ball geht zurück zum Trainer, und er spielt den nächsten an.",
  "Wechsel: Auf Kommando sprintet die Kette um die unteren Hütchen und außen hoch bis zur Torlinie. Die zweite Kette rückt sofort ins Feld und verteidigt weiter. Die Angreifer bleiben einige Durchgänge drin."],
 "organisation_show": ORG,
 "coaching_points": ["Einer geht raus, die anderen drei schieben zusammen", "Laut ansagen, wer presst und wer sichert", "Schnell hin und eng an den Mann, dann spielt er zurück", "Die Linie halten, kurze Abstände zum Nebenmann"],
 "materials": ["1 großes Tor", "4 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Viererkette presst und sichert. Vier Verteidiger und ein Torwart gegen fünf Angreifer. Der Trainer spielt an, einer rückt raus, drei sichern ab. Auf Kommando wird gesprintet, und die zweite Kette kommt rein.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *TB)] + ERSATZ,
  "steps": [
   S("Ball zu Spieler vier, einer rückt raus", "Der Trainer spielt Spieler vier an. Spieler sechs steht am nächsten und rückt sofort raus. Er stellt ihn nur, den Ball erobert er nicht. Gleichzeitig schieben die anderen drei nach innen und sichern hinter ihm ab.",
     ps("b1", [41.1, 36.6]), mv("n6", [42.5, 31], delay=0.2), mv("n2", [34.5, 24.5], delay=0.4), mv("n5", [54, 21.5], delay=0.4), mv("n3", [63.5, 22.5], delay=0.4)),
   S("Ball nach rechts, die Kette schiebt", "Spieler vier kommt nicht vorbei und spielt zurück. Der Trainer legt nach rechts raus auf Spieler sieben. Jetzt ist Spieler drei dran. Spieler sechs fällt zurück in die Linie, und alle rücken ein Stück nach rechts.",
     ps("b1", TB), ps("b1", [78.1, 33.6], after=True), mv("n6", [48.5, 21.5], delay=0.5), mv("n3", [73, 29], delay=1.2),
     mv("n5", [64, 24], delay=1.2), mv("n2", [38.5, 23], delay=1.2)),
   S("Kommando: Sprint und Wechsel", "Der Ball geht zurück, und der Trainer ruft das Kommando. Die vier sprinten um die Hütchen unten an der Seite und außen hoch bis zur Torlinie. Sofort rücken die Spieler zwölf bis fünfzehn ins Feld und stellen die neue Kette. Der Trainer spielt gleich den nächsten Ball an.",
     ps("b1", TB),
     *weg("n2", [[27, 40], [22, 47.5], [15.5, 44.5], [16.5, 3.5]], delay=0.5), *weg("n6", [[33, 31], [25, 49], [12, 44], [8, 3.5]], delay=0.5),
     *weg("n3", [[71.5, 39], [78, 47.5], [84.5, 44.5], [83.5, 3.5]], delay=0.5), *weg("n5", [[67, 31], [75, 49], [88, 44], [91.5, 3.5]], delay=0.5),
     mv("n12", [31, 22], delay=0.9), mv("n13", [40.5, 20], delay=0.9), mv("n14", [59, 22], delay=0.9), mv("n15", [69, 22], delay=0.9))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nur einer rückt raus.", "Nur einer rückt raus",
    "Gehen zwei Verteidiger auf denselben Angreifer, fehlt daneben einer. Darum sagt der Nächste laut an, dass er geht. Sein Nebenmann bleibt schräg dahinter und macht die Lücke zu.",
    sp(), [B("b1", *TB)] + ERSATZ,
    [S("Zwei gehen auf denselben Mann", "Der Ball kommt zu Spieler acht. Spieler fünf rückt raus, das passt. Aber Spieler drei läuft auch hin. Rechts ist jetzt alles offen, und Spieler sieben steht frei.",
       ps("b1", [60.1, 39.1]), mv("n5", [57.5, 33], delay=0.2), mv("n3", [66, 35], delay=0.3)),
     S("Einer presst, einer sichert", "Besser so. Spieler fünf ruft: Ich gehe! Spieler drei lässt sich fallen und sichert schräg hinter ihm ab. Links schieben Spieler sechs und Spieler zwei nach, die Abstände bleiben kurz.",
       mv("n3", [67, 24.5]), mv("n6", [48.5, 21], delay=0.3), mv("n2", [39.5, 23], delay=0.3))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Auf Kommando wird frei gespielt.", "Freies Spiel auf Kommando",
    "Erst läuft alles wie bisher. Ruft der Trainer das Kommando, greifen die fünf Angreifer richtig an und suchen den Abschluss. Die Kette muss sofort umstellen. Die Mitte bleibt zu, außen wird das Duell angenommen, und im Strafraum hat jeder seinen Gegenspieler.",
    sp(), [B("b1", *TB)] + ERSATZ,
    [S("Kommando: Jetzt wird angegriffen", "Der Trainer spielt Spieler vier an und ruft: Frei! Spieler sechs rückt raus. Spieler vier spielt gleich weiter in die Mitte zu Spieler neun.",
       ps("b1", [41.1, 36.6]), mv("n6", [42.5, 31], delay=0.2), ps("b1", [50.6, 27.6], after=True)),
     S("Über außen", "Durch die Mitte geht nichts, Spieler fünf ist sofort bei Spieler neun. Also raus auf den Flügel. Spieler elf geht die Linie runter, Spieler zwei läuft mit. Die anderen fallen in den Strafraum zurück.",
       mv("n5", [55, 23]), mv("r11", [23.5, 13], delay=0.3), ps("b1", [24.1, 13.6], delay=0.5), mv("n2", [28, 19.5], delay=0.5),
       mv("n6", [41, 12.5], delay=0.7), mv("n5", [51.5, 15.5], after=True), mv("n3", [62, 14], delay=0.7), mv("r9", [47, 18.5], delay=1.0), mv("r7", [70, 20], delay=1.0)),
     S("Flanke geklärt", "Spieler elf flankt flach vor das Tor. Spieler sechs steht richtig, ist vor Spieler neun am Ball und klärt nach außen. Die Kette hat das Tor verteidigt, und der Trainer spielt den nächsten Ball an.",
       ps("b1", [41.6, 13.1]), ps("b1", [30, 30], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
