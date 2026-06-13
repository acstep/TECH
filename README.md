# TECH — 每日 AI 新聞中文整理

每日自動整理 TechCrunch AI 新聞，繁體中文摘要。  
由 OpenClaw cron 每天 12:30 台北時間自動更新。

## 版本

| 版本 | 部署 | URL |
|------|------|-----|
| 靜態 HTML | GitHub Pages | https://acstep.github.io/TECH/ |
| 互動式 (Streamlit) | 本機 / Streamlit Cloud | http://192.168.1.64:18790（LAN）|

## 本地跑（已建立 systemd service）

```bash
# service 在 /home/matt/.config/systemd/user/tech-streamlit.service
systemctl --user start tech-streamlit
systemctl --user status tech-streamlit
# 訪問 http://localhost:18790
```

## 部署到 share.streamlit.io

1. 確認此 repo 已 push 到 GitHub（已完成）
2. 前往 https://share.streamlit.io
3. 用 GitHub 帳號登入
4. 點 "New app"
5. 選 `acstep/TECH` repo，main branch，main file = `app.py`
6. Deploy！3 分鐘後拿到 `https://acstep-tech.streamlit.app` 永久網址

## 部署到 Hugging Face Spaces

1. `huggingface-cli login`（需要 token）
2. `huggingface-cli repo create tech-news --type space --space_sdk streamlit`
3. `git push https://huggingface.co/spaces/acstep/tech-news main`

## 檔案結構

```
TECH/
├── app.py            # Streamlit 主程式
├── requirements.txt  # Python 套件
├── .streamlit/
│   └── config.toml   # Streamlit 設定（深色主題）
├── index.html        # 靜態首頁（GitHub Pages 用）
├── news/
│   └── YYYY-MM-DD.html  # 每日新聞
└── README.md
```

## 資料來源
- TechCrunch（每日自動抓取 + 摘要）
- AI 整理 + 翻譯
