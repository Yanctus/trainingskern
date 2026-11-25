# Auftrag: Übungen einer Woche aus dem Plan U12-U14 nachbauen (Trainingskern, Base44-App 6afec076c6c4a55a7cb4995e)

Du baust die Übungen EINER Woche als neue Einheiten (Entity `Einheit`) und lädst sie hoch. Arbeitsverzeichnis:
`/home/user/trainingskern/werkzeuge`. Lies zuerst komplett `SCHNELLWEG.md` (Workflow und feste Regeln) und `bau/hilfe.py`
(Bausteine). Gute Vorbilder: `bau/ue145.py` bis `bau/ue156.py` (Kommentarkopf, POS/sp(), Steps, Versions). Die Rohdaten jeder
Übung liegen schon unter `import/<Woche>/<Übung>/` (text.txt, ton.txt, pdf-1.png, pdf-2.png, uebersicht.png, video.mp4).

## Ablauf pro Übung
1. text.txt und ton.txt lesen, pdf-1.png ansehen, dann gezielt `python3 werkbank.py szene "<Ordner>" <von> <bis> <fps>` für die
   Abschnitte mit Laufwegen (Grundform, Steigerungen). Sichtkegel suchen (siehe unten).
2. Dubletten-Check: Wenn dir im Auftrag ein Verdacht genannt ist, vergleiche mit der genannten Einheit
   (`python3 werkbank.py lesen UE-0xx /tmp/claude-0/x.json`). Ist es dieselbe Übung (gleiche Organisation und Abläufe), NICHT neu
   bauen, sondern `update_entities` mit Query `{"code":"UE-0xx"}` und `{"$addToSet": {"altersbereiche": "U12-U14"}}`, dann melden.
3. `python3 werkbank.py vorgaben "<Übungsname>"` für age_groups und duration_minutes (genau übernehmen).
4. `bau/ueNNN.py` schreiben, `python3 bau/ueNNN.py ueNNN.json && python3 werkbank.py pruefen ueNNN.json` bis „0 Treffer“ und
   nur noch der Hinweis „access … hidden false“ übrig ist. Dann `python3 werkbank.py blatt ueNNN.json` und das Bild
   `ueNNN-blatt.png` ansehen (2D-Laufwege und 3D): Laufwege sinnvoll? Verdeckt sich etwas in 3D? Ggf. korrigieren.
   **Sichtkegel (Inhaber, 25.11.2026):** Ein Kegel gehört nur zu dem Spieler, der schaut und danach selbst passt oder schießt
   (Passgeber vor seinem Pass; beim Annehmen und Aufdrehen schaut der Empfänger zum Passgeber und schwenkt nach der Annahme zum
   Ziel). Nie beim Empfänger, der in den Raum schaut, nie bei Läufern, beobachtenden Verteidigern oder in Reaktionsspielen. Sagt das
   Original „scanning“ eines Läufers, bekommt der Passgeber den Kegel. Prüfen: `node blickpruefung.mjs /tmp/claude-0/pb.mjs ueNNN.json
   /tmp/b-ueNNN.json` muss „Funde: 0“ zeigen. Einzelheiten anleitung/BLICK_FIX.md.
   **Passbahn (Inhaber, 25.11.2026):** Kein Pass geht durch einen Gegenspieler. Prüfen mit
   `node passbahn.mjs /tmp/claude-0/pb.mjs ueNNN.json /tmp/pb-ueNNN.json` (Abspielcode der App, gebündelt; fehlt die Datei, in
   der Base44-Sandbox neu bündeln, Befehl im Kopf von passbahn.mjs). Erwartet: „Treffer: 0“. Ausnahmen nur, wenn der Pass
   absichtlich zugestellt ist oder abgefangen werden soll (dann sagt es der Text). Korrigieren wie in anleitung/PASSBAHN_FIX.md.
5. Hochladen (genau so):
   a) `create_entities` (entityName `Einheit`) mit nur `{"code","title","kind","duration_minutes","hidden":true,"access":"abo"}`.
   b) Payload erzeugen: `python3 -c "import json;u=json.load(open('ueNNN.json'));[u.pop(k) for k in ['code','title','kind','duration_minutes','hidden','access']];print(json.dumps({'\$set':u},ensure_ascii=False,separators=(',',':')))"`
      und GENAU diesen Text als `data` an `update_entities` (Query `{"code":"UE-NNN"}`) geben. Nichts abtippen oder umformulieren.
   c) `update_entities` mit `{"$set":{"hidden":false}}`.
   d) `python3 werkbank.py lesen UE-NNN e2_NNN.json`, in ueNNN.json `hidden` auf false setzen,
      `python3 werkbank.py vergleichen ueNNN.json e2_NNN.json` muss „0 Abweichungen“ zeigen, `pruefen e2_NNN.json` „0 Hinweise“.
      Bei Abweichungen: `python3 werkbank.py patch e2_NNN.json ueNNN.json` und nur diesen $set senden, erneut prüfen.
