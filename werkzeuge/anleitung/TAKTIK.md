# Anleitung: Taktik-Erklärungen (Spielsysteme), Stand 24.11.2026, vom Inhaber mit TA-001 abgenommen

Projekt: Base44-App „Trainingskern“ (App-ID 6afec076c6c4a55a7cb4995e). Eine Taktik-Erklärung ist eine Einheit mit
`kind: "Taktik"`: ein animiertes, eingesprochenes „Video“, das ein Spielsystem erklärt (wer steht wo, wie bewegen sich alle,
welche Muster gibt es). Sie kommt nie in Trainingspläne. Im Katalog unter „Spielsysteme“.

**Vorbild ist TA-001 „Aufbau im 4-3-3 über den Torwart“:** `werkzeuge/bau/ta001.py`. Lies es ganz, bevor du anfängst.
Gemeinsame Bauhilfe: `werkzeuge/bau/taktik.py` (Großfeld quer, Klasse `Lage` mit allen Prüfungen, `fertig()`).
Weitere Regeln, die immer gelten: `werkzeuge/anleitung/AUFTRAG.md` (Schema, Sprechstil, Schreiben in die Datenbank).

## Die elf Regeln (Inhaber, 24.11.2026)
1. **Ganzer Platz quer** (Großfeld wie TA-001: Tore links/rechts, echte Linien, `"massstab": "gross"`, nur die Maßlinie „100 m“).
   Vier Kapitel: Grundform = Kapitel 1, dazu genau drei Fassungen mit `label` „Kapitel 2“, „Kapitel 3“, „Kapitel 4“ und `say`
   „Kapitel zwei: …“, „Kapitel drei: …“, „Kapitel vier: …“. Grundform 3-7 Schritte, jede Fassung 2-6 Schritte.
2. **Alle bewegen sich mit dem Ball:** Bei jedem Pass verschieben beide Mannschaften (`Lage.schieb`). Wer weit weg vom Ball ist,
   bleibt breit. Nie stehen zehn Spieler still, während einer passt.
3. **Vor jedem Pass zwei bis vier Anspielstationen** (`Lage.opts`, dünne Pfeile), dann der Pass und im Text die Begründung
   („… ist frei, also …“).
4. **Wer angespielt wird, hat sich freigelaufen:** mindestens `FREI` (7 Einheiten, etwa 8 m) zum nächsten Gegner beim Abspiel.
   Gegner laufen den Empfänger erst an, wenn der Ball unterwegs ist (Verschieben mit `delay` nach dem Pass).
5. **Einer kommt, einer geht:** Kommt einer zum Ball, geht im selben Moment ein anderer weg (in die Tiefe, in den frei gewordenen
   Raum). In jedem Kapitel mindestens einmal **zeigen**, aber die Formel „Einer kommt, einer geht“ im ganzen Video **höchstens
   zweimal sagen** (Inhaber, 24.11.2026: „man sieht das ja selbst anhand der Bewegung“). Sonst nur beschreiben, wer kommt und wer
   geht („Der Flügel kommt nach innen. Dafür geht der Außenverteidiger die Linie hoch.“). Ein Kapiteltitel mit der Formel zählt mit.
   In geschriebenen Feldern (organisation, coaching_points, Kapiteltitel ohne say) darf sie stehen.
6. **Muster** (passend zum System auswählen): innen-außen und außen-innen; eine Reihe überspielen, klatschen lassen, verlagern;
   dritter Mann; freier Mann durch Andribbeln und Locken; Seitenwechsel über den Torwart; Überzahl in der ersten Aufbaulinie.
7. **Gegner realistisch:** presst, schiebt zum Ball, stellt mit Deckungsschatten zu, kommt beim Verlagern zu spät. Er steht nie
   zufällig im Passweg; wenn ein Weg zu ist, dann weil er ihn zustellt, und das wird gesagt.
8. **Sprache wie ein Trainer am Platz, natürlich gesprochen** (siehe Sprechstil unten). Positionen statt Nummern.
9. **Kein Abseits:** Beim Pass steht niemand von Team Neon im Abseits (`Lage.abseits` prüft bei jedem `pas`). Tiefenläufe starten
   mit dem Pass (`Lage.steil`: Läufer steht beim Abspiel auf Höhe, Lauf und Ball starten zusammen).
10. **Jeder Pass geht durch eine Lücke:** Kein Gegner näher als `GASSE` (4,5 Einheiten) an der Passbahn (`Lage.gasse` bei `pas`,
    `steil` und `opts`). Absichtlich zugestellte Anspielstationen tragen `zu=("n7",)` und der Text sagt, dass sie zu sind.
11. **Text und Bild passen zusammen (Timing):** Der `say` eines Schritts beschreibt nur, was in genau diesem Schritt auf dem Feld
    passiert, in der Reihenfolge, in der es passiert. Nichts ankündigen, was erst im nächsten Schritt kommt, nichts nacherzählen,
    was schon vorbei ist. Wird ein Lauf erwähnt, läuft er in diesem Schritt. So läuft es ab: Die Bewegungen starten mit dem Schritt,
    die Stimme spricht dazu, und am Ende des Schritts wartet das Bild, bis der Satz fertig ist. Grob: etwa 17 Zeichen pro Sekunde
    Sprechzeit. Ist der Text viel länger als die Bewegungen, steht das Feld lange still, während noch erzählt wird: dann den
    Schritt teilen oder die Bewegungen mit `delay` später starten lassen, damit sie zum gesprochenen Satz passen.

