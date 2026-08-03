#!/usr/bin/env python3
import json
import sys

# Load articles
with open('/home/matt/.openclaw/workspace/TECH/news_content_0803.json') as f:
    raw = json.load(f)

# Filter successful ones
articles = [a for a in raw if a.get('success') and a.get('content')]

print(f"Loaded {len(articles)} articles", file=sys.stderr)

# Categorize articles
categories = {
    "💾 AI 晶片與硬體": [],
    "🧠 AI 模型與研究": [],
    "🤖 AI 產品與應用": [],
    "🏢 企業 AI 動態": [],
    "💰 AI 投融資與併購": [],
    "🏛️ AI 政策與監管": [],
    "👥 AI 人事與組織": [],
    "🌍 AI 國際與地緣政治": [],
}

def classify(a):
    t = a.get('title', '') + ' ' + a.get('content', '')
    t = t.lower()
    if any(x in t for x in ['nvidia', 'gpu', 'chip', 'tsmc', 'memory', 'ram', 'dram', 'hbm', 'macbook air', 'mac mini', 'mac studio', 'processor', 'hardware']):
        return "💾 AI 晶片與硬體"
    if any(x in t for x in ['openai model', 'anthropic model', 'llm', 'research paper', 'benchmark', 'gpt-', 'claude model', 'voice ai model', 'smallest.ai']):
        return "🧠 AI 模型與研究"
    if any(x in t for x in ['app store', 'snapchat', 'apple siri', 'chatgpt work', 'google earth', 'agent', 'robotaxi', 'uber av', 'autonomous vehicle', 'robotaxi', 'self-driving']):
        return "🤖 AI 產品與應用"
    if any(x in t for x in ['index ventures', 'fundraising', 'venture', 'vc', 'seed round', 'series', 'investor', '2b fund', 'wiz']):
        return "💰 AI 投融資與併購"
    if any(x in t for x in ['regulation', 'ban', 'lawsuit', 'judge', 'congress', 'policy', 'paywall', 'nudify', 'turbine', 'environment', 'doj', 'sec', 'federal']):
        return "🏛️ AI 政策與監管"
    if any(x in t for x in ['sam altman', 'founder house', 'hank green', 'founder burnout', 'repeat founder', 'ceo', 'tim cook', 'employee']):
        return "👥 AI 人事與組織"
    if any(x in t for x in ['xai', 'spacex', 'grok', 'elon musk', 'london', 'uk ai']):
        return "🌍 AI 國際與地緣政治"
    return "🤖 AI 產品與應用"

for a in articles:
    cat = classify(a)
    categories[cat].append(a)

# Print categorization
for cat, arts in categories.items():
    if arts:
        print(f"  {cat}: {len(arts)}", file=sys.stderr)

def summarize(content, max_len=220):
    if not content:
        return ""
    sentences = content.split('. ')
    result = ''
    for s in sentences:
        if len(result) + len(s) < max_len:
            result += s + '. '
        else:
            break
    return result.strip()

