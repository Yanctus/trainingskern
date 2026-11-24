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
  (nur der Aufbau einer Übung, Szene `aufbau`), `kampagne-03` bis `-06` (Übung erklärt, nur Grundform), `kampagne-09` bis `-11`
  (Übung komplett: Grundform, Coaching-Punkt, Steigerung),
  `kampagne-07-woanders.json`, `kampagne-08-was-neues.json` und `kampagne-14-alles-drin.json` (Marketing: was Trainingskern bietet,
  wo es woanders hakt, wie breit der Katalog ist). Je Runde: ein Marketing-Video und zwei Übungs-Videos, jedes Mal anders aufgebaut.
- **Je Übung ein Video, und zwar das Erklärvideo mit Coaching-Punkt und Steigerung** (Format `kampagne-11-komplett-pressing-rondo.json`,
  gilt für alle künftigen Übungs-Videos): eines der Comic-Intros mit einem Satz, der hängen bleibt, dann drei Szenen `uebung` mit
  `"stimme": true`: die Grundform, `"fassung": 1` (Coaching-Punkt) und `"fassung": 2` (Steigerung), dann `blende` ins Outro.
  Die Seite hat für alle drei Teile Aufnahmen. Bei sehr langen Grundformen reichen die ersten Schritte (`"schritte": 3`).
  Ein Aufbau-Video ist nur auf Wunsch dabei. Die kurzen Fassungen ohne Coaching-Punkt (`kampagne-03` bis `-06`) sind der alte Stand.
- **Jedes Übungs-Video zeigt eine andere Übung** (Vorgabe vom 23.11.2026): nie eine, die schon ein Video hat, und quer durch den Katalog
  gemischt (Athletik, Koordination, Torhüter, Technik, Spielformen, verschiedene Altersklassen). Es geht darum, die Vielfalt zu zeigen.
  Schon verfilmt: UE-001, UE-004, UE-005, UE-007, UE-008, UE-011, UE-207 (Athletik), UE-264 (Torwart).
  Nur kurz angerissen in `kampagne-14-alles-drin.json`: UE-129, UE-265, UE-292 (dürfen noch ein eigenes Video bekommen).
  Für das komplette Format Übungen wählen, die Coaching-Punkt und Steigerung haben (manche haben stattdessen zwei Coaching-Punkte).
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
- Musik läuft leise mit: leichter Elektro, generiert, ohne Gesang. Vier Titel liegen bereit (`ton/musik-elektro.mp3` 32 s,
  `ton/musik-elektro-2.mp3` 61 s, `ton/musik-elektro-3.mp3` 66 s, `ton/musik-elektro-4.mp3` 110 s). `"musik": "zufall"` wählt einen,
  der bis zum Ende reicht (je Story immer denselben). Ist ein Video länger als jeder Titel, setzt die Musik an einem Szenenwechsel
  neu an. Fertige Storys nennen ihren Titel fest, damit ein neues Rendern gleich klingt. Kein Funk-Beat, kein Swing.
- Im Sprechertext sagt die Stimme „von mir auf Deutsch erklärt“, damit klar ist, dass es Ton zur Übung gibt.
- Keine Spielminute, kein Fortschrittsbalken im Bild. Der Bildschirm der Seite zeigt nur Titel und Tafel (`"verstecke"` blendet den Rest aus).
- Vorlage: `story-studio/stories/vorlage-kampagne.json`.

## Sprache

- **„Neutrale Spieler“, nie „Springer“** (Vorgabe vom 24.11.2026): gilt für alle eigenen Texte, Sprechersätze und Beschriftungen.
  Die Aufnahmen und Texte mancher Übungen auf der Seite sagen noch „Springer“; solche Übungen erst verfilmen, wenn sie dort geändert sind,
  oder dem Nutzer vorher Bescheid geben.

## Prüfliste vor dem Abgeben (Vorgabe vom 24.11.2026: keine Fehler, aber sparsam arbeiten)

Erst prüfen, dann rendern. Ein Fehler, der erst im fertigen Video auffällt, kostet ein zweites Rendern und eine zweite Runde.

