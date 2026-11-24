import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# TA-003: Taktik-Erklärung (kind "Taktik", Vorbild TA-001, Regeln werkzeuge/anleitung/TAKTIK.md). Aufbau im flachen 4-4-2.
# Vier Kapitel: 1 Grundordnung ohne Gegner (Feld groß machen, staffeln, weil die flache Vier von sich aus kaum Dreiecke hat,
# Dreieck Außenverteidiger-Flügel-Mittelfeld, Flügel kommt / Stürmer geht), 2 gegen das Pressing eines 4-3-3 mit drei Stürmern
# (Linksverteidiger bleibt tief: Dreierkette plus Torwart gegen drei, Torwart findet den freien Mann außen, Flügel kommt,
# Stürmer geht hinter den Außenverteidiger), 3 das Stürmerpaar (einer lässt sich fallen und zieht seinen Innenverteidiger mit,
# Pass durch zwei Reihen, klatschen lassen, der andere geht in die Lücke), 4 Seitenwechsel über die Doppelsechs und
# Hinterlaufen (Flügel zieht nach innen, Außenverteidiger läuft außen vorbei, Ball in den Lauf, zurück in den Rückraum).
# Recherche (24.11.2026): premierleague.com/en/news/4243787, learning.coachesvoice.com (4-4-2 Ferguson/Simeone/Dyche),
# tactico.pages.dev/formations/4-4-2 (4-3-3-Pressing: drei Stürmer auf vier Verteidiger, Lösung Dreierkette), goal.com (4-4-2).
# Nummern im klassischen 4-4-2: 2 RV, 3 LV, 4 und 5 Innenverteidiger, 6 und 8 zentrale Mittelfeldspieler, 7 rechter Flügel,
# 11 linker Flügel, 9 und 10 die Stürmer. Neon baut links auf und spielt nach rechts, oben ist die linke Seite.
# Team Rot (4-3-3) neu nummeriert 12-21: Abwehr 13/14/15/12 (von oben nach unten), Sechser 16, Achter 17 und 18,
# Mittelstürmer 19, Flügelstürmer 20 (oben) und 21 (unten). Torhüter neutral k1 (Neon) und k2 (Rot). Ein Trainer.

# ---------- Kapitel 1: Grundordnung, Feld groß machen, staffeln, Aufbau ohne Gegner ----------
GRUND = {"k1": (10.5, 27.5), "n5": (24, 21), "n4": (24, 34), "n3": (31, 8), "n2": (31, 47), "n6": (39, 21.5),
         "n8": (39, 33.5), "n11": (50, 8), "n7": (50, 47), "n9": (62, 21.5), "n10": (62, 33.5)}
GROSS = {"n5": (19, 14), "n4": (19, 41), "n3": (38, 5), "n2": (38, 50), "n6": (30, 24), "n8": (46, 34),
         "n11": (60, 6), "n7": (60, 49), "n9": (72, 22), "n10": (64, 32)}
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 4-4-2", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Vier-vier-zwei. Hinten die Viererkette, davor die zweite Viererkette: zwei Mittelfeldspieler in der Mitte und außen die beiden Flügelspieler. Und vorn zwei Stürmer nebeneinander. Zwei Ketten, schön kompakt.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Feld groß machen und staffeln", "Sobald der Torwart den Ball hat, machen wir das Feld groß. Die Innenverteidiger gehen breit, die Außenverteidiger hoch an die Linie. Und jetzt pass auf: Im Vier-vier-zwei stehen viele auf einer Linie. Dann gibt's kaum Dreiecke. Also staffeln wir. Ein Mittelfeldspieler bleibt tief, der andere schiebt hoch. Vorn genauso: Ein Stürmer bleibt ganz vorn, der andere lässt sich etwas fallen.",
            *L.schieb(GROSS)))
s3 = L.opts("n5", "n6", "n4")
s3.append(L.pas("n4", after=True))
s3 += L.schieb({"n5": (22, 21), "n6": (30, 31), "n2": (44, 50), "n8": (48, 40), "n3": (38, 10), "n11": (60, 12),
                "n9": (72, 27), "n10": (62, 36), "n7": (64, 49)}, delay=2.0)
