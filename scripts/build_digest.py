"""
Builds digest.json for the Chronoscope public site from free, public RSS
news feeds — no API keys, no paid services. Runs inside GitHub Actions.
"""
import datetime
import html
import json
import random
import re

import feedparser

# Each source: (feed url, fallback display name, category, how many stories to take)
# categories must be one of: world, politics, war, economy, science, culture, disaster
SOURCES = [
    ("http://feeds.bbci.co.uk/news/world/rss.xml", "BBC News", "world", 4),
    ("https://www.aljazeera.com/xml/rss/all.xml", "Al Jazeera", "world", 4),
    ("https://feeds.npr.org/1004/rss.xml", "NPR", "world", 3),
    ("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en", "Google News (India)", "politics", 3),
    ("https://news.google.com/rss?hl=en&gl=KR&ceid=KR:en", "Google News (Korea)", "politics", 3),
    ("https://news.google.com/rss?hl=en-NG&gl=NG&ceid=NG:en", "Google News (Africa)", "world", 3),
    ("https://news.google.com/rss?hl=en&gl=BR&ceid=BR:en", "Google News (Latin America)", "world", 3),
    ("https://news.google.com/rss?hl=en&gl=SG&ceid=SG:en", "Google News (Asia)", "world", 3),
    ("https://news.google.com/rss?hl=en&gl=AE&ceid=AE:en", "Google News (Middle East)", "world", 3),
    ("https://news.google.com/rss?hl=en&gl=DE&ceid=DE:en", "Google News (Europe)", "world", 3),
    ("http://feeds.bbci.co.uk/news/business/rss.xml", "BBC Business", "economy", 3),
    ("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "BBC Science", "science", 2),
    ("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml", "BBC Culture", "culture", 2),
]

MAX_ITEMS = 30

# Google News titles arrive as "Headline text - Outlet Name" and their
# "summary" field is a jumbled multi-outlet "full coverage" cluster, not a
# real sentence — so we handle google feeds differently from real ones.
GOOGLE_NEWS_HOST = "news.google.com"


def clean_text(raw, limit=220):
    if not raw:
        return ""
    text = html.unescape(raw)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + "\u2026"
    return text


def split_google_title(title):
    """Google News titles end with ' - Outlet Name'; pull that apart."""
    match = re.match(r"^(.*) - ([^-]{2,40})$", title)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return title, None


def fetch_source(url, fallback_name, category, count):
    items = []
    is_google = GOOGLE_NEWS_HOST in url
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[: count * 2]:  # look at a few extra in case some are skipped
            raw_title = clean_text(entry.get("title", ""), limit=200)
            if not raw_title:
                continue

            source_name = fallback_name
            if is_google:
                title, outlet = split_google_title(raw_title)
                # feedparser exposes the per-item <source> tag as entry.source
                real_outlet = None
                src = entry.get("source")
                if isinstance(src, dict):
                    real_outlet = src.get("title")
                source_name = real_outlet or outlet or fallback_name
                summary = title  # google's own "summary" is a jumbled link cluster, unusable as prose
            else:
                title = raw_title
                summary = clean_text(entry.get("summary", "") or entry.get("description", ""))
                if not summary:
                    summary = title

            title = title[:140]
            link = entry.get("link", "") or url

            items.append(
                {
                    "title": title,
                    "summary": summary,
                    "category": category,
                    "sourceName": source_name,
                    "sourceUrl": link,
                }
            )
            if len(items) >= count:
                break
    except Exception as exc:  # noqa: BLE001 - a flaky feed should never break the whole run
        print(f"skipping {fallback_name}: {exc}")
    return items


def main():
    items = []
    for url, name, category, count in SOURCES:
        items.extend(fetch_source(url, name, category, count))

    random.shuffle(items)
    items = items[:MAX_ITEMS]

    now = datetime.datetime.now(datetime.timezone.utc)
    data = {
        "generatedAt": now.isoformat(),
        "dateLabel": now.strftime("%B %-d, %Y") if hasattr(now, "strftime") else str(now.date()),
        "items": items,
    }

    with open("digest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"wrote digest.json with {len(items)} items")


if __name__ == "__main__":
    main()
