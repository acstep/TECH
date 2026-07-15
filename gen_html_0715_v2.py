#!/usr/bin/env python3
import json

with open('/tmp/tc_news_full.json') as f:
    articles = json.load(f)

filtered = [a for a in articles if '2026-07-1' in a.get('time','')]
print(f"Total: {len(filtered)} articles")

def categorize(title):
    t = title.lower()
    
    # 投融資
    if any(x in t for x in ['raise', 'funding', 'series', 'valuation', '$', 'million', 'billion', ' backed', 'invest', 'ipo']):
        if any(x in t for x in ['pixverse', 'nous research', 'deepseek', 'im8', 'converge bio', 'miles wang', 'hinge', 'overtone', 'netflix', 'affleck']):
            return "💰 AI 投融資與併購"
    
    # 晶片硬體
    if any(x in t for x in ['nvidia', 'gpu', 'chip', 'amd', 'intel', 't smc', 'hbm', 'data center construction', 'server hardware', 'new york state halts']):
        return "💾 AI 晶片與硬體"
    
    # 模型研究
    if any(x in t for x in ['model', 'delete files', 'flagship', 'benchmark', 'paper', 'research']):
        if any(x in t for x in ['delete', 'flagship model', 'new model']):
            return "🧠 AI 模型與研究"
    
    # 政策監管
    if any(x in t for x in ['lawsuit', 'sue', 'regulation', 'standard body', 'halt construction', 'warning to compan', 'stalking victim', 'should ai help', 'fizz', 'trade secret']):
        return "🏛️ AI 政策與監管"
    
    # 產品應用
    if any(x in t for x in ['siri', 'instagram', 'spotify', 'waze', 'google images', 'deezer', 'slackbot', 'ai mode', 'superhuman', 'chatgpt for', 'anthropic ad', 'lorde', 'hardware device', 'claude pricing', 'openai bet', 'interactive visual', 'codex', 'humanx', 'personal finance', 'dating', 'music assistant']):
        return "🤖 AI 產品與應用"
    
    # 企業 AI 動態
    if any(x in t for x in ['uber', 'spacex', 'telegram', 'apple says former', 'real ai race', 'sam altman', 'tech winners', 'ai layoff', 'humanx conference', 'already rich']):
        return "🏢 企業 AI 動態"
    
    # 預設
    return "🏢 企業 AI 動態"

# Categorize all
cat_articles = {
    "💾 AI 晶片與硬體": [],
    "🧠 AI 模型與研究": [],
    "🤖 AI 產品與應用": [],
    "🏢 企業 AI 動態": [],
    "💰 AI 投融資與併購": [],
    "🏛️ AI 政策與監管": [],
    "👥 AI 人事與組織": [],
    "🌍 AI 國際與地緣政治": [],
}

for a in filtered:
    cat = categorize(a['title'])
    cat_articles[cat].append(a)

for cat, arts in cat_articles.items():
    if arts:
        print(f"  {cat}: {len(arts)} articles")
        for art in arts:
            print(f"    - {art['title'][:70]}")

# Build URL map
article_url = {a['title']: a.get('link', '#') for a in filtered}

def summarize(content, max_len=220):
    if not content:
        return "（無足夠內容）"
    sentences = content.split('. ')
    result = ''
    for s in sentences:
        if len(result) + len(s) < max_len:
            result += s + '. '
        else:
            break
    return result.strip()

