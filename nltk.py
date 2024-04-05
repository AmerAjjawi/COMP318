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

#fix add remove of alphanumerical
#clean_text = [re.sub(r'[^0-9a-zA-Z\s]+', '', token_with_re).lower() for token in token_with_re if token.strip() != " "] 