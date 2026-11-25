import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 03-P5 (U15-U17, Woche 28 Phase 5): Defend The Defending Third Opposed Skill (How to defend centrally as a pair).
# Feld nach der PDF-Skizze 45 x 50 Yards = 41 x 46 m (gerundet 40 x 45 m); der Text nennt 30 x 30 Yards. Kein Großfeld, kein
# langes Feld: hochkant, x 29-71, y 5-52. Ausrichtung wie im PDF (großes Tor oben, zwei Minitore unten an der Grundlinie,
# Trainer mit Bällen dazwischen unten). Großfeldtor mit Torwart (nur C- und B-Jugend).
# Pink -> Team Neon (Torwart n1, aktive Verteidiger 4 und 5, wartende 3 und 2 mit Ball neben dem Tor), Blau -> Team Rot
# (aktive Angreifer 9 und 10, wartende 7 und 11 neben dem Feld statt dahinter, wegen 3D). Nummern wie im PDF (eindeutig).
# Die wartenden Verteidiger 3 und 2 stehen neben dem Feld auf Höhe des Torraums statt neben dem Tor (dort kein Platz auf der Tafel).
# Ein Trainer. Die vier roten Markierungshütchen als orange Hütchen, leicht versetzt (Laufwege).
# Grundform nach PDF und Video (0:05-0:25): Spieler fünf spielt auf Spieler neun, einer presst erst, wenn der andere sichert,
# Angreifer nach außen drängen, Ballgewinn und Konter aufs Minitor. Wertung für Team Rot (Treffer ins große Tor) ergänzt.
# Fassungen = PDF Progression 1 (drei gegen zwei, dritter Angreifer kommt mit Ball von außen) und Progression 2 (Spieler zwei
# kommt nach zehn Sekunden dazu, drei gegen drei). Die Wechsel-Reihenfolge (nächstes Paar) aus „rotation“ abgeleitet.
# Sichtkegel: Text „Awareness from defenders …“, im Video kein Kegel eingezeichnet; Richtung aus dem Sinn: Spieler zwei schaut
# beim Reinkommen zum freien Spieler zehn (Steigerung 2), fängt dann ab und dribbelt. Die Kegel beim sichernden Spieler fünf
# (Grundform, Steigerung 1) sind gestrichen (Regel vom 25.11.2026: kein Kegel bei Verteidigern, die nur beobachten).
# Keine Dublette: UE-098 (03-P6, vier gegen vier auf zwei Tore), UE-166 (03-P3, Viererkette), UE-115 (19-P2, Hütchentore).
T = P("T", "c", 50, 55.3, "T")
ERSATZ = [B("s1", 53.5, 55.8), B("s2", 56, 55.8)]
POS = {"n1": (50, 8.5), "n4": (40, 20.5), "n5": (59, 19), "n3": (24, 8), "n2": (76, 8),
       "r9": (35, 44.5), "r10": (65, 44.5), "r7": (22, 49), "r11": (77.5, 49)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:]) for i, (x, y) in d.items()] + [T]
WARTE = [B("b3", 24.6, 8.6), B("b2", 76.6, 8.6)]
LINES = [rect(29, 5, 42, 47), rect(34.8, 5, 30.4, 14.3), rect(41.4, 5, 17.2, 5.5)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 40, "y": 52, "side": "bottom"}, {"x": 60, "y": 52, "side": "bottom"}]
CONES = [C(36.5, 18), C(63.5, 17), C(31.5, 41), C(68.5, 41)]
DIMS = dims(29, 71, 5, 52, "40 m", "45 m", rx=86)