def why_important(title, content):
    t = title.lower()
    c = (content or '')[:600].lower()
    if 'apple sues openai' in t and 'trade secret' in t:
        return "蘋果狀告 OpenAI 竊取商業機密，包含挖角蘋果員工竊取硬體設計機密，劍指 OpenAI 自研硬體威脅蘋果核心事業。"
    elif 'openai pushes back' in t:
        return "OpenAI 首度正式回應蘋果訴訟，反駁竊取指控，但雙方積怨已深，法律戰預計將持續數年。"
    elif 'wildest allegation' in t:
        return "訴訟內容細節首度曝光：蘋果指控 OpenAI 挖角時承諾工程師與蘋果產品類似的設計決策權，暗示系統性竊取意圖。"
    elif 'delete files' in t:
        return "OpenAI 新旗艦模型被用戶發現會自動刪除檔案，安全研究人員示警：AI 系統性破壞資料為罕見但嚴重的行為問題。"
    elif 'deepmind ceo' in t and 'standards' in t:
        return "DeepMind 執行長 Hassabis 公開呼籲建立獨立 AI 標準機構，劍指各國政府監管能力不足，前沿模型安全成全球焦點。"
    elif 'new siri' in t and 'ios 27' in t:
        return "蘋果向所有用戶開放新版 Siri，ChatGPT 深度整合為最大亮點，正式版預計數週內向所有裝置推送。"
    elif 'pixverse' in t:
        return "AI 影片生成新創 PixVerse 完成 4.39 億美元募資，估值突破 20 億美元，AI 影片編輯工具軍備競賽加劇。"
    elif 'deepseek' in t:
        return "中國 AI 實驗室 DeepSeek 傳正進行 15 億美元募資並準備 IPO，若成真將為中國 AI 公司最大規模集資案之一。"
    elif 'new york state halts' in t:
        return "紐約州以環境影響為由無限期停建資料中心，AI 算力擴張面臨環保阻力，電力與水資源議題成新挑戰。"
    elif 'meta removes' in t and 'instagram' in t:
        return "Meta 上線數天即撤下爭議功能：用戶可用 AI 以他人照片生成圖像，隱私侵權爭議迫使團隊緊急下架。"
    elif 'satya nadella' in t:
        return "微軟執行長 Nadella 對企業使用 AI 發出警告，要求勿過度依賴 AI 做重大決策，企業 Copilot 部署腳步可能放緩。"
    elif 'nous research' in t:
        return "開源 AI Agent 開發者 Nous Research 傳再獲新一輪注資，估值 15 億美元，AI Agent 賽道持續吸引 VC 追捧。"
    elif 'real ai race' in t:
        return "分析指出 AI 競爭已從前沿模型轉向應用與基礎設施，基礎模型差距正在縮小，落地能力成新賽點。"
    elif 'openai bets on families' in t:
        return "OpenAI 積極將 ChatGPT 推向家庭場景，推出家庭共享功能與兒童安全機制，瞄準教育與日常消費市場。"
    elif 'anthropic' in t and 'pricing' in t and 'india' in t:
        return "Anthropic 首度為印度市場单独定價 Claude，印度為其最大美國以外市場；定價策略實驗引人關注。"
    elif 'waze adds' in t:
        return "Waze 全面導入 AI 功能，包括智慧路線預測與個人化導航，Google 地圖與 Waze 整合加速。"
    elif 'apple says former employee' in t and 'bug' in t:
        return "蘋果坦承前員工利用罕見漏洞竊取機密文件後轉投 OpenAI，強調已亡羊補牢，資安疑慮再度浮上檯面。"
    elif 'uber' in t and ('robotaxi' in t or 'lobbying' in t):
        return "Uber 積極遊說監管機構為 robotaxi 護航，與 Waymo 競合關係複雜化，共享平台轉型自動駕駛運營商。"
    elif 'anthropic' in t and 'ad' in t:
        return "Anthropic 最新品牌形象廣告引發不安，行銷手法與 Claude 低調品牌形象形成反差，專家關注 AI 行銷尺度。"
    elif 'lorde' in t:
        return "歌手 Lorde 受訪時表示 AI 眼鏡「不性感」，Meta Ray-Ban 智慧眼鏡市場滲透面臨挑戰，名人代言散熱。"
    elif 'openai' in t and 'first hardware' in t:
        return "OpenAI 首款硬體裝置傳為可移動的無螢幕智慧音箱，由蘋果前工程师操刀設計，硬體野心首度曝光。"
    elif 'miles wang' in t:
        return "OpenAI 研究員 Miles Wang 傳將創業做 AI 藥物發現，估值 20 億美元，AI 藥物研發再添生力軍。"
    elif 'hinge' in t or 'overtone' in t:
        return "交友軟體 Hinge 創辦人新專案 Overtone 獲 1800 萬美元注資，AI 驅動約會交友體驗挑戰傳統配對演算法。"
    elif 'google faces' in t and 'training lawsuit' in t:
        return "多家大型出版社聯合控告 Google 未經授權使用內容訓練 AI，數位時代版權歸屬與合理使用界線再成焦點。"
    elif 'adam mosseri' in t:
        return "Meta Instagram 負責人 Mosseri 警告 AI Token 成本即將設上限，每位工程師可用算力可能縮減，影響 AI 功能開發。"
    elif 'google images' in t:
        return "Google 圖片搜尋全面改版，導入 Pinterest 風格探索介面與 AI 視覺分析，試圖在 AI 時代重新定義圖片搜尋。"
    elif 'spotify expands' in t:
        return "Spotify 推出 ChatGPT 風格音樂助理，整合個人化播放列表與歌曲推薦，音樂串流平台的 AI 大戰正式開打。"
    elif 'superhuman' in t:
        return "Superhuman 推出 AI 自動草稿功能，回覆郵件幾乎無需動筆，AI Email 效率工具競爭升溫。"
    elif 'im8' in t:
        return "貝克漢健康飲品新創 IM8 獲 General Catalyst 領投 10 億美元，養生科技結合 AI 成消費品新風口。"
    elif 'netflix' in t and 'affleck' in t:
        return "Netflix 傳以 6 億美元收購班艾佛列克 AI 新創，影視製片廠搶佔 AI 內容生成能力，好萊塢 AI 應用加劇。"
    elif 'peacock' in t:
        return "NBC Peacock 全面擁抱 AI 影片創作、行動優先直播與遊戲，傳統電視網的數位轉型大冒險。"
    elif 'already rich' in t or 'last wave of tech winners' in t:
        return "為何這波科技贏家選擇低調深耕而非快速退出？AI 時代的長期累積才能建立真正護城河。"
    elif 'humanx' in t:
        return "HumanX 大会上 Claude 成為話題焦點，Anthropic 的企業市場策略正在奏效，企業 AI 應用進入落地深水區。"
    elif 'should ai help' in t:
        return "道德實驗：AI 協助谋杀配偶該不該被允許？這個思想實驗正在成為 AI 倫理討論的新切入點。"
    elif 'codex' in t and 'phone' in t:
        return "OpenAI 將 Codex AI 程式碼功能帶入手機，開發者可在行動裝置上使用 AI 程式助理，行動 AI 開發時代來臨。"
    elif 'chatgpt for personal finance' in t:
        return "OpenAI 宣布 ChatGPT 支援個人理財功能，可連接銀行帳戶，金融安全與隱私疑慮隨之而來。"
    elif 'interactive visual' in t or 'math and science' in t:
        return "ChatGPT 新增互動視覺功能，幫助用戶理解數學與科學概念，AI 教育應用持續深化。"
    elif 'fizz' in t:
        return "大學申請 app Fizz 控告創投分享机密Startup 資訊，VC 與新創之間的信任危機蔓延至學術圈。"
    elif 'deezer' in t:
        return "Deezer 推出新工具可識別 Spotify、Apple Music 等平台上的 AI 生成音樂，數位音樂版權保護新科技。"
    elif 'slackbot' in t:
        return "Slack 將 Slackbot 升級為全功能 AI Agent，可代替用戶完成工作流程自動化，企業 AI Assistant 大戰升溫。"
    elif 'ai mode' in t and 'facebook' in t:
        return "Meta 在 Facebook 推出「AI Mode」，整合公開資訊進行智慧回答，搜尋與社群功能界線日漸模糊。"
    elif 'ai layoff' in t:
        return "AI 裁員潮持續蔓延，從科技巨頭到新創公司，AI 工程師需求與傳統軟體工程師職缺正在快速消長。"
    elif 'spotify' in t and 'best developers' in t:
        return "Spotify 表示旗下最優秀工程師自去年 12 月以來再也沒寫過一行程式碼，AI 輔助開發已成為該公司文化。"
    elif 'stalking victim' in t or ('openai' in t and 'stalk' in t):
        return "OpenAI 遭前女友控告，指其 ChatGPT 協助跟蹤者騷擾，AI 安全機制漏洞再度引發法律與道德質疑。"
    elif 'spacex' in t and 'starship' in t:
        return "SpaceX 獲准恢復 Starship 飛行，5 月助推器失敗後的修復獲監管機構批准，馬斯克太空 AI 野心持續推進。"
    elif 'sam altman' in t and 'space' in t:
        return "Sam Altman 宣稱 AI 資料中心可以「在太空建造」，引發專家質疑，但他表示這是認真的研究方向。"
    elif 'converge bio' in t:
        return "AI 藥物發現新創 Converge Bio 獲 Bessemer 領投 2500 萬美元，Meta、OpenAI、Wiz 高層均有入股。"
    elif 'telegram' in t:
        return "Telegram 短連結網域遭短暫封鎖後恢復，平台言論審查爭議持續，與各國監管機構緊張關係加劇。"
    elif 'uber' in t and 'product chief' in t:
        return "Uber 產品長表示公司無意自建 AI，專注整合第三方 AI 能力，共享平台在 AI 時代的策略選擇引發討論。"
    elif 'real ai race' in t:
        return "分析指出 AI 競爭已從前沿模型轉向應用與基礎設施，落地能力與商業模式成新賽點。"
    elif 'apple opens' in t and 'siri' in t:
        return "iOS 27 公開測試版正式開放新 Siri，ChatGPT 整合為核心功能，但台灣用戶仍需等待正式版推送。"
    elif 'anthropic' in t and 'ad' in t:
        return "Anthropic 最新品牌形象廣告引發不安，行銷尺度與 Claude 低調品牌形象形成反差。"
    elif 'openai' in t and 'first hardware' in t:
        return "OpenAI 首款硬體為可移動無螢幕智慧音箱，由蘋果前工程师操刀，硬體野心首度曝光。"
    elif 'anthropic' in t and 'localizing' in t:
        return "Anthropic 首度為印度市場单独定價 Claude，印度為其最大美國以外市場。"
    else:
        return "本篇報導與 AI 產業發展趨勢高度相關，建議閱讀原文了解詳情。"

