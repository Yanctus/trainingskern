import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 04-P11 (U15-U17, Woche 7 Phase 1): 8 v 8 Game Interchanging Positions. 50 x 40 Yards = 46 x 37 m (gerundet 45 x 35 m).
# Kein Großfeld (45 m, nur ein Teil des Platzes): Feld quer wie im PDF, füllt die Tafel (x 9-89, y 4-51), Figuren normal groß,
# keine Platzlinien (im Original nur das Rechteck). Zwei Großfeldtore mit Torwart (nur C- und B-Jugend).
# GESPIEGELT: Im PDF/Video baut das weiße Team (1-2-4-1) vom Tor rechts auf. Hier baut Team Neon vom Tor links auf und greift
# nach rechts an (oben/unten bleiben). Weiß -> Team Neon (1 TW, 5, 6, 4, 2, 3, 10, 9 wie im PDF). Dunkelblau (1-3-3-1) -> Team
# Rot, neu nummeriert, weil die Nummern doppelt sind: 3 -> 12, 5 -> 13, 2 -> 14, 11 -> 11, 4 -> 15, 7 -> 7, 9 -> 16.
# Der Torwart von Team Rot ist neutral (k, TW), damit „TW“ nicht doppelt vorkommt; der Torwart von Team Neon gehört zum Aufbau
# (n1, TW). Ein Trainer, unten an der Seitenlinie.
# 3D-Abstand: Aufstellung in Spalten geordnet (x 14 / 24 / 32.5 / 41 / 49.5 / 58 / 66.5 / 76 / 85), grob wie im PDF.
# Grundform nach Video und Ton: Innenverteidiger gehen breit, der Sechser lässt sich in die Lücke fallen und zieht seinen
# Gegenspieler mit, der Zehner kommt in den frei gewordenen Raum, der Torwart spielt ihn direkt an, Aufdrehen, Pass auf den
# Stürmer im Eins gegen eins. Neustart nach einem Treffer im Original nicht genannt (Annahme: wieder beim Torwart von Team Neon).
# Fassung 1 = Ton/Video „CDM drop further to create a back three … pushes centre backs forward … leaves space for centre back
# creating 2 v 1“. Fassung 2 = PDF-Progression (Mittelzone, nur zwei Spieler je Team), als gestrichelte Linien.
# Sichtkegel: Ton „Our goalkeeper needs to be aware of direct passing options“: Der Torwart schaut vor dem Pass zum Zehner.
# Der Zehner nimmt an und dreht auf (bl mit von, drehen). Im Video kein Kegel eingezeichnet.
FX0, FX1, FY0, FY1 = 9, 89, 4, 51
MY = (FY0 + FY1) / 2
T = P("T", "c", 67.5, 55.3, "T")
ERSATZ = [B("s1", 71, 55.8), B("s2", 73.5, 55.8)]
NEON = {"n1": (14, 28), "n5": (24, 14), "n6": (24, 42), "n2": (41, 7), "n4": (41, 25), "n3": (41, 46),
        "n10": (58, 40), "n9": (66.5, 30)}
ROT = {"k": (85, 28), "r16": (32.5, 28), "r11": (49.5, 10), "r15": (58, 22), "r7": (49.5, 47),
       "r12": (76, 12), "r13": (76, 30), "r14": (76, 47)}
