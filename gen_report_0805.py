#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate TechCrunch AI News Report for 2026-08-05"""

import json
from datetime import datetime

# Load content data
with open('/home/matt/.openclaw/workspace/TECH/news_content_0805.json') as f:
    articles = json.load(f)

# Filter to past ~24h (2026-08-04 and 2026-08-03)
recent = [a for a in articles if a.get('success') and a.get('time', '').startswith('2026-08-0')]

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

# Category tagging
def tag_article(article):
    title = article.get('title', '').lower()
    content = article.get('content', '').lower()
    text = title + ' ' + content

    cats = []
    # Chips/hardware
    if any(kw in text for kw in ['nvidia', 'gpu', 'chip', 'volta', 'bitdeer', 'rubin', 'runware', 'data center', 'data centre', 'inference pod', 'spacex', 'xai', 'megapack', 'semiconductor', 'amd', 'intel']):
        if 'nvidia' in text or 'gpu' in text or 'volta' in text or 'bitdeer' in text or 'rubin' in text or 'runware' in text or 'megapack' in text or 'inference pod' in text:
            cats.append('💾 AI 晶片與硬體')
    # Models/research
    if any(kw in text for kw in ['glm', 'open-weight', 'open weight', 'safety gap', 'frontier', 'model', 'saferai', 'llm', 'benchmark']):
        if 'glm' in text or 'open-weight' in text or 'saferai' in text:
            cats.append('🧠 AI 模型與研究')
    # Products/apps
    if any(kw in text for kw in ['spotify', 'siri', 'apple ai', 'wrinkles', 'superblocks', 'vibe coding', 'remix', 'chatgpt work', 'app']):
        if 'spotify' in text or 'siri' in text or 'wrinkles' in text or 'superblocks' in text:
            cats.append('🤖 AI 產品與應用')
    # Enterprise
    if any(kw in text for kw in ['palantir', 'alex karp', 'tesla', 'elon musk', 'congress', 'chatgpt', 'earnings', 'enterprise']):
        if 'palantir' in text or 'alex karp' in text or 'congress' in text:
            cats.append('🏢 企業 AI 動態')
    # Investment/M&A
    if any(kw in text for kw in ['deal', 'funding', 'raises', 'series', 'acquisition', 'acquire', 'billion', 'valuation', 'investment', 'benioff', 'design arena', 'airtable', 'valar']):
        if 'deal' in text or 'raises' in text or 'funding' in text or 'acquire' in text or 'airtable' in text or 'valar' in text:
            cats.append('💰 AI 投融資與併購')
    # Policy/regulation
    if any(kw in text for kw in ['texas', 'governor', 'audit', 'nudify', 'xai', 'minnesota', 'apple', 'openai', 'trade secret', 'uk', 'backdoor', 'regulation', 'ban', 'legal', 'lawsuit']):
        if 'texas' in text or 'nudify' in text or 'minnesota' in text or 'trade secret' in text or 'uk' in text or 'backdoor' in text:
            cats.append('🏛️ AI 政策與監管')
    # People/org
    if any(kw in text for kw in ['influencer', 'openai trip', 'luxury', 'hank green', 'sam altman']):
        if 'influencer' in text or 'luxury' in text or 'hank green' in text:
            cats.append('👥 AI 人事與組織')
    # International
    if any(kw in text for kw in ['china', 'chinese', 'geopolitics', 'export', 'open-weight']):
        if 'china' in text or 'chinese' in text:
            cats.append('🌍 AI 國際與地緣政治')

    return cats

