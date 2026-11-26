import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# PS-115 (U15-U17, Woche 1 Pre-Season): SAQ, Combine and Cross to Finish. Skizze 30 x 25 Yards = Feld x 20-80, y 5-55 (27 x 23 m),
# Tor oben mit neutralem Torwart (Großfeldtor, nur C- und B-Jugend). Ein Team (Neon), Nummern wie in der Skizze, in der Steigerung
# ein Verteidiger von Team Rot (Nummer 5 wie im Video). Nicht gedreht. Ein Trainer statt zwei.
# Wartende (10, 7, 4, 3) neben das Feld gesetzt und Leiter/Startpunkt links etwas auseinandergezogen (3D-Abstand).
# Kein Sichtkegel im Video eingezeichnet; Sichtkegel aus Text und Ton ("Scanning and Decision Making in Wide Areas",
# "wide players must scan early and often before crossing"): Flügelspieler schaut vor der Flanke in den Strafraum.
# Kein Dubletten-Fall: UE-140 (PS-97) und UE-141 (PS-99) haben andere Stationen und andere Passfolgen.
T = P("T", "c", 7, 12, "T")
TW = P("k", "t", 50.9, 7.3, "TW")
POS = {"n9": (27, 21), "n8": (27, 37), "n6": (50.3, 48.5), "n11": (74.5, 48.5),
       "n10": (18, 21), "n7": (18, 37), "n4": (60, 53.5), "n3": (84, 51)}
def sp(extra=(), **k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + list(extra) + [TW, T]
ERSATZ = [B("s1", 8.6, 15.5), B("s2", 10, 9)]
LINES = [rect(20, 5, 60, 50), rect(31, 5, 39, 13.6), rect(40.5, 5, 19.5, 5.5), line(69.7, 18.6, 69.7, 55)]
KEGEL = [leiter(39.5, 21), C(52, 20.5, shape="stange"), C(31, 44, shape="stange"),
         C(56.5, 45, shape="huerde"), C(59.5, 42.5, shape="huerde"), C(62.5, 40, shape="huerde"),
         C(75, 42.5, shape="stange"), C(75, 36, shape="stange"), C(75, 29.5, shape="stange"),
         C(23, 24.5, "neon"), C(23, 40.5, "neon"), C(46, 50.5, "neon"), C(79, 53, "neon")]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}]
def weg(who, pkt, **k): return [mv(who, pkt[0], **k)] + [mv(who, p, after=True) for p in pkt[1:]]
STANGE = [[27.5, 43], [30, 47.5], [34, 46], [43.5, 37.6]]
LEITER = [[47.5, 21.5], [49, 26], [52, 29.5]]
HUERDEN = [[56.5, 45], [59.5, 42.5], [62.5, 40], [65.5, 37.5]]
SLALOM = [[78, 43.5], [75, 39.3], [72, 36], [75, 32.8], [78, 29.5], [78, 25]]
# Stand nach den Laufaufgaben (Start beider Fassungen): Ball bei Spieler acht in der Mitte.
NACH = {"n9": (52, 29.5), "n8": (43.5, 37.6), "n6": (65.5, 37.5), "n11": (78, 25)}
R5 = P("r5", "b", 60.5, 14, "5")

