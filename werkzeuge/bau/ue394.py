import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 65-P12 (U15-U17, Woche 34 Phase 5): Playing the High Line (PDF: How to Play the High Defensive Line). Im Titel und in den
# Texten keine Länder- oder Vereinsnamen (Vorgabe). Feld 35 x 40 Yards = 32 x 37 m, gerundet 30 x 35 m (Breite nach PDF und
# Video geschätzt, die Länge 5 + 15 + 10 + 10 Yards steht im PDF). Verhältnis 1,2: kein langes Feld, kein Großfeld, hochkant.
# Um 180 Grad gedreht: Team Rot greift nach oben an, die Zielzone liegt oben, die schmale Zone (5 Yards) unten.
# Feld x 15-85, y 5-55 (in der Breite etwas gestreckt, damit Kette und Spitzen den 3D-Abstand halten). Zielzone 10 Yards
# (y 5-17.5, Zone von Team Rot, orange), Zone der Kette 10 Yards, Mittelstreifen 15 Yards mit Quadrat 15 x 15 Yards
# (gestrichelt), schmale Zone 5 Yards (y 48.75-55, Zone von Team Neon). Mittelkreis weggelassen.
# PDF pink (Viererkette und Mittelfeldpaar) -> Team Neon, navy -> Team Rot. Keine Nummern im PDF: Neon 2, 3, 4, 5 (Kette),
# 6, 8 (Paar); Rot 10, 14 (Quadrat), 13 (Helfer), 7, 11 (Flügel), 9, 12 (Spitzen). Ein Trainer statt zwei (links an der Seite).
# Positionen auf ein Spaltenraster gesetzt (3D-Abstand), die Spitzen stehen zwischen den Verteidigern.
# Grundform nach PDF, Ton und Video: zwei gegen zwei plus Helfer, nach fünf Pässen auf den Flügel, der Flügelspieler bricht
# durch, Ablage und Pass in die Tiefe, Punkt für Team Rot.
# Fassungen: PDF Key Coaching Point 1 (Paar bleibt eng, nicht auseinanderziehen lassen; hier der richtige Ablauf mit Ballgewinn
# und Punkt in der schmalen Zone) und 2 (Kette rückt gemeinsam raus, Spitze im Abseits).
# Sichtkegel: Text „Checks to see attackers positioning“ und „Awareness of long balls … in behind“, im Video kein Kegel
# eingezeichnet: Spieler vier achtet vor dem Rausrücken auf Spieler neun (nur im Text, kein Kegel beim Verteidiger nach der
# Regel vom 25.11.2026).
# Keine Dublette: UE-162 (65-P6, fünf gegen fünf mit Endzonen und Minitoren), UE-380 (78-P13, halbes Feld mit großem Tor)
# und UE-320 (78-P4) haben andere Zonen und Abläufe.
T = P("T", "c", 7.5, 50, "T")
ERSATZ = [B("s1", 4.5, 53.5), B("s2", 11, 53.5)]
POS = {"n3": (19, 22), "n5": (37.5, 20.5), "n4": (62.5, 20.5), "n2": (81, 22), "n8": (45, 36.5), "n6": (55, 36.5),
       "r12": (28, 25), "r9": (72, 25), "r14": (36.5, 47), "r10": (63.5, 47), "r11": (19, 40), "r7": (81, 40), "r13": (50, 52.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(15, 5, 70, 50), {"type": "zone", "x": 15, "y": 5, "w": 70, "h": 12.5, "color": "orange"},
         {"type": "zone", "x": 15, "y": 48.75, "w": 70, "h": 6.25},
         line(15, 17.5, 85, 17.5), line(15, 30, 85, 30), line(15, 48.75, 85, 48.75), rect(35, 30, 30, 18.75, dashed=True)]
DIMS = dims(15, 85, 5, 55, "30 m", "35 m", rx=94)
def f(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]

u = {"title": "Hohe Linie mit Abseitsfalle", "code": "UE-394", "kind": "Spielform",
 "focuses": ["Verteidigen", "Zusammenspiel", "Umschalten"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 13, "players_max": 13,
 "field_size": "30 x 35 m",
 "description": "Eine hohe Abwehrlinie mit Abseitsfalle. Im Zentrum spielen zwei gegen zwei, ein dritter Angreifer hilft von außen. Nach fünf Pässen geht der Ball auf einen Flügel, und vier Angreifer wollen gegen die Viererkette in die Zone dahinter. Die Kette schiebt als Linie, rückt gemeinsam raus und stellt die Angreifer ins Abseits.",
 "organisation": ["Aufbauen: Ein Feld von 30 mal 35 Metern, quer in vier Streifen geteilt. Am einen Ende die Zielzone von Team Rot, 9 Meter tief, davor die Zone der Viererkette, ebenfalls 9 Meter. Dann ein Streifen von 14 Metern mit einem Quadrat in der Mitte, am anderen Ende eine schmale Zone von 4,5 Metern.",
  "Verteilen: Team Neon mit der Viererkette in ihrer Zone und zwei Mittelfeldspielern im Quadrat. Team Rot mit zwei Spielern im Quadrat, einem Helfer in der schmalen Zone, je einem Flügelspieler neben dem Quadrat und zwei Spitzen bei der Kette. Der Trainer steht mit Bällen an der Seite.",
  "Ablauf: Im Quadrat spielen zwei gegen zwei, der Helfer spielt für Team Rot mit. Nach fünf Pässen, oder wenn Team Rot durch das Paar durchspielt, geht der Ball auf einen Flügel. Dann greifen vier Angreifer die Kette an und wollen mit Pass und Lauf in die Zielzone.",
  "Wertung: Kommt Team Rot mit Ball in die Zielzone, gibt das einen Punkt für Team Rot. Erobert das Paar den Ball im Quadrat und kommt mit ihm in die schmale Zone, gibt das einen Punkt für Team Neon. Auch ein Ballgewinn der Kette oder ein Angreifer im Abseits gibt einen Punkt für Team Neon."],
 "organisation_show": ORG,
 "coaching_points": ["Das Paar presst, die Kette rückt nach", "Kein Druck auf den Ball, die Kette fällt ab", "Laut sprechen und eine Linie halten", "Schulterblick zu den Spitzen"],
 "materials": ["Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Hohe Linie mit Abseitsfalle. Die Viererkette steht hoch und schiebt als Linie. Im Zentrum spielen zwei gegen zwei, und nach fünf Pässen greifen vier Angreifer die Kette an.",
 "board": {"lines": LINES, "goals": [], "cones": [], "players": sp(), "balls": [B("b1", *f(63.5, 47)), B("b0", 8.1, 50.6)] + ERSATZ,
  "steps": [
   S("Zwei gegen zwei im Quadrat", "Spieler zehn spielt zurück zu Spieler dreizehn, der draußen hilft. Weiter zu Spieler vierzehn. Spieler acht läuft ihn an, Spieler sechs bleibt nah bei ihm. Weil das Paar drückt, rückt die Kette ein Stück nach.",
     ps("b1", f(50, 52.5)), ps("b1", f(36.5, 47), after=True), mv("n8", [40, 41.5], delay=0.8), mv("n6", [49, 39], delay=0.9),
     mv("n3", [19, 24], delay=1.0), mv("n5", [37.5, 23], delay=1.0), mv("n4", [62.5, 23], delay=1.0), mv("n2", [81, 24], delay=1.0)),
   S("Fünf Pässe, dann auf den Flügel", "Nach dem fünften Pass darf der Ball raus. Spieler vierzehn spielt quer zu Spieler zehn, und der spielt gleich weiter auf Spieler sieben. Die Kette schiebt zusammen zum Ball.",
     ps("b1", f(63.5, 47)), ps("b1", f(81, 40), after=True),
     mv("n3", [26, 22], delay=1.2), mv("n5", [44, 23], delay=1.2), mv("n4", [65, 24], delay=1.2), mv("n2", [79, 27], delay=1.2)),
   S("Der Flügel bricht durch", "Spieler sieben nimmt den Ball mit nach vorn. Spieler neun kommt ihm entgegen und bekommt den Ball flach in den Fuß.",
     dr("r7", "b1", [83, 33]), mv("r9", [71, 31], delay=0.3), ps("b1", f(71, 31), after=True)),
   S("Steil in die Zone: Punkt für Rot", "Spieler neun spielt direkt in die Tiefe. Spieler sieben läuft hinter Spieler zwei durch und ist mit dem Ball in der Zone, und das gibt einen Punkt für Team Rot. Danach spielt der Trainer den nächsten Ball ins Quadrat, und es geht wieder zwei gegen zwei los.",
     mv("r7", [84, 22]), mv("r7", [80, 12], after=True), ps("b1", f(80, 12), delay=0.5))],
  "dims": DIMS},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Das Paar bleibt eng zusammen.", "Das Paar bleibt eng",
    "Die zwei im Zentrum arbeiten als Paar. Läuft einer an, rückt der andere mit und macht die Lücke zu. Stehen sie weit auseinander, spielt Team Rot einfach durch die Mitte, und die Kette steht allein. Ist der Ball erobert, geht es zu zweit in die schmale Zone.",
    sp(), [B("b1", *f(36.5, 47)), B("b0", 8.1, 50.6)] + ERSATZ,
    [S("Einer läuft an, der andere rückt mit", "Spieler vierzehn hat den Ball. Spieler acht läuft ihn an, und Spieler sechs rückt eng neben ihn. Spieler neun lässt sich fallen und will den Ball durch die Mitte.",
       mv("n8", [37, 41.5]), mv("n6", [47, 36], delay=0.2), mv("r9", [56, 31], delay=0.2)),
     S("Pass durch die Mitte abgefangen", "Spieler vierzehn versucht es trotzdem durch die Mitte. Weil die zwei eng stehen, ist Spieler sechs dran und hat den Ball.",
       ps("b1", f(47, 36))),
     S("Zu zweit in die Zone: Punkt", "Spieler sechs legt ab auf Spieler acht und startet. Spieler acht spielt ihm den Ball in den Lauf. Spieler sechs nimmt ihn in der schmalen Zone an, und das gibt einen Punkt für Team Neon.",
       ps("b1", f(37, 41.5)), mv("n6", [57, 50.5], delay=0.3), ps("b1", f(57, 50.5), after=True))], dims=DIMS),
  V("Coaching-Punkt", "Der zweite Coaching-Punkt: Die Kette rückt gemeinsam raus.", "Gemeinsam raus, Abseits",
    "Die Viererkette bleibt eine Linie. Kommt Druck auf den Ball, rücken alle vier gleichzeitig ein paar Meter raus. Einer schaut, wo die Spitzen stehen, und ruft. Wer dann hinter der Kette stehen bleibt, ist im Abseits.",
    sp(), [B("b1", *f(63.5, 47)), B("b0", 8.1, 50.6)] + ERSATZ,
    [S("Druck auf den Ball", "Spieler zehn hat den Ball. Spieler sechs läuft ihn an und setzt ihn unter Druck. Hinten achtet Spieler vier darauf, wo Spieler neun steht.",
       mv("n6", [60, 41.5])),
     S("Alle vier rücken raus", "Spieler vier ruft, und alle vier rücken gleichzeitig raus, in einer Linie. Spieler zwölf geht mit zurück. Spieler neun bleibt stehen und steht jetzt hinter der Kette.",
       mv("n3", [19, 28]), mv("n5", [37.5, 28]), mv("n4", [62.5, 28]), mv("n2", [81, 28]), mv("r12", [28, 33], delay=0.3)),
     S("Steilpass, Abseits: Punkt", "Spieler zehn spielt steil, Spieler neun startet in die Zone. Er stand aber schon hinter der Kette, als der Pass kam. Abseits, und das gibt einen Punkt für Team Neon.",
       mv("r9", [74, 12], delay=0.2), ps("b1", f(74, 12)))], dims=DIMS)]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
