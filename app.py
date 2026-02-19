import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Nasza Historia Miłości", page_icon="💖", layout="centered")

# --- TWOJE DANE ---
START_DATE = datetime(2022, 5, 15)  # WPISZ SWOJĄ DATĘ
BG_IMAGE_URL = "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=2070&auto=format&fit=crop"

compliments = [
    "Masz najpiękniejszy uśmiech na świecie! 😊",
    "Uwielbiam Twój sposób bycia. ✨",
    "Jesteś moją ulubioną osobą! ❤️",
    "Dziękuję, że jesteś przy mnie. 🌸",
    "Dzień z Tobą to zawsze dobry dzień! ☀️"
]

# --- OBLICZENIA ---
now = datetime.now()
diff = relativedelta(now, START_DATE)
total_days = (now - START_DATE).days

# --- CSS (TŁO, SERCA I RAMKI) ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{BG_IMAGE_URL}");
        background-size: cover;
        background-attachment: fixed;
    }}

    @keyframes heart-fall {{
        0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
    }}

    .heart {{
        position: fixed;
        top: -10%;
        color: rgba(255, 105, 180, 0.7);
        font-size: 24px;
        user-select: none;
        z-index: 1000;
        animation: heart-fall linear infinite;
    }}

    /* Styl dla głównego kontenera */
    .main-container {{
        background: rgba(255, 255, 255, 0.15);
        padding: 30px;
        border-radius: 25px;
        backdrop-filter: blur(15px);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        margin-bottom: 20px;
        font-family: 'sans-serif';
    }}

    .title {{ font-size: 40px; font-weight: bold; margin-bottom: 10px; }}
    .counter {{ font-size: 30px; color: #ffb6c1; margin: 15px 0; }}
    </style>

    <div class="heart" style="left: 5%; animation-duration: 6s;">❤️</div>
    <div class="heart" style="left: 15%; animation-duration: 8s;">💖</div>
    <div class="heart" style="left: 30%; animation-duration: 7s;">💕</div>
    <div class="heart" style="left: 50%; animation-duration: 10s;">❤️</div>
    <div class="heart" style="left: 70%; animation-duration: 9s;">💗</div>
    <div class="heart" style="left: 85%; animation-duration: 5s;">💘</div>
    """,
    unsafe_allow_html=True
)

# --- WYŚWIETLANIE LICZNIKA (W jednym bloku HTML) ---
st.markdown(
    f"""
    <div class="main-container">
        <div class="title">❤️ Razem od: ❤️</div>
        <div class="counter">{diff.years} lat, {diff.months} miesięcy, {diff.days} dni</div>
        <p style="font-size: 18px;">To już <b>{total_days}</b> wspaniałych dni razem!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- DODATKI (Wbudowane komponenty Streamlit) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='text-align:center; color:white; font-weight:bold;'>📸 Nasze Wspomnienie</div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1516589174184-c685266e430c?w=500", use_container_width=True)
    
with col2:
    st.markdown("<div style='color:white; font-weight:bold;'>📝 Nasze Marzenia</div>", unsafe_allow_html=True)
    st.checkbox("Wspólne wakacje", value=True)
    st.checkbox("Lot balonem", value=False)
    st.checkbox("Wspólny dom", value=False)

st.write("---")

# --- KOMPLEMENTY (Przycisk bez balonów) ---
st.markdown("<h3 style='text-align:center; color:#ffb6c1;'>✨ Coś miłego ✨</h3>", unsafe_allow_html=True)
if st.button('Wylosuj komplement!'):
    st.success(random.choice(compliments))

st.markdown("<br><p style='text-align: center; color: white; opacity: 0.6;'>Stworzone z ❤️</p>", unsafe_allow_html=True)
