import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P6 (U15-U17, Woche 26 Phase 4): Attack at Speed Transition Game, Small Sided Game. 24 x 36 Yards = 22 x 33 m
# (gerundet 20 x 35 m). Keine Dublette: UE-194 (95-P4), UE-245 (95-P5), UE-305 (95-P9), UE-357 (95-P8), UE-057, UE-118 haben
# andere Organisation (kein 3 gegen 3 mit zwei Springern in Außenzonen und zwei Torhütern).
# LANGES FELD QUER (Vorbild ue317.py): Die lange Seite (36 Yards) liegt waagrecht, Feld x 9-89, y 4-51. Die Tore stehen im
# Original an den langen Seiten (PDF links und rechts), hier also oben und unten: PDF um 90 Grad im Uhrzeigersinn gedreht
# (PDF links -> oben, PDF oben -> rechts). Team Neon greift nach oben an, Team Rot nach unten.
# Großfeldtore mit neutralen Torhütern (k1, k2; nur C- und B-Jugend). Die Außenzonen (4 Yards = knapp 4 m) links und rechts
# gestrichelt, vier Hütchen an den Zonenlinien wie im PDF. Die Pitch-Markierungen im Hintergrund des PDF (Mittellinie,
# Strafraum) weggelassen.
# PDF pink -> Team Neon (7, 8, 9), navy -> Team Rot (3, 4, 5), im PDF ohne Nummern. Blau (Floater) -> Springer F.
# Positionen auf ein Raster gesetzt (3D-Abstand). Ein Trainer statt zwei, unten an der Seitenlinie neben dem Tor.
# Grundform nach PDF/Video: Ballgewinn, Pass zum Springer, Springer legt in den Lauf, Abschluss.
# Fassungen: Coaching-Punkt aus PDF Seite 2 („Don't block passing lanes to the floater ... move away into space“),
# Steigerung aus PDF Seite 2 (drei Sekunden). Annahme Steigerung: Der Text ist unklar; umgesetzt wie im Video beschriftet
# („possession retained for 3 seconds - goal stands“): Wer trifft, bekommt den nächsten Ball, erobert das andere Team ihn
# binnen drei Sekunden, zählt der Punkt nicht.
# Sichtkegel: Ton „Players must be aware of their positioning at all times“, Video „Trigger quick counter“; im Video kein Kegel.
# Richtung aus dem Sinn: Der Balleroberer schaut nach dem Ballgewinn zum Springer, bevor er ihn anspielt.
T = P("T", "c", 74, 55.3, "T")  # unten an der Seitenlinie, neben dem unteren Tor
ERSATZ = [B("s1", 77.5, 55.8), B("s2", 80, 55.8)]
POS = {"k1": (49, 6.5), "k2": (49, 48.5), "f1": (13.5, 27.5), "f2": (84.5, 27.5),
       "n7": (24, 38), "n8": (52, 26), "n9": (68, 10), "r3": (30, 15), "r4": (40, 31), "r5": (62, 38)}
def sp(**k):
    d = dict(POS); d.update(k)
    out = []
    for i, (x, y) in d.items():
        if i[0] == "k": out.append(P(i, "t", x, y, "TW"))
        elif i[0] == "f": out.append(P(i, "t", x, y, "F"))
        else: out.append(P(i, "a" if i[0] == "n" else "b", x, y, i[1:]))
    return out + [T]
ZL, ZR = 17.9, 80.1  # Außenzonen, je 4 Yards
LINES = [rect(9, 4, 80, 47), line(ZL, 4, ZL, 51), line(ZR, 4, ZR, 51)]
CONES = [C(ZL, 4), C(ZL, 51), C(ZR, 4), C(ZR, 51)]
TORE = [{"x": 49, "y": 4, "side": "top", "size": "gross"}, {"x": 49, "y": 51, "side": "bottom", "size": "gross"}]
DIMS = dims(9, 89, 4, 51, "35 m", "20 m", rx=96)

