import json, math, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 28-P10 (U15-U17, Woche 19 Phase 1): How to Build from the Back in a 433, Phase of Play. 30 x 50 Yards = 27 x 46 m
# (gerundet 25 x 45 m). LANGES FELD QUER (Verhältnis 1,67, Vorbild ue317.py): Feld x 9-89, y 4-51, großes Tor links, die zwei
# Minitore rechts, wie im Video. Koordinaten direkt quer aus der PDF-Skizze umgerechnet: PDF unten -> links, oben -> rechts,
# PDF links -> oben, PDF rechts -> unten. Kein Großfeld (45 m lang), Figuren normal groß. Nur die Längen-Maßlinie unten.
# Platzlinien wie im PDF: Mittellinie und Mittelkreis des Spielfelds, Strafraum und Torraum (Teilkreis am Strafraum weggelassen).
# Gestrichelt: die Linie vor den beiden Außenzonen über die ganze Breite und die zwei Außenzonen (Minitore am Ende der Zonen).
# Pink (Torwart, Viererkette 6, 5, 3, 2, Flügel 7 und 11) -> Team Neon, Nummern wie im PDF, Torwart n1 „TW“.
# Gold (Floater, im Ton „our CDM“) -> Springer F (spielt für das Team in Ballbesitz, wie im Text: Rot kontert über ihn).
# Blau (Stürmer 10, 9; je zwei Verteidiger in den Außenzonen) -> Team Rot, neu nummeriert, weil die Nummern doppelt sind:
# Blau 2 -> 12, Blau 3 -> 13, Blau 7 -> 14, Blau 11 -> 15; 9 und 10 bleiben. Großfeldtor (nur C- und B-Jugend).
# Positionen grob wie im PDF, für den 3D-Abstand leicht verschoben (Innenverteidiger weiter vor den Torwart, Spieler zwei weiter
# vorn, Spieler elf und Rot 14 auseinander). Ein Trainer statt zwei, unten an der Seitenlinie.
# Grundform = PDF-Skizze und Video 0:04-0:18: Torwart -> 5 -> 2 -> Springer -> Verlagerung auf 3, der in die Außenzone startet,
# dann zwei gegen zwei mit 11 aufs Minitor (Doppelpass ergänzt, im Original nur „quick combinations“).
# Fassung 1 = PDF Key Coaching Point 1 (zwei gegen zwei auf der anderen Seite: Doppelpass, Hinterlaufen, Abschluss),
# Fassung 2 = Key Coaching Point 2 (Stürmer stehen zu weit auseinander: Torwart spielt flach durch auf den Springer).
# Sichtkegel aus Text und Ton („awareness“, „recognise when spaces are created“), im Video nicht eingezeichnet:
# Der Springer schaut zum Passgeber, nimmt an, dann schwenkt der Kegel zur Verlagerung (bl mit von) und er dreht auf (drehen);
# in Fassung 1 schaut Spieler sieben vor dem Pass in den Lauf von Spieler zwei; in Fassung 2 sieht der Torwart die Lücke.
# Konter von Team Rot über den Springer und „nur eine Verlagerung“ (Ton) nur im Text.
def fu(p): return [round(p[0] + 0.6, 1), round(p[1] + 0.6, 1)]
def richt(a, b, d=21):
    # Blickkegel nicht zu lang: Punkt in Richtung b, etwa 21 Einheiten von a entfernt
    l = math.dist(a, b)
    return [round(a[0] + (b[0] - a[0]) * d / l, 1), round(a[1] + (b[1] - a[1]) * d / l, 1)]
T = P("T", "c", 30, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 33.5, 55.8), B("s2", 36, 55.8)]
POS = {"n1": (12, 27.5), "n6": (21, 22.5), "n5": (21, 38.5), "n3": (22, 6.5), "n2": (40, 48), "n11": (57, 12), "n7": (54, 48.2),
       "f": (50, 31), "r10": (31, 19.5), "r9": (31, 36), "r14": (66, 6), "r12": (76, 15), "r13": (74.6, 41.6), "r15": (63.6, 48)}
def sp(pos=POS, **k):
    d = dict(pos); d.update(k)
    return [P(i, "t", x, y, "F") if i == "f" else P(i, "a" if i[0] == "n" else "b", x, y, "TW" if i == "n1" else i[1:])
            for i, (x, y) in d.items()] + [T]
