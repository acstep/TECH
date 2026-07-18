import datetime

today = "2026-07-18"
report_date = "2026年7月18日（週六）"
date_display = "July 18, 2026"

news_items = [
    {
        "id": "1",
        "title": "Neil Rimer thinks the AI money is coming back out",
        "title_tw": "Index Ventures 共同創辦人 Neil Rimer：AI 財富將會重新分配",
        "url": "https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/",
        "source": "TechCrunch",
        "pubDate": "Sat, 18 Jul 2026 04:47:25 +0000",
        "pubDate_tw": "2026年7月18日",
        "category": "💰 AI 投融資與併購",
        "summary": "Index Ventures 共同創辦人 Neil Rimer 預測，AI 在矽谷創造的歷史性財富將不得不重新分配，無論是自願或非自願。他表示：「強烈感覺會有某種形式的財富重分配，希望是自願的。」此番發言正值 OpenAI 傳出考慮 2027 年 IPO 之際，而 Giving Pledge 等慈善承諾已日漸失色。據 Forbes 統計，2026 年新增了 45 位 AI 億萬富翁，總淨資產達 2.9 兆美元。",
        "why_important": "反映矽谷 AI 財富高度集中的爭議，加州富人稅提案若通過將重創科技富豪，OpenAI 上市時機充滿變數。",
        "entities": "Index Ventures、Neil Rimer、OpenAI、Anthropic、Sam Altman、Elon Musk",
        "stocks": "MSFT、GOOG",
        "category_key": "funding"
    },
    {
        "id": "2",
        "title": "Databricks hits $188B valuation, extending its run as AI's favorite second act",
        "title_tw": "Databricks 估值達 1880 億美元，AI 轉型故事持續發燒",
        "url": "https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 22:12:56 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "💰 AI 投融資與併購",
        "summary": "Databricks 宣布新一輪募資，公司估值一舉攀升至 1880 億美元。本輪由 Coatue 領投，金額約 30 億美元。這是 Databricks 在過去一年半以來第四度大型募資：去年 12 月以 620 億美元估值募得 100 億；今年 2 月以 1340 億美元估值募得 50 億；如今再以 1880 億美元估值募資。Databricks 已成功從大數據公司轉型為 AI 企業，並積極推廣開源模型（如 Z.ai 的 GLM 5.2）以節省 AI 編碼成本。",
        "why_important": "Databricks 的快速轉型與估值飆升，代表企業 AI 市場持續火熱，開源模型在企業端的採用率明顯提升。",
        "entities": "Databricks、Coatue、Ali Ghodsi、GLM 5.2、Z.ai",
        "stocks": "Databricks（私募）",
        "category_key": "funding"
    },
    {
        "id": "3",
        "title": "Why the first GPU financiers are turning to inference chips in a $400 million deal",
        "title_tw": "首批 GPU 投資人轉向推論晶片，4 億美元交易揭示 AI 基礎設施新趨勢",
        "url": "https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 12:00:00 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "💾 AI 晶片與硬體",
        "summary": "AI 推論雲端新創 General Compute 從 Upper90 獲得 4 億美元晶片抵押貸款，可能是首筆以推論專用晶片（而非訓練用 GPU）作為擔保的貸款。General Compute 使用 SambaNova 的 SN50 晶片，號稱比 GPU 雲端快 16 倍，且不需水冷系統，可更快部署。Upper90 曾於 2021 年率先以 GPU 作為抵押品借貸給 Crusoe，如今則看好開源推論市場的成長。",
        "why_important": "AI 基礎設施投資焦點正從訓練晶片轉向推論晶片，開源模型生態系的興起正在改變晶片市場格局，Nvidia 壟斷地位可能開始鬆動。",
        "entities": "General Compute、Upper90、SambaNova、CoreWeave、Nvidia、AMD、Groq、Cerebras",
        "stocks": "NVDA、AMD、INTC",
        "category_key": "chips"
    },
    {
        "id": "4",
        "title": "Agility Robotics plants its flag in Tesla's backyard",
        "title_tw": "Agility Robotics 進駐特斯拉工廠附近，開啟人形機器人商業化競賽",
        "url": "https://techcrunch.com/2026/07/17/agility-robotics-plants-its-flag-in-teslas-backyard/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 20:19:49 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🤖 AI 產品與應用",
        "summary": "Agility Robotics 宣布在加州佛利蒙（Fremont）設立 6 萬平方英尺的新訓練中心，距離特斯拉 Optimus 工廠僅數英里。Agility 的 Digit 機器人已在亞馬遜、GXO、Schaeffler、豐田等客戶的倉庫中賺取營收，累計完成 10 萬次搬運籃筐任務。公司已取得 3 億美元訂單，並預計透過反向併購於年底前上市。執行長 Peggy Johnson 表示：「人形機器人領域有特斯拉加入是好事，過去 Agility 一直孤軍奮戰。」",
        "why_important": "人形機器人商業化進程加速，Agility 已有實際營收與訂單，成為首家公開上市的人形機器人公司，與特斯拉 Optimus 的競爭正式開打。",
        "entities": "Agility Robotics、Digit、Peggy Johnson、Tesla、Optimus、Elon Musk、Jonathan Hurst、Damion Shelton",
        "stocks": "TSLA",
        "category_key": "product"
    },
    {
        "id": "5",
        "title": "Vertu wants executives to pay $6,880 for an AI agent — here's how it actually performs",
        "title_tw": "Vertu 推 6,880 美元 AI 代理手機，Hermes Agent 實測出爐",
        "url": "https://techcrunch.com/2026/07/17/vertu-wants-executives-to-pay-6880-for-an-ai-agent-heres-how-it-actually-performs/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 22:55:09 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🤖 AI 產品與應用",
        "summary": "英國奢侈品手機品牌 Vertu 推出 Alphafold 折疊手機，售價 6,880 美元起，核心賣點是預裝的 Hermes Agent AI 代理。Hermes 基於開源 Hermes 專案構建，可分析文件、在應用程式間自動化任務、記憶對話，並在必要時轉接人工禮賓服務。實測顯示，Hermes 在分析本地檔案和試算表方面優於三星 Galaxy Z Fold 7 的 Gemini，但在機場導航場景中出現錯誤（設錯提醒時間、未自動開始導航）。Vertu 已坦承硬體平台來自中興通訊的 ZTE Nubia Fold。",
        "why_important": "AI Agent 硬體化成為高階手機新戰場，Vertu 以奢侈品定位切入 Executive AI 市場，測試結果顯示 AI Agent 的自主性與可靠性仍有改進空間。",
        "entities": "Vertu、Alphafold、Hermes Agent、Nous Research、Samsung、ZTE、Google Gemini",
        "stocks": "GOOG、三星（KRX:005930）",
        "category_key": "product"
    },
    {
        "id": "6",
        "title": "Apple and Google ordered to purge 'nudify' apps from App Stores",
        "title_tw": "舊金山市府下令 Apple 與 Google 下架「脫衣」deepfake 應用程式",
        "url": "https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 19:49:53 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🏛️ AI 政策與監管",
        "summary": "舊金山市檢察長 David Chiu 向 Apple 和 Google 發出正式信函，要求兩家公司從應用商店移除數十款「nudify」應用程式——即利用 AI 將照片中人物自動脫衣的軟體。舊金山市府援引加州法律，刑事化明知且協助或魯莽協助創建非自願 deepfake 色情內容的行為。信中指出，兩家公司長期知曉這些違規應用程式，並從非法購買中賺取「數百萬美元」費用。Apple 表示已移除 3 款問題應用並終止開發者帳戶；Google 聲稱已暫停信中提及的全部 5 款 Play 商店應用。",
        "why_important": "Deepfake 監管從立法走向執法階段，平台責任被重新檢視，Apple 與 Google 可能面臨民事罰款，這是 AI 倫理監管的重要風向球。",
        "entities": "Apple、Google、David Chiu、舊金山市府、Tech Transparency Project",
        "stocks": "AAPL、GOOG",
        "category_key": "policy"
    },
    {
        "id": "7",
        "title": "Patreon stops asking AI bots not to scrape — and starts blocking them",
        "title_tw": "Patreon 放棄 robots.txt，改用 Cloudflare 直接封鎖 AI 爬蟲",
        "url": "https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 15:21:17 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🏛️ AI 政策與監管",
        "summary": "創作人贊助平台 Patreon 宣布與 Cloudflare 合作，採用 AI Crawl Control 技術主動封鎖未經授權的 AI 訓練爬蟲，不再僅依賴 robots.txt 協議。Patreon 表示，2023 年設定的防護措施已無法抵擋日益精密的 AI 爬蟲，部分爬蟲直接無視 robots.txt 規定。新技術上線後，個別 AI 訓練爬蟲的每週訪問嘗試從「數千次降至零」。Patreon 產品長 Drew Rowny 表示：「同意不應取決於爬蟲是否選擇遵守規則。」允許索引頁面並導流回 Patreon 的爬蟲正常運作。",
        "why_important": "AI 訓練資料的版權與授權爭議加劇，Patreon 的做法代表內容平台從被動聲明轉向主動技術封鎖，可能成為業界標準。",
        "entities": "Patreon、Cloudflare、Drew Rowny、AI Crawl Control、Pay Per Crawl",
        "stocks": "NET（Cloudflare）",
        "category_key": "policy"
    },
    {
        "id": "8",
        "title": "How Apple's big lawsuit could disrupt OpenAI's IPO plans",
        "title_tw": "Apple 控告 OpenAI 侵權：可能攪亂 OpenAI IPO 佈局",
        "url": "https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 17:45:46 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🏛️ AI 政策與監管",
        "summary": "Apple 上週五對 OpenAI 提起商業機密訴訟，指控其不當行為一路涉及 OpenAI 首席硬體長，並聲稱超過 400 名蘋果前員工現在任職於 OpenAI。投訴時機正值 OpenAI 據報導正考慮最快今年底 IPO 之際。OpenAI 的回應迄今相當謹慎。TechCrunch Equity podcast 分析師認為，此訴訟不僅影響 OpenAI 的硬體野心，也為整體 AI 產業的資料信任議題敲響警鐘。",
        "why_important": "Apple vs OpenAI 訴訟時機敏感，恰好在 OpenAI 衝刺 IPO 階段，可能被迫延後上市或增加額外監管壓力，並引發企業對 AI 廠商資料處理的高度關注。",
        "entities": "Apple、OpenAI、Sam Altman、Satya Nadella（微軟 CEO）",
        "stocks": "AAPL、MSFT、OPENAI（私募）",
        "category_key": "policy"
    },
    {
        "id": "9",
        "title": "The Zoom hack that says, 'Don't record me'",
        "title_tw": "對抗 AI 錄音風：創投將名字改為「拒絕錄音」",
        "url": "https://techcrunch.com/2026/07/17/the-zoom-hack-that-says-dont-record-me/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 21:20:47 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "🏛️ AI 政策與監管",
        "summary": "華爾街日報報導，隨著 AI 記事錄音應用程式（如 Granola、Pocket、Speakons）蓬勃興起，創投 Jeremy Levine 在 Zoom 上的名字變成了「Jeremy Levine I do not consent to transcribing or recording」。另一位創投 Eric Bahn 表示，現在與新創創辦人開會時，他默認對方已在錄音。有創辦人甚至用 Granola 記錄第一次約會，再餵給 Claude 分析自己的表現。專家警告，萬一所有會議、聊天、約會都被轉錄存檔，這些「音訊垃圾掩埋場」遲早會失去實用價值。",
        "why_important": "AI 錄音滲透日常對話隱私， consent（同意）與資料所有權問題日益尖銳，相關法律規範將加速研擬。",
        "entities": "Zoom、Granola、Pocket、Speakons、Claude",
        "stocks": "ZM（Zoom）",
        "category_key": "policy"
    },
    {
        "id": "10",
        "title": "AI-driven memory crunch jolts India's smartphone market",
        "title_tw": "AI 記憶體需求衝擊印度手機市場：出貨量暴跌 10% 創六年最深跌幅",
        "url": "https://techcrunch.com/2026/07/17/ai-driven-memory-crunch-jolts-indias-smartphone-market/",
        "source": "TechCrunch",
        "pubDate": "Fri, 17 Jul 2026 20:09:27 +0000",
        "pubDate_tw": "2026年7月17日",
        "category": "💾 AI 晶片與硬體",
        "summary": "記憶體晶片大廠將產能轉向 AI 加速器所需的高頻寬記憶體（HBM），導致手機與筆電用標準記憶體供應縮減、價格攀升。印度身為全球第二大智慧手機市場，受到最大衝擊：今年 Q2 出貨量年減 10%，創六年來 Q2 最大跌幅。約 60% 市場集中在 20,000 盧比（約 210 美元）以下低價區段，該區段價格漲幅最劇（4%~68%）。三星是唯一逆勢成長的大品牌（出貨增 2%），中國品牌市占率跌至 2020 年以來新低。消費者平均換機周期從 3.5 年延長至 4 年。",
        "why_important": "AI 熱潮對消費電子供應鏈的副作用顯現，HBM 需求搶走手機記憶體產能，長期低價手機的價格競爭力受損，智慧手機產業結構將被迫重組。",
        "entities": "Samsung、SK Hynix、Micron、Apple、OnePlus、Counterpoint Research、IDC",
        "stocks": "005930.KS（三星）、AMAT、MU",
        "category_key": "chips"
    },
    {
        "id": "11",
        "title": "Google Vids now lets you star in your own AI videos",
        "title_tw": "Google Vids 推出個人化 AI 虛擬人影片功能，挑戰 HeyGen、Synthesia",
        "url": "https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 18:32:54 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🤖 AI 產品與應用",
        "summary": "Google 宣布更新 Workspace 中的 Google Vids，加入個人化 AI 虛擬人功能：用戶上傳一張自拍和一條語音錄製，即可生成外貌與聲音相似的數位分身。結合 Gemini Omni 多模態模型，可透過文字提示與參考圖片創作影片、交換背景、修正照明。支援逐步編輯。Google 強調所有虛擬人與帳戶綁定並有無痕 SynthID浮水印。Vids 從原本的 AI 簡報工具升級為一站式影片創作平台，直接挑戰 HeyGen、Synthesia、D-ID 等新創。",
        "why_important": "AI 影片創作門檻持續降低，Google 以 Workspace 生態系優勢切入個人化 AI 影片市場，企業培訓與行銷影片應用場景將快速普及。",
        "entities": "Google、Google Vids、Gemini Omni、Sundar Pichai、HeyGen、Synthesia、Cap、OpenAI Sora",
        "stocks": "GOOG",
        "category_key": "product"
    },
    {
        "id": "12",
        "title": "Why is OpenAI selling a ChatGPT basketball?",
        "title_tw": "OpenAI 推出 70 美元 ChatGPT 籃球：行銷还是精神勝利？",
        "url": "https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 15:31:09 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🤖 AI 產品與應用",
        "summary": "OpenAI 本週發布了首款硬體——一款 230 美元的 Codex 鍵盤——但更引人注目的是同時推出的 70 美元 ChatGPT 籃球。產品說明寫道：「這個籃球來自『Pause. Play. Prompt.』活動，是一個提醒：創造力不只存在於我們的螢幕上。」這款全橡膠籃球較適合戶外使用。評論者調侃：很難想像目標客群是誰，也有人拿它與失敗的 Humane Ai Pin 相比。OpenAI 同期還推出了 175 美元的「Research」書法字樣刷手衣。",
        "why_important": "OpenAI 硬體策略引發質疑，ChatGPT 籃球的象徵意義大於實質，但代表 OpenAI 建立消費品牌認知的嘗試。",
        "entities": "OpenAI、Sam Altman、Humane Ai Pin、ChatGPT",
        "stocks": "MSFT（OpenAI 大股东）",
        "category_key": "product"
    },
    {
        "id": "13",
        "title": "Google's AI Mode now lets you link and interact with select apps",
        "title_tw": "Google AI Mode 新增應用程式串接：Instacart、Canva、YouTube 率先支援",
        "url": "https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 16:00:00 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🤖 AI 產品與應用",
        "summary": "Google 宣布 AI Mode 新增第三方應用串接功能，上線時支援 Instacart、Canva、YouTube。用戶可在 AI Mode 中規劃烤肉購物清單並直接加入 Instacart 購物車；或在需要設計提案時讓 Canva 顯示範本；也可讓 AI Mode 幫你策劃派對歌單並一鍵存到 YouTube Music。這是 Google 將 AI Mode 從「回答問題」擴展到「完成任務」的關鍵一步，也可視為對 OpenAI ChatGPT 與 Anthropic Claude 應用串接功能的正面競爭。",
        "why_important": "AI 助手從被動工具走向主動代理（Agent），Google 以搜尋優勢疊加應用生態系搶奪 AI 日常應用場景。",
        "entities": "Google、AI Mode、Gemini、Instacart、Canva、YouTube Music",
        "stocks": "GOOG",
        "category_key": "product"
    },
    {
        "id": "14",
        "title": "Moonshot's upcoming Kimi 3 is expected to close the gap with Anthropic's Opus 4.8",
        "title_tw": "中國 Moonshot AI 推出 Kimi K3：參數量 2~3 兆，瞄準 Anthropic Opus 4.8",
        "url": "https://techcrunch.com/2026/07/16/moonshot-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 14:26:29 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🧠 AI 模型與研究",
        "summary": "金融時報引述知情人士報導，Moonshot AI 即將發布的 Kimi K3 模型在效能上可與 Anthropic 的旗艦模型 Opus 4.8 並駕齊驅，甚至超越。Kimi K3 將是中國最大開源權重模型，參數量達 2 兆至 3 兆，預計「數日內」發布。Moonshot 同期也在洽談新一輪募資，估值將達 315 億美元；今年 5 月剛以 200 億美元估值募得 20 億美元。此消息正值企業高層重新評估使用昂貴封閉模型（OpenAI、Anthropic）的價值。",
        "why_important": "中國 AI 模型能力快速追趕美國頂級封閉模型，開源模型陣營持續壯大，進一步削弱封閉模型公司的訂價能力與市場主導地位。",
        "entities": "Moonshot AI、Kimi K3、Anthropic、Opus 4.8、DeepSeek、Z.ai、OpenAI",
        "stocks": "Anthropic（私募，投資者包括 GOOG）",
        "category_key": "model"
    },
    {
        "id": "15",
        "title": "AMI Labs' Alexandre LeBrun won't call his AI 'AGI' or 'superintelligence'",
        "title_tw": "Yann LeCun 投資的 AMI Labs：我們不稱呼自己的 AI 為 AGI",
        "url": "https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 14:40:00 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🧠 AI 模型與研究",
        "summary": "Yann LeCun 共同創立的 AI 新創 AMI Labs，其執行長 Alexandre LeBrun 明確拒絕使用「AGI」或「超智慧」等詞彙來描述自家技術。他認為這些術語過度承諾且無意義：「我不會用 AGI 或超智慧這些詞，因為這些詞已經失去精確定義。」AMI Labs 專注於「世界模型」（world model）技術，LeBrun 強調這是一個具體、可測量的研究方向，而非一個行銷術語。",
        "why_important": "AI 業界對 AGI 命名的反彈情緒升溫，LeBrun 的表態反映一股拒絕過度行銷的聲音，有助於市場對 AI 能力建立更務實的期待。",
        "entities": "AMI Labs、Alexandre LeBrun、Yann LeCun、Meta、World Model",
        "stocks": "META（LeCun 是 Meta 首席 AI 科學家）",
        "category_key": "model"
    },
    {
        "id": "16",
        "title": "Roblox launches an AI-powered game-creation feature in its mobile app",
        "title_tw": "Roblox 在手機 App 推出 AI 遊戲生成功能，降低創作門檻",
        "url": "https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 18:22:06 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🤖 AI 產品與應用",
        "summary": "Roblox 宣布在行動 App 中推出「Build」功能，用戶只需輸入一段文字提示，AI 即可生成一款基礎遊戲。這是 Roblox 將 AI 創作工具從桌面端擴展到行動端的重要一步，讓任何人都能成為遊戲創作者。Roblox 表示此功能旨在降低遊戲創作門檻，吸引更多休閒玩家轉型為創作者，進一步擴大平台生態系。",
        "why_important": "AI 遊戲創作工具從專業人士走向一般大眾，Roblox 結合平台與 AI 降低門檻，可能催生新一波 UGC 遊戲浪潮。",
        "entities": "Roblox、Build",
        "stocks": "RBLX",
        "category_key": "product"
    },
    {
        "id": "17",
        "title": "Yes, you can now order DoorDash from the command line",
        "title_tw": "DoorDash 推出命令列外送工具 dd-cli，瞄準 AI Agent 應用場景",
        "url": "https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 15:38:55 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "🤖 AI 產品與應用",
        "summary": "DoorDash 宣布開放 dd-cli 限量測試版，這是一款命令列工具，讓開發者與 AI Agent 可直接在終端機中搜尋商店、建立購物車並下單外送。DoorDash 表示這是朝向「為 AI Agent 而非僅為人類設計的軟體」願景的又一步。Claude、ChatGPT 等 AI 助理現在可以代替用戶直接完成外送任務，標誌著 AI Agent 滲透日常消費場景的重大進展。",
        "why_important": "AI Agent 電子商務時代來臨，DoorDash 率先將外送流程 API 化，讓 AI 代理直接執行消費任務，這是 AI 商業化的重要里程碑。",
        "entities": "DoorDash、dd-cli、AI Agent、Claude、ChatGPT",
        "stocks": "DASH",
        "category_key": "product"
    },
    {
        "id": "18",
        "title": "How a former DeepMind researcher raised at a $300M pre-seed valuation before launching a product",
        "title_tw": "前 DeepMind 研究員創立 AMI Labs：產品未推出估值已達 3 億美元",
        "url": "https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/",
        "source": "TechCrunch",
        "pubDate": "Thu, 16 Jul 2026 15:02:00 +0000",
        "pubDate_tw": "2026年7月16日",
        "category": "💰 AI 投融資與併購",
        "summary": "前 Google DeepMind 研究員 Andrew Dai 創立的新創公司，在尚未推出任何產品的情況下，即以 3 億美元 pre-seed 估值獲得資金。Andrew Dai 曾參與部分日後成為 ChatGPT 發展基礎的研究。他選擇視覺 AI 作為下一個重大突破口，並獲得包括 Yann LeCun 在內的重量級投資人支持。這類超高估值的 pre-seed 輪在 AI 領域日益常見，反映資金對於頂級 AI 人才的強烈飢渴。",
        "why_important": "AI 人才戰激烈，頂級研究人員可在無產品階段募集巨額資金，代表 AI 領域「以人為本」的投資邏輯已成為主流。",
        "entities": "AMI Labs、Andrew Dai、DeepMind、Yann LeCun、Google、ChatGPT",
        "stocks": "GOOG（DeepMind）",
        "category_key": "funding"
    }
]

