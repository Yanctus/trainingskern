import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 66-P7 (U12-U14, Woche 35 Phase 3): 3rd Man Runs to Finish (PDF: Third Man Movement and Runs to Finish, Pattern).
# 40 x 45 Yards = Feld x 27.5-72.5, y 5-55 (37 x 41 m), Tor oben mit neutralem Torwart (im PDF grün -> "k" TW, Jugendtor).
# Orientierung wie im PDF (Tor oben, nicht gedreht). Vier Dummys als Stangen: zwei auf der Strafraumlinie (y 24.5), zwei davor
# (y 40.5); Abstand der Reihen etwas größer als im PDF (3D-Abstand), Spieler stehen direkt vor ihren Stangen.
# Alle Feldspieler Team Neon: 8 Starter, 11 untere Stange links, 9 Spitze oben links, 10 oben rechts, 7 unten rechts,
# weitere Wartende nur im Text (am Start). Ein Trainer links statt Trainer-Symbol am Rand.
# Grundform = Organisation aus PDF/Ton (Doppelpass mit 11, Pass zur Spitze 9, Ablage in den Lauf des dritten Mannes 11).
# Coaching-Punkt = PDF Seite 2 links (vor den Läufer spielen), Steigerung = PDF Seite 2 rechts / Ton (alle vier Stangen-Spieler).
# Sichtkegel: Text "Head up to see GK's positioning before finishing", im Video Kegel vom Läufer zum Torwart eingezeichnet
# (ca. 0:26-0:30) -> bl() des Schützen Richtung Torwart vor jedem Abschluss.
T = P("T", "c", 19, 30, "T")
POS = {"n9": (39, 26.5), "n10": (61, 26.5), "n11": (39, 42.5), "n7": (61, 42.5), "n8": (49, 55)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k", "t", 50, 8.5, "TW"), T]
ERSATZ = [B("s1", 22.6, 33.5), B("s2", 19, 33.5), B("s3", 44.5, 58)]
LINES = [rect(27.5, 5, 45, 50), rect(38.6, 5, 22.8, 6.5), line(27.5, 25, 72.5, 25, dashed=False)]
KEGEL = [C(39, 24.5, shape="stange"), C(61, 24.5, shape="stange"), C(39, 40.5, shape="stange"), C(61, 40.5, shape="stange")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]

u = {"title": "Hinterlaufen zum Abschluss", "code": "UE-227", "kind": "Übungsform",
 "focuses": ["Torschuss", "Passspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 7, "players_max": 11, "field_size": "37 x 41 m",
 "description": "Eine Passfolge mit vier Stangen vor dem Strafraum und einem Torwart. Der Starter spielt einen Doppelpass mit dem Spieler an der unteren Stange und passt dann zur Spitze. Der erste Passgeber läuft im Bogen hinter dem Starter in die Mitte, bekommt den Ball von der Spitze vorgelegt und schließt ab. Gespielt wird abwechselnd über die linke und die rechte Seite.",
 "organisation": ["Aufbauen: Ein Feld von 37 mal 41 Metern vor einem Jugendtor mit Torwart. Zwei Stangen stehen auf der Strafraumlinie, zwei weitere etwa 14 Meter davor.",
  "Verteilen: An jeder Stange steht ein Spieler von Team Neon. Die anderen warten mit Bällen am Start unten in der Mitte. Der Trainer steht an der Seite mit Ersatzbällen.",
  "Ablauf: Doppelpass mit der unteren Stange, dann Pass zur Spitze an der oberen Stange. Die Spitze legt in die Mitte ab, und der dritte Mann kommt im Bogen, nimmt den Ball in den Strafraum mit und schießt.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Der Schütze stellt sich am Start an, der Starter rückt auf seinen Platz. Nach jeder Runde wechselt die Seite."],
 "organisation_show": ORG,
 "coaching_points": ["Den Lauf so timen, dass er den Pass im Lauf trifft", "Genau und mit dem richtigen Tempo passen", "Vor dem Abschluss kurz zum Torwart schauen", "Flach und in die Ecken schießen"],
 "materials": ["1 Jugendtor", "4 Stangen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Hinterlaufen zum Abschluss. Doppelpass, Pass zur Spitze, und der dritte Mann kommt im Bogen in die Mitte und schießt.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 49.6, 55.6)] + ERSATZ,
  "steps": [
   S("Doppelpass", "Spieler acht spielt zu Spieler elf und läuft ein paar Schritte nach vorn. Spieler elf legt den Ball direkt zurück.",
     ps("b1", [39.6, 43.1]), mv("n8", [47, 47], delay=0.3), ps("b1", [47.6, 47.6], after=True)),
   S("Pass zur Spitze", "Spieler acht spielt direkt zu Spieler neun an der oberen Stange. Gleichzeitig startet Spieler elf im Bogen hinter Spieler acht herum.",
     ps("b1", [39.6, 27.1]), mv("n11", [44, 50.5], delay=0.2), mv("n11", [52.5, 49.5], after=True), mv("n11", [55, 37], after=True)),
   S("Ablage in den Lauf", "Spieler neun legt den Ball direkt in die Mitte, genau in den Lauf von Spieler elf. Der schaut kurz hoch zum Torwart.",
     mv("n11", [52, 26]), ps("b1", [52.6, 26.6], delay=0.2), bl("n11", [50.5, 8], after=True)),
   S("Abschluss: Punkt", "Spieler elf nimmt den Ball mit dem ersten Kontakt in den Strafraum mit und schießt flach ins Eck. Das gibt einen Punkt für Spieler elf. Danach stellt er sich am Start an, Spieler acht rückt auf seinen Platz, und die nächste Runde läuft über die rechte Seite.",
     dr("n11", "b1", [51, 18]), ps("b1", [55.5, 5.3], after=True))],
  "dims": dims(27.5, 72.5, 5, 55, "37 m", "41 m", rx=80)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Den Ball vor den Läufer spielen.", "Vor den Läufer spielen",
    "Die Ablage kommt nicht in die Füße, sondern ein Stück vor den Läufer in den freien Raum. So muss er nicht abbremsen und kann den Schwung bis zum Abschluss mitnehmen. Ein Pass hinter den Läufer macht den Angriff langsam.",
    sp(n11=(50, 36.5)), [B("b1", 39.6, 27.1)] + ERSATZ,
    [S("In den Lauf", "Spieler neun spielt den Ball nicht in die Füße, sondern ein Stück vor Spieler elf in den freien Raum. So muss Spieler elf nicht abbremsen.",
       mv("n11", [52, 22]), ps("b1", [52.6, 22.6], delay=0.2)),
     S("Ohne Abbremsen: Punkt", "Spieler elf schaut kurz zum Torwart und schießt ohne abzubremsen ins lange Eck. Das gibt einen Punkt für Spieler elf.",
       bl("n11", [50.5, 6]), ps("b1", [44.5, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Alle vier Spieler an den Stangen sind dabei.", "Alle vier spielen mit",
    "Jetzt kommen alle vier Spieler an den Stangen in die Passfolge, und es wird möglichst direkt gespielt. Der Ball geht quer, zur Spitze, zum anderen Stangen-Spieler und dann zurück in den Lauf des dritten Mannes. Der schießt direkt, ohne den Ball anzunehmen.",
    sp(), [B("b1", 49.6, 55.6)] + ERSATZ,
    [S("Quer spielen", "Spieler acht spielt zu Spieler elf, und Spieler elf spielt direkt quer zu Spieler sieben.",
       ps("b1", [39.6, 43.1]), ps("b1", [61.6, 43.1], after=True)),
     S("Zur Spitze", "Spieler sieben spielt schräg zu Spieler neun. Gleichzeitig startet Spieler elf hinten herum Richtung Mitte.",
       ps("b1", [39.6, 27.1]), mv("n11", [45, 47.5], delay=0.2), mv("n11", [50, 43], after=True)),
     S("Weiter und ablegen", "Spieler neun spielt direkt zu Spieler zehn, und Spieler zehn legt den Ball zurück in den Lauf von Spieler elf.",
       ps("b1", [61.6, 27.1]), mv("n11", [51, 24], delay=0.4), ps("b1", [51.6, 24.6], after=True)),
     S("Direkt abschließen: Punkt", "Spieler elf schaut kurz zum Torwart und schießt direkt, ohne den Ball anzunehmen. Das gibt einen Punkt für Spieler elf. Danach rücken alle eine Position weiter.",
       bl("n11", [50.5, 6.5]), ps("b1", [45, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
