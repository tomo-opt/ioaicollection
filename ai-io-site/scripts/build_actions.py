from __future__ import annotations

import hashlib
import html as html_stdlib
import json
import os
import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

from lxml import html


ROOT = Path(__file__).resolve().parents[2]
APP_ROOT = ROOT / "ai-io-site"
ORGS_JSON = APP_ROOT / "data" / "orgs.json"
SOURCES_CONFIG = APP_ROOT / "config" / "action-sources.json"
OUT_ACTIONS = APP_ROOT / "data" / "actions.json"
OUT_REVIEW = APP_ROOT / "data" / "review-queue.json"
OUT_SOURCES = APP_ROOT / "data" / "source-registry.json"
OUT_STATUS = APP_ROOT / "data" / "pipeline-status.json"
STATE_JSON = APP_ROOT / "data" / "discovery-state.json"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36"
LOOKBACK_DAYS = int(os.getenv("ACTION_LOOKBACK_DAYS", "180"))
DISCOVERY_BATCH_SIZE = int(os.getenv("DISCOVERY_BATCH_SIZE", "8"))
LOOKBACK_CUTOFF = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)

AI_TERMS = {
    "artificial intelligence",
    "machine learning",
    "generative ai",
    "foundation model",
    "ai",
    "ml",
    "algorithmic",
    "ai governance",
    "responsible ai",
}
ACTION_TERMS = {
    "launch",
    "launched",
    "publish",
    "published",
    "announce",
    "announced",
    "report",
    "summit",
    "forum",
    "conference",
    "training",
    "toolkit",
    "guidance",
    "policy",
    "initiative",
    "partnership",
    "programme",
    "program",
    "workshop",
    "assessment",
    "capacity",
    "framework",
    "call for",
    "resource",
    "curriculum",
    "competency",
    "convention",
    "course",
    "signed",
    "signs",
    "meeting",
    "webinar",
    "paper",
}
STRONG_ACTION_TERMS = {
    "launch",
    "launched",
    "publish",
    "published",
    "announce",
    "announced",
    "report",
    "summit",
    "forum",
    "conference",
    "toolkit",
    "guidance",
    "initiative",
    "partnership",
    "programme",
    "program",
    "workshop",
    "assessment",
    "capacity",
    "framework",
    "call for",
    "curriculum",
    "competency",
    "convention",
    "course",
    "signed",
    "signs",
    "meeting",
    "webinar",
    "paper",
}
REJECT_TERMS = {
    "job",
    "jobs",
    "career",
    "careers",
    "vacancy",
    "vacancies",
    "opening",
    "openings",
    "recruit",
    "recruitment",
}
BAD_DOMAINS = {
    "news.google.com",
    "google.com",
    "bing.com",
}


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text)
    return normalize_ws(text)


def strip_html(text: str) -> str:
    return normalize_ws(re.sub(r"<[^>]+>", " ", html_stdlib.unescape(text or "")))


def short_hash(*parts: str) -> str:
    return hashlib.sha1("||".join(parts).encode("utf-8")).hexdigest()[:16]


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    query = [(k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True) if not k.lower().startswith("utm_")]
    clean = parsed._replace(query=urlencode(query), fragment="")
    return urlunparse(clean)


