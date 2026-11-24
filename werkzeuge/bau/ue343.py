import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 48-P11 (U15-U17, Woche 9 Phase 2): Possession and Transition to Attack. 35 x 20 Yards = 32 x 18 m (gerundet 18 x 30 m).
# Langes Feld quer wie im PDF (Inhaber 24.11.2026, Vorbild ue317.py): Feld x 9-89, y 4-51, großes Tor mit neutralem Torwart
# rechts (Großfeldtor, nur C- und B-Jugend), zwei Minitore links. Zonengrenze gestrichelt bei x 55 wie im PDF (etwa 57 Prozent
# der Länge für die Ballbesitzzone). PDF blau -> Team Neon (4-10 wie im PDF), pink -> Team Rot, neu nummeriert (doppelt):
# 2 -> 2, 6 -> 3, 7 -> 11, 10 -> 12, 4 -> 13, 8 -> 14, 5 -> 15. Grüner Torwart -> neutraler Torwart. Ein Trainer statt zwei,
# unten an der Seitenlinie bei der Zonengrenze. Die vierzehn Feldspieler stehen in einem Raster (3D-Abstand), die
# Zuordnung folgt grob dem PDF. Passfolge vereinfacht (sechs Pässe ohne Abfangen), Angriff mit zwei Spielern.
# Fassung 1 = PDF Key Coaching Point (gemeinsam pressen, abfangen, schnell aufs Minitor). Fassung 2 = PDF Progression
# (Springer für das Team am Ball). Die Ideen aus dem Ton (Kontakte begrenzen, Zeitlimit nach dem sechsten Pass) nicht eingebaut.
# Sichtkegel: kein Kegel im Video eingezeichnet; aus dem Text ("Decision-making in the final third", "Recognise the 6 pass
# trigger moment"), Richtung aus dem Sinn: Spieler neun schaut vor dem letzten Pass zum Torwart. Annehmen und Aufdrehen
# nach dem sechsten Pass mit bl(von=...) und drehen().
T = P("T", "c", 64, 55.3, "T")
ERSATZ = [B("s1", 67.5, 55.8), B("s2", 70, 55.8)]
POS = {"n6": (12, 9), "n5": (12, 28), "n4": (12, 47), "n10": (29, 8), "n8": (29, 45), "n9": (46, 27), "n7": (54.5, 40),
       "r11": (20.5, 15), "r14": (20.5, 40), "r12": (29, 27), "r3": (37.5, 30), "r15": (37.5, 46), "r2": (46, 9), "r13": (46, 44),
       "k": (85, 27.5)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + list(extra) + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
F = P("f1", "t", 54.5, 18, "F")
POSF = dict(POS, f1=(54.5, 18))
LINES = [rect(9, 4, 80, 47), line(55, 4, 55, 51)]
TORE = [{"x": 89, "y": 27.5, "side": "right", "size": "gross"}, {"x": 9, "y": 14.8, "side": "left"}, {"x": 9, "y": 40.2, "side": "left"}]
KEGEL = [C(9, 4), C(89, 4), C(9, 51), C(89, 51), C(55, 4), C(55, 51)]
DIMS = dims(9, 89, 4, 51, "30 m", "18 m")[:1]  # rechts steht das Tor: nur die Länge

u = {"title": "Sechs Pässe, dann aufs Tor", "code": "UE-343", "kind": "Spielform",
 "focuses": ["Passspiel", "Umschalten", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 16,
 "field_size": "18 x 30 m",
 "description": "Sieben gegen sieben in einer großen Ballbesitzzone, davor eine kleinere Angriffszone mit großem Tor und Torwart. Das Team am Ball braucht sechs Pässe in Folge, erst dann darf es in die Angriffszone und aufs Tor. Das andere Team presst gemeinsam. Erobert es den Ball, kontert es sofort auf zwei Minitore am anderen Ende.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 30 Metern, geteilt in eine größere Ballbesitzzone und eine kleinere Angriffszone. Vor der Angriffszone steht ein großes Tor mit Torwart, am anderen Ende stehen zwei Minitore.",
  "Verteilen: Team Neon und Team Rot spielen mit je sieben Spielern in der Ballbesitzzone. Der Torwart ist neutral. Der Trainer steht mit Bällen an der Seitenlinie bei der Zonengrenze.",
  "Ablauf: Der Trainer spielt Team Neon an. Nach sechs Pässen in Folge darf Team Neon in die Angriffszone und aufs große Tor spielen. Erobert Team Rot in einer der Zonen den Ball, kontert es sofort auf eines der beiden Minitore.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach jedem erfolgreichen Angriff oder nach einer festen Zeit tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Ball halten, aber immer mit dem Ziel Tor", "Sechster Pass, jetzt mit Tempo nach vorn", "Anspielbar sein, Winkel zum Ballführer suchen", "Gegen den Ball zusammen pressen und sofort kontern"],
 "materials": ["1 großes Tor", "2 Minitore", "6 Hütchen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Sechs Pässe, dann aufs Tor. Sieben gegen sieben, und erst nach sechs Pässen in Folge darf Team Neon nach vorn in die Angriffszone. Team Rot presst und kontert auf die Minitore.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", *fuss("n4"))] + ERSATZ, "dims": DIMS,
  "steps": [
   S("Pass eins und zwei", "Spieler vier hat den Ball vom Trainer. Er spielt zu Spieler fünf, der gleich weiter zu Spieler sechs. Das sind zwei Pässe.",
     ps("b1", fuss("n5")), ps("b1", fuss("n6"), after=True)),
   S("Pass drei und vier", "Spieler sechs spielt flach zu Spieler zehn. Der findet Spieler neun zwischen den Linien. Vier Pässe.",
     ps("b1", fuss("n10")), ps("b1", fuss("n9"), after=True), mv("r12", [33, 22], delay=0.6)),
   S("Pass fünf und sechs", "Spieler neun legt raus auf Spieler sieben und bietet sich gleich wieder an. Er schaut zum Ball, und Spieler sieben spielt zurück. Das ist der sechste Pass.",
     ps("b1", fuss("n7")), bl("n9", POS["n7"], after=True), ps("b1", fuss("n9"), after=True)),
   S("Aufdrehen, ab in die Angriffszone", "Jetzt darf Team Neon nach vorn. Spieler neun dreht auf und treibt den Ball in die Angriffszone. Spieler sieben sprintet mit. Team Rot läuft hinterher.",
     bl("n9", [68, 24], von=POS["n7"], dauer=1.3), drehen("n9", [68, 24], gegen=True, delay=0.4), dr("n9", "b1", [68, 24], after=True),
     mv("n7", [72, 40], delay=0.6), mv("r3", [58, 30], delay=0.8), mv("r13", [62, 44], delay=0.8)),
   S("Querpass am Torwart vorbei: Punkt", "Spieler neun schaut zum Torwart. Der kommt raus, also legt Spieler neun quer auf Spieler sieben. Der schiebt ins leere Tor, und das gibt einen Punkt für Team Neon. Danach tauschen die Rollen, und der Trainer spielt Team Rot an.",
     bl("n9", POS["k"]), mv("k", [80, 30], delay=0.3), ps("b1", [72.6, 40.6], after=True), ps("b1", [88.4, 24], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zusammen pressen und nach dem Ballgewinn sofort kontern.", "Gemeinsam pressen, kontern",
    "Team Rot presst nicht allein, sondern zusammen. Einer läuft den Ballführer an, die anderen stellen die Passwege zu. Kommt der Ball doch, ist einer dazwischen. Nach dem Ballgewinn geht es mit wenigen Kontakten sofort aufs Minitor.",
    sp(), [B("b1", *fuss("n5"))] + ERSATZ,
    [S("Zusammen anlaufen", "Spieler fünf spielt zu Spieler sechs. Das ist das Zeichen. Spieler elf läuft an, Spieler drei schiebt in den Weg zu Spieler zehn, und Spieler zwölf stellt den Rückpass zu.",
       ps("b1", fuss("n6")), mv("r11", [17, 14], delay=0.3), mv("r3", [24, 10], delay=0.3), mv("r12", [20, 24], delay=0.3)),
     S("Pass abgefangen", "Spieler sechs will zu Spieler zehn spielen. Spieler drei steht schon im Passweg und fängt den Ball ab.",
       ps("b1", [22.6, 9.6]), mv("r3", [22, 9], delay=0.2)),
     S("Schnell aufs Minitor: Punkt", "Sofort geht der Ball zu Spieler zwölf. Der schießt direkt aufs Minitor, und das gibt einen Punkt für Team Rot.",
       ps("b1", [20.6, 24.6]), ps("b1", [9.6, 39.5], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Springer spielt mit.", "Mit Springer für das Team am Ball",
    "Ein Springer spielt immer für das Team am Ball. So steht es acht gegen sieben, und die sechs Pässe kommen leichter zusammen. Wer den Ball hat, findet öfter einen freien Mitspieler, und der Angriff kommt schneller.",
    sp(extra=[F]), [B("b1", *fuss("n6"))] + ERSATZ,
    [S("Springer frei an der Linie", "Spieler sechs spielt zu Spieler zehn. Der findet den Springer frei an der Zonengrenze. Zwei Pässe.",
       ps("b1", fuss("n10")), ps("b1", fuss("f1", POSF), after=True)),
     S("Ablegen und weiter", "Der Springer legt ab auf Spieler neun, der spielt gleich weiter zu Spieler sieben. Vier Pässe.",
       ps("b1", fuss("n9")), ps("b1", fuss("n7"), after=True)),
     S("Pass fünf und sechs", "Spieler sieben spielt zurück zum Springer. Spieler neun schaut zum Ball und bekommt den sechsten Pass.",
       ps("b1", fuss("f1", POSF)), bl("n9", POSF["f1"], after=True), ps("b1", fuss("n9"), after=True)),
     S("Aufdrehen und abschließen: Punkt", "Spieler neun dreht auf, treibt den Ball in die Angriffszone und schießt flach ins Eck, und das gibt einen Punkt für Team Neon.",
       bl("n9", [70, 26], von=POSF["f1"], dauer=1.3), drehen("n9", [70, 26], delay=0.4), dr("n9", "b1", [70, 26], after=True),
       mv("r3", [58, 31], delay=0.8), ps("b1", [88.4, 21.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
