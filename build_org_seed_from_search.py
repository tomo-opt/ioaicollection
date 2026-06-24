from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import pandas as pd


ROOT = Path(r"C:\Users\14916\Desktop\ioaicollection")
XLSX_PATH = next(p for p in ROOT.glob("*.xlsx") if not p.name.startswith("~$"))
CSV_PATH = ROOT / "international_orgs_seed.csv"
WORKLOG_PATH = ROOT / "institution-verification-worklog.md"
METHOD_PATH = ROOT / "collection-method-notes.md"
SEARCH_CACHE_PATH = ROOT / "org_search_cache.jsonl"


def zh(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


F = {
    "idx": zh(r"\u5e8f\u53f7"),
    "raw_name": zh(r"\u539f\u59cb\u82f1\u6587\u540d\u79f0"),
    "raw_acronym": zh(r"\u539f\u59cb\u7b80\u79f0"),
    "norm_name": zh(r"\u89c4\u8303\u82f1\u6587\u540d\u79f0"),
    "cn_name": zh(r"\u6807\u51c6\u4e2d\u6587\u540d\u79f0"),
    "cn_ref": zh(r"\u4e2d\u6587\u540d\u79f0\u53c2\u8003\u94fe\u63a5"),
    "exists": zh(r"\u662f\u5426\u771f\u5b9e\u5b58\u5728"),
    "official": zh(r"\u5b98\u65b9\u7f51\u7ad9"),
    "official_ref": zh(r"\u5b98\u7f51\u53c2\u8003\u94fe\u63a5"),
    "uia_profile": zh(r"\u0055\u0049\u0041\u516c\u5f00\u6863\u6848\u94fe\u63a5"),
    "founded": zh(r"\u6210\u7acb\u5e74\u4efd"),
    "hq_city": zh(r"\u603b\u90e8\u57ce\u5e02"),
    "hq_country": zh(r"\u603b\u90e8\u56fd\u5bb6\u6216\u5730\u533a"),
    "org_type": zh(r"\u7ec4\u7ec7\u7c7b\u578b"),
    "level": zh(r"\u6240\u5c5e\u5c42\u7ea7"),
    "frontend": zh(r"\u662f\u5426\u5efa\u8bae\u524d\u53f0\u5c55\u793a"),
    "role": zh(r"\u9879\u76ee\u89d2\u8272\u5efa\u8bae"),
    "status": zh(r"\u6838\u9a8c\u72b6\u6001"),
    "note": zh(r"\u5907\u6ce8"),
    "aims": zh(r"\u516c\u5f00\u5b97\u65e8\u6458\u8981"),
}

YES = zh(r"\u662f")
PENDING = zh(r"\u5f85\u4eba\u5de5\u590d\u6838")
VERIFIED = zh(r"\u5df2\u6838\u9a8c")
NO_UIA = zh(r"\u672a\u547d\u4e2dUIA\u516c\u5f00\u6863\u6848")
NO_CN = zh(r"\u672a\u68c0\u7d22\u5230\u7a33\u5b9a\u4e2d\u6587\u540d\u79f0")
NO_SITE = zh(r"\u672a\u8bfb\u5230\u7a33\u5b9a\u5b98\u7f51")
NA = zh(r"\u65e0")
NOT_PUBLIC = zh(r"\u672a\u516c\u5f00")
NOT_FOUND = zh(r"\u672a\u547d\u4e2d")
NOT_READ = zh(r"\u672a\u8bfb\u5230")
FULL_COLON = zh(r"\uff1a")
FULL_SEMI = zh(r"\uff1b")


def decode_escapes(text: str) -> str:
    if "\\u" in text or "\\x" in text:
        try:
            return text.encode("utf-8").decode("unicode_escape")
        except Exception:
            return text
    return text


def normalize_value(text: str) -> str:
    text = decode_escapes(text.strip())
    text = re.sub(r"\s+", " ", text).strip()
    return text


def read_search_cache() -> dict[str, dict]:
    if not SEARCH_CACHE_PATH.exists():
        return {}
    out: dict[str, dict] = {}
    for line in SEARCH_CACHE_PATH.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        out[obj["name"]] = obj
    return out


def parse_worklog_sections() -> dict[str, dict]:
    text = WORKLOG_PATH.read_text(encoding="utf-8-sig")
    parts = re.split(r"^##\s+(\d+)\.\s+(.+)$", text, flags=re.M)
    out: dict[str, dict] = {}
    i = 1
    while i < len(parts):
        idx = parts[i].strip()
        name = parts[i + 1].strip()
        body = parts[i + 2]
        item = {"idx": idx, "name": name}
        for line in body.splitlines():
            m = re.match(r"^- ([^:：]+)[：:](.*)$", line.strip())
            if not m:
                continue
            key = normalize_value(m.group(1))
            value = normalize_value(m.group(2))
            item[key] = value
        out[name] = item
        i += 3
    return out


def split_city_country(text: str) -> tuple[str, str]:
    text = normalize_value(text)
    if not text or text == NOT_PUBLIC:
        return "", ""
    parts = [p.strip() for p in text.split("/") if p.strip()]
    if len(parts) >= 2:
        return parts[0], parts[1]
    return "", ""


def read_year(value: object) -> str:
    if pd.isna(value):
        return ""
    try:
        return str(int(value))
    except Exception:
        return normalize_value(str(value))


def build_records() -> list[dict]:
    df = pd.read_excel(XLSX_PATH)
    sections = parse_worklog_sections()
    search_cache = read_search_cache()
    records: list[dict] = []

    for _, row in df.iterrows():
        row = row.to_dict()
        name = normalize_value(str(row.get("Name", "")))
        sec = sections.get(name, {})
        search_item = search_cache.get(name, {})

        raw_acronym = "" if pd.isna(row.get("Acronym")) else normalize_value(str(row.get("Acronym")))
        founded = normalize_value(sec.get(F["founded"], ""))
        if founded in {"", NOT_PUBLIC}:
            founded = read_year(row.get("Founded"))

        city = normalize_value(sec.get(F["hq_city"] + " / " + F["hq_country"], ""))
        sec_city, sec_country = split_city_country(city)
        if not sec_city:
            sec_city = "" if pd.isna(row.get("City HQ")) else normalize_value(str(row.get("City HQ")))
        if not sec_country:
            sec_country = "" if pd.isna(row.get("Country/Territory HQ")) else normalize_value(str(row.get("Country/Territory HQ")))

        cn_name = normalize_value(sec.get(F["cn_name"], ""))
        if cn_name == NO_CN:
            cn_name = ""
        cn_ref = normalize_value(search_item.get("picked_cn_ref", ""))
        if search_item.get("picked_cn_name") and not cn_name:
            cn_name = normalize_value(search_item.get("picked_cn_name", ""))

        status = normalize_value(sec.get(F["status"], ""))
        if not status:
            status = VERIFIED if sec.get(F["uia_profile"]) else NO_UIA
        exists = YES if status == VERIFIED else PENDING

        record = {
            F["raw_name"]: name,
            F["raw_acronym"]: raw_acronym,
            F["norm_name"]: normalize_value(sec.get(F["norm_name"], name)) or name,
            F["cn_name"]: cn_name,
            F["cn_ref"]: cn_ref,
            F["exists"]: exists,
            F["official"]: normalize_value(sec.get(F["official"], "")),
            F["official_ref"]: normalize_value(sec.get(F["official_ref"], "")),
            F["uia_profile"]: normalize_value(sec.get(F["uia_profile"], "")),
            F["founded"]: founded,
            F["hq_city"]: sec_city,
            F["hq_country"]: sec_country,
            F["org_type"]: normalize_value(sec.get(F["org_type"], "")),
            F["level"]: normalize_value(sec.get(F["level"], "")),
            F["frontend"]: normalize_value(sec.get(F["frontend"], "")),
            F["role"]: normalize_value(sec.get(F["role"], "")),
            "UIA_Type_I": "" if pd.isna(row.get("Type I")) else normalize_value(str(row.get("Type I"))),
            "UIA_Type_II": "" if pd.isna(row.get("Type II")) else normalize_value(str(row.get("Type II"))),
            "UIA_Org_ID": "" if pd.isna(row.get("UIA Org ID")) else normalize_value(str(row.get("UIA Org ID"))),
            F["status"]: status,
            F["note"]: normalize_value(sec.get(F["note"], "")),
            F["aims"]: normalize_value(sec.get(F["aims"], "")),
        }
        records.append(record)

    return records


def write_csv(records: list[dict]) -> None:
    headers = [
        F["idx"],
        F["raw_name"],
        F["raw_acronym"],
        F["norm_name"],
        F["cn_name"],
        F["cn_ref"],
        F["exists"],
        F["official"],
        F["official_ref"],
        F["uia_profile"],
        F["founded"],
        F["hq_city"],
        F["hq_country"],
        F["org_type"],
        F["level"],
        F["frontend"],
        F["role"],
        "UIA_Type_I",
        "UIA_Type_II",
        "UIA_Org_ID",
        F["status"],
        F["note"],
        F["aims"],
    ]
    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for idx, rec in enumerate(records, start=1):
            w.writerow([idx] + [rec.get(h, "") for h in headers[1:]])


def write_worklog(records: list[dict]) -> None:
    lines = [
        "# " + zh(r"\u673a\u6784\u6838\u9a8c\u5de5\u5355"),
        "",
        zh(r"\u66f4\u65b0\u65f6\u95f4") + FULL_COLON + "2026-06-19",
        "",
        zh(r"\u8bf4\u660e") + FULL_COLON
        + zh(r"\u672c\u7248\u4e3a\u6839\u636e\u5df2\u5b8c\u6210\u7684 UIA \u516c\u5f00\u6863\u6848\u6838\u9a8c\u5de5\u5355\u53cd\u5411\u6062\u590d\u7684\u7ed3\u6784\u5316\u8f93\u51fa\u3002")
        + zh(r"\u5b98\u7f51\u3001UIA \u6863\u6848\u94fe\u63a5\u3001\u5b97\u65e8\u6458\u8981\u4ee5\u5de5\u5355\u4e2d\u5df2\u6838\u9a8c\u5185\u5bb9\u4e3a\u51c6\uff1b")
        + zh(r"\u4e2d\u6587\u540d\u79f0\u4ec5\u5728\u67e5\u5230\u7a33\u5b9a\u516c\u5f00\u8868\u8ff0\u65f6\u56de\u586b\u3002"),
        "",
        "## " + zh(r"\u603b\u8868"),
        "",
        "| %s | %s | %s | %s | %s |" % (F["idx"], F["raw_name"], F["status"], F["official"], F["note"]),
        "|---|---|---|---|---|",
    ]

    for idx, rec in enumerate(records, start=1):
        lines.append("| %s | %s | %s | %s | %s |" % (idx, rec[F["raw_name"]], rec[F["status"]], rec[F["official"]], rec[F["note"]]))

    lines.extend(["", "---", ""])

    for idx, rec in enumerate(records, start=1):
        lines.extend(
            [
                "## %s. %s" % (idx, rec[F["raw_name"]]),
                "",
                "- %s%s%s" % (F["raw_acronym"], FULL_COLON, rec[F["raw_acronym"]] or NA),
                "- %s%s%s" % (F["status"], FULL_COLON, rec[F["status"]] or NA),
                "- %s%s%s" % (F["norm_name"], FULL_COLON, rec[F["norm_name"]] or NA),
                "- %s%s%s" % (F["cn_name"], FULL_COLON, rec[F["cn_name"]] or NO_CN),
                "- %s%s%s" % (F["official"], FULL_COLON, rec[F["official"]] or NO_SITE),
                "- %s%s%s" % (F["official_ref"], FULL_COLON, rec[F["official_ref"]] or NOT_PUBLIC),
                "- %s%s%s" % (F["uia_profile"], FULL_COLON, rec[F["uia_profile"]] or NOT_FOUND),
                "- %s%s%s" % (F["founded"], FULL_COLON, rec[F["founded"]] or NOT_PUBLIC),
                "- %s / %s%s%s / %s" % (F["hq_city"], F["hq_country"], FULL_COLON, rec[F["hq_city"]] or NOT_PUBLIC, rec[F["hq_country"]] or NOT_PUBLIC),
                "- %s%s%s" % (F["org_type"], FULL_COLON, rec[F["org_type"]] or NA),
                "- %s%s%s" % (F["level"], FULL_COLON, rec[F["level"]] or NA),
                "- %s%s%s" % (F["frontend"], FULL_COLON, rec[F["frontend"]] or NA),
                "- %s%s%s" % (F["role"], FULL_COLON, rec[F["role"]] or NA),
                "- %s%s%s" % (F["aims"], FULL_COLON, rec[F["aims"]] or NOT_READ),
                "- %s%s%s" % (F["note"], FULL_COLON, rec[F["note"]] or NA),
                "",
            ]
        )

    WORKLOG_PATH.write_text("\n".join(lines), encoding="utf-8-sig")


def write_method_doc() -> None:
    lines = [
        "# " + zh(r"\u6536\u5f55\u4e0e\u81ea\u52a8\u66f4\u65b0\u65b9\u6cd5\u8bf4\u660e"),
        "",
        zh(r"\u66f4\u65b0\u65f6\u95f4") + FULL_COLON + "2026-06-19",
        "",
        "## " + zh(r"\u4e00\u3001\u514d\u8d39\u4e3b\u6570\u636e\u6e90\u548c\u81ea\u52a8\u66f4\u65b0"),
        "",
        "1. UIA " + zh(r"\u516c\u5f00\u6863\u6848") + FULL_COLON
        + zh(r"\u7528 `https://uia.org/org_xml/<name>` \u6309\u82f1\u6587\u540d\u68c0\u7d22 profile\uff0c\u518d\u8bfb profile \u9875\u4e2d URL\u3001Founded\u3001Aims \u7b49\u5b57\u6bb5\u3002"),
        "2. UN AI Resource Hub / UN for Good" + FULL_COLON
        + zh(r"\u7528\u201c\u5217\u8868\u9875\u5b9a\u65f6\u6293\u53d6 + \u8be6\u60c5\u9875\u7ed3\u6784\u5316\u62bd\u53d6 + diff \u53d8\u66f4\u68c0\u6d4b\u201d\u3002"),
        "3. " + zh(r"\u5176\u4ed6\u56fd\u9645\u7ec4\u7ec7 AI \u884c\u52a8\u6e90") + FULL_COLON
        + zh(r"\u4f8b\u5982 OECD\u3001UNESCO\u3001Council of Europe\u3001ITU\u3001WEF \u7b49\u5b98\u65b9\u516c\u5f00\u9875\u9762\uff0c\u540c\u6837\u7528 HTML \u5217\u8868\u6293\u53d6\u6216 RSS/JSON \u589e\u91cf\u62c9\u53d6\u3002"),
        "4. " + zh(r"\u514d\u8d39\u6280\u672f\u6808") + FULL_COLON + "Python + urllib/lxml + pandas + GitHub Actions cron + csv/jsonl/sqlite",
        "5. " + zh(r"\u66f4\u65b0\u673a\u5236") + FULL_COLON
        + zh(r"\u5b9a\u65f6\u62c9\u53d6\u5217\u8868 -> \u6309 URL \u548c\u6807\u9898 hash \u505a diff -> \u65b0\u589e/\u53d8\u66f4\u9879\u5148\u8fdb review queue -> \u4eba\u5de5\u5ba1\u6838\u540e\u5165\u524d\u53f0\u3002"),
        "",
        "## " + zh(r"\u4e8c\u3001`https://unaihub.aiforgood.itu.int/activities.php` \u8fd9\u7c7b\u9875\u9762\u600e\u4e48\u6536\u5f55"),
        "",
        zh(r"\u4e0d\u662f iframe \u6574\u9875\u642c\u8fd0\uff0c\u800c\u662f\u62c6\u6210\u4f60\u81ea\u5df1\u7684 action \u8bb0\u5f55\u3002"),
        zh(r"\u6bcf\u6761 action \u81f3\u5c11\u5b58 `action_id`\u3001`title`\u3001`summary`\u3001`source_org`\u3001`source_program`\u3001`action_type`\u3001`theme`\u3001`region`\u3001`published_at`\u3001`deadline`\u3001`source_url`\u3001`last_seen_at`\u3002"),
        zh(r"\u524d\u53f0\u91cc\u5219\u628a action \u6302\u5230\u53d1\u8d77\u7ec4\u7ec7\u3001\u8ba1\u5212\u3001\u4e3b\u9898\u548c\u65f6\u95f4\u7ef4\u5ea6\u4e0a\u3002"),
        "",
        "## " + zh(r"\u4e09\u3001\u600e\u4e48\u907f\u514d\u786c\u5173\u952e\u8bcd\u8fc7\u6ee4"),
        "",
        zh(r"\u5173\u952e\u8bcd\u53ea\u7528\u6765\u53ec\u56de\uff0c\u4e0d\u7528\u6765\u88c1\u51b3\u3002"),
        zh(r"\u5148\u9650\u5b9a\u6765\u6e90\u57df\u4e3a\u5df2\u786e\u8ba4\u7684\u56fd\u9645\u7ec4\u7ec7\u53ca\u5176\u9879\u76ee\u9875\uff0c\u518d\u8bfb source page \u672c\u8eab\u7684\u6807\u9898\u3001\u6458\u8981\u3001about \u548c\u53d1\u5e03\u4e3b\u4f53\u4fe1\u606f\u6765\u5f52\u7c7b\u3002"),
        zh(r"\u8fd9\u79cd\u201csource-driven + \u9605\u8bfb\u5f0f\u5f52\u7c7b\u201d\u7684\u6d41\u7a0b\uff0c\u6bd4\u57df\u540d\u6a21\u677f\u6216\u5173\u952e\u8bcd\u786c\u7b5b\u7a33\u5f97\u591a\u3002"),
        "",
        "## " + zh(r"\u56db\u3001Excel \u8fd9\u6279\u673a\u6784\u5728\u9879\u76ee\u91cc\u7684\u4f5c\u7528"),
        "",
        "- " + zh(r"\u79cd\u5b50\u7ec4\u7ec7\u5e93") + FULL_COLON + zh(r"\u786e\u5b9a\u201c\u54ea\u4e9b\u662f\u5408\u6cd5\u7684\u56fd\u9645\u7ec4\u7ec7\u4e3b\u4f53\u201d\u3002"),
        "- " + zh(r"\u884c\u52a8\u6302\u8f7d\u4e3b\u4f53") + FULL_COLON + zh(r"\u540e\u7eed\u6293\u5230\u7684 action \u9700\u8981\u80fd\u56de\u6302\u5230\u8fd9\u4e2a\u79cd\u5b50\u5e93\u3002"),
        "- " + zh(r"\u4fe1\u4efb\u8fc7\u6ee4\u5c42") + FULL_COLON + zh(r"\u5f53 action \u80fd\u6620\u5c04\u56de\u56fd\u9645\u7ec4\u7ec7\u5e93\u65f6\uff0c\u5c31\u80fd\u533a\u5206\u4e0e\u4e00\u822c\u56fd\u5bb6\u653f\u7b56\u6216\u4ea7\u4e1a\u65b0\u95fb\u7684\u5dee\u522b\u3002"),
        "- " + zh(r"\u524d\u53f0\u5bfc\u822a\u5c42") + FULL_COLON + zh(r"\u53ef\u6309\u7ec4\u7ec7\u7c7b\u578b\u3001\u5730\u57df\u3001\u662f\u5426\u653f\u5e9c\u95f4\u3001\u662f\u5426\u6807\u51c6/\u4f26\u7406/\u6559\u80b2/\u7814\u7a76\u5bfc\u5411\u5206\u533a\u3002"),
    ]
    METHOD_PATH.write_text("\n".join(lines), encoding="utf-8-sig")


def main() -> int:
    records = build_records()
    write_csv(records)
    write_worklog(records)
    write_method_doc()
    print("processed_rows=%s" % len(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