k1.append(S("Drei Möglichkeiten für den Torwart", "Jetzt schau auf den Torwart. Er hat drei Möglichkeiten: die beiden Innenverteidiger oder den tiefen Mittelfeldspieler. Er spielt nach rechts. Und mit dem Ball schiebt die ganze Mannschaft rüber. Auch die, die weit weg sind.", *s3))
s4 = L.opts("n2", "n8", "n6")
s4.append(L.pas("n2", after=True))
s4 += L.schieb({"n8": (52, 42), "n7": (66, 49), "n6": (34, 38), "n4": (24, 45), "n5": (24, 26), "n10": (64, 38),
                "n9": (74, 30), "n11": (60, 16), "n3": (40, 14)}, delay=2.0)
k1.append(S("Das Dreieck auf der Seite", "Rechts ist am meisten Platz, also geht der Ball raus zum Außenverteidiger. Jetzt steht da ein Dreieck: Außenverteidiger, Flügel und schräg davor der Mittelfeldspieler. Das muss man im Vier-vier-zwei bauen. Von allein ist es nicht da.", *s4))
s5 = L.schieb({"n7": (58, 47), "n10": (76, 42)})
s5 += L.opts("n7", "n8", "n4", delay=1.4)
s5.append(L.pas("n7", after=True))
s5 += L.schieb({"n2": (50, 50), "n8": (56, 38), "n6": (40, 36), "n9": (76, 28), "n11": (66, 16), "n3": (44, 12),
                "n4": (28, 44), "n5": (26, 28)}, delay=3.0)
k1.append(S("Einer kommt, einer geht", "Und jetzt pass auf: Einer kommt, einer geht. Der Flügel kommt dem Ball entgegen. Im selben Moment geht der Stürmer in die Tiefe, genau in den Raum, den der Flügel frei macht. Der Außenverteidiger hat drei Möglichkeiten. Der Flügel steht offen, also kriegt er den Ball.", *s5))
von = f(L.p["n2"])
s6 = [bl("n7", list(L.p["n10"]), von=von, dauer=1.3), drehen("n7", list(L.p["n10"]), delay=0.4)]
s6 += L.opts("n10", "n8", "n2", delay=1.5)
s6.append(L.pas("n10", after=True))
s6 += L.schieb({"n9": (82, 30), "n11": (76, 18), "n8": (64, 38), "n6": (50, 34), "n2": (62, 50)}, delay=3.2)
k1.append(S("Aufdrehen, dann in die Tiefe", "Erst nach der Annahme dreht der Flügel auf. Vor ihm der Stürmer in der Tiefe, der Mittelfeldspieler, und hinten der Außenverteidiger. Der Stürmer ist durch, also bekommt er den Ball. Und der zweite Stürmer? Der geht mit in den Strafraum.", *s6))

# ---------- Kapitel 2: gegen das Pressing eines 4-3-3 mit drei Stürmern ----------
NEON2 = {"k1": (10.5, 27.5), "n5": (19, 14), "n4": (19, 41), "n3": (36, 5), "n2": (36, 50), "n6": (28, 25), "n8": (48, 33),
         "n11": (62, 5), "n7": (62, 50), "n9": (68, 22), "n10": (63, 34)}
ROT2 = {"k2": (88, 27.5), "r13": (78, 9), "r14": (76, 21), "r15": (76, 34), "r12": (78, 46),
        "r17": (56, 14), "r16": (54, 27.5), "r18": (56, 41), "r20": (42, 14), "r19": (40, 27.5), "r21": (42, 41)}
L2 = Lage(NEON2, ROT2, ball="k1")
k2 = []
a = L2.schieb({"r20": (22, 17), "r19": (25, 29), "r21": (25, 39), "r17": (40, 20), "r16": (44, 28), "r18": (46, 40),
               "r13": (64, 8), "r14": (64, 20), "r15": (64, 33), "r12": (64, 45)})
