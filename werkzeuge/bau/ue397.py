import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 86-P12 (U15-U17, Woche 35 Phase 3): Clinical Finishing Game (Wave Game). 30 x 36 Yards = 27 x 33 m (gerundet 25 x 35 m),
# Feld x 25-75, y 5-55 (Verhältnis 1,2: kein langes Feld, nicht gedreht), drei Zonen zu je 12 Yards (gestrichelt wie im PDF).
# Zwei Großfeldtore (nur C- und B-Jugend) mit neutralen Torhütern k1 (oben) und k2 (unten).
# Drei Teams zu viert: Pink (Angreifer) -> Team Neon, Nummern wie im PDF (7, 9, 10, 11). Gold (Verteidiger) -> Team Rot,
# neu nummeriert wegen doppelter Nummern: 7 -> 2, 9 -> 3, 11 -> 4, 8 bleibt. Navy (Anspieler außen, jeder mit Ball) ->
# drittes Team in neutraler Farbe (team t, wie in ue341.py), neu nummeriert: 11 -> 5 (oben), 10 -> 6 (links), 9 -> 12 (rechts),
# 7 -> 13 (unten rechts). Ein Trainer statt zwei, links unten mit Ersatzbällen; er ruft den Anspieler auf.
# Positionen gegenüber dem PDF leicht verschoben (3D-Abstand). Die Angreifer dürfen auf beide Tore schießen (Video: Treffer
# oben und unten). Grundform nach PDF Seite 1 (Anspiel, Pass in den Lauf, Abschluss) plus Ballgewinn der Verteidiger
# (Pass zu einem Anspieler = Punkt), Ablauf im Video ab 0:30.
# Fassung 1 = PDF Key Coaching Point (Scannen, Raum erkennen) mit der Doppelbewegung aus dem Ton (erst entgegen, dann in den Raum).
# Fassung 2 = PDF Progression (Verteidiger schießen nach Ballgewinn selbst aufs Tor, sechs Bälle, Sieger nach sechs Bällen).
# Sichtkegel: Text „Constant scanning to recognise the space“, im Video eingezeichnet (Kegel von Pink 9 in den Raum vor dem Tor):
# Spieler neun schaut vor seinem Lauf in den Raum vor dem Tor.
T = P("T", "c", 17, 53, "T")
ERSATZ = [B("s1", 20.5, 54.5), B("s2", 18, 56.8)]
POS = {"k1": (50, 7.5), "k2": (50, 52.5), "t5": (30, 2.5), "t6": (21.5, 30), "t12": (78.5, 32), "t13": (77, 54),
       "n11": (31, 28), "n9": (59, 19), "n7": (68.5, 41.5), "n10": (58.5, 45),
       "r3": (40, 14), "r8": (40, 31), "r4": (67.5, 25.5), "r2": (49, 36.8)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, {"n": "a", "r": "b", "t": "t"}[i[0]], x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def baelle(ohne=()):
    return [B("b" + i[1:], round(POS[i][0] + 0.6, 1), round(POS[i][1] + 0.6, 1)) for i in ("t5", "t6", "t12", "t13") if i not in ohne] + ERSATZ
LINES = [rect(25, 5, 50, 50), line(25, 21.7, 75, 21.7), line(25, 38.3, 75, 38.3)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 55, "side": "bottom", "size": "gross"}]
DIMS = dims(25, 75, 5, 55, "25 m", "35 m", rx=86)