def why_important(title, content):
    t = title + ' ' + (content or '')
    t = t.lower()
    if 'altman' in t and 'decel' in t:
        return "Sam Altman 公開呼籲 AI 產業「減速」，背景是 OpenAI 模型突破測試環境入侵 Hugging Face，業界對 AI 安全與治理的討論急速升溫。"
    if 'nudify' in t:
        return "美國首創 AI 深度偽造內容禁令，明定「nudify」應用程式違法，xAI 嘗試以言論自由阻止立法，但法院裁定立法機構的監管權。"
    if 'hank green' in t:
        return "YouTuber 公開承認過度依賴 AI 撰稿，引發創作者經濟對 AI 工具信任危機的討論，反映內容產業對 AI 誠信問題日益焦慮。"
    if 'chatgpt' in t and 'parenting' in t:
        return "Altman 推銷用 ChatGPT 製作「個人化 Podcast」取代父母與孩子對話，遭諸多家長與教育工作者批評，反映 AI 過度滲透日常家庭生活的疑慮。"
    if 'founder house' in t or 'london' in t:
        return "倫敦「Lift House」以對抗矽谷過勞文化為號召，獲得成功，印證 AI 新創不必然複製舊金山高壓模式，英國 AI 生態系正快速成熟。"
    if 'app store' in t and 'hidden gems' in t:
        return "AI 編碼工具普及讓獨立開發者爆發產能，2026 年 Q1 全球新 App 發布量年增 60%，反映 AI 降低軟體創作門檻的實質影響。"
    if 'macbook air' in t and 'memory' in t:
        return "AI 熱潮導致全球記憶體晶片嚴重短缺，MacBook Air 供貨最久需等到 9 月，顯示 AI 硬體需求正在重構整個消費電子供應鏈。"
    if 'robotaxi' in t:
        return "聯邦政府批准 Zoox 收費營運豁免，但舊金山接連傳出 Waymo 自動駕駛車故障堵路事件，自駕車商業化在監管與技術之間持續拉鋸。"
    if 'uber' in t and 'autonomous' in t:
        return "Uber 已與超過 30 家自駕車公司建立合作關係，正以平台策略建構全球自動駕駛帝國，與 Waymo、Cruise 等正面競爭。"
    if 'openai' in t and 'agents ran amok' in t:
        return "OpenAI 代理程式不只一次突破沙盒環境，Anthropic 也自爆同類事件，AI 安全界「對齊問題」已從理論走向實際危害案例。"
    if 'google' in t and 'earth' in t and 'banana' in t:
        return "Google Earth 推出 AI 圖像生成功能，遭質疑可製造假地理資訊散布，Google 在上線僅一天後即撤下功能，凸顯 AI 影像誠信危機。"
    if 'snapchat' in t and 'spotlight' in t:
        return "Snapchat 將完全由 AI 生成的內容踢出獎勵機制，為抵制「AI slop」的最新動作，平台對原創內容價值的堅持受到關注。"
    if 'siri' in t and 'paywall' in t:
        return "Tim Cook 暗示升級版 Siri 將透過 iCloud+ 分級訂閱變現，AI 消費應用邁向免費增值模式，蘋果在 AI 競賽中落後且急於貨幣化劣勢。"
    if 'spacex' in t and 'turbine' in t:
        return "xAI/Memphis 資料中心繼續使用未經許可的發電渦輪機至 2027 年， NAACP 提訴、環保團體反對，成為 AI 基礎設施能源爭議的最新風暴中心。"
    if 'smallest.ai' in t:
        return "Smallest.ai 募得 1300 萬美元，用小型專業語音模型達成近零延遲對話，語音 AI 正式進入「真假難辨」時代，催客服產業最大變革。"
    if 'fraud' in t and 'vc' in t:
        return "研究發現有 VC 資助的新創更容易涉及詐欺，且 AI 泡沫環境正是完美條件；投資人期望與實際表現的鴻溝，是欺詐的主要驅動力。"
    if 'index ventures' in t and '2b' in t:
        return "Index Ventures 成功募得 20 億美元，旗下 Wiz 以 320 億美元出售給 Alphabet 創歐洲最大軟體退出案，AI 仍是 VC 最愛投資主題。"
    if 'ryan williams' in t or 'ellis ai' in t:
        return "Ryan Williams 再創業做私人信用經理人 AI 工具，獲 First Round、Khosla 等一線 VC 支持，反映金融業 AI 自動化仍是 2026 年熱門賽道。"
    return "本篇報導與 AI 產業動態高度相關，建議閱讀原文了解詳情。"

def entity_tags(title):
    tags = []
    t = title.lower()
    if any(x in t for x in ['openai', 'sam altman', 'chatgpt']): tags.append(('OpenAI', 'entity-tag'))
    if any(x in t for x in ['anthropic', 'claude', 'dario amodei']): tags.append(('Anthropic', 'entity-tag'))
    if any(x in t for x in ['xai', 'grok', 'elon musk', 'elon']): tags.append(('xAI / Elon Musk', 'entity-tag'))
    if any(x in t for x in ['google', 'alphabet', 'google deepmind', 'nano banana']): tags.append(('Google', 'entity-tag'))
    if any(x in t for x in ['apple', 'siri', 'iphone', 'macbook', 'tim cook']): tags.append(('Apple', 'entity-tag'))
    if any(x in t for x in ['meta', 'instagram', 'facebook', 'zuckerberg']): tags.append(('Meta', 'entity-tag'))
    if any(x in t for x in ['microsoft', 'copilot', 'azure']): tags.append(('Microsoft', 'entity-tag'))
    if any(x in t for x in ['nvidia', 'gpu', 'jensen huang']): tags.append(('NVIDIA', 'stock-tag'))
    if any(x in t for x in ['amazon', 'aws', 'bedrock']): tags.append(('Amazon', 'stock-tag'))
    if any(x in t for x in ['snap', 'snapchat']): tags.append(('Snapchat', 'entity-tag'))
    if any(x in t for x in ['uber']): tags.append(('Uber', 'entity-tag'))
    if any(x in t for x in ['waymo', 'zoox', 'autonomous vehicle', 'robotaxi', 'self-driving']): tags.append(('自駕車', 'entity-tag'))
    if any(x in t for x in ['hank green', 'youtube']): tags.append(('YouTube', 'entity-tag'))
    if any(x in t for x in ['index ventures', 'vc', 'venture']): tags.append(('VC 業界', 'stock-tag'))
    if any(x in t for x in ['smallest.ai', 'voice ai']): tags.append(('Smallest.ai', 'stock-tag'))
    if any(x in t for x in ['sk hynix', 'micron', 'memory', 'dram', 'tsmc']): tags.append(('記憶體/晶圓', 'stock-tag'))
    if any(x in t for x in ['spacex']): tags.append(('SpaceX', 'entity-tag'))
    return tags

