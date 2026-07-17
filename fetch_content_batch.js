const puppeteer = require('puppeteer-core');
const fs = require('fs');
const https = require('https');
const http = require('http');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36';

async function fetchArticleContent(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer', '--disable-extensions']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 25000 });
    await new Promise(r => setTimeout(r, 6000));
    
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || 
                    document.querySelector('[data-test="article-title"]')?.textContent?.trim() || '';
      
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      
      // Try many paragraph selectors
      let paras = [];
      const selectors = [
        '.article-body p',
        '.post-content p', 
        '.entry-content p',
        '.article__body p',
        '.story-body p',
        'article p',
        '[class*="article"] p',
        '[class*="post"] p',
        '[class*="content"] p',
        'main p',
        '#main-content p'
      ];
      
      for (const sel of selectors) {
        paras = Array.from(document.querySelectorAll(sel))
          .map(p => p.textContent.trim())
          .filter(t => t.length > 80);
        if (paras.length >= 3) break;
      }
      
      // Fallback: all p tags with substantial content
      if (paras.length < 3) {
        paras = Array.from(document.querySelectorAll('p'))
          .map(p => p.textContent.trim())
          .filter(t => t.length > 100)
          .slice(0, 10);
      }
      
      const content = paras.join(' ').substring(0, 3000);
      return { title, time, content, parasFound: paras.length };
    });
    
    await browser.close();
    return { url, ...data, success: true };
  } catch(e) {
    await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  // Load the article list
  const raw = fs.readFileSync('/home/matt/.openclaw/workspace/TECH/news_data_0717.json', 'utf8');
  const articles = JSON.parse(raw);
  
  console.error(`Fetching content for ${articles.length} articles...`);
  
  const results = [];
  for (let i = 0; i < articles.length; i++) {
    const art = articles[i];
    console.error(`[${i+1}/${articles.length}] ${art.title.substring(0, 60)}`);
    const r = await fetchArticleContent(art.url);
    r.originalTitle = art.title;
    r.originalTime = art.time;
    results.push(r);
    if (r.success) {
      console.error(`  OK (${r.parasFound} paras, ${(r.content||'').length} chars)`);
    } else {
      console.error(`  ERR: ${r.error}`);
    }
    // Short delay between articles
    await new Promise(r => setTimeout(r, 1000));
  }
  
  fs.writeFileSync('/home/matt/.openclaw/workspace/TECH/news_content_0717.json', JSON.stringify(results, null, 2));
  console.error(`\nDone! Saved ${results.length} articles`);
}

main().catch(e => { console.error(e); process.exit(1); });
