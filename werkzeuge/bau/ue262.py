import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK 2 (im PDF GK-P2, U12-U14, Torwarttraining): Goalkeeper Quick Feet Shot Stopping (Develop Reactions and Shot Stopping).
# 45 x 18 Yards am Tor = Feld x 8-92, y 5-49 (41 x 16 m), quer wie im Video (im PDF hochkant, Tor links): Tor oben (Jugendtor),
# davor der Torraum. Zwei Torhüter, jeder in einem Viereck aus vier Hütchen. Abweichung: Im Original vier Farben (rot, blau,
# weiß, gelb), hier zwei: diagonal gleich, orange und neongelb. Der Trainer ruft deshalb "Orange!", "Neon!" oder "Alle!"
# statt Farbkombinationen. Links und rechts außen je eine Koordinationsleiter (im Original schräg, hier senkrecht, von unten
# nach oben durchlaufen) und je zwei Stangen am Pfosten (Slalom). Abweichung: Im Original zwei Trainer; hier volleyt links der
# Trainer (genau einer) und rechts Spieler sieben von Team Neon. Der Trainer ruft und schießt den Reaktionsball.
# Keine Punkte (Technik und Reaktion), Ziel: jeden Ball festhalten.
# Sichtkegel aus dem PDF/Ton ("on their toes while waiting for coaches calls", Bereitschaftsstellung): beim Warten an den Pfosten
# schauen beide Torhüter zum Trainer. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Steigerung: längere Rufe wie im Video ("White, yellow and blue"), hier "Alle!" für alle vier Hütchen.
T = P("T", "c", 37, 43, "T")
POS = {"k1": (38, 22.5), "k2": (62, 22.5), "n7": (63, 43)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "t", x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 38.6, 46.5), B("s2", 35, 46.5)]
def baelle(b1=(37.6, 43.6), ersatz=ERSATZ): return [B("b1", *b1), B("b2", 63.6, 43.6)] + ersatz
LINES = [rect(8, 5, 84, 44), rect(30, 5, 40, 13)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
def viereck(x): return [C(x - 6, 16), C(x + 6, 16, "neon"), C(x - 6, 29, "neon"), C(x + 6, 29)]
CONES = viereck(38) + viereck(62) + [leiter(20, 24, senkrecht=True), leiter(80, 24, senkrecht=True)] \
      + [C(28, 10, shape="stange"), C(34, 10, shape="stange"), C(66, 10, shape="stange"), C(72, 10, shape="stange")]
def weg(who, punkte, erst_after=False):
    return [mv(who, punkte[0], after=erst_after or None)] + [mv(who, p, after=True) for p in punkte[1:]]
def rechts(punkte, dx=24): return [[x + dx, y] for x, y in punkte]
def gespiegelt(punkte): return [[100 - x, y] for x, y in punkte]
ORANGE = [[34, 18.5], [38, 22.5], [42, 26.5], [38, 22.5]]
ALLE = [[34, 18.5], [42, 18.5], [42, 26.5], [34, 26.5], [38, 22.5]]
RAUS = [[38, 34], [20, 34], [20, 14], [24, 14], [28, 14], [31, 10], [34, 6.5], [39, 11]]
L_TW, R_TW = [38.6, 23.1], [62.6, 23.1]

u = {"title": "Hütchen tippen, Leiter, Parade", "code": "UE-262", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 3, "field_size": "41 x 16 m",
 "description": "Zwei Torhüter stehen vor dem Tor in je einem Viereck aus vier Hütchen. Der Trainer ruft eine Farbe, und die Torhüter tippen diese Hütchen an und fangen in der Mitte einen Volley. Ruft er „Raus!“, sprinten beide durch die Leiter und um die Stangen an ihren Pfosten. Dort warten sie auf den Zehenspitzen, bis der Trainer einen von ihnen aufruft und quer durchs Tor schießt.",
 "organisation": ["Aufbauen: Ein Feld von 41 mal 16 Metern vor einem Jugendtor mit Torraum. Zwei Vierecke aus je vier Hütchen, außen je eine Leiter, am Torraum je zwei Stangen.",
  "Verteilen: In jedem Viereck ein Torwart. Unten stehen der Trainer links und Spieler sieben rechts mit Bällen.",
  "Ablauf: Der Trainer ruft eine Farbe. Die Torhüter tippen die Hütchen an, fangen in der Mitte einen Volley und rollen ihn zurück. Bei „Raus!“ geht es durch Leiter und Stangen an den Pfosten. Dann ruft der Trainer „Rechts!“ oder „Links!“, und dieser Torwart hält den Schuss quer durchs Tor.",
  "Wechsel: Danach gehen beide zurück in ihr Viereck, und es geht von vorn los. Ziel: jeden Ball festhalten."],
 "organisation_show": ORG,
 "coaching_points": ["Beim Warten auf den Zehenspitzen stehen und zum Trainer schauen", "Schnell auf den Ruf reagieren", "Mit sauberen, schnellen Schritten durch die Leiter und quer durchs Tor", "Den Volley mit guter Technik fangen und festhalten"],
 "materials": ["8 Hütchen", "2 Koordinationsleitern", "4 Stangen", "1 Jugendtor", "Viele Bälle"],
 "access": "abo", "hidden": False,
 "say_intro": "Hütchen tippen, Leiter, Parade. Zwei Torhüter reagieren auf die Rufe des Trainers und am Ende hält einer von ihnen einen Schuss auf die andere Torseite.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": baelle(),
  "steps": [
   S("Orange!", "Der Trainer ruft: Orange! Beide Torhüter sprinten gleichzeitig zu ihren zwei orangen Hütchen, tippen sie an und kommen zurück in die Mitte.",
     *weg("k2", rechts(ORANGE)), *weg("k1", ORANGE)),
   S("Volley fangen", "Der Trainer spielt dem linken Torwart einen Volley zu, Spieler sieben dem rechten. Beide fangen den Ball und halten ihn fest.",
     ps("b1", L_TW), ps("b2", R_TW)),
   S("Zurückrollen", "Beide rollen den Ball zurück. Dann ruft der Trainer die nächste Farbe.",
     ps("b1", [37.6, 43.6]), ps("b2", [63.6, 43.6])),
   S("Raus!", "Jetzt ruft der Trainer: Raus! Beide sprinten nach außen, laufen durch die Leiter und im Slalom um die zwei Stangen an ihren Pfosten.",
     *weg("k2", gespiegelt(RAUS)), *weg("k1", RAUS)),
   S("Auf den Zehenspitzen", "Dort warten beide auf den Zehenspitzen und schauen zum Trainer. Der Trainer geht mit dem Ball in die Mitte.",
     dr("T", "b1", [50, 38]), bl("k1", [46, 28]), bl("k2", [54, 28])),
   S("Rechts! Gehalten", "Der Trainer ruft: Rechts! und schießt quer zur anderen Seite. Der rechte Torwart reagiert sofort, läuft mit schnellen Seitschritten durchs Tor und hält den Ball. Dann gehen beide zurück in ihr Viereck, und es geht von vorn los.",
     mv("k2", [48, 7.5]), ps("b1", [48.6, 8.1], delay=0.3))],
  "dims": dims(8, 92, 5, 49, "41 m", "16 m", rx=97)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Auf den Zehenspitzen warten.", "Bereit an den Pfosten",
    "Wer auf den Fersen steht, ist zu spät. Beide Torhüter warten an ihren Pfosten auf den Zehenspitzen, die Hände vorn, und schauen zum Trainer. So reagieren sie sofort auf den Ruf und kommen schnell quer durchs Tor.",
    sp(k1=(39, 11), k2=(61, 11))[:3] + [P("T", "c", 50, 38, "T")], baelle(b1=(50.6, 38.6), ersatz=[B("s1", 51.6, 41.5), B("s2", 48, 41.5)]),
    [S("Bereit stehen", "Beide stehen auf den Zehenspitzen an ihren Pfosten und schauen zum Trainer.",
       bl("k1", [46, 28]), bl("k2", [54, 28])),
     S("Links! Gehalten", "Der Trainer ruft: Links! und schießt auf die rechte Seite. Der linke Torwart reagiert sofort, läuft mit Seitschritten durchs Tor und hält den Ball.",
       mv("k1", [52, 7.5]), ps("b1", [52.6, 8.1], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Alle vier Hütchen.", "Alle vier Hütchen",
    "Jetzt ruft der Trainer auch „Alle!“. Dann tippen die Torhüter alle vier Hütchen ihres Vierecks an, bevor der Volley kommt. So müssen sie sich gut merken, was gerufen wurde, und kommen trotzdem schnell bereit in die Mitte.",
    sp(), baelle(),
    [S("Alle!", "Der Trainer ruft: Alle! Beide Torhüter tippen gleichzeitig alle vier Hütchen an und kommen zurück in die Mitte.",
       *weg("k2", rechts(ALLE)), *weg("k1", ALLE)),
     S("Volley fangen", "Sofort kommen die Volleys. Beide fangen den Ball, halten ihn fest und rollen ihn zurück. Dann folgt der nächste Ruf.",
       ps("b1", L_TW), ps("b2", R_TW), ps("b1", [37.6, 43.6], delay=0.75), ps("b2", [63.6, 43.6], delay=0.75))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
