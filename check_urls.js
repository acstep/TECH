const puppeteer = require('puppeteer-core');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const urls = [
  { title: "OpenAI says GPT 5.6 is the 'preferred model'", link: "https://techcrunch.com/2026/07/10/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-365-amid-breach/" },
  { title: "Fidji Simo steps down", link: "https://techcrunch.com/2026/07/10/fidji-simo-steps-down-from-openais-no-2-role/" },
  { title: "OpenAI launches GPT-5.6", link: "https://techcrunch.com/2026/07/10/openai-launches-its-new-family-of-models-with-gpt-5-6/" },
  { title: "OpenAI shuts down Atlas", link: "https://techcrunch.com/2026/07/10/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/" },
  { title: "Elon Musk Mythos/Fable", link: "https://techcrunch.com/2026/07/10/elon-musk-praises-mythos-fable-promises-not-to-cut-off-anthropic/" },
  { title: "AI $3 trillion", link: "https://techcrunch.com/2026/07/10/can-ai-answer-the-3-trillion-question/" },
  { title: "Meta Muse Spark 1.1", link: "https://techcrunch.com/2026/07/10/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/" },
  { title: "NYT OpenAI evidence", link: "https://techcrunch.com/2026/07/10/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/" },
  { title: "Google AI ads", link: "https://techcrunch.com/2026/07/10/google-will-now-disclose-which-ads-are-made-with-ai/" },
  { title: "Gradium $100M", link: "https://techcrunch.com/2026/07/10/paris-based-ai-voice-startup-gradium-raises-100m-seed-backed-by-nvidia/" },
  { title: "Govt OpenAI model", link: "https://techcrunch.com/2026/07/10/how-did-the-government-decide-openais-frontier-model-was-safe-to-release/" },
  { title: "Meta AI chips Sept", link: "https://techcrunch.com/2026/07/10/metas-new-ai-chips-will-begin-production-in-september/" },
  { title: "Nvidia compute", link: "https://techcrunch.com/2026/07/10/nvidia-is-a-victim-of-the-compute-marketplace-it-created/" },
  { title: "Anthropic Claude feature", link: "https://techcrunch.com/2026/07/10/anthropics-new-claude-feature-is-quietly-selling-you-on-ai/" },
  { title: "Anthropic, OpenAI, SpaceX", link: "https://techcrunch.com/2026/07/10/anthropic-openai-and-spacex-are-bigger-than-the-last-25-years-of-tech-exits/" },
  { title: "Ollama $65M", link: "https://techcrunch.com/2026/07/10/popular-open-source-ai-developer-tool-ollama-raises-65m-grows-to-nearly-9m-users/" },
  { title: "Character.AI microdrama", link: "https://techcrunch.com/2026/07/10/character-ai-enters-the-microdrama-arena-with-its-own-productions-but-theres-a-problem/" },
  { title: "Lovable $13.2B", link: "https://techcrunch.com/2026/07/10/lovable-reportedly-in-talks-to-double-its-valuation-to-13-2b/" },
  { title: "Grok 4.5", link: "https://techcrunch.com/2026/07/10/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/" },
  { title: "AI agent $100M", link: "https://techcrunch.com/2026/07/10/an-ai-agent-startup-just-let-its-agent-run-its-100m-fundraise/" },
];

async function checkUrl(art) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(art.link, { waitUntil: 'load', timeout: 15000 });
    await new Promise(r => setTimeout(r, 3000));
    
    const h1 = await page.evaluate(() => document.querySelector('h1')?.textContent?.trim() || 'NO_H1');
    const body = await page.evaluate(() => document.body?.textContent?.substring(0, 100) || '');
    
    await browser.close();
    return { title: art.title, link: art.link, h1, ok: !h1.includes('404') && !h1.includes('Page not found') };
  } catch(e) {
    await browser.close();
    return { title: art.title, link: art.link, error: e.message, ok: false };
  }
}

async function main() {
  const results = [];
  for (const art of urls) {
    const r = await checkUrl(art);
    results.push(r);
    console.log(`${r.ok ? 'OK' : 'ERR'}: ${art.title.substring(0, 50)} => h1: ${(r.h1||r.error||'').substring(0,50)}`);
    await new Promise(r => setTimeout(r, 2000));
  }
  console.log('\nSummary:', results.filter(r => r.ok).length, '/', results.length, 'accessible');
}

main().catch(e => { console.error(e); process.exit(1); });
