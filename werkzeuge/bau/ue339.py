import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 19-P5 (U15-U17, Woche 8 Phase 4): Forcing Direction Activation Rondo (im PDF „Activation Rondo for Larger Squad“).
# 15 x 10 Yards = 14 x 9 m, in der Mitte ein Quadrat von 3 x 3 Yards (knapp 3 x 3 m) mit dem Springer.
# FELD QUER (langes Feld, Verhältnis 1,5): Die lange Seite liegt waagrecht, Feld x 18-82, y 12-48; außen ist Platz für die
# wartenden Partner. Im PDF hochkant mit drei Paaren an den langen und zwei an den kurzen Seiten (zehn Paare), im Video elf Paare.
# Hier acht Paare auf der Tafel (zwei an jeder Seite), die übrigen nur im Text (3D-Abstand). Die Partner stehen außen leicht
# versetzt hinter dem aktiven Spieler (3D-Abstand).
# Außenspieler = Team Neon (aktiv 2-9, Partner 10-17: Paare 2/10, 3/11, 4/12, 5/13, 6/14, 7/15, 8/16, 9/17).
# Die zwei Verteidiger (PDF „D“) = Team Rot 18 und 19, der Springer im Quadrat (PDF „F“) = neutral, Label F.
# Ein Trainer (unten an der Seitenlinie statt oben in der Ecke).
# Wertung ergänzt: Im Original gibt es keine Zählweise. Kommt der Ball über den Springer wieder nach außen, gibt das einen Punkt
# für Team Neon. Ballgewinn wie im Original und im Video: Das Paar, das den Ball verloren hat, geht als Verteidiger hinein,
# die beiden Verteidiger gehen raus auf dessen Platz.
# Fassungen: PDF Progression 1 (nach dem Pass mit einem Spieler eines anderen Paares tauschen, im Video zum Nachbarpaar an
# derselben Seite) und Progression 2 (zweiter Springer innen, beide verbinden sich direkt, dann geht der Ball nach außen).
# Sichtkegel: Text „awareness“, „always checking for next step in the sequence“; im Video nicht eingezeichnet. Richtung aus dem
# Sinn: Der Außenspieler schaut vor dem direkten Pass zum Springer in die Mitte (Grundform), der zweite Springer schaut vor der
# Annahme zum Springer im Quadrat (Steigerung 2).
# Keine Dublette: UE-224/UE-154/UE-233 (Paar-Rondos mit fünf gegen zwei oder Springern oben und unten), UE-312 (Aufwärmen am
# Viereck) haben keine Paare außen mit Platztausch und keinen Springer im Quadrat.
T = P("T", "c", 50, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n2": (18, 20), "n10": (9, 20), "n3": (18, 40), "n11": (9, 40),
       "n4": (37, 12), "n12": (28, 5), "n5": (63, 12), "n13": (72, 5),
       "n6": (82, 20), "n14": (91, 20), "n7": (82, 40), "n15": (91, 40),
       "n8": (37, 48), "n16": (28, 55), "n9": (63, 48), "n17": (72, 55),
       "r18": (37, 28), "r19": (63, 31), "f": (50, 30)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "f": "t"}[i[0]], x, y, "F" if i[0] == "f" else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, d=None): x, y = (d or POS)[i]; return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(18, 12, 64, 36), rect(44, 24.5, 12, 11, dashed=True)]
DIMS = dims(18, 82, 12, 48, "14 m", "9 m", rx=96.5)

