# Trainingskern

Die App selbst liegt bei Base44 (App „Trainingskern“), dieses Repo enthält das Marketing-Werkzeug.

## Feste Vorgaben für alles, was nach außen geht

- Die Adresse ist immer **trainingskern.de** (nie die base44.app-Adresse), in Videos, Texten und Aufrufen.
- Trainingskern gibt es (noch) nicht im App-Store, nur online unter trainingskern.de. Nichts schreiben, das nach Store-App klingt
  („Echte App“, „Jetzt laden“). Der Stempel auf dem Bildschirm heißt „Deutsches Audio“.
- Keine Zahl der Übungen nennen. Geworben wird mit dem Nutzen: jede Übung animiert und eingesprochen, fertige Trainingspläne.
- Instagram-Konto: @trainingskern. Nichts veröffentlichen ohne ausdrückliches Okay.
- Intros und Grafik im Stil der App (Papier, Tafel, Neon und Orange auf Schwarz), nicht als Realfilm.
- Keine generierten Kindergesichter, keine fremden Markenlogos in Clips.

## Kampagnen-Videos

- Jedes Video beginnt mit demselben Intro, nur der Text wechselt: ein gezeichnetes Comic-Intro (Cel-Shading, dicke Konturen) mit freier Fläche,
  `hook` mit `"film": "comic-..."`. Welche Variante das feste Intro wird, ist noch offen (Auswahl: `story-studio/stories/comic-vergleich.json`).
  Das Intro muss sich klar vom Outro unterscheiden; `hook-zettel` ist deshalb verworfen.
- Zwei Stilrichtungen stehen zur Wahl: Comic (`comic-*`, Outro `outro-comic`) und Zeichentrick der 30er (`cartoon-*`, Outro `outro-cartoon`,
  Übergänge `iris` und `tinte`). Figuren sind immer eigene; nie bestehende Figuren oder Namen fremder Marken in Bildaufträgen oder Werbetexten.
- Bilder für neue Intros: Nano Banana, Animation über Start- und Endbild (beides über OpenRouter). Keine Drei-Streifen-Kleidung, keine Logos.
- **Entschieden (23.11.2026): Die Videos laufen im Comic-Stil** (`comic-*`, Outro `"film": "outro-comic"`, Übergänge `knall`, `pinsel`,
  `raster`, `panel`, Musik `ton/musik-elektro.mp3`). Der Zeichentrick-Stil (`cartoon-*`) bleibt im Repo, wird aber vorerst nicht genutzt.
- Fertige Muster: `kampagne-01-kein-plan-comic.json` (Frage und Antwort), `kampagne-02-aufbau-rondo.json` (nur der Aufbau einer Übung, Szene `aufbau`),
  `kampagne-03-uebung-rondo.json` (Übung erklärt mit den Aufnahmen der Seite, `"stimme": true`), alle in `story-studio/stories/`.
- Für erklärte Übungen die vorhandenen Aufnahmen der Seite nehmen (kosten kein ElevenLabs-Kontingent). Der Aufbau hat auf der Seite keine
  Aufnahmen und wird neu eingesprochen. Jedes Video höchstens 30 Sekunden einschließlich Outro.
- Format der weiteren Videos: eines der sieben Comic-Intros mit Frage, Übergang, dann eine Übung, die erklärt wird (Szene `uebung` mit
  `sprecher`), höchstens 30 Sekunden, dann `blende` ins Outro.
- Jedes Video endet mit demselben Outro: `{ "typ": "outro" }` (Zeichentrick: Trainer schießt den Ball zur Kamera, Explosion, das K, TRAININGSKERN,
  trainingskern.de). Für den Comic-Stil: `"film": "outro-comic"`. Übergänge im Zeichentrick-Stil: `iris` und `tinte`,
  im Comic-Stil: `knall`, `pinsel`, `raster`, `panel`.
- Erstes Kampagnen-Video als Muster: `story-studio/stories/kampagne-01-kein-plan.json`.
- Generierte Clips bekommen die Farben der App über `"marke": true` in `filme/filme.json` (Rasen fast schwarz, kein Blau, genaues Neon und Orange).
- Intros dürfen keine Stimme im Ton haben (kein Schreien, kein Rufen): Den Text spricht die eigene ElevenLabs-Stimme.
- Vertonung: je Szene ein Satz in `"sprecher"`, gesprochen mit der Stimme aus `story-studio/stimme.json` (dieselbe wie in der App, „Jarvis deutsch“).
  Der Schlüssel ist in der Cloud-Umgebung für api.elevenlabs.io hinterlegt, nie ins Repo schreiben. Aufnahmen liegen in `ton/sprecher/` und kosten nur einmal.
  Das Zeichen-Kontingent ist knapp (Stand 23.11.2026 rund 15.000 Zeichen frei): Sätze kurz halten, nichts unnötig neu einsprechen.
- Musik läuft leise mit (`"musik"`): leichter Elektro, `ton/musik-elektro.mp3` (generiert, ohne Gesang). Kein Funk-Beat, kein Swing.
- Im Sprechertext sagt die Stimme „von mir auf Deutsch erklärt“, damit klar ist, dass es Ton zur Übung gibt.
- Keine Spielminute, kein Fortschrittsbalken im Bild. Der Bildschirm der Seite zeigt nur Titel und Tafel (`"verstecke"` blendet den Rest aus).
- Vorlage: `story-studio/stories/vorlage-kampagne.json`.

## Story-Studio

`story-studio/` rendert Instagram-Storys (1080 × 1920) aus Story-Dateien. Bedienung und Szenen: `story-studio/README.md`.
Gerenderte Videos liegen in `story-studio/out/` und werden nicht eingecheckt.
