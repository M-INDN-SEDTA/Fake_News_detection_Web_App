```md
# 🌍 News Authenticity & AI Credibility Checker

A web application that aggregates real-time global news, analyzes each article using AI credibility scoring, detects fake content using ML, supports user authentication, allows saving favorites, and provides text-to-speech reading of articles.

---

## ⭐ Key Features

- 🔍 Country-based news filtering  
- 📰 Real-time news aggregation  
- 🤖 AI credibility scoring (Gemini)  
- 🧠 Offline ML fake-news model  
- 🎙️ Text-to-speech article playback  
- ❤️ Save favorite verified articles  
- 🔐 Login & authentication system  
- 🎨 Clean, responsive UI  
- 🚀 Fast Flask backend APIs  

---

## 🏗️ Project Structure

```

project_root/
│
├── app.py               # Main Flask backend
├── model.py             # ML model loading & prediction
├── static/
│   ├── style.css        # UI styling
│   └── script.js        # Frontend logic
│
├── templates/
│   ├── index.html       # Homepage
│   ├── login.html       # Login
│   ├── register.html    # Signup
│   ├── favorites.html   # Saved articles
│   └── auth.html        # Auth layout wrappers
│
├── models/
│   ├── fake_news.pkl    # ML model (offline)
│   └── vectorizer.pkl   # Text vectorizer
│
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── LICENSE              # MIT or similar

```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```

git clone <your-repo-url>
cd <project-folder>

```

### 2️⃣ Create a Python virtual environment

```

python -m venv venv

```

### 3️⃣ Activate venv

**Windows:**
```

venv\Scripts\activate

```

**Mac / Linux:**
```

source venv/bin/activate

```

---

## 📦 Install dependencies

```

pip install -r requirements.txt

```

---

## ▶️ Run the app

```

python app.py

```

Then open:

```

[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

---

## 🧪 Testing the Project

- Load homepage  
- Select country  
- Search by keywords  
- Click article  
- Check AI authenticity  
- Save favorite if logged in  

---

## 🧠 Technology Stack

**Frontend:**
- HTML  
- CSS  
- JavaScript  

**Backend:**
- Python  
- Flask  
- Jinja2  

**AI & ML:**
- Gemini API  
- Scikit-learn  
- Pickle-based offline model  

**Storage:**
- Local DB (or JSON storage depending on your current implementation)

---

## 🔐 User Authentication

- Password hashed  
- Session-based login  
- User ownership of saved news  

---

## 🗂️ Requirements Example

Typical contents of `requirements.txt`:

```

Flask
requests
beautifulsoup4
scikit-learn
pandas
numpy
python-dotenv

```

If you add more, this file grows automatically.

---

## 🪪 License

This project is licensed under the MIT License — free to use, modify, distribute.

---

## 🙌 Credits

Created by: **YOU**  
Role: Full-stack + ML integration  

---

## ⭐ Contributing

Pull requests are welcome — improvements, UI suggestions, optimizations, model upgrades, etc.

---

## 👍 If you like this project

Leave a ⭐ on the repository!