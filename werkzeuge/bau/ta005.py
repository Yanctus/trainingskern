import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# TA-005: Taktik-Erklärung (kind "Taktik", Anleitung TAKTIK.md, Vorbild ta001.py). Aufbau im 3-4-3.
# Vier Kapitel: 1 Grundordnung und Aufbau ohne Gegner (Dreierkette, Schienen, Doppelsechs, Halbstürmer im Halbraum),
# 2 gegen zwei anlaufende Stürmer (4-4-2): Überzahl in der ersten Linie, andribbeln und locken, Ball zwischen die Linien,
# 3 das Dreieck Halbverteidiger-Schiene-Halbstürmer: Außenspieler locken, Außenverteidiger rückt raus, Halbstürmer in seinen Rücken,
# 4 steil, klatschen, verlagern auf die ballferne Schiene, die breit geblieben ist.
# Recherche (24.11.2026): premierleague.com/en/news/4244194 (Rollen, Doppelsechs, Schwächen), fifatrainingcentre.com
# (Chelsea 3-4-3: Schienen breit, Halbstürmer innen, 3-2-5), coachbetter.com (3-4-3 Atalanta), renderfoot.com/de/formations/3-4-3.
# Großfeld quer: Team Neon baut links auf und spielt nach rechts. Von Team Neon aus ist oben die linke Seite.
# Nummern Neon: 4 linker Halbverteidiger, 5 zentraler Innenverteidiger, 2 rechter Halbverteidiger, 3 linke Schiene,
# 7 rechte Schiene, 6 und 8 Doppelsechs, 10 linker Halbstürmer, 11 rechter Halbstürmer, 9 Mittelstürmer.
# Team Rot (4-4-2) 12-21, beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Ein Trainer.

GRUND = {"k1": (10.5, 27.5), "n4": (24, 16), "n5": (22, 27.5), "n2": (24, 39), "n3": (40, 7), "n7": (40, 48),
         "n6": (37, 21), "n8": (39, 34), "n10": (56, 17), "n11": (56, 38), "n9": (62, 27.5)}
GROSS = {"k1": (10.5, 27.5), "n4": (20, 12), "n5": (17, 27.5), "n2": (20, 43), "n3": (46, 5), "n7": (46, 50),
         "n6": (32, 21), "n8": (32, 34), "n10": (60, 16), "n11": (60, 39), "n9": (70, 27.5)}

# ---------- Kapitel 1: Grundordnung und Aufbau ohne Gegner ----------
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 3-4-3", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Drei-vier-drei. Hinten die Dreierkette: ein Innenverteidiger in der Mitte, links und rechts die zwei Halbverteidiger. Davor die Doppelsechs, und ganz außen die zwei Schienenspieler. Vorn der Mittelstürmer, mit zwei Halbstürmern neben sich.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Das Feld groß machen", "Sobald der Torwart den Ball hat, ziehen wir das Feld auseinander. Die Halbverteidiger gehen raus an die Ecken vom Strafraum, der zentrale bleibt vor dem Torwart. Die Schienen schieben hoch an die Linie. Und die Halbstürmer? Die gehen nach innen, in die Halbräume zwischen den Linien.",
            *L.schieb(GROSS)))
s3 = L.opts("n4", "n5", "n2")
s3.append(L.pas("n4", after=True))
s3 += L.schieb({"n5": (19, 24), "n2": (23, 38), "n6": (31, 18), "n8": (34, 31), "n10": (58, 14), "n9": (68, 25),
                "n11": (60, 35), "n7": (48, 47), "n4": (24, 11)}, delay=2.0)
k1.append(S("Drei Wege für den Torwart", "Jetzt schau auf den Torwart. Drei Innenverteidiger, also drei Anspielstationen. Er spielt nach links auf den Halbverteidiger, der hat am meisten Platz. Und mit dem Ball schiebt die ganze Mannschaft rüber. Nur die Schiene auf der anderen Seite bleibt breit.", *s3))
s4 = L.opts("n3", "n10", "n6")
s4.append(L.pas("n3", after=True))
s4 += L.schieb({"n10": (54, 15), "n9": (76, 23), "n4": (28, 10), "n6": (36, 16), "n8": (37, 29), "n5": (22, 22),
                "n2": (26, 36), "n11": (64, 31), "n7": (52, 46)}, delay=2.0)