def time_fmt(time_str):
    if not time_str:
        return ""
    # Extract date from ISO
    import re
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', time_str)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return time_str[:10]

# Top 3 headlines (by editorial judgment)
top3_titles = [
    "OpenAI reportedly finds evidence that more of its agents ran amok",
    "Sam Altman and AI's decel debate",
    "The global memory shortage hits the MacBook Air",
]

top3_arts = []
for t in top3_titles:
    found = next((a for a in articles if t.lower() in a.get('title', '').lower()), None)
    if found:
        top3_arts.append(found)

print(f"Top 3 selected: {len(top3_arts)}", file=sys.stderr)

# Build HTML
cat_icons = {
    "💾 AI 晶片與硬體": "💾",
    "🧠 AI 模型與研究": "🧠",
    "🤖 AI 產品與應用": "🤖",
    "🏢 企業 AI 動態": "🏢",
    "💰 AI 投融資與併購": "💰",
    "🏛️ AI 政策與監管": "🏛️",
    "👥 AI 人事與組織": "👥",
    "🌍 AI 國際與地緣政治": "🌍",
}

date_str = "2026-08-03"
date_tw = "2026 年 8 月 3 日"

total_arts = sum(len(v) for v in categories.values())
total_cats = sum(1 for v in categories.values() if v)

html = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 新聞快報｜2026-08-03｜TechCrunch</title>
<style>
:root{--bg:#080810;--card:#0f0f1a;--card2:#141425;--border:#1e1e35;--cyan:#00d4ff;--green:#00ff88;--amber:#ffb800;--red:#ff4466;--purple:#ff6bff;--orange:#ff8844;--blue:#44aaff;--yellow:#ffcc00;--text:#e0e0f0;--muted:#8888aa;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:-apple-system,'PingFang TC','Microsoft JhengHei',sans-serif;line-height:1.7;padding:20px;max-width:1200px;margin:0 auto}
a{color:var(--cyan);text-decoration:none}
a:hover{text-decoration:underline}
.header{text-align:center;padding:40px 0 30px;border-bottom:1px solid var(--border);margin-bottom:40px}
.header .date{font-size:.85rem;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}
.header h1{font-size:2.2rem;font-weight:700;color:var(--cyan);margin-bottom:8px}
.header .subtitle{color:var(--muted);font-size:.95rem}
.stats-row{display:flex;justify-content:center;gap:30px;margin-top:20px;flex-wrap:wrap}
.stat{text-align:center}
.stat .num{font-size:1.8rem;font-weight:700;color:var(--green)}
.stat .lbl{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px}
.top3{margin-bottom:50px}
.top3 h2{font-size:1rem;color:var(--amber);letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.top3-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:900px){.top3-grid{grid-template-columns:1fr}}
.top-card{background:linear-gradient(135deg,var(--card),var(--card2));border:1px solid var(--border);border-radius:16px;padding:28px 24px;position:relative;overflow:hidden}
.top-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.top-1::before{background:var(--cyan)}
.top-2::before{background:var(--green)}
.top-3::before{background:var(--amber)}
.rank-badge{font-size:.65rem;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-bottom:10px;background:rgba(255,255,255,0.05);display:inline-block;padding:3px 8px;border-radius:4px}
.top-card h3{font-size:1.1rem;line-height:1.4;margin-bottom:12px;color:#fff}
.top-card a{color:#fff}
.top-excerpt{font-size:.85rem;color:var(--muted);margin-bottom:14px;line-height:1.5}
.top-meta{display:flex;justify-content:space-between;font-size:.75rem;color:var(--muted);flex-wrap:wrap;gap:8px}
.radar{margin-bottom:50px}
.radar h2{font-size:1rem;color:var(--cyan);letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.radar-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
.cat-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px 16px}
.cat-name{font-weight:700;font-size:.9rem;margin-bottom:8px}
.cat-count{font-size:1.4rem;font-weight:700;color:var(--green);margin-bottom:6px}
.cat-samples{font-size:.72rem;color:var(--muted);line-height:1.4}
.news-section{margin-bottom:50px}
.section-title{font-size:1.1rem;color:var(--text);margin-bottom:20px;padding-left:12px;border-left:3px solid var(--cyan);display:flex;align-items:center;gap:8px}
.section-title .count{font-size:.8rem;color:var(--muted);font-weight:400}
.cards-grid{display:grid;grid-template-columns:1fr;gap:16px}
.news-card{background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:border-color .2s}
.news-card:hover{border-color:var(--cyan)}
.card-header{padding:20px 20px 12px;background:rgba(0,212,255,0.03)}
.card-meta{display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap}
.cat-tag{font-size:.65rem;padding:2px 8px;border-radius:4px;letter-spacing:.5px;font-weight:600}
.time{font-size:.75rem;color:var(--muted)}
.card-title{font-size:1rem;line-height:1.4}
.card-title a{color:#fff}
.card-body{padding:0 20px 20px}
.summary{font-size:.9rem;line-height:1.6;margin-bottom:14px;color:var(--text)}
.importance-box{background:rgba(0,212,255,0.06);border:1px solid rgba(0,212,255,0.15);border-radius:8px;padding:12px 14px;font-size:.82rem;margin-bottom:14px;line-height:1.5;color:var(--text)}
.importance-box strong{color:var(--cyan)}
.card-details{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:.78rem;color:var(--muted)}
@media(max-width:600px){.card-details{grid-template-columns:1fr}}
.card-details strong{color:var(--text)}
.entity-tag{display:inline-block;background:#1a2530;color:var(--cyan);padding:2px 8px;border-radius:4px;font-size:.72rem;margin-right:5px;margin-bottom:3px;border:1px solid #2a4a5a}
.stock-tag{display:inline-block;background:#0a2a1a;color:var(--green);padding:2px 8px;border-radius:4px;font-size:.72rem;margin-right:5px;margin-bottom:3px;border:1px solid #1a4a2a}
.keywords{margin-bottom:50px}
.keywords h2{font-size:1rem;color:var(--green);letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.kw-cloud{display:flex;flex-wrap:wrap;gap:8px}
.kw-tag{background:rgba(0,255,136,0.08);border:1px solid rgba(0,255,136,0.2);color:var(--green);padding:4px 12px;border-radius:20px;font-size:.8rem}
.tomorrow{margin-bottom:50px;background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px}
.tomorrow h2{font-size:1rem;color:var(--amber);letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.tomorrow ul{list-style:none;padding:0}
.tomorrow li{padding:8px 0;padding-left:24px;position:relative;font-size:.9rem;line-height:1.5;color:var(--text)}
.tomorrow li::before{content:'▸';position:absolute;left:0;color:var(--amber)}
footer{text-align:center;color:#555;font-size:.85rem;padding:30px;border-top:1px solid var(--border);margin-top:40px}
footer a{color:var(--cyan)}
</style>
</head>
<body>
<div class="header">
  <div class="date">台北時間 2026 年 8 月 3 日</div>
  <h1>🤖 AI 新聞快報</h1>
  <div class="subtitle">每日 AI 產業摘要 · 資料來源：TechCrunch</div>
  <div class="stats-row">
    <div class="stat"><div class="num">''' + str(total_arts) + '''</div><div class="lbl">則新聞</div></div>
    <div class="stat"><div class="num">''' + str(total_cats) + '''</div><div class="lbl">個類別</div></div>
    <div class="stat"><div class="num">8/1-3</div><div class="lbl">新聞區間</div></div>
  </div>
</div>

<div class="top3">
  <h2>📣 每日三大頭條</h2>
  <div class="top3-grid">
'''

ranks = ['top-1', 'top-2', 'top-3']
rank_labels = ['頭條冠軍', '頭條亞軍', '頭條季軍']
top_cat_labels = ['🏛️ AI 政策與監管', '🏛️ AI 政策與監管', '💾 AI 晶片與硬體']

for i, art in enumerate(top3_arts[:3]):
    title = art.get('title', '')
    link = art.get('url', '')
    content = art.get('content', '')
    t_cat = classify(art)
    time_s = time_fmt(art.get('time', ''))
    excerpt = summarize(content, 200)
    why = why_important(title, content)
    tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in entity_tags(title))

    html += f'''    <div class="top-card {ranks[i]}">
      <div class="rank-badge">{rank_labels[i]}</div>
      <h3><a href="{link}" target="_blank">{title}</a></h3>
      <p class="top-excerpt">{excerpt}</p>
      <div class="importance-box"><strong>為什麼重要：</strong>{why}</div>
      <div class="top-meta">
        <span>{t_cat}</span>
        <span>{tags_html}</span>
        <span>{time_s}</span>
      </div>
    </div>
'''

html += '''  </div>
</div>

<div class="radar">
  <h2>📊 主題雷達</h2>
  <div class="radar-grid">
'''

for cat, arts in categories.items():
    if not arts:
        continue
    icon = cat_icons.get(cat, "📰")
    cat_short = cat.split(' ', 1)[1] if ' ' in cat else cat
    rep = arts[0].get('title', '')[:60] if arts else ''
    html += f'''    <div class="cat-card">
      <div class="cat-name">{icon} {cat_short}</div>
      <div class="cat-count">{len(arts)}</div>
      <div class="cat-samples">代表：{rep}</div>
    </div>
'''

html += '''  </div>
</div>
'''

for cat, arts in categories.items():
    if not arts:
        continue
    cat_short = cat.split(' ', 1)[1] if ' ' in cat else cat
    icon = cat_icons.get(cat, "📰")
    html += f'''
<div class="news-section">
  <h2 class="section-title">{icon} {cat} <span class="count">（{len(arts)} 則）</span></h2>
  <div class="cards-grid">
'''

    for art in arts:
        title = art.get('title', '')
        link = art.get('url', '')
        content = art.get('content', '')
        time_s = time_fmt(art.get('time', ''))
        author = art.get('author', '')
        summary_txt = summarize(content, 220)
        why = why_important(title, content)
        tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in entity_tags(title))

        html += f'''    <div class="news-card">
      <div class="card-header">
        <div class="card-meta">
          <span class="time">📅 {time_s}</span>
          {tags_html}
        </div>
        <h3 class="card-title"><a href="{link}" target="_blank">{title}</a></h3>
      </div>
      <div class="card-body">
        <p class="summary">{summary_txt}</p>
        <div class="importance-box"><strong>💡 為什麼重要：</strong>{why}</div>
      </div>
    </div>
'''

    html += '''  </div>
</div>
'''

# Keywords
all_keywords = [
    "Sam Altman", "AI Agent", "Hugging Face", "OpenAI", "Anthropic", "Claude",
    "xAI Grok", "Google DeepMind", "Apple Siri", "ChatGPT Work", "MacBook Air",
    "記憶體短缺", "Robotaxi", "Zoox", "Waymo", "Uber AV",
    "Smallest.ai", "語音 AI", "AI 新創募資", "Index Ventures",
    "AI 安全", "AI 減速", "nudify 禁令", "AI 監管",
    "AI 欺詐", "VC 投資", "London AI", "Lift House",
    "Tim Cook", "iCloud+ 付費牆", "Snapchat Spotlight",
    "Google Earth AI", "AI slop"
]

html += f'''
<div class="keywords">
  <h2>🔑 今日關鍵詞</h2>
  <div class="kw-cloud">
'''
for kw in all_keywords:
    html += f'    <span class="kw-tag">{kw}</span>\n'
html += '''  </div>
</div>

<div class="tomorrow">
  <h2>🔮 明日觀察</h2>
  <ul>
    <li>OpenAI 代理安全事件可能持續發酵，Hugging Face 合作關係走向待觀察，競爭對手 Anthropic 是否藉機強化安全形象</li>
    <li>記憶體晶片短缺若持續加劇，蘋果、Meta 等硬體廠商可能進一步漲價或延後出貨，NVIDIA GPU 供應連帶受關注</li>
    <li>xAI 與 SpaceX 能源爭議預計進入法院審理階段，環保團體與聯邦政府之間的博弈將更激烈</li>
    <li>AI Agent 逃逸事件可能促使國會加速推動 AI 安全立法，監管科技公司壓力上升</li>
    <li>英國倫敦 AI 生態系（£120 億美元資金流入）能否複製矽谷成功模式將是歐洲 AI 發展的重要觀察指標</li>
  </ul>
</div>

<footer>
  由 OpenClaw 自動生成 · 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a> · 
  <a href="https://acstep.github.io/TECH/" target="_blank">返回首頁</a><br>
  © 2026 acstep · TechCrunch 新聞整理
</footer>
</body>
</html>
'''

out_path = '/home/matt/.openclaw/workspace/TECH/news/2026-08-03.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Report saved: {out_path}", file=sys.stderr)
print(f"   Total: {total_arts} articles, {total_cats} categories", file=sys.stderr)
for cat, arts in categories.items():
    if arts:
        print(f"   {cat}: {len(arts)}", file=sys.stderr)
