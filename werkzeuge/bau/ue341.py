import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 49-P8 (U15-U17, Woche 8 Phase 4): Press to Win Possession Counter (im PDF „Press as a Unit to Win Possession & Counter“).
# 30 x 35 Yards = 27 x 32 m (gerundet 25 x 30 m), Ballbesitzzone 20 x 15 Yards = 18 x 14 m an einem Ende, großes Tor mit
# Torwart am anderen Ende.
# QUER GELEGT (PDF 90 Grad im Uhrzeigersinn gedreht): Ballbesitzzone links, großes Tor rechts, Team Neon kontert nach rechts.
# Das Feld ist kaum länger als breit, liegt aber quer, weil die neun Spieler in der Zone hochkant für den 3D-Abstand keinen Platz
# haben (quer passen drei Reihen hintereinander). Feld x 13-85, y 4-51 (in der Länge etwas gestreckt), Zone x 13-46, y 11.8-43.2
# (in der Tiefe ebenfalls leicht gestreckt). Strafraum und Torraum wie im PDF verkleinert gezeichnet, Teilkreis weggelassen.
# Drei Teams zu dritt: Blau (presst, wird trainiert) -> Team Neon 4, 8, 9 (Nummern wie im PDF). Gold (verliert den Ball und
# verteidigt dann das Tor) -> Team Rot, neu nummeriert wegen doppelter Nummern: 4 -> 5, 9 -> 7, 6 bleibt 6.
# Pink (drittes Team, hilft beim Ballhalten) -> neutrale Farbe (team t) mit Nummern wie bei UE-330: 2 und 11 bleiben, 4 -> 10.
# Torwart neutral (TW). Ein Trainer statt zwei (unten an der Seitenlinie neben der Zone).
# Ablauf nach PDF (Gold 4 spielt quer auf Gold 6, Blau fängt ab, drei gegen drei aufs Tor). Im Video verliert dagegen Pink
# den Ball; hier wie im PDF. Positionen in der Zone für den 3D-Abstand in Spalten geordnet.
# Fassungen: PDF Progression 1 (zwei Minitore an den Seiten für Team Rot nach Ballgewinn im drei gegen drei) und
# Progression 2 (ein Spieler des dritten Teams läuft mit zurück, Team Neon kontert drei gegen vier).
# Sichtkegel aus dem Ton („reading the play, anticipating passes“): Spieler acht beobachtet den Ballführer, bevor er in den
# Passweg geht. Im Video kein Kegel eingezeichnet. Neue Kegel-Regel (25.11.2026): Kegel gestrichen (Spieler acht passt danach
# nicht selbst, er fängt ab), das Lesen steht nur noch im Text.
# Keine Dublette: UE-096 (zwei Hälften mit Minitoren), UE-238 (drei Stürmer gegen vier, Konter auf Torwart und Minitore),
# UE-187 (Dreiecke mit Springern) haben keine drei Teams mit Zehn-Pässe-Wertung und Konter des pressenden Teams.
T = P("T", "c", 17, 55.3, "T")  # unten an der Seitenlinie neben der Zone
ERSATZ = [B("s1", 20.5, 55.8), B("s2", 23, 55.8)]
POS = {"k": (79, 27.5), "n9": (21.5, 27), "n4": (38.5, 18), "n8": (38.5, 36),
       "r5": (13, 16), "r6": (30, 44.5), "r7": (47, 37), "t2": (13, 38), "t10": (47, 18), "t11": (30, 10.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "t": "t", "k": "t"}[i[0]], x, y, "TW" if i == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
ZONE = {"type": "zone", "x": 13, "y": 11.8, "w": 33, "h": 31.4}
LINES = [rect(13, 4, 72, 47), ZONE, rect(65, 13.9, 20, 27.2), rect(76, 20, 9, 15)]
TOR = {"x": 85, "y": 27.5, "side": "right", "size": "gross"}
MINI = [{"x": 52, "y": 4, "side": "top"}, {"x": 52, "y": 51, "side": "bottom"}]
DIMS = dims(13, 85, 4, 51, "30 m", "25 m")[:1]  # nur die Länge (rechts steht das Tor), die Breite steht in field_size

u = {"title": "Als Einheit pressen und kontern", "code": "UE-341", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 10, "players_max": 12,
 "field_size": "25 x 30 m",
 "description": "Drei Teams zu dritt und ein Torwart. In der Ballbesitzzone halten zwei Teams zusammen den Ball gegen Team Neon, zehn Pässe in Folge geben einen Punkt. Team Neon presst als Einheit, und nach dem Ballgewinn geht es sofort drei gegen drei aufs große Tor. Verteidigen muss das Team, das den Ball verloren hat.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern. An einem Ende liegt die Ballbesitzzone, etwa 18 mal 14 Meter groß. Am anderen Ende steht das große Tor mit Torwart.",
  "Verteilen: Drei Teams zu dritt. Team Rot und das dritte Team stehen außen an der Zone, Team Neon presst innen. Der Trainer steht mit Bällen neben der Zone.",
  "Ablauf: Sechs gegen drei in der Zone. Erobert Team Neon den Ball, kontert es sofort drei gegen drei aufs große Tor. Das Team, das den Ball verloren hat, sprintet zurück und verteidigt.",
  "Wertung und Wechsel: Zehn Pässe in Folge geben einen Punkt für die Ballbesitzer, jeder Treffer im Konter einen Punkt für Team Neon. Danach geht das Team, das den Ball verloren hat, in der Zone in die Mitte und presst."],
 "organisation_show": ORG,
 "coaching_points": ["Zu dritt pressen, die Passwege zustellen", "Sofort drauf, keine Zeit am Ball lassen", "Ball gewonnen? Sofort Richtung Tor", "Wer den Ball verliert, sprintet zurück"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Zone", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Als Einheit pressen und kontern. Drei Teams zu dritt. Team Neon presst in der Zone, erobert den Ball und kontert sofort drei gegen drei.",
 "board": {"lines": LINES, "goals": [TOR], "cones": [], "players": sp(), "balls": [B("b1", 30.6, 11.1)] + ERSATZ,
  "steps": [
   S("Sechs gegen drei in der Zone", "Team Rot und das dritte Team halten zusammen den Ball. Zehn Pässe in Folge, und das gibt einen Punkt für sie. Spieler elf spielt zu Spieler fünf.",
     ps("b1", fu(POS["r5"]))),
   S("Zu dritt pressen", "Jetzt geht Spieler neun von der Seite drauf. Spieler vier stellt den Rückpass zu. Spieler acht ahnt, wohin der Ball als Nächstes will, und schiebt in den Passweg.",
     mv("n9", [19, 15]), mv("n4", [26, 16.5], delay=0.2), mv("n8", [27.5, 33], delay=0.6)),
   S("Abgefangen, alle umschalten", "Spieler fünf bleibt nur der Pass quer zu Spieler sechs. Spieler acht ist dazwischen. Ab jetzt kontert Team Neon, und Team Rot sprintet zurück und verteidigt.",
     ps("b1", [23.5, 33]), mv("n8", [23, 32.4], delay=0.2), mv("r7", [64, 33], delay=0.6), mv("r6", [60, 44], delay=0.6),
     mv("r5", [24, 23], delay=0.6), mv("r5", [42, 26], after=True), mv("r5", [60, 14], after=True)),
   S("Drei gegen drei: Punkt", "Spieler acht treibt den Ball nach vorn und spielt Spieler vier in den Lauf. Der schießt flach ins Eck, und das gibt einen Punkt für Team Neon. In der nächsten Runde presst Team Rot in der Zone.",
     dr("n8", "b1", [44, 30]), mv("n4", [50, 13], delay=0.2), mv("n4", [64, 20], after=True), mv("n9", [44, 41], delay=0.4),
     ps("b1", fu([64, 20]), delay=1.6), ps("b1", [84.7, 24], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Team Rot darf nach Ballgewinn auf zwei Minitore kontern.", "Minitore für Team Rot",
    "An beiden Seiten steht auf Höhe der Zone ein Minitor. Erobert Team Rot im drei gegen drei den Ball, kontert es sofort auf eines der Minitore. So muss Team Neon auch im Angriff aufpassen und nach Ballverlust gleich wieder umschalten.",
    sp(n8=(58, 21), n4=(60, 40), n9=(49, 30), r7=(49.5, 13), r5=(67, 24), r6=(70, 42), t10=(22, 27)), [B("b1", 58.6, 21.6)] + ERSATZ,
    [S("Konter, Pass in die Mitte", "Team Neon kontert. Spieler acht will in die Mitte zu Spieler neun. Spieler sieben liest den Pass und geht dazwischen.",
       ps("b1", [53.5, 26.5]), mv("r7", [53, 26], delay=0.1)),
     S("Rot kontert aufs Minitor: Punkt", "Jetzt schnell. Spieler sieben dreht sich weg und dribbelt aufs Minitor zu. Er trifft, und das gibt einen Punkt für Team Rot. Danach geht es in der Zone weiter.",
       dr("r7", "b1", [52.5, 11]), mv("n9", [46, 20], delay=0.3), ps("b1", [52, 4.4], after=True))],
    goals=[TOR] + MINI, dims=DIMS),
  V("Steigerung", "Und jetzt die zweite Steigerung: Einer aus dem dritten Team läuft mit zurück.", "Drei gegen vier im Konter",
    "Nach dem Ballgewinn darf ein Spieler aus dem dritten Team mit zurücklaufen und Team Rot helfen. Team Neon kontert jetzt drei gegen vier. Wer da zu lange überlegt, hat den Ball schon wieder verloren, also schnell und direkt spielen.",
    sp(), [B("b1", 13.6, 16.6)] + ERSATZ,
    [S("Abgefangen, vier laufen zurück", "Spieler neun läuft an, und Spieler acht fängt den Querpass ab. Team Rot sprintet zurück, und diesmal läuft Spieler zehn mit.",
       mv("n9", [19, 15]), ps("b1", [23.5, 33], after=True), mv("n8", [23, 32.4], delay=0.3), mv("r7", [64, 33], delay=0.8), mv("t10", [66, 14], delay=0.8),
       mv("r6", [60, 44], delay=0.6), mv("r5", [24, 23], delay=0.6), mv("r5", [42, 26], after=True), mv("r5", [58, 10], after=True)),
     S("Schnell spielen: Punkt", "Spieler acht spielt sofort steil zu Spieler neun. Der legt direkt quer auf Spieler vier, bevor die Verteidiger sortiert sind. Spieler vier trifft, und das gibt einen Punkt für Team Neon.",
       mv("n9", [48, 38]), mv("n4", [50, 22], delay=0.2), ps("b1", fu([48, 38]), delay=0.5),
       ps("b1", fu([50, 22]), after=True), ps("b1", [84.7, 23.5], after=True))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
