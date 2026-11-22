import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 06-P5 (U12-U14, Woche 18 Phase 6): Defensive Compactness Opposed Skill (How to defend as a compact 3 and recovery).
# 30 x 30 Yards = Feld x 25-75, y 5-55 (27 x 27 m). Gespiegelt: Tor mit Torwart oben (im Original unten). Unten zwei Streifen
# von je 5 Yards (gestrichelt bei y 38.3 und 46.7): Mittelfeldzone für die zwei Sechser, ganz unten die Minitore in den Ecken.
# Orange (Angreifer) -> Neon 8 (ZM), 7 (RAM), 9 (ST), 11 (LAM); Rot (Verteidiger) -> Rot 3, 5, 4 (Dreierkette), 6 (ZM),
# Torwart -> Rot 1. Angreifer zwischen die Verteidiger versetzt (3D-Abstand). Ein Trainer statt zwei.
# Die Minitore sind im Text nicht erklärt: hier als Konterziele für Team Rot nach Ballgewinn gedeutet.
# Fassungen: Steigerung 1 aus Ton und Video (Sechser schaltet sich nach direktem Pass nach vorn ein, vier gegen drei),
# Steigerung 2 = PDF-Progression 1 (Rückpasszone, mutig herausrücken, Abseits). Für die Rückpasszone Abseitslinie und Zone
# etwas näher ans Tor gelegt (3D-Abstand zum Torwart). PDF-Progression 2 (zehn Sekunden, senkrechte Drittel) nicht gebaut.
# Sichtkegel: im Ton "defenders must recognise when to get tight, when to stay with opponents" (im Video kein Kegel):
# in der ersten Steigerung sieht Rot vier den nachrückenden Neon acht kommen und bleibt bei ihm.
T = P("T", "c", 81, 42.5, "T")
POS = {"r1": (50, 8), "r3": (36.5, 22.5), "r5": (45, 24), "r4": (62.5, 22.5),
       "n7": (28, 30), "n9": (54, 29.5), "n11": (71.5, 30), "r6": (45.5, 41), "n8": (55, 45.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "r1" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 82.6, 46), B("s2", 79, 46)]
LINES = [rect(25, 5, 50, 50), line(25, 38.3, 75, 38.3), line(25, 46.7, 75, 46.7)]
KEGEL = [C(25, 38.3), C(75, 38.3), C(25, 46.7), C(75, 46.7)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 31, "y": 55, "side": "bottom"}, {"x": 69, "y": 55, "side": "bottom"}]

