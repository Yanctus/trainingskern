import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 27-P8 (U12-U14, Woche 42 Phase 6): Defending Against Speed! (Wave of Play). 30 x 30 Yards = Feld x 24-76, y 5-55 (27 m),
# gedreht: im PDF liegt das Tor rechts, hier oben (Jugendtor mit neutralem Torwart, weil die Teams die Rollen tauschen).
# Strafraum x 35-65, y 5-13.6 nach der PDF-Skizze, Halbkreis weggelassen, die Linie durchs Feld gestrichelt bei y 35.
# Zwei Minitore unten in den Ecken (im PDF links). Gelb (Verteidiger 2, 6, 5) -> Team Neon, Pink (Angreifer 9, 11, 7) -> Team Rot,
# Nummern wie im PDF. Das wartende dritte Dreierteam (8, 4, 6) steht nur im Text (zwei Teams auf der Tafel). Ein Trainer statt
# zwei, links unten neben dem Feld.
# Steigerung nach PDF und Ton: Nach einer erfolgreichen Abwehr geht ein Verteidiger raus (drei gegen zwei, dann drei gegen eins).
# Sichtkegel aus dem PDF ("Timing of interceptions and awareness of attackers movement"): im Coaching-Punkt schaut Spieler sechs
# zu Spieler sieben, der hinter ihm in die Mitte startet, bevor er den Steilpass abfängt. Im Video ist nur eine dunkle Markierung
# um die Spieler am Ball, kein Kegel; Richtung aus dem Sinn.
T = P("T", "c", 14, 50, "T")
K = P("k", "t", 50, 8, "TW")
POS = {"n2": (36, 27), "n6": (50, 24.5), "n5": (64, 27), "r11": (26, 42), "r9": (50, 53), "r7": (74, 42)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [K] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 14.6, 53.5), B("s2", 11, 53.5)]
def baelle(b1=(50.6, 53.6)):
    return [B("b1", *b1)] + ERSATZ
LINES = [rect(24, 5, 52, 50), rect(35, 5, 30, 8.6), line(24, 35, 76, 35)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 30, "y": 55, "side": "bottom"}, {"x": 70, "y": 55, "side": "bottom"}]

