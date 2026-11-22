import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P16 (U12-U14, Einzeltraining): How to Beat Your Fullbacks - Wingers. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 m).
# Ausrichtung wie im Original (nicht gedreht): oben ein Minitor (nach vorn), links zwei Minitore zur Seite (Flanken-Ziele).
# Spieler P (orange) -> Spieler sieben (Team Neon, Flügelspieler rechts). Zwei Dummys (Mannequins) als Stangen: oben rechts
# der Außenverteidiger, in der Mitte ein zweiter. Das schräge zweite Seitentor ist hier ein normales Seitentor (nach rechts offen).
# Keine Wertung im Original: Ziel statt Punkte (Ball ins Minitor bringen).
# Fassungen: Coaching-Punkt aus PDF und Ton (Täuschung mit Schulter und Hüfte, explosiv raus, ein halber Meter reicht,
# Rückpass ins zweite Seitentor) und Steigerung 1 aus dem PDF (außen antäuschen, innen rein, Schuss ins obere Tor).
# Steigerung 2 im Original (Seite wechseln, linker Flügel) nur im Text unter Wechsel erwähnt (Tore dürfen in Fassungen
# nicht gespiegelt werden).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft; „use shoulders“ meint die Körpertäuschung, kein Schauen).
T = P("T", "c", 58.5, 49, "T")
POS = {"n7": (70, 42)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 51.5), B("s2", 51.5, 53)]
BAELLE = [B("b1", 59.1, 49.6)] + ERSATZ
LINES = [rect(25, 5, 50, 50)]
CONES = [C(65.5, 26.5, shape="stange"), C(55, 37, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top"}, {"x": 27, "y": 13, "side": "left"}, {"x": 33, "y": 30, "side": "left"}]

u = {"title": "Täuschen, vorbei und flanken", "code": "UE-281", "kind": "Übungsform",
 "focuses": ["Dribbling", "Ballannahme", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Flügelspieler übt mit dem Trainer, wie er am Außenverteidiger vorbeikommt. Ein Dummy ist der Gegenspieler. Der Spieler nimmt den Pass des Trainers auf dem hinteren Fuß an, dribbelt auf den Dummy zu und täuscht innen an. Dann geht er außen vorbei und flankt in eines der zwei seitlichen Minitore.",
 "organisation": ["Aufbauen: Ein Feld von achtzehn mal achtzehn Metern. Oben in der Mitte ein Minitor, links zwei Minitore, die zur Seite offen sind. Rechts oben steht ein Dummy als Außenverteidiger, in der Mitte ein zweiter Dummy.",
  "Verteilen: Der Spieler startet unten rechts als Flügelspieler. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Der Trainer passt auf den hinteren Fuß. Der Spieler dribbelt auf den Dummy zu, täuscht innen an und geht außen vorbei. Dann flankt er in eines der zwei Minitore links.",
  "Wechsel: Der Spieler holt sich sofort den nächsten Ball, bis alle Bälle gespielt sind. Danach wird das Feld gespiegelt, und er übt auf dem linken Flügel mit dem linken Fuß."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball auf dem hinteren Fuß annehmen und gleich nach vorn mitnehmen", "Mit Schulter, Hüfte und Füßen täuschen, damit der Verteidiger mitgeht", "Nach der Finte explosiv mit dem Ball wegsprinten", "Auch müde noch genau flanken und schießen"],
 "materials": ["3 Minitore", "2 Dummys", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Täuschen, vorbei und flanken. Ein Flügelspieler täuscht den Dummy innen an, geht außen vorbei und flankt ins Minitor.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Pass auf den hinteren Fuß", "Der Trainer passt Spieler sieben den Ball auf den hinteren Fuß. Spieler sieben ist der Flügelspieler, der Dummy oben rechts ist sein Gegenspieler.",
     ps("b1", [70.6, 42.6])),
   S("Auf den Dummy zu", "Spieler sieben nimmt den Ball mit und dribbelt direkt auf den Dummy zu.",
     dr("n7", "b1", [67, 33])),
   S("Innen antäuschen, außen vorbei", "Er täuscht nach innen an. Dann legt er den Ball nach außen und sprintet am Dummy vorbei.",
     dr("n7", "b1", [64.5, 32.5]), dr("n7", "b1", [70.5, 30], after=True), dr("n7", "b1", [71.5, 21], after=True)),
   S("Flanke ins Minitor", "Spieler sieben flankt den Ball mit Schwung ins linke obere Minitor. Ziel ist, jede Flanke ins Minitor zu bringen. Dann läuft er zurück und ist mit dem nächsten Ball gleich wieder dran.",
     ps("b1", [28, 13.5], bend=-8), mv("n7", [70, 42], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Täuschen und explosiv weg.", "Täuschen und explosiv weg",
    "Die Finte kommt aus Schulter und Hüfte, damit der Verteidiger mitgeht. Danach sofort explosiv weg, den Ball eng am Fuß. Der Spieler muss nicht ganz vorbei sein: Ein halber Meter Platz reicht für die Flanke.",
    sp(n7=(67, 33)), [B("b1", 67.6, 33.6)] + ERSATZ,
    [S("Finte mit dem Körper", "Spieler sieben steht vor dem Dummy. Er täuscht mit Schulter und Hüfte nach innen an.",
       dr("n7", "b1", [64.5, 32.5])),
     S("Explosiv nach außen", "Mit dem Außenrist legt er den Ball nach außen und ist mit dem nächsten Schritt weg. Ein halber Meter Platz reicht schon.",
       dr("n7", "b1", [70.5, 30]), dr("n7", "b1", [71.5, 18], after=True)),
     S("Rückpass ins Minitor", "Sofort spielt er den Ball flach und scharf zurück ins untere Minitor links. Dann holt er sich den nächsten Ball.",
       ps("b1", [33.6, 30.3]))]),
  V("Steigerung", "Und jetzt die Steigerung: Außen antäuschen, innen rein.", "Außen antäuschen, innen rein",
    "Jetzt täuscht der Spieler außen an und zieht nach innen. Er geht innen am Dummy vorbei und schießt mit Schnitt ins obere Minitor. So übt er enge Ballführung und einen genauen Abschluss.",
    sp(), BAELLE,
    [S("Pass und auf den Dummy", "Der Trainer passt auf den hinteren Fuß. Spieler sieben dribbelt sofort auf den Dummy zu.",
       ps("b1", [70.6, 42.6]), dr("n7", "b1", [67, 33], after=True)),
     S("Außen antäuschen", "Er zieht den Ball nach außen, als ob er außen vorbei will.",
       dr("n7", "b1", [69.5, 32])),
     S("Nach innen ziehen", "Dann zieht er den Ball scharf nach innen und geht innen am Dummy vorbei.",
       dr("n7", "b1", [60, 31]), dr("n7", "b1", [57, 22], after=True)),
     S("Schuss mit Schnitt", "Spieler sieben schießt mit Schnitt ins obere Minitor. Ziel ist, das Minitor genau zu treffen. Dann ist er mit dem nächsten Ball wieder dran.",
       ps("b1", [50.6, 5.8], bend=-5))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
