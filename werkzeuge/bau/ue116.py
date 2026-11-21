import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *
# 41-P1: Sechseck 25 x 25 Yards, gedreht: Tore links und rechts, Spitzen oben und unten. Neon wartet oben links, Rot unten rechts.
T = P("T", "c", 25, 50, "T")
CB = [B("c1", 27.5, 50.6), B("c2", 24, 53.5)]
FEST = [P("k1", "t", 16, 30, "TW"), P("k2", "t", 84, 30, "TW"), P("d1", "t", 50, 22, "D"), P("d2", "t", 50, 38, "D"), T]
POS = {"n2": (26, 9), "n3": (17, 10), "r6": (74, 51), "r7": (83, 50)}
def sp(**k):
    d = dict(POS); d.update(k)
    return [P(i, "a" if i[0] == "n" else "b", x, y, i[1:]) for i, (x, y) in d.items()] + FEST
ECK = [(14, 19), (14, 41), (50, 52), (86, 41), (86, 19), (50, 8)]
HEX = [line(*ECK[i], *ECK[(i + 1) % 6], dashed=False) for i in range(6)]
TORE = [{"x": 14, "y": 30, "side": "left"}, {"x": 86, "y": 30, "side": "right"}]
u = {"title": "Abschluss, dann sofort zurück", "code": "UE-116", "kind": "Übungsform",
 "focuses": ["Torschuss", "Umschalten", "1 gegen 1"], "age_groups": ["E-Jugend", "D-Jugend", "C-Jugend", "B-Jugend"], "duration_minutes": 15, "players_min": 9, "players_max": 12, "field_size": "23 x 23 m",
 "description": "In einem Sechseck mit zwei Toren und Torhütern greift ein Spieler mit Ball an und schließt ab, ein Verteidiger setzt ihn unter Druck. Sofort danach startet von der anderen Seite der nächste Angreifer mit Ball, und wer gerade abgeschlossen hat, muss zurücksprinten und verteidigen. So wechseln Angriff und Abwehr ohne Pause.",
 "organisation": ["Aufbauen: Ein Sechseck von etwa 23 mal 23 Metern mit einem Tor links und rechts, in jedem Tor ein Torhüter. In der Mitte stehen zwei Dummys.",
  "Verteilen: Team Neon wartet mit Bällen oben links, Team Rot mit Bällen unten rechts. Der Trainer steht mit weiteren Bällen an der Seite.",
  "Ablauf: Auf Zuruf dribbelt ein Spieler von Team Neon los und schließt aufs rechte Tor ab, ein Spieler von Team Rot verteidigt. Danach startet sofort ein Spieler von Team Rot mit Ball aufs linke Tor, und der Neon-Spieler sprintet zurück und verteidigt.",
  "Wechsel: So geht es im Wechsel weiter. Jedes Tor gibt einen Punkt für das Team."],
 "organisation_show": ORG,
 "coaching_points": ["Schnell vom Angriff auf die Abwehr umschalten", "Mit Tempo angreifen und mit voller Einstellung verteidigen", "Als Verteidiger den Angreifer vom Tor weglenken", "Vor dem Tor ruhig bleiben und genau abschließen"],
 "materials": ["2 Tore", "2 Dummys", "Hütchen für das Sechseck", "Viele Bälle", "Leibchen in zwei Farben"],
 "access": "frei", "hidden": True,
 "say_intro": "Abschluss, dann sofort zurück. Wer gerade aufs Tor geschossen hat, muss sofort zurück und verteidigen.",
 "board": {"lines": HEX, "goals": TORE, "players": sp(), "balls": [B("b2", 27.6, 9.6), B("b7", 84.6, 50.6)] + CB,
  "steps": [
   S("Neon greift an", "Neon zwei dribbelt mit Tempo los. Gleichzeitig kommt Rot sechs von der anderen Seite und setzt ihn unter Druck. Neon zwei schießt ins rechte Tor, das gibt einen Punkt für Team Neon.",
     dr("n2", "b2", [38, 26]), dr("n2", "b2", [62, 34], after=True), mv("r6", [72, 42], delay=0.3), ps("b2", [85.5, 35], after=True)),
   S("Umschalten", "Sofort startet Rot sieben mit Ball aufs linke Tor. Gleichzeitig sprintet Neon zwei zurück und verteidigt.",
     dr("r7", "b7", [66, 26]), dr("r7", "b7", [40, 26], after=True), mv("n2", [46, 31], delay=0.2)),
   S("Abschluss von Rot", "Rot sieben schließt trotz Druck ab und trifft ins linke Tor. Das gibt einen Punkt für Team Rot.",
     ps("b7", [14.5, 25]), mv("n2", [36, 30]))],
  "dims": [{"x1": 14, "y1": 58.6, "x2": 86, "y2": 58.6, "text": "23 m"}, {"x1": 94, "y1": 8, "x2": 94, "y2": 52, "text": "23 m"}]},
 "versions": [
  V("Coaching-Punkt", "Jetzt zum Coaching-Punkt: Nach dem Schuss nicht stehen bleiben.", "Nicht das Tor bewundern",
    "Wer nach dem Abschluss stehen bleibt und dem Ball hinterherschaut, lässt dem nächsten Angreifer freie Bahn. Deshalb gilt: Ball weg, sofort umdrehen und zurücksprinten. So bleibt das Spiel schnell und jeder bleibt wach.",
    sp(n2=(62, 34), r6=(72, 44)), [B("g", 63.6, 34.6), B("b7", 84.6, 50.6)] + CB,
    [S("Schießen und schauen", "Neon zwei schießt aufs Tor und bleibt stehen, um dem Ball hinterherzuschauen. Gleichzeitig startet Rot sieben schon mit Ball.",
       ps("g", [85.5, 35]), dr("r7", "b7", [66, 26], delay=0.3)),
     S("Freie Bahn", "Weil Neon zwei nicht zurückläuft, dribbelt Rot sieben ohne Gegner bis vors Tor und trifft. So darf es nicht laufen: Nach dem Schuss sofort zurücksprinten.",
       dr("r7", "b7", [30, 26]), ps("b7", [14.5, 25], after=True))]),
  V("Steigerung", "Und jetzt die Steigerung: Zwei gegen eins.", "Zwei gegen eins",
    "Jetzt greifen zwei Spieler gegen einen Verteidiger an. Sie kombinieren schnell und nutzen die Überzahl. Nach dem Abschluss muss einer der beiden zurück. Der Verteidiger von eben greift sofort mit dem nächsten Spieler seines Teams im zwei gegen eins an.",
    sp(), [B("b2", 27.6, 9.6), B("b7", 84.6, 50.6)] + CB,
    [S("Zu zweit los", "Gleichzeitig starten Neon zwei mit Ball und Neon drei. Rot sechs kommt von der anderen Seite und verteidigt.",
       dr("n2", "b2", [40, 24]), dr("n2", "b2", [56, 30], after=True), mv("n3", [34, 42]), mv("n3", [60, 46], after=True), mv("r6", [64, 37], delay=0.3)),
     S("Querpass und Abschluss", "Rot sechs greift Neon zwei an. Neon zwei spielt quer zu Neon drei, der direkt ins Tor schießt. Das gibt einen Punkt für Team Neon.",
       ps("b2", [61.6, 46.6]), ps("b2", [85.5, 34], after=True)),
     S("Zwei gegen eins zurück", "Sofort starten Rot sieben mit Ball und Rot sechs aufs linke Tor. Gleichzeitig sprintet Neon zwei zurück und verteidigt allein.",
       dr("r7", "b7", [66, 22]), mv("r6", [46, 48]), mv("n2", [40, 30], delay=0.2))])]}
json.dump(u, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
