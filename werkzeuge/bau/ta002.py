import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# TA-002: Taktik-Erklärung (kind "Taktik", Anleitung TAKTIK.md, Vorbild ta001.py). Aufbau im 4-2-3-1 von hinten.
# Vier Kapitel: 1 Grundordnung und Aufbau ohne Gegner (Doppelsechs gestaffelt, Zehner zwischen den Linien),
# 2 gegen ein 4-4-2-Pressing mit zwei Stürmern (Doppelsechs im Rücken der Stürmer, ballferner Sechser kommt zwischen die
# Stürmer, Spiel gegen die Verschieberichtung, Druckpass auf den eingerückten Flügel, dritter Mann, Außenverteidiger rückt vor),
# 3 Verlagern über die Doppelsechs (zwei Anspielstationen, tiefengestaffelt, Seitenwechsel auf den freien Außenverteidiger),
# 4 Zehner zwischen den Linien, Flügel zieht nach innen, Außenverteidiger überläuft, Doppelsechs sichert ab.
# Quellen (Recherche 24.11.2026): BDFL Internationaler Trainer-Kongress 2013, Ralf Peter, „Spielaufbau“ (4-2-3-1 gegen 4-4-2
# mit Mittelfeldkette): https://www.bdfl.de/images/ITK/2013/ITK_2013_Peter.pdf ; BDFL ITK 2009 (Positionstraining Viererkette und
# Doppel-6): https://www.bdfl.de/images/ITK/2009/ITK09_Peter.pdf ; Premier League „The 4-2-3-1: football tactics explained“:
# https://www.premierleague.com/en/news/4243785 ; Coaches' Voice zum 4-2-3-1:
# https://learning.coachesvoice.com/cv/the-4-2-3-1-football-tactics-pochettino-guardiola-flick-southgate/ ; 90min „Der abkippende
# Sechser“: https://www.90min.de/posts/6582083-der-abkippende-sechser-was-ist-das-eigentlich
# Nummern: 2 RV, 3 LV, 4 und 5 Innenverteidiger, 6 und 8 Doppelsechs (6 links, 8 rechts), 10 Zehner, 11 LA, 7 RA, 9 Stürmer.
# Team Rot (4-4-2) 12-21 wie in TA-001, beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Oben = linke Seite von Neon.

# ---------- Kapitel 1: Grundordnung und Aufbau ohne Gegner ----------
GRUND2 = {"k1": (10.5, 27.5), "n5": (24, 20), "n4": (24, 35), "n3": (30, 8), "n2": (30, 47), "n6": (36, 21.5), "n8": (36, 33.5),
          "n11": (54, 8), "n10": (52, 27.5), "n7": (54, 47), "n9": (64, 27.5)}
WEIT = {"n5": (19, 13.5), "n4": (19, 41.5), "n3": (40, 5), "n2": (40, 50), "n6": (30, 24), "n8": (38, 32),
        "n10": (57, 27.5), "n11": (66, 6), "n7": (66, 49), "n9": (73, 27.5)}
L = Lage(GRUND2)
k1 = []
k1.append(S("Wer steht wo im 4-2-3-1", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Vier-zwei-drei-eins. Hinten die Viererkette. Davor zwei Sechser nebeneinander, das ist die Doppelsechs. Davor drei Spieler: außen die beiden Flügel, in der Mitte der Zehner. Und ganz vorn ein Stürmer.",
            ps("b1", f(GRUND2["k1"]))))
L.ball = "k1"
k1.append(S("Breit und tief", "Hat der Torwart den Ball, machen wir das Feld groß. Die Innenverteidiger gehen raus bis an die Ecken vom Strafraum. Die Außenverteidiger schieben hoch an die Linie. Die Doppelsechs steht versetzt: einer etwas tiefer, einer etwas höher. Und der Zehner geht in den Raum hinter dem gegnerischen Mittelfeld.",
            *L.schieb(WEIT)))
