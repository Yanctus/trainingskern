import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-65 (U15-U17, Woche 6 Pre-Season): Acceleration Sprints and Race to Finish (PDF: Quick Sprints and Race to Finish).
# 30 x 35 Yards = 27 x 32 m (gerundet 25 x 30 m), Feld x 29-71, y 5-55, Tor oben wie im PDF (nicht gedreht).
# Großfeldtor mit neutralem Torwart (PDF grün 1, nur C- und B-Jugend). PDF pink -> Team Neon (9, 4, 7, 10 wie im PDF),
# blau -> Team Rot, neu nummeriert, weil die Nummern doppelt sind: 9 -> 6, 8 -> 8, 7 -> 5, 10 -> 11 (nicht 1 bis 4, damit
# "Spieler" und "Hütchen" im Sprechtext nicht verwechselt werden). Hütchenfarbe orange statt gelb, Hütchennummern nur im Text.
# Ein Trainer statt zwei (oben links, er ruft die Zahlen). Wartende neben dem Feld in einer Reihe untereinander (3D-Abstand).
# Gelaufen wird an der Innenseite der Hütchenreihen (Hand ans Hütchen), hoch und runter leicht versetzt.
# Grundform: Zahlenfolge "zwei, vier, eins" wie in der PDF-Skizze. Fassung 1 = Key Coaching Point 1 (Körper dazwischen,
# Folge "zwei, eins, drei" wie in PDF 2). Fassung 2 = Key Coaching Point 2 (Verteidiger erobert den Ball und wird Stürmer),
# mit Stange in der Folge ("vier, zwei, Stange" wie im Video).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 21, 8, "T")
ERSATZ = [B("s1", 24.5, 9), B("s2", 24.5, 11.5)]
TW = P("k", "t", 50, 8.5, "TW")
WARTE = {"n9": (12, 24), "n4": (12, 40), "n7": (12, 55.5), "r8": (88, 24), "r5": (88, 40), "r11": (88, 55.5)}
START = {"n10": (44.5, 52.5), "r6": (55.5, 52.5)}
def sp(**k):
    d = dict(START); d.update(WARTE); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
HY = {1: 45.5, 2: 39.5, 3: 33, 4: 27.5}
NX, RX = 41.5, 58.5  # Hütchenreihen
LINES = [rect(29, 5, 42, 50)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}]
CONES = [C(NX, y) for y in HY.values()] + [C(RX, y) for y in HY.values()] + [C(42, 55), C(58, 55)] \
    + [C(31.5, 21, shape="stange"), C(68.5, 21, shape="stange")]