u = {"title": "Rondo mit Wechselpaaren", "code": "UE-339", "kind": "Übungsform",
 "focuses": ["Passspiel", "Verteidigen", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 15, "players_max": 25,
 "field_size": "14 x 9 m",
 "description": "Ein Rondo für viele Spieler auf engem Raum. Außen stehen Paare, einer spielt mit, sein Partner wartet dahinter, und nach jedem Pass tauschen die beiden. In der Mitte steht ein Springer im kleinen Quadrat, zwei Verteidiger pressen zu zweit und stellen den Pass zu ihm zu. Wer den Ball verliert, geht mit seinem Partner als neues Verteidigerpaar hinein.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 9 Metern, in der Mitte ein Quadrat von knapp drei mal drei Metern.",
  "Verteilen: Alle Außenspieler stehen paarweise am Rand, einer an der Linie, sein Partner wartet direkt dahinter. Ein Springer steht im Quadrat, zwei Verteidiger im Feld. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Die Außenspieler spielen direkt und suchen den Pass zum Springer in die Mitte. Nach jedem Pass tauscht der Passgeber mit seinem Partner. Die Verteidiger pressen zu zweit, einer geht auf den Ball, der andere stellt den Weg zum Springer zu.",
  "Wertung und Wechsel: Kommt der Ball über den Springer wieder nach außen, gibt das einen Punkt für Team Neon. Erobern die Verteidiger den Ball, geht das Paar, das ihn verloren hat, als neues Verteidigerpaar hinein. Der Trainer spielt sofort den nächsten Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Direkt spielen, der Ball bleibt in Bewegung", "Nach dem Pass sofort mit dem Partner tauschen", "Einer geht auf den Ball, einer stellt die Mitte zu", "Kopf hoch, wo steht der Springer?"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rondo mit Wechselpaaren. Ein Rondo für eine große Gruppe. Außen spielen Paare direkt und tauschen nach jedem Pass, in der Mitte pressen zwei und stellen den Weg zum Springer zu.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": [B("b1", 50.6, 55.9)] + ERSATZ,
  "steps": [
   S("Einspielen, direkt weiter, tauschen", "Der Trainer spielt Spieler acht an. Der spielt direkt weiter zu Spieler drei. Sofort tauscht er mit seinem Partner, Spieler sechzehn kommt an die Linie.",
     ps("b1", fuss("n8")), ps("b1", fuss("n3"), after=True), mv("n8", [31.5, 57], delay=0.6), mv("n16", [37, 48], delay=0.9)),
   S("Nach oben, Rot presst", "Spieler drei legt direkt hoch auf Spieler zwei, und der spielt direkt weiter zu Spieler vier. Spieler achtzehn läuft Spieler vier an. Spieler neunzehn stellt den Weg in die Mitte zu.",
     ps("b1", fuss("n2")), ps("b1", fuss("n4"), after=True), mv("n3", [12, 44.5], delay=0.4), mv("n11", [18, 40], delay=0.7),
     mv("n2", [12, 15.5], delay=1.2), mv("n10", [18, 20], delay=1.5), mv("r18", [36, 19.5], delay=0.9), mv("r19", [49, 21.5], delay=0.9)),
   S("Kopf hoch, dann zum Springer", "Die Mitte ist zu, also weiter zu Spieler fünf. Der schaut schon vorher, wo der Springer steht. Spieler neunzehn kommt zu spät, und Spieler fünf spielt direkt ins Quadrat.",
     bl("n5", [50, 30]), ps("b1", fuss("n5"), after=True), mv("r19", [56, 17], delay=0.6), mv("r18", [44, 15], delay=0.6),
     mv("n4", [31.5, 8], delay=0.6), mv("n12", [37, 12], delay=0.9), ps("b1", fuss("f"), after=True)),
   S("Springer legt raus: Punkt", "Der Springer legt direkt raus auf Spieler neun. Der Ball war in der Mitte und ist wieder außen, das gibt einen Punkt für Team Neon. Spieler fünf tauscht mit Spieler dreizehn.",
     ps("b1", fuss("n9")), mv("n5", [66.5, 7.5], delay=0.3), mv("n13", [63, 12], delay=0.6)),
   S("Ballgewinn, das Paar geht rein", "Spieler neun will direkt zu Spieler sieben, aber Spieler neunzehn ist dazwischen. Jetzt gehen Spieler neun und Spieler siebzehn als neue Verteidiger rein. Die beiden Roten gehen raus an ihren Platz, und der Trainer spielt den nächsten Ball ein.",
     ps("b1", [72.5, 44]), mv("r19", [72, 43.5], delay=0.2), mv("n9", [58, 38], delay=1.2), mv("n17", [63, 28], delay=1.2),
     mv("r19", [66, 50], after=True), mv("r18", [59, 23], delay=1.2), mv("r18", [74, 57], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Pass wechselt man zu einem anderen Paar.", "Tausch mit anderem Paar",
    "Wer gepasst hat, tauscht jetzt nicht mehr mit seinem Partner. Er läuft zum Nachbarpaar und nimmt dort den Platz des Wartenden ein, der Wartende läuft an seine Stelle. So steht keiner herum, und jeder muss neu schauen, wer gerade neben ihm steht.",
    sp(), [B("b1", 82.6, 40.6)] + ERSATZ,
    [S("Quer durchs Feld, dann wechseln", "Spieler sieben spielt quer durchs Feld zu Spieler drei. Danach läuft er außen hoch zum Nachbarpaar. Spieler vierzehn wartet dort und kommt runter an die Linie.",
       ps("b1", fuss("n3")), mv("n7", [89, 32], delay=0.5), mv("n7", [94, 25], after=True), mv("n14", [86, 30], delay=0.7), mv("n14", [82, 40], after=True)),
     S("Direkt weiter, wieder wechseln", "Spieler drei spielt direkt hoch zu Spieler vier und läuft rüber zum oberen Paar auf seiner Seite. Spieler zehn kommt an seine Stelle. Spieler vier spielt direkt weiter zu Spieler fünf.",
       ps("b1", fuss("n4")), mv("n3", [12, 33], delay=0.4), mv("n3", [5, 25], after=True), mv("n10", [13, 29], delay=0.6), mv("n10", [18, 40], after=True),
       ps("b1", fuss("n5"), after=True), mv("r18", [42, 18], delay=0.6), mv("r19", [55, 20], delay=0.8))], dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein zweiter Springer kommt dazu.", "Zweiter Springer innen",
    "Ein zweiter Springer bewegt sich frei im Feld. Bevor der Ball wieder nach außen darf, müssen die beiden Springer sich direkt verbinden. Für die Verteidiger wird es schwerer, denn sie müssen zwei Wege in die Mitte zustellen.",
    sp(f2=(72, 22)) , [B("b1", 82.6, 20.6)] + ERSATZ,
    [S("Erst zum freien Springer", "Spieler sechs spielt den zweiten Springer an. Der hat vorher schon in die Mitte geschaut und weiß, wo der andere Springer steht.",
       bl("f2", [50, 30]), ps("b1", [72.6, 22.6], after=True), mv("r19", [65, 29], delay=0.5)),
     S("Springer zu Springer, raus: Punkt", "Direkt zum Springer im Quadrat, und der legt direkt raus auf Spieler vier. Beide Springer haben sich verbunden, das gibt einen Punkt für Team Neon.",
       ps("b1", fuss("f")), ps("b1", fuss("n4"), after=True), mv("r18", [42, 20], delay=0.4))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