6. Danach `ueNNN.json` nach `bau/` verschieben, `e2_NNN.json` und `ueNNN*.html`, `ueNNN-3d.js`, `ueNNN*.html.js` löschen.

## Feste Inhalts-Regeln (vom Inhaber, unbedingt)
- Deutsch, kurze Sätze, kindgerecht. Team Neon (team "a", ids n…) und Team Rot (team "b", ids r…). Trainer genau einer:
  `P("T","c",x,y,"T")` mit zwei Ersatzbällen daneben. Springer/neutrale Spieler: team "t", Label "F". Neutraler Torwart:
  `P("k","t",x,y,"TW")`. Torwart eines Teams: id n1 bzw. r1 mit Label "TW".
- Rückennummern über beide Teams eindeutig (bei Doppelten im PDF Rot neu nummerieren und im Kommentar vermerken).
- Titel höchstens 32 Zeichen, kein Wort länger als 14 Zeichen, kein Doppelpunkt-Untertitel. kind nur "Übungsform" oder "Spielform".
- description 3-4 Sätze. organisation genau 4 Einträge ("Aufbauen: …", "Verteilen: …", "Ablauf: …", "Wertung…/Wechsel: …").
  organisation_show = ORG. Genau 4 coaching_points. altersbereiche ["U12-U14"]. access "abo".
- tags (Feld an der Einheit): Übungen aus Pre-Season-Wochen `"tags": ["Vorbereitung"]`, aus dem Ordner „Goalkeeper Specific“
  `"tags": ["Torwart"]`, aus „Individual Development“ `"tags": ["Einzeltraining"]`. Sonst kein tags-Feld.
- „gibt einen Punkt“, nie „Tor“ als Ergebnis: „…, und das gibt einen Punkt für Team Neon“. Step-Label bei Treffern „…: Punkt“.
- Einzelne Spieler immer „Spieler sieben“, nie „Neon sieben“/„Rot vier“ (Team bleibt „Team Neon“).
- Fangen statt abschlagen. Machen alle gleichzeitig etwas, das sagen und parallel zeigen.
- say-Texte ohne Ziffern (Zahlen ausschreiben), nicht mit „Tor.“ oder „Punkt.“ enden ohne „gibt“. say_intro beginnt mit dem Titel.
- Grundform 3-6 Schritte. Der LETZTE Schritt der Grundform sagt das Ergebnis (wer bekommt den Punkt) UND wer danach dran ist.
- Genau 2 Fassungen (versions), Label nur "Coaching-Punkt" oder "Steigerung". say beginnt mit „Jetzt zum Coaching-Punkt: …“ /
  „Der zweite Coaching-Punkt: …“ bzw. „Und jetzt die Steigerung: …“ / „Und jetzt die zweite Steigerung: …“. Fassung mit eigenen
  Hütchen: alle Hütchen der Fassung brauchen eine id. Fassungen dürfen goals/lines ergänzen (Grundform-Linien mit übernehmen).
- Tore: Minitor Standard; mit Torwart `"size":"jugend"`. Geteilte Felder/Zonengrenzen als gestrichelte `line`.
- Farben für Hütchen nur "orange" (Standard) oder "neon". Dummy/Stange: `C(x,y,shape="stange")`. Hürden: shape "huerde"/"huerde_ou".
- Koordinationsleiter IMMER als Leiter, nie als Reihe Hürden: `leiter(x, y)` (liegt waagrecht, 16 x 5 Einheiten, Mitte bei x/y,
  wird von links nach rechts durchlaufen) oder `leiter(x, y, senkrecht=True)` (von oben nach unten). Längere Leiter = zwei Leitern
  hintereinander. Ringe/Reifen IMMER zeichnen: `ring(x, y)` (Durchmesser ca. 4,6 Einheiten, Abstand Mitte zu Mitte ca. 6).
  Leitern und Ringe sind für Laufwege kein Hindernis (man läuft hindurch). Echte Minihürden bleiben "huerde"/"huerde_ou".
