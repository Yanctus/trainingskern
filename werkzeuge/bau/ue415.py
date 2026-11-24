import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 30-P6 (U15-U17, Woche 41 Phase 3): Crossing and Finishing SSG. 35 x 45 Yards = 32 x 41 m (gerundet 30 x 40 m).
# Ausrichtung wie im PDF: Die 45 Yards liegen schon waagrecht, Tore oben und unten (Abstand Tor zu Tor 30 m), Feld x 17-83, y 5-54,
# Flügelzonen links und rechts (gestrichelt bei x 28 und 72). Kein Großfeld, kein langes Hochkant-Feld: nicht gedreht.
# Pink (greift nach oben an) -> Team Neon, Nummern wie im PDF (4, 5, 6, 7, 9, 11).
# Beide Torhüter neutral (k1 oben, k2 unten; zwei Team-Torhüter hätten beide das Label TW). Blau -> Team Rot; Blau neu nummeriert, weil die Nummern doppelt sind: 4 -> 2, 5 -> 3, 6 -> 12,
# 9 -> 14, 8 und 10 bleiben. Großfeldtore mit Torwart (nur C- und B-Jugend). Ein Trainer statt zwei (rechts neben dem Feld).
# Positionen gegenüber dem PDF leicht verschoben (Raster für den 3D-Abstand), Abläufe wie im PDF: Pass ins Zentrum, Pass in den
# Lauf des Flügelspielers, ein Verteidiger darf erst nach dem Pass in die Zone, Flanke, Abschluss.
# Fassungen: Coaching-Punkt = PDF Key Coaching Point 2 (scharf an den ersten Pfosten oder zurücklegen auf den späten Läufer),
# Steigerung = Hinterlaufen gegen den Verteidiger in der Zone (Ton und KCP-Liste „Players can overlap“).
# Sichtkegel: Text KCP 2 „Always keep your head up to read movement“, Video „Head up to see different runs“: Der Flügelspieler
# schaut vor der Flanke in den Strafraum (Richtung aus dem Sinn, im Video als Hinweis eingeblendet).
T = P("T", "c", 88, 54, "T")
POS = {"k2": (50, 51), "n4": (41, 50), "n5": (68, 46), "n6": (50, 29), "n9": (41, 16), "n11": (21, 30), "n7": (78, 28),
       "k1": (50, 8.5), "r2": (31, 10), "r3": (59, 15), "r12": (59, 32), "r8": (68, 28), "r10": (31, 31), "r14": (41, 34)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") if i[0] == "k" else P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 91.5, 55), B("s2", 91, 57.5)]
LINES = [rect(17, 5, 66, 49), line(28, 5, 28, 54), line(72, 5, 72, 54)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "gross"}, {"x": 50, "y": 54, "side": "bottom", "size": "gross"}]
KEGEL = [C(17, 5), C(28, 5), C(72, 5), C(83, 5), C(17, 54), C(28, 54), C(72, 54), C(83, 54)]
DIMS = dims(17, 83, 5, 54, "40 m", "30 m", rx=94)

