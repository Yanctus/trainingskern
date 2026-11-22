import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-60 (U12-U14, Woche 5 Pre-Season): One Touch Passing and Agility Exercise. 20 x 30 Yards hochkant = Feld x 33.3-66.7, y 5-55.
# Vier Gruppen zu dritt: oben links/rechts, unten links/rechts, je zwei Hütchen auf der Mittellinie als Passtor.
# Blau -> Neon (2, 3, 5, 6, 7, 8), Pink -> Rot (2 -> 9, 4 -> 10, 3 -> 11, 5 -> 12, 6 -> 13, 7 -> 14). Gruppen in Reihen mit Abstand
# (3D), die Hintersten außerhalb des Feldes. Ein Trainer statt zwei. Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 80, 30, "T")
POS = {"n5": (45.5, 15.7), "n2": (37.3, 15.7), "n3": (29, 15.7), "r9": (54.5, 15.7), "r10": (62.7, 15.7), "r11": (71, 15.7),
       "n6": (45.5, 45.7), "n8": (37.3, 45.7), "n7": (29, 45.7), "r12": (54.5, 45.7), "r13": (62.7, 45.7), "r14": (71, 45.7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 81.6, 33.5), B("s2", 83.5, 28)]
BAELLE = [B("b9", 55.1, 16.3), B("b6", 46.1, 46.3)] + ERSATZ
LINES = [rect(33.3, 5, 33.4, 50), line(50, 5, 50, 55)]
KEGEL = [C(50.2, 13), C(50.2, 18.6), C(50.2, 43.6), C(50.2, 48.9)] \
      + [C(38.9, y, shape="huerde_ou") for y in (27, 30, 33)] + [C(45.1, y, shape="huerde_ou") for y in (27.2, 30, 32.9)] \
      + [C(56.7, y, shape="huerde_ou") for y in (27, 30, 33)] + [C(61.7, y, shape="huerde_ou") for y in (27.2, 30, 32.9)]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
OBEN_DIREKT = [ps("b9", [46.1, 16.3]), ps("b9", [55.1, 16.3], after=True)]
UNTEN_DIREKT = [ps("b6", [55.1, 46.3], delay=0.1), ps("b6", [46.1, 46.3], after=True)]

