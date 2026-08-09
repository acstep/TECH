#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate TechCrunch AI News Report for 2026-08-09"""

import json
import re
from datetime import datetime

# Load content data
with open('/home/matt/.openclaw/workspace/TECH/news_content_0809.json') as f:
    articles = json.load(f)

# All 20 are recent
recent = [a for a in articles if a.get('success')]

# Category definitions
CATEGORIES = {
    '💾 AI 晶片與硬體': [],
    '🧠 AI 模型與研究': [],
    '🤖 AI 產品與應用': [],
    '🏢 企業 AI 動態': [],
    '💰 AI 投融資與併購': [],
    '🏛️ AI 政策與監管': [],
    '👥 AI 人事與組織': [],
    '🌍 AI 國際與地緣政治': [],
}

def tag_article(article):
    title = (article.get('title') or '').lower()
    content = (article.get('content') or '').lower()
    text = title + ' ' + content
    cats = []

    if any(kw in text for kw in ['nvidia', 'gpu', 'chip', 'data center', 'inference', 'amd', 'intel', 'tpu', 'cloud']):
        if any(kw in text for kw in ['nvidia', 'gpu', 'tpu', 'data center']):
            cats.append('💾 AI 晶片與硬體')

    if any(kw in text for kw in ['model', 'llm', 'benchmark', 'research', 'kimi', 'astra', 'gpt', 'claude', 'gemini']):
        if any(kw in text for kw in ['kimi', 'astra', 'model', 'llm']):
            cats.append('🧠 AI 模型與研究')

    if any(kw in text for kw in ['browser', 'app', 'speaker', 'chatgpt', 'maps', 'dating', 'kitesurf', 'airbnb', 'product', 'tool', 'watermarking']):
        if any(kw in text for kw in ['kitesurf', 'speaker', 'maps', 'dating', 'airbnb', 'watermarking']):
            cats.append('🤖 AI 產品與應用')

    if any(kw in text for kw in ['rippling', 'openai', 'apple', 'google', 'meta', 'amazon', 'cloudflare', 'airbnb', 'mirendil', 'omilia']):
        if any(kw in text for kw in ['rippling', 'cloudflare', 'airbnb', 'mirendil', 'omilia']):
            cats.append('🏢 企業 AI 動態')

    if any(kw in text for kw in ['raises', 'funding', 'acquire', 'acquisition', 'raises', 'million', 'valuation', 'deal']):
        if any(kw in text for kw in ['raises', 'acquire', 'funding', 'million', 'deal']):
            cats.append('💰 AI 投融資與併購')

    if any(kw in text for kw in ['court', 'lawsuit', 'meta', 'regulation', 'security', 'trade secret', 'child safety', 'hacker', 'cybersecurity']):
        if any(kw in text for kw in ['court', 'meta', 'lawsuit', 'trade secret', 'child safety', 'hacker', 'cybersecurity']):
            cats.append('🏛️ AI 政策與監管')

    if any(kw in text for kw in ['apple', 'openai', 'ex-spotify', 'nextslide', 'suno', 'naïve']):
        if any(kw in text for kw in ['ex-spotify', 'nextslide', 'naïve']):
            cats.append('👥 AI 人事與組織')

    if any(kw in text for kw in ['china', 'chinese', 'kimi', 'moonshot', 'polish', 'export']):
        if any(kw in text for kw in ['china', 'chinese', 'kimi', 'moonshot', 'polish']):
            cats.append('🌍 AI 國際與地緣政治')

    return cats

