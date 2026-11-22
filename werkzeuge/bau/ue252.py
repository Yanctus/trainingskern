import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P15 (U12-U14, Torwarttraining): Develop Elite Shot-Stopping Reactions. 30 x 30 Yards = Feld x 25-75, y 5-55 (27 m),
# Ausrichtung wie im PDF und Video (zwei Tore oben, zwei unten), vier Jugendtore (im PDF mittelgroße Tore, hier mit Torwart drin).
# Pink -> Team Neon (oben): Torwart n1 (PDF 1) links, Spieler 13 rechts; Gelb -> Team Rot (unten): Torwart r1 (PDF 1) rechts,
# Spieler 13 neu nummeriert zu 12 (im PDF doppelt) links. Die beiden dunklen Mittelspieler (PDF 1 und 13) -> neutrale Springer F
# (spielen für das Team am Ball). Ein Trainer links statt zwei (der rechte Trainer weggelassen); Springer rechts für den
# 3D-Abstand etwas nach außen gerückt. PDF-Progression 1 (Team mit Gegentor tauscht mit den Mittelspielern) steht in der Wertung,
# Fassung 1 ist der Coaching-Punkt aus dem Ton (rauskommen, Winkel verkürzen), Fassung 2 die PDF-Progression 2 (Abpraller).
# Sichtkegel aus dem Ton ("read the attacker's body language, particularly the eyes and hips, to anticipate"): der Torwart von
# Team Rot schaut vor dem Schuss auf den Schützen. Im Video kein Kegel eingezeichnet (nur Abwehrzonen am Ende), Richtung aus dem Sinn.
T = P("T", "c", 19, 30, "T")
POS = {"n1": (36, 9), "n13": (64, 9), "r12": (36, 51), "r1": (64, 51), "f1": (42, 33), "f2": (68, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "TW" if i in ("n1", "r1") else ("F" if i[0] == "f" else i[1:]))
            for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 15.5, 32.5), B("s2", 15.5, 27.5)]
LINES = [rect(25, 5, 50, 50)]
TORE = [{"x": 36, "y": 5, "side": "top", "size": "jugend"}, {"x": 64, "y": 5, "side": "top", "size": "jugend"},
        {"x": 36, "y": 55, "side": "bottom", "size": "jugend"}, {"x": 64, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Torhüter-Duell auf vier Tore", "code": "UE-252", "kind": "Übungsform",
 "focuses": ["Torschuss", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 6, "players_max": 6,
 "field_size": "27 x 27 m",
 "description": "Zwei Teams mit je zwei Torhütern verteidigen je zwei Tore auf einer Seite des Feldes. Wer den Ball hat, spielt zu einem Springer in der Mitte, bekommt ihn zurückgelegt und schießt direkt auf ein gegnerisches Tor. Hält der Torwart den Schuss, greift sein Team sofort selbst an. So üben die Torhüter, Schüsse aus vielen Winkeln und Entfernungen zu halten.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern. Oben und unten stehen je zwei Jugendtore.",
  "Verteilen: Team Neon hütet die oberen Tore, Team Rot die unteren, mit je einem Torwart und einem Spieler. Zwei Springer stehen in der Mitte. Der Trainer steht links an der Seite mit Bällen.",
  "Ablauf: Der Trainer spielt einem Team den Ball zu. Es passt zu einem Springer, der legt ab, und dann wird direkt auf ein gegnerisches Tor geschossen. Hält der Torwart, greift sein Team sofort selbst an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team, das geschossen hat. Das Team mit dem Gegentor tauscht mit den Springern. Geht der Ball ins Aus, bringt der Trainer einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Ein paar Schritte rauskommen und den Winkel verkürzen", "Auf Augen und Hüfte des Schützen schauen", "Fangen, wenn es geht, sonst zur Seite abwehren", "Nach dem Halten schnell abspielen und laut ansagen"],
 "materials": ["4 Jugendtore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Torhüter-Duell auf vier Tore. Zwei Teams mit je zwei Torhütern schießen und halten im schnellen Wechsel.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 19.6, 30.6)] + ERSATZ,
  "steps": [
   S("Anspiel", "Der Trainer spielt den Ball zum Torwart von Team Neon.",
     ps("b1", [36.6, 9.6])),
   S("Ablegen lassen", "Der Torwart passt zum Springer in der Mitte. Der Springer legt den Ball direkt ab, und Spieler dreizehn läuft ihm entgegen.",
     ps("b1", [42.6, 33.6]), mv("n13", [58, 18], delay=0.4), ps("b1", [58.6, 18.6], after=True)),
   S("Gehalten", "Der Torwart von Team Rot schaut auf Augen und Hüfte von Spieler dreizehn. Spieler dreizehn schießt direkt, und der Torwart fängt den Ball.",
     bl("r1", [60.5, 32]), ps("b1", [61.6, 52.6], after=True), mv("r1", [61, 52], after=True)),
   S("Gegenangriff: Punkt", "Jetzt greift Team Rot an. Der Torwart passt zum linken Springer, der legt für Spieler zwölf ab. Spieler zwölf schießt direkt ins obere linke Tor, und das gibt einen Punkt für Team Rot. Dann bringt der Trainer einen neuen Ball, und es geht weiter.",
     ps("b1", [42.6, 33.6]), mv("n13", [64, 9]), mv("r12", [33, 41], delay=0.3), ps("b1", [33.6, 41.6], after=True), ps("b1", [40, 5.4], after=True))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=82)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Rauskommen und den Winkel verkürzen.", "Rauskommen, Winkel verkürzen",
    "Bleibt der Torwart tief im Tor, sieht der Schütze viel freie Fläche. Kommt er schnell ein paar Schritte heraus, wird das Tor für den Schützen kleiner. Dabei schaut er auf Augen und Hüfte des Schützen, denn sie verraten, wohin der Ball fliegt.",
    sp(n13=(58, 18)), [B("b1", 58.6, 18.6)] + ERSATZ,
    [S("Rauskommen", "Spieler dreizehn hat den Ball. Der Torwart von Team Rot kommt schnell ein paar Schritte heraus und macht sich groß.",
       mv("r1", [62, 45])),
     S("Augen und Hüfte", "Er schaut auf Augen und Hüfte von Spieler dreizehn. Spieler dreizehn schießt, und der Torwart hält den Ball sicher.",
       bl("r1", [59.5, 27.5]), ps("b1", [62.6, 45.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Springer schießen Abpraller nach.", "Abpraller nachschießen",
    "Jetzt dürfen die Springer Abpraller sofort nachschießen. Lässt der Torwart den Ball nach vorn abprallen, wird es gefährlich. Darum wehrt er Bälle, die er nicht fangen kann, zur Seite ab, weg von der Mitte. Ein Treffer nach einem Abpraller zählt für das Team, das geschossen hat.",
    sp(n13=(58, 18)), [B("b1", 58.6, 18.6)] + ERSATZ,
    [S("Abpraller", "Spieler dreizehn schießt fest. Der Torwart von Team Rot kann den Ball nicht festhalten, und er prallt nach vorn ab.",
       ps("b1", [64.6, 51.6]), ps("b1", [66.6, 40.6], after=True)),
     S("Nachschuss: Punkt", "Der Springer rechts ist sofort da und schießt den Abpraller ins Tor. Das gibt einen Punkt für Team Neon. Darum Bälle, die man nicht fangen kann, immer zur Seite abwehren. Dann bringt der Trainer einen neuen Ball.",
       mv("f2", [66, 40]), ps("b1", [59, 54.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
