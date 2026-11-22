import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 1 to 1-P17 (U12-U14, Einzeltraining): What Type of Cross to Deliver - Wingers. 50 x 30 Yards = Feld x 15-85, y 10-52 (46 x 27 m).
# Ausrichtung wie im PDF (Tor oben, Flügelspieler rechts, nicht gedreht). Großes Tor im Hintergrund weggelassen (kein Torwart,
# Ziel sind die Minitore); Strafraum als gestrichelte Linie. Blauer Spieler -> Spieler sieben (Team Neon, Flügelspieler).
# Vier Dummys an der Strafraumlinie (im Original auf der Linie, hier knapp davor wegen der Minitore), ein Dummy außen als
# gegnerischer Außenverteidiger. Minitore im Strafraum mit Öffnung nach rechts (zum Flügel). Ballhaufen -> zwei Ersatzbälle.
# Reine Technikübung ohne Wertung: Ziel statt Punkte.
# Sichtkegel: Im Video (0:16-0:30 und 0:50-1:06) ist vor der Flanke ein Kegel vom Flügelspieler in den Strafraum
# eingezeichnet, PDF "enhancing vision", "Decision-making", Ton "Sell the cross using your body shape and eyes"
# -> bl() vor jeder Flanke Richtung Strafraum, in der Steigerung zwei Blicke (hinterer Pfosten, dann Strafraumrand).
# Fassungen: Coaching-Punkt = scharfe, flache Flanke vor das Tor (PDF Seite 2 links, Video 0:16-0:32, Zone im Original grau,
# hier neon). Steigerung = Dummys und Minitore umgestellt, Lupfer an den hinteren Pfosten oder Rückpass an den
# Strafraumrand (PDF Seite 2 rechts, Video 0:33-1:10). Gezeigt wird der angetäuschte Rückpass, der Lupfer steht im Text.
# Abweichung: Im Original werden die Minitore umgestellt. Fassungen dürfen Tore nur ergänzen, deshalb bleiben die beiden
# Minitore der Mitte stehen und werden von zwei Dummys zugestellt; dazu kommen die Minitore am hinteren Pfosten und am Strafraumrand.
T = P("T", "c", 63, 47, "T")
POS = {"n7": (80.5, 41)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 59.5, 49.5), B("s2", 57.5, 50.5)]
BALL_T = [63.6, 47.6]
STRAFRAUM = [line(30, 10, 30, 28), line(30, 28, 71, 28), line(71, 28, 71, 10)]
LINES = [rect(15, 10, 70, 42)] + STRAFRAUM
TORE = [{"x": 47.5, "y": 14, "side": "left"}, {"x": 47.5, "y": 23, "side": "left"}]
DUMMYS = [C(38.5, 30, shape="stange"), C(48, 30, shape="stange"), C(57, 30, shape="stange"), C(65.5, 30, shape="stange"),
          C(72, 33.5, shape="stange")]
# Steigerung: Dummys und Minitore umgestellt (eigene Hütchen, alle mit id)
DUMMYS2 = [C(53, 14, shape="stange", id="d1"), C(53, 23, shape="stange", id="d2"), C(60, 18.5, shape="stange", id="d3"),
           C(72, 33.5, shape="stange", id="d4")]
TORE2 = TORE + [{"x": 35, "y": 18, "side": "left"}, {"x": 52.5, "y": 31, "side": "bottom"}]

