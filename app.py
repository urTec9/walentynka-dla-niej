import streamlit as st
import base64
import time
from datetime import date
from PIL import Image, ImageOps
from streamlit_extras.let_it_rain import rain 
from dateutil.relativedelta import relativedelta

# 1. KONFIGURACJA STRONY
st.set_page_config(page_title="Moja Walentynka ❤️", page_icon="💌", layout="centered")

# --- FUNKCJA 1: TŁO ZE ZDJĘCIA (Dla strony startowej) ---
def set_bg_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{b64}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- FUNKCJA 2: TŁO GRADIENTOWE (Nowa wersja) ---
def set_bg_gradient():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            /* Czerwień przechodząca w delikatny róż */
            background-image: linear-gradient(to top, #ff9a9e 0%, #fecfef 99%, #fecfef 100%) !important;
            background-size: cover !important;
            background-attachment: fixed !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- FUNKCJA 3: MUZYKA W TLE ---
def autoplay_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except:
        st.warning("⚠️ Nie znaleziono pliku muzyki (love.mp3)")

# 2. INICJALIZACJA STANU
if 'page' not in st.session_state:
    st.session_state.page = 'question'

# ==========================================
# STRONA 1: PYTANIE (Landing Page)
# ==========================================
if st.session_state.page == 'question':
    
    # 1. Ładujemy zdjęcie tła
    try:
        set_bg_image('wallpaper1.jpg') 
    except FileNotFoundError:
        # Awaryjnie gradient, jakby nie było pliku tła
        set_bg_gradient()
        st.warning("⚠️ Brakuje pliku 'tlo.jpg'!")

    # Tytuł z cieniem (czytelny na zdjęciu)
    st.markdown(
        "<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>Hej Skarbie!</h1>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<h3 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>Mam do Ciebie bardzo ważne pytanie...</h3>", 
        unsafe_allow_html=True
    )
    
    
    
    st.markdown(
        "<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>Zostaniesz moją Walentynką?<br>💖</h1>", 
        unsafe_allow_html=True
    )
    
    # Przyciski
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("TAK 🥺", use_container_width=True):
            st.session_state.page = 'main'
            st.rerun()
            
    with col2:
        if st.button("NIE 😭", use_container_width=True):
            # Ciemne tło + Biały tekst = Super czytelność
            st.markdown("""
            <div style="
                background-color: rgba(0, 0, 0, 0.7);   /* Czarne tło, 70% widoczności */
                color: white;                           /* Biały tekst */
                border: 2px solid #ff4b4b;              /* Różowa ramka dla klimatu */
                border-radius: 15px;                    /* Zaokrąglone rogi */
                padding: 15px;                          /* Odstęp w środku */
                text-align: center;                     
                font-size: 18px;                        /* Nieco większy tekst */
                font-weight: bold;                      
                box-shadow: 0px 4px 15px rgba(0,0,0,0.5); /* Cień pod pudełkiem (efekt 3D) */
            ">
                Error 404: Odmowa nie została znaleziona
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# STRONA 2: GŁÓWNA TREŚĆ (Po kliknięciu TAK)
# ==========================================
elif st.session_state.page == 'main':
    
    # 1. Ładujemy GRADIENT
    # Dzięki !important w CSS, to teraz na pewno nadpisze zdjęcie
    set_bg_gradient()
    
    # --- TU WKLEJ URUCHOMIENIE MUZYKI ---
    autoplay_audio("love.mp3")

    # 3. EFEKT DESZCZU 
    rain(
    emoji="❤️", 
    font_size=54, 
    falling_speed=5, 
    animation_length=2, 
    )
    
    # Tekst bez cienia (czysty)
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; text-shadow: 2px 2px 4px #000000;'>Wiedziałem! Kocham Cię!</h1>", unsafe_allow_html=True)


    # --- LICZNIK CZASU (JESTEŚMY JUŻ... \n CZAS) ---
    # Upewnij się, że masz: from dateutil.relativedelta import relativedelta (na górze pliku)
    
    start_date = date(2024, 3, 9) 
    today = date.today()
    diff = relativedelta(today, start_date)

    st.write("")

    # Używamy HTML, żeby zrobić ładne łamanie linii (<br>) i kolory
    st.markdown(f"""
    <div style='text-align: center;'>
        <h3 style='margin-bottom: 5px; font-weight: normal; text-shadow: 2px 2px 4px #000000;'>Jesteśmy razem już:</h3>
        <h1 style='color: #ff4b4b; margin-top: 0; font-size: 40px;'>
            {diff.years} rok, {diff.months} miesięcy i {diff.days} dni! 🥰
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Opcjonalnie: tekst pod spodem
    st.markdown(f"""
    <div style='text-align: center;'>
        <h6 style='margin-bottom: 5px; font-weight: normal; text-shadow: 2px 2px 4px #000000;'>Każdy z tych { (today - start_date).days } dni był wyjątkowy</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # ZDJĘCIE PARY
    image_path = "nasze_zdjecie.jpg"
    try:
        original_image = Image.open(image_path)
        fixed_image = ImageOps.exif_transpose(original_image)
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            # 1. Wyświetlamy zdjęcie BEZ parametru caption
            st.image(fixed_image, use_container_width=True)
            
            # 2. Dodajemy własny, ładny podpis pod spodem
            st.markdown("""
            <p style='
                text-align: center; 
                color: white; 
                font-size: 15px; 
                font-weight: bold;
                margin-top: -10px; 
                text-shadow: 2px 2px 4px #000000; /* TO JEST TEN CIEŃ */
            '>
                Nasze chwile ❤️
            </p>
            """, unsafe_allow_html=True)
    except:
        st.info("Brak zdjęcia w folderze 'nasze_zdjecie.jpg'")

    st.write("")

    # ZAKŁADKI
    st.markdown("""
            <p style='
                text-align: center; 
                color: white; 
                font-size: 30px; 
                font-weight: bold;
                margin-top: -10px; 
            '>
                Dlaczego TY ? 💌
            </p>
            """, unsafe_allow_html=True)

    # ZAKŁADKI
    # --- STYLIZACJA ZAKŁADEK (CSS) ---
    st.markdown("""
    <style>
        /* Zmieniamy wygląd przycisków zakładek */
        button[data-baseweb="tab"] {
            font-size: 30px !important;   /* Rozmiar czcionki */
            font-weight: bold !important; /* Pogrubienie */
            color: black !important;      /* Kolor tekstu (opcjonalnie) */
        }
        
        /* Opcjonalnie: Zmiana koloru aktywnej zakładki na czerwony */
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #ff4b4b !important;
        }
    </style>
    """, unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Uśmiech😁", "Wsparcie💪", "Chwile✈️", "Przyszłość🏡"])

    with tab1:
        st.markdown("""
        <div style='text-align: center; font-size: 24px; padding: 20px;'>
            Kiedy się uśmiechasz świat staje się lepszy. (Masz piękny uśmiech). 🥰
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div style='text-align: center; font-size: 24px; padding: 20px;'>
            Zawsze we mnie wierzysz, nieważne co by się działo. Dziękuję, że jesteś. ❤️
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        st.markdown("""
        <div style='text-align: center; font-size: 24px; padding: 20px;'>
            Chce budować z Tobą najlepsze chwile i nie zamieniłbym naszych wspólnych chwil na nic innego. 💑
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div style='text-align: center; font-size: 24px; padding: 20px;'>
            Nie mogę się doczekać wszystkiego, co jeszcze przed nami! ✨
        </div>
        """, unsafe_allow_html=True)

    # --- QUIZ WALENTYNKOWY (DUŻY I WYŚRODKOWANY) ---
    st.write("---")
    
    # 1. Styl CSS powiększający odpowiedzi (działa tylko na radio buttons)
    st.markdown("""
    <style>
    /* Celujemy w tekst wewnątrz przycisków opcji */
    div.stRadio p {
        font-size: 22px !important; /* Rozmiar czcionki */
        margin-bottom: 10px;        /* Odstęp między opcjami */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Mały Quiz o Nas</h2>", unsafe_allow_html=True)
    
    # Układ kolumn dla wyśrodkowania [pusta, TREŚĆ, pusta]
    left, center, right = st.columns([1, 2, 1])
    
    with center:
        # Pytanie
        st.markdown("<h4 style='text-align: center;'>Gdzie byliśmy na pierwszej randce? 🤔</h4>", unsafe_allow_html=True)

        # Odpowiedzi
        quiz_pytanie = st.radio(
            "Pytanie ukryte", 
            ["Park", "Pizzeria", "Lodowisko", "Jezioro"],
            index=None,
            label_visibility="collapsed"
        )
        
        st.write("") 
        
        # Przycisk
        if st.button("Sprawdź odpowiedź ✅", use_container_width=True):
            if quiz_pytanie == "Lodowisko":
                # Eleganckie powiadomienie w rogu
                st.toast('Jesteś niesamowita! Brawo! 🌹', icon='😍')
                time.sleep(1) # Czekamy chwilę
                st.toast('Wygrałaś buziaka! 💋', icon='😘')
            
                st.success("Brawo Kochanie! Pamiętasz wszystko! 🏆")
            elif quiz_pytanie is None:
                st.warning("Zaznacz coś najpierw! 😉")
            else:
                st.error("Oj... chyba musimy tam iść jeszcze raz dla przypomnienia! 😅")

# --- STOPKA (FOOTER) ---
    st.write("")
    st.write("")
    st.markdown("""
    <p style='text-align: center; color: gray; font-size: 14px;'>
        Stworzone z miłością (i odrobiną Programowania) specjalnie dla Ciebie.<br>
        Twoja Walentynka ❤️
    </p>
    """, unsafe_allow_html=True)