# Story-Studio

Macht aus einer kleinen Story-Datei ein fertiges Video für Instagram-Storys (1080 × 1920, 30 Bilder pro Sekunde, MP4).
Das Aussehen kommt aus der Trainingskern-App: dieselben Farben und Schriften, derselbe Platz mit den Papierfiguren,
und die Übungen kommen direkt aus dem Katalog der App.

```bash
node studio.mjs render stories/ue-001.json
```

Das Video liegt danach in `out/ue-001.mp4`, daneben ein Titelbild `out/ue-001.jpg`.

## Was jede Story von selbst mitbringt

- **Intro:** ohne Angabe der Preloader der App im Hochformat (knapp 2 Sekunden): Mittelkreis, das K setzt sich zusammen,
  TRAININGSKERN steigt auf, der Ball rollt über die Seitenlinie. Dann zieht der Vorhang an der Mittellinie auf.
  Mit `"intro": { "film": "intro-papier" }` läuft stattdessen ein Film, der genau auf dem K endet, danach steigt
  TRAININGSKERN auf (zusammen gut 3 Sekunden). Im Stil der App gibt es `intro-papier`, `intro-skizze`, `intro-magnete`
  und `intro-collage`, als Realfilm `intro-flutlicht` und `intro-anstoss`. `"intro": false` lässt das Intro weg, zum Beispiel wenn die Story mit einer Frage beginnt.
- **Marke oben links** und die **Spielminute unten**: Der Ball rollt über die ganze Story von 0′ bis 90′.
- **Übergänge** zwischen den Szenen: `anstoss` (zwei schwarze Hälften schließen an der Mittellinie, Lichtblitz, K),
  `streifen` (schräges Band in Orange, Neon, Schwarz), `blitz` (harter Schnitt mit Neon-Blitz),
  `marker` (ein dicker Stift kritzelt das Bild zu und gibt das nächste frei), `staub` (eine Wolke Neon-Kreide fegt über den Schnitt).
  Jeder Übergang bringt sein Geräusch mit.
- **Sichere Zone:** Oben 250 px und unten 340 px bleiben ohne Text, dort liegen bei Instagram Profilzeile und Antwortfeld.
- **Tonspur:** Geräusche der Übergänge und der leise Ton der Filme. Musik kommt in der Instagram-App dazu (dort ist sie lizenziert).

## Eine Story schreiben

Eine Datei in `stories/`, zum Beispiel `stories/ue-001.json`:

```json
{
  "titel": "Dribbel-Dreieck mit Ablage",
  "uebergang": "anstoss",
  "szenen": [
    { "typ": "aufmacher", "code": "UE-001", "dach": "Übung der Woche" },
    { "typ": "uebung", "code": "UE-001", "schritte": 6, "tempo": 1.7, "uebergang": "streifen" },
    { "typ": "punkte", "code": "UE-001" },
    { "typ": "app", "seite": "/einheiten/{id:UE-001}", "dauer": 5, "scroll": [0, 3300] },
    { "typ": "abpfiff" }
  ]
}
```

`uebergang` ganz oben gilt für alle Schnitte, an einer Szene nur für den Schnitt in diese Szene.

| Szene | Was sie zeigt | Angaben |
| --- | --- | --- |
| `hook` | Große Frage oder Behauptung, auf Wunsch über einem Film | `zeilen` (`*so*` = Neon-Fläche), `film`, `dach`, `notiz`, `lage` (oben, mitte, unten), `ton` (dunkel, papier, neon), `takt` |
| `aufmacher` | Schlagzeile auf Papier, mit `code` dazu Minuten, Spieler und Altersklasse als Karten | `code`, `zeilen` (eigene Schlagzeile, `*so*` = schräg), `dach`, `notiz`, `stempel`, `karten: false` |
| `uebung` | Die Übung läuft auf dem Platz, Schritt für Schritt mit Beschriftung | `code`, `schritte` (nur die ersten N), `tempo`, `fassung` (1 = Coaching-Punkt, 2 = Steigerung …), `titel`, `zoom` |
| `punkte` | Zwei bis vier kurze Sätze als Karten, ohne `punkte` die Coaching-Punkte der Übung | `code` oder `punkte`, `titel`, `max`, `streichen: true` (durchgestrichen), `ton` |
| `app` | Die echte App im Handy, wird gescrollt | `seite` (`{id:UE-001}` wird zur Adresse der Übung), `scroll` [von, bis] in Pixeln, `dauer`, `notiz`, `stempel`, `zettel` |
| `abpfiff` | Logo, Schlusssatz, Aufruf, Adresse | `zeilen` (`*so*` = Neon), `knopf`, `adresse`, `notiz`, `zahl` (nur auf Wunsch) |
| `intro` | Das Intro als Szene an beliebiger Stelle (mit `"intro": false` oben) | `film`, `tempo` |

Jede Szene nimmt außerdem `dauer` (Sekunden). Bei `uebung` ergibt sich die Dauer aus dem Ablauf und dem Tempo.

## Filme und Geräusche

In `filme/` liegen kurze generierte Clips (Seedance 2.5, 720 × 1280, ohne Text, ohne Gesichter). Sie dienen als Hintergrund
für `hook`-Szenen, als Intro und als Wischer:

