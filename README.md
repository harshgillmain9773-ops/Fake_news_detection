# Fake_news_detection
Build to detect the fake news in market
# 📰 Fake News Detection AI

A machine learning web application that classifies news articles as **Real** or **Fake** using TF‑IDF features and Logistic Regression. The project includes a Flask backend, an HTML/JS frontend, and integration with live news feeds.

---

## 📂 Project Structure
fake-news-app/
│── app.py              # Flask backend
│── fake_news_model.pkl # Trained ML model
│── tfidf_vectorizer.pkl# TF-IDF vectorizer
│── requirements.txt    # Dependencies
│── Procfile            # For Heroku deployment
│── templates/
│    └── index.html     # Frontend HTML
│── static/
└── styles.css     # CSS styling
│── Fake.csv, True.csv  # Dataset files

Dataset
Source: Kaggle – Fake and Real News Dataset (ISOT)

Files: Fake.csv (fake articles), True.csv (real articles)

Columns: Title, Text, Subject, Date

License: CC BY-NC-SA 4.0
![image alt](https://github.com/harshgillmain9773-ops/Fake_news_detection/blob/ee3d21a7354b4567cc3bcd94d18a1a28a821398b/proj1.png)
![image alt](https://github.com/harshgillmain9773-ops/Fake_news_detection/blob/30109b48dc12cf01cf33f094ee733c8c24b1a4bd/proj2.png)
![image alt](https://github.com/harshgillmain9773-ops/Fake_news_detection/blob/aaa31a31525bbda604e428dcda3836f41a9330a8/proj3.png)
![image alt](https://github.com/harshgillmain9773-ops/Fake_news_detection/blob/13aa78754dbc75a02d7f44382f704800915e5e62/proj4.png )
ML Pipeline
Data Cleaning → remove nulls, preprocess text

Feature Extraction → TF‑IDF vectorizer

Model Training → Logistic Regression (or SVM)

Evaluation → Accuracy ~98–99%

Deployment → Flask backend + HTML frontend



Features
Today’s News Section → shows headlines with Real/Fake tags

Manual Check Section → paste any news text and classify instantly

Interactive UI → clean HTML/CSS with navigation bar

Tech Stack
Python (Flask, scikit-learn, pandas, numpy)

Frontend (HTML, CSS, JavaScript)

Dataset (Kaggle Fake/Real News)



Tech Stack
Python (Flask, scikit-learn, pandas, numpy)

Frontend (HTML, CSS, JavaScript)

Dataset (Kaggle Fake/Real News)
