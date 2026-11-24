import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 44-P8 (U15-U17, Woche 41 Phase 3): 1 v 1 Attack v Defence. 25 x 25 Yards = 23 x 23 m (gerundet 25 x 25 m), Feld x 25-75, y 4-53,
# Tor oben mit neutralem Torwart (Großfeldtor, nur C- und B-Jugend). Nicht gedreht.
# Im PDF/Video läuft Pink (links) als Angreifer unten um die Stange und bekommt den Pass, Blau (rechts) verteidigt über die obere
# Stange; der PDF-Text nennt Blau als Angreifer. Hier: Angreifer = Team Neon auf der linken Seite (Laufwege wie in der Skizze),
# Verteidiger = Team Rot rechts. Neon 4, 5, 6 (Pink 4, 5, 6), Rot 11, 9, 2 (Blau 11, 9, 2), Nummern eindeutig.
# Je Team nur drei Spieler gezeigt (weitere warten im Text), Wartende quer versetzt (3D). Ein Trainer statt zwei (unten mit Bällen).
# Fassungen: Coaching-Punkt = PDF Key Coaching Point (Finte, dann explosiv weg), Steigerung = PDF Progression 2 gegen 2
# (im Video greift dabei Blau an, hier wie in der Grundform Team Neon).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 47, 55.6, "T")
TW = P("k", "t", 50, 7.5, "TW")
POS = {"n4": (19, 33), "n5": (19, 49), "n6": (10.5, 41), "r11": (81, 33), "r9": (81, 49), "r2": (89.5, 41)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [TW, T]
BALLE = [B("b1", 47.6, 56.2), B("s1", 51, 56.3), B("s2", 53.5, 56.3)]
LINES = [rect(25, 4, 50, 49)]
KEGEL = [C(35, 23.5, shape="stange"), C(35, 42, shape="stange"), C(65, 23.5, shape="stange"), C(65, 42, shape="stange"),
         C(31.5, 29), C(31.5, 39), C(68.5, 29), C(68.5, 39), C(25, 34), C(75, 34)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "gross"}]
DIMS = dims(25, 75, 4, 53, "25 m", "25 m", rx=96)
# Wege um die Stangen: Angreifer um die hintere Stange auf seiner Seite, Verteidiger um die vordere auf der anderen Seite
def hinten_links(who, start_delay=None):
    return [mv(who, [33, 47.5], delay=start_delay), mv(who, [38.5, 47], after=True)]
def vorn_rechts(who, ziel, start_delay=None):
    return [mv(who, [67, 18.5], delay=start_delay), mv(who, ziel, after=True)]

