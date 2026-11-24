import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 19-P9 (U15-U17, Woche 14): Press to Force Direction. 35 x 50 Yards = 32 x 46 m, gerundet 30 x 45 m.
# QUER GELEGT (PDF um 90 Grad im Uhrzeigersinn gedreht: Feld x 14-86.5, y 5-55.75), hochkant stünden 14 Figuren in 3D
# voreinander. Das große Tor steht damit links, die zwei Seitentore (im PDF links, zur Platzmitte hin) oben, die zwei
# Endtore (im PDF oben) rechts, die Außenlinie ist unten. Team Rot (im PDF Blau) baut von links nach rechts auf.
# Team Neon (im PDF Pink, 6 Spieler) presst und behält die Nummern aus dem Video (3, 6, 8, 9, 10, 11).
# Rot neu nummeriert, weil 6, 8 und 9 doppelt wären: Blau 6 -> 4, Blau 4 -> 14, Blau 8 -> 15, Blau 9 -> 12; 2, 5, 7 bleiben.
# Torwart gehört zu Team Rot (r1 "TW"). Die schräg gestellten Minitore stehen gerade an der Linie. Ein Trainer statt zwei.
# Neustart: Im PDF steht "restart without goalkeeper", im Video beginnt jeder Ball beim Torwart; hier Neustart beim Torwart.
# Grundform = Szene aus PDF und Video (Pass auf den Innenverteidiger, weiter nach außen, Elf presst, Ballgewinn, Abschluss).
# Fassung 1 = Ton/Video "screening and preparing the jump press". Fassung 2 = Progression (Seitentore zwei Punkte).
# Sichtkegel: im Video keiner eingezeichnet; aus dem Text ("identify pressing triggers", "recognise where attackers can
# switch"): Spieler elf beobachtet den ersten Kontakt des Innenverteidigers (Fassung 1).
# Kein Dubletten-Fall: UE-155 (59-P4) ist ein 3 gegen 2 auf 14 x 18 m mit einem Minitor und zwei Hütchentoren.
T = P("T", "c", 6, 45, "T")
ERSATZ = [B("s1", 7.6, 48.5), B("s2", 4, 48.5)]
ROT = {"r5": (30, 9.4), "r4": (29, 33.6), "r2": (32.4, 50.5), "r15": (52.6, 36.3), "r14": (50.3, 15), "r12": (71, 30.2), "r7": (64.8, 49.4)}
NEON = {"n9": (38.5, 25), "n11": (49.4, 52), "n8": (61, 30.4), "n10": (59, 12.3), "n6": (80, 32.3), "n3": (76.4, 48.8)}
def sp(**k):
    n = dict(NEON); r = dict(ROT)
    for i, v in k.items(): (n if i in n else r)[i] = v
    return [P("r1", "b", 16.3, 16.4, "TW")] + [P(i, "b", x, y, i[1:]) for i, (x, y) in r.items()] \
        + [P(i, "a", x, y, i[1:]) for i, (x, y) in n.items()] + [T]
LINES = [rect(14, 5, 72.5, 50.75), rect(14, 5, 13.8, 34.8), rect(14, 5, 4.4, 17.4)]
TORE = [{"x": 14, "y": 15.5, "side": "left", "size": "gross"}, {"x": 48.8, "y": 5, "side": "top"}, {"x": 82, "y": 5, "side": "top"},
        {"x": 86.5, "y": 30.4, "side": "right"}, {"x": 86.5, "y": 51.4, "side": "right"}]
START = [B("b1", 16.9, 17)] + ERSATZ

