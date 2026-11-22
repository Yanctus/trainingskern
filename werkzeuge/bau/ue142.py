import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-44 (U12-U14, Woche 6 Pre-Season): Quick Sprints and 2 v 2 Games. 30 x 30 Yards = Feld x 22-72, y 5-55 (27 m), in der Mitte geteilt.
# Rechts die Sprintzone: vier Ecken-Hütchen (leicht nach außen gesetzt, damit die Laufwege frei sind) und ein Dummy in der Mitte.
# Links die Spielzone mit Minitor oben und unten. Blau -> Neon (5, 4, 6, 7), Pink -> Rot (3 -> 9, 5 -> 10, 2 -> 11, 4 -> 12).
# Gezeigt wird die erste Seite des Rundlaufs, der Rest steht im Text. Ein Trainer. Kein Sichtkegel im Original.
T = P("T", "c", 14, 40, "T")
POS = {"n5": (49, 3), "r9": (40.5, 3), "r10": (69, 3), "n4": (77.5, 3), "r11": (49, 57), "n6": (40.5, 57), "n7": (69, 57), "r12": (77.5, 57)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
BAELLE = [B("b1", 15.6, 40.6), B("s1", 12, 44), B("s2", 12, 36)]
LINES = [rect(22, 5, 50, 50), line(46.8, 5, 46.8, 55)]
KEGEL = [C(44.8, 3.2), C(73.2, 3.2), C(44.8, 56.8), C(73.2, 56.8), C(59.4, 27.3, "neon", shape="stange")]
TORE = [{"x": 35, "y": 5, "side": "top"}, {"x": 35, "y": 55, "side": "bottom"}]
P_TL, P_TR, P_BL, P_BR = [51, 7.5], [67, 7.5], [51, 52.5], [67, 52.5]
M_TL, M_TR, M_BL, M_BR = [57.6, 25.8], [61.2, 25.8], [57.6, 28.8], [61.2, 28.8]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]

u = {"title": "Sprint um den Dummy, 2 gegen 2", "code": "UE-142", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Das Feld ist geteilt. Rechts stehen an vier Ecken Spieler, in der Mitte ein Dummy. Auf Pfiff sprinten vier Spieler gleichzeitig zum Dummy und weiter zum nächsten Hütchen gegen den Uhrzeigersinn, bis jeder wieder an seinem Start-Hütchen ist. Dann sprinten alle vier nach links ins Spielfeld, und es wird zwei gegen zwei auf zwei Minitore gespielt. Das Team, das zuerst komplett drin ist, bekommt den Ball.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern, in der Mitte geteilt. Rechts vier Hütchen an den Ecken und ein Dummy in der Mitte, links ein Minitor oben und eins unten.",
  "Verteilen: Zwei Teams. An jeder Ecke steht ein Spieler vorn und einer wartet dahinter, von jedem Team zwei pro Seite. Der Trainer steht links mit Bällen.",
  "Ablauf: Auf Pfiff sprinten die vier Vordersten zum Dummy und weiter zum nächsten Hütchen gegen den Uhrzeigersinn, viermal, bis jeder wieder an seinem Hütchen steht. Dann geht es ins Spielfeld. Der Trainer spielt dem Team den Ball, das zuerst mit beiden Spielern drin ist.",
  "Wertung: Team Neon spielt aufs obere, Team Rot aufs untere Minitor. Jedes Tor ist ein Punkt. Nach einem Tor oder wenn der Ball ins Aus geht, starten die nächsten vier."],
 "organisation_show": ORG,
 "coaching_points": ["Schnelle Sprints zwischen Dummy und Hütchen", "Kurz und scharf wenden", "Mit Tempo ins Spielfeld kommen", "Am Ball ruhig bleiben und sich ohne Ball frei laufen"],
 "materials": ["4 Hütchen", "1 Dummy", "2 Minitore", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Sprint um den Dummy, zwei gegen zwei. Erst ein Rundlauf mit kurzen Sprints, dann sofort ein Spiel zwei gegen zwei.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BAELLE,
  "steps": [
   S("Sprint zum Dummy", "Auf Pfiff sprinten alle vier gleichzeitig zum Dummy, wenden scharf und laufen zum nächsten Hütchen gegen den Uhrzeigersinn.",
     *weg("n5", [M_TL, P_BL]), *weg("r10", [M_TR, P_TL], delay=0.1), *weg("r11", [M_BL, P_BR], delay=0.1), *weg("n7", [M_BR, P_TR])),
   S("Zurück zum Start", "So geht es weiter, viermal zum Dummy und zurück, bis jeder wieder an seinem eigenen Hütchen steht.",
     *weg("n5", [M_BL, P_TL]), *weg("r10", [M_TL, P_TR], delay=0.1), *weg("r11", [M_BR, P_BL], delay=0.1), *weg("n7", [M_TR, P_BR])),
   S("Rüber ins Spielfeld", "Dann sprinten alle vier nach links ins Spielfeld. Team Neon ist zuerst mit beiden Spielern drin, darum spielt der Trainer Neon fünf den Ball.",
     mv("n5", [38, 22]), mv("n7", [43, 14], delay=0.1), mv("r10", [30, 24], delay=0.5), mv("r11", [34, 40], delay=0.5), ps("b1", [38.6, 22.6], delay=0.8)),
   S("Zwei gegen zwei: Punkt", "Neon fünf spielt zu Neon sieben, der ins obere Minitor trifft, und das gibt einen Punkt für Team Neon. Dann starten die nächsten vier.",
     ps("b1", [43.6, 14.6]), mv("r10", [36, 18], delay=0.1), ps("b1", [35, 4.7], after=True))],
  "dims": [{"x1": 86, "y1": 5, "x2": 86, "y2": 55, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kurz und scharf wenden.", "Scharf wenden",
    "Am Dummy und am Hütchen nicht im weiten Bogen herumlaufen. Kurz vorher mit kleinen Schritten abbremsen, tief gehen und sofort in die neue Richtung abdrücken. So verliert man kaum Zeit.",
    sp(), BAELLE,
    [S("Abbremsen am Dummy", "Neon fünf sprintet zum Dummy, bremst mit kleinen Schritten ab und wendet scharf.",
       mv("n5", M_TL)),
     S("Sofort weiter", "Dann drückt er sich ab und sprintet ohne Umweg zum nächsten Hütchen.",
       mv("n5", P_BL))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Wer zuerst drin ist, hat den Ball.", "Schneller drin",
    "Das Team, das zuerst mit beiden Spielern im Spielfeld steht, bekommt den Ball. Wer nach dem Rundlauf trödelt, verschenkt den Ballbesitz.",
    sp(n5=P_TL, r10=P_TR, r11=P_BL, n7=P_BR), BAELLE,
    [S("Rot ist schneller drin", "Diesmal sind Rot zehn und Rot elf zuerst im Spielfeld, Team Neon kommt zu spät.",
       mv("r10", [36, 30]), mv("r11", [30, 42]), mv("n5", [40, 20], delay=0.6), mv("n7", [42, 38], delay=0.6)),
     S("Rot hat den Ball: Punkt", "Darum spielt der Trainer Team Rot den Ball. Rot zehn legt zu Rot elf, der ins untere Minitor trifft, und das gibt einen Punkt für Team Rot. Dann starten die nächsten vier.",
       ps("b1", [36.6, 30.6]), ps("b1", [30.6, 42.6], after=True), ps("b1", [34.6, 55.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
