const puppeteer = require('puppeteer-core');
const https = require('https');

const CHROME = '/usr/bin/google-chrome-stable';
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36';

const articles = [
  { title: "Meta removes controversial AI feature on Instagram after backlash", link: "https://techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/" },
  { title: "Apple sues OpenAI over alleged trade secret theft", link: "https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/" },
  { title: "SK Hynix raises $26.5B in the biggest foreign IPO in US history, is urged to build new US fabs", link: "https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/" },
  { title: "Hugging Face's CEO on why companies are done renting their AI", link: "https://techcrunch.com/2026/07/10/hugging-faces-ceo-on-why-companies-are-done-renting-their-ai/" },
  { title: "OpenAI says GPT 5.6 is the 'preferred model' for Microsoft Copilot 365 amid breach", link: "https://techcrunch.com/2026/07/10/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-365-amid-breach/" },
  { title: "Fidji Simo steps down from OpenAI's No. 2 role", link: "https://techcrunch.com/2026/07/10/fidji-simo-steps-down-from-openais-no-2-role/" },
  { title: "OpenAI launches its new family of models with GPT-5.6", link: "https://techcrunch.com/2026/07/10/openai-launches-its-new-family-of-models-with-gpt-5-6/" },
  { title: "An AI agent startup just let its agent run its $100M fundraise", link: "https://techcrunch.com/2026/07/10/an-ai-agent-startup-just-let-its-agent-run-its-100m-fundraise/" },
  { title: "OpenAI is shutting down Atlas, but its AI browser ambitions are still growing", link: "https://techcrunch.com/2026/07/10/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/" },
  { title: "Elon Musk praises Mythos/Fable, promises not to 'cut off' Anthropic", link: "https://techcrunch.com/2026/07/10/elon-musk-praises-mythos-fable-promises-not-to-cut-off-anthropic/" },
  { title: "Can AI answer the $3 trillion question?", link: "https://techcrunch.com/2026/07/10/can-ai-answer-the-3-trillion-question/" },
  { title: "Meta enters the crowded AI coding battle with Muse Spark 1.1", link: "https://techcrunch.com/2026/07/10/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/" },
  { title: "New York Times says OpenAI hid evidence in ChatGPT copyright trial", link: "https://techcrunch.com/2026/07/10/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/" },
  { title: "Google will now disclose which ads are made with AI", link: "https://techcrunch.com/2026/07/10/google-will-now-disclose-which-ads-are-made-with-ai/" },
  { title: "Paris-based AI voice startup Gradium raises $100M seed, backed by Nvidia", link: "https://techcrunch.com/2026/07/10/paris-based-ai-voice-startup-gradium-raises-100m-seed-backed-by-nvidia/" },
  { title: "How did the government decide OpenAI's frontier model was safe to release?", link: "https://techcrunch.com/2026/07/10/how-did-the-government-decide-openais-frontier-model-was-safe-to-release/" },
  { title: "Instagram users: Here's how to stop Meta's AI from using your photos", link: "https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/" },
  { title: "Meta's new AI chips will begin production in September", link: "https://techcrunch.com/2026/07/10/metas-new-ai-chips-will-begin-production-in-september/" },
  { title: "Nvidia is a victim of the compute marketplace it created", link: "https://techcrunch.com/2026/07/10/nvidia-is-a-victim-of-the-compute-marketplace-it-created/" },
  { title: "Anthropic's new Claude feature is quietly selling you on AI", link: "https://techcrunch.com/2026/07/10/anthropics-new-claude-feature-is-quietly-selling-you-on-ai/" },
  { title: "Anthropic, OpenAI, and SpaceX are bigger than the last 25 years of tech exits", link: "https://techcrunch.com/2026/07/10/anthropic-openai-and-spacex-are-bigger-than-the-last-25-years-of-tech-exits/" },
  { title: "Popular open source AI developer tool Ollama raises $65M, grows to nearly 9M users", link: "https://techcrunch.com/2026/07/10/popular-open-source-ai-developer-tool-ollama-raises-65m-grows-to-nearly-9m-users/" },
  { title: "Character.AI enters the microdrama arena with its own productions", link: "https://techcrunch.com/2026/07/10/character-ai-enters-the-microdrama-arena-with-its-own-productions-but-theres-a-problem/" },
  { title: "Lovable reportedly in talks to double its valuation to $13.2B", link: "https://techcrunch.com/2026/07/10/lovable-reportedly-in-talks-to-double-its-valuation-to-13-2b/" },
  { title: "SpaceXAI releases Grok 4.5, which Elon describes as an 'Opus-class model'", link: "https://techcrunch.com/2026/07/10/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/" },
];

async function fetchContent(url) {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.setUserAgent(UA);
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
    await new Promise(r => setTimeout(r, 4000));
    
    const data = await page.evaluate(() => {
      // Try multiple selectors for article body
      let content = '';
      const selectors = [
        'article .article-body',
        'article .post-content',
        'article .entry-content',
        '.article-body',
        '.post-content',
        '[class*="article-body"]',
        '[class*="post-content"]',
        'article',
      ];
      
      for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el) {
          const paras = Array.from(el.querySelectorAll('p'))
            .map(p => p.textContent.trim())
            .filter(t => t.length > 50);
          if (paras.length > 0) {
            content = paras.slice(0, 10).join(' ').substring(0, 2000);
            break;
          }
        }
      }
      
      // Fallback
      if (!content) {
        const paras = Array.from(document.querySelectorAll('p'))
          .map(p => p.textContent.trim())
          .filter(t => t.length > 50);
        content = paras.slice(0, 10).join(' ').substring(0, 2000);
      }
      
      return { content };
    });
    
    await browser.close();
    return { url, ...data, success: true };
  } catch(e) {
    await browser.close();
    return { url, error: e.message, success: false };
  }
}

async function main() {
  const results = [];
  
  for (const art of articles) {
    process.stderr.write(`Fetching: ${art.title.substring(0, 60)}...\n`);
    const r = await fetchContent(art.link);
    results.push({ title: art.title, link: art.link, ...r });
    if (r.success) {
      process.stderr.write(`  OK: ${(r.content||'').substring(0,80)}\n`);
    } else {
      process.stderr.write(`  ERR: ${r.error}\n`);
    }
    await new Promise(r => setTimeout(r, 2500));
  }
  
  process.stdout.write(JSON.stringify(results, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
