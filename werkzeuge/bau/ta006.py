import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *
# TA-006: Taktik-Erklärung (kind "Taktik", Anleitung TAKTIK.md, Vorbild TA-001). Aufbau im 4-1-4-1.
# Für Trainer U12 bis U17, etwa fünf Minuten, vier Kapitel: 1 Grundordnung und Aufbau ohne Gegner (die Flügel starten tief in der
# Mittelfeldreihe und rücken mit dem Ball nach vorn), 2 gegen ein 4-4-2-Pressing, das den Sechser in den Deckungsschatten nimmt
# (Achter kippt in den Halbraum ab, dritter Mann über den Sechser, Flügel startet aus der Mittelfeldreihe in die Tiefe),
# 3 Stürmer kommt entgegen und zieht den Innenverteidiger mit, Achter geht in die Tiefe (prallen lassen in den Lauf, Achter schieben
# nach), 4 Flügel und Außenverteidiger tauschen innen und außen (Flügel zieht mit Ball rein, Außenverteidiger hinterläuft).
# Recherche (24.11.2026): premierleague.com/news/4243851 (Rollen, Unterschied zum 4-3-3: Flügel tiefer, näher an Achtern und
# Außenverteidigern; im Ballbesitz wird oft ein 4-3-3), learning.coachesvoice.com (Achter laufen innen an den Flügeln vorbei in die
# Tiefe, Stürmer hält den Ball und bindet Mitspieler ein; Schwäche: Aufbau unter Druck, Stürmer allein), jobsinfootball.com und
# coachbetter.com (Sechser als erste Anspielstation, Dreiecke auf dem Flügel, Achter rücken aus der Reihe nach).
# Nummern: 2 RV, 3 LV, 4 und 5 Innenverteidiger, 6 Sechser, 8 und 10 Achter, 7 rechter Flügel, 11 linker Flügel, 9 Stürmer.
# Team Rot (4-4-2) 12-21, beide Torhüter neutral (k1 Neon links, k2 Rot rechts). Ein Trainer. Großfeld quer wie TA-001.
# Von Team Neon aus ist oben die linke Seite (3, 10, 11), unten die rechte (2, 8, 7).


def bogen(L, wer, ziel, bend, **k):
    """Laufweg im Bogen (Gegner läuft bogenförmig an), Position in der Lage mitführen."""
    L.p[wer] = tuple(ziel)
    return mv(wer, list(ziel), bend=bend, **k)


# ---------- Kapitel 1: Grundordnung, Feld groß machen, Aufbau ohne Gegner ----------
GRUND = {"k1": (10.5, 27.5), "n5": (24, 20), "n4": (24, 35), "n3": (31, 8), "n2": (31, 47), "n6": (36, 27.5),
         "n10": (47, 17), "n8": (47, 38), "n11": (48, 5), "n7": (48, 50), "n9": (64, 27.5)}
GROSS = {"n5": (19, 14), "n4": (19, 41), "n3": (38, 5), "n2": (38, 50), "n6": (29, 27.5), "n10": (43, 17), "n8": (43, 38),
         "n11": (54, 5), "n7": (54, 50), "n9": (72, 27.5)}
L = Lage(GRUND)
k1 = []
k1.append(S("Wer steht wo im 4-1-4-1", "Der Trainer spielt den Ball zum Torwart. Wir stehen im Vier-eins-vier-eins. Hinten die Viererkette. Davor ganz allein der Sechser. Dann kommt eine Reihe mit vier Spielern: innen die zwei Achter, außen die zwei Flügelspieler. Und ganz vorn der Stürmer.",
            ps("b1", f(GRUND["k1"]))))
L.ball = "k1"
k1.append(S("Das Feld groß machen", "Hat der Torwart den Ball, machen wir das Feld groß. Die Innenverteidiger gehen breit, die Außenverteidiger schieben hoch. Schau auf die Flügel: Die stehen nicht vorn neben dem Stürmer wie im Vier-drei-drei, sondern tiefer, in der Reihe mit den Achtern. Von da starten sie nach vorn.",
            *L.schieb(GROSS)))
s3 = L.opts("n5", "n6", "n4")
s3.append(L.pas("n5", after=True))
s3 += L.schieb({"n4": (22, 36), "n6": (27, 22), "n10": (44, 20), "n8": (45, 32), "n2": (42, 47), "n11": (56, 5),
                "n7": (56, 46), "n9": (70, 24)}, delay=2.0)
