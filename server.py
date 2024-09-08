"""
This is a docstring for my_module
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This is a docstring for def emo_detector()
    """
    text_to_analyze = request.args.get("textToAnalyze")

    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': \
    {dominant_emotion['anger']}, 'disgust': {dominant_emotion['disgust']}, \
    'fear': {dominant_emotion['fear']}, 'joy': {dominant_emotion['joy']} and \
    'sadness': {dominant_emotion['sadness']}. The dominant emotion is \
    {dominant_emotion['dominant_emotion']}"

@app.route("/")
def render_index_page():
    """
    This is a docstring for def render_index_page()
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
