from flask import Flask, request, jsonify, render_template
import requests
from EmotionDetection.emotion_detection import emotion_detector

app  = Flask(__name__)

@app.route("/EmotionDetection")
def emotion_detection():
    text_to_analyse = request.args.get("textToAnalyze")
    Response = emotion_detector(text_to_analyse)
    if not Response:
        return jsonify({"error": "No response from emotion detection service"}), 500
    emotions = {k: v for k, v in Response.items() if k != 'dominant_emotion'}
    dominant = Response['dominant_emotion']

    # Format emotions as: 'anger': 0.0062, etc.
    emotions_str = ', '.join([f"'{k}': {v}" for k, v in emotions.items()])

    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant}."
    
@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)