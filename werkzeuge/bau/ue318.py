import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
import hilfe as h
# WU-49 (U15-U17, Woche 15): Technical Passing Circuit. 15 x 20 Yards = 14 x 18 m. Ein Team (Neon), im PDF ohne Nummern:
# Start 6, Wartender 7, am Dummy 10, Stange eins 8, Stange vorn 9, Stange drei 11. Ein Trainer statt zwei.
# FELD QUER (Inhaber, 24.11.2026, Vorbild ue317.py): Die lange Seite (18 m) liegt waagrecht, Feld x 14-84, y 4-51 (Maßstab
# 3,9 zu 3,4 Einheiten je Meter: fast gleich, so groß wie möglich). Start links, der Ball läuft über die obere Stange nach
# rechts zur vorderen Stange und über die untere Stange zurück. Geplant im Hochformat wie im PDF (x 28-72, y 5-55, Start
# unten); R() legt jede Koordinate quer: unten -> links, oben -> rechts, links -> oben, rechts -> unten. Bälle am Fuß bleiben
# mit Rb() genau bei Spieler + 0.6. Kein Tor, daher beide Maßlinien (unten Länge, rechts Breite).
# Dummy (Mannequin) und die drei Stangen als shape "stange". Starthütchen etwas zur Seite gerückt (Passweg frei).
# Der wartende Spieler sieben steht quer neben dem Start, in der Breite weit genug weg (3D-Abstand).
# Weiterrücken: Jeder läuft nach seiner Aktion eine Station weiter. Texte ohne oben/unten/links/rechts, wo es geht.
# Fassung 1 = PDF Key Coaching Point (außen offen annehmen, mit bl(von=...) und drehen()), Fassung 2 = PDF Progression
# (Lösen vom Dummy, Pass zur Spitze, Steilpass durch die Hütchengasse).
# Kein Sichtkegel im Original (Text, Ton und Video geprüft); der Kegel in Fassung 1 gehört zum Annehmen und Aufdrehen.
FX0, FX1, FY0, FY1 = 14, 84, 4, 51
def R(x, y): return [round(FX0 + (55 - y) / 50 * (FX1 - FX0), 1), round(FY0 + (x - 28) / 44 * (FY1 - FY0), 1)]
def Rb(x, y):  # Ball: Punkt am Fuß (Spieler + 0.6) bleibt quer am Fuß
    p = R(x - 0.6, y - 0.6); return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def P(i, t, x, y, l): return h.P(i, t, *R(x, y), l)
def B(i, x, y): return h.B(i, *Rb(x, y))
def C(x, y, *a, **k): return h.C(*R(x, y), *a, **k)
def mv(who, to, *a, **k): return h.mv(who, R(*to), *a, **k)
def dr(who, ball, to, **k): return h.dr(who, ball, R(*to), **k)
def ps(ball, to, **k): return h.ps(ball, Rb(*to), **k)
def drehen(who, to, **k): return h.drehen(who, R(*to), **k)
def bl(who, to, von=None, **k): return h.bl(who, R(*to), von=R(*von) if von else None, **k)
T = h.P("T", "c", 40, 55.3, "T")  # unten an der Seitenlinie (quer gesetzt)
ERSATZ = [h.B("s1", 43.5, 55.8), h.B("s2", 46, 55.8)]
POS = {"n6": (46, 48), "n7": (61, 51), "n10": (53.5, 31), "n8": (31.5, 22), "n9": (46, 8.5), "n11": (69, 21)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
B7 = B("b2", 61.6, 51.6)
CONES = [C(49.5, 30, shape="stange", id="d"), C(36, 19, shape="stange", id="p1"), C(49.5, 11, shape="stange", id="p2"),
         C(64, 21, shape="stange", id="p3"), C(51, 49.5, id="h0")]
GASSE = [C(58.5, 29, "neon", id="g1"), C(67, 28, "neon", id="g2")]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)]
DIMS = dims(FX0, FX1, FY0, FY1, "18 m", "14 m", rx=FX1 + 8)
def zurueck(**k): return [dr("n11", "b1", [70.5, 28], **k), dr("n11", "b1", [47, 47.5], after=True)]

