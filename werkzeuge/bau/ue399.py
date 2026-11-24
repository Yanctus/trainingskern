import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 03-P10 (U15-U17, Woche 36 Phase 6): Defend in Defending Third Phase of Play. Ganze Platzbreite und zwei Drittel der Länge,
# 60 x 65 Yards = 55 x 59 m (gerundet 55 x 60 m), 18 Spieler.
# GROSSFELD QUER (Inhaber, 24.11.2026, Vorbild ue319.py): Feld quer wie im Video (dort schon quer), x 7-91 (60 m), y 3-52 (55 m),
# massstab "gross". Großes Tor links (Team Neon verteidigt links), rechts hinter einer gestrichelten Linie die Endzone mit zwei
# Minitoren für den Konter und den zwei Springern in den abgeteilten Ecken. Mittellinie und Mittelkreis an der Stelle wie in
# der PDF-Skizze (bei knapp drei Vierteln der Länge), Strafraum und Torraum nach der Skizze. Nur die Längen-Maßlinie.
# Orange (Video) / Pink (PDF) -> Team Neon im 4-4-0 mit Torwart n1 (Kette 3, 6, 5, 2; Mittelfeld 11, 8, 4, 7 wie im Video).
# Weiß (Video) / dunkel (PDF) -> Team Rot im 1-2-3-1, neu nummeriert (Nummern doppelt): 6 -> 13, 4 -> 16, 8 -> 12, 7 -> 14,
# 11 -> 15; 9 und 10 bleiben. Die zwei Springer (F) sind neutral und helfen Team Rot von hinten (Rückpässe).
# Ein Trainer statt zwei, unten an der Seitenlinie vor der Endzone, spielt die Bälle zu Team Rot ein.
# Grundform nach Video (0:07-0:55): zwei Viererketten verschieben zur Ballseite, früh eng dran („get tight early, force
# backwards“), Pass in die Lücke abgefangen („anticipate pass and cut off passing lines“), Konter aufs Minitor.
# Fassungen: PDF Key Coaching Point (früh eng dran, nach hinten zwingen, dann rückt der Block nach) und Progression
# (Seitenwechsel mit Flanke und Treffer gibt einen Extrapunkt für Team Rot; Ton „sliding across“).
# Sichtkegel: Video „anticipate pass and cut off passing lines“: Spieler vier hat Spieler zehn in der Lücke im Blick, bevor er den
# Pass abfängt (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn). Text und Ton nennen sonst kein Scannen.
# Keine Dublette: UE-319 (08-P14, elf gegen elf auf zwei große Tore), UE-166 (03-P3), UE-098 (03-P6), UE-378 (03-P5),
# UE-400 (03-P9, Dreierkette und zwei Sechser gegen fünf auf einem Drittel).
FX0, FX1, FY0, FY1 = 7, 91, 3, 52
MY = 27.5
T = P("T", "c", 72, 55.3, "T")
ERSATZ = [B("s1", 75.5, 55.8), B("s2", 78, 55.8)]
POS = {"n1": (11, 27.5), "n3": (29, 9), "n6": (26, 21.5), "n5": (26, 34), "n2": (29, 46.5),
       "n11": (44, 9), "n8": (41, 21.5), "n4": (41, 34), "n7": (44, 46.5),
       "r9": (33, 27.5), "r10": (51, 27.5), "r14": (36, 5), "r15": (36, 50), "r16": (60, 13), "r12": (60, 42), "r13": (68, 27.5),
       "f1": (85, 7.5), "f2": (85, 48.5)}
# Stand, nachdem der Block zur Ballseite (unten) geschoben hat
SCHUB = {"n3": (29, 13), "n6": (26, 25), "n5": (26, 37), "n2": (30, 48.5), "n11": (44, 14), "n8": (41, 25.5), "n4": (42, 37), "n7": (49, 43)}
def sp(**k):
    d = dict(POS); d.update(k)
    out = []
    for i, (x, y) in d.items():
        if i[0] == "f": out.append(P(i, "t", x, y, "F"))
        else: out.append(P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]))
    return out + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def schieben(ziel, delay=0.3): return [mv(i, list(p), delay=delay) for i, p in ziel.items()]
