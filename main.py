import streamlit as st
import sqlite3

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

def register(email, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (email, password) VALUES (?, ?)
    ''', (email, password))

    conn.commit()
    conn.close()

    st.success("Başarıyla kayıt oldunuz!")

def home_page():

    st.header("Ana Sayfa")
    st.write("Web3 ve blockchain teknolojileriyle güçlendirilmiş platformumuz,"
             " girişimciliğinizi desteklemek ve büyütmek için tasarlandı."
             "Girişimlerinizi paylaşabileceğiniz, destek alabileceğiniz ve büyütebileceğiniz bir ekosistemde bulunmak ister misiniz?"
             " İşte bu platform, hayallerinizi gerçeğe dönüştürmek için tasarlandı. "
             "Üyelerimiz olarak, girişimlerinize destek sağlamanın ve aynı zamanda kendinizi geliştirmenin bir yolunu sunuyoruz."
             "Platformumuza üye olduktan sonra girişimlerinizi burada sergileyebilecek ve ihtiyacınız olan desteği topluluktan alabileceksiniz. "
             "Örneğin, girişiminiz için 100 milyon değerinde token'e ihtiyacınız varsa, "
             "bu tokenler arz edilecek ve platformdaki diğer üyelerimiz parça parça yatırım yapabilecekler."
             " Bu, sadece girişiminize değil, aynı zamanda yatırım yapan diğer kadın üyelerimize de kazanç sağlayacak bir model olarak sizlere sunulmaktadır."
             "Her bir token başlangıçta 1'e 1 değerinde olacak, ancak platformumuzda yer alan eğitimler ve görevlerle bu değeri artırabileceksiniz. "
             "Yaptığınız katkılar ve başarılarınızla, belki de gün sonunda kendi girişimciliğinizin melek yatırımcısı olabilirsiniz."
             "Gelin, birlikte kadın girişimciliğine yeni bir soluk getirelim. Hayallerinizi destekleyen bir toplulukta yer alın ve başarıyı birlikte inşa edelim."
             "Siz de bu heyecan verici yolculuğa katılmak ve kadın girişimciliğine yeni bir boyut kazandırmak istiyorsanız, şimdi platformumuza üye olun!"
             "Daha fazla bilgi için bizimle iletişime geçebilir veya platformumuza göz atabilirsiniz.Başarılarla dolu bir gelecek için birlikte adım atalım!"
             "")

def challenges_page():
    st.header("Kadınların Sektörde Yaşadığı Zorluklar")
    st.write("""
        Kadınların teknoloji sektöründe karşılaştığı zorluklar konusunda bilgi ve farkındalık oluşturulması.
    """)
    st.subheader("İstatistikler")
    st.markdown("Amerika Birleşik Devletleri'nde Catalyst'in 2021 Catalyst Census: Women Board Directors raporundan bir veriye göre, Fortune 500 şirketlerindeki yönetim kurulu pozisyonlarında kadınların temsili artış göstermiştir. 2020 yılında Fortune 500 şirketlerinin yönetim kurullarında kadınların oranı %28.6'ya yükselmiştir. Bu oran 2019'da %26.5 idi. Bu veri, kadınların iş dünyasında yönetim pozisyonlarına yükselme konusunda yavaş ancak istikrarlı bir ilerleme kaydettiğini göstermektedir.")
    st.markdown("Amerika Birleşik Devletleri'nde National Women's Business Council (NWBC) tarafından sağlanan verilere göre, 2019 yılında ABD'deki küçük işletmelerin %42'si kadınlar tarafından yönetilmekteydi. Bu, ABD'deki işletmelerin neredeyse yarısının kadınlar tarafından yönetildiği anlamına gelmektedir. Ayrıca, ABD'deki yeni işletmelerin yaklaşık %40'ının da kadınlar tarafından kurulduğu belirtilmektedir.")
    st.markdown("Kaynak: National Women's Business Council (NWBC), 2020 Small Business Credit Survey: Report on Women-Owned Firms, 2020")

    st.markdown("Avrupa İstatistik Ofisi'nin (Eurostat) verilerine göre,"
                " 2020 yılında Avrupa Birliği'nde kadınların iş gücüne katılım oranı %67.4 idi."
                " Bu oran, 2010'da %63.6'ya kıyasla artış göstermektedir. "
                "Bu veri, Avrupa'da kadınların işgücüne katılımının zaman içinde arttığını göstermektedir.")
    st.markdown("Kaynak: Eurostat, Labour market participation rate by sex, 2020.")

    st.subheader("Kadınların Sektörde Yaşadığı Zorluklar")
    st.write("1) Sermaye Eksikliği: Kadın girişimcilerin iş kurmaları için yeterli sermayeye sahip olmamaları.")
    st.write(
        "2) Toplumun Geleneksel İnanç ve Baskısı: Toplumun kadınların iş hayatına katılımına yönelik geleneksel inanç ve baskıları.")
    st.write(
        "3) Cinsiyete Dayalı Rol Ayrımcılığı: Kadınların toplumda belirlenen cinsiyet rollerine dayalı ayrımcılığa maruz kalması.")
    st.write("*Cinsel ve Duygusal Taciz: Kadınların iş yaşamlarında cinsel veya duygusal tacize uğrama riski.")
    st.write(
        "4) Cam Tavan Engeli: Kadınların kariyerlerinde üst düzey pozisyonlara terfi etmelerini engelleyen görünmez engeller.")
    st.write(
        "5) Sosyal Pozisyon ve İletişim Eksikliği: Kadınların toplum içindeki sosyal pozisyonlarının düşüklüğü ve iletişim ağlarındaki eksiklikleri.")
    st.write(
        "6) Yasalardan Kaynaklanan Engeller: Yasalarda yer alan cinsiyete dayalı ayrımcılık ve kadınlara uygun görülmeyen işlerle ilgili engeller")
    st.write(
        "7. Basmakalıp Yargılar: Kadınlar, iş yaşamında karşılaştıkları basmakalıp yargılar ve önyargılar nedeniyle adil bir değerlendirme görmeyebilirler.")
    st.write(
        "8. Rol Çatışması: Kadınlar, iş ve özel yaşamları arasındaki dengeyi sağlama zorunluluğuyla karşı karşıya kalabilirler, bu da iş hayatında performanslarını etkileyebilir.")
    st.write(
        "9. Eğitim Düzeyinin Düşüklüğü: Kadınların eğitim düzeyinin düşük olması, iş hayatında ilerlemelerini ve potansiyellerini gerçekleştirmelerini engelleyebilir.")
    st.write(
        "10. Zaman Darlığı: Kadın girişimcilerin zaman kısıtlılığı, işlerini geliştirmeye veya yeni girişimlerde bulunmaya yeterli zaman ayıramamalarına neden olabilir.")
    st.write(
        "11. Sosyal Sorunlar: Kadınların iş hayatına katılımını engelleyen sosyal sorunlar, örneğin çocuk bakımı ve eğitimi gibi, iş yaşamını olumsuz etkileyebilir.")
    st.write(
        "12. Sağlık ve Psikolojik Sorunlar: Kadınların sağlık ve psikolojik sorunları, iş verimliliği üzerinde olumsuz etkiler yaratabilir ve iş hayatında ilerlemelerini engelleyebilir.")


def leadership_page():
    st.header("Sektörde Kadının Liderliği")
    st.write("""
        Teknoloji sektöründe kadın liderlerin başarıları ve liderlik rollerinde karşılaştıkları zorluklar.
    """)
    st.markdown("Campbell ve Vera (2008), İspanya'da kadınların işgücüne tarihsel olarak minimal katılımının olduğu bir ortamda, kadınların kurul içindeki yüzdesinin firmanın değeri üzerinde olumlu bir etkisi olduğunu buldu. "
                "Ayrıca, İspanyol yönetim kurullarındaki kadınların yüzdesinin firma değeri üzerinde pozitif bir etkisi olduğunu öne sürdüler.")

    st.subheader("SheNexTech KADIN GİRİŞİMCİLERİ NASIL DESTEKLİYOR?")
    st.markdown("Mentorluk ve Ağ Oluşturma:Mentor bulma özelliği ile kadın girişimcilere deneyimli mentörlerle bağlantı kurma imkanı sunarak, onlara rehberlik ve destek sağlamak. Etkinlikler kısmında düzenlenen etkinlikler aracılığıyla kadın girişimcilerin bir araya gelmelerini ve işbirlikleri oluşturmalarını teşvik etmek.")

    st.subheader("Mağaza ve Pazar Yeri:Mağaza kısmı girişimlere özel olarak, kadın girişimcilerin ürün veya hizmetlerini sergileyebilecekleri bir pazar yeri oluşturarak görünürlüklerini artırmak.")

    st.subheader("Eğitim ve Bilgi Paylaşımı: Etkinlikler bölümünde eğitim, seminer ve etkinlik takvimi düzenleyerek kadın girişimcilerin bilgi birikimini artırmalarını sağlamak.Bilgi Bölümü aracılığıyla, tokenizasyon, platform içindeki işleyiş ve genel bilgileri paylaşarak kadın girişimcilerin platformu daha iyi anlamalarına yardımcı olmak.")

def token_architecture_page():
    st.header("Token Mimarisi")
    st.write("""
        Token Mimarisi Değerli Kararlar, Güçlü Destek
    """)
    st.markdown("""
    **Platformumuzda Token Mimarisi**

    Platformumuzda token mimarisi, girişimcilere ve yatırımcılara güçlü bir katılım ve etki sağlayacak şekilde tasarlandı. Özel amaçlı bir şirket aracılığıyla desteklenen bu mimari, girişimlerinizi büyütürken aynı zamanda karar alma süreçlerinde de aktif olmanızı sağlayacak.

    **Özel Amaçlı Şirket:**
    Platformumuzun merkezinde, girişimcilerin ve yatırımcıların ortaklaşa yönlendireceği özel bir amaçlı şirket bulunmaktadır. Bu şirket, girişimlere destek vermek, mentorluk sağlamak ve önemli kararları almak için oluşturulmuştur. Girişimcilere rehberlik ederken aynı zamanda platformun stratejik yönünü belirlemek üzere görevlendirilmiştir.

    **Token Sahiplerinin Gücü:**
    Platformumuzdaki token sahipleri, önemli karar alma süreçlerinde etkin rol oynama hakkına sahiptirler. Tokenlerinizin sahibi olarak, platformun gelişimine doğrudan katkıda bulunabilir, yeni fikirleri destekleyebilir ve stratejik yönlendirmelerde bulunabilirsiniz. Bu, platformun sadece size değil, tüm üyelerimize ait olduğunu vurgulamak adına önemli bir adımdır.

    **Destek ve Mentorluk:**
    Token sahipleri, platformumuzda yer alan girişimlere sağlanacak destek ve mentorluk süreçlerinde de aktif rol alacaktır. Girişimcilerin başarılı olmaları için gereken kaynakları ve rehberliği sağlamak, platformun temel amaçları arasındadır. Bu sayede, birlikte büyüyebilme ve öğrenme ortamı yaratmış olacağız.

    Token mimarimiz, platformumuzun katılımcı ve adil bir yapıya sahip olmasını sağlarken aynı zamanda kadın girişimcilerin güçlenmesine odaklanmıştır. Token sahipleri olarak sizler, platformun gerçek sahipleri ve yönlendiricilerisiniz. Birlikte, kadın girişimciliğinin yeni ve güçlü bir dönemini inşa etmek için adım atıyoruz.
    """)
def register_token(email, password, token_value):
    conn_1 = sqlite3.connect('token_database.db')
    cursor_1 = conn_1.cursor()

    cursor_1.execute('''
        INSERT INTO users (email, password, token_value) VALUES (?, ?, ?)
    ''', (email, password, token_value))

    conn_1.commit()
    conn_1.close()

    st.success("Token Alımı Gerçekleşti!")

def token_alma_page():
    st.header("Bianance Cüzdanı")
    st.header("Aşağıdaki formu kullanarak sanal cüzdanınıza token yükleyebilirsiniz.")
    email = st.text_input("E-posta:")
    password = st.text_input("Şifre:", type='password')
    token_value = st.text_input("Token Miktarı")

    if st.button("Token Al"):
        if not email or not password or token_value <= 0:
            st.error("Lütfen tüm bilgileri doldurun ve geçerli bir token miktarı girin.")
        else:
            register_token(email, password, token_value)



# 21 ve 22 görseller eklenecek bu token_arhitecture sayfasına
def register_page():
    st.header("Kayıt Ol")
    email = st.text_input("E-posta:")
    password = st.text_input("Şifre:", type='password')

    if st.button("Kayıt Ol"):
        if not email or not password:
            st.error("Lütfen tüm bilgileri doldurun.")
        else:
            register(email, password)


def passport_page():
    st.header("Missions")
    st.markdown("Seviye 1")
    st.write("Profil fotoğrafı yükle.")
    st.write( "Telefon numaranı doğrula.")
    st.write(" Binance cüzdanını bağla.")
    st.markdown("Seviye 2")
    st.write("50$ token yükle.")


def main():
    st.sidebar.title("Navigation")
    page_options = ["Ana Sayfa", "Kadınların Sektörde Yaşadığı Zorluklar", "Sektörde Kadının Liderliği", "Token Mimarisi", "Kayıt Ol", "Token Alma", "Passport"]
    selected_page = st.sidebar.selectbox("Sayfa Seç", page_options)

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
    elif selected_page == "Token Alma":
        token_alma_page()
    elif selected_page == "Passport":
        passport_page()

if __name__ == "__main__":
    create_table()
    main()