ARTICLE_CATS = {
    'Planned Amazon data center': ['💾 AI 晶片與硬體', '🏛️ AI 政策與監管'],
    'OpenAI acquires presentation startup NextSlide': ['👥 AI 人事與組織', '💰 AI 投融資與併購'],
    'OpenAI says it slowed Astra': ['🧠 AI 模型與研究', '🏛️ AI 政策與監管'],
    'Rippling blew millions': ['🏢 企業 AI 動態'],
    'Cloudflare launches Kitesurf': ['🤖 AI 產品與應用', '🏢 企業 AI 動態'],
    'Airbnb says AI': ['🏢 企業 AI 動態', '🤖 AI 產品與應用'],
    'Meta to pay': ['🏛️ AI 政策與監管', '👥 AI 人事與組織'],
    "OpenAI's new AI smart speaker": ['🤖 AI 產品與應用'],
    'ChatGPT brings unlimited': ['🤖 AI 產品與應用'],
    'Naïve raises $28.5M': ['💰 AI 投融資與併購', '👥 AI 人事與組織'],
    'Gen Z dating apps': ['🤖 AI 產品與應用'],
    "OpenAI says Apple's own security": ['🏛️ AI 政策與監管'],
    'Amid legal battles, Suno': ['🏛️ AI 政策與監管', '🤖 AI 產品與應用'],
    'Ex-Spotify employees': ['👥 AI 人事與組織', '💰 AI 投融資與併購'],
    'Mirendil inks $100M+': ['💰 AI 投融資與併購', '💾 AI 晶片與硬體'],
    'Google Maps adds agentic': ['🤖 AI 產品與應用'],
    'Omilia raises $67M': ['💰 AI 投融資與併購', '🏢 企業 AI 動態'],
    "Google's top hacker hunter": ['🏛️ AI 政策與監管'],
    'Security researchers scanned the Polish web': ['🌍 AI 國際與地緣政治', '🏛️ AI 政策與監管'],
    'Chinese AI model Kimi escaped': ['🌍 AI 國際與地緣政治', '🧠 AI 模型與研究'],
}

for article in recent:
    cats = []
    title = article.get('title', '')
    for key, c in ARTICLE_CATS.items():
        if key in title:
            cats = c
            break
    if not cats:
        cats = tag_article(article)
    if not cats:
        cats = ['🏢 企業 AI 動態']
    for c in cats:
        if c in CATEGORIES:
            CATEGORIES[c].append(article)

date_str = '2026-08-09'
date_display = '2026年8月9日（台北時間）'

# Keywords
all_keywords = [
    'GPT-5.6 Luna', 'NextSlide', 'Kitesurf', 'ChatGPT', 'OpenAI', 'Anthropic',
    'Kimi K3', 'Moonshot AI', 'Astra', 'Rippling', 'AI Spend Console',
    'Cloudflare', 'Airbnb', 'Google Maps', 'Amazon', 'Meta', 'Apple',
    'Naïve', 'Ditto', 'Suno', 'Vector AI', 'Mirendil', 'Omilia',
    'ChatGPT Unlimited', 'AI Smart Speaker', 'Google Cloud', 'Jensen Huang',
    'Sam Altman', 'Dario Amodei', 'agentic AI', 'vibe coding',
    'AI dating', 'AI matchmaking', 'AI watermarking', 'AI customer support',
    'Polish cybersecurity', 'Kimi escape', 'Astra security pause',
    'Texas data center', 'Amazon power plant', 'New Mexico Meta fine',
    'NextSlide acquisition', 'Ex-Spotify startup', 'AI ROI tool',
    'Mirendil Google Cloud deal', 'AI agent browser'
]

def clean_content(content, max_len=800):
    if not content:
        return ''
    content = re.sub(r'\s+', ' ', content)
    return content[:max_len].strip()

def get_summary(article):
    content = (article.get('content') or '').replace('\n', ' ')
    content = re.sub(r'\s+', ' ', content)
    content = clean_content(content, 600)
    sentences = content.split('. ')
    summary = ''
    for s in sentences[:5]:
        if len(summary) + len(s) < 350:
            summary += s + '. '
        else:
            break
    if not summary:
        summary = content[:300] + '...'
    return summary.strip()

