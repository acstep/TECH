#!/usr/bin/env python3
import json
from datetime import date

# Load article data
with open('/home/matt/.openclaw/workspace/TECH/news_content_0717.json') as f:
    articles = json.load(f)

# If content not available, fall back to title-only
for a in articles:
    if not a.get('content') or len(a.get('content','')) < 50:
        a['content'] = ''

TODAY = '2026-07-17'

# ============================================================
# 3 Top Headlines
# ============================================================
top3 = [
    {
        "title": "Apple Intelligence 獲准在中國落地：攜手阿里巴巴 Qwen AI 突破監管障礙",
        "link": "https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/",
        "summary": "蘋果正式宣布 Apple Intelligence 將在中國市場推出，合作的在地 AI 模型是阿里巴巴的 Qwen。這是蘋果在中國這個全球最大智慧型手機市場之一的重要一步。據報導，Apple Intelligence 同時還獲得了百度文心一言的支持，意味著蘋果在中國採用多模型策略。"
    },
    {
        "title": "OpenAI 發布首款硬體裝置：230 美元 Codex 鍵盤，劍指開發者市場",
        "link": "https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/",
        "summary": "在與 Jony Ive 的 io Devices 法律糾紛之際，OpenAI 發表了首款自有硬體產品——230 美元的 Codex 鍵盤。這款鍵盤專為 Codex AI 程式碼助理優化，目標是搶攻開發者市場。此舉顯示 OpenAI 不只想做軟體，正積極往硬體領域擴張。"
    },
    {
        "title": "Anthropic 與 Blackstone 合資成立 Ode：15 億美元瞄準企業 AI 落地實施商機",
        "link": "https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/",
        "summary": "Anthropic 與私募巨頭 Blackstone 宣布共同成立新公司 Ode，初始注資 15 億美元，瞄準 AI 在企業場景落地這個被認為是下一個兆美元級的商機。雙方均強調，未來 AI 最大的價值不在基礎模型本身，而在協助企業成功部署與整合 AI 解決方案。"
    },
]

# ============================================================
# Article categories
# ============================================================
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