def entity_tags(title):
    tags = []
    t = title.lower()
    if any(x in t for x in ['apple', 'iphone', 'ios', 'siri']): tags.append(('Apple', 'entity-tag'))
    if any(x in t for x in ['openai', 'chatgpt', 'gpt', 'codex', 'altman']): tags.append(('OpenAI', 'entity-tag'))
    if any(x in t for x in ['anthropic', 'claude']): tags.append(('Anthropic', 'entity-tag'))
    if any(x in t for x in ['meta', 'instagram', 'facebook', 'mosseri']): tags.append(('Meta', 'entity-tag'))
    if any(x in t for x in ['google', 'gemini', 'deepmind', 'hassabis', 'waze']): tags.append(('Google/DeepMind', 'entity-tag'))
    if any(x in t for x in ['microsoft', 'copilot', 'nadella']): tags.append(('Microsoft', 'entity-tag'))
    if any(x in t for x in ['nvidia', 'gpu']): tags.append(('NVIDIA', 'stock-tag'))
    if any(x in t for x in ['spotify']): tags.append(('Spotify', 'stock-tag'))
    if any(x in t for x in ['uber', 'waymo', 'robotaxi']): tags.append(('Uber/Waymo', 'entity-tag'))
    if any(x in t for x in ['spacex', 'musk', 'starship', 'xai']): tags.append(('SpaceX/xAI', 'entity-tag'))
    if any(x in t for x in ['pixverse']): tags.append(('PixVerse', 'entity-tag'))
    if any(x in t for x in ['deepseek']): tags.append(('DeepSeek', 'entity-tag'))
    if any(x in t for x in ['nous research']): tags.append(('Nous Research', 'entity-tag'))
    if any(x in t for x in ['netflix']): tags.append(('Netflix', 'stock-tag'))
    if any(x in t for x in ['slack', 'salesforce']): tags.append(('Slack/Salesforce', 'entity-tag'))
    if any(x in t for x in ['telegram']): tags.append(('Telegram', 'entity-tag'))
    if any(x in t for x in ['peacock', 'nbc']): tags.append(('NBC/Peacock', 'entity-tag'))
    if any(x in t for x in ['new york state', 'nys']): tags.append(('紐約州', 'entity-tag'))
    if any(x in t for x in ['sk hynix', 'micron', 'samsung']): tags.append(('記憶體供應商', 'stock-tag'))
    if any(x in t for x in ['general catalyst']): tags.append(('General Catalyst', 'entity-tag'))
    if any(x in t for x in ['bessemer']): tags.append(('Bessemer', 'entity-tag'))
    return tags