def domain_of(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def domain_matches(source_url: str, final_url: str) -> bool:
    source_domain = domain_of(source_url)
    final_domain = domain_of(final_url)
    return bool(source_domain and final_domain and (final_domain == source_domain or final_domain.endswith("." + source_domain)))


def term_present(blob: str, term: str) -> bool:
    return bool(re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", blob))


def fetch_url(url: str, timeout: int = 18) -> tuple[str, str]:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=timeout) as resp:
        final_url = resp.geturl()
        body = resp.read().decode("utf-8", "ignore")
    return final_url, body


def fetch_article_snapshot(url: str, timeout: int = 15) -> tuple[str, str, str]:
    try:
        final_url, body = fetch_url(url, timeout=timeout)
    except Exception:
        return url, "", ""
    try:
        root = html.fromstring(body)
        title = normalize_ws(" ".join(root.xpath("//title//text()")))
        meta_desc = normalize_ws("".join(root.xpath('//meta[@name="description"]/@content | //meta[@property="og:description"]/@content')))
        body_text = normalize_ws(" ".join(root.xpath("//p//text()")))[:2400]
        return final_url, title, meta_desc or body_text
    except Exception:
        return final_url, "", ""


def ai_hits(text: str) -> list[str]:
    blob = normalize_text(text)
    return sorted({term for term in AI_TERMS if term_present(blob, term)})


def action_hits(text: str) -> list[str]:
    blob = normalize_text(text)
    return sorted({term for term in ACTION_TERMS if term_present(blob, term)})


def strong_action_hits(text: str) -> list[str]:
    blob = normalize_text(text)
    return sorted({term for term in STRONG_ACTION_TERMS if term_present(blob, term)})


def reject_hits(text: str) -> list[str]:
    blob = normalize_text(text)
    return sorted({term for term in REJECT_TERMS if term_present(blob, term)})


def cleanup_rss_title(title: str, source_label: str) -> str:
    title = normalize_ws(title)
    if source_label:
        pattern = re.compile(rf"\s*[-|–—]\s*{re.escape(source_label)}\s*$", re.IGNORECASE)
        title = pattern.sub("", title).strip()
    return title


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value.replace("Z", "+00:00")
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def keep_recent(date_value: str) -> bool:
    dt = parse_date(date_value)
    if dt is None:
        return True
    return dt >= LOOKBACK_CUTOFF


def build_org_registry(orgs: list[dict]) -> list[dict]:
    registry = []
    for org in orgs:
        registry.append(
            {
                "nameEn": org.get("nameEn", ""),
                "nameZh": org.get("nameZh", ""),
                "acronym": org.get("acronym", ""),
                "officialDomain": domain_of(org.get("officialUrl", "")),
            }
        )
    return registry


def match_org(text: str, url: str, registry: list[dict]) -> dict | None:
    norm_text = normalize_text(text)
    item_domain = domain_of(url)
    best = None
    best_score = 0.0
    best_reasons: list[str] = []

    for org in registry:
        score = 0.0
        reasons: list[str] = []
        name_en = normalize_text(org["nameEn"])
        name_zh = normalize_text(org["nameZh"])
        acronym = normalize_text(org["acronym"])

        if org["officialDomain"] and item_domain == org["officialDomain"]:
            score += 6.0
            reasons.append("official_domain_match")
        if name_en and name_en in norm_text:
            score += 4.0
            reasons.append("name_en_in_text")
        if name_zh and name_zh in norm_text:
            score += 3.0
            reasons.append("name_zh_in_text")
        if acronym and len(acronym) >= 3 and re.search(rf"\b{re.escape(acronym)}\b", norm_text):
            score += 1.5
            reasons.append("acronym_in_text")

        if score > best_score:
            best_score = score
            best = org
            best_reasons = reasons

    if not best or best_score < 1.5:
        return None
    return {
        "nameEn": best["nameEn"],
        "nameZh": best["nameZh"],
        "officialDomain": best["officialDomain"],
        "score": round(best_score, 2),
        "reasons": best_reasons,
    }


def score_item(item: dict, matched_org: dict | None, source: dict) -> tuple[int, list[str]]:
    text = item.get("rawText", "")
    score = 0
    reasons: list[str] = []
    ai = ai_hits(text)
    act = action_hits(text)
    reject = reject_hits(text)

    if source["strategy"] == "structured_html_cards":
        score += 45
        reasons.append("structured_source")
    elif source["kind"] == "trusted_domain_discovery":
        score += 18
        reasons.append("trusted_domain_discovery")
    else:
        score += 10
        reasons.append("open_web_seed_discovery")

    if matched_org:
        score += min(24, int(matched_org["score"] * 4))
        reasons.extend(matched_org["reasons"])

    trust_url = item.get("publisherUrl") or item.get("sourceUrl", "")
    if domain_matches(source.get("url", ""), trust_url):
        score += 16
        reasons.append("official_or_subdomain_match")

    if ai:
        score += 14 if len(ai) >= 2 else 8
        reasons.append("ai_cues:" + ",".join(ai[:3]))
    if act:
        score += 14 if len(act) >= 2 else 8
        reasons.append("action_cues:" + ",".join(act[:3]))
    if reject:
        score -= 18
        reasons.append("reject_terms:" + ",".join(reject[:3]))

    return score, reasons


def review_status_for(item: dict, score: int, source: dict) -> str:
    text = item.get("rawText", "")
    ai = ai_hits(text)
    act = action_hits(text)
    strong_act = strong_action_hits(text)
    reject = reject_hits(text)
    title_blob = normalize_text(item.get("title", ""))

    if reject:
        return "reject"
    if source["strategy"] == "structured_html_cards" and score >= 45:
        return "publish"
    if source["kind"] == "trusted_domain_discovery":
        trust_url = item.get("publisherUrl") or item.get("sourceUrl", "")
        if source.get("id") == "oecd-ai-open-web" and not any(
            term_present(title_blob, marker) for marker in ("oecd", "observatory")
        ):
            return "review" if domain_matches(source.get("url", ""), trust_url) and ai else "reject"
        if domain_matches(source.get("url", ""), trust_url) and ai and strong_act and score >= 38:
            return "publish"
        if domain_matches(source.get("url", ""), trust_url) and ai and score >= 24:
            return "review"
        return "reject"
    if source["strategy"] == "seed_org_news_rotation":
        if item.get("matchedOrg") and ai and act and score >= 34:
            return "review"
        return "reject"
    return "reject"


def parse_un_aihub(source: dict) -> list[dict]:
    final_url, body = fetch_url(source["url"])
    root = html.fromstring(body)
    cards = root.xpath('//*[contains(@class,"activity-card")]')
    out = []
    for card in cards:
        title = normalize_ws(" ".join(card.xpath('.//*[contains(@class,"activity-title")]//text()')))
        summary = normalize_ws(" ".join(card.xpath('.//*[contains(@class,"short-description")]//text()')))
        entity = normalize_ws(" ".join(card.xpath('.//*[contains(@class,"entity")]//text()')))
        regions = [normalize_ws(t) for t in card.xpath('.//*[contains(@class,"region")]//i/text()') if normalize_ws(t)]
        countries = [normalize_ws(t) for t in card.xpath('.//*[contains(@class,"country")]//i/text()') if normalize_ws(t)]
        action_types = [normalize_ws(t) for t in card.xpath('.//*[contains(@class,"a-type-lst")]//i/text()') if normalize_ws(t)]
        text_blob = " ".join([title, summary, entity, " ".join(action_types)])
        out.append(
            {
                "id": "act-" + short_hash(source["id"], title, summary),
                "title": title,
                "summary": summary,
                "sourceUrl": final_url,
                "sourceDomain": domain_of(final_url),
                "sourceName": source["name"],
                "sourceLabelZh": source.get("labelZh", ""),
                "sourceType": source["kind"],
                "sourceOrgLabel": entity,
                "regions": regions,
                "countries": countries,
                "actionType": action_types,
                "publishedAt": "",
                "lastSeenAt": now_iso(),
                "rawText": text_blob,
            }
        )
    return out


def parse_google_news_rss(query: str, source: dict, limit: int = 12) -> list[dict]:
    rss_url = "https://news.google.com/rss/search?" + urlencode(
        {"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"}
    )
    _, body = fetch_url(rss_url)
    root = ET.fromstring(body)
    items = []
    for item in root.findall(".//item")[:limit]:
        raw_title = normalize_ws(item.findtext("title", default=""))
        link = normalize_ws(item.findtext("link", default=""))
        pub = normalize_ws(item.findtext("pubDate", default=""))
        pub_iso = parsedate_to_datetime(pub).astimezone(timezone.utc).isoformat() if pub else ""
        if not keep_recent(pub_iso):
            continue
        source_label = ""
        source_url = ""
        source_el = item.find("source")
        if source_el is not None and source_el.text:
            source_label = normalize_ws(source_el.text)
            source_url = normalize_ws(source_el.attrib.get("url", ""))

        article_title = ""
        article_summary = ""
        final_url = ""
        clean_title = cleanup_rss_title(article_title or raw_title, source_label)
        rss_summary = cleanup_rss_title(strip_html(item.findtext("description", default="")), source_label)
        fallback_url = canonicalize_url(source_url or source.get("url", "") or link)
        public_url = final_url if final_url and domain_of(final_url) not in BAD_DOMAINS else fallback_url
        combined_text = " ".join([clean_title, article_title, article_summary, rss_summary])
        items.append(
            {
                "id": "act-" + short_hash(source["id"], clean_title, public_url or final_url),
                "title": clean_title or raw_title,
                "summary": article_summary or rss_summary,
                "sourceUrl": public_url,
                "sourceDomain": domain_of(public_url),
                "sourceName": source["name"],
                "sourceLabelZh": source.get("labelZh", ""),
                "sourceType": source["kind"],
                "sourceOrgLabel": source_label,
                "publisherUrl": source_url,
                "publisherDomain": domain_of(source_url),
                "resolvedUrl": final_url,
                "discoveryLink": link,
                "regions": [],
                "countries": [],
                "actionType": [],
                "publishedAt": pub_iso,
                "lastSeenAt": now_iso(),
                "rawText": combined_text,
                "discoveryQuery": query,
            }
        )
    return items


def load_state() -> dict:
    return load_json(STATE_JSON, {"orgCursor": 0})


def save_state(state: dict) -> None:
    save_json(STATE_JSON, state)


def seed_org_queries(orgs: list[dict], batch_size: int) -> tuple[list[tuple[dict, str]], dict]:
    eligible = [org for org in orgs if org.get("level") == "organization" and org.get("nameEn")]
    state = load_state()
    cursor = state.get("orgCursor", 0)
    if not eligible:
        return [], state
    picks: list[tuple[dict, str]] = []
    for i in range(batch_size):
        org = eligible[(cursor + i) % len(eligible)]
        query = f'"{org["nameEn"]}" ("artificial intelligence" OR AI OR "machine learning") when:{LOOKBACK_DAYS}d'
        picks.append((org, query))
    state["orgCursor"] = (cursor + batch_size) % len(eligible)
    return picks, state


def human_source_method(source: dict) -> str:
    return source.get("methodZh") or source.get("strategy", "")


def classify_and_partition(items: list[dict], org_registry: list[dict], source: dict) -> tuple[list[dict], list[dict]]:
    publish: list[dict] = []
    review: list[dict] = []

    for item in items:
        matched_org = match_org(item.get("rawText", ""), item.get("sourceUrl", ""), org_registry)
        item["matchedOrg"] = matched_org
        score, reasons = score_item(item, matched_org, source)
        status = review_status_for(item, score, source)
        record = {
            "id": item["id"],
            "title": item["title"],
            "summary": item["summary"],
            "sourceUrl": item["sourceUrl"],
            "sourceDomain": item["sourceDomain"],
            "publisherUrl": item.get("publisherUrl", ""),
            "publisherDomain": item.get("publisherDomain", ""),
            "resolvedUrl": item.get("resolvedUrl", ""),
            "discoveryLink": item.get("discoveryLink", ""),
            "sourceName": item["sourceName"],
            "sourceLabelZh": item.get("sourceLabelZh", ""),
            "sourceType": item["sourceType"],
            "sourceOrg": matched_org["nameEn"] if matched_org else item.get("sourceOrgLabel", ""),
            "sourceOrgLabel": item.get("sourceOrgLabel", ""),
            "orgMatch": matched_org,
            "actionType": item.get("actionType", []),
            "regions": item.get("regions", []),
            "countries": item.get("countries", []),
            "publishedAt": item.get("publishedAt", ""),
            "effectiveDate": item.get("publishedAt") or item.get("lastSeenAt", ""),
            "lastSeenAt": item.get("lastSeenAt", ""),
            "score": score,
            "scoreReasons": reasons,
            "reviewStatus": status,
            "discoveryQuery": item.get("discoveryQuery", ""),
        }
        if status == "publish":
            publish.append(record)
        elif status == "review":
            review.append(record)
    return publish, review


def dedupe(records: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for record in sorted(records, key=lambda x: x.get("effectiveDate", ""), reverse=True):
        key = (canonicalize_url(record.get("sourceUrl", "")), normalize_text(record.get("title", "")))
        if key in seen:
            continue
        seen.add(key)
        out.append(record)
    return out


def main() -> int:
    orgs = load_json(ORGS_JSON, [])
    sources = load_json(SOURCES_CONFIG, [])
    org_registry = build_org_registry(orgs)

    published: list[dict] = []
    review_queue: list[dict] = []
    source_runs: list[dict] = []

    for source in sources:
        if not source.get("enabled"):
            source_runs.append({**source, "lastRunAt": now_iso(), "lastResult": "disabled", "publishedCount": 0, "reviewCount": 0})
            continue

        try:
            if source["strategy"] == "structured_html_cards":
                items = parse_un_aihub(source)
                pub, rev = classify_and_partition(items, org_registry, source)
            elif source["strategy"] == "google_news_query":
                items = parse_google_news_rss(source["query"], source, limit=8)
                pub, rev = classify_and_partition(items, org_registry, source)
            elif source["strategy"] == "seed_org_news_rotation":
                queries, state = seed_org_queries(orgs, DISCOVERY_BATCH_SIZE)
                pub, rev = [], []
                for org, query in queries:
                    scoped = {**source, "name": f'{source["name"]}: {org["nameEn"]}', "labelZh": source.get("labelZh", "")}
                    items = parse_google_news_rss(query, scoped, limit=4)
                    sub_pub, sub_rev = classify_and_partition(items, org_registry, scoped)
                    pub.extend(sub_pub)
                    rev.extend(sub_rev)
                save_state(state)
            else:
                pub, rev = [], []

            published.extend(pub)
            review_queue.extend(rev)
            source_runs.append(
                {
                    **source,
                    "lastRunAt": now_iso(),
                    "lastResult": "ok",
                    "publishedCount": len(pub),
                    "reviewCount": len(rev),
                    "methodPublicLabel": human_source_method(source),
                }
            )
        except Exception as exc:
            source_runs.append(
                {
                    **source,
                    "lastRunAt": now_iso(),
                    "lastResult": f"error: {type(exc).__name__}",
                    "publishedCount": 0,
                    "reviewCount": 0,
                    "methodPublicLabel": human_source_method(source),
                }
            )

    published = dedupe([x for x in published if keep_recent(x.get("effectiveDate", ""))])
    review_queue = dedupe([x for x in review_queue if keep_recent(x.get("effectiveDate", ""))])

    save_json(OUT_ACTIONS, published)
    save_json(OUT_REVIEW, review_queue)
    save_json(OUT_SOURCES, source_runs)
    save_json(
        OUT_STATUS,
        {
            "generatedAt": now_iso(),
            "lookbackDays": LOOKBACK_DAYS,
            "publishedCount": len(published),
            "reviewCount": len(review_queue),
            "sourceCount": len(source_runs),
        },
    )
    print(f"published={len(published)}")
    print(f"review={len(review_queue)}")
    print(f"sources={len(source_runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