u = {"title": "Flankenarten vom Flügel", "code": "UE-295", "kind": "Übungsform",
 "focuses": ["Passspiel", "Dribbling", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Einzeltraining"], "duration_minutes": 15, "players_min": 1, "players_max": 2,
 "field_size": "46 x 27 m",
 "description": "Ein Flügelspieler übt verschiedene Flanken. Der Trainer passt nach außen, der Spieler zieht außen an einem Dummy vorbei und flankt in eines von zwei Minitoren im Strafraum. Vier Dummys stehen für die Verteidiger, die Minitore für die Mitspieler. Vor jeder Flanke hebt er den Kopf und wählt die passende Flanke.",
 "organisation": ["Aufbauen: Ein Feld von 46 mal 27 Metern mit Strafraum. Vier Dummys stehen an der Strafraumlinie, zwei Minitore im Strafraum, ein Dummy außen als Außenverteidiger.",
  "Verteilen: Spieler sieben steht rechts außen. Der Trainer steht tiefer in der Mitte mit vielen Bällen.",
  "Ablauf: Der Trainer passt nach außen. Spieler sieben nimmt den Ball mit, zieht außen am Dummy vorbei, hebt den Kopf und flankt in eines der Minitore.",
  "Wechsel: Nach jeder Flanke läuft der Spieler zurück an den Start, und der Trainer spielt den nächsten Ball. Sind alle Bälle gespielt, gibt es eine Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Scharfe Flanke: mit Tempo und den Oberkörper über dem Ball, damit sie flach bleibt",
  "Gelupfte Flanke: weich und hoch an den hinteren Pfosten, damit die Mitspieler hinkommen",
  "Rückpass: erst mit dem Körper die Flanke antäuschen, dann scharf zurücklegen",
  "Vor der Flanke den Kopf heben und die passende Flanke wählen"],
 "materials": ["5 Dummys", "2 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Flankenarten vom Flügel. Spieler sieben zieht am Außenverteidiger vorbei und flankt in die Minitore im Strafraum.",
 "board": {"lines": LINES, "goals": TORE, "cones": DUMMYS, "players": sp(), "balls": [B("b1", *BALL_T)] + ERSATZ,
  "steps": [
   S("Pass nach außen", "Der Trainer steht tiefer in der Mitte und passt nach außen zu Spieler sieben.",
     ps("b1", [81.1, 41.6])),
   S("Außen am Dummy vorbei", "Spieler sieben nimmt den Ball nach vorn mit. Er dribbelt auf den Dummy zu und zieht dann außen an ihm vorbei. Der Dummy ist der gegnerische Außenverteidiger.",
     dr("n7", "b1", [76.5, 37.5]), dr("n7", "b1", [80, 27.5], after=True)),
   S("Kopf hoch", "Vor der Flanke hebt Spieler sieben den Kopf und schaut in den Strafraum. Wo ist Platz hinter den Verteidigern?",
     bl("n7", [61, 20])),
   S("Flanke ins Minitor: Ziel", "Er flankt den Ball über die Dummys ins obere Minitor. Das ist das Ziel. Dann läuft Spieler sieben zurück an den Start, und der Trainer spielt den nächsten Ball.",
     ps("b1", [48, 14], bend=5), mv("n7", [80.5, 41], after=True))],
  "dims": dims(15, 85, 10, 52, "46 m", "27 m", rx=91)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die scharfe, flache Flanke.", "Scharf und flach flanken",
    "Die scharfe Flanke geht flach vor dem Tor entlang, in den Raum hinter den Verteidigern. Dafür bleibt der Oberkörper über dem Ball. Der Ball springt vor dem Minitor auf. So kommen Torwart und Verteidiger nur schwer an den Ball.",
    sp(n7=(80, 24)), [B("b1", 80.6, 24.6)] + ERSATZ,
    [S("Kopf hoch", "Spieler sieben ist am Dummy vorbei. Er hebt den Kopf und sieht: Hinter den Verteidigern ist Platz.",
       bl("n7", [61, 21])),
     S("Scharf und flach: Ziel", "Er bleibt mit dem Oberkörper über dem Ball und flankt scharf und flach. Der Ball springt in der Zone vor dem Tor auf und geht ins untere Minitor. Das ist das Ziel. Dann kommt der nächste Ball.",
       ps("b1", [48, 23], bend=-2))],
    lines=LINES + [{"type": "zone", "x": 50, "y": 16, "w": 16, "h": 10}]),
  V("Steigerung", "Und jetzt die Steigerung: Die Mitte ist zu. Lupfer an den hinteren Pfosten oder Rückpass.", "Lupfer oder Rückpass",
    "Jetzt stehen Dummys vor den Minitoren in der Mitte. Dazu kommen zwei Minitore: eines am hinteren Pfosten, eines am Rand des Strafraums. Spieler sieben dribbelt bis zur Grundlinie. Dann wählt er: ein weicher, hoher Lupfer an den hinteren Pfosten oder ein angetäuschter, scharfer Rückpass an den Strafraumrand.",
    sp(n7=(79, 38)), [B("b1", *BALL_T)] + ERSATZ,
    [S("Bis zur Grundlinie", "Der Trainer passt nach außen. Spieler sieben zieht außen am Dummy vorbei und dribbelt bis an die Grundlinie.",
       ps("b1", [79.6, 38.6]), dr("n7", "b1", [79.5, 26], after=True), dr("n7", "b1", [74.5, 14], after=True)),
     S("Zwei Blicke", "Jetzt hebt er den Kopf. Er schaut zum hinteren Pfosten und dann zum Rand des Strafraums.",
       bl("n7", [55, 16]), bl("n7", [60, 27], after=True)),
     S("Antäuschen, zurücklegen: Ziel", "Diesmal wählt Spieler sieben den Rückpass. Er täuscht die Flanke mit dem Körper an und legt den Ball dann scharf zurück ins Minitor am Strafraumrand. Das ist das Ziel. Beim nächsten Ball probiert er den Lupfer an den hinteren Pfosten.",
       ps("b1", [52.5, 31.5]))],
    cones=DUMMYS2, goals=TORE2)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
