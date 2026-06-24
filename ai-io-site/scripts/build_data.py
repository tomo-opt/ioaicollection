from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
INPUT_CSV = ROOT / "international_orgs_seed.csv"
OUTPUT_JSON = ROOT / "ai-io-site" / "data" / "orgs.json"
OVERRIDES_JSON = ROOT / "ai-io-site" / "data" / "manual" / "org-overrides.json"


def col(text: str) -> str:
    return text.encode("ascii").decode("unicode_escape")


COLS = {
    "name_en": col(r"\u89c4\u8303\u82f1\u6587\u540d\u79f0"),
    "name_zh": col(r"\u6807\u51c6\u4e2d\u6587\u540d\u79f0"),
    "acronym": col(r"\u539f\u59cb\u7b80\u79f0"),
    "official": col(r"\u5b98\u65b9\u7f51\u7ad9"),
    "official_ref": col(r"\u5b98\u7f51\u53c2\u8003\u94fe\u63a5"),
    "uia": col(r"\u0055\u0049\u0041\u516c\u5f00\u6863\u6848\u94fe\u63a5"),
    "founded": col(r"\u6210\u7acb\u5e74\u4efd"),
    "city": col(r"\u603b\u90e8\u57ce\u5e02"),
    "country": col(r"\u603b\u90e8\u56fd\u5bb6\u6216\u5730\u533a"),
    "org_type": col(r"\u7ec4\u7ec7\u7c7b\u578b"),
    "level": col(r"\u6240\u5c5e\u5c42\u7ea7"),
    "frontend": col(r"\u662f\u5426\u5efa\u8bae\u524d\u53f0\u5c55\u793a"),
    "role": col(r"\u9879\u76ee\u89d2\u8272\u5efa\u8bae"),
    "status": col(r"\u6838\u9a8c\u72b6\u6001"),
    "note": col(r"\u5907\u6ce8"),
    "aims": col(r"\u516c\u5f00\u5b97\u65e8\u6458\u8981"),
}


def clean(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def usable_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def load_overrides() -> dict[str, dict]:
    if not OVERRIDES_JSON.exists():
        return {}
    items = json.loads(OVERRIDES_JSON.read_text(encoding="utf-8"))
    return {str(item.get("nameEn", "")).strip(): item for item in items if str(item.get("nameEn", "")).strip()}


def apply_override(record: dict, override: dict) -> dict:
    for key, value in override.items():
        if key == "nameEn":
            continue
        if value is None:
            continue
        if isinstance(value, str):
            value = value.strip()
        if value == "":
            continue
        record[key] = value
    return record


def build_from_csv() -> list[dict]:
    df = pd.read_csv(INPUT_CSV, encoding="utf-8-sig")
    records: list[dict] = []

    for _, row in df.iterrows():
        official_url = clean(row.get(COLS["official"]))
        official_status = "verified" if usable_url(official_url) else "manual_needed"

        record = {
            "nameEn": clean(row.get(COLS["name_en"])),
            "nameZh": clean(row.get(COLS["name_zh"])),
            "acronym": clean(row.get(COLS["acronym"])),
            "officialUrl": official_url if usable_url(official_url) else "",
            "officialUrlStatus": official_status,
            "officialUrlNote": "" if usable_url(official_url) else official_url,
            "officialUrlRef": clean(row.get(COLS["official_ref"])),
            "uiaProfileUrl": clean(row.get(COLS["uia"])),
            "foundedYear": clean(row.get(COLS["founded"])),
            "hqCity": clean(row.get(COLS["city"])),
            "hqCountry": clean(row.get(COLS["country"])),
            "orgType": clean(row.get(COLS["org_type"])),
            "level": clean(row.get(COLS["level"])),
            "frontendSuggestion": clean(row.get(COLS["frontend"])),
            "roleSuggestion": clean(row.get(COLS["role"])),
            "verifyStatus": clean(row.get(COLS["status"])),
            "note": clean(row.get(COLS["note"])),
            "aims": clean(row.get(COLS["aims"])),
        }
        records.append(record)
    return records


def build_from_existing_json() -> list[dict]:
    if not OUTPUT_JSON.exists():
        raise FileNotFoundError("Neither source CSV nor existing orgs.json is available.")
    return json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))


def main() -> int:
    if INPUT_CSV.exists():
        records = build_from_csv()
    else:
        records = build_from_existing_json()

    overrides = load_overrides()
    if overrides:
        records = [apply_override(record, overrides.get(record.get("nameEn", ""), {})) for record in records]

    OUTPUT_JSON.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"built_records={len(records)}")
    print(f"used_csv={INPUT_CSV.exists()}")
    print(f"overrides={len(overrides)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
