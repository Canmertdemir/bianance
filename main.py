import streamlit as st
import sqlite3

# Sayfa arka plan görseli
background_image = "https://www.slidescarnival.com/es/para-que-son-adecuadas-estas-plantillas-de-powerpoint-de-maquinas"

# Veritabanını oluştur
def create_table():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Kayıt olma fonksiyonu
def register(email, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (email, password) VALUES (?, ?)
    ''', (email, password))

    conn.commit()
    conn.close()

    st.success("Başarıyla kayıt oldunuz!")

# Ana sayfa
def home_page():
    st.header("Ana Sayfa")

# Zorluklar sayfası
def challenges_page():
    st.header("Kadınların Sektörde Yaşadığı Zorluklar")
    st.write("""
        Kadınların teknoloji sektöründe karşılaştığı zorluklar konusunda bilgi ve farkındalık oluşturulması.
    """)
    st.subheader("İstatistikler")
    # İstatistiksel grafik ekleme

# Liderlik sayfası
def leadership_page():
    st.header("Sektörde Kadının Liderliği")
    st.write("""
        Teknoloji sektöründe kadın liderlerin başarıları ve liderlik rollerinde karşılaştıkları zorluklar.
    """)

# Token Mimarisi sayfası
def token_architecture_page():
    st.header("Token Mimarisi")
    st.write("""
        Kripto dünyasında token mimarisinin rolü ve kadınların bu alandaki katkıları.
    """)

# Kayıt olma sayfası
def register_page():
    st.header("Kayıt Ol")
    email = st.text_input("E-posta:")
    password = st.text_input("Şifre:", type='password')

    if st.button("Kayıt Ol"):
        if not email or not password:
            st.error("Lütfen tüm bilgileri doldurun.")
        else:
            register(email, password)

# Ana fonksiyon
def main():
    # Sayfalar arasında gezinmek için seçenekler
    page_options = ["Ana Sayfa", "Kadınların Sektörde Yaşadığı Zorluklar", "Sektörde Kadının Liderliği", "Token Mimarisi", "Kayıt Ol"]
    selected_page = st.sidebar.selectbox("Sayfa Seç", page_options)

    # Seçilen sayfayı göster
    if selected_page == "Ana Sayfa":
        home_page()
    elif selected_page == "Kadınların Sektörde Yaşadığı Zorluklar":
        challenges_page()
    elif selected_page == "Sektörde Kadının Liderliği":
        leadership_page()
    elif selected_page == "Token Mimarisi":
        token_architecture_page()
    elif selected_page == "Kayıt Ol":
        register_page()

# Arka plan görselini eklemek için CSS kullanma
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("{background_image}");
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    create_table()
    main()


