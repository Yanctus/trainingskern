# Vertonung: was noch eingesprochen wird und wie (Stand 26.11.2026)

Eine Übersicht an einer Stelle. Die Einzellisten stehen in den genannten Dateien.
Die Zeichenzahlen sind grob geschätzt und überschneiden sich zum Teil (eine Einheit kann auf mehreren Listen stehen).

## A. Jetzt einsprechen (noch nie vertont, braucht nur Guthaben)
| Was | Umfang |
|---|---|
| Plan U15-U17: UE-298 bis UE-418 (119 Einheiten, ohne UE-407 und UE-413) | zusammen mit Zeile 2 etwa 1.750 Sätze, 237.000 Zeichen |
| Taktik-Erklärungen TA-003 bis TA-006 (4-4-2, 3-5-2, 3-4-3, 4-1-4-1) | in der Zahl oben enthalten |

- Alle stehen auf `hidden: true` + `wartet_auf_ton: true`. Die Texte sind fertig und geprüft (0 Kollisionen, 0 Regel-Hinweise).
- **So:** Im Katalog als Admin den Sammel-Knopf „Alle fehlenden einsprechen“ (nimmt nur Sätze ohne jede Aufnahme) oder auf der
  Einheit-Seite den Knopf für diese Einheit. Sobald jeder Satz eine Aufnahme hat, setzt die App `hidden: false` von selbst.
- **Danach:** `python3 tonpruefung.py <Codes>` (findet Fehlerlaute von ElevenLabs am Satzende, wie bei TA-002 nach „Stürmer“).
  Verdacht mit faster-whisper gegenhören. Fehlerhafte Sätze markieren (anleitung/TAKTIK.md, Abschnitt „Nach dem Einsprechen“),
  dann nimmt „Geänderte neu einsprechen“ nur diese Sätze neu auf.

## B. Nach dem 22.12.2026 neu einsprechen (schon vertont, Ton passt nicht mehr ganz)
Am besten **pro Einheit in einem Zug**: erst alle Text- und Bildänderungen dieser Einheit machen (b bis f), dann einmal
„Geänderte neu einsprechen“. So wird keine Einheit zweimal aufgenommen.

| | Was | Umfang | Texte schon fertig? | Liste |
|---|---|---|---|---|
| a | „Neon sieben“ → „Spieler sieben“ | 119 Einheiten, etwa 940 Sätze, 121.000 Zeichen | ja, nur Knopf drücken | NEU_EINSPRECHEN.md |
| b | Lange Felder quer legen (Gruppe 3) | 48 Einheiten, etwa 230 Sätze, 32.000 Zeichen | nein, erst umbauen (anleitung/QUER.md) | OFFEN.md, Tabelle |
| c | Halbes Feld quer: UE-140, UE-141, UE-234 | 3 Einheiten | nein, erst umbauen (AUFTRAG.md „Halbes Feld QUER“) | OFFEN.md |
| d | UE-229 Dreiviertelfeld als „Großfeld quer“ | 1 Einheit | nein, erst umbauen | OFFEN.md |
| e | Sichtkegel nach der neuen Regel | 73 Kegel in 48 Einheiten, etwa 10.000 Zeichen | nein, erst umbauen (anleitung/BLICK_FIX.md) | BLICK_FIX_LISTE.md „Später“ |
| f | Darstellung mit Tonbezug | einzelne Sätze, meist Fehlalarme der Prüfung | nein | DARSTELLUNG_LISTE.md „Später“ |

Zu f: UE-001 hat in der Grundform 9 Schritte (erlaubt 3 bis 6). Bei UE-046 steht „gezielt“ im Ton. UE-020 und UE-046 behalten ihre
doppelten Rückennummern, weil sie zur Übung gehören. Die Meldungen „Ergebnis als Satz sprechen“ bei UE-005, 012, 018, 029, 031,
038, 039 und 042 sind Fehlalarme: Der Satz endet nur auf „Tor.“ oder „Punkt.“. Nur neu einsprechen, wenn die Einheit ohnehin
dran ist.

Grob zusammen für B: etwa 165.000 Zeichen, A und B zusammen etwa 400.000 Zeichen.

## C. Regeln für alles, was gesprochen wird
- Ein einzelner Spieler heißt „Spieler sieben“, nie „Neon sieben“. Mannschaften heißen „Team Neon“ und „Team Rot“.
  Ergebnisse sprechen wir als ganzen Satz: „das gibt einen Punkt für Team Neon“. Beim Fangspiel heißt es „fangen“, nicht „abschlagen“.
- Sprechen wie ein Trainer am Platz: kurze Sätze, keine Floskeln, keine Gedankenstriche, Zahlen ausgeschrieben
  (anleitung/AUFTRAG.md, anleitung/ZUSATZ_U15.md).
- Meter: ab 20 m auf Fünfer gerundet, unter 20 m genau, und Bild und Ton nennen dieselbe Zahl.
- Taktik (anleitung/TAKTIK.md): „Einer kommt, einer geht“ höchstens zweimal pro Video sagen. Der Text eines Schritts beschreibt
  nur, was in diesem Schritt zu sehen ist (Timing).
- Die Stimme bleibt bei der bewährten Einstellung (stability 0.5, similarity 0.8). Standard ist „am Stück“, dabei bekommt jeder
  Satz die Kennungen der drei Sätze davor mit. Nicht an style, previous_text oder next_text drehen, ohne vorher eine einzelne
  Einheit Probe zu hören (README der App, „Am Stück einsprechen“).
- Geänderte Sätze immer ganz neu einsprechen. Kein Wort vor eine fertige Aufnahme schneiden, das klingt abgehackt.
