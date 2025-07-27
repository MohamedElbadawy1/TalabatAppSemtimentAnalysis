import streamlit as st
import joblib
import base64
from PIL import Image

model = joblib.load("A:/NTI/SentimentAnalysisProject/models/sentiment_model.pkl")
vectorizer = joblib.load("A:/NTI/SentimentAnalysisProject/models/tfidfVectorizer.pkl")

st.set_page_config(page_title="Talabat Reviews Sentiment Analysis", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #ff5722;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #f6ea39;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #ff5722;'>Talabat Reviews Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Predict user review sentiment (Arabic)</p>", unsafe_allow_html=True)

user_input = st.text_area("Write your review in Arabic:")

if st.button(" Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review before analyzing.")
    else:
        text_vectorized = vectorizer.transform([user_input])
        prediction = model.predict(text_vectorized)[0]

        if prediction == "positive":
            st.markdown("###  Prediction: Positive Sentiment")
            st.success(" This review expresses satisfaction and positivity.")
        elif prediction == "negative":
            st.markdown("### Prediction: Negative Sentiment")
            st.error(" This review expresses dissatisfaction or complaint.")
        else:
            st.info(" Unable to determine sentiment clearly.")


st.markdown("---")
st.markdown("<p style='text-align: center; font-size:13px;'>Model trained with TF-IDF + Logistic Regression on Talabat reviews.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:13px;'>by : Mohamed Elbadawy</p>", unsafe_allow_html=True)
