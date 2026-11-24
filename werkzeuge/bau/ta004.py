import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# TA-004: Taktik-Erklärung (kind "Taktik"). Aufbau im 3-5-2. Vorbild TA-001 (bau/ta001.py), Bauhilfe bau/taktik.py.
# Vier Kapitel: 1 Grundordnung und Aufbau ohne Gegner (Feld groß machen, Halbverteidiger dribbelt an, Schiene gibt die Breite,
# Stürmer kommt, Achter geht), 2 gegen ein 4-4-2-Pressing mit zwei Stürmern (drei gegen zwei hinten, freier Halbverteidiger,
# andribbeln und locken, Schiene frei, Lauf in den Raum hinter dem Außenverteidiger), 3 zwei Stürmer im Wechselspiel (einer kommt,
# einer geht, klatschen lassen, dritter Mann), 4 Seitenverlagerung auf den freien Schienenspieler, Schiene läuft an, Stürmer
# über Kreuz an kurzen und langen Pfosten, Achter im Rückraum, flache Flanke; dann Absichern hinten (Raum hinter den Schienen).
# Recherche (24.11.2026): premierleague.com/en/news/4244123 (3-5-2 erklärt: Dreierkette gibt Überzahl im Aufbau, Torwart macht
# daraus vier gegen drei, Schienenspieler geben die Breite, schnelle Verlagerung auf die hohen Schienen, Doppelspitze mit
# Ablagen), learning.coachesvoice.com/cv/back-three-explained-why-conte-moyes-guardiola/ (Halbverteidiger dribbeln ins Mittelfeld,
# vor allem gegen zwei Stürmer; lange Bälle auf die andere Seite; Achter laufen durch; Schwäche: Breite und Konter über außen),
# renderfoot.com/de/formations/3-5-2 (Schienenspieler einzige natürliche Breite, gegen Ball 5-3-2),
# soccertutor.com/blogs/inside-football-coaching/3-5-2-attacking-patterns (Stürmer: einer kommt kurz, einer geht in die Tiefe).
# Nummern Team Neon: TW, 3 linker Halbverteidiger, 4 zentraler Innenverteidiger, 5 rechter Halbverteidiger, 11 linker und
# 2 rechter Schienenspieler, 6 Sechser, 10 linker und 8 rechter Achter, 9 und 7 Stürmer. Von Neon aus oben = links.
# Team Rot 12-21 (Kapitel 2 bis 4 im 4-4-2), beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Ein Trainer.

GRUND = {"k1": (10.5, 27.5), "n3": (24, 14), "n4": (22, 27.5), "n5": (24, 41), "n6": (34, 27.5), "n10": (44, 18),
         "n8": (44, 37), "n11": (42, 6), "n2": (42, 49), "n9": (60, 21.5), "n7": (60, 33.5)}
GROSS = {"k1": (10.5, 27.5), "n3": (22, 8), "n4": (18, 27.5), "n5": (22, 47), "n6": (30, 27.5), "n10": (46, 17),
         "n8": (46, 38), "n11": (62, 5), "n2": (62, 50), "n9": (74, 22), "n7": (74, 33)}

# ---------- Kapitel 1: Grundordnung, Feld groß machen, Aufbau ohne Gegner ----------
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 3-5-2", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Drei-fünf-zwei. Hinten eine Dreierkette: in der Mitte der Innenverteidiger, links und rechts die zwei Halbverteidiger. Davor der Sechser mit seinen zwei Achtern. Ganz außen die beiden Schienenspieler. Und vorn zwei Stürmer.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Das Feld groß machen", "Sobald der Torwart den Ball hat, machen wir das Feld groß. Die Halbverteidiger gehen weit raus, bis neben den Strafraum. Die Schienenspieler schieben ganz hoch an die Linie. Die zwei sind unsere Breite, sonst ist außen keiner. Und die Stürmer drücken die Abwehr nach hinten.",
            *L.schieb(GROSS)))
s = L.opts("n3", "n4", "n5")
s.append(L.pas("n5", after=True))
s += L.schieb({"n4": (20, 32), "n3": (25, 13), "n6": (31, 34), "n8": (47, 42), "n10": (47, 25), "n11": (62, 10),
               "n9": (74, 27), "n7": (75, 38)}, delay=2.0)
