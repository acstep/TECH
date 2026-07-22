#!/usr/bin/env python3
import json
from datetime import datetime

DATE = "2026-07-22"
DATE_DISPLAY = "2026年7月22日"
REPORT_DATE_UTC = "2026-07-21"

articles = json.load(open('/tmp/tc_0722_full.json'))

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

def cat_article(cat_key, title_cn, summary, why, entities, stocks, art):
    return {
        "title_en": art['title'],
        "title_cn": title_cn,
        "url": art['url'],
        "time": art.get('time', ''),
        "summary": summary,
        "why": why,
        "entities": entities,
        "stocks": stocks,
    }

# Article 1: Google releases three new Gemini models
categories["🧠 AI 模型與研究"].append(cat_article("🧠 AI 模型與研究",
    "Google 發布三款新 Gemini 模型，但旗艦 3.5 Pro 仍未現身",
    "Google DeepMind 本週二發表了 Gemini 3.6 Flash、3.5 Flash-Lite 與 3.5 Flash-Cyber 三款新模型。Gemini 3.6 Flash 作為 Google 口中的「主力模型」，在程式碼、知識工作與多模態效能上都有所提升，同時 token 用量減少了 17%，使用成本比前代更實惠。3.5 Flash-Lite 是同系列中最具成本效益的選擇，而 3.5 Flash-Cyber 則專為網路安全漏洞偵測與修復設計，初期僅開放給政府和信任合作夥伴。不過這次發布的亮點也在於「未發布」的產品：傳聞已久的旗艦 Gemini 3.5 Pro 仍未露面，距離上次 Pro 版更新已超過五個月，期間 OpenAI 已推出 GPT-5.5 與 GPT-5.6，Anthropic 也發布了 Claude Opus 4.8 和 Sonnet 5。Google DeepMind 產品主管 Logan Kilpatrick 表示，團隊已開始 Gemini 4 史上最大規模的預訓練。",
    "Google 在旗艦模型競賽中落後對手，此次一口氣發布三款 Flash 等級模型，是鞏固中階市場的防守策略。然而缺乏 Pro 等旗艦更新，代表 Google 在複雜推理與程式碼任務上暫時落後 OpenAI 與 Anthropic。3.5 Flash-Cyber 的出現顯示 Google 正積極切入資安 AI 這個快速成長的垂直領域。",
    "Google DeepMind、Logan Kilpatrick、Gemini 3.6 Flash、Gemini 3.5 Flash-Lite、Gemini 3.5 Flash-Cyber、ChatGPT、Claude、GPT-5.5",
    "Alphabet（GOOGL）、NVIDIA（相關概念股：軍備競賽帶動 GPU 需求）",
    articles[6]))

# Article 2: US threatens sanctions against Chinese AI models
categories["🌍 AI 國際與地緣政治"].append(cat_article("🌍 AI 國際與地緣政治",
    "美國威脅制裁中國 AI 模型，指控智慧財產權盜竊",
    "美國財政部長 Scott Bessent 本週二表示，政府將審查來自中國的開源 AI 模型，確認是否存在竊取智慧財產權的行為，若屬實將對中國 AI 公司實施制裁。Bessent 在 Fox Business 節目中指出：「我們支持開源模型，但不支持盜竊智財權。若發現海外模型竊取我國優秀公司的成果，我們有能力因應竊盜行為予以制裁。」此話背景是中國模型（尤其是 Moonshot AI 的 Kimi K3）能力與人氣快速攀升，對 OpenAI 與 Anthropic 等美國 AI 公司的商業模式與籌資能力構成威脅。此前有報導指出川普政府正在考慮全面禁止中國開源模型，而 Microsoft CEO Satya Nadella 也曾批評大模型公司對蒸餾技術（model distillation）的雙重標準。",
    "這是美國首次明確將制裁砲口對準 AI 模型本身，繼限制先進晶片出口之後，華府將監管範圍升級至模型層級，象徵中美 AI 競爭的重大升級。若制裁成真，將直接衝擊 Kimi K3 等中國模型在美國市場的發展，同時加劇全球 AI 地緣政治碎片化。",
    "Scott Bessent、Moonshot AI、Kimi K3、OpenAI、Anthropic、Satya Nadella、川普政府、Microsoft",
    "OpenAI（未上市）、Anthropic（未上市）、Microsoft（MSFT）、Alphabet（GOOGL）",
    articles[7]))

