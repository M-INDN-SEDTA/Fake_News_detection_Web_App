# 🌍 Real-Time AI-Powered News Credibility Checker

A full-stack application that fetches global news, verifies authenticity using AI + ML, supports user login, favorites, voice-reading of articles, and country-based news filtering.

---

[![Typing SVG](https://readme-typing-svg.herokuapp.com?size=30&center=true&vCenter=true&width=1000&lines=AI+Powered+Fake+News+Detection;Flask+%2B+Python+%2B+JavaScript;Gemini+AI+%2B+ML+Classifier;Real-Time+World+News+Scanner)](https://git.io/typing-svg)

## 🚀 Tech Used

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white&style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white&style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge)

---

## 📊 Repo Analytics

![Profile Views](https://komarev.com/ghpvc/?username=M-INDN-SEDTA&color=blue)
![Stars](https://img.shields.io/github/stars/M-INDN-SEDTA/Fake_News_detection_Web_App?style=social)


---

## ✨ Features

- 🌎 Country-specific and global news sources  
- 🔍 Search-based filtering  
- 🤖 Gemini-based AI credibility scoring (percentage true)  
- 🧠 Offline ML fake-news classifier (TF-IDF + Logistic Regression)  
- 🎙️ Text-to-speech article playback (Web Speech API)  
- ❤️ Favorite-saving system (requires login)  
- 🔐 Login, registration & session authentication (session-based)  
- 📱 Responsive UI built with Bootstrap

---

## 🏗 Project Structure

```bash
project_root/
│
├── app.py           # Main Flask app (or upload/app.py)
├── model/           # Saved ML model & vectorizer
│ ├── fake_news_model.pkl
│ └── tfidf_vectorizer.pkl
├── templates/       # Jinja2 templates
│ ├── index.html
│ ├── auth.html
│ └── favorites.html
├── data/            # Saved favorites (json files)
├── static/            # screenshots of this project
├── users.json       # Local user storage (json)
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Prerequisites

- Python 3.8+  
- Git (optional)  
- Internet access for Gemini API & World News API

---

## 🔧 Setup (copy-paste)

1. **Clone repo**

```bash
git clone https://github.com/M-INDN-SEDTA/Fake_News_detection_Web_App
cd Fake_News_detection_Web_App
```
```bash
python -m venv venv
```

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate venv**

* Windows:

```bash
venv\Scripts\activate
```

* macOS / Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Create `.env` file** (in project root) and add your API keys:

```
WORLD_NEWS_API_KEY=your_world_news_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

6. **Run the app**

```bash
python app.py
```

> Open this line in your browser.
```bash
Open http://127.0.0.1:5000 in your browser.
```

---

## 🔁 Example `requirements.txt`

```
Flask==2.2.5
requests==2.31.0
python-dotenv==1.0.0
nltk==3.8.1
scikit-learn==1.2.2
joblib==1.2.0
beautifulsoup4==4.12.2
pandas==2.1.0
numpy==1.26.0
google-generativeai==0.2.0   # or whichever package/wrapper you use for Gemini
```

---

## 🔐 Environment Variables / API Keys

The app reads keys from environment variables (via `python-dotenv`):

> Note: Please update this file without it app will not run

* `WORLD_NEWS_API_KEY` — API key for fetching news (World News API)
* `GEMINI_API_KEY` — API key for Gemini generative model
* `SECRET_KEY` — Flask session secret (use a secure random string)

---

## ⚙️ How the detection works (brief)

1. Frontend sends article `title + summary + text` to `/detect`.
2. Backend preprocesses text (lowercase, remove punctuation, stopwords, lemmatize).
3. Offline model: TF-IDF vectorizer → Logistic Regression (`fake_news_model.pkl`) → `True` / `Fake`.
4. Online AI: Gemini is queried with a strict prompt and returns a numeric 0–100 percent indicating likelihood the article is true.
5. Results shown side-by-side in the UI.

---

## 💾 Saving Favorites

* Users must **log in** to save favorites.
* Favorites are saved as JSON files in `/data/` with a randomized suffix (e.g. `user_example_com_1234.json`).
* Favorite payload includes `title`, `summary`, `text`, `publish_date`, `country`, `gemini_percent`, `model_label`, `url`.

---

## 🧪 Testing

* Load homepage → select country → get news → click “Check Authenticity” on a card → verify Gemini % and Offline ML label show → if logged in, save favorite → check `/data/` for the saved JSON.

---

## 📸 Screenshots & Demo (suggested)

This path `/static/images/` for repo screenshots:

```
1. homepage_dashboard1.png
2. homepage_dashboard2.png
3. login_screen.png
4. favorites_saved_list.png
```

---

## 🪪 License

This repo is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙌 Contributing

Contributions welcome — open an issue or a PR. Suggested improvements:

* Replace JSON local user store with a DB (SQLite/Postgres)
* Add hashed passwords (bcrypt)
* Add tests and CI
* Improve prompt & result parsing for Gemini

   

