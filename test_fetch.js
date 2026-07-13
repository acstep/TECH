const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

async function main() {
  process.stderr.write('Starting...\n');
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  process.stderr.write('Browser launched\n');
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    process.stderr.write('Going to TechCrunch...\n');
    await page.goto('https://techcrunch.com/', { waitUntil: 'domcontentloaded', timeout: 15000 });
    process.stderr.write('Page loaded\n');
    await new Promise(r => setTimeout(r, 5000));
    
    const articles = await page.evaluate(() => {
      const results = [];
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 300 && href.includes('techcrunch.com/202')) {
          results.push({ title: text, link: href });
        }
      });
      return results;
    });
    
    process.stderr.write(`Found ${articles.length} articles\n`);
    await browser.close();
    console.log(JSON.stringify(articles.slice(0, 30), null, 2));
  } catch(e) {
    process.stderr.write(`Error: ${e.message}\n`);
    await browser.close();
  }
}

main().catch(e => { process.stderr.write(`Fatal: ${e}\n`); process.exit(1); });
