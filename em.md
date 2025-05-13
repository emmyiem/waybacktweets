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
cd waybacktweets```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate```

### 3. Install dependencies

```bash
pip install -r requirements.txt```

Make sure you have these Python packages installed:

tqdm

beautifulsoup4

ratelimit

requests

## 🛠 Usage

### Step 1: Organize your tweet data

Place all your .json, .csv, or .html Twitter exports into a folder named after the Twitter username (e.g., username/).

Example folder structure:

pgsql

waybacktweets/
│
├── username/
│   ├── tweets.json
│   └── tweets.csv

### Step 2: Generate the Markdown report

Run the xx.py script:

```bash
python3 xx.py``

You will be prompted:

```yaml
Enter the folder name: username
This will generate a file like username/username_tweets.md, formatted like this:

markdown

# Tweets Report — @emsteck

**Total Tweets:** 150

---

- **09 May 2025**: [RT] `Tweet text` [Original](https://twitter.com/example/status/123) ([Archive](https://web.archive.org/...)) — ⏳ Unknown
- **08 May 2025**: `Tweet text` [Original](https://twitter.com/example/status/456) ([Archive](https://web.archive.org/...)) — ⏳ Unknown
The “⏳ Unknown” status will later be updated by the deletion checker.

###Step 3: Check for deleted tweets
Once you have your Markdown file, run the deletion check with:

```bash
python3 check_deletions.py```

You will be prompted:

```pgsql
Enter path to Markdown file (e.g., username/username_tweets.md):
Example input:

```bash
emsteck/emsteck_tweets.md```

The script will:

Check each tweet link for availability.

Update the deletion status in each Markdown bullet.

Insert a summary like this at the top of the file:

markdown
**🧾 Tweet Deletion Summary**

- ✅ Available: 140  
- ❌ Deleted: 8  
- ⏳ Unknown: 2

---
⏳ A progress bar will show you how long it takes to check the tweets.

📸 Screenshots
Add screenshots to the screenshots/ folder to illustrate:

The input folder structure

Example terminal output

Example Markdown report with deletion summary

🔧 File Reference
File	Purpose
xx.py	Parses tweets and generates the Markdown report
check_deletions.py	Checks tweet links and updates deletion status
requirements.txt	Required dependencies
emsteck_tweets.md	Example generated Markdown
screenshots/	Folder to store example images for documentation

