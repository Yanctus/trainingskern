#!/usr/bin/env python3
"""Prüft die eingesprochenen Sätze einer Einheit auf Fehlerlaute von ElevenLabs am Satzende.

Fehlerbild (TA-002, 24.11.2026): Nach dem letzten Wort kommt eine kurze Pause und dann noch ein kurzer Laut
(etwa eine Drittelsekunde), als finge die Stimme ein neues Wort an und bräche ab.

Aufruf: python3 tonpruefung.py TA-002 [UE-123 ...]
Ausgabe: je verdächtigem Satz Kapitel/Schritt, Zeit und Länge des letzten Lauts. Echte kurze Schlusswörter („mit.“)
können auch auffallen: dann mit faster-whisper gegenhören (Wortzeiten), bevor neu eingesprochen wird.
Neu aufnehmen lassen: in der Datenbank audio.chapters.<k>.steps_text.<s> (bzw. intro_text) auf einen Hinweistext setzen
(update_entities $set). Dann zählt der Satz als „geändert“ und „Geänderte neu einsprechen“ nimmt ihn neu auf.
"""
import json, os, subprocess, sys, tempfile, urllib.parse
import numpy as np

APP = "6afec076c6c4a55a7cb4995e"


def hole(url, ziel):
    subprocess.run(["curl", "-s", "-o", ziel, url], check=True)


def letzter_laut(datei):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", datei, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    w = 400  # 25 ms
    db = np.array([20 * np.log10(np.sqrt((a[i:i + w] ** 2).mean()) + 1e-9) for i in range(0, len(a) - w, w)])
    laut = np.where(db > -35)[0]
    if not len(laut):
        return None
    i = len(laut) - 1
    while i > 0 and laut[i] - laut[i - 1] < 4:
        i -= 1
    dauer = (laut[-1] - laut[i] + 1) * 0.025
    pause = (laut[i] - laut[i - 1] - 1) * 0.025 if i > 0 else 0
    return laut[i] * 0.025, dauer, pause


def main(codes):
    tmp = tempfile.mkdtemp(prefix="tonpruefung-")
    for code in codes:
        q = urllib.parse.quote(json.dumps({"code": code}))
        roh = subprocess.run(["curl", "-s", f"https://app.base44.com/api/apps/{APP}/entities/Einheit?q={q}"],
                             capture_output=True, text=True).stdout
        e = json.loads(roh)[0]
        a = e.get("audio") or {}
        saetze = [("Begrüßung", a.get("intro"))]
        for k, c in enumerate(a.get("chapters") or []):
            saetze.append((f"Kapitel {k + 1} Einleitung", c.get("intro")))
            saetze += [(f"Kapitel {k + 1} Schritt {s + 1}", u) for s, u in enumerate(c.get("steps") or [])]
        treffer = 0
        for name, url in saetze:
            if not url:
                continue
            ziel = os.path.join(tmp, os.path.basename(url))
            hole(url if url.startswith("http") else "https://trainingskern.de" + url, ziel)
            r = letzter_laut(ziel)
            if r and r[1] < 0.6 and r[2] >= 0.1:
                treffer += 1
                print(f"VERDACHT {code} {name}: letzter Laut ab {r[0]:.2f} s, {r[1]:.2f} s lang, nach {r[2]:.2f} s Pause")
        print(f"{code}: {len([s for s in saetze if s[1]])} Sätze geprüft, {treffer} Verdacht")


if __name__ == "__main__":
    main(sys.argv[1:] or ["TA-002"])
