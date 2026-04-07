# robots_finder
a script for OSİNT


Robots Finder

A fast and efficient command-line tool designed to locate, fetch, and analyze robots.txt files from target domains to identify disallowed paths and crawl rules.
Features

    Scans multiple domains/URLs simultaneously.
    Identifies hidden directories and sensitive paths listed in robots.txt.
    Validates URL status codes.
    Export results to text or JSON formats.
    User-agent customization.

Tech Stack

    Language: Python 3.x
    Libraries: requests, argparse, colorama

Setup
Prerequisites

    Python 3.7 or higher installed.

Installation

 copy

bash
# Clone the repository
git clone https://github.com/grostel018/robots_finder.git

# Navigate to the project directory
cd robots_finder

# Install dependencies
pip install -r requirements.txt

Usage
Basic Scan

 copy

bash
python robots_finder.py -u https://example.com

Scan from a List of Domains

 copy

bash
python robots_finder.py -l domains.txt

Save Output

 copy

bash
python robots_finder.py -u https://example.com -o results.json

Configuration

Options can be passed via command-line arguments:

    -u, --url: Target URL.
    -l, --list: Path to a file containing a list of targets.
    -o, --output: Save results to a specific file.
    -t, --timeout: Set request timeout (default: 5s).

API Documentation

If used as a module:

 copy

python
from robots_finder import RobotsScanner

scanner = RobotsScanner()
results = scanner.fetch("https://example.com")
print(results.disallowed_paths)

Testing

Run tests using pytest:

 copy

bash
pytest tests/

Deployment

This tool is designed to run locally. Ensure you have network access to the target domains.
Contributing

    Fork the repository.
    Create a feature branch (git checkout -b feature/NewFeature).
    Commit your changes (git commit -m 'Add NewFeature').
    Push to the branch (git push origin feature/NewFeature).
    Open a Pull Request.

License

Distributed under the MIT License. See LICENSE for more information.
Contact

Project Link: https://github.com/grostel018/robots_finder