- Großfeld QUER (Inhaber, 24.11.2026, mit UE-319 abgenommen; Vorbild: bau/ue319.py): Spielt die Übung auf dem ganzen Platz oder
  einem Dreiviertelfeld (ab etwa 60 m Länge, viele Spieler, z. B. 8 gegen 8 bis 11 gegen 11), liegt das Feld QUER wie im Fernsehbild:
  Tore links und rechts (`"side": "left"` / `"right"`, `"size": "gross"`), echte Platzlinien (Außenlinie, Mittellinie, Mittelkreis
  `{"type": "circle", ...}`, Strafräume, Torräume; Drittel-Linien gestrichelt, wenn das Original sie hat), Feld etwa x 7-91, y 3-52.
  Dazu im Haupt-board `"massstab": "gross"` (die 3D-Bühne zeigt Figuren, Bälle und Hütchen dann kleiner; der 3D-Abstand wird in
  `pruefen` entsprechend kleiner gerechnet). Nur die Längen-Maßlinie unten (rechts neben dem Tor ist kein Platz), die Breite steht
  in field_size. Trainer an der Seitenlinie unten, nahe der Stelle, wo er einspielt (kein Pass quer über den ganzen Platz).
  Spieler einer Kette stehen quer hintereinander: weit genug auseinander (pruefen meldet es sonst). Bequem: im Hochformat planen
  und mit einer Umrechnung R() quer legen wie in ue319.py. Ein halbes Feld liegt ebenfalls quer, aber nach eigener Regel
  („Halbes Feld QUER“, gleich darunter). Kleinere Felder ohne echten Strafraum wie bisher (lange Felder: „Langes Feld QUER“).
