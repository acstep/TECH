const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

async function main() {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--single-process']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  const url = 'https://techcrunch.com/category/artificial-intelligence/';
  await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 5000));
  
  const result = await page.evaluate(() => {
    return {
      // Get all article links
      links: Array.from(document.querySelectorAll('a[href*="/2026/"]')).map(a => ({
        href: a.href,
        text: a.textContent.trim(),
        parent: a.closest('article, div, section')?.className?.substring(0, 100)
      })).filter(a => a.text.length > 20).slice(0, 30),
      
      // Get main content area
      bodySnippet: document.body.innerHTML.substring(0, 5000)
    };
  });
  
  await browser.close();
  console.log(JSON.stringify(result, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
