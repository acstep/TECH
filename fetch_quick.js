const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36';
const OUT_FILE = '/home/matt/.openclaw/workspace/TECH/news_content_0717.json';

async function fetchOne(browser, url, originalTitle, originalTime) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
    await new Promise(r => setTimeout(r, 5000));
    const data = await page.evaluate(() => {
      const title = document.querySelector('h1')?.textContent?.trim() || '';
      const time = document.querySelector('time')?.dateTime || 
                   document.querySelector('time')?.textContent?.trim() || '';
      let paras = [];
      const sels = ['.article-body p','.post-content p','.entry-content p',
        '.article__body p','.story-body p','article p',
        '[class*="article"] p','main p','#main-content p'];
      for (const s of sels) {
        paras = Array.from(document.querySelectorAll(s))
          .map(p=>p.textContent.trim()).filter(t=>t.length>80);
        if(paras.length>=3) break;
      }
      if(paras.length<3) {
        paras = Array.from(document.querySelectorAll('p'))
          .map(p=>p.textContent.trim()).filter(t=>t.length>100).slice(0,8);
      }
      return {title, time, content: paras.join(' ').substring(0,2500), count: paras.length};
    });
    await page.close();
    return {url, title: data.title||originalTitle, time: data.time||originalTime, 
            content: data.content, success: true, originalTitle, originalTime};
  } catch(e) {
    await page.close();
    return {url, originalTitle, originalTime, error: e.message, success: false};
  }
}

async function main() {
  const raw = fs.readFileSync('/home/matt/.openclaw/workspace/TECH/news_data_0717.json', 'utf8');
  const articles = JSON.parse(raw);
  
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: true,
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-gpu']
  });
  
  const results = [];
  for(let i=0;i<articles.length;i++) {
    const a = articles[i];
    process.stderr.write(`[${i+1}/${articles.length}] ${a.title.substring(0,50)}...\n`);
    const r = await fetchOne(browser, a.url, a.title, a.time);
    results.push(r);
    if(r.success) process.stderr.write(`  OK (${r.content?.length||0} chars)\n`);
    else process.stderr.write(`  ERR: ${r.error}\n`);
    await new Promise(res=>setTimeout(res,1000));
  }
  
  await browser.close();
  fs.writeFileSync(OUT_FILE, JSON.stringify(results, null, 2));
  process.stderr.write(`\nDone! ${results.filter(x=>x.success).length}/${results.length} saved to ${OUT_FILE}\n`);
}

main().catch(e=>{console.error(e);process.exit(1);});
