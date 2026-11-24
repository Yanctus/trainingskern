import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P6 (U15-U17, Woche 12): Defending the Cross SSG. 35 x 40 Yards = 32 x 37 m (gerundet 30 x 35 m), Feld x 20-80, y 5-55
# (in der Breite etwas gestreckt, damit zehn Feldspieler den 3D-Abstand halten). Tor oben mit Torwart (Großfeldtor), unten in
# jeder Außenzone ein Stangentor. Nicht gedreht.
# PDF pink (Video gelb) = Verteidiger -> Team Neon: 4, 3, 6, 5 und Torwart (PDF grün 13 -> TW). PDF blau = Angreifer -> Team Rot:
# 11, 7, 9 und die beiden Mittelfeldspieler neu nummeriert, weil 5 und 6 doppelt wären: 8 (PDF 5) und 10 (PDF 6).
# Ein Trainer statt zwei. Fassungen: PDF Key Coaching Point 1 (richtig gezeigt: Innenverteidiger ballseitig und torseitig)
# und Key Coaching Point 2 (erster Kontakt, dann Pass in den Lauf, Abschluss durchs Stangentor).
# Sichtkegel: Text „Checks to see attackers positioning/runs“; im Video nicht eingezeichnet, Richtung aus dem Sinn:
# der Innenverteidiger schaut vor der Flanke über die Schulter zum Stürmer.
# Kein Dubletten-Fall: UE-225 (Leiter, Doppelpass, flache Flanke aufs Minitor) und UE-248 (zwei Verteidiger, Flanken im Wechsel,
# Kopfball) sind Übungsformen mit anderem Aufbau; das hier ist ein freies fünf gegen fünf mit Außenzonen.
T = P("T", "c", 8, 14, "T")
ERSATZ = [B("s1", 11.6, 17.5), B("s2", 8, 17.5)]
def sp(tw, **d):
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("n1", "a", *tw, "TW"), T]
LINES = [rect(20, 5, 60, 50), line(32.5, 5, 32.5, 55), line(67.5, 5, 67.5, 55)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}]
CONES = [C(21.8, 53.5, shape="stange"), C(31, 53.5, shape="stange"), C(69, 53.5, shape="stange"), C(78.2, 53.5, shape="stange")]
DIMS = dims(20, 80, 5, 55, "30 m", "35 m", rx=92)
G = dict(n6=(42.5, 18.8), r9=(53, 23), n5=(61.5, 18), r11=(24.2, 28.6), r7=(75.4, 29.3), n4=(44.5, 34.5), r8=(36, 45), n3=(62.5, 41), r10=(53, 49))
K1 = dict(r7=(75.5, 27), r9=(43.5, 21), n6=(35, 21), n5=(61, 16), r11=(26, 22), n4=(52, 33), r10=(62.5, 34), r8=(42, 44), n3=(58, 50))
K2 = dict(r7=(75.5, 20), n4=(38, 18), r11=(29.5, 16), n6=(46.5, 13), r9=(55, 24.5), n5=(63.5, 14.5), n3=(46.5, 30), r8=(38, 36), r10=(63.5, 31))

