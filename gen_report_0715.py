#!/usr/bin/env python3
import json
import sys

with open('/tmp/tc_news_full.json') as f:
    articles = json.load(f)

# Filter to July 10-15 only
filtered = []
for a in articles:
    t = a.get('time', '')
    if '/2026-07-1' in t:
        day = int(t.split('-')[2][:2])
        if day >= 10:
            filtered.append(a)

print(f"Filtered articles (July 10-15): {len(filtered)}")

# Categories
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

for a in filtered:
    t = a['title']
    content = a.get('content', '') + t
    
    if any(x in content.lower() for x in ['nvidia', 'gpu', 'chip', 'amd', 'intel', 't smc', 'hbm', 'data center construction', 'server hardware']):
        categories["💾 AI 晶片與硬體"].append(a)
    elif any(x in content.lower() for x in ['model', 'gpt', 'claude', 'gemini', 'llm', 'openai launch', 'anthropic', 'research', 'paper', 'benchmark']):
        if any(x in t.lower() for x in ['model', 'delete files', 'codex', 'flagship', 'new ai']):
            categories["🧠 AI 模型與研究"].append(a)
        elif 'siri' in t.lower() or 'instagram' in t.lower() or 'spotify' in t.lower() or 'waze' in t.lower() or 'google images' in t.lower() or 'chatgpt for' in t.lower() or 'deezer' in t.lower() or 'slackbot' in t.lower() or 'ai mode' in t.lower() or 'superhuman' in t.lower():
            categories["🤖 AI 產品與應用"].append(a)
        elif any(x in t.lower() for x in ['apple sue', 'trade secret', 'lawsuit', 'regulation', 'standards body', 'new york state', 'halt construction']):
            categories["🏛️ AI 政策與監管"].append(a)
        elif any(x in t.lower() for x in ['deepmind ceo', 'ceo call']):
            categories["🏛️ AI 政策與監管"].append(a)
        elif any(x in t.lower() for x in ['layoff', 'founder of hinge', 'miles wang', 'nous research', 'pixverse', 'deepseek', 'converge bio', 'im8', 'hermes']):
            categories["💰 AI 投融資與併購"].append(a)
        else:
            categories["🏢 企業 AI 動態"].append(a)
    elif any(x in t.lower() for x in ['apple sue openai', 'trade secret', 'deepmind ceo calls', 'new york state halts', 'lawsuit', 'nadella warning', 'regulation', 'standards body']):
        categories["🏛️ AI 政策與監管"].append(a)
    elif any(x in t.lower() for x in ['layoff', 'layoffs', 'founder of hinge', 'miles wang', 'nous research', 'pixverse', 'deepseek', 'converge bio', 'im8', 'hermes', 'funding', 'valuation', 'raises', ' SERIES']):
        categories["💰 AI 投融資與併購"].append(a)
    elif any(x in t.lower() for x in ['siri', 'instagram', 'spotify', 'waze', 'google images', 'chatgpt for', 'deezer', 'slackbot', 'ai mode', 'superhuman', 'slackbot', 'dating', 'overtone']):
        categories["🤖 AI 產品與應用"].append(a)
    elif any(x in t.lower() for x in ['nvidia', 'gpu', 'chip', 'amd', 't smc', 'hbm', 'data center', 'server']):
        categories["💾 AI 晶片與硬體"].append(a)
    else:
        categories["🏢 企業 AI 動態"].append(a)

# Manual corrections
# Move specific articles
def move_article(art_list, from_cat, to_cat):
    if art_list and art in art_list:
        categories[from_cat].remove(art)
        categories[to_cat].append(art)

