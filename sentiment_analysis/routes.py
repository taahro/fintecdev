from flask import Blueprint, render_template, request
from .sentiment_analysis_module import SentimentAnalyzer

sentiment_analysis_bp = Blueprint('sentiment_analysis', __name__)

@sentiment_analysis_bp.route('/', methods=['GET', 'POST'])
def analyze_sentiment():
    if request.method == 'POST':
        text = request.form['text']
        sentiment_analyzer = SentimentAnalyzer(text)
        result = sentiment_analyzer.analyze()
        return render_template('results.html', task='Sentiment Analysis', result=result)
    return render_template('sentiment_analysis.html')
