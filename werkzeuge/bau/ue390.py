import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 36-P8 (U15-U17, Woche 33 Phase 2): Central Overload Wave Game. 30 x 45 Yards = 27 x 41 m (gerundet 25 x 40 m).
# Kein Großfeld (40 m lang), aber LANGES FELD QUER (Vorbild ue317.py): Das Feld liegt quer und füllt die Tafel (x 9-89, y 4-51),
# Tore links und rechts (Großfeldtore, nur C- und B-Jugend). Koordinaten direkt quer gesetzt. Gegenüber dem PDF um 180 Grad
# gedreht und quer gelegt: Team Neon (PDF blau) baut links auf und greift nach rechts an (im PDF von oben nach unten).
# Drei Zonen gestrichelt (x 33 und x 65, Mittelzone etwas größer wie im PDF). Beide Torhüter neutral (k1 links, k2 rechts),
# weil zweimal TW als doppelte Nummer gilt (wie ue317/ue358).
# PDF blau -> Team Neon mit den Nummern aus dem PDF (5, 4, 6 hinten; 10, 8 innen; 11, 7 außen in der Mitte).
# PDF gold -> Team Rot, doppelte Nummern plus zehn: 4 -> 14, 6 -> 16, 8 -> 18, 10 -> 20, 11 -> 21; 2, 3 und 9 bleiben.
# Spieler neun von Team Rot wartet wie im PDF in der Aufbauzone von Team Neon (Spitze für die Gegenrichtung), Spieler zwanzig und
# einundzwanzig warten außen an der Mittelzone (oben und unten neben dem Feld). Ein Trainer statt zwei, unten an der Seitenlinie.
# Grundform nach PDF und Video: 5 -> 4 -> 8 -> 10 (lässt sich in die Mitte fallen, dreht auf) -> steil auf 7, der in die
# Angriffszone startet; 11 und 10 rücken nach (3 gegen 3), 7 schließt ab. Danach dreht die Welle wie im Video: 11 und 7 gehen
# raus, 20 und 21 kommen rein, der Torwart von Team Rot eröffnet. Abschluss ins kurze Eck (Weg am Torwart vorbei).
# Fassungen: Steigerung 1 = PDF Progression 1 (ein Mittelfeldspieler presst vorn, ein Verteidiger rückt in die Mitte).
# Steigerung 2 = PDF Progression 2 mit dem Schluss aus dem Ton (Team Rot 1-2-2 ohne Zonen-Regeln, Ballgewinn in der Mitte zwei
# Punkte, in der Aufbauzone von Team Neon drei Punkte). Spieler neun, zwanzig und einundzwanzig sind dort nicht auf der Tafel.
# Sichtkegel: Text KCP „Draw opposition one side, switch to free player in midfield zone“ (freien Spieler finden); im Video kein
# Kegel eingezeichnet. Richtung aus dem Sinn: Spieler zehn schaut vor der Annahme zum Passgeber, nach der Annahme schwenkt der
# Kegel zum Läufer in die Angriffszone (bl mit von plus drehen, Vorbild ue300).
# Kein Dublette: UE-316 (36-P9, 3 gegen 3 plus Springer), UE-358 (36-P10, 7 gegen 7 mit nachrückendem Verteidiger),
# UE-352 (36-P11, halbes Feld 10 gegen 9), UE-364/UE-357 (Wellen mit Dreiergruppen) haben andere Organisation und Abläufe.
T = P("T", "c", 30, 55.3, "T")  # unten an der Seitenlinie, nahe der Aufbauzone von Team Neon
ERSATZ = [B("s1", 33.5, 55.8), B("s2", 36, 55.8)]
POS = {"k1": (12.5, 27.5), "n5": (21, 10), "n4": (22, 27.5), "n6": (21, 45), "n11": (40, 6.5), "n10": (40, 24), "n7": (40, 48),
       "n8": (58, 31), "k2": (86, 27.5), "r9": (30.5, 20), "r14": (53, 15), "r18": (48.5, 36), "r3": (77, 11.5), "r16": (76, 27.5),
       "r2": (77, 43), "r20": (62, 1.2), "r21": (60, 55)}
