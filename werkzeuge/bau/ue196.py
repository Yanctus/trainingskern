import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-27 (U12-U14, Woche 23 Phase 3): Passing Finishing Warm Up. 30 x 25 Yards = Feld x 25-75, y 5-48 (27 x 23 m), oben ein
# Jugendtor mit neutralem Torwart (grün -> k, TW). Orientierung wie im PDF. Blau (7, 8, 10, 9) -> Team Neon, Nummern wie im PDF.
# Rote Hütchen -> orange: Stationen links (oben, Mitte) und unten bei der Neun, rechts die gespiegelten Stationen für die andere
# Seite. Das Hütchen der Neun steht rechts neben ihm statt links (sonst laufen die Pässe hindurch), das Hütchen der Zehn links
# oberhalb. Ballvorrat oben neben dem Tor (je zwei Bälle). Ein Trainer statt zwei (der rechte entfällt), er steht unten links.
# Steigerung nach dem Video: Dreiviertel-Tempo, Doppelpass Zehn-Neun und Steilpass um eine Stange (Dummy) herum.
# Sichtkegel aus dem Text der Steigerung ("improve timing, awareness"): Neon zehn schaut vor dem Steilpass zum Lauf der Neun.
T = P("T", "c", 18, 49, "T")
POS = {"k": (50, 8.5), "n8": (30, 7), "n7": (21, 5), "n10": (29.5, 35), "n9": (53, 39)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t" if i == "k" else "a", x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 21.6, 49), B("s2", 18, 52.5)]
VORRAT = [B("h1", 37, 2.5), B("h2", 39.5, 2.5), B("h3", 61, 2.5), B("h4", 63.5, 2.5)]
LINES = [rect(25, 5, 50, 43)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}]
CONES = [C(32, 5), C(68, 5), C(27, 31.5), C(72, 31.5), C(56.5, 39.5)]

u = {"title": "Passen und Abschließen", "code": "UE-196", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Passspiel", "Torschuss"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 5, "players_max": 10, "field_size": "27 x 23 m",
 "description": "Ein Aufwärmen mit Pass und Torschuss über drei Stationen. Der erste Spieler passt zum Mitspieler am Hütchen und läuft locker hinterher, dabei macht er eine Aufwärmübung. Der Mitspieler spielt steil in den Lauf des Stürmers, und der schießt mit der Innenseite am Torwart vorbei. Danach geht jeder eine Station weiter.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 23 Metern mit einem Jugendtor oben. Hütchen als Stationen oben links, in der Mitte links und unten in der Mitte, rechts die gleichen Stationen für die andere Seite. Neben dem Tor liegen Bälle.",
  "Verteilen: Ein Torwart steht im Tor. Neon acht startet oben links mit Ball, Neon sieben wartet dahinter. Neon zehn steht am Hütchen links, Neon neun unten als Stürmer. Der Trainer steht unten links.",
  "Ablauf: Neon acht passt zu Neon zehn und läuft locker hinterher, dabei macht er eine Aufwärmübung. Neon zehn spielt steil in den Lauf von Neon neun. Neon neun nimmt den Ball mit und schießt mit der Innenseite.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für den Stürmer. Danach geht jeder eine Station weiter, der Stürmer holt einen Ball und stellt sich oben an. Mit jeder Station die Aufwärmübung wechseln."],
 "organisation_show": ORG,
 "coaching_points": ["Zwischen den Stationen sauber und ruhig die Übung machen", "Enger erster Kontakt, genaue Pässe und gute Abschlüsse", "Auch mit mehr Tempo sauber bleiben", "Den Steilpass so spielen, dass der Stürmer ihn im Lauf bekommt"],
 "materials": ["1 Jugendtor", "5 Hütchen", "1 Stange", "Viele Bälle", "Leibchen"],
 "access": "abo", "hidden": True,
 "say_intro": "Passen und Abschließen. Ein Aufwärmen mit Pass, Steilpass und Torschuss, und zwischen den Stationen wird gedehnt.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 30.6, 7.6)] + VORRAT + ERSATZ,
  "steps": [
   S("Pass zur Station", "Neon acht spielt den Ball nach unten zu Neon zehn am Hütchen.",
     ps("b1", [30.1, 35.6])),
   S("Steilpass", "Neon acht läuft locker hinterher und macht dabei eine Aufwärmübung, zum Beispiel Knie hoch. Gleichzeitig startet Neon neun, und Neon zehn spielt steil in seinen Lauf.",
     mv("n8", [31, 27]), mv("n9", [51, 27.5]), ps("b1", [51.6, 28.1], delay=0.3)),
   S("Abschluss: Punkt", "Neon neun nimmt den Ball mit einem Kontakt mit und schiebt ihn mit der Innenseite am Torwart vorbei. Das gibt einen Punkt für Neon neun. Dann geht jeder eine Station weiter: Neon acht zum Hütchen, Neon zehn nach unten, und Neon sieben startet den nächsten Durchgang.",
     dr("n9", "b1", [52, 21]), ps("b1", [54, 5.4], after=True), mv("n10", [48, 42]), mv("n8", [29.5, 35], delay=0.3))],
  "dims": dims(25, 75, 5, 48, "27 m", "23 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Zwischen den Stationen sauber aufwärmen.", "Sauber dehnen",
    "Zwischen den Stationen wird locker gelaufen und gedehnt. Jede Bewegung wird ruhig und sauber gemacht, zum Beispiel Fußspitzen antippen oder Waden dehnen. Mit jeder Station kommt eine neue Übung dran.",
    sp(), [B("b1", 30.1, 35.6)] + VORRAT + ERSATZ,
    [S("Locker laufen", "Neon acht hat den Pass gespielt und läuft locker los. Unterwegs tippt er abwechselnd mit den Fußspitzen auf.",
       mv("n8", [30.5, 17])),
     S("Waden dehnen", "Dann bleibt er kurz stehen und dehnt ruhig die Waden. Erst danach läuft er weiter zur nächsten Station. Dort wartet schon die nächste Übung.",
       mv("n8", [31, 27], delay=0.8))]),
  V("Steigerung", "Und jetzt die Steigerung: Mehr Tempo und ein Doppelpass an der Stange.", "Doppelpass und Tempo",
    "Jetzt laufen alle mit Dreiviertel-Tempo zwischen den Stationen. In der Mitte steht eine Stange. Neon zehn und Neon neun spielen einen Doppelpass, dann kommt der Steilpass um die Stange herum.",
    sp(), [B("b1", 30.1, 35.6)] + VORRAT + ERSATZ,
    [S("Zu Neon neun", "Neon acht läuft jetzt mit Dreiviertel-Tempo hinterher. Neon zehn spielt flach zu Neon neun.",
       mv("n8", [31, 27]), ps("b1", [53.6, 39.6])),
     S("Doppelpass", "Neon zehn läuft nach vorn, und Neon neun spielt den Ball direkt zu ihm zurück.",
       mv("n10", [44, 35]), ps("b1", [44.6, 35.6], delay=0.4)),
     S("Steilpass: Punkt", "Neon neun läuft rechts an der Stange vorbei. Neon zehn schaut hoch und spielt steil in seinen Lauf. Neon neun schiebt den Ball mit der Innenseite ins Tor, und das gibt einen Punkt für Neon neun.",
       mv("n9", [57, 30]), mv("n9", [54, 21], after=True), bl("n10", [55, 22]), ps("b1", [54.6, 21.6], delay=0.5),
       ps("b1", [53.5, 5.4], after=True))],
    cones=[dict(c, id=f"c{i + 1}") for i, c in enumerate(CONES + [C(47, 27, shape="stange")])])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
