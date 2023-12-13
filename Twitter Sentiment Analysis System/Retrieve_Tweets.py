import credentials
import tweepy 
from tweepy import OAuthHandler 
import pandas as pd
from datetime import date
import datetime
import unicodedata


# keys and tokens from the Twitter Dev Console 
consumer_key = credentials.API_KEY
consumer_secret = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET
  
# attempt authentication 
try: 
    # create OAuthHandler object 
    auth = OAuthHandler(consumer_key, consumer_secret) 
    # set access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    # create tweepy API object to fetch tweets 
    api = tweepy.API(auth) 
except: 
    print("Error: Authentication Failed") 


def get_tweets(query, count): 
    
    tweets = [] 
    Date = date.today() 
  
    try: 
            # call twitter api to fetch tweets 
        fetched_tweets = api.search(q = query, count = count, lang='en', result_type = 'recent') 
  
        # parsing tweets one by one 
        for tweet in fetched_tweets: 
            if tweet.retweet_count<100:
                   # empty dictionary to store required params of a tweet 
                unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')
                parsed_tweet = {} 
      
                    # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # fetching the user 
                parsed_tweet['retweet_count'] = tweet.retweet_count
                
                
                # fetching the followers_count 
    
      
                    # appending parsed tweet to tweets list 
            
                if tweet.retweet_count > 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
      
            # return parsed tweets 
        #print(tweets)
        df = pd.DataFrame(tweets)
        return df
  
    except tweepy.TweepError as e: 
            # print error (if any) 
        print("Error : " + str(e)) 
        



def store_tweets(df):
    filename = "retrieved_tweets.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()
    df.to_csv(filename, index=False)
    return 
    


