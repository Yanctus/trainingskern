import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P5 (U12-U14, Woche 41 Phase 3): 3 Phase Finishing Drill. Volle Breite x 25 Yards = Feld x 8-92, y 5-55 (23 m tief),
# Strafraum und Torraum als durchgezogene Linien (Halbkreis weggelassen). Ausrichtung wie im PDF (Tor oben, Flügel rechts).
# Pink -> Team Neon mit den Nummern aus dem PDF (7 Stürmer, 8 Mittelfeld, 9 Start, 11 Flügel), grüner Torwart 1 -> neutraler
# Torwart TW. Spieler zehn (wartender Flügelspieler) nur im Text (3D-Abstand zu Spieler elf). Fünf Puppen als Stangen, die
# Startmarkierungen als Hütchen. Spieler neun leicht nach rechts gerückt (3D-Abstand zu Spieler sieben). Ein Trainer statt zwei;
# er spielt in Phase zwei und drei den neuen Ball zu Spieler neun (im Video liegt er schon dort). Rollentausch im Original nicht
# genauer beschrieben: hier "alle tauschen die Rollen, Spieler zehn kommt als Flügelspieler dazu".
# Sichtkegel: PDF "Quick look up to see GK's positioning before finish" -> Stürmer schaut vor dem Abschluss zum Torwart (Phase eins
# und zwei). Ton "wingers need to see this movement before the cross" -> Flügelspieler schaut vor der Flanke zum Stürmer.
# Im Video kein Kegel eingezeichnet (nur ein Kreis um den Stürmer), Richtung aus dem Sinn.
# Fassungen: Coaching-Punkt Doppelbewegung (PDF Seite 2, Video ab 1:24), Steigerung Seite wechseln (gespiegelt, Video ab 1:08).
T = P("T", "c", 76, 51, "T")
POS = {"k": (50, 9), "n7": (34, 27), "n8": (66, 39), "n9": (42.5, 44), "n11": (84, 35)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i == "k" else "a", x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 79.6, 54.5), B("s2", 76, 54.5)]
LINES = [rect(8, 5, 84, 50), rect(23.8, 5, 52.8, 21.7), rect(38, 5, 24, 7)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
PUPPEN = [(50, 16), (40.2, 25.3), (61, 26.4), (18.8, 21.4), (82.4, 21.4)]
def cones(gespiegelt=False):
    marken = [(40, 47.5), (63.5, 42.5), (81.5, 38.5)]
    if gespiegelt: marken = [(100 - x, y) for x, y in marken]
    k = [C(x, y, shape="stange", id="p%d" % i) for i, (x, y) in enumerate(PUPPEN)]
    return k + [C(x, y, id="m%d" % i) for i, (x, y) in enumerate(marken)]

u = {"title": "Drei Muster zum Abschluss", "code": "UE-245", "kind": "Übungsform",
 "focuses": ["Torschuss", "Zusammenspiel", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 8, "field_size": "Volle Breite x 23 m",
 "description": "Ein Stürmer schließt dreimal hintereinander ab, jedes Mal nach einem anderen Muster. Erst läuft er um eine Puppe und schießt aus der Mitte, dann legt er ab und startet hinter die Puppe zum Abschluss aus dem Winkel. Zum Schluss geht der Ball auf den Flügel, und der Stürmer verwertet die Flanke. Danach tauschen alle die Rollen.",
 "organisation": ["Aufbauen: Ein Feld über die volle Breite und 23 Meter tief, oben ein Jugendtor mit Torwart. Am Strafraum stehen fünf Puppen: eine vor dem Tor, zwei an der Strafraumlinie und je eine außen.",
  "Verteilen: Spieler sieben ist der Stürmer, Spieler acht steht rechts im Mittelfeld, Spieler neun links mit dem Ball. Spieler elf ist der Flügelspieler rechts, Spieler zehn wartet dahinter. Der Trainer steht unten mit Bällen.",
  "Ablauf: Phase eins Pass über Spieler acht, Lauf um die Puppe, Abschluss. Phase zwei Ablage, Pass außen an der Puppe vorbei, Abschluss aus dem Winkel. Phase drei Ablage, Pass auf den Flügel, Flanke, Abschluss.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach allen drei Phasen tauschen die Spieler die Rollen, und Spieler zehn kommt als Flügelspieler dazu."],
 "organisation_show": ORG,
 "coaching_points": ["Quer zum Torwart in die Ecken schießen", "Vor dem Schuss kurz zum Torwart schauen", "Mit einer Doppelbewegung lösen, bevor die Flanke kommt", "Genau und mit dem richtigen Tempo passen, höchstens zwei Kontakte"],
 "materials": ["1 Jugendtor", "5 Stangen als Puppen", "3 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Drei Muster zum Abschluss. Der Stürmer schließt dreimal hintereinander ab, jedes Mal nach einem anderen Muster.",
 "board": {"lines": LINES, "goals": TORE, "cones": cones(), "players": sp(),
  "balls": [B("b1", 43.1, 44.6), B("b2", 76.6, 51.6), B("b3", 72.4, 54.5)] + ERSATZ,
  "steps": [
   S("Phase eins: um die Puppe", "Phase eins: Spieler neun passt zu Spieler acht. Gleichzeitig läuft Spieler sieben unten um die linke Puppe herum in die Mitte.",
     ps("b1", [66.6, 39.6]), mv("n7", [37, 30.5]), mv("n7", [43, 30], after=True), mv("n7", [44.5, 25], after=True)),
   S("Phase eins: Punkt", "Spieler acht spielt flach in die Mitte. Spieler sieben schaut kurz zum Torwart und schießt direkt in die Ecke, und das gibt einen Punkt für Team Neon.",
     ps("b1", [45.1, 25.6]), bl("n7", [50, 9], after=True), ps("b1", [44.5, 5.4], after=True)),
   S("Phase zwei: Ablage", "Phase zwei: Der Trainer spielt Spieler neun einen neuen Ball. Spieler sieben kommt kurz entgegen, Spieler neun spielt ihn an, und Spieler sieben legt direkt ab zu Spieler acht.",
     ps("b2", [43.1, 44.6]), mv("n7", [50, 31]), ps("b2", [50.6, 31.6], after=True), ps("b2", [66.6, 39.6], after=True)),
   S("Phase zwei: Punkt", "Spieler acht spielt außen an der rechten Puppe vorbei in den Strafraum. Spieler sieben startet hinter die Puppe, schaut zum Torwart und schießt direkt ins lange Eck, und das gibt einen Punkt.",
     mv("n7", [56, 22.5]), mv("n7", [64, 17], after=True), ps("b2", [64.6, 17.6], delay=0.6), mv("k", [55, 7.5], delay=0.6),
     bl("n7", [55, 8], after=True), ps("b2", [44.5, 5.4], after=True)),
   S("Phase drei: auf den Flügel", "Phase drei: Der Trainer spielt Spieler neun den dritten Ball. Wieder kommt Spieler sieben entgegen und legt ab zu Spieler acht. Spieler acht spielt hinaus auf den Flügel, und Spieler elf sprintet in den Pass.",
     ps("b3", [43.1, 44.6]), mv("n7", [50, 31]), mv("k", [50, 9]), ps("b3", [50.6, 31.6], after=True), ps("b3", [66.6, 39.6], after=True),
     mv("n11", [89, 27], after=True), ps("b3", [89.6, 27.6], after=True)),
   S("Flanke: Punkt", "Spieler elf dribbelt zur Grundlinie und schaut, wohin Spieler sieben läuft. Der täuscht zum kurzen Pfosten an und zieht zurück. Flanke, Spieler sieben schießt direkt, und das gibt einen Punkt für Team Neon. Danach tauschen alle die Rollen, und Spieler zehn kommt als Flügelspieler dazu.",
     dr("n11", "b3", [87, 12]), mv("n7", [56, 22.5]), mv("n7", [61, 13], after=True), mv("n7", [55, 17], after=True),
     bl("n11", [67, 15], after=True), ps("b3", [55.6, 17.6], after=True), mv("k", [54, 7.5], after=True), ps("b3", [44.5, 5.4], after=True))],
  "dims": dims(8, 92, 5, 55, "volle Breite", "23 m", rx=96)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Doppelbewegung vor der Flanke.", "Doppelbewegung vor der Flanke",
    "Der Stürmer läuft nicht einfach geradeaus. Er täuscht erst in die eine Richtung an und startet dann schnell in die andere. So löst er sich im Spiel von seinem Gegenspieler. Der Flügelspieler schaut genau hin und flankt, wenn der Stürmer startet.",
    sp(n7=(51, 29), n11=(87, 12)), [B("b3", 87.6, 12.6)] + ERSATZ,
    [S("Antäuschen", "Spieler sieben täuscht erst einen Lauf nach links an. Dann dreht er schnell ab und sprintet zum kurzen Pfosten.",
       mv("n7", [46, 25]), mv("n7", [58, 19], after=True)),
     S("Kopf hoch, Flanke: Punkt", "Spieler elf schaut, wohin Spieler sieben läuft, und flankt genau dorthin. Spieler sieben schießt direkt ins lange Eck, und das gibt einen Punkt für Team Neon.",
       bl("n11", [67, 17]), ps("b3", [58.6, 19.6], after=True), mv("k", [54, 7.5], after=True), ps("b3", [44.5, 5.4], after=True))],
    cones=cones()),
  V("Steigerung", "Und jetzt die Steigerung: Wir wechseln die Seite.", "Angriff über links",
    "Jetzt läuft alles spiegelverkehrt. Spieler acht steht links, Spieler neun rechts, und der Flügelspieler kommt von links. So übt der Stürmer die Läufe von der anderen Seite und schießt auch mit dem anderen Fuß.",
    sp(n7=(49, 30), n8=(34, 39), n9=(57.5, 44), n11=(16, 35)), [B("b1", 58.1, 44.6)] + ERSATZ,
    [S("Ablage, ab auf links", "Spieler neun spielt Spieler sieben an, und der legt ab zu Spieler acht. Spieler acht spielt hinaus auf den linken Flügel, und Spieler elf sprintet in den Pass.",
       ps("b1", [49.6, 30.6]), ps("b1", [34.6, 39.6], after=True), mv("n11", [11, 27], after=True), ps("b1", [11.6, 27.6], after=True)),
     S("Flanke von links: Punkt", "Spieler elf dribbelt zur Grundlinie und schaut zu Spieler sieben. Der täuscht nach rechts an und startet zum kurzen Pfosten. Flanke, Spieler sieben schießt ins lange Eck, und das gibt einen Punkt für Team Neon.",
       dr("n11", "b1", [13, 12]), mv("n7", [54, 25]), mv("n7", [42, 19], after=True), bl("n11", [33, 17], after=True),
       ps("b1", [42.6, 19.6], after=True), mv("k", [46, 7.5], after=True), ps("b1", [55.5, 5.4], after=True))],
    cones=cones(True))]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