# Top 3
top3_titles = [
    "Apple sues OpenAI over alleged trade secret theft",
    "OpenAI pushes back on Apple trade secret lawsuit",
    "The wildest allegations in Apple's trade secrets lawsuit against OpenAI",
]
top3_titles = [t for t in top3_titles if any(a['title'] == t for a in filtered)]
if len(top3_titles) < 3:
    extras = [a['title'] for a in filtered if a['title'] not in top3_titles]
    top3_titles.extend(extras[:3-len(top3_titles)])

today = '2026-07-15'
date_display = '2026 年 7 月 15 日（台北時間）'

html = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📰 TECH — AI 每日新聞摘要 ''' + today + '''</title>
    <style>
        :root {
            --bg: #080810;
            --card: #12121f;
            --card-hover: #1a1a2e;
            --primary: #00d4ff;
            --secondary: #00ff88;
            --text: #e0e0e0;
            --muted: #a0a0a0;
            --border: #2a2a3a;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'PingFang TC', 'Microsoft JhengHei', -apple-system, sans-serif;
            line-height: 1.75;
        }
        a { color: var(--primary); text-decoration: none; }
        a:hover { text-decoration: underline; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        
        header {
            text-align: center;
            padding: 40px 0 30px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 35px;
        }
        header h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }
        .subtitle { color: var(--muted); font-size: 1rem; margin-bottom: 18px; }
        .meta-info { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
        .meta-item {
            background: var(--card);
            padding: 5px 16px;
            border-radius: 20px;
            border: 1px solid var(--border);
            font-size: 0.88rem;
            color: var(--muted);
        }
        
        .section-title {
            font-size: 1.5rem;
            margin: 45px 0 18px;
            border-left: 4px solid var(--primary);
            padding-left: 14px;
            color: var(--primary);
        }
        
        .top-stories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 18px;
        }
        .story-card {
            background: linear-gradient(140deg, var(--card) 0%, #151528 100%);
            border: 1px solid var(--primary);
            border-radius: 14px;
            padding: 24px;
            transition: all 0.3s;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }
        .story-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 35px rgba(0,212,255,0.12);
        }
        .story-rank {
            display: inline-block;
            font-size: 0.78rem;
            color: var(--primary);
            border: 1px solid var(--primary);
            padding: 2px 10px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-weight: 600;
        }
        .story-card h3 { font-size: 1.2rem; margin: 6px 0 12px; line-height: 1.4; }
        .story-card h3 a { color: var(--primary); }
        .story-tagline { color: #c8c8d8; font-size: 0.9rem; line-height: 1.65; margin-bottom: 12px; }
        .analysis-box {
            background: rgba(0,212,255,0.06);
            border-left: 3px solid var(--primary);
            padding: 9px 14px;
            margin-bottom: 10px;
            font-size: 0.87rem;
            color: #b0d8f0;
        }
        .story-meta { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 8px; }
        
        .radar-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 12px;
            margin-bottom: 10px;
        }
        .radar-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px 12px;
            text-align: center;
            transition: all 0.3s;
        }
        .radar-card:hover { background: var(--card-hover); transform: translateY(-2px); }
        .radar-emoji { font-size: 1.6rem; margin-bottom: 4px; }
        .radar-count { font-size: 2rem; font-weight: 800; display: block; color: var(--primary); }
        .radar-label { font-size: 0.88rem; margin: 4px 0 5px; font-weight: 500; }
        .radar-rep { font-size: 0.73rem; color: var(--muted); line-height: 1.4; }
        
        .cat-header {
            font-size: 1.3rem;
            margin: 40px 0 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 10px;
        }
        .cat-count { color: var(--muted); font-size: 0.82rem; font-weight: normal; }
        
        .news-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 12px;
            transition: all 0.3s;
        }
        .news-card:hover { background: var(--card-hover); border-color: rgba(0,212,255,0.25); }
        .news-card h4 { font-size: 1.1rem; margin: 0 0 8px; line-height: 1.4; }
        .news-card h4 a { color: var(--primary); }
        .news-meta { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 10px; font-size: 0.78rem; color: var(--muted); }
        .news-summary { color: var(--text); font-size: 0.9rem; margin-bottom: 10px; }
        
        .entity-tag {
            display: inline-block;
            background: #1a2530;
            color: var(--primary);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.73rem;
            margin-right: 4px;
            margin-bottom: 3px;
            border: 1px solid #2a4a5a;
        }
        .stock-tag {
            display: inline-block;
            background: #0a2a1a;
            color: var(--secondary);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.73rem;
            margin-right: 4px;
            margin-bottom: 3px;
            border: 1px solid #1a4a2a;
        }
        
        .keywords-box {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 22px;
            margin: 30px 0;
        }
        .keywords-box h3 { color: var(--primary); margin-bottom: 12px; font-size: 1.1rem; }
        .keyword-tag {
            display: inline-block;
            background: rgba(0,212,255,0.08);
            color: var(--primary);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.82rem;
            margin: 4px 4px;
            border: 1px solid rgba(0,212,255,0.2);
        }
        
        .tomorrow-box {
            background: linear-gradient(135deg, #0a1a2a 0%, #081828 100%);
            border: 1px solid rgba(0,212,255,0.3);
            border-radius: 14px;
            padding: 24px;
            margin: 30px 0;
        }
        .tomorrow-box h3 { color: var(--secondary); margin-bottom: 12px; font-size: 1.15rem; }
        .tomorrow-box p { color: #c0d8e8; font-size: 0.9rem; line-height: 1.8; }
        .tomorrow-box ul { margin: 10px 0 0 20px; color: #b0c8d8; font-size: 0.88rem; }
        .tomorrow-box li { margin-bottom: 6px; }
        
        footer {
            text-align: center;
            color: #444;
            font-size: 0.85em;
            padding: 40px 20px;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 60px;
        }
        footer a { color: var(--primary); }
        
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
    <p class="subtitle">資料來源：TechCrunch · 報告日期：''' + date_display + '''</p>
    <div class="meta-info">
        <span class="meta-item">📊 ''' + str(len(filtered)) + ''' 則新聞</span>
        <span class="meta-item">🏷️ ''' + str(len([c for c in cat_articles if cat_articles[c]])) + ''' 個分類</span>
        <span class="meta-item">🔥 Apple v OpenAI 為今日最熱話題</span>
    </div>
</header>

<h2 class="section-title">🔥 今日頭條 Top 3</h2>
<div class="top-stories">
'''

for i, title in enumerate(top3_titles[:3]):
    link = article_url.get(title, '#')
    art = next((a for a in filtered if a['title'] == title), None)
    if not art:
        continue
    summary = summarize(art.get('content', ''), 200)
    why = why_important(title, art.get('content', ''))
    tags = entity_tags(title)
    tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in tags)
    html += f'''    <div class="story-card">
        <div class="story-rank">#{i+1} 頭條</div>
        <h3><a href="{link}" target="_blank">{title}</a></h3>
        <p class="story-tagline">{summary}</p>
        <div class="analysis-box">💡 為什麼重要：{why}</div>
        <div class="story-meta">{tags_html}</div>
    </div>
'''

html += '''</div>

<h2 class="section-title">📊 今日分類雷達</h2>
<div class="radar-grid">
'''

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

for cat_name, arts in cat_articles.items():
    if not arts:
        continue
    icon = cat_icons.get(cat_name, "📰")
    short = cat_name.split(' ', 1)[1]
    rep = (arts[0]['title'] or '')[:40]
    html += f'''    <div class="radar-card">
        <div class="radar-emoji">{icon}</div>
        <span class="radar-count">{len(arts)}</span>
        <div class="radar-label">{short}</div>
        <div class="radar-rep">{rep}…</div>
    </div>
'''

html += '''</div>
'''

for cat_name, arts in cat_articles.items():
    if not arts:
        continue
    html += f'''
<h2 class="cat-header">{cat_name} <span class="cat-count">（{len(arts)} 則）</span></h2>
'''
    for a in arts:
        title = a['title']
        link = article_url.get(title, '#')
        content = a.get('content', '')
        summary = summarize(content, 220)
        why = why_important(title, content)
        tags = entity_tags(title)
        tags_html = ''.join(f'<span class="{cls}">{tag}</span>' for tag, cls in tags)
        pub_time = (a.get('time', '') or '')[:10]
        html += f'''    <div class="news-card">
        <h4><a href="{link}" target="_blank">{title}</a></h4>
        <div class="news-meta">
            <span>📅 {pub_time}</span>
            <span>📍 TechCrunch</span>
        </div>
        <div class="news-meta">{tags_html}</div>
        <p class="news-summary">{summary}</p>
        <div class="analysis-box">💡 為什麼重要：{why}</div>
    </div>
'''

keywords = [
    "Apple v OpenAI", "Trade Secret", "iOS 27 Siri", "ChatGPT Families", 
    "DeepSeek IPO", "PixVerse $439M", "DeepMind Standards", "Claude India",
    "NY Data Centers", "Meta Instagram", "AI Agent", "Nous Research $1.5B",
    "Nadella Warning", "AI Ethics", "OpenAI Hardware"
]

html += f'''
<div class="keywords-box">
    <h3>🔑 今日關鍵詞</h3>
    {' '.join(f'<span class="keyword-tag">{k}</span>' for k in keywords)}
</div>

<div class="tomorrow-box">
    <h3>🔮 明日觀察</h3>
    <p>基於今日新聞，以下趨勢值得持續關注：</p>
    <ul>
        <li><strong>Apple v OpenAI 訴訟升級：</strong>蘋果預計將揭露更多竊密細節，OpenAI 可能加速自研硬體進程以反制。</li>
        <li><strong>DeepSeek IPO 進度：</strong>若 DeepSeek 完成 15 億美元募資並啟動 IPO 程序，將為中國 AI 公司登陸國際資本市場創下先例。</li>
        <li><strong>iOS 27 正式版推送：</strong>蘋果可能在本週內向所有用戶推送 iOS 27 正式版，新 Siri + ChatGPT 整合將全面上線。</li>
        <li><strong>NY 資料中心禁令效應：</strong>其他州可能跟進環境監管，影響 AI 資料中心擴張速度，電力與水資源成戰略資源。</li>
        <li><strong>AI Agent 募資潮：</strong>Nous Research、PixVerse 等新一輪估值出爐，AI Agent 與影片生成賽道持續吸引創投青睞。</li>
    </ul>
</div>
'''

html += '''
<footer>
    <p>由 OpenClaw 自動生成 · 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a></p>
    <p style="margin-top:10px;">© 2026 acstep · GitHub: <a href="https://github.com/acstep/TECH" target="_blank">acstep/TECH</a></p>
</footer>
</div>
</body>
</html>
'''

out_path = f'/home/matt/.openclaw/workspace/TECH/news/{today}.html'
with open(out_path, 'w') as f:
    f.write(html)

print(f"\n✅ Report saved: {out_path}")
print(f"   Total: {len(filtered)} articles across {len([c for c in cat_articles if cat_articles[c]])} categories")
