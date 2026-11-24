# Auftrag: bestehende Übungen quer legen (Inhaber, 24.11.2026)

Projekt: Base44-App „Trainingskern“ (App-ID 6afec076c6c4a55a7cb4995e). Fußballübungen als Entität `Einheit` mit Tafel
(`board`, Raster 100 x 60), Fassungen (`versions`) und eingesprochener Tonspur. Werkzeuge im Repo `/home/user/trainingskern/werkzeuge`
(werkbank.py: lesen, pruefen, blatt, vergleichen, patch; bau/hilfe.py; regeln.py). Lies zuerst
`/home/user/trainingskern/werkzeuge/anleitung/AUFTRAG.md`, besonders die Abschnitte „Langes Feld QUER“ und „Großfeld QUER“,
und sieh dir die Vorbilder `werkzeuge/bau/ue317.py` (langes Feld quer, Umrechnung R()) und `werkzeuge/bau/ue319.py` an.

## Ziel
Die dir genannten Übungen haben ein langes Feld, das bisher hochkant oder gestaucht in der Mitte der Tafel steht. Lege sie quer:
lange Seite waagrecht, Feld füllt die Tafel (etwa x 9-89, y 4-51), Tore an den kurzen Seiten links/rechts, gleicher Maßstab in
beiden Richtungen soweit möglich. Alles muss mitgedreht werden: players, balls, cones (Formen leiter <-> leiter_ou, huerde <-> huerde_ou
tauschen!), goals (side top/bottom -> right/left usw.), lines (rect, line, zone, circle), labels, dims (neu setzen), alle moves
(`to`, `from`, `von`), auch in jeder Fassung (`versions[i].board`). Eine Drehung erhält den Drehsinn: `bend` und `drehen(gegen=...)`
bleiben, wie sie sind. Trainer unten an die Seitenlinie (y ca. 55), Ersatzbälle daneben.
Danach 3D-Abstand herstellen: Wer im Hochformat nebeneinander stand, steht jetzt hintereinander. Positionen in der Länge leicht
versetzen, bis `python3 werkbank.py pruefen <datei>` 0 Hinweise meldet. Pässe/Bälle, die bei einem Spieler enden (Spieler +0.6),
mit verschieben. Laufwege dürfen nicht durch Hütchen/Spieler gehen (pruefen meldet „Treffer“).

## Zwei Gruppen
- GRUPPE 1 (noch nicht eingesprochen, hidden + wartet_auf_ton): Hier hat das Bauskript `werkzeuge/bau/ueNNN.py` Vorrang. Skript
  quer umbauen wie ue317.py (R()-Umrechnung), Texte mit oben/unten/links/rechts anpassen (Sprechstil: Trainer am Platz, kurze Sätze,
  „Spieler sieben“, siehe AUFTRAG.md und anleitung/ZUSATZ_U15.md). Zustand bleibt hidden true + wartet_auf_ton true.
- GRUPPE 2 (schon eingesprochen!): KEIN Sprechtext darf sich ändern (`say`, `say_intro`, Fassungs-`say`, `text`, `label`,
  `title`), die Zahl und Reihenfolge der Schritte bleibt gleich, sonst passt die Tonspur nicht mehr. Nur Koordinaten, Linien, Tore,
  Hütchen, Maßlinien. Gibt es kein Bauskript, lies die Einheit mit `python3 werkbank.py lesen UE-NNN <datei>` und drehe das JSON
  mit einem eigenen kleinen Python-Skript (lege es als `werkzeuge/bau/ueNNN_quer.py` ab, Eingabe = gelesene Datei). Fällt dir beim
  Drehen ein Text auf, der danach nicht mehr stimmt (z. B. „nach links“), NICHT ändern, sondern im Bericht melden.

## Schreiben in die Datenbank
Nur mit dem Base44-MCP-Werkzeug `update_entities` (entityName "Einheit", query {"code": "UE-NNN"}, data {"$set": {...}}), nie per
curl. Sende `board` und `versions` ganz (bei Gruppe 1 dazu geänderte Textfelder wie organisation). Danach mit `werkbank.py lesen`
zurücklesen und `werkbank.py vergleichen <deine datei> <gelesene datei>` (0 Abweichungen). Bei Gruppe 2 zusätzlich prüfen, dass
alle say-Texte und das Feld `audio` unverändert sind (vorher/nachher vergleichen). Nichts veröffentlichen, nichts committen,
runden.js und BERICHT.md nicht anfassen. Kein Feld `hidden` bei Gruppe 2 ändern.

## Kontrolle
`python3 werkbank.py blatt <datei>` erzeugt `<datei>-blatt.png` (2D-Tafeln + 3D-Näherung). Ansehen: Feld füllt die Tafel, nichts
überdeckt sich, kein Text außerhalb. Aufräumen: Kontrolldateien löschen, nur `ueNNN-blatt.png` im Werkzeugordner lassen.

## Rückmeldung (knapp, deutsch)
Je Übung: was gedreht, welche Positionen versetzt, Ergebnis pruefen/vergleichen, bei Gruppe 2 „Texte und Ton unverändert“ und
Texte, die nach dem Drehen nicht mehr ganz stimmen. Probleme ehrlich nennen.
