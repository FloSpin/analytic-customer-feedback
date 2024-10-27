''' Server code for emotion detection '''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' Emotion detector '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions['joy'] is None:
        return "Invalide input! Try again"
    response = (f"For the given statement, the system response is "
                f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
                f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}"
                f" and 'sadness': {emotions['sadness']}. "
                f"The dominant emotion is {emotions['dominant_emotion']}.")
    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