- Halbes Feld QUER (Inhaber, 25.11.2026; Vorbild bau/ue352.py, Hilfsfunktion bau/halbfeld.py):
  WANN: Die Übung spielt auf einer Platzhälfte oder einem Stück davon mit echtem Strafraum und großem Tor (etwa 35-55 m tief,
  volle oder fast volle Breite), z. B. „full half“, „half pitch“. Gilt für den Umbau von UE-314, 340, 366, 370, 380, 381, 402.
  LAGE wie im Fernsehbild: großes Tor RECHTS (`"side": "right"`, `"size": "gross"`), die Platzbreite von oben nach unten
  (y 3-52), die Mittellinie (bzw. das Feldende) am linken Rand, Team Neon greift nach rechts an. Passt das nicht zur Übung
  (z. B. Team Rot greift an und der Text erzählt aus dessen Sicht), so legen, dass die Laufrichtung zum Text passt;
  Tor links mit `Halbfeld(tor="links")`. Immer drehen, nie spiegeln (bend und drehen(gegen=...) bleiben).
  `"massstab": "gross"` im Haupt-board (nicht in den Fassungen), Figuren dadurch kleiner; 3D-Abstand dann |dx| ≥ 5,9 ODER
  |dy| ≥ 11,2 (regeln.py rechnet 8,2 bzw. 15,5 mal 0,72).
  ABBILDUNG (nicht von Hand rechnen, `import halbfeld as hf; F = hf.Halbfeld(tief=50, breit=65)`): Eine Hälfte ist etwa 50 m
  tief und 65 m breit und muss in der Waagerechten gestreckt werden, damit sie die Tafel füllt (x 10-90). Die Streckung wächst
  ohne Knick vom Tor zur Mittellinie: an der Torlinie 1,39-mal so viel wie in der Breite (Strafraum, Torraum und Bogen wirken
  fast echt), an der Mittellinie gut 2-mal (dort sind keine Linien, die verraten es). Senkrecht überall 49 Einheiten für die
  Platzbreite. `F(d, q)` -> Tafelpunkt: d = Meter vor der Torlinie (0 = Torlinie), q = Meter von der OBEREN Seitenlinie
  (beim Tor rechts = linke Seite des Angreifers). Kürzere Felder (`tief=35`) werden gleich gestreckt und stehen mittig.
  `F.tiefe(x)` rechnet Tafel-x zurück in Meter.
  LINIEN: `F.linien()` liefert Außenlinie (ihre linke Kante IST die Mittellinie), Strafraum (16,5 x 40,3 m), Torraum
  (5,5 x 18,3 m), Strafraumbogen (Linienstücke, die App kennt keine Bögen) und ab 45 m Tiefe den halben Mittelkreis. Der
  Mittelkreis ist absichtlich RUND im Maßstab der Breite gezeichnet (umgerechnet wäre er ein langes Oval): nur Zierde, niemand
  danach ausrichten. Ohne Strafraum/Bogen/Kreis: `F.linien(strafraum=False, bogen=False, mittelkreis=False)`. Tore:
  `[F.tor()] + F.minitore(10, 55)` (Minitore auf der Mittellinie, q in Metern; `d=` für eine andere Linie). Eigene Zonen und
  Linien in Metern planen und mit F umrechnen (Rechteck aus den Ecken F(d0, q0) und F(d1, q1), gestrichelt), nicht genau auf
  eine Platzlinie legen (sonst doppelte Linie; in ue352 beginnt die Mittelzone bei 18 m statt 16 m).
  POSITIONEN: am besten in Metern planen wie ue352.py (POS = {"n9": (13, 33), ...}, Torwart ~2 m, Viererkette 8-12 m vor dem
  eigenen Tor usw.). Aus einem alten Hochkant-Skript: `R = F.von_hochkant(x0, y0, x1, y1)` (altes Feld, Tor oben bei y0) und
  `P, B, C, mv, ps, dr, drehen, bl = hf.umrechnen(R)`; das dreht auch Hürden und Leitern (huerde <-> huerde_ou, leiter <->
  leiter_ou). Achtung: alte Hochkant-Felder waren nicht metergenau (Torwart und Kette standen oft zu nah am Tor) und der
  Strafraum ist jetzt echt groß; danach jede Position in Metern prüfen (`F.tiefe(x)`) und neu setzen. `hf.am_fuss(p)` = Ball
  am Fuß / Pass zum Spieler (+0,6), `hf.richt(a, b, 20)` = Blickkegel höchstens 20 Einheiten lang (beides in Tafelpunkten).
  Wer im Hochformat nebeneinander stand (Ketten), steht jetzt hintereinander: in der Tiefe staffeln (die Verteidiger torseitig
  versetzt), bis pruefen nichts mehr meldet. In Strafraumnähe ist ein Meter weniger breit (1,05 Einheiten) als im Mittelfeld
  (über 2 Einheiten): Wer vor dem Tor steht, braucht in Metern mehr Abstand.
  TRAINER unten an der Seitenlinie (y 55,3) nahe der Stelle, wo er einspielt, Ersatzbälle rechts daneben (y 55,8). Maßlinie nur
  die Tiefe unten (`F.masslinie("50 m")`), nie rechts (dort steht das Tor); bei field_size „Halbes Spielfeld“ ohne Maßlinie.
  RICHTUNGSWÖRTER: Alle Texte (say_intro, say, label, title, text, description, organisation, coaching_points) auf oben/unten/
  links/rechts/Ecke durchsuchen. Aus „oben“ (Tor) wird „vorn“, „Richtung Tor“, „auf der Torlinie“; aus „unten“ (Mittellinie)
  „hinten“, „an der Mittellinie“; links/rechts im Hochformat werden quer zu oben/unten, darum lieber „auf der Seite“, „außen“,
  „auf der anderen Seite“, „zur Ballseite“. Steht in der runden.js-Zeile ein Richtungswort, eine neue Zeile melden.
  PRÜFEN: `pruefen` 0 Treffer und 0 Hinweise, `blatt` ansehen (Strafraum nicht verzerrt, nichts verdeckt sich in 3D, Tor und
  Minitore ganz auf der Tafel: das Großtor ragt bis x 95,5, Minitore an der Mittellinie bis x 6,8), dann $set wie üblich.
- Langes Feld QUER (Inhaber, 24.11.2026, mit UE-317 abgenommen; Vorbild: bau/ue317.py): Ist das Feld deutlich länger als breit
  (Verhältnis ab etwa 1,3, z. B. 25 x 40 m), liegt die lange Seite waagrecht und das Feld füllt die Tafel (etwa x 9-89, y 4-51;
  in beiden Richtungen möglichst derselbe Maßstab, so groß wie möglich). Nie mehr ein schmales Hochkant-Feld in der Mitte der Tafel.
  Tore an den kurzen Seiten dann links/rechts. Figuren normal groß (massstab "gross" nur beim Großfeld). Steht rechts ein Tor, nur die
  Längen-Maßlinie unten (rechts ist kein Platz). Trainer unten an der Seitenlinie. Wer im Hochformat nebeneinander stand, steht quer
  in der Tiefe hintereinander: in der Länge leicht versetzen, bis pruefen keinen 3D-Abstand mehr meldet. Bequem: im Hochformat planen
  und mit R() quer legen. Texte ohne oben/unten/links/rechts, wo es geht („auf der anderen Seite“, „außen“, „Richtung Tor“).
