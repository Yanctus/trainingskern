# Zusatz für den Plan U15-U17 (gilt zusätzlich zu AUFTRAG.md, geht bei Widerspruch vor)

## Plan
- Überall `TK_PLAN=u15` setzen (liste, holen, ton). `vorgaben` NICHT für die Altersstufen benutzen:
  `age_groups` ist immer `["C-Jugend", "B-Jugend"]`, `altersbereiche` immer `["U15-U17"]`.
  `duration_minutes`: Warm Up / WU 10, sonst 15 (Pre-Season-Zirkel 15).
- Quelle im Bericht: „(U15-U17, Woche X)“. Übungen aus Pre-Season-Wochen bekommen `"tags": ["Vorbereitung"]`.
- Im Ordner `import/Week 1 - Pre-Season/` liegen auch Übungen des U12-Plans; nur die dir genannte Übung bearbeiten.

## Texte auf der Tafel (Inhaber: „Texte müssen richtig drin stehen, nicht drüber“)
- Step-`label` höchstens 44 Zeichen, damit es im Bild nicht umbricht oder abgeschnitten wird. Fassungs-`title` höchstens 28 Zeichen.
- Keine freien Beschriftungen (`labels`) auf der Tafel, die über Figuren, Hütchen oder Laufwegen liegen. Im Zweifel keine labels.
- Maßlinien (`dims`) müssen ganz innerhalb der Tafel liegen (x 0-100, y 0-60), Feld so legen, dass rechts und unten Platz bleibt.
- Auf dem Blatt (`blatt`) prüfen: nichts überdeckt sich, kein Text läuft aus dem Bild.

## Sprechtexte: wie ein Trainer am Platz, nicht wie ein Lehrbuch und nicht wie KI
Die `say`-Texte werden mit der Stimme des Inhabers vertont. Sie müssen sich anhören, als erklärt er die Übung seinen
Trainerkollegen am Spielfeldrand.
- Kurze, gesprochene Sätze. Aktiv, Präsens. Ein Gedanke pro Satz. Satzlängen mischen.
- Konkretes sagen, was man sieht: wer, wohin, womit. Keine Floskeln und keine leeren Wertungen
  („entscheidend“, „wichtig ist“, „dabei gilt“, „es geht darum“, „so entsteht“, „optimal“, „effektiv“, „gezielt“).
- Keine Aufzählungen im Dreierpack als Stilmittel, keine Doppelpunkte-Konstruktionen als Dauerform, keine Gedankenstriche.
- Nicht jeden Satz gleich bauen („Spieler X macht …, Spieler Y macht …“ fünfmal hintereinander klingt nach Maschine).
  Abwechseln: mal mit dem Ball anfangen, mal mit dem Ort, mal mit „Jetzt“, „Sofort“, „Dann“.
- Keine englischen Fachwörter, wenn es ein deutsches gibt. Zahlen ausschreiben.
- Coaching-Punkte so, wie man sie zuruft: „Kopf hoch vor dem Pass“, nicht „Auf die Vororientierung achten“.
- Die festen Regeln bleiben: „Spieler sieben“ (nie Farbe + Zahl), „das gibt einen Punkt für Team Neon“, fangen statt
  abschlagen, letzter Grundform-Schritt sagt Ergebnis und wer dran ist, feste say-Anfänge der Fassungen.
- Laut lesen (im Kopf): Stolpert man, umschreiben.

## Niveau
U15-U17 ist älter als bisher: Sprache nicht kindlich („die Kinder“ vermeiden, stattdessen „die Spieler“), aber weiter einfach.

## Geräte
Leitern `leiter(...)`, Ringe `ring(...)`, nie Hürden als Ersatz. Klassen/Formen nicht neu erfinden.

## Neue Einheiten bleiben ausgeblendet, bis sie eingesprochen sind (Inhaber, 24.11.2026)
- Schritt 5c aus AUFTRAG.md ENTFÄLLT: Die Einheit wird NICHT sichtbar geschaltet. Endzustand in der Datenbank und im
  Bauskript: `"hidden": True, "wartet_auf_ton": True` (beides schon im $set bzw. beim Anlegen mitgeben).
  Die App blendet die Einheit von selbst ein, sobald der Inhaber alle Sätze eingesprochen hat.
- `pruefen` akzeptiert hidden true nur zusammen mit wartet_auf_ton true. `vergleichen` wie gehabt (0 Abweichungen).
- Der Link im Bericht bleibt gleich (https://trainingskern.de/einheiten/<id>), er funktioniert erst nach dem Einsprechen.

## Annehmen und Aufdrehen (Inhaber, 24.11.2026, mit UE-300 abgenommen; Vorbild: bau/ue300.py)
- Schritt A: Der Spieler schaut zum Passgeber: `bl(who, <Passgeber>)`, dann der Pass zu ihm (`ps(..., after=True)`).
- Schritt B (erst NACH der Annahme): `bl(who, <Passziel>, von=<Passgeber>, dauer=1.3)` (derselbe Kegel schwenkt zum Passziel und
  bleibt dort mittig stehen), dazu `drehen(who, <Passziel>, delay=0.4)` (Drehpfeil, er dreht auf der Stelle; `gegen=True` =
  gegen den Uhrzeigersinn), danach sein Pass (`ps(..., after=True)`).
- Nie zwei Kegel hintereinander für denselben Spieler, nie den Kegel fürs Aufdrehen.

## Meterangaben
Unter 20 m genau, ab 20 m auf Fünferschritte runden (27 -> 25, 36 -> 35), in field_size, dims und allen Texten.

## Großfeld quer (Inhaber, 24.11.2026, mit UE-319 abgenommen)
Ganzer Platz oder Dreiviertelfeld: Feld quer wie im Fernsehbild, Tore links/rechts, echte Platzlinien, `"massstab": "gross"` im
Haupt-board, nur die Längen-Maßlinie. Einzelheiten in AUFTRAG.md („Großfeld QUER“), Vorbild bau/ue319.py.

## Halbes Feld quer (Inhaber, 25.11.2026, Vorbild bau/ue352.py)
Platzhälfte (oder ein Stück davon mit echtem Strafraum): wie im Fernsehbild, großes Tor rechts, Platzbreite von oben nach unten,
Mittellinie links, echte Linien der Hälfte (Strafraum, Torraum, Strafraumbogen, halber Mittelkreis), `"massstab": "gross"`.
Abbildung und Linien nur mit `bau/halbfeld.py` (`F = hf.Halbfeld(tief, breit)`, `F(d, q)` in Metern, `F.linien()`, `F.tor()`,
`F.minitore(...)`, alte Skripte mit `F.von_hochkant(...)` + `hf.umrechnen(R)`). Richtungswörter in allen Texten anpassen
(„vorn“, „an der Mittellinie“, „auf der anderen Seite“ statt oben/unten/links/rechts). Einzelheiten in AUFTRAG.md
(„Halbes Feld QUER“).
