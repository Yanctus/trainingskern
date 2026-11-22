import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 24-P6 (U12-U14, Woche 29 Phase 3): Strikers Unopposed Finishing SSG. 35 x 25 Yards (32 x 23 m) = Feld x 27-73, y 5-55
# (etwas breiter gezeichnet, damit sich in 3D niemand verdeckt), oben und unten je eine Endzone (gestrichelt, y 17 und 43) und je
# ein Jugendtor mit neutralem Torwart (im Video grün und gelb). Gespiegelt (oben/unten): im PDF greift Blau auf das untere Tor
# an, hier greift Team Neon nach oben an. Blau -> Team Neon (4, 7, 11 Mitte, 9 Stürmer), Rot/Pink -> Team Rot (2 Mitte;
# 7 -> 6, 4 -> 5, Stürmer 9 -> 10 neu nummeriert, weil die Nummern doppelt waren). Ein Trainer statt zwei.
# Ablauf wie PDF und Video: Torwart spielt an, fünf Pässe in der Mitte, Steilpass zum Stürmer in der Endzone, Abschluss gegen den
# Torwart; danach spielt der Trainer den nächsten Ball ein. Wertung wie im PDF (Treffer zwei Punkte, aufs Tor einen Punkt,
# Torwart hält zwei Punkte für den Torwart). Wechsel der Stürmer nicht im Original (ergänzt).
# Sichtkegel aus dem Video ("Recognise danger", Ton "Defenders must be aware of dangerous attacks forming"): in der Steigerung
# schaut Rot zwei zum freien Stürmer Neon neun in der Endzone und läuft dann zurück (im Video Kegel von Rot 2 zum Stürmer).
T = P("T", "c", 18, 30, "T")
POS = {"k1": (50, 7), "k2": (50, 53), "n9": (62, 10), "r10": (38, 50),
       "n7": (28, 30), "r2": (36.5, 34), "n4": (45, 24), "r5": (53.5, 28), "n11": (62, 32), "r6": (70.5, 27)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 18, 34), B("s2", 14.4, 34)]