- 3D-Abstand: zwei Figuren (Spieler, Trainer) in derselben Tafel brauchen |dx| ≥ 8.2 ODER |dy| ≥ 15.5 (Board 0-100 × 0-60,
  Feld meist x 25-75, y 5-55). Wartende Spieler lieber neben das Feld oder nur im Text erwähnen.
- Bälle am Fuß: Spieler (x,y) → Ball (x+0.6, y+0.6). Pässe zu einem Spieler enden ebenso bei (x+0.6, y+0.6).
- Laufwege/Pässe dürfen nicht durch Hütchen, Stangen oder Spieler gehen (pruefen meldet „Treffer“) → Zwischenpunkte setzen
  (mehrere `mv(..., after=True)`), Positionen leicht verschieben. Spricht der Text von einem Bogen/„herum“, braucht der Weg Zwischenpunkte.
- Orientierung: möglichst nach oben spielen (Tor oben); gedreht/gespiegelt im Kommentar und Bericht vermerken.
- Aufdrehen/Drehung (Inhaber, 24.11.2026): Dreht ein Spieler auf (turn, open up, half-turn), dafür NIE den Blickkegel nehmen,
  sondern den Drehpfeil `drehen(who, to)` (Bogen um den Spieler, endet in Richtung to; `gegen=True` = gegen den Uhrzeigersinn).
  Der Blickkegel `bl()` ist nur fürs Schauen.
- Schaut ein Spieler erst hier, dann dort (z. B. erst zum Passgeber, dann dorthin, wohin er weiterspielt): EIN Kegel, der
  mitschwenkt, nie zwei Kegel: `bl(who, to=<wohin er als Nächstes spielt>, von=<worauf er zuerst schaut>)`. Der Kegel steht
  kurz auf `von`, dreht hinüber und bleibt genau mittig auf `to` stehen (`to` = Ziel des nächsten Passes).
  WICHTIG, Reihenfolge beim Annehmen und Aufdrehen: Der Blick wechselt ERST NACH der Ballannahme, nicht vorher.
  Schritt A: `bl(who, <Passgeber>)`, dann der Pass zu ihm (`ps(..., after=True)`). Er schaut also zum Ball, bis er ihn hat.
  Schritt B: `bl(who, <Passziel>, von=<Passgeber>, dauer=1.3)` (Kegel schwenkt hinüber), dazu `drehen(who, <Passziel>, delay=0.4)`
  (er dreht auf der Stelle auf), danach sein Pass (`ps(..., after=True)`).
- Meterangaben (Inhaber, 24.11.2026): Unter 20 m genau lassen, ab 20 m auf Fünferschritte runden (27 -> 25, 36 -> 35, 41 -> 40).
  Das gilt für `field_size`, die Maßlinien (`dims`) und alle Texte (organisation, description, say). Die App rundet die Anzeige
  von field_size und dims zusätzlich selbst; Texte muss man gleich gerundet schreiben.
- Sichtkegel (Pflicht): bei scan / check shoulder / head up / look up / awareness / vision / see the picture / identify / spot …
  in Text, Ton oder Video `bl(who, to)` einbauen. Richtung aus dem Video (dort eingezeichnet) oder aus dem Sinn. Kegel nicht
  zu lang (Ziel ca. 15-25 Einheiten entfernt in der richtigen Richtung). Sonst im Kommentar „Kein Sichtkegel im Original
  (Text, Ton und Video geprüft)“.
- Keine Geheimnisse ausgeben, nichts per curl in die Datenbank schreiben, nicht veröffentlichen, nicht git committen,
  `src/lib/runden.js` und `BERICHT.md` NICHT anfassen (das mache ich).

## Rückmeldung (am Ende, knapp)
Pro Übung eine Zeile im Format:
`UE-NNN | Titel | <Original-Name mit Kennung> (U12-U14, Woche X) | https://trainingskern.de/einheiten/<id> | Abweichungen und Sichtkegel-Info |`
plus je eine runden.js-Zeile im Stil:
`  "UE-NNN": { ablauf: "…", punkte: "… gibt einen Punkt …" (oder ziel: "…"), wechsel: "…" },`
Bei Dubletten: welche bestehende Einheit ergänzt wurde. Probleme ehrlich nennen (z. B. was nicht geprüft werden konnte).
