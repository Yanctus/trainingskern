# Pässe durch einen Gegenspieler (Prüfung mit passbahn.mjs)

**Erledigt (25.11.2026):** Alle unten gelisteten Pässe sind korrigiert (nur Koordinaten, `bend`, `delay`; Sprechtexte und Schritte
unverändert, Aufnahmen bleiben gültig). Kontrolllauf über alle 437 Einheiten danach: 1 Treffer, UE-412 Steigerung 2 Schritt 3, gewollt
(laut Text fängt Spieler sechs den Ball ab). Beim Korrigieren mitbehoben: weitere Treffer aus `pruefen` in UE-006, 011, 036, 045.
Hinweis: bau/ue099.py weicht jetzt von der Datenbank ab (Datenbank maßgeblich). Bei UE-188 wirft der Trainer im Coaching-Punkt 1 bewusst
zwischen Spieler zwei und Spieler elf (Duell um den Ball).

## Liste vor der Korrektur (Stand 25.11.2026)

Gefunden: 45 Pässe in 35 Einheiten. „eingesprochen“ = schon vertont und sichtbar.

| Code | Titel | Ton | Fassung | Schritt | Pass | Gegner | Abstand beim Abspiel | engster Abstand im Flug |
|---|---|---|---|---|---|---|---|---|
| UE-003 | Zonenspiel 4 gegen 4 | eingesprochen | Grundform | 2 | p2 → p3 | r6 | 2.5 | 0.5 |
| UE-003 | Zonenspiel 4 gegen 4 | eingesprochen | Coaching-Punkt 2 | 3 | p3 → p1 | r8 | 1 | 1 |
| UE-006 | 4 gegen 4 mit Strafrunde | eingesprochen | Grundform | 1 | n6 → n7 | r6 | 1.4 | 1.4 |
| UE-006 | 4 gegen 4 mit Strafrunde | eingesprochen | Grundform | 2 | n7 → n9 | r7 | 0.4 | 0.4 |
| UE-011 | 3 gegen 2 zum Abschluss | eingesprochen | Grundform | 3 | a2 → a1 | d4 | 2 | 2 |
| UE-012 | Vier-Tore-Spiel 5 gegen 5 | eingesprochen | Grundform | 3 | n3 → n4 | r7 | 2.7 | 0.8 |
| UE-015 | Dribbel-Durchbruch 4 gegen 4 | eingesprochen | Steigerung | 2 | n2 → n3 | r5 | 2.6 | 2.6 |
| UE-020 | Zahlenkette | eingesprochen | Grundform | 4 | n6 → n7 | r1 | 1.1 | 1.1 |
| UE-025 | Balljäger: Einer gegen alle | eingesprochen | Coaching-Punkt | 2 | n3 → n4 | rj | 1.2 | 1.2 |
| UE-033 | Drei-Zonen-Dribbling 5 gegen 5 | eingesprochen | Coaching-Punkt | 2 | n3 → n5 | r9 | 2.7 | 2.7 |
| UE-033 | Drei-Zonen-Dribbling 5 gegen 5 | eingesprochen | Coaching-Punkt | 3 | n5 → n3 | r9 | 2.6 | 2.6 |
| UE-036 | 3 gegen 4: Zusammen pressen | eingesprochen | Steigerung | 3 | n10 → k1 | r4 | 2.2 | 2.2 |
| UE-041 | Rondo 6 gegen 3: Raum schaffen | eingesprochen | Grundform | 2 | n8 → n11 | r4 | 2 | 2 |
| UE-041 | Rondo 6 gegen 3: Raum schaffen | eingesprochen | Steigerung | 3 | n8 → n11 | r4 | 2.4 | 2.4 |
| UE-042 | 3 gegen 2: Schnell über den Flügel | eingesprochen | Grundform | 4 | n7 → n9 | r4 | 1.4 | 0.9 |
| UE-045 | Breite oder Tiefe: 3 gegen 3 plus 2 | eingesprochen | Coaching-Punkt | 1 | n8 → n4 | r6 | 2.5 | 2.5 |
| UE-045 | Breite oder Tiefe: 3 gegen 3 plus 2 | eingesprochen | Coaching-Punkt | 3 | n4 → n8 | r4 | 1.1 | 1.1 |
| UE-047 | 2 gegen 1 und rüber: den Außenspieler finden | eingesprochen | Grundform | 3 | n11 → n6 | r3 | 1 | 1 |
| UE-099 | Pressen und absichern | eingesprochen | Steigerung | 1 | r10 → r11 | n5 | 3.2 | 0.7 |
| UE-136 | Slalom, Abschluss, Zweikampf | eingesprochen | Grundform | 2 | n2 → n6 | r8 | 1.8 | 2.3 |
| UE-188 | Den zweiten Ball gewinnen | eingesprochen | Grundform | 2 | n8 → n4 | r6 | 0.8 | 0.8 |
| UE-216 | Aufrücken und Überzahl schaffen | eingesprochen | Grundform | 3 | n4 → n8 | r6 | 2 | 2 |
| UE-216 | Aufrücken und Überzahl schaffen | eingesprochen | Grundform | 4 | n9 → n8 | r3 | 1.5 | 1.5 |
| UE-302 | Viererkette presst und sichert | noch nicht | Steigerung | 2 | r9 → r11 | n2 | 4.2 | 1.4 |
| UE-304 | Drei Wellen in Überzahl | noch nicht | Coaching-Punkt | 1 | r7 → r10 | n9 | 1.3 | 1.3 |
| UE-308 | Flanken klären im 5 gegen 5 | noch nicht | Coaching-Punkt | 2 | n6 → r8 | r9 | 0.2 | 0.2 |
| UE-314 | Pressingfalle am Flügel | noch nicht | Grundform | 4 | n9 → r1 | r4 | 1.9 | 1.9 |
| UE-333 | Vier machen das Zentrum dicht | noch nicht | Steigerung | 4 | r11 → r9 | n6 | 1.1 | 1 |
| UE-342 | Aus dem Rondo in die Torzone | noch nicht | Coaching-Punkt | 2 | n10 → n2 | r3 | 0.5 | 0.4 |
| UE-351 | Aufbau gegen zwei Spitzen | noch nicht | Grundform | 5 | n11 → n3 | r14 | 2 | 2 |
| UE-352 | Rotieren im Mittelfeld | noch nicht | Steigerung | 3 | n5 → n10 | r18 | 2.3 | 2.3 |
| UE-352 | Rotieren im Mittelfeld | noch nicht | Steigerung | 3 | n5 → n10 | r20 | 2.5 | 2.5 |
| UE-354 | Hohes Pressing im Zonenrondo | noch nicht | Coaching-Punkt | 1 | r13 → r16 | n5 | 3.2 | 1.2 |
| UE-356 | Drei Zonen, als Block pressen | noch nicht | Grundform | 5 | n10 → n9 | r14 | 0.6 | 0.6 |
| UE-359 | Sechs Pässe, dann ins Minitor | noch nicht | Grundform | 1 | n6 → n3 | r9 | 6.2 | 1.7 |
| UE-367 | Direkt, dann zwei Kontakte | noch nicht | Grundform | 1 | n2 → n9 | r10 | 0.4 | 0.5 |
| UE-381 | Sechs gegen vier, dann Konter | noch nicht | Steigerung | 2 | n7 → n9 | r3 | 2.5 | 2.5 |
| UE-381 | Sechs gegen vier, dann Konter | noch nicht | Steigerung | 2 | n7 → n9 | r15 | 0.8 | 0.8 |
| UE-393 | Kompakt stehen, schnell kontern | noch nicht | Grundform | 5 | n9 → n8 | r15 | 0.5 | 0.5 |
| UE-393 | Kompakt stehen, schnell kontern | noch nicht | Coaching-Punkt | 2 | n9 → n8 | r15 | 2.7 | 2.7 |
| UE-400 | Dreierkette mit zwei Sechsern | noch nicht | Coaching-Punkt | 3 | r3 → r11 | n2 | 0.8 | 3.3 |
| UE-400 | Dreierkette mit zwei Sechsern | noch nicht | Steigerung | 3 | n5 → n6 | r9 | 2.4 | 2.7 |
| UE-406 | Erster Ball, zweiter Ball | noch nicht | Grundform | 3 | n5 → n7 | r3 | 0.1 | 1 |
| UE-412 | Sechser schützt die Abwehr | noch nicht | Steigerung | 3 | n5 → n6 | r17 | 2.5 | 2.5 |
| UE-417 | Elf gegen elf, nach außen lenken | noch nicht | Steigerung | 3 | n5 → n4 | r19 | 2.4 | 2.4 |