a += L2.schieb({"n3": (16, 7), "n5": (18, 22), "n6": (34, 26), "n8": (40, 38), "n2": (46, 50), "n11": (52, 5),
                "n7": (58, 46), "n9": (62, 20), "n10": (58, 32)}, delay=0.3)
k2.append(S("Drei Stürmer laufen an", "Jetzt wird's ernst. Der Gegner spielt Vier-drei-drei und läuft mit drei Stürmern an. Gegen unsere zwei Innenverteidiger wär das Überzahl für ihn. Also bleibt unser Linksverteidiger hinten, und die Innenverteidiger rücken rüber. Jetzt sind wir hinten zu dritt, plus Torwart. Vier gegen drei. Und auch hier: Einer kommt, einer geht. Der Linksverteidiger kommt nach hinten, dafür geht der Rechtsverteidiger ganz hoch.", *a))
b2 = L2.opts("n3", "n5", "n4", zu=("n5", "n4"))
b2.append(L2.pas("n3", after=True))
b2 += L2.schieb({"r20": (21, 13), "r19": (22, 24), "r17": (36, 16), "r16": (40, 24), "r18": (44, 38)}, delay=2.0)
b2 += L2.schieb({"n6": (32, 20), "n5": (17, 21), "n8": (42, 35)}, delay=2.2)
k2.append(S("Wer ist frei?", "Der Torwart schaut sich um. Den mittleren Innenverteidiger und den rechten stellen die Flügelstürmer zu. Den Mittelfeldspieler verdeckt der Mittelstürmer. Aber ganz links steht der Linksverteidiger frei. Also geht der Ball dahin. Und sofort kommt der Flügelstürmer raus und läuft ihn von innen an.", *b2))
c2 = L2.schieb({"n11": (40, 6), "r13": (49, 12), "n9": (63, 11)})
c2 += L2.opts("n11", "n6", "n5", delay=1.4, zu=("n6", "n5"))
c2.append(L2.pas("n11", after=True))
c2 += L2.schieb({"r13": (46, 13), "r17": (38, 12), "r16": (40, 22), "r14": (64, 18), "r20": (24, 12),
                 "n10": (60, 26), "n8": (46, 34), "n2": (50, 50), "n7": (60, 44)}, delay=2.4)
k2.append(S("Flügel kommt, Stürmer geht", "Einer kommt, einer geht. Der linke Flügel kommt dem Ball entgegen, und sein Gegenspieler läuft mit. Genau in dem Moment geht der Stürmer los, in den Raum hinter dem Verteidiger. Innen ist alles zu. Aber der Flügel ist frei, also kriegt er den Ball.", *c2))
d2 = L2.opts("n9", "n6", "n3", zu=("n6",))
d2 += L2.steil("n9", (74, 8), delay=1.6)
d2 += L2.schieb({"r14": (70, 12), "r15": (68, 26), "r13": (52, 10), "n10": (66, 26), "n7": (64, 38), "n8": (52, 34),
                 "n6": (40, 22), "n11": (48, 6)}, delay=1.8)
k2.append(S("Hinter die Kette", "Der Flügel hat drei Möglichkeiten. Den Mittelfeldspieler stellt der Achter zu. Zurück geht immer. Aber der Stürmer ist unterwegs. Er startet genau mit dem Pass, so steht er nicht im Abseits. Und der Ball kommt direkt in seinen Lauf.", *d2))
e2 = [L2.dribbel("n9", (80, 14))]
e2 += L2.schieb({"n10": (74, 24), "n7": (72, 40), "n8": (60, 32), "n2": (58, 50), "n11": (56, 6), "n3": (28, 8)}, delay=0.3)
e2 += L2.schieb({"r14": (76, 11), "r15": (78, 32), "r12": (74, 44), "r13": (60, 10), "r17": (46, 14)}, delay=0.6)
e2 += L2.opts("n10", "n8", delay=2.2)
k2.append(S("Pressing überspielt", "Drei Pässe, und das Pressing ist überspielt. Der Stürmer zieht Richtung Strafraum. Und die anderen? Die rücken nach. Der zweite Stürmer kommt in die Mitte, dahinter der Mittelfeldspieler. Und der rechte Flügel geht an den zweiten Pfosten.", *e2))

