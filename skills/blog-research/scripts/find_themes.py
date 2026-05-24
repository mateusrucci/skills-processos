#!/usr/bin/env python3
"""
find_themes.py — busca temas virais via Hacker News + Reddit.

Adaptado da Máquina do Mastermind para uso no blog-research skill.

Uso:
    python3 find_themes.py --query "paid traffic" --query "meta ads" \
                           --reddit r/PPC --reddit r/Entrepreneur \
                           --slug rucci

Saída: ~/blog-research/{slug}/{timestamp}/raw.json
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

OUT_BASE = Path.home() / "blog-research"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

HN_URL = (
    "https://hn.algolia.com/api/v1/search?query={q}"
    "&hitsPerPage=20&tags=story&numericFilters=points%3E100"
)
# Nota: Reddit API pública passou a exigir OAuth (2024+).
# Se search_reddit retornar 403, o Claude deve usar web_search manualmente:
#   "site:reddit.com/r/{subreddit} top posts {nicho} this week"
REDDIT_URL = "https://www.reddit.com/{sub}/top.json?t=week&limit=25"


def _http_get_json(url: str, timeout: int = 25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def search_hn(query: str) -> list[dict]:
    url = HN_URL.format(q=urllib.parse.quote(query))
    try:
        data = _http_get_json(url)
    except Exception as e:
        print(f"[hn] {query!r} ERRO: {e}", file=sys.stderr)
        return []
    out = []
    for hit in data.get("hits", []):
        out.append({
            "source": "hn",
            "query": query,
            "title": hit.get("title") or hit.get("story_title"),
            "url": hit.get("url") or hit.get("story_url"),
            "points": hit.get("points"),
            "comments": hit.get("num_comments"),
            "created_at": hit.get("created_at"),
            "objectID": hit.get("objectID"),
        })
    return out


def search_reddit(sub: str) -> list[dict]:
    sub = sub.strip().lstrip("/")
    if not sub.startswith("r/"):
        sub = f"r/{sub}"
    url = REDDIT_URL.format(sub=sub)
    try:
        data = _http_get_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 403:
            sub_clean = sub.replace("r/", "")
            print(
                f"[reddit] {sub} 403 — API pública bloqueada.\n"
                f"  Fallback: use web_search com query:\n"
                f"  'site:reddit.com/r/{sub_clean} top week'\n"
                f"  ou acesse diretamente: https://www.reddit.com/{sub}/top/?t=week",
                file=sys.stderr
            )
            return []
        elif e.code == 429:
            print(f"[reddit] {sub} 429 — aguardando e retentando..", file=sys.stderr)
            time.sleep(20)
            try:
                data = _http_get_json(url)
            except Exception as e2:
                print(f"[reddit] {sub} segundo ERRO: {e2}", file=sys.stderr)
                return []
        else:
            print(f"[reddit] {sub} HTTP {e.code}", file=sys.stderr)
            return []
    except Exception as e:
        print(f"[reddit] {sub} ERRO: {e}", file=sys.stderr)
        return []
    out = []
    for child in (data.get("data") or {}).get("children", []):
        d = child.get("data") or {}
        out.append({
            "source": "reddit",
            "subreddit": sub,
            "title": d.get("title"),
            "url": "https://reddit.com" + (d.get("permalink") or ""),
            "ups": d.get("ups"),
            "comments": d.get("num_comments"),
            "selftext": (d.get("selftext") or "")[:600],
            "created_utc": d.get("created_utc"),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", action="append", default=[], help="termo de busca HN (pode repetir)")
    ap.add_argument("--reddit", action="append", default=[], help="subreddit ex: r/PPC")
    ap.add_argument("--slug", default="blog", help="slug do blog/cliente para organizar output")
    ap.add_argument("--out", default=None, help="path de saída customizado")
    args = ap.parse_args()

    if not args.query and not args.reddit:
        print("Sem queries nem subreddits — passa --query ou --reddit", file=sys.stderr)
        sys.exit(2)

    results: list[dict] = []
    for q in args.query:
        print(f"[hn] buscando: {q!r}..", flush=True)
        results.extend(search_hn(q))
        time.sleep(1.0)
    for sub in args.reddit:
        print(f"[reddit] buscando: {sub}..", flush=True)
        results.extend(search_reddit(sub))
        time.sleep(2.0)

    if args.out:
        out_path = Path(args.out).expanduser()
    else:
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        out_path = OUT_BASE / args.slug / ts / "raw.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n[find_themes] {len(results)} resultados -> {out_path}")
    print(f"  hn:     {sum(1 for r in results if r['source'] == 'hn')}")
    print(f"  reddit: {sum(1 for r in results if r['source'] == 'reddit')}")

    # Resumo de top sinais para o Claude curadoria
    top_hn = sorted([r for r in results if r["source"] == "hn"], key=lambda x: x.get("points") or 0, reverse=True)[:5]
    top_reddit = sorted([r for r in results if r["source"] == "reddit"], key=lambda x: x.get("ups") or 0, reverse=True)[:5]

    print("\n--- TOP HN (por pontos) ---")
    for r in top_hn:
        title = r.get('title') or '(sem título)'
        print(f"  [{r.get('points')} pts] {title} — {(r.get('url') or '')[:80]}")

    print("\n--- TOP REDDIT (por upvotes) ---")
    for r in top_reddit:
        title = r.get('title') or '(sem título)'
        print(f"  [{r.get('ups')} ups | {r.get('subreddit')}] {title}")


if __name__ == "__main__":
    main()