u = {"title": "Pressen und die Seite zumachen", "code": "UE-315", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 16,
 "field_size": "45 x 30 m",
 "description": "Team Rot baut mit Torwart und sieben Feldspielern auf und will eines von vier Minitoren treffen. Team Neon verteidigt zu sechst und bestimmt, wohin der Gegner spielen darf. Erst werden die Seitentore zugemacht, dann wird der Ball an die Außenlinie gelenkt und dort gemeinsam erobert. Ein Treffer nach Ballgewinn ins große Tor gibt zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 30 Metern auf einer Seite vor dem großen Tor. Zwei Minitore stehen an der Innenseite des Feldes als Seitentore, zwei am Ende gegenüber vom großen Tor.",
  "Verteilen: Team Rot baut mit Torwart und sieben Feldspielern auf. Team Neon verteidigt mit sechs Spielern. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Der Torwart eröffnet. Team Rot will in eines der vier Minitore treffen. Team Neon macht zuerst die Seitentore zu, lenkt das Spiel an die Außenlinie und presst dort gemeinsam.",
  "Wertung: Ein Treffer von Team Rot in ein Minitor gibt einen Punkt. Erobert Team Neon den Ball und trifft ins große Tor, gibt das zwei Punkte für Team Neon. Danach geht es beim Torwart weiter."],
 "organisation_show": ORG,
 "coaching_points": ["Erst die Seitentore zumachen, dann die Endtore", "Geht der Ball nach außen, schieben alle mit", "Passweg zustellen und bereit sein zum Herausspringen", "Kopf hoch, wo kann der Gegner verlagern?"],
 "materials": ["1 großes Tor", "4 Minitore", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Pressen und die Seite zumachen. Team Rot baut zu acht auf, Team Neon verteidigt zu sechst. Team Neon lenkt den Ball an die Außenlinie und holt ihn sich dort.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": START,
  "steps": [
   S("Torwart eröffnet auf Spieler vier", "Der Torwart spielt flach zu Spieler vier. Spieler neun läuft ihn von innen an. Damit ist der Weg zurück auf die andere Seite zu.",
     ps("b1", [29.6, 34.2]), mv("n9", [33.5, 29.5], delay=0.4)),
   S("Pass nach außen, alle schieben", "Spieler vier spielt nach außen zu Spieler zwei. Das ist das Signal. Spieler elf sprintet hin und macht die Linie zu. Dahinter schiebt das ganze Team zur Ballseite.",
     ps("b1", [33, 51.1]), mv("n11", [38, 54], delay=0.2), mv("n9", [31.5, 41.5], delay=0.4), mv("n8", [55.5, 41], delay=0.4),
     mv("n10", [54, 22], delay=0.4), mv("n6", [76, 38], delay=0.4)),
   S("Kein Ausweg, Ball erobert", "An der Linie geht nichts mehr. Spieler zwei versucht den Pass nach innen auf Spieler fünfzehn. Spieler acht hat das kommen sehen und geht dazwischen.",
     ps("b1", [50, 39.1]), mv("n8", [49.4, 38.5], delay=0.2)),
   S("Konter aufs große Tor: zwei Punkte", "Sofort nach vorn. Spieler zehn startet in die Mitte, bekommt den Ball in den Lauf und schießt ein. Das gibt zwei Punkte für Team Neon. Weiter geht es mit einem neuen Ball beim Torwart.",
     mv("n10", [33, 21]), ps("b1", [33.6, 21.6], delay=0.5), ps("b1", [14.3, 20.5], after=True))],
  "dims": dims(14, 86.5, 5, 55.75, "45 m", "30 m", rx=94)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zustellen und bereit sein zum Herausspringen.", "Zustellen und rausspringen",
    "Ein Spieler hat oft zwei Aufgaben. Er stellt einen Passweg zu und ist gleichzeitig bereit, nach vorn herauszuspringen. Das Signal ist ein schlechter Pass oder ein unsauberer erster Kontakt. Springt einer, rücken alle hinter ihm nach.",
    sp(), START,
    [S("Elf stellt zu und lauert", "Der Ball geht zu Spieler vier. Spieler elf steht so, dass der Pass auf Spieler zwei schwer wird. Dabei schaut er genau auf den ersten Kontakt von Spieler vier.",
       ps("b1", [29.6, 34.2]), mv("n11", [42, 47.5], delay=0.2), bl("n11", [31, 36], after=True)),
     S("Schlechter Kontakt, Elf springt", "Der Ball springt Spieler vier vom Fuß. Darauf hat Spieler elf gewartet. Er geht sofort drauf, Spieler neun kommt von der anderen Seite, und dahinter rücken alle mit.",
       ps("b1", [33, 37.5]), mv("n11", [35.5, 39.5], delay=0.2), mv("n9", [33.5, 31], delay=0.3), mv("n8", [57, 40], delay=0.5), mv("n10", [55, 20], delay=0.5))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Seitentore zählen doppelt.", "Seitentore zählen doppelt",
    "Ein Treffer von Team Rot in eines der beiden Seitentore gibt jetzt zwei Punkte. Team Neon muss die Mitte noch entschlossener schließen. Wer dabei zu weit einrückt, lässt aber die Tore am Ende offen. Also zustellen, ohne die Tore im Rücken zu vergessen.",
    sp(), START,
    [S("Über außen zurück in die Mitte", "Team Rot spielt über Spieler vier nach außen und von dort gleich wieder nach innen auf Spieler fünfzehn. Team Neon schiebt zu langsam nach.",
       ps("b1", [29.6, 34.2]), ps("b1", [33, 51.1], after=True), ps("b1", [53.2, 36.9], after=True), mv("n11", [40, 53], delay=1.0), mv("n9", [33.5, 31], delay=0.4)),
     S("Seitentor: zwei Punkte für Team Rot", "Die Mitte ist offen. Spieler fünfzehn legt quer auf Spieler vierzehn, und der schiebt ins Seitentor ein. Das gibt zwei Punkte für Team Rot.",
       ps("b1", [50.9, 15.6]), mv("n10", [55, 11], delay=0.4), ps("b1", [48.8, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
