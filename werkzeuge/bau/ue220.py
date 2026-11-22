import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 59-P8 (U12-U14, Woche 32 Phase 4): Quick Transitions (Wave of Play). 30 x 30 Yards = Feld x 20-80, y 4-52 (27 m), gedreht:
# im PDF liegt das Tor rechts, hier oben (Jugendtor mit neutralem Torwart). Strafraum x 33-67, y 4-12.4, Querlinie gestrichelt bei
# y 33. Halbkreis weggelassen. Pink (erst Abschluss, dann Verteidiger) -> Team Rot (11, 9), Gold (Angreifer der zweiten Welle)
# -> Team Neon (4, 8), Floater -> Springer F. Ein Trainer statt zwei, unten neben dem Feld.
# Sichtkegel aus Text und Ton ("Recognise triggers to press ... poor touch or bad pass"): im Coaching-Punkt schaut Spieler neun
# auf die Ballannahme von Spieler acht. Im Video sind nur Markierungen um Ball und Spieler, kein Kegel.
T = P("T", "c", 50, 55.5, "T")
K = P("k", "t", 50, 8, "TW")
POS = {"r11": (32, 35), "r9": (61, 36.5), "n4": (31, 53.5), "n8": (66, 54)}
FX = (48.5, 31)
def sp(f=FX, **k):
    d = dict(POS); d.update(k)
    return [K] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("f1", "t", f[0], f[1], "F"), T]
BAELLE = [B("b1", 46.4, 57.1), B("b2", 53.8, 57.1), B("b3", 50.6, 56.1)]
LINES = [rect(20, 4, 60, 48), rect(33, 4, 34, 8.4), line(20, 33, 80, 33)]
TORE = [{"x": 50, "y": 4, "side": "top", "size": "jugend"}]