u = {"title": "Laufen, kombinieren, flanken", "code": "UE-298", "kind": "Übungsform",
 "focuses": ["Passspiel", "Torschuss", "Koordination"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "tags": ["Vorbereitung"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "25 x 25 m",
 "description": "Jeder Spieler beginnt mit einer kurzen, schnellen Laufaufgabe an Leiter, Stangen oder Hürden. Danach läuft der Ball über drei Pässe nach vorn, steil, abgelegt und tief auf den Flügel. Der Flügelspieler flankt, drei Angreifer laufen in den Strafraum und schließen ab. Jeder Treffer gibt einen Punkt, das hält das Tempo hoch.",
 "organisation": ["Aufbauen: Ein Feld von etwa 25 mal 25 Metern mit Tor und Torwart. Links oben eine Leiter und dahinter eine Stange, links unten eine Stange, in der Mitte drei Minihürden, rechts außen drei Stangen für den Slalom. An jeder Station ein Hütchen als Startpunkt.",
  "Verteilen: Mindestens acht Spieler, zwei an jeder Station. Die Bälle liegen an der Station links. Der Trainer steht mit Ersatzbällen am Rand.",
  "Ablauf: Pass nach unten in die Mitte, dann läuft jeder seine Aufgabe. Der Ball geht steil nach vorn, wird abgelegt und tief auf den Flügel gespielt. Flanke, drei Angreifer im Strafraum, Abschluss.",
  "Wechsel: Nach jedem Angriff rückt jeder eine Station weiter. Jeder Treffer gibt einen Punkt."],
 "organisation_show": ORG,
 "coaching_points": ["Volles Tempo an Leiter, Stangen und Hürden", "Flanke in den Lauf, nicht in den Rücken", "Einer kurz, einer lang", "Kopf hoch vor der Flanke"],
 "materials": ["1 Tor", "1 Koordinationsleiter", "5 Stangen", "3 Minihürden", "4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Laufen, kombinieren, flanken. Erst kommt die schnelle Laufaufgabe, dann drei Pässe und die Flanke in den Strafraum.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(),
  "balls": [B("b1", 27.6, 37.6), B("b2", 18.6, 37.6)] + ERSATZ,
  "steps": [
   S("Pass, dann um die Stange", "Spieler acht spielt flach zu Spieler sechs und sprintet sofort um die Stange. Gleichzeitig läuft Spieler neun durch die Leiter.",
     ps("b1", [50.9, 49.1]), *weg("n8", STANGE, delay=0.3), *weg("n9", LEITER, delay=0.3)),
   S("Steil und ablegen", "Jetzt geht der Ball nach vorn auf Spieler neun. Der legt mit einem Kontakt ab auf Spieler acht. Spieler sechs geht über die Hürden, und außen läuft Spieler elf im Slalom durch die Stangen.",
     ps("b1", [52.6, 30.1]), ps("b1", [44.1, 38.2], after=True), *weg("n6", HUERDEN, delay=0.5), *weg("n11", SLALOM, delay=0.2)),
   S("Tiefer Pass auf den Flügel", "Spieler acht spielt den Ball tief in den Lauf von Spieler elf. Die drei anderen starten in den Strafraum.",
     ps("b1", [76.6, 19.6]), mv("n11", [76, 19]), mv("n9", [58, 12], delay=0.3), mv("n8", [44.6, 17], delay=0.3), mv("n6", [60, 24], delay=0.3)),
   S("Kopf hoch, dann flanken", "Kopf hoch. Spieler elf sieht Spieler neun am kurzen Pfosten und flankt.",
     bl("n11", [58, 12]), ps("b1", [58.6, 12.6], after=True)),
   S("Abschluss: Punkt", "Spieler neun nimmt die Flanke direkt und trifft, und das gibt einen Punkt für Team Neon. Danach rückt jeder eine Station weiter, und Spieler sieben startet mit dem nächsten Ball.",
     ps("b1", [56, 5.3]))],
  "dims": dims(20, 80, 5, 55, "25 m", "25 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Gegenläufig in den Strafraum.", "Gegenläufig in den Strafraum",
    "Laufen beide Angreifer in dieselbe Richtung, hat es jeder Verteidiger leicht. Darum geht einer kurz und einer lang. Und sie starten erst, wenn der Flügelspieler den Ball hat. Wer zu früh im Strafraum ist, steht und wartet.",
    sp(**NACH), [B("b1", 44.1, 38.2), B("b2", 18.6, 37.6)] + ERSATZ,
    [S("Erst der Pass, dann der Lauf", "Der Ball geht tief auf Spieler elf. Erst jetzt starten die Angreifer. Spieler neun zieht zum langen Pfosten, Spieler acht kreuzt hinter ihm zum kurzen.",
       ps("b1", [76.6, 19.6]), mv("n11", [76, 19]), mv("n9", [47, 22], delay=0.5), mv("n9", [43, 14], after=True),
       mv("n8", [47, 27], delay=0.6), mv("n8", [48.5, 18], after=True), mv("n8", [58, 12], after=True), mv("n6", [60, 24], delay=0.6)),
     S("Flanke kurz: Punkt", "Spieler elf flankt flach vor den kurzen Pfosten. Spieler acht kommt in vollem Lauf und schiebt ein, und das gibt einen Punkt für Team Neon.",
       ps("b1", [58.6, 12.6]), ps("b1", [54, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger steht im Strafraum.", "Mit Verteidiger im Strafraum",
    "Ein Verteidiger von Team Rot wartet im Strafraum und verteidigt die Flanke. Die Angreifer lösen sich mit ihren Läufen von ihm. Der Flügelspieler schaut früh, wo der Verteidiger steht, und flankt in den Raum weg von ihm.",
    sp(extra=[R5], **NACH), [B("b1", 44.1, 38.2), B("b2", 18.6, 37.6)] + ERSATZ,
    [S("Pass auf den Flügel, Blick zur Mitte", "Spieler acht spielt wieder tief auf Spieler elf. Noch vor der Flanke schaut Spieler elf in die Mitte. Wo steht Spieler fünf?",
       ps("b1", [76.6, 19.6]), mv("n11", [76, 19]), bl("n11", [60.5, 14], after=True)),
     S("Der kurze Pfosten ist zu", "Spieler neun läuft kurz, und Spieler fünf macht den kurzen Pfosten zu. Hinten am langen Pfosten wird Spieler acht frei.",
       mv("n9", [64.5, 14]), mv("r5", [60.5, 10], delay=0.2), mv("n8", [43, 15], delay=0.2), mv("n6", [58, 25], delay=0.2)),
     S("Flanke weg vom Verteidiger: Punkt", "Spieler elf flankt über beide hinweg an den langen Pfosten. Spieler acht trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", [43.6, 15.6]), ps("b1", [46.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
