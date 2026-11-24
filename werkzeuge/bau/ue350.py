import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P11 (U15-U17, Woche 18 Phase 6): Protecting the Box from Wide Attacks (Medium Sided Game). 50 x 40 Yards = 46 x 37 m
# (gerundet 45 x 35 m), kurzes, breites Feld, Tore oben und unten (Großfeldtore), links und rechts eine Außenzone (5 Yards = 5 m).
# Feld x 10-88, y 5-55 (in der Breite etwas gestreckt). Kein Großfeld (unter 60 m), nicht gedreht.
# Sieben gegen sieben: PDF dunkelblau (verteidigt oben) = Team Neon mit Nummern wie im PDF (4, 5, 6, 7, 9, 11);
# PDF pink (greift nach oben an) = Team Rot, 2 und 3 wie im PDF, neu nummeriert 8 (PDF 4), 10 (PDF 9),
# 12 (PDF 5), 14 (PDF 6), weil die Nummern doppelt wären. Positionen leicht verschoben (3D-Abstand). Ein Trainer statt zwei.
# Beide Torhüter als neutrale Torhüter (k1, k2) gezeichnet wie in UE-319, im Spiel gehört je einer zu einem Team.
# Wertung aus dem Ton: weit und breit geklärt = ein Punkt, ruhiger Ballgewinn mit Pass nach vorn = zwei Punkte für die Verteidiger.
# Fassungen: Progression 1 wie im PDF-Bild und Video (Treffer direkt oder nach Rückpass zählt doppelt; Text und Ton nennen
# stattdessen Punkte für ersten Kontakt und gute Flanke) und Progression 2 (Zone vor dem Tor, laut Text und Ton 15 Yards =
# 14 m, im Bild 10 Yards). Progression 3 (Konter nach Ballgewinn zählt doppelt) steckt in der Wertung der Grundform.
# Sichtkegel: kein Kegel im Video; aus dem Ton ("forces defenders to scan, communicate and decide"): In der zweiten Steigerung
# schaut Spieler fünf vor der Flanke zum späten Läufer.
# Keine Dublette: UE-308 (58-P6) ist ein 5 gegen 5 auf ein Tor mit Stangentoren, UE-348 (58-P8) Angriffswellen in Dreiergruppen.
T = P("T", "c", 4, 20, "T")
ERSATZ = [B("s1", 6.6, 23.5), B("s2", 3, 24.5)]
POS = {"n5": (34, 13), "n6": (66, 13), "n4": (45, 27), "n7": (24, 28), "n11": (76, 28), "n9": (39.5, 43),
       "r10": (57.5, 18.5), "r3": (15, 35), "r2": (85, 35), "r8": (55, 34.2), "r12": (29, 46), "r14": (66, 44)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + \
        [P("k1", "t", 49, 7.5, "TW"), P("k2", "t", 49, 52.5, "TW"), T]
def f(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(10, 5, 78, 50), line(18, 5, 18, 55), line(80, 5, 80, 55)]
ZONE = line(10, 24.6, 88, 24.6)
TORE = [{"x": 49, "y": 5, "side": "top", "size": "gross"}, {"x": 49, "y": 55, "side": "bottom", "size": "gross"}]
# Nur die Breiten-Maßlinie unten: rechts steht Spieler zwei in der Außenzone, die Länge steht in field_size
DIMS = dims(10, 88, 5, 55, "45 m", "35 m")[:1]
AUSSEN = dict(r2=(84, 18), n11=(75, 27))

u = {"title": "Strafraum schützen im 7 gegen 7", "code": "UE-350", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 14, "players_max": 16,
 "field_size": "45 x 35 m",
 "description": "Sieben gegen sieben mit Torhütern auf einem kurzen, breiten Feld. Links und rechts gibt es eine Außenzone, damit beide Teams über außen angreifen und flanken. Wir schauen auf Team Neon in der Abwehr, das den Flügelspieler verzögert, die Läufer mitnimmt und zuerst am Ball ist. Weit und breit geklärt gibt einen Punkt, ein ruhiger Ballgewinn mit Pass nach vorn zwei Punkte.",
 "organisation": ["Aufbauen: Ein Feld von 45 mal 35 Metern mit zwei Toren. Links und rechts ist eine Außenzone von 5 Metern abgeteilt.",
  "Verteilen: Zwei Teams mit je sechs Feldspielern und Torwart. Die Teams stellen sich frei auf, je ein Spieler geht gern auf jeden Flügel. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Normales Spiel auf zwei Tore, Einwurf und Abstoß wie immer. Beide Teams suchen den Weg über außen und flanken. Nach jeder Flanke ordnet sich die Abwehr schnell neu.",
  "Wertung: Ein Treffer gibt einen Punkt. Die Verteidiger holen einen Punkt, wenn sie weit und breit klären, und zwei Punkte, wenn sie den Ball ruhig erobern und nach vorn spielen."],
 "organisation_show": ORG,
 "coaching_points": ["Außen verzögern, die Mitte schützen", "Läufer mitnehmen, erster und zweiter Ball gehören uns", "Nach der Flanke kompakt bleiben", "Ball gewonnen? Ruhig bleiben und nach vorn"],
 "materials": ["2 Großfeldtore", "8 Hütchen für die Außenzonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Strafraum schützen im sieben gegen sieben. Ein freies Spiel auf zwei Tore, in dem viele Flanken kommen. Wir schauen auf Team Neon und wie es den Raum vor dem Tor verteidigt.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", *f(66, 44))] + ERSATZ,
  "steps": [
   S("Über die Mitte nach außen", "Team Rot greift an. Spieler vierzehn spielt in die Mitte zu Spieler acht, und der schickt Spieler zwei die Außenzone entlang.",
     ps("b1", f(55, 34.2)), mv("r2", [84, 18], delay=0.6), ps("b1", f(84, 18), after=True)),
   S("Außen verzögern, innen besetzen", "Spieler elf geht raus, läuft aber nicht blind an. Er bleibt vor Spieler zwei und macht ihm die Flanke schwer. Innen starten drei Angreifer, und jeder Verteidiger nimmt seinen Mann.",
     mv("n11", [79, 24]), mv("r10", [58, 10], delay=0.3), mv("n6", [62, 8.5], delay=0.5), mv("r8", [48, 21], delay=0.3),
     mv("n4", [45.5, 19], delay=0.5), mv("r3", [30, 17], delay=0.3, bend=-7), mv("n5", [34, 12], delay=0.5)),
   S("Flanke geklärt: Punkt", "Spieler zwei flankt. Spieler vier ist vor Spieler acht am Ball und köpft weit nach außen, und das gibt einen Punkt für Team Neon. Holt Team Neon den Ball ruhig und spielt nach vorn, gibt es zwei Punkte. Danach geht das Spiel einfach weiter.",
     ps("b1", f(45.5, 19)), ps("b1", [15, 24], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Direkt oder nach Rückpass zählt doppelt.", "Rückpass zählt doppelt",
    "Trifft Team Rot mit dem ersten Kontakt oder nach einem flachen Rückpass von der Grundlinie, zählt der Treffer doppelt. Das belohnt gute Flanken und gute Läufe. Für Team Neon heißt das, früh am Mann sein und den Raum am Elfmeterpunkt zumachen.",
    sp(**AUSSEN), [B("b1", *f(84, 18))] + ERSATZ,
    [S("Bis zur Grundlinie", "Spieler zwei geht mit Ball bis an die Grundlinie. Spieler zehn zieht an den kurzen Pfosten, Spieler acht wartet am Elfmeterpunkt. Spieler vier bleibt zu weit weg.",
       dr("r2", "b1", [84, 8.5]), mv("r10", [60, 10], delay=0.3), mv("n6", [63.5, 8], delay=0.5), mv("r8", [52, 18], delay=0.3), mv("n4", [43, 22], delay=0.6)),
     S("Rückpass, direkt: zwei Punkte", "Spieler zwei legt flach zurück. Spieler acht schießt direkt und trifft, und das gibt zwei Punkte für Team Rot. Spieler vier war einen Schritt zu spät.",
       ps("b1", f(52, 18)), ps("b1", [55, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Ein später Läufer, dem keiner folgen darf.", "Später Läufer aus der Tiefe",
    "Vor dem Tor gibt es jetzt eine Zone von 14 Metern. Bei einer Flanke darf der Mittelfeldspieler von Team Neon seinem Gegenspieler nicht in diese Zone folgen. Die Verteidiger müssen den späten Läufer selbst sehen und sich absprechen, wer ihn nimmt und wer den Ball.",
    sp(**AUSSEN), [B("b1", *f(84, 18))] + ERSATZ,
    [S("Spieler acht kommt spät", "Spieler zwei hat den Ball außen. Spieler acht startet spät aus der Tiefe. Spieler vier darf nicht mit in die Zone und bleibt an der Linie stehen. Spieler zehn zieht an den kurzen Pfosten.",
       mv("r8", [51, 18.5]), mv("n4", [46, 26.5], delay=0.3), mv("r10", [60, 10], delay=0.2), mv("n6", [63.5, 8], delay=0.4)),
     S("Schauen, rufen, rüberschieben", "Jetzt muss Spieler fünf schauen. Er sieht Spieler acht kommen, ruft und schiebt rüber. Spieler sechs bleibt bei Spieler zehn.",
       bl("n5", [51, 18.5]), mv("n5", [47, 13], after=True)),
     S("Flanke geklärt: Punkt", "Spieler zwei flankt auf Spieler acht. Spieler fünf ist zuerst da und köpft weit nach außen, und das gibt einen Punkt für Team Neon.",
       ps("b1", f(47, 13)), ps("b1", [15, 24], after=True))],
    lines=LINES + [ZONE])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