# ---------- Kapitel 3: das Stürmerpaar, einer kommt, einer geht ----------
NEON3 = {"k1": (10.5, 27.5), "n5": (26, 17), "n4": (30, 38), "n3": (42, 6), "n2": (42, 50), "n6": (36, 24), "n8": (40, 37),
         "n11": (64, 6), "n7": (64, 48), "n9": (68, 20), "n10": (68, 32)}
ROT3 = {"k2": (88, 27.5), "r13": (78, 9), "r14": (76, 21), "r15": (76, 33), "r12": (78, 46),
        "r17": (58, 14), "r16": (58, 27), "r18": (58, 40), "r20": (48, 14), "r19": (48, 28), "r21": (48, 42)}
L3 = Lage(NEON3, ROT3, ball="n4")
k3 = []
a = L3.schieb({"r21": (38, 44), "r19": (44, 28), "r20": (44, 14), "r17": (56, 18), "r16": (54, 26), "r18": (56, 40),
               "r13": (76, 14), "r14": (77, 22), "r15": (76, 34), "r12": (76, 45)})
a += L3.schieb({"n8": (44, 36), "n6": (42, 22), "n2": (44, 50), "n7": (64, 46), "n11": (64, 10), "n3": (44, 8),
                "n5": (26, 20)}, delay=0.3)
a += L3.schieb({"n10": (61, 30)}, delay=1.4)
a += L3.schieb({"r15": (69, 31), "n9": (73, 27)}, delay=1.7)
k3.append(S("Zwei Stürmer, zwei Wege", "Neue Situation. Der Gegner steht jetzt tiefer und schiebt zum Ball. Schau auf die zwei Stürmer. Einer kommt, einer geht. Der eine lässt sich fallen, zwischen die Linien. Sein Innenverteidiger läuft mit raus. Und genau da geht der andere los, in den Raum, den der Verteidiger frei macht.", *a))
b3 = L3.opts("n10", "n8", "n2", zu=("n2",))
b3.append(L3.pas("n10", after=True))
b3 += L3.schieb({"r15": (64, 32), "r16": (57, 35), "r19": (46, 30), "r17": (57, 16), "n6": (50, 22), "n8": (50, 37),
                 "r21": (42, 44), "n4": (32, 36)}, delay=2.0)
k3.append(S("Durch zwei Reihen", "Der Innenverteidiger hat drei Möglichkeiten. Außen stellt ihn der Flügelstürmer zu. Der Mittelfeldspieler ist frei, der Stürmer auch. Er spielt flach durch die Lücke, direkt in den Fuß vom Stürmer. Zwei Reihen überspielt. Und der Verteidiger klebt ihm im Rücken.", *b3))
c3 = L3.opts("n6", "n8", zu=("n8",))
c3.append(L3.pas("n6", after=True))
c3 += L3.schieb({"r17": (54, 18), "r19": (46, 26), "n8": (54, 40), "n11": (66, 12), "n2": (50, 50)}, delay=1.8)
k3.append(S("Klatschen lassen", "Aufdrehen geht nicht, der Verteidiger ist zu nah dran. Also lässt der Stürmer direkt prallen. Den einen Mittelfeldspieler stellt der Sechser zu, der andere ist nachgerückt und frei. Der kriegt den Ball, mit Blick nach vorn.", *c3))
d3 = L3.opts("n9", "n10", "n11", zu=("n11",))
d3 += L3.steil("n9", (84, 32), delay=1.6)
d3 += L3.schieb({"r14": (80, 28), "r12": (80, 40), "r15": (70, 32), "n10": (72, 30), "n11": (74, 14), "n7": (72, 44),
                 "n8": (60, 36)}, delay=1.8)
k3.append(S("Der andere geht", "Und der andere Stürmer? Der ist schon unterwegs. Er startet genau mit dem Pass, also kein Abseits. Der Ball kommt in die Lücke, die sein Partner aufgemacht hat. Einer kommt, einer geht. So funktioniert das Stürmerpaar im Vier-vier-zwei.", *d3))

