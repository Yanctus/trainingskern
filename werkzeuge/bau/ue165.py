import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# WU-41 (U12-U14, Woche 27 Phase 2): Technical Passing Activation Warm Up. 15 x 25 Yards = Feld x 35-65, y 5-55 (14 x 23 m),
# vier Hütchen an den Ecken. Alle Spieler ein Team (Neon), Nummern wie im PDF. Gespiegelt (oben/unten): Die erste Kombination
# läuft nach oben (im PDF nach unten). Wartende Paare stehen neben den Eckhütchen (3D-Abstand).
# Sichtkegel: Im Ton "players must be constantly scanning"; im Video ist kein Kegel eingezeichnet, Richtung aus dem Sinn
# (Spieler zehn schaut vor der Ablage zu Spieler elf, dem nächsten Passziel).
T = P("T", "c", 80, 24, "T")
POS = {"n10": (38.5, 51), "n8": (61.5, 50), "n4": (38.5, 9), "n11": (61.5, 9),
       "n5": (29, 53), "n6": (71, 53), "n3": (29, 7), "n2": (71, 7)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 83.6, 27.5), B("s2", 80, 27.5)]
LINES = [rect(35, 5, 30, 50)]
KEGEL = ecken(35, 5, 30, 50)

u = {"title": "Passen und Laufen zu zweit", "code": "UE-165", "kind": "Übungsform",
 "focuses": ["Erwärmung", "Passspiel", "Bewegung"], "age_groups": ["F-Jugend", "E-Jugend", "D-Jugend", "C-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 10, "players_min": 8, "players_max": 12, "field_size": "14 x 23 m",
 "description": "Eine Passkombination zum Aufwärmen in einem Viereck mit vier Hütchen. Zwei Partner spielen sich den Ball zu, binden einen Endspieler ein und spielen dann schräg durch zum anderen Endspieler. Danach laufen beide durch, und die Kombination geht in die andere Richtung. Gespielt wird mit ein oder zwei Kontakten und hohem Tempo.",
 "organisation": ["Aufbauen: Ein Viereck von 14 mal 23 Metern mit vier Hütchen an den Ecken.",
  "Verteilen: Die Spieler arbeiten zu zweit. Unten starten Spieler zehn und Spieler acht, oben stehen Spieler vier und Spieler elf als Endspieler. Die nächsten Paare warten neben den Hütchen. Der Trainer steht rechts mit Bällen.",
  "Ablauf: Spieler zehn spielt zu Spieler acht, der spielt zu Spieler vier. Spieler vier legt zurück für Spieler zehn, und der spielt schräg durch zu Spieler elf. Dann laufen beide durch, und es geht in die andere Richtung.",
  "Wechsel: Wer durchgelaufen ist, stellt sich an und wird später Endspieler. Nach ein paar Runden tauschen die Partner die Seiten."],
 "organisation_show": ORG,
 "coaching_points": ["Mit dem richtigen Tempo und genau passen", "Mit einem oder zwei Kontakten spielen", "In den Lauf vor den Mitspieler passen", "Vor der Ballannahme umschauen und laut rufen"],
 "materials": ["4 Hütchen", "Viele Bälle"],
 "access": "abo", "hidden": True,
 "say_intro": "Passen und Laufen zu zweit. Eine schnelle Passkombination mit zwei Endspielern, und danach geht es in die andere Richtung.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 39.1, 51.6)] + ERSATZ,
  "steps": [
   S("Pass zum Partner", "Spieler zehn spielt zu Spieler acht. Spieler acht kommt dabei schräg nach innen und nimmt den Ball im Laufen an.",
     mv("n8", [55, 37]), ps("b1", [55.6, 37.6], delay=0.2)),
   S("Zum Endspieler", "Gleichzeitig läuft Spieler zehn links nach vorn. Spieler acht spielt schräg nach vorn zu Spieler vier.",
     mv("n10", [41.5, 27]), ps("b1", [39.1, 9.6], delay=0.2)),
   S("Umschauen und ablegen", "Spieler zehn schaut über die Schulter, wo Spieler elf steht. Spieler vier legt den Ball zurück in den Lauf von Spieler zehn.",
     bl("n10", [56, 15]), ps("b1", [42.1, 27.6], after=True)),
   S("Durch zu Spieler elf", "Spieler zehn spielt mit dem ersten Kontakt schräg durch zu Spieler elf. Dann laufen Spieler zehn und Spieler acht gleichzeitig bis hinter die oberen Hütchen.",
     ps("b1", [62.1, 9.6]), mv("n10", [44, 2.5], after=True), mv("n8", [56, 2.5], after=True)),
   S("Andere Richtung", "Der Ball ist ohne Fehler bei Spieler elf, die Kombination ist geschafft. Jetzt spielen Spieler elf und Spieler vier dieselbe Kombination nach unten, und Spieler fünf und Spieler sechs sind dort die Endspieler.",
     mv("n5", [38.5, 51]), mv("n6", [61.5, 50]), mv("n4", [45, 22], delay=0.3), ps("b1", [45.6, 22.6], delay=0.5))],
  "dims": dims(35, 65, 5, 55, "14 m", "23 m", rx=86)},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: In den Lauf vor den Mitspieler passen.", "In den Lauf passen",
    "Der Pass kommt nicht in den Fuß, sondern ein Stück vor den Mitspieler. So nimmt er den Ball im Laufen mit und muss nicht abbremsen. Die Kombination bleibt schnell und flüssig.",
    sp(), [B("b1", 39.1, 51.6)] + ERSATZ,
    [S("Vor den Mitspieler", "Spieler acht läuft schräg nach innen. Spieler zehn spielt den Ball genau in den Raum vor ihn.",
       mv("n8", [55, 37]), ps("b1", [55.6, 37.6], delay=0.2)),
     S("Im Laufen weiter", "Spieler acht nimmt den Ball im Laufen mit und spielt ohne abzubremsen weiter zu Spieler vier.",
       ps("b1", [39.1, 9.6]), mv("n10", [41.5, 27], delay=0.2))]),
  V("Steigerung", "Und jetzt die Steigerung: Spieler zehn läuft innen hinterher und bekommt den Ball in der Mitte.", "Innen hinterlaufen",
    "Jetzt spielt Spieler acht nach vorn zu Spieler elf, und Spieler zehn läuft innen in die Mitte. Spieler elf legt in seinen Lauf ab, und Spieler zehn spielt schräg durch zu Spieler vier. Wichtig ist der richtige Moment für den Lauf.",
    sp(), [B("b1", 39.1, 51.6)] + ERSATZ,
    [S("Pass zum Partner", "Spieler zehn spielt zu Spieler acht, der schräg nach innen kommt.",
       mv("n8", [55, 37]), ps("b1", [55.6, 37.6], delay=0.2)),
     S("Innen hinterlaufen", "Spieler acht spielt nach vorn zu Spieler elf. Gleichzeitig läuft Spieler zehn innen in die Mitte und schaut dabei zu Spieler vier.",
       ps("b1", [62.1, 9.6]), mv("n10", [44, 36]), mv("n10", [52, 24], after=True), bl("n10", [40, 11], after=True)),
     S("Durch zu Spieler vier", "Spieler elf legt in den Lauf von Spieler zehn ab, und Spieler zehn spielt mit dem ersten Kontakt schräg durch zu Spieler vier.",
       ps("b1", [52.6, 24.6]), ps("b1", [39.1, 9.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
