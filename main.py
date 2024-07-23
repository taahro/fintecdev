from quantum_bounce.quantum_bounce_module import QuantumBounce
from mrca.mrca_module import MRCA
from sentiment_analysis.sentiment_analysis_module import SentimentAnalyzer

def main():
    # Quantum Bounce calculation
    qb = QuantumBounce(critical_density=1e-8, energy_density=12334e-4)
    qb_result = qb.calculate()
    print(f"Quantum Bounce Result: {qb_result}")

    # MRCA analysis
    mrca = MRCA()
    mrca_result = mrca.analyze()
    print(f"MRCA Result: {mrca_result}")

    # Sentiment Analysis
    text = "Thank ALLAH for ChatGPT that I can now become a master coder in the Python language the python, languge is very very hard to learn but i can leran it in a very short time and i will become a master coder with the help of chatgpt."
    sentiment_analyzer = SentimentAnalyzer(text)
    sentiment_result = sentiment_analyzer.analyze()
    print(f"Sentiment Analysis Result: {sentiment_result}")

if __name__ == "__main__":
    main()


