const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const SOURCES = [
  'https://techcrunch.com/category/artificial-intelligence/',
  'https://techcrunch.com/',
  'https://techcrunch.com/tag/ai/',
  'https://techcrunch.com/tag/artificial-intelligence/',
  'https://techcrunch.com/tag/openai/',
  'https://techcrunch.com/tag/google-deepmind/',
  'https://techcrunch.com/tag/generative-ai/',
  'https://techcrunch.com/tag/chatgpt/',
  'https://techcrunch.com/tag/machine-learning/',
  'https://techcrunch.com/tag/anthropic/',
  'https://techcrunch.com/tag/microsoft/',
  'https://techcrunch.com/tag/nvidia/',
];

async function fetchArticles(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 6000));
    
    const articles = await page.evaluate(() => {
      const results = [];
      const now = new Date();
      const cutoff = new Date(now.getTime() - 48 * 60 * 60 * 1000); // 48h window
      
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 300 && href.includes('techcrunch.com/202') && !href.includes('/video/') && !href.includes('/events/') && !href.includes('/podcast/')) {
          let time = '';
          let parent = el.closest('article, .post-block, .river-block, li, .wp-block');
          if (parent) {
            const timeEl = parent.querySelector('time');
            if (timeEl) {
              time = timeEl.dateTime || timeEl.textContent?.trim() || '';
            }
          }
          if (!time) {
            // Try to extract from URL
            const match = href.match(/\/2026\/(\d+)\/(\d+)\//);
            if (match) {
              time = `2026-${match[1]}-${match[2]}T00:00:00`;
            }
          }
          results.push({ title: text, link: href, time, source: url });
        }
      });
      
      return results;
    });
    
    await browser.close();
    return { url, articles, success: true };
  } catch(e) {
    await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  const seen = new Map();
  
  for (const url of SOURCES) {
    process.stderr.write(`Fetching: ${url}\n`);
    const result = await fetchArticles(url);
    if (result.success) {
      for (const art of result.articles) {
        const key = art.link.split('?')[0];
        if (!seen.has(key)) {
          seen.set(key, art);
        }
      }
      process.stderr.write(`  -> Found ${result.articles.length} articles\n`);
    } else {
      process.stderr.write(`  -> Error: ${result.error}\n`);
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  
  const all = Array.from(seen.values());
  // Filter to recent articles
  const cutoff = new Date(Date.now() - 48 * 60 * 60 * 1000);
  const recent = all.filter(a => {
    if (!a.time) return true;
    try {
      const d = new Date(a.time);
      return d >= cutoff;
    } catch { return true; }
  });
  
  process.stderr.write(`Total unique articles: ${all.length}, Recent (48h): ${recent.length}\n`);
  console.log(JSON.stringify({ all, recent }, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
