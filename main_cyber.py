from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_text = data.get("text", "")

    if not user_text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Sentiment analysis
    blob = TextBlob(user_text)
    sentiment_score = blob.sentiment.polarity

    # Determine sentiment
    if sentiment_score > 0:
        sentiment = "😊 Positive"
    elif sentiment_score < 0:
        sentiment = "😞 Negative"
    else:
        sentiment = "😐 Neutral"

    return jsonify({
        "sentiment": sentiment,
        "score": sentiment_score
    })

PORT = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