# ---------- Kapitel 4: Seitenwechsel über die Mitte und Hinterlaufen ----------
NEON4 = {"k1": (10.5, 27.5), "n5": (26, 16), "n4": (26, 38), "n3": (42, 7), "n2": (40, 49), "n6": (40, 24), "n8": (52, 42),
         "n11": (64, 5), "n7": (62, 48), "n9": (68, 18), "n10": (68, 30)}
ROT4 = {"k2": (88, 27.5), "r13": (76, 8), "r14": (76, 20), "r15": (76, 32), "r12": (76, 44),
        "r17": (56, 12), "r16": (56, 24), "r18": (58, 36), "r20": (48, 10), "r19": (46, 24), "r21": (46, 40)}
L4 = Lage(NEON4, ROT4, ball="n3")
k4 = []
a = L4.schieb({"r20": (48, 12), "r17": (52, 14), "r16": (52, 24), "r19": (40, 28), "r18": (56, 32), "r21": (40, 42),
               "r13": (64, 8), "r14": (72, 18), "r15": (72, 29), "r12": (74, 40)})
a += L4.schieb({"n6": (36, 18), "n8": (50, 38), "n11": (60, 6), "n9": (66, 16), "n10": (64, 28), "n2": (46, 49),
                "n7": (66, 48), "n5": (26, 18), "n4": (28, 36)}, delay=0.3)
a += L4.opts("n11", "n6", "n5", delay=1.8, zu=("n11",))
a.append(L4.pas("n6", after=True))
a += L4.schieb({"r19": (32, 24), "r16": (46, 20), "r21": (40, 42)}, delay=3.0)
k4.append(S("Eng auf der Ballseite", "Neue Situation. Der Ball ist links beim Außenverteidiger, und der Gegner schiebt mit allen rüber. Den Flügel hat sein Verteidiger. Einer kommt, einer geht: Der linke Mittelfeldspieler kommt zum Ball, der rechte geht weg auf die freie Seite. Der Außenverteidiger spielt den, der kommt.", *a))
b4 = L4.opts("n8", "n5", "n3")
b4.append(L4.pas("n8", after=True))
b4 += L4.schieb({"r18": (58, 34), "r21": (46, 44), "r12": (72, 44), "r16": (50, 26), "r15": (72, 32)}, delay=2.0)
b4 += L4.schieb({"n7": (64, 46), "n2": (52, 50), "n10": (66, 34), "n6": (40, 22), "n4": (30, 40)}, delay=2.1)
k4.append(S("Über die Mitte verlagern", "Der Mittelfeldspieler hat drei Möglichkeiten. Zurück zum Innenverteidiger, zurück nach außen, oder rüber zu seinem Partner. Der steht auf der freien Seite ganz offen. Also geht der Ball dahin. Jetzt muss der Gegner quer übers Feld schieben, und er kommt zu spät.", *b4))
c4 = L4.opts("n7", "n10", "n2", zu=("n10",))
c4.append(L4.pas("n7", after=True))
c4 += L4.schieb({"r12": (70, 45), "r18": (60, 40), "r15": (72, 34), "n8": (56, 40), "n9": (70, 22)}, delay=2.0)
k4.append(S("Raus auf den Flügel", "Vor ihm der Flügel, der Stürmer und der Außenverteidiger. Den Stürmer verdeckt der Achter. Der Flügel hat am meisten Platz, also spielt er ihn an. Und sofort kommt der Verteidiger raus auf ihn.", *c4))
d4 = [L4.dribbel("n7", (67, 40))]
d4 += L4.schieb({"r12": (73, 37), "r18": (62, 38)}, delay=0.3)
d4 += [mv("n2", [62, 51], delay=0.2), mv("n2", [70, 50], after=True)]
L4.p["n2"] = (70, 50)
d4 += L4.opts("n2", "n10", "n8", delay=2.2, zu=("n8",))
d4 += L4.steil("n2", (82, 49), delay=3.4)
d4 += L4.schieb({"r12": (85, 43), "n10": (76, 27), "n9": (78, 22), "n8": (66, 38)}, delay=3.2)
k4.append(S("Hinterlaufen", "Jetzt pass auf. Der Flügel zieht nach innen, und der Verteidiger geht mit. Einer kommt, einer geht: Gleichzeitig läuft der Außenverteidiger außen um ihn herum, die Linie runter. Innen ist zu, aber die Linie ist frei. Also kommt der Ball genau in seinen Lauf.", *d4))
e4 = L4.schieb({"r14": (80, 22), "r15": (80, 32), "r16": (60, 30), "r18": (66, 44)})
e4 += L4.schieb({"n10": (82, 30), "n9": (82, 20), "n8": (70, 36), "n7": (72, 42), "n6": (54, 24)}, delay=0.2)
e4 += L4.opts("n10", "n9", "n8", delay=1.6, zu=("n10", "n9"))
e4.append(L4.pas("n8", after=True))
k4.append(S("Zurück in den Rückraum", "Die Stürmer gehen in den Strafraum, die Verteidiger laufen mit. Vorn ist's eng. Aber hinten im Rückraum kommt der Mittelfeldspieler angelaufen. Der ist frei, also legt der Außenverteidiger zurück. So spielt man im Vier-vier-zwei über die Seite.", *e4))