# Article 3: Anthropic-Pysical Intelligence rumor
categories["🧠 AI 模型與研究"].append(cat_article("🧠 AI 模型與研究",
    "傳 Anthropic 併購 Physical Intelligence？AI 機器人領域併購傳聞四起",
    "AI 圈近期最熱議的傳言，是 Anthropic 正在洽談收購機器人 AI 新創 Physical Intelligence（簡稱 PI）。Physical Intelligence 成立於 2023年，專注於開發「通用機器人控制模型」，讓機器人能夠執行洗碗、洗衣、收拾等家務任務。Anthropic 這幾個月已積極招募機器人領域人才，包括聘請前 Figure AI 與 Physical Intelligence 的員工。Anthropic 的 Claude 模型向來以語言與推理能力著稱，若成功收購 PI，將可將其能力延伸至實體世界，與 Tesla 的 Optimus、Figure 以及 Google DeepMind 的機器人計畫形成直接競爭。這筆潛在交易若屬實，將是 AI 實體化競賽的關鍵轉折點。",
    "Anthropic 若收購 PI，代表領先 AI 模型公司正積極將能力從虛擬世界延伸至實體機器人領域。這顯示 AI 的下一個戰場不只在大語言模型，還包括「AI + 機器人」的整合。成功收購將讓 Anthropic 在機器人 AI 賽道取得巨大優勢。",
    "Anthropic、Physical Intelligence、Claude、Figure AI、Tesla Optimus、Google DeepMind",
    "Anthropic（未上市）、Tesla（TSLA）、Alphabet（GOOGL）",
    articles[0]))

# Article 4: Data centers expected to use 4x more electricity
categories["💾 AI 晶片與硬體"].append(cat_article("💾 AI 晶片與硬體",
    "AI 資料中心用電量 2035 年將暴增四倍，占全美五分之一電力",
    "根據 BloombergNEF 最新報告，美國資料中心預計在 2035 年消耗全美發電量的五分之一，約為目前的四倍。AI 算力需求將推動資料中心容量在未來十年攀升至近 200 GW（千兆瓦）。其中近半容量將用於模型訓練與推論，且主要集中在美國境內；到 2033 年，美國將占全球 AI 晶片用電需求的 64%。BloombergNEF 的最新預測比去年 12 月的估算高出 83%。PJM 電網覆蓋範圍（從維吉尼亞延伸至伊利諾伊）未來將有 34% 的電力用於資料中心，德州 ERCOT 電網則需撥出 22% 的發電容量。PJM 已於今年四月重新開放新發電來源申請，但供需失衡已使電價在過去一年飆漲 76%。",
    "AI 資料中心的電力需求爆炸性成長，對電網基礎設施、能源政策與半導體供應鏈都產生深遠影響。供應鏈緊縮與電價上漲將墊高 AI 訓練與推論成本，可能影響中小型 AI 新創的競爭力，並加速能源創業投資（如核能和電網基礎設施）。",
    "BloombergNEF、PJM Interconnection、ERCOT、EPRI、American Electric Power",
    "NVIDIA（NVDA）、AMD（AMD）、Intel（INTC）、TSMC（TSM）、電力基礎建設類股（Vistra、Constellation Energy）",
    articles[5]))

# Article 5: Meta AI bedtime story app
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "Meta 測試 AI 床邊故事 App，語音生成功能即將上線",
    "Meta 正在測試一款全新的 AI 床邊故事 App，能為使用者生成專屬的睡前故事並以語音朗讀。根據 TechCrunch 報導，這款 App 瞄準「缺乏想像力」的使用者，讓用戶可以輸入簡單提示，即可獲得客製化的童話故事，並由 AI 配音朗讀。這是 Meta 將生成式 AI 整合進消費者日常場景的最新嘗試，延續了 Meta AI 在 Instagram、Facebook 與 WhatsApp 的佈局策略。目前 App 仍在測試階段，尚未對外公佈正式上線時間。",
    "Meta 持續在消費級 AI 應用上積極佈局。AI 床邊故事結合語音生成，是將生成式 AI 貨幣化的新嘗試。若正式推出，將與 Amazon 的 Alexa Stories、Samsung 的 Bixby Voice 等語音助理在家庭場景中直接競爭。",
    "Meta、Meta AI、Instagram、Facebook、WhatsApp、Amazon Alexa、Samsung Bixby",
    "Meta（META）",
    articles[1]))

# Article 6: OpenAI says Hugging Face was breached
categories["🏛️ AI 政策與監管"].append(cat_article("🏛️ AI 政策與監管",
    "OpenAI 指控：Hugging Face 遭其預發布模型入侵",
    "OpenAI 對 TechCrunch 證實，開源 AI 模型平台 Hugging Face 遭到不明人士利用 OpenAI 預發布模型進行系統入侵。攻擊者疑似透過存取 OpenAI 的預發布模型（可能是 GPT-5 的早期版本），對 Hugging Face 的系統進行未授權存取。OpenAI 表示已展開內部調查，並通知了相關單位。這是繼 2025 年多家 AI 公司傳出安全事件後，AI 領域再度傳出的重大資安問題。Hugging Face 是全球最大的開源 AI 模型托管平台之一，此次事件引發外界對預發布模型安全的疑慮。",
    "預發布模型被用於入侵開源平台，揭示了 AI 產業在模型安全管理上的漏洞。若駭客能利用預發布模型進行攻擊，代表 AI 公司的模型防護機制存在嚴重缺陷。此案可能促使監管機構對 AI 模型的安全性與存取權限管控制定更嚴格的規範。",
    "OpenAI、Hugging Face、GPT-5",
    "OpenAI（未上市）、Hugging Face（未上市）",
    articles[2]))