k1.append(S("Drei Wege für den Torwart", "Jetzt schau auf den Torwart. Er hat drei Möglichkeiten: links, rechts oder der Sechser in der Mitte. Er spielt nach links. Und mit dem Ball schiebt die ganze Mannschaft rüber. Auch die auf der anderen Seite.", *s3))
s4 = L.opts("n3", "n10", "n6")
s4.append(L.pas("n3", after=True))
s4 += L.schieb({"n10": (45, 13), "n11": (70, 5), "n6": (30, 18), "n9": (72, 22), "n8": (50, 28), "n7": (60, 44),
                "n2": (44, 46), "n4": (22, 33)}, delay=2.0)
k1.append(S("Einer kommt, einer geht", "Der Innenverteidiger spielt raus auf den Außenverteidiger, da ist am meisten Platz. Und jetzt pass auf: Einer kommt, einer geht. Der Achter kommt schräg vor den Ball. Dafür geht der Flügel die Linie hoch. Der Sechser schiebt mit und sichert ab.", *s4))
s5 = L.opts("n11", "n10", "n6", "n5")
s5 += [bl("n10", f(L.p["n3"]), after=True), L.pas("n10", after=True)]
s5 += L.schieb({"n11": (76, 8), "n9": (78, 22), "n8": (58, 28), "n6": (36, 20), "n7": (68, 42), "n2": (50, 46),
                "n4": (26, 32)}, delay=3.0)
k1.append(S("Der Achter im Halbraum", "Der Außenverteidiger hat jetzt vier Wege. Die Linie hoch, schräg in den Achter, oder zurück zum Sechser oder zum Innenverteidiger. Der Achter steht offen im Halbraum und schaut zum Ball. Also kriegt er ihn.", *s5))
von = f(L.p["n3"])
s6 = [bl("n10", list(L.p["n11"]), von=von, dauer=1.3), drehen("n10", list(L.p["n11"]), delay=0.4)]
s6 += L.opts("n11", "n9", "n8", delay=1.5)
s6.append(L.pas("n11", after=True))
s6 += L.schieb({"n9": (84, 24), "n8": (74, 30), "n7": (80, 40), "n10": (58, 14), "n3": (50, 5), "n6": (44, 22),
                "n2": (56, 46)}, delay=3.2)
k1.append(S("Aus der Reihe nach vorn", "Der Achter dreht auf und sieht drei Möglichkeiten: den Flügel, den Stürmer oder den anderen Achter. Der Flügel ist frei, also geht der Ball zu ihm. Und schau, was vorn passiert: Beide Flügel und ein Achter sind jetzt mit dem Stürmer ganz vorn. Aus der Mittelfeldreihe wird ein Angriff.", *s6))

# ---------- Kapitel 2: gegen ein 4-4-2-Pressing, der Sechser steht im Deckungsschatten ----------
NEON2 = {"k1": (10.5, 27.5), "n5": (18, 13), "n4": (18, 42), "n6": (30, 23), "n3": (36, 5), "n2": (36, 50),
         "n10": (42, 17), "n8": (42, 38), "n11": (54, 5), "n7": (54, 50), "n9": (70, 27.5)}
ROT2 = {"k2": (88, 27.5), "r19": (24, 22), "r20": (24, 35), "r16": (48, 8), "r17": (48, 21), "r18": (48, 34),
        "r21": (48, 47), "r13": (62, 8), "r12": (62, 47), "r14": (76, 21), "r15": (76, 34)}
L2 = Lage(NEON2, ROT2, ball="k1")
k2 = []
a = L2.opts("n5", "n6", "n4", zu=("n6",))
a.append(L2.pas("n5", after=True))
a.append(bogen(L2, "r19", (21, 17.5), 3, delay=2.0))
a += L2.schieb({"r20": (26, 31), "r16": (44, 7), "r17": (46, 18), "r18": (48, 30), "r21": (50, 45), "r13": (60, 7),
                "r14": (72, 22), "r15": (72, 32), "r12": (64, 44)}, delay=2.0)
