const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME = '/usr/bin/google-chrome-stable';

const SOURCES = [
  'https://techcrunch.com/category/artificial-intelligence/',
  'https://techcrunch.com/',
  'https://techcrunch.com/tag/ai/',
  'https://techcrunch.com/tag/artificial-intelligence/',
  'https://techcrunch.com/tag/machine-learning/',
  'https://techcrunch.com/tag/openai/',
  'https://techcrunch.com/tag/google-deepmind/',
];

async function scrape() {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    headless: true,
  });

  const results = [];

  for (const url of SOURCES) {
    console.error(`Fetching: ${url}`);
    const page = await browser.newPage();
    try {
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
      await new Promise(r => setTimeout(r, 2000));

      const articles = await page.evaluate(() => {
        const items = [];
        // Try multiple selectors for TechCrunch article cards
        const cards = document.querySelectorAll('.post-block, .loop-card, article.post, .river-post, .story-card');
        cards.forEach(card => {
          const titleEl = card.querySelector('h2 a, h3 a, .post-block__title a, .loop-card__title a, .story-card__title a, .entry-title a') || 
                          card.querySelector('a.post-block__title-link') ||
                          card.querySelector('a');
          const href = titleEl ? titleEl.href : null;
          const title = titleEl ? titleEl.textContent.trim() : null;
          const timeEl = card.querySelector('time, .post-block__time, .loop-card__time, .story-card__time') || 
                         card.querySelector('[datetime]');
          const datetime = timeEl ? (timeEl.getAttribute('datetime') || timeEl.textContent.trim()) : null;
          const excerptEl = card.querySelector('.post-block__excerpt, .loop-card__excerpt, .story-card__excerpt, .entry-summary, p') ||
                           card.querySelector('.post-block__desc');
          const excerpt = excerptEl ? excerptEl.textContent.trim() : null;
          
          if (title && href && href.includes('techcrunch.com') && !href.includes('/video/') && !href.includes('/category/')) {
            items.push({ title, href, datetime, excerpt, source: window.location.href });
          }
        });
        return items;
      });

      if (articles.length > 0) {
        results.push(...articles.map(a => ({ ...a, sourceUrl: url })));
        console.error(`  Found ${articles.length} articles`);
      } else {
        // Fallback: try to get links from the page
        const links = await page.evaluate(() => {
          const items = [];
          const allLinks = document.querySelectorAll('a[href*="techcrunch.com/202"]');
          allLinks.forEach(a => {
            const title = a.textContent.trim();
            const href = a.href;
            if (title.length > 10 && title.length < 300 && href.includes('/202')) {
              items.push({ title, href, source: window.location.href });
            }
          });
          // Dedupe
          const seen = new Set();
          return items.filter(i => {
            if (seen.has(i.href)) return false;
            seen.add(i.href);
            return true;
          });
        });
        if (links.length > 0) {
          results.push(...links.map(l => ({ ...l, sourceUrl: url })));
          console.error(`  Fallback found ${links.length} links`);
        } else {
          console.error(`  No articles found`);
        }
      }
    } catch (e) {
      console.error(`  Error: ${e.message}`);
    }
    await page.close();
  }

  await browser.close();

  // Dedupe by href
  const seen = new Set();
  const deduped = results.filter(r => {
    if (seen.has(r.href)) return false;
    seen.add(r.href);
    return true;
  });

  console.log(JSON.stringify(deduped, null, 2));
}

scrape().catch(e => { console.error(e); process.exit(1); });