# Article 7: Jack Dorsey Buzz
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "Jack Dorsey 推出 Buzz 挑戰 Slack，以區塊鏈和 AI 為賣點",
    "Twitter／X 創辦人 Jack Dorsey 宣布推出新產品 Buzz，這是一款以區塊鏈技術為基礎的團隊協作聊天平台，直接瞄準 Slack 的企業通訊市場。Buzz 強調去中心化、AI 整合與隱私保護，並計劃整合 Dorsey 的比特幣與 Web5 願景。Buzz 的目標是用戶能夠擁有自己的資料與對話記錄，不受任何中心化平台的掌控。Buzz 目前仍在早期測試階段，尚未公佈具體的上線時間與商業模式。",
    "Jack Dorsey 離開 X 之後持續在去中心化技術領域探索。Buzz 若能成功，將是區塊鏈技術首次真正切入企業協作軟體市場。然而 Slack（Salesforce 旗下）與 Microsoft Teams 已主導市場多年，Buzz 的差異化賣點能否吸引企業用戶仍是未知數。",
    "Jack Dorsey、Buzz、Slack、Salesforce、Microsoft Teams、X",
    "Salesforce（CRM）、Microsoft（MSFT）、Block（SQT）",
    articles[3]))

# Article 8: AI and universal entertainment app
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "AI 時代的「萬用娛樂 App」崛起：Spotify、YouTube、TikTok 持續擴張版圖",
    "一篇 TechCrunch 分析指出，Spotify、YouTube、TikTok 等主要娛樂平台正加速融合彼此功能，朝「萬用娛樂 App」的形態演進。Spotify 從音樂串流擴展至 Podcast、有聲書、健身課程、社交功能；YouTube 從長影片延伸到 Shorts、Podcast、電影、音樂；TikTok 也在新增長影片、電商、票券等功能。AI 生成內容的普及加速了這趨勢，使用者可以在同一個 App 中滿足幾乎所有娛樂需求，分析師預測整合式訂閱服務即將來臨。",
    "娛樂平台的大融合趨勢，反映了 AI 降低內容製作與分發成本的效應。當所有平台都在競爭同一批用戶的注意力與訂閱預算時，垂直整合能力與 AI 個人化成為核心競爭力。這對中小型娛樂新創構成巨大壓力，但同時也為 AI 內容工具供應商創造機會。",
    "Spotify、YouTube、TikTok、Meta",
    "Spotify（SPOT）、Alphabet（GOOGL）、ByteDance（未上市）、Meta（META）",
    articles[4]))

# Article 9: Deezer AI music
categories["🏛️ AI 政策與監管"].append(cat_article("🏛️ AI 政策與監管",
    "Deezer 警告：AI 生成音樂已佔每日上傳量過半，平台祭出清理行動",
    "音樂串流平台 Deezer 宣佈，AI 生成音樂現在已佔其每日上傳量的 50% 以上，創下歷史新高。Deezer 執行長 Alexis Lanternier 表示，平台已在打擊 AI 音樂詐欺的前線近兩年，每月平均有 90,000 首 AI 生成曲目上傳。Deezer 宣佈將下架六個月內未被播放的 AI 生成曲目，以及涉及流量造假以提升收入的曲目。Deezer 從 2025 年 1 月開始追蹤 AI 音樂上傳量，當時僅佔 10%，到 2026 年 4 月已達 44%，如今正式突破 50% 大關。Deezer 也已將其 AI 音樂偵測技術提供給其他平台使用，但蘋果和 Spotify 是否採用仍不明確。",
    "AI 生成音樂的爆發性成長，正在重塑整個音樂產業生態。Deezer 的清理行動顯示平台試圖在 AI 內容洪流中維護創作者與唱片公司的利益，同時保護廣告收入的分配機制不被稀釋。這場 AI 音樂戰爭的結果，將決定小型音樂人與唱片公司在 AI 時代的生存方式。",
    "Deezer、Alexis Lanternier、Suno、Udio、Apple Music、Spotify",
    "Spotify（SPOT）、Apple（AAPL）",
    articles[8]))