u = {"title": "Zentral als Paar verteidigen", "code": "UE-378", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 9, "players_max": 12,
 "field_size": "40 x 45 m",
 "description": "Zwei Verteidiger und ein Torwart verteidigen das große Tor gegen zwei Angreifer. Die beiden Verteidiger arbeiten als Paar: Einer geht ran, der andere sichert schräg dahinter. Sie drängen den Ballführer nach außen auf seinen schwachen Fuß. Erobern sie den Ball, kontern sie auf zwei Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 40 mal 45 Metern mit Strafraum und großem Tor oben. Unten an der Grundlinie stehen zwei Minitore, vier Hütchen markieren die Startplätze.",
  "Verteilen: Team Neon mit Torwart und zwei Verteidigern im Feld, zwei weitere warten mit Ball außen auf Höhe des Tores. Team Rot mit zwei Angreifern im Feld, zwei warten außen. Der Trainer steht mit Bällen zwischen den Minitoren.",
  "Ablauf: Ein Verteidiger spielt den Ball weit zu einem Angreifer. Zwei gegen zwei aufs große Tor. Erobert Team Neon den Ball, kontert es auf die Minitore. Geht der Ball ins Aus, spielt der Trainer sofort einen neuen ein.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Rot, ein Treffer ins Minitor einen Punkt für Team Neon. Nach jedem Angriff kommt das nächste Paar, so bekommt jeder seine Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Auf den schwachen Fuß lenken", "Erst ran, wenn der Partner sichert", "Nach außen drängen, weg vom Tor", "Neuer Ball vom Trainer? Sofort wieder bereit"],
 "materials": ["1 Großfeldtor", "2 Minitore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Zentral als Paar verteidigen. Zwei Verteidiger und der Torwart gegen zwei Angreifer vor dem großen Tor. Die zwei arbeiten zusammen, und nach dem Ballgewinn geht es sofort auf die Minitore.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 59.6, 19.6)] + WARTE + ERSATZ,
  "steps": [
   S("Spieler fünf spielt auf", "Spieler fünf spielt den Ball weit zu Spieler neun. Sofort rücken beide Verteidiger raus. Vorn zieht Spieler zehn in die Mitte.",
     ps("b1", [35.6, 45.1]), mv("n4", [39, 30], delay=0.6), mv("n5", [52, 27], delay=0.6), mv("r10", [58, 38], delay=0.6)),
   S("Erst sichern, dann ran", "Spieler neun dribbelt an. Spieler vier wartet noch. Erst steht Spieler fünf schräg hinter ihm und sichert gegen Spieler zehn, dann geht Spieler vier ran.",
     dr("r9", "b1", [38.5, 38]), mv("n5", [46, 29], delay=0.2), mv("n4", [38.5, 32.5], after=True)),
   S("Nach außen drängen", "Spieler vier steht innen und drängt ihn nach außen, auf den schwachen Fuß. Der Winkel zum Tor wird immer kleiner. Spieler zehn sucht eine Lücke in der Mitte.",
     dr("r9", "b1", [32.5, 33.5]), mv("n4", [35.5, 29.5], delay=0.2), mv("r10", [52, 33.5], delay=0.4)),
   S("Abgefangen, ab ins Minitor: Punkt", "Spieler neun will nach innen zu Spieler zehn. Spieler fünf ahnt das und geht dazwischen. Er dribbelt los und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Danach verteidigen Spieler drei und Spieler zwei, und Spieler sieben und Spieler elf greifen an.",
     mv("n5", [44.5, 32]), ps("b1", [45.1, 32.6], delay=0.3), dr("n5", "b1", [42, 44], after=True), ps("b1", [40, 51.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein dritter Angreifer kommt dazu.", "Drei gegen zwei",
    "Der Trainer spielt einen dritten Angreifer an, der von außen ins Feld dribbelt. Jetzt sind es drei gegen zwei. Die Verteidiger müssen schnell umschalten und den Angriff verzögern, bis der Torwart helfen kann. Wer den Ball erobert, kontert sofort.",
    sp(n4=(41, 22), n5=(58.5, 21), r9=(68, 32), r10=(50, 37)), [B("b1", 50.6, 55.9)] + WARTE + ERSATZ,
    [S("Dritter Angreifer kommt", "Spieler sieben läuft ins Feld. Der Trainer spielt ihn an, und er dribbelt direkt aufs Tor zu. Jetzt sind es drei gegen zwei.",
       mv("r7", [34, 47]), ps("b1", [34.6, 47.6], after=True), dr("r7", "b1", [36, 38], after=True)),
     S("Umschalten und verzögern", "Spieler vier schaltet sofort um und stellt Spieler sieben. Spieler fünf rückt in die Mitte und hält die anderen zwei hin, auch Spieler neun in seinem Rücken.",
       mv("n4", [37, 31]), mv("n5", [54, 27], delay=0.2)),
     S("Torwart fängt, schnell raus: Punkt", "Spieler sieben spielt quer zu Spieler zehn, und der schießt sofort. Der Torwart fängt den Ball und wirft ihn gleich zu Spieler vier. Der dribbelt los und trifft ins Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [50.6, 37.6]), ps("b1", [50.6, 9.1], after=True), ps("b1", [37.6, 31.6], after=True),
       dr("n4", "b1", [43, 40], after=True), ps("b1", [40, 51.5], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Nach zehn Sekunden kommt ein dritter Verteidiger.", "Drei gegen drei",
    "Team Rot greift mit drei Spielern an. Halten die zwei Verteidiger zehn Sekunden lang dicht, sprintet ein dritter Verteidiger ins Feld. Jetzt steht es drei gegen drei, und Team Rot muss schneller entscheiden.",
    sp(n4=(40, 22), n5=(56, 24.5), r9=(65, 33), r10=(47, 38), r7=(32, 38)), [B("b1", 65.6, 33.6)] + WARTE + ERSATZ,
    [S("Zehn Sekunden dicht halten", "Team Rot lässt den Ball laufen, von Spieler neun zu Spieler zehn und weiter zu Spieler sieben. Spieler vier und Spieler fünf schieben mit und lassen nichts durch. Die zehn Sekunden sind um.",
       ps("b1", [47.6, 38.6]), mv("n5", [50.5, 27.5], delay=0.3), ps("b1", [32.6, 38.6], after=True), mv("n4", [36, 30], after=True)),
     S("Spieler zwei kommt dazu", "Jetzt darf Spieler zwei rein. Er sprintet sofort ins Feld und schaut, wer frei ist. Spieler zehn, den übernimmt er.",
       mv("n2", [61, 13]), mv("n2", [58, 22], after=True), bl("n2", [47, 38], after=True)),
     S("Drei gegen drei: Punkt", "Spieler sieben will zu Spieler zehn passen. Spieler zwei ist schon da und fängt den Ball ab. Er dribbelt los und trifft ins Minitor, und das gibt einen Punkt für Team Neon. Danach ist das nächste Paar dran.",
       mv("n2", [53, 31]), ps("b1", [53.6, 31.6], delay=0.3), dr("n2", "b1", [58, 43], after=True), ps("b1", [60, 51.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
