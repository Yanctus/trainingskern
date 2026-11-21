// Live-Check der echten Einheiten-Seite als Gast (Handy-Breite). Für die volle Story muss die Einheit kurz "frei" sein.
//   node live.js <ziel.png> <id> [<id> ...]   -> je Einheit eine Zeile im Kontaktbild: Kopf + 9 Bilder der laufenden 3D-Story
const { chromium } = require('playwright');
(async () => {
  const [out, ...ids] = process.argv.slice(2);
  const b = await chromium.launch();
  const shots = [];
  for (const id of ids) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 120)); });
    await p.goto('https://trainingskern.de/einheiten/' + id + '?t=' + Date.now(), { waitUntil: 'networkidle', timeout: 60000 });
    await p.waitForTimeout(1500);
    const row = [await p.screenshot()];
    const has = await p.$('.story');
    if (has) {
      await p.click('.story-snd').catch(() => {});
      await p.evaluate(() => { const s = document.querySelector('.story'); const at = s.getBoundingClientRect().top + scrollY; scrollTo(0, at - 40); return new Promise(r => setTimeout(() => { scrollTo(0, at + 2); r(); }, 300)); });
      for (let i = 0; i < 9; i++) { await p.waitForTimeout(i === 0 ? 2500 : 5000); row.push(await p.screenshot()); }
    }
    const sw = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
    console.log(id, '| Story:', !!has, '| Breite', sw.join('/'), '| Fehler:', errs.slice(0, 2).join(' || ') || 'keine');
    shots.push(row); await p.close();
  }
  // Kontaktbild bauen (im Browser, ohne Zusatzpakete)
  const pg = await b.newPage({ viewport: { width: 1000, height: 200 } });
  const html = '<body style="margin:0;background:#222">' + shots.map(r => '<div style="display:flex">' + r.map(s => `<img style="width:100px" src="data:image/png;base64,${s.toString('base64')}">`).join('') + '</div>').join('') + '</body>';
  await pg.setContent(html); await pg.waitForTimeout(300);
  await pg.screenshot({ path: out, fullPage: true });
  await b.close();
})();
