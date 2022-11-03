import tweepy
import pandas as pd
import time


consumer_key = "7vvk6JmaYEH7Fm3dhKznjD5w6"  # Your API/Consumer key
consumer_secret = "ZOzh0HcF8WfBLAGXH6qOsVHYTdXRcT7lgUApXNaJRZtU1w72Nk"  # Your API/Consumer Secret Key
access_token = "XXXX"  # Your Access token key
access_token_secret = "XXXX"  # Your Access token Secret key

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

username = "john"
no_of_tweets = 100

try:
    # The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)

    # Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count, tweet.source, tweet.text] for tweet in tweets]

    # Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,', str(e))
    time.sleep(3)


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