def sp(ohne=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items() if i not in ohne] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def F(i): return fuss(POS[i])
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
MY = (FY0 + FY1) / 2
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(33, FY0, 33, FY1), line(65, FY0, 65, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
# Nur die Länge als Maßlinie (rechts neben dem Tor ist kein Platz), die Breite steht in field_size
DIMS = dims(FX0, FX1, FY0, FY1, "40 m", "25 m")[:1]
V1 = dict(r9=(30.5, 39.5))  # Spieler neun steht in der Steigerung aus dem Weg von Spieler vierzehn
V2 = dict(r14=(31, 24), r16=(50, 13), r18=(49, 38), r3=(74, 17), r2=(74, 38))  # Team Rot im 1-2-2

u = {"title": "Welle mit vier gegen zwei", "code": "UE-390", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 16, "players_max": 18,
 "field_size": "25 x 40 m",
 "description": "Ein Wellenspiel auf zwei Tore in drei Zonen. Team Neon baut hinten ohne Gegner auf, spielt in der Mitte vier gegen zwei und greift vorn mit drei gegen drei an. Nach einem Treffer oder Ballverlust dreht die Welle. Zwei Spieler von Team Rot kommen in die Mitte, zwei von Team Neon gehen raus, und Team Rot greift in die andere Richtung an.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 40 Metern mit zwei Toren und Torhütern, in drei Zonen geteilt. Die Mittelzone ist etwas größer als die beiden Zonen vor den Toren.",
  "Verteilen: Hinten stehen drei Verteidiger von Team Neon, dort wartet auch Spieler neun von Team Rot als Spitze für die Gegenrichtung. In der Mitte spielen vier von Team Neon gegen zwei von Team Rot, zwei weitere von Team Rot warten außen an der Mittelzone. Vorn verteidigen drei von Team Rot.",
  "Ablauf: Team Neon spielt hinten frei in die Mitte, kombiniert sich im vier gegen zwei durch und spielt nach vorn. Drei Mittelfeldspieler rücken nach und greifen drei gegen drei an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach einem Treffer oder Ballverlust kommen die zwei Wartenden von Team Rot in die Mitte, die zwei Außen von Team Neon gehen raus, und die Welle läuft in die andere Richtung."],
 "organisation_show": ORG,
 "coaching_points": ["Ball schnell laufen lassen, ein, zwei Kontakte", "Rot auf eine Seite ziehen, dann zum Freien", "Ohne Ball in die Lücke anbieten", "Ball weg? Sofort umschalten"],
 "materials": ["2 große Tore", "Hütchen für die Zonen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Welle mit vier gegen zwei. Drei Zonen, zwei Tore. Team Neon spielt hinten frei, nutzt in der Mitte die Überzahl und greift vorn drei gegen drei an. Danach dreht die Welle.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *F("n5")), B("b2", *F("k2"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Hinten frei herausspielen", "Team Neon baut von hinten auf, hier gibt es keinen Gegner. Spieler fünf spielt quer zu Spieler vier. Der spielt den Ball sofort in die Mitte zu Spieler acht.",
     ps("b1", F("n4")), ps("b1", F("n8"), after=True)),
   S("Vier gegen zwei in der Mitte", "In der Mitte sind es vier gegen zwei. Spieler achtzehn läuft Spieler acht an. Spieler zehn bietet sich in der Lücke an und schaut zum Ball, und Spieler acht spielt ihn an.",
     mv("r18", [55, 38.5]), mv("n10", [45, 26], delay=0.2), bl("n10", POS["n8"], after=True), ps("b1", [45.6, 26.6], after=True)),
   S("Aufdrehen, steil nach vorn", "Spieler zehn dreht auf. Außen ist Spieler sieben schon losgelaufen, hinter die beiden aus der Mitte. Der Pass kommt flach in seinen Lauf. Spieler elf und Spieler zehn rücken nach.",
     bl("n10", [67, 42], von=POS["n8"], dauer=1.3), drehen("n10", [67, 42], delay=0.4), mv("n7", [67, 42], delay=0.3),
     ps("b1", [67.6, 42.6], after=True), mv("n10", [64, 24], after=True), mv("n11", [67, 11], delay=0.6)),
   S("Drei gegen drei vorn: Punkt", "Vorn spielen jetzt drei gegen drei. Spieler sieben zieht nach innen und schießt flach ins kurze Eck, und das gibt einen Punkt für Team Neon.",
     dr("n7", "b1", [73, 36]), ps("b1", [89, 33.5], after=True)),
   S("Die Welle dreht sich", "Das war der Punkt für Team Neon, jetzt dreht sich die Welle. Spieler sieben und Spieler elf gehen raus an die Seite, Spieler zwanzig und Spieler einundzwanzig kommen in die Mitte. Der Torwart von Team Rot spielt auf, und Team Rot greift mit vier gegen zwei in die andere Richtung an.",
     mv("n7", [60, 55]), mv("n11", [63, 1.2]), mv("r20", [44, 10], delay=0.2), mv("r21", [42, 44], delay=0.2), mv("n10", [48, 22], delay=0.3),
     ps("b2", fuss(POS["r16"]), delay=1.0))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Team Rot presst früher, vorn und in der Mitte.", "Früh pressen, Raum dahinter",
    "Ein Mittelfeldspieler von Team Rot darf jetzt vorn in der Aufbauzone pressen, und ein Verteidiger darf in die Mitte herausrücken. Der Aufbau wird schwerer. Dafür fehlt hinten ein Verteidiger, und vorn ist Platz für die Läufer von Team Neon.",
    sp(**V1), [B("b1", *F("k1"))] + ERSATZ,
    [S("Spieler vierzehn presst vorn", "Spieler vierzehn läuft aus der Mitte nach vorn und stellt Spieler vier zu. Also spielt der Torwart zu Spieler fünf.",
       mv("r14", [29.5, 22]), ps("b1", F("n5"), delay=0.6)),
     S("Ein Verteidiger rückt raus", "Gleichzeitig rückt Spieler sechzehn aus der Abwehr in die Mitte und presst Spieler zehn. Spieler zehn schaut zum Ball, und Spieler fünf spielt ihn trotzdem an.",
       mv("r16", [50, 19]), bl("n10", POS["n5"], delay=0.3), ps("b1", F("n10"), after=True)),
     S("Hinten ist jetzt Platz", "Hinten fehlt jetzt ein Verteidiger. Spieler zehn dreht auf, Spieler acht startet in die Lücke, und genau dahin kommt der Pass.",
       mv("n8", [70, 27], delay=0.3), bl("n10", [70, 27], von=POS["n5"], dauer=1.3), drehen("n10", [70, 27], delay=0.4),
       ps("b1", [70.6, 27.6], after=True)),
     S("Drei gegen zwei: Punkt", "Spieler elf und Spieler sieben rücken nach, vorn sind es drei gegen zwei. Spieler acht schießt flach ins Eck, und das gibt einen Punkt für Team Neon.",
       mv("n11", [68, 12]), mv("n7", [68, 43]), ps("b1", [89, 22], delay=0.6))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Team Rot verteidigt frei, und ein Ballgewinn bringt Extrapunkte.", "Ballgewinn gibt Extrapunkte",
    "Jetzt fallen die Zonen weg. Team Rot stellt sich mit einem vorn, zwei in der Mitte und zwei hinten auf und darf überall verteidigen. Ein Ballgewinn in der Mitte gibt zwei Punkte, in der Aufbauzone von Team Neon sogar drei. Team Neon muss den Ball schnell laufen lassen und die Lücken finden.",
    sp(ohne=("r9", "r20", "r21"), **V2), [B("b1", *F("n4"))] + ERSATZ,
    [S("Rot steht eins, zwei, zwei", "Team Rot steht mit einem vorn, zwei in der Mitte und zwei hinten. Spieler vierzehn läuft Spieler vier an, und der spielt raus zu Spieler sechs.",
       mv("r14", [27, 31]), ps("b1", F("n6"), delay=0.3)),
     S("Abgefangen: zwei Punkte", "Spieler sechs will in die Mitte zu Spieler zehn. Spieler achtzehn liest das, läuft in den Passweg und fängt den Ball ab. Ein Ballgewinn in der Mitte, das gibt zwei Punkte für Team Rot.",
       ps("b1", [35.6, 31]), mv("r18", [35, 30.4], delay=0.1))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
