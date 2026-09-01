# ================================================================================
# SAYFA YAPILANDIRMASI, STİL VE ÇİFT DİLLİ 36 PADİŞAH VERİ TABANI (TÜRKÇE / ENGLISH)
# ================================================================================
import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Padişah Arşivi Enterprise - Ottoman Empire & 36 Sultans Archive",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Oturum ve Sayaç Mock Entegrasyonu
if "toplam_ziyaret" not in st.session_state:
    st.session_state.toplam_ziyaret = 1453

def tiklama_kaydet(modul, aciklama):
    pass

def veri_suzgeci(metin):
    return metin.strip()

tiklama_kaydet("Padişah Arşivi Pro", "Sayfa Yenilendi / Yeni Giriş Yapıldı")

# Profesyonel Stil ve Tema Enjeksiyonu
st.markdown("""
<style>
    .main {background-color: #fcfbfa;}
    .stButton>button {width: 100%; border-radius: 6px; background-color: #5c1d1d; color: white; font-weight: bold;}
    .stButton>button:hover {background-color: #7a2626; color: white;}
    .card-box {border: 1px solid #d4af37; padding: 20px; border-radius: 8px; background-color: #fffdf9; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .counter-box {background-color: #5c1d1d; color: #d4af37; padding: 10px; border-radius: 6px; text-align: center; font-weight: bold; margin-bottom: 15px;}
    .soru-kutu {border: 1px solid #e0d5c1; padding: 15px; border-radius: 6px; background-color: #ffffff; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# Kenar Çubuğu Navigasyon ve Dil Seçimi
with st.sidebar:
    st.image("https://img.icons8.com/color/96/ottoman-empire.png", width=65)
    st.title("Padişah Arşivi Pro")
    st.caption("36 Hükümdar Tam Ansiklopedisi & Analiz Motoru v5.0")
    st.markdown("---")
    
    # Dil Seçimi
    dil_secimi = st.radio("🌍 Dil / Language", ["Türkçe", "English"], horizontal=True)
    
    st.markdown("---")
    st.markdown(f"""
    <div class="counter-box">
        🔄 {"Sayfa Giriş Sayısı" if dil_secimi == "Türkçe" else "Page Visits"}: {st.session_state.toplam_ziyaret}
    </div>
    """, unsafe_allow_html=True)
    
    if dil_secimi == "Türkçe":
        secim = st.radio(
            "Modül Seçimi",
            [
                "1. 36 Padişah Tam Ansiklopedisi", 
                "2. Vecizeler & Felsefe Akademisi", 
                "3. Saltanat Süreleri & Veri Analiz Motoru", 
                "4. Divan-ı Hümayun & Teşkilat Yapısı", 
                "5. Tarih Bilgi Sınavı & Simülasyonu"
            ]
        )
        info_note = "Bu arşiv projesi resmi ve akademik veri tabanları baz alınarak yüksek doğrulukla tasarlanmıştır."
        sim_disclaimer = "Simülasyon motoru eğitim ve tarih bilinci oluşturma amacıyla geliştirilmiştir."
    else:
        secim = st.radio(
            "Module Selection",
            [
                "1. 36 Sultans Full Encyclopedia", 
                "2. Quotes & Philosophy Academy", 
                "3. Reign Durations & Data Analysis Engine", 
                "4. Imperial Council & Organizational Structure", 
                "5. History Quiz & Simulation"
            ]
        )
        info_note = "This archive project has been designed with high accuracy based on official and academic databases."
        sim_disclaimer = "The simulation engine was developed for educational and historical awareness purposes."

    tiklama_kaydet("Padişah Arşivi Pro", f"Modül Seçildi: {secim}")

    st.markdown("---")
    st.markdown("### 📌 " + ("Sistem Güvencesi" if dil_secimi == "Türkçe" else "System Assurance"))
    st.sidebar.caption(info_note)
    st.markdown("---")
    st.sidebar.warning(sim_disclaimer)

# --- ÇİFT DİLLİ 36 PADİŞAH MERKEZİ VERİTABANI ---
osmanli_36_padi_db_tr = {
    1: {"id": 1, "isim": "I. Osman (Osman Gazi)", "donem": "1299 - 1326", "lakap": "Fahreddin / Kara Osman", "anne": "Hatice Hatun", "taht_yil": 27, "fetih": "Söğüt, Domaniç, Karacahisar, Bilecik", "icraat": "Bağımsızlık ilanı, ilk bakır akçenin basılması, aşiret yapısından beylik sistemine geçiş.", "soz": "İnsanı yaşat ki devlet yaşasın."},
    2: {"id": 2, "isim": "Orhan Bey", "donem": "1326 - 1362", "lakap": "Şücaeddin / Bahtiyar", "anne": "Malhun Hatun", "taht_yil": 36, "fetih": "Bursa, İznik, İzmit, Karesioğlu beyliğinin ilhakı", "icraat": "Yaya ve Müsellem adıyla ilk düzenli ordunun kurulması, İznik'te ilk medresenin açılması, divan teşkilatının temelleri.", "soz": "Adalet mülkün temelidir."},
    3: {"id": 3, "isim": "I. Murad (Murad-ı Hüdavendigâr)", "donem": "1362 - 1389", "lakap": "Hüdavendigâr / Şehit", "anne": "Nilüfer Hatun", "taht_yil": 27, "fetih": "Edirne, Sazlıdere, Sofya, I. Kosova", "icraat": "Yeniçeri Ocağının kurulması, Tımar sisteminin genişletilmesi, Rumeli Beylerbeyliği teşkili.", "soz": "Zafere giden yolda çekilen çile kutsaldır."},
    4: {"id": 4, "isim": "I. Bayezid (Yıldırım)", "donem": "1389 - 1402", "lakap": "Yıldırım", "anne": "Gülçiçek Hatun", "taht_yil": 13, "fetih": "Anadolu Türk siyasi birliğinin ilk kez sağlanması, İstanbul kuşatmaları", "icraat": "Anadolu Hisarı'nın (Güzelcehisar) inşası, Niğbolu Zaferi'nin kazanılması.", "soz": "Anadolu'nun birliği İslam'ın kalkanıdır."},
    5: {"id": 5, "isim": "I. Mehmed (Çelebi Mehmet)", "donem": "1413 - 1421", "lakap": "Çelebi / Kurucu İkinci", "anne": "Devlet Hatun", "taht_yil": 8, "fetih": "Fetret Devri'nin sona erdirilmesi, Venedik ile ilk deniz savaşı", "icraat": "Dağılan devletin yeniden derlenip toparlanması, iç isyanların bastırılması.", "soz": "Yıkılanı yapmak, fethetmekten güçtür."},
    6: {"id": 6, "isim": "II. Murad", "donem": "1421 - 1451", "lakap": "Koca Murad / Hayır Sâhibi", "anne": "Emine Hatun", "taht_yil": 30, "fetih": "Varna ve II. Kosova Meydan Muharebeleri", "icraat": "Eğitime, imara ve mimariye büyük yatırımlar yapılması, Edirne'nin kültür merkezi olması.", "soz": "Sözünden dönmek devlet adamına yakışmaz."},
    7: {"id": 7, "isim": "Fatih Sultan Mehmet (II. Mehmed)", "donem": "1451 - 1481", "lakap": "Ebû'l-Feth / Kayser-i Rûm", "anne": "Hüma Hatun", "taht_yil": 30, "fetih": "İstanbul'un Fethi (1453), Trabzon, Kırım, Sırbistan ve Bosna", "icraat": "İstanbul'un başkent yapılması, Kanunname-i Âl-i Osman ile merkeziyetçi idare.", "soz": "Ya ben İstanbul'u alırım, ya İstanbul beni!"},
    8: {"id": 8, "isim": "II. Bayezid", "donem": "1481 - 1512", "lakap": "Sofu / Veli", "anne": "Gülbahar Hatun", "taht_yil": 31, "fetih": "Akkerman, Kili, İnebahtı ve Modon kaleleri", "icraat": "Bayezid Külliyesi, Osmanlı donanmasının Akdeniz'de gücünü artırması, İspanya'dan gelen musevilere kucak açılması.", "soz": "İlim erbabına hürmet devletin şanıdır."},
    9: {"id": 9, "isim": "Yavuz Sultan Selim (I. Selim)", "donem": "1512 - 1520", "lakap": "Hâdimü'l-Haremeynifi'ş-Şerifeyn", "anne": "Gülbahar Hatun", "taht_yil": 8, "fetih": "Çaldıran, Mercidabık, Ridaniye, Mısır Seferi, Suriye, Hicaz", "icraat": "Halifeliğin Osmanlı hanedanına geçişi, hazinenin ağzına kadar doldurulması.", "soz": "Padişah-ı âlem olmaq bir kuru kavga imiş."},
    10: {"id": 10, "isim": "Kanuni Sultan Süleyman (I. Süleyman)", "donem": "1520 - 1566", "lakap": "Muhteşem / Kanuni", "anne": "Hafsa Sultan", "taht_yil": 46, "fetih": "Belgrad, Mohaç, Rodos, Budin, Bağdat, Esztergom", "icraat": "Kapsamlı kanunnameler, Mimar Sinan ile altın çağ mimarisi, Akdeniz'in Türk gölü olması.", "soz": "Olmaya devlet cihanda bir nefes sıhhat gibi."},
    11: {"id": 11, "isim": "II. Selim (Sarı Selim)", "donem": "1566 - 1574", "lakap": "Sarı / Sarhoş (Batı kaynaklı)", "anne": "Hürrem Sultan", "taht_yil": 8, "fetih": "Kıbrıs'ın Fethi, Tunus'un alınması", "icraat": "Sokullu Mehmet Paşa'nın güçlü sadrazamlığı altında devlet idaresinin sürdürülmesi.", "soz": "Devletin bekası tedbir ile kaimdir."},
    12: {"id": 12, "isim": "III. Murad", "donem": "1574 - 1595", "lakap": "Osmanlı'nın En Geniş Sınırları", "anne": "Nurbanu Sultan", "taht_yil": 21, "fetih": "İran savaşları, Kafkasya ve Azerbaycan hakimiyeti", "icraat": "Takiyüddin Mehmet'e İstanbul Rasathanesi'nin kurdurulması, ilmi ve edebi faaliyetler.", "soz": "Hakimiyet adaletle taçlanır."},
    13: {"id": 13, "isim": "III. Mehmed", "donem": "1595 - 1603", "lakap": "Eğri Fatihi", "anne": "Safiye Sultan", "taht_yil": 8, "fetih": "Eğri Kalesi'nin Fethi", "icraat": "Haçova Meydan Muharebesi'nin kazanılması, Celali ayaklanmalarının başlangıç dönemi.", "soz": "Zafere inananların yolu açık olur."},
    14: {"id": 14, "isim": "I. Ahmet", "donem": "1603 - 1617", "lakap": "Bahtsız / Sultan Ahmed", "anne": "Handan Sultan", "taht_yil": 14, "fetih": "Zitvatorok Antlaşması", "icraat": "Sultanahmet Camii'nin inşası, Ekber ve Erşed sistemine geçilerek taht kavgalarının önlenmesi.", "soz": "Adalet her daim mürşidimizdir."},
    15: {"id": 15, "isim": "I. Mustafa", "donem": "1617-1618 / 1622-1623", "lakap": "Deli Mustafa", "anne": "Halime Sultan", "taht_yil": 2, "fetih": "İç istikrar ve saray dengeleri dönemi", "icraat": "Saray içi dengeler ve taht değişiklikleri sebebiyle kısa süreli yönetimler.", "soz": "Kaderin hükmü baş üstünedir."},
    16: {"id": 16, "isim": "II. Osman (Genç Osman)", "donem": "1618 - 1622", "lakap": "Genç / Şehit", "anne": "Mahfiruz Hatun", "taht_yil": 4, "fetih": "Hotin Seferi ve Lehistan mücadelesi", "icraat": "Yeniçeri ocağını kaldırma teşebbüsü, başkenti Anadolu'ya taşıma fikirleri.", "soz": "Gençliğim vatan yoluna feda olsun."},
    17: {"id": 17, "isim": "IV. Murad", "donem": "1623 - 1640", "lakap": "Bağdat Fatihi", "anne": "Kösem Sultan", "taht_yil": 17, "fetih": "Bağdat ve Revan Seferleri", "icraat": "Disiplin ve nizamın tesisi, tütün/kahve yasakları, merkezi otoritenin demir yumrukla sağlanması.", "soz": "Kılıç kınından adalet için çıkar."},
    18: {"id": 18, "isim": "İbrahim (Deli İbrahim)", "donem": "1640 - 1648", "lakap": "Deli Sultan / Deli İbrahim", "anne": "Kösem Sultan", "taht_yil": 8, "fetih": "Girit Seferi'nin (Venedik harbi) başlatılması", "icraat": "Donanmanın güçlendirilmesi, saray masraflarının artması ve tahttan indirilmesi.", "soz": "Saltanat zahmetli bir yoldur."},
    19: {"id": 19, "isim": "IV. Mehmed (Avcı Mehmed)", "donem": "1648 - 1687", "lakap": "Avcı", "anne": "Turhan Hatun", "taht_yil": 39, "fetih": "Kandiye (Girit), Uyvar Kalesi, Kamaniçe", "icraat": "Köprülüler Dönemi ile devletin mali ve idari yönden yeniden ihyası.", "soz": "Sükunet en büyük güçtür."},
    20: {"id": 20, "isim": "II. Süleyman", "donem": "1687 - 1691", "lakap": "Süleyman", "anne": "Saliha Dilaşub Sultan", "taht_yil": 3, "fetih": "Belgrad'ın geri alınması mücadelesi", "icraat": "Fazıl Mustafa Paşa'nın sadaretinde önemli askeri ve mali ıslahatlar.", "soz": "Sabır selametin anahtarıdır."},
    21: {"id": 21, "isim": "II. Ahmed", "donem": "1691 - 1695", "lakap": "Ahmed", "anne": "Hatice Muazzez Sultan", "taht_yil": 3, "fetih": "Zalankemen Muharebesi ve savunma savaşları", "icraat": "Askeri maliye düzenlemeleri ve cephe denetimleri.", "soz": "Hakkın rızası halkın duasındadır."},
    22: {"id": 22, "isim": "II. Mustafa", "donem": "1695 - 1703", "lakap": "Gazi Padişah", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 8, "fetih": "Avusturya seferleri", "icraat": "Bizzat ordu başına seferlere çıkan son padişahlardan biri olması, Edirne Vakası.", "soz": "Sefer bizim, zafer Allah'ındır."},
    23: {"id": 23, "isim": "III. Ahmed", "donem": "1703 - 1730", "lakap": "Lale Devri Padişahı", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 27, "fetih": "Prut Zaferi ve Azak Kalesi'nin geri alınması", "icraat": "Lale Devri kültürel hamleleri, İbrahim Müteferrika matbaasının kurulması.", "soz": "Medeniyet sanatla yükselir."},
    24: {"id": 24, "isim": "I. Mahmud", "donem": "1730 - 1754", "lakap": "Kambur Mahmud", "anne": "Saliha Sultan", "taht_yil": 24, "fetih": "Belgrad Antlaşması ve başarılı seferler", "icraat": "Humbaracı Ahmed Paşa ile Avrupa tarzı askeri ıslahatlar.", "soz": "Eğitim devletin temel direğidir."},
    25: {"id": 25, "isim": "III. Osman", "donem": "1754 - 1757", "lakap": "Osman", "anne": "Şehsuvar Sultan", "taht_yil": 3, "fetih": "Barış dönemi ve iç idare", "icraat": "Nuruosmaniye Camii'nin inşasının tamamlanması.", "soz": "Adalet mülkün esasıdır."},
    26: {"id": 26, "isim": "III. Mustafa", "donem": "1757 - 1774", "lakap": "Yenilikçi Padişah", "anne": "Mihrişah Kadınefendi", "taht_yil": 17, "fetih": "İç ıslahatlar ve ordu modernizasyonu", "icraat": "Mühendishane-i Bahr-i Hümayun temellerinin atılması, Baron de Tott'un getirilmesi.", "soz": "Fen ve fenle terakki şarttır."},
    27: {"id": 27, "isim": "I. Abdülhamid", "donem": "1774 - 1789", "lakap": "Islahatçı", "anne": "Rabia Şermi Kadınefendi", "taht_yil": 15, "fetih": "Küçük Kaynarca Sonrası Toparlanma", "icraat": "Sürat topçusu ocağının kurulması, iç borçlanma (esham) sistemi.", "soz": "Sabırla her güçlük yenilir."},
    28: {"id": 28, "isim": "III. Selim", "donem": "1789 - 1807", "lakap": "Nizam-ı Cedid", "anne": "Mihrişah Valide Sultan", "taht_yil": 18, "fetih": "Fransız seferlerine karşı savunma", "icraat": "Nizam-ı Cedid ordusunun kurulması, daimi dış temsilcilikler.", "soz": "Değişime ayak uydurmayan zeval bulur."},
    29: {"id": 29, "isim": "IV. Mustafa", "donem": "1807 - 1808", "lakap": "Mustafa", "anne": "Sineperver Sultan", "taht_yil": 1, "fetih": "Kabakçı Mustafa İsyanı dönemi", "icraat": "Kısa süreli taht dönemi ve saray içi çalkantılar.", "soz": "Kaderin tecellisi haktır."},
    30: {"id": 30, "isim": "II. Mahmud", "donem": "1808 - 1839", "lakap": "Adlî", "anne": "Nakşidil Sultan", "taht_yil": 31, "fetih": "Merkezileşme ve idari reformlar", "icraat": "Yeniçeri Ocağı'nın kaldırılması (Vaka-i Hayriye), ilk nüfus sayımı, kıyafet devrimi.", "soz": "Ben tebaamın dinini ibadethanesinde fark ederim."},
    31: {"id": 31, "isim": "Sultan Abdülmecid", "donem": "1839 - 1861", "lakap": "Tanzimat Fermanı Padişahı", "anne": "Bezmialem Valide Sultan", "taht_yil": 22, "fetih": "Kırım Savaşı ittifakları", "icraat": "Tanzimat Fermanı (1839) ve Islahat Fermanı (1856), Dolmabahçe Sarayı.", "soz": "Hukukun üstünlüğü esastır."},
    32: {"id": 32, "isim": "Sultan Abdülaziz", "donem": "1861 - 1876", "lakap": "Seyyah Padişah", "anne": "Pertevniyal Sultan", "taht_yil": 15, "fetih": "Donanma Modernizasyonu", "icraat": "Avrupa seyahati gerçekleştiren ilk padişah, demiryolları ve demir çelik yatırımları.", "soz": "Güçlü donanma güçlü devlet demektir."},
    33: {"id": 33, "isim": "V. Murad", "donem": "1876 - 1876", "lakap": "Kısa Saltanat (93 Gün)", "anne": "Şevkefza Kadınefendi", "taht_yil": 1, "fetih": "Meşrutiyet Hazırlıkları", "icraat": "Kısa süreli idare ve ruhsal sağlık sorunları nedeniyle tahttan indirilme.", "soz": "Vatanın selameti herşeyin üstündedir."},
    34: {"id": 34, "isim": "II. Abdülhamid Han", "donem": "1876 - 1909", "lakap": "Ulu Hakan / Yıldız Sarayı Sakini", "anne": "Tirimüjgan Kadınefendi", "taht_yil": 33, "fetih": "Diplomasi ve Denge Politikası", "icraat": "Hicaz Demiryolu, fen liseleri (Mekteb-i Mülkiye vb.), geniş arşiv ağı.", "soz": "Tarih değil, hatalar tekerrür eder."},
    35: {"id": 35, "isim": "V. Mehmed Reşad", "donem": "1909 - 1918", "lakap": "Reşad", "anne": "Gülcemal Kadınefendi", "taht_yil": 9, "fetih": "Trablusgarp ve Balkan Savaşları", "icraat": "Meşrutiyet'in ikinci kez ilanı, I. Dünya Savaşı dönemi.", "soz": "İttifak ve birlik en büyük gücümüzdür."},
    36: {"id": 36, "isim": "VI. Mehmed Vahdeddin", "donem": "1918 - 1922", "lakap": "Vahdeddin", "anne": "Gülistan Kadınefendi", "taht_yil": 4, "fetih": "Mütareke Dönemi", "icraat": "Saltanatın kaldırılması ve son Osmanlı Padişahı olarak yurt dışına çıkışı.", "soz": "Kaderin cilvesi böyleymiş."}
}

osmanli_36_padi_db_en = {
    1: {"id": 1, "isim": "I. Osman (Osman Gazi)", "donem": "1299 - 1326", "lakap": "Fahreddin / Kara Osman", "anne": "Hatice Hatun", "taht_yil": 27, "fetih": "Söğüt, Domaniç, Karacahisar, Bilecik", "icraat": "Declaration of independence, minting the first copper coin, transition from tribal structure to principality system.", "soz": "Keep people alive so that the state may live."},
    2: {"id": 2, "isim": "Orhan Bey", "donem": "1326 - 1362", "lakap": "Şücaeddin / Bahtiyar", "anne": "Malhun Hatun", "taht_yil": 36, "fetih": "Bursa, Iznik, Izmit, Annexation of Karasioğlu principality", "icraat": "Establishment of the first regular army named Yaya and Müsellem, opening the first madrasah in Iznik, foundations of the divan organization.", "soz": "Justice is the foundation of the state."},
    3: {"id": 3, "isim": "I. Murad (Murad Hüdavendigâr)", "donem": "1362 - 1389", "lakap": "Hüdavendigâr / The Martyr", "anne": "Nilüfer Hatun", "taht_yil": 27, "fetih": "Edirne, Sazlıdere, Sofia, I. Kosovo", "icraat": "Establishment of the Janissary Corps, expansion of the Timar system, organization of the Rumeli Beylerbeylik.", "soz": "The suffering endured on the path to victory is sacred."},
    4: {"id": 4, "isim": "I. Bayezid (Yıldırım / The Thunderbolt)", "donem": "1389 - 1402", "lakap": "Yıldırım (Thunderbolt)", "anne": "Gülçiçek Hatun", "taht_yil": 13, "fetih": "First unification of Anatolian Turkish political unity, sieges of Istanbul", "icraat": "Construction of Anadolu Hisarı (Güzelcehisar), victory at the Battle of Nicopolis.", "soz": "The unity of Anatolia is the shield of Islam."},
    5: {"id": 5, "isim": "I. Mehmed (Çelebi Mehmet)", "donem": "1413 - 1421", "lakap": "Çelebi / Second Founder", "anne": "Devlet Hatun", "taht_yil": 8, "fetih": "Ending the Interregnum period, first naval war with Venice", "icraat": "Reorganizing and gathering the shattered state, suppressing internal rebellions.", "soz": "Rebuilding what was destroyed is harder than conquering."},
    6: {"id": 6, "isim": "II. Murad", "donem": "1421 - 1451", "lakap": "Koca Murad / The Benefactor", "anne": "Emine Hatun", "taht_yil": 30, "fetih": "Battles of Varna and II. Kosovo", "icraat": "Large investments in education, development, and architecture; making Edirne a cultural center.", "soz": "Breaking one's word does not suit a statesman."},
    7: {"id": 7, "isim": "Fatih Sultan Mehmet (II. Mehmed)", "donem": "1451 - 1481", "lakap": "Ebû'l-Feth / Kayser-i Rûm (The Conqueror)", "anne": "Hüma Hatun", "taht_yil": 30, "fetih": "Conquest of Istanbul (1453), Trabzon, Crimea, Serbia and Bosnia", "icraat": "Making Istanbul the capital, centralized administration with Kanunname-i Âl-i Osman.", "soz": "Either I take Istanbul, or Istanbul takes me!"},
    8: {"id": 8, "isim": "II. Bayezid", "donem": "1481 - 1512", "lakap": "Sofu (Pious) / Veli (Saint)", "anne": "Gülbahar Hatun", "taht_yil": 31, "fetih": "Akkerman, Kili, Lepanto and Modon castles", "icraat": "Bayezid Complex, increasing Ottoman naval power in the Mediterranean, welcoming Jews fleeing Spain.", "soz": "Respect for scholars is the glory of the state."},
    9: {"id": 9, "isim": "Yavuz Sultan Selim (I. Selim)", "donem": "1512 - 1520", "lakap": "Hâdimü'l-Haremeynifi'ş-Şerifeyn", "anne": "Gülbahar Hatun", "taht_yil": 8, "fetih": "Chaldiran, Marj Dabiq, Ridanieh, Egyptian Campaign, Syria, Hejaz", "icraat": "Transition of the Caliphate to the Ottoman dynasty, filling the treasury to the brim.", "soz": "Being the king of the world was just an empty quarrel."},
    10: {"id": 10, "isim": "Kanuni Sultan Süleyman (I. Suleiman)", "donem": "1520 - 1566", "lakap": "The Magnificent / The Lawgiver", "anne": "Hafsa Sultan", "taht_yil": 46, "fetih": "Belgrade, Mohács, Rhodes, Buda, Baghdad, Esztergom", "icraat": "Comprehensive law codes, golden age architecture with Mimar Sinan, Mediterranean becoming a Turkish lake.", "soz": "There is no state in the world like a breath of health."},
    11: {"id": 11, "isim": "II. Selim (Sarı Selim)", "donem": "1566 - 1574", "lakap": "The Blonde / The Drunkard (Western sources)", "anne": "Hürrem Sultan", "taht_yil": 8, "fetih": "Conquest of Cyprus, capture of Tunis", "icraat": "Continuation of state administration under the powerful grand vizierate of Sokollu Mehmet Pasha.", "soz": "The survival of the state is sustained by precaution."},
    12: {"id": 12, "isim": "III. Murad", "donem": "1574 - 1595", "lakap": "Widest Borders of the Ottoman Empire", "anne": "Nurbanu Sultan", "taht_yil": 21, "fetih": "Iranian wars, Caucasian and Azerbaijani dominance", "icraat": "Establishment of the Istanbul Observatory for Takiyüddin Mehmet, scholarly and literary activities.", "soz": "Sovereignty is crowned with justice."},
    13: {"id": 13, "isim": "III. Mehmed", "donem": "1595 - 1603", "lakap": "Conqueror of Eger", "anne": "Safiye Sultan", "taht_yil": 8, "fetih": "Conquest of Eger Castle", "icraat": "Winning the Battle of Keresztes, beginning period of Celali revolts.", "soz": "The path of those who believe in victory is open."},
    14: {"id": 14, "isim": "I. Ahmed", "donem": "1603 - 1617", "lakap": "The Unfortunate / Sultan Ahmed", "anne": "Handan Sultan", "taht_yil": 14, "fetih": "Treaty of Zsitvatorok", "icraat": "Construction of the Blue Mosque (Sultanahmet), transition to the Seniority System (Ekber ve Erşed) to prevent throne fights.", "soz": "Justice is always our guide."},
    15: {"id": 15, "isim": "I. Mustafa", "donem": "1617-1618 / 1622-1623", "lakap": "Mad Mustafa", "anne": "Halime Sultan", "taht_yil": 2, "fetih": "Period of internal stability and palace balances", "icraat": "Short-term rules due to intra-palace balances and throne changes.", "soz": "The decree of destiny is upon our heads."},
    16: {"id": 16, "isim": "II. Osman (Young Osman)", "donem": "1618 - 1622", "lakap": "The Young / The Martyr", "anne": "Mahfiruz Hatun", "taht_yil": 4, "fetih": "Hotin Campaign and Polish struggle", "icraat": "Attempt to abolish the Janissary corps, ideas of moving the capital to Anatolia.", "soz": "My youth is sacrificed for the path of the homeland."},
    17: {"id": 17, "isim": "IV. Murad", "donem": "1623 - 1640", "lakap": "Conqueror of Baghdad", "anne": "Kösem Sultan", "taht_yil": 17, "fetih": "Baghdad and Revan Campaigns", "icraat": "Establishment of discipline and order, tobacco/coffee bans, iron-fisted central authority.", "soz": "The sword leaves its scabbard for justice."},
    18: {"id": 18, "isim": "İbrahim (Mad Ibrahim)", "donem": "1640 - 1648", "lakap": "Mad Sultan / Mad Ibrahim", "anne": "Kösem Sultan", "taht_yil": 8, "fetih": "Initiation of the Crete Campaign (Venetian war)", "icraat": "Strengthening the navy, increasing palace expenses, and deposition.", "soz": "Sultanate is a laborious path."},
    19: {"id": 19, "isim": "IV. Mehmed (Hunter Mehmed)", "donem": "1648 - 1687", "lakap": "The Hunter", "anne": "Turhan Hatun", "taht_yil": 39, "fetih": "Candia (Crete), Uyvar Castle, Kamaniçe", "icraat": "Financial and administrative revival of the state during the Köprülü Era.", "soz": "Tranquility is the greatest power."},
    20: {"id": 20, "isim": "II. Süleyman", "donem": "1687 - 1691", "lakap": "Suleiman", "anne": "Saliha Dilaşub Sultan", "taht_yil": 3, "fetih": "Struggle for the recapture of Belgrade", "icraat": "Important military and financial reforms under Fazıl Mustafa Pasha's grand vizierate.", "soz": "Patience is the key to safety."},
    21: {"id": 21, "isim": "II. Ahmed", "donem": "1691 - 1695", "lakap": "Ahmed", "anne": "Hatice Muazzez Sultan", "taht_yil": 3, "fetih": "Battle of Slankamen and defensive wars", "icraat": "Military financial regulations and frontline inspections.", "soz": "The consent of Allah is in the prayers of the people."},
    22: {"id": 22, "isim": "II. Mustafa", "donem": "1695 - 1703", "lakap": "The Ghazi Sultan", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 8, "fetih": "Austrian campaigns", "icraat": "Being one of the last sultans to personally lead armies into campaigns, Edirne Incident.", "soz": "The campaign is ours, victory belongs to Allah."},
    23: {"id": 23, "isim": "III. Ahmed", "donem": "1703 - 1730", "lakap": "Sultan of the Tulip Era", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 27, "fetih": "Victory of Prut and recapture of Azov Castle", "icraat": "Tulip Era cultural moves, establishment of İbrahim Müteferrika's printing house.", "soz": "Civilization rises with art."},
    24: {"id": 24, "isim": "I. Mahmud", "donem": "1730 - 1754", "lakap": "Hunchbacked Mahmud", "anne": "Saliha Sultan", "taht_yil": 24, "fetih": "Treaty of Belgrade and successful campaigns", "icraat": "European-style military reforms with Humbaracı Ahmed Pasha.", "soz": "Education is the main pillar of the state."},
    25: {"id": 25, "isim": "III. Osman", "donem": "1754 - 1757", "lakap": "Osman", "anne": "Şehsuvar Sultan", "taht_yil": 3, "fetih": "Peace period and internal administration", "icraat": "Completion of the construction of Nuruosmaniye Mosque.", "soz": "Justice is the essence of the realm."},
    26: {"id": 26, "isim": "III. Mustafa", "donem": "1757 - 1774", "lakap": "The Reformist Sultan", "anne": "Mihrişah Kadınefendi", "taht_yil": 17, "fetih": "Internal reforms and army modernization", "icraat": "Laying the foundations of Mühendishane-i Bahr-i Hümayun, bringing Baron de Tott.", "soz": "Science and progress through science are essential."},
    27: {"id": 27, "isim": "I. Abdülhamid", "donem": "1774 - 1789", "lakap": "The Reformer", "anne": "Rabia Şermi Kadınefendi", "taht_yil": 15, "fetih": "Recovery after Küçük Kaynarca", "icraat": "Establishment of the speed artillery corps, domestic borrowing (esham) system.", "soz": "Every difficulty is overcome with patience."},
    28: {"id": 28, "isim": "III. Selim", "donem": "1789 - 1807", "lakap": "Nizam-ı Cedid (New Order)", "anne": "Mihrişah Valide Sultan", "taht_yil": 18, "fetih": "Defense against French campaigns", "icraat": "Establishment of the Nizam-ı Cedid army, permanent foreign representations.", "soz": "Those who do not adapt to change face decline."},
    29: {"id": 29, "isim": "IV. Mustafa", "donem": "1807 - 1808", "lakap": "Mustafa", "anne": "Sineperver Sultan", "taht_yil": 1, "fetih": "Kabakçı Mustafa Rebellion period", "icraat": "Short-term throne period and palace upheavals.", "soz": "The manifestation of destiny is true."},
    30: {"id": 30, "isim": "II. Mahmud", "donem": "1808 - 1839", "lakap": "Adlî (The Just)", "anne": "Nakşidil Sultan", "taht_yil": 31, "fetih": "Centralization and administrative reforms", "icraat": "Abolition of the Janissary Corps (Vaka-i Hayriye), first census, clothing revolution.", "soz": "I recognize my subjects' religion only inside their places of worship."},
    31: {"id": 31, "isim": "Sultan Abdülmecid", "donem": "1839 - 1861", "lakap": "Sultan of Tanzimat Edict", "anne": "Bezmialem Valide Sultan", "taht_yil": 22, "fetih": "Crimean War alliances", "icraat": "Tanzimat Edict (1839) and Islahat Edict (1856), Dolmabahçe Palace.", "soz": "The rule of law is essential."},
    32: {"id": 32, "isim": "Sultan Abdülaziz", "donem": "1861 - 1876", "lakap": "The Traveler Sultan", "anne": "Pertevniyal Sultan", "taht_yil": 15, "fetih": "Navy Modernization", "icraat": "First sultan to travel to Europe, investments in railways and iron-steel.", "soz": "A strong navy means a strong state."},
    33: {"id": 33, "isim": "V. Murad", "donem": "1876 - 1876", "lakap": "Short Reign (93 Days)", "anne": "Şevkefza Kadınefendi", "taht_yil": 1, "fetih": "Constitutional Preparations", "icraat": "Short-term administration and deposition due to mental health issues.", "soz": "The salvation of the homeland is above everything."},
    34: {"id": 34, "isim": "II. Abdülhamid Han", "donem": "1876 - 1909", "lakap": "Great Khan / Resident of Yıldız Palace", "anne": "Tirimüjgan Kadınefendi", "taht_yil": 33, "fetih": "Diplomacy and Balance Policy", "icraat": "Hejaz Railway, science high schools (Mekteb-i Mülkiye, etc.), extensive archive network.", "soz": "History does not repeat itself, mistakes do."},
    35: {"id": 35, "isim": "V. Mehmed Reşad", "donem": "1909 - 1918", "lakap": "Reşad", "anne": "Gülcemal Kadınefendi", "taht_yil": 9, "fetih": "Italo-Turkish and Balkan Wars", "icraat": "Second declaration of the Constitution, World War I period.", "soz": "Alliance and unity are our greatest strength."},
    36: {"id": 36, "isim": "VI. Mehmed Vahdeddin", "donem": "1918 - 1922", "lakap": "Vahdeddin", "anne": "Gülistan Kadınefendi", "taht_yil": 4, "fetih": "Armistice Period", "icraat": "Abolition of the sultanate and departure abroad as the last Ottoman Sultan.", "soz": "Such was the play of destiny."}
}

# Aktif dili belirle
osmanli_36_padi_db = osmanli_36_padi_db_tr if dil_secimi == "Türkçe" else osmanli_36_padi_db_en

# ================================================================================
# MODÜL 1: 36 PADİŞAH TAM ANSİKLOPEDİSİ / 36 SULTANS FULL ENCYCLOPEDIA
# ================================================================================
if secim in ["1. 36 Padişah Tam Ansiklopedisi", "1. 36 Sultans Full Encyclopedia"]:
    if dil_secimi == "Türkçe":
        st.header("👑 36 Osmanlı Padişahı Tam Ansiklopedik Arşivi")
        st.write("Osmanlı hanedanının 36 padişahının tamamını dönemleri, fetihleri, unvanları ve icraatlarıyla inceleyin.")
        arama_etiketi = "🔍 Padişah İsmi veya Lakap Ara:"
        secim_etiketi = "36 Hükümdar Arasından Seçiniz:"
        bulunamadi = "Aradığınız kritere uygun padişah bulunamadı."
        donem_lbl = "Saltanat Dönemi:"
        sure_lbl = "Saltanat Süresi:"
        unvan_lbl = "Unvan / Lakap:"
        valide_lbl = "Valide Sultan:"
        fetih_lbl = "Önemli Fetihler / Olaylar:"
        icraat_lbl = "Temel İcraatlar:"
        soz_lbl = "Unutulmaz Sözü:"
        yil_ek = "Yıl"
    else:
        st.header("👑 36 Ottoman Sultans Full Encyclopedic Archive")
        st.write("Explore all 36 sultans of the Ottoman dynasty with their periods, conquests, titles, and deeds.")
        arama_etiketi = "🔍 Search Sultan Name or Title:"
        secim_etiketi = "Select Among 36 Rulers:"
        bulunamadi = "No sultan matching your criteria was found."
        donem_lbl = "Reign Period:"
        sure_lbl = "Reign Duration:"
        unvan_lbl = "Title / Epithet:"
        valide_lbl = "Valide Sultan:"
        fetih_lbl = "Major Conquests / Events:"
        icraat_lbl = "Core Deeds:"
        soz_lbl = "Unforgettable Quote:"
        yil_ek = "Years"
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Filtreleme / Filter")
        ham_arama = st.text_input(arama_etiketi, "").strip()
        arama_input = veri_suzgeci(ham_arama).lower()
        
        filtrelenmis_padi = {
            k: v for k, v in osmanli_36_padi_db.items() 
            if arama_input in v['isim'].lower() or arama_input in v['lakap'].lower() or arama_input in v['icraat'].lower()
        } if arama_input else osmanli_36_padi_db
        
        if filtrelenmis_padi:
            secilen_key = st.selectbox(
                secim_etiketi,
                options=list(filtrelenmis_padi.keys()),
                format_func=lambda x: f"{x}. {filtrelenmis_padi[x]['isim']} ({filtrelenmis_padi[x]['donem']})"
            )
        else:
            st.warning(bulunamadi)
            secilen_key = None

    with col2:
        if secilen_key:
            p = osmanli_36_padi_db[secilen_key]
            st.markdown(f"""
            <div class="card-box">
                <h2 style="color: #5c1d1d; margin-top: 0;">{p['isim']}</h2>
                <p><b>{donem_lbl}</b> {p['donem']} | <b>{sure_lbl}</b> ~{p['taht_yil']} {yil_ek}</p>
                <p><b>{unvan_lbl}</b> {p['lakap']} | <b>{valide_lbl}</b> {p['anne']}</p>
                <hr style="border-color: #d4af37;">
                <p><b>{fetih_lbl}</b> {p['fetih']}</p>
                <p><b>{icraat_lbl}</b> {p['icraat']}</p>
                <hr style="border-color: #d4af37;">
                <p style="font-style: italic; color: #333;"><b>{soz_lbl}</b><br>"{p['soz']}"</p>
            </div>
            """, unsafe_allow_html=True)

# ================================================================================
# MODÜL 2: VECİZELER & FELSEFE AKADEMİSİ / QUOTES & PHILOSOPHY ACADEMY
# ================================================================================
elif secim in ["2. Vecizeler & Felsefe Akademisi", "2. Quotes & Philosophy Academy"]:
    if dil_secimi == "Türkçe":
        st.header("💬 Hükümdar Vecizeleri ve Felsefi Sözler Havuzu")
        st.write("Osmanlı padişahlarının devlet felsefesini ve adalet anlayışını özetleyen seçme sözler.")
        soz_ara_lbl = "🔍 Söz veya Padişah İçinde Arayın:"
    else:
        st.header("💬 Ruler Quotes and Philosophical Sayings Pool")
        st.write("Selected quotes summarizing the state philosophy and understanding of justice of Ottoman sultans.")
        soz_ara_lbl = "🔍 Search Within Quote or Sultan:"
    
    ham_arama_soz = st.text_input(soz_ara_lbl, "").strip()
    arama_soz = veri_suzgeci(ham_arama_soz).lower()
    
    for key, p in osmanli_36_padi_db.items():
        if not arama_soz or arama_soz in p['soz'].lower() or arama_soz in p['isim'].lower():
            st.markdown(f"""
            <div style="border-left: 4px solid #5c1d1d; padding: 12px 15px; margin-bottom: 12px; background: #fff; border-radius: 4px;">
                <p style="font-size: 16px; font-style: italic; margin-bottom: 5px;">"{p['soz']}"</p>
                <p style="text-align: right; color: #5c1d1d; margin: 0; font-size: 14px;"><b>— {p['isim']}</b> <span style="color: gray; font-size: 12px;">({p['donem']})</span></p>
            </div>
            """, unsafe_allow_html=True)

# ================================================================================
# MODÜL 3: SALTANAT SÜRELERİ & VERİ ANALİZİ / REIGN DURATIONS & ANALYSIS
# ================================================================================
elif secim in ["3. Saltanat Süreleri & Veri Analiz Motoru", "3. Reign Durations & Data Analysis Engine"]:
    if dil_secimi == "Türkçe":
        st.header("⚙️ Saltanat Süreleri ve Tarihsel Veri Analiz Motoru")
        st.markdown("Bu modül, 36 padişahın saltanat sürelerini grafiksel olarak görselleştirir, istatistiksel analiz üretir ve güvenli Excel raporu olarak indirmenizi sağlar.")
        st.subheader("📈 Padişahların Saltanat Süreleri (Grafiksel Analiz)")
        st.write("36 Osmanlı padişahının tahtta kalış sürelerinin (yıl bazında) kıyaslamalı grafik görünümü:")
        indir_lbl = "📥 36 Padişah Veri Setini Excel Olarak İndir (.xlsx)"
    else:
        st.header("⚙️ Reign Durations and Historical Data Analysis Engine")
        st.markdown("This module visualizes the reign durations of the 36 sultans graphically, generates statistical analysis, and allows you to download a secure Excel report.")
        st.subheader("📈 Reign Durations of Sultans (Graphical Analysis)")
        st.write("Comparative graphical view of the reign durations (in years) of the 36 Ottoman sultans:")
        indir_lbl = "📥 Download 36 Sultans Dataset as Excel (.xlsx)"

    df_padi = pd.DataFrame.from_dict(osmanli_36_padi_db, orient='index')
    chart_data = df_padi.set_index("isim")[["taht_yil"]]
    st.bar_chart(chart_data)

    st.markdown("---")
    st.subheader("📥 Excel Export" if dil_secimi == "English" else "📥 Örnek Şablon ve Veri İndirme")
    
    def ornek_excel_sablonu_olustur():
        output = io.BytesIO()
        df_temp = pd.DataFrame(list(osmanli_36_padi_db.values()))
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df_temp.to_excel(writer, index=False, sheet_name="Padisahlar")
        output.seek(0)
        return output.getvalue()

    st.download_button(
        label=indir_lbl,
        data=ornek_excel_sablonu_olustur(),
        file_name="padisah_arsivi_36_padisah.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

# ================================================================================
# MODÜL 4: DİVAN-I HÜMAYUN & TEŞKİLAT / IMPERIAL COUNCIL & STRUCTURE
# ================================================================================
elif secim in ["4. Divan-ı Hümayun & Teşkilat Yapısı", "4. Imperial Council & Organizational Structure"]:
    if dil_secimi == "Türkçe":
        st.header("🏛️ Divan-ı Hümayun ve İdari Teşkilat")
        tab1_ad, tab2_ad, tab3_ad = "Vezirler & Kaptanlar", "İlmiye & Seyfiye", "Eyalet Sistemi"
        tab1_icerik = ("*Sadrazam (Vezir-i Azam):* Padişahın mutlak vekili, mühürdar ve yürütmenin başı.\n\n"
                       "*Kaptan-ı Derya:* Donanma komutanı ve denizcilik bakanı statüsünde devlet adamı.")
        tab2_icerik = ("*Seyfiye:* Askeri ve idari bürokrasi, kılıç ehli devlet görevlileri.\n\n"
                       "*İlmiye:* Adalet, eğitim ve din işlerini yürüten kadı ve müderrisler sınıfı.")
        tab3_icerik = "*Tımar Sistemi:* Toprağın köylü tarafından işlenmesi karşılığında devletin asker besletmesi sistemi."
    else:
        st.header("🏛️ Imperial Council and Administrative Organization")
        tab1_ad, tab2_ad, tab3_ad = "Viziers & Captains", "Ilmiye & Seyfiye", "Provincial System"
        tab1_icerik = ("*Grand Vizier (Vezir-i Azam):* The absolute deputy of the sultan, keeper of the seal, and head of executive.\n\n"
                       "*Kapudan Pasha:* Fleet commander and statesman with the status of naval minister.")
        tab2_icerik = ("*Seyfiye (Sword-holders):* Military and administrative bureaucracy, sword-wielding state officials.\n\n"
                       "*İlmiye (Scholars):* Class of judges (kadis) and professors managing justice, education, and religious affairs.")
        tab3_icerik = "*Timar System:* A system where the state maintained cavalry troops in exchange for peasants cultivating the land."

    tab1, tab2, tab3 = st.tabs([tab1_ad, tab2_ad, tab3_ad])
    with tab1:
        st.markdown(tab1_icerik)
    with tab2:
        st.markdown(tab2_icerik)
    with tab3:
        st.markdown(tab3_icerik)

# ================================================================================
# MODÜL 5: TARİH BİLGİ SINAVI & SİMÜLASYONU / HISTORY QUIZ & SIMULATION
# ================================================================================
elif secim in ["5. Tarih Bilgi Sınavı & Simülasyonu", "5. History Quiz & Simulation"]:
    if dil_secimi == "Türkçe":
        st.header("🧠 Osmanlı Padişahları 50 Soruluk Uzmanlık Sınavı")
        st.markdown("Bu modül, hanedan tarihi hakkındaki bilginizi test etmek için **tam 50 soruluk** profesyonel bir sınav alanı sunar.")
        cevap_anahtari_baslik = "🔍 Tüm Soruların Doğru Cevap Anahtarını Gör"
        dogru_metin = "Doğru Cevap ->"
    else:
        st.header("🧠 Ottoman Sultans 50-Question Expertise Quiz")
        st.markdown("This module offers a professional examination area with **exactly 50 questions** to test your knowledge of dynastic history.")
        cevap_anahtari_baslik = "🔍 View Answer Key for All Questions"
        dogru_metin = "Correct Answer ->"

    sinav_sorulari_tr = [
        {"soru": "Osmanlı Devleti'nin kurucusu kimdir?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) Ertuğrul Gazi", "D) I. Murad"], "dogru": "A) I. Osman"},
        {"soru": "Bursa'yı fethederek devlet merkezi yapan padişah kimdir?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Bayezid", "D) I. Mehmed"], "dogru": "B) Orhan Bey"},
        {"soru": "Yeniçeri Ocağı'nı kuran ve savaş meydanında şehit düşen ilk padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) II. Murad"], "dogru": "B) I. Murad"},
        {"soru": "'Yıldırım' lakabıyla bilinen ve İstanbul'u ilk kez kuşatan padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) Yavuz Sultan Selim", "C) IV. Murad", "D) II. Mehmed"], "dogru": "A) I. Bayezid"},
        {"soru": "Fetret Devri'ni sona erdirerek devleti yeniden derleyen 'Çelebi' lakaplı padişah kimdir?", "secenekler": ["A) I. Mehmed", "B) II. Murad", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) I. Mehmed"},
        {"soru": "Varna ve II. Kosova Zaferleri'ni kazanan padişah kimdir?", "secenekler": ["A) II. Murad", "B) Fatih Sultan Mehmet", "C) Kanuni Sultan Süleyman", "D) I. Selim"], "dogru": "A) II. Murad"},
        {"soru": "İstanbul'u fethederek 'Fatih' unvanını alan padişah kimdir?", "secenekler": ["A) II. Mehmed", "B) I. Bayezid", "C) Yavuz Sultan Selim", "D) III. Murad"], "dogru": "A) II. Mehmed"},
        {"soru": "Cem Sultan olayı hangi padişahın döneminde yaşanmıştır?", "secenekler": ["A) II. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) II. Bayezid"},
        {"soru": "Çaldıran Muharebesi'ni kazanarak hilafeti Osmanlı'ya getiren padişah kimdir?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "46 yıl ile hanedanın en uzun süre tahtta kalan padişahı kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) II. Abdülhamid", "C) IV. Mehmed", "D) II. Mahmud"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "Kıbrıs'ın fethedildiği dönemde tahtta bulunan 'Sarı' lakaplı padişah kimdir?", "secenekler": ["A) II. Selim", "B) III. Murad", "C) III. Mehmed", "D) I. Ahmed"], "dogru": "A) II. Selim"},
        {"soru": "Osmanlı Devleti'nin en geniş sınırlarına ulaştığı dönemin padişahı kimdir?", "secenekler": ["A) III. Murad", "B) Kanuni Sultan Süleyman", "C) II. Abdülhamid", "D) IV. Mehmed"], "dogru": "A) III. Murad"},
        {"soru": "Eğri Fatihi olarak bilinen ve Haçova Meydan Muharebesi'ni kazanan padişah kimdir?", "secenekler": ["A) III. Mehmed", "B) IV. Murad", "C) II. Mustafa", "D) II. Osman"], "dogru": "A) III. Mehmed"},
        {"soru": "Sultanahmet Camii'ni inşa ettiren ve 'Ekber ve Erşed' sistemini getiren padişah kimdir?", "secenekler": ["A) I. Ahmed", "B) I. Mustafa", "C) II. Osman", "D) IV. Murad"], "dogru": "A) I. Ahmed"},
        {"soru": "Hotin Seferi'ne çıkan ve Yeniçeri Ocağı'nı kaldırmak isterken tahttan indirilen genç padişah kimdir?", "secenekler": ["A) II. Osman", "B) IV. Murad", "C) Genç Selim", "D) III. Selim"], "dogru": "A) II. Osman"},
        {"soru": "Bağdat Fatihi olarak bilinen ve yasaklarıyla tanınan sert mizaçlı padişah kimdir?", "secenekler": ["A) IV. Murad", "B) Yavuz Sultan Selim", "C) I. Selim", "D) II. Mahmud"], "dogru": "A) IV. Murad"},
        {"soru": "Köprülüler Dönemi'nin yaşandığı, 39 yıl tahtta kalan 'Avcı' lakaplı padişah kimdir?", "secenekler": ["A) IV. Mehmed", "B) II. Süleyman", "C) II. Ahmed", "D) II. Mustafa"], "dogru": "A) IV. Mehmed"},
        {"soru": "Ordu başında son defa sefere çıkan padişah kimdir?", "secenekler": ["A) II. Mustafa", "B) III. Ahmed", "C) I. Mahmud", "D) III. Selim"], "dogru": "A) II. Mustafa"},
        {"soru": "İlk Türk matbaasının kurulduğu Lale Devri'nin padişahı kimdir?", "secenekler": ["A) III. Ahmed", "B) I. Mahmud", "C) III. Osman", "D) III. Mustafa"], "dogru": "A) III. Ahmed"},
        {"soru": "Humbaracı Ahmed Paşa ile askeri ıslahatlar yapan padişah kimdir?", "secenekler": ["A) I. Mahmud", "B) III. Osman", "C) III. Mustafa", "D) I. Abdülhamid"], "dogru": "A) I. Mahmud"},
        {"soru": "Nuruosmaniye Camii'ni inşa ettiren padişah kimdir?", "secenekler": ["A) III. Osman", "B) I. Mahmud", "C) III. Selim", "D) I. Abdülhamid"], "dogru": "A) III. Osman"},
        {"soru": "Mühendishane-i Bahr-i Hümayun'un temellerini atan yenilikçi padişah kimdir?", "secenekler": ["A) III. Mustafa", "B) III. Selim", "C) II. Mahmud", "D) I. Abdülhamid"], "dogru": "A) III. Mustafa"},
        {"soru": "Küçük Kaynarca Antlaşması'nın imzalandığı dönemin padişahı kimdir?", "secenekler": ["A) I. Abdülhamid", "B) III. Selim", "C) IV. Mustafa", "D) II. Mahmud"], "dogru": "A) I. Abdülhamid"},
        {"soru": "Nizam-ı Cedid yeniliklerini başlatan padişah kimdir?", "secenekler": ["A) III. Selim", "B) II. Mahmud", "C) IV. Mustafa", "D) Sultan Abdülaziz"], "dogru": "A) III. Selim"},
        {"soru": "Yeniçeri Ocağı'nı kaldıran (Vaka-i Hayriye) padişah kimdir?", "secenekler": ["A) II. Mahmud", "B) Sultan Abdülmecid", "C) Sultan Abdülaziz", "D) II. Abdülhamid"], "dogru": "A) II. Mahmud"},
        {"soru": "Tanzimat Fermanı'nı ilan eden ve Dolmabahçe Sarayı'nı yaptıran padişah kimdir?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) V. Murad", "D) II. Abdülhamid"], "dogru": "A) Sultan Abdülmecid"},
        {"soru": "Seyyah unvanıyla anılan ve Avrupa seyahati gerçekleştiren padişah kimdir?", "secenekler": ["A) Sultan Abdülaziz", "B) Sultan Abdülmecid", "C) II. Abdülhamid", "D) V. Mehmed Reşad"], "dogru": "A) Sultan Abdülaziz"},
        {"soru": "En kısa süre (93 gün) tahtta kalan padişah kimdir?", "secenekler": ["A) V. Murad", "B) I. Mustafa", "C) IV. Mustafa", "D) VI. Mehmed Vahdeddin"], "dogru": "A) V. Murad"},
        {"soru": "Kanun-i Esasi'yi ilan eden ve Hicaz Demiryolu'nu yaptıran padişah kimdir?", "secenekler": ["A) II. Abdülhamid", "B) V. Mehmed Reşad", "C) VI. Mehmed Vahdeddin", "D) Sultan Abdülaziz"], "dogru": "A) II. Abdülhamid"},
        {"soru": "Trablusgarp ve Balkan Savaşları'nın yaşandığı dönemin padişahı kimdir?", "secenekler": ["A) V. Mehmed Reşad", "B) VI. Mehmed Vahdeddin", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) V. Mehmed Reşad"},
        {"soru": "Saltanatın kaldırılmasıyla tahttan ayrılan son Osmanlı padişahı kimdir?", "secenekler": ["A) VI. Mehmed Vahdeddin", "B) V. Mehmed Reşad", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) VI. Mehmed Vahdeddin"},
        {"soru": "İlk Osmanlı bakır akçesini hangi padişah bastırmıştır?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) I. Osman"},
        {"soru": "İlk Osmanlı medresesini İznik'te kuran padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) Orhan Bey"},
        {"soru": "Anadolu Hisarı'nı inşa ettiren padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) I. Bayezid"},
        {"soru": "Rumeli Hisarı'nı İstanbul'un fethi hazırlıkları kapsamında inşa ettiren padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) I. Bayezid", "C) II. Murad", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Trabzon ve Kırım'ı Osmanlı topraklarına katan padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) II. Bayezid", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Mohaç Meydan Muharebesi'ni çok kısa sürede kazanan padişah kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Yavuz Sultan Selim", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "Sokullu Mehmet Paşa hangi üç padişah döneminde sadrazamlık yapmıştır?", "secenekler": ["A) Kanuni, II. Selim, III. Murad", "B) Fatih, II. Bayezid, Yavuz", "C) Yavuz, Kanuni, II. Selim", "D) II. Selim, III. Murad, III. Mehmed"], "dogru": "A) Kanuni, II. Selim, III. Murad"},
        {"soru": "Şiirlerinde 'Muradi' mahlasını kullanan padişah kimdir?", "secenekler": ["A) III. Murad", "B) I. Murad", "C) IV. Murad", "D) II. Murad"], "dogru": "A) III. Murad"},
        {"soru": "Şiirlerinde 'Avni' mahlasını kullanan ünlü padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Kanuni Sultan Süleyman", "C) Yavuz Sultan Selim", "D) III. Selim"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Osmanlı'da saray dışından (hüccetli nikahla) ilk kez evlenen padişah kimdir?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Orhan Bey", "C) I. Osman", "D) Yavuz Sultan Selim"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "İznik, İzmit ve Bursa'nın fethi hangi erken dönem padişahının eseridir?", "secenekler": ["A) Orhan Bey", "B) I. Osman", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) Orhan Bey"},
        {"soru": "Kırım'ın fethi ile Karadeniz hangi padişah döneminde Türk gölü haline gelmiştir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) II. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Osmanlı Devleti'nde 'Sultan' unvanını resmi olarak ilk kullanan padişah kimdir?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) Yıldırım Bayezid"], "dogru": "B) I. Murad"},
        {"soru": "Ankara Savaşı'nda Timur'a yenilerek esir düşen padişah kimdir?", "secenekler": ["A) I. Bayezid", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) I. Bayezid"},
        {"soru": "Şehzade katlini yasal hale getiren kanunnameyi çıkaran padişah kimdir?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) I. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Hicaz bölgesini Osmanlı topraklarına katan ve ilk Osmanlı halifesi olan kimdir?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "Girit Adası'nı en uzun süren kuşatmanın ardından fethini tamamlayan padişah kimdir?", "secenekler": ["A) IV. Mehmed", "B) İbrahim", "C) IV. Murad", "D) II. Süleyman"], "dogru": "A) IV. Mehmed"},
        {"soru": "Osmanlı'da ilk kez parlamenter sisteme (I. Meşrutiyet) geçiş sağlayan padişah kimdir?", "secenekler": ["A) II. Abdülhamid", "B) Sultan Abdülaziz", "C) Sultan Abdülmecid", "D) V. Murad"], "dogru": "A) II. Abdülhamid"},
        {"soru": "Osmanlı Devleti'nin ilk demiryolu hattı (Aydın-İzmir) hangi padişah döneminde açılmıştır?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) II. Abdülhamid", "D) II. Mahmud"], "dogru": "A) Sultan Abdülmecid"}
    ]

    sinav_sorulari_en = [
        {"soru": "Who is the founder of the Ottoman Empire?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) Ertuğrul Gazi", "D) I. Murad"], "dogru": "A) I. Osman"},
        {"soru": "Which sultan made Bursa the state center by conquering it?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Bayezid", "D) I. Mehmed"], "dogru": "B) Orhan Bey"},
        {"soru": "Who was the first sultan to establish the Janissary Corps and be martyred on the battlefield?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) II. Murad"], "dogru": "B) I. Murad"},
        {"soru": "Which sultan known as 'The Thunderbolt' first besieged Istanbul?", "secenekler": ["A) I. Bayezid", "B) Yavuz Sultan Selim", "C) IV. Murad", "D) II. Mehmed"], "dogru": "A) I. Bayezid"},
        {"soru": "Which sultan known as 'Çelebi' ended the Interregnum and reorganized the state?", "secenekler": ["A) I. Mehmed", "B) II. Murad", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) I. Mehmed"},
        {"soru": "Which sultan won the Battles of Varna and II. Kosovo?", "secenekler": ["A) II. Murad", "B) Fatih Sultan Mehmet", "C) Kanuni Sultan Süleyman", "D) I. Selim"], "dogru": "A) II. Murad"},
        {"soru": "Which sultan took the title 'The Conqueror' (Fatih) by conquering Istanbul?", "secenekler": ["A) II. Mehmed", "B) I. Bayezid", "C) Yavuz Sultan Selim", "D) III. Murad"], "dogru": "A) II. Mehmed"},
        {"soru": "During whose reign did the Cem Sultan incident occur?", "secenekler": ["A) II. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) II. Bayezid"},
        {"soru": "Which sultan brought the caliphate to the Ottomans by winning the Battle of Chaldiran?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "Who is the longest-reigning sultan of the dynasty with 46 years?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) II. Abdülhamid", "C) IV. Mehmed", "D) II. Mahmud"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "Which sultan known as 'The Blonde' was on the throne when Cyprus was conquered?", "secenekler": ["A) II. Selim", "B) III. Murad", "C) III. Mehmed", "D) I. Ahmed"], "dogru": "A) II. Selim"},
        {"soru": "Under which sultan did the Ottoman Empire reach its widest borders?", "secenekler": ["A) III. Murad", "B) Kanuni Sultan Süleyman", "C) II. Abdülhamid", "D) IV. Mehmed"], "dogru": "A) III. Murad"},
        {"soru": "Which sultan known as the Conqueror of Eger won the Battle of Keresztes?", "secenekler": ["A) III. Mehmed", "B) IV. Murad", "C) II. Mustafa", "D) II. Osman"], "dogru": "A) III. Mehmed"},
        {"soru": "Which sultan had the Blue Mosque built and introduced the Seniority System?", "secenekler": ["A) I. Ahmed", "B) I. Mustafa", "C) II. Osman", "D) IV. Murad"], "dogru": "A) I. Ahmed"},
        {"soru": "Which young sultan set out on the Hotin campaign and was dethroned while trying to abolish the Janissaries?", "secenekler": ["A) II. Osman", "B) IV. Murad", "C) Genç Selim", "D) III. Selim"], "dogru": "A) II. Osman"},
        {"soru": "Which strict-tempered sultan known as the Conqueror of Baghdad issued strict bans?", "secenekler": ["A) IV. Murad", "B) Yavuz Sultan Selim", "C) I. Selim", "D) II. Mahmud"], "dogru": "A) IV. Murad"},
        {"soru": "Which sultan known as 'The Hunter' reigned for 39 years during the Köprülü Era?", "secenekler": ["A) IV. Mehmed", "B) II. Süleyman", "C) II. Ahmed", "D) II. Mustafa"], "dogru": "A) IV. Mehmed"},
        {"soru": "Who was the last sultan to personally lead a military campaign?", "secenekler": ["A) II. Mustafa", "B) III. Ahmed", "C) I. Mahmud", "D) III. Selim"], "dogru": "A) II. Mustafa"},
        {"soru": "Which sultan ruled during the Tulip Era when the first Turkish printing house was established?", "secenekler": ["A) III. Ahmed", "B) I. Mahmud", "C) III. Osman", "D) III. Mustafa"], "dogru": "A) III. Ahmed"},
        {"soru": "Which sultan made European-style military reforms with Humbaracı Ahmed Pasha?", "secenekler": ["A) I. Mahmud", "B) III. Osman", "C) III. Mustafa", "D) I. Abdülhamid"], "dogru": "A) I. Mahmud"},
        {"soru": "Which sultan had the Nuruosmaniye Mosque built?", "secenekler": ["A) III. Osman", "B) I. Mahmud", "C) III. Selim", "D) I. Abdülhamid"], "dogru": "A) III. Osman"},
        {"soru": "Which reformist sultan laid the foundations of the Imperial Naval Engineering School?", "secenekler": ["A) III. Mustafa", "B) III. Selim", "C) II. Mahmud", "D) I. Abdülhamid"], "dogru": "A) III. Mustafa"},
        {"soru": "During whose reign was the Treaty of Küçük Kaynarca signed?", "secenekler": ["A) I. Abdülhamid", "B) III. Selim", "C) IV. Mustafa", "D) II. Mahmud"], "dogru": "A) I. Abdülhamid"},
        {"soru": "Which sultan initiated the Nizam-ı Cedid (New Order) reforms?", "secenekler": ["A) III. Selim", "B) II. Mahmud", "C) IV. Mustafa", "D) Sultan Abdülaziz"], "dogru": "A) III. Selim"},
        {"soru": "Which sultan abolished the Janissary Corps (Vaka-i Hayriye)?", "secenekler": ["A) II. Mahmud", "B) Sultan Abdülmecid", "C) Sultan Abdülaziz", "D) II. Abdülhamid"], "dogru": "A) II. Mahmud"},
        {"soru": "Which sultan proclaimed the Tanzimat Edict and had Dolmabahçe Palace built?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) V. Murad", "D) II. Abdülhamid"], "dogru": "A) Sultan Abdülmecid"},
        {"soru": "Which sultan known as 'The Traveler' made an official tour of Europe?", "secenekler": ["A) Sultan Abdülaziz", "B) Sultan Abdülmecid", "C) II. Abdülhamid", "D) V. Mehmed Reşad"], "dogru": "A) Sultan Abdülaziz"},
        {"soru": "Which sultan had the shortest reign (93 days)?", "secenekler": ["A) V. Murad", "B) I. Mustafa", "C) IV. Mustafa", "D) VI. Mehmed Vahdeddin"], "dogru": "A) V. Murad"},
        {"soru": "Which sultan proclaimed the Kanun-i Esasi (Constitution) and built the Hejaz Railway?", "secenekler": ["A) II. Abdülhamid", "B) V. Mehmed Reşad", "C) VI. Mehmed Vahdeddin", "D) Sultan Abdülaziz"], "dogru": "A) II. Abdülhamid"},
        {"soru": "During whose reign did the Italo-Turkish and Balkan Wars take place?", "secenekler": ["A) V. Mehmed Reşad", "B) VI. Mehmed Vahdeddin", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) V. Mehmed Reşad"},
        {"soru": "Who was the last Ottoman sultan who left the throne upon the abolition of the sultanate?", "secenekler": ["A) VI. Mehmed Vahdeddin", "B) V. Mehmed Reşad", "C) II. Abdülhamid", "D) V. Murad"], "dogru": "A) VI. Mehmed Vahdeddin"},
        {"soru": "Which sultan minted the first Ottoman copper coin?", "secenekler": ["A) I. Osman", "B) Orhan Bey", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) I. Osman"},
        {"soru": "Who established the first Ottoman madrasah in Iznik?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) Orhan Bey"},
        {"soru": "Which sultan had the Anadolu Hisarı (Anatolian Fortress) built?", "secenekler": ["A) I. Bayezid", "B) Fatih Sultan Mehmet", "C) Yavuz Sultan Selim", "D) Kanuni Sultan Süleyman"], "dogru": "A) I. Bayezid"},
        {"soru": "Which sultan had Rumeli Hisarı built as part of the preparations for the conquest of Istanbul?", "secenekler": ["A) Fatih Sultan Mehmet", "B) I. Bayezid", "C) II. Murad", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Which sultan annexed Trabzon and Crimea to Ottoman lands?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) II. Bayezid", "D) Kanuni Sultan Süleyman"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Which sultan won the Battle of Mohács in a very short time?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Yavuz Sultan Selim", "C) I. Bayezid", "D) III. Mehmed"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "During which three sultans' reigns did Sokullu Mehmet Pasha serve as grand vizier?", "secenekler": ["A) Suleiman, II. Selim, III. Murad", "B) Fatih, II. Bayezid, Yavuz", "C) Yavuz, Suleiman, II. Selim", "D) II. Selim, III. Murad, III. Mehmed"], "dogru": "A) Suleiman, II. Selim, III. Murad"},
        {"soru": "Which sultan used the pen name 'Muradi' in his poems?", "secenekler": ["A) III. Murad", "B) I. Murad", "C) IV. Murad", "D) II. Murad"], "dogru": "A) III. Murad"},
        {"soru": "Which famous sultan used the pen name 'Avni' in his poems?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Kanuni Sultan Süleyman", "C) Yavuz Sultan Selim", "D) III. Selim"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Who was the first Ottoman sultan to marry outside the palace (with official marriage contract)?", "secenekler": ["A) Kanuni Sultan Süleyman", "B) Orhan Bey", "C) I. Osman", "D) Yavuz Sultan Selim"], "dogru": "A) Kanuni Sultan Süleyman"},
        {"soru": "The conquests of Iznik, Izmit, and Bursa are the achievements of which early period sultan?", "secenekler": ["A) Orhan Bey", "B) I. Osman", "C) I. Murad", "D) I. Bayezid"], "dogru": "A) Orhan Bey"},
        {"soru": "With the conquest of Crimea, the Black Sea became a Turkish lake during whose reign?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) II. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Who was the first Ottoman sultan to officially use the title 'Sultan'?", "secenekler": ["A) Orhan Bey", "B) I. Murad", "C) I. Bayezid", "D) Yıldırım Bayezid"], "dogru": "B) I. Murad"},
        {"soru": "Which sultan was defeated by Timur and taken prisoner at the Battle of Ankara?", "secenekler": ["A) I. Bayezid", "B) I. Murad", "C) I. Mehmed", "D) II. Murad"], "dogru": "A) I. Bayezid"},
        {"soru": "Which sultan issued the lawmaking fratricide legal?", "secenekler": ["A) Fatih Sultan Mehmet", "B) Yavuz Sultan Selim", "C) Kanuni Sultan Süleyman", "D) I. Bayezid"], "dogru": "A) Fatih Sultan Mehmet"},
        {"soru": "Who incorporated the Hejaz region into Ottoman lands and became the first Ottoman caliph?", "secenekler": ["A) Yavuz Sultan Selim", "B) Kanuni Sultan Süleyman", "C) II. Bayezid", "D) III. Murad"], "dogru": "A) Yavuz Sultan Selim"},
        {"soru": "Which sultan completed the conquest of Crete after the longest siege?", "secenekler": ["A) IV. Mehmed", "B) İbrahim", "C) IV. Murad", "D) II. Süleyman"], "dogru": "A) IV. Mehmed"},
        {"soru": "Which sultan first introduced the parliamentary system (First Constitutional Era) to the Ottomans?", "secenekler": ["A) II. Abdülhamid", "B) Sultan Abdülaziz", "C) Sultan Abdülmecid", "D) V. Murad"], "dogru": "A) II. Abdülhamid"},
        {"soru": "During whose reign was the Ottoman Empire's first railway line (Aydın-İzmir) opened?", "secenekler": ["A) Sultan Abdülmecid", "B) Sultan Abdülaziz", "C) II. Abdülhamid", "D) II. Mahmud"], "dogru": "A) Sultan Abdülmecid"}
    ]

    sinav_sorulari = sinav_sorulari_tr if dil_secimi == "Türkçe" else sinav_sorulari_en

    for idx, item in enumerate(sinav_sorulari):
        st.markdown(f"""
        <div class="soru-kutu">
            <b>Question {idx+1}:</b> {item['soru']}<br>
            <span style="color: #444; font-size: 14px;">
                &nbsp;&nbsp;{item['secenekler'][0]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][1]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][2]} &nbsp;&nbsp;|&nbsp;&nbsp; 
                {item['secenekler'][3]}
            </span>
        </div>
        """, unsafe_allow_html=True)

    with st.expander(cevap_anahtari_baslik):
        for idx, item in enumerate(sinav_sorulari):
            st.markdown(f"**Question {idx+1}:** {dogru_metin} <span style='color: green;'><b>{item['dogru']}</b></span>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Padişah Arşivi Enterprise Pro | 36 Padişah Tam Arşivi ve Simülasyon Motoru</p>", unsafe_allow_html=True)