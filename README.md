# Twitter-Sentiment-Analysis-System
A Twitter sentiment analysis system built using python with Naive Bayes Model.

## SYSTEM ARCHITECTURE
The sentiment analysis system contains of five major parts


![System Architecture](https://github.com/Jeffrey-David/Twitter-Sentiment-Analysis-System/assets/66271004/93578e0b-f64d-4ceb-a304-cf0a599889a4)

 
### Tweet Extraction
The first step to implementing the sentiment analysis system is to create a Twitter Developer account and get it approved so that we can access it through the Twitter API. After we get access to a developer account, we should extract and store the tweets that correspond to the given query term. For this we can use the Tweepy  to retrieve the tweets. The below picture is the dashboard of a Twitter Developer account.
 
### Cleaning the Tweets 
The retrieved tweets must be preprocessed and cleaned as they may contain irrelevant and unwanted data that may lead to wrong results while classifying them. We first remove the stopwords like articles, adjectives, special characters and others that does not contribute to the sentiment of the system. Then we Lemmatize the remaining words. Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma.  

### Training a Naïve Bayes Model
Here we have to train a Naïve Bayes model which can predict the sentiment of the tweets with high accuracy. For this we have to select a good fitting dataset and make the model learn the dataset and do predictions for the given tweets.

### Classification of Tweets
The retrieved tweets are sent to the machine learning model that we have trained and the sentiments are given as output by the model. We will use the Sentiments received and classify the tweets into positive and negative.

### Visualize the Sentiment of the Tweets
Finally we visualize the output in the form of a pie chart representing the percentage of posive, neutran and negative tweets. This can be used by the user for finding out an overall review of the brand i.e. the query term.