a += L2.schieb({"n4": (20, 40), "n2": (38, 49), "n8": (44, 36), "n9": (68, 25)}, delay=2.2)
k2.append(S("Der Sechser im Schatten", "Jetzt wird's ernst. Der Gegner presst im Vier-vier-zwei. Die zwei Stürmer stehen eng vor unserem Sechser, der Weg zu ihm ist zu. Also spielt der Torwart auf den linken Innenverteidiger. Und der Stürmer läuft ihn im Bogen an. So hat er unseren Sechser im Rücken, im Deckungsschatten.", *a))
b2 = L2.schieb({"n10": (34, 10), "n11": (66, 4), "n3": (38, 4), "r13": (70, 7)})
b2 += L2.opts("n3", "n10", "n6", delay=1.2, zu=("n3", "n6"))
b2.append(L2.pas("n10", after=True))
b2 += L2.schieb({"r17": (40, 13), "r18": (47, 25), "r20": (25, 31)}, delay=3.0)
k2.append(S("Der Achter kippt ab", "Was jetzt? Einer kommt, einer geht. Der Achter lässt sich in den Halbraum fallen, neben den Stürmer. Dafür geht der Flügel ganz nach vorn und nimmt seinen Gegenspieler mit. Den Außenverteidiger läuft schon einer an, der Sechser ist zu. Aber der Achter ist frei. Also kriegt er den Ball.", *b2))
c2 = [L2.pas("n6")]
c2 += L2.schieb({"n8": (53, 35), "n9": (66, 27), "r21": (50, 45)}, delay=0.8)
c2 += L2.schieb({"r20": (28, 27)}, delay=1.0)
k2.append(S("Der dritte Mann", "Und jetzt kommt der Trick. Der Achter lässt den Ball direkt prallen, auf den Sechser. Der Stürmer läuft immer noch zum Innenverteidiger. Unser Sechser steht also nicht mehr im Schatten. Er ist frei und hat das ganze Feld vor sich.", *c2))
von = f(L2.p["n10"])
d2 = [bl("n6", list(L2.p["n8"]), von=von, dauer=1.3), drehen("n6", list(L2.p["n8"]), delay=0.4)]
d2 += L2.opts("n8", "n9", "n10", delay=1.5, zu=("n9",))
d2.append(L2.pas("n8", after=True))
d2 += L2.schieb({"r18": (50, 30), "r21": (54, 43), "r15": (70, 34), "r12": (68, 47), "r20": (30, 26)}, delay=3.2)
k2.append(S("Raus aus dem Pressing", "Der Sechser dreht auf. Den Stürmer deckt der Innenverteidiger, aber rechts im Halbraum steht der andere Achter. Zwischen den Reihen, ganz allein. Also geht der Ball dahin. Das Pressing ist überspielt.", *d2))
e2 = L2.schieb({"n9": (60, 28), "n7": (66, 48), "n2": (44, 51)})
e2 += L2.schieb({"r15": (66, 32)}, delay=0.6)
e2 += L2.opts("n7", "n9", "n2", delay=1.4)
e2 += L2.steil("n7", (84, 46), delay=2.6)
e2 += L2.schieb({"r12": (80, 47), "r14": (78, 30)}, delay=2.8)
k2.append(S("Der Flügel startet", "Noch mal: Einer kommt, einer geht. Der Stürmer kommt dem Achter entgegen, und der Innenverteidiger geht mit. Dafür startet der Flügel aus der Mittelfeldreihe in die Tiefe. Mit dem Pass, also kein Abseits. Und weil er von hinten kommt, hat ihn keiner auf dem Zettel.", *e2))

# ---------- Kapitel 3: Stürmer kommt entgegen, Achter geht in die Tiefe ----------
NEON3 = {"k1": (10.5, 27.5), "n5": (22, 15), "n4": (22, 40), "n6": (32, 27.5), "n3": (44, 4), "n2": (44, 51),
         "n10": (50, 15), "n8": (50, 40), "n11": (64, 5), "n7": (64, 50), "n9": (68, 27.5)}
ROT3 = {"k2": (88, 27.5), "r19": (40, 21), "r20": (40, 34), "r16": (56, 8), "r17": (56, 20), "r18": (56, 35),
        "r21": (56, 47), "r13": (74, 9), "r14": (74, 21), "r15": (74, 34), "r12": (74, 46)}