s3 = L.opts("n5", "n6", "n4")
s3.append(L.pas("n4", after=True))
s3 += L.schieb({"n5": (22, 19), "n6": (31, 28), "n8": (38, 37), "n2": (44, 50), "n3": (40, 10), "n10": (57, 31), "n11": (64, 11),
                "n9": (73, 31), "n7": (66, 48)}, delay=2.0)
k1.append(S("Der Torwart wählt", "Schau auf den Torwart. Er kann zu beiden Innenverteidigern spielen oder zum tieferen Sechser. Er nimmt den rechten Innenverteidiger. Und mit dem Ball rutscht die ganze Mannschaft ein Stück rüber, auch die auf der anderen Seite.", *s3))
s4 = L.opts("n2", "n8", "n6")
s4.append(L.pas("n8", after=True))
s4 += L.schieb({"n7": (61, 40), "n2": (52, 50), "n6": (33, 31), "n10": (58, 29), "n9": (74, 29), "n4": (22, 44), "n5": (23, 23)}, delay=2.0)
k1.append(S("Einer kommt, einer geht", "Der Innenverteidiger hat drei Möglichkeiten. Außen, schräg den höheren Sechser oder quer den anderen. Er spielt den Sechser, der offen steht. Und jetzt pass auf: Einer kommt, einer geht. Der rechte Flügel kommt nach innen in die Lücke. Dafür geht der Außenverteidiger die Linie hoch. Der zweite Sechser bleibt hinten und sichert ab.", *s4))
von = f(L.p["n4"])
s5 = [bl("n8", list(L.p["n10"]), von=von, dauer=1.3), drehen("n8", list(L.p["n10"]), gegen=True, delay=0.4)]
s5 += L.opts("n10", "n7", "n2", delay=1.5)
s5.append(L.pas("n10", after=True))
s5 += L.schieb({"n9": (78, 33), "n11": (70, 16), "n7": (66, 40), "n2": (58, 50), "n8": (42, 36), "n6": (36, 30)}, delay=3.0)
k1.append(S("Der Zehner zwischen den Linien", "Erst nach der Annahme dreht der Sechser auf. Jetzt hat er den Zehner, den Flügel oder den Außenverteidiger. Der Zehner steht in der Mitte, genau zwischen den Linien. Also kriegt er den Ball. Der Stürmer geht dafür weg in die Tiefe und macht ihm Platz.", *s5))
s6 = [drehen("n10", list(L.p["n11"]), gegen=True)]
s6 += L.opts("n9", "n11", "n7", delay=0.8)
s6 += L.steil("n11", (82, 14), delay=2.2)
s6 += L.schieb({"n9": (82, 30), "n7": (76, 40), "n10": (66, 28), "n2": (64, 49), "n8": (48, 34), "n6": (42, 27)}, delay=2.4)
k1.append(S("Steil auf den Flügel", "Der Zehner dreht auf und hat wieder drei: den Stürmer, den linken Flügel und den rechten. Der linke Flügel startet in die Tiefe, also kommt der Ball genau in seinen Lauf. Die anderen gehen mit in den Strafraum. Und die Doppelsechs rückt nach, bleibt aber hinter dem Ball.", *s6))

# ---------- Kapitel 2: gegen ein 4-4-2-Pressing mit zwei Stürmern ----------
NEON2 = {"k1": (10.5, 27.5), "n5": (19, 13.5), "n4": (19, 41.5), "n3": (38, 5), "n2": (38, 50), "n6": (30, 22), "n8": (36, 34),
         "n10": (62, 27.5), "n11": (66, 6), "n7": (66, 49), "n9": (72, 27.5)}
ROT2 = {"k2": (88, 27.5), "r13": (80, 9), "r14": (80, 21), "r15": (80, 34), "r12": (80, 46),
        "r16": (56, 8), "r17": (52, 20), "r18": (52, 35), "r21": (56, 47), "r19": (44, 17), "r20": (44, 38)}
