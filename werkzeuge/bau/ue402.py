import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 18-P11 (U15-U17, Woche 37 Phase 1): Playing Through the Thirds (Medium Sided Game). 7 gegen 7 plus Torwart auf einer
# ganzen Platzhälfte in voller Breite. Halbes Feld, darum kein Großfeld quer: hochkant wie im PDF, großes Tor oben
# (Großfeldtor, nur C- und B-Jugend), zwei Minitore unten an der Mittellinie für den Konter. Feld x 15-85, y 4-57,
# Strafraum und Torraum oben, Zonengrenzen gestrichelt bei y 22 und y 40.5 (wie im PDF etwa ein Drittel und zwei Drittel).
# Mittelkreis weggelassen (ein Vollkreis ragte unten aus der Tafel).
# PDF pink (3, 4, 6 hinten, 11, 8, 7 Mitte, 9 vorn) -> Team Neon, Nummern wie im PDF. PDF blau -> Team Rot mit Torwart r1
# (im PDF grün), neu nummeriert, weil die Nummern doppelt sind: 4 -> 2, 5 -> 5, 8 -> 13, 6 -> 12, 10 -> 10, 9 -> 14, 11 -> 15.
# Positionen auf ein Spaltenraster gelegt (Abstand 8,5, 3D-Abstand), dafür leicht gegenüber dem PDF verschoben. Ein Trainer statt zwei.
# Grundform nach PDF und Video 0:03-0:23: 6 -> 4 -> 3, steil auf 8 in der Mitte, raus auf 11, Pass in die Endzone auf 9,
# 11 und 7 laufen mit ein ("support run"). Abschluss vereinfacht: Die Verteidiger gehen mit den Läufern mit, 9 dreht auf und schießt.
# Fassungen: PDF Key Coaching Point (Verteidiger dribbelt in die Mittelzone, vier gegen zwei; im Video als Regel "defender can
# dribble into middle zone", darum Steigerung) und Progression (mindestens zwei Spieler je Zone und Team).
# Die Zwischenstufe aus dem Video (ein Verteidiger von Team Rot darf in eine tiefere Zone helfen) nur im Bericht.
# Sichtkegel: Text/Ton "Recognise whether to advance", "spatial awareness", "fully aware of team mates' positioning"; im Video
# nicht eingezeichnet. Richtung aus dem Sinn: Spieler acht schaut zum Passgeber, nimmt an und schwenkt den Blick beim Aufdrehen
# nach außen (bl mit von + drehen, Vorbild ue300); Spieler neun genauso vor dem Abschluss; in den Steigerungen schaut Spieler vier
# (Kegel auf etwa 20 Einheiten gekürzt) vor dem Andribbeln bzw. vor dem Nachrücken nach vorn.
# Kein Dublette: UE-234 (43-P11) ist auch ein halbes Feld mit drei Zonen und Konter auf Minitore, aber 8 gegen 8 mit 2 gegen 1
# hinten und anderer Regel (Dribbling in die Mitte öffnet das Spiel); hier 3 gegen 3, 3 gegen 2, Anspiel in jeder Zone Pflicht.
T = P("T", "c", 8, 50, "T")
POS = {"r1": (48, 6), "r2": (39.5, 14), "r5": (68, 13), "n9": (59.5, 16),
       "n11": (17, 31), "r13": (42.5, 30), "n8": (51, 36), "r12": (68, 29), "n7": (77, 30),
       "r10": (25.5, 45), "r14": (59.5, 45), "r15": (77, 46), "n3": (17, 54), "n4": (51, 52), "n6": (68, 53)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, d=None): x, y = (d or POS)[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
ERSATZ = [B("s1", 9.6, 46.5), B("s2", 6, 46.5)]
LINES = [rect(15, 4, 70, 53), rect(29.5, 4, 41, 16.5), rect(40.6, 4, 18.8, 5.6), line(15, 22, 85, 22), line(15, 40.5, 85, 40.5)]
CONES = [C(15, 22), C(85, 22), C(15, 40.5), C(85, 40.5)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}, {"x": 28, "y": 57, "side": "bottom"}, {"x": 72, "y": 57, "side": "bottom"}]
SCHUSS = [52.5, 4.3]

