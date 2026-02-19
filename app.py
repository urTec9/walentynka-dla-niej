import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Nasz Licznik", page_icon="❤️", layout="centered")

# --- TWOJE DANE (Zmień tutaj) ---
# Data rozpoczęcia związku: Rok, Miesiąc, Dzień
START_DATE = datetime(2024, 3, 9) 
# Link do zdjęcia w tle
BG_IMAGE_URL = "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=2070&auto=format&fit=crop"

# --- LOGIKA OBLICZEŃ ---
now = datetime.now()
diff = relativedelta(now, START_DATE)
total_days = (now - START_DATE).days

# --- STYLIZACJA CSS I SERCA ---
st.markdown(
    f"""
    <style>
    /* Tło całej strony */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("{BG_IMAGE_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Animacja spadających serc */
    @keyframes heart-fall {{
        0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
    }}

    .heart {{
        position: fixed;
        top: -10%;
        /* Kolor serca (możesz zmienić, np. na czyste 'red') */
        color: rgba(220, 20, 60, 0.9); 
        font-size: 26px;
        user-select: none;
        z-index: 1000;
        animation: heart-fall linear infinite;
        text-shadow: 0 0 5px rgba(0,0,0,0.3);
    }}

    /* Kontener licznika (efekt szklanej karty) */
    .counter-container {{
        background: rgba(255, 255, 255, 0.1);
        padding: 50px 20px;
        border-radius: 30px;
        backdrop-filter: blur(15px);
        text-align: center;
        border: 1px