L3 = Lage(NEON3, ROT3, ball="n4")
k3 = []
a = L3.opts("n6", "n2", "n5")
a.append(L3.pas("n6", after=True))
a += L3.schieb({"r19": (40, 22), "r20": (41, 33)}, delay=2.0)
k3.append(S("Der Gegner steht kompakt", "Neue Situation. Der Gegner wartet im Mittelfeld, im Vier-vier-zwei, ganz eng. Der Innenverteidiger spielt auf den Sechser. Und vorn? Da stehen zwei Reihen, und der Stürmer hat einen Verteidiger im Rücken.", *a))
b3 = L3.schieb({"n9": (62, 24), "n10": (70, 14), "n8": (56, 30), "n11": (66, 5), "n7": (64, 47)})
b3 += L3.opts("n9", "n10", "n2", delay=1.2, zu=("n10",))
b3.append(L3.pas("n9", after=True))
b3 += L3.schieb({"r14": (68, 27), "r17": (57, 21), "r18": (58, 32), "r13": (74, 7)}, delay=2.6)
k3.append(S("Der Stürmer kommt entgegen", "Und jetzt das Muster für dieses System. Einer kommt, einer geht. Der Stürmer kommt entgegen, zwischen die Reihen. Im selben Moment geht der Achter in die Tiefe. Der Sechser spielt flach durch die Lücke, auf den Stürmer. Und schau: Der Innenverteidiger geht mit ihm raus.", *b3))
c3 = L3.opts("n10", "n8", zu=("n8",))
c3 += L3.steil("n10", (82, 14), delay=1.2)
c3 += L3.schieb({"r13": (80, 10), "r14": (82, 21), "r15": (82, 31), "r12": (80, 42), "r17": (62, 23), "r18": (64, 36)}, delay=1.6)
c3 += L3.schieb({"n9": (76, 27), "n8": (68, 30), "n11": (74, 4), "n7": (76, 44)}, delay=1.6)
k3.append(S("Prallen lassen in den Lauf", "Genau da, wo der Innenverteidiger weg ist, ist jetzt Platz. Den Achter daneben hat der Gegner zu. Also lässt der Stürmer den Ball direkt prallen, in den Lauf vom Achter in der Tiefe. Der war beim Pass noch auf Höhe, also kein Abseits. Ein Kontakt, und die Abwehr ist offen.", *c3))
d3 = L3.opts("n9", "n8", zu=("n9",))
d3.append(L3.pas("n8", after=True))
d3 += L3.schieb({"r18": (66, 33), "r15": (78, 30), "r14": (80, 24)}, delay=1.8)
k3.append(S("Die Achter schieben nach", "Und wer kommt hinterher? Den Stürmer hat der Verteidiger wieder. Aber der andere Achter schiebt aus der Mittelfeldreihe nach, genau in den Rückraum. Er ist frei, also legt der Achter vorn zurück. Freie Schussbahn.", *d3))

# ---------- Kapitel 4: Flügel und Außenverteidiger tauschen innen und außen ----------
NEON4 = {"k1": (10.5, 27.5), "n5": (22, 15), "n4": (24, 40), "n6": (32, 27.5), "n3": (44, 4), "n2": (40, 50),
         "n10": (50, 15), "n8": (50, 37), "n11": (64, 5), "n7": (52, 51), "n9": (68, 27.5)}
ROT4 = {"k2": (88, 27.5), "r19": (38, 23), "r20": (40, 35), "r16": (56, 10), "r17": (56, 22), "r18": (58, 34),
        "r21": (60, 46), "r13": (74, 10), "r14": (74, 21.5), "r15": (74, 33), "r12": (74, 44.5)}
L4 = Lage(NEON4, ROT4, ball="n4")
k4 = []
a = L4.opts("n7", "n6", "n2")
a.append(L4.pas("n7", after=True))
a += L4.schieb({"r21": (58, 47), "r18": (58, 36), "r20": (42, 38), "r12": (74, 45)}, delay=2.0)
k4.append(S("Der Flügel steht tief", "Zum Schluss die Flügel. Weil unser Flügel tief steht, in der Mittelfeldreihe, ist er oft frei. Der Außenverteidiger vom Gegner geht nicht so weit mit raus. Der Innenverteidiger spielt ihn schräg an.", *a))
b4 = [L4.dribbel("n7", (62, 41))]
b4 += L4.schieb({"r21": (56, 43), "r12": (70, 38)}, delay=0.5)
b4 += L4.schieb({"n2": (60, 51), "n9": (70, 24)}, delay=0.2)
b4 += [mv("n8", [56, 29], delay=0.2), mv("n8", [66, 31], after=True)]
L4.p["n8"] = (66, 31)
k4.append(S("Rein mit Ball, raus ohne Ball", "Jetzt tauschen sie. Der Flügel zieht mit Ball nach innen, in den Halbraum. Und der Außenverteidiger? Der läuft außen an ihm vorbei, die Linie hoch. Einer geht rein, einer geht raus. Und der Gegner muss sich entscheiden.", *b4))
c4 = L4.opts("n2", "n9", "n8", zu=("n9",))
c4 += L4.steil("n2", (82, 50), delay=1.4)
c4 += L4.schieb({"r12": (80, 44), "r15": (78, 34), "r21": (62, 46)}, delay=1.8)
c4 += L4.schieb({"n9": (80, 30), "n8": (70, 30), "n11": (76, 5)}, delay=1.8)
k4.append(S("Außen ist frei", "Der Außenverteidiger vom Gegner rückt rein zum Flügel. Genau dadurch ist außen frei. Also steckt der Flügel durch, in den Lauf vom Außenverteidiger. Und vorn gehen alle in den Strafraum.", *c4))