u = {"title": "Flanken aus den Flügelzonen", "code": "UE-415", "kind": "Spielform",
 "focuses": ["Zusammenspiel", "Torschuss", "Passspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 16,
 "field_size": "40 x 30 m",
 "description": "Sechs gegen sechs mit zwei Toren und Torhütern, links und rechts liegt je eine Flügelzone. Das Team in Ballbesitz spielt den Ball in den Lauf seines Flügelspielers, der früh flankt. Die Angreifer timen ihre Läufe in den Strafraum und schließen ab. Ein Verteidiger darf erst in die Zone, wenn der Pass gespielt ist.",
 "organisation": ["Aufbauen: Ein Feld von 40 mal 30 Metern mit zwei Toren. Auf beiden Seiten eine schmale Flügelzone über die ganze Länge, mit Hütchen markiert.",
  "Verteilen: Sechs gegen sechs im Mittelfeld, dazu ein Torwart in jedem Tor. Das Team in Ballbesitz hat in jeder Flügelzone einen Spieler. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Das Team spielt sich frei und passt in den Lauf des Flügelspielers. Der flankt mit einem oder zwei Kontakten, die Angreifer schließen ab. Ein Verteidiger darf erst nach dem Pass in die Zone, vorher steht dort keiner. Erobert Team Rot den Ball, greift es genauso über die Zonen an.",
  "Wertung: Jeder Treffer gibt einen Punkt. Wird direkt geflankt und direkt verwandelt, gibt das zwei Punkte. Nach jedem Treffer bringt der Trainer den nächsten Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Lücke sehen und in den Lauf passen, nicht in den Fuß", "Erst der Pass, dann der Lauf in den Strafraum", "Kopf hoch vor der Flanke, wo läuft wer hin", "Hinterlaufen, wenn der Flügelspieler gestellt wird"],
 "materials": ["2 Tore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Flanken aus den Flügelzonen. Sechs gegen sechs mit zwei Torhütern, und die Treffer sollen über die Flügel fallen.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": [B("b1", 41.6, 50.6)] + ERSATZ,
  "steps": [
   S("Pass ins Zentrum", "Spieler vier hat den Ball hinten und spielt flach ins Zentrum zu Spieler sechs. Team Rot zieht sich in der Mitte zusammen.",
     ps("b1", [50.6, 29.6]), mv("r10", [34, 29], delay=0.4), mv("r12", [56, 30], delay=0.4)),
   S("Lücke sehen, raus auf den Flügel", "Außen ist jetzt Platz. Spieler elf startet in seiner Zone nach vorn, und Spieler sechs spielt ihm den Ball in den Lauf. Erst jetzt darf Spieler zehn hinterher in die Zone.",
     mv("n11", [23, 16]), ps("b1", [23.6, 16.6], delay=0.4), mv("r10", [26, 23], after=True)),
   S("Kopf hoch, dann flanken", "Spieler elf schaut kurz in den Strafraum. Spieler neun startet zum langen Pfosten, Spieler sechs rückt nach. Dann kommt die Flanke.",
     mv("n6", [47, 21], delay=0.6), bl("n11", [42, 14]), mv("n9", [56, 12], after=True), ps("b1", [56.6, 12.6], after=True)),
   S("Direkt verwandelt: Punkt", "Spieler neun nimmt die Flanke direkt und trifft, und das gibt einen Punkt für Team Neon. War schon die Flanke direkt, gibt es sogar zwei Punkte. Danach bringt der Trainer den nächsten Ball.",
     ps("b1", [54.5, 5.3]))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Scharf an den ersten Pfosten oder zurücklegen.", "Erster Pfosten oder zurück",
    "Der Flügelspieler hat zwei Möglichkeiten. Er spielt scharf und flach an den ersten Pfosten, oder er legt zurück auf den Spieler, der spät an den Strafraum kommt. Vorher geht der Kopf hoch, damit er sieht, wohin die Mitspieler laufen.",
    sp(), [B("b1", 68.6, 46.6)] + ERSATZ,
    [S("Pass in den Lauf", "Spieler fünf spielt steil in die Zone. Spieler sieben läuft auf den Ball zu, nicht in die Ecke.",
       mv("n7", [79, 14]), ps("b1", [79.6, 14.6], delay=0.3), mv("r8", [74, 22], after=True)),
     S("Kopf hoch: Wer läuft wohin?", "Spieler sieben schaut hoch. Spieler neun zieht an den ersten Pfosten und nimmt Spieler drei mit. Spieler sechs kommt spät an die Strafraumgrenze.",
       bl("n7", [60, 17]), mv("n9", [57, 10.5], after=True), mv("r3", [55.5, 13], after=True), mv("k1", [55, 8], after=True), mv("n6", [57, 22], delay=1.2)),
     S("Zurückgelegt: Punkt", "Der erste Pfosten ist zu. Also legt Spieler sieben flach zurück auf Spieler sechs. Der schießt direkt, und das gibt einen Punkt für Team Neon.",
       ps("b1", [57.6, 22.6]), ps("b1", [45.5, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Hinterlaufen, wenn der Flügelspieler gestellt wird.", "Hinterlaufen auf dem Flügel",
    "Kommt der Verteidiger in die Zone und stellt den Flügelspieler, hilft ein Mitspieler. Der Flügelspieler zieht leicht nach innen, ein Mitspieler hinterläuft ihn außen. Der bekommt den Ball in den Lauf und flankt.",
    sp(), [B("b1", 21.6, 30.6)] + ERSATZ,
    [S("Verteidiger in der Zone", "Spieler elf hat den Ball in seiner Zone. Spieler zehn geht sofort hinterher und stellt ihn.",
       mv("r10", [24, 24])),
     S("Nach innen ziehen, außen hinterlaufen", "Spieler elf dribbelt leicht nach innen und zieht Spieler zehn mit. Von hinten kommt Spieler vier außen herum und läuft an ihm vorbei.",
       dr("n11", "b1", [26, 33]), mv("r10", [28, 27], delay=0.2), mv("n4", [27, 43], delay=0.2), mv("n4", [19, 37], after=True), mv("n4", [19, 18], after=True)),
     S("Flanke vom Hinterläufer: Punkt", "Spieler elf spielt in den Lauf von Spieler vier. Der flankt direkt zum langen Pfosten, Spieler neun trifft, und das gibt einen Punkt für Team Neon.",
       ps("b1", [19.6, 18.6]), mv("n9", [56, 12], delay=0.3), ps("b1", [56.6, 12.6], after=True), ps("b1", [54.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
