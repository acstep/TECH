#!/usr/bin/env python3
import json
from datetime import date

with open('/tmp/articles_data.json') as f:
    articles = json.load(f)

categories = {
    "💾 AI 晶片與硬體": [],
    "🧠 AI 模型與研究": [],
    "🤖 AI 產品與應用": [],
    "💰 AI 投融資": [],
    "🏛️ AI 政策與監管": [],
    "🌍 AI 國際動態": [],
}

for a in articles:
    t = a['title']
    if 'SK Hynix' in t or "Meta's new AI chips" in t or 'Nvidia is a victim' in t:
        categories["💾 AI 晶片與硬體"].append(a)
    elif any(x in t for x in ['OpenAI launches', 'OpenAI says GPT 5.6', 'Meta enters', "Anthropic's new Claude", 'How did the government', 'Meta Muse Spark']):
        categories["🧠 AI 模型與研究"].append(a)
    elif any(x in t for x in ['Meta removes', 'Atlas', 'Google will now', 'Instagram users: How']):
        categories["🤖 AI 產品與應用"].append(a)
    elif any(x in t for x in ['Gradium', 'Ollama', '$100M fundraise', 'bigger than the last 25']):
        categories["💰 AI 投融資"].append(a)
    elif any(x in t for x in ['Apple sues', 'New York Times says OpenAI hid']):
        categories["🏛️ AI 政策與監管"].append(a)
    else:
        categories["🌍 AI 國際動態"].append(a)

# Top headlines
top3 = [
    ("Apple sues OpenAI over alleged trade secret theft", "https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/"),
    ("SK Hynix raises $26.5B in biggest foreign IPO in US history", "https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/"),
    ("OpenAI launches its new family of models with GPT-5.6", "https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/"),
]

def summarize(content, max_len=200):
    sentences = content.split('. ')
    result = ''
    for s in sentences:
        if len(result) + len(s) < max_len:
            result += s + '. '
        else:
            break
    return result.strip()

