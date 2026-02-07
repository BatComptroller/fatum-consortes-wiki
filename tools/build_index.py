import json, re
from pathlib import Path

DOCS_DIR = Path("docs")
OUT_DIR = DOCS_DIR / "_data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FRONT_MATTER = re.compile(r"^---\s*(.*?)\s*---\s*", re.DOTALL)

def parse_front_matter(text: str):
    m = FRONT_MATTER.match(text)
    if not m:
        return {}, text
    fm = m.group(1)
    body = text[m.end():]
    data = {}
    key = None
    for line in fm.splitlines():
        line = line.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", line) and key:
            data.setdefault(key, []).append(line.split("-", 1)[1].strip())
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            key = k.strip()
            v = v.strip()
            if v == "":
                data[key] = []
            else:
                data[key] = v.strip('"').strip("'")
    return data, body

def title_from_body(body: str, fallback: str):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback

def slug_from_path(path: Path):
    rel = path.relative_to(DOCS_DIR).with_suffix("")
    return "/" + str(rel).replace("\\", "/") + "/"

def text_snippet(body: str, maxlen=240):
    body = re.sub(r"`{1,3}.*?`{1,3}", "", body, flags=re.DOTALL)
    body = re.sub(r"\[.*?\]\(.*?\)", "", body)
    body = re.sub(r"#+\s*", "", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body[:maxlen]

pages = []
for md in DOCS_DIR.rglob("*.md"):
    if "/_data/" in str(md).replace("\\", "/"):
        continue
    raw = md.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    title = meta.get("title") or title_from_body(body, md.stem)
    pages.append({
        "title": title,
        "url": slug_from_path(md),
        "source_path": str(md).replace("\\","/"),
        "canon_mode": meta.get("canon_mode", "UNSPECIFIED"),
        "continuity_flag": meta.get("continuity_flag", "UNSPECIFIED"),
        "version": meta.get("version", ""),
        "tags": meta.get("tags", []),
        "symbols": meta.get("symbols", []),
        "related": meta.get("related", []),
        "snippet": text_snippet(body),
    })

(OUT_DIR / "index.json").write_text(json.dumps(pages, indent=2), encoding="utf-8")
print(f"Wrote {len(pages)} records to docs/_data/index.json")
