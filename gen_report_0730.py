import json, sys
sys.path.insert(0, '/home/matt/.openclaw/workspace/TECH')
from datetime import datetime

DATE = "2026-07-30"

with open('/home/matt/.openclaw/workspace/TECH/news_content_0730.json') as f:
    articles = json.load(f)

# Categories
CAT_EMOJI = {
    "💾 AI 晶片與硬體": "chip",
    "🧠 AI 模型與研究": "model",
    "🤖 AI 產品與應用": "product",
    "🏢 企業 AI 動態": "enterprise",
    "💰 AI 投融資與併購": "funding",
    "🏛️ AI 政策與監管": "policy",
    "👥 AI 人事與組織": "people",
    "🌍 AI 國際與地緣政治": "geo",
}

def categorize(article):
    title = article.get('title', '').lower()
    content = article.get('content', '').lower()
    text = title + ' ' + content
    
    cats = []
    if any(k in text for k in ['nvidia', 'gpu', 'chip', 'amd', 'intel', 'tsmc', 'compute', 'server', 'hardware']):
        cats.append("💾 AI 晶片與硬體")
    if any(k in text for k in ['model', 'research', 'paper', 'benchmark', 'llm', 'gpt', 'claude', 'gemini', 'openai', 'anthropic', 'hugging face', 'self-improve', 'agent']):
        cats.append("🧠 AI 模型與研究")
    if any(k in text for k in ['app', 'launch', 'product', 'browser', 'startup', 'feature', 'platform']):
        cats.append("🤖 AI 產品與應用")
    if any(k in text for k in ['enterprise', 'business', 'customer', 'azure', 'microsoft', 'meta', 'google', 'ceo', 'earnings', 'quarterly']):
        cats.append("🏢 企業 AI 動態")
    if any(k in text for k in ['raise', 'fund', 'invest', 'valuation', 'acqui', 'million', 'billion', 'seed', 'series']):
        cats.append("💰 AI 投融資與併購")
    if any(k in text for k in ['government', 'ban', 'fcc', 'regulation', 'law', 'congress', 'policy', 'security', 'national', 'scrutiny']):
        cats.append("🏛️ AI 政策與監管")
    if any(k in text for k in ['hire', 'join', 'left', 'quit', 'ceo', 'founder', 'co-founder', 'departure', 'resign']):
        cats.append("👥 AI 人事與組織")
    if any(k in text for k in ['china', 'foreign', 'export', 'geopolitics', 'taiwan', 'trump']):
        cats.append("🌍 AI 國際與地緣政治")
    
    if not cats:
        cats = ["🤖 AI 產品與應用"]
    
    return list(dict.fromkeys(cats))  # preserve order, dedupe

# Assign categories to each article
for a in articles:
    a['cats'] = categorize(a)

# Group
from collections import OrderedDict
groups = OrderedDict()
for cat in CAT_EMOJI:
    groups[cat] = []

for a in articles:
    for c in a['cats']:
        if c not in groups:
            groups[c] = []
        groups[c].append(a)

# Remove empty
groups = {k: v for k, v in groups.items() if v}

print(f"Total articles: {len(articles)}")
for k, v in groups.items():
    print(f"  {k}: {len(v)}")

