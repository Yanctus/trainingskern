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

- Jedes Video beginnt mit einem der sieben gezeichneten Comic-Intros (Cel-Shading, dicke Konturen) mit freier Fläche, nur der Text wechselt:
  `hook` mit `"film": "comic-..."` (alle sieben: `story-studio/stories/comic-vergleich.json`). Die Intros wechseln von Video zu Video.
  Das Intro muss sich klar vom Outro unterscheiden; `hook-zettel` ist deshalb verworfen.
- **Texte müssen immer sauber im Bild stehen**, nichts darf überstehen oder abgeschnitten sein. Der Renderer prüft das vor jedem Lauf
  („Textprüfung“ in der Ausgabe) und warnt; zusätzlich vor dem Abgeben Standbilder ansehen (`--bild`), vor allem das Intro: Die Prüfung
  sieht nicht, ob Text über den Rand einer gezeichneten Fläche ragt (bei `comic-megafon` deshalb kein `dach`).
- Zwei Stilrichtungen stehen zur Wahl: Comic (`comic-*`, Outro `outro-comic`) und Zeichentrick der 30er (`cartoon-*`, Outro `outro-cartoon`,
  Übergänge `iris` und `tinte`). Figuren sind immer eigene; nie bestehende Figuren oder Namen fremder Marken in Bildaufträgen oder Werbetexten.
- Bilder für neue Intros: Nano Banana, Animation über Start- und Endbild (beides über OpenRouter). Keine Drei-Streifen-Kleidung, keine Logos.
- **Entschieden (23.11.2026): Die Videos laufen im Comic-Stil** (`comic-*`, Outro `"film": "outro-comic"`, Übergänge `knall`, `pinsel`,
  `raster`, `panel`, Musik `"zufall"` aus den Elektro-Titeln). Der Zeichentrick-Stil (`cartoon-*`) bleibt im Repo, wird aber vorerst nicht genutzt.
- Fertige Muster in `story-studio/stories/`: `kampagne-01-kein-plan-comic.json` (Frage und Antwort), `kampagne-02-aufbau-rondo.json`
  (nur der Aufbau einer Übung, Szene `aufbau`), `kampagne-03` bis `-06` (Übung erklärt mit den Aufnahmen der Seite, `"stimme": true`),
  `kampagne-07-woanders.json` und `kampagne-08-was-neues.json` (Marketing: was Trainingskern bietet, wo es woanders hakt).
- **Je Übung ein Video, und zwar das Erklärvideo** (Format `kampagne-03-uebung-rondo.json`): eines der Comic-Intros mit einem Satz,
  der hängen bleibt, Übergang, Szene `uebung` mit `"stimme": true`, dann `blende` ins Outro. Ein Aufbau-Video ist nur auf Wunsch dabei.
- Für erklärte Übungen die vorhandenen Aufnahmen der Seite nehmen (kosten kein ElevenLabs-Kontingent). Der Aufbau hat auf der Seite keine
  Aufnahmen und wird neu eingesprochen.
- **Die Länge entscheidet Claude** (Stand 23.11.2026): so lang, wie der Inhalt braucht, auch über 30 Sekunden. Nicht künstlich strecken.
- Marketing-Videos: Probleme „woanders“ nur allgemein benennen (suchen, unklare Skizzen, selbst erklären), nie einen Anbieter nennen
  und nichts behaupten, was die Seite nicht hält. Kostenlos sind einzelne Übungen, die Trainingspläne gehören zum Abo.
- Jedes Video endet mit demselben Outro im Comic-Stil: `{ "typ": "outro", "film": "outro-comic" }` (Stürmer schießt den Ball zur Kamera,
  Explosion, das K, TRAININGSKERN, trainingskern.de). Ohne `film` nimmt das Studio das Zeichentrick-Outro, das vorerst nicht genutzt wird.
- Veröffentlichen übernimmt später Claude, aber jedes Mal nur nach ausdrücklichem Okay.
- Generierte Clips bekommen die Farben der App über `"marke": true` in `filme/filme.json` (Rasen fast schwarz, kein Blau, genaues Neon und Orange).
- Intros dürfen keine Stimme im Ton haben (kein Schreien, kein Rufen): Den Text spricht die eigene ElevenLabs-Stimme.
- Vertonung: je Szene ein Satz in `"sprecher"`, gesprochen mit der Stimme aus `story-studio/stimme.json` (dieselbe wie in der App, „Jarvis deutsch“).
  Der Schlüssel ist in der Cloud-Umgebung für api.elevenlabs.io hinterlegt, nie ins Repo schreiben. Aufnahmen liegen in `ton/sprecher/` und kosten nur einmal.
  Das Zeichen-Kontingent ist knapp (Stand 23.11.2026 rund 15.000 Zeichen frei): Sätze kurz halten, nichts unnötig neu einsprechen.
- Musik läuft leise mit: leichter Elektro, generiert, ohne Gesang. Drei Titel liegen bereit (`ton/musik-elektro.mp3` 32 s,
  `ton/musik-elektro-2.mp3` und `-3.mp3` je 75 s). `"musik": "zufall"` wählt einen davon (je Story immer denselben); ein Video,
  das länger als 30 Sekunden läuft, braucht einen der langen Titel. Kein Funk-Beat, kein Swing.
- Im Sprechertext sagt die Stimme „von mir auf Deutsch erklärt“, damit klar ist, dass es Ton zur Übung gibt.
- Keine Spielminute, kein Fortschrittsbalken im Bild. Der Bildschirm der Seite zeigt nur Titel und Tafel (`"verstecke"` blendet den Rest aus).
- Vorlage: `story-studio/stories/vorlage-kampagne.json`.

## Story-Studio

`story-studio/` rendert Instagram-Storys (1080 × 1920) aus Story-Dateien. Bedienung und Szenen: `story-studio/README.md`.
Gerenderte Videos liegen in `story-studio/out/` und werden nicht eingecheckt.