# Categorize
categories = {
    "chips": {"name": "💾 AI 晶片與硬體", "items": [], "icon": "💾"},
    "model": {"name": "🧠 AI 模型與研究", "items": [], "icon": "🧠"},
    "product": {"name": "🤖 AI 產品與應用", "items": [], "icon": "🤖"},
    "enterprise": {"name": "🏢 企業 AI 動態", "items": [], "icon": "🏢"},
    "funding": {"name": "💰 AI 投融資與併購", "items": [], "icon": "💰"},
    "policy": {"name": "🏛️ AI 政策與監管", "items": [], "icon": "🏛️"},
    "people": {"name": "👥 AI 人事與組織", "items": [], "icon": "👥"},
    "global": {"name": "🌍 AI 國際與地緣政治", "items": [], "icon": "🌍"},
}

for item in news_items:
    cat_key = item["category_key"]
    if cat_key in categories:
        categories[cat_key]["items"].append(item)

# Top 3 headlines
top3 = news_items[:3]

# Keywords
keywords = [
    "1880億美元估值", "Databricks", "OpenAI IPO", "Apple 訴訟", "Kimi K3",
    "開源模型", "推理晶片", "人形機器人", "Deepfake 監管", "AI Agent",
    "Google Vids", "Cloudflare", "記憶體危機", "印度手機市場", "Vertu",
    "Patreon", "DoorDash CLI", "AGI", "Yann LeCun", "NVIDIA"
]