BALL = [50, 21]
DIMS = dims(29, 71, 5, 55, "25 m", "30 m", rx=79)
def n(z, hoch=True): return [44.5 if hoch else 45.5, HY[z]]
def r(z, hoch=True): return [55.5 if hoch else 54.5, HY[z]]
def folge(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Zahlen hören, Wettlauf zum Ball", "code": "UE-335", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "1 gegen 1", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 9, "players_max": 11,
 "field_size": "25 x 30 m",
 "description": "Der Trainer ruft eine Zahlenfolge, zum Beispiel zwei, vier, eins. Je ein Spieler aus jedem Team sprintet los und tippt die Hütchen in genau dieser Reihenfolge mit der Hand an. Danach geht es im Wettlauf zum Ball in der Mitte. Wer zuerst dran ist, schließt aufs Tor ab, der andere wird zum Verteidiger.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit großem Tor und Torwart. Für jedes Team eine Reihe mit vier Hütchen, von eins bis vier gezählt, dazu ein Starthütchen und eine Stange an der Seite. In der Mitte vor dem Tor liegt ein Ball.",
  "Verteilen: Zwei Teams zu viert. Je einer steht am Starthütchen, die anderen warten neben dem Feld. Der Trainer steht oben am Rand mit Bällen.",
  "Ablauf: Der Trainer ruft eine Folge aus Zahlen, manchmal auch die Stange. Beide sprinten los und tippen die Hütchen in dieser Reihenfolge mit der Hand an. Dann Wettlauf zum Ball. Der Erste greift an, der Zweite verteidigt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team. Erobert der Verteidiger den Ball, darf er selbst aufs Tor schießen. Danach legt der Trainer einen neuen Ball in die Mitte, und die Nächsten sind dran."],
 "organisation_show": ORG,
 "coaching_points": ["Genau hinhören, dann sofort los", "Hand ans Hütchen, kurz abbremsen und explosiv wieder an", "Als Erster am Ball den Körper zwischen Gegner und Ball", "Mit zwei Kontakten abschließen, flach ins Eck"],
 "materials": ["1 großes Tor", "10 Hütchen", "2 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zahlen hören, Wettlauf zum Ball. Der Trainer ruft eine Zahlenfolge, zwei Spieler sprinten die Hütchen ab, und wer zuerst am Ball ist, schließt ab.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", *BALL)] + ERSATZ,
  "steps": [
   S("Der Trainer ruft: zwei, vier, eins", "Der Trainer ruft: zwei, vier, eins. Spieler zehn und Spieler sechs sprinten gleichzeitig los. Zuerst zum Hütchen zwei, und die Hand geht ans Hütchen.",
     mv("n10", n(2)), mv("r6", r(2))),
   S("Hoch zur Vier, runter zur Eins", "Weiter hoch zur Vier, abbremsen, antippen. Dann wieder runter zur Eins. Spieler sechs ist einen Schritt langsamer.",
     *folge("n10", [n(4), n(1, False)]), *folge("r6", [r(4), r(1, False)], delay=0.3)),
   S("Wettlauf zum Ball", "Jetzt geht es im Sprint zum Ball. Spieler zehn ist als Erster dran, Spieler sechs kommt von der Seite und wird zum Verteidiger.",
     mv("n10", [49.4, 20.4]), mv("r6", [54, 25.5], delay=0.3)),
   S("Zwei Kontakte: Punkt", "Spieler zehn schirmt den Ball ab, legt ihn sich mit dem ersten Kontakt vor und schießt mit dem zweiten flach ins Eck. Das gibt einen Punkt für Team Neon. Jetzt sind Spieler neun und Spieler acht dran.",
     dr("n10", "b1", [48, 13]), mv("r6", [51.5, 16.5], delay=0.2), ps("b1", [45.5, 5.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Körper dazwischen.", "Körper dazwischen",
    "Wer zuerst am Ball ist, stellt sofort den Körper zwischen Gegner und Ball. So läuft der Verteidiger in ihn hinein und kommt nicht vorbei. Erst wenn der Ball sicher ist, geht es zum Abschluss.",
    sp(), [B("b1", *BALL)] + ERSATZ,
    [S("Zwei, eins, drei", "Diesmal ruft der Trainer: zwei, eins, drei. Beide tippen die Hütchen ab, Spieler zehn ist knapp vorn.",
       *folge("n10", [n(2), n(1, False), n(3)]), *folge("r6", [r(2), r(1, False), r(3)], delay=0.2)),
     S("Erster am Ball, Körper rein", "Spieler zehn ist zuerst am Ball. Sofort schiebt er den Körper in den Laufweg von Spieler sechs. Der kommt nicht vorbei.",
       mv("n10", [49.4, 20.4]), mv("r6", [54, 24], delay=0.2), dr("n10", "b1", [51, 21.5], after=True), mv("r6", [55, 22.5], after=True)),
     S("Abschluss: Punkt", "Der Ball ist sicher. Spieler zehn nimmt ihn mit und schießt mit dem zweiten Kontakt ins lange Eck. Das gibt einen Punkt für Team Neon.",
       dr("n10", "b1", [48.5, 13]), mv("r6", [53, 16], delay=0.2), ps("b1", [45.5, 5.3], after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ball erobert, sofort abschließen.", "Erobern, dann abschließen",
    "Der Zweite gibt nicht auf. Er setzt den Angreifer sofort unter Druck. Springt der Ball weg und er erobert ihn, wird er selbst zum Stürmer und schließt sofort ab.",
    sp(), [B("b1", *BALL)] + ERSATZ,
    [S("Vier, zwei, Stange", "Der Trainer ruft: vier, zwei, Stange. Beide tippen die Hütchen an und laufen dann außen zu ihrer Stange.",
       *folge("n10", [n(4), n(2, False), [44.5, 24], [33.5, 21.5]]), *folge("r6", [r(4), r(2, False), [55.5, 24], [66.5, 21.5]], delay=0.1)),
     S("Wettlauf, Spieler zehn vorn", "Von der Stange geht es in die Mitte. Spieler zehn ist zuerst am Ball, Spieler sechs geht sofort drauf.",
       mv("n10", [49.4, 20.4]), mv("r6", [55, 21.5], delay=0.2)),
     S("Ball erobert, er wird Stürmer", "Spieler zehn legt sich den Ball zu weit vor. Spieler sechs geht dazwischen, erobert den Ball und zieht sofort Richtung Tor davon.",
       dr("n10", "b1", [48.5, 16]), mv("r6", [51, 16], delay=0.3), dr("r6", "b1", [53, 11.5], after=True), mv("n10", [49, 13.5], after=True)),
     S("Abschluss: Punkt", "Spieler sechs schießt flach ins Eck, und das gibt einen Punkt für Team Rot. Jetzt sind Spieler neun und Spieler acht dran.",
       ps("b1", [55, 5.3]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