L2 = Lage(NEON2, ROT2, ball="k1")
k2 = []
a = L2.schieb({"r19": (27, 16), "r20": (27, 37), "r16": (47, 8), "r17": (45, 20), "r18": (45, 34), "r21": (47, 46),
               "r13": (70, 9), "r14": (68, 21), "r15": (68, 33), "r12": (70, 45)})
a += L2.schieb({"n5": (16, 10), "n4": (16, 45), "n3": (44, 5), "n2": (44, 50), "n6": (35, 21), "n8": (37, 32),
                "n10": (57, 27.5), "n9": (66, 27.5)}, delay=0.3)
k2.append(S("Der Gegner presst", "Jetzt wird's ernst. Der Gegner presst im Vier-vier-zwei. Zwei Stürmer laufen an, dahinter steht eine Viererreihe im Mittelfeld. Unsere Innenverteidiger gehen ganz breit. Und die Doppelsechs bleibt im Rücken der Stürmer. Denn kriegt da ein Sechser den Ball, sind beide Stürmer schon überspielt.", *a))
b2 = L2.opts("n5", "n6", "n4")
b2.append(L2.pas("n5", after=True))
b2 += L2.schieb({"r19": (23, 15), "r20": (24, 30), "r16": (44, 9), "r17": (43, 17), "r18": (44, 29), "r21": (48, 40),
                 "r13": (70, 7), "r14": (68, 18), "r15": (68, 29), "r12": (70, 40)}, delay=2.0)
b2 += L2.schieb({"n6": (34, 17), "n8": (37, 29), "n10": (57, 24), "n9": (66, 24), "n7": (64, 46), "n2": (44, 48), "n4": (17, 42)}, delay=2.2)
k2.append(S("Der Gegner lenkt nach außen", "Der Torwart hat drei Möglichkeiten und spielt nach links. Sofort läuft der Stürmer an, und zwar von innen. So macht er den Weg in die Mitte zu und will uns nach außen schicken. Die ganze Mannschaft vom Gegner schiebt mit.", *b2))
c2 = L2.opts("n3", "n6", "k1", zu=("n3", "n6"))
c2.append(L2.pas("k1", after=True))
c2 += L2.schieb({"n8": (32, 24), "n6": (40, 21)}, delay=1.8)
c2 += L2.schieb({"r19": (20, 20), "r17": (46, 19)}, delay=2.0)
k2.append(S("Die Doppelsechs tauscht", "Innen steht der Stürmer im Weg, außen lauert schon der Gegner auf unseren Außenverteidiger. Frei ist nur der Weg zurück zum Torwart. Und jetzt pass auf: Der rechte Sechser kommt zwischen die beiden Stürmer. Der linke geht im selben Moment nach vorn und nimmt seinen Gegenspieler mit.", *c2))
d2 = L2.opts("n8", "n4")
d2.append(L2.pas("n8", after=True))
d2 += L2.schieb({"r18": (42, 28), "r20": (25, 31), "n4": (30, 44)}, delay=1.6)
d2.append(bl("n8", list(L2.p["n4"]), von=f(L2.p["k1"]), dauer=1.2, delay=2.6))
d2.append(L2.pas("n4", after=True))
d2 += L2.schieb({"r20": (28, 37), "r21": (46, 44), "r18": (45, 31), "r17": (44, 21), "r16": (46, 10), "r19": (24, 24),
                 "r12": (68, 44), "r15": (66, 33), "r14": (66, 22), "r13": (68, 11),
                 "n2": (44, 50), "n7": (55, 37), "n9": (64, 28), "n10": (58, 27), "n6": (40, 23), "n3": (44, 7), "n5": (20, 16)}, delay=1.8)
