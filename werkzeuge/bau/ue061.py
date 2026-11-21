import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 37-P3: 1 gegen 1, Rollentausch. Feld 20 x 20 Yards = x 28-72, y 9-53. PDF gedreht: oben -> rechts, links -> oben.
T = P("T", "c", 21, 4, "T")
coachb = [B("b9", 24.5, 6), B("b10", 17.5, 6)]
neon_q = [P("n10", "a", 19.5, 33, "10"), P("n11", "a", 19.5, 49, "11"), P("n8", "a", 11, 41, "8")]
neon_b = [B("b6", 21.1, 34.6), B("b7", 21.1, 50.6), B("b8", 12.6, 42.6)]
rot_b = [B("b3", 70.6, 5.8), B("b4", 62.1, 5.8), B("b5", 53.6, 5.8)]
lines = [rect(28, 9, 44, 44)]
u = {"title": "1 gegen 1: angreifen, dann sofort verteidigen", "code": "UE-061", "kind": "Spielform",
 "focuses": ["1 gegen 1", "Verteidigen", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "duration_minutes": 15, "players_min": 6, "players_max": 10, "field_size": "18 x 18 m",
 "description": "Zwei Gruppen stehen an zwei Seiten eines Feldes von 18 mal 18 Metern, an den beiden anderen Seiten steht je ein Minitor. Ein Spieler dribbelt auf einen einzelnen Verteidiger zu und will ihn ausspielen und ins Minitor treffen. Erobert der Verteidiger den Ball, schießt er auf das andere Minitor. Danach stellt sich der Verteidiger hinten an, und der Angreifer verteidigt sofort gegen den nächsten Spieler aus der anderen Richtung.",
 "organisation": ["Feld abstecken: 18 mal 18 Meter mit vier orangen Hütchen, ein Minitor rechts und eines unten.",
  "Gruppen aufstellen: Team Neon wartet links mit je einem Ball und greift das rechte Tor an, Team Rot wartet oben und greift das untere Tor an.",
  "Starten: Ein Spieler von Team Rot verteidigt in der Mitte, der erste Spieler von Team Neon dribbelt auf ihn zu. Ich stehe mit Ersatzbällen an der Ecke.",
  "Wechseln: Nach jedem Angriff stellt sich der Verteidiger in seiner Gruppe hinten an, und der Angreifer wird sofort Verteidiger gegen die andere Gruppe."],
 "organisation_show": ORG,
 "coaching_points": ["Als Angreifer mutig andribbeln und den Verteidiger ausspielen", "Ruhig und entschlossen abschließen, flach oder ins Eck", "Nach dem eigenen Angriff sofort ins Verteidigen umschalten", "Als Verteidiger immer zwischen Ball und Tor stehen"],
 "materials": ["2 Minitore", "4 orange Hütchen", "1 Ball pro Spieler", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Eins gegen eins mit Rollentausch. Hier greift jeder an und muss danach sofort verteidigen.",
 "board": {"lines": lines,
  "players": [P("n9", "a", 29.5, 32, "9"), P("r5", "b", 49, 31, "5"), *neon_q, P("r3", "b", 69, 4, "3"), P("r4", "b", 60.5, 4, "4"), P("r6", "b", 52, 4, "6"), T],
  "cones": ecken(28, 9, 44, 44), "goals": [{"x": 72, "y": 31, "side": "right"}, {"x": 50, "y": 53, "side": "bottom"}],
  "balls": [B("b1", 31.1, 32.8), *neon_b, *rot_b, *coachb],
  "steps": [
   S("Die Neun dribbelt an", "Spieler neun dribbelt auf Spieler fünf zu, und der kommt ihm entgegen.",
     dr("n9", "b1", [41, 32.5]), mv("r5", [46, 31.5], delay=0.25)),
   S("Haken und oben vorbei", "Mit einem Haken zieht Spieler neun oben an Spieler fünf vorbei.",
     dr("n9", "b1", [45.5, 25]), dr("n9", "b1", [57, 25.5], after=True), mv("r5", [47.5, 28.5], delay=0.3)),
   S("Abschluss ins rechte Minitor: Tor", "Er schließt ruhig ins rechte Minitor ab, und das gibt ein Tor.", ps("b1", [73.8, 30.5])),
   S("Rollentausch, neue Richtung", "Jetzt wird Spieler neun sofort Verteidiger, Spieler fünf stellt sich oben hinten an, und Spieler drei greift das untere Tor an.",
     mv("n9", [53, 38]), mv("r5", [43.5, 4], delay=0.1), dr("r3", "b3", [62, 17], delay=0.3))],
  "dims": dims(28, 72, 9, 53, "18 m", "18 m", rx=82)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der Verteidiger stellt sich immer zwischen Ball und Tor, nicht nur vor den Ball.", "Zwischen Ball und Tor",
    "Ein Verteidiger, der nur zum Ball läuft, öffnet dem Angreifer den Weg zum Tor. Deshalb stellt er sich zuerst auf die Linie zwischen Ball und Tor und drängt den Angreifer dann nach außen. So kommt der Angreifer nicht zum Abschluss.",
    [P("r6", "b", 40, 20, "6"), P("n9", "a", 35, 38, "9"), *neon_q, P("r3", "b", 69, 4, "3"), P("r4", "b", 60.5, 4, "4"), P("r5", "b", 52, 4, "5"), T],
    [B("b1", 41.2, 21.2), *neon_b, *rot_b, *coachb],
    [S("Der Verteidiger steht falsch", "Spieler sechs dribbelt los, doch Spieler neun steht noch neben der Linie zwischen Ball und Tor, nicht darauf.", dr("r6", "b1", [48, 24])),
     S("In die Linie zum Tor", "Spieler neun läuft schnell in die Linie zwischen Ball und unterem Tor hinein.", mv("n9", [48.5, 36]), dr("r6", "b1", [50, 27], delay=0.4)),
     S("Nach außen gedrängt, kein Abschluss", "Spieler sechs muss nach außen ausweichen, Spieler neun bleibt dran, und der Weg zum Tor ist zu.",
       dr("r6", "b1", [60, 31]), mv("n9", [56, 37], delay=0.15))]),
  V("Steigerung", "Und jetzt die Steigerung: Das Feld wird geteilt, und der Verteidiger hält seine Hälfte.", "Hälften: über die Linie kommen",
    "Eine Linie teilt das Feld in eine Angriffs- und eine Abwehrhälfte. Der Angreifer muss erst über die Mittellinie kommen, bevor er abschließen darf, der Verteidiger will genau das verhindern. Erobert er den Ball, schaltet er sofort um und trifft in das Minitor an seiner Hälfte.",
    [P("r5", "b", 51, 20, "5"), P("n9", "a", 49, 40.5, "9"), *neon_q, P("r3", "b", 69, 4, "3"), P("r4", "b", 60.5, 4, "4"), P("r6", "b", 44, 4, "6"), T],
    [B("b1", 52.5, 21), *neon_b, *rot_b[:2], B("b5", 45.6, 5.8), *coachb],
    [S("Die Fünf will über die Linie", "Spieler fünf dribbelt auf die Mittellinie zu, und Spieler neun rückt bis an die Linie heran.",
       dr("r5", "b1", [57.5, 26]), mv("n9", [56, 35], delay=0.2)),
     S("Neun erobert den Ball", "Kurz vor der Linie geht Spieler neun dazwischen und erobert den Ball.", dr("n9", "b1", [62.5, 34])),
     S("Umschalten: Tor rechts", "Sofort schaltet er um und trifft ins rechte Minitor, und das gibt ein Tor für Team Neon.", ps("b1", [73.8, 31.5]))],
    lines=lines + [line(28, 31, 72, 31), line(50, 9, 50, 53)], labels=[{"x": 38, "y": 23, "text": "ANGRIFF"}, {"x": 38, "y": 46, "text": "ABWEHR"}]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Eng rangehen und eng dranbleiben.", "Eng rangehen, eng dranbleiben",
    "Wer als Verteidiger zu weit weg steht, lässt dem Angreifer Zeit und Platz. Deshalb geht er schnell eng heran, bleibt mit kurzen Schritten dran und lässt sich nicht abschütteln. So zwingt er den Angreifer zu Fehlern.",
    [P("r6", "b", 37, 20, "6"), P("n10", "a", 45, 44, "10"), P("n11", "a", 19.5, 33, "11"), P("n8", "a", 19.5, 49, "8"), P("n9", "a", 11, 41, "9"),
     P("r3", "b", 69, 4, "3"), P("r4", "b", 60.5, 4, "4"), P("r5", "b", 52, 4, "5"), T],
    [B("b1", 38.5, 21), *neon_b, *rot_b, *coachb],
    [S("Schnell eng heran", "Spieler sechs dribbelt an, und Spieler zehn geht schnell eng heran.", dr("r6", "b1", [42, 27]), mv("n10", [44, 32.5], delay=0.15)),
     S("Eng dranbleiben", "Spieler sechs will nach rechts weg, doch Spieler zehn bleibt mit kurzen Schritten eng dran.",
       dr("r6", "b1", [49, 28.5]), mv("n10", [50, 33], delay=0.15))],
    lines=lines + [line(28, 31, 72, 31), line(50, 9, 50, 53)])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
