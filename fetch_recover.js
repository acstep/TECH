const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36';
const OUT_FILE = '/home/matt/.openclaw/workspace/TECH/news_content_0717.json';

async function fetchArticleContent(url, originalTitle, originalTime) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 25000 });
    await new Promise(r => setTimeout(r, 6000));
    
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      let paras = [];
      const selectors = [
        '.article-body p', '.post-content p', '.entry-content p',
        '.article__body p', '.story-body p', 'article p',
        '[class*="article"] p', '[class*="post"] p',
        '[class*="content"] p', 'main p', '#main-content p'
      ];
      for (const sel of selectors) {
        paras = Array.from(document.querySelectorAll(sel))
          .map(p => p.textContent.trim())
          .filter(t => t.length > 80);
        if (paras.length >= 3) break;
      }
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
    return { url, title: data.title || originalTitle, time: data.time || originalTime, content: data.content, success: true, originalTitle, originalTime };
  } catch(e) {
    await browser.close();
    return { url, originalTitle, originalTime, error: e.message, success: false };
  }
}

async function main() {
  // Load the list file
  const raw = fs.readFileSync('/home/matt/.openclaw/workspace/TECH/news_data_0717.json', 'utf8');
  const articles = JSON.parse(raw);
  
  // Articles 1-21 were fetched (21 OK from log)
  // Article 22 failed - need to refetch it
  const failed = articles[21]; // 0-indexed, article 22
  
  process.stderr.write(`Re-fetching failed article 22: ${failed.title.substring(0,60)}\n`);
  const r = await fetchArticleContent(failed.url, failed.title, failed.time);
  process.stderr.write(`Result: ${r.success ? 'OK' : 'ERR: ' + r.error}\n`);
  
  // For articles 1-21, we need to reconstruct from log
  // Let's just rebuild from scratch - fetch all content again but faster
  // Actually, let me check if I can write a simpler approach: 
  // fetch all 22 articles fresh but use shorter delays and a fresh browser
  
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  
  const results = [];
  
  for (let i = 0; i < articles.length; i++) {
    const art = articles[i];
    if (i === 21) {
      // Already fetched above, skip or use result
      process.stderr.write(`[${i+1}/22] Already fetched article 22, using cached result\n`);
      results.push(r);
      continue;
    }
    process.stderr.write(`[${i+1}/22] ${art.title.substring(0,50)}...\n`);
    const resp = await fetchArticleContent(art.url, art.title, art.time);
    results.push(resp);
    if (resp.success) {
      process.stderr.write(`  OK (${resp.parasFound} paras)\n`);
    } else {
      process.stderr.write(`  ERR: ${resp.error}\n`);
    }
    await new Promise(res => setTimeout(res, 800));
  }
  
  await browser.close();
  
  fs.writeFileSync(OUT_FILE, JSON.stringify(results, null, 2));
  process.stderr.write(`\nSaved ${results.length} articles to ${OUT_FILE}\n`);
  
  const ok = results.filter(x => x.success).length;
  process.stderr.write(`Success: ${ok}/${results.length}\n`);
}

main().catch(e => { console.error(e); process.exit(1); });