k1.append(S("Drei Verteidiger, drei Wege", "Jetzt schau auf den Torwart. Er hat seine drei Verteidiger. Er spielt den rechten Halbverteidiger an. Und mit dem Ball schiebt die ganze Mannschaft rüber. Auch die auf der anderen Seite.", *s))
s = [L.dribbel("n5", (34, 46))]
s += L.schieb({"n4": (25, 33), "n3": (29, 14), "n6": (37, 33), "n10": (50, 25)}, delay=0.4)
s += L.opts("n2", "n8", "n6", delay=1.8)
k1.append(S("Der Halbverteidiger dribbelt an", "Und jetzt kommt was, das typisch ist für die Dreierkette. Vor dem Halbverteidiger ist Platz. Also dribbelt er an, rein ins Mittelfeld. Hinten bleiben ja noch zwei. Vor ihm drei Möglichkeiten: die Schiene außen, der Achter oder der Sechser.", *s))
s = [L.pas("n2")]
s += L.schieb({"n8": (54, 41), "n7": (76, 40), "n9": (76, 28), "n10": (54, 28), "n6": (40, 35), "n4": (28, 34),
               "n3": (32, 16), "n11": (66, 12), "n5": (40, 47)}, delay=0.5)
k1.append(S("Die Schiene gibt die Breite", "Außen ist am meisten Platz, also kriegt ihn die Schiene. Die steht ganz breit an der Linie. Und der Halbverteidiger? Der rückt hinter ihr nach und sichert ab.", *s))
s = L.schieb({"n7": (68, 42), "n8": (60, 44)})
s += L.opts("n7", "n8", "n10", delay=1.0)
s += L.steil("n8", (80, 45), delay=2.4)
s += L.schieb({"n9": (82, 30), "n10": (66, 30), "n11": (76, 14), "n7": (72, 38), "n6": (50, 36), "n5": (52, 48)}, delay=2.4)
k1.append(S("Einer kommt, einer geht", "Und jetzt pass auf: Einer kommt, einer geht. Der Stürmer kommt der Schiene entgegen. Dafür geht der Achter in die Tiefe, genau in den Raum, den der Stürmer frei macht. Die Schiene spielt ihn in den Lauf. Und vorn gehen jetzt zwei in den Strafraum.", *s))

# ---------- Kapitel 2: gegen zwei Stürmer (Gegner im 4-4-2) ----------
NEON2 = {"k1": (10.5, 27.5), "n3": (21, 10), "n4": (18, 27.5), "n5": (23, 45), "n6": (28, 27.5), "n10": (43, 14),
         "n8": (43, 41), "n11": (58, 5), "n2": (58, 50), "n9": (67, 21.5), "n7": (67, 34)}
ROT2 = {"k2": (88, 27.5), "r13": (76, 9), "r14": (74, 21), "r15": (74, 34), "r12": (76, 46),
        "r16": (52, 8), "r17": (50, 21), "r18": (50, 34), "r21": (52, 47), "r19": (36, 18), "r20": (36, 37)}
L2 = Lage(NEON2, ROT2, ball="k1")
k2 = []
a = L2.schieb({"r19": (26, 19), "r20": (27, 35), "r16": (48, 9), "r17": (40, 21), "r18": (40, 34), "r21": (48, 45),
               "r13": (68, 10), "r14": (64, 22), "r15": (64, 34), "r12": (68, 45)})
