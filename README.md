
# Robots Finder

Robots Finder is a Python tool for fetching and analyzing a website’s `robots.txt` file. It extracts disallowed paths, discovers sitemap entries, probes the discovered URLs, and reports potentially interesting findings such as accessible, protected, redirected, or broken paths.

## What it does

- Fetches `robots.txt` from a target website
- Parses `Disallow` rules
- Parses `Sitemap` entries
- Normalizes and deduplicates discovered paths
- Builds full URLs from discovered disallowed paths
- Probes each URL and groups results by HTTP status
- Highlights interesting findings such as:
  - `200` — publicly accessible
  - `401/403` — protected but exists
  - `301/302` — redirects
  - `500` — server-side errors

## Tech Stack

- **Language:** Python 3
- **Library:** `requests`

## Project Structure

```bash
robots_finder/
├── robots_finder.py
├── requirements.txt
└── README.md
````

## Requirements

* Python 3.7 or higher

## Installation

```bash
# Clone the repository
git clone https://github.com/grostel018/robots_finder.git

# Enter the project folder
cd robots_finder

# Install dependencies
pip install -r requirements.txt
```

## Usage

At the moment, the script uses a hardcoded target URL inside `robots_finder.py`.

Current default target:

```python
URL = "https://github.com"
ROBOTS_TXT = URL + "/robots.txt"
```

Run the script with:

```bash
python robots_finder.py
```

## How it works

### 1. Fetch `robots.txt`

The script requests the target site's `robots.txt` file.

### 2. Parse entries

It extracts:

* `Disallow:` paths
* `Sitemap:` URLs

### 3. Clean paths

It:

* removes duplicates
* ensures paths begin with `/`
* skips wildcard entries and root `/`

### 4. Build URLs

Each cleaned path is combined with the base URL.

### 5. Probe discovered URLs

The script sends HTTP requests and groups results into categories:

* `200`
* `301/302`
* `401/403`
* `404`
* `500`
* `other`

### 6. Report findings

It prints the most interesting categories in a readable summary.

## Example Output

```bash
[*] Fetching https://github.com/robots.txt

[+] Success!

[*] Parsing Disallow entries...
  [Disallow] /login
  [Disallow] /settings

[*] Parsing Sitemaps...
  [Sitemap]  https://github.com/sitemap.xml

[*] Probing discovered URLs...
  [200] https://github.com/login
  [403] https://github.com/settings
```

## Current Limitations

This version is an early script version and currently does **not** include:

* command-line arguments
* scanning from a file/list of domains
* user-agent customization
* text or JSON export
* concurrent scanning
* test suite

## Future Improvements

Planned improvements could include:

* Add `argparse` support for CLI usage
* Allow single URL or file input
* Add output export to `.txt` and `.json`
* Add custom user-agent support
* Add concurrency for faster scans
* Add retry/error handling improvements
* Add automated tests

## Disclaimer

Use this tool only on websites you are authorized to test or analyze. Respect website policies, laws, and platform terms of service.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Author

**Rostel Geni**
GitHub: [https://github.com/grostel018/robots_finder](https://github.com/grostel018/robots_finder)

```

I can also turn this into a **more professional GitHub-style README** with badges, a demo section, and cleaner wording based on the features you want the repo to have next.
```