## Technik
- Kopf des Skripts: `import json, sys; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from hilfe import *; from taktik import *`
- Positionen als Dicts (`"n5": (x, y)`), Team Neon `n…` (team a), Team Rot `r12`-`r21` (team b), Torhüter neutral `k1` (links,
  unser Torwart) und `k2` (rechts). Rückennummern eindeutig über beide Teams. Ein Trainer `T` (aus taktik.py).
- Feld x 7-91, y 3-52, Mitte (49, 27.5). Strafraum links x 7-21, y 12-43. Neon greift nach rechts an: oben = linke Seite.
- 3D-Abstand beim Großfeld (massstab gross): Zwei Figuren in derselben Ausgangsstellung brauchen |dx| ≥ 5,9 ODER |dy| ≥ 11,2.
  `python3 werkbank.py pruefen` meldet es. Spieler einer Kette stehen quer hintereinander: in der Tiefe weit genug auseinander.
- Am Ende des Skripts `fertig()` aufrufen und dann `json.dump(...)`. Das Skript darf **keine** „TAKTIK:“-Zeile ausgeben.
- Prüfen: `python3 bau/taNNN.py /tmp/…/taNNN.json` (keine TAKTIK-Zeilen), `python3 werkbank.py pruefen <datei>` (0 Treffer,
  0 Hinweise), `python3 werkbank.py blatt <datei>` und das Blatt ansehen (Laufwege sinnvoll, nichts überdeckt).
- Kein Pass, kein Laufweg durch einen Spieler (pruefen „Treffer“). Laufwege, die eng an Gegnern vorbeigehen, umlegen.

## Pflichtfelder der Einheit
`title` (höchstens 32 Zeichen, kein Wort über 14 Buchstaben, eindeutig, z. B. „Aufbau im 4-2-3-1“), `code` (dir genannt, TA-00N),
`kind: "Taktik"`, `focuses` (2-3 aus der festen Liste, z. B. "Passspiel", "Zusammenspiel", "Verteidigen", "Umschalten"),
`age_groups: ["D-Jugend", "C-Jugend", "B-Jugend"]`, `altersbereiche: ["U12-U14", "U15-U17"]`, `duration_minutes` 4-6,
`players_min/max: 22`, `field_size: "65 x 100 m"`, `description` (3-4 Sätze), `organisation` (genau 4 „Stichwort: Satz“, z. B.
Grundordnung/Hinten/Mittelfeld/Bewegung), `organisation_show: ORG`, `coaching_points` (genau 4, kurz, wie zugerufen),
`materials` (z. B. Großfeld mit zwei Toren, Leibchen in zwei Farben, Bälle), `access: "abo"`, `hidden: True`,
`wartet_auf_ton: True`, `say_intro`, `board` (Kapitel 1), `versions` (Kapitel 2-4).

## Sprechstil (so klingt es, als hätte ein Mensch es eingesprochen)
Wie in TA-001 nach der Überarbeitung: kurze Sätze, gesprochene Formen („gibt's“, „wird's“, „kriegt er ihn“, „übers Feld“,
„die Linie runter“), direkte Ansprache („Jetzt schau auf den Torwart.“, „Und jetzt pass auf: …“), kleine Rückfragen
(„Und der Flügel? Der ist schon unterwegs.“), Übergänge („Neue Situation.“, „Jetzt wird's ernst.“). Systeme ausschreiben:
„Vier-zwei-drei-eins“. Keine Ziffern, keine Floskeln („entscheidend“, „wichtig ist“, „es geht darum“, „dabei gilt“, „optimal“,
„effektiv“, „gezielt“), keine Gedankenstriche, keine Aufzählungs-Dreierpacks als Stilmittel. Positionen deutsch: Innenverteidiger,
Außenverteidiger, Sechser, Doppelsechs, Achter, Zehner, Flügelspieler, Schienenspieler, Stürmer, Torwart.

## In die Datenbank
Nur mit den Base44-MCP-Werkzeugen: erst `create_entities` (Einheit, klein: title, code, kind, duration_minutes, access, hidden
true, wartet_auf_ton true), dann `update_entities` mit `{"$set": {...alle übrigen Felder...}}` (query {"code": "TA-00N"}).
Danach `python3 werkbank.py lesen TA-00N <datei>` und `python3 werkbank.py vergleichen <deine datei> <gelesene datei>`
(0 Abweichungen). Nichts veröffentlichen, nichts committen, keine anderen Einheiten anfassen, runden.js/BERICHT.md nicht anfassen.
Bauskript als `werkzeuge/bau/taNNN.py` ablegen, Kontrollbild `werkzeuge/taNNN-blatt.png` liegen lassen, Rest aufräumen.

## Nach dem Einsprechen (Inhaber, 24.11.2026)
`python3 tonpruefung.py TA-00N` sucht Fehlerlaute von ElevenLabs am Satzende (Pause, dann noch ein kurzer Laut; so bei TA-002
Kapitel 1 Schritt 1 nach „Stürmer“). Verdacht mit faster-whisper gegenhören: Ist der Laut das letzte Wort, ist alles gut. Sonst
`audio.chapters.<k>.steps_text.<s>` per $set auf einen Hinweistext setzen, dann nimmt „Geänderte neu einsprechen“ den Satz neu auf.