LINES = [rect(27, 5, 46, 50), line(27, 17, 73, 17), line(27, 43, 73, 43)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Fünf Pässe, dann zum Stürmer", "code": "UE-211", "kind": "Spielform",
 "focuses": ["Passspiel", "Torschuss", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 12, "field_size": "32 x 23 m",
 "description": "In der Mitte spielen drei gegen drei, und jedes Team hat einen Stürmer in der Endzone vor dem gegnerischen Tor. Nach fünf Pässen in Folge darf das Team einen Steilpass zu seinem Stürmer spielen. Der Stürmer ist allein mit dem Torwart und muss schnell und sicher abschließen. In der Steigerung darf ein Verteidiger zurück in die Endzone laufen.",
 "organisation": ["Aufbauen: Ein Feld von 32 mal 23 Metern mit drei Zonen: oben und unten je eine Endzone von acht Metern, dazwischen die Mitte. Oben und unten je ein Jugendtor.",
  "Verteilen: Team Neon und Team Rot spielen mit je drei Spielern in der Mitte. Jedes Team hat einen Stürmer in der Endzone vor dem gegnerischen Tor. In beiden Toren steht ein Torwart. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Torwart spielt den Ball in die Mitte. Das Team am Ball muss fünf Pässe in Folge schaffen. Dann spielt es den Ball steil zum eigenen Stürmer, und der schießt allein gegen den Torwart.",
  "Wertung und Wechsel: Ein Treffer gibt zwei Punkte, ein Schuss aufs Tor gibt einen Punkt. Hält der Torwart, gibt das zwei Punkte für den Torwart. Danach spielt der Trainer den nächsten Ball ein, und nach ein paar Minuten tauschen die Stürmer mit Spielern aus der Mitte."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell kombinieren, um eine Chance zu bekommen", "Als Stürmer in der Endzone anbieten", "Allein vor dem Torwart ruhig und sicher abschließen", "Keinen Pass erzwingen, lieber Gegner herauslocken"],
 "materials": ["2 Jugendtore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Fünf Pässe, dann zum Stürmer. In der Mitte spielen drei gegen drei, und nach fünf Pässen geht der Ball steil zum Stürmer in der Endzone.",
 "board": {"lines": LINES, "goals": TORE, "players": sp(), "balls": [B("b1", 50.6, 53.6)] + ERSATZ,
  "steps": [
   S("Anspiel vom Torwart", "Der Torwart unten spielt den Ball zu Neon vier. Jetzt hat Team Neon den Ball und greift nach oben an.",
     ps("b1", [45.6, 24.6])),
   S("Fünf Pässe", "Team Neon passt sich den Ball in der Mitte zu, Team Rot presst. Neon vier spielt zu Neon sieben und bekommt den Ball zurück. So zählt Team Neon bis fünf.",
     ps("b1", [28.6, 30.6]), mv("r2", [31, 35], delay=0.3), ps("b1", [45.6, 24.6], after=True), mv("r5", [47, 21], after=True), ps("b1", [62.6, 32.6], after=True)),
   S("Steilpass zum Stürmer", "Nach dem fünften Pass bietet sich Neon neun in der Endzone an. Neon elf spielt den Ball steil zu ihm.",
     mv("n9", [57, 15]), ps("b1", [57.6, 15.6], delay=0.3)),
   S("Abschluss: Punkt", "Neon neun ist allein mit dem Torwart und schießt sicher ins Tor. Das gibt zwei Punkte für Team Neon. Dann spielt der Trainer den nächsten Ball ins Mittelfeld, und das Team, das ihn bekommt, greift an.",
     ps("b1", [55.5, 5.6]))],
  "dims": dims(27, 73, 5, 55, "23 m", "32 m", rx=80)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Lücke nutzen.", "Durch die Lücke",
    "Gehen zwei Verteidiger auseinander, entsteht zwischen ihnen eine Lücke. Genau dann spielt der Ballführende den Steilpass durch die Lücke. So kommt der Stürmer hinter die Abwehr.",
    sp(), [B("b1", 62.6, 32.6)] + ERSATZ,
    [S("Lücke geht auf", "Neon elf hat den Ball. Rot fünf läuft zu Neon vier. Rot sechs bleibt außen. Zwischen den beiden geht eine Lücke auf.",
       mv("r5", [48, 22]), mv("r6", [71, 31], delay=0.2)),
     S("Durch die Lücke: Punkt", "Neon neun startet, und Neon elf spielt den Ball genau durch die Lücke in seinen Lauf. Neon neun schießt, und das gibt zwei Punkte für Team Neon.",
       mv("n9", [60, 15]), ps("b1", [60.6, 15.6], delay=0.3), ps("b1", [55.5, 5.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger darf in die Endzone zurück.", "Ein Verteidiger hilft",
    "Sobald der Steilpass kommt, darf ein Verteidiger zurück in die Endzone laufen. Der Stürmer hat jetzt weniger Zeit und muss nach der ersten Ballannahme schnell schießen. Die Verteidiger müssen früh erkennen, wo es gefährlich wird.",
    sp(r2=(36.5, 20)), [B("b1", 62.6, 32.6)] + ERSATZ,
    [S("Gefahr erkennen", "Neon elf hat den Ball. Rot zwei schaut sich um und sieht Neon neun allein in der Endzone. Das ist gefährlich.",
       bl("r2", [55, 13])),
     S("Zurück in die Endzone", "Neon elf spielt steil zu Neon neun. Rot zwei läuft sofort zurück in die Endzone.",
       mv("n9", [57, 15]), ps("b1", [57.6, 15.6], delay=0.3), mv("r2", [48, 15], delay=0.3)),
     S("Schnell schießen: Punkt", "Neon neun nimmt den Ball mit dem ersten Kontakt Richtung Tor mit und schießt, bevor Rot zwei bei ihm ist. Das gibt zwei Punkte für Team Neon.",
       dr("n9", "b1", [59, 11]), mv("r2", [53, 13], delay=0.2), ps("b1", [55.5, 5.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
