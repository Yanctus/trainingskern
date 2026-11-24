import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P8 (U15-U17, Woche 18 Phase 6): Defending the Box Under Pressure (Wave). 50 x 40 Yards = 46 x 37 m (gerundet 45 x 35 m),
# Tore oben und unten mit neutralen Torhütern (Großfeldtore), links und rechts eine Außenzone (5 Yards = 4,6 m, gerundet 5 m).
# Feld x 10-88, y 5-55 (in der Breite etwas gestreckt). Nicht gedreht.
# Vier Dreiergruppen: Die beiden verteidigenden Gruppen sind Team Neon (PDF hellblau 2, 5, 3 oben; PDF pink 3, 5, 2 unten,
# neu nummeriert 4, 6, 8), die beiden angreifenden Gruppen sind Team Rot (PDF dunkelblau 11, 9, 7 greift oben an; PDF gelb
# 11, 9, 7 greift unten an, neu nummeriert 12, 10, 14). Die Gruppe unten steht wie im Video vor dem Tor (im PDF daneben).
# Die zweite Angriffsgruppe wartet an der Mittellinie, 12 und 14 außerhalb des Feldes (3D-Abstand).
# Ein Trainer statt zwei: Er steht links an der Seite und spielt beide Wellen an (im PDF spielt der Trainer unten rechts die erste).
# Fassungen: PDF Progression 1 (zwei gegen zwei) und Progression 2 (Ball behalten und die nächste Welle selbst anspielen,
# zwei Punkte laut Ton). Progression 3 (sofort zweite, tiefe Flanke) nur im Text der zweiten Fassung.
# Sichtkegel: kein Kegel im Video; aus dem PDF "Track runners into the box, not just the ball": Spieler zwei schaut vor der Flanke
# zu seinem Läufer. In der zweiten Steigerung nimmt Spieler drei an und dreht auf (Blick mit von und Drehpfeil).
# Keine Dublette: UE-225 (58-P3), UE-185 (58-P4), UE-308 (58-P6, 5 gegen 5 auf ein Tor) und UE-248 (58-P7) haben andere
# Organisation und Abläufe; hier laufen Angriffswellen auf zwei Tore.
T = P("T", "c", 4, 18, "T")
ERSATZ = [B("s1", 6.6, 21.5), B("s2", 3, 22.5)]
POS = {"n2": (32, 14), "n5": (58, 13), "n3": (69, 15.5),
       "r11": (14, 31), "r9": (45, 31), "r7": (84, 32),
       "r12": (4, 38), "r10": (55, 35), "r14": (94, 38),
       "n4": (31, 46), "n6": (40, 47.5), "n8": (67, 46)}
TW = [P("k1", "t", 49, 7.5, "TW"), P("k2", "t", 49, 52.5, "TW")]
def sp(ohne=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items() if i not in ohne] + TW + [T]
def f(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(10, 5, 78, 50), line(18, 5, 18, 55), line(80, 5, 80, 55)]
TORE = [{"x": 49, "y": 5, "side": "top", "size": "gross"}, {"x": 49, "y": 55, "side": "bottom", "size": "gross"}]
# Nur die Breiten-Maßlinie unten: rechts stehen Wartende an der Seite, die Länge steht in field_size
DIMS = dims(10, 88, 5, 55, "45 m", "35 m")[:1]
FLUEGEL = dict(r7=(84, 21))

