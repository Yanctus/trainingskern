import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-26: 20 x 15 Yards = x 15-85, y 4-56. PDF gedreht: Start unten -> links, Dummy oben -> rechts. Blau -> Neon (obere Bahn), Pink -> Rot (untere Bahn, gespiegelt: y -> 63,5 - y).
M = lambda p: [p[0], round(63.5 - p[1], 2)]
T = P("T", "c", 89, 31.5, "T"); cb = [B("c1", 92, 33), B("c2", 92, 29.5)]
stangen = [(46, 14.5), (54, 17), (62, 14.5), (70, 17)]
cones = [C(x, y, shape="stange") for x, y in stangen] + [C(x, 63.5 - y, shape="stange") for x, y in stangen] \
      + [C(81, 15.75, "neon", shape="stange"), C(81, 47.75, "neon", shape="stange"), C(26, 15.75), C(26, 47.75)]
def lane(steps_blue, rot):
    """Spiegelt die Züge der oberen Bahn (Team Neon) auf die untere Bahn (Team Rot), beide laufen gleichzeitig."""
    out = []
    for m in steps_blue:
        n = dict(m); n["who"] = rot.get(m["who"], m["who"]); n["to"] = M(m["to"])
        if m.get("ball"): n["ball"] = rot[m["ball"]]
        if m.get("bend"): n["bend"] = -m["bend"]
        out.append(n)
    return steps_blue + out
ROT = {"n6": "r9", "n3": "r10", "b1": "b2", "n4": "r14", "n2": "r11"}
def grund():
    return [
     S("Beide Paare starten gleichzeitig", "Auf los starten beide Teams gleichzeitig: Spieler sechs dribbelt an, Spieler drei läuft auf der anderen Seite der Stangen mit.",
       *lane([dr("n6", "b1", [44.4, 8]), mv("n3", [44, 24])], ROT)),
     S("Erster Direktpass", "Spieler sechs spielt mit einem Kontakt durch die Stangen zu Spieler drei, beide laufen weiter.",
       *lane([ps("b1", [54, 22.8]), mv("n3", [54, 24]), mv("n6", [54, 8], delay=0.1)], ROT)),
     S("Hin und her durch die Stangen", "Spieler drei spielt direkt zurück, und Spieler sechs legt mit einem Kontakt wieder quer.",
       *lane([mv("n6", [62, 8]), ps("b1", [62, 9.3], delay=0.1), mv("n3", [70, 24], delay=0.3), ps("b1", [70, 22.8], after=True)], ROT)),
     S("Am Dummy hochlupfen", "Am Dummy lupft Spieler drei den Ball hoch, genau in die Hände von Spieler sechs.",
       *lane([dr("n3", "b1", [69, 17.5]), mv("n6", [77.5, 12], delay=0.1), ps("b1", [77, 12.6], after=True)], ROT)),
     S("Einwurf zum nächsten Paar", "Spieler sechs wirft den Ball mit einem Einwurf zum nächsten Paar am Start, und beide laufen zurück. Das schnellste Team gewinnt.",
       *lane([ps("b1", [18, 8.9]), mv("n6", [33, 9.5], delay=0.3), mv("n3", [30, 27], delay=0.3)], ROT))]
spieler = [P("n6", "a", 25, 8, "6"), P("n3", "a", 25, 24, "3"), P("n4", "a", 16.5, 8, "4"), P("n2", "a", 16.5, 24, "2"),
           P("r9", "b", 25, 55.5, "9"), P("r10", "b", 25, 39.5, "10"), P("r14", "b", 16.5, 55.5, "14"), P("r11", "b", 16.5, 39.5, "11"), T]
