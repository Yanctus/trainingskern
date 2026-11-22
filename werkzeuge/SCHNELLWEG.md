# Schnellweg: Woche für Woche Übungen nachbauen (Stand 21.11.2026)

Ziel: alle restlichen Wochen (21 bis 42) nacheinander, richtig, geprüft und mit wenig Tokens. Diese Werkzeuge liegen im GitHub-Repo
(`werkzeuge/`) und sind in jeder neuen Sitzung sofort da, ohne sie aus der App zu kopieren. Maßgeblich für Regeln und Tafel bleibt die
README der App (Abschnitte „Übungen aus Video nachbauen“, „Laufweg-Abgleich“, „Prüfliste“). Pro Chat 2 Wochen, dann neuen Chat starten.

## Einmal pro Sitzung
- `base44_readme` aufrufen. Werkzeuge: `cd werkzeuge` (liegt im Repo). Nichts aus der App kopieren.
- Nächsten Code holen: `python3 werkbank.py lesen UE-0xx x.json` zum Prüfen, ob ein Code schon belegt ist (siehe README der App: „nächster Code“).

## Pro Woche
0. Drive-Ordner: `TK_PLAN=u12` (Standard, Plan U12-U14 ab 22.11.2026) oder `TK_PLAN=u9` (erster Plan). Wochen heißen
   „Week 1 - Pre-Season“ usw. Doppelte erkennen: Original-Kennung (z. B. 94-P6) mit BERICHT.md und bau/*.py abgleichen,
   und Titel/Beschreibung im Katalog durchsuchen (ältere Einheiten haben keine gespeicherte Kennung).
1. `python3 werkbank.py holen <Woche>` (Video, PDF, Text, Übersicht).
2. `python3 werkbank.py ton <Ordner>` für jede Übung (Spracherkennung, ca. 10 s, einmalig `pip install faster-whisper`): Die gesprochene
   Erklärung steht dann mit Zeitstempeln in `ton.txt`. Zuerst `text.txt` und `ton.txt` lesen (kostet fast nichts), dann ansehen
   (sparsam, jedes Bild kostet): `pdf-1.png`, `pdf-2.png`, `uebersicht.png`.
   Dann gezielt `szene <Ordner> <von> <bis>` nur für die Abschnitte mit Laufwegen (Grundform, jede Fassung). Abschnitte aus der
   Übersicht ablesen: Bild n (ab 0) liegt bei n × Dauer/25 Sekunden.
3. Pro Schritt notieren: wer, von wo, über welche Zwischenpunkte, welche Seite, wann (vor/nach dem Pass), wohin der Pass.
   **Sichtkegel suchen (Pflicht, Inhaber 22.11.2026):** Nicht nur „Schulterblick“: jede Wahrnehmung vor der Aktion zählt,
   z. B. scan, scanning, check your shoulder, look over the shoulder, head up, lift your head, look up, awareness, open your
   body to see, see the picture, know where …, identify the GK's position, spot the free player, before receiving.
   Suchen: `grep -iE "scan|shoulder|head up|look|aware|check|picture|identify|spot|see the|vision" text.txt ton.txt`.
   Die Richtung des Kegels kommt aus dem Original-Video (Szenenbilder): dort ist der Kegel eingezeichnet, also genau dahin
   schauen lassen (z. B. zum Torwart vor dem Abschluss, zum Gegenspieler im Rücken, zum freien Mitspieler). Steht es nur im
   Text, die Richtung aus dem Sinn ableiten (wohin muss er schauen, um die Entscheidung zu treffen). Gefunden = `bl(...)`
   einbauen (siehe Feste Regeln), sonst im BERICHT „kein Sichtkegel im Original“ vermerken.
4. `python3 werkbank.py vorgaben "<Übungsname>"` für Altersstufen und Dauer (stehen nicht im PDF; feste Regel).

## Feste Regeln (vom Inhaber, 21.11.2026)
- **Altersbereich = Plan, aus dem die Übung stammt** (Feld `altersbereiche`, unabhängig von `age_groups`): alle Übungen bis
  einschließlich des ersten Plans sind `["U9-U11"]`. Jede Übung aus dem Plan U12-U14 bekommt `"U12-U14"`.
  **Doppelte Übungen nicht neu bauen:** Gibt es die Übung schon (gleiche Organisation und Abläufe, evtl. anderer Name), die
  bestehende Einheit benutzen und nur `"U12-U14"` ergänzen: `update_entities` mit `{"$addToSet": {"altersbereiche": "U12-U14"}}`.
  Vorher abgleichen: `python3 werkbank.py lesen` und Titel, Beschreibung und Skizze vergleichen; im Zweifel den Inhaber fragen.
- **Titel kurz** wie bei UE-001 bis UE-030: höchstens 32 Zeichen, kein Untertitel nach dem Doppelpunkt (z. B. „Verteidigen zu zweit“).
- **Ein Tor ist immer ein Punkt:** „…, und das gibt einen Punkt für Team Neon“ (oder für Spieler X), nie „das gibt ein Tor“. Label „…: Punkt“.
- **Fangen, nicht abschlagen:** Kinder fangen sich (berühren), sie schlagen nicht ab.
- **Alle gleichzeitig:** Machen alle Spieler gleichzeitig dasselbe (Fangspiele, Staffeln), das in Text und Bühne sagen („Alle laufen
  gleichzeitig … Wir schauen auf Spieler sechs“) und auf der Bühne auch andere Spieler parallel handeln lassen.
- **Geteiltes Feld:** Hälften und Linien als gestrichelte `line` einzeichnen (erscheinen grau). Nur in einer Fassung: dort `lines` = alle
  Linien der Grundform plus die neuen.
- **Fassungen dürfen Linien UND Tore ergänzen** (z. B. Minitore nur in der Steigerung): alle der Grundform mit übernehmen, die Bühne zeigt die neuen mit dem Kapitel.
- **Bewegliche Hütchen in einer Fassung** (z. B. Farbtafel): dann müssen alle Hütchen der Fassung eine `id` haben (auch die festen).
- **Zonen farbig:** `{"type":"zone", …}`; Zonen von Team Rot mit `"color":"orange"`, sonst neon. Keine gestrichelten Rechtecke für Zonen.
- **Neue Einheiten gleich `access: "abo"` (Pro)** (Inhaber, 22.11.2026): Nur 5 Übungen sind frei mit Konto (UE-004, UE-005,
  UE-007, UE-008, UE-011), UE-001 ist offen ohne Konto. Alles andere ist Pro.
- **Wenig Prüfläufe:** kostenlos und immer: `pruefen`, `blatt`, `vergleichen`. Prüfstand nur nach Änderungen am Player-Code oder wenn
  das Blatt etwas Seltsames zeigt (dann nur Chromium). Live-Check einmal pro Woche mit `live.js` (dafür kurz auf „frei“, danach sofort zurück auf „abo“).

- **Zugang:** `offen` = ohne Konto (nur eine Schaufenster-Übung, zurzeit UE-001), `frei` = mit kostenlosem Konto (genau 5 Übungen),
  `abo` = Pro. Neue Einheiten sind sofort `abo`.
- **Schulterblick (ab 22.11.2026 für alle neuen Einheiten):** Zeigt das Video, dass ein Spieler vor der Ballannahme das Feld
  scannt (Blickwinkel eingezeichnet), dann im Schritt davor bzw. im selben Schritt `bl("n6", [x, y])` aus `bau/hilfe.py`
  einsetzen: ein halbtransparenter Kegel vom Spieler in Richtung `to`, so lang wie der Abstand (Standard: 70° Öffnung,
  0,9 s). Links und rechts scannen = zwei `bl(...)` nacheinander, das zweite mit `after=True`, danach der Pass mit
  `after=True`. Ein Blick bewegt niemanden. Im Sprechtext darf es stehen („schaut über die Schulter“), muss aber nicht.

- **Tore:** Minitor ist Standard (`{"x","y","side"}`). Steht ein Torwart drin, ist es ein großes Tor: `"size": "jugend"`
  (Jugendtor 5 x 2 m), sobald die Altersstufen D-Jugend oder jünger enthalten; nur C-Jugend und älter / Amateure bekommen
  `"size": "gross"` (Großfeldtor/Erwachsenentor 7,32 x 2,44 m). In 3D stehen Tore als Aufsteller auf der Torlinie, immer
  von vorn gezeichnet; Tore links und rechts drehen sich mit der Öffnung zum Feld. Auf der Skizze mit Netz, Tintenrahmen
  und orangen Pfosten.

## Feste Begriffe (vom Inhaber)
- **Springer sind immer neutrale Spieler:** `team: "t"`, Label „F“, spielen für das Team in Ballbesitz, im Text „Springer“.
- Einheiten dürfen zum Live-Check kurz auf „frei“, danach sofort zurück auf „abo“.
- Altersstufen, Dauer und Spielerzahl stehen nicht im PDF: `vorgaben` benutzen, Spielerzahl aus der Skizze.
- Fassungen dürfen Linien ergänzen (z. B. Hälften in einer Steigerung): dann alle Linien der Grundform mit übernehmen.

## Pro Einheit (JSON nur EINMAL schreiben)
Einheit als kleines Python-Skript in `werkzeuge/bau/ue0xx.py` bauen (Bausteine in `bau/hilfe.py`, Vorbild `bau/ue061.py` bis `ue063.py`),
`python3 bau/ue0xx.py e.json`, dann:
1. `create_entities` klein: `{"code","title","kind","duration_minutes","hidden":true,"access":"abo"}` (Antwort ist klein).
2. `update_entities` mit `{"$set": {…alle übrigen Felder…}}`. Felder mit `null` weglassen (spart Tokens). Antwort ist nur eine Zahl.
3. `python3 werkbank.py lesen UE-0xx e.json` (kostenlos) → `pruefen e.json --fix` → bei Änderungen
   `python3 werkbank.py lesen UE-0xx db.json` und `patch db.json e.json` → nur diesen `$set` senden.
   Wiederholen bis „Rest: 0“ und „Regeln: 0 Hinweise“ (bis auf „hidden false“, das kommt zuletzt).
4. `python3 werkbank.py blatt e.json` → EIN Bild mit 2D-Laufwegen und 3D aller Tafeln. Jeden Weg mit PDF/Video vergleichen.
5. Zum Schluss `$set {"hidden": false}` (zugleich das zweite Speichern). Dann `lesen` in `e2.json` und
   `vergleichen e.json e2.json` → „0 Abweichungen“.
6. (Nur bei Bedarf, siehe „Wenig Prüfläufe“) Prüfstand in der Sandbox, ein Aufruf für die ganze Woche:
   `run_command`: `nohup sh tools/pruefstand/alle.sh UE-0xx UE-0yy UE-0zz > /tmp/alle.log 2>&1 &`
   dann alle 3 bis 4 Minuten `grep -E "^(===|FEHLER|ALLES)" /tmp/alle.log` (sonst schläft die Sandbox ein und /tmp ist weg).
   Jede Zeile muss „PRÜFSTAND: ok“ haben. „viele lange Bilder“ direkt nach dem Aufwachen der Sandbox einmal wiederholen.
7. Live-Check einmal pro Woche: `NODE_PATH=$(npm root -g) node live.js wochen.png <id> <id> <id>` (EIN Kontaktbild: Kopf und
   9 Bilder der laufenden Story). Neue Einheiten stehen auf „abo“: für den Live-Check kurz auf „frei“, danach sofort zurück.
8. Schlusskarte „So läuft eine Runde“: In der App in `src/lib/runden.js` einen Eintrag für den neuen Code ergänzen
   (`ablauf`, `punkte` oder `ziel`, `wechsel`; kurze Sätze, „gibt einen Punkt“). Ohne Eintrag baut die Seite die Karte
   automatisch aus Beschreibung und Organisation, das ist aber schlechter. Prüfen: `node tools/pruefstand/schluss.mjs e.json`.
9. Der letzte Schritt der Grundform sagt immer, wie die Runde ausgeht (wer einen Punkt bekommt, Zeitlimit, wer gewinnt)
   und wer danach dran ist. Die Stimme liest genau die Schritt-Texte, was dort fehlt, fehlt auch in der Aufnahme.

## Bericht (kurz)
Je Einheit: Link `https://trainingskern.de/einheiten/<id>`, was vom Original abweicht, was nicht geprüft ist. Keine Tonspur aufnehmen.

## Was Tokens kostet (und was nicht)
- Teuer: ganze Einheiten in Tool-Aufrufen (deshalb nur einmal schreiben, danach `patch`), Bilder (nur die nötigen), `query_entities`
  mit ganzen Einheiten (stattdessen `werkbank.py lesen`).
- Kostenlos: `lesen`, `pruefen`, `vergleichen`, `patch`, Prüfstand-Lauf (nur das Log lesen).
- Nicht möglich: direkt per curl in die Datenbank schreiben (das App-Token zu holen ist in dieser Umgebung gesperrt). Schreiben nur mit
  `create_entities` und `update_entities`.
