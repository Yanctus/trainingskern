import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 64-P1 (U12-U14, Woche 15 Phase 2): 1st Touch and Passing. Kein PDF und kein text.txt vorhanden: gebaut aus Ton, Übersicht und
# Szenenbildern. 10 x 10 Yards = Feld x 25-75, y 5-55 (9 x 9 m). Drei Spieler an drei Hütchen wie im Video (oben links, Ecke unten
# links = Spieler in der Mitte des Ablaufs, unten rechts). Im Video ohne Nummern: Neon 4 oben, Neon 6 in der Ecke, Neon 8 rechts.
# Ein Trainer rechts mit Bällen (im Video kein Trainer). Sichtkegel aus Ton und Video ("Scan before receiving so you know your next
# action"): Neon 6 schaut vor der Annahme zu dem Spieler, den er als Nächstes anspielt.
T = P("T", "c", 83, 17, "T")
POS = {"n4": (32.5, 11), "n6": (32.5, 47.5), "n8": (70, 47.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 86.6, 20.5), B("s2", 83, 20.5)]
LINES = [rect(25, 5, 50, 50)]
KEGEL = [C(38, 12.5), C(38, 42.5), C(66, 42.5)]
AN4, AN6, AN8 = [33.1, 11.6], [33.1, 48.1], [70.6, 48.1]

u = {"title": "Annehmen mit dem hinteren Fuß", "code": "UE-175", "kind": "Übungsform",
 "focuses": ["Ballannahme", "Passspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 3, "players_max": 12, "field_size": "9 x 9 m",
 "description": "Drei Spieler stehen an drei Hütchen in einem kleinen Feld. Der Spieler in der Ecke bekommt jeden Ball, nimmt ihn mit dem hinteren Fuß an und spielt zum nächsten Spieler weiter. Danach läuft der Ball in die andere Richtung zurück. Vor jeder Annahme schaut er kurz, wohin der nächste Pass geht.",
 "organisation": ["Aufbauen: Ein Feld von 9 mal 9 Metern mit drei Hütchen: oben links, unten links in der Ecke und unten rechts.",
  "Verteilen: Drei Spieler pro Feld. Neon vier steht oben mit Ball, Neon sechs in der Ecke, Neon acht rechts. Bei mehr Kindern mehrere Felder. Der Trainer steht an der Seite mit Bällen.",
  "Ablauf: Neon vier passt zu Neon sechs, der mit dem hinteren Fuß annimmt und zu Neon acht spielt. Neon acht spielt zurück, und Neon sechs spielt wieder hoch zu Neon vier.",
  "Wechsel: Nach einer Minute geht ein anderer Spieler in die Ecke, bis jeder einmal dran war."],
 "organisation_show": ORG,
 "coaching_points": ["Feste und genaue Pässe spielen", "Mit dem hinteren Fuß annehmen, um schnell nach vorn zu spielen", "Vor der Annahme schauen, wohin der nächste Pass geht", "Auf den Zehenspitzen stehen, bereit für den Ball"],
 "materials": ["3 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Annehmen mit dem hinteren Fuß. Drei Spieler, ein kleines Feld, und der Spieler in der Ecke übt die erste Ballberührung und den schnellen Pass.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", *AN4)] + ERSATZ,
  "steps": [
   S("Schauen, dann Pass", "Neon sechs schaut kurz nach rechts zu Neon acht. Dann passt Neon vier fest zu Neon sechs.",
     bl("n6", [52, 47.5]), ps("b1", AN6, after=True)),
   S("Hinterer Fuß, weiter", "Neon sechs nimmt den Ball mit dem hinteren Fuß an, also mit dem Fuß, der weiter weg ist. So steht er offen und spielt gleich weiter zu Neon acht.",
     ps("b1", AN8)),
   S("Zurück in die Ecke", "Jetzt läuft der Ball in die andere Richtung. Neon sechs schaut kurz nach oben zu Neon vier, und Neon acht spielt zurück.",
     bl("n6", [32.5, 28]), ps("b1", AN6, after=True)),
   S("Hoch zu Neon vier", "Neon sechs nimmt wieder mit dem hinteren Fuß an und spielt hoch zu Neon vier. Dann geht alles von vorn los, und nach einer Minute ist ein anderer Spieler in der Ecke dran.",
     ps("b1", AN4))],
  "dims": dims(25, 75, 5, 55, "9 m", "9 m", rx=92)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Mit dem hinteren Fuß annehmen.", "Hinterer Fuß",
    "Wer den Ball mit dem vorderen Fuß stoppt, steht mit dem Rücken zum nächsten Mitspieler. Wer den Ball über den Körper rollen lässt und mit dem hinteren Fuß annimmt, ist schon offen und kann sofort nach vorn spielen.",
    sp(), [B("b1", *AN4)] + ERSATZ,
    [S("Offen stehen", "Neon sechs steht offen und schaut zu Neon acht. Neon vier passt, und der Ball rollt vor dem Körper vorbei.",
       bl("n6", [52, 47.5]), ps("b1", AN6, after=True)),
     S("Annahme und Pass", "Neon sechs nimmt ihn mit dem hinteren Fuß nach vorn mit und spielt sofort zu Neon acht.",
       dr("n6", "b1", [36, 49]), ps("b1", AN8, after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Doppelpass und Annahme am Hütchen vorbei.", "Am Hütchen vorbei",
    "Jetzt kommt ein Doppelpass dazu. Danach nimmt der Spieler in der Ecke den Ball mit dem ersten Kontakt am Hütchen vorbei mit und spielt ihn zurück. So gibt es mehr Ballkontakte, und das Tempo steigt.",
    sp(), [B("b1", *AN4)] + ERSATZ,
    [S("Doppelpass", "Neon vier passt zu Neon sechs, und Neon sechs spielt direkt zurück.",
       ps("b1", AN6), ps("b1", AN4, after=True)),
     S("Am Hütchen vorbei", "Neon vier passt noch einmal. Neon sechs nimmt den Ball mit dem ersten Kontakt am Hütchen vorbei mit und spielt ihn zurück zu Neon vier.",
       ps("b1", AN6), dr("n6", "b1", [42.5, 47.5], after=True), ps("b1", AN4, after=True)),
     S("Andere Seite", "Neon sechs geht zurück in die Ecke. Jetzt kommt der Ball zu Neon acht, und auf dieser Seite geht es genauso. Nach einer Minute ist ein anderer Spieler in der Ecke dran.",
       mv("n6", [32.5, 47.5]), ps("b1", AN6, after=True), ps("b1", AN8, after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