u = {"title": "Welle gegen schnelle Angreifer", "code": "UE-249", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 10, "players_max": 10, "field_size": "27 x 27 m",
 "description": "Drei Angreifer spielen mit viel Tempo gegen drei Verteidiger auf das große Tor. Die Verteidiger bleiben kompakt, drängen die Angreifer nach außen und fangen Pässe ab. Treffen die Angreifer, werden sie zu Verteidigern, und das nächste Dreierteam greift an. Erobern die Verteidiger den Ball, kontern sie auf zwei Minitore und bleiben im Feld.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern mit Strafraum und einem Jugendtor oben. Eine gestrichelte Linie quer durchs Feld, unten in den Ecken zwei Minitore.",
  "Verteilen: Drei Verteidiger von Team Neon stehen vor dem Tor, drei Angreifer von Team Rot unten. Ein neutraler Torwart steht im Tor. Das nächste Dreierteam wartet unten neben dem Feld beim Trainer mit Bällen.",
  "Ablauf: Spieler neun startet mit dem Ball, und Team Rot greift mit viel Tempo an. Team Neon bleibt eng zusammen und drängt nach außen. Erobert Team Neon den Ball, kontert es auf die Minitore.",
  "Wertung und Wechsel: Ein Treffer ins große Tor gibt einen Punkt für Team Rot, dann wird Team Rot zum Verteidiger, und das nächste Team greift an. Ein Ballgewinn gibt einen Punkt für Team Neon, ein Treffer ins Minitor noch einen, und Team Neon bleibt im Feld."],
 "organisation_show": ORG,
 "coaching_points": ["Kompakt bleiben und die Angreifer nach außen drängen", "Immer zwischen Gegner und Tor stehen", "Den Pass genau im richtigen Moment abfangen", "Mit viel Tempo angreifen, damit die Verteidiger gefordert sind"],
 "materials": ["1 Jugendtor", "2 Minitore", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Welle gegen schnelle Angreifer. Drei Verteidiger müssen gegen drei schnelle Angreifer kompakt bleiben.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": baelle(),
  "steps": [
   S("Pass nach außen", "Spieler neun startet mit dem Ball und spielt schnell nach links zu Spieler elf. Spieler zwei läuft Spieler elf an.",
     ps("b1", [26.6, 42.6]), mv("n2", [31, 33], delay=0.3)),
   S("Steilpass in den Lauf", "Spieler sieben startet von rechts quer in die Mitte. Spieler elf spielt den Ball genau in seinen Lauf. Spieler sechs ist zu weit weg.",
     mv("r7", [50, 31]), ps("b1", [50.6, 31.6], delay=0.4), mv("n6", [54, 21])),
   S("Abschluss: Punkt", "Spieler sieben schießt sofort und trifft. Das gibt einen Punkt für Team Rot. Jetzt verteidigt Team Rot, Team Neon geht raus, und das nächste Dreierteam greift an.",
     ps("b1", [45, 5.6]))],
  "dims": dims(24, 76, 5, 55, "27 m", "27 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Kompakt bleiben und nach außen drängen.", "Kompakt und nach außen",
    "Läuft der mittlere Verteidiger zu weit heraus, entsteht in der Mitte eine Lücke. Darum bleiben die drei eng zusammen. Wer den Ballführenden anläuft, drängt ihn nach außen. Die anderen schauen, wohin die Angreifer laufen, und fangen den Pass ab.",
    sp(), baelle(),
    [S("Nach außen drängen", "Spieler neun spielt zu Spieler elf. Spieler zwei läuft ihn von innen an und drängt ihn nach außen. Spieler sechs und Spieler fünf schieben mit und bleiben eng zusammen.",
       ps("b1", [26.6, 42.6]), mv("n2", [31, 35], delay=0.3), mv("n6", [44, 27], delay=0.3), mv("n5", [56, 27], delay=0.3)),
     S("Umschauen", "Spieler sieben startet in die Mitte. Spieler sechs schaut zu ihm und weiß jetzt, wohin der Pass gehen soll.",
       mv("r7", [58, 37]), bl("n6", [58, 37], after=True)),
     S("Abgefangen: Punkt", "Spieler elf spielt steil, aber Spieler sechs geht dazwischen und fängt den Ball ab. Das gibt einen Punkt für Team Neon. Trifft er danach ins Minitor, gibt das noch einen Punkt.",
       mv("n6", [48, 34]), ps("b1", [48.6, 34.6], delay=0.2), dr("n6", "b1", [66, 49], after=True), ps("b1", [70, 54.4], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Einer geht raus, dann drei gegen zwei.", "Drei gegen zwei",
    "Nach jeder erfolgreichen Abwehr geht ein Verteidiger raus. Dann verteidigen nur noch zwei gegen drei, danach einer gegen drei. Wird der Ball nach außen gedrängt, laufen die Verteidiger zwischen Gegner und Tor und fangen den Querpass ab. Schaffen sie alle drei Abwehren, gibt es drei Extrapunkte.",
    sp(), baelle(),
    [S("Einer geht raus", "Team Neon hat gerade abgewehrt. Jetzt geht Spieler fünf raus, und die nächsten drei greifen an. Spieler zwei und Spieler sechs verteidigen allein.",
       mv("n5", [86, 22]), mv("n2", [40, 27]), mv("n6", [58, 25])),
     S("Nach außen gedrängt", "Spieler neun spielt nach rechts zu Spieler sieben. Spieler sechs läuft ihn an und drängt ihn an die Seite. Spieler elf läuft in den Strafraum.",
       ps("b1", [74.6, 42.6]), dr("r7", "b1", [72, 22], after=True), mv("n6", [64, 24], after=True), mv("r11", [38, 14], delay=0.5)),
     S("Querpass abgefangen: Punkt", "Spieler sieben spielt quer vor das Tor. Aber Spieler zwei ist schnell zurück, steht zwischen Spieler elf und dem Ball und fängt ihn ab. Das gibt einen Punkt für Team Neon. Als Nächstes heißt es drei gegen eins.",
       mv("n2", [46, 13]), ps("b1", [46.6, 13.6], delay=0.3))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
