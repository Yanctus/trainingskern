import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 79-P6 (U12-U14, Woche 35 Phase 3): Movement in Behind to Finish on One Touch SSG. 25 x 40 Yards = Feld x 34.4-65.6,
# y 5-55 (23 x 37 m), Endzonen je 10 Yards (gestrichelt bei y 17.5 und 42.5), an beiden Enden ein Jugendtor mit Torwart.
# Orientierung wie im PDF (nicht gedreht): Blau/dunkel (greift nach oben an) -> Team Neon 2-6;
# Pink (verteidigt oben) -> Team Rot 7-11. Torhüter im PDF grün -> neutral k1/k2. Keine Nummern im PDF. Positionen auf ein Spaltenraster gesetzt
# (3D-Abstand: fünf Spalten im Abstand 8.25, Randspalten knapp auf der Seitenlinie), Spielidee wie im PDF: Pass, Kombination,
# Steilpass in die Endzone, Abschluss mit einem Kontakt. Ein Trainer (unten rechts) statt zwei.
# Coaching-Punkt = PDF Seite 2 links (Rot verteidigt eng, schnelle Doppelpässe), Steigerung = PDF Seite 2 rechts / Ton
# (ein Verteidiger darf zurück, ein zusätzlicher Angreifer hilft; Spieler wird nach außen gedrängt und legt quer).
# Sichtkegel: im Video "Awareness to provide support" beim zusätzlichen Angreifer (ca. 1:20-1:30), kein Kegel eingezeichnet:
# Steigerung bl() von Spieler fünf zu Spieler drei, bevor er in die Endzone startet (Richtung aus dem Sinn).
T = P("T", "c", 76, 48, "T")
POS = {"n2": (33.5, 45.5), "n3": (41.75, 37.5), "n5": (50, 38), "n4": (58.25, 36.5), "n6": (66.5, 42),
       "r7": (33.5, 29.5), "r8": (41.75, 21.5), "r9": (50, 22.5), "r10": (58.25, 21), "r11": (66.5, 26.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + \
           [P("k1", "t", 50, 7, "TW"), P("k2", "t", 50, 53.5, "TW"), T]
ERSATZ = [B("s1", 79.6, 51.5), B("s2", 76, 51.5)]
LINES = [rect(34.4, 5, 31.2, 50), line(34.4, 17.5, 65.6, 17.5), line(34.4, 42.5, 65.6, 42.5)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]

u = {"title": "Steilpass und direkt abschließen", "code": "UE-228", "kind": "Spielform",
 "focuses": ["Passspiel", "Bewegung", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 37 m",
 "description": "Fünf gegen fünf in der Mitte, an beiden Enden ein Tor mit Torwart und davor eine Endzone. Ein Treffer zählt nur, wenn ein Angreifer mit einem Steilpass in die Endzone geschickt wird und mit dem ersten Kontakt schießt. Sobald der Steilpass gespielt ist, darf kein anderer Spieler mehr in die Endzone. Die Verteidiger stehen eng in der Mitte, darum braucht es schnelle Doppelpässe und gute Läufe.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 37 Metern mit einem Jugendtor an jedem Ende. Vor jedem Tor eine Endzone von 9 Metern, gestrichelt abgeteilt.",
  "Verteilen: Team Neon und Team Rot mit je fünf Feldspielern in der Mitte, in jedem Tor ein Torwart. Team Neon greift das obere Tor an, Team Rot das untere. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Das Team am Ball kombiniert in der Mitte und spielt steil in die Endzone. Ein Angreifer läuft hinein und schießt direkt. Danach darf kein anderer Spieler mehr in die Endzone.",
  "Wertung und Wechsel: Jeder direkte Treffer gibt einen Punkt. Erobert das andere Team den Ball, greift es sofort selbst an. Nach einem Treffer oder Aus bringt der Trainer schnell einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Mit schnellen Doppelpässen um die Verteidiger herumspielen", "Den Steilpass so spielen, dass ein direkter Schuss möglich ist", "Laut und mit Zeichen sagen, wann der Lauf kommt", "Ist keine Lücke da, den Ball laufen lassen und neu aufbauen"],
 "materials": ["2 Jugendtore", "8 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Steilpass und direkt abschließen. Fünf gegen fünf, und ein Punkt gelingt nur nach einem Steilpass in die Endzone mit dem ersten Kontakt.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 34.1, 46.1)] + ERSATZ,
  "steps": [
   S("Pass", "Team Neon hat den Ball. Spieler zwei spielt nach vorn zu Spieler drei.",
     ps("b1", [42.35, 38.1])),
   S("Kombinieren", "Spieler drei spielt direkt zu Spieler fünf und startet sofort im Bogen um Spieler acht herum.",
     ps("b1", [50.6, 38.6]), mv("n3", [37.5, 28], after=True), mv("n3", [38.5, 18.5], after=True)),
   S("Steilpass in die Endzone", "Spieler fünf spielt den Ball durch die Lücke zwischen Spieler acht und Spieler neun in die Endzone. Spieler drei läuft genau im richtigen Moment hinein. Jetzt darf kein anderer Spieler mehr in die Endzone.",
     ps("b1", [44, 13.4]), mv("n3", [43.4, 12.8], delay=0.2)),
   S("Direkt abschließen: Punkt", "Spieler drei schießt direkt, ohne den Ball anzunehmen, flach ins Eck. Das gibt einen Punkt für Team Neon. Danach bringt der Trainer sofort einen neuen Ball, und jetzt greift Team Rot das untere Tor an.",
     ps("b1", [44.5, 5.3]))],
  "dims": dims(34.4, 65.6, 5, 55, "23 m", "37 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit schnellen Doppelpässen um die Verteidiger herum.", "Schnelle Doppelpässe",
    "Team Rot steht eng in der Mitte und macht die Wege zum Tor zu. Darum spielen die Angreifer schnelle Doppelpässe mit einem Kontakt und starten sofort in die Lücke. So kommen sie trotzdem hinter die Abwehr.",
    sp(), [B("b1", 50.6, 38.6)] + ERSATZ,
    [S("Doppelpass", "Spieler neun läuft Spieler fünf an. Spieler fünf spielt direkt zu Spieler vier, läuft sofort weiter und bekommt den Ball direkt zurück.",
       mv("r9", [49, 31]), ps("b1", [58.85, 37.1], delay=0.2), mv("n5", [54.5, 29], after=True), ps("b1", [55.1, 29.6], after=True)),
     S("Durch die Lücke: Punkt", "Gleichzeitig startet Spieler drei in die Endzone. Spieler fünf spielt direkt steil in seinen Lauf, und Spieler drei schießt mit dem ersten Kontakt. Das gibt einen Punkt für Team Neon.",
       mv("n3", [37, 27]), mv("n3", [40, 13], after=True), ps("b1", [40.6, 13.6], delay=0.6), ps("b1", [45, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Ein Verteidiger darf zurück, und ein Angreifer darf helfen.", "Einer zurück, einer hilft",
    "Nach dem Steilpass darf jetzt ein Verteidiger mit in die Endzone und ein zusätzlicher Angreifer darf nachrücken. Der Verteidiger drängt den Schützen nach außen. Der zweite Angreifer hat das im Blick, läuft mit und bekommt den Ball quer zum direkten Abschluss.",
    sp(), [B("b1", 42.35, 38.1)] + ERSATZ,
    [S("Lauf in die Tiefe", "Spieler drei spielt zu Spieler fünf und startet im Bogen Richtung Endzone.",
       ps("b1", [50.6, 38.6]), mv("n3", [37.5, 28], after=True), mv("n3", [38.5, 18.5], after=True)),
     S("Einer darf zurück", "Spieler fünf spielt steil in die Endzone, und Spieler drei läuft hinein. Jetzt darf ein Verteidiger mit zurück: Spieler acht läuft zurück in die Endzone.",
       ps("b1", [44, 13.4]), mv("n3", [43.4, 12.8], delay=0.2), mv("r8", [46, 9.5], delay=0.3)),
     S("Nach außen gedrängt", "Spieler acht drängt Spieler drei nach außen. Spieler fünf sieht das und startet als zusätzlicher Angreifer in die Endzone.",
       dr("n3", "b1", [38.5, 13]), mv("r8", [42.5, 9.5], delay=0.2), bl("n5", [42.2, 22.6]), mv("n5", [54.5, 25], after=True), mv("n5", [52, 13.5], after=True)),
     S("Querpass: Punkt", "Spieler drei spielt quer zu Spieler fünf, und Spieler fünf schießt direkt ins Eck. Das gibt einen Punkt für Team Neon.",
       ps("b1", [52.6, 14.1]), ps("b1", [55.5, 5.3], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
