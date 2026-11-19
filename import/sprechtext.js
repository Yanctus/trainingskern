// Macht aus einem Text der Scroll-Story den Satz, den die Stimme spricht.
// 1. Vor jeder Spielernummer steht „Spieler“: „Die Vier spielt auf die Acht“ wird zu „Spieler vier spielt auf Spieler acht“.
// 2. Zahlen werden ausgeschrieben. Endet ein Satz auf eine Ziffer, liest die Stimme sonst den Punkt dahinter laut mit.
const WORT = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig"];
const MENGE = "ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf";
const NAME = "Eins|Zwei|Drei|Vier|Fünf|Sechs|Sieben|Acht|Neun|Zehn|Elf";
// Steht eines dieser Wörter vor oder hinter der Zahl, ist eine Menge gemeint und kein Spieler
const DAVOR = /(?:gegen|plus|mal|Zone|Nummer|Coaching-Punkt|Steigerung|Runde|Bahn|zählt|gibt|=)\s*$/i;
const DANACH = /^\s*(?:gegen|plus|mal|Pässe[n]?|Pass\b|Tore?\b|Punkte?\b|Meter[n]?\b|m\b|Kontakte?n?\b|Sekunden?\b|Minuten?\b|Spieler[n]?\b|Bälle[n]?\b|Zonen?\b|Teams?\b|Runden?\b|Hütchen\b|Angreifer[n]?\b|Verteidiger[n]?\b|Schritte?\b|=|%)/;

export function sprechtext(text) {
  let t = String(text || "");
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
const SCHON = /^(?:Jetzt|Dann|Danach|Und|Sofort|Weiter|Erst|Zum Schluss|Anschließend|Nun|Wieder|Schon|Dort|So|Auf|Nach|Diesmal|Zuruf|Los|Bis)\b/;
const KEIN_VERB = /^(?:in|im|an|am|auf|aus|mit|von|vom|zu|zum|zur|für|und|oder|nach|vor|bei|über|unter|durch|gegen|ohne|um|bis|der|die|das|den|dem|des|noch|nicht|auch|als|hat|ist|beide|ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf)$/;
const VORN = ["Dann", "Jetzt", "Danach", "Anschließend"], DAVOR_SATZ = ["Und dann", "Danach", "Und jetzt", "Als Nächstes"];
const klein = (s) => s.charAt(0).toLowerCase() + s.slice(1);

export function fluss(text, step, count) {
  const t = String(text || "").trim();
  if (!t || step < 1 || SCHON.test(t) || /^[^ ]+[!?]/.test(t) || /^.{0,32}[:!?]/.test(t)) return t;
  const last = step === count - 1 && count > 3;
  // Satz mit Subjekt und Verb vorn: Das Verb rückt hinter die Überleitung („Dann spielt Spieler acht …“)
  const m = t.match(/^(Spieler [a-zäöüß]+|(?:Der|Die|Das) [A-ZÄÖÜ][\wäöüß-]*|Rot|Neon|Weiß|Alle|Beide|Ich) ([a-zäöüß]+)\b(.*)$/);
  if (m && !KEIN_VERB.test(m[2])) {
    const subjekt = /^(Spieler|Rot|Neon|Weiß|Ich)/.test(m[1]) ? (m[1] === "Ich" ? "ich" : m[1]) : klein(m[1]);
    return `${last ? "Zum Schluss" : VORN[(step - 1) % VORN.length]} ${m[2]} ${subjekt}${m[3]}`;
  }
  return `${last ? "Zum Schluss" : DAVOR_SATZ[(step - 1) % DAVOR_SATZ.length]}: ${t}`;
}