POS = dict(NEON); POS.update(ROT)
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i in ("n1", "k") else i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i, pos=POS): return [round(pos[i][0] + 0.6, 1), round(pos[i][1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
ZONE = [line(37, 15, 61, 15), line(37, 41, 61, 41), line(37, 15, 37, 41), line(61, 15, 61, 41)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
CONES = ecken(FX0, FY0, FX1 - FX0, FY1 - FY0)
DIMS = dims(FX0, FX1, FY0, FY1, "45 m", "35 m")[:1]
BALL = [B("b1", *fuss("n1"))] + ERSATZ

u = {"title": "Rotieren im Spielaufbau", "code": "UE-336", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Bewegung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 16, "players_max": 16,
 "field_size": "35 x 45 m",
 "description": "Acht gegen acht mit zwei großen Toren. Team Neon baut vom Torwart aus auf, mit zwei Innenverteidigern und dem Sechser. Durch Platztausch entstehen Lücken: Wer sich fallen lässt, zieht seinen Gegenspieler mit, und ein anderer läuft in den frei gewordenen Raum. Team Neon sucht so schnell die Überzahl im Mittelfeld und das Eins gegen eins vorn.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 45 Metern mit einem großen Tor auf jeder Seite.",
  "Verteilen: Team Neon spielt mit Torwart, zwei Innenverteidigern, dem Sechser, zwei Außenspielern, einem Zehner und einer Spitze. Team Rot verteidigt mit Dreierkette, drei Mittelfeldspielern und einer Spitze, im Tor steht ein Torwart. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart von Team Neon eröffnet. Die Innenverteidiger gehen breit, der Sechser lässt sich fallen, und der Zehner kommt in den frei gewordenen Raum. Je nachdem, wie Team Rot presst, spielt Team Neon kurz über die Rotation oder direkt auf die Spitze.",
  "Wertung: Jeder Treffer gibt einen Punkt, für beide Teams. Erobert Team Rot den Ball, greift es sofort an. Nach jedem Treffer oder Aus beginnt wieder der Torwart von Team Neon."],
 "organisation_show": ORG,
 "coaching_points": ["Lass dich fallen und nimm deinen Gegner mit", "Wo ist die Lücke? Rein da!", "Torwart, schau zuerst nach vorn", "Schnell entscheiden, schnell nach vorn"],
 "materials": ["2 große Tore", "4 Hütchen", "Leibchen in zwei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Rotieren im Spielaufbau. Acht gegen acht. Team Neon baut vom Torwart aus auf und schafft sich mit Platztausch freie Räume.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": BALL, "dims": DIMS,
  "steps": [
   S("Breit machen, der Sechser kommt", "Der Torwart hat den Ball. Die beiden Innenverteidiger gehen weit auseinander. In die Lücke lässt sich Spieler vier fallen, und Spieler fünfzehn läuft mit ihm.",
     mv("n5", [24, 9]), mv("n6", [24, 47]), mv("n4", [33, 21], delay=0.4), mv("r15", [44, 20], delay=0.7), mv("r16", [30, 38], delay=0.7)),
   S("Der Zehner kommt in den Raum", "Wo Spieler fünfzehn stand, ist jetzt Platz. Spieler zehn lässt sich genau dorthin fallen. Der Torwart schaut nach vorn, sieht ihn und spielt flach durch.",
     mv("n10", [55, 31]), bl("n1", [36, 29.6], delay=0.5), ps("b1", [55.6, 31.6], after=True)),
   S("Aufdrehen, Pass auf die Spitze", "Spieler zehn dreht mit dem ersten Kontakt auf. Spieler neun steht vorn allein gegen Spieler dreizehn, und der Ball kommt zu ihm.",
     bl("n10", [66.5, 30], von=[35.5, 29.5], dauer=1.3), drehen("n10", [66.5, 30], delay=0.4), ps("b1", fuss("n9"), after=True),
     mv("r15", [50, 26], delay=0.8)),
   S("Eins gegen eins: Punkt", "Spieler neun geht ins Duell, zieht an Spieler dreizehn vorbei und trifft, und das gibt einen Punkt für Team Neon. Danach beginnt wieder der Torwart von Team Neon.",
     mv("r13", [72, 28]), dr("n9", "b1", [73, 21], delay=0.2), dr("n9", "b1", [80, 19], after=True), ps("b1", [88.6, 24], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Sechser macht die Dreierkette.", "Sechser in die Dreierkette",
    "Spieler vier lässt sich ganz zwischen die Innenverteidiger fallen. Dadurch rücken die beiden nach vorn und die Außenspieler noch höher. Jetzt kann ein Innenverteidiger mit Ball nach vorn gehen, und außen entsteht zwei gegen eins.",
    sp(r16=(32.5, 36), r7=(49.5, 43)), BALL,
    [S("Dreierkette hinten", "Spieler vier geht ganz nach hinten zwischen die Innenverteidiger. Spieler fünf und Spieler sechs schieben nach vorn, die Außenspieler gehen noch höher. Der Torwart spielt Spieler vier an.",
       mv("n4", [26, 28]), mv("n5", [33, 10], delay=0.2), mv("n6", [33, 46], delay=0.2), mv("n2", [52, 5], delay=0.3), mv("n3", [52, 50], delay=0.3),
       ps("b1", fuss("n4", {"n4": (26, 28)}), delay=1.0)),
     S("Innenverteidiger rückt ein", "Spieler vier legt auf Spieler sechs. Den läuft keiner an, also geht er mit Ball in den freien Raum.",
       ps("b1", [33.6, 46.6]), dr("n6", "b1", [43, 44], after=True)),
     S("Zwei gegen eins außen", "Spieler sieben muss sich entscheiden. Geht er auf Spieler sechs, ist Spieler drei frei. Genau dorthin geht der Pass, in den Lauf.",
       mv("r7", [48, 40]), mv("n3", [61, 50], delay=0.4), ps("b1", [61.6, 50.6], delay=0.8))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: In die Mittelzone dürfen nur zwei.", "Nur zwei in der Mittelzone",
    "In der Mitte liegt eine Zone. Von jedem Team dürfen nur zwei Spieler gleichzeitig drin sein. Geht einer raus, darf ein anderer rein. So müssen die Spieler ständig die Plätze tauschen.",
    sp(), BALL,
    [S("Einer raus, einer rein", "Spieler vier und Spieler zehn sind in der Zone. Spieler vier geht raus nach hinten, Spieler fünfzehn läuft mit. Dafür kommt Spieler zwei von außen in die Zone.",
       mv("n4", [32, 20]), mv("r15", [38, 15], delay=0.3), mv("n2", [47, 22], delay=0.5)),
     S("Pass in die Zone", "Der Torwart spielt Spieler vier an. Der spielt sofort weiter zu Spieler zwei, der in der Zone frei steht.",
       ps("b1", [32.6, 20.6]), ps("b1", [47.6, 22.6], after=True)),
     S("Steil auf die Spitze: Punkt", "Spieler zwei spielt direkt steil auf Spieler neun. Der hat Platz, geht aufs Tor und trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", fuss("n9")), dr("n9", "b1", [74, 22], after=True), ps("b1", [88.6, 24], after=True))], lines=LINES + ZONE, dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