| Film | Zeigt | Gedacht für |
| --- | --- | --- |
| `klemmbrett` | Trainerhände mit leerem Klemmbrett, Stift zögert | „Heute Training und kein Plan?“ |
| `taktiktafel` | Hand schiebt Magnete unschlüssig über die Tafel | „Kein Spielsystem drin?“ |
| `huetchen-dribbling` | Beine dribbeln Slalom durch Hütchen, Flutlicht | „Immer dieselbe Übung?“ |
| `ballnetz` | Ballnetz fällt auf den Rasen, Bälle rollen zur Kamera | Trainingsbeginn |
| `pfeife-regen` | Pfeife hängt am Pfosten im Regen | ruhige Bilder, Zitate |
| `platz-daemmerung` | leerer Platz mit Hütchenreihe in der Dämmerung | allgemeiner Hintergrund |
| `intro-papier` | Papierfiguren auf dem dunklen Platz, eine schießt den Ball zur Kamera, Neon-Blitz, K | Intro im Stil der App |
| `intro-skizze` | Marker zeichnet Feld, Pfeile und Hütchen auf Papier, das Blatt reißt weg, K | Intro im Stil der App |
| `intro-magnete` | Taktiktafel von oben, Magnete und Pfeile laufen zur Mitte, Neon-Blitz, K | Intro im Stil der App |
| `intro-collage` | Papierfetzen, Klebeband, Ball und Hütchen schnappen zusammen, K | Intro im Stil der App |
| `intro-flutlicht`, `intro-anstoss` | Realfilm, enden auf dem K | Intro |
| `wischer-marker`, `wischer-staub` | Stift auf Weiß, Kreidestaub auf Schwarz | Übergänge `marker`, `staub` |

`filme/filme.json` hält die Angaben je Film (Ausschnitt, Tempo, Maske für Wischer). Bei Intro-Filmen (Name beginnt mit `intro-`)
misst der Renderer selbst aus, wo das K im letzten Bild sitzt und ab wann es steht; Angaben in `filme.json` gehen vor.
`stories/intro-vergleich.json` zeigt alle Intros im Stil der App hintereinander.
`intro-anstoss` wird erst ab der Staubwolke genutzt: Davor ist ein Stutzen mit einem Markenlogo zu sehen, das nicht in die Werbung soll.
In `ton/` liegen die Geräusche der gebauten Übergänge (`wusch`, `rumms`, `klick`), geschnitten aus dem Ton der Filme.
Ein neuer Film: Datei nach `filme/` legen (Name in Kleinbuchstaben mit Bindestrich) und in der Szene mit `"film": "name"` angeben.

## Ansehen, bevor gerendert wird

```bash
node studio.mjs vorschau stories/ue-001.json
```

Öffnet die Story im Browser mit Regler zum Spulen. „Sichere Zone“ blendet die Bereiche ein, die Instagram überdeckt.
Einzelne Standbilder gehen schneller als das ganze Video:

```bash
node studio.mjs render stories/ue-001.json --bild 3.5,8,20
```

## Formate, die sich bewährt haben

- **Selling-Video** (rund 23 Sekunden, ohne Intro): `hook` mit Film und einer Frage, die der Trainer kennt, dann die Antwort
  (`hook` in Neon oder `punkte` mit `streichen`), `app`, `uebung`, `abpfiff`. Siehe `stories/heute-training.json` und `stories/abwechslung.json`.
- **Übung der Woche** (rund 30 Sekunden): `aufmacher`, `uebung`, `punkte`, `app`, `abpfiff`. Siehe `stories/ue-001.json`.
- **Kurz und knapp** (rund 15 Sekunden): `aufmacher`, `uebung`, `abpfiff`. Siehe `stories/ue-011-kurz.json`.
- **Coaching-Punkt:** `aufmacher` mit eigener Schlagzeile, `uebung` mit `"fassung": 1`, `abpfiff`.
- **Blick in die App:** `aufmacher`, zwei `app`-Szenen (Katalog, dann eine Übung), `abpfiff`.

Kostenlose Übungen (offen oder mit kostenlosem Konto) eignen sich am besten: Wer auf den Link tippt, sieht sie auch wirklich.

## Wie es gebaut ist

- `studio/main.js`: Zeitleiste, Intro, Übergänge, Szenen. Alles hängt an einer Zeit `t`; `seek(t)` stellt jedes Teil auf diesen Moment.
- `studio/platz.js`: der Platz aus der App ohne React (gleiches Markup wie `LivePitch.jsx`, `Stage.jsx`, `Sketch.jsx`).
- `studio/app/`: Kopien aus der App (Stand 23.11.2026): `playbook.js` (Spielzug-Rechner), `sprechtext.js`, `zine.css`, `einheit.css`,
  `fonts.css` und die Schriften. Ändert sich in der App die Tafel oder das Aussehen, diese Dateien neu kopieren
  (in `playbook.js` nur die Import-Zeile auf `./sprechtext.js` anpassen).
- `filme/`, `ton/`: Clips und Geräusche (siehe oben). Der Renderer zerlegt jeden Film einmal in Einzelbilder, damit jedes Bild genau sitzt.
- `studio.mjs`: holt die Übungen aus dem Katalog (öffentliche Leseschnittstelle), nimmt für `app`-Szenen die veröffentlichte App
  im Handyformat auf, fotografiert die Story Bild für Bild mit Chromium, mischt die Tonspur und setzt alles mit ffmpeg zusammen.
  So ruckelt nichts, egal wie langsam der Rechner ist.

Braucht Node 20 oder neuer, Playwright mit Chromium (`npm i playwright`, dann `npx playwright install chromium`), ffmpeg und curl.
`--neu` holt Übungsdaten und App-Aufnahmen frisch (sonst gelten die Übungsdaten sechs Stunden).
