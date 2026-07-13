const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

async function fetchArticle(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'load', timeout: 20000 });
    await new Promise(r => setTimeout(r, 8000));
    
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      // Get substantial paragraphs
      const paras = Array.from(document.querySelectorAll('p'))
        .map(p => p.textContent.trim())
        .filter(t => t.length > 80)
        .slice(0, 10);
      const content = paras.join(' ').substring(0, 2500);
      return { title, content, paraCount: paras.length };
    });
    
    await browser.close();
    return { url, ...data, success: true };
  } catch(e) {
    await browser.close();
    return { url, error: e.message, success: false };
  }
}

fetchArticle('https://techcrunch.com/2026/07/10/fidji-simo-steps-down-from-openais-no-2-role/')
  .then(r => {
    console.log(JSON.stringify(r, null, 2));
  })
  .catch(e => console.error(e));