# Manual overrides for specific articles
ARTICLE_CATS = {
    'Open-weight AI models are catching up': ['🧠 AI 模型與研究', '🌍 AI 國際與地緣政治'],
    'Anthropic signs $10B deal': ['💾 AI 晶片與硬體', '💰 AI 投融資與併購'],
    'Nvidia doesn\'t mess around': ['💾 AI 晶片與硬體', '🏛️ AI 政策與監管'],
    'Spotify expands': ['🤖 AI 產品與應用'],
    'Texas halts': ['🏛️ AI 政策與監管', '💾 AI 晶片與硬體'],
    'Elon Musk spends half': ['🏢 企業 AI 動態'],
    'Apple says more ex-employees': ['🏛️ AI 政策與監管'],
    'Runware builds a pod': ['💾 AI 晶片與硬體'],
    'SpaceX doubles revenue': ['💾 AI 晶片與硬體', '🏢 企業 AI 動態'],
    'Bending Spoons': ['💰 AI 投融資與併購'],
    'Palantir CEO Alex Karp': ['🏢 企業 AI 動態'],
    'AWS is helping vibe-coding': ['🤖 AI 產品與應用', '🏢 企業 AI 動態'],
    'Design Arena': ['💰 AI 投融資與併購', '🤖 AI 產品與應用'],
    'Influencers draw backlash': ['👥 AI 人事與組織'],
    'Apple finally fixed Siri': ['🤖 AI 產品與應用'],
    'Congress': ['🏢 企業 AI 動態', '🏛️ AI 政策與監管'],
    'Marc Benioff-backed': ['💰 AI 投融資與併購'],
    'Sam Altman and AI\'s decel': ['🌍 AI 國際與地緣政治'],
    'Judge denies xAI': ['🏛️ AI 政策與監管'],
    'Hank Green': ['👥 AI 人事與組織'],
    'Who\'s legally to blame': ['🏛️ AI 政策與監管'],
    'Apple challenges UK': ['🏛️ AI 政策與監管'],
    'Lucid': ['🤖 AI 產品與應用'],
    'Waymo opens': ['🤖 AI 產品與應用'],
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
        cats = ['🏢 企業 AI 動態']  # default

    for c in cats:
        if c in CATEGORIES:
            CATEGORIES[c].append(article)

# Build HTML
date_str = '2026-08-05'
date_display = '2026年8月5日（台北時間）'

# Top 3 headlines (pick the most important)
top3 = recent[:3]

# Keywords
all_keywords = [
    'GLM-5.2', 'Z.ai', 'Volta', 'Bitdeer', 'Nvidia Vera Rubin', 'Open Secure AI Alliance',
    'OSAA', 'SpaceX', 'xAI', 'Palantir', 'Alex Karp', 'OpenAI', 'Anthropic',
    'ChatGPT', 'Siri AI', 'Apple', 'AWS', 'Superblocks', 'Spotify', 'Merlin',
    'Design Arena', 'Runware', 'Sonic Inference Pod', 'Texas', 'Greg Abbott',
    'Airtable', 'Bending Spoons', 'Valar Atomics', 'Waymo', 'Lucid Motors',
    'Hugging Face', 'SaferAI', 'OpenAI GPT-5.6 Sol', 'Claude Opus 4.7',
    'Elon Musk', 'Sam Altman', 'Dario Amodei', 'Jensen Huang',
    'ChatGPT Work', 'iOS 27', 'vibe coding', 'agent', 'robotaxi'
]

def clean_content(content, max_len=800):
    if not content:
        return ''
    # Remove excessive whitespace
    import re
    content = re.sub(r'\s+', ' ', content)
    return content[:max_len].strip()

def get_summary(article):
    """Generate a 200-300 char summary from content"""
    content = article.get('content', '') or ''
    title = article.get('title', '')
    content = clean_content(content, 600)

    # Extract first meaningful sentences
    sentences = content.split('. ')
    summary = ''
    for s in sentences[:4]:
        if len(summary) + len(s) < 350:
            summary += s + '. '
        else:
            break
    if not summary:
        summary = content[:300] + '...'
    return summary.strip()

def get_why_important(article):
    """Generate why important"""
    title = article.get('title', '')
    if 'GLM-5.2' in title or 'open-weight' in title.lower():
        return '中國開源模型 GLM-5.2 能力直逼前段班，但安全防護幾乎缺席，暴露開源模型治理缺口。'
    elif 'Anthropic signs $10B' in title:
        return 'Anthropic 擴大雲端合作，6 年 100 億美元大單顯示 AI 實驗室對算力的飢渴競爭。'
    elif 'Nvidia' in title and 'Alliance' in title:
        return 'Nvidia 主導的 OSAA 一週內已有 120 家企業加入，顯示 AI 安全標準化正在加速。'
    elif 'Texas halts' in title:
        return '德州暫停新資料中心審計，顯示 AI 基礎設施擴張已觸及電網與監管瓶頸。'
    elif 'Apple says more ex-employees' in title:
        return 'Apple 擴大指控 OpenAI 挖角竊密，突顯 AI 人才戰與智財權界線的緊張關係。'
    elif 'Palantir' in title:
        return 'Palantir 單季盈利 10 億美元，Alex Karp 公開抨擊 AI 業界「馬克思主義」，反映企業 AI 市場分歧加劇。'
    elif 'Apple finally fixed Siri' in title:
        return 'Siri AI 終於上線但已失去領先優勢，Apple AI 策略落後同業的代價浮現。'
    elif 'Spotify' in title:
        return 'Spotify AI 混音與重製工具擴大合作獨立唱片，音樂產業與 AI 的授權戰局持續演變。'
    elif 'Runware' in title:
        return '模組化 AI 推論艙挑戰大型資料中心剛性建造模式，反應市場對彈性算力的需求。'
    elif 'Elon Musk' in title:
        return '馬斯克在 Tesla 法說會上近半時間談論 AI 與機器人，顯示 Tesla 核心業務關注度正在質變。'
    elif 'Congress' in title:
        return '美國國會 ChatGPT 使用佔 AI 支出 90%，顯示生成式 AI 在政府機構已廣泛滲透。'
    elif 'Design Arena' in title:
        return 'Design Arena 以人類品味評估填補 AI 模型改進缺口，ARR 已達 6000 萬美元。'
    elif 'Bending Spoons' in title:
        return 'Bending Spoons 以 12.8 億美元收購 Airtable，顯示 SaaS 工具整合趨勢加速。'
    elif 'SpaceX doubles' in title:
        return 'SpaceX 營收翻倍，AI 算力租賃與 Starlink 為主要引擎，反映 Elon Musk 生態系整合深度。'
    elif 'Judge denies xAI' in title:
        return '法院拒絕封鎖「nudify」禁令，顯示 AI 濫用監管已在州層級展開執法。'
    elif 'Who\'s legally' in title:
        return 'Anthropic 與 OpenAI 旗下代理造成 Hugging Face 被駭，法律責任歸屬成為新監管焦點。'
    elif 'Apple challenges UK' in title:
        return 'Apple 挑戰英國國安局要求 iCloud 後門，數位主權與加密之爭延燒至 AI 時代。'
    elif 'Waymo opens' in title:
        return 'Waymo 開放達拉斯全域無人計程車服務，為商業化規模化重要里程碑。'
    elif 'Sam Altman' in title:
        return 'Sam Altman 持續倡議 AI 減速論，反映產業內部對發展速度的深刻分歧。'
    elif 'Influencers' in title:
        return 'OpenAI 首次網紅行銷trip 引發反彈，顯示 AI 企業品牌塑造策略正受公眾檢視。'
    else:
        return '此新聞反映 AI 產業動態，對投資人與觀察者具有參考價值。'

def get_stocks(article):
    """Get related stocks"""
    title = article.get('title', '') + article.get('content', '')
    stocks = []
    stock_map = {
        'NVIDIA': 'NVDA', '英偉達': 'NVDA', 'Nvidia': 'NVDA',
        'AMD': 'AMD', '超微': 'AMD',
        'Apple': 'AAPL', '蘋果': 'AAPL',
        'Google': 'GOOGL', 'Alphabet': 'GOOGL', 'DeepMind': 'GOOGL',
        'Microsoft': 'MSFT', '微軟': 'MSFT',
        'Meta': 'META', '亞馬遜': 'AMZN', 'Amazon': 'AMZN',
        'Tesla': 'TSLA', 'Palantir': 'PLTR',
        'Spotify': 'SPOT', 'Uber': 'UBER',
        'Anthropic': None, 'OpenAI': None,
        'SpaceX': None, 'xAI': None,
        'Waymo': None, 'Lucid': 'LCID',
    }
    for name, ticker in stock_map.items():
        if name.lower() in title.lower() and ticker:
            stocks.append(f'{name} ({ticker})')
    return list(set(stocks))

def get_key_entities(article):
    """Get key entities mentioned"""
    title = article.get('title', '') + article.get('content', '')
    entities = []
    entity_map = {
        'GLM-5.2': 'GLM-5.2', 'Z.ai': 'Z.ai', 'Zhong': 'Z.ai',
        'SaferAI': 'SaferAI', 'Henry Papadatos': 'Henry Papadatos（SaferAI 執行總監）',
        'Volta': 'Volta', 'Bitdeer': 'Bitdeer', 'Nvidia Vera Rubin': 'Nvidia Vera Rubin',
        'OSAA': 'Open Secure AI Alliance（OSAA）', 'Linux Foundation': 'Linux Foundation',
        'SpaceX': 'SpaceX', 'xAI': 'xAI', 'Tesla Megapack': 'Tesla Megapack',
        'Runware': 'Runware', 'Sonic Inference Pod': 'Sonic Inference Pod',
        'Palantir': 'Palantir', 'Alex Karp': 'Alex Karp（Palantir CEO）',
        'Apple': 'Apple', 'OpenAI': 'OpenAI', 'ChatGPT': 'ChatGPT',
        'Siri': 'Siri AI', 'Gemini': 'Google Gemini',
        'AWS': 'Amazon Web Services（AWS）', 'Superblocks': 'Superblocks',
        'Spotify': 'Spotify', 'Merlin': 'Merlin', 'UMG': 'Universal Music Group',
        'Design Arena': 'Design Arena', 'Intelligence': 'Intelligence',
        'Grace Li': 'Grace Li（Intelligence 共同創辦人）',
        'Airtable': 'Airtable', 'Bending Spoons': 'Bending Spoons',
        'Valar Atomics': 'Valar Atomics', 'Sequoia': 'Sequoia Capital',
        'Texas': '德州', 'Greg Abbott': 'Greg Abbott（德州州長）',
        'Waymo': 'Waymo', 'Lucid Motors': 'Lucid Motors',
        'Hugging Face': 'Hugging Face', 'Elon Musk': 'Elon Musk',
        'Sam Altman': 'Sam Altman（OpenAI CEO）',
        'Jensen Huang': 'Jensen Huang（NVIDIA CEO）',
        'Dario Amodei': 'Dario Amodei（Anthropic CEO）',
        'Hank Green': 'Hank Green（YouTuber）',
        'Minnesota': '明尼蘇達州',
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
.news-card .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px; gap: 10px; }}
.news-card h4 {{ flex: 1; }}
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