k1.append(S("Das Dreieck auf der Seite", "Der Halbverteidiger hat drei Möglichkeiten: die Schiene außen, den Halbstürmer im Halbraum oder den Sechser. Er spielt die Schiene. Und jetzt pass auf: Einer kommt, einer geht. Der Halbstürmer kommt dem Ball entgegen. Dafür geht der Mittelstürmer in die Tiefe und schiebt die Abwehr nach hinten.", *s4))
s5 = L.opts("n10", "n4", "n6")
s5 += [bl("n10", f(L.p["n3"]), after=True), L.pas("n10", after=True)]
s5 += L.schieb({"n3": (62, 5), "n6": (42, 17), "n11": (68, 32), "n8": (40, 28), "n4": (32, 10)}, delay=3.0)
k1.append(S("Rein in den Halbraum", "Die Schiene spielt flach rein in den Halbraum. Der Halbstürmer steht offen und schaut zum Ball, also kriegt er ihn. Hinter ihm rückt der Sechser nach. Und die Schiene? Die geht sofort die Linie runter.", *s5))
von = f(L.p["n3"])
s6 = [bl("n10", list(L.p["n9"]), von=von, dauer=1.3), drehen("n10", list(L.p["n9"]), delay=0.4)]
s6 += L.opts("n3", "n9", "n11", delay=1.5)
s6 += L.steil("n3", (78, 6), delay=2.6)
s6 += L.schieb({"n9": (82, 25), "n11": (78, 34), "n10": (64, 16), "n7": (64, 44), "n6": (48, 18), "n8": (46, 30)}, delay=3.0)
k1.append(S("Aufdrehen und Tiefe", "Erst nach der Annahme dreht der Halbstürmer auf. Vor ihm drei Möglichkeiten: die Schiene außen, der Mittelstürmer oder der zweite Halbstürmer. Die Schiene ist frei, also ab in ihren Lauf. Und vorn gehen der Mittelstürmer und der zweite Halbstürmer in den Strafraum.", *s6))

# ---------- Kapitel 2: gegen zwei anlaufende Stürmer (Gegner im 4-4-2) ----------
ROT2 = {"k2": (88, 27.5), "r13": (74, 8), "r14": (76, 21), "r15": (76, 34), "r12": (74, 47),
        "r16": (52, 9), "r17": (52, 21), "r18": (52, 33), "r21": (52, 46), "r19": (40, 24), "r20": (40, 36)}
L2 = Lage(GROSS, ROT2, ball="k1")
k2 = []
a = L2.schieb({"r19": (26, 19), "r20": (26, 36), "r16": (42, 8), "r17": (39, 23), "r18": (39, 33), "r21": (42, 47),
               "r13": (68, 10), "r14": (68, 22), "r15": (68, 33), "r12": (68, 45)})
