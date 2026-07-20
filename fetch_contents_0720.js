const https = require('https');

const ARTICLES = [
  { url: "https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/", title: "Can an Apple lawsuit derail OpenAI's hardware plans?", time: "2026-07-19T12:24:45-07:00" },
  { url: "https://techcrunch.com/2026/07/19/odyssey-director-christopher-nolan-calls-ai-an-obvious-trojan-horse/", title: "'Odyssey' director Christopher Nolan calls AI an obvious 'Trojan horse'", time: "2026-07-19T07:52:08-07:00" },
  { url: "https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/", title: "Nonprofit Current AI is racing to build the World Wide Web of AI, free for all", time: "2026-07-19T07:00:00-07:00" },
  { url: "https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/", title: "Neil Rimer thinks the AI money is coming back out", time: "2026-07-17T21:47:25-07:00" },
  { url: "https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/", title: "Vertu wants executives to pay $6,880 for an AI agent — here's how it actually performs", time: "2026-07-17T15:55:09-07:00" },
  { url: "https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/", title: "Databricks hits $188B valuation, extending its run as AI's favorite second act", time: "2026-07-17T15:12:56-07:00" },
  { url: "https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/", title: "Agility Robotics plants its flag in Tesla's backyard", time: "2026-07-17T13:19:49-07:00" },
  { url: "https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/", title: "AI-driven memory crunch jolts India's smartphone market", time: "2026-07-17T13:09:27-07:00" },
  { url: "https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/", title: "Patreon stops asking AI bots not to scrape — and starts blocking them", time: "2026-07-17T08:21:17-07:00" },
  { url: "https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/", title: "Why the first GPU financiers are turning to inference chips in a $400 million deal", time: "2026-07-17T05:00:00-07:00" },
  { url: "https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/", title: "Google Vids now lets you star in your own AI videos", time: "2026-07-16T11:32:54-07:00" },
  { url: "https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/", title: "Roblox launches an AI-powered game-creation feature in its mobile app", time: "2026-07-16T11:22:06-07:00" },
  { url: "https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/", title: "Google's AI Mode now lets you link and interact with select apps", time: "2026-07-16T09:00:00-07:00" },
  { url: "https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/", title: "Why is OpenAI selling a ChatGPT basketball?", time: "2026-07-16T08:31:09-07:00" },
  { url: "https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/", title: "How a former DeepMind researcher raised at a $300M pre-seed valuation before launching a product", time: "2026-07-16T08:02:00-07:00" },
  { url: "https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/", title: "Why AMI Labs' Alexandre LeBrun won't call his AI 'AGI' or 'superintelligence'", time: "2026-07-16T07:40:00-07:00" },
  { url: "https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/", title: "Moonshot's upcoming Kimi 3 is expected to close the gap with Anthropic's Opus 4.8", time: "2026-07-16T07:26:29-07:00" },
  { url: "https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/", title: "Apple Intelligence approved for launch in China with Alibaba and Baidu", time: "2026-07-16T06:17:59-07:00" },
  { url: "https://techcrunch.com/2026/07/15/applied-computing-wants-to-give-oil-and-gas-operators-an-ai-model-for-the-entire-plant/", title: "Applied Computing wants to give oil and gas operators an AI model for the entire plant", time: "2026-07-15T21:00:00-07:00" },
  { url: "https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/", title: "Microsoft is reportedly training salespeople to talk down OpenAI and Anthropic", time: "2026-07-15T16:59:44-07:00" },
  { url: "https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/", title: "Amid hardware legal battle, OpenAI releases a $230 keyboard for Codex", time: "2026-07-15T12:41:38-07:00" },
  { url: "https://techcrunch.com/2026/07/16/coca-cola-suspended-production-at-its-fairlife-dairy-after-a-ransomware-attack/", title: "Coca-Cola suspended production at its Fairlife dairy after a ransomware attack", time: "2026-07-16T14:22:31-07:00" },
  { url: "https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/", title: "Anthropic, Blackstone bet the next trillion-dollar AI business is implementation, not just models", time: "2026-07-15T06:10:47-07:00" },
  { url: "https://techcrunch.com/2026/07/14/openais-first-hardware-device-is-reportedly-a-screenless-speaker-that-can-move/", title: "OpenAI's first hardware device is reportedly a screenless speaker that can move", time: "2026-07-14T15:22:24-07:00" },
  { url: "https://techcrunch.com/2026/07/14/anthropics-newest-ad-is-creeping-people-out/", title: "Anthropic's newest ad is creeping people out", time: "2026-07-14T12:41:27-07:00" },
  { url: "https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/", title: "Satya Nadella has issued a shocking warning to companies using AI", time: "2026-07-13T13:59:00-07:00" },
  { url: "https://techcrunch.com/2026/07/19/techcrunch-mobility-the-battle-over-robotaxi-rules/", title: "TechCrunch Mobility: The battle over robotaxi rules", time: "2026-07-19T09:05:00-07:00" },
  { url: "https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/", title: "Netflix paid $587M for Ben Affleck's AI filmmaking startup", time: "2026-07-19T14:45:00-07:00" },
  { url: "https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/", title: "Federal employees can download TikTok on their work phones again", time: "2026-07-18T08:54:24-07:00" },
  { url: "https://techcrunch.com/2026/07/17/applications-close-in-48-hours-heres-everything-australian-founders-need-to-know-about-stripe-x-startup-battlefield/", title: "Applications close in 48 hours — here's everything Australian founders need to know about Stripe x Startup Battlefield", time: "2026-07-17T16:08:00-07:00" },
];

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

function extractText(html) {
  // Simple HTML tag stripper
  return html
    .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
    .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

async function main() {
  const results = [];
  for (const art of ARTICLES) {
    process.stderr.write(`Fetching: ${art.title.substring(0, 60)}...\n`);
    try {
      const html = await fetchUrl(art.url);
      const text = extractText(html);
      // Find main content - look for article body
      const articleMatch = text.match(/Apple recently filed a trade secrets lawsuit[\s\S]{100,3000}/);
      results.push({
        ...art,
        content: articleMatch ? articleMatch[0].substring(0, 2000) : text.substring(0, 2000),
        success: true
      });
    } catch(e) {
      results.push({ ...art, content: '', error: e.message, success: false });
    }
    await new Promise(r => setTimeout(r, 500));
  }
  process.stdout.write(JSON.stringify(results, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