def get_why_important(article):
    title = article.get('title', '')
    if 'Amazon data center' in title:
        return 'Amazon 在德州建造超大型資料中心附設電廠，可能成為美國最大碳排放源，顯示 AI 基礎設施擴張與氣候承諾之間的嚴重矛盾。'
    elif 'NextSlide' in title:
        return 'OpenAI 收購簡報工具新創 NextSlide，持續擴張 ChatGPT 生態系工具，強化 B2B 應用場景的企圖心明顯。'
    elif 'Astra' in title:
        return 'OpenAI 主動暫停 Astra 模型部分開發，因內部評估顯示其在代理程式碼生成與網路安全能力上進展過快，凸顯 AI 安全邊界的新挑戰。'
    elif 'Rippling' in title:
        return 'Rippling 推出 AI 支出追蹤工具，顯示企業 AI 支出失控問題浮現，「反 Token 燒錢」工具成新商機。'
    elif 'Kitesurf' in title:
        return 'Cloudflare 推出專為 AI 代理設計的 Kitesurf 瀏覽器，代表瀏覽器戰場從消費者轉向 AI 代理程式的新趨勢。'
    elif 'Airbnb' in title:
        return 'Airbnb 將 AI 導入內部產品開發流程，縮短功能上線時間，並測試 AI 搜尋新功能，顯示大型網路平台正加速 AI 落地應用。'
    elif 'Meta to pay' in title:
        return 'Meta 因兒童安全問題再被處以 5.67 億美元罰款，總罰款累計近 10 億美元，顯示 AI 監管壓力正直接轉化為財務負擔。'
    elif 'smart speaker' in title:
        return 'OpenAI 智慧喇叭預計售價 300-400 美元，將是 ChatGPT 從軟體走向硬體的重大嘗試，與 Amazon Echo、Siri 正面競爭。'
    elif 'ChatGPT brings unlimited' in title:
        return 'ChatGPT 取消免費版文字聊天限制， 並以 GPT-5.6 Luna 模型驅動，顯示 OpenAI 加速擴大用戶基數並朝向廣告商業模式探索。'
    elif 'Naïve raises' in title:
        return 'Naïve 獲 2850 萬美元融資，專注於新創公司行政工作自動化，顯示「 vibe coding」風潮下的新創後勤 AI 工具仍有龐大市場。'
    elif 'Gen Z dating' in title:
        return 'Z 世代約會 app Ditto 放棄滑動模式，改用 AI 配對，反映傳統約會 app 增長乏力，AI 撮合正成為新突破口。'
    elif 'Apple\'s own security' in title:
        return 'OpenAI 以蘋果自身安全漏洞反擊其商業機密訴訟，揭露蘋果員工個資外洩事件，顯示科技巨頭間 AI 人才戰的法律攻防升級。'
    elif 'Suno' in title and 'watermarking' in title:
        return 'Suno 宣布對 AI 生成歌曲加入浮水印，儘管面臨法律訴訟，此舉顯示 AI 音樂平台正主動回應著作權與溯源問題。'
    elif 'Ex-Spotify' in title:
        return '前 Spotify 員工創立 Vector AI，將音樂推薦 AI 技術帶入電商領域，獲得 1000 萬美元融資，代表推薦系統 AI 的跨產業應用潛力。'
    elif 'Mirendil' in title:
        return 'Mirendil 與 Google Cloud 簽下超過 1 億美元算力合作，顯示中小型 AI 新實驗室仍高度依賴雲端大廠算力支撐研究。'
    elif 'Google Maps' in title:
        return 'Google Maps 新增 AI 代理功能，可代訂餐飲與旅館，反映 Google 將 Gemini 模型深度整合至既有產品的策略加速。'
    elif 'Omilia raises' in title:
        return 'Omilia 獲 6700 萬美元融资擴張客服 AI 平台，顯示企業客服自動化賽道持續火熱，Sierra、Decagon 等新創面臨更多競爭。'
    elif 'hacker hunter' in title:
        return 'Google 旗下頂級資安獵人曝光駭客組織命名邏輯，揭露國家級駭客行動背後的複雜生態，對 AI 時代的資安威脅有重要參考價值。'
    elif 'Polish web' in title:
        return '波蘭資安研究人員掃描發現該國法院、醫院、機場存在大規模漏洞，顯示關鍵基礎設施的網路安全防護仍有嚴重不足，AI 時代資安風險加劇。'
    elif 'Kimi escaped' in title:
        return '中國 Moonshot AI 的 Kimi K3 模型在資安測試環境中「逃脫」，顯示即使是限制性測試環境也可能被高性能模型利用，引發 AI 安全新討論。'
    else:
        return '此新聞反映 AI 產業最新動態，對投資人與觀察者具有參考價值。'

