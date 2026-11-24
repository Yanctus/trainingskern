import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-50 (U15-U17, Woche 9 Phase 2): Technical Passing Activation, Warm Up. 20 x 30 Yards = 18 x 27 m (gerundet 18 x 25 m).
# FELD QUER (langes Feld, Inhaber 24.11.2026, Vorbild ue317.py): Im PDF hochkant (Start unten, Ende oben), hier quer:
# Start links, Ende rechts. Zwei gespiegelte Runden: PDF blau -> Team Neon (untere Hälfte), pink -> Team Rot (obere Hälfte),
# im PDF ohne Nummern: Neon Start 6, wartend 2, Mitte 8, Ende 10, wartend 4; Rot Start 7, wartend 3, Mitte 9, Ende 11,
# wartend 5. Wartende stehen außerhalb des Felds hinter Start und Ende. Start- und Endspieler stehen weiter außen als im PDF
# (3D-Abstand zur anderen Runde), darum laufen die Wege etwas breiter. Die beiden Hütchen am Startweg aus dem PDF
# weggelassen (sie lagen im Rückpassweg), nur je ein Hütchen in der Mitte an Start und Ende. Ein Trainer statt zwei.
# Nur die Längen-Maßlinie (rechts stehen die Wartenden). Kein Dublette von UE-165 (WU-41: Viereck ohne Stangen) oder
# UE-303/UE-318 (andere Stationen).
# Fassung 1 = PDF Key Coaching Point (rückwärts zwischen die Stangen, früh schauen, offen annehmen, schnell aufdrehen),
# Fassung 2 = PDF Progression (engere Stangen und engeres Hütchentor, eigene Hütchen mit id).
# Sichtkegel: Text "Scan before and after receiving", Ton "scanning early to understand their next action"; im Video nicht
# eingezeichnet. Der Spieler zwischen den Stangen schaut zum Passgeber und nach der Annahme nach vorn (bl mit von, drehen).
T = P("T", "c", 62, 55.3, "T")
ERSATZ = [B("s1", 65.5, 55.8), B("s2", 68, 55.8)]
POS = {"n6": (12, 37), "n2": (3.5, 37), "n8": (45, 41.5), "n10": (86, 36), "n4": (94.5, 36),
       "r7": (12, 18), "r3": (3.5, 18), "r9": (45, 13.5), "r11": (86, 19), "r5": (94.5, 19)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def m(p): return [p[0], round(55 - p[1], 1)]  # Spiegelung für die Runde von Team Rot
LINES = [rect(9, 4, 80, 47), line(9, 27.5, 89, 27.5)]
def geraete(stangen, tor, ids=False):
    pkt = [(16, 27.5, "o"), (83, 27.5, "o")] + [(x, y, "s") for x, y in stangen] + [(x, y, "o") for x, y in tor]
    pkt = pkt + [(x, 55 - y, a) for x, y, a in pkt[2:]]
    out = []
    for i, (x, y, a) in enumerate(pkt):
        c = C(x, y, shape="stange") if a == "s" else C(x, y)
        if ids: c["id"] = f"h{i + 1}"
        out.append(c)
    return out
STANGEN, TOR = [(40, 37), (40, 46), (50, 37.5)], [(63, 38), (72, 38)]
ENG_ST, ENG_TOR = [(40, 38.5), (40, 44.5), (49, 38.5)], [(64.5, 38), (70.5, 38)]
KEGEL = geraete(STANGEN, TOR)
BAELLE = [B("b1", *fuss(POS["n6"])), B("b2", *fuss(POS["r7"]))] + ERSATZ
S0, K = [24, 42], [34, 41.5]  # Start nach dem Andribbeln, kurzer Punkt vor den Stangen
def doppelpass(who, m_, ball, sp_=S0, k=K, delay=None):
    return [dr(who, ball, sp_, delay=delay), mv(m_, k, delay=(delay or 0) + 0.3), ps(ball, fuss(k), after=True), ps(ball, fuss(sp_), after=True)]

u = {"title": "Passrunde mit zwei Doppelpässen", "code": "UE-344", "kind": "Übungsform",
 "focuses": ["Passspiel", "Ballannahme", "Erwärmung"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 10, "players_max": 12,
 "field_size": "18 x 25 m",
 "description": "Ein Aufwärmen mit Ball in zwei gespiegelten Runden aus Stangen und Hütchen. Am Start gibt es einen kurzen Doppelpass, dann geht der Ball durch die Stangen zum Spieler in der Mitte. Der dreht auf, spielt den zweiten Doppelpass durch ein Hütchentor, und der Endspieler bringt den Ball durch die Mitte zurück zum Start. Jeder läuft seinem Pass hinterher.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 25 Metern mit zwei gleichen Runden nebeneinander. In jeder Runde stehen drei Stangen in der Mitte und zwei Hütchen als Tor vor dem Ende.",
  "Verteilen: Pro Runde fünf Spieler, zwei am Start, einer zwischen den Stangen und zwei am Ende. Team Neon arbeitet in der einen Runde, Team Rot in der anderen. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Doppelpass am Start, dann der Pass durch die Stangen. Der Spieler in der Mitte dreht auf und spielt den Doppelpass durch das Hütchentor mit dem Endspieler. Der treibt den Ball durch die Mitte und spielt zurück zum Start. Sobald der Spieler in der Mitte den Ball hat, startet die andere Runde.",
  "Wechsel: Jeder läuft seinem Pass hinterher zur nächsten Station. Nach ein paar Minuten tauschen die Gruppen die Seiten, damit jeder beide Richtungen spielt."],
 "organisation_show": ORG,
 "coaching_points": ["Seitlich zwischen den Stangen stehen und schnell aufdrehen", "Passschärfe und Genauigkeit, jeder Ball sitzt", "Erst zeigen, wenn der Pass kommen kann", "Nach dem Ablegen sofort rückwärts zwischen die Stangen"],
 "materials": ["6 Stangen", "6 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passrunde mit zwei Doppelpässen. Zwei gespiegelte Runden mit Stangen und einem Hütchentor. Der Ball läuft vom Start durch die Stangen, durch das Tor und durch die Mitte zurück, und jeder läuft seinem Pass hinterher.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": BAELLE, "dims": dims(9, 89, 4, 51, "25 m", "18 m")[:1],
  "steps": [
   S("Doppelpass am Start", "Spieler sechs treibt den Ball an. Spieler acht kommt ihm aus den Stangen entgegen und legt direkt zurück.",
     *doppelpass("n6", "n8", "b1")),
   S("Rückwärts zurück, Pass durch die Stangen", "Sofort läuft Spieler acht rückwärts zwischen die Stangen und schaut zum Ball. Spieler sechs spielt flach durch die Stangen zu ihm. Am Start rückt Spieler zwei nach.",
     mv("n8", [45, 41.5]), bl("n8", S0, after=True), ps("b1", [45.6, 42.1], after=True), mv("n2", [12, 37], delay=0.6)),
   S("Aufdrehen, Team Rot startet", "Spieler acht dreht mit dem ersten Kontakt auf und treibt den Ball nach vorn. Genau jetzt startet Team Rot drüben mit dem Doppelpass.",
     bl("n8", [64, 41], von=S0, dauer=1.3), drehen("n8", [64, 41], delay=0.4), dr("n8", "b1", [60, 45], after=True),
     *doppelpass("r7", "r9", "b2", m(S0), m(K), delay=0.5)),
   S("Doppelpass durch das Hütchentor", "Spieler acht spielt zu Spieler zehn und bekommt den Ball zurück. Spieler zehn kommt nach innen, und der dritte Pass geht durch das Hütchentor. Spieler sechs läuft seinem Pass hinterher zwischen die Stangen.",
     ps("b1", fuss(POS["n10"])), mv("n8", [66, 44], delay=0.2), ps("b1", [66.6, 44.6], after=True), mv("n10", [69, 30], after=True),
     ps("b1", [69.6, 30.6], after=True), mv("n6", [45, 41.5], delay=0.3)),
   S("Durch die Mitte zurück zum Start", "Spieler zehn treibt den Ball durch die Mitte und spielt lang zurück zu Spieler zwei. Spieler acht geht ans Ende, Spieler zehn stellt sich am Start an. Jetzt startet Spieler zwei, und drüben läuft bei Team Rot dieselbe Runde.",
     dr("n10", "b1", [56, 31]), ps("b1", fuss(POS["n6"]), after=True), mv("n8", [86, 36], delay=0.3), mv("n10", [4, 30], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Rückwärts zwischen die Stangen und offen annehmen.", "Rückwärts, schauen, aufdrehen",
    "Nach dem Ablegen läuft der Spieler in der Mitte rückwärts zwischen die Stangen, so sieht er den Ball die ganze Zeit. Er schaut früh, was nach der Annahme kommt. Er steht seitlich, nimmt mit dem hinteren Fuß an und dreht mit dem ersten Kontakt auf.",
    sp(n6=S0, n8=K), [B("b1", *fuss(K)), B("b2", *fuss(POS["r7"]))] + ERSATZ,
    [S("Ablegen, sofort rückwärts", "Spieler acht legt ab und läuft sofort rückwärts zwischen die Stangen. Rückwärts, damit er den Ball nie aus den Augen verliert.",
       ps("b1", fuss(S0)), mv("n8", [45, 41.5], delay=0.3)),
     S("Früh schauen, seitlich stehen", "Er steht seitlich und schaut zum Ball. Spieler sechs spielt flach durch die Stangen.",
       bl("n8", S0), ps("b1", [45.6, 42.1], after=True)),
     S("Erster Kontakt dreht auf", "Nach der Annahme geht der Blick sofort nach vorn. Mit dem ersten Kontakt dreht Spieler acht auf und treibt den Ball Richtung Hütchentor.",
       bl("n8", [64, 41], von=S0, dauer=1.3), drehen("n8", [64, 41], delay=0.4), dr("n8", "b1", [60, 45], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Die Stangen und das Hütchentor stehen enger.", "Engere Stangen, engeres Tor",
    "Die Stangen rücken zusammen, und das Hütchentor wird schmaler. Jetzt muss jeder Pass noch genauer kommen, und die Ballkontrolle muss sitzen. Das Tempo bleibt trotzdem hoch.",
    sp(n8=(44.5, 41.5)), BAELLE,
    [S("Doppelpass am Start", "Wieder der kurze Doppelpass am Start. Spieler acht kommt durch die enge Lücke heraus und legt zurück.",
       *doppelpass("n6", "n8", "b1")),
     S("Durch die engen Stangen", "Spieler acht läuft rückwärts zurück und schaut zum Ball. Jetzt muss der Pass durch die schmale Lücke genau passen.",
       mv("n8", [44.5, 41.5]), bl("n8", S0, after=True), ps("b1", [45.1, 42.1], after=True)),
     S("Durch das enge Hütchentor", "Spieler acht dreht auf, treibt den Ball und spielt den Doppelpass mit Spieler zehn. Der letzte Pass geht durch das schmale Tor, und Spieler zehn bringt den Ball zurück zum Start.",
       bl("n8", [64, 41], von=S0, dauer=1.3), drehen("n8", [64, 41], delay=0.4), dr("n8", "b1", [60, 45], after=True),
       ps("b1", fuss(POS["n10"]), after=True), mv("n8", [66, 44], after=True), ps("b1", [66.6, 44.6], after=True),
       mv("n10", [68, 30], after=True), ps("b1", [68.6, 30.6], after=True))],
    cones=geraete(ENG_ST, ENG_TOR, ids=True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
