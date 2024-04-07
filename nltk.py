#import libaries
import nltk
import pandas as pd
import seaborn as sn 
from bs4 import BeautifulSoup 
import random
from wordcloud import wordcloud
import os
import spacy 
nlp = spacy.load('en_core_web_sm') #assigns specific token vectors


import urllib.request

#request url for canadian law
with urllib.request.urlopen("https://www.canada.ca/en/health-canada/corporate/about-health-canada/legislation-guidelines/acts-regulations/list-acts-regulations.html") as url: #this is the response object

    canLaw = url.read()

print(canLaw)

#tokenize and split the strings
token_split = canLaw.split()
import pprint 
#printing the first 400 words
pprint.pprint(token_split[:400])
#convert from binary to string
import re
canLaw = str(canLaw, 'utf-8')
#grab the raw data and split it
token_with_re = re.split(r'\W+', canLaw)
#printing the length
print("len(token_with_re)")
print(len(token_with_re))
print("up to 600 tokens from token_with_re")
print(token_with_re[:600])
import pprint
pprint.pprint(token_with_re[:600])

#use beautiful soup
#import nltk
#from bs4 import BeautifulSoup
#from pprint import pprint
#create beautiful soup object and parsing the data
get_soup = BeautifulSoup(canLaw, 'html.parser')
#get text from soup
extract_text = get_soup.get_text()
# split data
split_data = [token for token in extract_text.split()]
#pprint 
pprint.pprint(split_data)

#display length of data
print(len(split_data))

#displaying range from 400 to 2299
pprint.pprint(split_data[400:2300])


#polish text 
#shows the full html - maybe delete
polish_text = canLaw.replace("n", " ")
polish_text = polish_text.replace("/", " ")
polish_text = ''.join(c for c in polish_text if c != " ")
pprint.pprint(polish_text)