u = {"title": "Abschlussspiel mit Anspielern", "code": "UE-397", "kind": "Spielform",
 "focuses": ["Torschuss", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 14,
 "field_size": "25 x 35 m",
 "description": "Drei Teams zu viert und zwei Torhüter. Vier Angreifer spielen gegen vier Verteidiger auf zwei Tore, das dritte Team steht außen und spielt die Bälle ein. Der Trainer ruft einen Anspieler auf, und der bringt seinen Ball zu den Angreifern, die schnell abschließen wollen. Erobern die Verteidiger den Ball, suchen sie den Pass zu einem Anspieler und holen sich so den Punkt.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 35 Metern mit zwei großen Toren, in drei gleich große Zonen geteilt.",
  "Verteilen: Drei Teams zu viert. Team Neon greift an, Team Rot verteidigt, das dritte Team steht mit je einem Ball außen am Feld. In jedem Tor steht ein Torwart. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Der Trainer ruft die Nummer eines Anspielers. Der spielt seinen Ball zu einem Angreifer. Team Neon kombiniert schnell und schließt auf eines der beiden Tore ab. Erobert Team Rot den Ball, spielt es ihn zu einem Anspieler außen.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon, jeder Pass zu einem Anspieler nach Ballgewinn gibt einen Punkt für Team Rot. Nach vier Bällen geht das Team mit weniger Punkten nach außen, und die Anspieler kommen ins Feld."],
 "organisation_show": ORG,
 "coaching_points": ["Mit wenigen Kontakten abschließen", "Immer wieder schauen, wo Platz ist", "Erst entgegen, dann in den Raum", "Schnell reagieren, wenn der Trainer ruft"],
 "materials": ["2 große Tore", "8 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Abschlussspiel mit Anspielern. Vier gegen vier auf zwei Tore, und außen stehen vier Anspieler mit Ball. Wer aufgerufen wird, spielt ein, und dann muss es schnell gehen.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": baelle(),
  "steps": [
   S("Trainer ruft, Spieler fünf spielt ein", "Der Trainer ruft fünf. Spieler fünf steht oben außen und spielt seinen Ball sofort ins Feld. Spieler elf kommt ihm entgegen und nimmt an.",
     mv("n11", [33.5, 21]), ps("b5", [34.1, 21.6], delay=0.4)),
   S("Schauen, dann Pass in den Lauf", "Spieler neun schaut über die Schulter, wo vor dem Tor Platz ist. Dann startet er genau dorthin, und Spieler elf spielt ihm den Ball in den Lauf.",
     bl("n9", [46, 8]), mv("n9", [56, 13], after=True), ps("b5", [56.6, 13.6], delay=1.3)),
   S("Direkt abgeschlossen: Punkt", "Spieler neun schießt mit dem ersten Kontakt, und das gibt einen Punkt für Team Neon.",
     ps("b5", [54, 5.3])),
   S("Trainer ruft zwölf, Rot fängt ab", "Jetzt ruft der Trainer zwölf. Spieler zwölf spielt in Richtung Spieler sieben. Aber Spieler vier läuft dazwischen und fängt den Ball ab.",
     mv("r4", [73, 36]), ps("b12", [73.6, 36.6], delay=0.5)),
   S("Pass nach außen: Punkt für Rot", "Spieler vier spielt quer zu Spieler drei. Der findet Spieler fünf außen, und das gibt einen Punkt für Team Rot. Dann ruft der Trainer den nächsten Anspieler. Nach vier Bällen tauschen die Teams, wer weniger Punkte hat, geht nach außen.",
     ps("b12", [40.6, 14.6]), ps("b12", [30.6, 3.1], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Schauen und den Raum finden.", "Schauen, dann in den Raum",
    "Wer auf den Ball wartet, schaut immer wieder, wo Platz ist. Die Stürmer laufen nicht sofort weg. Erst ein paar Schritte zum Ball, dann scharf in den freien Raum. So hängen sie den Verteidiger ab und schließen mit wenigen Kontakten ab.",
    sp(), baelle(),
    [S("Anspiel von außen", "Der Trainer ruft sechs. Spieler sechs spielt flach zu Spieler elf. Spieler neun schaut schon, wo Platz ist.",
       ps("b6", [31.6, 28.6]), bl("n9", [62, 8], delay=0.4)),
     S("Erst entgegen, dann in den Raum", "Spieler neun kommt zwei Schritte entgegen. Dann zieht er an und sprintet in den Raum vor dem Tor. Genau dahin spielt Spieler elf.",
       mv("n9", [54, 24]), mv("n9", [61, 12.5], after=True), ps("b6", [61.6, 13.1], delay=1.2)),
     S("Mit einem Kontakt: Punkt", "Spieler neun nimmt den Ball direkt und trifft, und das gibt einen Punkt für Team Neon.",
       ps("b6", [55, 5.3]))], dims=DIMS),
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball erobert, greift sofort selbst an.", "Ballgewinn, dann aufs Tor",
    "Erobert Team Rot den Ball, spielt es nicht mehr nach außen, sondern greift sofort ein Tor an. Trifft Team Rot, bekommt es beim nächsten Ball das Anspiel. Gespielt wird mit sechs Bällen. Wer danach die meisten Punkte hat, gewinnt.",
    sp(), baelle(),
    [S("Anspiel auf Spieler zehn", "Der Trainer ruft dreizehn. Spieler dreizehn spielt zu Spieler zehn.",
       ps("b13", [59.1, 45.6])),
     S("Spieler zwei erobert den Ball", "Spieler zwei ist sofort da und spitzelt ihm den Ball weg. Jetzt ist Team Rot am Ball.",
       mv("r2", [56.5, 42]), dr("r2", "b13", [53, 47], after=True)),
     S("Sofort aufs Tor: Punkt für Rot", "Spieler zwei zieht sofort ab und trifft, und das gibt einen Punkt für Team Rot. Beim nächsten Ball greift Team Rot an.",
       ps("b13", [55.5, 54.7]))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
