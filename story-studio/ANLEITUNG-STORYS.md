# Anleitung: Instagram-Storys zum Reel des Tages

Stand 24.11.2026. Diese Anleitung fasst zusammen, wie die Story-Bilder für @trainingskern entstehen, wie sie aussehen und wo sie landen.
Die festen Regeln stehen zusätzlich in `CLAUDE.md` (Abschnitt „Storys zum Reel des Tages“).

---

## 1. Das Prinzip

Jeden Abend um **18:30** erscheint ein Reel. Den Tag über führen **drei Story-Bilder** darauf hin:

| Story | Uhrzeit | Aufgabe | Hintergrund |
|---|---|---|---|
| 1 Morgen | **9:00** | Ankündigen oder Problem zeigen | dunkel |
| 2 Mittag | **12:30** | Frage an die Zuschauer | **Neon** (immer) |
| 3 Abend | **18:45** | Reel ist da / Lösung | dunkel |

- Immer genau **3 Bilder je Video**, Format **1080 × 1920**, Standbild (JPG), kein Video.
- Die Storys machen neugierig, das Reel am Abend liefert die Antwort.
- Gepostet wird nur nach ausdrücklichem Okay des Inhabers.

---

## 2. Zwei Arten von Videos, zwei Arten von Storys

### a) Übungs-Video (erklärt eine Übung)

1. **Morgen – Ankündigung:** Standbild aus der Übung (Übungsnummer, Titel, Platz, ein Schritt mit Beschriftung).
   Darunter die Neon-Fläche **„HEUTE 18:30“** und die Zeile „Neues Reel: *Name der Übung*“.
2. **Mittag – Frage an dich:** Neon-Hintergrund, kleine Marke „FRAGE AN DICH“, große Frage zum Thema der Übung
   in zwei Zeilen (zweite Zeile hervorgehoben), darunter ein Satz zum Antworten, darunter eine Notiz in oranger Handschrift
   (Standard: „Schreib uns ↓“), unten „trainingskern.de · Link in Bio“.
3. **Abend – Jetzt neu:** Standbild aus einem **späteren** Teil der Übung (meist die Steigerung), darunter Neon-Fläche
   **„JETZT NEU“** und „Ganzes Reel auf dem Profil.“

### b) Marketing-Video (bewirbt Trainingskern selbst)

1. **Morgen – „KENNST DU DAS?“:** dunkel, das Problem in zwei Zeilen (z. B. „Skizze gesehen. / Nichts verstanden?“),
   ein Satz dazu, Handschrift-Notiz (Standard: „Kommt dir bekannt vor?“).
2. **Mittag – „FRAGE AN DICH“:** wie oben, Neon, Frage zum Problem.
3. **Abend – „DIE LÖSUNG“:** dunkel, die Lösung in zwei Zeilen (z. B. „Sehen. Hören. / Machen.“), ein Satz dazu,
   Neon-Fläche **„HEUTE 18:30“** und „So geht’s: neues Reel auf dem Profil.“, Handschrift-Notiz (Standard: „Heute Abend zeigen wir’s.“).

---

## 3. Gestaltung (gilt für alle)

- Stil der Seite: Schwarz, Neon-Gelb, Orange, Logo „K TRAININGSKERN“ oben links.
- Die drei Bilder dürfen **nicht gleich aussehen**: Mittag ist immer Neon, dazu die orange Handschrift-Notiz unter dem Text.
- Die Beschriftung des Schritts im Übungsbild hat **höchstens zwei Zeilen**.
- Kein Bild mitten in einem Übergang (keine halben Blenden, kein „Knall“-Effekt im Bild).
- Bei Marketing muss das erste Standbild aus einer dunklen Szene mit Logo oben links stammen.
- Unten steht immer **trainingskern.de · Link in Bio** (nie die base44-Adresse).

## 4. Texte

- **Die Frage ist jedes Mal eine andere** und passt zum Thema des Videos (z. B. „Rondo: / Jede Woche dabei?“,
  „Torschuss: / Wie viele Wiederholungen?“). Kurz, zwei Zeilen, zweite Zeile ist der Knackpunkt.
- Darunter ein Satz zum Antworten, endet meist mit „Antworte per Nachricht.“
- Immer **„neutrale Spieler“, nie „Springer“**.
- Keine Anzahl der Übungen nennen, nichts nach App-Store klingen lassen („Jetzt laden“ usw.), keinen Anbieter nennen.
- Kostenlos sind einzelne Übungen, Trainingspläne gehören zum Abo – nichts anderes versprechen.

---

## 5. So entstehen die Bilder (technisch)

Die Bilder werden aus dem fertig gerenderten Video gebaut. In die Story-Datei des Videos (`story-studio/stories/<name>.json`)
kommt ein Block `"storys"`.

**Übungs-Video:**

