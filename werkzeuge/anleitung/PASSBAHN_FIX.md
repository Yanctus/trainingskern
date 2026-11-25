# Auftrag: Pässe durch einen Gegenspieler korrigieren (Inhaber, 25.11.2026)

In manchen Einheiten steht ein Gegenspieler beim Pass genau in der Passbahn, der Ball fliegt aber trotzdem durch ihn hindurch.
Das sieht falsch aus. Die Liste steht in `werkzeuge/PASSBAHN.md` (Code, Fassung, Schritt, Passgeber → Empfänger, Gegner).
Gefunden mit `werkzeuge/passbahn.mjs`, das den echten Abspielcode der App nutzt (gebündelt unter /tmp/claude-0/pb.mjs).

## Ziel
Danach steht bei keinem dieser Pässe ein Gegner näher als etwa 3 Einheiten an der Passbahn, und der Ball fliegt nicht durch ihn.
Der Ablauf der Übung bleibt gleich: gleiche Schritte, gleiche Reihenfolge, gleiche Pässe, gleiche Sprechtexte.

## So korrigieren (kleinster Eingriff zuerst)
1. Den Gegenspieler ein paar Einheiten zur Seite stellen (Startposition in `players` oder sein Laufziel `to` im Schritt davor),
   so dass er neben der Passbahn steht und trotzdem plausibel verteidigt (zum Ball schieben, Passweg nicht frei schenken).
2. Oder den Laufweg/Laufbeginn des Gegners so ändern, dass er erst nach dem Pass ankommt (`delay`).
3. Oder den Empfänger etwas weiter freilaufen lassen bzw. den Pass mit `bend` leicht um den Gegner herum legen.
4. Ist der Pass absichtlich zugestellt (der Text sagt, der Weg ist zu, oder der Ball soll abgefangen werden) oder ist es ein
   Torschuss am Verteidiger vorbei: nicht ändern, im Bericht als „gewollt“ melden.

## Regeln
- **Eingesprochene Einheiten (hidden false):** Sprechtexte (`say`, `say_intro`, Fassungs-`say`), Anzahl und Reihenfolge der
  Schritte NICHT ändern, die Aufnahme muss weiter passen. Nur Koordinaten, `delay`, `bend`. Passt ein gesprochener Satz dann
  nicht mehr (z. B. „der Verteidiger steht im Passweg“), nichts ändern und melden.
- **Nicht eingesprochene (hidden true, wartet_auf_ton true):** wie oben, Texte dürfen aber angepasst werden, wenn nötig.
- Quelle: Für U9-U14-Einheiten ist die Datenbank maßgeblich (`python3 werkbank.py lesen UE-NNN alt.json`). Gibt es
  `bau/ueNNN_quer.py`, ist dieses Skript maßgeblich: dort ändern, bauen, und nur den Unterschied hochladen. Bei U15-Einheiten
  (UE-298 bis UE-418) ist `bau/ueNNN.py` maßgeblich: dort ändern, neu bauen.
- Hochladen nur per `mcp__Base44__update_entities` mit `$set` (query {"code": "UE-NNN"}). Den Unterschied mit
  `python3 werkbank.py patch alt.json neu.json` erzeugen und genau diesen `$set` übergeben (nicht abtippen).
- Prüfen danach: `python3 werkbank.py lesen UE-NNN neu_db.json`, `python3 werkbank.py vergleichen neu.json neu_db.json`
  (0 Abweichungen), `python3 werkbank.py pruefen neu_db.json` (0 Treffer, 0 Hinweise; bei alten Einheiten höchstens die
  Hinweise, die vorher schon da waren), `node passbahn.mjs /tmp/claude-0/pb.mjs neu_db.json /tmp/x.json` (keine Treffer mehr,
  außer als gewollt gemeldete). `python3 werkbank.py blatt neu_db.json` ansehen.
- Nicht committen, runden.js und BERICHT.md nicht anfassen, keine anderen Einheiten anfassen. Kontrolldateien aufräumen.

## Rückmeldung (Deutsch, knapp)
Je Einheit eine Zeile: was geändert wurde (wer, wohin), Prüfergebnis, oder „gewollt, nicht geändert“ mit Grund.
