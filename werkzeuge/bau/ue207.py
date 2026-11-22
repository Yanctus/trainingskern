import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-24 (U12-U14, Woche 28 Phase 5): Defensive Reaction Speed Warm Up. 20 x 20 Yards = Feld x 25-75, y 5-55 (18 m).
# Ausrichtung wie im PDF. Pink (unten) -> Team Neon (4, 5, 6, 8), dunkel (oben) -> Team Rot (11, 9, 7, 6). Die 6 gibt es in
# beiden Teams: Rot 6 heißt hier Rot zehn. Unten eine Hürde und eine Leiter (als Reihe aus vier Minihürden), oben dasselbe.
# Wartende stehen neben dem Feld (3D-Abstand). Das rote Tor links -> orange Hütchen, das gelbe Tor rechts -> neon Hütchen;
# der Trainer hat ein oranges und ein gelbes Leibchen. Die beiden treffen sich in der Mitte leicht versetzt (3D-Abstand), der
# Trainer steht oben links statt in der Mitte. Wertung ergänzt: Wer zuerst durch das Tor ist, bekommt einen Punkt (im Original
# ohne Punkte). Kein Sichtkegel im Original (Text, Ton und Video geprüft).
T = P("T", "c", 36, 17, "T")
POS = {"n4": (41, 51), "n5": (20.5, 51), "n6": (12, 51), "n8": (3.5, 51),
       "r11": (59, 9), "r9": (79.5, 9), "r7": (88, 9), "r10": (96.5, 9)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 33, 21), B("s2", 29.5, 21)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(30, 24), C(30, 33.5), C(70, 24, "neon"), C(70, 33.5, "neon"),
         C(47, 51, "neon", shape="huerde"), C(53, 9, "neon", shape="huerde")] \
      + [C(50, y, "neon", shape="huerde_ou") for y in (37, 40, 43, 46)] \
      + [C(50, y, "neon", shape="huerde_ou") for y in (14, 17, 20, 23)]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
UNTEN = [[51, 51], [50, 48.5], [50, 35]]
OBEN = [[49, 9], [50, 11.5], [50, 25]]
MITTE_N, MITTE_R = [46, 31], [54.5, 26.5]

u = {"title": "Hürde, Leiter, Farbsprint", "code": "UE-207", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Schnelligkeit", "Koordination"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 8, "field_size": "18 x 18 m",
 "description": "Ein Aufwärmen für schnelle Füße und schnelle Reaktion. Je ein Spieler aus beiden Teams läuft gleichzeitig über eine Hürde und durch die Leiter. In der Mitte stehen sich beide gegenüber und wippen auf den Zehen. Der Trainer wirft ein Leibchen auf den Boden, und beide sprinten durch das Tor in dieser Farbe.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 18 Metern. Unten und oben je eine Hürde und eine Leiter zur Mitte. Links ein Tor aus orangen Hütchen, rechts eines aus gelben.",
  "Verteilen: Team Neon wartet unten links neben dem Feld, Team Rot oben rechts. Der Trainer steht oben links mit einem orangen und einem gelben Leibchen.",
  "Ablauf: Auf Pfiff starten je einer aus beiden Teams gleichzeitig: schnelle Schritte über die Hürde, dann durch die Leiter. In der Mitte stehen sie sich gegenüber und wippen auf den Zehen. Der Trainer wirft ein Leibchen, und beide sprinten durch das Tor in dieser Farbe.",
  "Wertung und Wechsel: Wer zuerst durch das Tor ist, bekommt einen Punkt für sein Team. Dann stellen sich beide hinten an, und die nächsten zwei starten."],
 "organisation_show": ORG,
 "coaching_points": ["Saubere Technik über Hürde und Leiter", "Schnell reagieren und sofort lossprinten", "Beim Sprint den Körper vor den Gegner schieben", "Konzentriert bleiben und richtig reagieren"],
 "materials": ["4 Hütchen", "2 Hürden", "2 Koordinationsleitern", "2 Leibchen (orange und gelb)"],
 "access": "abo", "hidden": True,
 "say_intro": "Hürde, Leiter, Farbsprint. Zwei Spieler laufen gleichzeitig los und müssen in der Mitte blitzschnell auf das Leibchen reagieren.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": ERSATZ,
  "steps": [
   S("Hürde und Leiter", "Auf Pfiff starten Neon vier und Rot elf gleichzeitig. Beide machen schnelle Schritte über die Hürde und laufen dann mit kleinen, schnellen Schritten durch die Leiter.",
     *weg("n4", UNTEN), *weg("r11", OBEN, delay=0.1)),
   S("In der Mitte wippen", "In der Mitte stehen sich beide gegenüber. Sie wippen auf den Zehen und schauen auf den Trainer, bereit zum Sprint.",
     mv("n4", MITTE_N), mv("r11", MITTE_R)),
   S("Orange: Punkt", "Der Trainer wirft das orange Leibchen. Beide sprinten nach links durch das orange Tor. Neon vier ist schneller und schiebt sich vor Rot elf, und das gibt einen Punkt für Team Neon. Dann stellen sich beide hinten an, und Neon fünf und Rot neun starten.",
     mv("n4", [14, 29.5]), mv("r11", [22.5, 26.5], delay=0.15))],
  "dims": dims(25, 75, 5, 55, "18 m", "18 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Körper vor den Gegner schieben.", "Körper davor",
    "Beim Sprint zum Tor schiebt man sich früh mit dem Körper vor den Gegner. Dann kann er nicht mehr vorbei, auch wenn er genauso schnell ist. Wichtig: nicht schubsen, nur den Weg zumachen.",
    sp(n4=tuple(MITTE_N), r11=tuple(MITTE_R)), ERSATZ,
    [S("Gelb: früh davor", "Der Trainer wirft das gelbe Leibchen. Rot elf steht näher am gelben Tor, sprintet los und schiebt sich sofort vor Neon vier.",
       mv("r11", [64, 27]), mv("n4", [60, 30.5], delay=0.15)),
     S("Durch das Tor: Punkt", "Neon vier kommt nicht mehr vorbei. Rot elf ist zuerst durch das gelbe Tor, und das gibt einen Punkt für Team Rot.",
       mv("r11", [86, 27]), mv("n4", [77.5, 30.5], delay=0.1))]),
  V("Steigerung", "Und jetzt die Steigerung: Durch das andere Tor sprinten.", "Das andere Tor",
    "Jetzt wird es schwerer für den Kopf: Man sprintet durch das Tor mit der anderen Farbe. Fällt das orange Leibchen, geht es durch das gelbe Tor, und umgekehrt. Wer falsch losläuft, verliert Zeit.",
    sp(n4=tuple(MITTE_N), r11=tuple(MITTE_R)), ERSATZ,
    [S("Orange fällt", "Der Trainer wirft das orange Leibchen. Rot elf läuft zuerst nach links, falsch! Neon vier denkt mit und sprintet nach rechts.",
       mv("r11", [47, 22]), mv("n4", [60, 30.5])),
     S("Gelbes Tor: Punkt", "Rot elf dreht um, ist aber zu spät. Neon vier ist zuerst durch das gelbe Tor, und das gibt einen Punkt für Team Neon.",
       mv("n4", [86, 30.5]), mv("r11", [57, 26]), mv("r11", [77.5, 27.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
