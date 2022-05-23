import os
import tweepy
import pandas as pd

#Twitter API Keys
Consumer_Key ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
Consumer_Secret ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
Access_Token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
Access_Token_Secret ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#Authendication
auth = tweepy.OAuth1UserHandler(
    Consumer_Key,
    Consumer_Secret,
    Access_Token,
    Access_Token_Secret   
)
api = tweepy.API(auth)


#Extract Tweets
 tweets_copy = []
for tweet in tweepy.Cursor(api.search_tweets, 
                            "#walmart", 
                            lang="en").items(50):
    tweets_copy.append(tweet)
    

# Intialize the dataframe
tweets_df = pd.DataFrame()


# Populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({'text': text, 
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop=True)

# Show the dataframe
tweets_df.head()