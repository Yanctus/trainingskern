// Macht aus einem Text der Scroll-Story den Satz, den die Stimme spricht.
// 1. Vor jeder Spielernummer steht „Spieler“: „Die Vier spielt auf die Acht“ wird zu „Spieler vier spielt auf Spieler acht“.
// 1b. Mannschaften heißen „Team Neon“, „Team Rot“, „Team Weiß“.
// 2. Zahlen werden ausgeschrieben. Endet ein Satz auf eine Ziffer, liest die Stimme sonst den Punkt dahinter laut mit.
const WORT = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig"];
const MENGE = "ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf";
const NAME = "Eins|Zwei|Drei|Vier|Fünf|Sechs|Sieben|Acht|Neun|Zehn|Elf";
// Steht eines dieser Wörter vor oder hinter der Zahl, ist eine Menge gemeint und kein Spieler
const DAVOR = /(?:gegen|plus|mal|Zone|Nummer|Coaching-Punkt|Steigerung|Runde|Bahn|zählt|gibt|=)\s*$/i;
const DANACH = /^\s*(?:gegen|plus|mal|Pässe[n]?|Pass\b|Tore?\b|Punkte?\b|Meter[n]?\b|m\b|Kontakte?n?\b|Sekunden?\b|Minuten?\b|Spieler[n]?\b|Bälle[n]?\b|Zonen?\b|Teams?\b|Runden?\b|Hütchen\b|Angreifer[n]?\b|Verteidiger[n]?\b|Schritte?\b|=|%)/;

export function sprechtext(text) {
  let t = String(text || "");
  // Eine Farbe allein meint die ganze Mannschaft: „Rot läuft an“ wird zu „Team Rot läuft an“. Vor einer Nummer fällt sie weg („Neon 6“ ist Spieler sechs).
  t = t.replace(/\b(?:Neon|Rot|Weiß) (?=\d)/g, "");
  t = t.replace(/(?<!Team |in |im )\b(Neon|Rot|Weiß)\b(?![-\wäöüß])/g, "Team $1");
  t = t.replace(new RegExp(`\\bden Ball der (${NAME})\\b`, "g"), (_, w) => `den Ball von Spieler ${w.toLowerCase()}`);
  t = t.replace(new RegExp(`\\bzur (${NAME})\\b`, "g"), (_, w) => `zu Spieler ${w.toLowerCase()}`);
  t = t.replace(new RegExp(`\\b[Dd](?:ie|er) (${NAME})\\b(?!er\\b)`, "g"), (_, w) => `Spieler ${w.toLowerCase()}`);
  t = t.replace(/\d+/g, (z, at) => {
    const n = Number(z), davor = t.slice(0, at), danach = t.slice(at + z.length);
    if (n > 20 || /[\d.,]$/.test(davor) || /^[.,]\d/.test(danach)) return z;
    const menge = DAVOR.test(davor) || DANACH.test(danach);
    if (!menge && n >= 1 && n <= 11) return `Spieler ${WORT[n]}`;
    return n === 1 && /^\s*[A-ZÄÖÜ]/.test(danach) ? "ein" : WORT[n];
  });
  // 3. Ein Punkt oder Tor als Ergebnis wird als Satz gesprochen: „… angekommen: Punkt“ wird zu „… angekommen: das gibt einen Punkt“.
  //    Sonst klingt das einzelne Wort „Punkt“ am Satzende wie ein vorgelesenes Satzzeichen.
  const gibt = (menge, was) => `das gibt ${menge ? (/^ein$/i.test(menge) && was === "Punkt" ? "einen" : menge.toLowerCase()) : was === "Punkt" ? "einen" : "ein"} ${was}`;
  t = t.replace(new RegExp(`([:,]) (?:(${MENGE}) )?(Punkte?|Tore?)(?= für |,|[.!]?$)`, "gi"), (_, trenner, menge, was) => `${trenner} ${gibt(menge, was)}`);
  t = t.replace(new RegExp(`^(${MENGE}) (Punkte|Tore)(?= für |[.!]?$)`, "i"), (_, menge, was) => `Das gibt ${menge.toLowerCase()} ${was}`);
  return t;
}

