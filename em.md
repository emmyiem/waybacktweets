# 🐦 waybacktweets + Deletion Checker

This project helps you collect, process, and report tweets from Twitter archive files (`.json`, `.csv`, or `.html`) and generate a clean Markdown report sorted by date. It also includes a separate script to check if those tweets have been deleted.

---

## 📦 Features

- Parses tweets from multiple formats.
- Generates Markdown reports organized by date.
- Detects retweets.
- Extracts dates from multiple sources.
- Sorts by available metadata (archived URL, tweet text, etc).
- Separate checker for deleted tweets.
- Progress bars and logging throughout.
- Lightweight and customizable.

---

## ✅ Setup

### 1. Clone this repository

```bash
git clone https://github.com/claromes/waybacktweets.git
cd waybacktweets

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate```

###3. Install dependencies
```bash
pip install -r requirements.txt```

Make sure you have these Python packages installed:

tqdm

beautifulsoup4

ratelimit

requests

