import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 92-P5 (U12-U14, Woche 33 Phase 2): Increase the Pressure Game (Increasing Pressure on the Possession Team). 30 x 35 Yards =
# Feld x 28.6-71.4, y 5-55 (27 x 32 m), Ausrichtung wie im PDF. Pink (Ballbesitz, 8) -> Team Neon 3, 4, 5, 7, 8, 9, 10, 11 (wie im PDF);
# Blau (pressendes Team) -> Team Rot, neu nummeriert (im PDF doppelte Nummern): 2 und 6 bleiben, 4 -> 12, 5 -> 13, 7 -> 14,
# 8 -> 15, 9 -> 16, 11 -> 17. Start mit acht gegen eins (Spieler zwei innen), die anderen Roten warten links und rechts neben
# dem Feld (im PDF rundherum, wegen 3D-Abstand nur an den Seiten). Positionen auf ein Spaltenraster gesetzt, ein Trainer statt zwei.
# Wertung ergänzt: Spielt Team Rot nach Ballgewinn zu einem Mitspieler draußen oder zum Trainer, gibt das einen Punkt für Team Rot.
# Sichtkegel aus dem Text ("improves defensive awareness and positioning", Coaching-Punkt 2): Spieler zwei schaut zum freien Gegner
# und stellt sich in den Passweg. Im Video kein Kegel eingezeichnet, im Ton kein Hinweis.
# Ähnlich, aber keine Dublette: UE-151 (32-P6, 5 in innerer Zone, Verteidiger aus den Ecken, Minitore), UE-109, UE-170.
T = P("T", "c", 8, 32, "T")
POS = {"n8": (40.5, 12), "n11": (57.5, 11), "n4": (32, 26), "n7": (49, 28), "n10": (66, 24), "n9": (57.5, 41),
       "n5": (32, 45), "n3": (49, 50), "r2": (40.5, 34),
       "r17": (20, 6), "r14": (20, 22), "r12": (20, 38), "r15": (20, 54), "r6": (80, 10), "r13": (80, 28), "r16": (80, 46)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 11.6, 35.5), B("s2", 8, 35.5)]
LINES = [rect(28.6, 5, 42.8, 50)]

