# app.py

from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = 0
    subjectivity = 0
    text = ""

    if request.method == 'POST':
        text = request.form['text']
        if text:
            # Create a TextBlob object
            blob = TextBlob(text)
            
            # Get polarity and subjectivity
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

            # Classify sentiment
            if polarity > 0.1:
                sentiment = 'Positive'
            elif polarity < -0.1:
                sentiment = 'Negative'
            else:
                sentiment = 'Neutral'

    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity, text=text)

if __name__ == '__main__':
    app.run(debug=True)