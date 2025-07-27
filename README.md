# 🧐 Talabat Sentiment Analysis App (Arabic)

This is a machine learning project to analyze the **sentiment of Arabic user reviews** for the Talabat app (positive or negative).  
The solution uses classic NLP (TF-IDF + Logistic Regression) and is deployed as a **Streamlit web application**.

---

## 📂 Folder Structure

```
Talabat-Sentiment-Analysis/
│
├── app.py                         # Streamlit app
├── README.md                      # Project documentation
│
├── models/                        # Saved ML model & vectorizer
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── data/
│   ├── raw/                       # Raw scraped reviews
│   └── processed/                 # Cleaned & labeled data
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01_preprocessing.ipynb     # Cleaning & labeling
│   ├── 02_model_training.ipynb    # Model building
│   └── 03_evaluation.ipynb        # Evaluation & testing
│
├── scripts/                       # Python scripts (scraping, utils)
│   └── scrape_talabat_reviews.py
│
├── assets/
│   └── talabat_logo.png           # Talabat logo for UI
│
└── test_cases.py                  # Manual test cases for model
```

---

## 💠 Tech Stack

- **Language**: Python 🐍
- **Libraries**:
  - `scikit-learn`: Model training
  - `nltk`: Text preprocessing (Arabic)
  - `streamlit`: Web app
  - `Pandas`: Data manipulation
- **ML Approach**: TF-IDF + Logistic Regression
- **Visualization**: WordCloud, Seaborn

---

## 📊 Example Inputs

| Review in Arabic                                 | Prediction |
|--------------------------------------------------|------------|
| الخدمة ممتازة جدًا والتوصيل سريع                 | ✅ Positive |
| الأكل سيء جدًا والتوصيل اتأخر ساعة               | ❌ Negative |
| جيد نوعًا ما                                      | ❓ May vary |

---

## 🚀 How to Run

### 1. Install requirements

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit scikit-learn pandas nltk joblib pillow
```

### 2. Run the app

```bash
streamlit run app.py
```

---

## 📌 Features

- Analyze any Arabic text review
- Supports modern slang and real user feedback
- Simple and beautiful UI (with Talabat logo)
- Works offline

---

## 🧪 Test Cases

You can test the model manually by running:

```bash
python test_cases.py
```

---

## 📦 Dataset

The reviews were scraped from the **Talabat Google Play Store**, using custom Python scripts. Reviews were manually labeled or inferred from ratings.

---

## 💡 Future Ideas

- Add confidence scores (`predict_proba`)
- Support batch analysis (CSV upload)
- Deploy online on Hugging Face / Streamlit Cloud
- Fine-tune using deep learning models (AraBERT)

---

## 👤 Author

**Mohamed Asaad Elbadawy**  
Junior Data Scientist | NLP & ML Enthusiast

📧 mohamedasaad.dev@gmail.com  
[LinkedIn](https://www.linkedin.com/in/mohamedelbadawy1)


