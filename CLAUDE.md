# Trainingskern

Die App selbst liegt bei Base44 (App „Trainingskern“), dieses Repo enthält das Marketing-Werkzeug.

## Feste Vorgaben für alles, was nach außen geht

- Die Adresse ist immer **trainingskern.de** (nie die base44.app-Adresse), in Videos, Texten und Aufrufen.
- Trainingskern gibt es (noch) nicht im App-Store, nur online unter trainingskern.de. Nichts schreiben, das nach Store-App klingt
  („Echte App“, „Jetzt laden“); passend sind „Ohne Download“, „Online“, „im Browser“.
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
- Gestartet wird im Zeichentrick-Stil der 30er (`cartoon-*`), der Comic-Stil (`comic-*`) bleibt als zweite Schiene erhalten.
- Jedes Video endet mit demselben Outro: `{ "typ": "outro" }` (Zeichentrick: Trainer schießt den Ball zur Kamera, Explosion, das K, TRAININGSKERN,
  trainingskern.de). Für den Comic-Stil: `"film": "outro-comic"`. Übergänge im Zeichentrick-Stil: `iris` und `tinte`,
  im Comic-Stil: `knall`, `pinsel`, `raster`, `panel`.
- Erstes Kampagnen-Video als Muster: `story-studio/stories/kampagne-01-kein-plan.json`.
- Generierte Clips bekommen die Farben der App über `"marke": true` in `filme/filme.json` (Rasen fast schwarz, kein Blau, genaues Neon und Orange).
- Intros dürfen keine Stimme im Ton haben (kein Schreien, kein Rufen): Den Text spricht später die eigene ElevenLabs-Stimme.
- Vorlage: `story-studio/stories/vorlage-kampagne.json`.

## Story-Studio

`story-studio/` rendert Instagram-Storys (1080 × 1920) aus Story-Dateien. Bedienung und Szenen: `story-studio/README.md`.
Gerenderte Videos liegen in `story-studio/out/` und werden nicht eingecheckt.