u = {"title": "Flanken klären im 5 gegen 5", "code": "UE-308", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 12,
 "field_size": "30 x 35 m",
 "description": "Fünf gegen fünf auf ein Tor, links und rechts gibt es eine Außenzone für die Flügelspieler. Team Rot greift an und muss nach fünf Pässen über außen flanken. Team Neon verteidigt mit Torwart, steht ballseitig und torseitig und klärt die Flanke. Geht der Ball danach durch eins der Stangentore unten, gibt das einen Punkt für Team Neon.",
 "organisation": ["Aufbauen: Ein Feld von 30 mal 35 Metern mit einem Tor oben. Links und rechts ist eine Außenzone abgeteilt. Unten steht in jeder Außenzone ein Tor aus zwei Stangen.",
  "Verteilen: Team Neon verteidigt mit vier Feldspielern und Torwart. Team Rot greift mit fünf Spielern an, je ein Flügelspieler steht in einer Außenzone. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Team Rot spielt fünf Pässe und dann raus auf den Flügel. Ein Verteidiger darf in die Außenzone und den Flankengeber stören. Dann kommt die Flanke, und Team Neon klärt.",
  "Wertung und Wechsel: Klärt oder passt Team Neon den Ball durch ein Stangentor, gibt das einen Punkt für Team Neon. Trifft Team Rot ins Tor, gibt das einen Punkt für Team Rot. Danach kommt ein neuer Ball vom Trainer, nach ein paar Minuten tauschen die Teams."],
 "organisation_show": ORG,
 "coaching_points": ["Ballseitig und torseitig vom Gegenspieler stehen", "Schulterblick, wo läuft mein Stürmer?", "Laut reden, Torwart und Verteidiger", "Beim Klären auf die Stangentore zielen"],
 "materials": ["1 Tor", "4 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Flanken klären im fünf gegen fünf. Team Rot kommt über außen und flankt. Team Neon verteidigt die Flanke und klärt den Ball durch die Stangentore.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp((50.9, 7.3), **G),
  "balls": [B("b1", 53.6, 49.6)] + ERSATZ,
  "steps": [
   S("Fünf Pässe, dann nach außen", "Team Rot hat seine fünf Pässe fast zusammen. Spieler zehn spielt quer zu Spieler acht, und der spielt raus auf den Flügel zu Spieler elf.",
     ps("b1", [36.6, 45.6]), ps("b1", [24.8, 29.2], after=True)),
   S("Einer raus, die anderen sortieren sich", "Ein Verteidiger darf in die Außenzone. Spieler vier läuft raus und stört. In der Mitte schaut Spieler fünf über die Schulter. Wo läuft Spieler neun? Spieler sechs rückt näher ans Tor, zwischen Ball und Stürmer.",
     mv("n4", [33, 31]), bl("n5", [53, 23], delay=0.3), mv("n6", [42, 14.5], delay=0.6)),
   S("Flanke, Spieler fünf ist vorher da", "Jetzt kommt die Flanke hoch vors Tor. Spieler neun startet, aber Spieler fünf steht ballseitig und geht vor ihm dazwischen.",
     ps("b1", [56.6, 16.6], bend=-0.25), mv("r9", [62, 18.5], delay=0.2), mv("n5", [56, 16], delay=0.2), mv("r7", [70, 22], delay=0.2)),
   S("Klären durchs Stangentor: Punkt", "Spieler fünf klärt mit dem ersten Kontakt weit nach vorn, genau durch das rechte Stangentor, und das gibt einen Punkt für Team Neon. Der Trainer spielt den nächsten Ball zu Team Rot.",
     ps("b1", [74, 55.5]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Ballseitig und torseitig stehen, bevor die Flanke kommt.", "Ballseitig und torseitig",
    "Die Position muss stimmen, bevor geflankt wird. Der Innenverteidiger steht zwischen Ball und Stürmer und näher am Tor als er. Steht er auf der falschen Seite, läuft der Stürmer frei ein und trifft.",
    sp((52.5, 7.3), **K1), [B("b1", 76.1, 27.6)] + ERSATZ,
    [S("Falsche Seite, Blick zum Stürmer", "Der Ball ist rechts außen bei Spieler sieben. Spieler sechs steht noch auf der falschen Seite von Spieler neun. Ein Blick über die Schulter, dann läuft er vor ihm vorbei auf die Ballseite.",
       bl("n6", [43.5, 21]), mv("n6", [39.5, 16], after=True), mv("n6", [48, 17], after=True)),
     S("Vor dem Stürmer am Ball: Punkt", "Spieler sieben flankt. Spieler neun läuft ein, aber Spieler sechs ist vor ihm am Ball und klärt durch das linke Stangentor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [48.6, 17.6], bend=-0.15), mv("r9", [46, 22.5], delay=0.3), ps("b1", [26.5, 55.5], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ruhig bleiben, wenn Zeit ist.", "Erst annehmen, dann passen",
    "Nicht jede Flanke muss blind weg. Hat der Verteidiger Zeit, nimmt er den Ball mit dem ersten Kontakt sauber an. Dann geht der Kopf hoch, und er spielt einem Mitspieler in den Lauf. Der schließt durch das Stangentor ab.",
    sp((55, 7.3), **K2), [B("b1", 76.1, 20.6)] + ERSATZ,
    [S("Annehmen statt wegschlagen", "Die Flanke von Spieler sieben fliegt über alle hinweg zu Spieler vier. Niemand ist nah genug bei ihm. Also nimmt er den Ball mit dem ersten Kontakt sauber an.",
       ps("b1", [38.6, 18.6], bend=-0.2), mv("r11", [31, 17.5], delay=0.6)),
     S("Kopf hoch, Pass in den Lauf: Punkt", "Kopf hoch. Spieler drei startet schon nach vorn. Der Pass kommt in seinen Lauf. Spieler drei schiebt den Ball durch das rechte Stangentor, und das gibt einen Punkt für Team Neon.",
       bl("n4", [46.5, 30]), mv("n3", [54, 40], delay=0.5), ps("b1", [54.6, 40.6], after=True), ps("b1", [76, 55.5], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
