import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 23-P3: 30 x 30 Yards, gedreht (großes Tor rechts): Feld x 14-86, y 8-52. Zone für das 2 gegen 1 vor dem Tor (x 51-86, y 19-42).
T = P("T", "c", 40, 30, "T")
CB = [B("c1", 42.5, 30.6), B("c2", 39, 33.5)]
POS = {"n3": (24, 22), "n4": (14, 15), "r7": (24, 38), "r8": (14, 45), "n2": (72, 40), "r6": (61, 34)}
def sp(d=None):
    d = dict(d or POS)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [P("k", "t", 82, 30, "TW"), T]
ZONE = {"type": "zone", "x": 51, "y": 19, "w": 35, "h": 23}
LINES = [rect(14, 8, 72, 44), ZONE]
CONES = [C(28, 30), C(45, 18), C(45, 42), C(35, 14, "neon", shape="stange"), C(35, 46, "neon", shape="stange")]
TORE = [{"x": 86, "y": 30, "side": "right"}, {"x": 52, "y": 8, "side": "top"}, {"x": 52, "y": 52, "side": "bottom"}]
def rennen(i, s, **k):
    pts = [(31, 30 + 21 * s), (44, 30 + 17 * s), (49, 30 + 11 * s)]
    return [mv(i, list(p), after=n > 0 or None, **(k if n == 0 else {})) for n, p in enumerate(pts)]
u = {"title": "Wettlauf, dann zwei gegen eins", "code": "UE-119", "kind": "Spielform",
 "focuses": ["Schnelligkeit", "Torschuss", "Umschalten"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 7, "players_max": 12, "field_size": "27 x 27 m",
 "description": "Zwei Spieler laufen um die Wette um Stange und Hütchen zum Ball, den der Trainer ins Feld spielt. Wer zuerst am Ball ist, greift mit dem wartenden Mitspieler in der Zone vor dem Tor zwei gegen eins an und schließt ab. Erobert der Verteidiger den Ball, kontert er auf eines der beiden Minitore.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern mit einem großen Tor und Torhüter rechts. Davor eine Zone von etwa 18 mal 18 Metern, oben und unten je ein Minitor.",
  "Verteilen: Team Neon wartet oben links, Team Rot unten links, getrennt durch ein Hütchen. In der Zone stehen ein Angreifer von Team Neon und ein Verteidiger von Team Rot. Der Trainer steht mit Bällen in der Mitte.",
  "Ablauf: Je ein Spieler beider Teams läuft um seine Stange und sein Hütchen zum Ball des Trainers. Wer ihn zuerst hat, greift mit dem Mitspieler in der Zone zwei gegen eins an. Ein Tor gibt einen Punkt. Erobert der Verteidiger den Ball, schießt er auf ein Minitor.",
  "Wechsel: Nach jedem Durchgang wird rotiert, damit jeder jede Rolle spielt. Mit hohem Tempo arbeiten."],
 "organisation_show": ORG,
 "coaching_points": ["Mit Tempo das Rennen gewinnen, um die Überzahl zu bekommen", "Den ersten Kontakt nach vorn mitnehmen und auf den Verteidiger zudribbeln", "Vor dem Tor die richtige Entscheidung treffen: Pass oder Abschluss", "Schnell zusammenspielen und mutig angreifen"],
 "materials": ["1 großes Tor", "2 Minitore", "2 Stangen", "3 orange Hütchen", "Mehrere Bälle beim Trainer", "Leibchen in drei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Wettlauf, dann zwei gegen eins. Wer zuerst am Ball ist, bekommt vor dem Tor die Überzahl.",
 "board": {"lines": LINES, "cones": CONES, "goals": TORE, "players": sp(), "balls": CB,
  "steps": [
   S("Wettlauf zum Ball", "Gleichzeitig sprinten Neon drei und Rot sieben um ihre Stange und ihr Hütchen. Der Trainer spielt den Ball ins Feld, und Neon drei ist zuerst da.",
     *rennen("n3", -1), mv("n3", [50, 22], after=True), *rennen("r7", 1, delay=0.4), ps("c1", [51.6, 22.6], delay=1.2)),
   S("Zwei gegen eins", "Neon drei dribbelt in die Zone. Rot sechs kommt heraus, und Neon drei spielt zu Neon zwei.",
     dr("n3", "c1", [60, 22]), mv("r6", [60, 28], delay=0.2), ps("c1", [70.4, 40.6], after=True)),
   S("Abschluss", "Neon zwei schließt sofort ab und trifft ins große Tor. Das gibt einen Punkt für Team Neon.",
     ps("c1", [85.5, 35]))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "27 m"}, {"x1": 94, "y1": 8, "x2": 94, "y2": 52, "text": "27 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Der erste Kontakt geht nach vorn.", "Erster Kontakt nach vorn",
    "Wer das Rennen gewinnt, nimmt den Ball mit dem ersten Kontakt nach vorn in den freien Raum mit und dribbelt direkt auf den Verteidiger zu. So muss der Verteidiger sich entscheiden, und der Mitspieler wird frei.",
    sp(dict(POS, n3=(50, 22), r7=(49, 41))), [B("g", 51.6, 22.6)] + CB,
    [S("Mitnahme nach vorn", "Neon drei nimmt den Ball mit dem ersten Kontakt weit nach vorn mit und dribbelt auf Rot sechs zu.",
       dr("n3", "g", [60, 22]), mv("r6", [60, 28], delay=0.3)),
     S("Pass zum Freien", "Rot sechs muss Neon drei angreifen. Jetzt ist Neon zwei frei, bekommt den Ball und schießt ins Tor. Das gibt einen Punkt für Team Neon.",
       ps("g", [70.4, 40.6]), ps("g", [85.5, 35], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Erobert der Verteidiger den Ball, wird sofort gekontert.", "Ballgewinn und Konter",
    "Fängt der Verteidiger den Ball ab, schaltet er sofort um und schießt auf eines der beiden Minitore. Das ist wie im Spiel: Nach dem Ballgewinn wird schnell nach vorn gespielt. Für die Angreifer heißt das, nach einem Ballverlust sofort nachzusetzen.",
    sp(dict(POS, n3=(58, 22), n2=(72, 47), r6=(67, 31))), [B("g", 59.6, 22.6)] + CB,
    [S("Ball abgefangen", "Neon drei spielt zu Neon zwei, aber Rot sechs läuft in den Pass und fängt den Ball ab.",
       ps("g", [65, 38]), mv("r6", [64, 37], delay=0.2)),
     S("Konter aufs Minitor", "Rot sechs dribbelt sofort los und schießt ins untere Minitor. Das gibt einen Punkt für Team Rot.",
       dr("r6", "g", [56, 45]), ps("g", [52, 51.5], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