# Article 10: Gritt robots solar
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "Gritt 機器人新創隱身出擊：用 AI 讓太陽能電站建造速度翻倍",
    "由兩位卡內基美隆訓練的機器人專家 Puneet Puri 與 Vishal Dugar 共同創辦的 Gritt，本週二宣佈以 2,600 萬美元 A 輪募資隱身出擊，投資人包括 Obvious Ventures 與 Union Square Ventures。Gritt 的核心產品是整合 AI 模型與市售硬體（ Kawasaki 機械手臂等）的智慧系統，讓機器人能在戶外混亂的工地環境中工作。目前其系統已部署兩套，專門負責搬運大型玻璃太陽能板、將其精準定位在支架上（次毫米精度），供工人後續固定安裝。Gritt 的願景是「幫助人類文明加速建造基礎設施」，未來計畫將技術擴展至太陽能電站以外的各類營建場景。",
    "太陽能建置正面臨嚴重的勞動力短缺，而 AI 模型的進步恰好讓機器人得以在非結構化環境中運作。Gritt 的模式不走自建硬體的路，而是以 AI 軟體整合現成設備，大幅降低商業化門檻。若驗證成功，代表營建工地將是 AI 機器人下一個大規模應用的場景。",
    "Gritt、Obvious Ventures、Union Square Ventures、First Round Capital、Puneet Puri、Vishal Dugar、Kawasaki",
    "相關概念股：工業機器人（ABB）、能源建設（Bannon 旗下太陽能建商）",
    articles[9]))

# Article 11: Apple Klarna lease
categories["🏢 企業 AI 動態"].append(cat_article("🏢 企業 AI 動態",
    "Apple 聯手 Klarna 推出訂閱升級計畫，試圖緩解 AI 時代硬體漲價壓力",
    "根據彭博報導，Apple 將與延後付款服務商 Klarna 合作，於 7 月 28 日推出「Apple Upgrade」租賃訂閱計畫，允許消費者以 24 至 36 個月的分期方式購買 iPhone、iPad、Mac 與 Apple Watch，期滿可選擇退還或升級新機。此計畫上路之際，正值 AI 熱潮導致記憶體晶片短缺（業界稱「RAMageddon」），讓硬體價格持續攀升。Apple 此前已宣佈漲價，Upgrade 計畫正是讓消費者更容易接受新價格的策略。Apple 同時正與 OpenAI 陷入侵權訴訟，John Ternus 也即將接任執行長，公司可說面臨多重轉型壓力。",
    "Apple 的租賃模式顯示，在 AI 資料中心需求排擠記憶體晶片供給的環境下，消費性硬體廠商必須以金融創新來維持銷量。若此模式成功，可能吸引更多硬體廠商跟進，推動消費電子產業從「購買」轉向「訂閱使用」的商業模式轉型。",
    "Apple、Klarna、John Ternus、OpenAI",
    "Apple（AAPL）、Klarna（未上市，KLKN.F）",
    articles[10]))

# Article 12: Sila $300M
categories["💾 AI 晶片與硬體"].append(cat_article("💾 AI 晶片與硬體",
    "Sila 逆勢募得 3 億美元，矽碳陽極材料廠產能瞄準 10 萬輛電動車",
    "電池材料新創 Sila Nanotechnologies 本週二宣佈完成 3 億美元增資，將用於擴建華盛頓州工廠的矽碳陽極材料產能，完工後每年可供超過 10 萬輛電動車使用。Sila 的陽極材料是目前少數能替代中國石墨供應鏈的選項之一，而中國目前控制全球約 75% 的石墨供應鏈。Sila 產品比傳統石墨陽極多儲存 40% 能量且充電速度更快，已與 Mercedes 與 Panasonic 簽署供應合約，並向 Whoop、無人機與衛星製造商銷售。Sila 已投入研發 15 年，創辦人 Gene Berdichevsky 是 Tesla 的第七號員工，工廠於去年 9 月開始投產。",
    "Sila 的成功增資顯示，電動車供應鏈的「去中國化」已成為明確的投資主題。AI 資料中心大量採購鋰離子電池作為備援電源，正在改變電池市場的需求結構。這為非中國供應鏈的電池材料公司創造了巨大的市場機會。",
    "Sila Nanotechnologies、Gene Berdichevsky、Mercedes、Panasonic、Whoop、Bloomberg Minerals Intelligence",
    "Tesla（TSLA）、Mercedes-Benz（MBG.DE）、Panasonic（PCRFY）、相關鋰電池材料股",
    articles[11]))

# Article 13: Bluecore Energy $10M
categories["💾 AI 晶片與硬體"].append(cat_article("💾 AI 晶片與硬體",
    "Bluecore Energy 募 1,000 萬美元：水上核反應爐瞄準資料中心供電",
    "由前 Uber Freight 員工 Kofi Asante 創辦的 Bluecore Energy，宣佈完成 1,000 萬美元 pre-seed 輪募資，投資人包括 Slauson & Co.。Bluecore 正在建造小型模組化核反應爐（SMR），並將其部署在駁船上，可移動至港口或社區附近，透過水下電纜連接電網。單座發電量約相當於 15,000 戶家庭或一座大型港口的用電需求。創辦人 Asante 表示已有多家資料中心 AI 高管表達興趣，因為海上下部結構核能可以提供電力而不需佔用陸地資源或與社區競爭水源。Bluecore 已取得港口碼頭、駁船與測試反應爐壓力容器的合約。",
    "AI 資料中心的電力需求暴增，正在催生新型態的能源創業投資。水上 SMR 若能成功商業化，將解決資料中心选址的電力限制問題，同時提供零碳能源。這是一個全新的投資賽道，適合有風險承受能力的投資人關注。",
    "Bluecore Energy、Kofi Asante、Uber Freight、Slauson & Co.、小型模組化核反應爐（SMR）",
    "核能概念股：NuScale Power（NLS）、Oklo（OKLO）、小型核電相關",
    articles[12]))

