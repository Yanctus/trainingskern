import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 94-P4 (U12-U14, Woche 19 Phase 1): Playing Out From the Back (4231). 30 x 30 Yards = Feld x 25-75, y 5-55 (27 x 27 m).
# Gedreht: im PDF spielt die Abwehr (rechts) nach links, hier spielt sie nach oben. Abwehr unten von links: 3, 6, 5, 2;
# Mittelfeld oben von links: 11, 10, 8, 7 (alle Team Neon, keine Gegner). Vier Stangen (Dummies) quer in der Mitte mit
# 5 Yards Lücke. Die kleinen Markierungshütchen neben den Außenspielern als vier Hütchen an den Seiten. Ein Trainer (unten
# links, spielt in die Abwehr) statt zwei. Muster wie im PDF: 6-3, 3-5, 5-6, 6-2, 2-5, 5 durch die Stangen zu 8; das
# Mittelfeld wiederholt und spielt zurück. Steigerung 1 = Progression 1 (zwei Bälle), Steigerung 2 = Progression 2
# (Innenverteidiger dribbelt ins Mittelfeld). Progression 3 (Minitore, Prallpass) weggelassen (nur zwei Fassungen).
# Sichtkegel: Ton "lift their heads, locate the ball on the opposite side", Text "Head up to see where other ball is":
# in Steigerung 1 bl() von Spieler fünf nach vorn zum anderen Ball (Richtung aus dem Sinn, im Video kein Kegel eingezeichnet).
T = P("T", "c", 19, 50, "T")
POS = {"n3": (30, 42), "n6": (41.7, 50), "n5": (58.3, 50), "n2": (70, 42),
       "n11": (30, 18), "n10": (41.7, 10), "n8": (58.3, 10), "n7": (70, 18)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 15.4, 53.5), B("s2", 19, 53.5)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(x, 30, shape="stange") for x in (37.5, 45.8, 54.2, 62.5)] + [C(27.5, 26), C(72.5, 26), C(27.5, 34), C(72.5, 34)]