k2.append(S("Gegen die Verschieberichtung", "Der Torwart spielt den Sechser zwischen den Stürmern an. Damit sind beide überspielt. Der Gegner hat alles auf unsere linke Seite geschoben. Also spielt der Sechser genau dagegen, rüber zum rechten Innenverteidiger. Der läuft schon in den Ball. Und der Gegner muss wieder quer rüber.", *d2))
e2 = [L2.dribbel("n4", (36, 45))]
e2 += L2.schieb({"r21": (46, 47), "r20": (30, 39)}, delay=0.8)
e2 += L2.opts("n2", "n7", "n9", delay=1.8, zu=("n2",))
e2.append(L2.pas("n7", after=True))
e2 += L2.schieb({"n8": (40, 40), "r18": (50, 32), "r12": (64, 41)}, delay=3.2)
k2.append(S("Pass in die Lücke", "Der Innenverteidiger dribbelt an. Jetzt muss sich der gegnerische Flügel entscheiden. Er geht raus zu unserem Außenverteidiger und macht die Linie zu. Dafür ist innen eine Lücke, und genau da steht unser Flügel, nach innen gerückt. Also kommt der Ball scharf und flach in seinen Fuß.", *e2))
g2 = [L2.pas("n8")]
g2 += L2.schieb({"n2": (50, 50)}, delay=0.2)
g2 += L2.schieb({"r18": (48, 35), "r21": (43, 50)}, delay=1.2)
g2 += L2.opts("n2", "n4", delay=1.6)
g2 += L2.steil("n2", (64, 50), delay=2.4)
g2 += L2.schieb({"n7": (66, 38), "n9": (70, 30), "r12": (68, 46), "n4": (30, 42), "n3": (46, 12), "n11": (68, 12), "n6": (42, 28)}, delay=2.4)
k2.append(S("Klatschen und raus", "Der Flügel lässt direkt klatschen, auf den Sechser, der sich offen hingestellt hat. Das ist der dritte Mann. Weil der Flügel jetzt innen ist, geht der Außenverteidiger die Linie hoch. Und genau da hin spielt der Sechser. Das Pressing ist überspielt.", *g2))

# ---------- Kapitel 3: verlagern über die Doppelsechs ----------
NEON3 = {"k1": (10.5, 27.5), "n5": (20, 14), "n4": (20, 40), "n3": (40, 5), "n2": (40, 50), "n6": (32, 20), "n8": (32, 33),
         "n10": (58, 27.5), "n11": (66, 6), "n7": (66, 49), "n9": (72, 27.5)}
ROT3 = {"k2": (88, 27.5), "r13": (80, 9), "r14": (80, 21), "r15": (80, 34), "r12": (80, 46),
        "r16": (52, 8), "r17": (50, 20), "r18": (50, 36), "r21": (52, 48), "r19": (40, 17), "r20": (40, 38)}
L3 = Lage(NEON3, ROT3, ball="n3")
k3 = []
a = L3.schieb({"r16": (48, 7), "r19": (30, 9), "r17": (46, 16), "r18": (46, 27), "r21": (50, 37), "r20": (38, 28),
               "r13": (72, 6), "r14": (70, 16), "r15": (70, 27), "r12": (72, 38)})
a += L3.schieb({"n6": (37, 15), "n8": (32, 30), "n5": (22, 13), "n4": (22, 36), "n10": (58, 22), "n11": (62, 6),
                "n9": (66, 22), "n7": (64, 46), "n2": (44, 48)}, delay=0.3)