u = {"title": "Umschalten mit zwei Springern", "code": "UE-372", "kind": "Spielform",
 "focuses": ["Umschalten", "Zusammenspiel", "Torschuss"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 10,
 "field_size": "20 x 35 m",
 "description": "Drei gegen drei mit zwei Springern und zwei Torhütern. Die Springer laufen außen in schmalen Zonen und spielen immer mit dem Team am Ball. Wer den Ball erobert, greift sofort an, und das andere Team muss genauso schnell verteidigen. Nach einem Treffer bekommt das Team, das getroffen hat, den nächsten Ball.",
 "organisation": ["Aufbauen: Ein Feld von 20 mal 35 Metern mit einem Großfeldtor oben und unten. Links und rechts liegt außen je eine Zone, knapp vier Meter breit, mit Hütchen markiert.",
  "Verteilen: Drei von Team Neon gegen drei von Team Rot im Feld. In jeder Außenzone steht ein Springer, in jedem Tor ein Torwart. Der Trainer steht mit vielen Bällen unten an der Seitenlinie.",
  "Ablauf: Der Trainer spielt ein. Das Team am Ball greift an und spielt die Springer außen an. Team Neon spielt aufs obere Tor, Team Rot aufs untere. Wer den Ball erobert, kontert sofort.",
  "Wertung: Jeder Treffer gibt einen Punkt. Das Team, das getroffen hat, bekommt vom Trainer den nächsten Ball. Die Springer werden nach einigen Angriffen getauscht."],
 "organisation_show": ORG,
 "coaching_points": ["Ball erobert? Sofort nach vorn", "Den Springer außen nutzen, dann ist man zu zweit", "Kurz und schnell kombinieren", "Raus aus dem Passweg zum Springer"],
 "materials": ["2 Großfeldtore", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Umschalten mit zwei Springern. Drei gegen drei auf zwei Tore, außen hilft je ein Springer. Wer den Ball holt, geht sofort mit Tempo nach vorn.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 74.6, 55.9)] + ERSATZ,
  "steps": [
   S("Trainer spielt Team Rot an", "Der Trainer spielt den Ball zu Spieler vier. Team Rot greift jetzt aufs untere Tor an. Team Neon verteidigt.",
     ps("b1", [40.6, 31.6])),
   S("Ballgewinn in der Mitte", "Spieler vier will zu Spieler fünf spielen. Spieler acht liest den Pass, geht dazwischen und hat den Ball. Ab jetzt greift Team Neon an.",
     ps("b1", [52.1, 35.6]), mv("n8", [51.5, 35], delay=0.2)),
   S("Kopf hoch, raus zum Springer", "Spieler acht schaut sofort zum Springer außen. Der steht frei, und der Ball geht direkt raus. Spieler neun startet schon.",
     bl("n8", [84.5, 27.5]), ps("b1", [85.1, 28.1], after=True), mv("n9", [62, 9], delay=0.6)),
   S("Springer legt in den Lauf", "Der Springer spielt mit einem Kontakt in den Lauf von Spieler neun. Team Rot ist noch auf dem Weg nach vorn und kommt zu spät zurück.",
     mv("n9", [57, 13]), ps("b1", [57.6, 13.6], delay=0.3), mv("r3", [42, 14], delay=0.3), mv("r4", [46, 22], delay=0.3)),
   S("Abschluss: Punkt", "Spieler neun schießt direkt, am Torwart vorbei, und das gibt einen Punkt für Team Neon. Als Belohnung bekommt Team Neon den nächsten Ball vom Trainer.",
     ps("b1", [54.5, 4.3]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Raus aus dem Passweg zum Springer.", "Passweg zum Springer frei",
    "Wer zwischen dem Ball und dem Springer steht, versperrt den Pass. Also weg da und in den freien Raum. Dann geht der Ball zum Springer, und der kann gleich in den Lauf spielen. So entstehen mehrere Anspielstationen.",
    sp(n8=(48, 28), n9=(68, 29), r4=(36, 32), r5=(58, 42)), [B("b1", 48.6, 28.6)] + ERSATZ,
    [S("Im Passweg, also weg da", "Spieler acht hat den Ball und schaut zum Springer. Spieler neun steht genau dazwischen. Er geht weg, Richtung Tor in den freien Raum.",
       bl("n8", [84.5, 27.5]), mv("n9", [70, 14], delay=0.5)),
     S("Über den Springer zum Punkt", "Jetzt ist der Weg frei. Der Ball geht raus zum Springer, und der spielt direkt zu Spieler neun. Der schließt sofort ab, und das gibt einen Punkt für Team Neon.",
       ps("b1", [85.1, 28.1]), ps("b1", [70.6, 14.6], after=True), ps("b1", [55.5, 4.3], after=True))],
    dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Nach dem Treffer drei Sekunden überstehen.", "Drei Sekunden nach dem Punkt",
    "Nach einem Treffer spielt der Trainer sofort den nächsten Ball zu dem Team, das getroffen hat. Das andere Team presst sofort. Erobert es den Ball innerhalb von drei Sekunden, zählt der Punkt nicht. Hält das Team den Ball drei Sekunden, bleibt der Punkt stehen.",
    sp(n9=(61, 11), r5=(65, 39)), [B("b1", 74.6, 55.9)] + ERSATZ,
    [S("Treffer, sofort der nächste Ball", "Spieler neun hat gerade getroffen. Der Trainer spielt sofort den nächsten Ball zu Spieler acht. Team Rot läuft auf der Stelle an.",
       ps("b1", [52.6, 26.6]), mv("r4", [47.5, 22.5], delay=0.4), mv("r5", [58, 32], delay=0.4), mv("r3", [28, 30], delay=0.4)),
     S("Drei Sekunden halten: Punkt zählt", "Spieler acht spielt schnell zu Spieler sieben, und der gleich weiter zum Springer. Drei Sekunden sind um, der Ball ist noch bei Team Neon. Der Punkt zählt. Hätte Team Rot den Ball vorher erobert, wäre er weg.",
       ps("b1", [24.6, 38.6]), ps("b1", [14.1, 28.1], after=True), mv("r3", [22, 33], delay=0.6))],
    dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