u = {"title": "Aufbau im 4-4-2", "code": "TA-003", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im flachen 4-4-2 von hinten auf? Zuerst siehst du die Grundordnung und warum man staffeln muss, weil zwei flache Viererketten von sich aus kaum Dreiecke bilden. Dann presst ein Gegner im 4-3-3 mit drei Stürmern, und ein Außenverteidiger bleibt hinten. Danach siehst du, wie das Stürmerpaar zusammenarbeitet, und zum Schluss Seitenwechsel und Hinterlaufen.",
 "organisation": ["Grundordnung: Torwart, Viererkette, davor vier im Mittelfeld mit zwei Flügelspielern, vorn zwei Stürmer.",
  "Hinten: Die Innenverteidiger gehen breit, die Außenverteidiger hoch; gegen drei Stürmer bleibt ein Außenverteidiger hinten.",
  "Mittelfeld: Die beiden zentralen Mittelfeldspieler staffeln sich, einer tief, einer hoch, die Flügel halten die Breite.",
  "Bewegung: Einer kommt, einer geht: Kommt ein Stürmer oder Flügel zum Ball, läuft ein anderer in die Tiefe."],
 "organisation_show": ORG,
 "coaching_points": ["Staffeln, nicht auf einer Linie stehen", "Einer kommt, einer geht", "Drei Stürmer? Einer bleibt hinten", "Innen eng? Über die Mitte verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Vier-vier-zwei. Zwei Viererketten und zwei Stürmer, das kennt jeder. Aber wie kommt man damit von hinten raus? Wer steht wo, wer bewegt sich wann, und was macht das Stürmerpaar? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen drei Stürmer.", "Gegen drei Stürmer",
    "Jetzt presst ein Gegner im 4-3-3 mit drei Stürmern. Der Linksverteidiger bleibt hinten, so sind wir mit dem Torwart vier gegen drei, und einer ist immer frei. Danach kommt der Flügel dem Ball entgegen, und der Stürmer läuft in den Raum hinter dem Verteidiger.",
    Lage(NEON2, ROT2).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Das Stürmerpaar.", "Einer kommt, einer geht",
    "Die zwei Stürmer arbeiten zusammen. Einer lässt sich fallen und zieht seinen Verteidiger mit, der Pass geht durch zwei Reihen in seinen Fuß. Er lässt klatschen, und der andere Stürmer läuft in die Lücke, die dabei aufgeht.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 30.6, 38.6)] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Verlagern und Hinterlaufen.", "Verlagern und Hinterlaufen",
    "Der Gegner schiebt auf unsere Ballseite. Über die beiden zentralen Mittelfeldspieler verlagern wir auf die freie Seite. Dort zieht der Flügel nach innen, der Außenverteidiger hinterläuft und bekommt den Ball in den Lauf. Dann legt er zurück in den Rückraum.",
    Lage(NEON4, ROT4).spieler(), [B("b1", 42.6, 7.6)] + ERSATZ, k4)]}
fertig()
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