a += L3.opts("n11", "n5", "n6", delay=1.8, zu=("n11", "n5"))
k3.append(S("Eingeklemmt an der Linie", "Neue Situation. Unser linker Außenverteidiger hat den Ball, und der Gegner schiebt mit allen rüber. Die Linie runter ist zu, und den Rückpass zum Innenverteidiger stellt der Stürmer zu. Frei ist nur einer: der Sechser, der zur Hilfe kommt.", *a))
b3 = [L3.pas("n6")]
b3 += L3.schieb({"r17": (42, 17), "r19": (31, 14)}, delay=0.9)
b3 += L3.schieb({"n8": (30, 26), "n10": (60, 32), "n7": (68, 48)}, delay=0.9)
b3 += L3.opts("n8", "n5", delay=1.8, zu=("n5",))
b3.append(L3.pas("n8", after=True))
k3.append(S("Zwei Sechser, zwei Stationen", "Er kriegt den Ball, aber mit dem Rücken zum Spiel, und der Gegner ist sofort da. Aufdrehen geht nicht. Brauchst du auch nicht, denn es gibt ja zwei Sechser. Der zweite Sechser kommt schräg hinter ihn, und der Zehner geht weg aus der Mitte, rüber auf die freie Seite. Also kurz zurück auf den zweiten Sechser.", *b3))
c3 = L3.schieb({"r20": (34, 24), "r18": (44, 24)}, delay=0.3)
c3.append(bl("n8", list(L3.p["n2"]), von=f(L3.p["n6"]), dauer=1.2, delay=0.3))
c3 += L3.opts("n4", "n2", delay=1.6)
c3.append(L3.pas("n2", after=True))
c3 += L3.schieb({"r21": (52, 44), "r18": (48, 32), "r12": (70, 44), "r15": (70, 33), "r14": (70, 22), "r13": (72, 12),
                 "r16": (50, 12), "r17": (46, 21), "r20": (36, 32), "r19": (30, 20)}, delay=2.6)
c3 += L3.schieb({"n4": (24, 40), "n6": (36, 22), "n8": (34, 30), "n11": (64, 12), "n9": (68, 27), "n3": (40, 14), "n5": (24, 18)}, delay=2.6)
k3.append(S("Seitenwechsel", "Der zweite Sechser steht offen und sieht das ganze Feld. Er hat den rechten Innenverteidiger und, weiter weg, den Außenverteidiger. Der ist ganz frei, also geht der Ball direkt rüber. Jetzt muss der Gegner quer übers ganze Feld schieben. Und er kommt zu spät.", *c3))
d3 = [L3.dribbel("n2", (56, 48))]
d3 += L3.schieb({"r21": (51, 45), "r12": (70, 44)}, delay=0.8)
d3 += L3.opts("n7", "n10", "n9", delay=1.6, zu=("n7",))
d3.append(L3.pas("n10", after=True))
d3 += L3.schieb({"n7": (70, 48), "n9": (68, 27), "n8": (40, 32), "n6": (40, 24), "r15": (71, 34), "r18": (54, 32)}, delay=2.6)
k3.append(S("Mit Tempo rein", "Der Außenverteidiger hat Platz, also nimmt er den Ball mit und dribbelt mit Tempo nach vorn. Der gegnerische Flügel muss raus, und der Verteidiger dahinter klebt an unserem Flügel. Innen aber ist der Zehner frei. Er kriegt den Ball und schaut sofort nach vorn.", *d3))
e3 = L3.opts("n7", "n9", zu=("n7",))
e3 += L3.steil("n9", (82, 24), delay=0.9)
e3 += L3.schieb({"n7": (78, 44), "n11": (74, 14), "n2": (64, 48), "n10": (68, 34)}, delay=0.9)
e3 += L3.schieb({"r14": (78, 22), "r15": (77, 31), "r12": (76, 44)}, delay=1.5)
k3.append(S("Auf der freien Seite", "Unser Flügel ist zugestellt, der Verteidiger klebt an ihm. Aber der Stürmer startet, genau mit dem Pass, also kein Abseits. Der Zehner steckt durch, in die Lücke zwischen zwei Verteidigern. Erst Druck auf einer Seite, dann über die Doppelsechs verlagern. So kommen wir dahin, wo der Gegner nicht ist.", *e3))

# ---------- Kapitel 4: Zehner zwischen den Linien, Flügel rein, Außenverteidiger überläuft ----------
NEON4 = {"k1": (10.5, 27.5), "n5": (24, 15), "n4": (24, 40), "n6": (42, 19), "n8": (44, 32), "n3": (46, 5), "n2": (48, 50),
         "n10": (64, 30), "n11": (68, 6), "n7": (68, 49), "n9": (70, 24)}