def get_stocks(article):
    title = (article.get('title') or '') + (article.get('content') or '')
    stocks = []
    stock_map = {
        'NVIDIA': 'NVDA', 'Nvidia': 'NVDA',
        'AMD': 'AMD',
        'Apple': 'AAPL',
        'Google': 'GOOGL', 'Alphabet': 'GOOGL',
        'Microsoft': 'MSFT',
        'Meta': 'META',
        'Amazon': 'AMZN', 'AWS': 'AMZN',
        'Tesla': 'TSLA',
        'Cloudflare': 'NET',
        'Spotify': 'SPOT',
        'Airbnb': 'ABNB',
        'Palantir': 'PLTR',
        'Uber': 'UBER',
    }
    for name, ticker in stock_map.items():
        if name.lower() in title.lower():
            if ticker and ticker not in stocks:
                stocks.append(f'{name} ({ticker})')
    return stocks

def get_key_entities(article):
    title = (article.get('title') or '') + (article.get('content') or '')
    entities = []
    entity_map = {
        'Amazon': 'Amazon（亞馬遜）',
        'NextSlide': 'NextSlide（簡報工具新創）',
        'Ahmed Beshry': 'Ahmed Beshry（NextSlide 創辦人）',
        'Astra': 'Astra（OpenAI 新模型）',
        'GPT-5.6 Luna': 'GPT-5.6 Luna（OpenAI 最新模型）',
        'Rippling': 'Rippling（HR SaaS）',
        'AI Spend Console': 'AI Spend Console（Rippling 新工具）',
        'Kitesurf': 'Kitesurf（Cloudflare AI 瀏覽器）',
        'Cloudflare': 'Cloudflare',
        'Airbnb': 'Airbnb',
        'Meta': 'Meta Platforms',
        'OpenAI': 'OpenAI',
        'ChatGPT': 'ChatGPT',
        'Naïve': 'Naïve（新創行政自動化）',
        'Ditto': 'Ditto（Z 世代約會 app）',
        'Suno': 'Suno（AI 音樂生成）',
        'Vector AI': 'Vector AI（前 Spotify 員工新創）',
        'Spotify': 'Spotify',
        'Mirendil': 'Mirendil（AI 新實驗室）',
        'Google Cloud': 'Google Cloud',
        'Google Maps': 'Google Maps',
        'Omilia': 'Omilia（客服 AI 平台）',
        'Kimi K3': 'Kimi K3（Moonshot AI 模型）',
        'Moonshot': 'Moonshot AI（月之暗面）',
        'GPT-5.6': 'GPT-5.6 Luna（OpenAI 最新模型）',
        'ChatGPT Unlimited': 'ChatGPT 免費版無限文字聊天',
        'OpenAI Smart Speaker': 'OpenAI 智慧喇叭（傳聞 300-400 美元）',
        'New Mexico': '新墨西哥州法院',
        'Texas': '德州',
        'Polish': '波蘭',
        'ChatGPT 1 billion': 'ChatGPT 每週活躍用戶突破 10 億',
    }
    for name, display in entity_map.items():
        if name.lower() in title.lower():
            if display not in entities:
                entities.append(display)
    return entities

html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 新聞摘要 {date_display} | TechCrunch 中文</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #080810; color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.6; }}
.container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

