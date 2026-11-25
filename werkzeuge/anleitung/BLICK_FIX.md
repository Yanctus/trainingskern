# Auftrag: Sichtkegel nach der neuen Regel korrigieren (Inhaber, 25.11.2026)

## Die Regel
Ein Sichtkegel (Schritt-Typ `blick`) gehört nur zu dem Spieler, der schaut und DANACH selbst passt oder schießt.
- Erlaubt: Der Passgeber schaut vor seinem Pass (zum Ziel, in den Raum, zum Gegner), dann spielt er.
- Erlaubt: Annehmen und Aufdrehen (ZUSATZ_U15.md): Der Empfänger schaut zum Passgeber, der Ball kommt, nach der Annahme schwenkt
  der Kegel (`von`) zum Passziel, dann passt oder schießt er selbst.
- Erlaubt und gewünscht (Inhaber, 25.11.2026, Nachtrag): Bereit zur Annahme. Sagt der Text ausdrücklich, dass sich ein Spieler
  zur Annahme bereit macht, offen steht, sich zum Ball öffnet oder den Ball kommen sieht, bekommt der Empfänger VOR dem Pass einen
  Kegel, der zum Ball bzw. Passgeber zeigt. Das gilt auch, wenn er danach nicht selbst passt. Solche Kegel nie streichen; fehlt in
  so einem Schritt der Kegel, einen ergänzen (`bl(empfänger, passgeber)`, dann der Pass mit `after`).
- Nicht erlaubt: Kegel beim Empfänger, der in den Raum schaut, während ein anderer passt (Fall UE-397). Kegel bei Spielern, die
  danach nicht selbst passen oder schießen (Läufer, Verteidiger, die nur beobachten, Reaktionsspiele, Torhüter ohne Abwurf).
- Ersatz: Steht im Original „scanning“ eines Läufers oder Empfängers, bekommt den Kegel der Spieler, der ihn anspielt (er schaut
  zum Läufer bzw. in den Raum, dann passt er). Gibt es keinen passenden Passgeber, entfällt der Kegel.

## Vorgehen je Einheit (Liste: werkzeuge/BLICK_FIX_LISTE.md, dein Paket)
1. Quelle wie in anleitung/PASSBAHN_FIX.md: U9-U14 Datenbank maßgeblich (`werkbank.py lesen`), `bau/ueNNN_quer.py` falls vorhanden,
   U15 (UE-298 bis UE-418) `bau/ueNNN.py`.
2. Je gelistetem Kegel: auf den Passgeber verlegen (Blick vor dessen Pass, Pass mit `after` oder `delay` danach) oder streichen.
   Gibt es im selben Schritt schon einen erlaubten Kegel für den Passgeber, den falschen einfach streichen.
3. Texte: Noch nicht eingesprochene Einheiten: Sprechtext, Label und Fassungstexte so anpassen, dass sie zum Kegel passen
   („Spieler elf schaut …, dann …“), Stil wie die übrigen Texte (Trainer am Platz). Eingesprochene Einheiten: Sprechtexte und
   Schrittzahl NICHT ändern (die Liste enthält nur Kegel, die die Stimme nicht erwähnt). Labels dürfen angepasst werden, wenn
   sie den Blick falsch beschreiben.
4. Hochladen mit `werkbank.py patch alt.json neu.json` → genau diesen `$set` per mcp__Base44__update_entities.
5. Prüfen: `lesen` + `vergleichen` 0 Abweichungen, `pruefen` 0 Treffer (keine neuen Hinweise), `node passbahn.mjs /tmp/claude-0/pb.mjs …`
   0 Treffer, `node blickpruefung.mjs /tmp/claude-0/pb.mjs <neu_db.json> /tmp/b.json`: keine Funde mehr außer denen, die in der
   Liste unter „Später“ stehen. Blatt ansehen.
Nicht committen, runden.js und BERICHT.md nicht anfassen, keine anderen Einheiten. Kontrolldateien in einem eigenen Unterordner
von /tmp/claude-0 anlegen und nur diesen aufräumen (andere Helfer arbeiten parallel).

## Rückmeldung (Deutsch, knapp)
Je Einheit eine Zeile: welcher Kegel wohin verlegt oder gestrichen, Textänderungen kurz, Prüfergebnis. Probleme extra.
