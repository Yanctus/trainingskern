import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 81-P6 (U12-U14, Woche 20 Phase 4): Winning the Second Ball (Small Sided Game). 25 x 35 Yards = Feld x 32-68, y 5-55
# (23 x 32 m), je ein Jugendtor mit Torwart oben und unten. Oben/unten gespiegelt: Team Neon spielt nach oben (im PDF nach unten).
# Pink -> Neon (2, 3, 4, 8, 9), Navy -> Rot (5, 6, 7, 10, 11). Die zwei grünen Torhüter (1 und 13) -> neutrale Torhüter k1, k2
# (TW), damit es keine doppelte Nummer gibt; jedes Team hat damit wie im Original einen Torwart im Tor. Ein Trainer statt zwei, er steht links und spielt die Bälle ein.
# Positionen leicht auseinandergezogen (3D-Abstand). Wertung wie im Original: Treffer = drei Punkte, saubere Annahme eines
# hohen Balls = ein Punkt ("three points equalling a goal").
# Sichtkegel aus dem PDF ("Awareness of coaches quick restarts of play"): Neon vier schaut zum Trainer, bevor der Ball kommt.
# Im Video kein Kegel eingezeichnet.
T = P("T", "c", 24, 18, "T")
POS = {"k2": (50, 54), "n2": (33.5, 43), "n3": (66, 49), "n4": (42, 33), "n8": (59, 33), "n9": (50.5, 21.5),
       "k1": (50, 6), "r6": (50.5, 37), "r11": (33, 26), "r7": (67.5, 28), "r10": (41.5, 13), "r5": (59, 13)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b", "k": "t"}[i[0]], x, y, "TW" if i[0] == "k" else i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 19.5, 19), B("s2", 19.5, 22.6)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]
LINES = [rect(32, 5, 36, 50)]
CONES = ecken(32, 5, 36, 50)

u = {"title": "Den zweiten Ball gewinnen", "code": "UE-188", "kind": "Spielform",
 "focuses": ["Ballannahme", "Umschalten", "Torschuss"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 12, "players_max": 12, "field_size": "23 x 32 m",
 "description": "Ein Spiel fünf gegen fünf mit zwei Torhütern. Der Trainer spielt den Ball hoch, springend oder flach ins Feld, und beide Teams kämpfen um den zweiten Ball. Wer ihn gewinnt, kombiniert schnell und schließt ab. Ist der Ball weg, kommt sofort ein neuer Ball vom Trainer.",
 "organisation": ["Aufbauen: Ein Feld von 23 mal 32 Metern mit einem Jugendtor an jeder Grundlinie.",
  "Verteilen: Team Neon und Team Rot je zu fünft im Feld, dazu je ein Torwart. Der Trainer steht an der Seite mit vielen Bällen.",
  "Ablauf: Der Trainer wirft oder schießt den Ball ins Feld. Beide Teams kämpfen um den Ball und den zweiten Ball. Wer ihn hat, spielt schnell aufs Tor.",
  "Wertung und Wechsel: Ein Treffer gibt drei Punkte. Wer einen hohen Ball sauber annimmt, holt einen Punkt für sein Team. Geht der Ball ins Aus oder ins Tor, spielt der Trainer sofort einen neuen Ball ein."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell reagieren und lose Bälle sofort holen", "Entschlossen in jeden Zweikampf um den Ball gehen", "Den Ball mit Oberschenkel, Brust, Fuß oder Kopf kontrollieren", "Laut rufen und immer auf den neuen Ball vom Trainer achten"],
 "materials": ["2 Jugendtore", "4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Den zweiten Ball gewinnen. Der Trainer spielt den Ball ins Feld, und beide Teams kämpfen darum.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 24.6, 18.6)] + ERSATZ,
  "steps": [
   S("Ball in die Luft", "Alle schauen zum Trainer, auch Neon vier. Der Trainer schießt den Ball hoch in die Mitte. Neon acht und Rot sechs gehen beide zum Ball.",
     bl("n4", [30, 23]), ps("b1", [55.6, 31.6], after=True), mv("n8", [56, 32], after=True), mv("r6", [53, 33.5], after=True)),
   S("Zweiter Ball", "Rot sechs köpft den Ball weg, aber er springt frei. Neon vier reagiert am schnellsten und holt sich den zweiten Ball.",
     ps("b1", [44.6, 36.6]), mv("n4", [44, 36], delay=0.2)),
   S("Schnell nach vorn", "Neon vier spielt sofort zu Neon neun, bevor Team Rot sich ordnen kann.",
     ps("b1", [51.1, 22.1])),
   S("Abschluss: Punkte", "Neon neun schießt flach ins Eck, vorbei am Torwart. Das gibt drei Punkte für Team Neon. Sofort spielt der Trainer einen neuen Ball ins Feld, und alle kämpfen wieder um den zweiten Ball.",
     ps("b1", [46.5, 5.5]))],
  "dims": dims(32, 68, 5, 55, "23 m", "32 m", rx=84)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Entschlossen in den Zweikampf.", "Entschlossen zum Ball",
    "Bei einem freien Ball zwischen zwei Spielern gewinnt der, der entschlossener ist. Also mit vollem Tempo hin, laut rufen und den Körper zwischen Ball und Gegner bringen.",
    sp(), [B("b1", 24.6, 18.6)] + ERSATZ,
    [S("Freier Ball", "Der Trainer wirft den Ball springend zwischen Neon zwei und Rot elf. Beide sprinten los.",
       ps("b1", [36.6, 34.6]), mv("n2", [36, 37], delay=0.2), mv("r11", [35, 29], delay=0.2)),
     S("Meiner!", "Neon zwei ruft laut „Meiner!“, ist zuerst am Ball und stellt den Körper zwischen Ball und Gegner.",
       mv("r11", [34, 30])),
     S("Ball behalten", "Neon zwei behält den Ball und spielt zu Neon vier. Jetzt ist Team Neon am Ball und greift an.",
       ps("b1", [42.6, 33.6]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Ein guter erster Kontakt unter Druck.", "Erster Kontakt",
    "Ein sauber angenommener Ball ist ein gewonnener Ball. Wer einen hohen Ball unter Druck gut annimmt, hat Zeit für die nächste Aktion. Dafür gibt es einen Punkt für das Team.",
    sp(), [B("b1", 24.6, 18.6)] + ERSATZ,
    [S("Hoher Ball", "Der Trainer schießt den Ball hoch zu Neon acht. Rot sechs läuft von hinten an.",
       ps("b1", [59.6, 33.6]), mv("r6", [55, 35.5], delay=0.3)),
     S("Saubere Annahme: Punkt", "Neon acht nimmt den Ball mit der Brust sauber an und schirmt ihn ab. Das gibt einen Punkt für Team Neon.",
       dr("n8", "b1", [61, 30])),
     S("Weiterspielen", "Mit dem ersten Kontakt ist er weg vom Gegner und spielt gleich zu Neon neun nach vorn.",
       ps("b1", [51.1, 22.1]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
