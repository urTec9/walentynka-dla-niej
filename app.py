import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import base64

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Nasz Licznik", page_icon="❤️", layout="centered")

# --- FUNKCJA DO ŁADOWANIA LOKALNEGO ZDJĘCIA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- TWOJE DANE ---
START_DATE = datetime(2024, 3, 9) 
NAZWA_PLIKU = "wallpaper1.jpg"       

try:
    bin_str = get_base64_of_bin_file(NAZWA_PLIKU)
except FileNotFoundError:
    st.error(f"Nie znaleziono pliku '{NAZWA_PLIKU}'. Upewnij się, że jest w tym samym folderze co kod!")
    bin_str = ""

# --- LOGIKA OBLICZEŃ ---
now = datetime.now()
diff = relativedelta(now, START_DATE)
total_days = (now - START_DATE).days

# --- STYLIZACJA CSS I SERCA ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    @keyframes heart-fall {{
        0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
    }}

    .heart {{
        position: fixed;
        top: -10%;
        color: rgba(220, 20, 60, 0.9); 
        font-size: 26px;
        user-select: none;
        z-index: 1000;
        animation: heart-fall linear infinite;
    }}

    .counter-container {{
        background: rgba(255, 255, 255, 0.1);
        padding: 50px 20px;
        border-radius: 30px;
        backdrop-filter: blur(15px);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        margin-top: 20vh;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        font-family: 'Helvetica', sans-serif;
    }}

    .title {{ font-size: 2.5rem; font-weight: bold; margin-bottom: 20px; }}
    .time {{ font-size: 1.8rem; color: #ffb6c1; margin-bottom: 10px; }}
    .days {{ font-size: 1.2rem; opacity: 0.8; }}

    #MainMenu, footer, header {{ visibility: hidden; }}
    </style>

    <div class="heart" style="left: 5%; animation-duration: 7s;">❤️</div>
    <div class="heart" style="left: 20%; animation-duration: 9s;">❤️</div>
    <div class="heart" style="left: 35%; animation-duration: 6s;">❤️</div>
    <div class="heart" style="left: 50%; animation-duration: 11s;">❤️</div>
    <div class="heart" style="left: 65%; animation-duration: 8s;">❤️</div>
    <div class="heart" style="left: 80%; animation-duration: 10s;">❤️</div>
    <div class="heart" style="left: 95%; animation-duration: 7.5s;">❤️</div>
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
