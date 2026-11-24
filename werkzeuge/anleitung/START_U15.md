# Start für Agenten, Plan U15-U17

Lies zuerst vollständig, in dieser Reihenfolge, und halte dich genau daran:
1. /home/user/trainingskern/werkzeuge/anleitung/AUFTRAG.md
2. /home/user/trainingskern/werkzeuge/anleitung/ZUSATZ_U15.md (geht bei Widerspruch vor; dort steht u. a.: Einheit bleibt
   ausgeblendet mit hidden true + wartet_auf_ton true, Annehmen/Aufdrehen mit bl(von=...) und drehen(), Meter runden,
   Sprechtexte wie ein Trainer am Platz, Texte auf der Tafel sauber)
3. /home/user/trainingskern/werkzeuge/bau/hilfe.py und als Vorbilder bau/ue298.py, bau/ue299.py, bau/ue300.py,
   bei Großfeld bau/ue319.py, bei langem Feld bau/ue317.py

Wo AUFTRAG.md auf „werkzeuge/anleitung/TITEL.txt“ verweist: Die Titelliste liegt unter
/tmp/claude-0/-home-user-trainingskern/717b55b0-9383-5e59-8671-45c768bc1d26/scratchpad/TITEL.txt (alle Einheiten mit Code). Keinen
Titel doppelt vergeben; parallel bauen andere Agenten weitere Codes, also konkrete, unterscheidbare Titel wählen.

Rohdaten: /home/user/trainingskern/werkzeuge/import/<Woche>/<Übung>/. In manchen Wochenordnern liegen auch Übungen des
U12-Plans: nur die dir genannten bearbeiten. ton.txt fehlt: `TK_PLAN=u15 python3 werkbank.py ton "<Ordner>"`.

Dubletten: Wenn dir eine Übung bekannt vorkommt (Titelliste, BERICHT.md), mit `python3 werkbank.py lesen UE-xxx /tmp/claude-0/x.json`
vergleichen. Nur bei gleicher Organisation UND gleichen Abläufen: nicht neu bauen, sondern update_entities {"code":"UE-xxx"} mit
{"$addToSet":{"altersbereiche":"U15-U17"}} und melden (Code bleibt frei).

Werkzeuge: mcp__Base44__create_entities und mcp__Base44__update_entities (appId 6afec076c6c4a55a7cb4995e, entityName Einheit).
Fehlen sie, sofort abbrechen und melden (kein curl-Schreiben, kein Token holen). $set-Text unverändert übergeben.
Bei „Rate limited“ warten und wiederholen. Nicht committen, runden.js und BERICHT.md nicht anfassen.

Rückmeldung am Ende, auf Deutsch, knapp: je Übung die Bericht-Zeile und die runden.js-Zeile (Formate wie in AUFTRAG.md),
Prüfergebnis (vergleichen/pruefen), und nur echte Probleme oder Annahmen. Die say-Texte NICHT auflisten.
Kontrollbilder außer ueNNN-blatt.png löschen, eigene szene-*.png auch.
