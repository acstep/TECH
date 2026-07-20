const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const ARTICLES = [
  'https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/',
  'https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/',
  'https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/',
  'https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/',
  'https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/',
  'https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/',
  'https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/',
  'https://techcrunch.com/2026/07/16/oil-giant-bp-shutters-its-corporate-venture-arm-after-20-years/',
  'https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/',
  'https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/',
  'https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/',
  'https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/',
  'https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/',
  'https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/',
  'https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/',
  'https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/',
  'https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/',
  'https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/',
  'https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/',
  'https://techcrunch.com/2026/07/18/kimi-threat-or-menace/',
];

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
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 4000));
    
    const result = await page.evaluate(() => {
      const article = document.querySelector('article') || document.querySelector('.article') || document.querySelector('.post-content');
      let content = '';
      if (article) {
        const paras = article.querySelectorAll('p');
        paras.forEach(p => { content += p.textContent + '\n'; });
      }
      if (!content) {
        const paras = document.querySelectorAll('p');
        paras.forEach(p => { content += p.textContent + '\n'; });
      }
      
      const title = document.querySelector('h1')?.textContent?.trim() || 
                    document.querySelector('[class*="title"]')?.textContent?.trim() || '';
      
      let byline = '';
      const author = document.querySelector('[class*="author"], .byline, [rel="author"]');
      if (author) byline = author.textContent.trim();
      
      let published = '';
      const time = document.querySelector('time');
      if (time) published = time.dateTime || time.textContent.trim();
      
      return { title, byline, published, content: content.trim() };
    });
    
    await browser.close();
    return { url, ...result, success: true };
  } catch(e) {
    await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  const results = [];
  for (let i = 0; i < ARTICLES.length; i++) {
    const url = ARTICLES[i];
    process.stderr.write(`[${i+1}/${ARTICLES.length}] Fetching: ${url.split('/').slice(-2,-1)[0]}\n`);
    const r = await fetchArticle(url);
    results.push(r);
    if (r.success) {
      process.stderr.write(`  -> OK: ${r.title?.substring(0,60)}\n`);
    } else {
      process.stderr.write(`  -> ERROR: ${r.error}\n`);
    }
    await new Promise(r => setTimeout(r, 3000));
  }
  
  fs.writeFileSync('/home/matt/.openclaw/workspace/TECH/news_content_0719.json', JSON.stringify(results, null, 2));
  process.stderr.write('Done! Saved to news_content_0719.json\n');
}

main().catch(e => { console.error(e); process.exit(1); });
