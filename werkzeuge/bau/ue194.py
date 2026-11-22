import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 95-P4 (U12-U14, Woche 23 Phase 3): 231 Central Build-Up Play to Finish. 20 x 30 Yards = Feld x 33-67, y 5-53 (18 x 27 m),
# oben ein Jugendtor mit neutralem Torwart (Orientierung wie im PDF, nicht gedreht). Drei Dummys als Stangen (vor der Neun,
# vor der Zehn, unten links vor der Acht), zwei gelbe Hütchen -> neon. Alle Feldspieler pink -> Team Neon (4, 6, 7, 8, 9, 10, 11,
# Nummern wie im PDF), der grüne Torwart neutral (k, TW). Trainer links statt rechts (rechts steht Spieler sechs mit Bällen).
# Abschluss wie im PDF-Bild: Flanke von Spieler elf an den langen Pfosten zu Spieler sieben, Spieler neun dreht sich um die Stange zum
# kurzen Pfosten. Rotation im Video: jeder rückt eine Position weiter, Spieler sechs startet den nächsten Angriff (nur im Text).
# Sichtkegel: Video-Schlusspunkt "Quality of final ball and decision to pick out player": Spieler elf schaut vor der Flanke zum langen
# Pfosten. Steigerung frei nach dem Video ("set, through ball, third-man run from midfield"), Abfolge vereinfacht.
T = P("T", "c", 25, 38, "T")
POS = {"k": (50, 8.5), "n9": (46, 25.5), "n11": (36, 25), "n7": (64, 25), "n10": (54, 41.5), "n8": (38, 50), "n4": (62.5, 50.5),
       "n6": (71.5, 54)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i == "k" else "a", x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 28.6, 41.5), B("s2", 25, 41.5)]
LINES = [rect(33, 5, 34, 48)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(49, 19.5, shape="stange"), C(52, 35, shape="stange"), C(43.5, 45, shape="stange"), C(39.5, 25.5, "neon"), C(60.5, 25.5, "neon")]