ROT4 = {"k2": (88, 27.5), "r13": (76, 9), "r14": (76, 21), "r15": (76, 33), "r12": (76, 45),
        "r16": (56, 9), "r17": (56, 21), "r18": (56, 33), "r21": (56, 45), "r19": (34, 22), "r20": (34, 36)}
L4 = Lage(NEON4, ROT4, ball="n8")
k4 = []
a = L4.schieb({"n10": (64, 25), "n9": (72, 33)})
a += L4.schieb({"r15": (76, 35)}, delay=0.6)
a += L4.opts("n10", "n2", "n6", delay=1.4)
a.append(L4.pas("n10", after=True))
a += L4.schieb({"r17": (60, 21), "r18": (59, 31), "r14": (72, 22), "r19": (40, 22), "r20": (40, 34)}, delay=2.6)
a += L4.schieb({"n5": (30, 15), "n4": (30, 38), "n3": (50, 8), "n6": (44, 21)}, delay=2.8)
k4.append(S("Zwischen den Linien", "Zum Schluss das Muster, für das man ein Vier-zwei-drei-eins spielt. Unser Sechser hat den Ball, die Stürmer sind schon überspielt. Einer kommt, einer geht: Der Stürmer zieht weg und nimmt seinen Verteidiger mit. Dafür kommt der Zehner in die Lücke. Der Pass geht flach durch die Mittelfeldreihe, direkt zu ihm.", *a))
b4 = [bl("n10", list(L4.p["n7"]), von=f(L4.p["n8"]), dauer=1.2), drehen("n10", list(L4.p["n7"]), delay=0.4)]
b4 += L4.schieb({"n7": (64, 40), "n2": (60, 50), "r12": (72, 42)}, delay=0.6)
b4 += L4.opts("n7", "n9", "n11", delay=2.0)
b4.append(L4.pas("n7", after=True))
b4 += L4.schieb({"r12": (69, 36), "r21": (58, 42), "r16": (58, 14), "r13": (74, 12), "n8": (50, 34), "n6": (46, 22),
                 "n3": (52, 12), "n4": (34, 40), "n11": (70, 10)}, delay=3.0)
k4.append(S("Flügel rein", "Der Zehner dreht auf. Und schau, was außen passiert. Unser rechter Flügel zieht nach innen. Der Verteidiger geht mit ihm mit. Der Zehner spielt den Flügel an, schräg nach rechts.", *b4))
c4 = L4.opts("n2", "n10")
c4 += L4.steil("n2", (82, 50), delay=0.9)
c4 += L4.schieb({"n9": (80, 30), "n10": (72, 28), "n11": (74, 12), "n7": (70, 38)}, delay=1.0)
c4 += L4.schieb({"r12": (78, 46), "r15": (80, 34), "r14": (80, 24), "r13": (80, 14)}, delay=1.6)
c4 += L4.schieb({"n8": (52, 36), "n6": (48, 26), "n5": (34, 18), "n4": (38, 38), "k1": (16, 27.5), "r19": (46, 22), "r20": (46, 33)}, delay=1.6)
k4.append(S("Außenverteidiger überläuft", "Der Flügel ist nach innen gekommen, also geht der Außenverteidiger außen vorbei. Er startet mit dem Pass, also kein Abseits. Hinten bleibt trotzdem keiner allein. Die Doppelsechs sichert ab, deshalb darf der Außenverteidiger mit nach vorn.", *c4))
d4 = [L4.dribbel("n2", (84, 46))]
d4 += L4.schieb({"r12": (85, 40), "r15": (83, 33), "r14": (83, 24), "n10": (72, 34), "n9": (82, 30), "n7": (74, 42)}, delay=0.4)
d4 += L4.opts("n9", "n10", "n7", delay=1.6, zu=("n9",))
d4.append(L4.pas("n10", after=True))
d4 += L4.schieb({"r18": (70, 34), "r21": (72, 42)}, delay=2.4)
k4.append(S("Zurück in den Rückraum", "Der Außenverteidiger geht bis fast an die Grundlinie. Vor dem Tor steht der Stürmer, aber da ist es eng. Der Zehner ist mitgelaufen und steht im Rückraum frei. Also kriegt er den Ball flach zurückgelegt. Zehner zwischen den Linien, Flügel rein, Außenverteidiger außen vorbei.", *d4))

