const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36';

const SOURCES = [
  'https://techcrunch.com/category/artificial-intelligence/',
  'https://techcrunch.com/',
  'https://techcrunch.com/tag/ai/',
  'https://techcrunch.com/tag/artificial-intelligence/',
  'https://techcrunch.com/tag/openai/',
  'https://techcrunch.com/tag/google-deepmind/',
  'https://techcrunch.com/tag/generative-ai/',
  'https://techcrunch.com/tag/chatgpt/',
  'https://techcrunch.com/tag/llm/',
  'https://techcrunch.com/tag/machine-learning/',
];

const AI_KEYWORDS = [
  'ai', 'artificial intelligence', 'machine learning', 'deepmind', 'openai', 'chatgpt',
  'claude', 'gemini', 'llm', 'gpt', 'neural', 'nlp', 'computer vision',
  'generative', 'nvidia', 'gpu', 'chip', 'inference', 'training',
  'anthropic', 'mistral', 'xai', 'grok', 'baseten', 'hugging face',
  'agent', 'model', 'voice', 'image generation', 'text to',
  'techcrunch', 'startup', 'funding', 'valuation', 'billion', 'million',
  'nvidia', 'amd', 'intel', 'qualcomm', 't smc', 'server', 'data center'
];

function isAIRelated(title) {
  if (!title) return false;
  const lower = title.toLowerCase();
  return AI_KEYWORDS.some(kw => lower.includes(kw));
}

async function fetchArticleList(url) {
  let browser;
  try {
    browser = await puppeteer.launch({
      executablePath: CHROME,
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer', '--disable-extensions']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.setUserAgent(UA);
    await page.setRequestInterception(true);
    
    // Block images and css to speed up
    page.on('request', req => {
      if (['image', 'stylesheet', 'font'].includes(req.resourceType())) {
        req.abort();
      } else {
        req.continue();
      }
    });
    
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 5000));
    
    const articles = await page.evaluate(() => {
      const results = [];
      // Find all article links from 2026
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 300 && href.includes('techcrunch.com/202')) {
          const timeEl = el.closest('article, .post-block, .river-block, li, div')?.querySelector('time');
          const time = timeEl?.dateTime || timeEl?.textContent?.trim() || '';
          results.push({ title: text, link: href.split('?')[0], time });
        }
      });
      return results;
    });
    
    await browser.close();
    return { url, articles, success: true };
  } catch(e) {
    if (browser) await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function fetchArticleContent(url) {
  let browser;
  try {
    browser = await puppeteer.launch({
      executablePath: CHROME,
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.setUserAgent(UA);
    
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 4000));
    
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      const paras = Array.from(document.querySelectorAll('article p, .article-body p, .post-content p, .wp-block-post-content p'))
        .map(p => p.textContent.trim())
        .filter(t => t.length > 80)
        .slice(0, 8);
      const content = paras.join(' ').substring(0, 2000);
      return { title, time, content };
    });
    
    await browser.close();
    return { url, ...data, success: true };
  } catch(e) {
    if (browser) await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  const seen = new Map();
  
  for (const url of SOURCES) {
    process.stderr.write(`Fetching: ${url}\n`);
    const result = await fetchArticleList(url);
    if (result.success) {
      for (const art of result.articles) {
        const key = art.link.split('?')[0];
        if (!seen.has(key)) {
          seen.set(key, art);
        }
      }
      process.stderr.write(`  -> ${result.articles.length} found\n`);
    } else {
      process.stderr.write(`  -> Error: ${result.error}\n`);
    }
    await new Promise(r => setTimeout(r, 2000));
  }
  
  let candidates = Array.from(seen.values()).filter(a => {
    if (!a.link.includes('/2026/')) return false;
    if (!a.link.includes('/07/')) return false;
    return isAIRelated(a.title);
  });
  
  // Dedupe
  const deduped = [];
  const keys = new Set();
  for (const a of candidates) {
    const k = a.link.split('?')[0];
    if (!keys.has(k)) { keys.add(k); deduped.push(a); }
  }
  
  process.stderr.write(`\nTotal July 2026 AI articles: ${deduped.length}\n`);
  
  // Fetch content for top articles
  const top = deduped.slice(0, 25);
  const results = [];
  
  for (const art of top) {
    process.stderr.write(`Content: ${art.title.substring(0, 50)}...\n`);
    const r = await fetchArticleContent(art.link);
    results.push(r);
    if (r.success) {
      process.stderr.write(`  OK: ${r.title.substring(0, 60)}\n`);
    } else {
      process.stderr.write(`  ERR: ${r.error}\n`);
    }
    await new Promise(r => setTimeout(r, 2000));
  }
  
  process.stdout.write(JSON.stringify(results, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