a += L2.schieb({"n3": (21, 7), "n5": (22, 48), "n6": (31, 27.5), "n9": (63, 18), "n7": (63, 37), "n10": (46, 15), "n8": (46, 41)}, delay=0.3)
k2.append(S("Zwei Stürmer laufen an", "Jetzt wird's ernst. Der Gegner presst im Vier-vier-zwei. Zwei Stürmer laufen an, und alle anderen rücken mit hoch. Aber hinten haben wir drei Verteidiger gegen zwei Stürmer. Einer von uns ist also immer frei. Die Halbverteidiger gehen dafür noch ein Stück breiter.", *a))
b = L2.opts("n3", "n4", "n5")
b.append(L2.pas("n4", after=True))
b += L2.schieb({"r19": (24, 22), "r20": (26, 32)}, delay=2.0)
b += L2.schieb({"n6": (33, 24), "n10": (47, 14)}, delay=2.2)
k2.append(S("Wer ist frei?", "Der Torwart spielt den Innenverteidiger in der Mitte an. Sofort läuft ihn ein Stürmer an, und zwar so, dass der linke Halbverteidiger hinter ihm im Schatten steht. Der zweite Stürmer stellt den Sechser zu. Also schau nach rechts.", *b))
c = L2.opts("n5", "n3", "n6", zu=("n3", "n6"))
c.append(L2.pas("n5", after=True))
c += L2.schieb({"r20": (30, 40), "r19": (27, 30), "r21": (48, 48), "r18": (44, 38), "r17": (44, 26), "r16": (50, 14),
                "r12": (70, 47), "r15": (66, 34), "r14": (64, 25), "r13": (68, 14)}, delay=2.0)
c += L2.schieb({"n4": (19, 33), "n6": (32, 30), "n8": (47, 43), "n7": (62, 38), "n9": (63, 26), "n10": (48, 20), "n11": (58, 9), "n3": (23, 13)}, delay=2.2)
k2.append(S("Der freie Halbverteidiger", "Links ist zu, der Sechser auch. Aber der rechte Halbverteidiger ist frei. Da ist die Überzahl, drei gegen zwei. Der Ball geht rüber, und alle schieben mit, wir und der Gegner.", *c))
d = [L2.dribbel("n5", (31, 47))]
d += L2.schieb({"r21": (38, 42)}, delay=0.8)
d += L2.opts("n2", "n8", "n6", delay=2.0, zu=("n8", "n6"))
k2.append(S("Andribbeln und locken", "Der Halbverteidiger hat Platz. Also dribbelt er an, so lange, bis einer kommt. Und der Gegner kommt: Der Mittelfeldspieler von außen läuft ihn an, von innen, damit der Weg zum Achter zu ist. Den Sechser deckt der Stürmer ab. Aber genau den Mittelfeldspieler wollten wir locken. Denn jetzt ist hinter ihm die Schiene frei.", *d))
e = [L2.pas("n2")]
e += L2.schieb({"r12": (63, 45), "r21": (51, 44), "r15": (70, 36)}, delay=0.6)
e += L2.schieb({"n8": (50, 41), "n5": (36, 47), "n4": (24, 35), "n6": (38, 33)}, delay=0.8)
k2.append(S("Die Schiene ist frei", "Der Ball geht raus auf die Schiene. Der Mittelfeldspieler kommt zu spät zurück. Also muss der Außenverteidiger raus zur Schiene. Und hinter ihm ist jetzt Platz.", *e))
g = L2.schieb({"n8": (56, 40)})
g += L2.opts("n8", "n5", delay=1.0)
g += L2.steil("n7", (78, 49), delay=2.2)
g += L2.schieb({"n9": (74, 32), "n10": (58, 26), "n11": (66, 10)}, delay=2.2)
g += L2.schieb({"r15": (76, 42), "r14": (72, 30), "r12": (70, 48)}, delay=2.6)
k2.append(S("Einer kommt, einer geht", "Einer kommt, einer geht. Der Achter kommt zur Schiene, und der Stürmer geht in die Tiefe, genau in den Raum hinter dem Außenverteidiger. Die Schiene könnte kurz spielen, aber vorn ist der Lauf. Der Stürmer startet mit dem Pass, also kein Abseits. Und das Pressing ist überspielt.", *g))

# ---------- Kapitel 3: zwei Stürmer im Wechselspiel ----------
# Gegner im 4-4-2-Mittelfeldpressing, wir haben den Ball beim linken Halbverteidiger.
NEON3 = {"k1": (10.5, 27.5), "n3": (30, 12), "n4": (24, 27.5), "n5": (30, 43), "n6": (38, 26), "n10": (50, 14),
         "n8": (52, 38), "n11": (66, 5), "n2": (66, 50), "n9": (68, 22), "n7": (68, 34)}
ROT3 = {"k2": (88, 27.5), "r13": (74, 10), "r14": (74, 22), "r15": (74, 34), "r12": (74, 46),
        "r16": (58, 8), "r17": (58, 20), "r18": (58, 32), "r21": (58, 45), "r19": (44, 18), "r20": (44, 34)}
