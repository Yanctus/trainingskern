# Trainingskern

Die App selbst liegt bei Base44 (App „Trainingskern“), dieses Repo enthält das Marketing-Werkzeug.

## Feste Vorgaben für alles, was nach außen geht

- Die Adresse ist immer **trainingskern.de** (nie die base44.app-Adresse), in Videos, Texten und Aufrufen.
- Keine Zahl der Übungen nennen. Geworben wird mit dem Nutzen: jede Übung animiert und eingesprochen, fertige Trainingspläne.
- Instagram-Konto: @trainingskern. Nichts veröffentlichen ohne ausdrückliches Okay.
- Intros und Grafik im Stil der App (Papier, Tafel, Neon und Orange auf Schwarz), nicht als Realfilm.
- Keine generierten Kindergesichter, keine fremden Markenlogos in Clips.

## Kampagnen-Videos

- Jedes Video beginnt mit demselben Intro, nur der Text wechselt: ein gezeichnetes Comic-Intro (Cel-Shading, dicke Konturen) mit freier Fläche,
  `hook` mit `"film": "comic-..."`. Welche Variante das feste Intro wird, ist noch offen (Auswahl: `story-studio/stories/comic-vergleich.json`).
  Das Intro muss sich klar vom Outro unterscheiden; `hook-zettel` ist deshalb verworfen.
- Bilder für neue Intros: Nano Banana, Animation über Start- und Endbild (beides über OpenRouter). Keine Drei-Streifen-Kleidung, keine Logos.
- Jedes Video endet mit demselben Outro: `{ "typ": "outro" }` (Papierfigur schießt den Ball zur Kamera, K, TRAININGSKERN, trainingskern.de).
- Vorlage: `story-studio/stories/vorlage-kampagne.json`.

## Story-Studio

`story-studio/` rendert Instagram-Storys (1080 × 1920) aus Story-Dateien. Bedienung und Szenen: `story-studio/README.md`.
Gerenderte Videos liegen in `story-studio/out/` und werden nicht eingecheckt.