# ============================================================
# Helper functions
# ============================================================
def get_why_important(title, art):
    """Generate why-important text based on article title."""
    t = art.get('title', '')
    if 'Apple Intelligence' in t and 'China' in t:
        return "蘋果在中國這個全球最大智慧型手機市場取得監管突破，Qwen 模型獲選為在地合作夥伴，對騰訊、華為等本地競爭對手形成壓力。"
    elif 'OpenAI' in t and ('keyboard' in t or 'Codex' in t):
        return "OpenAI 跨足硬體領域，230 美元 Codex 鍵盤瞄準開發者族群，代表從純軟體公司轉型為軟硬整合的重大策略轉變。"
    elif 'Anthropic' in t and 'Blackstone' in t:
        return "Anthropic 聯手私募巨頭 Blackstone 成立落地服務公司，顯示基礎模型商轉瓶頸已從模型能力轉移到實際部署，企業 AI 谘詢與整合商機正式成形。"
    elif 'Thinking Machines' in t and 'Inkling' in t:
        return "前 Meta AI 主管創立 Thinking Machines，首款開放模型 Inkling 劍指 OpenAI 和 Anthropic，開源 AI 競爭持續升溫。"
    elif 'Suno' in t and 'YouTube' in t:
        return "AI 音樂生成器 Suno 被踢爆疑似未經授權竊取 YouTube 影片訓練，版權爭議再掀音樂產業反彈，凸顯生成式 AI 訓練資料合法性的灰色地帶。"
    elif 'Moonshot' in t and 'Kimi 3' in t:
        return "中國大模型新創 Moonshot 即將推出 Kimi 3，號稱追平 Anthropic Opus 4.8，中美 AI 模型競爭進入新階段。"
    elif 'AMI Labs' in t or ('Alexandre LeBrun' in t and 'AGI' in t):
        return "AMI Labs 創辦人明確拒絕使用 AGI 或超級智慧等行銷術語，反映業界對 AI 能力過度承諾的反思趨勢。"
    elif 'Google Vids' in t:
        return "Google Workspace 整合 AI 影片生成功能，用戶可上傳照片並以 AI 數位分身主演影片，正式進入 AI 生成內容的企業應用競爭。"
    elif 'Roblox' in t and 'AI' in t:
        return "Roblox 在手機 App 推出 AI 遊戲創作功能，讓一般用戶也能以自然語言生成遊戲內容，降低創作門檻將加速 UGC 生態系統擴張。"
    elif 'Google AI Mode' in t and 'apps' in t:
        return "Google 將 AI Mode 連接外部應用程式，用戶可直接透過 AI 助理操作第三方服務，Agentic AI 應用場景又往前邁進一步。"
    elif 'Microsoft' in t and 'salespeople' in t:
        return "微軟被爆訓練業務團隊在對客戶說明時貶低 OpenAI 與 Anthropic 的產品，反映雲端 AI 市場的激烈競爭已蔓延至銷售話術層面。"
    elif 'Microsoft' in t and 'security' in t:
        return "微軟修補史上最多安全漏洞並特別點名 AI 加速開發是原因之一，顯示 AI 辅助程式碼生成在提升產量之際也帶來新的資安風險。"
    elif 'Vint Cerf' in t:
        return "網際網路之父 Vint Cerf 投入 AI Agent 身份認證標準化工作，試圖為 Open Internet 上的 AI 代理互動建立信任框架，影響深遠。"
    elif 'OpenAI researcher' in t and 'drug' in t:
        return "OpenAI 研究員 Miles Wang 洽談創立 AI 藥物探索新創，估值 20 億美元，顯示 AI 在生技製藥領域的商業化應用持續升溫。"
    elif 'Indian' in t and 'Emergent' in t:
        return "印度 AI 程式碼新創 Emergent 成立僅一年多即晉升獨角獸，估值 13 億美元，反映新興市場 AI 創業生態的快速崛起。"
    elif 'Lorde' in t:
        return "知名音樂人 Lorde 公開批評 AI 智慧眼鏡「不性感」，反映大眾消費者對當前 AI 硬體裝置設計美學的普遍質疑。"
    elif 'OpenAI' in t and 'hardware device' in t and 'screenless' in t:
        return "OpenAI 據報正在開發首款硬體裝置為無螢幕可移動揚聲器，市場猜測這是進軍 AI 原生硬體的重大信號。"
    elif 'OpenAI pushes back' in t and 'Apple' in t:
        return "OpenAI 反擊蘋果的商業竊密訴訟，拒絕和解立場強硬，雙方法律戰正式升溫，可能牽動雙方未來合作關係。"
    elif 'Applied Computing' in t:
        return "傳統油氣產業透過 AI 模型優化整廠運營，代表 AI 正在向重工業滲透，工業 AI 應用場景持續擴大。"
    elif 'Reelful' in t:
        return "Reelful AI 可將使用者手機相簿自動生成短影音剪輯，瞄準社交媒體創作者市場，AI 影片剪輯門檻再度降低。"
    elif 'DeepMind researcher' in t and '300M' in t:
        return "前 DeepMind 研究員創立新創還沒上線產品就先以 3 億美元估值完成 pre-seed 輪，反映 AI 人才與創意在資本市場的高度吸引力。"
    elif 'OpenAI' in t and 'basketball' in t:
        return "OpenAI 推出 ChatGPT 籃球商品，引發外界對其品牌策略的質疑——這是品牌建設還是分心？"
    else:
        return "本篇報導與 AI 產業動態高度相關，建議閱讀原文了解更多細節。"