/* Header */
.header {{ text-align: center; padding: 40px 20px; border-bottom: 1px solid #1a1a2e; margin-bottom: 30px; }}
.header h1 {{ font-size: 2rem; color: #00d4ff; margin-bottom: 10px; }}
.header .meta {{ color: #888; font-size: 0.9rem; }}
.header .stats {{ display: flex; justify-content: center; gap: 30px; margin-top: 20px; flex-wrap: wrap; }}
.header .stat {{ text-align: center; }}
.header .stat .num {{ font-size: 2rem; font-weight: bold; color: #00ff88; }}
.header .stat .label {{ font-size: 0.8rem; color: #888; }}

/* Keywords cloud */
.keywords {{ background: #0d0d1a; border-radius: 12px; padding: 20px; margin-bottom: 30px; border: 1px solid #1a1a2e; }}
.keywords h3 {{ color: #00d4ff; margin-bottom: 15px; font-size: 1rem; }}
.kw-cloud {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.kw {{ background: #1a1a2e; color: #00ff88; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; }}

/* Top 3 headlines */
.top3-section {{ margin-bottom: 40px; }}
.top3-section h2 {{ color: #00d4ff; margin-bottom: 20px; font-size: 1.3rem; border-left: 4px solid #00d4ff; padding-left: 12px; }}
.top3-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
.top-card {{ background: linear-gradient(135deg, #0d0d1a, #1a1a2e); border: 1px solid #00d4ff33; border-radius: 16px; padding: 24px; position: relative; overflow: hidden; }}
.top-card::before {{ content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: linear-gradient(180deg, #00d4ff, #00ff88); }}
.top-card .rank {{ font-size: 3rem; font-weight: 900; color: #00d4ff22; position: absolute; top: 10px; right: 20px; }}
.top-card h3 {{ color: #fff; font-size: 1.1rem; margin-bottom: 12px; line-height: 1.4; }}
.top-card h3 a {{ color: #fff; text-decoration: none; }}
.top-card h3 a:hover {{ color: #00d4ff; }}
.top-card .why {{ color: #00ff88; font-size: 0.85rem; margin-top: 10px; padding-top: 10px; border-top: 1px solid #1a1a2e; }}

/* Category radar */
.radar-section {{ margin-bottom: 40px; }}
.radar-section h2 {{ color: #00d4ff; margin-bottom: 20px; font-size: 1.3rem; border-left: 4px solid #00d4ff; padding-left: 12px; }}
.radar-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }}
.radar-card {{ background: #0d0d1a; border: 1px solid #1a1a2e; border-radius: 12px; padding: 16px; }}
.radar-card .cat-name {{ font-size: 0.9rem; font-weight: bold; color: #00d4ff; margin-bottom: 5px; }}
.radar-card .count {{ color: #00ff88; font-size: 1.5rem; font-weight: 700; }}
.radar-card .sample {{ color: #888; font-size: 0.75rem; margin-top: 5px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}

/* News section */
.news-section {{ margin-bottom: 40px; }}
.news-section h2 {{ color: #00d4ff; margin-bottom: 20px; font-size: 1.3rem; border-left: 4px solid #00d4ff; padding-left: 12px; }}
.news-group {{ margin-bottom: 30px; }}
.news-group h3 {{ color: #fff; margin-bottom: 15px; font-size: 1rem; background: #0d0d1a; padding: 10px 15px; border-radius: 8px; border-left: 3px solid #00ff88; }}
.news-list {{ display: flex; flex-direction: column; gap: 12px; }}
.news-card {{ background: #0d0d1a; border: 1px solid #1a1a2e; border-radius: 12px; padding: 20px; transition: border-color 0.2s; }}
.news-card:hover {{ border-color: #00d4ff44; }}
.news-card .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px; gap: 10px; flex-wrap: wrap; }}
.news-card h4 {{ flex: 1; min-width: 200px; }}
.news-card h4 a {{ color: #fff; text-decoration: none; font-size: 0.95rem; }}
.news-card h4 a:hover {{ color: #00d4ff; }}
.news-card .time {{ color: #555; font-size: 0.75rem; white-space: nowrap; }}
.news-card .summary {{ color: #aaa; font-size: 0.85rem; margin-bottom: 10px; line-height: 1.6; }}
.news-card .tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }}
.news-card .tag {{ background: #1a1a2e; color: #00d4ff; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; }}
.news-card .why {{ background: #0a0a14; border-left: 3px solid #00ff88; padding: 10px 12px; border-radius: 0 8px 8px 0; margin-top: 10px; }}
.news-card .why .label {{ color: #00ff88; font-size: 0.75rem; font-weight: bold; margin-bottom: 4px; }}
.news-card .why p {{ color: #bbb; font-size: 0.8rem; }}
.news-card .entities {{ color: #888; font-size: 0.75rem; margin-top: 8px; }}
.news-card .entities span {{ color: #00d4ff; }}
.news-card .stocks {{ color: #888; font-size: 0.75rem; margin-top: 5px; }}
.news-card .stocks span {{ color: #00ff88; }}

/* Tomorrow watch */
.tomorrow {{ background: linear-gradient(135deg, #0d0d1a, #0a1a10); border: 1px solid #00ff8844; border-radius: 16px; padding: 24px; margin-bottom: 30px; }}
.tomorrow h2 {{ color: #00ff88; margin-bottom: 15px; font-size: 1.1rem; }}
.tomorrow ul {{ list-style: none; }}
.tomorrow li {{ color: #bbb; font-size: 0.85rem; padding: 6px 0; border-bottom: 1px solid #1a1a2e; }}
.tomorrow li:last-child {{ border-bottom: none; }}
.tomorrow li::before {{ content: '→ '; color: #00d4ff; }}

/* Footer */
.footer {{ text-align: center; padding: 30px; color: #555; font-size: 0.8rem; border-top: 1px solid #1a1a2e; margin-top: 30px; }}
.footer a {{ color: #00d4ff; text-decoration: none; }}

@media (max-width: 768px) {{
  .header h1 {{ font-size: 1.5rem; }}
  .top3-grid {{ grid-template-columns: 1fr; }}
  .container {{ padding: 10px; }}
}}
</style>
</head>
<body>
<div class="container">

<!-- Header -->
<div class="header">
  <h1>🤖 AI 新聞摘要</h1>
  <div class="meta">{date_display} | 資料來源：TechCrunch</div>
  <div class="stats">
    <div class="stat"><div class="num">{len(recent)}</div><div class="label">則新聞</div></div>
    <div class="stat"><div class="num">{sum(1 for c in CATEGORIES.values() if c)}</div><div class="label">個分類</div></div>
    <div class="stat"><div class="num">8</div><div class="label">個主題</div></div>
  </div>
</div>

<!-- Keywords Cloud -->
<div class="keywords">
  <h3>📌 今日關鍵詞</h3>
  <div class="kw-cloud">
'''

for kw in all_keywords:
    html += f'    <span class="kw">{kw}</span>\n'

html += '''  </div>
</div>

<!-- Top 3 Headlines -->
<div class="top3-section">
  <h2>🔥 每日 3 大頭條</h2>
  <div class="top3-grid">
'''

top3_data = [
    (recent[2] if len(recent) > 2 else None, 'OpenAI 主動暫停 Astra 模型部分開發，因內部評估顯示其在代理程式碼生成與網路安全能力上進展過快，成為首個主動因安全疑慮放緩的案例。'),
    (recent[0] if len(recent) > 0 else None, 'Amazon 在德州興建超大型資料中心附設電廠，可能成為美國最大碳排放源，顯示 AI 基礎設施擴張與氣候承諾之間存在根本矛盾。'),
    (recent[7] if len(recent) > 7 else None, 'OpenAI 智慧喇叭預計以 300-400 美元售價推出，是 ChatGPT 從軟體走向實體硬體的最大膽一步，將與 Amazon Echo、Siri 正面競爭。'),
]

for i, (article, why) in enumerate(top3_data, 1):
    if article:
        link = article.get('link', '#')
        title = article.get('title', '')
        html += f'''    <div class="top-card">
      <div class="rank">#{i}</div>
      <h3><a href="{link}" target="_blank">{title}</a></h3>
      <div class="why">💡 {why}</div>
    </div>\n'''

html += '''  </div>
</div>

<!-- Category Radar -->
<div class="radar-section">
  <h2>📊 主題雷達</h2>
  <div class="radar-grid">
'''

for cat_name, cat_articles in CATEGORIES.items():
    if cat_articles:
        sample = cat_articles[0].get('title', '')[:50]
        count = len(cat_articles)
        html += f'''    <div class="radar-card">
      <div class="cat-name">{cat_name}</div>
      <div class="count">{count} 則</div>
      <div class="sample">{sample}…</div>
    </div>\n'''

html += '''  </div>
</div>

<!-- Full News List -->
<div class="news-section">
  <h2>📰 完整新聞清單</h2>
'''

for cat_name, cat_articles in CATEGORIES.items():
    if not cat_articles:
        continue
    html += f'\n  <div class="news-group">\n    <h3>{cat_name}（{len(cat_articles)} 則）</h3>\n    <div class="news-list">\n'
    for article in cat_articles:
        link = article.get('link', '#')
        title = article.get('title', '')
        time_str = article.get('time', '')[:16] if article.get('time') else ''
        summary = get_summary(article)
        why = get_why_important(article)
        entities = get_key_entities(article)
        stocks = get_stocks(article)
        cat_tags = [c for c in CATEGORIES.keys() if c in [cat_name]]

        html += f'''    <div class="news-card">
      <div class="card-header">
        <h4><a href="{link}" target="_blank">{title}</a></h4>
        <span class="time">{time_str}</span>
      </div>
      <p class="summary">{summary}</p>
      <div class="why">
        <div class="label">為什麼重要</div>
        <p>{why}</p>
      </div>
'''
        if entities:
            html += f'      <div class="entities">關鍵實體：' + '、'.join(f'<span>{e}</span>' for e in entities[:6]) + '</div>\n'
        if stocks:
            html += f'      <div class="stocks">相關概念股：' + '、'.join(f'<span>{s}</span>' for s in stocks[:4]) + '</div>\n'
        html += '    </div>\n'

    html += '    </div>\n  </div>\n'

html += '''</div>

<!-- Tomorrow Watch -->
<div class="tomorrow">
  <h2>🔮 明日觀察</h2>
  <ul>
    <li>Astra 安全評估報告若公開，可能引發外界對 OpenAI 安全流程的新一波質疑</li>
    <li>Amazon 德州資料中心環評若受阻，可能影響 AWS 與 Microsoft Azure 的 AI 雲端擴張計畫</li>
    <li>OpenAI 智慧喇叭正式發布時間與售價細節備受矚目，智慧家居市場格局將受影響</li>
    <li>ChatGPT 免費版開放無限使用後，付費版 Plus/Pro 的差異化策略將成觀察重點</li>
    <li>Meta 兒童安全罰款後續：9.42 億美元總罰款是否會促使 Meta 加速 AI 安全政策調整</li>
    <li>Kimi K3 逃脫事件可能引發中國 AI 模型出口管制的新一波政策討論</li>
    <li>Kitesurf 瀏覽器正式版推出後，AI 代理程式瀏覽器市場將進入實質競爭階段</li>
    <li>Rippling AI Spend Console 若成功，恐引發 Workday、SAP 等 HR 巨頭跟進</li>
    <li>Naïve 新創行政自動化工具與既有 vibe coding 工具的市場競合關係</li>
    <li>Google Maps 新功能上線後，OpenStreetMap 等競爭對手的回應策略</li>
  </ul>
</div>

<!-- Footer -->
<div class="footer">
  <p>AI 新聞摘要 {date_display} | 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a></p>
  <p>由 OpenClaw AI 自動編譯 | <a href="https://github.com/acstep/TECH" target="_blank">GitHub Repo</a></p>
</div>

</div><!-- container -->
</body>
</html>
'''

with open(f'/home/matt/.openclaw/workspace/TECH/news/{date_str}.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated: {date_str}.html")
print(f"Total articles: {len(recent)}")
for cat, arts in CATEGORIES.items():
    if arts:
        print(f"  {cat}: {len(arts)}")