def why_important(title, content):
    if 'Apple sues OpenAI' in title:
        return "蘋果直接狀告 OpenAI 竊取商業機密，凸顯 AI 硬體人才爭奪戰白熱化，OpenAI 自研硬體傳聞並非空穴來風。"
    elif 'SK Hynix' in title:
        return "南韓記憶體巨頭赴美集資 265 億美元創紀錄，HBM 為 AI GPU 關鍵元件，記憶體廠集體被華府催促進美國設廠。"
    elif 'GPT-5.6' in title and 'launches' in title:
        return "OpenAI一口氣發布 Sol / Terra / Luna 三款模型，直接對標 Anthropic Fable 5，定價更有競爭力，企業 Copilot 大戰開打。"
    elif 'GPT 5.6' in title and 'preferred model' in title:
        return "OpenAI 急忙宣布自己是 Microsoft 365 Copilot 的「首選模型」，反駁雙方分手傳言，但微軟同時也在用自家 MAI 模型降低成本。"
    elif 'Atlas' in title:
        return "OpenAI 關閉 Atlas 瀏覽器，但把功能整合進 ChatGPT 桌面版與 Chrome 擴充功能，AI 瀏覽器戰爭仍在繼續。"
    elif 'Meta removes' in title:
        return "Meta 上線僅數天即撤下爭議功能：用戶可用 AI 以他人 Instagram 照片生成圖像，引發隱私與侵權反彈。"
    elif 'Meta AI chips' in title:
        return "Meta 自主 AI 晶片 9 月投產，交由 Broadcom 設計、TSMC 代工，目標減少對 NVIDIA/AMD 的依賴。"
    elif 'Nvidia is a victim' in title:
        return "GPU 短缺緩解、記憶體成新瓶頸，NVIDIA 股價自高點跌 15%，Micron 股價卻飆漲近 3 倍。"
    elif 'Elon Musk' in title:
        return "馬斯克大讚 Anthropic 為「AI 領先者」，並透露已與 Anthropic 簽署 400 億美元算力合約，SpaceX 成為最大 AI 基礎設施供應商。"
    elif 'Fidji Simo' in title:
        return "OpenAI 二號人物閃辭，Altman 須立即尋找接班人，正值 OpenAI 籌備 IPO 之際，領導真空風險加劇。"
    elif 'Apple sues' in title:
        return "蘋果狀告 OpenAI 挖角竊密，包括前 iPhone 硬體主管 Tang Tan，劍指 OpenAI 自研手機威脅蘋果核心事業。"
    elif 'Anthropic Claude' in title:
        return "Anthropic 推出 Claude Reflect 功能，以「AI 使用分析」培養用戶忠誠度，悄悄提升黏著度與轉換成本。"
    elif 'Hugging Face' in title:
        return "開源 AI 平台 Hugging Face 執行長：企業租用 Frontier API 成本太高，最終都會轉向開源模型。"
    elif 'Lyzr' in title:
        return "AI Agent 新創 Lyzr 靠自家 Agent 完成 1 億美元 B 輪募資，無需創辦人親自拜會，展現 AI Agent 自我銷售能力。"
    elif 'Gradium' in title:
        return "法國 AI 語音新創 Gradium 獲 Nvidia 支持，募得 1 億美元種子輪，無延遲語音生成為核心優勢，已獲雷諾採用。"
    elif 'Ollama' in title:
        return "開源 AI 本地執行工具 Ollama 募得 6500 萬美元 B 輪，每月 890 萬開發者使用，14 人團隊撐起企業 AI 版圖。"
    elif 'Anthropic, OpenAI, SpaceX' in title:
        return "SpaceX 估值 1.77 兆美元上市， Anthropic + OpenAI 合計估值數兆，三家 IPO 產生的價值超越 2000 年以來所有美國 VC 退出案總和。"
    elif 'Can AI answer the $3 trillion' in title:
        return "AI 基礎設施投資需創造 3 兆美元營收才能回本，記憶體成本持續攀升、算力價格下跌，專家警告可能觸發經濟震盪。"
    elif 'Google will now disclose' in title:
        return "Google 要求廣告主揭露 AI 生成內容，但僅限自願申報，監管強度引發質疑。"
    elif 'NYT says OpenAI hid evidence' in title:
        return "紐約時報指控 OpenAI 在版權訴訟中隱瞞證據，包括已建立 7800 萬筆對話資料庫與主動刪除可能有害輸出。"
    elif 'How did the government' in title:
        return "政府如何判定 OpenAI 前沿模型「安全可發布」？專家坦言：流程不透明，監管框架仍是一片空白。"
    elif 'Instagram users' in title:
        return "用戶可拒絕自己的公開照片被拿來餵給 Meta AI，設定方法一次看。"
    elif 'Muse Spark' in title:
        return "Meta 進軍 AI 編碼市場，Muse Spark 1.1 每百萬 Token 1.25 美元，Zuckerberg 三年來首度發文力挺。"
    else:
        return "本篇報導與 AI 產業發展趨勢高度相關，建議閱讀原文了解詳情。"

def entity_tags(title):
    tags = []
    if any(x in title for x in ['Apple', 'iPhone']): tags.append(('Apple', 'entity-tag'))
    if any(x in title for x in ['OpenAI', 'ChatGPT', 'GPT']): tags.append(('OpenAI', 'entity-tag'))
    if any(x in title for x in ['Anthropic', 'Claude']): tags.append(('Anthropic', 'entity-tag'))
    if any(x in title for x in ['Meta', 'Instagram', 'Facebook']): tags.append(('Meta', 'entity-tag'))
    if any(x in title for x in ['Google', 'Gemini']): tags.append(('Google', 'entity-tag'))
    if any(x in title for x in ['Microsoft', 'Copilot']): tags.append(('Microsoft', 'entity-tag'))
    if any(x in title for x in ['Nvidia', 'GPU']): tags.append(('NVIDIA', 'entity-tag'))
    if any(x in title for x in ['SK Hynix', 'HBM']): tags.append(('SK Hynix', 'stock-tag'))
    if any(x in title for x in ['SpaceX', 'Musk']): tags.append(('SpaceX/xAI', 'entity-tag'))
    if any(x in title for x in ['Hugging Face']): tags.append(('Hugging Face', 'entity-tag'))
    if any(x in title for x in ['Sequoia', 'Benchmark', 'VC']): tags.append(('VC/PE', 'stock-tag'))
    return tags

