# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:54:41 2020

@author: Jeffrey David
"""
import Retrieve_Tweets as rt
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import re


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

  
lemmatizer = WordNetLemmatizer() 
Stopwords = stopwords.words('english')
Extra_Stopwords=['.',',','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','\"','\'','RT','<',',','>','.','?','/']
Stopwords = Stopwords + Extra_Stopwords
Stopwords.remove('not')
bad_chars = ['–', '’', '…', '“', 'Ÿ', 'Ž', '¯', '*', '‡', '‘']


def remove_non_ascii(text): 
    return ''.join(i for i in text if ord(i)<128)

def preprocess(tweets):
    #removing Non ASCII characters
    tweets['text'] = tweets['text'].apply(remove_non_ascii)
    
    processed_sentences =[]
    #iterating over the list of tweets
    for sentence in tweets['text']:  
        #To remove the insignifican Characters
        for i in bad_chars:
            sentence = sentence.replace(i, "")
            
        #To remove Emojis    
        sentence = deEmojify(sentence)
        
        #Tokenizing the sentence
        sentence = word_tokenize(sentence)
        
        #Removing URLs and Mentions
        for i,w in enumerate(sentence):
            if w[0] == '@' or w[0] == '#' or w[0] == '&':
                del sentence[i]
                try:
                    del sentence[i]
                except:
                    print()
            if w[0:2] == '//' or w[0:4] == 'http' or w[-3:] == '.com':
                del sentence[i]  
                
        #Removing Stopwords
        sentence = [w for w in sentence if w.lower() not in Stopwords]
        
        #Lemmatizing the words
        sentence = [lemmatizer.lemmatize(l) for l in sentence]
        processed_sentence = ''     
        for j in sentence:           
            processed_sentence = processed_sentence + ' ' + j
        processed_sentences.append(processed_sentence)
    tweets['preprocessed_text'] = processed_sentences
    processed_tweets = tweets
    return(processed_tweets)