u = {"title": "Acht gegen immer mehr", "code": "UE-221", "kind": "Spielform",
 "focuses": ["Passspiel", "Zusammenspiel", "Verteidigen"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 16, "players_max": 16, "field_size": "27 x 32 m",
 "description": "Team Neon hält zu acht den Ball, zuerst gegen nur einen Verteidiger. Auf Zuruf des Trainers kommt immer ein weiterer Spieler von Team Rot ins Feld, bis acht gegen acht gespielt wird. Erobert Team Rot den Ball, spielt es ihn zu einem Mitspieler draußen oder zum Trainer. Nach einer festen Zeit tauschen die Teams die Rollen.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 32 Metern mit vier Hütchen.",
  "Verteilen: Team Neon zu acht im Feld. Von Team Rot ist ein Spieler im Feld, die anderen sieben warten links und rechts daneben. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Team Neon spielt sich den Ball zu. Auf Zuruf des Trainers kommt ein weiterer Spieler von Team Rot dazu: acht gegen zwei, acht gegen drei, bis acht gegen acht.",
  "Wertung und Wechsel: Erobert Team Rot den Ball und spielt ihn zu einem Mitspieler draußen oder zum Trainer, gibt das einen Punkt für Team Rot. Nach einer festen Zeit tauschen die Teams die Rollen."],
 "organisation_show": ORG,
 "coaching_points": ["Immer zwei oder drei Anspielstationen für den Ballführenden schaffen", "Ohne Ball laufen und das Feld groß machen", "Schnell passen und die Seite wechseln", "Als Verteidiger Passwege zustellen und Pässe abfangen"],
 "materials": ["4 Hütchen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Acht gegen immer mehr. Team Neon hält den Ball, und Team Rot wird mit jedem Zuruf des Trainers stärker.",
 "board": {"lines": LINES, "cones": ecken(28.6, 5, 42.8, 50), "players": sp(), "balls": [B("b1", 32.6, 26.6)] + ERSATZ,
  "steps": [
   S("Acht gegen eins", "Team Neon hält zu acht den Ball, nur Spieler zwei verteidigt. Spieler vier spielt zu Spieler sieben, der weiter zu Spieler elf.",
     ps("b1", [49.6, 28.6]), mv("r2", [45, 31], delay=0.3), ps("b1", [58.1, 11.6], after=True)),
   S("Der Nächste kommt", "Der Trainer ruft, und Spieler dreizehn läuft ins Feld. Jetzt heißt es acht gegen zwei. Spieler elf spielt zu Spieler zehn.",
     mv("r13", [66, 40]), ps("b1", [66.6, 24.6], delay=0.3)),
   S("Seite wechseln", "Spieler dreizehn läuft Spieler zehn an. Der spielt schnell zu Spieler neun, und der wechselt die Seite zu Spieler fünf.",
     mv("r13", [70, 30]), ps("b1", [58.1, 41.6], delay=0.3), ps("b1", [32.6, 45.6], after=True)),
   S("Abgefangen: Punkt", "Spieler fünf will zu Spieler drei passen, aber Spieler zwei fängt den Ball ab und spielt zu Spieler fünfzehn nach draußen. Das gibt einen Punkt für Team Rot. Dann bringt der Trainer einen neuen Ball, und Team Neon spielt weiter, bis die Teams die Rollen tauschen.",
     mv("r2", [41, 47.5]), ps("b1", [41.6, 48.1], delay=0.3), ps("b1", [20.6, 54.6], after=True))],
  "dims": dims(28.6, 71.4, 5, 55, "27 m", "32 m", rx=88)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Immer zwei oder drei Anspielstationen.", "Gute Passwinkel",
    "Wer den Ball hat, braucht immer zwei oder drei Mitspieler, die er anspielen kann. Dafür laufen die anderen so, dass kein Verteidiger zwischen ihnen und dem Ball steht. So bleibt der Ball sicher im Team.",
    sp(r13=(66, 40)), [B("b1", 32.6, 26.6)] + ERSATZ,
    [S("Anbieten", "Spieler vier hat den Ball, Spieler zwei und Spieler dreizehn verteidigen. Alle bieten sich gleichzeitig an: Spieler acht, Spieler sieben und Spieler fünf laufen so, dass der Passweg frei ist.",
       mv("n8", [38, 15]), mv("n7", [47, 26]), mv("n5", [30, 41])),
     S("Freien Mann finden", "Spieler vier hat drei Anspielstationen. Er spielt zu Spieler sieben, der hat Zeit und spielt weiter zu Spieler neun.",
       ps("b1", [47.6, 26.6]), ps("b1", [58.1, 41.6], after=True))]),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Passwege zustellen.", "Passwege zustellen",
    "Jetzt schauen wir auf Team Rot. Die Verteidiger stellen sich in die Passwege, statt nur dem Ball hinterherzulaufen. Dann muss Team Neon schwierige Pässe spielen, und Team Rot kann sie abfangen.",
    sp(r12=(49, 9), r13=(66, 40), r14=(32, 9), r16=(80, 36), n9=(57.5, 46)), [B("b1", 32.6, 26.6)] + ERSATZ,
    [S("Passweg sehen", "Spieler vier hat den Ball. Spieler zwei schaut, wo der freie Gegner steht, und stellt sich in den Passweg zu Spieler fünf. Spieler zwölf und Spieler vierzehn machen die anderen Wege zu.",
       bl("r2", [30, 48]), mv("r2", [34, 36], after=True), mv("r12", [42, 25.5], delay=0.9), mv("r14", [36, 19], delay=0.9)),
     S("Abgefangen: Punkt", "Spieler vier muss den langen Pass zu Spieler neun spielen. Spieler dreizehn fängt ihn ab und spielt zu Spieler sechzehn nach draußen. Das gibt einen Punkt für Team Rot.",
       mv("r13", [51, 41]), ps("b1", [51.6, 41.6], delay=0.2), ps("b1", [80.6, 36.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
