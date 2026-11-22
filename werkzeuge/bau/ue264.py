import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# GK-12 (GK-P12, U12-U14, Torwarttraining): Goalkeeper Quick Thinking Reactions Handling. 15 x 10 Yards = Feld x 25-75, y 8-52
# (14 x 9 m), Ausrichtung wie im PDF (Trainer unten, kein Tor). Grüner Torwart 1 -> Torwart k1 in der Mitte, wartender Torwart
# (orange 1 im PDF, oben links) -> zweiter Torwart k2 neben dem Feld. Die vier Hütchen im Quadrat haben im Original vier Farben
# (rot, blau, weiß, gelb); die Tafel kennt nur orange und neon. Daher je zwei Hütchen pro Farbe über Kreuz, und der Trainer ruft
# Farbe und Reihe ("Neon hinten" = blaues Hütchen oben rechts, "Orange vorn" = gelbes Hütchen unten rechts; vorn = beim Trainer).
# Der Ton des Videos passt nicht zum Bild (spricht von Schüssen und Paraden); Ablauf daher aus PDF-Text und Video-Grafik.
# Sichtkegel: PDF "set for a volley", Ton "assess strikers body shape" -> der Torwart schaut nach dem Zurücklaufen zum Trainer,
# bevor der Volley kommt. Im Video kein Kegel eingezeichnet, Richtung aus dem Sinn.
# Fassungen: Coaching-Punkt Abpraller sichern (PDF Seite 2 links), Steigerung Farbkombinationen (PDF Seite 2 rechts, Video ab 1:00).
T = P("T", "c", 50, 46, "T")
POS = {"k1": (50, 24), "k2": (30, 14)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "t", x, y, "TW") for i, (x, y) in d.items()] + [T]
ERSATZ = [B("s1", 54, 48.5), B("s2", 46, 48.5)]
LINES = [rect(25, 8, 50, 44)]
KEGEL = [C(40, 16), C(60, 16, "neon"), C(40, 32, "neon"), C(60, 32)]

u = {"title": "Farbe rufen, Volley fangen", "code": "UE-264", "kind": "Übungsform",
 "focuses": ["Schnelligkeit", "Koordination", "Ballannahme"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "tags": ["Torwart"], "duration_minutes": 15, "players_min": 2, "players_max": 2, "field_size": "14 x 9 m",
 "description": "Der Torwart steht in der Mitte von vier Hütchen. Der Trainer ruft eine Farbe und eine Reihe, der Torwart läuft mit schnellen Seitschritten hin, tippt das Hütchen an und ist sofort zurück in der Mitte. Dort fängt er einen Volley vom Trainer und wirft den Ball zurück. Nach ein bis zwei Minuten tauschen die Torhüter.",
 "organisation": ["Aufbauen: Ein Feld von 14 mal 9 Metern. In der Mitte stehen vier Hütchen im Quadrat, je zwei orange und zwei neon über Kreuz.",
  "Verteilen: Ein Torwart steht in der Mitte des Quadrats, der zweite Torwart wartet neben dem Feld. Der Trainer steht unten mit Bällen.",
  "Ablauf: Der Trainer ruft zum Beispiel „Neon hinten“. Der Torwart läuft hin, tippt das Hütchen an und läuft zurück in die Mitte. Der Trainer spielt einen Volley, der Torwart fängt und wirft zurück. Dann kommt die nächste Farbe.",
  "Wechsel: Nach ein bis zwei Minuten tauschen die Torhüter. Wer wartet, erholt sich und schaut zu."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell zuhören, denken und loslaufen", "Kurze, schnelle Schritte zum Hütchen und zurück", "Vor dem Volley stehen und zum Trainer schauen", "Den Ball sicher fangen und genau zurückwerfen"],
 "materials": ["2 orange Hütchen", "2 neon Hütchen", "Mehrere Bälle beim Trainer"],
 "access": "abo", "hidden": True,
 "say_intro": "Farbe rufen, Volley fangen. Der Torwart hört genau hin, tippt das gerufene Hütchen an und fängt danach den Volley.",
 "board": {"lines": LINES, "cones": KEGEL, "players": sp(), "balls": [B("b1", 50.6, 46.6)] + ERSATZ,
  "steps": [
   S("Neon hinten", "Der Trainer ruft: Neon hinten. Der Torwart läuft mit schnellen Seitschritten zum neon Hütchen oben rechts und tippt es an.",
     mv("k1", [57.5, 18])),
   S("Zurück in die Mitte", "Sofort läuft er zurück in die Mitte. Dort steht er bereit und schaut zum Trainer.",
     mv("k1", [50, 24]), bl("k1", [50, 44], after=True)),
   S("Volley fangen", "Der Trainer spielt einen Volley aus der Hand. Der Torwart fängt den Ball sicher und wirft ihn genau zurück.",
     ps("b1", [50.6, 24.6]), ps("b1", [50.6, 46.6], after=True)),
   S("Nächste Farbe, dann Wechsel", "Der Trainer ruft: Orange vorn. Der Torwart tippt das orange Hütchen unten rechts an, läuft zurück und fängt den nächsten Volley. So geht es ein bis zwei Minuten weiter. Dann tauschen die Torhüter, und der zweite Torwart kommt in die Mitte.",
     mv("k1", [57.5, 30]), mv("k1", [50, 24], after=True), ps("b1", [50.6, 24.6], after=True), ps("b1", [50.6, 46.6], after=True))],
  "dims": dims(25, 75, 8, 52, "14 m", "9 m")},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Fällt der Ball herunter, sofort hinterher.", "Abpraller sofort sichern",
    "Der Torwart bleibt die ganze Zeit hellwach. Rutscht ihm der Ball aus den Händen, reagiert er blitzschnell, wirft sich auf den Ball und sichert ihn. Erst dann geht es weiter mit der nächsten Farbe.",
    sp(), [B("b1", 50.6, 46.6)] + ERSATZ,
    [S("Ball springt weg", "Der Trainer spielt einen festen Volley. Der Ball springt dem Torwart aus den Händen und rollt zur Seite.",
       ps("b1", [50.6, 24.6]), ps("b1", [45.6, 27.6], after=True)),
     S("Hinterher und sichern", "Der Torwart reagiert sofort, wirft sich auf den Ball und hält ihn fest. Dann wirft er ihn zurück zum Trainer.",
       mv("k1", [45, 27]), ps("b1", [50.6, 46.6], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Der Trainer ruft zwei Hütchen hintereinander.", "Zwei Farben nacheinander",
    "Jetzt ruft der Trainer zwei oder drei Hütchen, zum Beispiel „Neon hinten, Orange vorn“. Der Torwart merkt sich die Reihenfolge, tippt die Hütchen nacheinander an und ist dann sofort zurück in der Mitte für den Volley.",
    sp(), [B("b1", 50.6, 46.6)] + ERSATZ,
    [S("Neon hinten, Orange vorn", "Der Trainer ruft: Neon hinten, Orange vorn. Der Torwart tippt erst das neon Hütchen oben rechts an und dann das orange Hütchen unten rechts.",
       mv("k1", [57.5, 18]), mv("k1", [57.5, 30], after=True)),
     S("Zurück und fangen", "Dann schnell zurück in die Mitte. Der Torwart schaut zum Trainer, fängt den Volley und wirft ihn zurück.",
       mv("k1", [50, 24]), bl("k1", [50, 44], after=True), ps("b1", [50.6, 24.6], after=True), ps("b1", [50.6, 46.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