u = {"title": "Aufbau im 4-2-3-1", "code": "TA-002", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 4-2-3-1 von hinten auf? Zuerst siehst du die Grundordnung mit der Doppelsechs, dem Zehner zwischen den Linien und den hohen Außenverteidigern, und wie alle mit jedem Pass verschieben. Dann presst ein Gegner im 4-4-2, und die Doppelsechs spielt sich im Rücken der Stürmer frei. Zum Schluss zwei Muster: Verlagern über die Doppelsechs und der Zehner zwischen den Linien, wenn der Flügel nach innen zieht und der Außenverteidiger überläuft.",
 "organisation": ["Grundordnung: Torwart, Viererkette, Doppelsechs, davor zwei Flügelspieler und der Zehner, vorn ein Stürmer.",
  "Hinten: Beim Aufbau gehen die Innenverteidiger breit bis an die Ecken vom Strafraum, die Außenverteidiger schieben hoch an die Linie.",
  "Mittelfeld: Die Doppelsechs steht versetzt im Rücken der gegnerischen Stürmer, der Zehner sucht die Lücke zwischen Mittelfeld und Abwehr.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball. Einer kommt, einer geht: Zieht der Flügel nach innen, geht der Außenverteidiger die Linie hoch."],
 "organisation_show": ORG,
 "coaching_points": ["Sechser versetzt, nie auf einer Linie", "Zehner, such die Lücke zwischen den Linien", "Einer kommt, einer geht", "Eine Seite zu? Über die Doppelsechs verlagern"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "frei", "hidden": False, "wartet_auf_ton": False,  # eingesprochen (24.11.2026), sichtbar
 "say_intro": "Aufbau im Vier-zwei-drei-eins. Heute schauen wir uns das System an. Was macht die Doppelsechs? Wo steht der Zehner? Und wie kommen wir gegen ein Pressing nach vorn? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND2).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Gegen zwei Stürmer",
    "Der Gegner presst im 4-4-2 und lenkt uns mit den Stürmern nach außen. Die Doppelsechs bleibt im Rücken der Stürmer, der ballferne Sechser kommt zwischen die beiden. Wir spielen gegen die Verschieberichtung auf den anderen Innenverteidiger und dann flach auf den eingerückten Flügel. Der lässt klatschen, und der Außenverteidiger geht die Linie hoch.",
    Lage(NEON2, ROT2).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Verlagern über die Doppelsechs.", "Über die Doppelsechs",
    "Der Gegner klemmt unseren Außenverteidiger an der Linie ein. Ein Sechser kommt zur Hilfe, der zweite steht versetzt dahinter und ist frei. Über ihn geht der Ball auf die andere Seite, wo der Außenverteidiger Platz hat. Der Gegner kommt beim Verschieben zu spät.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 40.6, 5.6)] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Der Zehner und der Außenverteidiger.", "Zehner und Überlaufen",
    "Der Zehner holt sich den Ball zwischen den Linien, weil der Stürmer seinen Verteidiger wegzieht. Der Flügel zieht nach innen, der Außenverteidiger überläuft außen. Die Doppelsechs sichert dahinter ab. Am Ende legt der Außenverteidiger in den Rückraum zurück.",
    Lage(NEON4, ROT4).spieler(), [B("b1", 44.6, 32.6)] + ERSATZ, k4)]}
fertig()
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
