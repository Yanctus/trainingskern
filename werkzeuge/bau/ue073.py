import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 43-P1: 15 x 20 Yards, gedreht (Start links, Viereck rechts): Feld x 18-82, y 6-54. Viereck x 52-76, y 15-45 (etwas größer als im PDF, damit sich in 3D niemand verdeckt).
T = P("T", "c", 9, 50, "T")
def spieler(extra=()):
    return [P("n4", "a", 28, 31, "4"), P("n9", "a", 73, 30, "9"), P("n10", "a", 60, 45, "10"), P("n11", "a", 60, 15, "11"), T] + list(extra)
def baelle(): return [B("b1", 29.6, 31.6), B("c1", 11.5, 51), B("c2", 8, 53.5)]
lines = [rect(18, 6, 64, 48)]
cones = ecken(52, 15, 24, 30) + [C(28, 36.5)]
lines.append(rect(52, 15, 24, 30))
druck = mv("n10", [64.5, 32], delay=0.3)
dp = [ps("b1", [61.5, 16.6]), mv("n9", [69, 43], delay=0.2), mv("n9", [57, 41], after=True), ps("b1", [58.6, 41.6], after=True)]
u = {"title": "Doppelpass um den Gegner", "code": "UE-073", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Bewegung"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 4, "players_max": 6, "field_size": "18 x 14 m",
 "description": "Drei Spieler stehen in einem Viereck, ein vierter startet mit Ball davor. Sein Pass zum entferntesten Spieler ist das Startsignal: Ein Spieler im Viereck läuft heraus und setzt nur halb unter Druck. Die beiden anderen spielen einen Doppelpass um ihn herum und passen danach zurück zum Start. Möglichst alles mit einem Kontakt.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 14 Metern. Im hinteren Teil ein Viereck mit vier Hütchen, vorne ein Hütchen als Startpunkt.",
  "Verteilen: Drei Spieler stehen im Viereck: einer ganz hinten, je einer an den beiden Seiten. Der vierte Spieler steht mit Ball am Start.",
  "Ablauf: Der Start spielt zum hintersten Spieler. Sofort läuft der Spieler einer Seite heraus und setzt nur halb unter Druck. Der Angespielte und der Spieler der anderen Seite spielen einen Doppelpass um ihn herum, dann geht der Ball zurück zum Start.",
  "Wechsel: Der hinterste Spieler und der Störer tauschen die Rollen, der Partner beim Doppelpass bleibt. Die Seite regelmäßig wechseln und alle paar Durchgänge einen neuen Startspieler bestimmen, damit jeder jede Rolle spielt."],
 "organisation_show": ORG,
 "coaching_points": ["Wo es geht mit einem Kontakt spielen, Tempo und Richtung des Passes stimmen", "Schnell herauslaufen, aber nur halb unter Druck setzen", "Auf den Zehen bleiben und den Rückpass zum Start fest spielen", "Vor und nach jedem Pass miteinander sprechen"],
 "materials": ["5 orange Hütchen", "Mehrere Bälle beim Trainer", "2 Minitore für die zweite Steigerung"],
 "access": "frei", "hidden": True,
 "say_intro": "Doppelpass um den Gegner. Drei Spieler im Viereck, einer am Start, und möglichst alles mit einem Kontakt.",
 "board": {"lines": lines, "cones": cones, "players": spieler(), "balls": baelle(),
  "steps": [
   S("Pass nach hinten, Störer kommt", "Spieler vier spielt flach zu Spieler neun ganz hinten. Der Pass ist das Signal: Gleichzeitig läuft Spieler zehn heraus und setzt Spieler neun halb unter Druck.",
     ps("b1", [71.4, 30.6]), druck),
   S("Doppelpass um den Störer", "Spieler neun spielt direkt zu Spieler elf und läuft hinter Spieler zehn vorbei in den freien Raum. Spieler elf spielt direkt in seinen Lauf.", *dp),
   S("Zurück zum Start, Rollen tauschen", "Spieler neun spielt fest zurück zu Spieler vier. Danach tauschen Spieler neun und Spieler zehn die Rollen, Spieler elf bleibt.",
     ps("b1", [29.6, 31.6]), mv("n10", [73, 30], after=True), mv("n9", [60, 45], after=True))],
  "dims": [{"x1": 18, "y1": 58.6, "x2": 82, "y2": 58.6, "text": "18 m"}, {"x1": 90, "y1": 6, "x2": 90, "y2": 54, "text": "14 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Auf den Zehen bleiben und mit einem Kontakt spielen.", "Ein Kontakt, dann fest zurück",
    "Wer auf den Zehen steht, ist für jeden Pass bereit. Möglichst mit einem Kontakt spielen, mit dem richtigen Tempo und genau in den Fuß oder in den Lauf. Vor dem Pass kurz ansagen, was man vorhat. Der Rückpass zum Start kommt besonders fest, damit es sofort weitergehen kann.",
    [P("n4", "a", 28, 31, "4"), P("n9", "a", 73, 30, "9"), P("n10", "a", 64.5, 32, "10"), P("n11", "a", 60, 15, "11"), T],
    [B("b1", 71.4, 30.6), B("c1", 11.5, 51), B("c2", 8, 53.5)],
    [S("Mit einem Kontakt", "Spieler neun lässt den Ball nicht erst liegen, sondern spielt ihn mit einem Kontakt zu Spieler elf. Spieler elf spielt ebenfalls direkt.", *dp),
     S("Fest zurück", "Der Rückpass zu Spieler vier kommt flach und fest. So beginnt der nächste Durchgang ohne Pause.", ps("b1", [29.6, 31.6]))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Startspieler läuft nach seinem Pass mit ins Viereck.", "Start läuft mit",
    "Am Start wartet ein fünfter Spieler. Nach seinem Pass sprintet der Startspieler an den Rand des Vierecks und ist im nächsten Durchgang dabei. Wer zum Start zurückspielt, läuft seinem Pass hinterher und stellt sich dort an. So sind alle ständig in Bewegung und müssen mehr miteinander sprechen.",
    spieler([P("n8", "a", 19.5, 31, "8")]), baelle(),
    [S("Pass und hinterher", "Spieler vier spielt zu Spieler neun und sprintet sofort an den Rand des Vierecks. Gleichzeitig läuft Spieler zehn als Störer heraus.",
       ps("b1", [71.4, 30.6]), mv("n4", [49, 51], delay=0.2), druck),
     S("Doppelpass um den Störer", "Spieler neun und Spieler elf spielen den Doppelpass um Spieler zehn herum, wie in der Grundform.", *dp),
     S("Zurück und mitlaufen", "Spieler neun spielt zum neuen Startspieler acht und läuft seinem Pass hinterher zum Start. Gleichzeitig rücken Spieler vier und Spieler zehn auf die freien Plätze im Viereck.",
       ps("b1", [21.1, 31.6]), mv("n9", [29, 31], delay=0.3), mv("n4", [60, 45], delay=0.3), mv("n10", [73, 30], delay=0.3))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei Minitore, und der Doppelpass endet mit einem Abschluss.", "Abschluss ins Minitor",
    "Zwischen Start und Viereck stehen zwei Minitore schräg an den Seiten. Nach dem Doppelpass wird nicht zurückgespielt, sondern ins schräg gegenüberliegende Minitor geschossen, mit Gefühl statt mit voller Kraft. Sofort spielt der Trainer den nächsten Ball zum Start, und es geht weiter.",
    spieler(), [B("b1", 29.6, 31.6), B("c1", 11.5, 51), B("c2", 8, 53.5)],
    [S("Pass nach hinten, Störer kommt", "Spieler vier spielt zu Spieler neun, gleichzeitig läuft Spieler zehn als Störer heraus.", ps("b1", [71.4, 30.6]), druck),
     S("Doppelpass um den Störer", "Spieler neun und Spieler elf spielen den Doppelpass um Spieler zehn herum.", *dp),
     S("Abschluss ins Minitor", "Spieler neun schießt genau ins schräg gegenüberliegende Minitor oben, und das gibt einen Punkt für Spieler neun.", ps("b1", [40, 11.5])),
     S("Trainer spielt den nächsten Ball", "Sofort spielt der Trainer den nächsten Ball zu Spieler vier. Gleichzeitig tauschen Spieler neun und Spieler zehn die Rollen.",
       ps("c1", [29.6, 31.6]), mv("n10", [73, 30]), mv("n9", [60, 45]))],
    goals=[{"x": 40, "y": 12, "side": "top"}, {"x": 40, "y": 48, "side": "bottom"}])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
