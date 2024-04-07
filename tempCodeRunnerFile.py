nltk.downloader.down('vader_lexicon')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
vad_object = SentimentIntensityAnalyzer()
print(vad_object.polarity_scores(canLaw))