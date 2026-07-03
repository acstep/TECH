const puppeteer = require('puppeteer-core');
const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36';

async function fetch(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({width:1280,height:900});
  await page.setUserAgent(UA);
  try {
    await page.goto(url, {waitUntil:'networkidle2', timeout:30000});
    await new Promise(r=>setTimeout(r,8000));
    const data = await page.evaluate(()=>{
      const title = document.querySelector('h1')?.textContent?.trim()||'';
      const time = document.querySelector('time')?.dateTime||'';
      const paras = Array.from(document.querySelectorAll('p')).map(p=>p.textContent.trim()).filter(t=>t.length>50);
      return {title, time, content: paras.slice(0,12).join(' ').substring(0,1200)};
    });
    await browser.close();
    return {url, ...data, success:true};
  } catch(e) {
    await browser.close();
    return {url, error:e.message, success:false};
  }
}

const urls = [
  'https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/',
  'https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/',
  'https://techcrunch.com/2026/07/02/openai-proposed-donating-5-of-its-equity-to-a-us-sovereign-wealth-fund/',
  'https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/',
  'https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/',
  'https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/',
  'https://techcrunch.com/2026/07/01/indian-tech-tycoon-bets-30m-to-build-an-ai-alternative-to-microsoft-office/',
  'https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/',
  'https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/',
  'https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/',
  'https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/',
  'https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/',
  'https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/',
  'https://techcrunch.com/2026/07/02/spacex-has-an-ai-device-prototype-and-it-sure-sounds-phone-ish/',
  'https://techcrunch.com/2026/07/02/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/',
  'https://techcrunch.com/2026/07/02/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/',
];

async function main() {
  const results = [];
  for (const url of urls) {
    process.stderr.write('Fetching: ' + url.split('/').slice(-2,-1) + '\n');
    const r = await fetch(url);
    results.push(r);
    if(r.success) {
      process.stderr.write('  OK: ' + r.title.substring(0,60) + '\n');
    } else {
      process.stderr.write('  ERR: ' + r.error.substring(0,80) + '\n');
    }
    await new Promise(r=>setTimeout(r,2000));
  }
  process.stdout.write(JSON.stringify(results, null, 2));
}
main().catch(e=>{console.error(e);process.exit(1);});
