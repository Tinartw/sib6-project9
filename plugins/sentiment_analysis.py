import re
from textblob import TextBlob


class SentimentAnalysis:

    def _init_(self, tweet):
        self.tweet = tweet

    # only for english language
    def execute(self):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.tweet)

        # set sentiment
        if analysis.sentiment.polarity > 0:
            data = {'text': self.tweet, 'sentiment': 'positive'}
        elif analysis.sentiment.polarity == 0:
            data = {'text': self.tweet, 'sentiment': 'neutral'}
        else:
            data = {'text': self.tweet, 'sentiment': 'negative'}

        return data

if _name_ == "_main_":
    # calling main function
    SentimentAnalysis('hard to learn NLTK').execute()