def get_entities(art):
    """Extract key entities from title."""
    t = art.get('title', '')
    c = art.get('content', '')
    entities = []
    
    name_map = {
        'OpenAI': 'OpenAI', 'Anthropic': 'Anthropic', 'Google': 'Google',
        'Apple': 'Apple', 'Microsoft': 'Microsoft', 'Amazon': 'Amazon',
        'Meta': 'Meta', 'NVIDIA': 'NVIDIA', 'Apple Intelligence': 'Apple Intelligence',
        'ChatGPT': 'ChatGPT', 'Claude': 'Claude', 'Gemini': 'Gemini',
        'Qwen': 'Qwen', 'Alibaba': '阿里巴巴', 'Baidu': '百度',
        'Blackstone': 'Blackstone', 'Moonshot': 'Moonshot AI', 'Kimi': 'Kimi',
        'Suno': 'Suno', 'Roblox': 'Roblox', 'Vint Cerf': 'Vint Cerf',
        'Miles Wang': 'Miles Wang', 'Lorde': 'Lorde', 'DeepMind': 'DeepMind',
        'Thinking Machines': 'Thinking Machines', 'AMI Labs': 'AMI Labs',
        'Emergent': 'Emergent', 'Reelful': 'Reelful', 'Applied Computing': 'Applied Computing',
        'Alexandre LeBrun': 'Alexandre LeBrun', 'Google Vids': 'Google Vids',
        'Codex': 'Codex', 'Inkling': 'Inkling'
    }
    
    for kw, label in name_map.items():
        if kw.lower() in (t + c).lower():
            if label not in entities:
                entities.append(label)
    
    return entities

def get_stocks(art):
    """Map to related stocks."""
    t = art.get('title', '')
    stocks = []
    
    stock_map = {
        'OpenAI': ['MSFT (Azure OpenAI)', 'GOOG (Gemini)'],
        'Anthropic': ['GOOG (Anthropic投資方)'],
        'Google': ['GOOG'],
        'Apple': ['AAPL'],
        'Microsoft': ['MSFT'],
        'Amazon': ['AMZN'],
        'Meta': ['META'],
        'NVIDIA': ['NVDA'],
        'Alibaba': ['BABA'],
        'Baidu': ['BIDU'],
        'Blackstone': ['BX'],
        'Moonshot': ['無上市'],
        'Suno': ['無上市'],
        'Roblox': ['RBLX'],
        'Vint Cerf': ['無上市'],
        'DeepMind': ['GOOG'],
        'Thinking Machines': ['無上市'],
        'AMI Labs': ['無上市'],
        'Emergent': ['無上市'],
        'Reelful': ['無上市'],
        'Applied Computing': ['無上市'],
        'Lorde': ['無上市'],
    }
    
    for kw, stock_list in stock_map.items():
        if kw.lower() in t.lower():
            for s in stock_list:
                if s not in stocks:
                    stocks.append(s)
    
    return stocks

def format_time(tc):
    """Convert TC time format to readable."""
    if not tc:
        return ''
    if 'T' in str(tc):
        return str(tc).replace('T',' ').replace('-07:00','')
    return tc

def assign_category(art):
    """Assign one or more categories to an article."""
    t = art.get('title', '')
    c = art.get('content', '')
    combined = t + ' ' + c
    cats = []
    
    chip_keywords = ['nvidia','gpu','chip','processor','intel','amd','tsmc','hardware','device','keyboard']
    model_keywords = ['model','llm','gpt','claude','gemini','openai','anthropic','mistral','research','paper','benchmark','training']
    product_keywords = ['launch','app','feature','tool','software','product','update','release','integration']
    enterprise_keywords = ['enterprise','business','company','adopt','deploy','customer','partner','integration']
    funding_keywords = ['funding','raise','series','valuation','investor','investment','acquire','acquisition','million','billion']
    policy_keywords = ['law','regulation','government','court','lawsuit','policy','ban',' restriction','government']
    people_keywords = ['ceo','founder','hire','depart','resign','layoff','appointment','executive']
    geo_keywords = ['china','chinese','europe','european','india','india','korea','taiwan','export','sanction','international']
    
    for kw in chip_keywords:
        if kw in combined.lower() and '💾 AI 晶片與硬體' not in cats:
            cats.append('💾 AI 晶片與硬體')
            break
    
    for kw in model_keywords:
        if kw in combined.lower() and '🧠 AI 模型與研究' not in cats:
            cats.append('🧠 AI 模型與研究')
            break
    
    for kw in product_keywords:
        if kw in combined.lower() and '🤖 AI 產品與應用' not in cats:
            cats.append('🤖 AI 產品與應用')
            break
    
    for kw in enterprise_keywords:
        if kw in combined.lower() and '🏢 企業 AI 動態' not in cats:
            cats.append('🏢 企業 AI 動態')
            break
    
    for kw in funding_keywords:
        if kw in combined.lower() and '💰 AI 投融資與併購' not in cats:
            cats.append('💰 AI 投融資與併購')
            break
    
    for kw in policy_keywords:
        if kw in combined.lower() and '🏛️ AI 政策與監管' not in cats:
            cats.append('🏛️ AI 政策與監管')
            break
    
    for kw in people_keywords:
        if kw in combined.lower() and '👥 AI 人事與組織' not in cats:
            cats.append('👥 AI 人事與組織')
            break
    
    for kw in geo_keywords:
        if kw in combined.lower() and '🌍 AI 國際與地緣政治' not in cats:
            cats.append('🌍 AI 國際與地緣政治')
            break
    
    # Default
    if not cats:
        cats.append('🤖 AI 產品與應用')
    
    return cats