# Generate HTML
html = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 每日新聞分析報告 - 2026-07-11</title>
    <style>
        :root {
            --bg-color: #080810;
            --card-bg: #12121f;
            --card-bg-hover: #1a1a2e;
            --primary: #00d4ff;
            --secondary: #00ff88;
            --text-main: #e0e0e0;
            --text-muted: #a0a0a0;
            --border: #2a2a3a;
            --accent-gradient: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'PingFang TC', 'Microsoft JhengHei', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.7;
            margin: 0; padding: 0;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header {
            text-align: center;
            padding: 40px 0 30px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 30px;
        }
        header h1 {
            font-size: 2.5rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }
        header .subtitle { color: var(--text-muted); font-size: 1rem; }
        .meta-info {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 18px;
            flex-wrap: wrap;
        }
        .meta-item {
            background: var(--card-bg);
            padding: 6px 16px;
            border-radius: 20px;
            border: 1px solid var(--border);
            font-size: 0.9rem;
            color: var(--text-muted);
        }
        .section-title {
            font-size: 1.6rem;
            margin: 45px 0 20px;
            border-left: 4px solid var(--primary);
            padding-left: 15px;
            color: var(--primary);
        }
        .top-stories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .story-card-big {
            background: linear-gradient(135deg, var(--card-bg) 0%, var(--card-bg-hover) 100%);
            border: 1px solid var(--primary);
            border-radius: 14px;
            padding: 24px;
            position: relative;
            transition: all 0.3s;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .story-card-big:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
        }
        .story-rank {
            display: inline-block;
            font-size: 0.8rem;
            color: var(--primary);
            border: 1px solid var(--primary);
            padding: 2px 10px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-weight: 600;
        }
        .story-card-big h3 { margin: 5px 0 12px 0; font-size: 1.25rem; }
        .story-card-big h3 a { color: var(--primary); text-decoration: none; }
        .story-card-big h3 a:hover { text-decoration: underline; }
        .story-tagline { color: #c8c8d0; font-size: 0.92rem; line-height: 1.6; }
        .story-meta {
            display: flex;
            gap: 12px;
            margin-top: 14px;
            font-size: 0.8rem;
            color: var(--text-muted);
            flex-wrap: wrap;
        }
        .radar-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 14px;
            margin-bottom: 20px;
        }
        .radar-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 18px 14px;
            text-align: center;
            transition: all 0.3s;
        }
        .radar-card:hover {
            transform: translateY(-3px);
            background: var(--card-bg-hover);
        }
        .radar-emoji { font-size: 1.8rem; margin-bottom: 6px; }
        .radar-count { font-size: 1.8rem; font-weight: bold; display: block; }
        .radar-label { font-size: 0.9rem; color: var(--text-main); margin: 4px 0 6px; font-weight: 500; }
        .radar-rep { font-size: 0.75rem; color: var(--text-muted); line-height: 1.4; }
        .category-group { margin-bottom: 40px; }
        .category-header {
            font-size: 1.35rem;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 10px;
        }
        .cat-count { color: var(--text-muted); font-size: 0.85rem; font-weight: normal; }
        .news-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 22px;
            margin-bottom: 14px;
            transition: all 0.3s;
        }
        .news-card:hover {
            background: var(--card-bg-hover);
            border-color: rgba(0, 212, 255, 0.3);
        }
        .news-card h4 { margin: 0 0 8px 0; font-size: 1.15rem; }
        .news-card h4 a { color: var(--primary); text-decoration: none; }
        .news-card h4 a:hover { text-decoration: underline; }
        .news-meta {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-bottom: 12px;
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }
        .news-summary { margin-bottom: 14px; color: var(--text-main); }
        .analysis-box {
            background: rgba(0, 212, 255, 0.05);
            border-left: 3px solid var(--primary);
            padding: 10px 15px;
            margin-bottom: 12px;
            font-size: 0.88rem;
            color: #c0e0f0;
        }
        .entity-tag {
            display: inline-block;
            background: #1a2530;
            color: var(--primary);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            margin-right: 5px;
            margin-bottom: 4px;
            border: 1px solid #2a4a5a;
        }
        .stock-tag {
            display: inline-block;
            background: #0a2a1a;
            color: var(--secondary);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            margin-right: 5px;
            margin-bottom: 4px;
            border: 1px solid #1a4a2a;
        }
        footer {
            text-align: center;
            color: #555;
            font-size: 0.9em;
            padding: 40px 20px;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 60px;
        }
        footer a { color: var(--primary); text-decoration: none; }
        @media (max-width: 600px) {
            header h1 { font-size: 1.8rem; }
            .top-stories { grid-template-columns: 1fr; }
            .radar-grid { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
</head>
<body>
<div class="container">
<header>
    <h1>📰 TECH — AI 每日新聞摘要</h1>
    <p class="subtitle">資料來源：TechCrunch · 報告日期：2026-07-11（台北時間）</p>
    <div class="meta-info">
        <span class="meta-item">📊 22 則新聞</span>
        <span class="meta-item">🏷️ 6 個分類</span>
        <span class="meta-item">🤖 AI 為主</span>
    </div>
</header>

<h2 class="section-title">🔥 今日頭條 Top 3</h2>
<div class="top-stories">
'''

for i, (title, link) in enumerate(top3):
    art = next((a for a in articles if a['title'] == title), None)
    if art:
        summary = summarize(art['content'], 180)
        why = why_important(title, art['content'])
        tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in entity_tags(title))
        html += f'''    <div class="story-card-big">
        <div class="story-rank">#{i+1} 頭條</div>
        <h3><a href="{link}" target="_blank">{title}</a></h3>
        <p class="story-tagline">{summary}</p>
        <div class="analysis-box">💡 為什麼重要：{why}</div>
        <div class="story-meta">{tags_html}</div>
    </div>
'''

html += '''</div>

<h2 class="section-title">📊 今日數據總覽</h2>
<div class="radar-grid">
'''

cat_icons = {
    "💾 AI 晶片與硬體": "💾",
    "🧠 AI 模型與研究": "🧠",
    "🤖 AI 產品與應用": "🤖",
    "💰 AI 投融資": "💰",
    "🏛️ AI 政策與監管": "🏛️",
    "🌍 AI 國際動態": "🌍",
}

for cat, arts in categories.items():
    icon = cat_icons.get(cat, "📰")
    cat_short = cat.split(' ', 1)[1] if ' ' in cat else cat
    html += f'''    <div class="radar-card">
        <div class="radar-emoji">{icon}</div>
        <span class="radar-count">{len(arts)}</span>
        <div class="radar-label">{cat_short}</div>
        <div class="radar-rep">{', '.join(a['title'].split(' on ')[0].split(' ')[0:2]) if arts else '—'}</div>
    </div>
'''

html += '''</div>
'''

for cat, arts in categories.items():
    cat_short = cat.split(' ', 1)[1] if ' ' in cat else cat
    html += f'''
<h2 class="section-title">{cat} <span class="cat-count">（{len(arts)} 則）</span></h2>
<div class="category-group">
'''
    for a in arts:
        title = a['title']
        link = a['link']
        content = a['content']
        summary = summarize(content, 180)
        why = why_important(title, content)
        tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in entity_tags(title))
        html += f'''    <div class="news-card">
        <h4><a href="{link}" target="_blank">{title}</a></h4>
        <div class="news-meta">
            {tags_html}
        </div>
        <p class="news-summary">{summary}</p>
        <div class="analysis-box">💡 為什麼重要：{why}</div>
    </div>
'''

html += '''
<footer>
    <p>由 OpenClaw 自動生成 · 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a></p>
    <p style="margin-top:10px;">© 2026 acstep</p>
</footer>
</div>
</body>
</html>
'''

with open('/home/matt/.openclaw/workspace/TECH/news/2026-07-11.html', 'w') as f:
    f.write(html)

print("Report generated: /home/matt/.openclaw/workspace/TECH/news/2026-07-11.html")
print(f"Total articles: {len(articles)}")
for cat, arts in categories.items():
    print(f"  {cat}: {len(arts)}")