u = {"title": "Erst treffen, dann verteidigen", "code": "UE-220", "kind": "Spielform",
 "focuses": ["Umschalten", "Verteidigen", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Zwei Spieler von Team Rot bekommen nacheinander einen Ball und schießen allein gegen den Torwart. Danach schalten beide sofort um und verteidigen gegen zwei Spieler von Team Neon und einen Springer. Die zwei Verteidiger stehen kompakt, drängen die Angreifer nach außen und pressen bei einem schlechten Ballkontakt. Dann tauschen die Teams die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern vor einem Jugendtor mit Strafraum. Eine gestrichelte Querlinie teilt das Feld.",
  "Verteilen: Zwei Spieler von Team Rot und ein Springer stehen im Feld, zwei Spieler von Team Neon warten unten an der Linie. Ein neutraler Torwart steht im Tor. Der Trainer steht unten mit Bällen.",
  "Ablauf: Der Trainer passt nacheinander zu den beiden Roten, und jeder schießt allein gegen den Torwart. Dann passt er zu Team Neon, und die zwei Neon-Spieler greifen mit dem Springer drei gegen zwei an. Die beiden Roten schalten sofort um und verteidigen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team des Schützen. Nach dem Angriff tauschen die Teams die Rollen: Jetzt schießt Team Neon zuerst und verteidigt danach. Das Team mit den meisten Punkten gewinnt."],
 "organisation_show": ORG,
 "coaching_points": ["Nach dem Schuss sofort umschalten und zurücklaufen", "Kompakt stehen und die Angreifer nach außen drängen", "Bei schlechter Annahme oder schlechtem Pass sofort pressen", "Im Strafraum eng dran sein und Schüsse blocken"],
 "materials": ["1 Jugendtor", "Viele Bälle", "Leibchen in zwei Farben", "1 Leibchen für den Springer"],
 "access": "abo", "hidden": True,
 "say_intro": "Erst treffen, dann verteidigen. Zwei Spieler schießen aufs Tor und müssen danach sofort gegen drei Angreifer verteidigen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": BAELLE,
  "steps": [
   S("Erster Abschluss: Punkt", "Der Trainer passt zu Spieler elf. Er nimmt den Ball mit und schießt allein gegen den Torwart. Trifft er, gibt das einen Punkt für Team Rot.",
     ps("b1", [32.6, 35.6]), dr("r11", "b1", [40, 20], after=True), ps("b1", [46, 4.6], after=True)),
   S("Zweiter Abschluss: Punkt", "Gleich danach passt der Trainer zu Spieler neun. Auch er schießt allein gegen den Torwart, und ein Treffer gibt einen Punkt für Team Rot.",
     ps("b2", [61.6, 37.1]), dr("r9", "b2", [58, 20], after=True), ps("b2", [54, 4.6], after=True)),
   S("Umschalten", "Jetzt passt der Trainer zu Spieler acht, und Team Neon greift mit dem Springer an. Spieler elf und Spieler neun sprinten sofort zurück und verteidigen. Spieler vier läuft nach vorn.",
     ps("b3", [62.6, 46.6]), mv("n8", [62, 46]), mv("r11", [42, 42], delay=0.3), mv("r9", [58, 36], delay=0.3), mv("n4", [32, 40], delay=0.3)),
   S("Drei gegen zwei: Punkt", "Spieler acht spielt zum Springer, und der Springer spielt zum freien Spieler vier. Spieler vier dribbelt in den Strafraum und trifft. Das gibt einen Punkt für Team Neon. Dann tauschen die Teams die Rollen: Jetzt schießt Team Neon zuerst und verteidigt danach.",
     ps("b3", [49.1, 31.6]), ps("b3", [32.6, 40.6], after=True), dr("n4", "b3", [37, 20], after=True), ps("b3", [47, 4.6], after=True))],
  "dims": dims(20, 80, 4, 52, "27 m", "27 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den richtigen Moment zum Pressen erkennen.", "Moment zum Pressen",
    "Die Verteidiger schauen genau hin: Springt dem Gegner der Ball vom Fuß oder kommt ein schlechter Pass, ist das der Moment. Dann pressen sie sofort und erobern den Ball.",
    sp(f=(48, 24), r11=(38, 37), r9=(58, 37), n4=(28, 46), n8=(67, 52)), [B("b3", 67.6, 52.6), B("b1", 46.4, 57.1), B("b2", 53.8, 57.1)],
    [S("Genau hinschauen", "Spieler acht hat den Ball. Spieler neun schaut genau hin: Wie nimmt Spieler acht den Ball mit?",
       bl("r9", [66, 50])),
     S("Schlechte Annahme", "Spieler acht nimmt den Ball zu weit mit, er springt ihm vom Fuß.",
       ps("b3", [62, 44])),
     S("Sofort pressen", "Das ist der Moment. Spieler neun presst sofort und erobert den Ball. Spieler elf rückt mit in die Mitte. Damit ist der Angriff vorbei, und die Teams tauschen die Rollen.",
       mv("r9", [61.4, 43.4]), mv("r11", [46, 40], delay=0.2))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Im Strafraum eng am Gegner sein.", "Eng dran im Strafraum",
    "Kommt ein Angreifer an den Strafraum, muss der Verteidiger schnell eng an ihn heran und den Schuss blocken. Der zweite Verteidiger stellt mit seinem Körper den Pass zum nächsten Angreifer zu.",
    sp(f=(55, 25), r11=(42, 36), r9=(64, 40), n4=(30, 30), n8=(74, 44)), [B("b3", 30.6, 30.6)] + BAELLE[:2],
    [S("Eng heran", "Spieler vier dribbelt zum Strafraum. Spieler elf läuft schnell eng an ihn heran. Spieler neun stellt sich in den Passweg zum Springer.",
       dr("n4", "b3", [34, 20]), mv("r11", [39, 15]), mv("r9", [46, 26], delay=0.2)),
     S("Schuss geblockt", "Spieler vier schießt, aber Spieler elf ist eng dran und blockt den Schuss. Es gibt keinen Punkt für Team Neon, und die Teams tauschen die Rollen.",
       ps("b3", [39.6, 15.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
