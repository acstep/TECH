#!/usr/bin/env python3
"""
AI 雙驅動站 — 純導航 Hub
- 📰 TECH：跳轉到 https://acstep.github.io/TECH/
- 📊 AI 股票：跳轉到 https://acstep.github.io/stock-reports/
不嵌入任何東西，乾淨導向。
"""
import streamlit as st
from bs4 import BeautifulSoup
from pathlib import Path
import re

# ---- 設定 ----
st.set_page_config(
    page_title="AI 雙驅動站",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

TECH_DIR = Path(__file__).parent
INDEX_HTML = TECH_DIR / "index.html"

URL_TECH = "https://acstep.github.io/TECH/"
URL_STOCK = "https://acstep.github.io/stock-reports/"

# ---- 自訂 CSS ----
st.markdown("""
<style>
.stApp { background: #080810; }
[data-testid="stHeader"] { background: rgba(8,8,16,0.5); backdrop-filter: blur(10px); }
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding-top: 3rem; max-width: 1100px; }

.hero {
    text-align: center;
    padding: 30px 20px 10px;
    background: linear-gradient(135deg, #00d4ff 0%, #a855f7 50%, #00ff88 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 30px;
}
.hero h1 { font-size: 3.2em; font-weight: 900; margin: 0; letter-spacing: -1px; }
.hero p { color: #888; margin: 10px 0 0; font-size: 1.1em; }

.card {
    background: rgba(255,255,255,0.03);
    border-radius: 20px;
    padding: 40px 32px;
    margin-bottom: 20px;
    text-align: center;
    min-height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}
.card-tech {
    border: 1px solid rgba(0, 212, 255, 0.3);
    background: linear-gradient(135deg, rgba(0,212,255,0.04) 0%, rgba(0,212,255,0.01) 100%);
}
.card-tech:hover {
    border-color: #00d4ff;
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.25);
    transform: translateY(-4px);
}
.card-stock {
    border: 1px solid rgba(168, 85, 247, 0.3);
    background: linear-gradient(135deg, rgba(168,85,247,0.04) 0%, rgba(168,85,247,0.01) 100%);
}
.card-stock:hover {
    border-color: #a855f7;
    box-shadow: 0 12px 40px rgba(168, 85, 247, 0.25);
    transform: translateY(-4px);
}

.card-icon { font-size: 4em; margin-bottom: 16px; }
.card-title { color: #fff; font-size: 1.6em; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.5px; }
.card-desc { color: #aaa; font-size: 1em; line-height: 1.6; margin-bottom: 16px; }
.card-tag {
    display: inline-block;
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
    color: #ccc;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8em;
    margin: 0 4px;
}
.card-tech .card-tag { color: #00d4ff; border-color: rgba(0,212,255,0.3); }
.card-stock .card-tag { color: #a855f7; border-color: rgba(168,85,247,0.3); }

.stLinkButton a {
    background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%) !important;
    color: #080810 !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 14px 24px !important;
    border-radius: 10px !important;
    font-size: 1.05em !important;
    text-decoration: none !important;
    display: block !important;
    text-align: center !important;
    transition: all 0.2s !important;
}
.stLinkButton a:hover {
    background: linear-gradient(135deg, #00ff88 0%, #00d4ff 100%) !important;
    transform: translateY(-2px) !important;
}
.card-stock .stLinkButton a {
    background: linear-gradient(135deg, #a855f7 0%, #00d4ff 100%) !important;
}
.card-stock .stLinkButton a:hover {
    background: linear-gradient(135deg, #00d4ff 0%, #a855f7 100%) !important;
}

[data-testid="stMetricValue"] { color: #00d4ff; }
[data-testid="stMetricLabel"] { color: #888; }

.foot {
    text-align: center;
    color: #555;
    font-size: 0.85em;
    margin-top: 50px;
    padding: 20px;
}
.foot a { color: #00d4ff; text-decoration: none; }
</style>
""", unsafe_allow_html=True)


# ---- 解析 index.html 拿最新日期 ----
def get_latest_date():
    if not INDEX_HTML.exists():
        return None, 0
    try:
        soup = BeautifulSoup(INDEX_HTML.read_text(encoding="utf-8"), "lxml")
        dates = []
        for card in soup.select("a.report-card"):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", card.get("href", ""))
            if m:
                dates.append(m.group(1))
        if dates:
            return dates[0], len(dates)
    except Exception:
        pass
    return None, 0


# ---- 標題 ----
st.markdown("""
<div class="hero">
    <h1>🚀 AI 雙驅動站</h1>
    <p>每日 AI 新聞 × AI 基建選股 · 全自動更新</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# ---- 兩張大卡片 ----
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="card card-tech">
        <div class="card-icon">📰</div>
        <div class="card-title">TECH 新聞</div>
        <div class="card-desc">
            每日 AI 新聞中文整理<br>
            TechCrunch 自動摘要<br>
            11 大主題 + 個股情報
        </div>
        <div>
            <span class="card-tag">每日 12:30</span>
            <span class="card-tag">繁體中文</span>
            <span class="card-tag">GitHub Pages</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📰 開啟 TECH 新聞 →", URL_TECH, use_container_width=True)

with col2:
    st.markdown("""
    <div class="card card-stock">
        <div class="card-icon">📊</div>
        <div class="card-title">AI 股票研究</div>
        <div class="card-desc">
            AI 基礎建設美股每日研究<br>
            精選 50+ 檔 + 深度分析<br>
            完整進出場價 / 主題雷達
        </div>
        <div>
            <span class="card-tag">每日 12:00</span>
            <span class="card-tag">60+ 檔</span>
            <span class="card-tag">11 子板塊</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📊 開啟 AI 股票研究 →", URL_STOCK, use_container_width=True)

st.markdown("")

# ---- 統計快覽 ----
latest_date, total_reports = get_latest_date()
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("📰 TECH 歷史日報", f"{total_reports} 篇" if total_reports else "—")
with m2:
    st.metric("📅 最新更新", latest_date or "—")
with m3:
    st.metric("🤖 自動頻率", "每日兩報")

# ---- 頁尾 ----
st.markdown("""
<div class="foot">
    🚀 部署於 <a href="https://share.streamlit.io" target="_blank">Streamlit Cloud</a> ·
    原始碼 <a href="https://github.com/acstep/TECH" target="_blank">github.com/acstep/TECH</a><br>
    兩個靜態站都會自動跟著 <code>git push</code> 同步更新，無需手動操作
</div>
""", unsafe_allow_html=True)
