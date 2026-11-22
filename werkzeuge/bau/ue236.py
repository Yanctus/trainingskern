import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 25-P8 (U12-U14, Woche 38 Phase 4): High Press Wave Game. 20 x 25 Yards = Feld x 30-70, y 5-55 (18 x 23 m), Mittellinie
# gestrichelt, oben und unten ein Jugendtor mit neutralem Torwart (Grün 1 und 13 -> k1, k2). Navy (presst) -> Neon 9, 11, 7;
# Pink (mit Ball, greift nach oben an) -> Rot 10, 6, 8 (Pink 9 -> 6 und Pink 11 -> 8 neu nummeriert, weil 9 und 11 bei Neon).
# Wartende Gruppen (Navy 4, 5, 8 und Pink 6, 4, 8) nur im Text. Ein Trainer statt zwei. Grundform wie im Video ab 0:18:
# Mitte presst den Ballführenden, Pass nach rechts, Spieler sieben fängt ab, Konter aufs untere Tor.
# Fassungen: Progression 1 (Außenzonen, je 5 Yards, gestrichelt) und Progression 2 (Ballgewinn in sechs Sekunden).
# Progression 3 bis 5 (nur Vorwärtspässe, zwei pressen + einer sichert, drei gegen zwei) nicht übernommen.
# Sichtkegel aus dem Text ("awareness of space during defensive play", Progression 1): Spieler sieben schaut vor dem Pass
# zum Gegner in der Außenzone. Im Video kein Kegel eingezeichnet.
T = P("T", "c", 21, 40, "T")
POS = {"n9": (37, 18), "n11": (52, 24), "n7": (63, 18), "r10": (31, 46), "r6": (41, 38), "r8": (62, 43)}
TW = [P("k1", "t", 50, 7, "TW"), P("k2", "t", 50, 53, "TW")]
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + TW + [T]
ERSATZ = [B("s1", 22.6, 43.5), B("s2", 19, 43.5)]
LINES = [rect(30, 5, 40, 50), line(30, 30, 70, 30)]
TORE = [{"x": 50, "y": 5, "side": "top", "size": "jugend"}, {"x": 50, "y": 55, "side": "bottom", "size": "jugend"}]
CONES = ecken(30, 5, 40, 50)

