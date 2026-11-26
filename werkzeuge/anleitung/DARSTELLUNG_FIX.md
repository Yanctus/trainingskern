# Auftrag: Darstellungsfehler in bestehenden Einheiten korrigieren (Inhaber, 26.11.2026)

Grundsatz des Inhabers: Bei schon eingesprochenen Einheiten nur ändern, was KEINE neue Aufnahme braucht. Alles, was eine neue
Aufnahme bräuchte, NICHT ändern, sondern melden (es kommt auf die Liste für das Neueinsprechen nach dem 22.12.).
Noch nicht eingesprochene Einheiten (hidden true, wartet_auf_ton true) dürfen vollständig korrigiert werden.

Deine Einheiten: dein Paket in werkzeuge/DARSTELLUNG_LISTE.md. Die genauen Meldungen je Einheit stehen in
werkzeuge/PRUEFUNG_ALLE.txt (Zeilen „Regel: UE-NNN …“ und Kollisionszeilen „UE-NNN Fassung | Schritt … | wer (art) | [Hindernis]“).

## Was gesprochen wird (darf bei eingesprochenen Einheiten NICHT geändert werden)
- `say_intro`, Fassungs-`say`, Schritt-`say`.
- Schritt-`label` NUR DANN, wenn der Schritt kein `say` hat (dann spricht die App das Label). Hat der Schritt ein `say`, ist das
  Label nur Bildschirmtext und darf gekürzt werden.
- `title` nur dann, wenn es kein `say_intro` gibt (dann spricht die App den Titel).
- Anzahl und Reihenfolge der Schritte und Fassungen.
Nicht gesprochen und frei änderbar: Positionen, Laufwege (`to`, `bend`, `delay`, `after`), `dims` (Maßlinien), `labels`
(Beschriftungen auf der Tafel), `field_size`, `coaching_points`, `organisation`, `description`, `materials`.

## Was zu tun ist
1. Kollisionen (Lauf oder Pass durch eine Figur): Laufweg mit `bend` um die Figur legen oder die Figur leicht versetzen.
2. „stehen zu dicht, verdecken sich in 3D“: Figuren in der Ausgangsstellung so versetzen, dass der Abstand reicht (regeln.py
   nennt die Grenzwerte), ohne den Sinn der Aufstellung zu ändern. Wartende Reihen notfalls auffächern.
3. Label zu lang (über 44 Zeichen): kürzen, nur wenn der Schritt ein `say` hat (sonst melden).
4. Beschriftung (`labels`) liegt auf einem Laufweg: verschieben, nicht über Figuren, ganz in der Tafel; im Zweifel weglassen.
5. Maßlinie außerhalb der Tafel: in die Tafel legen (x 0-100, y 0-60).
6. Nicht genau 4 Coaching-Punkte: auf 4 bringen (zusammenfassen oder aus dem Text der Einheit ergänzen), kurz, wie zugerufen.
7. Titel über 32 Zeichen: kürzen, nur wenn es ein `say_intro` gibt (sonst melden). Kein Wort über 14 Buchstaben, eindeutig
   (Titelliste: /tmp/claude-0/-home-user-trainingskern/717b55b0-9383-5e59-8671-45c768bc1d26/scratchpad/TITEL.txt).
8. „M“ Meterangaben: ab 20 m auf Fünfer runden (27 → 25, 46 → 45, 23 → 25), unter 20 m genau. In `field_size`, `dims`-Labels und
   in nicht gesprochenen Texten (organisation, description, coaching_points). Nennt ein gesprochener Text dieselbe Zahl (z. B.
   „sechsundvierzig Meter“), bei eingesprochenen Einheiten die Zahl NIRGENDS ändern und melden (Bild und Ton sollen gleich sein).
9. Sonstige Regelmeldungen: beheben, wenn es nichts Gesprochenes betrifft; sonst melden.

## Technik
- Quelle: Datenbank (`python3 werkbank.py lesen UE-NNN alt.json`), bei Einheiten mit `bau/ueNNN_quer.py` dieses Skript.
  Für U15 (UE-298+) `bau/ueNNN.py`.
- Hochladen nur per `mcp__Base44__update_entities` mit dem `$set` aus `python3 werkbank.py patch alt.json neu.json`
  (patch setzt weggefallene Felder auf null), query {"code": "UE-NNN"}.
- Prüfen: `lesen` + `vergleichen` 0 Abweichungen; `patch` gegen den neuen Datenbankstand = „keine Änderung“; `pruefen` (Ziel:
  0 Treffer, keine Hinweise mehr außer gemeldeten); `node passbahn.mjs /tmp/claude-0/pb.mjs …` 0 Treffer; `node blickpruefung.mjs
  /tmp/claude-0/pb.mjs …` nicht mehr Funde als vorher. Bei größeren Verschiebungen das Blatt ansehen.
- Eigener Arbeitsordner /tmp/claude-0/darstNN, nur diesen aufräumen. Nicht committen, runden.js/BERICHT.md nicht anfassen.

## Rückmeldung (Deutsch, knapp)
Je Einheit eine Zeile: was geändert, Prüfergebnis. Gesammelt am Ende: alles, was wegen Ton NICHT geändert wurde (Einheit, Stelle,
Grund), damit es auf die Liste für das Neueinsprechen kommt.
