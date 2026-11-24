import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 88-P4 (U15-U17, Woche 20 Phase 4): Pressing Activation, Technical. 10 x 10 Yards = 9 x 9 m, Feld x 25-75, y 5-55.
# Vier Puppen (als Stangen gezeichnet) als Raute: links (32,30), oben (50,12), rechts (68,30), unten (50,48). Ausrichtung wie
# im PDF. Ein Team (Pink) -> Team Neon, Nummern wie im PDF. An jeder Puppe stehen im Original drei Spieler; auf der Tafel nur
# die ersten zwei (3D-Abstand), der dritte (6, 12, 7, 2) nur im Text. Trainer außerhalb oben rechts statt im Feld
# (im Feld stünde er in der 3D-Ansicht vor Spieler fünf).
# Ablauf nach PDF und Video: Trainer spielt Spieler vier an, der Spieler an der Puppe gegenüber (5) läuft an. Annehmen, Pass
# nach links (zur Puppe oben), dann zur Puppe rechts von sich laufen. Der Pass löst den Nächsten gegenüber aus (10).
# Annahme (nicht eindeutig im Original): Der Anläufer stellt sich danach an der Puppe an, an der er angelaufen hat.
# Keine Punktwertung (Technikübung).
# Fassungen: PDF Key Coaching Point (auf den Zehen, ständig scannen, in jede Richtung bereit) und Progression (Passseite
# selbst wählen und in die andere Richtung laufen).
# Sichtkegel aus dem Text (Key Coaching Point „scanning constantly“, Summary „Recognise quickly which side pass is played“) und
# Video (Kegel beim Anläufer eingezeichnet): Der nächste Anläufer schaut auf den Ball, bevor der Pass kommt.
T = P("T", "c", 80, 12, "T")  # außerhalb oben rechts
ERSATZ = [B("s1", 83.5, 12.6), B("s2", 86, 12.6)]
POS = {"n4": (37.5, 33), "n3": (26.5, 37), "n11": (53, 17.5), "n9": (62, 7),
       "n5": (63, 27), "n14": (75, 36), "n10": (54.5, 44.5), "n8": (44, 54.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(i): return [round(POS[i][0] + 0.6, 1), round(POS[i][1] + 0.6, 1)]
PUPPEN = [C(32, 30, shape="stange"), C(50, 12, shape="stange"), C(68, 30, shape="stange"), C(50, 48, shape="stange")]
LINES = [rect(25, 5, 50, 50)]
DIMS = dims(25, 75, 5, 55, "9 m", "9 m", rx=91)

u = {"title": "Anlaufen an vier Puppen", "code": "UE-355", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Passspiel", "Schnelligkeit"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "9 x 9 m",
 "description": "Eine kurze Technikübung, die das Anlaufen aktiviert. Vier Puppen stehen als Raute, an jeder warten zwei oder drei Spieler. Der Ball läuft von Puppe zu Puppe, und bei jedem Pass sprintet der Spieler von der Puppe gegenüber los und läuft den Annehmenden an. Wer gepasst hat, läuft zur Puppe rechts von sich.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern. Vier Puppen stehen als Raute, je eine links, oben, rechts und unten.",
  "Verteilen: An jeder Puppe stehen drei Spieler, der Erste vor der Puppe. Der Trainer steht mit Bällen außen an einer Ecke.",
  "Ablauf: Der Trainer spielt den Ersten an der Puppe links an. Sofort läuft der Erste von der Puppe gegenüber an. Der Annehmende spielt mit dem zweiten Kontakt zur Puppe links von sich und läuft zur Puppe rechts von sich. Jeder Pass löst den Nächsten gegenüber aus.",
  "Wechsel: Der Anläufer stellt sich danach an der Puppe an, an der er angelaufen hat. Gezählt wird nicht, der Ball läuft ohne Pause im Kreis. Nach ein paar Minuten wird die Passrichtung gewechselt."],
 "organisation_show": ORG,
 "coaching_points": ["Die ersten Meter mit Vollgas anlaufen", "Kurz vor ihm abbremsen, Knie beugen, seitlich stellen", "Erster Kontakt zur Seite, zweiter Kontakt ist der Pass", "Auf den Zehen bleiben und auf den Ball schauen"],
 "materials": ["4 Puppen", "Viele Bälle"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Anlaufen an vier Puppen. Der Ball läuft im Kreis von Puppe zu Puppe. Bei jedem Pass sprintet einer von gegenüber los und setzt den Annehmenden unter Druck.",
 "board": {"lines": LINES, "goals": [], "cones": PUPPEN, "players": sp(), "balls": [B("b1", 80.6, 12.6)] + ERSATZ,
  "steps": [
   S("Trainer spielt an, gegenüber läuft an", "Der Trainer spielt Spieler vier an der Puppe links an. Im selben Moment sprintet Spieler fünf von der Puppe gegenüber los. Die ersten Meter mit Vollgas, kurz vor Spieler vier bremst er ab.",
     ps("b1", fuss("n4")), mv("n5", [45.5, 32], delay=0.3)),
   S("Ein Kontakt zur Seite, Pass nach links", "Spieler vier nimmt den Ball zur Seite mit und spielt zur Puppe links von sich, zu Spieler elf. Danach läuft er zur Puppe rechts von sich und stellt sich dort an.",
     dr("n4", "b1", [39, 29.5]), ps("b1", [53.6, 18.1], after=True), mv("n4", [41, 50], after=True)),
   S("Der Pass löst den Nächsten aus", "Jetzt hat Spieler elf den Ball, also läuft Spieler zehn von unten an. Spieler elf legt sich den Ball vor und spielt weiter zu Spieler vierzehn, der vor seine Puppe kommt. Spieler fünf stellt sich hinten links an.",
     mv("n10", [52, 25.5]), mv("n5", [27, 20], delay=0.4), mv("n14", [64.5, 35.5], delay=0.4),
     dr("n11", "b1", [58, 19], delay=0.3), ps("b1", [65.1, 36.1], after=True)),
   S("Weiter im Kreis, keine Pause", "Spieler drei sprintet zu Spieler vierzehn, und Spieler elf läuft zur Puppe rechts von sich. Punkte gibt es hier keine. Der Ball läuft einfach weiter im Kreis, und als Nächster spielt Spieler vierzehn nach links.",
     mv("n3", [57, 35]), mv("n11", [36, 19], delay=0.2), mv("n11", [24.5, 27.5], after=True))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Wach bleiben, auf den Zehen und den Ball im Blick.", "Auf den Zehen, Ball im Blick",
    "Wer an der Puppe wartet, steht nicht einfach herum. Er bleibt auf den Zehen und schaut auf den Ball. So sieht er früh, wohin der Pass geht, und ist sofort weg. Kurz vor dem Gegner bremst er ab, beugt die Knie und stellt sich seitlich.",
    sp(), [B("b1", *fuss("n4"))] + ERSATZ,
    [S("Auf den Zehen, Blick zum Ball", "Spieler zehn wartet unten. Er steht auf den Zehen und schaut auf Spieler vier mit dem Ball. Der spielt nach oben zu Spieler elf, und Spieler zehn ist sofort weg.",
       bl("n10", [37.5, 33]), ps("b1", [53.6, 18.1], after=True), mv("n10", [53.5, 27.5], after=True)),
     S("Abbremsen und seitlich stellen", "Die letzten Schritte werden kurz. Spieler zehn beugt die Knie und stellt sich seitlich. Spieler elf nimmt den Ball zur Seite mit, und Spieler zehn geht den Schritt mit.",
       dr("n11", "b1", [58, 19]), mv("n10", [55.5, 25.5], delay=0.3))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Annehmende sucht sich die Passseite selbst aus.", "Passseite selbst wählen",
    "Wer den Ball hat, entscheidet selbst, ob er nach links oder nach rechts spielt. Danach läuft er immer in die andere Richtung. Die Wartenden wissen also nicht mehr, wer als Nächstes dran ist. Sie müssen den Ball beobachten und schnell reagieren.",
    sp(), [B("b1", 80.6, 12.6)] + ERSATZ,
    [S("Trainer spielt an, Spieler fünf läuft an", "Wie vorher spielt der Trainer zu Spieler vier, und Spieler fünf läuft von gegenüber an.",
       ps("b1", fuss("n4")), mv("n5", [45.5, 32], delay=0.3)),
     S("Andere Seite, andere Richtung", "Spieler vier spielt diesmal nach unten zu Spieler zehn. Danach läuft er in die andere Richtung, zur Puppe oben. Spieler elf schaut genau hin, denn jetzt ist er gefragt.",
       bl("n11", [38, 34]), dr("n4", "b1", [40, 36], delay=0.3), ps("b1", fuss("n10"), after=True), mv("n4", [40, 12], after=True)),
     S("Spieler elf reagiert", "Der Ball ist unten, also sprintet Spieler elf von oben los und läuft Spieler zehn an. Wer zu spät schaut, kommt zu spät.",
       mv("n11", [54, 37]))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
