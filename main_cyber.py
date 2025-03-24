from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)

# Allow all origins or specify the frontend origin
CORS(app, resources={r"/*": {"origins": "*"}})   # Allow all origins
# OR to be more secure, specify the frontend origin only
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5501"}})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    if text:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        return jsonify({
            "polarity": polarity,
            "subjectivity": subjectivity
        })
    return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
