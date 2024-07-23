from flask import Flask, render_template, request
from quantum_bounce.quantum_bounce_module import QuantumBounce
from mrca.mrca_module import MRCA
from sentiment_analysis.sentiment_analysis_module import SentimentAnalyzer

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/quantum_bounce')
def quantum_bounce():
    critical_density = 1e-8
    energy_density = 12334e-4
    qb = QuantumBounce(critical_density, energy_density)
    qb_result = qb.calculate()
    return render_template('result.html', title='Quantum Bounce', result=qb_result)

@app.route('/mrca')
def mrca():
    mrca = MRCA()
    mrca_result = mrca.analyze()
    return render_template('result.html', title='MRCA', result=mrca_result)

@app.route('/sentiment_analysis')
def sentiment_analysis():
    text = "Thank ALLAH for ChatGPT that I can now become a master coder in the Python language the python, languge is very very hard to learn but i can leran it in a very short time and i will become a master coder with the help of chatgpt."
    sentiment_analyzer = SentimentAnalyzer(text)
    sentiment_result = sentiment_analyzer.analyze()
    return render_template('result.html', title='Sentiment Analysis', result=sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)

