#import libaries
import nltk
import pandas as pd
import seaborn as sn 
from bs4 import BeautifulSoup 
import random
from wordcloud import wordcloud
import urllib as req 

#setting up the url for canadian law
resp = req.urlopen("https://www.canada.ca/en/health-canada/corporate/about-health-canada/legislation-guidelines/acts-regulations/list-acts-regulations.html") #this is the response object