u = {"title": "Kompakt zu dritt verteidigen", "code": "UE-184", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 9, "players_max": 9, "field_size": "27 x 27 m",
 "description": "Drei Verteidiger mit Torwart verteidigen gegen drei Angreifer. Dahinter spielen zwei Sechser in einer schmalen Mittelfeldzone, und der Sechser von Team Neon bringt den Ball schnell nach vorn. Die Verteidiger stehen eng zusammen, drängen den Ball nach außen und gehen eng an die Stürmer. Erobern sie den Ball, kontern sie auf zwei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, oben ein Jugendtor. Unten zwei Streifen von je gut 4 Metern: die Mittelfeldzone und ganz unten zwei Minitore in den Ecken.",
  "Verteilen: Team Rot mit Torwart und drei Verteidigern vor dem Tor, dazu ein Sechser in der Mittelfeldzone. Team Neon mit drei Angreifern und einem Sechser in der Mittelfeldzone. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Der Trainer spielt den Sechser von Team Neon an. Der kombiniert mit den drei Angreifern, die aufs Tor spielen. Der Sechser von Team Rot stört ihn, die drei Verteidiger schieben zusammen und drängen nach außen.",
  "Wertung und Wechsel: Ein Treffer gibt einen Punkt für Team Neon. Erobert Team Rot den Ball und spielt ihn in ein Minitor, gibt das einen Punkt für Team Rot. Nach ein paar Minuten tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Kurze Abstände zwischen den Verteidigern, zusammen zur Ballseite schieben", "Schnell eng an den Stürmer, damit er sich nicht drehen kann", "Bei Läufern in die Tiefe bleiben und mitlaufen", "Mutig zusammen herausrücken, wenn der Ball zurückgespielt wird"],
 "materials": ["1 Jugendtor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Kompakt zu dritt verteidigen. Drei Verteidiger stehen eng zusammen und drängen die Angreifer weg vom Tor nach außen.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 81.6, 43.1)] + ERSATZ,
  "steps": [
   S("Pass ins Mittelfeld", "Der Trainer spielt Neon acht in der Mittelfeldzone an. Rot sechs geht sofort drauf und stellt den Pass in die Mitte zu.",
     ps("b1", [55.6, 46.1]), mv("r6", [55, 40], delay=0.4)),
   S("Zur Ballseite schieben", "Neon acht spielt nach außen zu Neon sieben. Rot drei läuft ihn an. Rot fünf und Rot vier schieben gleichzeitig mit zur Ballseite und bleiben eng zusammen.",
     ps("b1", [28.6, 30.6]), mv("r3", [31, 25], delay=0.3), mv("r5", [40, 24], delay=0.3), mv("r4", [52, 23], delay=0.3)),
   S("Nach außen drängen", "Rot drei steht innen und drängt Neon sieben nach außen, weg vom Tor. Rot fünf bleibt eng an Neon neun.",
     dr("n7", "b1", [27.5, 17]), mv("r3", [31.5, 16.5], delay=0.2), mv("n9", [50, 25]), mv("r5", [44, 20], delay=0.2)),
   S("Ins Minitor: Punkt", "Rot drei erobert den Ball, dribbelt los und spielt ins Minitor. Das gibt einen Punkt für Team Rot. Ein Treffer gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Neon acht.",
     ps("b1", [32.1, 17.1]), dr("r3", "b1", [36, 32], after=True), ps("b1", [31, 54.5], after=True))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=94)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Der Sechser darf mit nach vorn.", "Vier gegen drei",
    "Spielt der Sechser von Team Neon den Ball direkt nach vorn, darf er mit angreifen. Jetzt sind es vier gegen drei. Die Verteidiger müssen erkennen, wann sie eng rangehen, wann sie einen Läufer begleiten und wann sie einrücken.",
    sp(), [B("b1", 81.6, 43.1)] + ERSATZ,
    [S("Direkt nach vorn", "Der Trainer spielt zu Neon acht. Der spielt direkt zu Neon neun und sprintet sofort mit nach vorn. Jetzt sind es vier gegen drei.",
       ps("b1", [55.6, 46.1]), ps("b1", [54.6, 30.1], after=True), mv("n8", [66, 35], after=True)),
     S("Eng ran und mitgehen", "Rot fünf geht eng an Neon neun, damit er sich nicht drehen kann. Rot vier sieht Neon acht kommen und bleibt bei ihm. Rot drei rückt ein.",
       mv("r5", [51, 26]), bl("r4", [64, 38]), mv("r4", [63, 29.5], after=True), mv("r3", [42, 22], delay=0.3)),
     S("Abgefangen: Punkt", "Neon neun legt ab zu Neon acht, aber Rot vier fängt den Pass ab. Er dribbelt los und spielt ins Minitor. Das gibt einen Punkt für Team Rot.",
       ps("b1", [63.6, 30.1]), dr("r4", "b1", [57, 36], after=True), ps("b1", [69, 54.5], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Mutig herausrücken.", "Mutig herausrücken",
    "Vor der Abseitslinie liegt eine Rückpasszone. Unter Druck dürfen die Angreifer den Ball dorthin zurückspielen. Dann rücken alle drei Verteidiger gemeinsam und mutig heraus, und wer stehen bleibt, ist im Abseits.",
    sp(r1=(50, 7), r3=(35, 23), r5=(43.5, 23), r4=(60.5, 23), n7=(26.5, 28), n9=(52, 28), n11=(69, 28), r6=(60.5, 41), n8=(48, 44)),
    [B("b1", 27.1, 28.6)] + ERSATZ,
    [S("Zurück in die Zone", "Neon sieben hat den Ball, und Rot drei presst. Neon acht kommt in die Rückpasszone, und Neon sieben spielt zu ihm zurück.",
       mv("r3", [30, 25.5]), mv("n8", [42, 34], delay=0.2), ps("b1", [42.6, 34.6], after=True)),
     S("Gemeinsam heraus", "Sobald der Ball zurückgeht, rücken alle drei Verteidiger gleichzeitig heraus. Neon neun und Neon elf bleiben stehen und sind jetzt im Abseits.",
       mv("r3", [33, 31]), mv("r5", [45, 29.5]), mv("r4", [61, 31])),
     S("Ins Minitor: Punkt", "Neon acht findet keinen freien Mitspieler. Rot sechs presst von hinten und erobert den Ball. Er spielt schnell ins Minitor, und das gibt einen Punkt für Team Rot.",
       mv("r6", [45.5, 36.5]), dr("r6", "b1", [38, 46], after=True), ps("b1", [31, 54.5], after=True))],
    lines=LINES + [line(25, 25.5, 75, 25.5), {"type": "zone", "x": 25, "y": 30, "w": 50, "h": 8.3}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
