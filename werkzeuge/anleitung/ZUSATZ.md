# Zusatz für die Ordner „Additional Practices“ (Torwart und Einzeltraining)

Es gilt AUFTRAG.md, mit diesen Abweichungen:

## Allgemein
- Statt „Woche“ heißt die Quelle im Bericht „(U12-U14, Torwarttraining)“ bzw. „(U12-U14, Einzeltraining)“.
- `kind` meist "Übungsform". `altersbereiche` ["U12-U14"], `access` "abo".
- `tags`: Torwart-Ordner `["Torwart"]`, Einzeltraining-Ordner `["Einzeltraining"]`.
- Es muss kein Team Neon gegen Team Rot geben. Gibt es nur eine Farbe, heißen Spieler trotzdem „Spieler sieben“ (nie Farbe + Zahl).
- Punkte nur, wo es einen echten Wettbewerb gibt („das gibt einen Punkt“). Bei reinen Technikübungen statt Punkten ein Ziel
  (runden.js-Zeile mit `ziel:` statt `punkte:`). Der letzte Grundform-Schritt sagt trotzdem, wie die Runde endet und wer dann dran ist.
- `players_min`/`players_max` ehrlich (z. B. 1-2 beim Einzeltraining, ohne Trainer).
- Leitern IMMER `leiter(...)`, Ringe IMMER `ring(...)`, nie Hürden-Ersatz (siehe AUFTRAG.md).
- Viele Übungen eines Ordners ähneln sich: Titel deshalb konkret und unterscheidbar wählen (was passiert, nicht nur
  „Torwart-Reaktion“). Andere Agenten bauen parallel die übrigen Übungen desselben Ordners.

## Torwarttraining
- Torhüter: `P("k1", "t", x, y, "TW")` (neutral, Label "TW"); bei mehreren k1, k2, … Im Text „der Torwart“, bei mehreren
  „der linke Torwart“ / „der zweite Torwart“ o. ä. (keine Nummern).
- Wer schießt oder flankt, ist der Trainer (genau einer) oder ein Spieler von Team Neon mit Nummer („Spieler sieben schießt“).
- Tor: `"size": "jugend"` (Torwart steht drin). Kegel/Stangen/Ringe/Leitern wie im Original.
- focuses aus der festen Liste wählen, passend z. B. "Koordination", "Schnelligkeit", "Ballannahme", "Passspiel", "Torschuss".
- Sichtkegel bei „watch the ball“, „set position“, „scan“, „head up“ usw. wie in AUFTRAG.md.

## Einzeltraining („1 to 1“: ein Trainer mit einem Spieler)
- Ein Spieler von Team Neon (z. B. `P("n7","a",x,y,"7")`) und der Trainer. Mehr Figuren nur, wenn das Original sie zeigt
  (z. B. Torwart neutral "TW", ein Gegenspieler von Team Rot).
- Positionsbezeichnungen (ST, CAM, CM, CB, CDM, Wingers, Full Backs) deutsch im Text: Stürmer, Zehner, zentraler Mittelfeldspieler,
  Innenverteidiger, Sechser, Flügelspieler, Außenverteidiger.