for kw in all_keywords[:40]:
    html += f'    <span class="kw">{kw}</span>\n'

html += '''  </div>
</div>

<!-- Top 3 Headlines -->
<div class="top3-section">
  <h2>🔥 每日 3 大頭條</h2>
  <div class="top3-grid">
'''

# Top 3 articles
top3_data = [
    (recent[0] if len(recent) > 0 else None, '中國開源模型 GLM-5.2 能力直逼 OpenAI/Claude 前段班，但安全防護嚴重不足，引發開源 AI 治理危機。'),
    (recent[1] if len(recent) > 1 else None, 'Anthropic 與雲端新創 Volta 簽下 6 年 100 億美元算力大單，顯示 AI 實驗室的算力軍備競賽持續升溫。'),
    (recent[2] if len(recent) > 2 else None, 'Nvidia 號召 120 家企業成立 Open Secure AI Alliance，一週內提出首份 AI 安全建議，顯示產業自律加速。'),
]

for i, (article, why) in enumerate(top3_data, 1):
    if article:
        link = article.get('link', '#')
        title = article.get('title', '')
        time_str = article.get('time', '')[:10] if article.get('time') else ''
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

# Render each category
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
            html += f'      <div class="entities">關鍵實體：' + '、'.join(f'<span>{e}</span>' for e in entities[:5]) + '</div>\n'
        if stocks:
            html += f'      <div class="stocks">相關概念股：' + '、'.join(f'<span>{s}</span>' for s in stocks[:4]) + '</div>\n'
        html += '    </div>\n'

    html += '    </div>\n  </div>\n'

html += '''</div>

<!-- Tomorrow Watch -->
<div class="tomorrow">
  <h2>🔮 明日觀察</h2>
  <ul>
    <li>GLM-5.2 安全報告可能引發美國政府對中國開源模型的新一波政策討論</li>
    <li>Anthropic 算力擴張新聞可能帶動雲端基礎建設類股（NVIDIA、AMD）持續走高</li>
    <li>Apple vs OpenAI 官司預計有新進展，雙方攻防持續升級</li>
    <li>Nvidia OSAA 安全聯盟可能吸引更多企業加入，抗衡 Anthropic 缺席的疑慮</li>
    <li>Texas 資料中心審計結果出爐，可能影響其他州跟進監管 AI 基礎設施</li>
    <li>ChatGPT 在國會的廣泛使用可能引發新一波政府 AI 採購政策辯論</li>
    <li>Palantir 季報後續效應：Alex Karp 的「馬克思主義」言論是否影響企業夥伴關係</li>
    <li>Siri AI 正式版（iOS 27）發布時間臨近，Apple AI 生態系能見度將提升</li>
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
