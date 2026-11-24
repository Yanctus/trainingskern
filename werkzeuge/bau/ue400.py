import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 03-P9 (U15-U17, Woche 36 Phase 6): Defend The Defending 3rd Function. 40 (L) x 50 (W) Yards = 37 x 46 m (gerundet 35 x 45 m).
# Kein Großfeld (gut ein Drittel des Platzes, 12 Spieler), kein langes Feld (breiter als lang). Um 90 Grad gedreht: im PDF steht das
# Tor links, hier oben (Team Rot greift nach oben an); das Feld liegt mit der Breite waagrecht, x 20-78, y 5-52.
# Strafraum und Torraum in echter Größe. Die gestrichelte Linie vor der Endlinie ist die Zone des Springers, dort stehen die zwei
# Minitore für den Konter (im PDF schräg in den Ecken, hier gerade an der Endlinie). Die durchgezogene Linie bei zwei Dritteln und die
# gestrichelte Längslinie aus dem PDF weggelassen (im Text ohne Rolle).
# Pink + grüner Torwart -> Team Neon (n1 TW, Dreierkette 2, 5, 6, davor 4 und 8), dunkel -> Team Rot (9, 10, 11, dahinter
# 7 und 3; im PDF 4 und 8, wegen doppelter Nummern neu vergeben). Ein Springer F wie in Skizze und Video (der Text nennt zwei).
# Ein Trainer statt zwei, unten an der Seitenlinie, spielt die Bälle zu Team Rot ein („immediate coach ball feed“).
# Positionen auf Abstand gesetzt (3D), Spielidee wie im PDF und Video: Rückpass als Signal zum Anlaufen, Ballgewinn, Konter über
# den Springer aufs Minitor. Fassungen: PDF Key Coaching Point 1 (nicht auseinanderreißen lassen, zurück und den Strafraum
# schützen) und Progression (der Springer spielt für Team Rot mit, sechs gegen fünf).
# Sichtkegel: Ton „players must recognize when and how to force direction … on selected triggers“, Video „pressing triggers e.g.
# slow backwards pass“: In der Grundform sieht Spieler vier den langsamen Rückpass, bevor er anläuft. In der Steigerung schaut
# Spieler fünf vor der Flanke zu Spieler neun (aus dem Sinn, im Video kein Kegel eingezeichnet).
# Keine Dublette: UE-166 (03-P3, vier gegen vier), UE-098 (03-P6, kleines Spiel vier gegen vier), UE-378 (03-P5, zwei gegen zwei),
# UE-399 (03-P10, zwei Viererketten gegen sieben auf dem Großfeld).
T = P("T", "c", 76, 55.3, "T")
ERSATZ = [B("s1", 79.5, 55.8), B("s2", 82, 55.8)]
POS = {"n1": (49, 8), "n2": (31, 24.5), "n5": (49, 26), "n6": (67, 24.5), "n4": (40, 34), "n8": (58, 34),
       "r9": (58, 15), "r10": (40, 17), "r11": (22, 31), "r3": (31, 43), "r7": (67, 44), "f": (49, 49.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    out = []
    for i, (x, y) in d.items():
        if i == "f": out.append(P(i, "t", x, y, "F"))
        else: out.append(P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]))
    return out + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(20, 5, 58, 47), rect(23.5, 5, 51, 21), rect(37.4, 5, 23.2, 7), line(20, 47, 78, 47)]
TORE = [{"x": 49, "y": 5, "side": "top", "size": "gross"}, {"x": 31, "y": 52, "side": "bottom"}, {"x": 67, "y": 52, "side": "bottom"}]
DIMS = dims(20, 78, 5, 52, "45 m", "35 m", rx=86)

