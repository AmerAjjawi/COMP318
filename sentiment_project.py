# import libaries
from textblob import TextBlob
import pprint
import re
import urllib.request
from pattern.text.en import wordnet
from nltk.corpus import wordnet as wn
import sentiment_project
import pandas as pd
import seaborn as sn
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import random
from wordcloud import wordcloud
import os
import spacy
nlp = spacy.load('en_core_web_sm')  # assigns specific token vectors
# from textblob import TextBlob

# request url for canadian law
with urllib.request.urlopen("https://www.canada.ca/en/health-canada/corporate/about-health-canada/legislation-guidelines/acts-regulations/list-acts-regulations.html") as url:  # this is the response object

    canLaw = url.read()

print(canLaw)

# tokenize and split the strings
token_split = canLaw.split()
# printing the first 400 words
pprint.pprint(token_split[:400])
# convert from binary to string
canLaw = str(canLaw, 'utf-8')
# grab the raw data and split it
token_with_re = re.split(r'\W+', canLaw)
# printing the length
print("len(token_with_re)")
print(len(token_with_re))
print("up to 600 tokens from token_with_re")
print(token_with_re[:600])
pprint.pprint(token_with_re[:600])

# use beautiful soup
# import nltk
# from bs4 import BeautifulSoup
# from pprint import pprint
# create beautiful soup object and parsing the data
get_soup = BeautifulSoup(canLaw, 'html.parser')
# get text from soup
extract_text = get_soup.get_text()
# split data
split_data = [token for token in extract_text.split()]
# pprint
pprint.pprint(split_data)

# display length of data
print(len(split_data))

# displaying range from 400 to 2299
pprint.pprint(split_data[400:2300])


# polish text
# shows the full html - maybe delete later
polish_text = canLaw.replace("n", " ")
polish_text = polish_text.replace("/", " ")
polish_text = ''.join(c for c in polish_text if c != " ")
pprint.pprint(polish_text)


# split the texts in individual sentences
individual_sentences = []
tokens = nlp(polish_text)
for sent in tokens.sents:
    individual_sentences.append((sent.text.strip()))
print(individual_sentences)
print(len(individual_sentences))

# print the sentences from index 10 to 20
print(individual_sentences[10:20])

# try to use textblob to give the score of polarity -> either postive or negative and subjectivity between 0 & 1
TextBlob_sentences = []
for s in individual_sentences:
    text = TextBlob(s)
    a = text.sentiment.polarity
    b = text.sentiment.subjectivity
    TextBlob_sentences.append([s, a, b])

# transform the data from list to a table using pandas

df_sentiment = pd.DataFrame(data=TextBlob_sentences, columns=[
                            'individual_sentences', 'Polarity', 'Subjectivity'])

df_sentiment.head()
df_sentiment.info()

# data has 58 sentences and their polarity and subjectivity scores
# seaborn uses Matplotlib to visualize distributions
# display the polarity & subjectivity from the textblob
sn.displot(df_sentiment["Polarity"], height=5, aspect=1.8)
plt.xlabel("Displaying the subjectivity in textblob")
plt.show()

sn.displot(df_sentiment["Subjectivity"], height=5, aspect=1.8)
plt.xlabel("Displaying the subjectivity in textblob")
plt.show()
