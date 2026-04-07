import requests

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
URL = "https://github.com"
ROBOTS_TXT = URL + "/robots.txt"


# ─────────────────────────────────────────
# STEP 1 — PARSE robots.txt
# ─────────────────────────────────────────
def parse_robots_txt(data):
    disallowed_paths = []

    for line in data.splitlines():
        if line.startswith("Disallow:"):
            path = line[len("Disallow:"):].strip()
            if path:
                disallowed_paths.append(path)
                print(f"  [Disallow] {path}")

    return disallowed_paths


def parse_sitemap(data):
    sitemaps = []

    for line in data.splitlines():
        if line.startswith("Sitemap:"):
            url = line[len("Sitemap:"):].strip()
            if url:
                sitemaps.append(url)
                print(f"  [Sitemap]  {url}")

    return sitemaps


# ─────────────────────────────────────────
# STEP 2 — NORMALIZE & DEDUPLICATE
# ─────────────────────────────────────────
def normalize_and_deduplicate(paths):
    seen = set()
    clean = []

    for path in paths:
        if "*" in path or path == "/":   # skip wildcards and root
            continue
        if not path.startswith("/"):     # ensure leading slash
            path = "/" + path
        if path not in seen:             # deduplicate
            seen.add(path)
            clean.append(path)

    return clean


# ─────────────────────────────────────────
# STEP 3 — BUILD FULL URLs
# ─────────────────────────────────────────
def build_full_urls(base_url, paths):
    base = base_url.rstrip("/")
    return [base + path for path in paths]


# ─────────────────────────────────────────
# STEP 4 — PROBE URLs
# ─────────────────────────────────────────
def probe_urls(urls):
    results = {
        "200":     [],
        "301/302": [],
        "401/403": [],
        "404":     [],
        "500":     [],
        "other":   [],
    }

    for url in urls:
        try:
            res  = requests.get(url, timeout=5, allow_redirects=False)
            code = res.status_code
            print(f"  [{code}] {url}")

            if code == 200:                results["200"].append(url)
            elif code in (301, 302):       results["301/302"].append(url)
            elif code in (401, 403):       results["401/403"].append(url)
            elif code == 404:              results["404"].append(url)
            elif code == 500:              results["500"].append(url)
            else:                          results["other"].append(url)

        except requests.exceptions.RequestException as e:
            print(f"  [ERROR] {url} → {e}")

    return results


# ─────────────────────────────────────────
# STEP 5 — REPORT INTERESTING FINDINGS
# ─────────────────────────────────────────
def report_interesting(results):
    categories = [
        ("200",     "Publicly accessible"),
        ("401/403", "Protected but exists"),
        ("301/302", "Redirects"),
        ("500",     "Server errors"),
    ]

    print("\n" + "═" * 50)
    print("  INTERESTING FINDINGS")
    print("═" * 50)

    for key, label in categories:
        urls = results[key]
        print(f"\n[{key}] {label} ({len(urls)}):")
        for url in urls:
            print(f"  → {url}")


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
def main():
    print(f"\n[*] Fetching {ROBOTS_TXT}\n")
    r = requests.get(ROBOTS_TXT)

    if r.status_code != 200:
        print(f"[!] Failed to fetch robots.txt — status code: {r.status_code}")
        return

    print("[+] Success!\n")
    data = r.text

    print("[*] Parsing Disallow entries...")
    paths = parse_robots_txt(data)
    print(f"\n    → {len(paths)} disallowed paths found")

    print("\n[*] Parsing Sitemaps...")
    sitemaps = parse_sitemap(data)
    print(f"\n    → {len(sitemaps)} sitemaps found")

    print("\n[*] Normalizing and deduplicating paths...")
    clean_paths = normalize_and_deduplicate(paths)
    print(f"    → {len(clean_paths)} unique paths after cleanup")

    print("\n[*] Building full URLs...")
    full_urls = build_full_urls(URL, clean_paths)
    for url in full_urls:
        print(f"  {url}")

    print(f"\n[*] Probing {len(full_urls)} URLs...")
    results = probe_urls(full_urls)

    report_interesting(results)


if __name__ == "__main__":
    main()