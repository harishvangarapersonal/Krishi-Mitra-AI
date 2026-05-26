from flask import Flask, render_template, request

import pickle
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# =========================================
# FLASK APP
# =========================================

app = Flask(__name__)

# =========================================
# LOAD MODEL & VECTORIZER
# =========================================

model = pickle.load(
    open("models/career_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

# =========================================
# NLP SETUP
# =========================================

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

# =========================================
# TEXT PREPROCESSING
# =========================================

def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        f"[{string.punctuation}]",
        " ",
        text
    )

    text = re.sub(r'\d+', '', text)

    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(words)

# =========================================
# CAREER PREDICTION
# =========================================

def predict_career(skills):

    cleaned = preprocess_text(skills)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    return prediction[0]

# =========================================
# CAREER SKILLS DATABASE
# =========================================

career_skills = {

    "Data Scientist": {

        "Core Skills": [
            "python",
            "machine learning",
            "statistics",
            "sql",
            "data analysis",
            "feature engineering",
            "deep learning",
            "nlp"
        ],

        "Libraries": [
            "pandas",
            "numpy",
            "scikit learn",
            "tensorflow",
            "pytorch"
        ],

        "Visualization Tools": [
            "power bi",
            "tableau",
            "matplotlib",
            "seaborn"
        ]
    },

    "AI Engineer": {

        "Core Skills": [
            "python",
            "deep learning",
            "nlp",
            "transformer",
            "llm"
        ],

        "Libraries": [
            "tensorflow",
            "pytorch",
            "hugging face",
            "langchain"
        ]
    }
}

# =========================================
# SKILL GAP ANALYSIS
# =========================================

def advanced_skill_gap_analysis(
    user_skills,
    predicted_role
):

    cleaned_skills = preprocess_text(
        user_skills
    )

    user_skill_list = cleaned_skills.split()

    role_data = career_skills.get(
        predicted_role,
        {}
    )

    results = {}

    for category, skills in role_data.items():

        missing = []

        for skill in skills:

            processed_skill = preprocess_text(
                skill
            )

            skill_words = processed_skill.split()

            if not all(
                word in user_skill_list
                for word in skill_words
            ):

                missing.append(skill)

        results[category] = missing

    return results

# =========================================
# HOME ROUTE
# =========================================

@app.route("/", methods=["GET", "POST"])

def home():

    prediction = ""

    gaps = {}

    if request.method == "POST":

        skills = request.form["skills"]

        prediction = predict_career(
            skills
        )

        gaps = advanced_skill_gap_analysis(
            skills,
            prediction
        )

    return render_template(
        "index.html",
        prediction=prediction,
        gaps=gaps
    )

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    app.run(debug=True)