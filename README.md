```md
# 🌍 Real-Time AI-Powered News Credibility Checker

A full-stack application that fetches global news, verifies authenticity using AI + ML, supports user login, favorites, voice-reading of articles, and country-based news filtering.

---

## ✨ Features

- 🌎 Country-specific and global news sources
- 🔍 Search-based filtering
- 🤖 Gemini-based AI credibility scoring (percentage true)
- 🧠 Offline ML fake-news classifier
- 🎙️ Text-to-speech voice reading
- ❤️ Favorite-saving system (user required)
- 🔐 Login, registration & session authentication
- 📱 Fully responsive Bootstrap UI

---

## 🏗 Project Structure

```

project/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── favorites.html
│   └── auth.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── icons/
│
└── models/
├── fake_news.pkl
└── vectorizer.pkl

```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```

git clone <repo-url>
cd <repo-folder>

```

### 2️⃣ Create a virtual environment

```

python -m venv venv

```

### 3️⃣ Activate it

**Windows:**
```

venv\Scripts\activate

```

**Mac/Linux:**
```

source venv/bin/activate

```

### 4️⃣ Install dependencies

```

pip install -r requirements.txt

```

### 5️⃣ Run application

```

python app.py

```

Now open:

```

[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

---

## 🧠 Models Used

### Gemini Online Authenticator  
Returns:  
```

87% true

```

### Offline ML Model  
Returns:
```

True  /  Fake

```

Both displayed inside each news card.

---

## 🛡 Authentication

- Password hashing  
- Session tracking  
- Email-based identification  
- Only logged-in users can save favorites  

---

## 📦 Requirements

Sample `requirements.txt` (expandable):

```

Flask
requests
beautifulsoup4
numpy
pandas
scikit-learn
python-dotenv

```

---

## 🪪 License

MIT License

---

## 🙌 Developer

Made with Python + JS + Flask + Gemini API  
Built by: **YOU**

---

## ⭐ Support

If this project helped you — star the repo 👍

