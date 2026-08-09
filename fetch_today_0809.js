const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const OUT_FILE = '/home/matt/.openclaw/workspace/TECH/news_raw_0809.json';
const CONTENT_FILE = '/home/matt/.openclaw/workspace/TECH/news_content_0809.json';

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
  'tts', 'speech', 'translation', 'cursor', 'github copilot', 'perplexity',
  'openai', 'anthropic', 'google deepmind', 'microsoft copilot', 'amazon ai',
  'ai safety', 'ai regulation', 'ai ethics', 'ai policy',
  'sam altman', 'dario amodei', 'jeff dean', 'jensen huang',
  'stability ai', 'stabilityai', 'ai chip', 'tpu', 'ai server',
  'ai infrastructure', 'data center', 'cloud ai', 'bedrock', 'azure openai',
  'amd', 'intel', 'qualcomm', 'deepfake', 'reasoning',
  'world model', 'ai startup', 'ai company', 'ai lab', 'ai VC', 'ai investment'
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
  'https://techcrunch.com/tag/ai-startup/',
  'https://techcrunch.com/tag/ai-funding/',
  'https://techcrunch.com/tag/artificial-intelligence/',
  'https://techcrunch.com/tag/machine-learning/',
  'https://techcrunch.com/tag/robotics/',
  'https://techcrunch.com/tag/ai-regulation/',
];

async function fetchArticleList(browser, url) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
    await new Promise(r => setTimeout(r, 5000));
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
            !href.includes('/strictlyvc/') &&
            !href.includes('/disrupt/') &&
            !href.includes('/tc-next/') &&
            !href.includes('/startup/') &&
            !href.includes('/startups/') &&
            !href.includes('/ebm/')) {
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
    return articles;
  } catch(e) {
    console.error(`Error fetching ${url}: ${e.message}`);
    await page.close().catch(()=>{});
    return [];
  }
}

async function fetchArticleContent(browser, url) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 4000));
    const content = await page.evaluate(() => {
      const selectors = [
        '.article-content', '.post-content', '.entry-content',
        '[class*="article-body"]', '[class*="post-body"]',
        'article', '.story-body'
      ];
      for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el) return el.textContent?.trim() || '';
      }
      return document.body.textContent?.trim().substring(0, 3000) || '';
    });
    const title = await page.evaluate(() => {
      const el = document.querySelector('h1');
      return el?.textContent?.trim() || '';
    });
    const published = await page.evaluate(() => {
      const el = document.querySelector('time') || document.querySelector('[class*="date"]');
      return el?.textContent?.trim() || '';
    });
    await page.close();
    return { title, content: content.substring(0, 4000), published };
  } catch(e) {
    await page.close().catch(()=>{});
    return null;
  }
}

async function main() {
  console.log('Starting TechCrunch AI news fetch for 2026-08-09...');
  
  const partialArticles = [];
  const partialContents = [];

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer', '--disable-accelerated-2d-canvas']
  });

  const allArticles = [...partialArticles];
  const seenLinks = new Set(allArticles.map(a => a.link));

  for (const source of SOURCES) {
    console.log(`Fetching article list: ${source}`);
    const articles = await fetchArticleList(browser, source);
    for (const a of articles) {
      if (!seenLinks.has(a.link)) {
        seenLinks.add(a.link);
        allArticles.push(a);
      }
    }
    fs.writeFileSync(OUT_FILE, JSON.stringify(allArticles, null, 2));
    await new Promise(r => setTimeout(r, 2000));
  }

  console.log(`Total unique articles found: ${allArticles.length}`);

  const now = Date.now();
  const oneDay = 24 * 60 * 60 * 1000;
  const filtered = allArticles.filter(a => {
    if (!isAIRelated(a.title)) return false;
    if (a.time) {
      const artTime = new Date(a.time).getTime();
      if (now - artTime > oneDay * 3) return false;
    }
    return true;
  });

  console.log(`AI-related articles (past 3 days): ${filtered.length}`);

  const fetchedLinks = new Set(partialContents.map(c => c.link));
  const toFetch = filtered.filter(a => !fetchedLinks.has(a.link)).slice(0, 40);
  console.log(`Fetching content for ${toFetch.length} new articles...`);

  for (const article of toFetch) {
    console.log(`  Fetching: ${article.title.substring(0, 60)}...`);
    const content = await fetchArticleContent(browser, article.link);
    if (content && content.content) {
      partialContents.push({ ...article, ...content, success: true });
    } else {
      partialContents.push({ ...article, success: false });
    }
    fs.writeFileSync(CONTENT_FILE, JSON.stringify(partialContents, null, 2));
    await new Promise(r => setTimeout(r, 1500));
  }

  await browser.close();
  console.log(`Done. Total raw: ${allArticles.length}, Content fetched: ${partialContents.filter(c=>c.success).length}`);
}

main().catch(console.error);