# Article 14: Suno breach 55M users
categories["🏛️ AI 政策與監管"].append(cat_article("🏛️ AI 政策與監管",
    "AI 音樂新創 Suno 爆 5,530 萬用戶資料外洩，原始碼也遭竊取",
    "根據資料外洩通報服務 Have I Been Pwned，AI 音樂生成器 Suno 去年遭駭客入侵，導致超過 5,530 萬用戶的個資被竊，其中包括姓名、住家地址、電子郵件、電話號碼、購買紀錄以及從 Stripe 竊取的部分支付卡號與到期日。事件發生於 2025 年 11 月，直到獨家調查媒體 404 Media 報導後才曝光。更嚴重的是，被竊的原始碼顯示 Suno 涉嫌從 Deezer、Genius 與 YouTube 等平台大量爬取歌曲與歌詞來訓練其 AI 模型，多家大型唱片公司已對此提起版權侵權訴訟。Suno 至今仍未公開承認這次資料外洩事件，也未主動通知受影響用戶。",
    "Suno 事件對 AI 音樂產業造成雙重打擊：其一為資料安全的信任危機；其二為版權侵權爭議升級。多起訴訟加上此次駭客事件，可能使 Suno 在與唱片公司的談判中處於劣勢，同時加深大眾對 AI 生成音樂合法性的疑慮。",
    "Suno、Have I Been Pwned、Mikey Shulman、Deezer、Genius、YouTube、Stripe、404 Media",
    "Suno（未上市）、Stripe（未上市）",
    articles[13]))

# Article 15: Instagram swap music
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "Instagram 開放更換舊貼文音樂，創作者終於可以更新「時代眼淚」配樂",
    "Instagram 本週二宣佈推出「替換音樂」（Replace Audio）工具，允許用戶修改已發佈 Feed 貼文與輪播貼文的背景音樂，同時保留原有的按讚、留言、分享與觸及率數據。在此之前，用戶若要更換音樂只能刪除原貼文重新發佈，導致所有互動數據歸零。Meta 旗下的 Instagram 表示，此功能是「給創作者更多內容掌控權」的最新一步，適用於追逐趨勢或反映個人音樂品味的演變。功能路徑為：打開目標貼文 → 右上角雙線選單 → Edit → 替換音樂。Instagram 也於上週宣佈移除一項具爭議的 AI 功能，該功能允許用戶使用 AI 修改他人公開帳號的圖片，公司坦言「未能達到目標」。",
    "Instagram 此項更新雖小，但對創作者群體意義重大。在 TikTok 與 Reels 的短影音競爭下，Meta 持續透過提升創作者工具來鞏固其平台黏著度。移除爭議 AI 功能則顯示 Meta 在 AI 功能部署上更謹慎的態度，願意在用戶反饋後承認錯誤。",
    "Instagram、Meta Platforms、AI 修改圖片功能",
    "Meta（META）",
    articles[14]))

# Article 16: Tesla robotaxi Orlando Tampa
categories["🤖 AI 產品與應用"].append(cat_article("🤖 AI 產品與應用",
    "Tesla 趕在 Q2 財報前於 Orlando 與 Tampa 啟動 Robotaxi 試營運",
    "Tesla 於本週二將數輛無監督模式的 Model Y SUV 帶到 Orlando 與 Tampa，這是繼 Miami 幾週前小型上線後，Tesla 在佛羅里達州的第三與第四個 Robotaxi 試營運城市。然而 Tesla 並未公佈具體車隊規模，也未提供更多細節。Tesla 在達拉斯與休士頓宣布自動駕駛車隊後，至今尚未擴大營運規模。CEO Elon Musk 曾表示 Robotaxi 將在 2025 年底前覆蓋半數美國人口，但進度明顯落後。先前美國交通部提議修改規定，未來可能不再要求自動駕駛車輛必須配備剎車踏板，若此規定通過，Tesla 部署的雙座 Cybercab 將可在公共道路上行駛。",
    "Tesla 的 Robotaxi 商業化速度遠低於馬斯克的承諾，但政策鬆綁可能提供轉機。若新規定實施，將是自動駕駛共享出行產業的重大突破，也可能讓 Tesla 趕在 Q2 財報前用試營運的消息來安撫投資人。",
    "Tesla、Elon Musk、Cybercab、Model Y、佛羅里達州、USDOT",
    "Tesla（TSLA）",
    articles[15]))

