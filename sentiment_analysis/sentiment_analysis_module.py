from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("The `text` argument must be a string.")
        self.text = text

    def analyze(self):
        # Perform sentiment analysis
        blob = TextBlob(self.text)
        sentiment_score = blob.sentiment.polarity  # Polarity score
        return {'text': self.text, 'score': sentiment_score}

