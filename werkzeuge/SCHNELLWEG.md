# Schnellweg: Woche für Woche Übungen nachbauen (Stand 21.11.2026)

Ziel: alle restlichen Wochen (21 bis 42) nacheinander, richtig, geprüft und mit wenig Tokens. Diese Werkzeuge liegen im GitHub-Repo
(`werkzeuge/`) und sind in jeder neuen Sitzung sofort da, ohne sie aus der App zu kopieren. Maßgeblich für Regeln und Tafel bleibt die
README der App (Abschnitte „Übungen aus Video nachbauen“, „Laufweg-Abgleich“, „Prüfliste“). Pro Chat 2 Wochen, dann neuen Chat starten.

## Einmal pro Sitzung
- `base44_readme` aufrufen. Werkzeuge: `cd werkzeuge` (liegt im Repo). Nichts aus der App kopieren.
- Nächsten Code holen: `python3 werkbank.py lesen UE-0xx x.json` zum Prüfen, ob ein Code schon belegt ist (siehe README der App: „nächster Code“).

## Pro Woche
1. `python3 werkbank.py holen <Woche>` (Video, PDF, Text, Übersicht).
2. `python3 werkbank.py ton <Ordner>` für jede Übung (Spracherkennung, ca. 10 s, einmalig `pip install faster-whisper`): Die gesprochene
   Erklärung steht dann mit Zeitstempeln in `ton.txt`. Zuerst `text.txt` und `ton.txt` lesen (kostet fast nichts), dann ansehen
   (sparsam, jedes Bild kostet): `pdf-1.png`, `pdf-2.png`, `uebersicht.png`.
   Dann gezielt `szene <Ordner> <von> <bis>` nur für die Abschnitte mit Laufwegen (Grundform, jede Fassung). Abschnitte aus der
   Übersicht ablesen: Bild n (ab 0) liegt bei n × Dauer/25 Sekunden.
3. Pro Schritt notieren: wer, von wo, über welche Zwischenpunkte, welche Seite, wann (vor/nach dem Pass), wohin der Pass.
4. `python3 werkbank.py vorgaben "<Übungsname>"` für Altersstufen und Dauer (stehen nicht im PDF; feste Regel).

## Feste Regeln (vom Inhaber, 21.11.2026)
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
- **Neue Einheiten gleich `access: "frei"`**, der Inhaber stellt am Ende alle auf Pro.
- **Wenig Prüfläufe:** kostenlos und immer: `pruefen`, `blatt`, `vergleichen`. Prüfstand nur nach Änderungen am Player-Code oder wenn
  das Blatt etwas Seltsames zeigt (dann nur Chromium). Live-Check einmal pro Woche mit `live.js` (Einheiten sind ja frei).

## Feste Begriffe (vom Inhaber)
- **Springer sind immer neutrale Spieler:** `team: "t"`, Label „F“, spielen für das Team in Ballbesitz, im Text „Springer“.
- Einheiten dürfen zum Live-Check kurz auf „frei“, danach sofort zurück auf „abo“.
- Altersstufen, Dauer und Spielerzahl stehen nicht im PDF: `vorgaben` benutzen, Spielerzahl aus der Skizze.
- Fassungen dürfen Linien ergänzen (z. B. Hälften in einer Steigerung): dann alle Linien der Grundform mit übernehmen.

## Pro Einheit (JSON nur EINMAL schreiben)
Einheit als kleines Python-Skript in `werkzeuge/bau/ue0xx.py` bauen (Bausteine in `bau/hilfe.py`, Vorbild `bau/ue061.py` bis `ue063.py`),
`python3 bau/ue0xx.py e.json`, dann:
1. `create_entities` klein: `{"code","title","kind","duration_minutes","hidden":true,"access":"frei"}` (Antwort ist klein).
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
   9 Bilder der laufenden Story). Neue Einheiten stehen auf „frei“, daher ohne Umstellen.
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