1. `node studio.mjs render stories/<name>.json --bild <zeiten>` vor dem Rendern: Die Ausgabe darf kein „ACHTUNG“ zeigen. Sie prüft,
   ob Text übersteht oder abgeschnitten wird und ob Stimme und Bewegung zusammenpassen.
2. **Ein** Übersichtsbild je Video ansehen (Standbilder nebeneinander, klein skaliert), nicht jedes Bild einzeln: das Intro, je ein Bild
   aus jeder Szene, das Outro. Beim Intro darauf achten, dass der Text mittig auf der freien Fläche sitzt, sie gut ausfüllt und nicht
   an ihren gezeichneten Rand stößt.
3. Der Text im Intro steht mittig (macht das Studio von selbst) und ist höchstens vier kurze Zeilen lang. Bild und Sprecher sagen dasselbe.
4. Stimme und Bewegung: Die Bewegung eines Schritts läuft, solange die Stimme sie beschreibt (macht das Studio von selbst). Übungen mit
   sehr langen Sätzen je Schritt meldet die Ausgabe; dann Standbilder aus diesem Schritt ansehen.
5. Der gesprochene Name der Übung muss vollständig sein (Namen mit Kommas wurden früher abgeschnitten).
6. Erst wenn 1 bis 5 stimmen, rendern. Danach den Ton einmal mitschreiben lassen und mit dem Text vergleichen. Selbst hören kann Claude nicht:
   das dem Nutzer jedes Mal sagen.
7. Nur neu rendern, was sich geändert hat. Keine neuen Clips, Songs oder Sprechersätze erzeugen, wenn vorhandene reichen.

## Storys zum Reel des Tages (Vorgabe vom 24.11.2026)

Zu jedem Video, das abends als Reel erscheint, gehören drei Story-Bilder (1080 × 1920, Standbilder, kein Video), die den Tag über darauf
hinführen. Muster des Nutzers:

1. **Ankündigung:** Bild aus der Übung (Titel, Platz, ein Schritt), darunter Neon-Fläche „HEUTE 18:30“ und „Neues Reel: <Name der Übung>“.
2. **Frage an die Zuschauer:** dunkler Grund, kleine Neon-Marke „FRAGE AN DICH“, große Frage zum Thema (zweite Zeile in Neon), darunter ein
   Satz zum Antworten, unten „trainingskern.de · Link in Bio“.
3. **Jetzt neu:** Bild aus der Übung (späterer Schritt), darunter Neon-Fläche „JETZT NEU“ und „Ganzes Reel auf dem Profil.“

Die Bilder entstehen zusammen mit dem Video und kommen mit in den passenden Drive-Ordner.

## Ablage der fertigen Videos (Vorgabe vom 23.11.2026)

Fertige Videos kommen in Google Drive, Ordner „Trainingskern Videos“ (`1kgJvEBkFK7TOQKSHF-CZqkVThPoBqMN4`):

- **Vermarktung** (`1Qvr8n36wUqcJo-mie32PV-U43YgVz37Y`): alles, was Trainingskern allgemein bewirbt (bisher kampagne-01, -07, -08).
- **Übungen** (`1adLAJwAyhhvE9BT5b6Uj2wfLqGVvbrHA`): alles, was eine Übung erklärt (bisher kampagne-02 bis -06, -09 bis -11).

Hochladen: über die Drive-Schnittstelle (`POST https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart`, `parents` = Ordner).
Der Drive-Zugang der Sitzung selbst kann keine Videodateien hochladen. Der Nutzer holt dafür einen Zugangsschlüssel im Google OAuth Playground
(Scope `https://www.googleapis.com/auth/drive`, gilt eine Stunde) und hinterlegt ihn über das sichere Formular für `www.googleapis.com`;
nie in den Chat oder ins Repo. Für jede Runde braucht es einen neuen Schlüssel (der Drive-Zugang der Sitzung nimmt nur Dateien bis 10 MB).
Stand 24.11.2026 liegen kampagne-01 (Comic) bis -14 im Drive (Vermarktung: 01, 07, 08, 14; Übungen: alle anderen).

## Story-Studio

`story-studio/` rendert Instagram-Storys (1080 × 1920) aus Story-Dateien. Bedienung und Szenen: `story-studio/README.md`.
Gerenderte Videos liegen in `story-studio/out/` und werden nicht eingecheckt.
