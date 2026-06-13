#!/usr/bin/env python3
"""
TECH 每日 AI 新聞 - Streamlit 版
讀取 news/*.html 與 index.html，顯示為互動式新聞瀏覽器
"""
import streamlit as st
from bs4 import BeautifulSoup
from pathlib import Path
import re
from datetime import datetime

# ---- 設定 ----
st.set_page_config(
    page_title="TECH — 每日 AI 新聞中文整理",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 自訂 CSS（移植原本的 #080810 深色主題）
st.markdown("""
<style>
.stApp { background: #080810; }
[data-testid="stSidebar"] { background: #0a0a18; }
h1, h2, h3, h4 { color: #e8e8f0 !important; }
.news-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 14px;
    transition: all 0.2s;
}
.news-card:hover {
    border-color: rgba(0,212,255,0.4);
    transform: translateY(-2px);
}
.news-date { color: #00d4ff; font-size: 0.9em; font-weight: 600; }
.news-title { color: #fff; font-size: 1.15em; font-weight: 700; margin: 6px 0; }
.news-summary { color: #aaa; font-size: 0.92em; line-height: 1.5; }
.hero-header {
    text-align: center;
    padding: 30px 20px 20px;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}
.hero-header h1 { font-size: 2.6em; font-weight: 900; margin: 0; letter-spacing: -1px; }
.hero-header p { color: #888; margin: 4px 0 0; }
.stButton button { background: rgba(0,212,255,0.15); border: 1px solid #00d4ff; color: #00d4ff; }
.stButton button:hover { background: rgba(0,212,255,0.25); border-color: #00ff88; color: #00ff88; }
[data-testid="stMetricValue"] { color: #00d4ff; }
</style>
""", unsafe_allow_html=True)


# ---- 路徑 ----
TECH_DIR = Path(__file__).parent
NEWS_DIR = TECH_DIR / "news"
INDEX_HTML = TECH_DIR / "index.html"


@st.cache_data(ttl=300)
def load_news_index():
    """從 index.html 解析每日新聞清單（日期、標題、摘要、連結）"""
    if not INDEX_HTML.exists():
        return []
    soup = BeautifulSoup(INDEX_HTML.read_text(encoding="utf-8"), "lxml")
    items = []
    for card in soup.select("a.report-card"):
        date_el = card.select_one(".report-date")
        title_el = card.select_one(".report-title")
        summary_el = card.select_one(".report-summary")
        stats_el = card.select_one(".report-stats")
        href = card.get("href", "")
        # 從 href 抽出日期：news/2026-06-13.html
        m = re.search(r"(\d{4}-\d{2}-\d{2})", href)
        date = m.group(1) if m else ""
        items.append({
            "date": date,
            "title": title_el.get_text(strip=True) if title_el else "",
            "summary": summary_el.get_text(strip=True) if summary_el else "",
            "stats": stats_el.get_text(strip=True) if stats_el else "",
            "href": href,
        })
    return items


@st.cache_data(ttl=300)
def load_news_detail(date_str):
    """讀取指定日期的新聞 HTML，解析成結構化資料"""
    fpath = NEWS_DIR / f"{date_str}.html"
    if not fpath.exists():
        return None
    soup = BeautifulSoup(fpath.read_text(encoding="utf-8"), "lxml")
    # 標題
    title = soup.find("h1").get_text(strip=True) if soup.find("h1") else date_str
    # 內文（拿 hero 之後的部分）
    body = soup.find("body")
    if not body:
        return {"title": title, "items": []}
    # 抓所有 .news-item 或 article 區塊
    news_items = []
    for item in body.find_all(["article", "div"], class_=re.compile(r"news|item|card")):
        heading = item.find(["h2", "h3"])
        if heading:
            news_items.append({
                "heading": heading.get_text(strip=True),
                "body": item.get_text("\n", strip=True)[:2000],
            })
    # 簡化版：把所有文字段落抓出來
    paragraphs = []
    for p in body.find_all(["p", "li"]):
        text = p.get_text(strip=True)
        if text and len(text) > 20:
            paragraphs.append(text)
    return {
        "title": title,
        "paragraphs": paragraphs,
        "raw_html": str(body),
    }


# ---- 主介面 ----
st.markdown("""
<div class="hero-header">
    <h1>📰 TECH</h1>
    <p>每日 AI 新聞中文整理 · TechCrunch 自動摘要</p>
</div>
""", unsafe_allow_html=True)

news_index = load_news_index()

# 側邊欄
with st.sidebar:
    st.markdown("### 📅 歷史日報")
    if news_index:
        dates = [item["date"] for item in news_index if item["date"]]
        selected = st.selectbox(
            "選擇日期",
            options=dates,
            format_func=lambda d: f"{d}  {dict(zip(dates, [n['title'][:25] for n in news_index])).get(d, '')}",
        )
    else:
        st.warning("找不到新聞")
        selected = None
    st.markdown("---")
    st.markdown("### 📊 統計")
    st.metric("總日報數", len(news_index))
    if news_index:
        latest = news_index[0]
        st.metric("最新更新", latest["date"])

# 主要內容
if not selected:
    st.info("👈 從側邊欄選擇日期")
elif selected:
    st.markdown(f"## 📅 {selected} AI 新聞日報")
    detail = load_news_detail(selected)
    if not detail:
        st.error(f"找不到 {selected}.html")
    else:
        # 找對應的 index 摘要
        meta = next((n for n in news_index if n["date"] == selected), None)
        if meta:
            st.markdown(f"**{meta['title']}**")
            st.markdown(f"*{meta['summary']}*")
            if meta.get("stats"):
                st.caption(meta["stats"])
        st.markdown("---")
        # 顯示原始 HTML 內容（保留樣式）
        if detail.get("raw_html"):
            st.components.v1.html(detail["raw_html"], height=2000, scrolling=True)
        # 同步顯示純文字版本
        with st.expander("📝 純文字版本"):
            if detail.get("paragraphs"):
                for p in detail["paragraphs"][:50]:
                    st.markdown(f"- {p}")
            else:
                st.write(detail.get("body", "（無內容）"))

# 頁尾
st.markdown("---")
st.caption("""
📡 資料來源：TechCrunch（每日自動摘要） · 🤖 由 AI 整理
🌐 原始 HTML 版本：<https://acstep.github.io/TECH/>
""", unsafe_allow_html=True)
