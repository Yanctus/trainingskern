import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 35-P9 (U15-U17, Woche 16 Phase 5): Stopping Penetration as a Compact Midfield 4 (Video: The Compact Midfield Four).
# 30 x 35 Yards = 27 x 32 m, gerundet 25 x 30 m. Verhältnis 1,2: kein langes Feld, bleibt hochkant wie im PDF
# (Feld x 26-74, y 5-52, Team Rot greift nach oben an). Fünf Zonen quer wie im PDF: 5, 5, 15, 5, 5 Yards
# (Linien bei y 11,7 / 18,4 / 38,6 / 45,3). Minitore oben und unten (im Original „ST“, ein Tor als Stürmer markiert).
# Pink/Video bordeaux (Mittelfeld 26, 8, 24, 15 und der Verteidiger 6) -> Team Neon, Nummern wie im Video.
# Blau -> Team Rot, neu nummeriert, weil 6 und 26 doppelt wären: tief 6 -> 2, Aufbau 16 -> 3, 25 -> 4, Zehner 17 -> 10,
# vorn 47 -> 9, 26 -> 11. Ein Trainer statt zwei, an der unteren linken Ecke (speist in Steigerung zwei den Ball ein).
# Grundform: Ablauf nach PDF/Video-Einblendungen („3 midfielders build“, „2 midfielders can press in zone“, „be organised
# with press and cover“, Ballgewinn -> Angriff aufs andere Minitor). Steigerung 1 = PDF Key Coaching Point 1 (ein Angreifer darf in
# die Mittelzone fallen), Steigerung 2 = Key Coaching Point 2 (Trainer spielt sofort ein, schnelle Rückkehr; laut Video nur ein
# Verteidiger in der tiefen Zone, zwei Angreifer von Team Neon). Als „Steigerung“ gefasst, weil beide die Regeln ändern.
# Kein Ton im Video (nur Musik, ton.txt leer): Ablauf aus PDF und den Einblendungen im Video.
# Sichtkegel: PDF „Ability to check shoulders to cover passing lines“ -> Grundform: Spieler acht schaut über die Schulter zu
# Spieler zehn, bevor er den Pass abfängt. Steigerung 1: Spieler zehn nimmt an und dreht auf (Kegel mit von + Drehpfeil).
# Kein Dubletten-Fall: UE-203, UE-205 (35-P4, sieben gegen vier ohne Tore), UE-307 und UE-320 geprüft, andere Organisation.
FX0, FX1, FY0, FY1 = 26, 74, 5, 52
ZL = [11.7, 18.4, 38.6, 45.3]
T = P("T", "c", 19.5, 52, "T")  # untere linke Ecke
ERSATZ = [B("s1", 22.6, 52.6), B("s2", 15.9, 52.6)]
POS = {"n6": (42, 8.5), "n26": (38, 32), "n8": (46.5, 30), "n24": (55, 30), "n15": (63.5, 32),
       "r9": (32, 8.5), "r11": (66, 8.5), "r10": (53, 14), "r3": (29, 42), "r4": (72, 42), "r2": (50, 48.5)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
def fuss(x, y): return [round(x + 0.6, 1), round(y + 0.6, 1)]
LINES = [rect(FX0, FY0, FX1 - FX0, FY1 - FY0)] + [line(FX0, y, FX1, y) for y in ZL]
TORE = [{"x": 50, "y": FY0, "side": "top"}, {"x": 50, "y": FY1, "side": "bottom"}]
DIMS = dims(FX0, FX1, FY0, FY1, "25 m", "30 m")

u = {"title": "Vier machen das Zentrum dicht", "code": "UE-333", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 11, "players_max": 11,
 "field_size": "25 x 30 m",
 "description": "Vier Mittelfeldspieler von Team Neon verteidigen die große Zone in der Mitte, hinter ihnen ordnet ein Verteidiger das Spiel. Drei Aufbauspieler von Team Rot wollen durch diesen Block auf ihren Zehner spielen, der vorn mit zwei Angreifern drei gegen eins aufs Minitor spielt. Erobert Team Neon den Ball, greift es sofort das Minitor auf der anderen Seite an. Zwei aus dem Mittelfeld dürfen nach vorn pressen, die anderen bleiben eng und stellen die Passwege zu.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 30 Metern mit einem Minitor an jeder Grundlinie. Es ist quer in fünf Zonen geteilt: in der Mitte die große Mittelzone, davor und dahinter je zwei schmale Zonen von knapp fünf Metern.",
  "Verteilen: Team Neon hat vier Spieler in der Mittelzone und einen Verteidiger in der Zone vor dem oberen Minitor. Team Rot baut mit drei Spielern in den beiden unteren Zonen auf, Spieler zehn steht direkt vor der Mittelzone, zwei Angreifer warten ganz vorn. Der Trainer steht mit Bällen an der Ecke.",
  "Ablauf: Team Rot spielt durch den Block oder um ihn herum zu Spieler zehn, dann geht es drei gegen eins aufs obere Minitor. Zwei Spieler von Team Neon dürfen in die Aufbauzone pressen, die anderen bleiben in der Mittelzone. Nach einem Ballgewinn greift Team Neon sofort das untere Minitor an.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt für das Team, das trifft. Danach spielt der Trainer den nächsten Ball zu Team Rot. Nach drei bis vier Minuten tauschen die Teams die Aufgaben."],
 "organisation_show": ORG,
 "coaching_points": ["Eng zusammen, keine Lücke zwischen euch", "Einer presst, der Nebenmann sichert", "Zusammen anlaufen, nicht einer allein", "Schulterblick: Wo steht der Zehner?"],
 "materials": ["2 Minitore", "Hütchen für Feld und Zonen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Vier machen das Zentrum dicht. Vier Mittelfeldspieler von Team Neon verteidigen zusammen die große Zone in der Mitte. Team Rot will mit drei Spielern durch diesen Block spielen, und vorn warten drei Angreifer gegen einen Verteidiger.",
 "board": {"lines": LINES, "goals": TORE, "cones": [], "players": sp(), "balls": [B("b1", 50.6, 49.1)] + ERSATZ,
  "steps": [
   S("Rot baut auf, der Block schiebt mit", "Spieler zwei spielt raus zu Spieler vier. Sofort schiebt das ganze Mittelfeld zur Ballseite. Spieler fünfzehn darf aus der Zone raus und läuft Spieler vier an.",
     ps("b1", fuss(72, 42)), mv("n15", [69.5, 38.5], delay=0.4), mv("n24", [59, 30.5], delay=0.4),
     mv("n8", [51, 29.5], delay=0.5), mv("n26", [43, 31], delay=0.5)),
   S("Zurück und auf die andere Seite", "Vorn ist zu. Also geht der Ball zurück zu Spieler zwei, und der verlagert gleich auf Spieler drei. Jetzt muss der Block rüber. Spieler sechsundzwanzig läuft von außen an, Spieler acht sichert hinter ihm.",
     ps("b1", fuss(50, 48.5)), ps("b1", fuss(29, 42), after=True), mv("n26", [27.5, 38.5], delay=0.2),
     mv("n8", [37, 33], delay=0.3), mv("n24", [47.5, 30], delay=0.3), mv("n15", [57, 31], delay=0.3)),
   S("Schulterblick, Ball abgefangen", "Spieler drei will flach durch die Mitte auf Spieler zehn. Spieler acht hat vorher über die Schulter geschaut und weiß, wo der Zehner steht. Ein Schritt in den Passweg, und der Ball gehört Team Neon.",
     bl("n8", [53, 14]), ps("b1", fuss(37.5, 31.5), after=True), mv("n8", [37.5, 31.5], delay=0.2)),
   S("Umschalten, steil in die Tiefe", "Jetzt schnell nach vorn. Spieler vierundzwanzig startet sofort in die Tiefe, und Spieler acht spielt ihm den Ball in den Lauf. Spieler zwei kommt ihm entgegen.",
     mv("n24", [55, 43]), ps("b1", fuss(55, 43), delay=0.5), mv("r2", [55, 47.3], delay=0.6)),
   S("Vorbei und rein: Punkt", "Spieler vierundzwanzig zieht an Spieler zwei vorbei und schiebt ins Minitor, und das gibt einen Punkt für Team Neon. Danach spielt der Trainer den nächsten Ball zu Spieler zwei, und Team Rot baut wieder auf.",
     dr("n24", "b1", [47.5, 46.5]), ps("b1", [49.5, 52.3], after=True))],
  "dims": DIMS},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Angreifer darf sich in die Mittelzone fallen lassen.", "Der Zehner lässt sich fallen",
    "Spieler zehn darf jetzt in die Mittelzone kommen und sich dort anbieten. Team Rot hat so einen Mitspieler zwischen den Linien. Das Mittelfeld muss über die Schulter schauen, sonst sieht es ihn nicht kommen. Wer ihm am nächsten ist, rückt raus, die anderen schieben nach.",
    sp(n26=(39, 32.5), n8=(47.5, 30), n24=(56, 30), n15=(64.5, 30), r4=(73, 42)), [B("b1", 29.6, 42.6)] + ERSATZ,
    [S("Spieler zehn lässt sich fallen", "Der Block steht noch auf der Seite, wo der Ball eben war. Spieler zehn lässt sich in die Mittelzone fallen und bietet sich an.",
       mv("r10", [40, 22])),
     S("Pass in den Fuß", "Spieler zehn schaut zum Ball. Spieler drei spielt flach an Spieler sechsundzwanzig vorbei in den Fuß. Spieler sechsundzwanzig hat nicht über die Schulter geschaut und kommt zu spät.",
       bl("r10", [29, 42]), ps("b1", fuss(40, 22), after=True), mv("n26", [41, 27.5], delay=0.6)),
     S("Aufdrehen und steil nach vorn", "Spieler zehn nimmt an und dreht auf. Vorn läuft Spieler elf in die Lücke neben Spieler sechs, und genau da kommt der Pass hin.",
       bl("r10", [62, 10], von=[29, 42], dauer=1.3), drehen("r10", [62, 10], delay=0.4), mv("r11", [62, 10], delay=0.3),
       ps("b1", fuss(62, 10), after=True)),
     S("Drei gegen eins: Punkt", "Jetzt ist es drei gegen eins. Spieler sechs muss raus zu Spieler elf, und der legt quer auf Spieler neun. Der schiebt ins Minitor, und das gibt einen Punkt für Team Rot.",
       mv("n6", [57, 9.5]), mv("r9", [38, 9], delay=0.2), ps("b1", fuss(38, 9), delay=0.5), ps("b1", [48.5, 5.3], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Nach jedem Angriff spielt der Trainer sofort den nächsten Ball ein.", "Trainer spielt sofort ein",
    "Nach einem Ballgewinn greifen zwei von Team Neon das Minitor an, hinten darf nur ein Spieler von Team Rot verteidigen. Ist der Angriff vorbei, spielt der Trainer sofort den nächsten Ball zu Team Rot. Die zwei Angreifer sprinten zurück in die Mittelzone, und der Block ordnet sich, bevor Team Rot durchspielen kann.",
    sp(), [B("b1", 47.1, 30.6)] + ERSATZ,
    [S("Ball erobert, zwei gehen mit", "Spieler acht hat den Ball gerade erobert. Jetzt dürfen zwei nach vorn. Spieler fünfzehn startet in die tiefe Zone und bekommt den Ball, Spieler vierundzwanzig läuft mit. Hinten verteidigt nur Spieler zwei.",
       mv("n15", [61, 45.5]), mv("n24", [46, 46], delay=0.2), ps("b1", fuss(61, 45.5), delay=0.6), mv("r2", [58, 49.5], delay=0.8)),
     S("Quer und rein: Punkt", "Spieler zwei geht auf den Ball. Spieler fünfzehn legt quer, und Spieler vierundzwanzig schiebt ins Minitor. Das gibt einen Punkt für Team Neon.",
       ps("b1", fuss(46, 46)), ps("b1", [49.5, 52.3], after=True)),
     S("Trainer spielt ein, alle zurück", "Der Ball ist kaum drin, da spielt der Trainer schon den nächsten zu Spieler drei. Spieler fünfzehn und Spieler vierundzwanzig sprinten sofort zurück in die Mittelzone. Bevor Team Rot nach vorn spielen kann, steht der Block wieder eng.",
       ps("s1", fuss(29, 42)), mv("n24", [52, 31], delay=0.2), mv("n15", [61, 31.5], delay=0.2),
       mv("n26", [34.5, 33.5], delay=0.4), mv("n8", [43.5, 30.5], delay=0.4))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