MX = 67.5  # Mittellinie (wie in der Skizze)
ZX = 80.4  # Linie zur Endzone
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0), line(MX, FY0, MX, FY1, dashed=False), {"type": "circle", "x": MX, "y": MY, "r": 8},
         rect(FX0, 12, 18.8, 31), rect(FX0, 19.7, 6.8, 15.6), line(ZX, FY0, ZX, FY1), line(ZX, 11, FX1, 11), line(ZX, 45.2, FX1, 45.2)]
TORE = [{"x": FX0, "y": MY, "side": "left", "size": "gross"}, {"x": FX1, "y": 16, "side": "right"}, {"x": FX1, "y": 39, "side": "right"}]
DIMS = dims(FX0, FX1, FY0, FY1, "60 m", "55 m")[:1]

u = {"title": "Zwei Viererketten machen dicht", "code": "UE-399", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 18, "players_max": 18,
 "field_size": "55 x 60 m",
 "description": "Team Neon verteidigt mit Torwart und zwei Viererketten das große Tor, ohne Spitzen. Team Rot greift mit sieben Spielern an, zwei Springer helfen von hinten. Team Neon verschiebt als Block zur Ballseite, geht früh eng an den Gegenspieler und zwingt Team Rot nach hinten. Nach dem Ballgewinn kontert Team Neon auf zwei Minitore.",
 "organisation": ["Aufbauen: Die ganze Platzbreite und zwei Drittel der Länge, 55 mal 60 Meter, mit dem großen Tor. Am anderen Ende ist eine Endzone abgeteilt, dort stehen zwei Minitore, und in den beiden Ecken steht je ein Springer.",
  "Verteilen: Team Neon mit Torwart und zwei Viererketten. Team Rot mit sieben Spielern: einer ganz hinten, zwei davor, drei im Mittelfeld und eine Spitze. Der Trainer steht mit Bällen an der Seitenlinie vor der Endzone.",
  "Ablauf: Der Trainer spielt zu Team Rot, und Team Rot will die beiden Ketten knacken. Team Neon schiebt zur Ballseite, geht früh drauf und macht die Lücken zu. Nach dem Ballgewinn kontert Team Neon auf die Minitore.",
  "Wertung: Ein Treffer ins große Tor gibt einen Punkt für Team Rot, ein Treffer ins Minitor gibt einen Punkt für Team Neon. Danach spielt der Trainer sofort den nächsten Ball zu Team Rot."],
 "organisation_show": ORG,
 "coaching_points": ["Beide Ketten schieben zusammen zur Ballseite", "Früh eng dran, bevor der Ball ankommt", "Zwing ihn nach hinten, dann rückt der Block nach", "Passweg zu, Ball abfangen, sofort nach vorn"],
 "materials": ["1 Großfeldtor", "2 Minitore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zwei Viererketten machen dicht. Team Neon verteidigt mit zwei Viererketten vor dem eigenen Strafraum gegen sieben Angreifer und kontert nach dem Ballgewinn auf zwei Minitore.",
 "board": {"massstab": "gross", "lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 72.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt ein", "Der Trainer spielt Spieler dreizehn an. Team Neon steht in zwei Viererketten vor dem eigenen Strafraum, ganz ohne Spitzen. Hinten in den Ecken warten die beiden Springer.",
     ps("b1", fu(POS["r13"]))),
   S("Raus nach außen, Block schiebt", "Der Ball geht raus zu Spieler zwölf. Beide Ketten schieben zusammen zur Ballseite, und Spieler sieben geht ihm entgegen.",
     ps("b1", fu(POS["r12"])), *schieben(SCHUB)),
   S("Früh eng dran, nach hinten zwingen", "Spieler zwölf spielt auf den Flügel zu Spieler fünfzehn. Spieler zwei läuft schon los, als der Ball noch rollt, und steht ihm eng im Rücken. Spieler fünfzehn kann nicht aufdrehen und muss zurückspielen.",
     ps("b1", fu(POS["r15"])), mv("n2", [33, 47], delay=0.2), ps("b1", fu(POS["r12"]), after=True)),
   S("Pass in die Lücke abgefangen", "Spieler zwölf sucht Spieler zehn in der Lücke zwischen den Ketten. Spieler vier hat ihn im Blick, ahnt den Pass und geht dazwischen. Ball erobert.",
     mv("r10", [51, 32]), bl("n4", [51, 32], delay=0.2), mv("n4", [55, 36.6], delay=0.9), ps("b1", fu([55, 36.6]), delay=1.0)),
   S("Konter aufs Minitor: Punkt", "Jetzt schnell nach vorn. Spieler vier dribbelt in den freien Raum und schießt ins Minitor, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Team Rot.",
     dr("n4", "b1", [70, 36]), ps("b1", [90.5, 39], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Früh eng dran und nach hinten zwingen.", "Früh drauf, Block rückt nach",
    "Der Verteidiger läuft los, während der Pass noch unterwegs ist, und steht eng hinter dem Angreifer. Der kann nicht aufdrehen und muss zurückspielen. Geht der Ball nach hinten, rücken beide Ketten nach vorn und machen den Raum vor dem Strafraum klein.",
    sp(**SCHUB), [B("b1", *fu(POS["r12"]))] + ERSATZ,
    [S("Losgehen, wenn der Ball rollt", "Spieler zwölf spielt raus auf Spieler fünfzehn. Spieler zwei wartet nicht, bis der Ball da ist. Er läuft los, sobald gespielt wird, und steht eng hinter ihm.",
       ps("b1", fu(POS["r15"])), mv("n2", [33, 47], delay=0.1)),
     S("Kein Aufdrehen, Ball zurück", "Spieler fünfzehn will aufdrehen, aber Spieler zwei klebt an ihm. Ihm bleibt nur der Pass zurück zu Spieler zwölf.",
       ps("b1", fu(POS["r12"]))),
     S("Ball nach hinten, Block nach vorn", "Der Ball geht nach hinten, also rückt der ganze Block nach vorn. Beide Ketten schieben ein paar Meter raus, und der Raum vor unserem Strafraum wird klein.",
       *schieben({"n3": (33, 13), "n6": (30, 24.5), "n5": (30, 37), "n2": (34, 46), "n11": (48, 14), "n8": (45, 25.5), "n4": (46, 37), "n7": (53, 43)}, delay=0.1))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Ein schneller Seitenwechsel mit Treffer gibt einen Extrapunkt.", "Seitenwechsel gibt Extrapunkt",
    "Trifft Team Rot nach einem Seitenwechsel und einer Flanke, gibt es einen Extrapunkt. Team Rot sucht deshalb schnell die andere Seite. Team Neon muss im Sprint mit rüberschieben, sonst ist außen alles frei.",
    sp(**SCHUB), [B("b1", *fu(POS["r12"]))] + ERSATZ,
    [S("Schnell auf die andere Seite", "Spieler zwölf spielt zurück zu Spieler dreizehn, und der verlagert sofort zu Spieler sechzehn. Die Viererkette schiebt mit rüber, aber das dauert.",
       ps("b1", fu(POS["r13"])), ps("b1", fu(POS["r16"]), after=True),
       *schieben({"n3": (29, 10), "n6": (26, 22), "n5": (26, 34.5), "n2": (29.5, 46)}, delay=1.0)),
     S("Außen ist Platz", "Spieler vierzehn startet außen in den freien Raum, und Spieler sechzehn spielt ihn an. Spieler drei kommt zu spät.",
       mv("r14", [25, 5]), ps("b1", [25.6, 5.6], delay=0.3), mv("n3", [28.5, 8], delay=0.6)),
     S("Flanke, Treffer: Extrapunkt", "Spieler vierzehn flankt flach an den Fünfer. Spieler neun ist vor seinem Gegenspieler da und schiebt ein, und das gibt einen Punkt und einen Extrapunkt für Team Rot.",
       mv("r9", [18, 30]), mv("n1", [10.5, 23], delay=0.3), ps("b1", [18.6, 30.6], delay=0.4), ps("b1", [7.5, 30], after=True))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
