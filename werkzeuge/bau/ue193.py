import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 89-P2 (U12-U14, Woche 22 Phase 5): Stopping Penetration (CDM) Skill. 20 x 15 Yards = Feld x 25-75, y 11.25-48.75 (18 x 14 m),
# drei Zonen zu 5 Yards (gestrichelt). Ausrichtung wie im PDF: unten links drei Dummys (Stangen) von Team Neon (pink, Spieler vier
# davor), oben rechts drei Dummys von Team Rot (dunkel, Spieler neun davor). Wartende Spieler nur im Text. Im PDF zwei Trainer als
# Passgeber; hier ein Trainer (oben links, passt auf die Neon-Dummys) und ein Springer (F, unten rechts, passt auf die Rot-Dummys),
# der Ton erlaubt "the coach or a player". Steigerung eins: je ein Hütchentor oben und unten (im Video gelb, hier neon).
# Sichtkegel: Text "Awareness of coaches body shape and eyes to anticipate pass direction" -> Spieler vier schaut zum Trainer,
# Spieler neun zum Springer, bevor der Pass kommt; Ton "get their head up to drive out" -> in Steigerung eins schaut Spieler vier nach dem
# Abfangen zum Tor oben (im Video kein Kegel eingezeichnet, Richtung aus dem Sinn).
T = P("T", "c", 39.7, 20.2, "T")
F = P("f1", "t", 63.5, 39.1, "F")
POS = {"n4": (37.9, 41.2), "r9": (63.8, 20.7)}
def sp(F=F, **k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [F, T]
ERSATZ = [B("s1", 36, 17), B("s2", 32.4, 17)]
LINES = [rect(25, 11.25, 50, 37.5), line(25, 23.75, 75, 23.75), line(25, 36.25, 75, 36.25)]
DUMMYS = [C(x, 15.3, shape="stange") for x in (56.5, 63.8, 71)] + [C(x, 44.7, shape="stange") for x in (30.9, 38.1, 45.3)]
DUMMYS_ID = [dict(c, id=f"d{i + 1}") for i, c in enumerate(DUMMYS)]
TORE = [C(50, 11.25, "neon", id="g1"), C(57, 11.25, "neon", id="g2"), C(43, 48.75, "neon", id="g3"), C(50, 48.75, "neon", id="g4")]

u = {"title": "Pässe in die Tiefe stoppen", "code": "UE-193", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "18 x 14 m",
 "description": "Ein Spieler steht vor drei Dummys und soll Pässe abfangen, wie ein Sechser vor der Abwehr. Der Passgeber spielt den Ball fest auf einen Dummy, und der Spieler muss blitzschnell reagieren. Blockt er den Ball ins Aus, gibt das einen Punkt, erobert er ihn und dribbelt hinaus, gibt das zwei Punkte. Zwei Teams spielen gleichzeitig an beiden Enden gegeneinander.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern in drei Zonen. Unten links drei Dummys für Team Neon, oben rechts drei Dummys für Team Rot.",
  "Verteilen: Je ein Spieler steht vor den Dummys seines Teams, die anderen warten hinter den Dummys. Der Trainer passt oben links mit vielen Bällen, ein Springer passt unten rechts.",
  "Ablauf: Trainer und Springer spielen gleichzeitig einen festen Pass auf einen Dummy. Der Spieler davor blockt den Ball oder erobert ihn, dribbelt aus dem Feld und passt zurück.",
  "Wertung und Wechsel: Ball ins Aus geblockt gibt einen Punkt, erobert und zurückgepasst gibt zwei Punkte. Nach jedem Pass kommt der nächste Spieler. Welches Team hat am Ende die meisten Punkte?"],
 "organisation_show": ORG,
 "coaching_points": ["Auf den Zehenspitzen stehen und den Pass ahnen", "Auf Körper und Augen des Passgebers schauen", "Schnell entscheiden: Ball blocken oder sichern", "Den Ball eng führen und mit erhobenem Kopf hinausdribbeln"],
 "materials": ["6 Dummys oder Stangen", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pässe in die Tiefe stoppen. Wer vor den Dummys steht, fängt die Pässe ab wie ein Sechser vor der Abwehr.",
 "board": {"lines": LINES, "goals": [], "cones": DUMMYS, "players": sp(), "balls": [B("b1", 40.3, 20.8), B("b2", 64.1, 39.7)] + ERSATZ,
  "steps": [
   S("Auf den Zehenspitzen", "Spieler vier und Spieler neun stehen auf den Zehenspitzen vor ihren Dummys. Beide schauen genau auf den Passgeber: Wohin schaut er, wie steht sein Körper?",
     bl("n4", [39.7, 20.2]), bl("r9", [63.5, 39.1])),
   S("Pass und blocken", "Gleichzeitig spielen der Trainer und der Springer einen festen Pass auf einen Dummy. Spieler neun blockt den Ball ins Aus, und das gibt einen Punkt für Team Rot. Spieler vier stoppt den Ball.",
     ps("b1", [33.9, 37.1]), mv("n4", [33.3, 36.5], delay=0.2), ps("b2", [69.1, 22.1]), mv("r9", [68.5, 21.5], delay=0.2),
     ps("b2", [78, 25], after=True)),
   S("Rausdribbeln: Punkte", "Spieler vier hebt den Kopf, dribbelt links aus dem Feld und passt zum Trainer zurück. Das gibt zwei Punkte für Team Neon. Dann kommen die nächsten Spieler beider Teams vor die Dummys.",
     dr("n4", "b1", [23.5, 33]), ps("b1", [40.3, 20.8], after=True))],
  "dims": dims(25, 75, 11.25, 48.75, "18 m", "14 m", rx=86)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Durch das Tor dribbeln.", "Durch das Tor dribbeln",
    "Jetzt steht oben und unten ein Hütchentor. Wer den Ball erobert, dribbelt mit Tempo durch das Tor auf der anderen Seite und bekommt dafür zwei Punkte. So schaltet der Spieler nach dem Ballgewinn sofort um, wie im Spiel.",
    sp(), [B("b1", 40.3, 20.8), B("b2", 64.1, 39.7)] + ERSATZ,
    [S("Abfangen", "Der Trainer und der Springer passen gleichzeitig auf die Dummys. Spieler vier und Spieler neun fangen beide den Ball ab.",
       ps("b1", [33.9, 37.1]), mv("n4", [33.3, 36.5], delay=0.2), ps("b2", [69.1, 22.1]), mv("r9", [68.5, 21.5], delay=0.2)),
     S("Durch das Tor: Punkte", "Spieler vier hebt den Kopf, sieht das Tor oben und dribbelt mit Tempo hindurch. Das gibt zwei Punkte für Team Neon. Gleichzeitig dribbelt Spieler neun unten durch sein Tor, und das gibt zwei Punkte für Team Rot.",
       bl("n4", [46, 20]), dr("n4", "b1", [53.5, 8], after=True), dr("r9", "b2", [46.5, 51.5], delay=0.5))],
    cones=DUMMYS_ID + TORE),
  V("Steigerung", "Und jetzt die zweite Steigerung: Näher am Passgeber.", "Näher am Passgeber",
    "Jetzt starten die Spieler weiter vorn, näher am Passgeber. Der Weg zum Ball ist kürzer, aber der Pass kommt viel schneller. Darum noch früher auf Körper und Augen des Passgebers schauen.",
    sp(F=P("f1", "t", 57.5, 39.1, "F"), n4=(31, 33), r9=(66, 28)), [B("b1", 40.3, 20.8), B("b2", 58.1, 39.7)] + ERSATZ,
    [S("Näher dran", "Spieler vier und Spieler neun stehen jetzt weiter vorn. Beide schauen genau auf den Passgeber.",
       bl("n4", [39.7, 20.2]), bl("r9", [57.5, 39.1])),
     S("Blitzschnell: Punkte", "Die Pässe kommen. Beide reagieren blitzschnell, erobern den Ball und dribbeln hinaus. Spieler vier passt zum Trainer, Spieler neun zum Springer, und das gibt zwei Punkte für jedes Team.",
       ps("b1", [39.4, 30.6]), mv("n4", [38.8, 30], delay=0.1), ps("b2", [60.7, 28.6]), mv("r9", [60.1, 28], delay=0.1),
       dr("n4", "b1", [23.5, 28], after=True), ps("b1", [40.3, 20.8], after=True),
       dr("r9", "b2", [77, 24], delay=1.4), ps("b2", [58.1, 39.7], delay=2.6))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