L3 = Lage(NEON3, ROT3, ball="n3")
k3 = []
a = L3.schieb({"r19": (36, 20), "r20": (42, 30), "r17": (57, 17), "r13": (72, 9)})
a += L3.schieb({"n10": (50, 16), "n11": (66, 6)}, delay=0.3)
a += L3.opts("n11", "n10", "n6", delay=1.4, zu=("n11", "n6"))
k3.append(S("Der Gegner steht kompakt", "Neue Situation. Der Gegner wartet jetzt in der eigenen Hälfte, kompakt in zwei Reihen. Der linke Halbverteidiger hat den Ball. Die Schiene ist zugestellt, den Sechser deckt ein Stürmer ab. Frei ist der Achter.", *a))
b = [L3.pas("n10")]
b += L3.schieb({"r17": (54, 11), "r16": (58, 6)}, delay=0.6)
b += L3.schieb({"n9": (62, 26), "n7": (70, 30), "n3": (32, 12), "n6": (40, 24), "n4": (28, 24), "n5": (34, 38), "n8": (55, 33), "n2": (66, 46)}, delay=0.6)
b += L3.schieb({"r20": (44, 27), "r21": (58, 40), "r12": (74, 42)}, delay=0.8)
b += L3.schieb({"r14": (69, 24)}, delay=1.4)
k3.append(S("Der Stürmer kommt entgegen", "Der Achter kriegt ihn, und ein Mittelfeldspieler läuft ihn an. Jetzt schau auf die zwei Stürmer. Der eine kommt entgegen, raus aus der Abwehrreihe, in die Lücke hinter dem Mittelfeld. Und sein Innenverteidiger geht ein Stück mit. Genau das wollen wir.", *b))
c = L3.opts("n9", "n6", "n11", zu=("n11",))
c.append(L3.pas("n9", after=True))
c += L3.schieb({"n7": (73, 22), "n10": (48, 18)}, delay=2.2)
c += L3.schieb({"r14": (65, 26), "r15": (72, 32)}, delay=2.4)
k3.append(S("Einer kommt, einer geht", "Einer kommt, einer geht. Der Achter spielt den Stürmer an, der entgegenkommt. Und im selben Moment geht der andere Stürmer quer rüber, genau in die Lücke, die der Innenverteidiger hinter sich lässt. Der Innenverteidiger rückt raus und drückt von hinten.", *c))
d = [L3.pas("n10")]
d += L3.schieb({"r17": (52, 13), "r21": (60, 38)}, delay=0.8)
d += L3.schieb({"n8": (60, 36), "n2": (70, 46), "n5": (36, 36)}, delay=0.8)
k3.append(S("Klatschen lassen", "Der Stürmer dreht gar nicht erst auf. Er lässt direkt klatschen, zurück auf den Achter. Der hat sich ein Stück abgesetzt und steht mit Blick nach vorn.", *d))
e = L3.opts("n7", "n9", "n11", zu=("n9", "n11"))
e += L3.steil("n7", (80, 22), delay=1.6)
e += L3.schieb({"n9": (74, 30), "n8": (66, 38), "n11": (76, 9), "n2": (74, 46), "n6": (46, 21)}, delay=1.6)
e += L3.schieb({"r14": (74, 22), "r15": (80, 29), "r13": (80, 13)}, delay=2.0)
k3.append(S("Der dritte Mann", "Und jetzt der Pass in die Tiefe, genau in den Lauf vom zweiten Stürmer. Er startet mit dem Pass, also kein Abseits. Das ist der dritte Mann: Der eine Stürmer lockt den Verteidiger raus, der andere kriegt den Ball. Zwei Stürmer, die so zusammenspielen, sind schwer zu verteidigen.", *e))

# ---------- Kapitel 4: Seitenverlagerung auf die freie Schiene, hinten absichern ----------
NEON4 = {"k1": (10.5, 27.5), "n3": (34, 12), "n4": (26, 26), "n5": (30, 40), "n6": (38, 24), "n10": (50, 15),
         "n8": (50, 32), "n11": (62, 4), "n2": (64, 50), "n9": (64, 18), "n7": (64, 32)}
