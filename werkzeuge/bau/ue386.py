import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 58-P12 (U15-U17, Woche 30 Phase 6): Defending The Cross (Advanced Lead). 30 x 40 Yards = 27 x 37 m (gerundet 25 x 35 m).
# LANGES FELD QUER: Im PDF steht das Feld hochkant mit dem Tor rechts an der langen Seite. Um 90 Grad gegen den Uhrzeigersinn
# gedreht: Tor oben (an der langen Seite, etwas links wie im PDF), Verteidiger-Station mit Puppe unten links, Flügelspieler
# rechts, Trainer unten an der Seitenlinie. Feld x 9-87, y 4-51. Großfeldtor mit Torwart (nur C- und B-Jugend).
# Puppe als Stange, die gelbe und die rote Stange als zwei Stangen, durch die der Trainer passt (schräg zum Pass gestellt).
# Video gelb (Verteidiger) -> Team Neon 6 (aktiv), 4 und 5 (warten); Torwart grün 1 -> n1, der zweite Torwart (13) nur im Text.
# Video rot (Flügelspieler, Stürmer) -> Team Rot 7, 11 (Flügel), 9 und 10 (Stürmer in den Steigerungen). Rot 2 und 4 aus dem
# Video weggelassen (Nummern doppelt mit Gelb, nur Wartende). Ein Trainer statt zwei. Ballhaufen nur als zwei Ersatzbälle.
# Wertung ergänzt (im Original keine): weit geklärt oder vom Torwart gefangen = Punkt für Team Neon, Flanke ungeklärt vors Tor
# bzw. Treffer der Stürmer = Punkt für Team Rot.
# Fassungen: PDF Progression 1 (Stürmer vor dem Tor, eng ran) und Progression 2 (zwei gegen einen, ein Stürmer wechselt raus).
# In den Steigerungen fällt wie im Video der Sprint zur Puppe weg (Puppe bleibt stehen).
# Sichtkegel: kein Kegel im Video eingezeichnet; aus dem Ton („read the flight early“, „read ball flight and opposition
# movement early“, „positional awareness“): Grundform Spieler sechs schaut zum Flankengeber (bereit zur Annahme der Flanke).
# Die Kegel in Steigerung 1 und 2 (Verteidiger beobachtet die Stürmer) sind gestrichen (Regel vom 25.11.2026).
# Kegel auf etwa 20 Einheiten gekürzt (Richtung Flankengeber).
# Kein Dubletten-Fall: UE-185 (58-P4, köpfen und blocken an Minitoren), UE-225 (58-P3, Leiter und flache Flanke aufs Minitor),
# UE-248 (58-P7, zwei Verteidiger, Flanken im Wechsel), UE-308 (58-P6, 5 gegen 5), UE-348 (58-P8, Wellen), UE-350 (58-P11,
# 7 gegen 7), UE-368 (58-P5, Viererkette auf Zuruf) haben eine andere Organisation und andere Abläufe.
T = P("T", "c", 58, 55.3, "T")  # unten an der Seitenlinie
ERSATZ = [B("s1", 62, 55.8), B("s2", 64.5, 55.8)]
TW = P("n1", "a", 27.5, 8.5, "TW")
POS = {"n6": (38, 24), "n4": (12, 44), "n5": (21, 47), "r7": (82, 30), "r11": (84, 47)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [TW] + [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + [T]
LINES = [rect(9, 4, 78, 47)]
TORE = [{"x": 27.5, "y": 4, "side": "top", "size": "gross"}]
KEGEL = [C(29, 40.5, shape="stange"), C(65.6, 33.1, shape="stange"), C(73.6, 37.4, shape="stange")]
BALL = [B("b1", 58.6, 55.9)] + ERSATZ
FLUEGEL = [80.6, 14.6]
def einspielen(delay=0.2): return [ps("b1", FLUEGEL), mv("r7", [80, 14], delay=delay)]

u = {"title": "Puppe antippen, Flanke klären", "code": "UE-386", "kind": "Übungsform",
 "focuses": ["Verteidigen", "Schnelligkeit", "Zusammenspiel"], "age_groups": ["C-Jugend", "B-Jugend"],
 "altersbereiche": ["U15-U17"], "duration_minutes": 15, "players_min": 8, "players_max": 12,
 "field_size": "25 x 35 m",
 "description": "Ein Verteidiger von Team Neon sprintet vom Tor weg zur Puppe und tippt sie an. Das ist das Zeichen für den Trainer, der durch zwei Stangen auf den Flügel spielt. Der Flügelspieler von Team Rot nimmt den Ball im Lauf mit und flankt, der Verteidiger sprintet zurück und klärt zusammen mit dem Torwart. Weit geklärt gibt einen Punkt für Team Neon.",
 "organisation": ["Aufbauen: Ein Feld von 25 mal 35 Metern mit einem großen Tor an der langen Seite. Bei den Verteidigern steht eine Puppe, auf dem Weg zum Flügel zwei Stangen, durch die der Trainer passt.",
  "Verteilen: Ein Verteidiger von Team Neon steht vor dem Tor, die anderen warten an der Puppe. Die Flügelspieler von Team Rot warten außen. Ein Torwart steht im Tor, ein zweiter wartet daneben. Der Trainer steht mit vielen Bällen an der Seitenlinie.",
  "Ablauf: Der Verteidiger sprintet zur Puppe und tippt sie an. Der Trainer spielt durch die Stangen in den Lauf des Flügelspielers, der einmal mitnimmt und flankt. Der Verteidiger sprintet zurück vors Tor und klärt zusammen mit dem Torwart.",
  "Wertung und Wechsel: Weit geklärt gibt einen Punkt für Team Neon. Kommt die Flanke ungeklärt vors Tor, gibt das einen Punkt für Team Rot. Danach sind der nächste Verteidiger und der nächste Flügelspieler dran, die Torhüter wechseln nach drei Flanken."],
 "organisation_show": ORG,
 "coaching_points": ["Puppe antippen, dann Vollgas zurück vors Tor", "Torwart und Verteidiger sprechen: Wer geht?", "Hoch und weit klären, im Zweifel ins Aus", "Eng an den Stürmer, Körper rein"],
 "materials": ["1 Großfeldtor", "1 Puppe", "2 Stangen", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "abo", "hidden": True, "wartet_auf_ton": True,
 "say_intro": "Puppe antippen, Flanke klären. Ein Verteidiger sprintet raus zur Puppe und sofort zurück vors Tor, denn vom Flügel kommt die Flanke. Die klärt er zusammen mit dem Torwart.",
 "board": {"lines": LINES, "goals": TORE, "cones": KEGEL, "players": sp(), "balls": BALL,
  "steps": [
   S("Sprint zur Puppe", "Spieler sechs steht vor dem Tor und sprintet raus zur Puppe. Er tippt sie an. Das ist das Zeichen für den Trainer.",
     mv("n6", [31.5, 38])),
   S("Pass durch die Stangen", "Jetzt spielt der Trainer flach durch die zwei Stangen, und Spieler sieben läuft in den Ball. Spieler sechs dreht sofort um. Er sprintet zurück vors Tor, an den kurzen Pfosten.",
     *einspielen(), mv("n6", [34, 15], delay=0.3)),
   S("Mitnehmen und flanken", "Spieler sieben nimmt den Ball einmal mit. Spieler sechs schaut zu ihm und liest die Flanke früh. Der Torwart deckt den kurzen Pfosten und ruft laut, wer geht. Dann kommt die Flanke.",
     dr("r7", "b1", [77, 10.5]), bl("n6", [56, 12.5], delay=0.6), ps("b1", [34.6, 15.6], after=True)),
   S("Weit geklärt: Punkt", "Spieler sechs geht entschlossen hin und köpft den Ball weit raus ins Aus, und das gibt einen Punkt für Team Neon. Kommt die Flanke ungeklärt vors Tor, gibt das einen Punkt für Team Rot. Danach sprintet Spieler vier zur Puppe, und Spieler elf bekommt den nächsten Pass.",
     ps("b1", [44, 54]))],
  "dims": dims(9, 87, 4, 51, "35 m", "25 m", rx=93)},
 "versions": [
  V("Steigerung", "Und jetzt die Steigerung: Ein Stürmer wartet vor dem Tor auf die Flanke.", "Mit Stürmer vor dem Tor",
    "Ohne Sprint zur Puppe, dafür steht ein Stürmer von Team Rot vor dem Tor und will die Flanke verwerten. Der Verteidiger achtet darauf, wo der Stürmer hinläuft, und geht eng an ihn heran. Mit dem Körper nimmt er ihm den Schwung und ist vor ihm am Ball.",
    sp(r9=(24, 30)), list(BALL),
    [S("Ball auf den Flügel", "Der Trainer spielt durch die Stangen auf Spieler sieben. Spieler sechs wartet vorn bei Spieler neun.",
       *einspielen()),
     S("Eng ran an den Stürmer", "Spieler neun startet zum kurzen Pfosten. Spieler sechs geht sofort mit und bleibt eng an ihm dran, zwischen Stürmer und Tor. Außen nimmt Spieler sieben den Ball mit.",
       dr("r7", "b1", [77, 10.5]), mv("r9", [30, 17], delay=0.2), mv("n6", [33.5, 13], delay=0.3)),
     S("Vorn am Ball: Punkt", "Die Flanke kommt an den kurzen Pfosten. Spieler sechs ist vor Spieler neun am Ball und köpft weit raus, und das gibt einen Punkt für Team Neon. Trifft Spieler neun, gibt das einen Punkt für Team Rot. Danach ist Spieler vier mit dem nächsten Stürmer dran.",
       ps("b1", [34.1, 13.6]), ps("b1", [46, 54], after=True))]),
  V("Steigerung", "Und jetzt die zweite Steigerung: Zwei Stürmer gegen einen Verteidiger.", "Zwei gegen einen vor dem Tor",
    "Zwei Stürmer von Team Rot gegen einen Verteidiger, dazu der Torwart. Einer läuft zum kurzen, einer zum langen Pfosten. Der Flügelspieler flankt mal kurz, mal lang. Verteidiger und Torwart sprechen ab, wer welchen Ball nimmt. Nach jedem Angriff wechselt ein Stürmer raus.",
    sp(r9=(29, 31), r10=(16, 26)), list(BALL),
    [S("Kurz und lang", "Der Trainer spielt auf Spieler sieben. Vorn laufen beide Stürmer los, Spieler neun zum kurzen Pfosten, Spieler zehn zum langen. Spieler sechs bleibt am kurzen Pfosten bei Spieler neun.",
       *einspielen(), mv("r9", [32, 19], delay=0.3), mv("r10", [18, 15], delay=0.4), mv("n6", [36, 18], delay=0.4)),
     S("Torwart fängt: Punkt", "Spieler sieben nimmt mit und flankt lang an den zweiten Pfosten. Der Torwart ruft laut, kommt raus und fängt den Ball vor Spieler zehn. Das gibt einen Punkt für Team Neon. Trifft ein Stürmer, gibt das einen Punkt für Team Rot. Danach wechselt ein Stürmer raus, und Spieler elf bekommt den nächsten Pass.",
       dr("r7", "b1", [77, 10.5]), mv("n1", [21, 12], delay=0.9), ps("b1", [21.6, 12.6], after=True))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