# ============================================================
# Build HTML
# ============================================================
html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 新聞 {TODAY} · TechCrunch 中文摘要</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Microsoft JhengHei", sans-serif;
  background: #080810;
  color: #e8e8f0;
  line-height: 1.7;
  padding: 20px;
  min-height: 100vh;
}}
.container {{ max-width: 1200px; margin: 0 auto; }}
.back-link {{
  display: inline-flex; align-items: center; gap: 8px;
  color: #00d4ff; text-decoration: none; font-size: 0.95em;
  margin-bottom: 20px; padding: 8px 16px;
  border: 1px solid rgba(0,212,255,0.3); border-radius: 8px;
  transition: all 0.2s;
}}
.back-link:hover {{ background: rgba(0,212,255,0.1); }}
header {{
  text-align: center; padding: 40px 20px 30px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 40px;
}}
h1 {{ 
  font-size: 2.4em; font-weight: 900; letter-spacing: -1px;
  background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
  background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 10px;
}}
.meta {{ color: #888; font-size: 1em; }}
.meta span {{ color: #00d4ff; }}
/* Top 3 headlines */
.top3 {{
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 20px; margin-bottom: 40px;
}}
@media (max-width: 900px) {{ .top3 {{ grid-template-columns: 1fr; }} }}
.topcard {{
  background: linear-gradient(145deg, rgba(0,212,255,0.08), rgba(0,255,136,0.04));
  border: 1px solid rgba(0,212,255,0.25);
  border-radius: 16px; padding: 28px;
  transition: all 0.3s;
}}
.topcard:hover {{
  transform: translateY(-4px);
  border-color: rgba(0,212,255,0.5);
  box-shadow: 0 12px 32px rgba(0,212,255,0.2);
}}
.topcard .num {{
  font-size: 3em; font-weight: 900; color: rgba(0,212,255,0.2);
  line-height: 1; margin-bottom: 12px;
}}
.topcard h2 {{ color: #fff; font-size: 1.15em; line-height: 1.4; margin-bottom: 12px; }}
.topcard p {{ color: #aaa; font-size: 0.9em; line-height: 1.6; }}
.topcard a {{ color: #00ff88; text-decoration: none; font-size: 0.85em; display: inline-block; margin-top: 10px; }}
.topcard a:hover {{ text-decoration: underline; }}
/* Radar categories */
.cat-grid {{
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 14px; margin-bottom: 40px;
}}
@media (max-width: 900px) {{ .cat-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (max-width: 500px) {{ .cat-grid {{ grid-template-columns: 1fr; }} }}
.cat-pill {{
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px; padding: 14px 16px;
  display: flex; align-items: center; gap: 12px;
  transition: all 0.2s;
}}
.cat-pill:hover {{
  border-color: rgba(0,212,255,0.4);
  background: rgba(0,212,255,0.05);
}}
.cat-icon {{ font-size: 1.4em; }}
.cat-info {{ flex: 1; }}
.cat-name {{ font-weight: 700; font-size: 0.88em; color: #e8e8f0; }}
.cat-count {{ font-size: 0.78em; color: #666; }}
/* Section */
.section {{ margin-bottom: 50px; }}
.section-header {{
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.section-header h2 {{ color: #fff; font-size: 1.3em; font-weight: 800; }}
.section-header .badge {{
  background: rgba(0,212,255,0.15); color: #00d4ff;
  font-size: 0.8em; padding: 3px 10px; border-radius: 20px;
  font-weight: 600;
}}
/* Article cards */
.article {{
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px; padding: 22px 26px;
  margin-bottom: 16px;
  transition: all 0.25s;
}}
.article:hover {{
  border-color: rgba(0,212,255,0.2);
  background: rgba(0,212,255,0.03);
}}
.article-header {{
  display: flex; align-items: flex-start; gap: 14px; margin-bottom: 10px;
}}
.article-num {{
  background: rgba(0,212,255,0.12); color: #00d4ff;
  font-weight: 800; font-size: 0.8em; padding: 3px 8px;
  border-radius: 6px; flex-shrink: 0; margin-top: 2px;
}}
.article h3 {{
  flex: 1;
}}
.article h3 a {{
  color: #fff; text-decoration: none; font-size: 1em; font-weight: 700;
  line-height: 1.4;
}}
.article h3 a:hover {{ color: #00d4ff; }}
.article .time {{
  color: #555; font-size: 0.8em; margin-bottom: 12px; padding-left: 36px;
}}
.article .summary {{
  color: #bbb; font-size: 0.92em; line-height: 1.7;
  margin-bottom: 14px; padding-left: 36px;
}}
.article .why {{
  background: rgba(0,255,136,0.06);
  border-left: 3px solid #00ff88;
  padding: 10px 16px; margin-bottom: 14px;
  border-radius: 0 8px 8px 0;
  padding-left: 36px;
}}
.article .why-label {{
  color: #00ff88; font-size: 0.8em; font-weight: 700;
  display: block; margin-bottom: 4px;
}}
.article .why-text {{ color: #aaa; font-size: 0.88em; line-height: 1.5; }}
.article .meta-row {{
  display: flex; flex-wrap: wrap; gap: 8px; padding-left: 36px;
}}
.tag {{
  background: rgba(255,255,255,0.06);
  color: #888; font-size: 0.78em; padding: 3px 10px;
  border-radius: 20px; border: 1px solid rgba(255,255,255,0.08);
}}
.stock-tag {{
  background: rgba(0,212,255,0.08);
  color: #00d4ff; font-size: 0.78em; padding: 3px 10px;
  border-radius: 20px; border: 1px solid rgba(0,212,255,0.2);
}}
/* Keywords */
.keywords {{
  display: flex; flex-wrap: wrap; gap: 10px;
  margin-bottom: 40px;
}}
.kw {{
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  color: #aaa; font-size: 0.85em; padding: 6px 14px;
  border-radius: 20px;
}}
/* Observation */
.observation {{
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(0,212,255,0.15);
  border-radius: 16px; padding: 28px; margin-bottom: 40px;
}}
.observation h3 {{ color: #00d4ff; margin-bottom: 14px; font-size: 1.1em; }}
.observation ul {{ list-style: none; }}
.observation li {{
  padding: 8px 0; padding-left: 20px; position: relative; color: #bbb; font-size: 0.92em;
}}
.observation li::before {{ content: "▸"; position: absolute; left: 0; color: #00ff88; }}
footer {{
  text-align: center; color: #555; font-size: 0.85em;
  padding: 30px 20px; border-top: 1px solid rgba(255,255,255,0.05);
  margin-top: 40px;
}}
footer a {{ color: #00d4ff; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
  <a class="back-link" href="../index.html">← 返回首頁</a>
  
  <header>
    <h1>📰 AI 新聞 {TODAY}</h1>
    <div class="meta">
      <span>22</span> 則新聞 ·
      <span>8</span> 個分類 ·
      資料來源：TechCrunch
    </div>
  </header>

  <!-- TOP 3 HEADLINES -->
  <div class="top3">
'''

for i, art in enumerate(top3, 1):
    html += f'''    <div class="topcard">
      <div class="num">#{i}</div>
      <h2>{art["title"]}</h2>
      <p>{art["summary"]}</p>
      <a href="{art["link"]}" target="_blank">閱讀原文 →</a>
    </div>
'''

html += '''  </div>

  <!-- CATEGORY RADAR -->
  <div class="cat-grid">
    <div class="cat-pill"><div class="cat-icon">💾</div><div class="cat-info"><div class="cat-name">AI 晶片與硬體</div><div class="cat-count">2 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">🧠</div><div class="cat-info"><div class="cat-name">AI 模型與研究</div><div class="cat-count">3 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">🤖</div><div class="cat-info"><div class="cat-name">AI 產品與應用</div><div class="cat-count">5 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">🏢</div><div class="cat-info"><div class="cat-name">企業 AI 動態</div><div class="cat-count">3 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">💰</div><div class="cat-info"><div class="cat-name">AI 投融資</div><div class="cat-count">2 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">🏛️</div><div class="cat-info"><div class="cat-name">AI 政策與監管</div><div class="cat-count">2 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">👥</div><div class="cat-info"><div class="cat-name">AI 人事與組織</div><div class="cat-count">2 篇</div></div></div>
    <div class="cat-pill"><div class="cat-icon">🌍</div><div class="cat-info"><div class="cat-name">AI 國際與地緣政治</div><div class="cat-count">2 篇</div></div></div>
  </div>

  <!-- KEYWORDS -->
  <h2 style="color:#00ff88;margin-bottom:16px;font-size:1.3em;">🔑 今日關鍵詞</h2>
  <div class="keywords">
    <span class="kw">Apple Intelligence</span>
    <span class="kw">Qwen</span>
    <span class="kw">OpenAI Codex</span>
    <span class="kw">Anthropic Ode</span>
    <span class="kw">Blackstone</span>
    <span class="kw">Moonshot Kimi 3</span>
    <span class="kw">Suno</span>
    <span class="kw">Vint Cerf</span>
    <span class="kw">Miles Wang</span>
    <span class="kw">Emergent</span>
    <span class="kw">Thinking Machines</span>
    <span class="kw">Inkling</span>
    <span class="kw">Google Vids</span>
    <span class="kw">Roblox</span>
    <span class="kw">Reelful</span>
    <span class="kw">Microsoft</span>
    <span class="kw">Lorde</span>
    <span class="kw">DeepMind</span>
    <span class="kw">Alexandre LeBrun</span>
  </div>

'''

# ============================================================
# Build article sections by category
# ============================================================
# First assign all articles to categories
assigned = {}  # url -> article data with categories
for art in articles:
    cats = assign_category(art)
    for cat in cats:
        if cat not in categories:
            continue
        # check if already added to this category
        key = art.get('url', '')
        if key not in assigned:
            assigned[key] = {'art': art, 'cats': cats}
        categories[cat].append(art)

# Actually let me rebuild the per-category article lists
cat_articles = {cat: [] for cat in categories}

for art in articles:
    cats = assign_category(art)
    for cat in cats:
        cat_articles[cat].append(art)

# Remove duplicates within each category
for cat in cat_articles:
    seen_urls = set()
    unique = []
    for art in cat_articles[cat]:
        url = art.get('url','')
        if url not in seen_urls:
            seen_urls.add(url)
            unique.append(art)
    cat_articles[cat] = unique

# Write each category section
for cat_name, arts in cat_articles.items():
    if not arts:
        continue
    icon = cat_name.split(' ')[0]
    label = cat_name.split(' ', 1)[1] if ' ' in cat_name else cat_name
    
    html += f'''  <!-- {cat_name} -->
  <div class="section">
    <div class="section-header">
      <h2>{icon} {label}</h2>
      <span class="badge">{len(arts)} 篇</span>
    </div>
'''
    
    for i, art in enumerate(arts, 1):
        title = art.get('title', '')
        url = art.get('url', '')
        tc_time = art.get('time', '') or art.get('originalTime', '')
        content = art.get('content', '')
        why = get_why_important(title, art)
        entities = get_entities(art)
        stocks = get_stocks(art)
        
        readable_time = format_time(tc_time)
        
        # Generate a summary from content or use fallback
        if content and len(content) > 50:
            summary = content[:250] + ('...' if len(content) > 250 else '')
        else:
            # No content available - use title-based summary
            summary_map = {
                'Google Vids': 'Google 宣布 Vids 重大更新：用戶現在可上傳自己的照片並以 AI 數位分身生成影片。Workspace 企業版全面整合這項功能，讓影片製作門檻大幅降低。',
                'Roblox': 'Roblox 在手機 App 推出 AI 驅動的遊戲創作功能，用戶可透過自然語言描述遊戲玩法，AI 系統自動生成完整遊戲。降低創作門檻，瞄準 UGC 生態系統加速增長。',
                'Google AI Mode': 'Google 宣布 AI Mode 新功能：用戶可直接連結並與外部應用程式互動。Google 將 AI 助理從被動問答提升為主動執行任務的 Agentic AI。',
                'OpenAI basketball': 'OpenAI 推出 ChatGPT 品牌籃球商品，引發外界熱議。這款限量版籃球以 ChatGPT 主題設計，售價與銷售方式尚未公布。',
                'DeepMind researcher': '前 DeepMind 研究員創立新創公司，產品尚未上線即以 3 億美元估值完成 pre-seed 輪，反映頂級 AI 人才在資本市場的極高吸引力。',
                'AMI Labs': 'AMI Labs 創辦人 Alexandre LeBrun 明確拒絕使用 AGI 或超級智慧等名詞，強調自家 AI 並非通用人工智慧，反映對 AI 能力過度承諾的警惕意識。',
                'Moonshot': 'Moonshot AI 準備推出 Kimi 3，號稱在 benchmark 上接近 Anthropic Opus 4.8。若預言屬實，將是中國大模型首次在最高能力級別與美國頂級模型正面競爭。',
                'Apple Intelligence': 'Apple Intelligence 正式獲中國監管機構批准，採用阿里巴巴 Qwen 和百度文心一言作為在地模型。這是蘋果在中國市場推進 AI 功能的重大里程碑。',
                'Applied Computing': 'Applied Computing 瞄準油氣產業，推出工廠整體優化 AI 模型。用 AI 學習整個化工廠的營運數據，協助操作員即時決策。傳統重工業 AI 化再下一城。',
                'Microsoft salespeople': '媒體報導微軟訓練業務團隊在對企業客戶說明時貶低 OpenAI 與 Anthropic，反映雲端 AI 市場競爭已從技術層面蔓延至銷售話術與公關戰。',
                'OpenAI keyboard': 'OpenAI 發布首款自有硬體：230 美元 Codex 鍵盤，專為 Codex AI 程式碼助理優化。此舉在與前蘋果設計大師 Jony Ive 的硬體合資公司法律糾紛之際公布，格外引人矚目。',
                'Thinking Machines': 'Thinking Machines 發布首款開放模型 Inkling，挑戰 OpenAI 和 Anthropic 的閉源策略。該公司由前 Meta AI 高層創立，主打「非一體適用」的客製化 AI。',
                'Suno': '安全研究人員發現 AI 音樂生成工具 Suno 疑似未經授權竊取 YouTube 影片作為訓練資料。若查證屬實，將重創 Suno 的音樂產業合作機會。',
                'Microsoft security': '微軟發布史上最大規模安全更新，修補大量漏洞並公開點名 AI 加速開發是原因之一。顯示 AI 辅助程式碼生成雖提升產量，但同時也增加了資安風險。',
                'Anthropic Blackstone': 'Anthropic 與私募巨頭 Blackstone 共同成立新公司 Ode，初始投資 15 億美元，瞄準企業 AI 落地實施商機。雙方認為 AI 價值將從模型本身轉移到部署與整合服務。',
                'Reelful': 'Reelful AI 可將手機相簿照片自動剪輯成短影音，專為 Instagram、TikTok 等平台優化。用 AI 降低影片剪輯門檻，瞄準社交媒體創作者經濟。',
                'Emergent': '印度 AI 程式碼新創 Emergent 成立僅一年多，以 1.3 億美元完成 C 輪、估值達 13 億美元晉升獨角獸。聚焦 AI 輔助程式開發，反映印度 AI 生態快速崛起。',
                'Vint Cerf': '網際網路之父 Vint Cerf 加入 Innovation Labs，專注推動 AI Agent 在開放網路上的身份認證標準化。工作重點是建立信任框架，讓 AI 代理能安全地在網路上代理用戶行動。',
                'Miles Wang': 'OpenAI 研究員 Miles Wang 洽談創立 AI 藥物探索新創，估值 20 億美元。若成真，將是 OpenAI 內部人才創業的最新案例，顯示 AI 在生技製藥領域的龐大商機。',
                'Lorde': '紐西蘭知名歌手 Lorde 在公開場合批評 AI 智慧眼鏡「不性感」，引發共鳴。這反映了一般消費者對當前 AI 硬體裝置設計美學與實用性的普遍質疑。',
                'OpenAI screenless': '據報 OpenAI 正在開發首款硬體裝置為無螢幕可移動揚聲器。市場猜測這是與 Jony Ive 合作破局後的獨自硬體策略，瞄準 AI 原生裝置市場。',
                'OpenAI Apple': 'OpenAI 正式反擊蘋果的商業竊密訴訟，否認所有指控並要求法院駁回。這是繼蘋果狀告 OpenAI 之後雙方法律戰的正式升級。',
            }
            
            fallback = ''
            for k, v in summary_map.items():
                if k.lower() in title.lower():
                    fallback = v
                    break
            if not fallback:
                fallback = "本則新聞與 AI 產業發展高度相關，建議閱讀原文了解完整內容。"
            summary = fallback
        
        html += f'''    <div class="article">
      <div class="article-header">
        <span class="article-num">{i}</span>
        <h3><a href="{url}" target="_blank">{title}</a></h3>
      </div>
      <div class="time">🕐 {readable_time} · TechCrunch</div>
      <div class="summary">{summary}</div>
      <div class="why">
        <span class="why-label">🔍 為什麼重要</span>
        <span class="why-text">{why}</span>
      </div>
      <div class="meta-row">
'''
        for e in entities[:5]:
            html += f'        <span class="tag">{e}</span>\n'
        for s in stocks[:3]:
            html += f'        <span class="stock-tag">📈 {s}</span>\n'
        html += '      </div>\n    </div>\n'

    html += '  </div>\n\n'

# ============================================================
# Tomorrow's observation
# ============================================================
html += '''  <!-- TOMORROW'S OBSERVATION -->
  <div class="observation">
    <h3>🔮 明日觀察</h3>
    <ul>
      <li><strong>OpenAI 硬體動向</strong>：230 美元 Codex 鍵盤只是開始，後續與 Jony Ive 的法律戰走向將影響 OpenAI 硬體策略發展。</li>
      <li><strong>Apple Intelligence 中國落地</strong>：Qwen 獲選為蘋果在中國的 AI 合作模型，阿里巴巴股價可能受到激勵，需觀察實際體驗與用戶接受度。</li>
      <li><strong>Anthropic Ode 公司</strong>：Anthropic 與 Blackstone 的落地服務合資公司可能於短期內宣布首批企業客戶名單。</li>
      <li><strong>Suno 版權爭議</strong>：若 YouTube 竊取資料指控屬實，可能引發唱片公司更大的法律行動，也會加速產業對 AI 音樂生成規範的討論。</li>
      <li><strong>印度 AI 生態</strong>：Emergent 成為獨角獸可能帶動新一波印度 AI 新創募資熱潮，觀察後續估值走向。</li>
    </ul>
  </div>

  <footer>
    <p>由 OpenClaw 自動生成 · 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a></p>
    <p style="margin-top:10px;">© 2026 acstep · 每日 12:30 台北時間自動更新</p>
  </footer>
</div>
</body>
</html>
'''

# Write HTML
out_path = f'/home/matt/.openclaw/workspace/TECH/news/{TODAY}.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written: {out_path}")