u = {"title": "Passzirkel um drei Stangen", "code": "UE-318", "kind": "Übungsform",
 "focuses": ["Passspiel", "Erwärmung", "Ballannahme"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 10, "players_min": 6, "players_max": 8,
 "field_size": "14 x 18 m",
 "description": "Ein Passzirkel zum Aufwärmen mit einem Dummy in der Mitte und drei Stangen. Der Ball läuft vom Start über den Dummy auf die eine Seite, mit zwei Doppelpässen um die Stangen nach vorn und auf der anderen Seite wieder raus. Der Letzte dribbelt mit Tempo zurück zum Start. Nach jeder Aktion rückt jeder eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 18 Metern. In der Mitte steht ein Dummy. An beiden Seiten und vorn am anderen Ende steht je eine Stange. Ein Hütchen markiert den Start.",
  "Verteilen: Je ein Spieler steht am Dummy und an den drei Stangen. Die anderen stehen mit Ball am Start. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Doppelpass mit dem Spieler am Dummy, dann raus auf die erste Seite. Ablage nach innen und Doppelpass um die Stange dort. Weiter nach vorn, Doppelpass um die vordere Stange, Pass auf die andere Seite. Der Spieler dort dribbelt außen an der Stange vorbei zurück zum Start.",
  "Wechsel: Jeder rückt nach seiner Aktion eine Station weiter, vom Start zum Dummy, dann auf die erste Seite, nach vorn und auf die andere Seite. Dribbelt der Letzte zurück, startet der Nächste."],
 "organisation_show": ORG,
 "coaching_points": ["Flach und mit Druck passen", "Außen offen stehen und mit Tempo rausgehen", "Doppelpass mit einem Kontakt, genau in den Lauf", "Nach dem Pass sofort nachrücken"],
 "materials": ["1 Dummy", "3 Stangen", "3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Passzirkel um drei Stangen. Zum Aufwärmen läuft der Ball einmal durch alle Stationen, mit zwei Doppelpässen um die Stangen. Der Letzte dribbelt zurück, und jeder rückt eine Station weiter.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 46.6, 48.6), B7] + ERSATZ,
  "dims": DIMS,
  "steps": [
   S("Doppelpass am Dummy", "Spieler sechs startet am Hütchen. Er spielt flach zu Spieler zehn am Dummy, und der lässt den Ball direkt zurückprallen.",
     ps("b1", [54.1, 31.6]), ps("b1", [46.6, 48.6], after=True)),
   S("Raus auf die Seite", "Jetzt geht der Ball raus zu Spieler acht an der Seite. Spieler zehn löst sich schon vom Dummy und kommt ihm entgegen.",
     ps("b1", [32.1, 22.6]), mv("n10", [53, 26], delay=0.3), mv("n10", [46, 23], after=True)),
   S("Doppelpass um die erste Stange", "Spieler acht legt nach innen ab und läuft außen an der Stange vorbei. Spieler zehn spielt ihm den Ball mit einem Kontakt in den Lauf. Spieler sechs rückt vom Start zum Dummy nach.",
     ps("b1", [46.6, 23.6]), mv("n8", [31.5, 16], delay=0.2), mv("n8", [33.5, 13], after=True), ps("b1", [34.1, 13.6], delay=0.9),
     mv("n6", [53.5, 31], delay=0.4)),
   S("Doppelpass um die vordere Stange", "Weiter nach vorn zu Spieler neun. Der legt kurz zurück und dreht um die Stange Richtung Spieler elf. Spieler acht ist nachgelaufen und spielt ihm den Ball wieder in den Lauf.",
     ps("b1", [46.6, 9.1]), mv("n8", [42, 16], delay=0.2), ps("b1", [42.6, 16.6], after=True),
     mv("n9", [52, 6.5], delay=0.9), mv("n9", [57, 12.5], after=True), ps("b1", [57.6, 13.1], delay=1.7), mv("n10", [31.5, 22], delay=0.5)),
   S("Raus zur Seite, mit Ball zurück", "Spieler neun spielt raus zu Spieler elf. Der nimmt den Ball außen an der Stange mit und dribbelt mit Tempo zurück zum Start.",
     ps("b1", [69.6, 21.6]), *zurueck(after=True)),
   S("Weiterrücken, der Nächste startet", "Der Ball ist wieder am Start, die Runde ist durch. Spieler acht rückt nach vorn, Spieler neun auf die andere Seite. Und Spieler sieben ist schon dran. Er startet, sobald Spieler elf losdribbelt.",
     mv("n8", [46, 8.5]), mv("n9", [66, 15]), mv("n9", [69, 21], after=True), ps("b2", [54.1, 31.6], delay=0.3), ps("b2", [61.6, 51.6], after=True))]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Außen offen annehmen und mit Tempo raus.", "Offen annehmen, Tempo raus",
    "Der Spieler an der letzten Stange steht seitlich und schaut zum Ball. Er nimmt den Pass mit dem hinteren Fuß an. So dreht er in einer Bewegung auf und geht mit dem ersten Kontakt Richtung Start.",
    sp(n6=(53.5, 31), n10=(31.5, 22), n8=(42, 16), n9=(57, 12.5)), [B("b1", 57.6, 13.1), B7] + ERSATZ,
    [S("Seitlich stehen, Blick zum Ball", "Spieler elf steht seitlich an der Stange und schaut zu Spieler neun. Der Pass kommt flach auf seinen hinteren Fuß.",
       bl("n11", [57, 12.5]), ps("b1", [69.6, 21.6], after=True)),
     S("Aufdrehen und los", "Erst jetzt dreht er auf, der Blick geht Richtung Start. Der erste Kontakt führt außen an der Stange vorbei, dann zieht er das Tempo an bis zum Starthütchen.",
       bl("n11", [62, 37], von=[57, 12.5], dauer=1.3), drehen("n11", [62, 37], gegen=True, delay=0.4), *zurueck(after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Eine neue Passfolge, und am Ende geht der Ball steil durch die Gasse.", "Steilpass durch die Gasse",
    "Der Ball geht vom Start direkt raus auf die erste Seite. Der Spieler am Dummy täuscht kurz an, löst sich und bekommt die Ablage in der Mitte. Er spielt vor zur Spitze, und von dort kommt der Steilpass durch die Hütchengasse. Der Spieler auf der anderen Seite läuft in den Ball und dribbelt zum Start.",
    sp(), [B("b1", 46.6, 48.6), B7] + ERSATZ,
    [S("Nach außen, antäuschen, Ablage", "Spieler sechs spielt direkt raus zu Spieler acht. Spieler zehn täuscht einen Schritt zum Ball an, geht dann weg vom Dummy nach vorn und bekommt von ihm die Ablage.",
       ps("b1", [32.1, 22.6]), mv("n10", [53.5, 36], delay=0.2), mv("n10", [55, 28], after=True), mv("n10", [50, 22.5], after=True), ps("b1", [50.6, 23.1], delay=1.9)),
     S("Pass zur Spitze", "Vorn kommt Spieler neun um die Stange herum und zeigt sich. Spieler zehn spielt ihn flach an.",
       mv("n9", [52, 6.5]), mv("n9", [56.5, 12.5], after=True), ps("b1", [57.1, 13.1], delay=0.9)),
     S("Steil durch die Gasse", "Jetzt kommt der Steilpass genau zwischen den beiden Hütchen durch. Spieler elf startet außen, läuft in den Ball und dribbelt zurück zum Start. Dann beginnt Spieler sieben.",
       mv("n11", [71, 29]), mv("n11", [66.5, 39.5], after=True), ps("b1", [67.1, 40.1], delay=0.4), dr("n11", "b1", [47, 47.5], after=True))],
    cones=CONES + GASSE)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
