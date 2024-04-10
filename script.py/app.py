""" This project is about scrapping, transforming, removing, displaying data
"""

# 1 add the proper module
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pprint
import re
import nltk
import urllib.request
from pattern.text.en import wordnet
from nltk.corpus import wordnet as wn
import pandas as pd
import seaborn as sn
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import spacy
nlp = spacy.load('en_core_web_sm')

with urllib.request.urlopen('https://www.canada.ca/en/canadian-heritage/services/how-rights-protected/guide-canadian-charter-rights-freedoms.html#a3') as url:
    charter_rights = url.read()
    # Reading and printing this data gives html
print(charter_rights)


# use beautiful_soup
soup = BeautifulSoup(charter_rights, "html.parser")
pretty_soup = soup.get_text()
tokenized_soup = nltk.tokenize.word_tokenize(soup.get_text())
pprint.pprint(tokenized_soup[0:20])


# filter out text
words = [word for word in tokenized_soup if word.isalpha()]
print(words[0:20])


# use textblob to give score -> of polarity


text_blobs = []
for w in words:
    new_blob = TextBlob(w)
    a = new_blob.sentiment.polarity
    b = new_blob.sentiment.subjectivity
text_blobs.append([w, a, b])
print(text_blobs)

# seaborn
df_sentiment = pd.DataFrame(data=text_blobs, columns=[
                            "text_blobs", "Polarity", "Subjectivity"])
df_sentiment.head()
df_sentiment.info()

sn.displot(df_sentiment[0:5], height=4, aspect=1.8)
plt.xlabel("graph")
plt.show()


# using pattern
nltk.download('vader_lexicon')
vad_object = SentimentIntensityAnalyzer()
pattern_object = (vad_object.polarity_scores(words[:50]))
# print(pattern_object)
keys_pattern = {k: v for k, v in pattern_object.items()}
new_polarity_scores = (vad_object.polarity_scores(keys_pattern))
df_pattern = pd.DataFrame(data=new_polarity_scores, columns=[
                          "words", "polarity", "subjectivity"])
df_pattern.head()
df_pattern.info()

# find the frquenecy
freq_dis = nltk.FreqDist(words)
freq_dis.plot(20)

# convert to string
new_string = ''.join([s for s in words if not s.isdigit()])

# plotting data
plt.subplots(figsize=(16, 10))
wordcloud = WordCloud(
    background_color='black',
    max_words=10,
    width=1400,
    height=1200
).generate(new_string)
plt.imshow(wordcloud)
plt.title('Canadian Legalisation')
plt.axis('off')
plt.show()
