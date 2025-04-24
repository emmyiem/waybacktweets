from waybacktweets import WaybackTweets, TweetsParser
from datetime import datetime

# Define the username and other parameters
USERNAME = "emsteck"  # Replace with the target Twitter username
api = WaybackTweets(USERNAME)
archived_tweets = api.get()

# If archived tweets are found, process and export to markdown
if archived_tweets:
    # Debug: Print the structure of the first tweet in the archived_tweets list
    print(archived_tweets[0])  # This will print the structure of the first tweet
    
    # Define fields to include in the markdown format based on the available fields
    field_options = [
        "timestamp",  # Use timestamp for the date
        "original",  # Use original tweet URL
        "statuscode",  # Use status code to determine if tweet is deleted
    ]
    
    # Parse the archived tweets
    parser = TweetsParser(archived_tweets, USERNAME, field_options)
    parsed_tweets = parser.parse()

    # Define a function to convert the timestamp to DAY MONTH YEAR format
    def format_date(timestamp):
        """Convert the timestamp to DAY MONTH YEAR format."""
        try:
            dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
            return dt.strftime("%d %B %Y")
        except ValueError:
            return timestamp  # Return original timestamp if parsing fails

    def is_tweet_deleted(status_code):
        """Determine if the tweet is deleted based on the status code."""
        if status_code == "404":
            return "Deleted"
        return "Not Deleted"

    def tweets_to_markdown(parsed_tweets):
        markdown_content = []

        # Initialize counters for deleted and live tweets
        deleted_count = 0
        live_count = 0
        total_count = len(parsed_tweets)  # Total number of archived tweets

        # Loop through each tweet and determine if it's deleted or not
        for tweet in parsed_tweets:
            timestamp = tweet.get("timestamp", "No Timestamp")
            original_url = tweet.get("original", "#")
            status_code = tweet.get("statuscode", "N/A")
            
            # Convert timestamp to desired format
            formatted_date = format_date(timestamp)
            
            # Determine tweet status and count
            tweet_status = is_tweet_deleted(status_code)
            if tweet_status == "Deleted":
                deleted_count += 1
            else:
                live_count += 1
            
            # Format the tweet in markdown style
            markdown_tweet = f"[{formatted_date}]({original_url}): Tweet content not available <!--Tweet ID-->\n"
            # Add a line for whether the tweet is deleted or not
            tweet_status_line = f"**Tweet Status**: {tweet_status}\n\n"
            markdown_content.append(markdown_tweet + tweet_status_line)

        # Add the breakdown of deleted and live tweets at the top in the requested format
        markdown_header = f"The list below includes **{deleted_count} deleted tweets** out of **{total_count} total archived tweets** by [{USERNAME}](https://twitter.com/{USERNAME}).\n\n"
        markdown_header += f"There are also **{live_count} tweets** that are indicated as **not currently deleted** by the Twitter API but are scraped from pages of deleted tweets (as replies, etc.).\n"
        markdown_header += f"These possibly undeleted tweets are included for context and are indicated by a _(live)_ link.\n\n"
        
        # Return the final markdown content with the header
        return markdown_header + "".join(markdown_content)

    # Convert parsed tweets to markdown
    markdown_data = tweets_to_markdown(parsed_tweets)

    # Save the markdown content to a file
    with open(f"{USERNAME}_archived_tweets.md", "w") as md_file:
        md_file.write(markdown_data)
    
    print(f"Archived tweets for {USERNAME} have been saved to {USERNAME}_archived_tweets.md")
else:
    print(f"No archived tweets found for {USERNAME}.")
