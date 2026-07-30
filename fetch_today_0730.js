const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const OUT_FILE = '/home/matt/.openclaw/workspace/TECH/news_raw_0730.json';
const CONTENT_FILE = '/home/matt/.openclaw/workspace/TECH/news_content_0730.json';

const AI_KEYWORDS = [
  'ai', 'artificial intelligence', 'machine learning', 'deepmind', 'openai', 'chatgpt',
  'claude', 'gemini', 'llm', 'gpt', 'neural', 'nlp', 'computer vision',
  'generative', 'nvidia', 'gpu', 'chip', 'inference', 'training',
  'anthropic', 'mistral', 'xai', 'grok', 'hugging face',
  'agent', 'voice', 'image generation', 'stable diffusion', 'suno', 'udio',
  'robot', 'automation', 'model', 'startup', 'funding', 'valuation',
  'microsoft', 'google', 'meta', 'apple', 'amazon', 'softbank',
  'llm', 'rag', 'embedding', 'fine-tuning', 'reasoning',
  'stable diffusion', 'text-to-image', 'text-to-video', 'video generation',
  'robotics', 'self-driving', 'autonomous', 'ai agent', 'copilot',
  'tts', 'speech', 'translation', 'cursor', 'github copilot', 'perplexity'
];

function isAIRelated(title) {
  const lower = title.toLowerCase();
  return AI_KEYWORDS.some(kw => lower.includes(kw));
}

const SOURCES = [
  'https://techcrunch.com/category/artificial-intelligence/',
  'https://techcrunch.com/',
  'https://techcrunch.com/tag/ai/',
  'https://techcrunch.com/tag/openai/',
  'https://techcrunch.com/tag/generative-ai/',
  'https://techcrunch.com/tag/chatgpt/',
  'https://techcrunch.com/tag/google-deepmind/',
  'https://techcrunch.com/tag/anthropic/',
  'https://techcrunch.com/tag/machine-learning/',
  'https://techcrunch.com/tag/nvidia/',
  'https://techcrunch.com/tag/microsoft/',
];

async function fetchArticleList(browser, url) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 6000));
    const articles = await page.evaluate(() => {
      const results = [];
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 300 && 
            href.includes('techcrunch.com/202') &&
            !href.includes('/video/') &&
            !href.includes('/events/') &&
            !href.includes('/podcast/') &&
            !href.includes('/strictlyvc/')) {
          let time = '';
          let parent = el.closest('article, .post-block, .river-block, li, .wp-block');
          if (parent) {
            const timeEl = parent.querySelector('time');
            if (timeEl) time = timeEl.dateTime || timeEl.textContent?.trim() || '';
          }
          if (!time) {
            const m = href.match(/\/2026\/(\d+)\/(\d+)\//);
            if (m) time = `2026-${m[1]}-${m[2]}T00:00:00`;
          }
          results.push({ title: text, link: href, time });
        }
      });
      return results;
    });
    await page.close();
    return { url, articles, success: true };
  } catch(e) {
    await page.close();
    return { url, error: e.message, success: false };
  }
}

async function fetchArticleContent(browser, url) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
    await new Promise(r => setTimeout(r, 4000));
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      const author = document.querySelector('.author-name, .byline, [rel="author"]')?.textContent?.trim() || '';
      const paras = Array.from(document.querySelectorAll('article p, .article-body p, .post-content p, .entry-content p'))
        .map(p => p.textContent.trim())
        .filter(t => t.length > 80)
        .slice(0, 8);
      const content = paras.join(' ').substring(0, 3000);
      return { title, time, author, content };
    });
    await page.close();
    return { url, ...data, success: true };
  } catch(e) {
    await page.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  const seen = new Map();
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer']
  });

  for (const url of SOURCES) {
    process.stderr.write(`Fetching list: ${url}\n`);
    const result = await fetchArticleList(browser, url);
    if (result.success) {
      for (const art of result.articles) {
        const key = art.link.split('?')[0];
        if (!seen.has(key)) seen.set(key, art);
      }
      process.stderr.write(`  -> ${result.articles.length} articles\n`);
    } else {
      process.stderr.write(`  -> Error: ${result.error}\n`);
    }
    await new Promise(r => setTimeout(r, 3000));
  }

  await browser.close();
  fs.writeFileSync(OUT_FILE, JSON.stringify(Array.from(seen.values()), null, 2));

  // Filter July 29-30 (yesterday and today)
  const candidates = Array.from(seen.values()).filter(a => {
    if (!a.link.includes('/2026/')) return false;
    const m = a.link.match(/\/2026\/(\d+)\/(\d+)\//);
    if (!m) return false;
    const month = parseInt(m[1]);
    const day = parseInt(m[2]);
    if (month !== 7) return false;
    if (day < 29) return false; // July 29 or 30
    return isAIRelated(a.title);
  });

  const deduped = [];
  const dedupedKeys = new Set();
  for (const a of candidates) {
    const k = a.link.split('?')[0];
    if (!dedupedKeys.has(k)) {
      dedupedKeys.add(k);
      deduped.push(a);
    }
  }

  process.stderr.write(`\nAI articles from July 29-30: ${deduped.length}\n`);

  // Also grab July 28 as backup
  const candidates28 = Array.from(seen.values()).filter(a => {
    if (!a.link.includes('/2026/')) return false;
    const m = a.link.match(/\/2026\/(\d+)\/(\d+)\//);
    if (!m) return false;
    if (parseInt(m[1]) !== 7) return false;
    if (parseInt(m[2]) !== 28) return false;
    return isAIRelated(a.title);
  });
  process.stderr.write(`AI articles from July 28 (backup): ${candidates28.length}\n`);

  const allToFetch = [...deduped, ...candidates28].slice(0, 30);
  const results = [];
  const browser2 = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });

  for (const art of allToFetch) {
    process.stderr.write(`Fetching: ${art.title.substring(0, 50)}...\n`);
    const r = await fetchArticleContent(browser2, art.link);
    results.push(r);
    if (r.success) {
      process.stderr.write(`  OK: ${(r.title || art.title).substring(0, 60)}\n`);
    } else {
      process.stderr.write(`  ERR: ${r.error}\n`);
    }
    await new Promise(r => setTimeout(r, 2000));
  }

  await browser2.close();
  fs.writeFileSync(CONTENT_FILE, JSON.stringify(results, null, 2));
  process.stderr.write(`\nSaved ${results.length} articles to ${CONTENT_FILE}\n`);
}

main().catch(e => { console.error(e); process.exit(1); });