u = {"title": "Durch die Mitte zum Abschluss", "code": "UE-194", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 12, "field_size": "18 x 27 m",
 "description": "Ein Angriff wird über die Mitte aufgebaut und mit einer Flanke abgeschlossen. Der Ball läuft von hinten über die Zehn zurück zur Acht, dann in die Spitze zur Neun und nach außen zum Flügel. Der Flügel flankt, die Neun dreht sich in den Strafraum, und der andere Flügel kommt an den langen Pfosten. Danach rücken alle eine Position weiter.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 27 Metern mit einem Jugendtor oben. Drei Stangen als Gegenspieler in der Mitte und unten links, zwei Hütchen für die Flügel.",
  "Verteilen: Ein Torwart steht im Tor. Team Neon besetzt sieben Positionen: vier und acht hinten, zehn in der Mitte, neun vorn, elf und sieben außen. Spieler sechs wartet rechts mit Bällen, der Trainer steht links.",
  "Ablauf: Spieler vier spielt zu Spieler zehn, der lässt zu Spieler acht abprallen. Spieler acht spielt in die Spitze zu Spieler neun, der spielt direkt nach außen zu Spieler elf. Spieler elf flankt, Spieler neun und Spieler sieben laufen in den Strafraum.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für Team Neon. Danach rücken alle eine Position weiter, und der nächste Angriff startet. Ab und zu auf der anderen Seite beginnen."],
 "organisation_show": ORG,
 "coaching_points": ["Saubere Pässe und Ballannahme bestimmen das Tempo", "Erst weglaufen, dann anbieten", "Die Läufe so starten, dass der Ball im Lauf kommt", "Nach dem Pass sofort in den Strafraum, gut flanken und ruhig abschließen"],
 "materials": ["1 Jugendtor", "3 Stangen", "2 Hütchen", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Durch die Mitte zum Abschluss. Team Neon spielt den Ball durch die Mitte nach vorn und schließt nach einer Flanke ab.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 63.1, 51.1)] + ERSATZ,
  "steps": [
   S("Abprallen lassen", "Spieler vier spielt in die Mitte zu Spieler zehn. Gleichzeitig läuft Spieler acht kurz weg und kommt wieder zurück. Spieler zehn lässt den Ball direkt zu Spieler acht abprallen.",
     ps("b1", [54.6, 42.1]), mv("n8", [35.5, 44]), mv("n8", [38.5, 50], after=True), ps("b1", [39.1, 50.6], after=True)),
   S("In die Spitze", "Spieler acht spielt den Ball nach vorn in die Spitze zu Spieler neun.",
     ps("b1", [46.6, 26.1])),
   S("Direkt nach außen", "Spieler elf läuft nach vorn, und Spieler neun spielt den Ball direkt zu ihm nach außen.",
     mv("n11", [38, 15.5]), ps("b1", [38.6, 16.1], delay=0.3)),
   S("Flanke: Punkt", "Spieler neun dreht sich um die Stange in den Strafraum, Spieler sieben läuft an den langen Pfosten. Spieler elf schaut hoch und flankt zu Spieler sieben. Der schießt direkt ins Tor, und das gibt einen Punkt für Team Neon. Danach rücken alle eine Position weiter, und Spieler sechs startet den nächsten Angriff.",
     mv("n9", [53.5, 21]), mv("n9", [51, 13.5], after=True), mv("n9", [45.5, 11.5], after=True), mv("n7", [57.5, 14.5]),
     bl("n11", [56, 14.5], after=True), ps("b1", [58.1, 15.1], after=True), ps("b1", [53.5, 5.4], after=True))],
  "dims": dims(33, 67, 5, 53, "18 m", "27 m", rx=78)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Erst weglaufen, dann anbieten.", "Weg und zurück",
    "Wer sich anbietet, läuft zuerst ein Stück weg, als würde er seinen Gegenspieler mitnehmen. Dann kommt er schnell zurück und zeigt sich. So ist er frei, wenn der Pass kommt.",
    sp(), [B("b1", 38.6, 50.6)] + ERSATZ,
    [S("Erst weg", "Spieler acht hat den Ball. Spieler neun läuft erst weg, hinter die Stange, als ob er seinen Gegenspieler mitnimmt.",
       mv("n9", [45, 17.5])),
     S("Dann zeigen", "Dann kommt Spieler neun schnell zurück und zeigt sich. Jetzt ist er frei, und Spieler acht spielt ihn an.",
       mv("n9", [47, 26]), ps("b1", [47.6, 26.6], delay=0.3)),
     S("Direkt weiter", "Spieler neun spielt direkt weiter zu Spieler elf, und der Angriff läuft weiter wie in der Grundform.",
       mv("n11", [38, 15.5]), ps("b1", [38.6, 16.1], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Der dritte Mann kommt aus dem Mittelfeld.", "Der dritte Mann",
    "Jetzt wechseln die Spieler die Abfolge. Spieler acht spielt gleich in die Spitze, Spieler neun legt ab, und Spieler acht startet nach vorn. Der Steilpass kommt in seinen Lauf, und er schließt selbst ab.",
    sp(), [B("b1", 38.6, 50.6)] + ERSATZ,
    [S("In die Spitze", "Spieler acht spielt gleich in die Spitze zu Spieler neun.",
       ps("b1", [46.6, 26.1])),
     S("Ablegen", "Spieler zehn rückt nach, und Spieler neun legt den Ball zu ihm ab. Gleichzeitig startet Spieler acht aus dem Mittelfeld nach vorn.",
       mv("n10", [55, 33]), ps("b1", [55.6, 33.6], after=True), mv("n8", [42, 30])),
     S("Steilpass: Punkt", "Spieler zehn spielt steil in den Lauf von Spieler acht. Spieler acht nimmt den Ball mit und schießt ins Tor, und das gibt einen Punkt für Team Neon.",
       mv("n8", [43, 16]), ps("b1", [43.6, 16.6], delay=0.3), ps("b1", [47, 5.4], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