u = {"title": "Direktpass und Koordination", "code": "UE-139", "kind": "Übungsform",
 "focuses": ["Passspiel", "Koordination", "Kondition"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "18 x 27 m",
 "description": "Vier Gruppen zu dritt stehen sich oben und unten gegenüber, zwischen ihnen stehen zwei Hütchen. Die Vordersten spielen sich den Ball mit einem Kontakt zu, durch die Lücke zwischen den Hütchen und außen an den Hütchen vorbei. Dann lassen sie den Ball liegen und laufen durch Leiter oder Hürden zur nächsten Gruppe. Unten läuft das Gleiche gespiegelt. Nach einem kompletten Durchgang laufen alle eine Runde ums Feld.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern, längs geteilt. Oben und unten stehen auf der Mittellinie je zwei Hütchen als Passtor. In der Mitte des Feldes liegen links eine Leiter und Minihürden, rechts genauso.",
  "Verteilen: Zwölf Spieler in vier Gruppen zu dritt, je eine Gruppe oben links, oben rechts, unten links und unten rechts. Oben und unten hat ein Vorderster einen Ball. Der Trainer steht am Rand mit Ersatzbällen.",
  "Ablauf: Die Vordersten spielen Direktpässe durch die Lücke, dann über das obere und unter dem unteren Hütchen. Danach lassen sie den Ball liegen und laufen durch Hürden oder Leiter zur Gruppe gegenüber. Alle Gruppen arbeiten gleichzeitig.",
  "Runde und Pause: Ist jeder wieder an seiner Startposition, ruft der Trainer: Alle laufen eine Runde ums Feld und gehen zurück zu den Stationen. Nach einer kurzen Pause geht es wieder los."],
 "organisation_show": ORG,
 "coaching_points": ["Direktpässe genau spielen", "Mit beiden Füßen passen, je nach Seite des Hütchens", "Saubere Technik in Leiter und Hürden, schnelle Füße", "Beim Warten bewusst erholen, bei der Runde ums Feld Tempo machen"],
 "materials": ["4 Hütchen", "2 Koordinationsleitern", "6 Minihürden", "Mehrere Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Direktpass und Koordination. Erst Pässe mit einem Kontakt durch und um die Hütchen, dann durch Leiter und Hürden zur nächsten Gruppe.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Direktpässe durch die Lücke", "Oben und unten spielen sich die Vordersten gleichzeitig den Ball mit einem Kontakt zu, durch die Lücke zwischen den Hütchen.",
     *OBEN_DIREKT, *UNTEN_DIREKT),
   S("Außen an den Hütchen vorbei", "Dann gehen sie einen Schritt zur Seite und passen über das obere Hütchen und unter dem unteren Hütchen hindurch, mal mit rechts, mal mit links.",
     mv("n5", [45.5, 9.5]), dr("r9", "b9", [54.5, 9.5]), ps("b9", [46.1, 10.1], after=True), dr("n5", "b9", [45.5, 22], after=True), mv("r9", [54.5, 22], delay=0.8), ps("b9", [55.1, 22.6], after=True),
     mv("r12", [54.5, 40.5], delay=0.1), dr("n6", "b6", [45.5, 40.5], delay=0.1), ps("b6", [55.1, 41.1], after=True), dr("r12", "b6", [54.5, 52], after=True), mv("n6", [45.5, 52], delay=0.9), ps("b6", [46.1, 52.6], after=True)),
   S("Durch Hürden und Leiter", "Jetzt lassen alle vier den Ball liegen. Die Oberen laufen über die Hürden nach unten, die Unteren durch die Leiter nach oben, und jeder stellt sich hinten bei der Gruppe gegenüber an.",
     *weg("n5", [[45.1, 25], [45.1, 36], [20.5, 45.7]]), *weg("r9", [[61.7, 25], [61.7, 36], [79.5, 45.7]]),
     *weg("n6", [[38.9, 37], [38.9, 24], [20.5, 15.7]], delay=0.6), *weg("r12", [[56.7, 37], [56.7, 24], [79.5, 15.7]], delay=0.6)),
   S("Die Nächsten", "Die Nächsten rücken nach vorn und beginnen sofort. Ist jeder wieder an seiner Startposition, laufen alle eine Runde ums Feld, dann gibt es eine kurze Pause.",
     mv("n2", [45.5, 15.7]), mv("r10", [54.5, 15.7]), mv("n8", [45.5, 45.7], delay=0.1), mv("r13", [54.5, 45.7], delay=0.1))],
  "dims": dims(33.3, 66.7, 5, 55, "18 m", "27 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit beiden Füßen passen.", "Beide Füße",
    "Geht der Pass links am Hütchen vorbei, spielt man mit dem linken Fuß, geht er rechts vorbei, mit dem rechten. So muss sich niemand verrenken, der Ball kommt genau und mit einem Kontakt zurück.",
    sp(), BAELLE,
    [S("Über das Hütchen", "Spieler fünf und Spieler neun gehen einen Schritt nach oben und passen über das obere Hütchen, jeder mit dem Fuß, der näher an der Linie ist.",
       mv("n5", [45.5, 9.5]), dr("r9", "b9", [54.5, 9.5]), ps("b9", [46.1, 10.1], after=True)),
     S("Unter dem Hütchen", "Dann geht es unter dem unteren Hütchen hindurch, jetzt mit dem anderen Fuß. Danach lassen beide den Ball liegen und laufen zur Koordination.",
       dr("n5", "b9", [45.5, 22]), mv("r9", [54.5, 22], delay=0.2), ps("b9", [55.1, 22.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Saubere Technik, schnelle Füße.", "Schnelle Füße",
    "In Leiter und Hürden zählt saubere Technik vor Tempo: kurze Schritte, auf den Fußballen, Arme mitnehmen, nichts umstoßen. Erst wenn das sitzt, wird es schneller.",
    sp(), BAELLE,
    [S("Über die Hürden", "Spieler fünf läuft mit kurzen, schnellen Schritten über die Hürden nach unten und stellt sich bei der Gruppe gegenüber an.",
       *weg("n5", [[45.1, 25], [45.1, 36], [20.5, 45.7]])),
     S("Durch die Leiter", "Danach läuft Spieler sechs mit schnellen Füßen durch die Leiter nach oben und stellt sich oben hinten an.",
       *weg("n6", [[38.9, 37], [38.9, 24], [20.5, 15.7]]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
