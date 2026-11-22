import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-P16 (U12-U14, Torwarttraining): Coming Out to Collect Crosses (Develop GK Ability to Claim Crosses). 50 x 45 Yards = Feld
# x 15-85, y 5-55 (46 x 41 m), Strafraum und Torraum nach der Video-Skizze, Halbkreis weggelassen. Im PDF liegt das Tor links,
# im Video oben: hier oben wie im Video, aber gespiegelt (im Video Leiter rechts und Trainer links), damit die Leiter von links
# nach rechts durchlaufen wird. Vier Puppen als Stangen wie im Video (die PDF-Skizze zeigt nur drei). Pinker Torwart -> neutraler
# Torwart TW, Trainer flankt (im Original mit der Hand bzw. dem Fuß von der Seite). Kein Wettbewerb: Ziel statt Punkte.
# PDF-Progression 1 (Pfosten rufen, zuerst den anderen Pfosten antippen) und 2 (drei Minitore, Abwurf) als die zwei Steigerungen.
# Sichtkegel aus Text und Ton ("Scan Before and During the Cross", "scan the area", "effective scanning to select the best
# outlet") und Video (Progression 1 und 2: dunkler Kegel vom Torwart): Grundform und Steigerung 1 schaut der Torwart zum
# Trainer bzw. Ball, Steigerung 2 nach dem Fangen zum freien Minitor.
T = P("T", "c", 75, 31, "T")
def sp(x=20, y=8.5): return [P("k1", "t", x, y, "TW"), T]
ERSATZ = [B("s1", 79, 33.5), B("s2", 79, 29)]
def baelle(): return [B("b1", 75.6, 31.6)] + ERSATZ
LINES = [rect(15, 5, 70, 50), rect(22, 5, 56, 20), rect(39, 5, 22, 7)]
STANGEN = [C(41, 12, shape="stange"), C(59, 12, shape="stange"), C(46.5, 19.5, shape="stange"), C(53.5, 19.5, shape="stange")]
TOR = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
MINITORE = [{"x": 27, "y": 55, "side": "bottom"}, {"x": 50, "y": 55, "side": "bottom"}, {"x": 73, "y": 55, "side": "bottom"}]

