# /upload/app.py
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
from dotenv import load_dotenv
import os
import requests
import joblib
import re
import string
import nltk
import json

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Gemini
import google.generativeai as genai

import random
from pathlib import Path

DATA_FOLDER = Path("./data")
DATA_FOLDER.mkdir(exist_ok=True)


# -----------------
# LOAD ENV
# -----------------
load_dotenv(override=True)
WORLD_KEY = os.getenv("WORLD_NEWS_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

PAGE_SIZE = 10

# -----------------
# FLASK APP
# -----------------
app = Flask(__name__)
app.secret_key = "supersecretkey"  # already present
app.config['SESSION_TYPE'] = 'filesystem'  # optional, for clarity


# -----------------
# NLTK FIX — Download if missing
# -----------------
try:
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
except:
    nltk.download("stopwords")
    nltk.download("wordnet")
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

# -----------------
# PREPROCESS
# -----------------
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>+", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), " ", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)

    text = " ".join([
        lemmatizer.lemmatize(word)
        for word in text.split()
        if word not in stop_words
    ])
    return text

# -----------------
# LOAD ML MODEL
# -----------------
logreg_model = joblib.load("./model/fake_news_model.pkl")
tfidf = joblib.load("./model/tfidf_vectorizer.pkl")

# -----------------
# FETCH NEWS API
# -----------------
def fetch_news(country, search, page):
    offset = (page - 1) * PAGE_SIZE
    url = (
        f"https://api.worldnewsapi.com/search-news?"
        f"number={PAGE_SIZE}&offset={offset}&language=en"
    )
    if country != "all":
        url += f"&source-countries={country}"
    if search:
        url += f"&text={search}"

    res = requests.get(url, headers={"x-api-key": WORLD_KEY})
    try:
        data = res.json()
    except:
        return []

    raw_news = data.get("news", [])
    news_list = []

    for item in raw_news:
        summary = item.get("summary") or ""
        full_text = item.get("text") or ""
        if not summary:
            summary = full_text[:250] + "..." if len(full_text) > 250 else full_text or "No summary available."
        news_list.append({
            "title": item.get("title"),
            "summary": summary,
            "text": full_text,
            "url": item.get("url"),
            "publish_date": item.get("publish_date"),
            "country": item.get("source_country")
        })

    return news_list

# -----------------
# ROUTES
# -----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load")
def load_news():
    country = request.args.get("country", "all")
    search = request.args.get("search", "")
    page = int(request.args.get("page", 1))
    return jsonify(news=fetch_news(country, search, page))

# AI DETECTOR
@app.route("/detect", methods=["POST"])
def detect_fake_news():
    data = request.json
    text_for_ml = f"{data['title']} {data['summary']} {data['text']}"
    processed = preprocess(text_for_ml)
    tfidf_vec = tfidf.transform([processed])
    pred = logreg_model.predict(tfidf_vec)[0]
    model_label = "True" if pred == 1 else "Fake"

    # Gemini AI
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are a strict fake news evaluator.
Respond ONLY with a number from 0 to 100 indicating the likelihood that the following news is TRUE.

Title: {data['title']}
Summary: {data['summary']}
Full Text: {data['text']}
"""
    try:
        response = model.generate_content(prompt)
        digits = "".join(c for c in response.text.strip() if c.isdigit())
        percent = int(digits) if digits else 50
    except:
        percent = 50

    return jsonify({"gemini_percent": percent, "model_label": model_label})

# -----------------
# AUTH
# -----------------
USER_FILE = "./users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # File is empty or invalid JSON, reset it
        return {}


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

@app.route("/auth")
def auth_page():
    return render_template("auth.html")

@app.route("/signup", methods=["POST"])
def signup():
    data = request.form
    username = data.get("username").strip()
    email = data.get("email").strip().lower()
    password = data.get("password")
    password2 = data.get("password2")

    if not username or not email or not password or not password2:
        flash("All fields are required", "danger")
        return redirect(url_for("auth_page") + "#signup")

    if password != password2:
        flash("Passwords do not match", "danger")
        return redirect(url_for("auth_page") + "#signup")

    users = load_users()
    if email in users:
        flash("Email already registered, please login", "warning")
        return redirect(url_for("auth_page") + "#login")

    # Save new user
    users[email] = {"username": username, "password": password}
    save_users(users)

    # Set session
    session['user'] = {"username": username, "email": email}

    flash("Signup successful! You are now logged in.", "success")
    return redirect(url_for("index"))


@app.route("/save_favorite", methods=["POST"])
def save_favorite():
    data = request.json
    email = data.get("email")
    if not email:
        return jsonify({"error": "No email provided"}), 400

    # Create random filename
    rand_num = random.randint(1000, 9999)
    file_path = DATA_FOLDER / f"{email.replace('@','_')}_{rand_num}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"status": "saved"})

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")

@app.route("/get_favorites")
def get_favorites():
    email = request.args.get("email")
    if not email:
        return jsonify([])

    files = DATA_FOLDER.glob(f"{email.replace('@','_')}_*.json")
    all_data = []
    for f in files:
        try:
            with open(f) as file:
                all_data.append(json.load(file))
        except:
            continue
    return jsonify(all_data)


@app.route("/login", methods=["POST"])
def login():
    data = request.form
    email = data.get("email").strip().lower()
    password = data.get("password")

    users = load_users()
    if email not in users:
        flash("No user found. Please signup.", "danger")
        return redirect(url_for("auth_page") + "#signup")

    if users[email]["password"] != password:
        flash("Incorrect password.", "danger")
        return redirect(url_for("auth_page") + "#login")

    # Set session
    session['user'] = {"username": users[email]['username'], "email": email}

    flash(f"Welcome {users[email]['username']}!", "success")
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear() 
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
