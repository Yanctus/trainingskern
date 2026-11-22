import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P30 (U12-U14, Einzeltraining): Link Up Play - ST. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 x 18 m).
# Ausrichtung wie im PDF (Dummy oben in der Mitte, Trainer unten, zwei Minitore unten links und rechts), nicht gedreht.
# Die Minitore stehen im Original schräg zur Mitte gedreht; hier gerade mit Öffnung nach oben (schräge Tore gibt es nicht).
# Blauer Spieler -> Spieler neun (Team Neon, Stürmer). Dummy als Stange. Ballhaufen beim Trainer nur als zwei Ersatzbälle.
# Ablauf nach PDF und Video (0:06-0:40): Doppelbewegung am Dummy, Trainer passt; Zuruf „Prallen“ (Bounce) = direkt zurück,
# gehobene Hand = Ball ins Minitor auf dieser Seite ablegen; danach zurück an den Dummy. Reine Technikübung: Ziel statt Punkte.
# Sichtkegel: PDF/Ton „Scan quickly to recognise the coach's signal before receiving“, im Video (0:30-0:40) ist ein Kegel vom
# Stürmer nach unten zum Trainer eingezeichnet -> bl() vor jeder Annahme Richtung Trainer.
# Fassungen: Coaching-Punkt aus PDF (früh schauen, mit beiden Füßen ablegen: linke Hand -> linkes Minitor), Steigerung aus PDF
# Seite 2 und Video (0:52-1:10): Zuruf „Drehen“ = Prallpass, außen öffnen, annehmen, über die Linie hinter dem Dummy dribbeln,
# zurück zum Trainer passen. Die Linie (im Video gestrichelt nahe der oberen Feldkante) erscheint nur in der Steigerung.
T = P("T", "c", 52, 50, "T")
POS = {"n9": (45, 17)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 46.5, 52), B("s2", 44, 54)]
BALL_T = [52.6, 50.6]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 32, "y": 46, "side": "bottom"}, {"x": 68, "y": 46, "side": "bottom"}]
CONES = [C(52, 13, shape="stange")]
AN = [51.5, 22]
AN_B = [52.1, 22.6]

u = {"title": "Stürmer legt auf Zeichen ab", "code": "UE-283", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 1,
 "field_size": "18 x 18 m",
 "description": "Ein Stürmer übt das Ablegen mit dem Rücken zum Tor. Er löst sich mit einer Doppelbewegung vom Dummy und bekommt den Pass vom Trainer. Ruft der Trainer „Prallen“, spielt er direkt zurück, hebt der Trainer eine Hand, legt er den Ball ins Minitor auf dieser Seite. Danach geht er schnell zurück an den Dummy.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Oben in der Mitte steht ein Dummy, unten links und rechts je ein Minitor.",
  "Verteilen: Spieler neun steht links neben dem Dummy. Der Trainer steht unten in der Mitte mit vielen Bällen.",
  "Ablauf: Doppelbewegung weg vom Dummy, schauen und den Pass annehmen. Bei „Prallen“ direkt zum Trainer zurück, bei gehobener Hand ins Minitor auf dieser Seite ablegen.",
  "Wechsel: Nach jedem Ablegen schnell zurück an den Dummy. Gearbeitet wird auf Zeit mit kurzen Pausen dazwischen."],
 "organisation_show": ORG,
 "coaching_points": ["Mit einer scharfen Doppelbewegung Platz zum Dummy schaffen", "Vor der Annahme schnell zum Trainer schauen und das Zeichen erkennen", "Genau und mit dem richtigen Tempo ablegen", "Mit beiden Füßen ablegen und schnell wieder bereit sein"],
 "materials": ["1 Dummy", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Stürmer legt auf Zeichen ab. Spieler neun löst sich vom Dummy, schaut zum Trainer und legt den Ball so ab, wie der Trainer es zeigt.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *BALL_T)] + ERSATZ,
  "steps": [
   S("Doppelbewegung", "Spieler neun läuft zuerst ein Stück hinter den Dummy. Dann zieht er scharf nach vorn vor den Dummy und bietet sich an.",
     mv("n9", [46, 9]), mv("n9", AN, after=True)),
   S("Schauen und annehmen", "Spieler neun schaut zum Trainer: Ruft er etwas, oder hebt er eine Hand? Der Trainer passt zu ihm.",
     bl("n9", [52, 41]), ps("b1", AN_B, after=True)),
   S("Prallen", "Der Trainer ruft „Prallen“. Spieler neun spielt den Ball direkt zum Trainer zurück und geht wieder an den Dummy.",
     ps("b1", BALL_T), mv("n9", [46, 16], after=True)),
   S("Wieder anbieten", "Spieler neun löst sich noch einmal vom Dummy und schaut zum Trainer. Der Trainer passt und hebt die rechte Hand.",
     mv("n9", AN), bl("n9", [52, 41], after=True), ps("b1", AN_B, after=True)),
   S("Ins Minitor: Ziel", "Spieler neun nimmt den Ball mit und legt ihn ins rechte Minitor. Das ist das Ziel. Danach geht er schnell zurück an den Dummy, und die nächste Runde beginnt.",
     dr("n9", "b1", [55, 25]), ps("b1", [67.5, 45], after=True), mv("n9", [45, 17], after=True))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=81)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Früh schauen und mit beiden Füßen ablegen.", "Früh schauen, beidfüßig",
    "Der Stürmer schaut schon zum Trainer, bevor der Ball kommt. So weiß er früh, wohin er ablegen muss. Zeigt die Hand nach links, legt er mit dem linken Fuß ins linke Minitor, sonst mit dem rechten.",
    sp(n9=tuple(AN)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Früh schauen", "Spieler neun schaut zum Trainer, bevor der Pass kommt. Der Trainer hebt die linke Hand und passt.",
       bl("n9", [52, 41]), ps("b1", AN_B, after=True)),
     S("Links ablegen: Ziel", "Spieler neun legt den Ball mit dem linken Fuß ins linke Minitor. Das ist das Ziel. Dann geht er zurück an den Dummy.",
       dr("n9", "b1", [49, 25]), ps("b1", [32.5, 45], after=True), mv("n9", [45, 17], after=True))],
    ),
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft auch „Drehen“.", "Zuruf Drehen",
    "Ruft der Trainer „Drehen“, spielt der Stürmer zuerst direkt zurück. Dann öffnet er sich nach außen und nimmt den Pass mit offenem Körper an. Er dribbelt über die Linie hinter dem Dummy und passt zurück zum Trainer.",
    sp(n9=tuple(AN)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Prallen", "Der Trainer passt und ruft „Drehen“. Spieler neun spielt den Ball zuerst direkt zurück.",
       bl("n9", [52, 41]), ps("b1", AN_B, after=True), ps("b1", BALL_T, after=True)),
     S("Außen öffnen", "Spieler neun läuft nach links außen und öffnet den Körper nach vorn. Der Trainer passt in den Lauf.",
       mv("n9", [36, 25]), ps("b1", [36.6, 25.6], after=True)),
     S("Über die Linie: Ziel", "Spieler neun dribbelt schnell über die Linie hinter dem Dummy, dann nach rechts, und passt zurück zum Trainer. Das ist das Ziel. Danach geht er zurück an den Dummy.",
       dr("n9", "b1", [41, 7]), dr("n9", "b1", [60, 7], after=True), ps("b1", BALL_T, after=True))],
    lines=LINES + [line(25, 9, 75, 9)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
