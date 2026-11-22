import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-117 (U12-U14, Woche 2 Pre-Season): Pass, SAQ and Finish. 50 x 45 Yards am Strafraum, nach der PDF-Skizze: Feld x 10-90, y 5-56,
# Tor oben (Jugendtor, D-Jugend dabei). Gelb -> Neon (8, 9, 10), Pink -> Rot (9 -> 2, 8 -> 3 im Tor, 5). Leitern als drei Minihürden
# auf der Strafraumlinie, Dummys als neongelbe Stangen. Ein Trainer links mit Ersatzbällen.
# Sichtkegel im Video ("Scan to see GK position - finish in space"): vor dem Abschluss schaut der Schütze zum Torwart.
T = P("T", "c", 8, 30, "T")
POS = {"n9": (26, 8), "n10": (17, 8), "n8": (8, 8), "r3": (48.5, 7.5), "r2": (74, 8), "r5": (83, 8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 9.6, 32.6)]
def baelle(**k):
    d = {"b9": (26.6, 9.2), "b10": (17.6, 9.2), "b8": (8.6, 9.2), "b2": (74.6, 9.2), "b5": (83.6, 9.2)}; d.update(k)
    return [B(i, x, y) for i, (x, y) in d.items()] + ERSATZ
LINES = [rect(10, 5, 80, 51), rect(28.6, 5, 42.8, 18), rect(40, 5, 20, 5.8)]
KEGEL = [C(28.9, y, shape="huerde_ou") for y in (19.5, 23, 26.5)] + [C(71.1, y, shape="huerde_ou") for y in (19.5, 23, 26.5)] \
      + [C(37.6, 27.6, "neon", shape="stange"), C(62.4, 27.6, "neon", shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
RAND = [50, 25.5]  # Ball an der Strafraumgrenze
N_WEG = [[28.9, 16], [28.9, 29], [33, 32.5], [41, 32], [47.2, 28.2]]  # links: Leiter runter, um den Dummy, schräg zum Ball
R_WEG = [[71.1, 16], [71.1, 29], [67, 32.5], [59, 32], [52.8, 28.2]]
def weg(who, punkte, **k): return [mv(who, punkte[0], **k)] + [mv(who, p, after=True) for p in punkte[1:]]

u = {"title": "Pass, Leiter, Abschluss", "code": "UE-130", "kind": "Übungsform",
 "focuses": ["Torschuss", "Koordination", "Schnelligkeit"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "46 x 41 m",
 "description": "Zwei Teams spielen vor einem Tor gegeneinander, wer die meisten Tore schießt. Ein Spieler passt seinen Ball an die Strafraumgrenze, läuft durch die Koordinationsleiter, um einen Dummy herum und schießt den Ball direkt aufs Tor. Danach sprintet er sofort ins Tor und ist Torwart für den nächsten Schützen des anderen Teams. So wechseln sich die Teams ab, und jeder ist mal Schütze und mal Torwart.",
 "organisation": ["Aufbauen: Ein Feld von etwa 46 mal 41 Metern um den Strafraum, oben ein Jugendtor. Links und rechts liegt auf der Strafraumlinie je eine Koordinationsleiter, daneben steht je ein Dummy.",
  "Verteilen: Zwei Teams mit je drei Spielern, Team Neon links und Team Rot rechts neben dem Tor, jeder mit einem Ball. Ein Spieler von Team Rot steht zu Beginn im Tor. Der Trainer steht links mit Ersatzbällen.",
  "Ablauf: Der Erste passt seinen Ball an die Strafraumgrenze, läuft durch die Leiter, um den Dummy herum und schließt direkt ab. Dann sprintet er ins Tor und ist der neue Torwart. Der alte Torwart geht zurück zu seinem Team, und der Nächste vom anderen Team startet auf seiner Seite.",
  "Wertung: Jedes Tor ist ein Punkt für das Team. Welches Team hat nach allen Durchgängen die meisten Punkte?"],
 "organisation_show": ORG,
 "coaching_points": ["Schräg anlaufen, damit der Ball direkt geschossen werden kann", "Früh zum Torwart schauen und vor dem Schuss sehen, wo er steht", "Mit Tempo und sauberen Schritten durch die Leiter", "Ruhig abschließen und dann blitzschnell ins Tor wechseln"],
 "materials": ["2 Koordinationsleitern (oder 6 Minihürden)", "2 Dummys", "1 Jugendtor", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pass, Leiter, Abschluss. Erst passen, dann durch die Leiter und um den Dummy, dann direkt aufs Tor, und wer geschossen hat, wird danach selbst Torwart.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": baelle(),
  "steps": [
   S("Pass an die Strafraumgrenze", "Neon neun passt seinen Ball an die Strafraumgrenze. Im Tor steht Rot drei.",
     ps("b9", RAND)),
   S("Leiter und Dummy", "Dann läuft er durch die Leiter, um den Dummy herum und schräg auf den Ball zu.",
     *weg("n9", N_WEG)),
   S("Torwart sehen, Abschluss: Punkt", "Vor dem Schuss schaut er kurz zum Torwart, sieht die freie Ecke und schießt direkt hinein, und das gibt einen Punkt für Team Neon.",
     bl("n9", [48.5, 7.5]), ps("b9", [53.2, 4.7], after=True)),
   S("Ab ins Tor, Rot ist dran", "Neon neun sprintet sofort ins Tor und ist jetzt Torwart. Rot drei geht zurück zu seinem Team, und Rot zwei ist dran: Pass an die Strafraumgrenze, dann durch die rechte Leiter.",
     mv("r3", [92, 15]), mv("n9", [50, 8], delay=0.3), ps("b2", RAND, delay=0.6), *weg("r2", R_WEG[:2], after=True))],
  "dims": dims(10, 90, 5, 56, "46 m", "41 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schräg anlaufen.", "Schräg anlaufen",
    "Wer gerade auf den Ball zuläuft, muss ihn erst stoppen oder ausholen. Wer im leichten Bogen von der Seite anläuft, hat den Körper schon zum Tor gedreht und kann den Ball direkt mit dem ersten Kontakt nehmen.",
    sp(n9=(40, 32.5)), baelle(b9=RAND),
    [S("Im Bogen anlaufen", "Neon neun kommt vom Dummy und läuft im leichten Bogen von der Seite an den Ball.",
       mv("n9", [44.5, 31.5]), mv("n9", [48.4, 27.4], after=True)),
     S("Direkt abschließen: Punkt", "So steht er schon zum Tor gedreht und schießt den Ball direkt ins Eck, und das gibt einen Punkt für Team Neon. Dann sprintet er ins Tor.",
       ps("b9", [53.2, 4.7]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Früh zum Torwart schauen.", "Früh den Torwart sehen",
    "Schon beim Anlaufen hebt der Schütze den Kopf und schaut, wo der Torwart steht. Steht er etwas zu weit auf einer Seite, geht der Schuss ruhig in die andere Ecke. Erst schauen, dann schießen, nicht blind draufhauen.",
    sp(n9=(40, 32.5), r3=(46.5, 7.5)), baelle(b9=RAND),
    [S("Kopf hoch, Torwart sehen", "Beim Anlaufen hebt Neon neun den Kopf und sieht: Rot drei steht im Tor etwas zu weit links.",
       mv("n9", [44.5, 31.5]), bl("n9", [46.5, 7.5], after=True)),
     S("Ins freie Eck: Punkt", "Also schießt er ruhig in die freie rechte Ecke, und das gibt einen Punkt für Team Neon. Dann sprintet er ins Tor, und Team Rot ist dran.",
       mv("n9", [48.4, 27.4]), ps("b9", [53.6, 4.7], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer trifft, bleibt dran.", "Wer trifft, bleibt dran",
    "Trifft der Schütze, darf sein Team gleich noch einmal angreifen, und der Torwart bleibt im Tor. Schießt er daneben, muss er selbst ins Tor, und das andere Team greift an. So lohnt sich ein ruhiger, genauer Abschluss doppelt.",
    sp(n9=(40, 32.5)), baelle(b9=RAND),
    [S("Treffer: Neon bleibt dran", "Neon neun trifft, und das gibt einen Punkt für Team Neon. Weil er getroffen hat, bleibt Rot drei im Tor, und Neon zehn ist sofort dran.",
       mv("n9", [44.5, 31.5]), mv("n9", [48.4, 27.4], after=True), bl("n9", [48.5, 7.5], after=True), ps("b9", [53.2, 4.7], after=True),
       ps("b10", RAND, delay=0.5)),
     S("Neon zehn läuft", "Neon zehn läuft durch die Leiter und um den Dummy herum zum Ball.",
       mv("n9", [8, 20]), mv("n10", [24, 12], delay=0.2), *weg("n10", N_WEG, after=True)),
     S("Daneben: Wechsel", "Neon zehn schießt am Tor vorbei. Jetzt muss er selbst ins Tor, Rot drei geht zurück zu seinem Team, und Team Rot greift an.",
       ps("b10", [61, 3]), mv("r3", [92, 15], after=True), mv("n10", [50, 8], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