u = {"title": "Stangenlauf ins Eins gegen Eins", "code": "UE-414", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Dribbling", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 7, "players_max": 13,
 "field_size": "25 x 25 m",
 "description": "Ein schnelles Eins gegen Eins aufs Tor mit Torwart. Auf Zuruf sprinten ein Angreifer und ein Verteidiger um ihre Stangen, dann spielt der Trainer den Angreifer an. Der will mit Finte und Tempo vorbei und abschließen, der Verteidiger drängt ihn weg und holt sich den Ball. Nach zwei bis drei Angriffen tauschen die Teams die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 25 Metern mit Tor und Torwart. Auf jeder Seite stehen zwei Stangen, eine näher am Tor und eine weiter hinten. Je ein Hütchen auf den Seitenlinien markiert den Start.",
  "Verteilen: Team Neon wartet auf der einen Seite, Team Rot auf der anderen. Der Trainer steht mit vielen Bällen an der Linie gegenüber dem Tor.",
  "Ablauf: Auf Zuruf sprintet der Angreifer von Team Neon um die hintere Stange auf seiner Seite, der Verteidiger von Team Rot um die vordere auf der anderen Seite. Der Trainer spielt den Angreifer an, dann läuft das Eins gegen Eins aufs Tor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Gewinnt der Verteidiger den Ball, darf er selbst aufs Tor gehen. Nach zwei bis drei Angriffen tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Tempo auf den Verteidiger zu", "Finte oder Übersteiger, dann explosiv weg", "Vor dem Torwart ruhig bleiben und platziert abschließen", "Als Verteidiger eine Seite zumachen und wegdrängen"],
 "materials": ["1 Tor", "4 Stangen", "6 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Stangenlauf ins Eins gegen Eins. Erst ein kurzer Sprint um die Stangen, dann das Duell Mann gegen Mann mit Abschluss.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BALLE,
  "steps": [
   S("Auf Zuruf: Sprint um die Stangen", "Der Trainer ruft, und beide sprinten los. Spieler vier läuft um die hintere Stange auf seiner Seite. Spieler elf nimmt drüben die vordere Stange.",
     *hinten_links("n4"), *vorn_rechts("r11", [60, 22])),
   S("Pass vom Trainer", "Jetzt spielt der Trainer Spieler vier an. Der nimmt den Ball mit und geht sofort Richtung Tor. Spieler elf kommt ihm entgegen.",
     ps("b1", [39.1, 47.6]), dr("n4", "b1", [46, 36], after=True), mv("r11", [54, 28], delay=0.6)),
   S("Finte, dann vorbei", "Spieler vier zeigt den Weg nach innen an. Spieler elf geht mit, und genau da zieht Spieler vier zur anderen Seite weg.",
     dr("n4", "b1", [48.5, 34.5]), mv("r11", [55, 31], delay=0.2), dr("n4", "b1", [42, 29], after=True), dr("n4", "b1", [45, 19], after=True)),
   S("Abschluss: Punkt", "Spieler vier schließt flach ins lange Eck ab, und das gibt einen Punkt für Team Neon. Holt sich Spieler elf den Ball, darf er selbst aufs Tor gehen. Danach sind Spieler fünf und Spieler neun dran.",
     ps("b1", [44.5, 4.4]), mv("r11", [48, 22], delay=0.1))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Täuschen und dann explodieren.", "Täuschen und explodieren",
    "Der Angreifer läuft mit Tempo auf den Verteidiger zu. Mit einer Finte, einem Übersteiger oder einer Körpertäuschung bringt er ihn aus dem Gleichgewicht. Dann zieht er explosiv in den freien Raum und schließt ab.",
    sp(n4=(42, 40), r11=(51, 26)), [B("b1", 42.6, 40.6), B("s1", 51, 56.3), B("s2", 53.5, 56.3)],
    [S("Mit Tempo drauf, dann täuschen", "Spieler vier dribbelt mit Tempo auf Spieler elf zu. Kurz vor ihm macht er einen Übersteiger nach innen. Spieler elf verlagert sein Gewicht und geht mit.",
       dr("n4", "b1", [45, 34]), mv("r11", [49, 29], delay=0.2), dr("n4", "b1", [47, 33], after=True), mv("r11", [52, 29.5], after=True)),
     S("Explosiv vorbei: Punkt", "Jetzt explodiert Spieler vier zur anderen Seite und ist vorbei. Er geht allein aufs Tor und trifft, und das gibt einen Punkt für Team Neon.",
       dr("n4", "b1", [41, 27]), dr("n4", "b1", [43, 17], after=True), ps("b1", [44.5, 4.4], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei gegen zwei.", "Zwei gegen zwei",
    "Jetzt sprinten zwei Angreifer und zwei Verteidiger los, je einer um jede Stange. Der Trainer spielt einen der Angreifer an. Die beiden Angreifer kombinieren schnell und kommen mit einem Doppelpass hinter die Verteidiger. Die Verteidiger müssen schnell zurück und sich absprechen.",
    sp(), BALLE,
    [S("Zu zweit um die Stangen", "Auf Zuruf starten auf jeder Seite zwei Spieler. Spieler vier und Spieler fünf laufen um ihre beiden Stangen, drüben machen es Spieler elf und Spieler neun genauso.",
       mv("n4", [31, 18]), mv("n4", [40, 20], after=True), *hinten_links("n5"), *vorn_rechts("r11", [55, 22]),
       mv("r9", [67, 47.5]), mv("r9", [61, 44], after=True)),
     S("Pass vom Trainer", "Der Trainer spielt Spieler fünf an. Er dribbelt an. Spieler neun stellt ihn, und Spieler vier bietet sich vorn an.",
       ps("b1", [39.1, 47.6]), dr("n5", "b1", [45, 40], after=True), mv("r9", [53, 38], delay=0.6), mv("n4", [46, 25], delay=0.6), mv("r11", [53, 20], delay=0.7)),
     S("Doppelpass hinter die Abwehr", "Spieler fünf spielt auf Spieler vier und sprintet sofort an Spieler neun vorbei. Der Ball kommt direkt zurück in seinen Lauf.",
       ps("b1", [46.6, 25.6]), mv("n5", [50, 33], delay=0.2), mv("n5", [58, 28], after=True), mv("r11", [50, 21], delay=0.3), ps("b1", [58.6, 28.6], after=True)),
     S("Abschluss: Punkt", "Spieler fünf ist durch und trifft, und das gibt einen Punkt für Team Neon. Spieler neun kommt zu spät zurück.",
       dr("n5", "b1", [56, 18]), mv("r9", [54, 27], delay=0.2), ps("b1", [55, 4.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