```json
"storys": {
  "name": "Abschluss in drei Phasen",
  "zeit": "18:30",
  "bilder": [12.3, 55.0],
  "frage": ["Torschuss:", "Wie viele Wiederholungen?"],
  "antwort": "Zählst du mit? Antworte per Nachricht."
}
```

**Marketing-Video:**

```json
"storys": {
  "art": "marketing",
  "zeit": "18:30",
  "bilder": [11.4, 11.4],
  "problem": ["Skizze gesehen.", "Nichts verstanden?"],
  "problemSatz": "Pfeile, Kreise, Kreuze. Und wer läuft jetzt wohin?",
  "frage": ["Skizze oder Video:", "Was hilft dir?"],
  "antwort": "Wie verstehst du eine Übung am schnellsten? Antworte per Nachricht.",
  "loesung": ["Sehen. Hören.", "Machen."],
  "loesungSatz": "Jede Übung läuft als Animation und wird dir auf Deutsch erklärt."
}
```

- `bilder`: zwei Zeitpunkte im Video in Sekunden (Morgen- und Abendbild). Bei Übungen: erstes Bild etwa im ersten Drittel
  der Grundform, zweites Bild in der Steigerung. Bei Marketing wird nur das Logo aus dem Bild genommen.
- Optional eigene Handschrift-Notizen: `problemNotiz`, `frageNotiz`, `loesungNotiz`.

Dann im Ordner `story-studio/`:

```bash
node storys.mjs stories/<name>.json
```

Ergebnis in `story-studio/out/`:

- `<name>-story-1-morgen.jpg`
- `<name>-story-2-mittag.jpg`
- `<name>-story-3-abend.jpg`

(Hilfsdateien `…-story-bild1.jpg` / `…-story-bild3.jpg` werden **nicht** hochgeladen.)

---

## 6. Prüfen, bevor es rausgeht

1. **Ein Übersichtsbild** der drei Bilder nebeneinander ansehen (nicht jedes einzeln).
2. Stimmt: Beschriftung ≤ 2 Zeilen? Kein Übergang im Bild? Logo da? Text nirgends abgeschnitten? Name der Übung richtig?
3. Wenn etwas nicht passt: nur die Zeitpunkte in `bilder` ändern und `node storys.mjs …` erneut laufen lassen
   (das Video muss dafür nicht neu gerendert werden).

---

## 7. Ablage im Google Drive

Ordner „Trainingskern Videos“:

| Ordner | Inhalt |
|---|---|
| **Storys** | **alle Story-Bilder**, die Claude erstellt (nie neben das Video legen) |
| Übungen | Übungs-Videos |
| Vermarktung | Marketing-Videos |
| Geplant | vom Inhaber eingeplante Videos und Storys (`tagNN_1_morgen_0900.jpg` usw.) – **Claude ändert oder löscht hier nichts** |
| Bereits geposted | was schon draußen ist |

Hochladen geht über `story-studio/drive.sh <datei> <ordner-id> <mime>`. Dafür braucht es pro Runde einen neuen
Zugangsschlüssel aus dem Google OAuth Playground (Scope `https://www.googleapis.com/auth/drive`, gilt eine Stunde),
den der Inhaber über das sichere Formular für `www.googleapis.com` hinterlegt – **nie in den Chat oder ins Repo**.

---

## 8. Ablauf für den Inhaber (Einplanen auf Instagram)

1. Video aus „Übungen“ bzw. „Vermarktung“ nehmen, die drei passenden Bilder aus „Storys“ (gleicher Name, Endung
   `-story-1-morgen`, `-2-mittag`, `-3-abend`).
2. In „Geplant“ einem Tag zuordnen (z. B. `tag12_1_morgen_0900.jpg`, `tag12_2_mittag_1230.jpg`, `tag12_3_abend_1845.jpg`).
3. Einplanen: Story 9:00 · Story 12:30 · **Reel 18:30** · Story 18:45.
4. Tipp: Bei der Mittags-Story in Instagram einen Frage-Sticker ergänzen, damit Zuschauer direkt antworten können.
5. Nach dem Posten in „Bereits geposted“ verschieben.

---

## 9. Kurz-Checkliste

- [ ] 3 Bilder je Video, 1080 × 1920
- [ ] Morgen 9:00 dunkel · Mittag 12:30 Neon · Abend 18:45 dunkel · Reel 18:30
- [ ] Übung: HEUTE 18:30 → Frage → JETZT NEU
- [ ] Marketing: KENNST DU DAS? → Frage → DIE LÖSUNG
- [ ] Frage neu und passend, „neutrale Spieler“, trainingskern.de
- [ ] Beschriftung ≤ 2 Zeilen, kein Übergang im Bild, Logo sichtbar
- [ ] Übersichtsbild angesehen
- [ ] In Drive-Ordner „Storys“ hochgeladen
- [ ] Nichts posten ohne Okay