u = {"title": "Pressingwelle drei gegen drei", "code": "UE-236", "kind": "Spielform",
 "focuses": ["Verteidigen", "Umschalten", "Zusammenspiel"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"],
 "altersbereiche": ["U12-U14"], "duration_minutes": 15, "players_min": 8, "players_max": 14, "field_size": "18 x 23 m",
 "description": "Ein Wellenspiel drei gegen drei mit einem Torwart in jedem Tor. Team Rot greift mit Ball nach oben an, drei Spieler von Team Neon pressen sofort hoch in der Hälfte von Team Rot. Erobert Team Neon den Ball, kontert es sofort aufs untere Tor. Nach jeder Runde wechselt das pressende Team, und die nächste Gruppe kommt ins Feld.",
 "organisation": ["Aufbauen: Ein Feld von 18 mal 23 Metern mit Mittellinie. Oben und unten ein Jugendtor mit Torwart.",
  "Verteilen: Vier Gruppen zu dritt, zwei von Team Neon und zwei von Team Rot. Drei von Team Rot stehen mit Ball in der unteren Hälfte, drei von Team Neon in der oberen. Die anderen Gruppen warten hinter den Toren. Der Trainer steht links mit Bällen.",
  "Ablauf: Team Rot will nach oben durchspielen und aufs obere Tor schießen. Team Neon presst gemeinsam in die Hälfte von Team Rot, erobert den Ball und kontert aufs untere Tor.",
  "Wertung und Wechsel: Jeder Treffer gibt einen Punkt. Nach jeder Runde geht das pressende Team raus, das angreifende Team presst jetzt, und die nächste Gruppe greift mit Ball an."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell und als Einheit pressen, alle laufen zusammen los", "Mit dem Körper die Richtung vorgeben, damit ein Mitspieler abfangen kann", "Eng zusammenbleiben, damit niemand durch die Mitte kommt", "Nach Ballgewinn sofort kontern, nach der Runde schnell wechseln"],
 "materials": ["2 Jugendtore", "4 Hütchen", "Viele Bälle", "Leibchen in drei Farben"],
 "access": "abo", "hidden": True,
 "say_intro": "Pressingwelle drei gegen drei. Team Rot greift mit Ball an, und Team Neon presst sofort hoch, um den Ball zu erobern.",
 "board": {"lines": LINES, "goals": TORE, "cones": CONES, "players": sp(), "balls": [B("b1", 41.6, 38.6)] + ERSATZ,
  "steps": [
   S("Alle pressen", "Spieler sechs hat den Ball. Sofort laufen Spieler neun, Spieler elf und Spieler sieben gleichzeitig in die Hälfte von Team Rot. Spieler elf läuft direkt auf Spieler sechs zu.",
     mv("n11", [46, 31]), mv("n9", [36, 35]), mv("n7", [59, 32])),
   S("Richtung vorgeben", "Spieler elf läuft im Bogen an und macht den Pass nach links zu. Spieler sechs muss nach rechts spielen, zu Spieler acht.",
     mv("n11", [42, 31]), mv("n11", [37.5, 34], after=True)),
   S("Abgefangen", "Spieler sechs spielt nach rechts, aber Spieler sieben hat den Pass geahnt. Er läuft in den Passweg und fängt den Ball ab, bevor er bei Spieler acht ankommt.",
     mv("n7", [55, 41.2]), ps("b1", [55.6, 41.8], delay=0.3)),
   S("Konter: Punkt", "Spieler sieben kontert sofort und schießt ins untere Tor. Das gibt einen Punkt für Team Neon. Dann gehen Spieler sieben, neun und elf raus, Team Rot presst jetzt, und die nächste Gruppe von Team Neon greift mit Ball von oben an.",
     dr("n7", "b1", [57, 47]), ps("b1", [54, 54.7], after=True))],
  "dims": dims(30, 70, 5, 55, "18 m", "23 m", rx=80)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Die Außenzonen.", "Außenzonen",
    "Links und rechts gibt es eine Außenzone. Erobert Team Neon den Ball in einer Außenzone, gibt das sofort einen Punkt. Darum spielt Team Rot lieber durch die Mitte, und Team Neon muss dort schnell eng zusammenrücken.",
    sp(), [B("b1", 41.6, 38.6)] + ERSATZ,
    [S("Spieler sieben schaut", "Alle drei pressen gleichzeitig, Spieler elf läuft auf Spieler sechs zu. Spieler sieben schaut, wo Spieler acht steht: in der rechten Außenzone.",
       mv("n11", [46, 31]), mv("n9", [36, 35]), mv("n7", [58, 30]), bl("n7", [62, 43], after=True)),
     S("Pass nach außen", "Spieler sechs spielt nach außen zu Spieler acht. Spieler sieben sprintet sofort hinterher.",
       ps("b1", [62.6, 43.6]), mv("n7", [63, 37], delay=0.2)),
     S("Außen erobert: Punkt", "Spieler sieben erobert den Ball in der Außenzone. Das gibt sofort einen Punkt für Team Neon. Darum spielt Team Rot lieber durch die Mitte.",
       mv("n7", [64.5, 41.5]), dr("n7", "b1", [57, 40], after=True))],
    lines=LINES + [line(40, 5, 40, 55), line(60, 5, 60, 55)]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Sechs Sekunden.", "Sechs Sekunden",
    "Team Neon hat nur sechs Sekunden. Erobert es den Ball in dieser Zeit, gibt das einen Punkt, und ein Treffer danach gibt noch einen Punkt. Hält Team Rot den Ball sechs Sekunden lang, gibt das einen Punkt für Team Rot.",
    sp(), [B("b1", 41.6, 38.6)] + ERSATZ,
    [S("Mit Tempo anlaufen", "Alle drei von Team Neon sprinten gleichzeitig los. Spieler elf geht ganz nah an Spieler sechs heran, Spieler neun und Spieler sieben machen die Passwege zu.",
       mv("n11", [43, 32.5]), mv("n9", [35, 38.5]), mv("n7", [57, 38])),
     S("Erobert: Punkt", "Nach vier Sekunden erobert Spieler elf den Ball. Das gibt einen Punkt für Team Neon, und jetzt geht es noch auf das Tor.",
       dr("n11", "b1", [46, 41])),
     S("Konter: Punkt", "Spieler neun startet nach vorn, Spieler elf spielt ihn an, und Spieler neun trifft ins untere Tor. Das gibt noch einen Punkt für Team Neon.",
       mv("n9", [42, 47]), ps("b1", [42.6, 47.6], delay=0.3), ps("b1", [46, 54.7], after=True))],
    )]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
