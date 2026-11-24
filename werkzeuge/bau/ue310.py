import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 97-P8 (U15-U17, Woche 13 Phase 1): 3 V 3 Build Up Play, Wave Game. 25 x 30 Yards (23 x 27 m, nach der Meter-Regel 25 x 25 m).
# Um 90 Grad gedreht: im PDF wird nach oben gespielt, hier von links nach rechts (Feld x 19-80.4, y 4-56), weil sonst
# Aufbauer, Verteidiger und Empfänger in 3D übereinander stehen. Die zwei Linien (10 Yards = 9 m vom Rand) gestrichelt.
# Vier Dreiergruppen: Orange (Aufbau, 4, 5, 6) -> Team Neon. Pink/Rot (Verteidiger 2, 5, 6) -> Team Rot 2, 3, 7 (neu
# nummeriert, weil 5 und 6 bei Neon). Weiß an der Ziellinie (3, 4, 5) -> neutrale Gruppe 9, 10, 11 (team t, mit Nummern).
# Blau an der Startlinie (3, 4, 2) -> neutrale Gruppe 12, 13, 14. Ein Trainer statt zwei, Ballhaufen weggelassen.
# Grundform wie im Video ab 0:17 (Pass zur Seite, Verlagerung, Pass durch die Lücke). Steigerung = Key Coaching Point 2
# (Ballgewinn: Angreifer tauschen mit der Gruppe an der nächsten Linie), Zeitvorgabe aus dem Ton nur im Text.
# Sichtkegel aus Text und Ton ("identify the gaps", "read the defensive structure"): der Passgeber schaut vor dem Pass
# in die Lücke. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 8, 30, "T")
ERSATZ = [B("s1", 11.6, 33.5), B("s2", 8, 33.5)]
POS = {"n4": (41.5, 30), "n5": (45, 12), "n6": (42.5, 52), "r2": (53.5, 14), "r3": (53, 30), "r7": (51, 47),
       "g9": (62, 10), "g10": (62, 30), "g11": (62, 50), "h12": (30, 12), "h13": (30, 30), "h14": (30, 48)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, {"n": "a", "r": "b"}.get(i[0], "t"), x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(19, 4, 61.4, 52), line(39.5, 4, 39.5, 56), line(60, 4, 60, 56)]
CONES = [C(39.5, 4), C(39.5, 56), C(60, 4), C(60, 56)] + ecken(19, 4, 61.4, 52)