u = {"title": "Leiter laufen, Flanke fangen", "code": "UE-251", "kind": "Übungsform",
 "focuses": ["Koordination", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 1, "players_max": 3,
 "field_size": "46 x 41 m",
 "description": "Der Torwart läuft auf das Zeichen des Trainers schnell durch eine Koordinationsleiter. Dann kommt eine hohe Flanke, und er fängt den Ball am höchsten Punkt über den Puppen. Danach läuft er zurück an die Leiter und wartet auf das nächste Zeichen. So übt er schnelle Füße, das richtige Timing und sicheres Fangen.",
 "organisation": ["Aufbauen: Ein Feld von 46 mal 41 Metern mit Strafraum und einem Jugendtor oben. Links neben dem Tor liegt eine Koordinationsleiter, vor dem Tor stehen vier Puppen oder Stangen.",
  "Verteilen: Der Torwart steht am linken Ende der Leiter. Der Trainer steht rechts vor dem Strafraum mit vielen Bällen. Weitere Torhüter warten neben dem Tor.",
  "Ablauf: Auf das Zeichen läuft der Torwart durch die Leiter. Der Trainer flankt hoch vor das Tor, und der Torwart fängt den Ball über den Puppen. Dann rollt er den Ball zurück und läuft wieder an die Leiter.",
  "Wechsel: Nach sechs Flanken ist der nächste Torwart dran. Ziel ist, jede Flanke sicher am höchsten Punkt zu fangen."],
 "organisation_show": ORG,
 "coaching_points": ["Den Ball am höchsten Punkt fangen und früh abspringen", "Mit kurzen, schnellen Schritten durch die Leiter", "Vor und während der Flanke umschauen und den Ball beobachten", "Vor dem Absprung die Schritte verkürzen"],
 "materials": ["1 Jugendtor", "1 Koordinationsleiter", "4 Puppen oder Stangen", "3 Minitore", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Leiter laufen, Flanke fangen. Der Torwart läuft schnell durch die Leiter und fängt dann eine hohe Flanke über den Puppen.",
 "board": {"lines": LINES, "goals": TOR, "cones": [leiter(31, 8.5)] + STANGEN, "players": sp(), "balls": baelle(),
  "steps": [
   S("Durch die Leiter", "Der Trainer ruft: Los! Der Torwart dreht sich um und läuft mit kurzen, schnellen Schritten durch die Leiter.",
     mv("k1", [41, 7.5])),
   S("Umschauen", "Am Ende der Leiter schaut der Torwart sofort zum Trainer. Wohin kommt die Flanke?",
     bl("k1", [57, 18])),
   S("Am höchsten Punkt fangen", "Der Trainer flankt hoch vor das Tor. Der Torwart macht kurze Schritte, springt früh ab und fängt den Ball am höchsten Punkt über den Puppen.",
     ps("b1", [50.6, 15.6], bend=6), mv("k1", [50, 15], delay=0.4)),
   S("Zurück zur Leiter", "Geschafft, die Flanke ist sicher gefangen. Der Torwart rollt den Ball zum Trainer zurück und läuft zurück an die Leiter. Dort wartet er auf das nächste Zeichen, und nach sechs Flanken ist der nächste Torwart dran.",
     ps("b1", [75.6, 31.6]), mv("k1", [45, 9], after=True), mv("k1", [20, 8.5], after=True))],
  "dims": dims(15, 85, 5, 55, "46 m", "41 m", rx=92)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft einen Pfosten.", "Erster oder zweiter Pfosten",
    "Die Leiter bleibt jetzt liegen, der Torwart startet in der Mitte des Tors. Der Trainer ruft „Erster Pfosten“ oder „Zweiter Pfosten“. Der Torwart tippt zuerst den anderen Pfosten an und fängt dann die Flanke am gerufenen Pfosten. Dafür muss er sich umschauen und schnell quer durch den Torraum laufen.",
    sp(50, 7.5), baelle(),
    [S("Zweiter Pfosten!", "Der Trainer ruft: Zweiter Pfosten! Der Torwart läuft zuerst zum ersten Pfosten und tippt ihn an.",
       mv("k1", [54.5, 6.5])),
     S("Umschauen und rüber", "Er schaut über die Schulter zum Trainer und sieht die Flanke kommen. Dann läuft er schnell quer zum zweiten Pfosten.",
       bl("k1", [69, 21]), ps("b1", [45.6, 11.1], bend=6, after=True), mv("k1", [45, 10.5], after=True)),
     S("Am zweiten Pfosten fangen", "Der Torwart springt ab und fängt den Ball sicher am zweiten Pfosten. Dann rollt er ihn zurück, und der Trainer ruft wieder einen Pfosten.",
       ps("b1", [75.6, 31.6]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Nach dem Fangen schnell abwerfen.", "Fangen und schnell abwerfen",
    "Unten stehen jetzt drei Minitore. Der Torwart fängt die Flanke und schaut sich sofort um. Dann wirft er den Ball schnell und genau in ein freies Minitor, wie beim Start eines Konters. Aber erst sicher fangen, dann abwerfen.",
    sp(50, 7.5), baelle(),
    [S("Flanke fangen", "Der Trainer flankt. Der Torwart kommt heraus und fängt den Ball sicher über den Puppen.",
       ps("b1", [50.6, 15.6], bend=6), mv("k1", [50, 15], delay=0.4)),
     S("Umschauen", "Mit dem Ball in den Händen schaut er sich um. Das linke Minitor ist frei.",
       bl("k1", [40, 33])),
     S("Abwurf ins Minitor", "Er wirft den Ball schnell und genau ins linke Minitor. Geschafft! Dann holt der Trainer den nächsten Ball, und die nächste Flanke kommt.",
       ps("b1", [27, 54.5]))], goals=TOR + MINITORE)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
