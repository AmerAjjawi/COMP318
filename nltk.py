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

import urllib as req 

#request url for canadian law
resp = req.urlopen("https://www.canada.ca/en/health-canada/corporate/about-health-canada/legislation-guidelines/acts-regulations/list-acts-regulations.html") #this is the response object

#read the webpage
canadian_law = resp.read()
print(canadian_law)