ROT4 = {"k2": (88, 27.5), "r13": (70, 6), "r14": (72, 18), "r15": (74, 30), "r12": (74, 42),
        "r16": (56, 4), "r17": (56, 15.5), "r18": (56, 27), "r21": (58, 39), "r19": (44, 12), "r20": (44, 30)}
L4 = Lage(NEON4, ROT4, ball="n11")
k4 = []
a = L4.schieb({"r13": (67, 6), "r16": (55, 12), "r14": (67, 16), "r19": (44, 17)})
a += L4.schieb({"n2": (64, 50), "n7": (66, 32), "n5": (30, 41)}, delay=0.3)
a += L4.opts("n10", "n9", "n3", delay=1.4, zu=("n10", "n9"))
k4.append(S("Alles auf einer Seite", "Neue Situation. Die linke Schiene hat den Ball, und der Gegner schiebt mit allen auf unsere linke Seite. Achter und Stürmer sind zugestellt. Frei ist der Weg zurück zum Halbverteidiger. Aber schau mal auf die andere Seite. Da steht unsere rechte Schiene ganz allein.", *a))
b = [L4.pas("n3")]
b += L4.schieb({"r19": (40, 16), "r20": (44, 28), "r16": (54, 9)}, delay=0.6)
b += L4.schieb({"n6": (36, 30), "n4": (26, 30), "n11": (64, 8), "n10": (52, 18)}, delay=0.6)
b += L4.opts("n6", "n4", delay=1.6)
b.append(L4.pas("n6", after=True))
k4.append(S("Der Sechser löst sich", "Der Ball geht zurück zum Halbverteidiger, und ein Stürmer läuft ihn an. Jetzt löst sich der Sechser aus dem Schatten und zeigt sich. Der Halbverteidiger hat zwei Wege: den Sechser oder den Innenverteidiger. Der Sechser ist frei und hat schon die andere Seite im Blick, also kriegt er ihn.", *b))
c = L4.opts("n2", "n8", "n5", zu=("n8",))
c.append(L4.pas("n2", after=True))
c += L4.schieb({"r12": (69, 47), "r21": (55, 45), "r18": (58, 32), "r15": (74, 34), "r14": (70, 22)}, delay=2.4)
c += L4.schieb({"n7": (70, 36), "n8": (56, 36), "n5": (34, 44), "n9": (68, 24), "n10": (56, 20)}, delay=2.4)
k4.append(S("Verlagern auf die freie Schiene", "Jetzt der lange Ball. Den Achter verdeckt der zweite Stürmer, aber die rechte Schiene ist ganz frei. Also geht der Ball diagonal rüber. Der Gegner muss quer übers ganze Feld schieben. Und er kommt zu spät.", *c))
d = [L4.dribbel("n2", (80, 49))]
d += L4.schieb({"r12": (73, 50.5), "r21": (64, 46), "r15": (81, 31), "r14": (79, 24), "r13": (76, 14), "r18": (64, 34),
                "r17": (62, 20), "r16": (60, 12), "r20": (52, 30), "r19": (48, 20)}, delay=0.3)
d += L4.schieb({"n9": (74, 26), "n7": (75, 36), "n8": (68, 36), "n10": (64, 22), "n11": (70, 10), "n6": (48, 34),
                "n5": (44, 44), "n4": (34, 32), "n3": (38, 18)}, delay=0.6)
k4.append(S("Die Schiene läuft an", "Die Schiene hat Platz, also läuft sie an, die Linie runter. Ihr Gegenspieler kommt nicht mehr hinterher. Die Abwehr läuft zurück in den Strafraum. Vorn warten die zwei Stürmer, beide noch auf Höhe vom letzten Verteidiger. Und der Achter rückt nach.", *d))
e = L4.opts("n9", "n7", "n8")
e += L4.steil("n9", (84, 37), delay=1.6)
e += L4.schieb({"n7": (86, 20), "n8": (73, 31), "n10": (72, 22)}, delay=1.6)
e += L4.schieb({"r15": (83, 34), "r14": (82, 26), "r13": (80, 18), "r12": (78, 48)}, delay=2.0)
k4.append(S("Kurzer und langer Pfosten", "Und jetzt pass auf: Einer kommt, einer geht. Der eine Stürmer kommt an den kurzen Pfosten, zum Ball hin. Der andere geht weg an den langen. Die zwei laufen über Kreuz, und der Achter wartet im Rückraum. Beide Stürmer starten erst mit der Flanke, also kein Abseits. Am kurzen Pfosten ist der Weg frei, also kommt der Ball flach dahin. Die Abwehr muss drei Räume auf einmal verteidigen.", *e))
f = L4.schieb({"n5": (52, 46), "n4": (42, 32), "n3": (46, 18), "n11": (72, 8)})
f += L4.schieb({"r21": (66, 44), "r20": (56, 30), "r19": (54, 22)}, delay=0.4)
k4.append(S("Hinten absichern", "Und hinten? Wenn beide Schienen so hoch stehen, ist hinter ihnen viel Platz. Darum schiebt die Dreierkette mit. Der Halbverteidiger rückt nach außen, hinter die Schiene. Der Innenverteidiger bleibt in der Mitte. Verlieren wir den Ball, ist schon einer da.", *f))