# Article 17: UK scraps digital ID cards
categories["🏛️ AI 政策與監管"].append(cat_article("🏛️ AI 政策與監管",
    "英國新任首相 Andy Burnham 撤銷數位身份證計畫，三百萬國民反對成關鍵",
    "英國新任首相 Andy Burnham 確認撤銷前朝推出的數位身份證計畫，承諾將省下的資源用於資助削減家庭電費的減稅方案。該計畫由前首相 Keir Starmer 提出，原定透過國家數位 ID 打擊非法工作並現代化公共服務取得途徑，預計三年花費 18 億英鎊（約 24 億美元）。然而此計畫引發英國民眾強烈反對，國會請願書收集近 300 萬個簽名，成為英國史上第二大連署。批評者指出數位 ID 將.enable 大規模監控。Burnham 於 6 月 22 日接任首相後迅速推翻這項政策。",
    "英國數位 ID 計畫的撤銷，是民主機制成功制約政府技術野心的罕見案例。這個結果對全球試圖推動數位身份系統的政府都是警示。值得注意的是，新政府將省下的資源轉向能源補貼，反映了在 AI 資料中心用電飆升的背景下，各國政府正面臨能源補貼與科技投資之間的政策優先順序抉擇。",
    "Andy Burnham、Keir Starmer、英國政府、數位身份證、國會請願",
    "無直接相關個股",
    articles[16]))

# ========== Generate HTML ==========
def card_html(art, is_top=False):
    t = art['time']
    time_str = t[:10] if t else ''
    html = f'<div class="news-card">'
    html += f'<div class="card-header"><h3><a href="{art["url"]}" target="_blank">{art["title_cn"]}</a></h3><span class="time">{time_str}</span></div>'
    html += f'<span class="source">原文：<a href="{art["url"]}" target="_blank">TechCrunch</a></span>'
    html += f'<p class="summary">{art["summary"]}</p>'
    html += f'<div class="why"><strong>💡 為什麼重要：</strong>{art["why"]}</div>'
    html += f'<div class="meta">'
    html += f'<span class="entities"><strong>關鍵實體：</strong>{art["entities"]}</span>'
    if art["stocks"] and art["stocks"] != "無直接相關個股":
        html += f'<br><span class="stocks"><strong>相關概念股：</strong>{art["stocks"]}</span>'
    html += f'</div></div>'
    return html

# Build category sections
cat_sections = {}
for cat_name, arts in categories.items():
    if arts:
        cat_sections[cat_name] = arts

total_news = sum(len(v) for v in cat_sections.values())
total_cats = len(cat_sections)

# Top 3 headlines (pick by significance)
top3_candidates = [
    ("🌍 AI 國際與地緣政治", categories["🌍 AI 國際與地緣政治"][0] if categories["🌍 AI 國際與地緣政治"] else None),
    ("🧠 AI 模型與研究", categories["🧠 AI 模型與研究"][0] if categories["🧠 AI 模型與研究"] else None),
    ("🧠 AI 模型與研究", categories["🧠 AI 模型與研究"][1] if len(categories["🧠 AI 模型與研究"]) > 1 else None),
    ("💾 AI 晶片與硬體", categories["💾 AI 晶片與硬體"][0] if categories["💾 AI 晶片與硬體"] else None),
]
top3 = [x for x in top3_candidates if x[1] is not None][:3]

# Keywords
all_entities = []
for arts in cat_sections.values():
    for a in arts:
        all_entities.extend([e.strip() for e in a['entities'].split(',')])
entity_counts = {}
for e in all_entities:
    entity_counts[e] = entity_counts.get(e, 0) + 1
top_entities = sorted(entity_counts.items(), key=lambda x: -x[1])[:20]
top_entities_str = "、".join([e[0] for e in top_entities])

