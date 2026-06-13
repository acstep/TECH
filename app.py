#!/usr/bin/env python3
"""
AI 雙驅動站 — 統一入口
- 📰 TECH：每日 AI 新聞中文整理（TechCrunch 自動摘要）
- 📊 AI 股票：AI 基礎建設美股研究報告（嵌入 stock-reports GitHub Pages）
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
    initial_sidebar_state="expanded",
)

TECH_DIR = Path(__file__).parent
NEWS_DIR = TECH_DIR / "news"
INDEX_HTML = TECH_DIR / "index.html"
STOCK_REPORTS_URL = "https://acstep.github.io/stock-reports/"

# ---- 自訂 CSS（深色主題）----
st.markdown("""
<style>
.stApp { background: #080810; }
[data-testid="stSidebar"] { background: #0a0a18; }
[data-testid="stHeader"] { background: rgba(8,8,16,0.7); backdrop-filter: blur(10px); }
h1, h2, h3, h4 { color: #e8e8f0 !important; }

.hero {
    text-align: center;
    padding: 40px 20px 20px;
    background: linear-gradient(135deg, #00d4ff 0%, #a855f7 50%, #00ff88 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}
.hero h1 { font-size: 2.8em; font-weight: 900; margin: 0; letter-spacing: -1px; }
.hero p { color: #888; margin: 8px 0 0; font-size: 1.1em; }

.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 16px;
    padding: 36px 24px;
    margin-bottom: 20px;
    text-align: center;
    min-height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.3s;
}
.card-tech { border-color: rgba(0, 212, 255, 0.3); }
.card-tech:hover { border-color: #00d4ff; box-shadow: 0 8px 24px rgba(0,212,255,0.2); }
.card-stock { border-color: rgba(168, 85, 247, 0.3); }
.card-stock:hover { border-color: #a855f7; box-shadow: 0 8px 24px rgba(168,85,247,0.2); }

.card-icon { font-size: 3.5em; margin-bottom: 12px; }
.card-title { color: #fff; font-size: 1.4em; font-weight: 700; margin-bottom: 8px; }
.card-desc { color: #aaa; font-size: 0.95em; line-height: 1.5; }

.stButton button {
    background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
    color: #080810;
    font-weight: 700;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
}
.stButton button:hover {
    background: linear-gradient(135deg, #00ff88 0%, #00d4ff 100%);
    transform: translateY(-1px);
}

[data-testid="stMetricValue"] { color: #00d4ff; }
.nav-radio label { color: #e8e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ---- Session state 預設 ----
if "section" not in st.session_state:
    st.session_state.section = "home"

# ---- 側邊欄導航 ----
with st.sidebar:
    st.markdown("### 🚀 AI 雙驅動站")
    st.caption("每日自動更新")
    st.markdown("---")

    if st.button("🏠 首頁", use_container_width=True):
        st.session_state.section = "home"
        st.rerun()
    if st.button("📰 TECH 新聞", use_container_width=True):
        st.session_state.section = "tech"
        st.rerun()
    if st.button("📊 AI 股票", use_container_width=True):
        st.session_state.section = "stock"
        st.rerun()
    st.markdown("---")
    st.markdown("### 📅 TECH 日期")
    if (INDEX_HTML).exists():
        soup = BeautifulSoup(INDEX_HTML.read_text(encoding="utf-8"), "lxml")
        dates = []
        for card in soup.select("a.report-card"):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", card.get("href", ""))
            if m:
                dates.append(m.group(1))
        if dates:
            st.metric("歷史日報", len(dates))
            st.metric("最新", dates[0])
    st.markdown("---")
    st.caption("""
    📡 來源：TechCrunch / Yahoo Finance  
    🌐 主站：[acstep.github.io/TECH](https://acstep.github.io/TECH/)
    """)


# ===========================================================
# 載入資料函式（caching）
# ===========================================================
@st.cache_data(ttl=300)
def load_news_index():
    if not INDEX_HTML.exists():
        return []
    soup = BeautifulSoup(INDEX_HTML.read_text(encoding="utf-8"), "lxml")
    items = []
    for card in soup.select("a.report-card"):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", card.get("href", ""))
        date = m.group(1) if m else ""
        title_el = card.select_one(".report-title")
        summary_el = card.select_one(".report-summary")
        date_el = card.select_one(".report-date")
        items.append({
            "date": date,
            "title": title_el.get_text(strip=True) if title_el else "",
            "summary": summary_el.get_text(strip=True) if summary_el else "",
            "date_label": date_el.get_text(strip=True) if date_el else date,
        })
    return items


@st.cache_data(ttl=300)
def load_news_detail(date_str):
    fpath = NEWS_DIR / f"{date_str}.html"
    if not fpath.exists():
        return None
    return fpath.read_text(encoding="utf-8")


# ===========================================================
# 視圖 1：首頁
# ===========================================================
if st.session_state.section == "home":
    st.markdown("""
    <div class="hero">
        <h1>🚀 AI 雙驅動站</h1>
        <p>每日 AI 新聞 × AI 基建選股 · 全自動更新</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")  # 間距

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card card-tech">
            <div class="card-icon">📰</div>
            <div class="card-title">TECH 新聞</div>
            <div class="card-desc">
                每日 AI 新聞中文整理<br>
                TechCrunch 自動摘要<br>
                11 大主題追蹤 + 個股情報
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📰 進入 TECH 新聞", key="btn_tech", use_container_width=True):
            st.session_state.section = "tech"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card card-stock">
            <div class="card-icon">📊</div>
            <div class="card-title">AI 股票研究</div>
            <div class="card-desc">
                AI 基礎建設美股研究<br>
                每日精選 50+ 檔<br>
                完整進出場價 + 深度分析
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 進入 AI 股票", key="btn_stock", use_container_width=True):
            st.session_state.section = "stock"
            st.rerun()

    st.markdown("---")

    # 快速統計
    news_index = load_news_index()
    n1, n2, n3 = st.columns(3)
    with n1:
        st.metric("📰 TECH 日報數", len(news_index))
    with n2:
        if news_index:
            st.metric("📅 最新日報", news_index[0]["date"])
    with n3:
        st.metric("🤖 更新頻率", "每日 12:30")

    st.caption("👉 從上方選單或首頁卡片選擇想看的服務")


# ===========================================================
# 視圖 2：TECH 新聞
# ===========================================================
elif st.session_state.section == "tech":
    st.markdown("""
    <div class="hero">
        <h1>📰 TECH 每日 AI 新聞</h1>
        <p>TechCrunch 自動摘要 · 繁體中文整理</p>
    </div>
    """, unsafe_allow_html=True)

    news_index = load_news_index()

    if not news_index:
        st.warning("找不到新聞")
    else:
        dates = [item["date"] for item in news_index if item["date"]]
        selected = st.selectbox(
            "📅 選擇日期",
            options=dates,
            index=0,
            format_func=lambda d: next(
                (f"{d}  {it['title'][:50]}" for it in news_index if it["date"] == d),
                d,
            ),
        )

        if selected:
            meta = next((it for it in news_index if it["date"] == selected), None)
            if meta:
                st.markdown(f"### {meta['title']}")
                st.caption(f"📅 {meta['date_label']}")
                if meta.get("summary"):
                    st.markdown(f"*{meta['summary']}*")

            html_content = load_news_detail(selected)
            if html_content:
                st.components.v1.html(html_content, height=1800, scrolling=True)
            else:
                st.error(f"找不到 {selected}.html")


# ===========================================================
# 視圖 3：AI 股票（嵌入 stock-reports GitHub Pages）
# ===========================================================
elif st.session_state.section == "stock":
    st.markdown("""
    <div class="hero">
        <h1>📊 AI 股票研究</h1>
        <p>AI 基礎建設美股每日研究報告</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("💡 嵌入自 [acstep.github.io/stock-reports](https://acstep.github.io/stock-reports/) · 每日 12:00 自動更新")

    # 嵌入 stock-reports
    st.components.v1.html(
        f"""
        <iframe
            src="{STOCK_REPORTS_URL}"
            width="100%"
            height="2400"
            frameborder="0"
            style="border-radius: 12px; background: #080810;"
            loading="lazy"
        ></iframe>
        """,
        height=2450,
        scrolling=False,
    )

    st.markdown("---")
    st.caption("👆 完整功能請在 [stock-reports 主站](https://acstep.github.io/stock-reports/) 瀏覽")


# ---- 頁尾 ----
st.markdown("---")
st.caption("""
🚀 AI 雙驅動站 · 自動部署於 [share.streamlit.io](https://share.streamlit.io)  
📡 資料來源：TechCrunch（每日自動摘要）· Yahoo Finance（即時報價）· Barchart（技術信號）
""")