u = {"title": "Aufbau im 3-5-2", "code": "TA-004", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 3-5-2 von hinten auf? Zuerst siehst du, wer wo steht, wie die Dreierkette das Feld groß macht und warum die Schienenspieler die ganze Breite geben. Gegen zwei anlaufende Stürmer ist hinten immer einer frei, der Halbverteidiger dribbelt an und lockt den Gegner. Danach zwei Muster: die Stürmer im Wechselspiel und die Verlagerung auf die freie Schiene, mit der Absicherung hinten.",
 "organisation": ["Grundordnung: Torwart, Dreierkette mit zwei Halbverteidigern, ein Sechser, zwei Achter, außen zwei Schienenspieler, vorn zwei Stürmer.",
  "Hinten: Die Halbverteidiger gehen breit bis neben den Strafraum, gegen zwei Stürmer ist immer einer frei und dribbelt an.",
  "Außen: Die Schienenspieler stehen hoch und breit an der Linie, sie sind die einzige Breite im System.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball. Einer kommt, einer geht: Kommt ein Stürmer entgegen, läuft ein anderer in die Tiefe."],
 "organisation_show": ORG,
 "coaching_points": ["Halbverteidiger: breit und andribbeln", "Schiene hoch und breit", "Einer kommt, einer geht", "Seite zu? Auf die freie Schiene"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Drei-fünf-zwei. Heute keine Übung, sondern das System dahinter. Drei Verteidiger, zwei Schienenspieler und zwei Stürmer. Wer steht wo? Wer ist frei, wenn der Gegner presst? Und wie kommen wir nach vorn? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Gegen zwei Stürmer.", "Drei gegen zwei",
    "Jetzt presst ein Gegner im 4-4-2 mit zwei Stürmern. Hinten sind wir zu dritt, also ist immer ein Halbverteidiger frei. Der dribbelt an, bis ihn ein Mittelfeldspieler anläuft, und dann ist die Schiene frei. Kommt der Außenverteidiger raus, startet ein Stürmer in den Raum dahinter.",
    Lage(NEON2, ROT2).spieler(), [B("b1", 11.1, 28.1)] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Zwei Stürmer im Wechselspiel.", "Zwei Stürmer",
    "Der Gegner steht kompakt in der eigenen Hälfte. Ein Stürmer kommt entgegen und nimmt seinen Innenverteidiger mit, der andere läuft in die Lücke. Der Ball geht zum Stürmer, der lässt klatschen, und der Achter spielt den zweiten Stürmer in die Tiefe.",
    Lage(NEON3, ROT3).spieler(), [B("b1", 30.6, 12.6)] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Verlagern auf die freie Schiene.", "Auf die freie Schiene",
    "Der Gegner schiebt mit allen auf unsere Ballseite. Über den Halbverteidiger und den Sechser verlagern wir mit einem langen Ball auf die Schiene der anderen Seite. Die Schiene läuft an, die zwei Stürmer gehen über Kreuz an den kurzen und den langen Pfosten, der Achter in den Rückraum, und die Flanke kommt flach. Hinten schiebt die Dreierkette mit und sichert den Raum hinter den Schienen ab.",
    Lage(NEON4, ROT4).spieler(), [B("b1", 60.6, 4.6)] + ERSATZ, k4)]}
fertig()
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
