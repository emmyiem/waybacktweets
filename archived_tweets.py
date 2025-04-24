from waybacktweets import WaybackTweets
from datetime import datetime

# Prompt for Twitter username
USERNAME = input("Enter the Twitter username (without @): ").strip()
api = WaybackTweets(USERNAME)
archived_tweets = api.get()

def format_date(timestamp):
    """Convert timestamp to DAY MONTH YEAR format."""
    try:
        dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
        return dt.strftime("%d %B %Y")
    except Exception:
        return timestamp

def is_deleted(status_code):
    return status_code == "404"

if archived_tweets:
    deleted_count = 0
    live_count = 0
    total_count = len(archived_tweets)
    markdown_lines = []

    for tweet in archived_tweets:
        timestamp = tweet.get("timestamp")
        original_url = tweet.get("original")
        status_code = tweet.get("statuscode")
        formatted_date = format_date(timestamp)
        deleted = is_deleted(status_code)

        if deleted:
            deleted_count += 1
            status_label = ""
        else:
            live_count += 1
            status_label = " _(live)_"

        markdown_line = f"[{formatted_date}]({original_url}): Tweet content not available{status_label} <!--{tweet.get('urlkey')}-->\n"
        markdown_lines.append(markdown_line)

    # Markdown summary header
    summary = (
        f"The list below includes **{deleted_count} deleted tweets** out of "
        f"**{total_count} total archived tweets** by "
        f"[{USERNAME}](https://twitter.com/{USERNAME}).\n\n"
        f"There are also **{live_count} tweets** that are indicated as "
        f"**not currently deleted** by the Twitter API but have been scraped from pages of deleted tweets (as replies, etc.). "
        f"These possibly undeleted tweets are included for context and are indicated by a _(live)_ link.\n\n"
    )

    # Write to file
    output_file = f"{USERNAME}_archived_tweets.md"
    with open(output_file, "w") as f:
        f.write(summary + "".join(markdown_lines))

    print(f"✅ Done! Markdown saved to: {output_file}")
else:
    print(f"No archived tweets found for @{USERNAME}.")