u = {"title": "Spielaufbau von hinten", "code": "UE-161", "kind": "Übungsform",
 "focuses": ["Passspiel", "Zusammenspiel", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 8, "field_size": "27 x 27 m",
 "description": "Eine Abwehrkette und vier Mittelfeldspieler üben den Spielaufbau ohne Gegner. Die Abwehr wechselt mit schnellen Doppelpässen die Seite und spielt dann durch eine Lücke zwischen den Stangen ins Mittelfeld. Das Mittelfeld macht dasselbe und spielt zurück in die Abwehr. So läuft der Ball ohne Pause mit ein oder zwei Kontakten.",
 "organisation": ["Aufbauen: Ein Feld von 27 mal 27 Metern. Quer durch die Mitte vier Stangen mit Lücken von etwa 4,5 Metern. An den Seiten vier Hütchen als Markierung.",
  "Verteilen: Unten stehen vier Abwehrspieler von Team Neon, oben vier Mittelfeldspieler. Der Trainer steht unten links mit vielen Bällen.",
  "Ablauf: Der Trainer spielt in die Abwehr. Die Abwehr wechselt mit Doppelpässen die Seite, dann spielt ein Innenverteidiger durch die Stangen ins Mittelfeld. Das Mittelfeld wiederholt das Muster und spielt zurück.",
  "Wechsel: Nach sechs bis sieben Pässen oder auf Zuruf geht der Pass durch die Stangen. Geht ein Ball verloren, bringt der Trainer sofort einen neuen Ball."],
 "organisation_show": ORG,
 "coaching_points": ["Genau und mit dem richtigen Tempo passen", "Laut rufen und absprechen, wann die Seite gewechselt wird", "Mit ein oder zwei Kontakten spielen", "Durch die Stangen besonders scharf passen"],
 "materials": ["4 Stangen", "4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Spielaufbau von hinten. Die Abwehr wechselt mit schnellen Pässen die Seite und spielt dann durch die Stangen ins Mittelfeld.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 19.6, 50.6)] + ERSATZ,
  "steps": [
   S("Anspiel", "Der Trainer spielt den Ball zu Spieler sechs. Spieler sechs passt zu Spieler drei, und der spielt direkt weiter zu Spieler fünf.",
     ps("b1", [42.3, 50.6]), ps("b1", [30.6, 42.6], after=True), ps("b1", [58.9, 50.6], after=True)),
   S("Seitenwechsel", "Spieler fünf legt zurück zu Spieler sechs. Spieler sechs spielt auf die andere Seite zu Spieler zwei, und der spielt zurück zu Spieler fünf.",
     ps("b1", [42.3, 50.6]), ps("b1", [70.6, 42.6], after=True), ps("b1", [58.9, 50.6], after=True)),
   S("Durch die Stangen", "Jetzt ruft Spieler acht nach dem Ball. Spieler fünf spielt einen scharfen Pass durch die Lücke zwischen den Stangen zu Spieler acht.",
     ps("b1", [58.9, 10.6])),
   S("Mittelfeld wechselt", "Das Mittelfeld macht dasselbe. Spieler acht spielt zu Spieler sieben, der zurück zu Spieler acht, und Spieler acht wechselt die Seite zu Spieler zehn.",
     ps("b1", [70.6, 18.6]), ps("b1", [58.9, 10.6], after=True), ps("b1", [42.3, 10.6], after=True)),
   S("Zurück: geschafft", "Spieler zehn spielt scharf durch die Stangen zurück zu Spieler sechs. Geschafft, der Ball war in beiden Reihen, und jetzt ist wieder die Abwehr dran.",
     ps("b1", [42.3, 50.6]))],
  "dims": dims(25, 75, 5, 55, "27 m", "27 m", rx=83)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Zwei Bälle gleichzeitig.", "Zwei Bälle",
    "Jetzt laufen zwei Bälle gleichzeitig, einer in der Abwehr und einer im Mittelfeld. Vor dem Pass durch die Stangen hebt der Spieler den Kopf und schaut, wo der andere Ball ist. Erst dann spielt er zum Mitspieler, der gerade frei ist. Am Anfang gibt es Chaos, aber mit lautem Rufen klappt es bald.",
    sp(), [B("b1", 70.6, 42.6), B("b2", 30.6, 18.6)] + ERSATZ,
    [S("Zwei Bälle", "Jetzt laufen zwei Bälle gleichzeitig. Hinten spielt Spieler zwei zu Spieler fünf, und vorne spielt Spieler elf zu Spieler acht.",
       ps("b1", [58.9, 50.6]), ps("b2", [58.9, 10.6])),
     S("Kopf hoch", "Spieler fünf hebt den Kopf und schaut nach vorn, wo der andere Ball ist. Spieler acht hat ihn, also ist Spieler zehn frei.",
       bl("n5", [58.3, 29])),
     S("Gleichzeitig durch", "Spieler fünf spielt durch die Stangen zu Spieler zehn. Gleichzeitig spielt Spieler acht nach hinten zu Spieler zwei. Die Bälle kreuzen sich, darum rufen alle laut.",
       ps("b1", [42.3, 10.6]), ps("b2", [70.6, 42.6]))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Der Innenverteidiger dribbelt ins Mittelfeld.", "Abwehr dribbelt an",
    "Auf ein Zeichen dribbelt ein Innenverteidiger selbst durch eine Lücke zwischen den Stangen ins Mittelfeld. Dort spielt er zu einem Mittelfeldspieler. Ein Mittelfeldspieler läuft dafür nach hinten und füllt die Lücke in der Abwehr.",
    sp(), [B("b1", 58.9, 50.6)] + ERSATZ,
    [S("Andribbeln", "Auf ein Zeichen dribbelt Spieler fünf mit Ball durch die Lücke zwischen den Stangen ins Mittelfeld.",
       dr("n5", "b1", [58.3, 22])),
     S("Ins Mittelfeld", "Spieler fünf spielt zu Spieler sieben. Gleichzeitig läuft Spieler acht nach hinten und füllt den Platz in der Abwehr.",
       ps("b1", [70.6, 18.6]), mv("n8", [66, 30]), mv("n8", [58.3, 48], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
