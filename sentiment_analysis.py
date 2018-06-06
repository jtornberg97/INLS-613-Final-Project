# import textblob
from textblob import TextBlob

# Inputting CSV files
import csv

# For regular expression
import re

# For sorting dictionaries
import operator

# To plot results
import numpy as numpy
import matplotlib as matplotlib
import matplotlib.pyplot as plt

# Empty Twitter array
tweets = []

# A helper function to remove all non ASCII characters
def strip_non_asii(string):
    '''returns string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# Load file and process each row
# File has 2 rows we are concerned with
    #0. Tweet text
    #1. Tweet ID

#Create data structure for tweets:
    # id: Tweet ID
    # orig: The original, unpreprocessed string
    # clean: The preprocessed string
    # TextBlob: The textblob oject, created from 'clean' string

with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
    reader._next_()
    for row in reader:

        tweet = dict()
        tweet['orig'] = row[0]
        tweet['id'] = int(row[1])

        tweet['clean'] = tweet['orig']

        # Remove all non-ascii characters
        tweet['clean'] = strip_non_asii(tweet['clean'])

        # Downcase
        tweet['clean'] = tweet['clean'].lower()

        # Remove URLS
        tweet['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet['clean'])

        # Understanding Slang
        tweet['clean'] = re.sub(r'\bthats\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bive\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\bim\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bya\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcant\b', 'can not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwont\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bid\b', 'i would', tweet['clean'])
        tweet['clean'] = re.sub(r'wtf', 'what the fuck', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwth\b', 'what the hell', tweet['clean'])
        tweet['clean'] = re.sub(r'\br\b', 'are', tweet['clean'])
        tweet['clean'] = re.sub(r'\bu\b', 'you', tweet['clean'])
        tweet['clean'] = re.sub(r'\bk\b', 'OK', tweet['clean'])
        tweet['clean'] = re.sub(r'\bsux\b', 'sucks', tweet['clean'])
        tweet['clean'] = re.sub(r'\bno+\b', 'no', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcoo+\b', 'cool', tweet['clean'])

        # Create textblob object
        tweet['TextBlob'] 

        # Correct spelling (SLOW)
        #tweet['TextBlob'] = tweet['TextBlob'].correct()

        tweets.append(tweet)

# Develop Models

for tweet in tweets:
    tweet['polarity'] = float(tweet['TextBlob'].sentiment.polarity)
    tweet['subjectivity'] = float(tweet['TextBlob'].sentiment.subjectivity)

    if tweet['polarity'] >= 0.1:
        tweet['sentiment'] = 'positive'
    elif tweet['polarity'] <= 0.1: 
        tweet['sentiment'] = 'negative'
    else:
        tweet['sentiment'] = 'netural'

tweets_sorted = sorted(tweets, key=lambda k: k['polarity'])