a += L2.schieb({"n9": (67, 27.5), "n10": (58, 16), "n11": (58, 39), "n6": (32, 20), "n8": (32, 35)}, delay=0.3)
k2.append(S("Zwei Stürmer laufen an", "Jetzt wird's ernst. Der Gegner presst im Vier-vier-zwei. Seine zwei Stürmer laufen gegen unsere drei Innenverteidiger. Hinten sind wir also immer einer mehr, und der Torwart spielt auch noch mit. Die Schienen und die Doppelsechs stellt er zu. Dafür haben die Halbstürmer Platz zwischen den Linien.", *a))
b2 = L2.opts("n4", "n5", "n2")
b2.append(L2.pas("n5", after=True))
b2 += L2.schieb({"r19": (27, 21), "r20": (29, 36), "r17": (40, 22), "r18": (40, 34)}, delay=2.0)
b2 += L2.schieb({"n6": (33, 19), "n8": (33, 36), "n10": (58, 17), "n11": (58, 38)}, delay=2.0)
k2.append(S("Drei gegen zwei", "Der Torwart hat drei Anspielstationen. Er nimmt den zentralen Innenverteidiger. Die zwei Stürmer stehen jetzt genau zwischen unseren drei Verteidigern. Einen von uns können sie also nie anlaufen.", *b2))
c2 = [L2.dribbel("n5", (25, 27.5))]
c2 += L2.schieb({"r19": (30, 26)}, delay=0.6)
c2 += L2.schieb({"n4": (22, 10), "n2": (22, 45)}, delay=0.6)
c2 += L2.opts("n4", "n2", "n6", delay=1.6, zu=("n6",))
c2.append(L2.pas("n4", after=True))
c2 += L2.schieb({"r19": (28, 16), "r17": (40, 20), "r16": (42, 9), "r20": (28, 28), "r18": (42, 30)}, delay=3.0)
c2 += L2.schieb({"n5": (22, 24), "n2": (24, 40), "n6": (34, 18), "n8": (34, 32)}, delay=3.0)
k2.append(S("Andribbeln und locken", "Der zentrale Innenverteidiger hat Platz, also dribbelt er an. So lange, bis ein Stürmer kommt. Jetzt kommt er. Der Sechser steht in seinem Rücken, der ist zu. Aber außen ist der Halbverteidiger frei. Also geht der Ball dahin, und der Gegner muss wieder verschieben.", *c2))
d2 = [L2.dribbel("n4", (32, 12))]
d2 += L2.schieb({"r16": (40, 8)}, delay=0.5)
d2 += L2.schieb({"n10": (57, 19), "n3": (56, 5)}, delay=0.5)
d2 += L2.opts("n3", "n10", "n6", delay=1.6, zu=("n3", "n6"))
d2.append(L2.pas("n10", after=True))
d2 += L2.schieb({"r17": (46, 18), "r13": (68, 8)}, delay=3.0)
k2.append(S("Durch den Halbraum", "Auch der Halbverteidiger dribbelt an. Der Außenspieler bleibt bei unserer Schiene und macht den Weg nach außen zu. Den Sechser hat der Stürmer im Schatten. Und jetzt pass auf: Der Halbstürmer kommt in die Lücke, und die Schiene geht hoch an die Linie. Da ist der Weg frei, flach rein in den Halbraum.", *d2))
von2 = f(L2.p["n4"])
e2 = [bl("n10", list(L2.p["n9"]), von=von2, dauer=1.3), drehen("n10", list(L2.p["n9"]), delay=0.4)]
e2 += L2.opts("n3", "n11", "n9", delay=1.5, zu=("n9",))
e2 += L2.steil("n9", (80, 14), delay=2.6)
e2 += L2.schieb({"n11": (72, 34), "n3": (68, 4), "n10": (62, 18)}, delay=2.6)
e2 += L2.schieb({"r14": (76, 19), "r13": (74, 10), "r15": (74, 30), "r17": (50, 18), "r16": (48, 10)}, delay=3.0)
e2 += L2.schieb({"n6": (44, 16), "n8": (46, 34), "n4": (38, 12), "n5": (24, 24), "n2": (30, 40)}, delay=2.8)
k2.append(S("Hinter die Kette", "Der Halbstürmer dreht auf. Zwei Reihen sind schon überspielt. Vor ihm die Schiene und der zweite Halbstürmer. Der Mittelstürmer steht noch zwischen zwei Verteidigern, also zu. Aber zwischen Außen- und Innenverteidiger ist eine Lücke. Er startet genau mit dem Pass, also kein Abseits. Und der Ball kommt direkt in seinen Lauf.", *e2))

# ---------- Kapitel 3: das Dreieck Halbverteidiger, Schiene, Halbstürmer ----------
NEON3 = {"k1": (10.5, 27.5), "n4": (30, 10), "n5": (22, 26), "n2": (28, 42), "n6": (36, 21), "n8": (36, 35),
         "n3": (46, 4), "n7": (46, 50), "n10": (62, 15), "n11": (62, 38), "n9": (68, 27.5)}
