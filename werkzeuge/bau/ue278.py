import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P5 (U12-U14, Einzeltraining): Drive To Finish on the Angle (Ordner "Drive To Finish on the Angle 1 to 1- P5").
# 15 x 20 Yards = Feld x 25-75, y 12-51 (18 x 14 m). Gedreht (90 Grad gegen den Uhrzeigersinn): im Original stehen die drei
# Minitore rechts und die Hütchen links; hier Minitore oben, Puppen in der Mitte, Hütchen unten. Die obere Reihe des Originals
# ist hier die linke Bahn, die untere Reihe die rechte Bahn. Trainer C (im Original rechts neben den Toren) steht hier rechts
# oben neben dem Feld. Spieler P -> Spieler sieben (Team Neon), startet an der rechten Bahn mit Ball; ein Ball am linken
# Hütchen, zwei Bälle am mittleren Hütchen (zusammen vier Bälle).
# Ablauf aus dem Video: Jeder Ball geht schräg zur Puppe der Nachbarbahn, scharf um sie herum und zurück schräg in das Minitor
# der eigenen Startbahn (rechts -> mittlere Puppe -> rechtes Tor; Mitte -> linke Puppe -> mittleres Tor; links -> mittlere
# Puppe -> linkes Tor; Mitte -> rechte Puppe -> mittleres Tor, im Video an den Pfosten und Abpraller direkt verwandelt).
# Keine Wertung im Original: Ziel statt Punkte (vier Bälle, möglichst viele Treffer).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
# Fassungen: beide Coaching-Punkte aus PDF Seite 2 (Genauigkeit vor Härte; Abpraller vom Pfosten direkt verwandeln).
T = P("T", "c", 84, 14, "T")
POS = {"n7": (64, 48.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 87, 17), B("s2", 87, 11)]
LINES = [rect(25, 12, 50, 39)]
TORE = [{"x": x, "y": 12, "side": "top"} for x in (33.5, 50, 66.5)]
CONES = [C(33.5, 31, shape="stange"), C(50, 31, shape="stange"), C(66.5, 31, shape="stange"),
         C(33.5, 46), C(50, 46), C(66.5, 46)]
B2, B3, B4 = B("b2", 36.6, 46.6), B("b3", 47, 46.6), B("b4", 53.6, 46.6)
def weg(who, ball, pkt): return [dr(who, ball, pkt[0])] + [dr(who, ball, p, after=True) for p in pkt[1:]]

u = {"title": "Schräg um die Puppe abschließen", "code": "UE-278", "kind": "Übungsform",
 "focuses": ["Torschuss", "Dribbling", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 14 m",
 "description": "Ein Spieler trainiert allein mit dem Trainer den Abschluss aus spitzem Winkel. Er dribbelt schräg zu einer Puppe, dreht scharf um sie herum und schießt schräg ins Minitor seiner Startbahn. Dann sprintet er zurück und holt den nächsten Ball. Erst kommt die Genauigkeit, die Härte kommt später.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern mit drei Bahnen. Oben drei Minitore, in der Mitte drei Puppen oder Stangen, unten drei Hütchen.",
  "Verteilen: Der Spieler startet an der rechten Bahn mit Ball. Ein Ball liegt am linken Hütchen, zwei Bälle am mittleren. Der Trainer steht rechts neben dem Feld.",
  "Ablauf: Der Spieler dribbelt schräg zur Puppe der Nachbarbahn, dreht scharf um sie herum und schießt schräg ins Minitor seiner Startbahn. Dann sprintet er zum nächsten Ball.",
  "Wechsel: Sind alle vier Bälle geschossen, ist die Runde vorbei. Der Spieler holt die Bälle zurück, macht kurz Pause und startet die nächste Runde."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball mit Tempo eng am Fuß führen", "Scharf um die Puppe drehen und sofort abschließen", "Erst genau schießen, später fester", "Mal mit links, mal mit rechts schießen"],
 "materials": ["3 Minitore", "3 Puppen oder Stangen", "3 Hütchen", "4 Bälle", "2 Ersatzbälle beim Trainer"],
 "access": "abo", "hidden": True,
 "say_intro": "Schräg um die Puppe abschließen. Mit Tempo zur Puppe dribbeln, scharf drehen und aus spitzem Winkel genau ins Minitor schießen.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 64.6, 49.1), B2, B3, B4] + ERSATZ,
  "steps": [
   S("Schräg zur Puppe", "Spieler sieben dribbelt mit Tempo schräg nach links zur mittleren Puppe. Er läuft links an ihr vorbei.",
     *weg("n7", "b1", [[58, 42], [46, 37], [44.5, 31]])),
   S("Scharfe Drehung", "Hinter der Puppe dreht er scharf nach rechts. Jetzt steht er schräg vor dem rechten Minitor.",
     *weg("n7", "b1", [[47, 26], [52, 24.5]])),
   S("Abschluss", "Spieler sieben schießt aus dem spitzen Winkel genau ins rechte Minitor. Treffer!",
     ps("b1", [66.5, 12.3])),
   S("Nächster Ball", "Dann sprintet er zurück und holt den nächsten Ball am mittleren Hütchen. So geht es weiter, bis alle vier Bälle geschossen sind. Dann holt Spieler sieben die Bälle zurück, macht kurz Pause und startet die nächste Runde.",
     mv("n7", [57, 33]), mv("n7", [46.4, 46], after=True))],
  "dims": dims(25, 75, 12, 51, "18 m", "14 m", rx=79)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst genau, dann fest.", "Genau vor fest",
    "Aus spitzem Winkel ist das Tor klein. Der Spieler schießt deshalb lieber flach und genau als fest. Wer zu fest schießt, verfehlt das Minitor oft. Die Härte kommt erst, wenn die Schüsse sicher sitzen.",
    sp(n7=(46.4, 46)), [B3, B4, B2] + ERSATZ,
    [S("Zur linken Puppe", "Spieler sieben dribbelt vom mittleren Hütchen schräg zur linken Puppe und läuft links an ihr vorbei.",
       *weg("n7", "b3", [[40, 39], [29, 33], [29, 27]])),
     S("Drehen und genau schießen", "Er dreht scharf nach rechts und schießt flach und genau ins mittlere Minitor. Lieber genau als fest.",
       *weg("n7", "b3", [[34, 24.5]]), ps("b3", [50, 12.3], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Trifft der Ball den Pfosten, sofort nachsetzen.", "Abpraller direkt verwandeln",
    "Prallt der Ball vom Pfosten zurück ins Feld, bleibt der Spieler wach. Er reagiert schnell und schießt den Abpraller direkt mit dem ersten Kontakt ins Tor. So lernt er, auch nach einem Fehlschuss ruhig zu bleiben.",
    sp(n7=(53, 46)), [B4] + ERSATZ,
    [S("Zur rechten Puppe", "Spieler sieben nimmt den letzten Ball am mittleren Hütchen und dribbelt schräg zur rechten Puppe. Er läuft rechts an ihr vorbei.",
       *weg("n7", "b4", [[60, 39], [71, 33], [71, 27]])),
     S("An den Pfosten", "Er dreht scharf nach links und schießt aufs mittlere Minitor. Der Ball prallt vom Pfosten zurück ins Feld.",
       *weg("n7", "b4", [[66, 24.5]]), ps("b4", [54, 12.5], after=True), ps("b4", [58.6, 20.6], after=True)),
     S("Direkt nachsetzen", "Spieler sieben reagiert sofort, läuft in den Abpraller und schießt ihn direkt ins mittlere Minitor. Treffer!",
       mv("n7", [58, 20]), ps("b4", [50, 12.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