u = {"title": "Staffel mit Direktpässen", "code": "UE-066", "kind": "Spielform",
 "focuses": ["Erwärmung", "Passspiel", "Schnelligkeit"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"], "duration_minutes": 10, "players_min": 8, "players_max": 12, "field_size": "18 x 14 m",
 "description": "Zwei Teams treten in Paaren gegeneinander an, jedes Team hat eine eigene Bahn mit vier Stangen und einem Dummy am Ende. Beide Paare starten gleichzeitig, dribbeln los und spielen sich den Ball zwischen den Stangen mit einem Kontakt zu. Am Dummy lupft einer den Ball in die Hände des Partners, der ihn mit einem Einwurf zum nächsten Paar am Start wirft. Das Team, dessen Spieler zuerst alle durch sind, gewinnt.",
 "organisation": ["Bahnen aufbauen: Zwei Bahnen von 18 mal 7 Metern nebeneinander, in jeder vier Stangen im Zickzack und am Ende ein Dummy.",
  "Teams einteilen: Zwei Teams, jedes stellt sich in Paaren am Starthütchen seiner Bahn auf. Das erste Paar hat einen Ball.",
  "Ablauf: Losdribbeln, mit einem Kontakt zwischen den Stangen hin und her passen, am Dummy den Ball in die Hände des Partners lupfen, dann Einwurf zum nächsten Paar.",
  "Wertung: Nach dem Einwurf laufen beide zurück und stellen sich hinten an. Das Team, das zuerst komplett durch ist, gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Direktpässe zwischen den Stangen mit dem richtigen Tempo spielen", "Den Ball genau in die Hände des Partners lupfen", "Schnell und genau einwerfen, damit das nächste Paar sofort losdribbeln kann", "Nach einem Fehler sofort weitermachen, die Wartenden feuern an"],
 "materials": ["8 Stangen", "2 Dummys", "2 Hütchen für den Start", "2 Bälle", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Staffel mit Direktpässen. Hier spielen sich zwei Partner den Ball durch die Stangen zu, und das schnellere Team gewinnt.",
 "board": {"lines": [rect(15, 4, 70, 52), line(15, 31.75, 85, 31.75)], "cones": cones, "players": spieler,
  "balls": [B("b1", 26.6, 8), B("b2", 26.6, 55.5), *cb], "steps": grund(),
  "dims": [{"x1": 15, "y1": 58.6, "x2": 85, "y2": 58.6, "text": "18 m"}, {"x1": 96, "y1": 4, "x2": 96, "y2": 56, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball genau in die Hände des Partners lupfen.", "Genau in die Hände lupfen",
    "Am Dummy kommt es auf einen genauen Lupfer an. Steht der Partner zu weit weg oder kommt der Ball ungenau, muss er hinterherlaufen, und das Team verliert Zeit. Nah beieinander bleiben und den Ball sanft in die Hände spielen, so bleibt das Tempo hoch.",
    [P("n3", "a", 69, 17.5, "3"), P("n6", "a", 77.5, 12, "6"), P("r10", "b", 69, 49, "10"), P("r9", "b", 79.5, 55.5, "9"),
     P("n4", "a", 16.5, 8, "4"), P("n2", "a", 16.5, 24, "2"), P("r14", "b", 16.5, 55.5, "14"), P("r11", "b", 16.5, 39.5, "11"), T],
    [B("b1", 70.5, 17), B("b2", 70.5, 48.5), *cb],
    [S("Zu weit weg vom Partner", "Bei Team Rot steht Spieler neun zu weit weg, der Lupfer fällt daneben, und er muss hinterherlaufen.",
       ps("b2", [74.5, 50.5]), mv("r9", [75.5, 52], delay=0.35)),
     S("Nah dran, genau in die Hände", "Bei Team Neon steht Spieler sechs nah dran, und Spieler drei lupft den Ball genau in seine Hände.", ps("b1", [77, 12.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Am Dummy kreuzen die Partner und laufen die Bahn ein zweites Mal.", "Kreuzen und zweite Runde",
    "Am Dummy wird nicht sofort eingeworfen. Die Partner kreuzen um den Dummy herum, tauschen so die Seiten und spielen sich auf dem Rückweg wieder mit einem Kontakt durch die Stangen zu. Das bringt mehr Pässe, mehr Bewegung und verlangt gute Absprache.",
    [P("n3", "a", 70, 24, "3"), P("n6", "a", 70, 8, "6"), P("r10", "b", 70, 39.5, "10"), P("r9", "b", 70, 55.5, "9"),
     P("n4", "a", 16.5, 8, "4"), P("n2", "a", 16.5, 24, "2"), P("r14", "b", 16.5, 55.5, "14"), P("r11", "b", 16.5, 39.5, "11"), T],
    [B("b1", 71.6, 24), B("b2", 71.6, 39.5), *cb],
    [S("Um den Dummy kreuzen", "Spieler drei dribbelt im Bogen um den Dummy herum auf die andere Seite, und Spieler sechs kreuzt hinter ihm durch.",
       *lane([dr("n3", "b1", [78, 24]), dr("n3", "b1", [85.5, 15.75], after=True), dr("n3", "b1", [78, 8], after=True), dr("n3", "b1", [71.5, 8], after=True), mv("n6", [74, 24], delay=0.4)], ROT)),
     S("Zurück durch die Stangen", "Auf dem Rückweg spielen sie sich den Ball wieder mit einem Kontakt durch die Stangen zu.",
       *lane([ps("b1", [62, 22.8]), mv("n6", [62, 24]), mv("n3", [54, 8], delay=0.1), ps("b1", [54, 9.3], after=True)], ROT)),
     S("Zweite Runde geschafft", "Mit einem letzten Direktpass und einem Dribbling sind sie zurück am Start, und das nächste Paar ist dran.",
       *lane([mv("n6", [46, 24]), ps("b1", [46, 22.8], delay=0.1), dr("n6", "b1", [30, 24], after=True), mv("n3", [33, 9.5], delay=0.3)], ROT))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