ROT3 = {"k2": (88, 27.5), "r13": (72, 9), "r14": (74, 21), "r15": (74, 33), "r12": (72, 45),
        "r16": (54, 8), "r17": (54, 20), "r18": (54, 32), "r21": (54, 45), "r19": (42, 24), "r20": (44, 36)}
L3 = Lage(NEON3, ROT3, ball="n4")
k3 = []
a = [L3.dribbel("n4", (34, 9))]
a += L3.schieb({"r16": (43, 12)}, delay=0.4)
a += L3.schieb({"n3": (50, 4), "r19": (40, 21), "r17": (52, 19), "r18": (52, 30), "r20": (42, 33), "r21": (54, 42)}, delay=0.6)
a += L3.schieb({"n10": (63, 13), "n6": (38, 18), "n8": (38, 31), "n5": (24, 22), "n2": (30, 38), "n7": (48, 47)}, delay=0.6)
k3.append(S("Einer gegen zwei", "Neue Situation. Der Gegner steht jetzt tiefer, im Mittelfeld. Der Halbverteidiger hat den Ball, vor ihm die Schiene und der Halbstürmer. Das ist unser Dreieck auf der Seite. Der Außenspieler vom Gegner hat jetzt ein Problem: Er muss zwei verteidigen. Der Halbverteidiger dribbelt an, und der Außenspieler kommt raus.", *a))
b3 = L3.opts("n3", "n10", "n6", zu=("n6", "n10"))
b3.append(L3.pas("n3", after=True))
b3 += L3.schieb({"r13": (60, 4), "r14": (77, 24), "r17": (50, 17), "r16": (46, 9)}, delay=2.0)
b3 += L3.schieb({"n6": (42, 15), "n4": (36, 10), "n8": (40, 30), "n5": (24, 23), "n9": (72, 28), "n11": (64, 33)}, delay=2.0)
k3.append(S("Die Schiene ist frei", "Damit ist die Schiene frei. Den Halbstürmer macht der Außenspieler mit seinem Laufweg zu, den Sechser verdeckt der Stürmer. Also geht der Ball raus an die Linie. Jetzt muss der Außenverteidiger raus auf die Schiene. Und genau das wollen wir. Der Sechser rückt schon nach, und der Halbstürmer bleibt erst mal innen.", *b3))
c3 = L3.opts("n10", "n6", "n4", zu=("n6", "n4"))
c3 += L3.steil("n10", (72, 18), delay=1.6)
c3 += L3.schieb({"r13": (66, 10), "r14": (78, 21), "r15": (77, 30), "r12": (72, 40)}, delay=2.2)
c3 += L3.schieb({"n6": (40, 11)}, delay=1.6)
c3 += L3.schieb({"n11": (68, 33), "n3": (58, 4)}, delay=2.0)
k3.append(S("In den Rücken", "Der Außenverteidiger läuft die Schiene an. Hinter ihm ist jetzt ein Loch. Und jetzt pass auf: Der Sechser kommt nach und sichert ab. Und der Halbstürmer geht, genau in dieses Loch, mit dem Pass. Kurz zurück ist zu, da läuft der Außenspieler hinterher. Also spielt die Schiene direkt, schräg in den Lauf. Ein Gegner, zwei Probleme.", *c3))
d3 = [L3.dribbel("n10", (81, 15))]
d3 += L3.schieb({"r14": (85, 20), "r15": (84, 28), "r12": (72, 38), "r13": (76, 12)}, delay=0.3)
d3 += L3.schieb({"n9": (82, 25), "n11": (74, 30), "n3": (66, 5)}, delay=0.3)
d3 += L3.opts("n9", "n3", "n11", delay=1.6, zu=("n9", "n3"))
d3.append(L3.pas("n11", after=True))
k3.append(S("Flach in den Rückraum", "Jetzt ist er durch und geht in den Strafraum. Den Mittelstürmer hat der Innenverteidiger. Zurück zur Schiene geht's nicht, da läuft der Außenverteidiger hinterher. Aber hinten kommt der zweite Halbstürmer, und der steht frei. Also flach zu ihm.", *d3))

