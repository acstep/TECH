const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const SOURCES = [
  'https://techcrunch.com/category/artificial-intelligence/',
  'https://techcrunch.com/',
  'https://techcrunch.com/tag/ai/',
  'https://techcrunch.com/tag/artificial-intelligence/',
  'https://techcrunch.com/tag/machine-learning/',
  'https://techcrunch.com/tag/openai/',
  'https://techcrunch.com/tag/google-deepmind/',
  'https://techcrunch.com/tag/generative-ai/',
  'https://techcrunch.com/tag/chatgpt/',
  'https://techcrunch.com/tag/llm/',
];

async function fetchArticles(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--single-process']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
    await new Promise(r => setTimeout(r, 3000));
    
    const articles = await page.evaluate(() => {
      // Try multiple selectors to find articles
      const results = [];
      
      // Main article cards on category pages
      document.querySelectorAll('article.post-block, article.river-block, .post-block, .wp-block-articlesriver article').forEach(el => {
        const titleEl = el.querySelector('h2 a, h3 a, .post-block__title__link');
        const timeEl = el.querySelector('time, .post-block__meta time');
        const link = titleEl?.href || '';
        const title = titleEl?.textContent?.trim() || '';
        const time = timeEl?.dateTime || timeEl?.textContent?.trim() || '';
        if (title && link) results.push({ title, link, time, source: 'tc-category' });
      });
      
      // River block articles (older format)
      document.querySelectorAll('.river-block .river-block__title a, .river-block h2 a').forEach(el => {
        const href = el.href;
        const text = el.textContent.trim();
        const parent = el.closest('article, .river-block');
        const timeEl = parent?.querySelector('time');
        const time = timeEl?.dateTime || timeEl?.textContent?.trim() || '';
        if (text && href) results.push({ title: text, link: href, time, source: 'tc-river' });
      });
      
      // Fallback: any link that looks like article
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 200 && href.includes('techcrunch.com/202')) {
          results.push({ title: text, link: href, time: '', source: 'tc-link' });
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
    console.error(`Fetching: ${url}`);
    const result = await fetchArticles(url);
    if (result.success) {
      for (const art of result.articles) {
        const key = art.link.split('?')[0];
        if (!seen.has(key)) {
          seen.set(key, art);
        }
      }
      console.error(`  -> Found ${result.articles.length} articles`);
    } else {
      console.error(`  -> Error: ${result.error}`);
    }
    await new Promise(r => setTimeout(r, 2000));
  }
  
  const all = Array.from(seen.values());
  console.log(JSON.stringify(all, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
