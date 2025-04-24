from waybacktweets import WaybackTweets

# Prompt for Twitter username
USERNAME = input("Enter the Twitter username (without @): ").strip()

# Get archived tweets
api = WaybackTweets(USERNAME)
archived_tweets = api.get()

# Print the archived tweets structure to understand the exact field names
print("Archived Tweets:")
for tweet in archived_tweets:
    print(tweet)  # Print out each tweet to see its structure
    break  # Print just the first tweet to avoid printing too many lines

# Once you see the structure, you will be able to adjust field options accordingly