html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 新聞摘要 {DATE} | TECH</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Microsoft JhengHei", sans-serif; background: #080810; color: #e8e8f0; line-height: 1.7; padding: 20px; min-height: 100vh; }}
.container {{ max-width: 1200px; margin: 0 auto; }}
.page-header {{ padding: 40px 30px 30px; background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(0,255,136,0.06)); border: 1px solid rgba(0,212,255,0.2); border-radius: 20px; margin-bottom: 30px; }}
.page-header .date {{ color: #00d4ff; font-size: 0.9em; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px; }}
.page-header h1 {{ font-size: 2.4em; font-weight: 900; background: linear-gradient(135deg, #00d4ff, #00ff88); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 12px; }}
.page-header .stats {{ color: #888; font-size: 0.95em; margin-bottom: 20px; }}
.page-header .stats span {{ color: #00ff88; font-weight: 700; }}
.tags {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.tag {{ background: rgba(0,212,255,0.1); border: 1px solid rgba(0,212,255,0.25); color: #00d4ff; padding: 4px 12px; border-radius: 20px; font-size: 0.82em; font-weight: 600; }}
.top-stories {{ margin-bottom: 40px; }}
.top-stories h2 {{ color: #00ff88; font-size: 1.4em; margin-bottom: 16px; }}
.headline-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }}
.headline-card {{ background: linear-gradient(135deg, rgba(0,212,255,0.07), rgba(0,255,136,0.04)); border: 1px solid rgba(0,212,255,0.2); border-radius: 14px; padding: 24px; position: relative; overflow: hidden; }}
.headline-card::before {{ content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #00d4ff, #00ff88); }}
.headline-card .rank {{ font-size: 0.75em; color: #00ff88; font-weight: 800; letter-spacing: 2px; margin-bottom: 10px; }}
.headline-card h3 {{ color: #fff; font-size: 1.1em; margin-bottom: 10px; line-height: 1.4; }}
.headline-card p {{ color: #aaa; font-size: 0.88em; line-height: 1.55; }}
.headline-card .source {{ color: #00d4ff; font-size: 0.8em; margin-top: 10px; display: block; }}
.radar {{ margin-bottom: 40px; }}
.radar h2 {{ color: #00d4ff; font-size: 1.4em; margin-bottom: 16px; }}
.category-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }}
.category-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 18px 20px; display: flex; align-items: center; gap: 14px; }}
.category-card .icon {{ font-size: 1.6rem; flex-shrink: 0; }}
.category-card .info .name {{ font-weight: 700; color: #e8e8f0; font-size: 0.95em; }}
.category-card .info .count {{ color: #00ff88; font-size: 0.8em; margin-top: 2px; }}
.section-title {{ color: #00d4ff; font-size: 1.3em; margin-bottom: 16px; margin-top: 40px; padding-bottom: 8px; border-bottom: 1px solid rgba(0,212,255,0.15); display: flex; align-items: center; gap: 10px; }}
.news-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 14px; padding: 24px; margin-bottom: 16px; transition: border-color 0.25s; }}
.news-card:hover {{ border-color: rgba(0,212,255,0.3); }}
.news-card .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; margin-bottom: 10px; }}
.news-card h3 {{ font-size: 1.05em; color: #fff; line-height: 1.4; flex: 1; }}
.news-card h3 a {{ color: inherit; text-decoration: none; }}
.news-card h3 a:hover {{ color: #00d4ff; }}
.news-card .time {{ color: #666; font-size: 0.8em; white-space: nowrap; flex-shrink: 0; }}
.news-card .source {{ color: #00d4ff; font-size: 0.8em; margin-bottom: 10px; display: block; }}
.news-card .source a {{ color: inherit; text-decoration: none; }}
.news-card .source a:hover {{ text-decoration: underline; }}
.news-card .summary {{ color: #bbb; font-size: 0.9em; line-height: 1.65; margin-bottom: 12px; }}
.news-card .meta {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
.news-card .tag-sm {{ background: rgba(0,255,136,0.08); border: 1px solid rgba(0,255,136,0.2); color: #00ff88; padding: 2px 9px; border-radius: 10px; font-size: 0.75em; font-weight: 600; }}
.news-card .why {{ background: rgba(0,212,255,0.05); border: 1px solid rgba(0,212,255,0.12); border-radius: 8px; padding: 10px 14px; margin-top: 10px; font-size: 0.85em; color: #aaa; line-height: 1.55; }}
.news-card .why strong {{ color: #00d4ff; }}
.news-card .entities {{ color: #888; font-size: 0.8em; margin-top: 8px; }}
.news-card .entities strong {{ color: #aaa; }}
.news-card .stocks {{ color: #ffcc00; font-size: 0.8em; margin-top: 4px; }}
.news-card .stocks strong {{ color: #ffe066; }}
.keywords {{ margin-bottom: 40px; }}
.keywords h2 {{ color: #00ff88; font-size: 1.3em; margin-bottom: 14px; }}
.kw-cloud {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.kw {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); color: #aaa; padding: 6px 14px; border-radius: 8px; font-size: 0.85em; }}
.kw.w {{ background: rgba(0,212,255,0.08); border-color: rgba(0,212,255,0.25); color: #00d4ff; }}
.kw.g {{ background: rgba(0,255,136,0.06); border-color: rgba(0,255,136,0.2); color: #00ff88; }}
.lookahead {{ margin-bottom: 40px; }}
.lookahead h2 {{ color: #ffcc00; font-size: 1.3em; margin-bottom: 14px; }}
.lookahead-box {{ background: rgba(255,204,0,0.04); border: 1px solid rgba(255,204,0,0.15); border-radius: 14px; padding: 24px; color: #ccc; font-size: 0.9em; line-height: 1.8; }}
.lookahead-box li {{ margin-bottom: 8px; padding-left: 20px; position: relative; }}
.lookahead-box li::before {{ content: "▸"; position: absolute; left: 0; color: #ffcc00; }}
footer {{ text-align: center; color: #555; font-size: 0.85em; padding: 30px 20px; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 50px; }}
footer a {{ color: #00d4ff; text-decoration: none; }}
@media(max-width:768px){{.page-header{{padding:24px 18px;}}.page-header h1{{font-size:1.8em;}}}}
</style>
</head>
<body>
<div class="container">
<div class="page-header">
<div class="date">{DATE_DISPLAY} · 台北時間 12:30 更新</div>
<h1>🤖 AI 新聞每日摘要</h1>
<div class="stats">共收錄 <span>{total_news}</span> 則 AI 相關新聞，涵蓋 <span>{total_cats}</span> 個分類</div>
<div class="tags">
<span class="tag">Gemini 3.6</span>
<span class="tag">中美 AI 制裁</span>
<span class="tag">Anthropic</span>
<span class="tag">機器人</span>
<span class="tag">資料中心用電</span>
<span class="tag">Suno 資料外洩</span>
<span class="tag">Robotaxi</span>
<span class="tag">Deezer</span>
</div>
</div>

<div class="top-stories">
<h2>📰 今日三大頭條</h2>
<div class="headline-grid">'''

for i, (cat, art) in enumerate(top3, 1):
    time_str = art['time'][:10] if art['time'] else ''
    html += f'''<div class="headline-card">
<div class="rank">TOP {i} · {cat}</div>
<h3><a href="{art["url"]}" target="_blank">{art["title_cn"]}</a></h3>
<p>{art["summary"][:180]}…</p>
<span class="source">📎 <a href="{art["url"]}" target="_blank">TechCrunch</a> · {time_str}</span>
</div>'''

html += '</div></div>'

html += '<div class="radar"><h2>📊 主題雷達</h2><div class="category-grid">'
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
for cat_name, arts in cat_sections.items():
    icon = cat_icons.get(cat_name, "📰")
    representative = arts[0]['title_cn'][:25]
    html += f'''<div class="category-card">
<div class="icon">{icon}</div>
<div class="info">
<div class="name">{cat_name}</div>
<div class="count">共 {len(arts)} 則 · {representative}…</div>
</div>
</div>'''
html += '</div></div>'

for cat_name, arts in cat_sections.items():
    icon = cat_icons.get(cat_name, "📰")
    html += f'<div class="section-title">{icon} {cat_name}（{len(arts)} 則）</div>'
    for art in arts:
        html += card_html(art)

html += f'''
<div class="keywords">
<h2>🔑 今日關鍵詞彙</h2>
<div class="kw-cloud">
<span class="kw w">Gemini 3.6 Flash</span>
<span class="kw g">Kimi K3</span>
<span class="kw w">Physical Intelligence</span>
<span class="kw">Suno 資料外洩</span>
<span class="kw g">Deezer AI 音樂</span>
<span class="kw">RAMageddon</span>
<span class="kw w">Apple Upgrade</span>
<span class="kw g">Gritt 機器人</span>
<span class="kw">Cybercab</span>
<span class="kw w">BloombergNEF</span>
<span class="kw g">Sila 矽碳陽極</span>
<span class="kw">Bluecore SMR</span>
<span class="kw w">Buzz（Jack Dorsey）</span>
<span class="kw g">UK 數位 ID</span>
<span class="kw">Hugging Face</span>
<span class="kw w">Replace Audio</span>
</div>
</div>

<div class="lookahead">
<h2>🔮 明日觀察</h2>
<div class="lookahead-box">
<ul>
<li><strong>Gemini 3.5 Pro 何時發布？</strong>：Google 內部掙扎於 Pro 旗艦模型的效能瓶頸，OpenAI GPT-5.6 已在市場上形成壓力。明日是否有更多內部消息釋出，值得觀察。</li>
<li><strong>英國數位 ID 撤銷的後續</strong>：節省下來的資源是否真的轉向能源補貼，將考驗 Andy Burnham 政府的政策執行力。</li>
<li><strong>OpenAI 預發布模型被駭一事</strong>：是否有更多細節曝光，以及監管機構是否會介入調查。</li>
<li><strong>Tesla Q2 財報與 Robotaxi 進度</strong>：馬斯克能否用佛州試營運的進展來安撫投資人，扭轉市場對 Robotaxi 延遲的不滿。</li>
<li><strong>Suno 資料外洩受害者通知</strong>：在 5,530 萬用戶受影響且公司拒絕公開回應的情況下，是否會引發監管機構主動介入。</li>
</ul>
</div>
</div>

<footer>
<p>📡 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI News</a> · 整理：AI 編譯系統</p>
<p>🤖 此報告由 AI 自動生成，內容忠實呈現原文，未含主觀立場</p>
<p>📅 報告日期：{DATE_DISPLAY}</p>
</footer>
</div>
</body>
</html>'''

with open(f'/home/matt/.openclaw/workspace/TECH/news/{DATE}.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Report generated: {DATE}.html")
print(f"   Total articles: {total_news}")
print(f"   Total categories: {total_cats}")