u = {"title": "Flankenwellen auf zwei Tore", "code": "UE-348", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 16,
 "field_size": "45 x 35 m",
 "description": "Vier Dreiergruppen und zwei Tore. Vor jedem Tor verteidigt eine Gruppe von Team Neon, die beiden anderen Gruppen greifen in Wellen an, erst auf das eine Tor, dann sofort auf das andere. Jeder Angriff läuft über außen und endet mit einer Flanke. Wer weit und breit klärt, holt einen Punkt für Team Neon.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 35 Metern mit zwei Toren und Torhütern. Links und rechts ist eine Außenzone von 5 Metern abgeteilt.",
  "Verteilen: Vor jedem Tor stehen drei Verteidiger von Team Neon. Die erste Angriffsgruppe von Team Rot steht an der Mittellinie, die zweite wartet daneben. Der Trainer steht mit den Bällen an der Seite.",
  "Ablauf: Der Trainer spielt in die Mitte, der Ball geht raus auf den Flügel, dann kommt die Flanke. Ist der Angriff vorbei, greift sofort die zweite Gruppe das andere Tor an.",
  "Wertung und Wechsel: Weit und breit geklärt gibt einen Punkt für Team Neon, ein Treffer einen Punkt für Team Rot. Nach zwei Wellen verteidigt die erste Angriffsgruppe, und die Verteidiger greifen an."],
 "organisation_show": ORG,
 "coaching_points": ["Den Raum zwischen den Pfosten zumachen", "Nicht nur auf den Ball schauen, Läufer mitnehmen", "Erster am Ball, dann weit und breit klären", "Früh reden, wer geht drauf und wer sichert"],
 "materials": ["2 Großfeldtore", "8 Hütchen für die Außenzonen", "Viele Bälle", "Leibchen in vier Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Flankenwellen auf zwei Tore. Team Neon verteidigt vor beiden Toren, und Team Rot kommt in Wellen über außen, eine Flanke nach der anderen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *f(4, 18))] + ERSATZ,
  "steps": [
   S("Trainer spielt in die Mitte", "Der Trainer spielt flach in die Mitte zu Spieler neun. Die erste Gruppe von Team Rot greift jetzt das obere Tor an.",
     ps("b1", f(45, 31))),
   S("Raus auf den Flügel", "Spieler sieben startet in der Außenzone nach vorn und bekommt den Ball in den Lauf. Gleichzeitig starten Spieler neun und Spieler elf in die Mitte.",
     mv("r7", [84, 21]), ps("b1", f(84, 21), delay=0.4), mv("r9", [54, 20], delay=0.8), mv("r11", [30, 24], delay=0.8)),
   S("Läufer im Blick behalten", "Spieler zwei schaut nicht nur auf den Ball. Er dreht kurz den Kopf und sieht Spieler elf kommen. Dann geht er mit und bleibt zwischen ihm und dem Tor. Spieler fünf nimmt Spieler neun am kurzen Pfosten.",
     bl("n2", [30, 24]), mv("r11", [42, 18], after=True), mv("n2", [37, 11], delay=0.6), mv("r9", [60, 12], delay=0.6), mv("n5", [56, 9.5], delay=0.8)),
   S("Weit und breit geklärt: Punkt", "Spieler sieben flankt an den langen Pfosten. Spieler zwei ist vor Spieler elf dran und köpft hoch und weit nach außen, und das gibt einen Punkt für Team Neon. Sofort spielt der Trainer die zweite Gruppe an, und die greift das andere Tor an.",
     ps("b1", f(37, 11), bend=-3), ps("b1", [14, 40], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Vor dem Tor verteidigen nur noch zwei.", "Zwei gegen zwei vor dem Tor",
    "Vor dem Tor verteidigen jetzt nur noch zwei Spieler gegen zwei Angreifer. Der dritte setzt aus, nach jeder Welle wird durchgewechselt. Die beiden sprechen sich früh ab, einer nimmt den kurzen Pfosten, der andere den Raum dahinter.",
    sp(ohne=("n3",), **FLUEGEL), [B("b1", *f(84, 21))] + ERSATZ,
    [S("Zwei Läufer, zwei Verteidiger", "Spieler sieben hat den Ball außen. Spieler neun läuft an den kurzen Pfosten, Spieler elf an den langen. Spieler fünf geht mit Spieler neun, Spieler zwei nimmt Spieler elf. Mehr Hilfe gibt es nicht.",
       mv("r9", [58, 12]), mv("r11", [40, 16], delay=0.2), mv("n5", [55, 9.5], delay=0.4), mv("n2", [35, 11.5], delay=0.5)),
     S("Kurzer Pfosten geklärt: Punkt", "Die Flanke kommt scharf an den kurzen Pfosten. Spieler fünf ist vor Spieler neun am Ball und köpft weit nach außen, und das gibt einen Punkt für Team Neon.",
       ps("b1", f(55, 9.5)), ps("b1", [20, 40], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ball behalten statt klären.", "Ball sichern, dann raus",
    "Kommt ein Verteidiger sauber an den Ball, muss er nicht klären. Er nimmt ihn an, bleibt ruhig und spielt selbst die nächste Welle an. Das gibt zwei Punkte für Team Neon. Noch schwerer wird es, wenn Team Rot nach dem Klären sofort eine zweite, tiefe Flanke schlagen darf.",
    sp(**FLUEGEL), [B("b1", *f(84, 21))] + ERSATZ,
    [S("Flanke zu flach", "Spieler sieben flankt zu flach. Spieler drei schaut zum Ball, geht dazwischen und hat ihn.",
       mv("r9", [56, 21]), mv("r11", [40, 16], delay=0.2), bl("n3", [84, 21]), mv("n3", [64, 13], delay=0.3), ps("b1", f(64, 13), after=True)),
     S("Annehmen, aufdrehen: zwei Punkte", "Er bleibt ruhig, dreht auf und spielt flach zu Spieler vierzehn an der Seite. Damit läuft die nächste Welle aufs andere Tor, und das gibt zwei Punkte für Team Neon.",
       mv("r14", [85, 40]), bl("n3", [85, 40], von=[84, 21], dauer=1.3), drehen("n3", [85, 40], delay=0.4), ps("b1", f(85, 40), after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
