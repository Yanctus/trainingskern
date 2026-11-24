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
  und mit einer Umrechnung R() quer legen wie in ue319.py. Halbes Feld und kleiner bleibt wie bisher.
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