# Fix misplaced articles
for a in filtered:
    t = a['title']
    # DeepMind CEO -> policy
    if 'DeepMind CEO' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Apple opens Siri AI -> product
    elif 'Apple opens its new Siri AI' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # New York State data centers -> hardware/policy
    elif 'New York State halts' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💾 AI 晶片與硬體"].append(a)
    # Google Images redesign -> product
    elif 'Google Images gets' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Spotify AI -> product
    elif 'Spotify expands' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Superhuman -> product
    elif 'Superhuman' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Satya warning -> policy
    elif 'Satya Nadella' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # OpenAI Codex -> product
    elif 'codex' in t.lower() and 'phone' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # OpenAI families -> product
    elif 'OpenAI bets on families' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Anthropic Claude pricing India -> product
    elif 'Anthropic starts localizing' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Waze AI -> product
    elif 'Waze adds' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Hermes -> funding
    elif 'Hermes agent maker' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Nous Research -> funding
    elif 'Nous Research' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # PixVerse -> funding
    elif 'PixVerse' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # DeepSeek -> funding
    elif 'DeepSeek' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # IM8 -> funding
    elif 'IM8' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Converge Bio -> funding
    elif 'Converge Bio' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Miles Wang -> funding
    elif 'Miles Wang' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Hinge/Overtone -> funding
    elif 'Overtone' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Stalking victim -> policy
    elif 'Stalking victim' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Wildest allegations Apple -> policy
    elif 'wildest allegations' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # OpenAI pushes back lawsuit -> policy
    elif 'OpenAI pushes back' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Apple sues OpenAI -> policy
    elif 'Apple sues OpenAI' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Google faces lawsuit -> policy
    elif 'Google faces another' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Uber lobbying -> enterprise
    elif 'Uber' in t and ('robotaxi' in t.lower() or 'lobbying' in t.lower()):
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Real AI race -> enterprise
    elif 'real AI race' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Robotaxi -> enterprise
    elif 'robotaxi' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Last wave of tech winners -> enterprise
    elif 'last wave of tech winners' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Slackbot -> product
    elif 'Slackbot' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Meta AI Mode -> product
    elif 'AI Mode' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Anthropic ad -> product
    elif "Anthropic's newest ad" in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Meta removes Instagram -> product
    elif 'Meta removes' in t and 'Instagram' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Telegram -> enterprise
    elif 'Telegram' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Lorde AI glasses -> product
    elif 'Lorde' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # SpaceX -> enterprise
    elif 'SpaceX' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # AI layoff wave -> enterprise
    elif 'AI layoff wave' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Should AI help -> policy
    elif 'Should AI help' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # HumanX conference -> enterprise
    elif 'HumanX' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # OpenAI hardware speaker -> product
    elif 'first hardware device' in t.lower() or 'screenless speaker' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # OpenAI new flagship model deletes -> model
    elif 'flagship model deletes' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🧠 AI 模型與研究"].append(a)
    # OpenAI ChatGPT personal finance -> product
    elif 'ChatGPT for personal finance' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # OpenAI Codex phone -> product
    elif 'codex' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Apple ex-employee bug -> enterprise
    elif 'former employee' in t.lower() and 'bug' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Fizz VC -> policy (confidential info)
    elif 'Fizz accuses' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏛️ AI 政策與監管"].append(a)
    # Peacock AI video -> product
    elif 'Peacock expands' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Netflix AI startup -> funding
    elif 'Netflix' in t and 'AI startup' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["💰 AI 投融資與併購"].append(a)
    # Deezer AI music -> product
    elif 'Deezer' in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Spotify best developers -> enterprise
    elif 'Spotify' in t and 'best developers' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # ChatGPT interactive visuals -> product
    elif 'interactive visuals' in t.lower() or 'math and scien' in t.lower():
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🤖 AI 產品與應用"].append(a)
    # Meta Adam Mosseri -> enterprise
    elif "Adam Mosseri" in t:
        for cat in categories:
            if a in categories[cat]:
                categories[cat].remove(a)
        categories["🏢 企業 AI 動態"].append(a)
    # Stalking victim OpenAI -> policy
    # Already covered above

# Show categories
for cat, arts in categories.items():
    print(f"  {cat}: {len(arts)} articles")

# Select top 3 headlines
top3_candidates = [a for a in filtered if a['title'] in [
    "Apple sues OpenAI over alleged trade secret theft",
    "OpenAI pushes back on Apple trade secret lawsuit",
    "The wildest allegations in Apple's trade secrets lawsuit against OpenAI",
    "OpenAI's new flagship model deletes files on its own, people keep warning",
    "DeepMind CEO calls for an independent standards body to regulate frontier AI",
    "Apple opens its new Siri AI to everyone with the iOS 27 public beta",
    "Video-generation startup PixVerse raises $439M, valuation soars past $2B",
    "DeepSeek reportedly in talks to raise $1.5B, then IPO",
    "New York State halts construction of all new data centers",
    "Meta removes controversial AI feature on Instagram after backlash",
    "Satya Nadella has issued a shocking warning to companies using AI",
    "Hermes agent maker Nous Research in talks for new funding at $1.5B valuation",
    "The real AI race may no longer be at the frontier",
]]

# Fallback top 3
if len(top3_candidates) < 3:
    top3_candidates = filtered[:3]

top3 = [(a['title'], a.get('link', '')) for a in top3_candidates[:3]]
print(f"\nTop 3: {[t for t,_ in top3]}")

sys.exit(0)