u = {"title": "Sieben gegen sieben in Dritteln", "code": "UE-402", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 15, "field_size": "Halbes Spielfeld",
 "description": "Sieben gegen sieben plus Torwart auf einer ganzen Platzhälfte, geteilt in drei Zonen. Team Neon spielt sich von hinten Zone für Zone nach vorn und greift das große Tor an. In die nächste Zone darf der Ball nur, wenn ein Mitspieler in seiner Zone angespielt wurde. Erobert Team Rot den Ball, kontert es auf zwei Minitore an der Mittellinie.",
 "organisation": ["Aufbauen: Eine Platzhälfte in voller Breite mit großem Tor und Torwart. Zwei gestrichelte Linien teilen sie in drei Zonen: hinten, Mitte und die Endzone vor dem Tor. An der Mittellinie stehen zwei Minitore.",
  "Verteilen: Team Neon mit drei Spielern hinten, drei in der Mitte und einem Stürmer vorn. Team Rot mit Torwart, zwei Verteidigern vorn, zwei Spielern in der Mitte und drei Spielern hinten. Hinten ist es drei gegen drei, in der Mitte drei gegen zwei, vorn einer gegen zwei. Der Trainer steht mit Bällen an der Ecke.",
  "Ablauf: Team Neon baut hinten auf. Der Ball geht erst in die nächste Zone, wenn dort ein Mitspieler angespielt wurde. Wer angespielt ist, darf nach vorn nachrücken. Vorn laufen die Mittelfeldspieler mit in die Endzone und helfen dem Stürmer.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und trifft in ein Minitor, gibt das einen Punkt für Team Rot. Danach spielt der Trainer einen neuen Ball zu den drei Spielern hinten."],
 "organisation_show": ORG,
 "coaching_points": ["Passen oder andribbeln? Erst schauen, dann entscheiden", "Ist vor dir Platz, nimm den Ball mit", "Geht einer nach vorn, sichert ein anderer ab", "Ball weg? Sofort umschalten"],
 "materials": ["1 großes Tor", "2 Minitore", "4 Hütchen für die Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sieben gegen sieben in Dritteln. Team Neon spielt sich auf einer Platzhälfte von hinten durch drei Zonen bis vor das große Tor. Team Rot verteidigt und kontert auf zwei Minitore.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": [B("b1", *fuss("n6"))] + ERSATZ,
  "steps": [
   S("Hinten drei gegen drei", "Spieler sechs eröffnet hinten. Über Spieler vier geht der Ball weiter zu Spieler drei. Hier hinten hat jeder einen Gegenspieler, also schnell spielen.",
     ps("b1", fuss("n4")), mv("r14", [55, 48], delay=0.3), ps("b1", fuss("n3"), after=True)),
   S("Steil in die Mittelzone", "Spieler acht zeigt sich in der Mitte und schaut zum Ball. Spieler drei spielt flach und steil zu ihm. Wer in seiner Zone angespielt wird, darf weiter nach vorn.",
     bl("n8", [33.3, 45.4]), ps("b1", fuss("n8"), after=True)),
   S("Aufdrehen, raus nach außen", "Erst jetzt dreht Spieler acht auf, und der Blick geht nach außen. Spieler dreizehn kommt zu spät. Der Ball geht raus zu Spieler elf.",
     bl("n8", [31.2, 33.1], von=[33.3, 45.4], dauer=1.3), drehen("n8", POS["n11"], delay=0.4), mv("r13", [45, 33], delay=0.6), ps("b1", fuss("n11"), after=True)),
   S("Pass in die Endzone", "Spieler neun kommt kurz und schaut zum Ball. Spieler elf spielt ihn in der Endzone an und läuft sofort hinterher. Auf der anderen Seite startet Spieler sieben. Die beiden Verteidiger gehen mit.",
     mv("n9", [52, 17]), bl("n9", [33.4, 24.4], delay=0.5), ps("b1", [52.6, 17.6], after=True),
     mv("n11", [29, 11], after=True), mv("r2", [34, 12], after=True), mv("n7", [78, 12], delay=1.2), mv("r5", [72, 11], delay=1.5)),
   S("Aufdrehen, Abschluss: Punkt", "Spieler neun dreht auf und hat freie Bahn. Er schießt flach ins Eck, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu den drei Spielern hinten.",
     bl("n9", SCHUSS, von=[33.4, 24.4], dauer=1.3), drehen("n9", SCHUSS, delay=0.4), ps("b1", SCHUSS, after=True))]},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Spieler von hinten darf mit Ball in die Mittelzone dribbeln.", "Vier gegen zwei in der Mitte",
    "Jetzt darf ein Spieler von hinten mit Ball in die Mittelzone dribbeln. Dann stehen dort vier gegen zwei. Team Rot zieht sich zurück und stellt den Raum zu, statt sofort zu pressen. Team Neon hat so mehr Zeit am Ball.",
    sp(), [B("b1", *fuss("n4"))] + ERSATZ,
    [S("Kopf hoch, Platz sehen", "Spieler vier hat den Ball. Vor ihm ist frei, Spieler vierzehn steht zu weit weg. Er schaut kurz hoch und dribbelt los in die Mittelzone.",
       bl("n4", [46, 38]), dr("n4", "b1", [44, 39], after=True), mv("n8", [58, 33], delay=0.8)),
     S("Vier gegen zwei ausspielen", "Jetzt sind es in der Mitte vier gegen zwei. Spieler dreizehn und Spieler zwölf ziehen sich zurück. Spieler vier spielt zu Spieler acht, und der spielt sofort in die Endzone auf Spieler neun.",
       mv("r13", [42.5, 25]), mv("r12", [66, 24]), ps("b1", [58.6, 33.6], delay=0.6), ps("b1", fuss("n9"), after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: In jeder Zone stehen immer mindestens zwei Spieler von jedem Team.", "Zwei Spieler in jeder Zone",
    "Jedes Team hat in jeder Zone immer mindestens zwei Spieler. Geht einer nach vorn, rückt ein anderer nach. So muss jeder wissen, wo seine Mitspieler stehen. Die Abstände bleiben gut, und hinten ist immer einer zum Absichern da.",
    sp(n7=(77, 17)), [B("b1", *fuss("n3"))] + ERSATZ,
    [S("Einer geht vor, einer rückt nach", "Spieler drei spielt hoch zu Spieler elf. Gleichzeitig startet Spieler acht in die Endzone. Jetzt fehlt in der Mitte einer. Spieler vier schaut nach vorn, sieht das und rückt sofort nach.",
       ps("b1", fuss("n11")), mv("n8", [50, 19], delay=0.3), bl("n4", [50, 36], delay=0.8), mv("n4", [44, 39], after=True)),
     S("In die Endzone: Punkt", "Spieler elf spielt in die Endzone auf Spieler acht. Der legt quer zu Spieler neun, und Spieler neun schießt. Das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 19.6]), ps("b1", fuss("n9"), after=True), ps("b1", SCHUSS, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