LINES = [rect(9, 4, 80, 47), line(60.3, 4, 60.3, 51, dashed=False), {"type": "circle", "x": 60.3, "y": 27.5, "r": 7.3},
         rect(9, 12.5, 16, 29.5), rect(9, 20, 5.7, 15),
         line(43.4, 4, 43.4, 51), line(43.4, 16.2, 81, 16.2), line(43.4, 38.3, 81, 38.3), line(81, 4, 81, 16.2), line(81, 38.3, 81, 51)]
TORE = [{"x": 9, "y": 27.5, "side": "left", "size": "gross"}, {"x": 81, "y": 10, "side": "right"}, {"x": 81, "y": 44.6, "side": "right"}]
DIMS = dims(9, 89, 4, 51, "45 m", "25 m")[:1]  # nur die Länge (rechts stehen die Minitore), die Breite steht in field_size
START = [B("b1", *fu(POS["n1"]))] + ERSATZ
LAUF3 = (44, 10)  # Spieler drei startet bis an die Außenzone
# Fassung 2: Die Spitzen laufen die Innenverteidiger an und stehen weit auseinander
POS2 = dict(POS, n6=(14, 8), n5=(14, 47), n3=(34, 6), n2=(40, 49), r10=(24, 17), r9=(24, 38), f=(46, 27.5))

