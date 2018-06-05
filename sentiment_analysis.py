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
    reader.next()
    for row in reader:

        tweet = dict()
        tweet['orig'] = row[0]
        tweet['id'] = int(row[1])

        tweet['clean'] = tweet['orig']

        # Remove all non-ascii characters
        tweet['clean'] = strip_non_asii(tweet['clean'])
        
