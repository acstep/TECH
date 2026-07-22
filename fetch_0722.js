const puppeteer = require('puppeteer-core');
const fs = require('fs');

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
  'generative', 'nvidia', 'amd', 'gpu', 'chip', 'inference', 'training',
  'anthropic', 'mistral', 'xai', 'grok', 'hugging face',
  'agent', 'model', 'voice', 'image generation', 'text to',
  'techcrunch', 'startup', 'funding', 'valuation', 'billion', 'million',
  'server', 'data center',
  'satya nadella', 'sam altman', 'demis hassabis', 'dario amodei',
  'apple', 'siri', 'meta', 'instagram', 'google', 'microsoft', 'copilot',
  'robotics', 'autonomous', 'self-driving', 'robot', 'automation',
  'agent', 'reasoning', 'frontier', 'safety', 'regulation', 'policy',
  'equity', 'justice', 'copyright', 'patent', 'lawsuit', 'settlement'
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
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.setUserAgent(UA);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 5000));
    
    const articles = await page.evaluate(() => {
      const results = [];
      document.querySelectorAll('a[href*="/2026/"]').forEach(el => {
        const href = el.href;
        const text = el.textContent?.trim() || '';
        if (text.length > 20 && text.length < 300 && href.includes('techcrunch.com/202')) {
          results.push({ title: text, link: href.split('?')[0] });
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
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.setUserAgent(UA);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
    await new Promise(r => setTimeout(r, 3000));
    
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      const paras = Array.from(document.querySelectorAll('article p, .article-body p, .post-content p, .wp-block-post-content p, main p'))
        .map(p => p.textContent.trim())
        .filter(t => t.length > 80)
        .slice(0, 8);
      const content = paras.join(' ').substring(0, 2500);
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
  
  // Collect all articles
  for (const url of SOURCES) {
    process.stderr.write(`Fetching: ${url}\n`);
    const result = await fetchArticleList(url);
    if (result.success) {
      for (const art of result.articles) {
        const key = art.link.split('?')[0];
        if (!seen.has(key)) seen.set(key, art);
      }
      process.stderr.write(`  -> ${result.articles.length} found\n`);
    } else {
      process.stderr.write(`  -> Error: ${result.error}\n`);
    }
    await new Promise(r => setTimeout(r, 1000));
  }
  
  // Filter July 22, 2026 + AI related
  let candidates = Array.from(seen.values()).filter(a => {
    if (!a.link.includes('/2026/')) return false;
    // Match July 22 (day 22)
    const m = a.link.match(/\/2026\/(\d{2})\/(\d{2})\//);
    if (!m) return false;
    const month = parseInt(m[1]);
    const day = parseInt(m[2]);
    return month === 7 && day === 22;
  }).filter(a => isAIRelated(a.title));
  
  // Dedupe
  const keys = new Set();
  candidates = candidates.filter(a => {
    const k = a.link.split('?')[0];
    if (keys.has(k)) return false;
    keys.add(k); return true;
  });
  
  // Sort newest first
  candidates.sort((a, b) => {
    const ma = a.link.match(/\/2026\/(\d{2})\/(\d{2})\//);
    const mb = b.link.match(/\/2026\/(\d{2})\/(\d{2})\//);
    return (mb && ma ? (mb[2] - ma[2]) : 0);
  });
  
  process.stderr.write(`\nTotal AI articles July 22: ${candidates.length}\n`);
  fs.writeFileSync('/tmp/tc_0722_raw.json', JSON.stringify(candidates, null, 2));
  
  // Also keep July 21 for reference (might be late posts)
  let candidates21 = Array.from(seen.values()).filter(a => {
    if (!a.link.includes('/2026/')) return false;
    const m = a.link.match(/\/2026\/(\d{2})\/(\d{2})\//);
    if (!m) return false;
    const month = parseInt(m[1]);
    const day = parseInt(m[2]);
    return month === 7 && day === 21;
  }).filter(a => isAIRelated(a.title));
  
  const keys21 = new Set();
  candidates21 = candidates21.filter(a => {
    const k = a.link.split('?')[0];
    if (keys21.has(k)) return false;
    keys21.add(k); return true;
  });
  
  process.stderr.write(`Total AI articles July 21 (backup): ${candidates21.length}\n`);
  
  // Combine
  const allCandidates = [...candidates];
  for (const c of candidates21) {
    if (!allCandidates.find(x => x.link === c.link)) {
      allCandidates.push(c);
    }
  }
  
  // Fetch content for all articles
  const results = [];
  for (let i = 0; i < allCandidates.length; i++) {
    const art = allCandidates[i];
    process.stderr.write(`[${i+1}/${allCandidates.length}] ${art.title.substring(0, 60)}...\n`);
    const r = await fetchArticleContent(art.link);
    r.title = art.title;
    results.push(r);
    if (r.success) {
      process.stderr.write(`  OK (content: ${r.content?.length || 0} chars)\n`);
    } else {
      process.stderr.write(`  ERR: ${r.error}\n`);
    }
    
    if ((i + 1) % 5 === 0) {
      fs.writeFileSync('/tmp/tc_0722_partial.json', JSON.stringify(results, null, 2));
    }
    await new Promise(r => setTimeout(r, 1200));
  }
  
  fs.writeFileSync('/tmp/tc_0722_full.json', JSON.stringify(results, null, 2));
  process.stderr.write(`\nDone! Saved ${results.length} articles\n`);
  process.stdout.write(JSON.stringify(results, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