u = {"title": "Aufbau im 4-1-4-1", "code": "TA-006", "kind": "Taktik",
 "focuses": ["Passspiel", "Zusammenspiel"], "age_groups": ["D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14", "U15-U17"], "duration_minutes": 5, "players_min": 22, "players_max": 22,
 "field_size": "65 x 100 m",
 "description": "Wie baut eine Mannschaft im 4-1-4-1 von hinten auf? Zuerst siehst du, wer wo steht und wie die Flügel aus der Mittelfeldreihe nach vorn rücken. Dann presst ein Gegner und nimmt den Sechser in den Deckungsschatten, und ein Achter kippt in den Halbraum ab. Zum Schluss zwei Muster: Der Stürmer kommt entgegen und ein Achter geht in die Tiefe, und Flügel und Außenverteidiger tauschen innen und außen.",
 "organisation": ["Grundordnung: Torwart, Viererkette, davor ein Sechser, dann eine Reihe aus zwei Achtern und zwei Flügeln, vorn ein Stürmer.",
  "Hinten: Die Innenverteidiger gehen breit, die Außenverteidiger schieben hoch, der Sechser bietet sich zwischen den gegnerischen Stürmern an.",
  "Mittelfeld: Die Achter stehen in den Halbräumen, die Flügel starten tiefer als im 4-3-3 und rücken mit dem Ball nach vorn.",
  "Bewegung: Mit jedem Pass schiebt die ganze Mannschaft zum Ball. Einer kommt, einer geht: Kommt einer zum Ball, läuft ein anderer in die Tiefe."],
 "organisation_show": ORG,
 "coaching_points": ["Sechser zu? Achter kippt ab", "Einer kommt, einer geht", "Flügel starten aus der Reihe", "Achter schieben nach"],
 "materials": ["Großfeld mit zwei Toren", "Leibchen in zwei Farben", "Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau im Vier-eins-vier-eins. Heute keine Übung, sondern das System dahinter. Ein Sechser ganz allein vor der Abwehr, davor eine Reihe aus vier. Wie kommt so eine Mannschaft von hinten nach vorn? Schauen wir's uns an.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": Lage(GRUND).spieler(),
  "balls": [B("b1", 16.6, 55.9)] + ERSATZ, "dims": DIMS, "steps": k1},
 "versions": [
  V("Kapitel 2", "Kapitel zwei: Wenn der Sechser zu ist.", "Wenn der Sechser zu ist",
    "Jetzt presst ein Gegner im 4-4-2. Seine Stürmer laufen die Innenverteidiger im Bogen an und nehmen den Sechser in den Deckungsschatten. Ein Achter kippt in den Halbraum ab, lässt prallen, und der Sechser kommt doch noch an den Ball. Dann startet ein Flügel aus der Mittelfeldreihe in die Tiefe.",
    Lage(NEON2, ROT2).spieler(), [B("b1", *f(NEON2["k1"]))] + ERSATZ, k2),
  V("Kapitel 3", "Kapitel drei: Einer kommt, einer geht.", "Stürmer kommt, Achter geht",
    "Der Gegner steht kompakt im Mittelfeld. Der Stürmer kommt zwischen die Reihen entgegen und zieht seinen Innenverteidiger mit. Im selben Moment geht ein Achter in die Tiefe, genau in den Raum, der frei wird. Der andere Achter schiebt aus der Mittelfeldreihe nach.",
    Lage(NEON3, ROT3).spieler(), [B("b1", *f(NEON3["n4"]))] + ERSATZ, k3),
  V("Kapitel 4", "Kapitel vier: Flügel und Außenverteidiger tauschen.", "Innen und außen tauschen",
    "Der Flügel steht tief und wird angespielt. Er zieht mit Ball nach innen, der Außenverteidiger hinterläuft ihn außen. Rückt der gegnerische Außenverteidiger rein, ist die Linie frei. Dann rücken alle in den Strafraum nach.",
    Lage(NEON4, ROT4).spieler(), [B("b1", *f(NEON4["n4"]))] + ERSATZ, k4)]}
fertig()
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