u = {"title": "Aufbauwelle drei gegen drei", "code": "UE-310", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 12, "players_max": 16,
 "field_size": "25 x 25 m",
 "description": "Drei Aufbauspieler lassen den Ball laufen und suchen den flachen Pass durch drei Verteidiger hindurch. Kommt der Pass bei der Gruppe an der Linie dahinter an, gibt das einen Punkt. Sofort greift diese Gruppe in die andere Richtung an, und die Passgeber verteidigen. Vier Dreiergruppen wechseln so Welle um Welle durch.",
 "organisation": ["Aufbauen: Ein Feld von etwa 25 mal 25 Metern. Zwei Linien teilen es, jede liegt 9 Meter vom Rand entfernt. Hütchen markieren die Ecken und die Linien.",
  "Verteilen: Vier Gruppen zu je drei Spielern. Eine Gruppe baut auf, eine verteidigt in der Mitte, je eine wartet an den beiden Linien. Der Trainer steht mit Bällen am Rand.",
  "Ablauf: Die Aufbauer spielen sich den Ball zu, bis eine Lücke aufgeht. Dann kommt der flache Pass durch die Verteidiger zur Gruppe an der Linie. Diese Gruppe greift sofort in die andere Richtung an, die Passgeber verteidigen, die alten Verteidiger gehen an die Linie.",
  "Wertung: Jeder Pass durch die Verteidiger zur Linie gibt einen Punkt. Gewinnen die Verteidiger den Ball, tauschen die Angreifer mit der Gruppe an der nächsten Linie."],
 "organisation_show": ORG,
 "coaching_points": ["Breit und tief stehen, das Feld groß machen", "Flach und scharf passen", "Kopf hoch, wo geht die Lücke auf?", "Nach dem Pass sofort umschalten"],
 "materials": ["8 Hütchen", "Viele Bälle", "Leibchen in vier Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Aufbauwelle drei gegen drei. Drei bauen auf, drei verteidigen, und hinter den Verteidigern wartet schon die nächste Gruppe auf den Pass.",
 "board": {"lines": LINES, "goals": [], "cones": CONES, "players": sp(), "balls": [B("b1", 42.1, 30.6)] + ERSATZ,
  "steps": [
   S("Aufbau über die Seite", "Team Neon baut auf. Spieler vier spielt nach außen zu Spieler sechs. Team Rot schiebt geschlossen zum Ball, Spieler sieben läuft an.",
     ps("b1", [43.1, 52.6]), mv("r7", [47.5, 50], delay=0.3), mv("r3", [50, 36], delay=0.3), mv("r2", [52, 22], delay=0.3)),
   S("Schnell auf die andere Seite", "Zurück in die Mitte und gleich weiter zu Spieler fünf. Jetzt muss Team Rot den ganzen Weg rüber. Spieler zwei sprintet weit raus, die anderen kommen nicht hinterher.",
     ps("b1", [42.1, 30.6]), ps("b1", [45.6, 12.6], after=True), mv("r2", [49.5, 9.5], delay=0.6), mv("r3", [50, 31], delay=0.7), mv("r7", [50, 44], delay=0.7)),
   S("Kopf hoch, wo ist die Lücke?", "Spieler fünf nimmt den Kopf hoch. Zwischen Spieler zwei und Spieler drei ist Platz, und genau dort bietet sich Spieler zehn an.",
     mv("g10", [62, 24]), bl("n5", [62, 24], delay=0.3)),
   S("Pass durch die Lücke: Punkt", "Flach durch die Lücke zu Spieler zehn, und das gibt einen Punkt für Team Neon. Sofort drehen sich die Rollen. Die drei von der Linie greifen in die andere Richtung an, Team Neon verteidigt, und Team Rot geht an die Linie.",
     ps("b1", [62.6, 24.6]), dr("g10", "b1", [56.5, 25], after=True), mv("g9", [56, 12], delay=0.9), mv("g11", [56, 48], delay=0.9),
     mv("n5", [40, 14], delay=0.9), mv("n4", [37, 30], delay=0.9), mv("n6", [40, 50], delay=0.9),
     mv("r2", [66, 4.5], delay=1.1), mv("r3", [67, 38], delay=1.1), mv("r7", [68, 43], delay=1.1))],
  "dims": dims(19, 80.4, 4, 56, "25 m", "25 m", rx=90)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Die Lücke sehen und sofort nutzen.", "Die Lücke sofort nutzen",
    "Rückt ein Verteidiger zu weit heraus, fehlt er in der Kette. Diese Lücke ist nur kurz offen. Wer den Ball hat, schaut vor dem Pass hoch und spielt flach hindurch, bevor die Verteidiger wieder zusammenrücken.",
    sp(), [B("b1", 42.1, 30.6)] + ERSATZ,
    [S("Spieler drei rückt zu weit raus", "Spieler drei will den Ball haben und läuft Spieler vier weit entgegen. Der bleibt ruhig und spielt nach außen zu Spieler sechs.",
       mv("r3", [46.5, 31.5]), ps("b1", [43.1, 52.6], delay=0.5), mv("r7", [49, 53.5], delay=0.7)),
     S("Blick in die Mitte", "Kopf hoch. Wo eben noch Spieler drei stand, ist jetzt alles offen.",
       bl("n6", [57.5, 35])),
     S("Durch die Mitte: Punkt", "Spieler sechs spielt sofort flach durch die Mitte zu Spieler zehn, und das gibt einen Punkt für Team Neon.",
       ps("b1", [62.6, 30.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Wer den Ball gewinnt, baut selbst auf.", "Ballgewinn tauscht die Teams",
    "Gewinnen die Verteidiger den Ball, ist die Welle für die Angreifer vorbei. Sie tauschen sofort mit der Gruppe an der nächsten Linie. Die Balleroberer bauen jetzt selbst auf. Dauert ein Angriff zu lange, gibt der Trainer eine Zeit vor.",
    sp(), [B("b1", 42.1, 30.6)] + ERSATZ,
    [S("Spieler drei fängt den Pass ab", "Spieler vier will zu Spieler fünf spielen. Spieler drei ahnt das, geht dazwischen und hat den Ball.",
       mv("r3", [46, 22]), ps("b1", [46.6, 22.6], delay=0.2)),
     S("Team Neon raus, die Nächsten rein", "Damit ist Team Neon raus und läuft zurück an die Linie. Von dort kommen die nächsten drei ins Feld und verteidigen.",
       mv("n5", [36, 6]), mv("n4", [35.5, 37]), mv("n6", [35, 55]),
       mv("h12", [40, 10], delay=0.5), mv("h13", [40, 24], delay=0.5), mv("h14", [40, 44], delay=0.5)),
     S("Team Rot baut jetzt auf", "Team Rot hat den Ball erobert und baut jetzt selbst auf. Spieler drei spielt raus zu Spieler zwei, und die nächste Welle läuft.",
       ps("b1", [54.1, 14.6]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
