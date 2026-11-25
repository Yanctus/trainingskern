import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 39-P13 (U15-U17, Woche 42 Phase 6): Defending the Switch of Play (Advanced Lead). 40 x 50 Yards = 37 x 46 m (gerundet
# 35 x 45 m). Quer wie im PDF und im Video (Tore links und rechts), Feld x 12-86, y 4-51, Mittellinie gestrichelt. Kein Großfeld
# (14 Spieler), Figuren normal groß. Rechts steht ein Tor: nur die Längen-Maßlinie.
# Rot (Video) / Pink (PDF), die Verteidiger, sind Team Neon, Nummern wie im Video (5, 6 Innenverteidiger; Paare 8/4 und 10/9
# warten an der Mittellinie). Blau ist Team Rot, neu nummeriert, wo Nummern doppelt sind: 10 -> 11, 6 -> 16, 4 -> 14; 2, 3, 7
# bleiben. Beide Torhüter neutral (k1, k2), weil zwei TW-Nummern nicht gehen. Die vier Puppen als Stangen. Die gelben
# Markierungsscheiben (Grundposition der Innenverteidiger) weggelassen, damit keine Laufwege hindurchgehen. Ein Trainer statt zwei,
# unten an der Seitenlinie. Positionen für den 3D-Abstand leicht verschoben (wartende Paare weiter zur Seitenlinie).
# Ablauf nach Video (0:10-0:35, Passfolge 1-6) und PDF-Text: links passen Spieler 16, 11 und 7, die Innenverteidiger pressen und
# sichern im Wechsel; rechts Spieler 14 über den Torwart zu Spieler 2, Pass nach innen auf Spieler 4 (Neon), Ablage, Seitenwechsel
# lang auf Spieler 3, Flanke, vier gegen zwei vor dem linken Tor. Zugleich geht der linke Ball zu Spieler 4, der mit Spieler 9 zwei
# gegen eins auf das rechte Tor kontert. Im Original kommt der linke Ball von Spieler 11, hier von Spieler 7 (der Ball ist nach
# dem Wechsel dort). Wertung im Original nicht genannt: Treffer nach der Flanke gibt einen Punkt für Team Rot, Treffer im Konter
# einen Punkt für Team Neon. Rollentausch wie im Video: die Paare 8/10 werden die nächsten Innenverteidiger.
# Fassungen: PDF Key Coaching Point 1 (pressen und sichern als Paar) und 2 (das Tor gemeinsam schützen; Ton „goal side, ball side“).
# Sichtkegel aus dem Ton („getting goal side, ball side, so players can see the ball and their opposition player“, im Video nicht
# eingezeichnet): In Fassung 2 hat Spieler sechs erst seinen Gegenspieler, dann den Flankengeber im Blick (ein Kegel mit von).
# Keine Dublette: UE-232 (50-P8, Welle mit Seitenwechsel), UE-274 (Seitenwechsel ins Minitor), UE-248 (58-P7, Flanken klären),
# UE-308 (58-P6, Flanken klären im 5 gegen 5).
FX0, FX1, FY0, FY1 = 12, 86, 4, 51
MY = 27.5
T = P("T", "c", 70, 55.3, "T")
ERSATZ = [B("s1", 73.5, 55.8), B("s2", 76, 55.8)]
POS = {"k1": (13.5, 27.5), "n5": (22, 19.5), "n6": (22, 35.5), "r11": (33.5, 21.5), "r7": (33.5, 37), "r16": (48, 28.5),
       "n8": (43, 12), "n4": (51.5, 12), "n10": (43, 45), "n9": (51.5, 45),
       "r2": (61, 6.5), "r14": (66, 26), "r3": (60, 48.5), "k2": (83, 27.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(49, FY0, 49, FY1)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": MY, "side": "right", "size": "gross"}]
STANGEN = [C(70, 10, shape="stange"), C(59, 22.5, shape="stange"), C(59, 33.5, shape="stange"), C(69, 41, shape="stange")]
DIMS = dims(FX0, FX1, FY0, FY1, "45 m", "35 m")[:1]
BAELLE = [B("b1", *fu(POS["r16"])), B("b2", *fu(POS["r14"]))]

u = {"title": "Seitenwechsel verteidigen", "code": "UE-418", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "35 x 45 m",
 "description": "Zwei Abläufe laufen gleichzeitig. Vor dem einen Tor pressen und sichern zwei Innenverteidiger von Team Neon im Wechsel, während Team Rot sich den Ball zuspielt. Auf der anderen Seite baut Team Rot über den Torwart auf und verlagert lang, dann kommt die Flanke, und es heißt vier gegen zwei. Gleichzeitig kontert Team Neon zwei gegen eins auf das andere Tor.",
 "organisation": ["Aufbauen: Ein Feld von 35 mal 45 Metern mit zwei großen Toren und gestrichelter Mittellinie. In der rechten Hälfte stehen vier Stangen als Gegenspieler. Der Trainer steht mit vielen Bällen an der Seitenlinie.",
  "Verteilen: Links verteidigen zwei Innenverteidiger von Team Neon vor dem Torwart gegen drei Spieler von Team Rot. Rechts stehen von Team Rot ein Innenverteidiger und zwei Außenverteidiger vor dem anderen Torwart. Zwei Paare von Team Neon warten an der Mittellinie.",
  "Ablauf: Links spielt sich Team Rot den Ball zu, und die Innenverteidiger pressen und sichern je nach Ballseite. Rechts geht der Ball über den Torwart nach außen, nach innen zu einem Spieler von Team Neon und zurück, dann lang auf die andere Seite zur Flanke. Im selben Moment geht der linke Ball zu diesem Spieler, und er kontert mit seinem Partner zwei gegen eins.",
  "Wertung und Wechsel: Ein Treffer nach der Flanke gibt einen Punkt für Team Rot, ein Treffer im Konter gibt einen Punkt für Team Neon. Nach jedem Durchgang tauschen die Rollen, und ein wartendes Paar wird zu den neuen Innenverteidigern."],
 "organisation_show": ORG,
 "coaching_points": ["Einer presst, einer sichert, immer als Paar", "Torseitig und ballseitig stehen", "Bei der Flanke gehört der erste Kontakt uns", "Zwei gegen eins: Gegner anlocken, dann querlegen"],
 "materials": ["2 Großfeldtore", "4 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Seitenwechsel verteidigen. Zwei Abläufe laufen gleichzeitig. Vor dem einen Tor pressen und sichern die Innenverteidiger, nach dem Seitenwechsel kommt die Flanke, und auf der anderen Seite läuft ein Konter zwei gegen eins.",
 "board": {"lines": LINES, "goals": TORE, "cones": STANGEN, "players": sp(), "balls": BAELLE + ERSATZ,
  "steps": [
   S("Links pressen, rechts zum Torwart", "Beide Seiten laufen gleichzeitig. Links spielt Spieler sechzehn auf Spieler elf. Spieler fünf geht drauf, und Spieler sechs sichert schräg hinter ihm ab. Rechts spielt Spieler vierzehn zum Torwart und läuft sich frei.",
     ps("b1", fu(POS["r11"])), mv("n5", [30.5, 21], delay=0.3), mv("n6", [25.5, 27.5], delay=0.3),
     ps("b2", fu(POS["k2"])), mv("r14", [76, 19], delay=0.4)),
   S("Ball rüber, Rollen tauschen", "Links geht der Ball rüber zu Spieler sieben. Jetzt presst Spieler sechs, und Spieler fünf fällt hinter ihn zurück. Rechts kommt der Ball vom Torwart zurück zu Spieler vierzehn.",
     ps("b1", fu(POS["r7"])), mv("n6", [30.5, 35.5], delay=0.3), mv("n5", [25.5, 27], delay=0.3), ps("b2", fu([76, 19]))),
   S("Raus, nach innen, abgelegt", "Spieler vierzehn spielt raus zu Spieler zwei. Der passt nach innen auf Spieler vier, und Spieler vier legt direkt zurück auf Spieler vierzehn.",
     ps("b2", fu(POS["r2"])), ps("b2", fu(POS["n4"]), after=True), ps("b2", fu([76, 19]), after=True)),
   S("Seitenwechsel, der Konter startet", "Jetzt kommt der Seitenwechsel. Spieler drei sprintet außen nach vorn, und Spieler vierzehn spielt ihn lang an. Genau in dem Moment spielt Spieler sieben den linken Ball zu Spieler vier. Spieler neun startet sofort in die Tiefe.",
     mv("r3", [44, 50.5]), mv("r3", [31, 47], after=True), ps("b2", fu([31, 47]), delay=0.8),
     ps("b1", fu(POS["n4"]), delay=0.3), mv("n9", [67, 33], delay=0.6)),
   S("Flanke, erster Kontakt klärt", "Spieler drei flankt, drinnen sind es vier gegen zwei. Spieler fünf und Spieler sechs nehmen ihre Läufer mit und bleiben zwischen Gegner und Tor. Spieler sechs ist zuerst am Ball und klärt weit raus. Kein Punkt für Team Rot.",
     mv("r11", [20, 21]), mv("n5", [17, 23.5], delay=0.2), mv("r7", [22.5, 32.5]), mv("n6", [17.5, 31.5], delay=0.2),
     mv("r16", [27, 28], delay=0.2), ps("b2", fu([17.5, 31.5]), delay=1.0), ps("b2", [30, 16], after=True)),
   S("Zwei gegen eins: Punkt", "Auf der anderen Seite dribbelt Spieler vier auf Spieler vierzehn zu und lockt ihn raus. Dann legt er quer auf Spieler neun. Der schiebt ein, und das gibt einen Punkt für Team Neon. Danach tauschen die Rollen, und Spieler acht und Spieler zehn sind die nächsten Innenverteidiger.",
     dr("n4", "b1", [62, 16]), mv("r14", [69, 21], delay=0.3), ps("b1", fu([67, 33]), after=True), ps("b1", [85.5, 31.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Einer presst, der andere sichert ab, und das immer als Paar.", "Pressen und sichern zu zweit",
    "Der Innenverteidiger auf der Ballseite geht drauf, der andere steht schräg hinter ihm und sichert ab. Wechselt der Ball die Seite, tauschen beide die Rollen. Der Abstand zwischen den beiden bleibt klein, damit kein Pass durch die Mitte geht.",
    sp(), [B("b1", *fu(POS["r11"])), B("b2", *fu(POS["r14"]))] + ERSATZ,
    [S("Einer drauf, einer sichert", "Spieler elf hat den Ball. Spieler fünf geht drauf, bis auf einen Meter. Spieler sechs rückt schräg hinter ihn und sichert ab, nicht neben ihn.",
       mv("n5", [30.5, 21]), mv("n6", [25.5, 27.5], delay=0.1)),
     S("Pass rüber, Rollen tauschen", "Der Pass geht rüber zu Spieler sieben. Jetzt drehen sich die Rollen. Spieler sechs geht drauf, und Spieler fünf fällt schräg hinter ihn zurück.",
       ps("b1", fu(POS["r7"])), mv("n6", [30.5, 35.5], delay=0.3), mv("n5", [25.5, 27], delay=0.3)),
     S("Ball zurück, beide rücken raus", "Spieler sieben spielt zurück zu Spieler sechzehn. Beide schieben zusammen raus und bleiben eng beieinander. So geht kein Pass zwischen ihnen durch.",
       ps("b1", fu(POS["r16"])), mv("n5", [28, 23], delay=0.3), mv("n6", [28, 32], delay=0.3))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Gemeinsam das Tor schützen, torseitig und ballseitig.", "Torseitig und ballseitig",
    "Bei einer Flanke steht jeder Verteidiger zwischen seinem Gegenspieler und dem Tor, etwas zur Ballseite hin. So sieht er den Ball und den Gegner zugleich und kann sich nach dem Flug des Balls richten. Verteidiger und Torwart reden die ganze Zeit miteinander. Der erste Kontakt gehört uns.",
    sp(r3=(24, 51)), [B("b2", *fu([24, 51]))] + ERSATZ,
    [S("Läufer kommen, wir bleiben dran", "Spieler drei hat den Ball außen. Drinnen laufen drei Spieler von Team Rot aufs Tor. Spieler fünf und Spieler sechs bleiben zwischen Gegner und Tor. Spieler sechs hat seinen Mann und den Ball gleichzeitig im Blick.",
       mv("r11", [20, 21]), mv("n5", [17, 23.5], delay=0.2), mv("r7", [22.5, 32.5]), mv("n6", [17.5, 31.5], delay=0.2),
       mv("r16", [27, 28], delay=0.3), bl("n6", fu([24, 51]), von=[22.5, 32.5], dauer=1.3, after=True)),
     S("Flanke, erster Kontakt klärt", "Die Flanke kommt flach an den ersten Pfosten. Spieler sechs ist vor Spieler sieben am Ball und klärt mit dem ersten Kontakt weit raus. Torwart und Verteidiger reden dabei die ganze Zeit.",
       ps("b2", fu([17.5, 31.5])), ps("b2", [30, 16], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
