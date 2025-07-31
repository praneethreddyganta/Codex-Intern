# Sentiment Analysis Web Application

This web application allows users to enter text and receive a sentiment classification (**Positive**, **Negative**, or **Neutral**) along with detailed polarity and subjectivity scores. Built with Python using Flask (or Django) and powered by the TextBlob library.

---

## Features

- Simple web interface for user text input
- Instant sentiment classification: **Positive**, **Negative**, or **Neutral**
- Displays both **polarity** and **subjectivity** scores for each input
- Built with [TextBlob](https://textblob.readthedocs.io/en/dev/) for robust NLP

---

## Demo

_A screenshot or GIF here (optional)_

---

## Technologies Used

- Python 3.8+
- Flask (or Django)
- TextBlob
- HTML/CSS (Templates)
- Bootstrap (optional, for styling)

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/your-username/sentiment-analysis-app.git
    cd sentiment-analysis-app
    ```

2. **Create a virtual environment and activate it:**
    ```
    python -m venv venv
    source venv/bin/activate        # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the web application:**
    ```
    # If using Flask:
    flask run

    # If using Django:
    python manage.py runserver
    ```

---

## Usage

- Open your browser and navigate to `http://127.0.0.1:5000/` (Flask) or `http://127.0.0.1:8000/` (Django).
- Enter or paste your text in the input field.
- Submit to see the sentiment result, polarity, and subjectivity scores displayed on the page.

---

## Example Output

- **Input:**  
    `I love this product! It works perfectly.`

- **Output:**  
    - **Sentiment:** Positive
    - **Polarity:** 0.625
    - **Subjectivity:** 0.6

---


---

## requirements.txt Example
*or for Django:*

Remember to also download TextBlob corpora:

---

## Acknowledgements

- Built with [Flask](https://flask.palletsprojects.com/) / [Django](https://www.djangoproject.com/)
- Sentiment analysis by [TextBlob](https://textblob.readthedocs.io/)

---