# ---------- Kapitel 4: steil, klatschen, verlagern auf die ballferne Schiene ----------
NEON4 = {"k1": (10.5, 27.5), "n4": (28, 12), "n5": (24, 27.5), "n2": (28, 43), "n6": (34, 18), "n8": (34, 37),
         "n3": (47, 4), "n7": (47, 51), "n10": (62, 15), "n11": (62, 40), "n9": (70, 27.5)}
ROT4 = {"k2": (88, 27.5), "r13": (73, 9), "r14": (76, 21), "r15": (76, 33), "r12": (73, 45),
        "r16": (54, 9), "r17": (55, 21), "r18": (55, 33), "r21": (54, 45), "r19": (40, 21), "r20": (40, 34)}
L4 = Lage(NEON4, ROT4, ball="n5")
k4 = []
a = L4.schieb({"n9": (64, 27.5), "n10": (70, 20)})
a += L4.opts("n6", "n8", "n9", delay=1.2, zu=("n6", "n8"))
a.append(L4.pas("n9", after=True))
a += L4.schieb({"r17": (61, 22), "r18": (62, 33), "r14": (70, 24), "r16": (56, 14), "r21": (58, 40)}, delay=2.8)
a += [mv("n8", [42, 40], delay=2.8), mv("n8", [48, 30], after=True), mv("n6", [44, 17], delay=2.8)]
L4.p.update({"n8": (48, 30), "n6": (44, 17)})
k4.append(S("Steil", "Zum Schluss ein Muster, das du im Drei-vier-drei immer wieder siehst. Der Gegner steht eng, und seine zwei Stürmer stellen unsere Doppelsechs zu. Aber in der Mitte ist eine Gasse. Einer kommt, einer geht: Der Mittelstürmer kommt entgegen, und der Halbstürmer geht nach vorn an die letzte Linie. Also steil in den Mittelstürmer.", *a))
b4 = L4.opts("n8", "n6", "n5", zu=("n6", "n5"))
b4.append(L4.pas("n8", after=True))
b4 += L4.schieb({"r20": (44, 36), "r18": (56, 34), "r21": (60, 37), "r17": (56, 25), "r19": (44, 24)}, delay=1.5)
b4 += L4.schieb({"n7": (56, 51), "n11": (68, 40), "r12": (72, 42), "n2": (34, 44)}, delay=1.5)
k4.append(S("Klatschen lassen", "Der Mittelstürmer hat den Gegner im Rücken. Also dreht er nicht auf, er lässt klatschen. Den zweiten Sechser hat ein Gegner im Schatten, und zurück ist auch zu. Aber der Sechser auf dieser Seite ist an seinem Stürmer vorbei mitgelaufen und steht frei. Er kriegt den Ball mit Blick nach vorn. Und der ganze Gegner zieht sich in die Mitte.", *b4))
c4 = L4.opts("n7", "n11", "n9", zu=("n11", "n9"))
c4.append(L4.pas("n7", after=True))
c4 += L4.schieb({"r21": (60, 45), "r18": (58, 38), "r12": (74, 44), "r15": (78, 33), "r14": (76, 24)}, delay=2.0)
c4 += L4.schieb({"n11": (72, 38), "n9": (72, 28), "n10": (76, 20), "n8": (52, 36)}, delay=2.0)
k4.append(S("Verlagern", "Und jetzt schau nach außen. Innen ist alles zu. Aber die Schiene auf der anderen Seite ist die ganze Zeit breit geblieben. Da ist keiner. Also verlagert der Sechser sofort. Der Gegner schiebt rüber, aber er kommt zu spät.", *c4))
d4 = [L4.dribbel("n7", (68, 49))]
d4 += L4.schieb({"r12": (75, 48), "r21": (62, 48), "r15": (80, 33), "r14": (79, 24), "r18": (62, 40), "r17": (60, 28), "r16": (60, 16), "r13": (76, 12)}, delay=0.4)
d4 += L4.schieb({"n9": (76, 30), "n3": (68, 8), "n8": (58, 40), "n6": (52, 24), "n2": (40, 44), "n4": (36, 16), "n5": (30, 28)}, delay=0.4)
d4 += L4.opts("n11", "n9", "n10", delay=1.4, zu=("n10",))
d4.append(L4.pas("n11", after=True))
k4.append(S("Wer ist jetzt frei?", "Die Schiene nimmt den Ball mit nach vorn. Jetzt muss der Außenverteidiger raus. Den Halbstürmer auf der anderen Seite hat der Innenverteidiger. Aber der auf unserer Seite steht innen frei. Also flach zu ihm. Steil, klatschen, verlagern. So kommen wir dahin, wo der Gegner nicht ist.", *d4))