// Verbindet die Schritte eines Ablaufs mit kleinen Überleitungen, so wie man es beim Erklären sagen würde:
// „Spieler acht spielt den Seitenspieler an.“ … „Dann dreht Spieler vier auf.“ … „Zum Schluss: Abschluss ins Minitor.“
// Der erste Schritt bleibt, wie er ist. Sätze, die schon selbst überleiten oder mit einem Ausruf beginnen, bleiben auch.
const SCHON = /^(?:Jetzt|Dann|Danach|Und|Sofort|Weiter|Erst|Zum Schluss|Anschließend|Nun|Wieder|Schon|Dort|So|Auf|Nach|Diesmal|Zuruf|Los|Bis|Von|Hier|Da|Wenn|Sobald)\b/;
const KEIN_VERB = /^(?:in|im|an|am|auf|aus|mit|von|vom|zu|zum|zur|für|und|oder|nach|vor|bei|über|unter|durch|gegen|ohne|um|bis|der|die|das|den|dem|des|noch|nicht|auch|als|hat|ist|beide|ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf)$/;
// Abwechslung: Die Überleitung richtet sich nach Schritt und Länge des Ablaufs, bleibt für denselben Satz aber immer gleich
// (sonst gälte eine fertige Aufnahme bei jedem Laden als geändert).
const VORN = ["Dann", "Jetzt", "Danach", "Anschließend", "Nun", "Gleich danach", "Daraufhin", "Als Nächstes"];
const DAVOR_SATZ = ["Und dann", "Und jetzt", "Danach", "Anschließend", "Nun", "Gleich danach", "Und weiter", "Als Nächstes"];
// Wörter, die am Satzanfang nur wegen des Satzanfangs großgeschrieben sind
const KLEIN = /^(?:Eng|Ohne|Quer|Mit|Im|In|An|Am|Aus|Durch|Zurück|Beim|Bei|Kurz|Seitlich|Direkt|Erster|Großer|Kleine|Viele|Schnell|Tief|Genau|Flach|Ruhig|Mutig|Sauber|Kontrolliert|Per|Über|Unter|Vor|Hinter|Rüber|Rein|Raus|Weit|Fester|Kleine|Offen|Frei|Eng)\b/;
const ENDE = ["Zum Schluss", "Am Ende", "Zum Abschluss"];
// Beginnt ein Satz so, ist er schon ein ganzer Satz mit eigenem Anfang: Er bekommt keine Überleitung davor
const GANZ = /^(?:Der|Die|Das|Den|Dem|Ein|Eine|Einen|Kein|Keine|Es|Er|Sie|Wer|Wo|Wie|Beide|Alle|Zwei|Drei|Vier|Fünf|Sechs|Sieben|Acht|Neun|Zehn|Spieler|Team)\b/;
const klein = (s) => s.charAt(0).toLowerCase() + s.slice(1);

export function fluss(text, step, count) {
  const t = String(text || "").trim();
  if (!t || step < 1 || SCHON.test(t) || /^[^ ]+[!?]/.test(t) || /^.{0,32}[:!?]/.test(t)) return t;
  const last = step === count - 1 && count > 3, n = step - 1 + count;
  // Satz mit Subjekt und Verb vorn: Das Verb rückt hinter die Überleitung („Dann spielt Spieler acht …“)
  const m = t.match(/^(Spieler [a-zäöüß]+|(?:Der|Die|Das) [A-ZÄÖÜ][\wäöüß-]*|Team (?:Rot|Neon|Weiß)|Alle|Beide|Ich) ([a-zäöüß]+)\b(.*)$/);
  if (m && !KEIN_VERB.test(m[2])) {
    const subjekt = /^(Spieler|Team|Ich)/.test(m[1]) ? (m[1] === "Ich" ? "ich" : m[1]) : klein(m[1]);
    return `${last ? ENDE[count % ENDE.length] : VORN[n % VORN.length]} ${m[2]} ${subjekt}${m[3]}`;
  }
  if (GANZ.test(t)) return t;
  // Stichwort-Satz („Pass in den Lauf“, „Mit Tempo aufs Tor zu“): Die Überleitung geht ohne Pause in ihn über
  return `${last ? ENDE[count % ENDE.length] : DAVOR_SATZ[n % DAVOR_SATZ.length]} ${KLEIN.test(t) ? klein(t) : t}`;
}
