import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-99 (U12-U14, Woche 5 Pre-Season): Shuttle Runs and Attacking the Cross. Halbes Spielfeld nach der PDF-Skizze: Feld x 20-80,
# y 5-57, Tor oben (Jugendtor, D-Jugend dabei) mit neutralem Torwart, vier Hütchen senkrecht für die Pendelläufe.
# Dunkel -> Neon (8, 7, 11, 9), Pink -> Rot (6, 5, 3, 2). Reihen auseinandergezogen (3D-Abstand), ein Trainer links statt zwei.
# Laufwege in den Strafraum so gesetzt, dass die Flanke an keinem Mitspieler vorbeigeht (Kreuzungslauf 9/11 bleibt).
# Sichtkegel aus dem Text ("Head up before delivery from wide"): der Flügelspieler schaut vor der Flanke in den Strafraum.
T = P("T", "c", 12, 33.8, "T")
TW = P("k", "t", 51.2, 7.3, "TW")
POS = {"n9": (45, 51.3), "n11": (36.5, 51.3), "n7": (28, 51.3), "n8": (19.5, 51.3),
       "r6": (54.5, 51.3), "r5": (63, 51.3), "r3": (71.5, 51.3), "r2": (80, 51.3)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
ERSATZ = [B("s1", 10, 37.5), B("s2", 8.5, 31)]
LINES = [rect(20, 5, 60, 52), rect(26.4, 5, 47.1, 17.7), rect(38.1, 5, 24.1, 7.3)]
KEGEL = [C(49.7, y) for y in (32.4, 38.5, 44.5, 51.1)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
def hin_her(who, x, **k): return [mv(who, [x, 40], **k), mv(who, [x, 49], after=True)]

u = {"title": "Pendelsprints und Flanke", "code": "UE-141", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Torschuss", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "Halbes Spielfeld",
 "description": "Zwei Teams zu viert wechseln sich ab. Ein Team macht zuerst Pendelsprints an einer Reihe Hütchen. Danach sprintet ein Spieler auf den Flügel und bekommt vom Trainer den Ball, die anderen drei laufen in den Strafraum, mit Kreuzungsläufen. Der Flügelspieler schaut auf und flankt, und die drei schließen ab. Danach joggen alle zurück, und das andere Team startet.",
 "organisation": ["Aufbauen: Eine halbe Platzhälfte mit Tor und Torwart. Vor dem Strafraum stehen vier Hütchen in einer Reihe für die Pendelsprints.",
  "Verteilen: Zwei Teams zu viert stehen unten links und rechts neben den Hütchen. Der Trainer steht links an der Seitenlinie mit Bällen.",
  "Ablauf: Team Neon macht Pendelsprints zwischen den Hütchen. Dann sprintet einer auf den Flügel und bekommt den Ball vom Trainer, die anderen drei laufen in den Strafraum. Flanke, Abschluss.",
  "Wechsel: Nach dem Angriff joggen alle locker zurück, das startet das andere Team. Jedes Tor ist ein Punkt. Nach einigen Runden gibt es eine Pause."],
 "organisation_show": ORG,
 "coaching_points": ["Jeden Sprint mit vollem Tempo", "Vor der Flanke den Kopf heben und die Läufe im Strafraum sehen", "Im Strafraum gute Läufe machen, zum Beispiel über Kreuz", "Eiskalt abschließen und auf Abpraller lauern"],
 "materials": ["4 Hütchen", "1 Jugendtor", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pendelsprints und Flanke. Erst Sprints an den Hütchen, dann sofort ein Angriff mit Flanke und Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 13.6, 34.4)] + ERSATZ,
  "steps": [
   S("Pendelsprints", "Alle vier von Team Neon sprinten gleichzeitig nach vorn und wieder zurück, so schnell sie können.",
     *hin_her("n9", 45), *hin_her("n11", 36.5), *hin_her("n7", 28), *hin_her("n8", 19.5)),
   S("Auf den Flügel, rein in den Strafraum", "Dann sprintet Spieler acht auf den Flügel, und der Trainer spielt ihm den Ball. Die anderen drei laufen in den Strafraum, Spieler neun und Spieler elf kreuzen dabei.",
     mv("n8", [24.1, 24]), ps("b1", [24.7, 24.6], delay=0.2), mv("n7", [35, 19.5], delay=0.1), mv("n11", [47, 13.5], delay=0.1), mv("n9", [42, 20], delay=0.2)),
   S("Kopf hoch, Flanke", "Spieler acht dribbelt ein Stück nach vorn, hebt den Kopf, sieht Spieler elf am langen Pfosten frei und flankt.",
     dr("n8", "b1", [23.1, 11.9]), bl("n8", [47, 13.5], after=True), ps("b1", [47.6, 14.1], after=True)),
   S("Abschluss: Punkt", "Spieler elf schließt direkt ab und trifft, und das gibt einen Punkt für Team Neon. Dann joggen alle zurück, und Team Rot startet.",
     ps("b1", [46, 4.7]))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kopf hoch vor der Flanke.", "Erst schauen, dann flanken",
    "Wer blind flankt, trifft meistens nur den Torwart oder niemanden. Der Flügelspieler hebt vorher den Kopf und schaut, wer frei ist: kurzer Pfosten, Elfmeterpunkt oder langer Pfosten. Dann flankt er genau dorthin.",
    sp(n8=(23, 12), n7=(33, 17), n9=(43, 21), n11=(60, 17)), [B("b1", 23.6, 12.6)] + ERSATZ,
    [S("Kopf hoch", "Spieler acht hebt den Kopf und schaut in den Strafraum: Spieler neun am Elfmeterpunkt ist gedeckt, Spieler elf am langen Pfosten ist frei.",
       bl("n8", [43, 21]), bl("n8", [60, 17], after=True)),
     S("Zum Freien: Punkt", "Also flankt er an den langen Pfosten. Spieler elf trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", [60.6, 17.6]), ps("b1", [54.5, 4.7], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger kommt dazu.", "Mit Verteidiger",
    "Jetzt verteidigt ein Spieler von Team Rot im Strafraum. Er folgt den Läufen und will die Flanke abfangen. Die Angreifer müssen sich mit Kreuzungsläufen von ihm lösen.",
    sp(n8=(24.1, 24), n7=(28, 40), n11=(36.5, 40), n9=(45, 40), r6=(50, 24)), [B("b1", 24.7, 24.6)] + ERSATZ,
    [S("Läufe, Verteidiger folgt", "Spieler neun läuft zum kurzen Pfosten, und Spieler sechs geht mit. Spieler elf kreuzt hinter ihm zum langen Pfosten, Spieler sieben bleibt hinten am Strafraumrand.",
       mv("n9", [43, 16]), mv("r6", [40, 14], delay=0.2), mv("n11", [58, 17], delay=0.1), mv("n7", [33, 28], delay=0.1)),
     S("Der Freie trifft: Punkt", "Spieler acht hebt den Kopf, sieht Spieler elf frei am langen Pfosten und flankt. Spieler elf trifft, und das gibt einen Punkt für Team Neon.",
       bl("n8", [58, 17]), ps("b1", [58.6, 17.6], after=True), ps("b1", [54.5, 4.7], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