u = {"title": "Aufbau im 3-4-3", "code": "TA-005", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 3-4-3 von hinten auf? Zuerst siehst du die Grundordnung mit Dreierkette, Doppelsechs, zwei Schienen und drei Stürmern, und wie alle mit dem Ball verschieben. Dann presst ein Gegner mit zwei Stürmern, und die Überzahl in der ersten Linie bringt den Ball zwischen die Linien. Danach geht es um das Dreieck aus Halbverteidiger, Schiene und Halbstürmer und zum Schluss um steil, klatschen, verlagern.",
 "organisation": ["Grundordnung: Torwart, Dreierkette, Doppelsechs, zwei Schienenspieler, vorn ein Mittelstürmer und zwei Halbstürmer.",
  "Hinten: Die Halbverteidiger gehen breit bis an die Ecken vom Strafraum, der zentrale Innenverteidiger bleibt vor dem Torwart, gegen zwei Stürmer ist immer einer frei.",
  "Breite und Halbraum: Die Schienen geben außen an der Linie die Breite, die Halbstürmer stehen innen in den Halbräumen zwischen den Linien.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball, die ballferne Schiene bleibt breit. Einer kommt, einer geht."],
 "organisation_show": ORG,
 "coaching_points": ["Schiene an die Linie, Halbstürmer nach innen", "Hinten einer mehr: andribbeln, bis einer kommt", "Einer kommt, einer geht", "Steil, klatschen, verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "frei", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Drei-vier-drei. Heute keine Übung, sondern das System dahinter. Wer steht wo? Wer gibt die Breite, und wer besetzt die Räume dazwischen? Und wie kommen wir gegen ein Pressing nach vorn? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Gegen zwei Stürmer",
    "Jetzt presst ein Gegner im 4-4-2 mit zwei Stürmern. Gegen drei Innenverteidiger ist hinten immer einer frei. Wer am Ball ist, dribbelt an, bis ein Gegner kommt, und spielt dann den freien Mann. So kommt der Ball zum Halbstürmer zwischen die Linien.",
    Lage(GROSS, ROT2).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Das Dreieck auf der Seite.", "Das Dreieck auf der Seite",
    "Halbverteidiger, Schiene und Halbstürmer bilden auf jeder Seite ein Dreieck. Der gegnerische Außenspieler muss zwei verteidigen. Kommt er raus, ist die Schiene frei. Rückt dann der Außenverteidiger auf die Schiene, startet der Halbstürmer in seinen Rücken.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 30.6, 10.6)] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Steil, klatschen, verlagern.", "Steil, klatschen, verlagern",
    "Der Ball geht steil in den Mittelstürmer, der entgegenkommt. Er lässt auf den Sechser klatschen, der mit Blick nach vorn kommt. Weil der Gegner sich in der Mitte zusammenzieht, verlagert der Sechser auf die ballferne Schiene. Die ist breit geblieben und hat Platz.",
    Lage(NEON4, ROT4).spieler(), [B("b1", 24.6, 28.1)] + ERSATZ, k4)]}
fertig()
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
