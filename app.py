import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Nasza Historia Miłości", page_icon="💖", layout="centered")

# --- TWOJE DANE (Zmień tutaj!) ---
START_DATE = datetime(2022, 5, 15)  # Data początku związku
BG_IMAGE_URL = "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=2070&auto=format&fit=crop"

# --- LISTA KOMPLEMENTÓW ---
compliments = [
    "Masz najpiękniejszy uśmiech na świecie! 😊",
    "Uwielbiam Twój sposób bycia. ✨",
    "Jesteś moją ulubioną osobą! ❤️",
    "Dziękuję, że jesteś przy mnie. 🌸",
    "Dzień z Tobą to zawsze dobry dzień! ☀️",
    "Twoja obecność sprawia, że wszystko jest lepsze. 🥂"
]

# --- STYLIZACJA CSS (TŁO, SERCA, WYGLĄD) ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{BG_IMAGE_URL}");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }}

    @keyframes heart-fall {{
        0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
    }}

    .heart {{
        position: fixed;
        top: -10%;
        color: rgba(255, 105, 180, 0.7);
        font-size: 20px;
        user-select: none;
        z-index: 1000;
        animation: heart-fall linear infinite;
    }}

    .counter-box {{
        background: rgba(255, 255, 255, 0.15);
        padding: 40px;
        border-radius: 30px;
        backdrop-filter: blur(15px);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    .section-title {{
        color: #ffb6c1;
        text-align: center;
        margin-top: 40px;
    }}
    </style>
    
    <div class="heart" style="left: 10%; animation-duration: 5s;">❤️</div>
    <div class="heart" style="left: 25%; animation-duration: 8s;">💖</div>
    <div class="heart" style="left: 40%; animation-duration: 6s;">💗</div>
    <div class="heart" style="left: 60%; animation-duration: 9s;">❤️</div>
    <div class="heart" style="left: 75%; animation-duration: 7s;">💕</div>
    <div class="heart" style="left: 90%; animation-duration: 10s;">💘</div>
    """,
    unsafe_allow_html=True
)

# --- LOGIKA OBLICZEŃ ---
now = datetime.now()
diff = relativedelta(now, START_DATE)

# --- GŁÓ
