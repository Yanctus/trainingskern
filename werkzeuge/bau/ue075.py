import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# MB-P29: 25 x 35 Yards laut Text (Skizze: 20 x 25). Gedreht: Tore links/rechts, Feld x 12-88, y 7-53. 4 gegen 4 plus je ein Torwart, zwei Bälle.
T = P("T", "c", 94, 50, "T")
def sp(*l): return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, x, y in l] + [T]
cb = [B("c1", 91.5, 51.5), B("c2", 96.5, 52.8)]
goals = [{"x": 12, "y": 30, "side": "left"}, {"x": 88, "y": 30, "side": "right"}]
u = {"title": "Spiel mit zwei Bällen", "code": "UE-075", "kind": "Spielform",
 "focuses": ["Torschuss", "Umschalten", "Dribbling"], "age_groups": ["Bambini", "F-Jugend"], "duration_minutes": 10, "players_min": 10, "players_max": 10, "field_size": "32 x 23 m",
 "description": "Vier gegen vier mit Torwart auf zwei Tore, aber mit zwei Bällen gleichzeitig. Jedes Team startet mit einem Ball, greift also an und verteidigt zur selben Zeit. Fällt ein Tor oder geht ein Ball ins Aus, spielt der Trainer sofort einen neuen Ball ein. Ein Team darf auch beide Bälle haben.",
 "organisation": ["Aufbauen: Ein Feld von 32 mal 23 Metern mit je einem Tor an beiden Enden.",
  "Verteilen: Zwei Teams mit je vier Feldspielern und einem Torwart. Jedes Team bekommt zum Start einen Ball. Der Trainer steht mit weiteren Bällen an der Seite.",
  "Ablauf: Beide Bälle sind gleichzeitig im Spiel. Jedes Team greift mit seinem Ball an und versucht zugleich, den anderen Ball zu erobern. Jedes Tor gibt einen Punkt. Fällt ein Tor oder ist ein Ball im Aus, spielt der Trainer sofort einen neuen Ball ins Feld.",
  "Wertung: Ein Bonuspunkt für zwei Tore kurz hintereinander oder wenn ein Team beide Bälle zehn Sekunden lang behält. Die Teams überlegen sich selbst, wer angreift und wer verteidigt."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell vom Angreifen aufs Verteidigen umschalten", "Viel miteinander sprechen", "Das Durcheinander nutzen und schnell abschließen", "Immer auf den neuen Ball vom Trainer achten"],
 "materials": ["2 Tore", "4 orange Hütchen", "Leibchen in zwei Farben", "Viele Bälle beim Trainer"],
 "access": "frei", "hidden": True,
 "say_intro": "Spiel mit zwei Bällen. Beide Teams haben einen Ball, greifen an und verteidigen gleichzeitig.",
 "board": {"lines": [rect(12, 7, 76, 46)], "cones": ecken(12, 7, 76, 46), "goals": goals,
  "players": sp(("n1", 16, 30), ("n2", 30, 14), ("n3", 46, 12), ("n4", 40, 40), ("n5", 60, 46), ("r6", 84, 30), ("r7", 70, 16), ("r8", 55, 26), ("r9", 70, 36), ("r10", 30, 32)),
  "balls": [B("b1", 41.6, 40.6), B("b2", 68.4, 16.6)] + cb,
  "steps": [
   S("Beide Teams starten mit Ball", "Jedes Team startet mit einem Ball. Gleichzeitig spielt Spieler vier zu Spieler fünf und Spieler sieben zu Spieler acht.",
     ps("b1", [61.6, 46.6]), ps("b2", [53.4, 26.6])),
   S("Angreifen und verteidigen zugleich", "Spieler fünf dribbelt auf das rechte Tor, Spieler acht auf das linke. Wer keinen Ball hat, verteidigt sofort: Spieler neun läuft zu Spieler fünf, Spieler zwei zu Spieler acht.",
     dr("n5", "b1", [72, 47]), dr("r8", "b2", [38, 22]), mv("r9", [66, 42], delay=0.3), mv("n2", [33, 17], delay=0.3)),
   S("Zwei Abschlüsse", "Beide schießen fast gleichzeitig. Das Tor von Spieler fünf gibt einen Punkt für Neon, das Tor von Spieler acht einen Punkt für Rot.",
     ps("b1", [87.5, 33.5]), ps("b2", [12.5, 26])),
   S("Der Trainer spielt den nächsten Ball", "Sofort spielt der Trainer einen neuen Ball ins Feld. Spieler drei ist zuerst dort und startet den nächsten Angriff.",
     ps("c1", [60, 24]), mv("n3", [58, 22], delay=0.3))],
  "dims": [{"x1": 12, "y1": 58.6, "x2": 88, "y2": 58.6, "text": "32 m"}, {"x1": 5, "y1": 7, "x2": 5, "y2": 53, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Immer wissen, wo der Trainer den nächsten Ball hineinspielt.", "Den neuen Ball sehen",
    "Der Trainer spielt jederzeit einen neuen Ball ein. Wer sich ständig umschaut, sieht ihn früh, sprintet als Erster hin und startet sofort den nächsten Angriff. Nicht stehen bleiben und zuschauen, sondern immer bereit sein.",
    sp(("n1", 16, 30), ("n2", 28, 44), ("n3", 58, 22), ("n4", 36, 14), ("n5", 76, 14), ("r6", 84, 30), ("r7", 46, 10), ("r8", 26, 18), ("r9", 68, 30), ("r10", 44, 46)),
    [B("b1", 59.6, 22.6), B("b2", 47.6, 10.6)] + cb,
    [S("Neuer Ball kommt", "Der Trainer spielt einen neuen Ball ins Feld. Spieler zehn hat sich umgeschaut und sieht ihn sofort.", ps("c1", [56, 38])),
     S("Hin und los", "Spieler zehn sprintet als Erster zum Ball und dribbelt sofort los nach links.", mv("r10", [54.5, 38.5]), dr("r10", "c1", [33, 24], after=True)),
     S("Abschluss", "Spieler zehn schießt flach ins Tor, und das gibt einen Punkt für Rot.", ps("c1", [12.5, 26.5]))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Herrscht hinten Durcheinander, schnell den freien Ball holen und abschließen.", "Das Durcheinander nutzen",
    "Mit zwei Bällen wissen die Verteidiger oft nicht, wer wohin muss. Liegt hinten ein Ball frei, schnell hinlaufen, den Ball holen und sofort abschließen, bevor sich die Abwehr sortiert hat.",
    sp(("n1", 16, 30), ("n2", 30, 14), ("n3", 46, 12), ("n4", 40, 44), ("n5", 56, 30), ("r6", 84, 30), ("r7", 44, 28), ("r8", 72, 20), ("r9", 72, 40), ("r10", 28, 32)),
    [B("b1", 41.6, 44.6), B("b2", 65, 29)] + cb,
    [S("Freier Ball hinten", "Hinten bei Rot liegt ein Ball frei. Spieler acht und Spieler neun schauen beide hin und zögern.", mv("r8", [71, 22.5]), mv("r9", [71, 37.5], delay=0.2)),
     S("Schneller am Ball", "Spieler fünf ist schneller, sprintet zum Ball und nimmt ihn mit.", mv("n5", [63.5, 28.5])),
     S("Sofort abschließen", "Spieler fünf schießt sofort, bevor sich die Abwehr sortiert, und das gibt einen Punkt für Neon.", ps("b2", [87.5, 26]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