u = {"title": "Dreierkette mit zwei Sechsern", "code": "UE-400", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 13,
 "field_size": "45 x 35 m",
 "description": "Fünf Verteidiger und ein Torwart verteidigen das große Tor gegen fünf Angreifer. Team Neon steht mit einer Dreierkette und zwei Sechsern davor und verteidigt als Block. Ein langsamer Rückpass ist das Signal zum Anlaufen. Nach dem Ballgewinn spielt Team Neon den Springer an der Endlinie an und kontert auf zwei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 35 Metern mit Strafraum und großem Tor. An der anderen Endlinie stehen zwei Minitore, davor ist eine schmale Zone für den Springer abgetrennt.",
  "Verteilen: Team Neon mit Torwart, drei Verteidigern und zwei Sechsern. Team Rot greift mit fünf Spielern an, zwei davon kommen von hinten. Der Springer steht in seiner Zone. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Trainer spielt zu einem der hinteren Spieler von Team Rot, und Team Rot greift das große Tor an. Team Neon verschiebt als Block und läuft beim Rückpass an. Nach dem Ballgewinn spielt Team Neon den Springer an und kontert auf ein Minitor.",
  "Wertung: Trifft Team Rot ins große Tor, gibt das einen Punkt für Team Rot. Trifft Team Neon nach dem Ballgewinn ins Minitor, gibt das einen Punkt für Team Neon. Danach spielt der Trainer sofort den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Rückpass heißt anlaufen, alle rücken mit", "Die zwei Sechser bleiben eng zusammen", "Ball verloren? Alle zurück, den Strafraum zumachen", "Ball gewonnen? Sofort den Springer suchen"],
 "materials": ["1 Großfeldtor", "2 Minitore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Dreierkette mit zwei Sechsern. Fünf Verteidiger und ein Torwart gegen fünf Angreifer vor dem eigenen Strafraum. Team Neon verteidigt als Block und kontert nach dem Ballgewinn über den Springer.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 76.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein", "Der Trainer spielt den Ball zu Spieler sieben. Team Neon steht mit drei Verteidigern hinten und zwei Sechsern davor. Alle fünf bleiben eng beisammen.",
     ps("b1", fu(POS["r7"]))),
   S("Quer und raus, Block schiebt", "Spieler sieben spielt quer zu Spieler drei, und der legt raus zu Spieler elf. Spieler zwei geht drauf, und der ganze Block schiebt mit zur Ballseite.",
     ps("b1", fu(POS["r3"])), ps("b1", fu(POS["r11"]), after=True), mv("n2", [27, 28], delay=0.3), mv("n4", [36, 34], delay=0.3), mv("n5", [45, 26.5], delay=0.3),
     mv("n6", [62, 25], delay=0.3), mv("n8", [52, 34.5], delay=0.3)),
   S("Rückpass, jetzt anlaufen", "Spieler elf kommt nicht weiter und spielt langsam zurück zu Spieler drei. Das ist das Signal. Spieler vier sieht den Rückpass und läuft sofort an, und hinten rücken alle ein Stück raus.",
     ps("b1", fu(POS["r3"])), bl("n4", POS["r3"], delay=0.2), mv("n4", [34, 39.5], after=True),
     mv("n8", [46, 36], delay=0.9), mv("n2", [27, 31], delay=0.9), mv("n5", [44, 29.5], delay=0.9), mv("n6", [60, 28], delay=0.9)),
   S("Nach innen zu, Ball erobert", "Spieler drei will nach innen andribbeln. Spieler vier macht den Weg zu, geht dazwischen und hat den Ball.",
     dr("r3", "b1", [33, 42]), mv("n4", [35.5, 40], delay=0.2), ps("b1", fu([35.5, 40]), after=True)),
   S("Über den Springer ins Minitor: Punkt", "Sofort geht der Ball zum Springer. Spieler acht startet, bekommt ihn zurück und schießt ins Minitor, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer gleich den nächsten Ball zu Team Rot.",
     ps("b1", fu(POS["f"])), mv("n8", [58, 45], delay=0.2), ps("b1", [58.6, 45.6], after=True), ps("b1", [66, 51.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nicht auseinanderreißen lassen.", "Eng bleiben, Strafraum zu",
    "Die beiden Sechser bleiben eng zusammen, damit kein Pass durch die Mitte geht. Reißt die Lücke auf, steht es hinten drei gegen drei. Kommt der Ball doch hinter die Kette, laufen alle sofort zurück und machen den Strafraum zu.",
    sp(), [B("b1", *fu(POS["r7"]))] + ERSATZ,
    [S("Die Sechser rücken zusammen", "Spieler sieben hat den Ball. Spieler zehn lässt sich zwischen unsere beiden Sechser fallen. Spieler vier und Spieler acht rücken zusammen, und Spieler fünf geht von hinten mit.",
       mv("r10", [49, 30.5]), mv("n4", [44, 35], delay=0.2), mv("n8", [54, 35], delay=0.2), mv("n5", [49, 27], delay=0.4)),
     S("Kein Pass durch die Mitte", "Durch die Mitte geht nichts, also spielt Spieler sieben quer zu Spieler drei. Der Block schiebt mit, und die Abstände bleiben klein.",
       ps("b1", fu(POS["r3"])), mv("n4", [38, 36], delay=0.3), mv("n8", [48, 36], delay=0.3), mv("n2", [28, 26], delay=0.3),
       mv("n5", [44, 27], delay=0.3), mv("n6", [61, 25], delay=0.3)),
     S("Alle zurück, Strafraum zu", "Spieler drei spielt lang auf Spieler elf, der hinter die Kette startet. Jetzt laufen alle zurück. Spieler zwei bleibt an ihm dran, die anderen machen den Strafraum zu.",
       mv("r11", [25, 19]), ps("b1", [25.6, 19.6], delay=0.3), mv("n2", [28, 18], delay=0.3), mv("n5", [44, 15], delay=0.4),
       mv("n6", [58, 19], delay=0.4), mv("n4", [37, 26], delay=0.4), mv("n8", [55, 29], delay=0.4))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Der Springer spielt für Team Rot mit.", "Springer spielt mit",
    "Jetzt darf der Springer ins Feld kommen und für Team Rot mitspielen. Dann steht es sechs gegen fünf. Er verteilt die Bälle und verlagert das Spiel. Team Neon muss schneller verschieben und früher entscheiden, wer drauf geht.",
    sp(), [B("b1", *fu(POS["r7"]))] + ERSATZ,
    [S("Der Springer kommt dazu", "Der Springer kommt aus seiner Zone ins Feld, und Spieler sieben spielt ihn an. Jetzt sind es sechs gegen fünf.",
       mv("f", [49, 41]), ps("b1", fu([49, 41]), delay=0.4)),
     S("Weit auf die andere Seite", "Der Springer verlagert weit auf Spieler elf. Spieler zwei geht raus, und alle anderen schieben schnell rüber.",
       ps("b1", fu(POS["r11"])), mv("n2", [24, 27], delay=0.3), mv("n4", [33, 33], delay=0.3), mv("n5", [42, 24.5], delay=0.3),
       mv("n6", [57, 23], delay=0.3), mv("n8", [47, 33], delay=0.3)),
     S("Flanke in die Mitte geklärt", "Spieler fünf schaut kurz über die Schulter zu Spieler neun. Dann kommt die Flanke, und Spieler fünf ist vor ihm am Ball und köpft ihn weg.",
       bl("n5", POS["r9"]), mv("r9", [52, 13], after=True), mv("n5", [50.5, 14.5], delay=1.1), ps("b1", [51.1, 15.1], delay=1.2), ps("b1", [76, 20], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
