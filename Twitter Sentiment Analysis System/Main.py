# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:35:01 2020

@author: Jeffrey David
"""

import Retrieve_Tweets as RT
print("Retrieve_Tweets Module has been imported\n")
import preprocessing as PPR
print("preprocessing Module has been imported\n")
# import Naive_Bayes as TNB
import visualize as VZ
print("visualize Module has been imported\n")
import classifier as CL
print("classifier Module has been imported\n")

query = input("Enter the Brand name\t\t")
count = input("Enter the number of tweets to process\t\t")

tweets = RT.get_tweets(query,count)

print("No of Tweets retrieved:  ", tweets.shape[0])
processed_tweets = PPR.preprocess(tweets)


Final = CL.Add_Sentiment(processed_tweets)
# Final = TNB.Add_Sentiment(Final)

# Final_Sentiment = []
# k=0
# for j in Final['Sentiments']:
#     if j == 0:
#         Final_Sentiment.append(0)
#     if j!=0:
#         Final_Sentiment.append(Final['Sentiment'][k])
#     k = k+1

# Final['Tweet_Sentiment'] = Final_Sentiment
# Final = Final.drop(['Sentiment', 'Sentiments'], axis = 1)
        
Final['retweet_count'] = Final['retweet_count']+1
Final = Final.rename(columns={"retweet_count": "Tweet_Count"})
RT.store_tweets(Final)
print("The result is stored in a retrieved_tweets.csv file")

VZ.visual(Final)