u = {"title": "Aufbau gegen zwei Spitzen", "code": "UE-351", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Passspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 16,
 "field_size": "25 x 45 m",
 "description": "Team Neon baut mit Torwart und Viererkette gegen zwei Stürmer von Team Rot auf. Ziel ist der Springer in der Mitte, der in eine der beiden Außenzonen verlagert. Dort greifen Außenverteidiger und Flügelspieler zu zweit gegen zwei Verteidiger an und schließen auf ein Minitor ab. Pro Angriff gibt es nur eine Verlagerung.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 45 Metern. An einem Ende steht ein großes Tor mit Strafraum, am anderen Ende zwei Minitore. Davor sind außen zwei Zonen abgesteckt, eine gestrichelte Linie markiert ihren Anfang.",
  "Verteilen: Team Neon mit Torwart, Viererkette und zwei Flügelspielern, in der Mitte ein Springer. Team Rot presst mit zwei Stürmern, in jeder Außenzone verteidigen zwei Spieler. Der Trainer steht mit Bällen an der Seitenlinie.",
  "Ablauf: Der Torwart eröffnet, Team Neon spielt sich gegen die zwei Stürmer frei und findet den Springer. Der verlagert in eine Außenzone, und ein Außenverteidiger kommt zum Flügelspieler. Erobert Team Rot den Ball, spielt es mit dem Springer und kontert aufs große Tor.",
  "Wertung: Ein Treffer ins Minitor gibt einen Punkt für Team Neon, ein Treffer ins große Tor gibt einen Punkt für Team Rot. Jeder Angriff beginnt wieder beim Torwart."],
 "organisation_show": ORG,
 "coaching_points": ["Breit machen und gute Passwinkel anbieten", "Stehen die Spitzen weit auseinander, flach durch zum Springer", "Außen zu zweit schnell kombinieren", "Nichts frei? Zurückspielen und neu aufbauen"],
 "materials": ["1 großes Tor", "2 Minitore", "Hütchen für die Zonen", "Leibchen in drei Farben", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbau gegen zwei Spitzen. Team Neon spielt sich vom Torwart aus gegen zwei Stürmer frei, verlagert über den Springer und greift außen zu zweit an.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": START,
  "steps": [
   S("Torwart eröffnet", "Der Torwart beginnt. Er spielt flach zu Spieler fünf. Spieler neun läuft sofort an.",
     ps("b1", fu(POS["n5"])), mv("r9", [27, 34], delay=0.5)),
   S("Raus auf Spieler zwei", "Spieler fünf spielt weiter nach außen auf Spieler zwei. Auf der anderen Seite schiebt Spieler drei schon nach vorn.",
     ps("b1", fu(POS["n2"])), mv("n3", list(LAUF3), delay=0.3)),
   S("Der Springer zeigt sich", "Der Springer kommt dem Ball entgegen und schaut zu Spieler zwei. Der spielt ihn flach an.",
     bl("f", list(POS["n2"])), ps("b1", fu(POS["f"]), after=True)),
   S("Verlagern auf die andere Seite", "Jetzt geht der Blick rüber. Der Springer dreht auf und verlagert auf Spieler drei, der an der Außenzone ankommt.",
     bl("f", richt(POS["f"], LAUF3), von=richt(POS["f"], POS["n2"]), dauer=1.3), drehen("f", list(LAUF3), delay=0.4),
     ps("b1", fu(LAUF3), after=True)),
   S("Doppelpass in der Außenzone", "Zwei gegen zwei in der Außenzone. Spieler drei spielt auf Spieler elf und startet an Spieler vierzehn vorbei. Spieler elf legt in den Lauf.",
     ps("b1", fu(POS["n11"])), mv("r14", [62, 14.5], delay=0.3), mv("n3", [55, 5], delay=0.2), mv("n3", [68, 6], after=True),
     ps("b1", [68.6, 6.6], after=True)),
   S("Abschluss: Punkt", "Spieler drei schiebt ins Minitor, und das gibt einen Punkt für Team Neon. Danach beginnt der Torwart mit dem nächsten Ball.",
     mv("r12", [76, 12], delay=0.1), ps("b1", [80.4, 9.4]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Außen zu zweit schnell kombinieren.", "Zu zweit über außen",
    "In der Außenzone heißt es zwei gegen zwei. Wer lange dribbelt, verliert den Ball. Schneller geht es mit einem Doppelpass und einem Lauf hinter den Mitspieler. Das Timing muss stimmen: Der Pass kommt, wenn der Läufer schon unterwegs ist.",
    sp(n2=(50, 46), n7=(69, 40), r15=(59, 37), r13=(79, 44), f=(48, 29)), [B("b1", 50.6, 46.6)] + ERSATZ,
    [S("Pass auf Spieler sieben", "Spieler zwei hat den Ball am Anfang der Außenzone. Er spielt auf Spieler sieben und läuft sofort außen hinter ihm vorbei.",
       ps("b1", [69.6, 40.6]), mv("r13", [75, 42], delay=0.3), mv("n2", [64, 49.5], delay=0.3), mv("n2", [76, 49.5], after=True)),
     S("Kopf hoch, in den Lauf", "Spieler sieben schaut hoch und sieht Spieler zwei kommen. Er spielt ihm den Ball in den Lauf, an Spieler dreizehn vorbei.",
       bl("n7", [76, 49.5]), ps("b1", [76.6, 50.1], after=True)),
     S("Abschluss: Punkt", "Spieler zwei nimmt mit und schiebt ins Minitor, und das gibt einen Punkt für Team Neon.",
       ps("b1", [80.4, 45.2]))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Stehen die Spitzen weit auseinander, geht der Ball durch die Lücke.", "Durch die Lücke zum Springer",
    "Laufen die beiden Stürmer die Innenverteidiger an, wird es zwischen ihnen frei. Dann spielt der Torwart flach durch die Lücke auf den Springer. Der dreht auf und bringt den Ball sofort nach außen, bevor Team Rot sich ordnet.",
    sp(POS2), START,
    [S("Die Spitzen gehen weit raus", "Spieler zehn und Spieler neun laufen die Innenverteidiger an. Zwischen ihnen wird es weit. Der Torwart sieht die Lücke.",
       mv("r10", [21, 12]), mv("r9", [21, 43]), bl("n1", richt(POS2["n1"], POS2["f"]), delay=0.6)),
     S("Flach durch die Lücke", "Der Springer schaut zum Torwart, und der spielt flach und scharf durch die Lücke.",
       bl("f", richt(POS2["f"], POS2["n1"])), ps("b1", fu(POS2["f"]), after=True)),
     S("Aufdrehen und nach außen", "Der Springer dreht auf und spielt sofort nach außen zu Spieler elf. Die zwei Stürmer sind überspielt, und vorn geht es zwei gegen zwei.",
       bl("f", richt(POS2["f"], POS2["n11"]), von=richt(POS2["f"], POS2["n1"]), dauer=1.3), drehen("f", list(POS2["n11"]), delay=0.4),
       ps("b1", fu(POS2["n11"]), after=True), mv("n3", [48, 5], delay=0.6))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
