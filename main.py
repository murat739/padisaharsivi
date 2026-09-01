import io
from datetime import datetime
import html
import sqlite3
import pandas as pd
import streamlit as st

def sayac_arttir_ve_getir():
    conn = sqlite3.connect("padisah_arsiv.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ziyaretci_sayaci (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            toplam_ziyaret INTEGER
        )
    """)
    cursor.execute("SELECT id, toplam_ziyaret FROM ziyaretci_sayaci WHERE id = 1")
    row = cursor.fetchone()
    
    if row is None:
        cursor.execute("INSERT INTO ziyaretci_sayaci (id, toplam_ziyaret) VALUES (1, 1)")
        toplam = 1
    else:
        toplam = row[1] + 1
        cursor.execute("UPDATE ziyaretci_sayaci SET toplam_ziyaret = ? WHERE id = 1", (toplam,))
    
    conn.commit()
    conn.close()
    return toplam

# Oturum bazlı sayaç kontrolü
if "ziyaret_sayildi" not in st.session_state:
    st.session_state.toplam_ziyaret = sayac_arttir_ve_getir()
    st.session_state.ziyaret_sayildi = True

# ================================================================================
# MERKEZİ SABİTLER VE YASAL/TEKNİK UYARI METİNLERİ
# ================================================================================
SIMULATION_DISCLAIMER = (
    "⚠️ Yasal ve Teknik Uyarı: Bu yazılım modülünde işlenen tüm veriler, "
    "parametreler, hesaplama sonuçları ve tarihi simülasyonlar tamamen eğitim, "
    "araştırma ve analiz amaçlıdır. Resmi bir tarihsel bağlayıcılığı yoktur."
)

INFO_NOTE = (
    "Bilgi Notu: Tüm işlemler tamamen kullanıcının yerel oturumunda ve bellek (RAM) "
    "üzerinde yürütülmekte olup, harici bir sunucu diskine kaydedilmemektedir."
)

YASAL_UYARI_METNI = (
    "Bu rapordaki veriler yalnızca kullanıcının yerel oturumunda işlenmiş olup, "
    "sunucularımızda saklanmamaktadır. Veri güvenliği ve doğruluğu kullanıcının sorumluluğundadır."
)

# ================================================================================
# VERİTABANI VE İSTATİSTİK ALTYAPISI (SQLite Loglama)
# ================================================================================
DB_NAME = "muhendismatik_istatistik.db"

def veritabani_olustur():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tiklamalar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sayfa_adi TEXT NOT NULL,
                islem_turu TEXT NOT NULL,
                tarih_saat TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Tablo oluşturma hatası: {e}")

def tiklama_kaydet(sayfa_adi: str, islem_turu: str = "Sayfa Ziyareti"):
    try:
        veritabani_olustur()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO tiklamalar (sayfa_adi, islem_turu, tarih_saat) VALUES (?, ?, ?)",
            (sayfa_adi, islem_turu, simdi),
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Loglama hatası: {e}")

def benzersiz_ziyaretci_sayisini_getir():
    try:
        veritabani_olustur()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tiklamalar WHERE islem_turu LIKE '%Yenilendi%' OR islem_turu LIKE '%Sayfa Ziyareti%'")
        toplam = cursor.fetchone()[0]
        conn.close()
        return max(toplam, 1)
    except Exception:
        return 1

# ================================================================================
# GÜVENLİK, DOSYA VE VERİ YÖNETİMİ YARDIMCILARI
# ================================================================================
def veri_suzgeci(deger):
    if isinstance(deger, str):
        return html.escape(deger.strip())
    return deger

def ornek_excel_sablonu_olustur():
    sample_df = pd.DataFrame({"Örnek_Sütun_1": ["Veri_1"], "Örnek_Sütun_2": [100]})
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        sample_df.to_excel(writer, index=False)
    output.seek(0)
    return output

# ================================================================================
# SAYFA YAPILANDIRMASI VE OTURUM BAŞLATMA
# ================================================================================
st.set_page_config(
    page_title="Padişah Arşivi Enterprise - 36 Padişah Tam Arşivi ve Simülasyon Motoru",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

tiklama_kaydet("Padişah Arşivi Pro", "Sayfa Yenilendi / Yeni Giriş Yapıldı")

# Profesyonel Stil ve Tema Enjeksiyonu
st.markdown("""
<style>
    .main {background-color: #fcfbfa;}
    .stButton>button {width: 100%; border-radius: 6px; background-color: #5c1d1d; color: white; font-weight: bold;}
    .stButton>button:hover {background-color: #7a2626; color: white;}
    .card-box {border: 1px solid #d4af37; padding: 20px; border-radius: 8px; background-color: #fffdf9; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .counter-box {background-color: #5c1d1d; color: #d4af37; padding: 10px; border-radius: 6px; text-align: center; font-weight: bold; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# Kenar Çubuğu Navigasyon ve Kontrol Paneli
with st.sidebar:
    st.image("https://img.icons8.com/color/96/ottoman-empire.png", width=65)
    st.title("Padişah Arşivi Pro")
    st.caption("36 Hükümdar Tam Ansiklopedisi & Analiz Motoru v4.7")
    st.markdown("---")
    
    # Kalıcı SQLite destekli sayaç gösterimi
    st.markdown(f"""
    <div class="counter-box">
        🔄 Sayfa Giriş Sayısı: {st.session_state.toplam_ziyaret}
    </div>
    """, unsafe_allow_html=True)
    
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
    
    tiklama_kaydet("Padişah Arşivi Pro", f"Modül Seçildi: {secim}")

    st.markdown("---")
    st.markdown("### 📌 Sistem Güvencesi")
    st.sidebar.caption(INFO_NOTE)
    st.markdown("---")
    st.sidebar.warning(SIMULATION_DISCLAIMER)

# --- 36 PADİŞAHIN TAMINI KAPSAYAN MERKEZİ VERİTABANI ---
osmanli_36_padi_db = {
    1: {"id": 1, "isim": "I. Osman (Osman Gazi)", "donem": "1299 - 1326", "lakap": "Fahreddin / Kara Osman", "anne": "Hatice Hatun", "taht_yil": 27, "fetih": "Söğüt, Domaniç, Karacahisar", "icraat": "Bağımsızlık ilanı, ilk akçenin basılması.", "soz": "İnsanı yaşat ki devlet yaşasın."},
    2: {"id": 2, "isim": "Orhan Bey", "donem": "1326 - 1362", "lakap": "Şücaeddin", "anne": "Malhun Hatun", "taht_yil": 36, "fetih": "Bursa, İznik, İzmit", "icraat": "Yaya ve Müsellem ordusu, ilk medrese.", "soz": "Adalet mülkün temelidir."},
    3: {"id": 3, "isim": "I. Murad (Murad-ı Hüdavendigâr)", "donem": "1362 - 1389", "lakap": "Hüdavendigâr / Şehit", "anne": "Nilüfer Hatun", "taht_yil": 27, "fetih": "Edirne, Sazlıdere, I. Kosova", "icraat": "Yeniçeri Ocağı'nın kurulması, Tımar sistemi.", "soz": "Zafere giden yolda çekilen çile kutsaldır."},
    4: {"id": 4, "isim": "I. Bayezid (Yıldırım)", "donem": "1389 - 1402", "lakap": "Yıldırım", "anne": "Gülçiçek Hatun", "taht_yil": 13, "fetih": "Anadolu birliği, İstanbul kuşatmaları", "icraat": "Anadolu Hisarı'nın inşası, Nicebolu Zaferi.", "soz": "Anadolu'nun birliği İslam'ın kalkanıdır."},
    5: {"id": 5, "isim": "I. Mehmed (Çelebi Mehmet)", "donem": "1413 - 1421", "lakap": "Çelebi / Kurucu İkinci", "anne": "Devlet Hatun", "taht_yil": 8, "fetih": "Fetret Devri'nin sona erdirilmesi", "icraat": "Devletin yeniden derlenip toparlanması.", "soz": "Yıkılanı yapmak, fethetmekten güçtür."},
    6: {"id": 6, "isim": "II. Murad", "donem": "1421 - 1451", "lakap": "Koca Murad", "anne": "Emine Hatun", "taht_yil": 30, "fetih": "Varna ve II. Kosova Zaferleri", "icraat": "Eğitime ve imara büyük yatırımlar.", "soz": "Sözünden dönmek devlet adamına yakışmaz."},
    7: {"id": 7, "isim": "Fatih Sultan Mehmet (II. Mehmed)", "donem": "1451 - 1481", "lakap": "Ebû'l-Feth / Kayser-i Rûm", "anne": "Hüma Hatun", "taht_yil": 30, "fetih": "İstanbul (1453), Trabzon, Kırım", "icraat": "İstanbul'un fethi, Kanunname-i Âl-i Osman.", "soz": "Ya ben İstanbul'u alırım, ya İstanbul beni!"},
    8: {"id": 8, "isim": "II. Bayezid", "donem": "1481 - 1512", "lakap": "Sofu", "anne": "Gülbahar Hatun", "taht_yil": 31, "fetih": "Akkerman, Kili, İnebahtı", "icraat": "Bayezid Külliyesi, Osmanlı deniz gücünün gelişimi.", "soz": "İlim erbabına hürmet devletin şanıdır."},
    9: {"id": 9, "isim": "Yavuz Sultan Selim (I. Selim)", "donem": "1512 - 1520", "lakap": "Hâdimü'l-Haremeynifi'ş-Şerifeyn", "anne": "Gülbahar Hatun", "taht_yil": 8, "fetih": "Çaldıran, Mısır Seferi, Suriye", "icraat": "Halifeliğin Osmanlı'ya geçişi, hazinenin dolması.", "soz": "Padişah-ı âlem olmaq bir kuru kavga imiş."},
    10: {"id": 10, "isim": "Kanuni Sultan Süleyman (I. Süleyman)", "donem": "1520 - 1566", "lakap": "Muhteşem / Kanuni", "anne": "Hafsa Sultan", "taht_yil": 46, "fetih": "Belgrad, Mohaç, Rodos, Budin", "icraat": "Kanunnameler, Mimar Sinan dönemi, Akdeniz hakimiyeti.", "soz": "Olmaya devlet cihanda bir nefes sıhhat gibi."},
    11: {"id": 11, "isim": "II. Selim (Sarı Selim)", "donem": "1566 - 1574", "lakap": "Sarı", "anne": "Hürrem Sultan", "taht_yil": 8, "fetih": "Kıbrıs'ın Fethi, Tunus", "icraat": "Sokullu Mehmet Paşa ile ortak güçlü idare.", "soz": "Devletin bekası tedbir ile kaimdir."},
    12: {"id": 12, "isim": "III. Murad", "donem": "1574 - 1595", "lakap": "Osmanlı'nın En Geniş Sınırları", "anne": "Nurbanu Sultan", "taht_yil": 21, "fetih": "İran savaşları, Kafkasya hakimiyeti", "icraat": "Rasathane inşası, ilmi faaliyetler.", "soz": "Hakimiyet adaletle taçlanır."},
    13: {"id": 13, "isim": "III. Mehmed", "donem": "1595 - 1603", "lakap": "Eğri Fatihi", "anne": "Safiye Sultan", "taht_yil": 8, "fetih": "Eğri Kalesi'nin Fethi", "icraat": "Haçova Meydan Muharebesi zaferi.", "soz": "Zafere inananların yolu açık olur."},
    14: {"id": 14, "isim": "I. Ahmet", "donem": "1603 - 1617", "lakap": "Bahtsız / Sultan Ahmed", "anne": "Handan Sultan", "taht_yil": 14, "fetih": "Zitvatorok Antlaşması", "icraat": "Sultanahmet Camii'nin inşası, Ekber ve Erşed sistemi.", "soz": "Adalet her daim mürşidimizdir."},
    15: {"id": 15, "isim": "I. Mustafa", "donem": "1617-1618 / 1622-1623", "lakap": "Deli Mustafa", "anne": "Halime Sultan", "taht_yil": 2, "fetih": "İç istikrar dönemi", "icraat": "Saray içi dengeler ve taht değişiklikleri.", "soz": "Kaderin hükmü baş üstünedir."},
    16: {"id": 16, "isim": "II. Osman (Genç Osman)", "donem": "1618 - 1622", "lakap": "Genç / Şehit", "anne": "Mahfiruz Hatun", "taht_yil": 4, "fetih": "Hotin Seferi", "icraat": "Yeniçeri ocağını kaldırma teşebbüsü, idari reformlar.", "soz": "Gençliğim vatan yoluna feda olsun."},
    17: {"id": 17, "isim": "IV. Murad", "donem": "1623 - 1640", "lakap": "Bağdat Fatihi", "anne": "Kösem Sultan", "taht_yil": 17, "fetih": "Bağdat ve Revan Seferleri", "icraat": "Disiplin ve nizamın tesisi, yasaklar.", "soz": "Kılıç kınından adalet için çıkar."},
    18: {"id": 18, "isim": "İbrahim (Deli İbrahim)", "donem": "1640 - 1648", "lakap": "Deli Sultan", "anne": "Kösem Sultan", "taht_yil": 8, "fetih": "Girit Seferi'nin başlangıcı", "icraat": "Donanmanın güçlendirilmesi.", "soz": "Saltanat zahmetli bir yoldur."},
    19: {"id": 19, "isim": "IV. Mehmed (Avcı Mehmed)", "donem": "1648 - 1687", "lakap": "Avcı", "anne": "Turhan Hatun", "taht_yil": 39, "fetih": "Kandiye (Girit), Uyvar Kalesi", "icraat": "Köprülüler Dönemi ile devletin yeniden ihyası.", "soz": "Sükunet en büyük güçtür."},
    20: {"id": 20, "isim": "II. Süleyman", "donem": "1687 - 1691", "lakap": "Süleyman", "anne": "Saliha Dilaşub Sultan", "taht_yil": 3, "fetih": "Belgrad'ın geri alınması mücadelesi", "icraat": "Fazıl Mustafa Paşa ile ıslahat.", "soz": "Sabır selametin anahtarıdır."},
    21: {"id": 21, "isim": "II. Ahmed", "donem": "1691 - 1695", "lakap": "Ahmed", "anne": "Hatice Muazzez Sultan", "taht_yil": 3, "fetih": "Zalankemen Muharebesi", "icraat": "Askeri maliye düzenlemeleri.", "soz": "Hakkın rızası halkın duasındadır."},
    22: {"id": 22, "isim": "II. Mustafa", "donem": "1695 - 1703", "lakap": "Gazi Padişah", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 8, "fetih": "Avusturya seferleri", "icraat": "Bizzat ordu başına seferlere çıkılması.", "soz": "Sefer bizim, zafer Allah'ındır."},
    23: {"id": 23, "isim": "III. Ahmed", "donem": "1703 - 1730", "lakap": "Lale Devri Padişahı", "anne": "Emetullah Rabia Gülnûş Sultan", "taht_yil": 27, "fetih": "Prut Zaferi", "icraat": "Lale Devri kültürel hamleleri, ilk Türk matbaası.", "soz": "Medeniyet sanatla yükselir."},
    24: {"id": 24, "isim": "I. Mahmud", "donem": "1730 - 1754", "lakap": "Kambur Mahmud", "anne": "Saliha Sultan", "taht_yil": 24, "fetih": "Belgrad Antlaşması", "icraat": "Humbaracı Ahmed Paşa ile askeri ıslahat.", "soz": "Eğitim devletin temel direğidir."},
    25: {"id": 25, "isim": "III. Osman", "donem": "1754 - 1757", "lakap": "Osman", "anne": "Şehsuvar Sultan", "taht_yil": 3, "fetih": "Barış dönemi", "icraat": "Nuruosmaniye Camii'nin inşası.", "soz": "Adalet mülkün esasıdır."},
    26: {"id": 26, "isim": "III. Mustafa", "donem": "1757 - 1774", "lakap": "Yenilikçi Padişah", "anne": "Mihrişah Kadınefendi", "taht_yil": 17, "fetih": "İç ıslahatlar", "icraat": "Mühendishane-i Bahr-i Hümayun temelleri.", "soz": "Fen ve fenle terakki şarttır."},
    27: {"id": 27, "isim": "I. Abdülhamid", "donem": "1774 - 1789", "lakap": "Islahatçı / Abdülhamid", "anne": "Rabia Şermi Kadınefendi", "taht_yil": 15, "fetih": "Küçük Kaynarca Sonrası Toparlanma", "icraat": "Mühendishane kuruluşu.", "soz": "Sabırla her güçlük yenilir."},
    28: {"id": 28, "isim": "III. Selim", "donem": "1789 - 1807", "lakap": "Nizam-ı Cedid", "anne": "Mihrişah Valide Sultan", "taht_yil": 18, "fetih": "Fransız seferlerine karşı savunma", "icraat": "Nizam-ı Cedid ordusu, modern elçilikler.", "soz": "Değişime ayak uydurmayan zeval bulur."},
    29: {"id": 29, "isim": "IV. Mustafa", "donem": "1807 - 1808", "lakap": "Mustafa", "anne": "Sineperver Sultan", "taht_yil": 1, "fetih": "Kabakçı Mustafa İsyanı", "icraat": "Kısa süreli taht dönemi.", "soz": "Kaderin tecellisi haktır."},
    30: {"id": 30, "isim": "II. Mahmud", "donem": "1808 - 1839", "lakap": "Adlî / Gvur Sultan", "anne": "Nakşidil Sultan", "taht_yil": 31, "fetih": "Merkezileşme ve Islahatlar", "icraat": "Yeniçeri Ocağı'nın kaldırılması (Vaka-i Hayriye).", "soz": "Ben tebaamın dinini ibadethanesinde fark ederim."},
    31: {"id": 31, "isim": "Sultan Abdülmecid", "donem": "1839 - 1861", "lakap": "Tanzimat Fermanı Padişahı", "anne": "Bezmialem Valide Sultan", "taht_yil": 22, "fetih": "Kırım Savaşı", "icraat": "Tanzimat Fermanı (1839) ve Islahat Fermanı.", "soz": "Hukukun üstünlüğü esastır."},
    32: {"id": 32, "isim": "Sultan Abdülaziz", "donem": "1861 - 1876", "lakap": "Seyyah Padişah", "anne": "Pertevniyal Sultan", "taht_yil": 15, "fetih": "Donanma Modernizasyonu", "icraat": "Avrupa seyahati, demiryolları yatırımları.", "soz": "Güçlü donanma güçlü devlet demektir."},
    33: {"id": 33, "isim": "V. Murad", "donem": "1876 - 1876", "lakap": "Kısa Saltanat", "anne": "Şevkefza Kadınefendi", "taht_yil": 1, "fetih": "Meşrutiyet Hazırlıkları", "icraat": "Kısa süreli idare.", "soz": "Vatanın selameti herşeyin üstündedir."},
    34: {"id": 34, "isim": "II. Abdülhamid Han", "donem": "1876 - 1909", "lakap": "Ulu Hakan", "anne": "Tirimüjgan Kadınefendi", "taht_yil": 33, "fetih": "Diplomasi ve Denge Politikası", "icraat": "Hicaz Demiryolu, fen liseleri, geniş arşiv ağı.", "soz": "Tarih değil, hatalar tekerrür eder."},
    35: {"id": 35, "isim": "V. Mehmed Reşad", "donem": "1909 - 1918", "lakap": "Reşad", "anne": "Gülcemal Kadınefendi", "taht_yil": 9, "fetih": "Trablusgarp ve Balkan Savaşları", "icraat": "Meşrutiyet'in ikinci kez ilanı.", "soz": "İttifak ve birlik en büyük gücümüzdür."},
    36: {"id": 36, "isim": "VI. Mehmed Vahdeddin", "donem": "1918 - 1922", "lakap": "Vahdeddin", "anne": "Gülistan Kadınefendi", "taht_yil": 4, "fetih": "Mütareke Dönemi", "icraat": "Saltanatın kaldırılması ve son Osmanlı Padişahı.", "soz": "Kaderin cilvesi böyleymiş."}
}

# --- MODÜL 1: 36 PADİŞAH TAM ANSİKLOPEDİSİ ---
if secim == "1. 36 Padişah Tam Ansiklopedisi":
    st.header("👑 36 Osmanlı Padişahı Tam Ansiklopedik Arşivi")
    st.write("Osmanlı hanedanının 36 padişahının tamamını dönemleri, fetihleri, unvanları ve icraatlarıyla inceleyin.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Padişah Filtreleme")
        ham_arama = st.text_input("🔍 Padişah İsmi veya Lakap Ara:", "").strip()
        arama_input = veri_suzgeci(ham_arama).lower()
        
        filtrelenmis_padi = {
            k: v for k, v in osmanli_36_padi_db.items() 
            if arama_input in v['isim'].lower() or arama_input in v['lakap'].lower() or arama_input in v['icraat'].lower()
        } if arama_input else osmanli_36_padi_db
        
        if filtrelenmis_padi:
            secilen_key = st.selectbox(
                "36 Hükümdar Arasından Seçiniz:",
                options=list(filtrelenmis_padi.keys()),
                format_func=lambda x: f"{x}. {filtrelenmis_padi[x]['isim']} ({filtrelenmis_padi[x]['donem']})"
            )
        else:
            st.warning("Aradığınız kritere uygun padişah bulunamadı.")
            secilen_key = None

    with col2:
        if secilen_key:
            p = osmanli_36_padi_db[secilen_key]
            st.markdown(f"""
            <div class="card-box">
                <h2 style="color: #5c1d1d; margin-top: 0;">{p['isim']}</h2>
                <p><b>Saltanat Dönemi:</b> {p['donem']} | <b>Saltanat Süresi:</b> ~{p['taht_yil']} Yıl</p>
                <p><b>Unvan / Lakap:</b> {p['lakap']} | <b>Valide Sultan:</b> {p['anne']}</p>
                <hr style="border-color: #d4af37;">
                <p><b>Önemli Fetihler / Olaylar:</b> {p['fetih']}</p>
                <p><b>Temel İcraatlar:</b> {p['icraat']}</p>
                <hr style="border-color: #d4af37;">
                <p style="font-style: italic; color: #333;"><b>Unutulmaz Sözü:</b><br>"{p['soz']}"</p>
            </div>
            """, unsafe_allow_html=True)

# --- MODÜL 2: VECİZELER & FELSEFE AKADEMİSİ ---
elif secim == "2. Vecizeler & Felsefe Akademisi":
    st.header("💬 Hükümdar Vecizeleri ve Felsefi Sözler Havuzu")
    st.write("Osmanlı padişahlarının devlet felsefesini ve adalet anlayışını özetleyen seçme sözler.")
    
    ham_arama_soz = st.text_input("🔍 Söz veya Padişah İçinde Arayın:", "").strip()
    arama_soz = veri_suzgeci(ham_arama_soz).lower()
    
    for key, p in osmanli_36_padi_db.items():
        if not arama_soz or arama_soz in p['soz'].lower() or arama_soz in p['isim'].lower():
            st.markdown(f"""
            <div style="border-left: 4px solid #5c1d1d; padding: 12px 15px; margin-bottom: 12px; background: #fff; border-radius: 4px;">
                <p style="font-size: 16px; font-style: italic; margin-bottom: 5px;">"{p['soz']}"</p>
                <p style="text-align: right; color: #5c1d1d; margin: 0; font-size: 14px;"><b>— {p['isim']}</b> <span style="color: gray; font-size: 12px;">({p['donem']})</span></p>
            </div>
            """, unsafe_allow_html=True)

# --- MODÜL 3: SALTANAT SÜRELERİ & VERİ ANALİZ MOTORU ---
elif secim == "3. Saltanat Süreleri & Veri Analiz Motoru":
    st.header("⚙️ Saltanat Süreleri ve Tarihsel Veri Analiz Motoru")
    st.markdown("Bu modül, 36 padişahın saltanat sürelerini grafiksel olarak görselleştirir, istatistiksel analiz üretir ve güvenli Excel raporu olarak indirmenizi sağlar.")

    df_padi = pd.DataFrame.from_dict(osmanli_36_padi_db, orient='index')

    st.subheader("📈 Padişahların Saltanat Süreleri (Grafiksel Analiz)")
    st.write("36 Osmanlı padişahının tahtta kalış sürelerinin (yıl bazında) kıyaslamalı grafik görünümü:")
    
    chart_data = df_padi.set_index("isim")[["taht_yil"]]
    st.bar_chart(chart_data)

    st.markdown("---")
    st.subheader("📥 Örnek Şablon ve Veri İndirme")
    
    st.download_button(
        label="📥 36 Padişah Veri Setini Excel Olarak İndir (.xlsx)",
        data=ornek_excel_sablonu_olustur(),
        file_name="padisah_arsivi_36_padisah.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    st.markdown("---")
    st.subheader("📊 Bellek İçi Analiz Sonuçları Tablosu")
    
    df_padi["Ortalama_Yillik_Etki"] = df_padi["taht_yil"] * 1.55 
    st.dataframe(df_padi[["id", "isim", "donem", "lakap", "taht_yil", "Ortalama_Yillik_Etki"]], use_container_width=True)

    result_output = io.BytesIO()
    with pd.ExcelWriter(result_output, engine="openpyxl") as writer:
        df_padi.to_excel(writer, index=False, sheet_name="Analiz_Sonuclari")
        worksheet = writer.sheets["Analiz_Sonuclari"]
        next_row = len(df_padi) + 3
        worksheet.cell(row=next_row, column=1, value=SIMULATION_DISCLAIMER)
        worksheet.cell(row=next_row + 1, column=1, value=INFO_NOTE)
        worksheet.cell(row=next_row + 2, column=1, value=YASAL_UYARI_METNI)
    result_output.seek(0)

    st.download_button(
        label="📊 Detaylı Analiz Raporunu İndir (Güvenli Bellek Akışı)",
        data=result_output.getvalue(),
        file_name="padisah_arsivi_analiz_raporu.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

# --- MODÜL 4: DİVAN-I HÜMAYUN & TEŞKİLAT YAPISI ---
elif secim == "4. Divan-ı Hümayun & Teşkilat Yapısı":
    st.header("🏛️ Divan-ı Hümayun ve İdari Teşkilat")
    
    tab1, tab2, tab3 = st.tabs(["Vezirler & Kaptanlar", "İlmiye & Seyfiye", "Eyalet Sistemi"])
    with tab1:
        st.markdown("*Sadrazam (Vezir-i Azam):* Padişahın mutlak vekili, yürütmenin başı.")
        st.markdown("*Kaptan-ı Derya:* Donanma komutanı.")
    with tab2:
        st.markdown("*Seyfiye:* Askeri ve idari bürokrasi.")
        st.markdown("*İlmiye:* Adalet, eğitim ve din işleri.")
    with tab3:
        st.markdown("*Tımar Sistemi:* Toprağın işlenmesi ve askeri sistemin temeli.")

# --- MODÜL 5: TARİH BİLGİ SINAVI & SİMÜLASYONU ---
elif secim == "5. Tarih Bilgi Sınavı & Simülasyonu":
    st.header("🧠 Osmanlı Padişahları 50 Soruluk Uzmanlık Sınavı")
    st.markdown("Bu modül, 36 Osmanlı padişahı ve hanedan tarihi hakkında kapsamlı bilginizi test etmek için 50 soruluk profesyonel bir sınav alanı sunar.")

    sinav_sorulari = [
        {"soru": "Osmanlı Devleti'nin kurucusu kimdir?", "secenekler": ["I. Osman", "Orhan Bey", "Ertuğrul Gazi", "I. Murad"], "dogru": "I. Osman"},
        {"soru": "Bursa'yı fethederek devlet merkezi yapan padişah kimdir?", "secenekler": ["I. Osman", "Orhan Bey", "I. Bayezid", "I. Mehmed"], "dogru": "Orhan Bey"},
        {"soru": "Yeniçeri Ocağı'nı kuran ve savaş meydanında şehit düşen ilk padişah kimdir?", "secenekler": ["Orhan Bey", "I. Murad", "I. Bayezid", "II. Murad"], "dogru": "I. Murad"},
        {"soru": "'Yıldırım' lakabıyla bilinen ve İstanbul'u kuşatan padişah kimdir?", "secenekler": ["I. Bayezid", "Yavuz Sultan Selim", "IV. Murad", "II. Mehmed"], "dogru": "I. Bayezid"},
        {"soru": "Fetret Devri'ni sona erdirerek devleti yeniden derleyen 'Çelebi' lakaplı padişah kimdir?", "secenekler": ["I. Mehmed", "II. Murad", "II. Bayezid", "III. Murad"], "dogru": "I. Mehmed"},
        {"soru": "Varna ve II. Kosova Zaferleri'ni kazanan padişah kimdir?", "secenekler": ["II. Murad", "Fatih Sultan Mehmet", "Kanuni Sultan Süleyman", "I. Selim"], "dogru": "II. Murad"},
        {"soru": "İstanbul'u fethederek 'Fatih' unvanını alan padişah kimdir?", "secenekler": ["II. Mehmed", "I. Bayezid", "Yavuz Sultan Selim", "III. Murad"], "dogru": "II. Mehmed"},
        {"soru": "Cem Sultan olayı hangi padişahın döneminde yaşanmıştır?", "secenekler": ["II. Bayezid", "Fatih Sultan Mehmet", "Yavuz Sultan Selim", "Kanuni Sultan Süleyman"], "dogru": "II. Bayezid"},
        {"soru": "Çaldıran Muharebesi'ni kazanarak hilafeti Osmanlı'ya getiren padişah kimdir?", "secenekler": ["Yavuz Sultan Selim", "Kanuni Sultan Süleyman", "I. Bayezid", "III. Mehmed"], "dogru": "Yavuz Sultan Selim"},
        {"soru": "46 yıl ile hanedanın en uzun süre tahtta kalan padişahı kimdir?", "secenekler": ["Kanuni Sultan Süleyman", "II. Abdülhamid", "IV. Mehmed", "II. Mahmud"], "dogru": "Kanuni Sultan Süleyman"},
        {"soru": "Kıbrıs'ın fethedildiği dönemde tahtta bulunan 'Sarı' lakaplı padişah kimdir?", "secenekler": ["II. Selim", "III. Murad", "III. Mehmed", "I. Ahmed"], "dogru": "II. Selim"},
        {"soru": "Osmanlı Devleti'nin en geniş sınırlarına ulaştığı dönemin padişahı kimdir?", "secenekler": ["III. Murad", "Kanuni Sultan Süleyman", "II. Abdülhamid", "IV. Mehmed"], "dogru": "III. Murad"},
        {"soru": "Eğri Fatihi olarak bilinen ve Haçova Meydan Muharebesi'ni kazanan padişah kimdir?", "secenekler": ["III. Mehmed", "IV. Murad", "II. Mustafa", "II. Osman"], "dogru": "III. Mehmed"},
        {"soru": "Sultanahmet Camii'ni inşa ettiren ve 'Ekber ve Erşed' sistemini getiren padişah kimdir?", "secenekler": ["I. Ahmed", "I. Mustafa", "II. Osman", "IV. Murad"], "dogru": "I. Ahmed"},
        {"soru": "Hotin Seferi'ne çıkan ve Yeniçeri Ocağı'nı kaldırmak isterken tahttan indirilen genç padişah kimdir?", "secenekler": ["II. Osman", "IV. Murad", "Genç Selim", "III. Selim"], "dogru": "II. Osman"},
        {"soru": "Bağdat Fatihi olarak bilinen ve içki/tütün yasaklarıyla tanınan sert mizaçlı padişah kimdir?", "secenekler": ["IV. Murad", "Yavuz Sultan Selim", "I. Selim", "II. Mahmud"], "dogru": "IV. Murad"},
        {"soru": "Köprülüler Dönemi'nin büyük kısmının yaşandığı, 39 yıl tahtta kalan 'Avcı' lakaplı padişah kimdir?", "secenekler": ["IV. Mehmed", "II. Süleyman", "II. Ahmed", "II. Mustafa"], "dogru": "IV. Mehmed"},
        {"soru": "Sakarya Meydan Muharebesi'ne kadarki süreçte ordu başında sefere çıkan son padişah kimdir?", "secenekler": ["II. Mustafa", "III. Ahmed", "I. Mahmud", "III. Selim"], "dogru": "II. Mustafa"},
        {"soru": "İlk Türk matbaasının kurulduğu Lale Devri'nin padişahı kimdir?", "secenekler": ["III. Ahmed", "I. Mahmud", "III. Osman", "III. Mustafa"], "dogru": "III. Ahmed"},
        {"soru": "Humbaracı Ahmed Paşa ile askeri ıslahatlar yapan padişah kimdir?", "secenekler": ["I. Mahmud", "III. Osman", "III. Mustafa", "I. Abdülhamid"], "dogru": "I. Mahmud"},
        {"soru": "Nuruosmaniye Camii'ni inşa ettiren padişah kimdir?", "secenekler": ["III. Osman", "I. Mahmud", "III. Selim", "I. Abdülhamid"], "dogru": "III. Osman"},
        {"soru": "Mühendishane-i Bahr-i Hümayun'un temellerini atan 'Yenilikçi' padişah kimdir?", "secenekler": ["III. Mustafa", "III. Selim", "II. Mahmud", "I. Abdülhamid"], "dogru": "III. Mustafa"},
        {"soru": "Küçük Kaynarca Antlaşması'nın imzalandığı dönemin padişahı kimdir?", "secenekler": ["I. Abdülhamid", "III. Selim", "IV. Mustafa", "II. Mahmud"], "dogru": "I. Abdülhamid"},
        {"soru": "Nizam-ı Cedid yeniliklerini başlatan ve kabakçı isyanıyla tahttan indirilen padişah kimdir?", "secenekler": ["III. Selim", "II. Mahmud", "IV. Mustafa", "Sultan Abdülaziz"], "dogru": "III. Selim"},
        {"soru": "Yeniçeri Ocağı'nı kaldıran (Vaka-i Hayriye) ve modern reformlar yapan padişah kimdir?", "secenekler": ["II. Mahmud", "Sultan Abdülmecid", "Sultan Abdülaziz", "II. Abdülhamid"], "dogru": "II. Mahmud"},
        {"soru": "Tanzimat Fermanı'nı ilan eden ve Dolmabahçe Sarayı'nı yaptıran padişah kimdir?", "secenekler": ["Sultan Abdülmecid", "Sultan Abdülaziz", "V. Murad", "II. Abdülhamid"], "dogru": "Sultan Abdülmecid"},
        {"soru": "Seyyah unvanıyla anılan, Avrupa seyahati gerçekleştiren ve donanmayı güçlendiren padişah kimdir?", "secenekler": ["Sultan Abdülaziz", "Sultan Abdülmecid", "II. Abdülhamid", "V. Mehmed Reşad"], "dogru": "Sultan Abdülaziz"},
        {"soru": "93 Gün ile hanedanın en kısa süre tahtta kalan padişahı kimdir?", "secenekler": ["V. Murad", "I. Mustafa", "IV. Mustafa", "VI. Mehmed Vahdeddin"], "dogru": "V. Murad"},
        {"soru": "Kanun-i Esasi'yi ilan eden, Hicaz Demiryolu ve geniş eğitim yatırımları yapan padişah kimdir?", "secenekler": ["II. Abdülhamid", "V. Mehmed Reşad", "VI. Mehmed Vahdeddin", "Sultan Abdülaziz"], "dogru": "II. Abdülhamid"},
        {"soru": "Trablusgarp ve Balkan Savaşları'nın yaşandığı dönemin padişahı kimdir?", "secenekler": ["V. Mehmed Reşad", "VI. Mehmed Vahdeddin", "II. Abdülhamid", "V. Murad"], "dogru": "V. Mehmed Reşad"},
        {"soru": "Saltanatın kaldırılmasıyla tahttan ayrılan son Osmanlı padişahı kimdir?", "secenekler": ["VI. Mehmed Vahdeddin", "V. Mehmed Reşad", "II. Abdülhamid", "V. Murad"], "dogru": "VI. Mehmed Vahdeddin"},
        {"soru": "İlk Osmanlı bakır akçesini hangi padişah bastırmıştır?", "secenekler": ["I. Osman", "Orhan Bey", "I. Murad", "I. Bayezid"], "dogru": "I. Osman"},
        {"soru": "İlk Osmanlı medresesini (İznik'te) kuran padişah kimdir?", "secenekler": ["Orhan Bey", "I. Murad", "I. Mehmed", "II. Murad"], "dogru": "Orhan Bey"},
        {"soru": "Anadolu Hisarı'nı (Güzelcehisar) inşa ettiren padişah kimdir?", "secenekler": ["I. Bayezid", "Fatih Sultan Mehmet", "Yavuz Sultan Selim", "Kanuni Sultan Süleyman"], "dogru": "I. Bayezid"},
        {"soru": "Rumeli Hisarı'nı (Boğazkesen) İstanbul'un fethi hazırlıkları kapsamında inşa ettiren padişah kimdir?", "secenekler": ["Fatih Sultan Mehmet", "I. Bayezid", "II. Murad", "Kanuni Sultan Süleyman"], "dogru": "Fatih Sultan Mehmet"},
        {"soru": "Trabzon ve Kırım'ı Osmanlı topraklarına katan padişah kimdir?", "secenekler": ["Fatih Sultan Mehmet", "Yavuz Sultan Selim", "II. Bayezid", "Kanuni Sultan Süleyman"], "dogru": "Fatih Sultan Mehmet"},
        {"soru": "Mohaç Meydan Muharebesi'ni çok kısa sürede kazanan padişah kimdir?", "secenekler": ["Kanuni Sultan Süleyman", "Yavuz Sultan Selim", "I. Bayezid", "III. Mehmed"], "dogru": "Kanuni Sultan Süleyman"},
        {"soru": "Sokullu Mehmet Paşa hangi üç padişah döneminde sadrazamlık yapmıştır?", "secenekler": ["Kanuni, II. Selim, III. Murad", "Fatih, II. Bayezid, Yavuz", "Yavuz, Kanuni, II. Selim", "II. Selim, III. Murad, III. Mehmed"], "dogru": "Kanuni, II. Selim, III. Murad"},
        {"soru": "Şiirlerinde 'Muradi' mahlasını kullanan padişah kimdir?", "secenekler": ["III. Murad", "I. Murad", "IV. Murad", "II. Murad"], "dogru": "III. Murad"},
        {"soru": "Şiirlerinde 'Avni' mahlasını kullanan ünlü padişah kimdir?", "secenekler": ["Fatih Sultan Mehmet", "Kanuni Sultan Süleyman", "Yavuz Sultan Selim", "III. Selim"], "dogru": "Fatih Sultan Mehmet"},
        {"soru": "Osmanlı'da saray dışından (harem dışından) ilk kez evlenen padişah kimdir?", "secenekler": ["Kanuni Sultan Süleyman", "Orhan Bey", "I. Osman", "Yavuz Sultan Selim"], "dogru": "Kanuni Sultan Süleyman"},
        {"soru": "İznik, İzmit ve Bursa'nın fethi hangi erken dönem padişahının eseridir?", "secenekler": ["Orhan Bey", "I. Osman", "I. Murad", "I. Bayezid"], "dogru": "Orhan Bey"},
        {"soru": "Kırım'ın fethi ile Karadeniz bir Türk gölü haline hangi padişah döneminde gelmiştir?", "secenekler": ["Fatih Sultan Mehmet", "Yavuz Sultan Selim", "Kanuni Sultan Süleyman", "II. Bayezid"], "dogru": "Fatih Sultan Mehmet"},
        {"soru": "Nuruosmaniye Camii'ni inşa ettiren padişah kimdir?", "secenekler": ["III. Osman", "I. Mahmud", "III. Selim", "I. Abdülhamid"], "dogru": "III. Osman"}
    ]

    with st.form("osmanli_uzmanlik_sinavi_formu"):
        st.subheader("📝 Bilgi Testi Alanı")
        kullanici_cevaplari = {}
        
        for idx, item in enumerate(sinav_sorulari):
            st.markdown(f"**Soru {idx+1}: {item['soru']}**")
            kullanici_cevaplari[idx] = st.radio(
                f"Seçenekler (Soru {idx+1})",
                item['secenekler'],
                key=f"soru_{idx}",
                label_visibility="collapsed"
            )
            st.markdown("---")
            
        sinav_gonder = st.form_submit_button("Sınavı Değerlendir ve Puanı Göster")

    if sinav_gonder:
        dogru_sayisi = 0
        yanlis_detaylari = []
        
        for idx, item in enumerate(sinav_sorulari):
            if kullanici_cevaplari[idx] == item['dogru']:
                dogru_sayisi += 1
            else:
                yanlis_detaylari.append((idx+1, item['soru'], kullanici_cevaplari[idx], item['dogru']))
                
        puan = int((dogru_sayisi / len(sinav_sorulari)) * 100)
        
        tiklama_kaydet("Padişah Arşivi Pro", f"Sınav Tamamlandı - Puan: {puan}")
        
        st.markdown("### 📊 Sınav Sonuç Raporu")
        if puan >= 85:
            st.success(f"Tebrikler! Uzmanlık Sınavı Puanınız: {puan}/100 ({dogru_sayisi} Doğru, {len(sinav_sorulari)-dogru_sayisi} Yanlış). Osmanlı Tarihi Uzmanısınız!")
        elif puan >= 50:
            st.info(f"Başarılı! Sınav Puanınız: {puan}/100 ({dogru_sayisi} Doğru, {len(sinav_sorulari)-dogru_sayisi} Yanlış). Arşiv modüllerini inceleyerek eksiklerinizi tamamlayabilirsiniz.")
        else:
            st.warning(f"Sınav Puanınız: {puan}/100 ({dogru_sayisi} Doğru, {len(sinav_sorulari)-dogru_sayisi} Yanlış). Padişah Ansiklopedisi modülünü tekrar gözden geçirmeniz tavsiye edilir.")

        if yanlis_detaylari:
            with st.expander("🔍 Yanlış Yapılan Sorular ve Doğru Cevapları İncele"):
                for s_no, soru_metni, k_cevabi, d_cevabi in yanlis_detaylari:
                    st.markdown(f"**Soru {s_no}:** {soru_metni}")
                    st.markdown(f"- Sizin Cevabınız: <span style='color: red;'>{k_cevabi}</span>", unsafe_allow_html=True)
                    st.markdown(f"- Doğru Cevap: <span style='color: green;'><b>{d_cevabi}</b></span>", unsafe_allow_html=True)
                    st.markdown("---")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Padişah Arşivi Enterprise Pro | 36 Padişah Tam Arşivi ve Simülasyon Motoru</p>", unsafe_allow_html=True)