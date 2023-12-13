# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 04:50:52 2020

@author: Jeffrey David
"""
import matplotlib.pyplot as plt

def visual(df):
    Sentiment = df['Sentiment']
    No_Tweets = df['Tweet_Count']
    positive = 0
    negative = 0
    for i,j in enumerate(Sentiment):
        if j ==0:
            negative = negative + No_Tweets[i]
        else:
            positive = positive + No_Tweets[i]
            
            
    print('Positive: ',positive,'\nNegative: ', negative)
    

    # Pie chart
    labels = 'Positive', 'Negative'
    sizes = [positive, negative]
    explode = (0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.show()