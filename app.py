import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Nasz Licznik", page_icon="❤️")

# --- TWOJE DANE (Zmień tutaj) ---
# Data rozpoczęcia związku: Rok, Miesiąc, Dzień
START_DATE = datetime(2024, 03, 09) 
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
        color: rgba(255, 182, 193, 0.8);
        font-size: 24px;
        user-select: none;
        z-index: 1000;
        animation: heart-fall linear infinite;
    }}

    /* Kontener licznika (efekt szklanej karty) */
    .counter-container {{
        background: rgba(255, 255, 255, 0.1);
        padding: 50px 20px;
        border-radius: 30px;
        backdrop-filter: blur(15px);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        margin-top: 15vh;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        font-family: 'Helvetica', sans-serif;
    }}

    .title {{ font-size: 2.5rem; font-weight: bold; margin-bottom: 20px; }}
    .time {{ font-size: 1.8rem; color: #ffb6c1; margin-bottom: 10px; }}
    .days {{ font-size: 1.2rem; opacity: 0.8; }}
    </style>

    <div class="heart" style="left: 10%; animation-duration: 7s;">❤️</div>

    """,
    unsafe_allow_html=True
)

# --- WYŚWIETLANIE LICZNIKA ---
st.markdown(
    f"""
    <div class="counter-container">
        <div class="title">Jesteśmy razem już: ❤️</div>
        <div class="time">
            {diff.years} lat, {diff.months} miesięcy i {diff.days} dni
        </div>
        <div class="days">To łącznie już {total_days} pięknych dni!</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Ukrywamy domyślne menu Streamlit, żeby strona była "czysta"
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