html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 新聞 {today}｜TECH 每日 AI 新聞中文整理</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Microsoft JhengHei", sans-serif; background: #080810; color: #e8e8f0; line-height: 1.7; padding: 20px; min-height: 100vh; }}
.container {{ max-width: 1200px; margin: 0 auto; }}
.back-link {{ display: inline-flex; align-items: center; gap: 8px; color: #00d4ff; text-decoration: none; font-size: 0.95em; margin-bottom: 24px; padding: 8px 16px; background: rgba(0,212,255,0.06); border: 1px solid rgba(0,212,255,0.2); border-radius: 8px; transition: all 0.25s; }}
.back-link:hover {{ background: rgba(0,212,255,0.12); border-color: rgba(0,212,255,0.4); }}
header {{ padding: 40px 0 30px; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 40px; }}
.header-top {{ display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; }}
.header-date {{ color: #888; font-size: 0.9em; margin-bottom: 6px; }}
h1 {{ font-size: 2.4em; font-weight: 900; background: linear-gradient(135deg, #00d4ff, #00ff88); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px; }}
.header-stats {{ display: flex; gap: 20px; flex-wrap: wrap; margin-top: 16px; }}
.stat-badge {{ background: rgba(0,212,255,0.08); border: 1px solid rgba(0,212,255,0.2); border-radius: 20px; padding: 4px 14px; font-size: 0.85em; color: #00d4ff; }}

/* Top 3 */
.top3-section {{ margin-bottom: 50px; }}
.section-label {{ color: #00ff88; font-size: 0.85em; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 16px; }}
.top3-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
.top3-card {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(0,212,255,0.2); border-radius: 16px; padding: 28px; transition: all 0.3s; position: relative; overflow: hidden; }}
.top3-card::before {{ content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #00d4ff, #00ff88); }}
.top3-card:hover {{ transform: translateY(-3px); border-color: rgba(0,212,255,0.5); box-shadow: 0 12px 32px rgba(0,212,255,0.12); }}
.top3-number {{ font-size: 3.5em; font-weight: 900; color: rgba(0,212,255,0.12); position: absolute; top: 12px; right: 20px; line-height: 1; }}
.top3-title {{ color: #fff; font-size: 1.15em; font-weight: 700; margin-bottom: 12px; line-height: 1.4; }}
.top3-meta {{ font-size: 0.82em; color: #666; margin-bottom: 12px; }}
.top3-summary {{ color: #aaa; font-size: 0.9em; line-height: 1.6; }}
.top3-link {{ display: inline-block; margin-top: 14px; color: #00d4ff; font-size: 0.85em; text-decoration: none; }}
.top3-link:hover {{ text-decoration: underline; }}

/* Category section */
.categories-section {{ margin-bottom: 50px; }}
.cat-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; }}
.cat-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 20px; transition: all 0.25s; }}
.cat-card:hover {{ border-color: rgba(0,212,255,0.25); transform: translateY(-2px); }}
.cat-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }}
.cat-icon {{ font-size: 1.4em; }}
.cat-name {{ color: #e8e8f0; font-size: 0.95em; font-weight: 600; }}
.cat-count {{ background: rgba(0,212,255,0.15); color: #00d4ff; border-radius: 10px; padding: 1px 8px; font-size: 0.75em; margin-left: auto; }}
.cat-preview {{ color: #888; font-size: 0.82em; line-height: 1.5; margin-top: 6px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }}

/* News list */
.news-section {{ margin-bottom: 50px; }}
.news-group {{ margin-bottom: 40px; }}
.news-group-header {{ display: flex; align-items: center; gap: 10px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 20px; }}
.news-group-icon {{ font-size: 1.2em; }}
.news-group-name {{ color: #e8e8f0; font-size: 1.1em; font-weight: 700; }}
.news-list {{ display: flex; flex-direction: column; gap: 16px; }}
.news-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 20px; transition: all 0.25s; }}
.news-card:hover {{ border-color: rgba(0,212,255,0.2); background: rgba(255,255,255,0.04); }}
.news-title-row {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 8px; }}
.news-title {{ color: #fff; font-size: 1.02em; font-weight: 600; line-height: 1.4; flex: 1; }}
.news-title a {{ color: inherit; text-decoration: none; }}
.news-title a:hover {{ color: #00d4ff; }}
.news-cat-badge {{ background: rgba(0,255,136,0.08); color: #00ff88; border: 1px solid rgba(0,255,136,0.2); border-radius: 6px; padding: 2px 8px; font-size: 0.72em; white-space: nowrap; flex-shrink: 0; }}
.news-meta {{ font-size: 0.78em; color: #666; margin-bottom: 10px; }}
.news-meta a {{ color: #00d4ff; text-decoration: none; }}
.news-meta a:hover {{ text-decoration: underline; }}
.news-summary {{ color: #aaa; font-size: 0.9em; line-height: 1.65; margin-bottom: 12px; }}
.news-why {{ background: rgba(0,255,136,0.05); border-left: 3px solid #00ff88; padding: 10px 14px; border-radius: 0 8px 8px 0; margin-bottom: 12px; }}
.news-why-label {{ color: #00ff88; font-size: 0.78em; font-weight: 700; margin-bottom: 4px; }}
.news-why-text {{ color: #bbb; font-size: 0.85em; line-height: 1.5; }}
.news-footer {{ display: flex; flex-wrap: wrap; gap: 12px; font-size: 0.8em; }}
.news-entities {{ color: #888; flex: 1; min-width: 200px; }}
.news-entities span {{ color: #00d4ff; }}
.news-stocks {{ color: #888; }}
.news-stocks span {{ background: rgba(0,212,255,0.1); color: #00d4ff; padding: 1px 6px; border-radius: 4px; margin-left: 4px; }}

/* Keywords */
.keywords-section {{ margin-bottom: 50px; }}
.keywords-cloud {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.kw {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 6px 14px; font-size: 0.85em; color: #aaa; transition: all 0.2s; cursor: default; }}
.kw:hover {{ border-color: rgba(0,212,255,0.4); color: #00d4ff; background: rgba(0,212,255,0.06); }}

/* Tomorrow */
.tomorrow-section {{ background: rgba(0,255,136,0.04); border: 1px solid rgba(0,255,136,0.15); border-radius: 16px; padding: 28px; margin-bottom: 50px; }}
.tomorrow-label {{ color: #00ff88; font-size: 0.82em; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; }}
.tomorrow-title {{ color: #e8e8f0; font-size: 1.1em; font-weight: 600; margin-bottom: 12px; }}
.tomorrow-items {{ list-style: none; padding: 0; }}
.tomorrow-items li {{ padding: 6px 0; padding-left: 20px; position: relative; color: #aaa; font-size: 0.9em; }}
.tomorrow-items li::before {{ content: "▸"; position: absolute; left: 0; color: #00ff88; }}

footer {{ text-align: center; color: #555; font-size: 0.85em; padding: 30px 0; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 40px; }}
footer a {{ color: #00d4ff; text-decoration: none; }}
footer a:hover {{ text-decoration: underline; }}
@media (max-width: 768px) {{
  h1 {{ font-size: 1.8em; }}
  .top3-grid {{ grid-template-columns: 1fr; }}
  .cat-grid {{ grid-template-columns: 1fr 1fr; }}
}}
@media (max-width: 480px) {{
  .cat-grid {{ grid-template-columns: 1fr; }}
  body {{ padding: 14px; }}
}}
</style>
</head>
<body>
<div class="container">
<a href="index.html" class="back-link">← 返回首頁</a>

<header>
  <div class="header-date">{report_date}｜TechCrunch AI 新聞精選</div>
  <h1>🤖 每日 AI 新聞中文摘要</h1>
  <div class="header-stats">
    <span class="stat-badge">📰 {len(news_items)} 則新聞</span>
    <span class="stat-badge">📂 {len([c for c in categories.values() if c['items']])} 個分類</span>
    <span class="stat-badge">🕐 過去 24 小時</span>
  </div>
</header>

<!-- 三大頭條 -->
<section class="top3-section">
  <div class="section-label">📌 今日三大頭條</div>
  <div class="top3-grid">
"""

for i, item in enumerate(top3):
    html += f"""
    <div class="top3-card">
      <div class="top3-number">#{i+1}</div>
      <div class="top3-title">{item['title_tw']}</div>
      <div class="top3-meta">{item['pubDate_tw']} · <a href="{item['url']}" target="_blank" style="color:#00d4ff;text-decoration:none">{item['source']} 原文 →</a></div>
      <div class="top3-summary">{item['summary'][:200]}…</div>
      <a href="{item['url']}" target="_blank" class="top3-link">閱讀全文 →</a>
    </div>"""

html += """
  </div>
</section>

<!-- 主題雷達 -->
<section class="categories-section">
  <div class="section-label">📊 主題雷達</div>
  <div class="cat-grid">
"""

active_cats = [(k, v) for k, v in categories.items() if v['items']]
for k, v in active_cats:
    preview = v['items'][0]['title_tw'][:40] + "…" if v['items'] else ""
    html += f"""
    <div class="cat-card">
      <div class="cat-header">
        <span class="cat-icon">{v['icon']}</span>
        <span class="cat-name">{v['name']}</span>
        <span class="cat-count">{len(v['items'])} 則</span>
      </div>
      <div class="cat-preview">{preview}</div>
    </div>"""

html += """
  </div>
</section>

<!-- 完整新聞清單 -->
<section class="news-section">
  <div class="section-label">📋 完整新聞</div>
"""

for k, v in active_cats:
    html += f"""
  <div class="news-group">
    <div class="news-group-header">
      <span class="news-group-icon">{v['icon']}</span>
      <span class="news-group-name">{v['name']}</span>
    </div>
    <div class="news-list">
"""
    for item in v['items']:
        html += f"""
      <div class="news-card">
        <div class="news-title-row">
          <div class="news-title"><a href="{item['url']}" target="_blank">{item['title_tw']}</a></div>
          <span class="news-cat-badge">{item['category']}</span>
        </div>
        <div class="news-meta">
          <a href="{item['url']}" target="_blank">{item['source']}</a> · {item['pubDate_tw']}
        </div>
        <div class="news-summary">{item['summary']}</div>
        <div class="news-why">
          <div class="news-why-label">為什麼重要</div>
          <div class="news-why-text">{item['why_important']}</div>
        </div>
        <div class="news-footer">
          <div class="news-entities">關鍵實體：<span>{item['entities']}</span></div>
        </div>
        {"<div class=\"news-stocks\">概念股：" + " ".join([f"<span>{s}</span>" for s in item['stocks'].split(",")]) + "</div>" if item['stocks'] else ""}
      </div>"""
    html += "</div></div>"

html += """
</section>

<!-- 今日關鍵詞 -->
<section class="keywords-section">
  <div class="section-label">🔑 今日關鍵詞</div>
  <div class="keywords-cloud">
"""
for kw in keywords:
    html += f'<span class="kw">{kw}</span>'
html += """
  </div>
</section>

<!-- 明日觀察 -->
<section class="tomorrow-section">
  <div class="tomorrow-label">🔮 明日觀察</div>
  <div class="tomorrow-title">基於今日新聞，明日可能延伸的報導方向</div>
  <ul class="tomorrow-items">
    <li><strong>OpenAI IPO 進度：</strong>Apple 訴訟文件可能進一步披露，監管機構態度和 IPO 時程表是否調整</li>
    <li><strong>Kimi K3 發布動態：</strong>若正式發布，將有第一手效能評測出爐，與 Opus 4.8 的 Benchmark 對比將成焦點</li>
    <li><strong>印度手機市場：</strong>記憶體價格壓力是否迫使更多中國品牌撤出或重組當地業務</li>
    <li><strong>Deepfake 監管：</strong>Apple 與 Google 回應舊金山市府的 28 天期限將至，是否有更多州跟進</li>
    <li><strong>AI 基礎設施：</strong>$4 億推理晶片貸款的後續，是否有更多資本跟進開源推論市場</li>
    <li><strong>Databricks 動向：</strong>新一輪募資細節（30 億美元）以及 GLM 5.2 編碼基準的後續討論</li>
  </ul>
</section>

<footer>
  <p>📡 資料來源：<a href="https://techcrunch.com/category/artificial-intelligence/" target="_blank">TechCrunch AI</a>｜每日 12:30 自動更新</p>
  <p>⚡ 由 OpenClaw AI 編譯整理｜<a href="https://github.com/acstep/TECH" target="_blank">GitHub Repo</a></p>
</footer>
</div>
</body>
</html>
"""

with open(f"/home/matt/.openclaw/workspace/TECH/news/{today}.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {today}.html with {len(news_items)} news items in {len(active_cats)} categories")
